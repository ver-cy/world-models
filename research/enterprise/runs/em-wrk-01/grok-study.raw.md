# Grok independent review — EM-WRK-01

Source conversation: https://grok.com/c/78ffb803-8e50-4e71-b87d-49005ed09146

Two earlier attempts failed without a semantic answer. After fresh user confirmation, the third exact retry completed successfully. Only the successful third response is synthesized below; the earlier failures remain recorded in the manifest attempt count.

## Verdict

Conditional accept of a WorkItem profile over WM-ACT-006. Do not mint identifiers or claim completeness. WorkItemType is a governed versioned vocabulary. Estimate remains a revisioned Task assertion and actual effort remains external. Backlog and Iteration stay identifier-unassigned, but current evidence does not prove that either needs independent catalogue identity.

## Identity and mastership

WorkItem reuses WM-ACT-006 identity. The tracker-of-record native key is the source correlation key; other tracker keys are aliases with originating, master or mirror roles. Title, sequence, board column, parent and container membership are not identity. Tracker fields, canonical mappings, outcome assertions and acceptance authority retain distinct masters; equal-authority conflicts are preserved rather than overwritten.

## Type, workflow and outcomes

Executable tracker kinds may profile Task; grouping kinds remain adapter classifications until requirement and product-grouping semantics are complete. WorkItemType binds by scheme, version and code. A type change is a classified revision, not a new WorkItem.

Permitted transitions belong to a versioned lifecycle definition while occurred transitions remain append-only Task history. Transition receives no standalone identifier. WM-ACT-003 is an unspecified catalogue stub and collides with EM-OPS-01. Tracker state machines should bind to WM-XCT-021; WM-ACT-003 remains a later alignment only for process-shaped definitions. Native status, canonical state and evidence-bearing outcome are distinct. Closed is not accepted; Task completion is neither Project acceptance nor program-benefit realization.

## Backlog, iteration, estimate and external boundaries

Backlog can be an ordered selection under product/team/project scope. Iteration can be a timeboxed plan interval with membership and goal. Tool container identifiers remain correlation aliases. Independent identity should be reconsidered only if irreducible mastered facts survive deletion of all members and are not already owned by Product, Team, WM-ACT-008 Plan or WM-ACT-005 Project. A mandatory Iteration identity would fail Kanban and continuous-flow profiles.

Estimate records method, unit, scale, asserter and effectivity as a Task assertion. Consumed effort is a separate measurement series; no universal points-to-hours conversion exists. Epic and Feature are adapter WorkItemType codes unless an external authoritative boundary resolves them. WM-REC-006 Requirement, WM-ACT-005 Project and WM-ACT-029 Program/Portfolio remain referenced masters.

## Import and acceptance scenario

Migration uses source namespace plus native identifier, idempotency keys for create and transition events, versioned status crosswalks, separate evidence-backed outcomes and explicit loss annotations. Re-import merges by source event identifier or a deterministic transition fingerprint, never synthesizes unobserved transitions and pins definition versions before and after cutover. Repeating the import creates no duplicate WorkItems or transitions; unmapped native statuses remain recorded loss.

## Invariants and blockers

Done requires criteria and evidence. Tracker container is not Project. Estimate is not actual effort. Permitted and occurred transitions differ. Type change does not mint identity. Epic/Feature is not automatically Task or Requirement. Unknown mapping is never coerced. Component masters retain lifecycle.

Publication remains held: WM-ACT-003 is unspecified and conflicts with WM-XCT-021/EM-OPS-01; WM-REC-006 and related edges are not canonical; effort/cost and WBS authorities are incomplete; no approved two-tracker crosswalk and executable fixture pack exists.
