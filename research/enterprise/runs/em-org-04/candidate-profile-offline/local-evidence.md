# EM-ORG-04 local synthesis

## Disposition

- Create a narrow Enterprise profile over WM-ORG-002 Organizational Unit.
- Do not create another unit model or runtime ID.
- Add scenario-qualified structural placements and enforce rules that the current draft leaves as questions.

## Identity and boundary

OrganizationalUnit has a stable parent-scoped identifier and lifecycle independent of its name, mandate and placement. Rename and reparent preserve identity. Merge, split and disband create explicit lineage through a reorganization act.

UnitType is a versioned classification assignment. UnitMandate is a temporal assignment keyed by unit, governing instrument and validity interval. StructuralPlacement is a reified edge keyed by child, parent, axis, scenario and validity interval. None requires independent model identity.

A cross-functional team or community is a collective with affiliations to units. It is not forced into the administrative hierarchy and does not become a unit merely to render an org chart.

## Placement contract

Administrative, functional, legal, cost and reporting axes coexist as separately governed edge sets. The unit-level unqualified `parentUnitRef` must not serve as a second write path. Every placement declares axis, scenario, validity and evidence.

Asserted current, historical replay, approved future and hypothetical scenario are distinct states. Approved future placement may use future effective time. Hypothetical structures require an explicit scenario/branch and must remain excluded from authoritative reads until adopted.

## Invariants

1. Placement is always axis-, scenario- and interval-qualified.
2. At most one parent applies per child, axis, scenario and instant where the axis requires a tree.
3. Acyclicity is validated independently per axis, scenario and interval.
4. Rename and reparent preserve unit identity.
5. Merge, split and disband require lineage plus a reorganization act.
6. Management placement never determines employer or legal entity.
7. Collaboration/team typing excludes administrative parent placement.
8. Scenario placements never enter asserted-current projections before adoption.
9. Mandate is independent of structural parent and retains its own interval and evidence.

## Scenario result

The negative case is rejected: a cross-department product team keeps affiliations to contributing units rather than receiving an invented administrative parent. In the accepted reorganization, old placements remain available for as-of replay, approved future placements open new intervals, and acyclicity is checked on the selected axis. Hypothetical to-be options require the new scenario qualifier and cannot contaminate the current graph.

## Holds

WM-ORG-002 remains non-canonical. Hypothetical scenario semantics and scenario-aware query parameters are absent from the base. Unit/site and finance-axis boundaries remain deferred; unit-grain staffing evidence is extension-grade; source/version checks and several organizational forms are unvalidated. This checkpoint is a profile boundary, not an installable release.


## Provider reconciliation and frozen audit

Grok confirmed PROFILE/no new ID and sharpened axis, scenario and team boundaries. The single frozen Claude audit returned REVISE because current base text lacks the scenario and mandate deltas and contains relation/cardinality conflicts. Revision 3 applies the checklist once, strikes out-of-dossier identifiers and keeps every base amendment and unexecuted fixture as a publication blocker.
