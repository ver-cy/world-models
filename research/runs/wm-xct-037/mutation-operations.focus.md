Research mutation-operation contracts for WM-XCT-037 Dependency / Impact.

- Define declare, validate, review, approve, activate, revise, supersede, retire and observation-update commands.
- State actor, preconditions, inputs, invariants, idempotency, concurrency, result, failure and emitted-event semantics.
- Preserve immutable historical identity and distinguish correction from supersession.
- Prevent commands from mutating externally owned endpoints or executing dependent actions.
- Require authorization references and audit hooks without deciding access or storing audit evidence.
- Do not perform package resolution, deployment, remediation or notification delivery.
- Target 2 bundles, 4-5 layers and 7-9 findings. Every local ID begins `dep-mut-`.
