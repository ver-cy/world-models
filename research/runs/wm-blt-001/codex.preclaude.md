# WM-BLT-001 frozen pre-provider dossier

## Identity and boundary

- Registry ID: `vr.wm-blt-001`
- Model ID: `WM-BLT-001`
- Name: `Building / Structure`
- Record-plane label: `standalone-mm`
- Candidate subject kind: `aggregate`
- Previous card: `models/built-environment/U1-building-and-structure.md`
- Candidate relation: `WM-BLT-001 CONTAINS WM-BLT-002` for premises or
  spatial units.
- Inbound candidate relation: `WM-BLT-006 CONTAINS WM-BLT-001` for an
  operational facility aggregation.

The model owns the persistent physical artifact: its stable identity,
classification, location footprint and pose, geometric and spatial
decomposition, load-bearing system, envelope, materials, installed-system
bindings, physical characteristics, current observed condition, performance
assessments and lifecycle changes. It does not own the operating Facility,
land parcel or site, interior occupancy and tenancy, individual maintainable
equipment, construction-project execution, parties, permits, addresses,
financial valuation or incident lifecycle.

The word `structure` is broad. The base must support roofed buildings and
engineered structures such as bridges, towers, tunnels, dams and retaining
works while allowing subtype profiles to require different geometry,
components, actions, hazards and performance metrics. Do not universalize one
building-code taxonomy or make every structure habitable.

## Existing conceptual structure to test

The previous card proposed fabric (massing, elements, materials), performance
(condition, energy) and lifecycle (provenance, alterations). Deep research
should also test:

1. Authoritative identity, aliases, class and intended function.
2. Georeference, footprint, extent, orientation and level of detail.
3. Storeys, spaces or segments, zones and containment boundaries.
4. Foundations, frame, load paths, envelope and openings.
5. Materials and measured physical properties with units and tolerances.
6. Installed systems as external equipment or system references.
7. Recognition features and distinctions from temporary works, equipment,
   sites and facilities.
8. Affordances, supported uses, loads, access, evacuation and hazards.
9. Condition, inspection, defects, damage, capacity, energy and other
   performance assessments.
10. Design, construction, commissioning, alteration, change of use,
    decommissioning and demolition with provenance.

## Adversarial checks

- Do not confuse physical artifact status with construction-project, permit,
  occupancy, facility-operation or financial status.
- Do not store an owner or occupant as if they were an intrinsic property.
- Keep designed, as-built, surveyed and current observed geometry distinct.
- Preserve measurement method, units, tolerance, coordinate reference system,
  level of detail, observation time and uncertainty.
- Do not infer structural safety from age, appearance or a generic condition
  grade.
- Keep damage observations, engineering assessments, restrictions and repair
  work as distinct objects.
- Do not claim round-trip IFC or CityGML conformance without versioned
  crosswalks and loss declarations.
