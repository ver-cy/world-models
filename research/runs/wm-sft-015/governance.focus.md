Research only assurance, governance and lifecycle for WM-SFT-015 Test Case /
Test Result.

- Use the exact registry identity and output `entry_kind` `aggregate`.
- The `model` block must describe the complete combined WM-SFT-015 boundary,
  not merely this split pass. Include definition/design, execution/results,
  evidence, assurance and governance as in scope while limiting this result's
  structure, functions and evidence gathering to the assigned area.
- Cover ownership and stewardship; author/reviewer/approver/executor roles;
  separation of duties; lifecycle and state transitions; revision and
  supersession; provenance; source/tool trust; validation; completeness and
  coverage claims; requirement/risk traceability; quality/confidence;
  sensitivity; field/artifact-level access; personal or production data;
  retention/legal hold/disposal; audit references; integrity; export/redaction;
  interoperability mappings; regional or regulated-sector variation.
- Cover canonical read, add, edit, delete/tombstone, execute, approve, export
  and patch rules for the combined model, including authorization, optimistic
  concurrency, idempotency, immutable evidence, corrections by supersession,
  referential integrity and explicit failure semantics.
- Distinguish coverage measurements and release-gate references from the test
  evidence itself. Do not claim that coverage proves adequacy, that a passing
  test proves absence of defects, or that alignment to a standard establishes
  conformance without the required evidence.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight distinct question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `tst-gov-`.
- Functions own authorization, review/approval, assurance calculation,
  reconciliation, redaction/export, retention and tombstoning. This pass must
  provide the canonical complete `service_layers` block for the merged result.
- Prefer primary testing, quality, security, records-management, provenance
  and privacy standards. Clearly label paywalled, jurisdiction-specific or
  tool-specific evidence and preserve unresolved conflicts as publication
  holds rather than flattening them.
