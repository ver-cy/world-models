# EM-XCT-01 second frozen candidate: review verdict

**Verdict: BLOCK (narrow).**

Most of the round-1 BLOCK items appear closed in the supplied bytes. These are now in place:
- receipt-time live import against the global head;
- a genesis digest that commits to the claim;
- unconditional policy validation;
- the scheme→kind register and disjoint kind namespaces;
- the restricted target URI profile;
- issuer-qualified assignment identity;
- separate negative proposals;
- endpoint-resolution gating;
- a more honest native V3 claim.

Two new defects break stated guarantees. Both can be triggered by the lowest-privilege actor (`importer`, which may only propose). Each fix is small, and I expect ACCEPT WITH LIMITS once they are fixed and tested. This is a reading of the supplied bytes only. I did not run anything and did not check upstream sources.

## Blockers

### B1: A lone surrogate is accepted at import, then permanently breaks reads and retraction

`encode()` does convert surrogate failures to `Invalid`. However, the admission path never encodes the whole assertion:
- `validate()` digests the policy, the claim (without history) and every event except the last.
- `validate_set()` digests only `binding`.

So `reason` or `evidence[].description` in the newest event is never encoded at admission. `resolve()` later computes `inputDigest` over all assertions and raises `Invalid`. Any later append computes `digest(previous)` and also raises.

```python
a=self.other();a['history']=a['history'][:1]
a['history'][0].update(recordedAt='2026-09-21T00:00:00Z',actor='urn:synthetic:actor:importer',reason='x\ud800')
rows=p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')  # accepted, 4 rows
self.query(rows)                     # Invalid for EVERY query key (inputDigest covers the whole set)
self.append(copy.deepcopy(a),'retracted','2026-09-22T00:00:00Z','2026-09-21T00:00:00Z')  # Invalid: cannot retract
```

The same input arrives from JSON as `"x\ud800"`, because `json.loads` accepts the escape. Import forbids truncation, so the ledger cannot recover.

**Fix:** call `encode(assertion)` in `validate()`, or `encode(assertions)` in `validate_set()`, before accepting. Add a test that puts the surrogate in the last event's `reason` and in its `description`.

### B2: A proposal permanently squats an issuer-qualified assignment ID

`validate_set()` requires identical binding content for every assertion sharing `(issuer, assignmentId)`. This applies to all assertions, including those that are only proposed or already retracted. An importer can therefore pre-empt a source assignment with arbitrary content. The genuine observation can then never be recorded. The README forbids inventing a new assignment ID to work around this, so no path remains.

```python
s=self.other();s['history']=s['history'][:1]
s['binding'].update(assignmentId='urn:synthetic:assignment:hr-9',value='bogus')
s['history'][0].update(recordedAt='2026-09-21T00:00:00Z',actor='urn:synthetic:actor:importer');self.seal(s)
rows=p.import_assertion(self.rows,s,self.policy,now='2026-09-21T00:00:00Z')        # accepted
# Steward retracts s at now=2026-09-22 (accepted). Then the genuine claim g:
# same issuer and assignmentId, value 'E9', new assertion/event IDs, sealed, genesis recordedAt=2026-09-23
p.import_assertion(rows_after_retraction,g,self.policy,now='2026-09-23T00:00:00Z')  # Invalid: assignment ID reused
```

**Fix, pick one:**
- Enforce binding-content consistency only among assertions that have reached `asserted`, and report other conflicts in the query result.
- Release the ID on retraction.
- Bind issuers to the actors allowed to introduce their assignments.

Whichever you choose, add the squat scenario as a test.

## Required fix or explicit declaration

### L1: A backdated dispute vetoes a claim that was not yet active at that valid time

This contradicts model-spec invariant 10. `resolve()` uses the full record-order history (`a['history'][:index(e)]`) to decide whether a dispute follows an assertion. It should use the history already filtered by valid time.

```python
b=self.other()
b['history'][1].update(effectiveAt='2025-06-01T00:00:00Z',recordedAt='2025-06-02T00:00:00Z');self.seal(b)
self.append(b,'disputed','2025-07-01T00:00:00Z','2025-02-01T00:00:00Z')
self.query([self.a,b],valid_at='2025-03-01T00:00:00Z',known_at='2025-08-01T00:00:00Z')['status']  # 'contested'
```

At 2025-03-01, `b` had never been effectively asserted. The same input without the later-effective activation returns `accepted-in-input`, with `b` listed in `candidateDisputes`.

**Fix:** set `prior=history[:-1]`, using the filtered list.

### L2: `known_at` can lie in the future, so "stable past answers" is not enforced

`resolve()` only requires `known_at ≤ evaluation_at`, and `evaluation_at` only needs to fall inside policy validity. Nothing ties either value to a trusted current time.

```python
self.query(known_at='2026-12-01T00:00:00Z',evaluation_at='2026-12-01T00:00:00Z')['status']  # accepted-in-input
# Later, a correctly timed import: retraction recorded at now=2026-10-01, effective 2025-02-01.
# The same query now returns 'unknown'. The first report claimed a knowledge state that did not yet exist.
```

**Fix:** either take a trusted `now` and require `known_at ≤ now`, or declare that `evaluation_at` must be the trusted clock. The latter requirement is currently stated only against backdating a read.

## Remaining limits (acceptable if disclosed)

1. **Unpinned runtime schema.** `schema()` re-reads `identity-profile.schema.json` from beside the module on every call, with no digest check at runtime. Integrity is proven only at install time in the harness. The inline `binding` schema is also duplicated in `$defs.binding` rather than referenced with `$ref`, which risks drift. The four "generated companion views" are not in this bundle.
2. **Loader errors are not converted.** `load()` lets `JSONDecodeError`, `UnicodeDecodeError`, BOM input and `RecursionError` escape as non-`Invalid` exceptions. This still fails closed, but callers that catch only `Invalid` will crash.
3. **Weak source-referent rules.** `sourceReferentRef` is not namespace-restricted, so it may point into the local subject namespace and create a local-to-local link. Distinctness from the target is exact-string, so `URN:synthetic:…` and `urn:synthetic:…` pass as different, although URN scheme and NID are case-insensitive.
4. **Wide HTTPS prefixes.** A `subjectPrefix` such as `https://id.example.com:` is valid and admits any port, i.e. a different origin. The policy author controls this, but the profile should reject authority-terminal prefixes.
5. **Unenforced model-spec wording.** Model-spec describes the assertion `id` as "issuer-qualified", but nothing enforces that.
6. **Unqualified dispute rule.** A disputed, previously asserted *negative* with no positive yields `contested`. This is probably intended, but it should be stated.
7. **Acceptance harness gaps:**
   - Pins hash `.py` bytes, but Python may execute stale or tampered `__pycache__` bytecode whose recorded source mtime and size still match.
   - Unpinned modules on the inserted `sys.path` entries can shadow imports.
   - Pins are hashed before import (TOCTOU).
   - The negative scenario accepts any `Invalid` reason.
   - The restored victim file is not re-validated.

   These are acceptable under the "explicitly trusted local tools" premise, but "byte-pinned" should say "pinned source bytes".

## Test observations (from reading)

- The supplied file contains 78 `test_` methods, which matches the report count.
- `test_endpoint_change_refused` fails on the genesis predecessor mismatch, never reaching the `claim-bearing content changed` branch. That branch is only reachable if the incoming claim is re-sealed, and no test does that. Add a re-sealed variant with a regex on the message.
- Missing tests: B1, B2, L1, L2.

## Deliberate scoping accepted as stated

I accept these as declared semantics, not bugs:
- the overlap and duplicate-claim semantics;
- backdated effective supersession;
- single-transition-per-second live import;
- policy-expiry lockout;
- no four-eyes or attestation;
- V3 outer rank `0` plus a mandatory, explicitly invoked companion validator;
- the crosswalk's narrower/overlap-only claim.

EM-XCT-01 correctly remains **partial**, and the parent 011/036 holds are unchanged. This review grants no publication authority.
