# Frozen audit: EM-XCT-01 enterprise identity profile

**Verdict: ACCEPT WITH LIMITS**

This is not approval authority. It is a review of the frozen evaluator text plus the accompanying design sentences. Publication remains an additive versioned profile of WM-XCT-036 with WM-XCT-011 carriage. It does not close WM-XCT-036’s historical Claude-only waiver or the 108-source hold, and it does not make EM-XCT-01 a complete enterprise identity system.

---

## Exact scope, and what was not seen

**Seen (frozen in this turn):** the reference evaluator module; the design reconciliation sentences; the parent-definition claims for `identifier-assignment-record` and `als-tax-kind-register` (`equivalent-in-context`, `probable-entity-match`, `not-same-assertion`); the schema *summary* (closed assertion and nested objects, URI-qualified IDs, UTC-second dates, fixed version, relation enum, policy actors as actor-plus-states, unique issuer/reader lists, required claim fields and event history); the trust boundary (policy, clock, and input completeness are caller-trusted; this checker does not authenticate users or evidence).

**Not seen:** `identity-profile.schema.json` and its `$defs`; fixtures; the 48 tests; the three native new-Dimension scenarios; the native harness; Vercy V3 composition output; SHA pins; WM-XCT-011 / 036 full specs; any live Dimension. Those artifacts are **unreviewed**. A local pass count is not evidence in this audit.

The evaluator is a declared-constraint checker over a caller-supplied closed world. That matches its own banner. It is not an identity authority.

---

## What the frozen design actually implements

Aligned with the reconciliation note:

- Parent relation codes only, gated by `policy['relations']`. `probable-entity-match` cannot enter `asserted`. First lifecycle state must be `proposed`.
- No `resolution_status` on the assertion. `resolve()` is a pure query and labels success `accepted-in-input` with `scope: supplied-input-only`, `grantsAccess: False`, `globalEquality: False`.
- Two positive targets, a positive/negative clash on the same target, or any `disputed` row on the query key → `contested`. No ranking.
- Policy is digest-pinned (`assertion['policyDigest']==digest(policy)`). Any byte change fails closed. Resolve also requires `evaluation_at` inside the supplied policy window.
- `binding.kind` must equal `target.kind`. Target id must use `policy['subjectPrefix']`. Binding issuer must be on `policy['issuers']`.
- Import is pure and append-only. Claim-bearing fields cannot change under the same assertion id. Exact replay is idempotent.
- No endpoint writes, no matcher, no clock of record inside the module.

That is a coherent narrower profile. It is also **partial** versus the original owner goal (HR + Git + issue-tracker IDs denoting one Person). The kind-equality rule plus “fixtures use synthetic person-reference exports, not Git/tracker account IDs” means a UserAccount/ServiceAccount identifier **cannot** be asserted onto a Person target. That is an explicit scope cut, not a silent implementation miss — but it must stay on the publication label.

---

## Defects

Bugs are violations of stated invariants or of the evaluator’s own rules. Out-of-scope items are capabilities the banner already disclaims. Limits are incomplete but internally consistent behaviour.

### BUG-1 — “Cannot become Person even by override” is not enforced

The only kind rule is `b['kind']==target['kind']`. Both fields are caller-supplied. Override: set both to `Person`.

```json
"binding": {
  "scheme": "https://git.example/ns",
  "schemeVersion": "1",
  "issuer": "https://id.example/issuers/git",
  "scope": "acme",
  "value": "u-42",
  "kind": "Person",
  "assignmentId": "asg-git-1",
  "sourceRecord": "https://git.example/users/u-42",
  "validFrom": "2026-01-01T00:00:00Z",
  "validTo": null,
  "recordedAt": "2026-01-02T00:00:00Z"
},
"target": { "kind": "Person", "id": "https://dim.example/acme/person/p-7" },
"relation": "equivalent-in-context"
```

If `subjectPrefix` is `https://dim.example/acme/person/` and the issuer is listed, this validates. The evaluator never consults a scheme→kind register. **“Even by override” is false** unless the unseen schema hard-codes per-scheme kinds (not visible here). Treat as a residual gate, not a type safety proof.

### BUG-2 — Namespace gate is raw `startswith`

```python
target['id'].startswith(policy['subjectPrefix'])
```

```text
subjectPrefix = "https://dim.example/acme/person"
target.id     = "https://dim.example/acme/personality/p-9"
```

or

```text
subjectPrefix = "https://dim.example/acme/person/"
target.id     = "https://dim.example/acme/person/../other-dim/p-9"
```

Both pass. This is not RFC 3986 path safety and not a closed local-namespace test. Executable once the schema allows those URI strings (the summary says URI-qualified IDs; it does not say segment-normalized IDs).

### BUG-3 — Assignment collision on the same qualified key is not rejected

`validate_set` only binds `assignmentId → digest(binding)`. Different `assignmentId`s may share `(scheme, schemeVersion, issuer, scope, value)` with **overlapping** `validFrom/validTo` and different targets. 011 assignment records are supposed to make that a collision incident, not two quiet rows.

```text
A1 assignmentId=asg-1 value=10021 valid 2019-01-01 .. 2023-01-01 target=person/alice
A2 assignmentId=asg-2 value=10021 valid 2021-01-01 .. null      target=person/bob
same scheme/issuer/scope/version
```

`validate_set` accepts both. `resolve` at `2022-06-01T00:00:00Z` becomes `contested` (two positives). Detection exists only as a query symptom, not as an assignment invariant. Reuse after a closed window is indistinguishable from overlapping collision at write time.

`schemeVersion` is part of `key()`. Bumping version on the same issuer/scope/value splits the query key and can hide a collision.

### BUG-4 — Sole asserted `not-same-assertion` reports `unknown`

```text
positives empty, negative = {person/bob}, disputed empty, candidates empty
contested = bool(disputed or len(positives)>1 or set(positives)&set(negative))
status    = unknown
```

A reviewed, activated denial is not contested and not a first-class negative status. It is buried in `opposing`. Any caller that branches only on `status` treats an explicit not-same as absence. That is the wrong default for the negative case the profile claims to own.

Mixed `equivalent-in-context` to Alice plus `not-same-assertion` to Bob is `accepted-in-input` (different targets, empty intersection). That can be right, but it should be documented; it is not an authority conflict under the current predicate.

### BUG-5 — Event `effectiveAt` is not capped by assertion or assignment `validTo`

```python
stamp(assertion['validFrom']) <= stamp(event['effectiveAt']) <= stamp(event['recordedAt'])
```

No upper bound against `assertion['validTo']` or `binding['validTo']`.

```text
assertion.validFrom=2020-01-01T00:00:00Z  validTo=2021-01-01T00:00:00Z
event.retracted    effectiveAt=2025-01-01T00:00:00Z  recordedAt=2025-01-02T00:00:00Z
```

`validate()` accepts the retraction. `resolve` then ignores that event whenever `valid_at` is inside 2020, because the assertion row is `outside-validity`. The history contains an effect that cannot apply inside the claim’s own window. Either reject at write time or define events as having their own interval.

Related observability gap: if `valid_at` is inside the assertion window but every event has `effectiveAt > valid_at`, the row is skipped with **no** `excluded` reason. Status can be `unknown` with an empty explanation.

### BUG-6 — Backdated later event always wins, even when its `effectiveAt` precedes a still-in-force activation

`resolve` takes the last history element with `recordedAt <= known_at` and `effectiveAt <= valid_at`.

```text
E1 asserted  effectiveAt=2021-06-01  recordedAt=2021-06-02
E2 retracted effectiveAt=2020-01-01  recordedAt=2021-07-01
query valid_at=2021-06-15  known_at=2021-08-01
```

Both events qualify; E2 wins; status path is `retracted` → `excluded`. That is defensible as “correction from 2020-01-01 learned in July”, but it is not “the event whose effective interval covers `valid_at`”. There is no event interval, so a backdated retraction erases a later activation for all earlier valid times once it is known. If tests treat E1 as still covering June 2021 after E2 is recorded, those tests disagree with this function.

### BUG-7 — Schema / `KeyError` contract is unverified

`schema()` is the only required-field gate. Missing keys then raise `KeyError`, not `Invalid`. Extra properties, open `$defs`, or a root document that is not actually `additionalProperties: false` are **schema-bypass risks**. The companion is `Draft202012Validator` over an unseen file. Nested V3 success, if anyone claims it, is a different validator and was not supplied. Do not equate the two.

### BUG-8 — Duplicate live claims with different assertion ids are not idempotent

Same binding bytes, same target, same relation, two ids → `validate_set` accepts. `resolve` stays `accepted-in-input` with two `supporting` ids. Replay idempotency holds only for the same `assertion['id']`. Cross-id duplicates are silent.

---

## Out of scope (not bugs in this checker)

| Item | Why it is not a defect here |
|---|---|
| Authentication of actors/readers | Banner + no verifier |
| Evidence truth (`source-record` / `review-decision` refs) | Only kind-set and ref equality to `binding.sourceRecord` on `asserted` |
| Scheme-specific canonicalization of `value` | `key()` is raw; `Alice` and `alice` are different identifiers |
| Read/write enforcement beyond policy lists | `readers` / `actors` / `issuers` are caller-trusted arrays |
| Global completeness of the assertion set | `scope: supplied-input-only` |
| Retention, tombstones after `retracted` | `retracted` is terminal; no tombstone state in the transition table |
| Endpoint mutation, matching engines, `owl:sameAs`, access grants | Absent by construction |
| Policy rotation while keeping one working set | Fail-closed is intended; mixed-digest batches cannot `resolve` |
| Post-expiry evaluation at wall-clock now | `evaluation_at` must lie inside `policy.validFrom/validTo`; caller must backdate |
| Linking Git/Jira *account* ids to Person | Explicit fixture/scope cut |
| `supersedes` pointer to a replacement id | Replacement requires a new assertion id; no lineage field |
| 011 reuse/quarantine policy, privacy classification, credential-prohibition | Not in this evaluator |

`main()` only runs `validate_set`. `resolve` and `import_assertion` are library paths. That is an interface limit, not a semantic bug.

---

## Contested / candidate / policy checks that do hold

Use these as the positive control when writing tests; they are visible in the text.

- `probable-entity-match` + event `asserted` → `Invalid: candidate relation cannot activate`.
- First event not `proposed` → `invalid lifecycle transition`.
- `retracted` then any later state → rejected (`retracted: set()`).
- Append-only import with edited `relation`, `target`, window, or binding → `claim-bearing content changed`.
- Shortened or rewritten history → `history is not an append-only extension`.
- Policy byte change vs pinned digest → fail closed.
- Reader not in `policy['readers']` or `purpose != policy['purpose']` → deny read.
- `known_at > evaluation_at` → reject.
- Two positives to different targets on one query key → `contested`.
- Any `disputed` event selected on that key → `contested`, even if another row is clean.

---

## Claims that must not travel with this review

**“48 tests and three native new-Dimension scenarios passed locally.”** Not seen. Several cases above are either untested or tested against a different bitemporal rule. Do not repeat the pass count as an audited fact.

**“Companion validation implies V3 / Dimension readiness.”** The companion here is JSON Schema Draft 2020-12 plus this module. WM-XCT-040 still requires a separate nested-domain validator; V3 passing is not that validator. Unseen either way.

**“This review verifies WM-XCT-036 / 108 sources / parent completeness.”** It does not. Parent kind glosses were supplied as verified sentences for three codes only. Assignment-record ownership of assigner, evidence, valid time and recorded time is reflected only partly: assigner is not a field this evaluator reads; evidence is event-scoped and only demanded on `asserted`.

**“accepted-in-input means the identifier is the Person.”** It means: inside this caller-supplied list, under this pinned policy, at these two times, one positive target remains. It is not global equality and not an access decision.

---

## Publication limits

Publish, if at all, as an **additive versioned profile** attached to WM-XCT-036, mixing WM-XCT-011 carriage by reference. Keep the three parent relation codes. Do not add `source-scoped-denotation` in this profile. Label the artifact:

- semantic-only constraint checker;
- caller-trusted policy, clock, and evidence;
- `accepted-in-input` only;
- Person vs account linkage out of band except synthetic person-reference exports;
- historical 036/011 holds unchanged.

Do not ship BUG-1..BUG-4 without either a schema-level kind/namespace register and an assignment-collision rule, or an explicit “known holes” section that those tests must name.

---

## Principal objections

1. Kind equality is not a kind system. The override the design forbids is a two-character edit.
2. Collision is a resolve by-product, not an assignment invariant. That is the opposite of 011’s assignment-record story.
3. Negative assertions do not have a status. `unknown` will be misread as “no information” rather than “explicit denial in input”.
4. Bitemporal events are a stack of instants, not intervals. Backdated retractions and post-window effect times are accepted then interpreted by a last-match rule that is easy to test wrong.
5. Unseen schema, tests, and harness mean this pass cannot certify the 48-test claim or nested-Dimension scenarios. Limits stay limits until those bytes are in the same frozen bundle as the evaluator.