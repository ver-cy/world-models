# U5 Utility Service Point

This meta-model describes the points where utility networks meet the places they serve: connections for water, heat, power and sewage, the meters registered at them, readings, supply status and the tariff scheme in force. It is its own model because service points churn (connect, disconnect, re-meter) on a different cadence than the long-lived network assets (U3) and the premises they serve (U2), and because consumption data carries its own consent regime.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:u5"
  csn: world.utilityServicePoint
  version: 0.2.0
  displayName: "Utility Service Point"
  description: "Connections for water, heat, power and sewage: service points, meters, readings, supply status and tariff references."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.utilityServicePoint
bundles:
  - csn: world.utilityServicePoint.connection
    displayName: "Connection"
    layers:
      - world.utilityServicePoint.connection.servicePoints
      - world.utilityServicePoint.connection.physicalConnections
  - csn: world.utilityServicePoint.metering
    displayName: "Metering"
    layers:
      - world.utilityServicePoint.metering.meters
      - world.utilityServicePoint.metering.readings
  - csn: world.utilityServicePoint.supply
    displayName: "Supply"
    layers:
      - world.utilityServicePoint.supply.supplyStatus
      - world.utilityServicePoint.supply.tariffReference
imports:
  - source: iec-cim
    version: "*"
  - source: dlms-cosem
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `connection` | Where and how a served place ties into a network | `servicePoints`: the delivery points where service is handed over · `physicalConnections`: the pipe or cable from network segment to service point |
| `metering` | How delivery is measured | `meters`: measuring devices registered at service points · `readings`: dated values taken from meters |
| `supply` | Whether and on what terms supply is active | `supplyStatus`: active, disconnected and suspended spells · `tariffReference`: pointers to externally governed tariff schemes |

## Objects

- `servicePoint`: the delivery point where a utility service is handed over to a served premise or site; key attributes: serviceKind, status, commissionedAt
- `physicalConnection`: the pipe or cable tie from a network segment to the service point; key attributes: capacity, length, installedYear
- `meter`: a measuring device registered at a service point; key attributes: meterKind, accuracyClass, installedAt
- `meterReading`: a dated value taken from a meter; key attributes: readAt, value, unit, readingMethod
- `supplySpell`: a continuous period of active supply at a service point; key attributes: startAt, endAt, supplyBasis
- `tariffReference`: a pointer to an externally governed tariff scheme applying at a service point; key attributes: schemeRef, term, validFrom

## Relationships

- `servicePoint` -> serves -> `premise` (n:1): a service point delivers to a premise, building or site modelled in U2/U1
- `physicalConnection` -> taps -> `segment` (n:1): the U3 segment the connection draws from
- `physicalConnection` -> feeds -> `servicePoint` (1:1): each connection terminates in one delivery point
- `meter` -> installedAt -> `servicePoint` (n:1): meters succeed one another at the same point over time
- `meterReading` -> takenFrom -> `meter` (n:1): the reading history of a device
- `supplySpell` -> under -> `tariffReference` (n:1): each active spell runs under one tariff term at a time

## Events

- `connectionEnergized`: a new connection was made live and delivery became possible
- `meterInstalled`: a meter was registered at a service point
- `meterExchanged`: a meter was replaced and closing/opening readings recorded
- `readingTaken`: a dated reading was captured from a meter
- `supplyDisconnected`: supply at a service point was cut off
- `supplyReconnected`: supply at a service point was restored

## Contracts

- `consumptionAccessGrant`: the served party consents per S2 to share consumption data with a named consumer
- `supplierSwitchExchange`: the data exchange executed when the supplying party at a service point changes
- `aggregateLoadLicense`: release of anonymized, aggregated load data to network and settlement planners

## Projections

- `billingProjection`: readings and tariff references needed for settlement; omits network topology
- `networkLoadProjection`: aggregate demand per segment for U3 planning; omits customer identity
- `premisePassportProjection`: which services a premise is connected to; omits consumption values

## Composition

- REFERENCE `world.premisesSpatialUnit` (U2): the served premises; occupancy context lives there
- REFERENCE `world.physicalInfrastructureNetwork` (U3): the tapped segments and their capacity
- REFERENCE `world.buildingStructure` (U1): service points serving whole buildings or sites
- REFERENCE `world.person` (H1): the served party in a supply spell
- REFERENCE `world.organization` (O1): organizational customers and supplying operators
- imports: iec-cim (EXTEND: usage point and metering semantics)
- imports: dlms-cosem (ALIGN: meter reading exchange semantics)

## Stewardship

The owner archetype is the utility operator, which stewards service points, connections and meters for its service kind. Consumption data is disclosed only with the served party's S2 grant; aggregate releases are anonymized, and all disclosures are auditable via S4.