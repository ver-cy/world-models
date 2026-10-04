Research mutation command semantics for WM-XCT-036 Alias / Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define propose, validate, submit evidence, approve/reject, activate,
  supersede and retract commands, with explicit inputs, outputs, preconditions,
  effects, failure modes and external side-effect boundaries.
- Every mutation requires an idempotency key and optimistic-concurrency
  precondition. Prior assertions, evidence and decisions are immutable; changes
  append new versions or decision assertions.
- Validation checks endpoint reference and version, relation-property contract,
  type/scheme/context compatibility, required evidence/review, contradictions,
  not-same constraints, effective interval and declared access scope.
- Cover duplicate commands, concurrent proposals, stale versions, conflicting
  active assertions, partial failure, compensation and emergency quarantine.
- Functions calculate, validate or record only: no entity matching, reasoning,
  redirect execution, endpoint merge, authorization decision, audit-log
  operation, notification delivery or physical deletion.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-cmd-`.
- Prefer primary HTTP conditional/idempotency, provenance and lifecycle sources.
