# Frozen semantic audit — EM-DAT-05 (Metric Definition)

**Verdict: REVISE.** Boundary is sound; two internal contradictions and several fail-open requireds must close first. Revision needs no boundary change and the draft stays reviewable.

**Critical findings**

1. *Identity contradiction.* Fixture `method-and-population-change` keeps one Metric across headcount→FTE, but invariant 14 and fixture `headcount-plus-fte` treat quantity-kind/statistical-unit change as re-identification. Add a written re-identification test (phenomenon + quantity kind + statistical unit) and reclassify the fixture; local evidence repeats the same conflation.
2. *Immutability leak.* `PopulationBoundary.effectiveFrom/effectiveTo` and mutable `DimensionRule` give referenced children their own time axis, so population or additivity can change under a pinned active version — contradicting invariants 2 and 10. Require version-pinned child references covered by `contentDigest`, or freeze children at activation.
3. *Fail-open requireds.* `methodRefs`, `sourceRefs`, `dimensions` are optional while invariant 8 and both studies require method/source binding before activation; declared-additivity is unenforceable when `dimensions` is absent. `quantityKind`, `scale`, `comparisonDirection` appear in `boundary.owns` but in no object, leaving invariant 14 and unit-commensurability with nothing to bind. No precision/rounding field: a reported-value-changing rounding change escapes versioning and comparability.
4. *Missing conditional requirement.* `comparable-with-restatement` does not require `restatementMethodRef`/`evidenceRefs`, so fixture `explicit-restatement` cannot be satisfied fail-closed. `dimensionRef` lacks a code-list version pin though units and methods are pinned.
5. *Enforcement sits outside the boundary.* `invalid-aggregation` and `target-version-pin` refusals execute in WM-DAT-010 and WM-KNW-011. State them as declared consumer obligations with conformance points; otherwise the fixtures assert authority the candidate does not own.
6. *Policy / second-authority scan.* Clean of thresholds, SLO budgets, calendars, scorecard weights and incentives. Two risks: `DimensionRule.aggregationPolicy` must be narrowed to commensurability semantics, not local rollup preference; `ComparabilityDeclaration.authorityRef` must reference external governance, not host an approval workflow. Add explicit excludes for organisation-specific KPI policy.
7. *Fixture gaps.* No case for equal-authority conflict (inv. 16), facet narrowing-but-never-widening (inv. 13), quantity-kind re-identification (inv. 14), or resolvability of withdrawn/tombstoned versions (inv. 17).

**Required holds**

- Registry allocation pending; no numeric gap may be inferred.
- Neighbour publication holds stand; all five neighbours are drafts under single-provider waivers with unfrozen relation rows, so their exclusions are declared, not enforceable.
- WM-DAT-007 and WM-DAT-010 admitted no external review.
- WM-XCT-025's open aggregate-root/identity question destabilises the result-field reference.
- WM-KNW-011's unassigned measure-definition reference must resolve to this entry.
- Standards pins unverified under live-source holds; the gap rests on `catalogueSearchFinding` alone, no negative-search log.
- Package conversion and live verification pending; two-provider boundary review required (no waiver).
- Discharged within this packet: "independent Grok review pending" and "one frozen semantic audit pending".

**Scenario result:** 6 of 9 pass as specified. `method-and-population-change` fails on finding 1. `explicit-restatement` is indeterminate on finding 4. `target-version-pin` passes only via default non-comparability once the consumer obligation of finding 5 is stated. `invalid-aggregation` and `headcount-plus-fte` pass semantically but depend on external enforcement.

**Identifier decision:** none. `modelId` and `registryId` remain null, `allocationState` unassigned, `canonicalPublishable` false. Carry forward as an identifier-unassigned reviewable draft (`0.1.0-candidate.3`). No publication authority granted.
