# EM-WRK-02 local synthesis

## Disposition

- Reuse WM-ACT-005 as the Project aggregate. ProjectCharter is a serial, revisioned authorization artifact inside that aggregate.
- Split baseline responsibility without duplicating identity: WM-ACT-005 owns the approved, authority-bearing baseline package; WM-ACT-008 owns referenced plan/schedule content, forecasts, actuals and computation provenance.
- Reuse WM-ACT-031 for the discriminated Milestone / Deliverable / Acceptance record.
- Profile WM-ACT-032 as ProjectChangeRequest. WM-ACT-005 retains only the project-side request register projection and prior/resulting baseline linkage.
- Keep project-to-product and project-to-tracker-container relations many-to-many. A tracker container is tooling context and never automatically a business Project.
- Allocate no runtime or model identifier.

## Identity, mastership and lifecycle

The sponsoring organization's PPM system masters Project identity. WM-ACT-008 masters plan identity, versioning, schedule facts, forecasts and actuals. WM-ACT-031 masters milestone/deliverable identity, criteria and acceptance evidence. WM-ACT-032 masters a change request; the decision master remains externally referenced.

An approved baseline is immutable, digested, versioned and approval-time-stamped. It references plan/schedule components and its predecessor. Forecast values carry as-of time, method and confidence; actual values carry status date and source. Variance is invalid without a named baseline version. Derived dates carry a computation-run reference.

Acceptance records criteria version, verification method, accepting authority, decision time, conditions and evidence references. Approval of a change request does not edit or issue a baseline. It triggers WM-ACT-005 to establish a successor baseline referencing the request, predecessor and effectivity basis. Project closure records outcome, handover, benefit owner and residual obligations; it neither closes the product nor deletes open changes.

## Scenario

Projects P-A and P-B share tracker T and product X. Each work item resolves its own project, so T creates no merged Project identity. An approved change for P-A cites BL-1 and causes BL-2 to supersede it. BL-1 remains resolvable for the original promise and prior variance. Existing acceptance evidence stays pinned to its criteria version; only explicitly changed deliverables rebind. P-B and product X remain unaffected.

## Holds

Baseline ownership and change-register duplication require explicit edits; product/tracker and decision/parent relation rows are incomplete; WM-ACT-031 artifact identity and rollup rules need correction; WM-ACT-032 mapping/status extracts need re-scoping; criteria-version pins and shared-tracker/rebaseline fixtures are missing; two specifications retain single-provider waivers and external source pins remain incomplete. This dossier makes no canonical-completeness or publication claim.
