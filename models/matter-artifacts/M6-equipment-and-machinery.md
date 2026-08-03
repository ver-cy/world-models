# M6 Equipment & Machinery

This meta-model describes industrial and household machinery as working assets: what a machine is and how it is configured, what it is rated to do and how much it has worked, and how it is maintained, inspected and certified. It is its own model because the maintenance-and-assurance life of a machine (plans, states, certificates) is a semantic world of its own that generic item tracking does not carry, and because capability ratings are what other models match against when work needs doing.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m6"
  csn: world.equipment
  version: 0.2.0
  displayName: "Equipment & Machinery"
  description: Machines as working assets with configuration, rated capability, utilization, maintenance and certification.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.equipment
bundles:
  - csn: world.equipment.asset
    displayName: Asset
    layers:
      - world.equipment.asset.machineIdentity
      - world.equipment.asset.configuration
  - csn: world.equipment.operation
    displayName: Operation
    layers:
      - world.equipment.operation.capability
      - world.equipment.operation.utilization
  - csn: world.equipment.assurance
    displayName: Assurance
    layers:
      - world.equipment.assurance.maintenanceState
      - world.equipment.assurance.inspectionAndCertification
imports:
  - source: eclass
    version: "*"
  - source: iso-55000
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `asset` | The machine as an identified, configured asset | `machineIdentity`: type, model, serial, commissioning data, site reference Â· `configuration`: installed options, attachments and settings that change what the unit is |
| `operation` | What the machine can do and how much it has done | `capability`: rated capacities, performance envelopes, supported operations Â· `utilization`: operating hours, cycles, load history |
| `assurance` | Keeping the machine fit and provably safe | `maintenanceState`: plans, due work, current serviceability standing Â· `inspectionAndCertification`: inspections, conformity certificates, their validity |

## Objects

- `machine`: one individual machine; key attributes: serial reference, model reference, commissioning date, site reference.
- `machineModel`: the class the machine instantiates; key attributes: maker reference, model code, classification code.
- `capabilitySpec`: one rated capability; key attributes: capability kind, rated value, unit, conditions.
- `configurationItem`: an installed option or attachment; key attributes: kind, identifier, installed date.
- `utilizationRecord`: a usage measurement over a period; key attributes: metric (hours, cycles), value, period.
- `maintenancePlan`: scheduled upkeep the machine is under; key attributes: plan reference, interval basis, tasks.
- `maintenanceState`: current serviceability standing; key attributes: state, due items, last service date.
- `certificate`: an inspection or conformity certificate; key attributes: scheme, issuer reference, validity period, scope.

## Relationships

- `machine` -> instanceOf -> `machineModel` (many-to-one): the unit inherits its model's baseline description.
- `machine` -> ratedFor -> `capabilitySpec` (1..*): effective ratings, possibly narrowed by configuration or wear.
- `machine` -> configuredWith -> `configurationItem` (0..*): current installed options and attachments.
- `machine` -> maintainedUnder -> `maintenancePlan` (0..*): plans in force for the unit.
- `machine` -> standsIn -> `maintenanceState` (exactly one current): the unit's serviceability at any moment.
- `machine` -> certifiedBy -> `certificate` (0..*): certificates held, each with its own validity.
- `machine` -> partOf -> `machine` (0..1): lines, installations and machine trains.

## Events

- `machineCommissioned`: the unit entered service at a site.
- `utilizationRecorded`: a usage reading extended the utilization history.
- `maintenancePerformed`: planned or corrective work was completed on the unit.
- `breakdownReported`: the unit failed or was taken out of service unexpectedly.
- `inspectionPassed`: an inspection concluded with a positive result.
- `certificateExpired`: a certificate's validity lapsed without renewal.
- `machineDecommissioned`: the unit permanently left service.

## Contracts

- `serviceProviderAccess`: owner-granted read and write access for a maintainer to the assurance bundle of named units.
- `certificateVerification`: query contract confirming that a unit holds a valid certificate of a given scheme.
- `fleetVisibility`: aggregated read access over an owner's fleet for an insurer, lessor or auditor.

## Projections

- `operatorView`: capability, configuration and current serviceability; omits commercial and certificate internals.
- `insurerRiskView`: utilization, breakdown history and certificate standing; omits configuration detail.
- `resaleView`: identity, hours, maintenance history summary and certificates; omits site and operational data.

## Composition

- EXTEND `world.physicalItem` (M2): a machine is an item; identity, custody and location semantics are inherited.
- REFERENCE `world.deviceHardware` (M8): condition-monitoring sensors and controllers attached to the unit are devices whose streams describe it.
- REFERENCE `world.materialSubstance` (M1): consumables, lubricants and process media resolve to substance classes.
- REFERENCE `world.place` (P1): installation sites resolve to place identities.
- ALIGN `world.vehicle` (M7): self-propelled work machines sit on the boundary; they are modelled here for their work function and there for their transport function, with field equivalences declared instead of duplication.
- imports: eclass (REFERENCE): classification and property dictionary for machine models and capabilities.
- imports: iso-55000 (ALIGN): asset management lifecycle vocabulary.

## Stewardship

Each machine record is stewarded by the machine's owner per the catalogue's S1 ownership model; maintainers, insurers and inspectors see it only under grants issued through S1/S2, and assurance events carry S4 audit traceability.
