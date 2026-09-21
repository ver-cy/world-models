# Verdict: **ACCEPT WITH LIMITS**

This verdict applies to a bounded reviewable-draft reference only. I found no blocking defect and no claim that would make the package unsafe to use as described. Four local inconsistencies should be fixed before publication (F1–F4 below). None of them changes code behaviour, and none of them creates a serving grant or a privacy claim.

This review does not authorize serving source values, does not prove privacy and does not confer or remove the owner's publication authority.

---

## 1. Local defects and contradictory claims (fix before publication)

| # | Anchor | Witness | Severity | Minimal fix |
|---|---|---|---|---|
| **F1** | `spec.json` → DR-ACT06, DR-ACT21 | The action text says "Return insufficient-context for unsupported comparison" and "Return insufficient-context until actual custodian resolves". `disclosure.py:inspect()` never does either: it compares opaque pins by exact equality and can return `applicable-review` while a hold is unresolved. The correction exists only in `adoption-limits.md`, which is not covered by the spec digest. An agent reading only `spec.json` could treat `applicable-review` as meaning custody is resolved. This is the closest thing in the package to an unsafe implied use. `notServingAuthorization=true` and the "Proposed operation only" suffix mitigate it. | Medium (documentation) | Reword both actions to "Host evaluator returns insufficient-context…; `inspect()` does not perform this check". Add one sentence to the embedded contract's custodyContext paragraph. Doing so changes the spec digest, so re-pin. |
| **F2** | `review.md` ¶2 | Cites "the review.json release bookkeeping". `review.json` is not in the supplied frozen package. The claim is dangling and unverifiable. | Low–Medium | Supply `review.json`, or reword the sentence as future and not-yet-existing. |
| **F3** | `composition.yaml`, `spec.json.composition`, `crosswalk.json` row WM-XCT-002 | The relation is labelled `selected-semantic-overlap-not-subtype`, but the same row says `selectedFindingIds: []` and "boundary-only reference, no finding selected". The label contradicts the row. | Low | Use a distinct relation such as `boundary-reference-no-findings-selected` for 002, in all three places. |
| **F4** | `crosswalk.json` vs `adjacent-model-checks.json` | See details below. The two files support different evidence strengths for the same parents, and `crosswalk.json` makes the stronger claim for all four. | Low (evidence hygiene) | Either narrow the crosswalk wording or add equivalent byte and parse evidence for 002, 003, 004 and 012. |

Details for F4:
- `crosswalk.json` asserts `fullSpecificationBytesCompared: true` and "Complete spec parsed" for 002, 003, 004 and 012.
- `adjacent-model-checks.json` records only "Runtime metadata only; semantic compatibility… not established" for 004 and 012, and records no entry at all for 002 or 003.
- Only 020 has supplied `liveByteEqualityVerified`.

The digests themselves agree across all three files.

### Smaller local items (optional, would strengthen evidence)

- **`disclosure.py:validate_native`: one error message covers three time conditions.**
  - One string, "native storage time", covers `object ≤ receipt`, `receipt ≤ now` and `declared ≤ receipt`.
  - The `isolated-receipt-before-assessment` negative in `acceptance.py` is only isolated by construction. I checked the construction and it is sound: the corrected review was assessed at 10:02:00 and receipt was set to 10:01:30, with the object and `now` ordered correctly.
  - The error message cannot distinguish which condition failed. Distinct messages would match the inspect-side distinct reasons added in this release.
- **Hard-coded fields in `acceptance.py`'s report.**
  - `objects: 2`, `immutableRevisionFacts: 3`, `sameVersionRoundtrip` and `companionRejected: True` are constants.
  - The first three are guarded by earlier `require()` calls and corroborated by the native counts.
  - `companionRejected` is evidenced only indirectly, by the equivalent `nested-invalid` mutation. The byte-written bad fact is never passed to `nested()`. Compute the field rather than asserting it.
- **Tool-pin closure in `acceptance.py:run`.**
  - The harness verifies the bytes of the listed files only. It does not check the transitive import closure, stale `__pycache__` bytecode, or name shadowing from `sys.path.insert(0, …)` for both tool roots.
  - `README.md` claims "tool-pins.json pins every required external tool asset". That claim is stronger than what the harness enforces.
  - Fix: run with `-B -I`, or assert that every loaded module's `__file__` is in the pinned set. Otherwise soften the README.
- **Cycle-detection wording in `model-spec.md`.**
  - It says a digest-consistent cycle "is not part of the executed fixture evidence". It could say plainly that such a cycle is infeasible without a SHA-256 collision, because each link pins its target's digest. The traversal is defensive only.
- **Unbounded review validity.**
  - `validTo` has no maximum. "Every verdict expires" (`adoption-limits.md`) is formally true, but the window can run to year 9999.
  - Either state that the maximum validity window is host policy, or add a profile bound.

---

## 2. Topic-by-topic check

**Two-object identity: sound.**
- `import_records` and `inspect` both reject an identity that changes type.
- `native_fact_id` is derived from Dimension, id and revision. `objectId` equals the record id and `objectType` is checked.
- Members, fields and pins are embedded and have no lifecycle of their own (`boundary-decision.md`, `whole-object-coverage.yaml`).

**Immutable revisions: sound within the supplied register.**
- The same revision with a different digest is rejected. Exact replay is idempotent. Duplicate stored revisions are rejected.
- At-rest append-only storage and CAS are correctly declared as host duties (`bindings/native-v3.md`, `model-spec.md`).

**Time: sound.**
- `instant()` uses `[0-9]` with `fullmatch`. This covers the schema `\d` and `$` weaknesses (Unicode digits, trailing newline) for every time field that reaches `instant()`.
- Review times satisfy `reviewedAt ≤ validFrom < validTo`, and the review window is half-open.
- `asOf` must equal `now`.
- Native receipt is checked as `object ≤ fact ≤ now` and `declared ≤ fact`, with `validFrom == recordedAt`.
- The two constructed snapshots (10:01:30 and 12:00) are honestly labelled as not preserved history.

**Digest encoding: consistent with the documentation.**
- Keys are sorted by code point, output is compact with `ensure_ascii=False`, and control characters use lowercase `\u00xx`.
- Surrogates and `str`/`dict` subclasses are rejected.
- Integers are limited to ±(2⁵³−1). `-0` parses to `0`, so the digest is over the parsed value, which matches the documented model.
- The "not JCS" disclaimer is present.

**Active, superseded and withdrawn sets: sound as scoped.**
- Active IDs are unique, and active and withdrawn sets must be disjoint by (id, revision).
- The supplied reviews must equal the active set.
- A still-active immediate supersession target is rejected, as is a forged supersession digest.
- Deactivating transitive ancestors is declared as a host duty. A successor whose target is neither active nor withdrawn is allowed, which is consistent with invariant 9 as worded.

**Conflict and mastership: sound.**
- Disagreeing eligible verdicts produce `conflict`. Ignored reviews keep their verdict and reason.
- An author's objection under segregation still counts.
- `mastership-and-rights.yaml` separates owners correctly.

**Scalar metadata boundary: sound.**
- The schema is closed. Field names are top-level identifiers only. Kinds are limited to scalars. There is no payload field.
- The free-text `residualRisk` leakage risk is disclosed.

**Exact pins: sound.**
- Every reference is `{id, revision, digest}`. Reference coherence is enforced per record.
- The snapshot compares the proposal pin, context and members exactly.

**Five facets: complete.** `whole-object-coverage.yaml` gives all five canonical facets as `required` for both types.

**24 question routes: complete.** Each finding names its local versus host or deferred scope, and the counts match `statistics`: 4 bundles × 2 layers × 3 findings = 24. The one wording issue is F1.

**External policy, classification and custody: correctly deferred.**
- These appear only as opaque pins.
- There is no executable delegation to 002, 003, 020, DAT-004, KNW-012, 035 or 038.
- WM-XCT-035 is an explicit deferred target, and parent holds are retained verbatim.

**Bounds and migration: honestly stated.**
- The 128-record register ceiling is described as effectively a growth ceiling.
- There is no tombstone or disposal operation, and no cross-version conversion. Version guards use `RuntimeError`, not `assert`, and a `-O` test covers them.

**Negative evidence: matches the claims.**
- There are 22 negatives per profile, and the listed labels match the code.
- 108 unit tests are listed in `test_disclosure.py`, and I counted 108 methods. This matches `testsRun`, but that is executed evidence from the package, not from me.
- The boolean-rank bypass is correctly closed: `False == 0` defeats the dict equality check, and the separate `type(...) is int` check catches it.

**V3 envelope versus nested validation: explicit and demonstrated.**
- `invalidNestedFact.native.valid = true` while the companion rejects the same content.
- `bindings/native-v3.md` states the required call sequence and that V3 does not dispatch the companion automatically.

**Hash cross-consistency (declared values only, not recomputed):**
- `acceptance-results.sourceDigests` and `test-results.inputHashes`/`exampleHashes` match the supplied header hashes for every overlapping file.
- `installationPin.specDigest` equals the `spec.json` header.
- The fixture proposal and review digests in `examples/*.json` equal those in the acceptance answers.
- `AGENTS.md` and `agent-guide.md` are byte-identical by declared hash, which is intentional.

---

## 3. Host duties correctly declared (not defects)

The host is responsible for:
- authentication and IAM
- current grant evaluation
- independent pin resolution and completeness of the snapshot
- mapping actor aliases to actual people
- clock accuracy
- deactivating transitive ancestors
- append-only storage, CAS and anchors for prior digests
- the diagnostic channel and side-channel control
- custody and hold decisions
- disposal while preserving reference closure

The package states all of these consistently across `adoption-limits.md`, `bindings/native-v3.md`, `model-spec.md` and `lifecycle/transitions.md`.

## 4. Deferred domain scope (not defects)

The following are out of scope and stated as such: a retention and disposition engine (035), policy evaluation (038), privacy mechanisms, classification comparability, source-aggregate calculation, existing-Dimension migration, concurrency and production adapters.

---

## 5. Read scope

I read 33 file blocks completely, and each ended with its END FILE marker. I detected no truncation.

- acceptance-results.json
- acceptance.py
- adjacent-model-checks.json
- adoption-limits.md
- agent-guide.md
- AGENTS.md
- bindings/native-v3.md
- boundary-decision.md
- composition.yaml
- crosswalk.json
- disclosure.py
- disclosure.schema.json
- examples/ai.json
- examples/matrix.json
- examples/startup.json
- invariants.md
- lifecycle/transitions.md
- mastership-and-rights.yaml
- migration.md
- model-fields.md
- model-spec.md
- publication-manifest.draft
- README.md
- requirements.txt
- research.md
- review.md
- runtime-model.reference.json
- source-verification.json
- spec.json
- test-results.json
- test_disclosure.py
- tool-pins.json
- whole-object-coverage.yaml

**Referenced but not supplied:** `review.json` (see F2), all pinned composer and skill toolchain bytes, the parent specifications, the source-verification pages, and every `ver.cy` URL.

## 6. Unverified scope

- I used no tools, executed nothing and recomputed no hashes. All hash agreement above compares declared values only.
- Test and acceptance results are package-supplied execution evidence, not mine.
- I inferred no behaviour of the toolchain (`c.now`, `c.digest`, `append`, `native_validate`, `bootstrap`) beyond what the acceptance report records.
- I did not verify parent-spec content, the parent finding inventories or holds, the external sources, or live catalogue state.
- I did not byte-compare `spec.json`'s embedded `contract` and `invariants` against `model-spec.md` and `invariants.md`. They agreed on reading.
- I verified no real governance, production storage or privacy property, and none is claimed.
