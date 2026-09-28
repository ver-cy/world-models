# Frozen semantic audit — EM-FAC-01

## Verdict
**ACCEPT WITH LIMITS.** The composed boundary is semantically sound: identity, containment, designation, allocation, lease, access, booking and employment are separated with distinct authorities. Nine defects must be closed before allocation or canonical publication; none invalidates the composition.

## Critical findings
1. **Dual containment representation.** `SpatialUnit.parentRef` is required *and* `ContainmentAssertion` owns effective-dated parentage. Two sources of truth; a mutable required `parentRef` contradicts "re-parenting changes containment evidence and does not mint identity." Make parentage assertion-only, or declare `parentRef` a derived as-of projection.
2. **Missing containment invariants.** Acyclicity is stated, but there is no non-overlap rule for concurrent parents below the top level, and no rule that a child extent may not exceed its parent extent. Both were present in local evidence and are lost.
3. **Out-of-boundary assertions.** The facility-without-site, building-without-facility and gazetteer-not-container invariants and fixtures are asserted by a model that delegates site and facility identity and declares no relation to WM-BLT-006 or WM-BLT-008. Unenforceable here; relocate to the composition profile.
4. **Designation authority collapsed.** `UseDesignation` carries one `useClass` plus one `authorityRef`, merging code occupancy (authority having jurisdiction) with operational designation (facility management). This permits single-role cross-assertion. Add a designation basis/authority kind.
5. **WM-PLC-009 retirement is semantically safe but not yet record-safe.** The profile preserves a *name* only: no adjacency, connectivity, traversal or indoor-positioning objects, no alias redirect, no inbound relation-retargeting ledger. Risk is silent loss of topology, not duplication.
6. **Allocation root/version duplication.** `locus` and `workplaceKind` are required on both `WorkplaceAllocation` and `AllocationVersion` while the identity test says locus change creates a version. Lifecycle also mismatches: `superseded` appears in `independentLifecycle` and `successorRef` exists, but not in the object lifecycle.
7. **LocusChoice under-constrained.** No invariant binds `locusKind` to the populated `oneOf` field; `mobileRegionRef` names no referenced master; no granularity ceiling field exists for home or mobile loci.
8. **Fail-open defaults.** `disclosureClass` and `exclusivity` are optional with no declared default, so non-public-by-default and "pooled is not a reservation" are prose-only. The single-primary rule cites a "named profile" with no profile reference field.
9. **Reference label hazard.** WM-ORG-016 is labelled "Position or work assignment context," conflating two distinct masters in the supplied evidence. Verify against pinned registry sources; no identifier is asserted here.

## Required holds
Blocking canonical publication and identifier allocation: registry mutation; Workplace Allocation namespace and identifier assignment; WM-PLC-009 retirement and relation retargeting; data-protection and employment-law review in a non-US jurisdiction; IFC, IndoorGML, area-standard and Facility/Building crosswalk source pinning; WM-BLT-002 migration packaging from 0.2.0-legacy; package conversion and live verification. Permitting reviewable draft only: findings 1–9, with 5, 7 and 8 also blocking any operational or derived-directory use.

## Scenario result
Pass: leased-office, address-change, office-to-lab, reparent-no-reidentify, indoor-space-duplicate, leased-hybrid-office, client-site, client-site-branch, mobile-work, allocation-grants-access, endpoint-split. Pass with limits: unit-split (no invariant retires predecessors at `effectiveAt`); facility-without-site, building-without-facility, gazetteer-not-container (asserted outside this boundary); home-work-privacy and remote-home (no granularity field); desk-booking (exclusivity optional); double-primary (no profile reference). No fixture fails closed incorrectly; no negative case passes.

## Identifier decisions
WM-BLT-002 completion accepted as reviewable candidate, `canonicalPublishable: false`. WM-PLC-009 retirement remains a proposal; no mutation approved. Workplace Allocation remains identifier-unassigned NEW MODEL; no namespace proposed. Office Use and Indoor Topology remains a profile with no runtime identifier.
