# F1 Energy

This meta-model describes energy as it flows through the world: the carriers energy takes (electricity, gas, heat, fuels), the sources that generate or transform it, the points that consume it, and the continuous reconciliation of supply and demand across balance areas. It is its own model because energy obeys network physics and balance identities: quantities must reconcile per carrier, per area and per settlement period, a discipline that generic goods or financial models do not carry.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f1"
  csn: world.energy
  version: 0.2.0
  displayName: Energy
  description: Energy carriers, their generation, transformation, consumption and system balance.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.energy
bundles:
  - csn: world.energy.carrier
    displayName: Carrier
    layers:
      - world.energy.carrier.carrierTypes
      - world.energy.carrier.unitsAndConversion
  - csn: world.energy.production
    displayName: Production
    layers:
      - world.energy.production.generationAssets
      - world.energy.production.transformation
  - csn: world.energy.consumption
    displayName: Consumption
    layers:
      - world.energy.consumption.demandAndLoad
      - world.energy.consumption.metering
  - csn: world.energy.balance
    displayName: Balance
    layers:
      - world.energy.balance.gridBalance
      - world.energy.balance.storageAndReserves
      - world.energy.balance.interchange
imports:
  - source: iec-cim
    version: "*"
  - source: iea-energy-balances
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `carrier` | What energy is and how it is measured | `carrierTypes`: catalogue of carriers (electricity, gas, heat, hydrogen, liquid fuels) and their physical qualities · `unitsAndConversion`: energy content units and conversion rules between carriers |
| `production` | Where energy enters or changes form | `generationAssets`: generating units, their technology and capacity · `transformation`: conversion processes between carriers (refining, gas to power, power to heat) |
| `consumption` | Where energy is drawn | `demandAndLoad`: consumption points, sectors and load profiles · `metering`: quantified readings at delivery points |
| `balance` | Reconciling supply and demand | `gridBalance`: balance areas and settlement periods · `storageAndReserves`: buffering of carriers over time · `interchange`: scheduled and measured flows between areas |

## Objects

- `energyCarrier`: a form in which energy is held or moved; key attributes: carrierType, physicalState, energyContentUnit.
- `generationSource`: a unit that produces a carrier (plant, turbine, panel array); key attributes: technology, capacity, commissioningDate, siteRef.
- `transformationProcess`: a conversion between carriers; key attributes: inputCarrier, outputCarrier, conversionEfficiency.
- `consumptionPoint`: a delivery point where energy is drawn; key attributes: sector, connectionCapacity, profileClass.
- `meterReading`: a quantified measurement at a point over an interval; key attributes: quantity, unit, interval, qualityFlag.
- `storageFacility`: a buffer that shifts a carrier over time; key attributes: storageCapacity, roundTripEfficiency, stateOfCharge.
- `balanceArea`: a grid zone or territory over which supply and demand are reconciled; key attributes: areaCode, carrier, settlementPeriod.
- `interchangeFlow`: a scheduled or measured flow between two balance areas; key attributes: direction, quantity, period.

## Relationships

- `generationSource` -> produces -> `energyCarrier` (n:m): which carriers a unit can deliver.
- `transformationProcess` -> converts -> `energyCarrier` (n:m): input and output carriers of a conversion.
- `consumptionPoint` -> draws -> `energyCarrier` (n:1): the carrier delivered at a point.
- `balanceArea` -> aggregates -> `generationSource` (1:n): units settled within an area.
- `balanceArea` -> aggregates -> `consumptionPoint` (1:n): delivery points settled within an area.
- `storageFacility` -> buffers -> `energyCarrier` (n:1): the carrier a facility stores.
- `interchangeFlow` -> links -> `balanceArea` (n:2): the exporting and importing areas of a flow.

## Events

- `generationRecorded`: a generating unit delivered a quantified amount of a carrier in a period.
- `consumptionMetered`: a meter reading was taken at a consumption point.
- `outageOccurred`: a generation, storage or network asset became unavailable.
- `storageCharged`: a storage facility absorbed energy from the system.
- `storageDischarged`: a storage facility returned energy to the system.
- `interchangeExecuted`: a flow between balance areas was delivered and measured.
- `balancePeriodClosed`: supply, demand, storage and interchange were reconciled for an area and period.

## Contracts

- `meteringDataAccess`: a consumption point owner or their delegate reads interval meter data for that point.
- `aggregateBalanceFeed`: a consumer receives per-area, per-period balance aggregates without per-meter detail.
- `assetRegisterLookup`: resolution of a generation or storage asset's descriptive record by identifier.

## Projections

- `publicEnergyBalance`: national and area-level supply and demand aggregates by carrier; omits all per-asset and per-meter data.
- `gridOperationsView`: near-real-time state of areas, assets and interchange for operations; omits commercial and personal attributes.
- `consumerUsageView`: a single holder's own consumption points and readings; omits everything else.

## Composition

- REFERENCE `world.landParcel` (P2): generation, storage and network assets are sited on identified parcels.
- REFERENCE `world.organization` (O1): operators of assets and balance areas are organizations governed elsewhere.
- REFERENCE `world.emission` (F6): fuel combustion and process activity recorded here serves as activity data for emission quantification.
- COMPOSE `world.money` (F2): imbalance settlement amounts embed the money value object rather than local amount fields.
- imports: IEC CIM (ALIGN): field equivalences for grid assets, measurement and network semantics.
- imports: IEA energy balances (ALIGN): definitions of aggregate balance categories and carrier accounting.

## Stewardship

Grid and asset operators steward the records of their own assets, meters and balance areas, and a statistics office archetype stewards the published aggregates. Access to any record is granted by its steward through the catalogue's S1/S2 ownership and access models, with usage auditable via S4.
