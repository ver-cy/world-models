Research the format-neutral geometric structure for WM-XCT-033 Geometry /
Coordinate Reference.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-033 boundary,
  including geometry, CRS context, transformation quality and governance.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover geometry identity only as host-dependent weak identity; primitive and
  aggregate types; point, curve/line, surface/polygon and collection semantics;
  coordinate sequences; topological dimension versus coordinate dimension;
  Z/M handling; rings, closure, orientation, interiors/holes, multipart
  membership, empty versus absent geometry, envelopes/extents, validity and
  declared spatial relations.
- Separate mathematical geometry from serialization. Do not make WKT, WKB,
  GeoJSON, GML, database types or a vendor API canonical storage.
- Do not own the host feature/place/object, address, map styling, raster,
  observation, route/network semantics, geometry computation engine or CRS
  register. The geometry is a value bound to a host.
- Treat antimeridian, poles, curved geometry, 3D solids and non-planar validity
  as explicit boundary cases rather than silently applying planar rules.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `geo-core-`.
- Prefer primary OGC Simple Features, GeoSPARQL, OGC/ISO geometry abstracts,
  RFC 7946 and W3C/OGC spatial-data guidance. Record paywall or retrieval
  limitations and unresolved curved/solid/geodesic differences as gaps.
