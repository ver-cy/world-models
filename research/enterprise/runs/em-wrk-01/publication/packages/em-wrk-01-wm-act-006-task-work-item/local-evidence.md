# EM-WRK-01 reconciled synthesis

## Decision

EM-WRK-01 is a restrictive profile over reserved WM-ACT-006. No new model or runtime identifier is allocated. WM-XCT-021 is the current lifecycle-definition and permitted-transition authority; WM-ACT-003 remains a deferred process-shaped alignment. WorkItemType is a governed versioned vocabulary. Estimate and evidence-bearing outcomes are append-only task assertions.

Grok and Claude agree on canonical Task reuse, external Requirement/Project/Program mastership, idempotent import and the separation of native status, canonical state and outcome. Grok challenged independent Backlog and Iteration identity. The reconciled model therefore registers Backlog as an ordered selection view and Iteration as a timeboxed WM-ACT-008 Plan view. Rank and membership are mastered as scoped view facts, and Kanban does not require Iteration.

## Audited integration semantics

WM-ACT-006 `taskId` is canonical. Each source uses an immutable internal native ID as its natural key; mutable human keys and container paths are effective-dated aliases. Source transition identity never includes mapped canonical states. It prefers a native event ID and otherwise uses an immutable native fingerprint plus occurrence time and source ordinal. Occurrence time selects the lifecycle version; retrospective mappings are marked.

Every mapped value carries the producing crosswalk version. Compatible and breaking crosswalk succession are explicit; remapping appends a superseding assertion and never changes the source event. Unmapped values create retained, queryable loss records. Import observations record credential scope, distinguish absent from empty, create tombstones only for observed deletion, retain identity through actor redaction, tag write provenance, suppress echo and surface equal-authority conflicts.

Outcomes are open-world append-only assertions with asserter, authority, basis, evidence and explicit supersession or retraction. Closed is never accepted by inference. Estimate revisions declare unit scheme version, estimate kind and grain; actual effort remains under a named external authority.

Fifteen executable fixtures cover repeat import, crosswalk succession, tied transitions, key changes, conflicting masters, closure without acceptance, reopening, unmapped values, scoped absence, omission versus deletion, multi-context rank, Kanban, estimate unit changes, echo suppression and historical lifecycle versions.

## Publication state

The candidate is provider-reconciled and remediated after one frozen Claude audit. It remains noncanonical while parent specifications, approved relations and adapter-specific actual-effort authority are incomplete. No blocker is published as a model release.
