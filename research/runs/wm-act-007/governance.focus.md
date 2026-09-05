Research only lifecycle, change control, evidence, quality, access and retention for WM-ACT-007 Work Order.

- Keep the authoritative work order as aggregate root and use exact registry identity.
- Cover draft/authorized/released/suspended/cancelled/closed administrative states; immutable issued revisions; supersession; cancellation and expiry; transition authority and reason; conflict/duplicate handling; provenance and source quality; ownership/delegated write authority; disclosure and access exceptions; retention, legal hold, tombstone and disposition.
- Distinguish order administrative state from actual work state. Never own execution, enforcement or audit-trail semantics.
- This pass exclusively owns merged service_layers. Make identity priority, RFC 3339 timestamp separation, CRUD, validation, roles, access scopes, artifact rules and AGENTS.md bootstrap concrete for the full Work Order model.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 questions each.
- Every local ID must begin with `wo-gov-`.
- Use at least eight question kinds. Limit functions to revision, lifecycle governance, validation, access decision requests and disposition handoff.
- Prefer primary provenance, records-management, access-policy and work-order standards. Mark jurisdiction-specific rules and unread paywalled text as gaps.
