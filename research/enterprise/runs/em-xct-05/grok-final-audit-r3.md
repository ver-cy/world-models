**ACCEPT WITH LIMITS**

Bounded reviewable-draft reference `vr.profile.enterprise-disclosure-review` `0.1.0` / EM-XCT-05. This review is of the reconstructed R3 freeze only. Prior prototype, R1, or R2 evidence is not treated as execution or verification of these bytes. Local contract, schema, companion functions, synthetic fixtures, and claimed Codex reports are internally consistent for metadata-only review. This is not a serving grant, privacy proof, classification engine, or custody/disposition system. Publication authority remains the owner’s.

---

## Completeness and read scope

Parts 1–6 were joined in order. Transport cuts (`bindings/native-v3.md`, `disclosure.schema.json`, `model-spec.md`, `spec.json`, `whole-object-coverage.yaml`) were repaired by later parts. No supplied file remains truncated after join.

**Files actually read (33):**
`acceptance-results.json`, `acceptance.py`, `adjacent-model-checks.json`, `adoption-limits.md`, `agent-guide.md`, `AGENTS.md`, `bindings/native-v3.md`, `boundary-decision.md`, `composition.yaml`, `crosswalk.json`, `disclosure.py`, `disclosure.schema.json`, `examples/ai.json`, `examples/matrix.json`, `examples/startup.json`, `invariants.md`, `lifecycle/transitions.md`, `mastership-and-rights.yaml`, `migration.md`, `model-fields.md`, `model-spec.md`, `publication-manifest.draft`, `README.md`, `requirements.txt`, `research.md`, `review.md`, `runtime-model.reference.json`, `source-verification.json`, `spec.json`, `test-results.json`, `test_disclosure.py`, `tool-pins.json`, `whole-object-coverage.yaml`.

`AGENTS.md` and `agent-guide.md` carry the same claimed SHA-256 and the same agent-use text.

**Cited and explicitly not evidence:** `review.json`. `review.md` now labels it “not-yet-created … post-audit release bookkeeping … deliberately not evidence in this audit.” That is not a missing required file.

Toolchain bytes named in `tool-pins.json` and parent WM-* specification bytes are not in this package.

---

## Checklist

### Two-object identity
Closed `oneOf` `#/$defs/proposal` | `#/$defs/review`. Inspect refuses ID collision (`Invalid('identity changes type')`). Import refuses type change on a reused ID. Native binding requires `objectType == vr.profile.enterprise-disclosure-review:{proposal|review}`, `objectId == record['id']`, `path == disclosure.{type}.revision`, and `state == active`. Object negatives `object-state` (`retired`) and `object-accessClass` (`public`) are rejected. Withdrawal is snapshot-only; native objects stay `active` (`bindings/native-v3.md`, `adoption-limits.md`). `inspect()` output is ephemeral, not a third persisted type.

`native_fact_id()` hashes `(dimension, id, revision)` and omits type. That remains safe only while the two-object rule forbids ID reuse. Host object-registry duty.

Witnesses: `test_identity_cannot_change_type`, `test_cross_type_identity_on_inspection`, acceptance `object-type` / `object-state` / `object-accessClass`.

### Immutable revisions
Import key is `(type, id, revision)`. Different digest → `immutable revision conflict`; duplicate stored row → `duplicate stored revision`; same digest is idempotent; failed merge leaves the caller list unchanged. Invariant 14 is scoped to “within a supplied register.” Outer V3 does not detect in-place replacement; the pure merge compares only the supplied register (`model-spec.md`, `bindings/native-v3.md`). Prior digest/snapshot anchors are host duties.

Acceptance stores **2 objects / 3 immutable revision facts** per profile and requires installed-companion import replay.

### Time
Separate axes remain implemented: capture, assessment/validity `[validFrom, validTo)`, snapshot `asOf == now`, and native receipt (`validFrom == recordedAt`; `object.recordedAt ≤ recorded ≤ now`; declared capture/assessment ≤ recorded).

Two constructed snapshots: `10:01:30Z` counts revision `1`; `12:00:00Z` counts revision `2` and lists revision `1` as withdrawn (`acceptance-results.json` `historicalAndCurrentAnswers`). `clockMeaning` states neither is preserved real history nor a serving decision.

Isolated assessment≤receipt negative: corrected review `reviewedAt=10:02:00Z`; fact `recordedAt`/`validFrom` forced to `10:01:30Z` with matching object receipt; `validate_native` must raise `native storage time` while object≤receipt and receipt≤now remain true.

Ignored-review reasons remain distinct and ordered: `authority`, `self-clearance`, `future-assessment`, `not-yet-valid`, `expired`.

New honest limit in `model-spec.md`: the format requires an end time but permits dates through year 9999; finite validity is not a short-expiry guarantee.

### Digest encoding
`hash_body` is SHA-256 over `canonical(record without top-level digest)`. `canonical()` is the named local restricted JSON (not JCS). `load()` rejects duplicate keys, non-integer numbers, invalid UTF-8, and integers outside `±(2^53-1)`. Version is inside the digested record. Module import checks schema `const` on proposal, review, and snapshot, including under `python -O`.

**Hashes were not recomputed.** Claimed cross-links inside the package are consistent: `disclosure.py` `c2371aac…` appears as file header, `test-results.json` `codeSha256` / `inputHashes`, and `acceptance-results.json` `sourceDigests`; `spec.json` `208854fb…` is file pin, `installationPin.specDigest`, and `sourceDigests.spec.json`; example headers match `exampleHashes`; README `c13deb9e…` matches `test-results.json` `inputHashes.README.md`.

### Active / superseded / withdrawn
Unique active IDs; unique withdrawn `(id, revision)`; active ∩ withdrawn empty even when digests differ. Supplied review pins must equal `activeReviews`. Immediate still-active supersession target and forged supersession digest are rejected. Import checks exact pin, type, same proposal identity, nondecreasing `reviewedAt`, and acyclicity. Inspect sees only immediate edges in the supplied active set; transitive ancestor deactivation remains a host duty. Native `V3-CURRENT-TRUTH-CONTESTED` is expected coexistence, not an active-review selector.

### Conflict and mastership
Disagreeing eligible verdicts → `conflict`. Under segregation, an author’s `rejected`/`inconclusive` still counts. Self-clearance is excluded only when `separateReviewer` and verdict is `cleared`. Startup fixture `separateReviewer: false`; matrix/ai `true`.

Storage authority is exact `{source: writer, rank: 0}` **and** `type(rank) is int`, so `rank=False` cannot pass via `False == 0`. Witnesses: `storage-authority` and `boolean-authority-rank`. Capability dicts are host assertions (`authorize`).

`inspect()` can still return `applicable-review` while a custody hold is unresolved, because it compares only the opaque supplied pins. That limit is now inside `spec.json` DR-ACT06/DR-ACT21 and `model-spec.md`, not only `adoption-limits.md`. Question-tree “denied” maps to raised `Unauthorized`, not a denied status.

### Scalar metadata and exact pins
Field kinds are scalars only. Nested/wildcard names and payload value fields are rejected. Missing classification bindings cannot collapse to public/empty. Pins are `{id, revision, digest}` with `additionalProperties: false`. Record-level coherence: one revision/digest per referenced ID. No URI alias folding.

### Five facets and 24 routes
`whole-object-coverage.yaml` marks all five canonical facets required on both types, without promoting seal/inspect to grants or deletion.

`spec.json` tree completes through `DR-Q24`. Statistics match: 4 bundles, 8 layers, 24 findings/questions/artifacts/actions. Q10 grant, Q17 privacy mechanism, Q21–Q23 retention/disposal, and Q24 cross-version migration are outside or deferred. Invariant 16 is explicitly not a unit-test proof.

DR-ACT06 and DR-ACT21 now say the **host evaluator** returns insufficient-context for unsupported comparison or unresolved custody; `inspect()` does not perform those checks and `applicable-review` does not establish comparison or custody resolution.

### External policy / classification / custody
`composition.yaml`, `spec.json` `composition.semanticReferences`, and `crosswalk.json` `composition.semanticReferences` list the same five pins. WM-XCT-002 is consistently `boundary-reference-no-findings-selected` with `selectedFindingIds: []`. WM-XCT-003, 020, DAT-004, and KNW-012 remain `selected-semantic-overlap-not-subtype`. WM-XCT-035 is only a `research-target` row plus `deferredTargets: ["WM-XCT-035"]`.

`adjacent-model-checks.json` is supplied. `exactFiveParentChecks` is dated `2026-09-21T22:06:03.092316+00:00` and claims Codex byte comparison plus complete YAML parse for all five parents. `evidenceChronology` states that this stage supersedes the earlier reconnaissance depth labels and that no source-citation or runtime-conformance ratification is inferred. Decision remains: no runtime import or inherited readiness.

005 is legacy non-installable; 038 is an unversioned todo. Inherited parent holds stay with the parents. `custodyContext` equality is not retain/serve/destroy.

### Bounds and migration
Reference bounds unchanged: 256 KiB, depth 20, string 4096, generic list/object 128, `existing+incoming ≤ 128`, reviews ≤ 64; schema maxima 32 members / 64 fields / 8 bindings / 16 evidence. Same-version roundtrip only; no tombstones; dangling internal pins fail later import. Existing-Dimension migration remains out of scope. At-rest append-only/CAS is a named host duty.

### Negative evidence and V3 vs nested validation
Acceptance records **22** rejected native cases per profile: `subject`, `path`, `revision-storage-key`, `digest`, `public-access`, `master`, `storage-authority`, `boolean-authority-rank`, `validity-receipt-mismatch`, `unit`, `validTo`, `status`, `provenance-source`, `native-supersession`, `storage-before-assessment`, `storage-future`, `nested-invalid`, `isolated-receipt-before-assessment`, `object-state`, `object-accessClass`, `object-type`, `cross-Dimension`.

V3-versus-nested witness is executed against the **stored** file, not only an in-memory copy: `acceptance.py` writes `verdict=grant-access` to the last fact path, requires outer `native_validate` still `valid`, then `nested(read(paths[-1]), obj)` must raise. `invalidNestedFact` records `native.valid=true`, `conformanceLevel=V3`, `companionRejected=true` on all three profiles.

Required sequence remains host auth → pinned V3 envelope → `validate_native` → `import_records` → `inspect` under an independently built snapshot. V3 does not auto-dispatch companion functions. `grant-access` is not in the verdict enum (`cleared|rejected|inconclusive`).

Unit-suite partition: `test_disclosure.py` claimed hash `dd35bec9…` is unchanged across the last two freezes. New rank/time/object/stored-fact negatives live in `acceptance.py` only. That is a coverage partition, not a contract contradiction.

### Serving / privacy / environment claims
`inspect` unconditionally sets `notServingAuthorization: true`. README, `adoption-limits.md`, invariant 16, `agent-guide.md`/`AGENTS.md`, native `scope`, and `review.md` all refuse serving rights, source-value delivery, inference proof, legal conclusion, and verified destruction.

README now narrows `tool-pins.json` to the listed external tool **source assets**. It does not attest transitive Python-library imports, module-cache contents, or the whole execution environment.

Matrix `residualRisk` still states that the validator does not calculate the subtraction path. No inaccurate production-safety guarantee was found that is not already caveated as host/deferred.

---

## Local defects vs host duties vs deferred scope

**Local leftovers (not contract breaks):**
1. Acceptance fixture still uses `publicationStatus: published`, caveated in `acceptance.py` `compatibility.scope` and README. `publication-manifest.draft` remains `candidate-not-published` / `contourStatus: partial`.
2. Wire `format` remains `vercy-disclosure-research`. README calls that a deliberate permanent 0.1.0 identifier; renaming requires a version migration.

R3 closed the remaining documentation/evidence leftovers from the prior freeze: the `review.json` pointer is now future bookkeeping and not evidence; WM-XCT-002 is consistently a boundary-only reference; DR-ACT06/21 host-evaluator limits sit in `spec.json`; five-parent byte/parse evidence is a dated stage; the malformed nested fact is checked on stored bytes; the tool-pin environment claim is narrowed; year-9999 validity is not sold as short expiry.

Contract implementation bytes (`disclosure.py` `c2371aac…`, `disclosure.schema.json` `45b2f2c8…`, `test_disclosure.py` `dd35bec9…`) are unchanged from the immediately preceding freeze.

**Explicit trusted-host duties:** authentic actors and write authority; independently resolved complete current snapshot; correct clock; complete local register; active/withdrawn history including transitive predecessor deactivation; distinct-person mapping; storage transactions, append-only/CAS, and independent prior digest anchors; pin resolution for source/schema/shape/classification/custody; current grant evaluation and hold/comparability checks before any serve.

**Deferred / out of scope (do not demand implementation):** production IAM/policy engine, source-value projection, classification comparability engine, privacy mechanism, retention/hold evaluator, disposal/destruction evidence, automatic V3 dispatch, existing-Dimension migration, concurrency store, hostile-input performance.

---

## Minimal fixes

Do not reopen sealed contract bytes for these.

1. Keep the fixture `published` caveat adjacent to any synthetic `publicationStatus` so catalogue status cannot be read off the install object.
2. Leave `vercy-disclosure-research` as the 0.1.0 wire identifier; do not rename in place.
3. After this freeze is recorded, create `review.json` only as the bookkeeping file `review.md` already describes.

---

## Unverified scope

This review did not execute code, recompute SHA-256, fetch URLs, or inspect toolchain bytes.

Unverified:
- Every `ORIGINAL SHA256` and every digest inside records, fixtures, and pins
- Codex claims in `test-results.json` (`testsRun: 108`, `failures: 0`, Python `3.12.14`, `jsonschema==4.26.0`) and `acceptance-results.json` (`passed: 3`, `executedAt: 2026-09-21T22:06:07Z`)
- Pinned composer/skill bytes in `tool-pins.json`, and any transitive runtime environment
- Parent WM-* specification bytes, live catalogue URLs, and the claimed `liveByteEqualityVerified` / `completeYamlParse` results
- Any real host snapshot, clock, actor-alias mapping, custody register, or grant
- Privacy, legal, or standards conformance
- Cross-language digest compatibility (explicitly not claimed)

A local metadata review of this package is not a source-value serving grant or a privacy proof.
