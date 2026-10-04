Research only governance and lifecycle for WM-PER-010 Contact Point / Party
Profile.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the boundary of the final combined
  WM-PER-010, not merely this split pass. Include channels, preferences and
  governance as in scope while limiting only `structure.bundles`, functions
  and evidence gathering in this result.
- Cover source and authority to assert or change a contact point; links to
  consent, legal basis or communication restriction without absorbing those
  records; ownership/stewardship; lifecycle and temporal versioning;
  provenance; validation and reconciliation; sensitivity classification;
  field- and purpose-level access; minimization; retention/deletion;
  auditability; breach/staleness handling; interoperability mappings and
  quality controls.
- Cover canonical service rules for reading, adding, editing, deleting and
  exporting the combined model, including authorization, optimistic
  concurrency, idempotency, audit linkage, error semantics and patch rules.
- Separate proof that an endpoint is controlled from legal permission to use
  it for a purpose. Never store secret authenticators, message content or a
  complete consent/evidence object inside this model.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight distinct question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `cp-gov-`.
- Functions own authorization, lifecycle, reconciliation, redaction/export
  and deletion or tombstoning. This pass must provide the canonical complete
  service_layers block for the merged result.
- Prefer primary privacy, records-management, provenance and data-quality
  standards. Clearly label jurisdiction-specific duties and unresolved
  retention or erasure conflicts.
