Research coordinate transformation, accuracy and quality context for
WM-XCT-033 Geometry / Coordinate Reference.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-033 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover source and target CRS, ordered coordinate-operation chain, conversion
  versus transformation, concatenated operations, method and parameter pins,
  grid/resource identity and checksum, coordinate epoch, area of use, ballpark
  or fallback status, stated operation accuracy, positional uncertainty,
  precision/resolution, dimensionality changes, axis/unit normalization,
  densification, clipping/wrapping, antimeridian and polar handling.
- Preserve original geometry and CRS whenever a derived geometry is produced.
  Record sufficient lineage and resource/version pins for reproduction.
- Make missing grids, out-of-area coordinates, epoch mismatch, axis ambiguity,
  unsupported dimensions, invalid geometry, tolerance breach and lossy export
  explicit outcomes. Do not promise exact round trips for non-bijective or
  rounded operations.
- Functions calculate, validate or report only. External engines own execution
  environment and resource acquisition; registries own operation definitions.
- Target 2 bundles, 4-6 layers and 9-12 findings with 3-5 discriminating
  questions each. Use at least eight question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `geo-xform-`.
- Prefer primary ISO/OGC coordinate-operation material, EPSG guidance, PROJ
  operation documentation and authoritative geodetic agencies. Preserve
  method/resource licensing and jurisdictional accuracy differences as gaps.
