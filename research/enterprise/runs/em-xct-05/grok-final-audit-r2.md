**ACCEPT WITH LIMITS**

Bounded reviewable-draft reference `vr.profile.enterprise-disclosure-review` `0.1.0` / EM-XCT-05. This review is of the reconstructed R2 freeze only. Prior prototype or first-package evidence is not treated as execution or verification of these bytes. Local contract, schema, companion functions, synthetic fixtures, and claimed Codex reports are internally consistent for metadata-only review. This is not a serving grant, privacy proof, classification engine, or custody/disposition system. Publication authority remains the owner’s.

---

## Completeness and read scope

Parts 1–5 were joined in order. Transport cuts (`bindings/native-v3.md`, `research.md`, `spec.json`) were repaired by later parts. No supplied file remains truncated after join.

**Files actually read (33):**
`acceptance-results.json`, `acceptance.py`, `adjacent-model-checks.json`, `adoption-limits.md`, `agent-guide.md`, `AGENTS.md`, `bindings/native-v3.md`, `boundary-decision.md`, `composition.yaml`, `crosswalk.json`, `disclosure.py`, `disclosure.schema.json`, `examples/ai.json`, `examples/matrix.json`, `examples/startup.json`, `invariants.md`, `lifecycle/transitions.md`, `mastership-and-rights.yaml`, `migration.md`, `model-fields.md`, `model-spec.md`, `publication-manifest.draft`, `README.md`, `requirements.txt`, `research.md`, `review.md`, `runtime-model.reference.json`, `source-verification.json`, `spec.json`, `test-results.json`, `test_disclosure.py`, `tool-pins.json`, `whole-object-coverage.yaml`.

`AGENTS.md` and `agent-guide.md` carry the same claimed SHA-256 and the same agent-use text.

**Cited but not supplied:** `review.json` (named in `review.md` as post-audit freeze bookkeeping). Toolchain bytes named in `tool-pins.json` and parent WM-* specification bytes are not in this package.

R2 closed the previous package’s dangling `review.md` and `adjacent-model-checks.json` pointers and aligned the five selected semantic references.

---

## Checklist

### Two-object identity
Closed `oneOf` `#/$defs/proposal` | `#/$defs/review`. Inspect refuses ID collision (`inspect` → `Invalid('identity changes type')`). Import refuses type change on a reused ID (`import_records` `types{}`). Native binding requires `objectType == vr.profile.enterprise-disclosure-review:{proposal|review}`, `objectId == record['id']`, `path == disclosure.{type}.revision`, and `state == active`. New native object negatives: `object-state` (`retired`) and `object-accessClass` (`public`). Withdrawal is snapshot-only; native objects stay `active` (`bindings/native-v3.md`, `adoption-limits.md`). `inspect()` output is ephemeral, not a third persisted type.

`native_fact_id()` still hashes `(dimension, id, revision)` and omits type. That remains safe only while the two-object rule forbids ID reuse. Host object-registry duty, not a hidden third type.

Witnesses: `test_identity_cannot_change_type`, `test_cross_type_identity_on_inspection`, acceptance `object-type` / `object-state` / `object-accessClass`.

### Immutable revisions
Import key is `(type, id, revision)`. Different digest → `immutable revision conflict`; duplicate stored row → `duplicate stored revision`; same digest is idempotent; failed merge leaves the caller list unchanged. Invariant 14 is now scoped to “within a supplied register,” matching the at-rest limit: outer V3 does not detect in-place replacement, and the pure merge compares only the supplied register (`model-spec.md`, `bindings/native-v3.md`). Prior digest/snapshot anchors are host duties.

Acceptance stores **2 objects / 3 immutable revision facts** per profile and requires installed-companion import replay.

### Time
Separate axes are implemented:

| Axis | Rule | Anchor |
|---|---|---|
| Capture | future `capturedAt` → `stale` / `future-capture` | `inspect` |
| Assessment / validity | `reviewedAt ≤ validFrom < validTo`; window `[validFrom, validTo)` | `validate`, `inspect` |
| Snapshot clock | `asOf` must equal evaluation `now` | `validate_snapshot` |
| Native receipt | `validFrom == recordedAt`; `object.recordedAt ≤ recorded ≤ now`; declared `capturedAt`/`reviewedAt` ≤ recorded | `validate_native` |

R2 adds two constructed snapshots, not one relabeled clock: `10:01:30Z` counts revision `1`; `12:00:00Z` counts revision `2` and lists revision `1` as withdrawn (`acceptance-results.json` `historicalAndCurrentAnswers`). `clockMeaning` states neither is preserved real history nor a serving decision.

Isolated assessment≤receipt negative: corrected review `reviewedAt=10:02:00Z`; fact `recordedAt`/`validFrom` forced to `10:01:30Z` with matching object receipt; `validate_native` must raise `native storage time` while object≤receipt and receipt≤now remain true (`isolated-receipt-before-assessment`).

Ignored-review reasons remain distinct and ordered: `authority`, `self-clearance`, `future-assessment`, `not-yet-valid`, `expired`.

### Digest encoding
`hash_body` is SHA-256 over `canonical(record without top-level digest)`. `canonical()` is the named local restricted JSON (not JCS). `load()` rejects duplicate keys, non-integer numbers, invalid UTF-8, and integers outside `±(2^53-1)`. Version is inside the digested record. Module import checks schema `const` on proposal, review, and snapshot, including under `python -O`.

**Hashes were not recomputed.** Claimed cross-links inside the package are consistent: `disclosure.py` `c2371aac…` appears as file header, `test-results.json` `codeSha256` / `inputHashes`, and `acceptance-results.json` `sourceDigests`; `spec.json` `c5cd24a3…` is both file pin and `installationPin.specDigest`; example headers match `exampleHashes`.

### Active / superseded / withdrawn
Unique active IDs; unique withdrawn `(id, revision)`; active ∩ withdrawn empty even when digests differ. Supplied review pins must equal `activeReviews`. Immediate still-active supersession target and forged supersession digest are rejected. Import checks exact pin, type, same proposal identity, nondecreasing `reviewedAt`, and acyclicity. Inspect sees only immediate edges in the supplied active set; transitive ancestor deactivation remains a host duty. Native `V3-CURRENT-TRUTH-CONTESTED` is expected coexistence, not an active-review selector.

### Conflict and mastership
Disagreeing eligible verdicts → `conflict`. Under segregation, an author’s `rejected`/`inconclusive` still counts. Self-clearance is excluded only when `separateReviewer` and verdict is `cleared`. Startup fixture `separateReviewer: false`; matrix/ai `true`.

Storage authority is exact `{source: writer, rank: 0}` **and** `type(rank) is int`. That extra type check is required because in Python `False == 0`, so `rank=False` would otherwise pass dict equality. Witnesses: `storage-authority` (`rank=1`) and `boolean-authority-rank` (`rank=False`). Capability dicts are host assertions (`authorize`).

`inspect()` can still return `applicable-review` while a custody hold is unresolved, because it compares only the opaque supplied pins. `adoption-limits.md` now states that DR-ACT06/DR-ACT21 and hold resolution are host checks before serving, not `inspect()` computations. Question-tree “denied” maps to raised `Unauthorized`, not a denied status.

### Scalar metadata and exact pins
Field kinds are scalars only. Nested/wildcard names and payload value fields are rejected. Missing classification bindings cannot collapse to public/empty. Pins are `{id, revision, digest}` with `additionalProperties: false`. Record-level coherence: one revision/digest per referenced ID. No URI alias folding.

### Five facets and 24 routes
`whole-object-coverage.yaml` marks all five canonical facets required on both types, without promoting seal/inspect to grants or deletion.

`spec.json` tree completes through `DR-Q24`. Statistics match: 4 bundles, 8 layers, 24 findings/questions/artifacts/actions. Q10 grant, Q17 privacy mechanism, Q21–Q23 retention/disposal, and Q24 cross-version migration are outside or deferred. Invariant 16 is explicitly not a unit-test proof.

### External policy / classification / custody
`composition.yaml`, `spec.json` `composition.semanticReferences`, and `crosswalk.json` `composition.semanticReferences` now list the same five overlap pins (002, 003, 020, DAT-004, KNW-012). WM-XCT-035 is only a `research-target` row plus `deferredTargets: ["WM-XCT-035"]`. `adjacent-model-checks.json` is supplied and concludes “No runtime import or inherited readiness is established.” 005 is legacy non-installable; 038 is an unversioned todo. Inherited parent holds stay with the parents. `custodyContext` equality is not retain/serve/destroy.

### Bounds and migration
Reference bounds unchanged: 256 KiB, depth 20, string 4096, generic list/object 128, `existing+incoming ≤ 128`, reviews ≤ 64; schema maxima 32 members / 64 fields / 8 bindings / 16 evidence. Same-version roundtrip only; no tombstones; dangling internal pins fail later import. Existing-Dimension migration remains out of scope. At-rest append-only/CAS is a named host duty.

### Negative evidence and V3 vs nested validation
Acceptance records **22** rejected native cases per profile: `subject`, `path`, `revision-storage-key`, `digest`, `public-access`, `master`, `storage-authority`, `boolean-authority-rank`, `validity-receipt-mismatch`, `unit`, `validTo`, `status`, `provenance-source`, `native-supersession`, `storage-before-assessment`, `storage-future`, `nested-invalid`, `isolated-receipt-before-assessment`, `object-state`, `object-accessClass`, `object-type`, `cross-Dimension`.

V3-versus-nested witness is unchanged in kind: stored `verdict=grant-access` still passes outer `native_validate` and is rejected by `validate_native`. `invalidNestedFact` records `native.valid=true`, `conformanceLevel=V3`, `companionRejected=true` on all three profiles. Required sequence remains host auth → pinned V3 envelope → `validate_native` → `import_records` → `inspect` under an independently built snapshot. V3 does not auto-dispatch companion functions.

`grant-access` is not in the verdict enum (`cleared|rejected|inconclusive`).

Unit-suite limit: `test_disclosure.py` claimed hash is unchanged from the prior freeze (`dd35bec9…`). New rank/time/object negatives live in `acceptance.py` only. That is a coverage partition, not a contract contradiction.

### Serving / privacy boundary
`inspect` unconditionally sets `notServingAuthorization: true`. README, `adoption-limits.md`, invariant 16, `agent-guide.md`/`AGENTS.md`, native `scope`, and `review.md` all refuse serving rights, source-value delivery, inference proof, legal conclusion, and verified destruction. Matrix `residualRisk` still states that the validator does not calculate the subtraction path. No inaccurate production-safety guarantee was found that is not already caveated as host/deferred.

---

## Local defects vs host duties vs deferred scope

**Local leftovers (not contract breaks):**
1. `review.md` cites `review.json` for freeze bookkeeping; that file is not in this package. Treat it as post-audit bookkeeping, or drop the sentence.
2. Acceptance fixture still uses `publicationStatus: published`, caveated in `acceptance.py` `compatibility.scope` and now also in README. `publication-manifest.draft` remains `candidate-not-published` / `contourStatus: partial`.
3. Wire `format` remains `vercy-disclosure-research`. README now calls that a deliberate permanent 0.1.0 identifier; renaming requires a version migration.

R2 closed the earlier local defects that mattered: dangling `review.md` and `adjacent-model-checks.json`, 035 listed among selected-overlap pins, boolean rank accepted via `False == 0`, single undifferentiated snapshot clock, and unspecified at-rest/native-object lifecycle limits.

**Explicit trusted-host duties:** authentic actors and write authority; independently resolved complete current snapshot; correct clock; complete local register; active/withdrawn history including transitive predecessor deactivation; distinct-person mapping; storage transactions, append-only/CAS, and independent prior digest anchors; pin resolution for source/schema/shape/classification/custody; current grant evaluation and hold/comparability checks before any serve.

**Deferred / out of scope (do not demand implementation):** production IAM/policy engine, source-value projection, classification comparability engine, privacy mechanism, retention/hold evaluator, disposal/destruction evidence, automatic V3 dispatch, existing-Dimension migration, concurrency store, hostile-input performance.

---

## Minimal fixes

Do not reopen sealed contract bytes for these.

1. Drop the `review.json` sentence from `review.md`, or add that bookkeeping file after this freeze is recorded.
2. Keep the fixture `published` caveat adjacent to any synthetic `publicationStatus` so catalogue status cannot be read off the install object.
3. Leave `vercy-disclosure-research` as the 0.1.0 wire identifier; do not rename in place.

---

## Unverified scope

This review did not execute code, recompute SHA-256, fetch URLs, or inspect toolchain bytes.

Unverified:
- Every `ORIGINAL SHA256` and every digest inside records, fixtures, and pins
- Codex claims in `test-results.json` (`testsRun: 108`, `failures: 0`, Python `3.12.14`, `jsonschema==4.26.0`) and `acceptance-results.json` (`passed: 3`, `executedAt: 2026-09-21T21:57:41Z`)
- Pinned composer/skill bytes in `tool-pins.json`
- Parent WM-* specification bytes and live catalogue URLs
- Any real host snapshot, clock, actor-alias mapping, custody register, or grant
- Privacy, legal, or standards conformance
- Cross-language digest compatibility (explicitly not claimed)
- Contents of the unsupplied `review.json`

A local metadata review of this package is not a source-value serving grant or a privacy proof.
