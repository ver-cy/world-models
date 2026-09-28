## Verdict

**REVISE** — narrow text repair, not a disposition change. PROFILE over WM-DAT-001 and WM-DAT-004 with `newRuntimeId: false` is confirmed correct; no constraint requires an aggregate the bases lack. Four constraint defects admit contradiction as written.

## Critical findings

1. **Released-version mutability is unstated.** Constraint 5 pins one exact contract version per governed dataset version, but fixture `independent-contract-version` updates that binding "under publication rules" with no new dataset version. No listed constraint supplies those rules. As written, one dataset-version identifier resolves to different contract pins over time. Same hole on bytes: nothing forbids a distribution being regenerated under an unchanged version identifier, so `two-distributions` fixity is not durable. Add: conformance assertions are append-only and timestamped, and re-issued bytes force either re-declared fixity under a new distribution or a successor version.
2. **Breaking-change derivation is under-determined.** Constraint 8 makes dataset breaking status derivable *only* from a contract compatibility outcome. Content-level and value-domain breaks (constraint 11: a retired code-list value, a unit change) pass structural checks or produce no outcome at all — fixture `dataset-successor` exercises exactly that path. Either scope the flag to contract-structural breakage and name it so, or admit a second signal with its own master; a single flag with two silent sources recreates the duplicate master the profile forbids.
3. **`NONE` and transitive modes.** Constraint 7 requires a mode and "one compatibility-check outcome" but neither constrains `NONE` (verdict vacuous, derivation always non-breaking) nor names the baseline version. Transitive modes yield checks against N predecessors. Require the outcome to name its baseline set and require a recorded exception for `NONE`.
4. **"or equivalent fixity evidence" is undefined**, reopening `missing-distribution-fixity`. Require a named digest algorithm and value, or a signed manifest that itself carries one.
5. **Prose-only boundaries.** Dataset-level quality evidence versus the EM-DAT-04 metric/run masters appears in local evidence but in no constraint. The ODCS `dataProduct` element is a live import path for the EM-DAT-02 master; constraint 13's exclusion should name it.

No hidden `DatasetSchemaContract` root is present: constraints 1, 2, 12, 13 and fixture `fused-new-root` close it. The conformance binding is the only site where such a root could accrete — it must remain a facet of the WM-DAT-001 dataset version, never a joint entity.

## Required holds

All six candidate holds stand; none contradicts the candidate, and each is base-level. Blocking canonical publication: both bases `publishableCanonical: false` / `reviewable-draft`; DataCite 4.6/4.7 and live source pinning; ODCS pinning plus the `dataProduct` deprecation contradiction; ISO/IEC 11179 clause-level evidence absent; multi-profile SHACL unrun. Add two candidate-level holds: released-version immutability unspecified (finding 1) and breaking-change source scope unresolved (finding 2). None prevents a non-canonical reviewable draft.

## Scenario result

Nine negative fixtures pass on the stated constraints, except `missing-distribution-fixity`, which the "or equivalent" escape weakens. Four positives pass; `independent-contract-version` is not derivable from any constraint and conflicts with the exact-pin rule.

## Identifier decision

No new model or runtime identity. Reuse WM-DAT-001 and WM-DAT-004, version-pinned at `0.3.0-research.1`. Issue the repairs as `0.1.0-candidate.3`, `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`. No publication authority granted here.
