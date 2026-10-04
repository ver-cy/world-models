**ACCEPT WITH LIMITS**

Bounded reviewable-draft reference `vr.profile.enterprise-disclosure-review` `0.1.0` / EM-XCT-05. Local contract, schema, companion functions, synthetic fixtures, and claimed Codex evidence are internally consistent for metadata-only review. This is not a serving grant, privacy proof, classification engine, or custody/disposition system. Publication authority remains the owner’s; this audit neither confers nor removes it.

---

## Completeness and read scope

Transport parts 1–5 were joined in order. Mid-file cuts (`crosswalk.json`, `examples/startup.json`, `spec.json`, `test_disclosure.py`) were **transport truncations only**; after join, those four files parse as complete documents. No remaining cut inside a supplied file body.

**Files actually read (31):**
`acceptance-results.json`, `acceptance.py`, `adoption-limits.md`, `agent-guide.md`, `AGENTS.md`, `bindings/native-v3.md`, `boundary-decision.md`, `composition.yaml`, `crosswalk.json`, `disclosure.py`, `disclosure.schema.json`, `examples/ai.json`, `examples/matrix.json`, `examples/startup.json`, `invariants.md`, `lifecycle/transitions.md`, `mastership-and-rights.yaml`, `migration.md`, `model-fields.md`, `model-spec.md`, `publication-manifest.draft`, `README.md`, `requirements.txt`, `research.md`, `runtime-model.reference.json`, `source-verification.json`, `spec.json`, `test-results.json`, `test_disclosure.py`, `tool-pins.json`, `whole-object-coverage.yaml`.

`AGENTS.md` and `agent-guide.md` carry the same claimed SHA-256 and the same agent-use text.

**Referenced but not supplied:**
- `review.md` — cited in the `disclosure.py` module docstring (“exact external audit scope”) and in `model-spec.md` (“actual audit scope”).
- `adjacent-model-checks.json` — cited from `crosswalk.json` `otherNeighbors`.

Toolchain bytes named in `tool-pins.json` are **not** in this package (by design). Parent WM-* specification bytes are **not** in this package.

---

## Checklist

### Two-object identity
Two exported records only: `ContextPackageProposal` and `JointDisclosureReview`. Schema root is closed `oneOf` `#/$defs/proposal` | `#/$defs/review`. Inspect refuses ID collision (`disclosure.py` `inspect`: `Invalid('identity changes type')`). Import refuses type change on a reused ID (`import_records` `types{}`). Native binding requires `objectType == vr.profile.enterprise-disclosure-review:{proposal|review}` and `path == disclosure.{type}.revision` (`validate_native`). `inspect()` output is ephemeral, not a third persisted type (`boundary-decision.md`, `whole-object-coverage.yaml` `embeddedValues`).

Witnesses: `test_identity_cannot_change_type`, `test_cross_type_identity_on_inspection`, acceptance negative `object-type`.

`native_fact_id()` hashes `(dimension, id, revision)` and omits type. That is safe only while the two-object rule forbids ID reuse across types. That coupling is a named host-registry duty, not a hidden third type.

### Immutable revisions
Import key is `(type, id, revision)`. Different digest → `immutable revision conflict`; duplicate already-stored row → `duplicate stored revision`; same digest is idempotent; failed merge leaves the caller list unchanged (`test_immutable_revision_conflict_transactional`). Corrections are a new revision plus optional exact `body.supersedes` pin. Native facts use empty `supersedes`, `validTo=null`, `status=asserted`; a second storage key cannot conceal a digest change for the same identity/revision (`bindings/native-v3.md`). Acceptance stores **2 objects / 3 immutable revision facts** per profile.

### Time
Separate axes are implemented and named:

| Axis | Rule | Anchor |
|---|---|---|
| Capture | `capturedAt`; future capture → `stale` / `future-capture` | `inspect` |
| Assessment / validity | `reviewedAt ≤ validFrom < validTo`; window `[validFrom, validTo)` | `validate`, `inspect` |
| Snapshot clock | `snapshot.asOf` must equal evaluation `now` | `validate_snapshot` → `snapshot time mismatch` |
| Native receipt | `validFrom == recordedAt`; `object.recordedAt ≤ recorded ≤ now`; declared `capturedAt`/`reviewedAt` ≤ recorded | `validate_native` |

Ignored-review reasons are distinct and ordered as claimed after R3: `authority`, then `self-clearance`, then `future-assessment`, `not-yet-valid`, `expired` (`inspect` cascade; `test_future_assessment_reason`, `test_not_yet_valid_reason`, `test_expired_reason`, `test_start_is_inclusive`, `test_expiry_is_exclusive`).

Acceptance `clockMeaning` correctly separates installation receipt from fixture `asOf=2026-09-21T12:00:00Z`. Clock accuracy and recovery remain host duties.

### Digest encoding
`hash_body` is SHA-256 over `canonical(record without top-level digest)`, encoded `sha256:` + hex. `canonical()` is a **named local** restricted JSON (sorted keys, UTF-8, compact separators, no floats/NaN, list order significant). Explicitly not JCS/RFC 8785 (`model-spec.md`). `load()` rejects duplicate keys, non-integer numbers, invalid UTF-8, integers outside `±(2^53-1)`. Golden vector: `test_golden_encoding_controls_and_separator`. Version is inside the digested record; `0.1.0` rejects prototype versions (`test_unsupported_version`). Module import checks schema `const` on proposal, review, and snapshot (`test_optimized_module_still_rejects_schema_version_mismatch`).

**Hashes in this package were not recomputed.** Claimed cross-file pins are internally consistent (see Unverified scope).

### Active / superseded / withdrawn
`validate_snapshot`: unique active IDs; unique withdrawn `(id, revision)`; active ∩ withdrawn empty even when digests differ (`test_active_withdrawn_different_digest_rejected`). Supplied review pins must equal `activeReviews` or the result is `insufficient-context` / `review-set-incomplete`. Immediate still-active supersession target is rejected (`superseded review still active`). Forged supersession digest is rejected (`incoherent supersession pin`). Import checks exact pin, type, same proposal identity, nondecreasing `reviewedAt`, and acyclicity. Inspect only sees **immediate** edges in the supplied active set; transitive ancestor deactivation is an explicit host duty (`model-spec.md`, `adoption-limits.md`, `bindings/native-v3.md`). Native `V3-CURRENT-TRUTH-CONTESTED` is expected coexistence, not an active-review selector.

Acceptance current answers count revision `2` and list revision `1` under `withdrawn`.

### Conflict and mastership
Disagreeing eligible verdicts → `conflict`; no silent winner (invariant 12; `test_conflicting_active_reviews`). Under segregation, an author’s `rejected`/`inconclusive` still counts and conflicts with another clearance (`test_self_objection_still_counts_under_segregation`). Self-clearance is excluded only when `separateReviewer` and verdict is `cleared`. Startup fixture has `separateReviewer: false`; matrix/ai are `true`.

`mastership-and-rights.yaml` splits source, classification, proposal, review, current active set, supersession, and custody. Storage `masterSystem` + `authority.rank==0` is the registrar, not the reviewer (`validate_native` negatives `master`, `storage-authority`). Capability dicts are host assertions, not credentials (`authorize`).

### Scalar metadata and exact pins
Field `kind` ∈ `{string, integer, number, boolean, null}`; object/array kinds and nested/wildcard names are rejected. No source-value payload field. Missing classification bindings cannot collapse to public/empty (`minItems: 1`; `test_missing_classification_not_public`). Pins are `{id, revision, digest}` with `additionalProperties: false`. Record-level coherence: one revision/digest per referenced ID (`exact_identifiers(..., coherence=True)`; invariants 3). Snapshot-level coherence is not applied; inspect instead exact-compares snapshot context/members and the active pin set. No URI alias folding; hidden/newline characters are rejected.

### Five facets and 24 routes
`whole-object-coverage.yaml` marks all five canonical facets required on both types, without promoting seal/inspect to grants or deletion.

`spec.json` tree: 4 bundles (`DR-B-identity`, `DR-B-disclosure`, `DR-B-composition`, `DR-B-continuity`), 8 layers, `DR-F01`–`DR-F24` / `DR-Q01`–`DR-Q24`. Declared statistics match (24/24/24/24). Each route states local vs host/deferred `implementationScope`. Q10 grant, Q17 privacy mechanism, Q21–Q23 retention/disposal, Q24 cross-version migration are outside or deferred. Invariant 16 is explicitly not a unit-test proof.

### External policy / classification / custody
`crosswalk.json` dispositions:

- WM-XCT-002 — permission evidence only; grant evaluation is host; `runtimeImport: false`
- WM-XCT-003 — exact shape pin; no transform
- WM-XCT-020 — exact binding pin; no scheme authoring or grant
- WM-DAT-004 — exact source-schema pin
- WM-KNW-012 — governed-policy context; no combining language
- WM-XCT-035 — documented deferral; `custodyContext` is an opaque host pin

Inherited publication holds stay with the parents. No executable delegation to 035/038. Equality of `custodyContext` is not retain/serve/destroy.

**Local list inconsistency:** `crosswalk.json` `composition.semanticReferences` includes `vr.wm-xct-035`; `composition.yaml` and `spec.json` `composition.semanticReferences` do not. 035 remains a `research-target` row, not an installable overlap pin.

### Bounds and migration
Code bounds: 256 KiB, depth 20, string 4096 code points, generic list/object 128, `existing+incoming ≤ 128`, supplied reviews ≤ 64. Schema maxima: 32 members, 64 fields, 8 bindings, 16 evidence pins, 64 actor/active/withdrawn entries. These are reference limits, not a hostile-input guarantee (`model-spec.md`, `adoption-limits.md`).

Migration policy is honest: same-version roundtrip only; version is inside the digest; no auto up/down/mixed merge; no tombstones; partial disposal that leaves a dangling internal pin fails later import (`test_partial_disposal_breaks_internal_links`). Existing-Dimension migration is out of scope.

### Negative evidence and V3 vs nested validation
Acceptance mutations (13 per profile) match `negativeCasesRejected`: `subject`, `path`, `revision-storage-key`, `digest`, `public-access`, `master`, `storage-authority`, `native-supersession`, `storage-before-assessment`, `storage-future`, `nested-invalid`, `object-type`, `cross-Dimension`.

V3-versus-nested witness is explicit: `acceptance.py` writes `verdict=grant-access` into a stored fact, requires outer `native_validate` still `valid`, and requires companion `validate_native` to raise `Invalid`. `acceptance-results.json` `invalidNestedFact` records `native.valid=true`, `conformanceLevel=V3`, `companionRejected=true` on all three profiles. Required sequence in `bindings/native-v3.md`: host auth → pinned V3 envelope → `validate_native` → `import_records` on the complete register → `inspect` under an independently built snapshot. V3 does not auto-dispatch companion functions.

`grant-access` is not in the verdict enum (`cleared|rejected|inconclusive`).

### Serving / privacy boundary
`inspect` unconditionally sets `notServingAuthorization: true`. README, `adoption-limits.md`, invariant 16, `agent-guide.md`/`AGENTS.md`, and native `scope` all refuse serving rights, source-value delivery, inference proof, legal conclusion, and verified destruction. Matrix `residualRisk` states that the validator does not calculate the subtraction path. No inaccurate production-safety guarantee was found that is not already caveated as host/deferred.

---

## Local defects vs host duties vs deferred scope

**Local defects (package-internal, not host gaps):**
1. Dangling `review.md` citations (`disclosure.py` docstring; `model-spec.md`).
2. Dangling `adjacent-model-checks.json` citation (`crosswalk.json` `otherNeighbors`).
3. `vr.wm-xct-035` listed in `crosswalk.json` composition references but not in `spec.json` / `composition.yaml` selected-overlap lists.
4. Wire `format` remains `vercy-disclosure-research` at version `0.1.0` (naming leftover, not a logic break).
5. Acceptance fixture `publicationStatus: published` vs `publication-manifest.draft` `candidate-not-published`. The fixture explains this as a catalogue lifecycle value in synthetic install data (`acceptance.py` `compatibility.scope`). Still a reader footgun if that sentence is ignored.

**Explicit trusted-host duties (not defects):** authentic actors and write authority; independently resolved complete current snapshot; correct clock; complete local register; active/withdrawn history; distinct-person mapping; storage transactions and access/custody; deactivation of transitive superseded ancestors; pin resolution for source/schema/shape/classification/custody; current grant evaluation before any serve.

**Deferred / out of scope (do not demand implementation):** production IAM/policy engine, source-value projection, classification comparability engine, privacy mechanism, retention/hold evaluator, disposal/destruction evidence, automatic V3 dispatch, existing-Dimension migration, concurrency/CAS store, hostile-input performance.

---

## Minimal fixes

Do not reopen sealed contract bytes for these.

1. Replace the two `review.md` pointers with `adoption-limits.md` + `publication-manifest.draft`, or add `review.md`.
2. Drop or supply `adjacent-model-checks.json`.
3. Keep WM-XCT-035 only on the deferral row (or give it a separate `research-targets` list, not `selected-semantic-overlap`).
4. Keep the acceptance fixture caveat next to any `publicationStatus: published` so catalogue status cannot be read off the synthetic install object.

Optional later (not required for this draft): rename wire `format` away from `-research` on the next version bump (that bump will change every digest).

---

## Unverified scope

This review did not execute code, recompute SHA-256, fetch URLs, or inspect toolchain bytes.

Unverified:
- Every `ORIGINAL SHA256` and every digest inside records/fixtures/pins
- Codex claims in `test-results.json` (`testsRun: 108`, `failures: 0`, Python `3.12.14`, `jsonschema==4.26.0`) and `acceptance-results.json` (`passed: 3`, `executedAt: 2026-09-21T21:42:53Z`)
- Pinned composer/skill bytes in `tool-pins.json`
- Parent WM-* specification bytes and live catalogue URLs
- Any real host snapshot, clock, actor-alias mapping, custody register, or grant
- Privacy, legal, or standards conformance
- Cross-language digest compatibility (explicitly not claimed)

Claimed hash *cross-links* inside the package are consistent with one another (`disclosure.py` `c08df6f0…` in acceptance sourceDigests and test-results; `spec.json` `0a0b6926…` as both file pin and `installationPin.specDigest`; example file headers match `test-results.json` `exampleHashes`). Consistency of labels is not verification of bytes.

---

Existing prototype evidence is treated as Codex evidence of *those* runs, not as a re-execution of these transported bytes. A local metadata review of this package is not a source-value serving grant or a privacy proof.
