# EM-WRK-02 local synthesis

## Disposition

- Reuse WM-ACT-005 as the Project aggregate. ProjectCharter is a serial, revisioned authorization artifact inside that aggregate.
- Split baseline responsibility without duplicating identity: WM-ACT-005 owns the approved, authority-bearing baseline package; WM-ACT-008 owns referenced plan/schedule content, forecasts, actuals and computation provenance.
- Reuse WM-ACT-031 for the discriminated Milestone / Deliverable / Acceptance record.
- Profile WM-ACT-032 as ProjectChangeRequest. WM-ACT-005 retains only the project-side request register projection and prior/resulting baseline linkage.
- Keep project-to-product and project-to-tracker-container relations many-to-many. A tracker container is tooling context and never automatically a business Project.
- Allocate no runtime or model identifier.

## Identity and mastership

The sponsoring organization's PPM system masters Project identity. WM-ACT-008 masters plan identity, versioning, schedule facts, forecasts and actuals. WM-ACT-031 masters milestone/deliverable identity, criteria and acceptance evidence. WM-ACT-032 masters a change request; the decision master remains externally referenced.

A Project boundary is established by an authorization instrument, a declared scope with exclusions/assumptions and a temporal frame. Delivery method, phase structure, gate set and WBS are optional profiles and do not create project identity. A charter revision is superseded, never overwritten; a change requiring a new project identity uses explicit succession.

## Plan, baseline, forecast and actual

The approved baseline is immutable, digested, versioned and approval-time-stamped. It contains referenced plan/schedule components and records its predecessor. Forecast values carry as-of time, method and confidence. Actual values carry status date and source. Variance is invalid without a named baseline version. Derived dates carry a computation-run reference.

WM-ACT-031 projects baseline, forecast and actual for its own milestone/deliverable without creating another baseline master.

## Milestone, deliverable and acceptance

WM-ACT-031 keeps one discriminated union for milestone, deliverable and deliverable-linked milestone. Achievement, schedule and submission statuses stay independent. A milestone is not a completed task.

Acceptance records criteria version, verification method, accepting authority, decision time, conditions and evidence references. Project-level scope confirmation aggregates accepted deliverables but is not a second acceptance decision.

## Change request and lifecycle

WM-ACT-032 records the request, affected baseline/items, proposed delta, impact/risk assessment, routing and externally resolved disposition. Approval does not edit or issue a baseline. It triggers WM-ACT-005 to establish a successor baseline referencing the request, predecessor and effectivity basis. Reversal is a new decision/outcome.

Project closure records outcome, handover, benefit owner and residual obligations. It neither closes the product nor deletes open changes; those must be dispositioned or transferred.

## Acceptance scenario

Projects P-A and P-B share tracker container T and product X. Each work item resolves its own project, so T creates no merged Project identity. An approved change request for P-A cites BL-1 and causes BL-2 to supersede it. BL-1 remains resolvable for the original promise and prior variance. Existing acceptance evidence remains pinned to the criteria version under which it was decided; only explicitly changed deliverables rebind. P-B and product X remain unaffected.

## Invariants

1. A Project may use many tracker containers; a tracker container is not Project identity.
2. A milestone is not a completed task.
3. Project closure does not close a product.
4. Approved baselines are immutable; variance names a baseline version.
5. Forecast, baseline and actual remain distinct.
6. Derived values record computation provenance.
7. Approved change requests trigger successor baselines but never issue them directly.
8. Acceptance requires criteria version, authority and evidence.
9. Earlier acceptance bases survive re-baselining.
10. Project-product and project-tracker relations are many-to-many.
11. Cost is asserted once and view allocations are deduplicated.
12. Charters, baselines, assessments and dispositions are superseded, not overwritten.
13. Names, dates and periods are not identifiers.

## Holds

Baseline ownership and change-register duplication require explicit edits; product/tracker and decision/parent relation rows are incomplete; WM-ACT-031 artifact identity and rollup rules need correction; WM-ACT-032 mapping/status extracts need re-scoping; criteria-version pins and shared-tracker/rebaseline fixtures are missing; two specifications retain single-provider waivers and external source pins remain incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
