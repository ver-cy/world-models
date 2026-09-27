# EM-ORG-06 local synthesis

## Disposition

- Reuse WM-ORG-004 as the durable Position master.
- Profile WM-XCT-023 Party Role for Accountability, held Decision Rights and RACI assignments.
- Complete a governed BusinessRole concept scheme only after registry allocation; identifier remains unassigned.
- Keep HeadcountPlan as an identifier-unassigned candidate pending independent evidence. Create no runtime/model ID now.

## Boundary

Position is a vacant-capable organizational seat. It owns stable identity, unit placement, job/grade references, authorized FTE/headcount, seat budget, requirements and seat-level delegated authority. Occupancy is a separate relationship master; employee removal changes occupancy and open capacity, never the position or budget.

BusinessRole is a versioned concept. PartyRole is an addressable, time-bounded assertion connecting a player or position to a host under a role concept. Positions may bind abstract roles, and PartyRole supports roles with no position. Occupation, job family, grade and skill taxonomies remain external classifiers.

Accountability and RACI are PartyRole profiles. Seat-durable responsibility may be attached to WM-ORG-004; the assertion of who currently bears it uses WM-XCT-023. Decision rights describe real-world representation limits; IAM roles and grants remain external technical authorization facts.

HeadcountPlan is not intrinsic seat capacity: it aggregates units and fiscal periods and precedes seat establishment. Position budget/FTE fields are approved-plan projections.

## Invariants

1. A position exists while vacant and survives occupant change.
2. Vacancy is derived from authorized capacity and occupancy.
3. Occupancy termination cannot delete position, FTE or budget.
4. Role types declare scheme, version and axis.
5. PartyRole assertions grant no IAM permissions.
6. RACI identifies host/context, role type, player or position, validity and conflict policy.
7. One Accountable and at least one Responsible apply per host and interval unless a profile explicitly states another rule.
8. Segregation conflicts require an explicit, time-limited exception.
9. Fractional occupancies may share a pooled seat only when their effective sum respects capacity.

## Scenario result

Deleting an employee ends occupancy and opens capacity while the seat, budget and authorized FTE remain. A successor occupies the same position. One person can hold two independently scoped role assertions. Two 0.5-FTE occupancies can fill a 1.0-FTE pooled position under a declared job-share profile and overlap policy.

## Holds

Both bases remain non-canonical. Occupancy model WM-ORG-016 and candidate relations are outside the dossier. No allocated BusinessRole vocabulary model exists, HeadcountPlan lacks evidence, and job-share fractions/RACI vocabularies lack primary-source fixtures. Source and profile validation holds remain open. This checkpoint is not an installable release.
