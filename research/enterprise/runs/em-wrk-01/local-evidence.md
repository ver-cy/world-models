# EM-WRK-01 local synthesis

## Disposition

- Define WorkItem as a tracker-facing profile over WM-ACT-006 Task. Jira and other tracker issue types remain adapter mappings.
- Use a governed, versioned WorkItemType vocabulary rather than separate entity subclasses.
- Profile WM-ACT-003 Process / Workflow for WorkflowDefinition. Permitted transitions belong to the definition; occurred transitions are append-only task history entries.
- Give **Backlog** and **Iteration** independent identities and lifecycles outside the Task aggregate. Both remain identifier-unassigned candidates.
- Keep Estimate as an identified, revisioned assertion inside Task. Actual effort and elapsed time stay in their own source masters.
- Reference WM-REC-006 for requirement/value intent, WM-ACT-005 for Project and WM-ACT-029 for Program/Portfolio.
- Allocate no runtime or model identifier.

## Identity and mastership

The producing tracker masters WorkItem identity, native status and tracker-container membership. Its stable correlation key is source system, source container and source item ID. PPM masters project/program identities and baselines. Requirement management masters verifiable intent and acceptance criteria. Acceptance protocols master acceptance decisions and evidence.

Epic, Feature and Initiative are WorkItem container roles when their authority is delivery decomposition and workflow. A record is a Requirement when it states verifiable intent, owns criteria and baseline membership. A tracker project, board or epic tree becomes a Project/Program reference only after resolving to those authoritative masters.

## Workflow and outcomes

Each WorkItem retains three separate layers:

1. native source status/resolution with pinned workflow version;
2. canonical task state plus optional business-status nuance;
3. evidence-bearing normalized outcome: done, accepted, cancelled or rejected.

Closed is only a workflow state. `accepted` requires an explicit acceptance record naming criteria version, accepting authority, evidence digests and decision time. Cancellation claims no delivered result. Rejection remains distinct and records whether execution occurred.

## Backlog, iteration and estimate

Backlog owns an ordered, revisioned membership set. Rank belongs to one backlog revision and is never WorkItem identity. Iteration owns its time box, capacity, planning-close commitment and closure record. Membership changes after planning close become scope-change records.

Estimate carries value, unit/scale, basis, method, estimator, effective time and revision. Re-estimation supersedes without overwriting. Actual effort never overwrites estimate; velocity and capacity are derived views.

## Idempotent import scenario

Tracker A statuses and resolution values map into Tracker B while preserving the original workflow version. Closed/Fixed with acceptance evidence maps to accepted; without evidence it maps to done. Closed/Won't Do maps to cancelled; Closed/Declined maps to rejected. Re-import upserts by the source correlation key, rejects stale revisions and appends no duplicate transition or identity.

## Invariants

1. Closed is not an outcome; accepted requires evidence.
2. Native status/resolution remain alongside canonical state.
3. Cancelled, rejected, done and accepted remain distinct.
4. Tracker containers are not projects/programs without authoritative resolution.
5. Estimate is never actual effort.
6. Backlog rank belongs to a backlog revision.
7. Iteration commitment is sealed at planning close; later change is explicit.
8. Re-import is idempotent on the source correlation key.
9. WorkItem closure does not prove Requirement satisfaction.
10. Priority and estimate values name their scales.
11. State, assignment, estimate and outcome changes record actor, reason, event time and recording time.

## Holds

WM-ACT-006 retains noncanonical source, profile and retention holds; WM-ACT-003 lacks a current specification; WM-REC-006 lacks a verified specification and has a view-classification conflict; WM-ACT-005/029 relation maturity is incomplete; Backlog and Iteration lack registry allocation; normalized-outcome sources, crosswalk fixtures and round-trip migration tests are incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
