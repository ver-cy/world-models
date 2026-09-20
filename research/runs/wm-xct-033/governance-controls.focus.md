Research governance controls and the canonical service-layer policy block for
WM-XCT-033 Geometry / Coordinate Reference.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-033 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover host-object owner, geometry steward, CRS/geodetic authority, producer,
  independent reviewer and approver; authority for geometry correction, CRS
  selection and transformation policy; host-dependent identity; version,
  effective interval and supersession; provenance of source and derived
  geometries; sensitive-location classification and precision-reduction policy;
  licensing of definitions, grids and source data; retention, legal hold,
  tombstone; interoperability profiles and audit references.
- Roles and authorization metadata are advisory only. External components own
  allow/deny, enforcement, registry maintenance, grid acquisition, physical
  deletion and map rendering.
- Access and redistribution rights are distinct. A readable grid, definition or
  source geometry is not automatically redistributable.
- Target 2 bundles, 4-5 layers and 8-10 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `geo-govctl-`.
- This result supplies the canonical complete `service_layers` block, including
  format-neutral canonicalization/patch/compatibility rules, CRUD policy,
  roles, access and AGENTS.md read order. Operations may be concise because
  detailed service evidence is owned by the operation result.
- Prefer primary OGC/W3C, ISO public material, authoritative CRS registries,
  access-control, provenance and records-management standards. Preserve legal,
  licensing, privacy and regional differences as gaps/holds.
