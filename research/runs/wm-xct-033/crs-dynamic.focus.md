Research dynamic, temporal, compound and non-register CRS context for
WM-XCT-033 Geometry / Coordinate Reference.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-033 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover dynamic reference frames and frame reference epoch, coordinate epoch,
  temporal CRS and time scale, vertical CRS, compound CRS components and their
  order, ensemble/datum realization, deformation model references, coordinate
  metadata, unknown/custom/engineering definitions and pinned snapshots.
- Distinguish coordinate epoch, observation time, transformation reference
  epoch, definition publication time and ingestion time. A coordinate epoch is
  not a timestamp for when the record was created.
- Unknown/custom CRS is allowed only with a resolvable definition or complete
  governed snapshot; a bare local name or numeric code is insufficient.
- Do not own registry maintenance, deformation computation or transformation
  execution. Record definitions, references and applicability context only.
- Target 2 bundles, 4-5 layers and 8-10 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `geo-crsdyn-`.
- Prefer primary ISO/OGC dynamic-CRS and coordinate-metadata material, EPSG
  guidance, IERS and authoritative national geodetic agencies. Preserve
  incomplete public access, time-scale and regional realization differences as
  gaps/holds.
