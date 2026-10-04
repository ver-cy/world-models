# EM-WRK-02 local synthesis

## Disposition

- Reuse WM-ACT-005 as the Project aggregate. ProjectCharter is a serial, revisioned authorization artifact inside that aggregate.
- Split baseline responsibility without duplicating identity: WM-ACT-005 owns the approved, authority-bearing baseline package; WM-ACT-008 owns referenced plan/schedule content, forecasts, actuals and computation provenance.
- Reuse WM-ACT-031 as the shared aggregate for discriminated Milestone, Deliverable and Acceptance records. Acceptance remains a separate immutable record inside that aggregate, not the same identity row as a milestone or deliverable.
- Profile WM-ACT-032 as ProjectChangeRequest. WM-ACT-005 retains only the project-side request register projection and prior/resulting baseline linkage.
- Keep project-to-product and project-to-tracker-container relations many-to-many. A tracker container is tooling context and never automatically a business Project.
- Allocate no runtime or model identifier.

## Identity, mastership and lifecycle

The sponsoring organization's PPM system masters Project identity. WM-ACT-008 masters plan identity, versioning, schedule facts, forecasts and actuals. WM-ACT-031 masters milestone/deliverable identity, criteria and acceptance evidence. WM-ACT-032 masters a change request; the decision master remains externally referenced.

An approved baseline is a project-scoped sub-entity: immutable, digested, versioned and approval-time-stamped. It pins immutable WM-ACT-008 revisions. Any embedded snapshot is a non-authoritative copy with source revision and digest. The draft package owns the frozen selection record; the governed transition freezes the selection, creates one complete atomic package across its declared scope/schedule/cost dimensions and switches the current pointer without rewriting the predecessor. A partial rebaseline creates a complete successor package that reuses unchanged pins. Forecast values carry as-of time, method and confidence; actual values carry status date and source. Variance is invalid without a named baseline-package identifier and reads only its pinned revisions. Derived dates carry a computation-run reference.

WM-ACT-031 gives Milestone, Deliverable and Acceptance independent record identities and revision series inside one aggregate. It masters criteria revisions with the relevant milestone or deliverable. Acceptance is an immutable record distinct from that subject and pins object revision, criteria revision, baseline package, verification method, accepting authority, decision time, conditions and evidence references. Milestone achievement requires its own status, effective time, authority and evidence; task completion is insufficient. Approval of a change request does not edit or issue a baseline. Only an approved rebaseline-class request triggers WM-ACT-005 to establish a successor package referencing the request, predecessor and effectivity basis. Re-baselining does not reopen acceptance unless the approved request contains an explicit impact assertion. Project closure records outcome, handover, benefit owner and residual obligations; it neither closes the product nor deletes open changes.

## Scenario

Projects P-A and P-B share tracker T and product X. Each work item resolves its own project, so T creates no merged Project identity. An approved change for P-A cites BL-1 and causes BL-2 to supersede it. BL-1 remains resolvable for the original promise and prior variance. Existing acceptance evidence stays pinned to its criteria version; only explicitly changed deliverables rebind. P-B and product X remain unaffected.

## Holds

Baseline ownership, transition atomicity, atomic package grain and change-register duplication require explicit base adoption; product/tracker and decision/parent relation rows are incomplete; WM-ACT-031 record identity, independent revision series, disjoint relation sets and rollup rules need correction; WM-ACT-032 mapping/status extracts need re-scoping; canonical base fixtures do not yet exercise immutable plan pins or shared-tracker re-baselining; external source pins remain incomplete. Claude and Grok evidence is preserved with their disagreement resolved only at aggregate/record granularity. The frozen no-tools audit accepted this held profile with limits and confirmed `newRuntimeId=false`. This dossier makes no canonical-completeness or installability claim.
