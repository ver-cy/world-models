Research CRS identity, static definition and coordinate-system semantics for
WM-XCT-033 Geometry / Coordinate Reference.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-033 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover authoritative CRS identifier, authority and registry/version; full
  definition or resolvable reference; datum/reference frame; coordinate system;
  axis count, order, name, abbreviation, direction and unit; ellipsoid and prime
  meridian; geographic, projected, vertical and engineering CRS; area and scope
  of use; alias, deprecation and supersession.
- Never infer axis order from a code, label or serialization convention and
  never silently default a CRS. Distinguish definition identity, display names,
  aliases and versioned registry records.
- Keep the external CRS registry authoritative. A cached definition is a pinned
  snapshot with provenance, not a local re-registration.
- Target 2 bundles, 4-5 layers and 8-10 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `geo-crsid-`.
- Prefer primary ISO 19111 public material, OGC CRS WKT, OGC API Features CRS,
  EPSG registry/guidance and authoritative national geodetic sources. Preserve
  paywall, registry-version and regional datum differences as gaps/holds.
