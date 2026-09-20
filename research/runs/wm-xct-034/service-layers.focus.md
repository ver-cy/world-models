Research the canonical service-layer and agent-bootstrap contract for
WM-XCT-034 Digital Signature / Proof.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-034 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- The `service_layers` block is the primary deliverable and must be complete:
  dimension, namespace, canon, patch, artifact rules, policies, processes,
  roles, access and AGENTS.md bootstrap. Do not omit a section merely to keep
  the structural bundles small.
- Require AGENTS.md fields Name, Type, Specification URL, Storage type URL,
  Interface URL, Processes URL, Registry ID and Owner, with an explicit read
  order that fails closed when a reference cannot be resolved.
- Require format/interface neutrality across Git/files/MCP/Mongo and signature
  bindings. Every projection reports losses; no container, database or API is
  canonical.
- Artifact identity priority is master-system ID, then governed IRI, then
  Dimension ULID. Dates and timestamps are never identifiers. All record times
  include seconds and explicit offset or Z; signer-claimed time and trusted
  evidence time remain distinct.
- Define authority and roles without execution: external systems own key
  custody, signing authorization, cryptographic operations, CA/TSA/trust-list,
  audit storage, legal effect, retention enforcement and physical deletion.
- Define access by bundle/layer/finding/artifact, including separate controls
  for payload, proof bytes, public credentials, identity attributes, status
  evidence and diagnostics; exceptions are explicit, expiring and auditable.
- Target 1 bundle, 3-4 layers and 5-7 findings with 3-5 questions each. Use at
  least eight question kinds. Every local ID must begin with `sig-slayer-`.
