# EM-XCT-05 review decision

**ACCEPT WITH LIMITS**

Declared scope only: frozen metadata-only research candidate `0.0.0-prototype.1`. This is not authorization to publish, install, ship as a Vercy release, claim native V3 integration, or treat the Codex suite as an external security/privacy audit. The Bundle/Layer/Finding/Question/Artifact/Action tree, five facets, and mastership contracts are absent by README admission.

Team consensus (identity/time/digest, inspect applicability, import/supersession/schema/custody) found no silent grant path and no digest-forge or mutate-on-failed-import path **if** the documented trusted-host duties actually hold. Several claims are incomplete or awkwardly worded. Several controls are explicitly deferred. Those are limits, not invented product features.

---

## Files actually read

All bytes came from the supplied bundle. No execution, no web, no filesystem beyond the paste. No truncation observed in these eight files:

| File | Declared SHA-256 | Truncation |
|---|---|---|
| `README.md` | `b87a7ac51d2b3ef3…28edb677` | none |
| `disclosure.py` | `2300e7d8e1abcd14…09e0dcc5` | none |
| `disclosure.schema.json` | `2cd0c891c3b5f486…89c43a3f` | none |
| `test_disclosure.py` | `efffa7ad910c09c8…9d8a87d9` | none |
| `test-results.json` | `4112bb21cf5f81aa…21d9ec22` | none |
| `examples/startup.json` | `57f12b7785a5f1c1…e5d957cf` | none |
| `examples/matrix.json` | `f28b47c3adaadbf3…50b19ad42` | none |
| `examples/ai.json` | `6665dd7d593130cc…9b954da7d` | none |

`test-results.json` reports `status=passed`, `testsRun=51`, `failures=0`, `errors=0`, and `codeSha256=2300e7d8…0dcc5`, which matches the declared `disclosure.py` digest. That is Codex evidence only. This review did not run the tests.

---

## What the prototype actually is

Two immutable record types (`disclosure.schema.json` `$defs.proposal` / `$defs.review`), local seal/validate, in-memory merge, and an internal applicability function.

| Function | What it does | What it does not do |
|---|---|---|
| `canonical` / `load` / `hash_body` / `seal` / `validate` | Restricted JSON bounds, digest over record minus top-level `digest`, schema + local uniqueness | Approve content, parse hostile text except via `load()`, resolve pins |
| `authorize` | Require host dict `dimension` match and `inspect is True` | Authenticate, sign, bind a caller |
| `inspect` | Compare sealed proposal + supplied reviews to a host snapshot at a host-supplied `now` | Serve data, retain/destroy, hide existence, apply `supersedes` |
| `import_records` | Transactional immutable merge in memory | Persist, CAS, enforce reviewer authority at write, resolve references |

That matches the README’s own non-goals more closely than a typical “research prototype” write-up. The remaining work is to keep those non-goals from being read as features.

---

## Defects vs trusted-host duties

Do not invent controls the bytes refuse to own. Separate the two.

### Explicit trusted-host duties (not defects)

1. **Capability is not a token.** `authorize(capability, dimension)` only checks a caller-supplied dict. Host authenticates and authorizes outside this file. Forgery of `{dimension, inspect: True, record: True}` is in-scope for any process that can call the functions.
2. **Snapshot is an attestation, not a proof.** `inspect` requires exact key set `{dimension, context, members, proposalAuthors, reviewers, authority, activeReviews, withdrawnReviews, separateReviewer}` and then exact Python equality of `context` and `members` against the proposal body. Echoing the caller’s proposal into `hostSnapshot` makes the happy path succeed. README already says that defeats the integration contract. Fixtures in `examples/*.json` do exactly that echo.
3. **Active vs withdrawn vs superseded is host classification.** Completeness is `pins(supplied) == pins(snapshot['activeReviews'])` only. A rejecting review listed only under `withdrawnReviews` stays dark. `body.supersedes` is never read by `inspect` or `import_records`.
4. **`now` is a host argument**, not a clock pin. A confused host can reopen an expired window or flip `future-capture`.
5. **Pins do not resolve.** Source, schema, shape, classification, audience, purpose, environment, `priorReleases`, `custodyContext`, authority, method, evidence are opaque `{id, revision, digest}` triples. The library does not fetch, type-check against a compiler, rank schemes, or compute disposition.
6. **`inspect` output is internal.** Distinct statuses and `ignored[]` (`withdrawn` / `authority` / `self-review` / `outside-window`) are existence and reason oracles if forwarded. README forbids verbatim forwarding and admits there is no uniform HTTP refusal or timing/existence protection.
7. **Write path does not enforce review authority.** Unauthoritative reviews may be retained as evidence. Applicability is a later snapshot question.
8. **Scalar-leaf and closed-schema claims are host attestations.** Field names are identifier-shaped; kinds are a closed scalar enum. That is not a source-schema proof.

### Defects / incomplete claims inside the supplied bytes

These are real, but none of them produce `applicable-review` by themselves under a non-echoed snapshot.

1. **Misleading custody sentence.** README: “Matching it proves no permission to retain, serve or destroy.” Matching an opaque pin proves neither permission nor prohibition. Code never computes hold/schedule/destroy. Rewrite to the negative claim the rest of the paragraph already makes.
2. **Digest field list omits `format`.** `hash_body` hashes every top-level key except `digest`, so `format` is included. README lists type/version/Dimension/identity/revision/body only. `format` is a schema const, so this is a documentation miss, not a semantic hole.
3. **`supersedes` is a live field with no graph.** `validate` only rejects `supersedes == pin(self)`. Cycles, dangling pins, proposal-typed targets, and “same id/rev different digest” are accepted. `inspect` ignores the field. README correctly defers this and says implement or remove before release. Leaving it in a published model without that work would be a **REVISE** later, not a pass now.
4. **`notServingAuthorization` is missing on fail-closed statuses.** Set only on `applicable-review` / `rejected` / `inconclusive`. Absent on `stale`, `insufficient-context`, `conflict`. Safe if callers key on `status == 'applicable-review'`. Unsafe if a sloppy integrator treats “flag missing” as a serve grant.
5. **Actor catalog is weaker than record identity.** Records use `^[A-Za-z][A-Za-z0-9+.-]*:[^\s]+$`. Snapshot `proposalAuthors` / `reviewers` only require `':' in v`. Harm is limited because applicability still exact-matches a schema-valid author/reviewer string. `test_actor_catalog_cannot_be_substring` is a real guard against `x in 'xy'`.
6. **Write capability implies inspect.** `import_records` calls `authorize()` (`inspect is True`) then also requires `record is True`. Undocumented coupling. Stricter, not weaker.
7. **Product-flavored format id.** `format: "vercy-disclosure-research"` plus README “reserves no public runtime ID.” Low risk while version stays `0.0.0-prototype.1`; colliding later with a published format would be a migration defect.
8. **Leap-second split between layers.** Schema `$defs.time` is `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$` and therefore admits `23:59:60`. `instant()` uses `datetime.strptime` and should reject it. No dedicated test.
9. **`member.key` charset is loose** (any string 1–128) while `field.name` is tight. Not a serving bug.
10. **`kind: "number"` is representable** while `load`/`canonical` forbid floats. Safe only because this prototype stores no source values. Easy to misread as “numeric payloads are in scope.”

---

## Identity, time, digest

Anchors: `disclosure.py:canonical`, `load`, `hash_body`, `seal`, `validate`, `instant`, `pin`; `disclosure.schema.json` `$defs.pin` / `$defs.time`.

- Digest is `sha256:` + SHA-256 of the restricted encoding with **only the top-level** `digest` removed. Nested pin digests are part of the hashed body. Correct.
- Encoding is local restricted JSON: UTF-8, sorted keys, compact separators, no floats/non-finites, no Unicode normalization, list order significant. Not RFC 8785/JCS. README is accurate here.
- `load` is the hostile-text parser (duplicate keys, invalid UTF-8, non-integer numbers). `seal`/`validate`/`inspect`/`import_records` take Python dicts. Do not describe `validate` as a wire parser.
- Integers must sit in `±(2^53-1)`. Bool is checked with `type(x) is bool`, so `True` is not an integer. Good.
- Timestamps are whole UTC seconds with `Z`. `instant` round-trips through `strftime`, so structural regex acceptance is not calendar acceptance (`test_invalid_calendar_date`). No offsets, no fractions, no leap-second support in the time function.
- Review seal: `reviewedAt <= validFrom < validTo`. Inspect window: `[validFrom, validTo)` (`test_start_is_inclusive`, `test_expiry_is_exclusive`). Review before proposal `capturedAt` is `Invalid`, not a soft ignore.
- Assessment time cannot predate capture (`stale` / `future-capture`). Equal `reviewedAt == capturedAt` is allowed.
- `pin()` is `id`/`revision`/`digest` only. Call sites pin after `validate`.

Adversarial witnesses:

- **W-time.** Host passes `now` inside an expired window → `applicable-review` if the rest matches. Host duty.
- **W-nfc.** NFC vs NFD strings are different digests. Documented. Catalogs must store exact pins.
- **W-seal.** `seal()` needs no capability. Integrity is not approval. Intended.

---

## Caller authority, incomplete sets, conflicts

Anchors: `disclosure.py:authorize`, `inspect`.

Capability gate runs before `validate(proposal)`. Cross-dimension capability → `Unauthorized`. Missing capability with a garbage proposal → `Unauthorized` (`test_missing_capability_before_record_diagnostics`). Extra capability keys are ignored.

Review-set rule is exact set equality of canonical pin bytes. Extra supplied review, missing catalogued review, or hidden `activeReviews` pin → `insufficient-context` / `review-set-incomplete`. Duplicate `(id, revision)` in the list → `Invalid` (`test_duplicate_reviews_not_votes`). Caller cannot inject a vote or drop an active reject without failing completeness.

Filter order on each supplied review:

1. wrong proposal pin → `Invalid`
2. withdrawn → ignore
3. reviewer not in catalog or authority pin ≠ snapshot authority → ignore
4. `separateReviewer` and reviewer == author → ignore
5. `reviewedAt < capturedAt` → `Invalid`
6. `now` outside `[validFrom, validTo)` → ignore

Then: no remaining verdicts → `insufficient-context` / `no-applicable-review`; disagreeing verdicts → `conflict`; `cleared` → `applicable-review` with `notServingAuthorization=True`; `rejected` / `inconclusive` returned as themselves with the same flag.

Self-review is a snapshot boolean, not a NIST profile. `startup` allows it; `matrix` / `ai` do not. Documented governance choice.

Adversarial witnesses:

- **W-echo.** Host copies proposal `context`/`members` into the snapshot without independently resolving pins. Happy path succeeds. Fixtures teach this pattern.
- **W-withdraw-dark.** Host omits a reject from `activeReviews` and optionally lists it only as withdrawn. Completeness does not require withdrawn objects. Host duty.
- **W-forward.** Recipient sees `ignored: ['authority','outside-window']` and learns catalog/window facts. Host duty not to forward.
- **W-flag.** Integrator treats any inspect dict lacking `notServingAuthorization` as a serve grant. Optional hygiene: set the flag on every return.
- **W-self.** `separateReviewer=False` plus author in `reviewers` yields a self-clearance. Allowed by the startup profile; not a stealth path.

---

## Schema / path / source / classification

Anchors: `$defs.field`, `$defs.member`, `validate` duplicate-key / duplicate-field / `conflicting binding pin`; tests `test_no_nested_or_wildcard_fields`, `test_no_object_or_array_kind`, `test_no_payload_field`, `test_missing_classification_not_public`, `test_two_classification_schemes_representable`, `test_same_binding_revision_conflict`.

- Field names reject dots, slashes, wildcards, indexes.
- Kinds reject `object` / `array`.
- `additionalProperties: false` plus `test_no_payload_field` keep source values out of the record.
- Reordered members change the digest; an old review then fails `review points to another proposal` (`test_reordered_members_changes_pin`). Fail-closed.
- Classification bindings: 1–8 pins, `uniqueItems` on the full pin, plus a tighter `(id, revision)` conflict check so the same scheme revision cannot appear with two digests.
- Bindings are typeless. A source pin can be stuffed into `classificationBindings`. No scheme fetch, no rank, no “public by omission” (omission is illegal).
- No check that `field.name` is a leaf of the pinned schema/shape. Host attestation.

Adversarial witnesses:

- **W-shape.** Field `name` declared `string` while the real source leaf is an object. Prototype cannot know.
- **W-label.** `kind: "number"` looks like values are in play. They are not.

---

## Idempotency, supersession, migration, retention

Anchors: `disclosure.py:import_records`; `validate` self-supersession; proposal `priorReleases` / `custodyContext`; version const `0.0.0-prototype.1`.

`import_records`:

- Same `(type, id, revision, digest)` incoming is idempotent.
- Same revision, different digest → `Invalid('immutable revision conflict')`; `existing` is not mutated (`test_immutable_revision_conflict_transactional`).
- New revision appends; history is preserved (`test_correction_preserves_history`).
- Same `id` cannot change `type`.
- Combined length cap 128 is a prototype bound, not a DoS guarantee.
- Does not require `review.body.proposal` to exist in the merged set. Dangling reviews import.

`supersedes`:

- Evidence link only.
- Host must move superseded reviews out of `activeReviews` (typically into `withdrawnReviews`) or `inspect` will `conflict` on disagreeing live verdicts rather than “last pin wins.”
- Future publication must validate existence, type, direction, and acyclicity **or delete the field**.

Migration:

- Version is a schema const. `test_unsupported_version` rejects `0.0.0-prototype.2`. There is no migration map. Acceptable only while this remains a frozen candidate.

Retention / privacy:

- No delete, no disposition state, no recipient-omniscience check.
- `priorReleases` and `custodyContext` participate only in context equality. Drift → `stale` (`test_context_drift` walks every context key).
- Human clearance plus exact pins does not prove non-identifiability and does not erase earlier releases. README is correct on that negative claim; the custody “proves no permission” sentence is the one that needs a rewrite.

Adversarial witnesses:

- **W-dangle.** Import a review whose proposal was never in the set. Merge succeeds. Later `inspect` is either `Invalid` (pin mismatch) or applies if the host also presents that target. Completeness remains a host problem.
- **W-cycle.** A↔B `supersedes` seals and imports. `inspect` ignores both links.
- **W-custody-echo.** Host copies caller `custodyContext` without opening the instruction object (holds/schedules). Applicability can still return `applicable-review`. That is the echo-contract failure again.

---

## Tests vs README

README’s topic list is mostly real in `test_disclosure.py`: three profiles, context/source/schema/shape/classification drift, membership/field/order changes, withdrawn authority, segregation, half-open window, conflict, incomplete set, import idempotency/conflict/history, type freeze, capability gates, hostile JSON, nested-field reject, round-trip.

Over-claims to keep bounded:

- “known prior-release/custody-context changes” is generic pin inequality, not a custody engine.
- “51 tests” are Codex-reported prototype checks. `test-results.json` already disclaims external audit, native integration, and privacy/security conformance.
- Untested edges that matter before promotion: `23:59:60`, `1e2`, surrogates / `$defs.time` vs `instant`, integer `2^53`, self-supersession, supersede cycles/dangling, inspect ignores `supersedes`, `activeReviews ∩ withdrawnReviews`, import cross-dimension and 128-bound, `inspect` with `record: False`, NFC vs NFD digest split, snapshot extra keys.

Example fixtures: per-profile `review.body.proposal.digest` equals `proposal.digest`, and `hostSnapshot.activeReviews` matches the review pin. Synthetic pin helper hashes `name+rev`, not a real object. `matrix` / `ai` still reuse `project-schema` / `name-only-shape` / `name-classification` under different field names. Harmless as syntax fixtures; harmful if copied as binding evidence.

---

## Minimal fixes

Required before any promotion out of this scope (not required to hold the present prototype verdict):

1. Implement cross-record `supersedes` (existence, type=review, direction, acyclicity, interaction with `activeReviews`/`withdrawnReviews`) **or remove the field**.
2. Rewrite the custody sentence so match ≠ retain/serve/destroy authorization.
3. Put `notServingAuthorization: True` on every `inspect` return value.
4. State in README that `format` is inside the digest and that `import_records` currently requires `inspect is True` as well as `record is True`.
5. Keep examples from being an integration template: show a snapshot that is not a copy of the caller proposal, or stamp them “echoed; illegal as a host implementation.”

Optional hygiene:

- Align snapshot actor strings with `$defs.pin.id` (or document the weaker check).
- Schema-validate `snapshot.authority` as a pin; reject `active ∩ withdrawn` overlap.
- Add the untested edges listed above.
- Tighten `member.key` or document why it is free-form.

Do not add a source resolver, policy engine, clock, store CAS, HTTP uniform denial, or disposition calculator inside this file and then pretend they were always there. Those are new components.

---

## Limits that travel with this verdict

1. Do not publish, install, or assign a public runtime ID.
2. Do not claim native V3 integration, production security boundary, NIST conformance, or privacy/inference prevention.
3. Host must independently attest snapshot, actor catalogs, authority, complete active-review set, withdrawn set, and `now`. Echo is a contract failure.
4. Wrap `inspect` / `import_records` behind real host authentication. The capability dict is an assertion.
5. Do not forward `inspect()` results. No timing/existence protection exists.
6. `applicable-review` is not permission to retain, serve, or destroy. `custodyContext` and `priorReleases` are opaque pins.
7. `body.supersedes` is inert evidence until implement-or-remove.
8. Codex `51/51` is not this review and is not an external audit.
9. Version freeze is `0.0.0-prototype.1` / `vercy-disclosure-research`. A later version needs its own review after the missing metamodel package exists.

**Decision: ACCEPT WITH LIMITS** for the declared metadata-only research-prototype scope. **REVISE** if this artifact is presented as a release candidate while `supersedes` remains unresolved or while inspect results / echoed snapshots are treated as serving authority. **BLOCK** if publication, native production integration, or a conformance claim is requested on these bytes.