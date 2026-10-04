# EM-FAC-01 local synthesis

## Disposition

EM-FAC-01 is a composed landscape with two missing pieces:

1. **complete reserved WM-BLT-002 Premises / Spatial Unit** as the single interior-space authority;
2. research a separate **Workplace Allocation relationship** whose identifier remains unassigned.

Reuse WM-PLC-010 Gazetteer Place, WM-BLT-008 Site / Campus, WM-BLT-006 Facility and WM-BLT-001 Building / Structure. Treat `office` as an effective-dated use/designation profile, not a new physical object or legal branch.

## Duplicate resolution

WM-PLC-009 Indoor Space overlaps the same bounded interior extent as WM-BLT-002. WM-BLT-002 has stronger inbound evidence: WM-BLT-001 contains it, WM-OBJ-001 names it as premises identity/geometry master, and WM-BLT-006 explicitly delegates room and space semantics to a space model.

Proposed registry action: retire WM-PLC-009 as a standalone candidate and preserve indoor navigation/topology as a profile of WM-BLT-002. This remains a proposal pending independent review and relation-ledger audit.

## Physical containment spine

`Gazetteer Place <- Site/Campus -> Facility -> Building/Structure -> Premises/Spatial Unit`, with recursive premises containment where appropriate. Address, legal branch, lease, ownership, employment, access grant, booking and person identity remain external.

## WM-BLT-002 minimum boundary

The model owns persistent spatial-unit identity, parent containment with validity, kind, designator, geometry reference, measured area evidence, design capacity, separately-governed status, control/occupancy role references, effective-dated use designations and split/merge lineage.

Address, room number, current occupier and use designation never define identity. Re-parenting does not mint identity. Split and merge do.

## Workplace Allocation candidate

An allocation relates an employment or engagement context to a physical or external locus for a validity window. It needs its own identity because one engagement may have concurrent allocations, remote/mobile/client-site loci may have no premises record, and allocation survives changes to either endpoint.

Portable fields: subject-context reference, locus choice, workplace kind, exclusivity/pooled status, validity and recurrence, approving authority, purpose, primary-location flag, disclosure class and status.

The identifier is deliberately unassigned. Claude proposed `WM-WPL-001`, but no WPL namespace exists in the registry; allocation must follow the registry process.

## Privacy and authority invariants

- A home address never becomes a company office, premises record or public fact merely because work occurs there.
- Remote-home allocation stores at most an appropriate jurisdiction/generalized place reference.
- Workplace allocation never grants physical or logical access automatically.
- A legal branch references a location; location designation never creates a branch.
- Lease and licence terms remain agreement records.
- Desk reservations remain booking records; pooled entitlement is an allocation.
- At most one primary work location is effective per subject context and period unless a declared profile allows multiple primaries.

## Holds

WM-BLT-002 now has a reviewable completion candidate with persistent identity, temporal containment, boundary and area evidence, use designations, split/merge lineage, four external relation contracts and seven fixtures. The previous description still requires migration packaging. IFC host/version differences, Facility/Building crosswalk, indoor topology sources, area standards, privacy review, WM-PLC-009 retirement and Workplace Allocation allocation remain unresolved. Exact Grok comparison, one frozen semantic audit, package conversion and live verification are still required.
