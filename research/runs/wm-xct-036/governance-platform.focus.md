Research platform, interoperability and canonical service-layer controls for
WM-XCT-036 Alias / Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Own and fully populate the final `service_layers` block: dimension,
  namespace, canon/patch, artifact rules, policies, CRUD processes, roles,
  access and the mandatory AGENTS.md bootstrap.
- Require format/interface neutrality across Git/files/MCP/Mongo, RDF/JSON/
  YAML/CSV/APIs and redirect projections. Every information loss, semantic
  weakening, unsupported relation kind and round-trip limitation is reported.
- Define artifact identity priority: master-system ID, governed IRI, then
  Dimension ULID. Dates, timestamps, digests and filenames are never identity.
  Serial editions use an opaque sequence separate from event time.
- Require RFC 3339 date-times with seconds and explicit numeric offset or `Z`,
  and keep event time separate from observation and ingestion time.
- Cover namespace ownership, canonical schema/version/patch references,
  validation rules, compatibility promises and safe evolution without defining
  endpoint identifier schemes.
- Define the minimal AGENTS.md orientation contract: name, type, specification,
  storage, interface and process links, including how an agent finds data held
  through MCP or Mongo rather than local files.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-gplat-`.
- Prefer primary W3C, IETF and Vercy contract sources.
