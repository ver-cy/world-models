## Verdict

**ACCEPT WITH LIMITS.** The PROFILE disposition over WM-KNW-010, WM-REC-010, WM-KNW-007 and WM-KNW-008 is semantically sound and correctly declines a runtime ID; the five-authority split (source work / citation act / claim assertion / decision content / fixed record) is coherent and non-circular. Limits attach to the allocation candidate's object schema and to the fixture file, which contain errors that must be corrected before this checkpoint is filed as a research result.

## Critical findings

1. **A positive fixture is unsatisfiable under the declared bases.** `source-retraction` requires one retraction to reach two citations. With no source-work master, status can only be copied per citation, which is exactly the drift the packet's own holds identify. Reclassify as `conditional` (blocked on allocation), or the fixture asserts a capability the profile does not have.
2. **Dual authoring of fixity.** `contentDigest` is required on both `SourceExpression` and `RepresentationBinding`. This violates the profile's own constraint 15 ("every duplicate field has one authoring master"). Digest is a property of a fixed representation, not of an abstract expression; move it to `RepresentationBinding` and leave the expression with a non-authoritative reference.
3. **Ownership leakage in the invariant set.** Allocation invariants 3, 7 and 8 ("every citation pins…", "citation stance and verification remain owned by WM-KNW-008", "source status never establishes truth") constrain models the candidate explicitly excludes from owning. Restate as neighbor expectations; an aggregate may not carry invariants it cannot enforce.
4. **Required fields over-constrain the domain.** `SourceWork.authorityRef` required forces a fabricated authority for works with none (datasets, preprints, personal communications). `SourceExpression.contentDigest` required makes an unresolved or non-digital consulted expression unrepresentable, contradicting the packet's own "expression unresolved" allowance. `SourceStatusEvent.evidenceRef` required creates unbounded regress for the first notice.
5. **Status scoping is expression-only.** `SourceStatusEvent.sourceExpressionRef` cannot express work-level withdrawal or authority-wide retraction. Admit a work-or-expression target.
6. **Lifecycle mismatch.** `identityTest.independentLifecycle` lists eight states; `SourceWork.lifecycle` omits `corrected`, `preserved`, `disposed`. Reconcile, or state which layer owns preservation states.
7. **Fixture file is mis-scoped and redundant.** `shared-source` and `shared-source-distinct-locators` are the same case. Six cases (`rejected-alternative-reopened`, `adr-without-instrument`, `record-edits-decision`, `conflict-is-adjudication`, `erase-dissent`, `rewrite-after-retraction`) test profile behaviour, not allocation behaviour, yet sit in `vercy-model-allocation-fixtures/v1`. Split into profile and allocation sets.
8. **Coverage gaps.** No negative fixture for external-identifier collision (invariant 10), none for disposition preserving cited fixity (invariant 12), none for the unresolved-expression path.
9. **Unverifiable provenance in the Grok study.** "Lucas has not objected" attributes a review position to an unidentified party with no record reference. Strike or substitute a registered reviewer identity.

## Required holds

All eight profile holds and all six allocation holds stand unchanged. Add: fixture reclassification (finding 1); fixity single-master correction (2); invariant re-scoping (3); required-field relaxation (4); status-target widening (5); lifecycle reconciliation (6); fixture split and de-duplication (7–8); provenance correction (9). `publishableCanonical: false` remains correct on all four bases; the single-provider waiver remains displayable.

## Scenario result

Negative cases 4, 5, 9–13 are correctly rejected by the stated constraints. Positives 1, 3, 6, 7, 8 pass. Positive 2 does not pass as written — it passes only once the source-work aggregate exists.

## Identifier decisions

No profile ID; no runtime ID; `newRuntimeId: false` upheld. Evidence Artifact / Source Work remains `unassigned` with `modelId` and `registryId` null. No identifier guessed, reserved or implied here. No publication authority granted.
