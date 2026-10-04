# EM-XCT-09 R1: Static Implementation Audit

## 1. Scope reviewed

I read the full bodies of all 32 files listed under `includedFullBodies` in parts 1–10. No part was truncated. The files were:

- **Executable:** `classification_review.py`, `classification.schema.json`, `acceptance.py`, `fixtures.py`, `test_classification.py`
- **Examples:** the three example packets
- **Reports:** `test-results.json`, `acceptance-results.json`
- **Metadata:** `spec.json`, `tool-pins.json`, `runtime-model.reference.json`, `composition.yaml`, `crosswalk.json`, `invariants.json`, `lifecycle/transitions.json`, `mastership-and-rights.yaml`, `whole-object-coverage.yaml`
- **Documentation:** all Markdown docs and `LICENSE`

**Excluded, hash-only or not supplied:**

- the four upstream WM-KNW-018/WM-XCT-020 `spec.yaml`/`AGENTS.md` files
- the WM-XCT-040 composer (`composition.py`, `bootstrap_dimension.py`)
- the Vercy native skill (`write_record.py`, `validate_dimension.py`, schemas)

I make no claim about their behaviour, including what "outer V3 validation" actually checks.

I used no tools. I did not execute tests, fixtures or acceptance code, and did not compute or verify any SHA-256. Where I say digests "agree", I mean only that the same literal strings appear consistently across files: for example, the `spec.json` digest in `acceptance-results.json` pins matches the manifest, and `test-results.json` and `acceptance-results.json` report the same `buildId`. Author test and acceptance reports are treated as claims. I also did not verify source authenticity, jsonschema version behaviour, or production fitness.

## 2. Verdict

**BLOCK**, on one narrow, cheaply fixable blocker (B1). Apart from B1, the evaluator matches its stated finite dialect closely. Without B1 I would return ACCEPT WITH LIMITS.

## 3. Blocker

### B1. Conflicting captures of the same release coordinate are not refused across profiles, so a false `candidate-only` can result

**Where:** `classification_review.py`, `_assess`: the snapshot loop and `compile_profile`.

**Spec claim** (`model-spec.md` / `spec.json`, "Profile and membership semantics"): "Duplicated codes, duplicated/conflicting release coordinates and duplicate allowed entries are refused."

**Implementation:** the only check is `require(rk not in releases, 'Conflicting or duplicate release snapshots')`. It runs inside a single profile's `releasePins`. Base and target profiles each get their own `releases` dict. In `migration` mode no ancestry relation is required between them, so the base can pin one scheme-release snapshot for `(S, "1")` and the target a different one for the same `(S, "1")`. Both can declare `complete: true` and still disagree on concepts, status, selectability, definitions or validity.

**Minimal counterexample** (a static trace through the code, not executed):

1. Mode `migration`, `inference: direct-only`.
2. `rel-old` scheme-release: `scheme=S, version="1", complete=true`. Concept A is `status: "retired", selectable: false, validFrom: START, validUntil: null`. B and C are active.
3. Base profile pins `rel-old`, allows `S/1/{A,B,C}`, min 1, max 2, strength required.
4. Assignment `{S,1,A}` is asserted, valid from START, and pinned to the base.
5. `rel-new` scheme-release: `scheme=S, version="1", complete=true`, containing only A, with `status: "active", selectable: true` and a different definition.
6. Target profile pins `rel-new`, allows `[S/1/A]`, min 1, max 2, with the same subjectClass, unit, slot, meaning and required strength.
7. Crosswalk with matching context, `complete: true`, one entry `S/1/A → S/1/A`, `exactMatch`, approved, with a matching host acknowledgment.

**How the trace runs:**

- Every snapshot-level check passes.
- `compile_profile(base)` and `compile_profile(target)` each see one release.
- `historic` is `conforms`, because `new=False` ignores A's retired and non-selectable status.
- Target eligibility reads `rel-new`, finds A active and selectable, and returns `eligible`.
- `safe` holds, `distinct == {S/1/A}`, and `identity_ok` holds.

**Result:** `migrationDisposition = proposed-candidate`, `outcome = candidate-only`. The packet thereby recommends new use of a code that another complete capture of the same release records as retired and non-selectable. Nothing is emitted: no finding, question or insufficient-context outcome.

This is an internal contradiction that the evaluator can see. It is not an external-truth problem delegated to the host. It also directly contradicts the documented refusal rule.

**Smallest fix:**

- In the snapshot loop, keep a packet-wide map from `(scheme, version)` to a canonical encoding of `{complete, concepts}` for every `scheme-release` payload.
- Raise `require(..., 'Conflicting release snapshots for one coordinate')` when a second snapshot for the same coordinate differs. Simpler still, refuse any second snapshot for the same coordinate.
- Add a regression test using the counterexample above, asserting `Invalid`.
- Regenerate `buildId`, the fixtures, `test-results.json` and `acceptance-results.json`.

Exact duplicates can be allowed, but the rule should say so explicitly.

## 4. Nonblocking observations

Ordered roughly by significance. None of these produced a false conformance or a false candidate in my trace.

### 1. A selected revision that the packet itself shows was corrected passes silently

If snapshot X is selected and another snapshot in the packet has `corrects = pin(X)`, the evaluator never notices. It will return `conforms` or propose a migration candidate from the superseded revision. This follows the documented "host selects" rule, but the evidence is in the packet.

*Fix:* emit a notice, or preferably an `insufficient-context` finding, when any packet snapshot corrects a selected assignment.

### 2. Same-source collisions for other snapshot kinds are unchecked (same class as B1, lower impact)

Two `slot-profile` snapshots can share a payload `(id, version)` with different content. Two `assignment` snapshots can share `(id, revision)` with different values. Neither is detected. Assignments are gated by explicit host selection, and profiles in migration mode are legitimately distinct, so neither yields a false candidate in my trace. Hardening them alongside B1 is still recommended.

### 3. Duplicate crosswalk pins are accepted

`packet.crosswalks` has no uniqueness check, unlike assignments. The same crosswalk pinned twice duplicates `alternatives` and applicable rows. There is no false candidate, because `distinct` is unchanged, but the output overstates the evidence and can grow up to 8×.

*Fix:* require unique crosswalk pin IDs.

### 4. Native replay cannot distinguish a host-issued basis from a fabricated one

- `native_records` and `validate_native_fact` only call `inspect_snapshot`.
- Anyone with storage write rights can fabricate `approvalBasis` entries, recompute a self-consistent `candidate-only` assessment, and record a fact whose `authority.source` is the owner.
- Both outer validation and nested validation will pass it.

The limitation is documented ("historical consistency, not future authorization"; host storage permissions are mandatory) and is within the stated trust model. However, the assessment records no host-context identity (actor, grant interval, or a host-context digest), so a later reader cannot tell which grant produced it.

*Recommendations:* record a non-authorizing host-context digest and actor in the assessment. In `bindings/native-v3.md`, state explicitly that `native_records` performs no authorization.

### 5. `bindings/native-v3.md` overstates what the companion validator checks

The doc says the validator "checks local object identity/owner/digest/capture". `validate_native_fact` checks only the fact record. The companion never validates the object record (objectType, accessClass, provenance, `recordId`).

*Fix:* either add `validate_native_object` or narrow the wording.

### 6. Capacity limits are inconsistent

- The native value `{packet, assessment}` must encode within 1 MiB.
- A near-limit valid packet, whose assessment copies full source and target arrays into `alternatives`, will make `inspect_snapshot` or `native_records` raise `Invalid`. That result is valid but can be neither recorded nor replayed.
- `review()` returns the assessment without schema-validating or encoding it, so the CLI can fail at print time and report the error as `rejected-input`.

*Fix:* validate and encode the assessment inside `review()`, and document the effective native ceiling.

### 7. `chain-requested` is honoured in every mode

In `profile` and `assignment` mode, `inference=chain-requested` yields `unsupported-chain` and outcome `unsupported`. This over-refuses: it is safe, but probably unintended.

*Fix:* either require `direct-only` outside migration, or document the behaviour.

### 8. Validity failures at `effectiveAt` are categorized inconsistently

When the assignment interval excludes `effectiveAt`, the result is `outside-valid-time`. When a concept interval excludes it, the result is `does-not-conform`. Both collapse to `does-not-conform` at top level, but the per-assignment distinction the spec emphasises is lost for concept validity.

### 9. Proposed assignments pass assignment mode

A `proposed` assignment yields top-level `conforms-to-local-profile`, with `stateAsClaimed` retained. The spec permits this ("structurally assessed"), but a notice finding would reduce the risk of the result being read as operative truth. Migration mode correctly requires `asserted`.

### 10. Irrelevant host approvals are silently absorbed

Acknowledgments whose `snapshotDigest` or `entryId` matches nothing in the packet are kept in `approvalBasis` and change `assessmentId`. This is harmless, but consider refusing them or at least flagging them.

### 11. Profile minimum versus the assignment cap

`slot-profile.min` may reach 256, while assignment `values` is capped at 32. A profile with min greater than 32 passes profile-only review even though no schema-valid assignment can ever satisfy it. The spec acknowledges the cap, but the "unsatisfiable minimum" rule could also check `min <= 32`.

### 12. Several non-migration branches emit no alternatives

The chain, metamodel and multi-input migration branches return empty `alternatives`. The evidence remains in the packet, as documented. Callers should not read an empty `alternatives` array as "no correspondence exists".

### 13. Acceptance-report literals

`acceptance.py` writes `failed: 0` and `nativeRoundTripExact: True` as literals. They are reachable only after the corresponding `require` checks pass, so they are not dishonest. A failing run, however, produces no report rather than a failure report.

### 14. Referenced files missing from the package

The package references `review.json`, `review.md`, `primary-notes.md`, `platform-evidence.json`, `study-request.md` and `browser-delivery.json`. None is in the audited set. These are outside audit scope, but readers following `README.md` or `publication-addendum.md` will not find them in the package.

### 15. Test gaps

Tests worth adding:

- B1
- observations 1 and 3
- a deprecated (not retired) target
- a target outside its concept validity window at `targetAt`
- a competing entry in a context-mismatched crosswalk (expected to be ignored, with a notice)
- `unsupported` in profile-only mode

`test_empty_source_birth_is_preserved_in_packet` asserts only that no candidate is produced, not that anything is preserved.

## 5. Checked and found consistent (static reasoning only)

**Host gate.** `review()` binds actor, purpose, Dimension, owner and exact packet digest, over a half-open grant interval. Host-context errors collapse uniformly to `Denied`. A future `knowledgeAt` is refused. All timestamp fields in packets, snapshots, concepts, entries and the host are passed through `stamp` or `interval`, so the lexicographic string comparisons in `within` are sound for this fixed format.

**Canonical encoding.** Floats, NaN, duplicate keys, a BOM, C0/C1/DEL characters and lone surrogates are refused, and nesting and size are bounded.

**Snapshot integrity.** Digests are recomputed. Pins check both ID and kind. Corrections require the same binding, subject and slot with a lower revision. Capture time must not follow `knowledgeAt`, and assertion time must not follow capture.

**Profiles.** Ancestry is acyclic and bounded to 8. Child profiles preserve identity, meaning, strength and the exact release-pin set. Allowed sets and cardinality only narrow. Incomplete releases yield `insufficient-context`, and non-required strength yields `unsupported`. The base must appear in the target's ancestry outside migration mode.

**Migration.** The rule matches the spec:

- All applicable targets are collected before eligibility, so profile exclusion does not hide a competitor.
- Compound and empty-sided entries are never flattened.
- The `eligible[0]` index is guarded by short-circuiting.
- Scores, labels and order are never used for selection.
- Approval requires an exact `(snapshotDigest, entryId, approver, evidence)` acknowledgment, and a changed snapshot invalidates it.
- Rejected and superseded rows remain visible but are not operative.

**Top-level priority.** The ordering matches the spec. `effects` is always empty, and model-ID migration is refused.

**Assessment identity.** `assessmentId` is derived from the packet digest, the build ID and the sorted approval basis.

**Native records.** The native object and fact IDs derive from the assessment, not from the classified subject. The validator requires the exact envelope key set, no supersession, and capture at or after the knowledge cut. Replay rejects a forged outcome or candidate.

**Fixtures.** All three reach their documented expected dispositions under my trace.

## 6. Remaining limits (not audit gates for this scoped reference)

- **Host trust and source authenticity.** Everything rests on the trusted host: actor authentication, the clock, full-packet read rights, source custody and completeness, selection of the authoritative revision, and the competence behind mapping approvals. A coherent forged host context cannot be detected.
- **Unverified toolchain behaviour.** Outer V3 validation, writer duplicate-ID behaviour and composer installation fidelity are unverified here, since that code was excluded.
- **Unverified dependency behaviour.** jsonschema `date-time` format checking depends on an installed optional validator. The evaluator's own `stamp` checks make this non-critical.
- **Explicitly deferred scope.** No SKOS, XKOS, SHACL, PROF or FHIR semantics; no chain reasoning; no bitemporal engine; no redacted or federated projection; no retention or erasure; no existing-Dimension migration; no scale guarantees; no standards certification.
- **No publication authorization.** This audit grants no publication, installation or authority. The BLOCK can be cleared by the B1 fix, its regression test, and regenerated test and acceptance evidence, followed by a delta re-audit of `classification_review.py` and `test_classification.py`.