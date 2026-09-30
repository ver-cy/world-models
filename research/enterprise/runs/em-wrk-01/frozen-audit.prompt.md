# Frozen semantic audit request — EM-WRK-01

Audit this reconciled English metamodel decision once, without tools and without inventing identifiers.

Decision under audit:

- PROFILE WM-ACT-006 Task as WorkItem; reuse its identity and lifecycle. No WorkItem runtime/model ID.
- Tracker-native identity is source namespace + native item ID; imported IDs are aliases with explicit originating/master/mirror role.
- WorkItemType is a governed versioned vocabulary binding by scheme/version/code, not an aggregate.
- WM-XCT-021 is the versioned lifecycle/state-machine authority. Permitted transitions reference its definition; occurred transitions are append-only WM-ACT-006 history. WM-ACT-003 is only a deferred process-shaped alignment, not current tracker workflow mastership.
- Native status, canonical state and evidence-bearing outcomes done/accepted/cancelled/rejected are distinct. Closed is not accepted.
- Estimate is a revisioned Task assertion; actual effort is separately mastered.
- Requirement WM-REC-006, Project WM-ACT-005 and Program/Portfolio WM-ACT-029 remain referenced masters.
- Backlog and Iteration remain identifier-unassigned, specified-deferred-non-normative candidates. Current semantics are ordered selection and timeboxed Plan views/correlation aliases; independent identity requires irreducible mastered facts. Kanban cannot require Iteration.
- Migration is idempotent on source identity and transition-event identity, pins crosswalk and lifecycle-definition versions, records unmapped loss, never synthesizes unobserved transitions and never overwrites equal-authority conflicts.
- No new identifier and no canonical completeness/publication claim.

Return: verdict; blocking defects; exact remediation; required fixtures; publication disposition. Check identity, mastership, temporal semantics, outcome evidence, alias collision, transition deduplication/order, crosswalk succession, Backlog/Iteration demotion, Kanban, deletion/retention, access control and round-trip migration. Be concise and sceptical.
