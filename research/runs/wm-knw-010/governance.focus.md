Research only governance, participation and lifecycle for WM-KNW-010
Decision / Rationale.

- Use the exact registry identity and output `entry_kind` `aggregate`. The
  governed decision content remains the aggregate root; governance controls
  its authority, lifecycle, accountability and safe operation without turning
  the model into an activity log, document container, policy or legal judgment.
- Cover deciding authority and mandate; owner, steward, custodian and reviewer;
  participants and declared roles; delegation, quorum, conflict of interest and
  recusal; submission, review, approval or ratification; effective, conditional,
  suspended, superseded, revoked, expired and reopened states; review, appeal
  and reconsideration triggers; version and change history; provenance of the
  decision content; access classification, disclosure and exceptions; integrity,
  audit, retention, legal hold and defensible disposition; implementation and
  outcome monitoring only as referenced follow-up obligations, never as owned
  execution data.
- Make approval activity references point to WM-ACT-024, carrying decision
  records point to WM-REC-010, legal judgments point to WM-POL-021, claims and
  evidence point to WM-KNW-007 and WM-KNW-008, and policies or executable rules
  remain referenced neighbours. Do not duplicate their internal structures.
- Do not repeat the decision problem, alternatives, criteria, evaluation and
  outcome structures owned by `core`, or rationale, claims, evidence bindings,
  assumptions, arguments, dissent and explanation structures owned by
  `reasoning`. Boundary notes may cite them.
- The following artefacts already exist and must not be re-created under new
  IDs: `dr-core-art-drg`, `dr-core-art-rule-table`,
  `dr-core-art-comparison-matrix`, `dr-rsn-art-statement-of-reasons`,
  `dr-rsn-art-argument-structure`, `dr-rsn-art-assumption-register`,
  `dr-rsn-art-sensitivity-record`, `dr-rsn-art-dissent-record`,
  `dr-rsn-art-explanation-rendition` and `dr-rsn-art-reasoning-trace`.
  Governance may reference them by ID and may add only genuinely governance-
  owned artefacts such as a decision authority register, lifecycle/change
  ledger, access-and-disclosure schedule or review/disposition record.
- For any serial governance artefact, require the decision master identifier,
  an artefact-kind discriminator and a zero-padded monotonic sequence within
  the explicitly named scope. Never derive identity from a date or timestamp.
  All timestamps must use RFC 3339 with seconds and `Z` or an explicit offset,
  and event, observation and ingestion time must remain distinct where used.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight distinct question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artefact and function IDs, must begin with `dr-gov-`.
- This pass is the canonical owner of all `service_layers`: namespace and
  Dimension bindings, AGENTS.md entrypoint contract, identity and versioning,
  read/add/edit/delete rules, roles and authority, validation, access and
  exceptions, retention/disposition, provenance, audit/integrity and format-
  neutral interface expectations. Deletion must be tombstone/supersession-first
  unless an authorised erasure rule applies, and the surviving identity and
  audit facts must be explicit.
- Prefer primary standards and official specifications for records governance,
  provenance, access, retention and decision accountability. Mark jurisdiction-
  specific duties as profiles or alignments and never claim global conformance.
