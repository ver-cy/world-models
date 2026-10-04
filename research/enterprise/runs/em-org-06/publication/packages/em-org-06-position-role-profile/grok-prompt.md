# Independent review request: EM-ORG-06 Positions, Roles and Accountability

Review this Enterprise boundary independently using public organization/post, workforce planning, RACI, delegation and authorization practice where useful. Separate standards evidence from design inference. Do not invent a Vercy identifier.

WM-ORG-004 Position and WM-XCT-023 Party Role are non-canonical reviewable drafts.

Proposed boundary: reuse WM-ORG-004 for durable vacant positions; profile WM-XCT-023 for Accountability, held Decision Rights and RACI. BusinessRole is a versioned concept scheme whose identifier remains unassigned. HeadcountPlan is a separate planning candidate with identifier unassigned; position FTE/budget are projections from an approved plan.

Position owns seat identity, unit placement, job/grade refs, authorized capacity/budget and seat-level authority. Occupancy is external. PartyRole connects a party or position to a host using a role concept, scope, validity, authority and constraints. IAM roles/grants remain external; PartyRole may only be policy input.

Test rules: vacant seat remains valid; occupant changes do not alter seat identity; vacancy is derived; RACI pins host, role, player/position, period and conflict policy; one Accountable and at least one Responsible per host/period; segregation exceptions are explicit and temporary; pooled positions may support fractional occupancy only within capacity.

Negative case: deleting an employee deletes the seat and budget. Acceptance: occupant change preserves position; one person holds two roles; two 0.5 FTE assignments fill one allowed pooled seat.

Return at most 1000 words with: Verdict per type; position/occupancy boundary; role concept/assertion boundary; accountability/RACI rules; IAM distinction; headcount-plan test; scenario results; required relations; publication blockers.
