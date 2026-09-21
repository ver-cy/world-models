# Audit: enterprise identity-assertion profile 0.1.0 (WM-XCT-036 profile, WM-XCT-011 carriage)

## Verdict: **BLOCK** on the current frozen bytes

The main blocker is F1. The profile claims that "a later correction changes a current view without rewriting an earlier knowledge-time answer." `import_assertion` is the only place that could enforce this, and it accepts caller-chosen `recordedAt` values, both backdated and future-dated. The counterexample is five lines long and uses only the designated import path.

F2 and F3 are smaller, but each would make a published claim inaccurate. The profile could become **ACCEPT WITH LIMITS** after the fixes listed at the end. None of them needs a redesign.

This review is not approval authority. I executed nothing. Every "returns X" below comes from tracing the supplied source by hand, and I mark where a result depends on library behaviour I could not observe.

## Scope

**Seen (frozen text only):** `README.md`, `model-spec.md`, `identity_profile.py`, `identity-profile.schema.json`, `test_identity.py`, `acceptance.py`, `examples/{policy,startup,group,ai-team}.json`, `test-results.json`, `acceptance-results.json`, and the selected parent definitions. From WM-XCT-011 those are `identifier-assignment-record` and `granularity-qualifiers-and-notations`. From WM-XCT-036 they are `als-tax-kind-register`, `als-tax-projection-crosswalk`, `als-tax-property-profile`, `als-tax-strength-inference`, `als-tax-endpoint-scope` and `als-tax-conflict-change`.

**Not seen:**
- Profile files: `crosswalk.json`, `whole-object-coverage.json`, `mastership-and-rights.json`, `field-catalog.json`, `runtime-model.reference.json`, `tool-pins.json`, and any separate `assertion/binding/policy/query.schema.json`.
- Upstream and tooling: `upstream/*/spec.yaml`, `AGENTS.md`, the WM-XCT-040 composer (`composition`, `bootstrap_dimension`), and the skill scripts (`write_record`, `validate_dimension`).
- Other material: the V3 schemas, the Claude and Grok reviews, the other parent findings, and the 108 historical sources.

**Not verified:** every sha256 value. That includes the fixture `policyDigest`, the `previousDigest` chains, the installed validator digest `2ef8…` and the spec pins. I also could not check that the reports were produced from these bytes.

Nothing here verifies the whole parent model, the historical sources, or EM-XCT-01. EM-XCT-01 stays partial.

## Findings

Classes: **BUG** (the code contradicts its own stated contract), **MISMATCH** (the documentation and the implementation diverge), **GAP** (in scope but missing or untested), **OOS** (legitimately out of scope, but the wording must say so).

### Shared prelude for counterexamples (run in the profile directory)

```python
import copy, identity_profile as p
P=p.load('examples/policy.json'); R=p.load('examples/startup.json')
def Q(a): return {k:a['binding'][k] for k in ('scheme','schemeVersion','issuer','scope','value')}
def view(rows,a,**kw):
    d=dict(valid_at='2026-01-01T00:00:00Z',known_at='2026-01-01T00:00:00Z',evaluation_at='2026-09-21T00:00:00Z',reader='urn:synthetic:actor:steward',purpose=P['purpose']);d.update(kw)
    return p.resolve(rows,Q(a),P,**d)
def ev(a,state,rec,eff,sfx):
    last=a['history'][-1];e=copy.deepcopy(last)
    e.update(id=last['id']+sfx,previousDigest=p.digest(last),state=state,recordedAt=rec,effectiveAt=eff);a['history'].append(e);return a
def fork(a,sfx):  # same claim content, fresh assertion/event IDs, relinked chain
    b=copy.deepcopy(a);b['id']+=sfx;prev=None
    for e in b['history']:
        e['id']+=sfx;e['previousDigest']=p.digest(prev) if prev else None;prev=e
    return b
```

### High

**F1 — BUG: knowledge time is caller-asserted at import, so historical answers can be rewritten or time-bombed.**

`import_assertion` has no clock or head-time parameter. It only requires that `recordedAt` increases strictly within one assertion. The README says "the caller supplies the … trusted clock", but the API gives the caller nowhere to supply it.

```python
before=view(R,R[0],known_at='2025-06-01T00:00:00Z')['status']            # 'accepted-in-input'
a=ev(copy.deepcopy(R[0]),'retracted','2025-01-02T00:00:00Z','2025-01-01T00:00:00Z',':late')
R2=p.import_assertion(R,a,P)                                             # accepted "today"
after=view(R2,R[0],known_at='2025-06-01T00:00:00Z')['status']            # 'unknown'  ← past answer rewritten
```

Future-dating works too, and it blocks legitimate corrections until the planted date passes:

```python
f=ev(copy.deepcopy(R[0]),'disputed','2026-12-01T00:00:00Z','2026-12-01T00:00:00Z',':future')
R3=p.import_assertion(R,f,P)                                             # accepted
view(R3,R[0],valid_at='2026-12-02T00:00:00Z',known_at='2026-09-21T00:00:00Z')['status']  # accepted-in-input
view(R3,R[0],valid_at='2026-12-02T00:00:00Z',known_at='2026-12-02T00:00:00Z',evaluation_at='2026-12-02T00:00:00Z')['status']  # contested (self-activates)
p.validate(ev(copy.deepcopy(f),'asserted','2026-09-22T00:00:00Z','2026-09-22T00:00:00Z',':fix'),P)  # Invalid: recorded time must strictly increase
```

The same backdating works through a brand-new assertion ID, for example a p2 claim whose events are recorded at `2025-01-01T00:00:02Z`. The existing test `test_history_preserved_after_append` passes only because its appended event is recorded after the queried `known_at`.

Fix: add `import_assertion(..., now=)`. Require every new event to satisfy `recordedAt ≤ now`. Also require it to be after an `import_head`, meaning the maximum `recordedAt` already present in `existing`, or else have the importer stamp `recordedAt` itself. Add both counterexamples as tests.

**F2 — MISMATCH/GAP: the "native-binding" label overstates what native V3 checks, and the outer fact misrepresents the claim.**

- The acceptance script shows that V3 accepts a nested snapshot with `inferencePermitted: true` (`negative_v3.valid == true`). V3 also accepted the corrupted snapshot in all three scenarios. Nothing on the native write or validate path calls the declared `companionValidator`, so companion validation is advisory unless some unseen integration enforces it. The truncation check is also missing: `import_assertion` is the only prefix check, and it is not wired to V3 supersession. My prediction is that superseding a stored fact with a history-truncated snapshot would pass both V3 and `validate_set`. That depends on `write_record`, which I have not seen.
- The outer fact carries `authority: {'rank': 1}`, which contradicts "no ranking". It also carries `status: 'asserted'` whatever the inner state is: a proposed, disputed or retracted snapshot would still be stored as an asserted fact. Its `validFrom`/`validTo` are copied from the claim window, which invites native temporal consumers to read `value.target` directly and skip `resolve()`.
- `acceptance.py` never asserts `stored == rows`. It only re-validates. `test_round_trip` checks Python `json` against itself, so it is tautological. The claim "full JSON round-trip is lossless" through native storage is therefore untested.

**F3 — BUG: an empty input set bypasses policy validation in both `resolve` and the CLI.**

`validate_set([])` never runs `schema(policy)`. `resolve` then does `reader in policy['readers']`, which is a substring test when `readers` is a string.

```python
bad={'readers':'urn:synthetic:actor:steward','purpose':'x','validFrom':'2025-01-01T00:00:00Z','validTo':None}
p.resolve([],Q(R[0]),bad,valid_at='2026-01-01T00:00:00Z',known_at='2026-01-01T00:00:00Z',
          evaluation_at='2026-09-21T00:00:00Z',reader='steward',purpose='x')   # returns 'unknown' + policyDigest of a non-policy
```

On the CLI, `[]` as the assertions file with `{}` as `--policy` prints `{"valid": true, ...}`. Fix: validate the policy schema unconditionally at the top of `validate_set`, `resolve` and `main`.

### Medium

**F4 — BUG (semantic): a disputed candidate can veto an accepted claim.** A `probable-entity-match` "can never enter asserted state", yet once disputed it forces `contested`.

```python
b=fork(R[0],':cand');b['relation']='probable-entity-match';b['target']['id']='urn:synthetic:subject:p2'
b['history']=b['history'][:1];ev(b,'disputed','2025-02-01T00:00:00Z','2025-02-01T00:00:00Z',':d')
view([R[0],b],R[0])['status']      # 'contested'
```

The same happens for any proposal that is disputed without ever being asserted. The design needs to choose: only a dispute of a previously asserted claim contests, or this behaviour is intended and should be written into the spec.

**F5 — BUG: a proposed negative is reported as a positive `candidate`.**

```python
n=copy.deepcopy(R[0]);n['relation']='not-same-assertion';n['history']=n['history'][:1]
view([n],n)['status']              # 'candidate'
```

Proposed negatives should go into a separate bucket and never produce `candidate` status.

**F6 — BUG: the assignment-ID collision check is global, so one trusted issuer can squat another's ID.** Uniqueness is keyed on bare `assignmentId`, not `(issuer, assignmentId)`, and IDs are not constrained to the issuer's namespace. Which import succeeds depends on arrival order.

```python
s=fork(R[0],':squat');s['binding']['assignmentId']=R[1]['binding']['assignmentId']
p.import_assertion([s],R[1],P)     # Invalid: assignment ID reused for different binding content
```

**F7 — BUG: the namespace gate is a lexical prefix check, so dot segments escape it.** The policy pattern allows hierarchical prefixes.

```python
P2=copy.deepcopy(P);P2['subjectPrefix']='https://example.org/subjects/'
g=copy.deepcopy(R[0]);g['policyDigest']=p.digest(P2);g['target']['id']='https://example.org/subjects/../admin/p1'
p.validate(g,P2)                   # passes; RFC 3986 dot-segment removal yields https://example.org/admin/p1
```

An empty local part (`target.id == subjectPrefix`) is also admitted. Fix: refuse `.`/`..` segments, `%2e` and empty suffixes, or restrict prefixes to URNs.

**F8 — BUG: timestamps accept non-ASCII digits.** `\d` in Python `str` regexes matches Unicode Nd characters, and `strptime`/`int` accept them.

```python
p.stamp('２０２５-01-01T00:00:00Z')  # returns 2025-01-01 UTC instead of raising
u=copy.deepcopy(R[0]);u['validFrom']='２０２５-01-01T00:00:00Z';p.validate(u,P)   # expected to pass (rfc3339-validator also uses Unicode \d)
```

Two assertions can then denote the same instant with different digests, and ECMA-262 JSON Schema validators, where `\d` is ASCII-only, would reject what Python accepts. Fix: use `[0-9]` in `stamp()` and in the schema patterns.

**F9 — GAP: history and evidence are not bound to the claim, so they can be transplanted.** The genesis event has `previousDigest: null`, and the `review-decision` reference is not tied to the target or the assertion.

```python
t=fork(R[0],':t');t['target']['id']='urn:synthetic:subject:p2'
p.validate(t,P)                    # passes, reusing the review of the p1 link to activate a p2 claim
```

Fix: make the genesis `previousDigest` the digest of the fixed claim content, meaning everything except `history`. Authenticity of evidence remains OOS.

**F10 — GAP: the assignment carrier is not bitemporal.** `binding.validTo`, `recordedAt` and `sourceRecord` are all inside the collision digest. When a source later closes an open-ended assignment, the same `assignmentId` cannot carry the new end date, because it is refused as reuse. The importer is also not allowed to mint a new source-issued ID. The fixture `suba-old` hides this: at `recordedAt 2025-01-01` it already "knows" `validTo 2025-06-01`.

In addition, `recordedAt ≥ validFrom` refuses pre-recorded future-effective assignments. Parent 011 q-assignment-time explicitly allows a gap and asks for its reason. Retracting with an `effectiveAt` does close the assertion correctly, but the stale binding content remains. The spec should state this, or the fields should be split into immutable assignment identity and observed assignment state.

**F11 — MISMATCH: read authority is folded into the write pin.** The README describes "the supplied current read policy" as if it were separate. In the implementation, `readers` sits inside the digest-pinned policy. Removing a compromised reader therefore invalidates every assertion (fail-closed means nobody can read), and adding one has the same effect. Revocation is declared as deferred, but the README wording must change. At 2027-01-01 the only continuation is to reissue every assertion under new IDs; the documentation should state this cliff explicitly.

**F12 — MISMATCH: the schema files named in the docs are not the ones the code uses.** The README and spec cite four schemas (`assertion`, `binding`, `policy`, `query` `.schema.json`). The code loads a single `identity-profile.schema.json`, `$defs.binding` is never used (it is a dead duplicate of the inline binding, so it can drift), and acceptance installs only the combined file. The error message says "policy bytes do not match pinned digest", but the digest is taken over canonical JSON, not raw bytes, while the composer digests raw bytes. `sha256sum policy.json` will not reproduce `policyDigest`. The canonicalization needs to be specified.

### Low

- **F13:** a lone surrogate (`reason='\ud800'`, which JSON's `\ud800` escape produces) raises `UnicodeEncodeError` from `digest()`, not `Invalid`. This still fails closed, but it breaks the error contract and the CLI prints a traceback.
- **F14:** `resolve` runs `validate_set` before the reader and purpose check, so an unauthorized caller gets validation diagnostics about the input set.
- **F15:** `FormatChecker` silently skips the `uri` and `date-time` checks if the extras are absent. Assert at import that both checkers are present.
- **F16:** the result omits target kind, `evaluation_at`, reader and purpose, so it is not self-describing. Assertions skipped because no event was yet effective are missing from `excluded`.
- **F17:** policy does not constrain `scheme`, `scope` or `personalDataClass`. A `restricted` record validates under the synthetic policy.
- **F18:** `acceptance.py` verifies composer bytes but imports unpinned skill scripts. It does not check the installed schema's digest (the validator reads the schema beside it). Its reported "pins" are digests of whatever sits in `upstream/`, not checks against expected values. It is also time-bound: `validFrom 2026-09-21`, plan valid until `2026-12-31`, so it cannot reproduce outside that window.

### Semantic/representation gaps (design, not bugs)

- **Account boundary.** The kind gate compares two caller-declared strings. A Git-account ID labelled `kind: person` passes, because policy has no scheme→kind register. The sentence "cannot become Person even by override" is true only for bindings *declared* as accounts. Narrow the wording, or add scheme→kind to the policy.
- **Cross-kind negatives are refused.** "This person reference is NOT the bot account" fails with `different referent kinds`, yet exactly that negative knowledge is useful.
- **Four-eyes review is not enforced.** In every fixture the steward proposes and then asserts their own proposal one second later. "Independently reviewed" is not structural.
- **Fixture naming.** One scheme URI (`person-directory`) is shared by three issuers, and the ai-team bot is a `service-account` in `person-directory`.

## Parent mapping (relation and assignment questions)

| Parent element | Profile | Verdict |
|---|---|---|
| 036 exactly one kind; codes `equivalent-in-context` / `not-same-assertion` / `probable-entity-match` | `relation` enum, one value | ✓ The retained-codes decision is respected; I am not re-arguing it |
| probable-entity-match non-asserted | `asserted` refused | ✓ (see F4 on disputed) |
| inference_permitted (required) | `const false` | ✓ |
| equivalent-in-context needs a named context | Dimension + purpose + kind + interval | ✓ |
| Admissible endpoint types per kind (register column) | identifier-assignment → local subject | **Unverified.** The register column was not supplied. If equivalent-in-context does not admit identifier-token → individual, this is a conformance defect |
| subject_type / object_type (required) | `binding.kind` / `target.kind` | Partial: referent class only, no endpoint-type code |
| endpoint_resolution_state (1..n, required) | absent | **GAP** if the crosswalk claims `als-tax-endpoint-scope` |
| justification_category (required) | evidence kinds, per event only | Partial |
| Change control: prior kind, superseded reference | new ID; no successor/predecessor link | **GAP.** Reconstructing a kind change depends on the old record surviving |
| Register release in force | not pinned | GAP (minor) |
| 011 value / system | `value` / `scheme`(+`schemeVersion`) | ✓, but the key adds `issuer` + `scope`. Under 011, hr:`E7` and git-person-map:`E7` in the shared `person-directory` scheme are one identifier; the profile treats them as unrelated. Make schemes issuer-specific, or document the divergence |
| 011 referent reference (required) | none. `target` is the local subject, not the source's referent; `sourceRecord` is ambiguous | **Mapping unresolved.** Needs `crosswalk.json` |
| 011 effective time / recorded time / validity period | `validFrom` / `recordedAt` / `validTo` | Effective time is merged with validity; not bitemporal (F10); no carrier for the gap reason |
| 011 exclusivity statement | absent | The resolver silently assumes exclusivity, so overlapping occurrences are contested |
| 011 granularity (required, scheme-level) | not carried | Acceptable only if it is resolvable from the scheme definition; unverified |

## Claims audit

- **"48 tests passed":** there are exactly 48 test methods, and my traces agree with the assertions, assuming the fixture digests are correct. However, `test-results.json` has no source or fixture digests, so it cannot be tied to these bytes. Most negative tests only check `assertRaises(Invalid)`, so a test can pass for the wrong reason.
- **Branches with no test at all:**
  - Validation failures: untrusted issuer, `relation outside supplied policy`, source-evidence ref mismatch, `claim predates binding evidence`, `binding observed before assignment began`, `assertion starts outside assignment`, wrong purpose in isolation (the policy tamper hits the digest check first), duplicate assertion ID, duplicate policy actor.
  - Loader and read path: duplicate JSON members, read-purpose denial.
  - Resolver states: disputed→asserted recovery, proposed negative.
  - All of F1–F9.
- **"Three native scenarios passed":** these depend on unseen tools. As evidence, they show that the companion validator is *needed*, not that the model is enforced natively (F2). They also do not show round-trip equality or behaviour under history updates.
- **Input mutation:** I found no mutation in `validate`, `validate_set`, `resolve` or `import_assertion` (outputs are deep copies). `validate` and `validate_set` return the caller's own objects, so callers must not treat those as sanitized copies.
- **Idempotency:** an identical replay is a no-op ✓. A stale earlier version that arrives after an extension is refused rather than ignored. That is acceptable, but at-least-once importers need to know it.

## To reach ACCEPT WITH LIMITS

1. Fix F1 with a trusted `now` and an import head, and test both counterexamples.
2. Fix F3, F5, F7 and F8. For F4, either fix it or specify the behaviour.
3. Bind the genesis event to the claim digest (F9), and key assignment uniqueness by issuer (F6).
4. Outer V3 fact: drop `rank`, use a neutral status or mark it as a snapshot, and assert `stored == rows` in acceptance (F2).
5. Reconcile the schema filenames and specify digest canonicalization (F12). Correct the README wording on the read policy, the account boundary and "native-binding" (F11, F2, and the account-boundary item).
6. Supply `crosswalk.json` so the unresolved rows in the mapping table (referent reference, endpoint resolution state, endpoint admissibility) can be checked.

**Publication wording, if accepted later:** "Additive, versioned 0.1.0 profile associated with WM-XCT-036 (with WM-XCT-011 carriage); reviewable-draft; companion validation mandatory and not enforced by native V3; recorded times caller-asserted unless the importer supplies a trusted clock; this bounded review covers only the listed files and does not verify the parent models, the 108 historical sources, or EM-XCT-01."
