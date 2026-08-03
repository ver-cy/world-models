# M7 Vehicle & Transport Means

This meta-model describes vehicles across all modes (road, rail, water, air) as registered means of transport: their mode-specific identity schemes, registration standing, design capacities, and fitness to operate. It is its own model because vehicles are the one item family whose existence is mediated by public registries and periodic fitness regimes in every jurisdiction, giving them a registration-and-fitness semantic core that neither generic items nor machinery share.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m7"
  csn: world.vehicle
  version: 0.2.0
  displayName: "Vehicle & Transport Means"
  description: Vehicles of all modes with identity schemes, registration, capacity and operational fitness.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.vehicle
bundles:
  - csn: world.vehicle.identity
    displayName: Identity
    layers:
      - world.vehicle.identity.vehicleIdentity
      - world.vehicle.identity.registration
  - csn: world.vehicle.design
    displayName: Design
    layers:
      - world.vehicle.design.modeAndClass
      - world.vehicle.design.capacityAndPerformance
  - csn: world.vehicle.fitness
    displayName: Fitness
    layers:
      - world.vehicle.fitness.fitnessCertification
      - world.vehicle.fitness.inspectionHistory
imports:
  - source: iso-3779-vin
    version: "*"
  - source: vehicle-registries
    version: "*"
  - source: unece-wp29
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `identity` | Who this vehicle is to the world's registries | `vehicleIdentity`: mode-specific identifiers (VIN, hull id, tail number, rolling stock number) Â· `registration`: registry entries, plates and marks, jurisdiction, standing over time |
| `design` | What the vehicle is built as | `modeAndClass`: mode, category and class assignments with approval references Â· `capacityAndPerformance`: seats, payload, tonnage, range and comparable rated figures |
| `fitness` | Whether it may operate | `fitnessCertification`: roadworthiness, airworthiness, seaworthiness certificates and their validity Â· `inspectionHistory`: periodic and incident-driven inspections with outcomes and readings |

## Objects

- `vehicle`: one individual means of transport; key attributes: mode, build year, maker reference, lifecycle status.
- `vehicleIdentifier`: a mode-specific identity assignment; key attributes: scheme, value, issuing context.
- `registrationEntry`: an entry in a registry; key attributes: registry reference, jurisdiction, plate or mark, standing, period.
- `modeClass`: a category or class assignment; key attributes: scheme, category code, approval reference.
- `capacitySpec`: one rated capacity; key attributes: capacity kind (seats, payload, tonnage), value, unit, conditions.
- `fitnessCertificate`: a certificate of fitness to operate; key attributes: certificate kind, issuer reference, validity period, restrictions.
- `inspectionRecord`: a completed inspection; key attributes: inspection kind, date, outcome, findings.
- `usageMeterReading`: a dated meter value; key attributes: meter kind (odometer, engine hours), value, unit, source.

## Relationships

- `vehicle` -> identifiedBy -> `vehicleIdentifier` (1..*): every vehicle bears at least one scheme identity.
- `vehicle` -> registeredUnder -> `registrationEntry` (0..* over time): at most one entry per registry is current.
- `vehicle` -> classifiedAs -> `modeClass` (1..*): mode and category assignments, possibly per jurisdiction.
- `vehicle` -> ratedFor -> `capacitySpec` (1..*): the design figures the vehicle may be used up to.
- `vehicle` -> certifiedBy -> `fitnessCertificate` (0..*): fitness certificates with independent validity.
- `inspectionRecord` -> assesses -> `vehicle` (many-to-one): inspections accumulate as the fitness history.
- `usageMeterReading` -> readFrom -> `vehicle` (many-to-one): meter readings form the usage timeline.

## Events

- `vehicleManufactured`: the vehicle came into existence with its build identity.
- `vehicleRegistered`: a registry entry was created for the vehicle in a jurisdiction.
- `registrationTransferred`: the registration passed to a new keeper or registry.
- `inspectionCompleted`: an inspection concluded with a recorded outcome.
- `fitnessRevoked`: a fitness certificate was suspended or withdrawn.
- `meterReadingRecorded`: a usage meter value was captured.
- `vehicleExported`: the vehicle left a registry's jurisdiction for another.
- `vehicleScrapped`: the vehicle was destroyed and its registrations closed.

## Contracts

- `registryLookup`: query contract resolving an identifier or plate to registration standing and class, without keeper personal data.
- `historyReport`: owner-consented compilation of inspections, meter readings and registration periods for a prospective buyer.
- `fleetDataShare`: standing grant from a fleet owner to an operator, insurer or lessor over named vehicles.

## Projections

- `buyerHistoryView`: build data, meter timeline, inspection outcomes and registration periods; omits keeper identities.
- `enforcementView`: current registration standing, class and fitness; omits usage history and commercial data.
- `fleetOperationsView`: capacities, fitness validity and meter state across a fleet; omits registry internals.

## Composition

- EXTEND `world.physicalItem` (M2): a vehicle is an item; instance identity, custody and location semantics are inherited.
- REFERENCE `world.deviceHardware` (M8): telematics units and onboard sensors are devices; their streams describe this vehicle.
- ALIGN `world.equipment` (M6): self-propelled work machines are aligned across the two models rather than modelled twice.
- REFERENCE `world.place` (P1): home bases, ports of registry and stationing points resolve to place identities.
- imports: iso-3779-vin (REFERENCE): identifier scheme for road vehicles.
- imports: vehicle-registries (REFERENCE): national and modal registries as the authorities behind registration entries.
- imports: unece-wp29 (ALIGN): vehicle category and type approval concept alignment.

## Stewardship

Each vehicle record is stewarded by its owner per the catalogue's S1 ownership model, with a registrar archetype stewarding the registration layer; lookups and history reports are served only under S1/S2 grants, and registry events carry S4 audit traceability.
