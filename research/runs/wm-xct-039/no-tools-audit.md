# Separate no-tools adversarial review

Reviewer: separate Codex agent `audit_it_graph`, 2026-09-20. Scope: supplied design summary only; no tools, source research or runtime execution. This is not an external provider research result.

Outcome: coherent as a limited reviewable draft after explicit fail-closed rules.

Four conditional blockers were identified and addressed in service-layer policies:

1. Ambiguous identity, unknown master or authority conflict must block affected writes.
2. Every modified fact needs one master; cross-master changes require rejection or explicit decomposition and partial-completion handling.
3. Preconditions and idempotency must be enforced by the receiver, not merely described by fields. Unsupported guarantees hold execution; timeouts are indeterminate.
4. Steward designation, approval and client acceptance are not implicit grants; handover and temporary overlap need explicit authority, scope and expiry.

Two further limits were made explicit: incomplete/filtered dependency graphs cannot prove no impact; retention exceptions do not preserve operational access or redistribution rights.

Publication label: REVIEWABLE DRAFT — semantic composition proposal. Validation covers research-document structure and reference integrity. Runtime schemas, connector behavior, authorization enforcement, revocation propagation, and recovery guarantees are not implemented or verified. This draft does not authorize operational execution or claim standards conformance.

The revised policies were checked by the primary author against each requested correction. This is not a second audit of the full revised artifact.
