# Verdict

Reuse, do not create a new work-item model. **WorkItem is a tracker-facing profile over WM-ACT-006 Task**, not a sibling of it: WM-ACT-006 is already adjudicated `entry_kind: aggregate` with a consistency boundary drawn at "the task record plus the parts that have no independent identity outside it," and every candidate type in EM-WRK-01 either falls inside that boundary, resolves to an existing model, or is a container that must not be inside it. Disposition per candidate:

- **WorkItem** — profile over WM-ACT-006. No new identifier.
- **WorkItemType** — governed vocabulary, already `art-task-type-code-list`, versioned independently of the model. Jira types are crosswalk entries, not ontology.
- **WorkflowDefinition** — profile over WM-ACT-003 Process/Workflow (`definition.stateModel`), pinned by version; WM-ACT-006's `art-state-model-definition` is the per-type binding the instance cites.
- **Transition** — no independent identity. A permitted transition is part of the definition; an occurred transition is an entry on `art-state-transition-log`.
- **Backlog**, **Iteration** — independent record identity required (below); registry allocation deferred, no identifier invented here.
- **Estimate** — identified, revisioned assertion inside the Task aggregate; never merged with actual time.

# Evidence

WM-ACT-006 is `published` but `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, with six open publication holds. Its coverage declares **measurement a gap** (only percent-complete has primary support) and an adversarial check explicitly **rejected definition-of-done, story points, sprints and burndown as canonical structural nodes** for want of primary sources. That finding governs this contour: backlog and iteration are method-profile constructs, admissible as profile records, not as evidence-backed canonical structure. WM-ACT-003 is `described-previous-version` under `migration-boundary-review`; only its legacy K3 specification exists, and its objects (`process`, `state`, `stepExecution`, `deviation`) are the right shape for WorkflowDefinition but are not a current spec. WM-REC-006 is a `view-candidate` with no specification; prior research EM-PRD-03 resolved it to a Requirement aggregate with immutable revisions, which this review adopts by reference only.

# Identity/mastership

Tracker is master for work-item identity, native status and container membership. PPM is master for WM-ACT-005 Project and WM-ACT-029 Program/Portfolio identity, baseline and cost. Acceptance protocols are master for accepted outcomes and evidence. WM-ACT-006's identity priority rule already resolves the conflict: the producing tracker is the master system; its key is authoritative and the imported record carries source keys as business identifiers. Requirement/value intent is mastered by WM-REC-006, never by the tracker.

# Work item/type

One WorkItem record kind, discriminated by WorkItemType code with its code system and version — not by subclassing. Container behaviour (Epic, Feature, Initiative) is a property of the type's declared role plus `de-part-of` edges, not a distinct entity. Priority carries its scale identifier (mandatory per WM-ACT-006 policy; four incompatible scales are recorded as a conflict). Local Jira types enter as crosswalk rows with loss notes, never overwriting the governed vocabulary.

# Workflow/transition/outcome

Three separable things, currently conflated by every tracker:

1. **Native status** — source workflow status value, retained verbatim with the pinned workflow definition version and source resolution code. Never overwritten by a canonical code.
2. **Canonical state** — WM-ACT-006 `de-status` against the pinned state-model version, plus `de-business-status` for nuance the canonical vocabulary deliberately does not encode.
3. **Normalized outcome** — a separate, evidence-bearing assertion: `done` (completion criteria met, performer claim), `accepted` (acceptance record by an authority distinct from the performer, citing criteria version and evidence digests), `cancelled` (stopped externally, no result claimed), `rejected` (result assessed and refused, or refused before performance — the two are distinguished by whether an execution period exists).

The negative case fails on this separation: `Closed` is a workflow sink, not an outcome. `Closed/Won't Do`, `Closed/Declined` and `Closed/Fixed` share one status and carry three different outcomes; absence of an acceptance record is never acceptance.

# Backlog/iteration

Both need independent record identity, outside the Task consistency boundary, because each is shared by many work items, has its own lifecycle, revisions and mastership, and carries assertions that are false if attributed to a single task. Backlog owns ordered, revisioned membership (rank is a property of the backlog revision, never of the item, and is never an identifier). Iteration owns a time box, capacity, commitment set at close of planning, and a closure record; membership changes after commitment are recorded as scope-change entries, not silent edits. Neither may be modelled as a task attribute; both require registry allocation and source grounding before publication.

# Estimate/time

Estimate is an assertion: `{value, unit or scale, basis, estimator, method, effective time, revision}`, scoped to one work-item revision, append-only — re-estimation supersedes, never overwrites. Actual effort and time records stay in a sibling effort/cost master and are referenced. WM-ACT-006 declares effort accounting a gap, so no estimate-to-actual variance semantics may be asserted as canonical. Velocity and capacity are computed views over closed iterations, storing no new facts.

# Epic/feature/requirement/project

Test of authority, not of label. If a record's authority is **delivery decomposition** — it exists to group and sequence work, its lifecycle is workflow status, its closure is a delivery event — it is a WorkItem container. If its authority is **verifiable intent** — it states what must hold, carries acceptance criteria, baseline membership and verification — it is WM-REC-006. Both may exist for the same intent and are linked by a reified, revision-pinned trace link; neither is derived from the other, and Done on the container proves nothing about requirement satisfaction. A tracker project, board or epic tree is a tooling container and becomes a WM-ACT-005 Project or WM-ACT-029 Program/Portfolio node only when it resolves to an authoritative identifier from those masters.

# Import and acceptance

Import key = `{source system, source container, source item id}` recorded as business identifiers; an idempotency key per import batch; source revision token or sequence orders updates. Upsert on the correlation key: an already-correlated item is updated, never re-minted; transitions append only when the source revision advances; stale and duplicate submissions are logged as rejected updates. Updates arriving for terminal records are annotated, not applied. Acceptance requires an acceptance record citing the criteria version, the accepting party, evidence items with digests, and the decision time; `accepted` is never inferred from status, resolution, closure date or an empty comment field.

# Scenario

Tracker A `{Open, In Progress, Closed}` × resolutions `{Fixed, Won't Do, Declined}` migrates to tracker B `{To Do, Doing, Done, Rejected, Cancelled}`. Native statuses and resolutions from A are retained with A's pinned workflow version; canonical state and normalized outcome are recomputed from evidence, not from names. `Closed/Fixed` with an acceptance record → `accepted`; `Closed/Fixed` without one → `done`, not accepted; `Closed/Won't Do` → `cancelled`; `Closed/Declined` with no execution period → `rejected`. All three remain distinct in B and survive a return projection through the crosswalk. Second import of the same export: every item matches on its correlation key, zero new identities, zero new transition entries, one skipped-duplicate audit entry per item.

# Invariants

1. Closed is not an outcome; `accepted` requires an acceptance record with evidence.
2. Native status and resolution are preserved alongside canonical state; neither is overwritten.
3. `cancelled`, `rejected`, `done` and `accepted` are separately asserted and separately queryable.
4. A tracker container is not a project or program until it resolves to a WM-ACT-005 or WM-ACT-029 identifier.
5. Estimate never functions as, nor is overwritten by, actual effort.
6. Backlog rank is a backlog-revision property and is never an identifier.
7. Iteration commitment is sealed at planning close; later membership change is a recorded scope change.
8. Import is idempotent on the correlation key; re-import mints no identity and appends no duplicate transition.
9. Work-item closure proves nothing about requirement satisfaction.
10. Every priority and estimate value carries its scale identifier.
11. Every state, assignment, estimate and outcome change records actor, reason, event time and recording time.

# Minimal completion shape

WM-ACT-006 profile adding: native status + source workflow version + source resolution; normalized outcome with evidence references; work-item type binding with container role; correlation identifier set and import idempotency key; estimate assertion series. WM-ACT-003 profile for WorkflowDefinition and its permitted transitions, pinned per version. Two deferred records for Backlog and Iteration pending registry allocation. Reference edges to WM-REC-006 (trace link), WM-ACT-005 and WM-ACT-029 (container resolution).

# Holds

WM-ACT-006 remains non-canonical with six unresolved publication holds (source verification, citation provenance, multi-profile validation, retention, conformance, source remapping); WM-ACT-003 has no current specification and an open migration boundary; WM-REC-006 has no specification and its view classification conflicts with the reference identity this contour needs; WM-ACT-029 relation rows are unapproved and WM-ACT-005 is a previous-version description. Backlog, Iteration and the normalized-outcome vocabulary have no primary source grounding and no allocated identifiers; crosswalk fixtures, round-trip tests and the two-workflow migration above are unexecuted design assertions. Boundary decision remains pending; no canonical completeness, publication readiness or installability is claimed.
