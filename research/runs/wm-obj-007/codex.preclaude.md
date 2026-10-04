# Codex pre-provider boundary: WM-OBJ-007 Vehicle

Status: provisional preparation, not provider evidence or synthesis.

## Boundary

Vehicle is an individual manufactured or assembled physical artifact whose
designed function includes movement or carriage through an operational medium.
The base is multimodal and owns instance identity, physical composition,
intrinsic specifications, installed systems, observed condition, capabilities,
registration references, lifecycle events and context.

Vehicle type, model and variant are separate design or regulatory classes.
Components, engines, batteries, sensors and cargo are whole-part references.
Owners, keepers, operators, occupants and maintainers are parties and roles.
Trips, movements, inspections, repairs, incidents, transfers and observations
are events. Registrations, titles, approvals, permits and certificates are
external governed records.

## Candidate structure

1. Identity and classification: master identifiers, mode, type, role and
   registration markings.
2. Physical structure: geometry, mass, materials, body, chassis, hull, airframe,
   running gear and installed systems.
3. Propulsion and energy: prime movers, drives, fuels, batteries, charging,
   consumption, emissions and ranges.
4. Capacity and capabilities: occupants, cargo, towing, speed, range, operating
   envelope, controls and interfaces.
5. Recognition and state: markings, appearance, pose, location, telemetry,
   condition, damage, faults and operability.
6. Lifecycle and operational context: manufacture, commissioning, ownership,
   custody, registration, service, inspection, modification and retirement.
7. Safety, compliance and interoperability: hazards, approvals, certificates,
   per-mode profiles, evidence, access, retention and projections.

## Five facets and controls

- Identity and class: required, with authoritative mode-specific identifiers.
- Direct physical properties: required, always with unit, tolerance, method,
  conditions and time where mutable.
- Recognition and observation: required, including distinctive marks, confusing
  classes, sensors, confidence and evidence.
- Capabilities and affordances: required, with operating limits, preconditions,
  hazards, reversibility and failure modes.
- Context and evidence: required, with manufacture, ownership, custody,
  registration, location, events, rules, provenance, access and retention.

Published source records remain immutable; corrections and modifications create
successors. Event timestamps use RFC 3339 with seconds and explicit offset or Z.
No approved outgoing registry relations currently exist for WM-OBJ-007, so
candidate component, party, location, journey, maintenance, evidence and
compliance links remain proposals.

## Primary source candidates

- https://unece.org/transport/vehicle-regulations/wp29/resolutions
- https://www.iso.org/standard/52200.html
- https://www.nhtsa.gov/vehicle-manufacturers
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32018R0858
- https://www.imo.org/en/ourwork/msas/pages/imo-identification-number-scheme.aspx
- https://www.icao.int/nationality-marks
- https://www.era.europa.eu/registers/evr_en
- https://www.w3.org/TR/vocab-ssn/
- https://www.w3.org/TR/prov-o/
- https://www.rfc-editor.org/rfc/rfc3339
