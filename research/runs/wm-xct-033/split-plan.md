# WM-XCT-033 bounded Claude research plan

WM-XCT-033 is a format-neutral mixin for describing geometry together with the
coordinate reference context needed to interpret it. It is researched through
six bounded, independently schema-valid passes.

1. `geometry-core` owns geometric primitives, composition, dimensionality,
   topology, orientation, emptiness, validity and spatial extent.
2. `crs-identity` owns CRS identity and definition, datum/reference frame,
   coordinate-system axes, units, area of use and registry lifecycle.
3. `crs-dynamic` owns dynamic reference frames, coordinate epoch, temporal,
   vertical and compound components, plus custom/unknown CRS context.
4. `transform-quality` owns coordinate-operation chains, transformation
   resources, accuracy, uncertainty, precision, distortion and loss reporting.
5. `governance-controls` owns authority, lifecycle, provenance, access,
   licensing, retention, interoperability and the canonical service-layer block.
6. `service-operations` owns read, bind, correct, validate, transform,
   compare/relate, export/redact and disposition operation semantics.

Each pass uses a disjoint local-ID prefix. The deterministic merger keeps the
complete boundary from `geometry-core`, service layers from
`governance-controls`, remaps sources and validates the union. A later no-tools
adjudication must verify that the result remains a host-scoped mixin rather
than a place, feature/entity, map, file encoding, geometry engine, observation,
coordinate-operation service or CRS registry.
