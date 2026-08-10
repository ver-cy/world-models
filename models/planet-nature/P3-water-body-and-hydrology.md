# P3 Water Body & Hydrology

This meta-model describes surface and subsurface water as physical objects and as regimes: rivers, lakes, seas, wetlands and aquifers, the catchments that feed them, the flows and levels they carry through the year, and the measured quality of the water itself. It is its own model because a water body is a connected, moving system whose identity survives changes of level and course, and because the network topology of upstream and downstream relations is the basis for almost every other water question. Supply chains and treatment are described in F4, and abstraction rights are granted elsewhere; here the subject is the water and its behaviour.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p3"
  csn: world.waterBodyAndHydrology
  version: 0.2.0
  displayName: "Water Body & Hydrology"
  description: "Rivers, lakes, seas, wetlands and aquifers with their catchments, flow regimes and measured quality."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.waterBodyAndHydrology
bundles:
  - csn: world.waterBodyAndHydrology.hydrography
    displayName: "Hydrography and network"
    layers:
      - world.waterBodyAndHydrology.hydrography.waterFeature
      - world.waterBodyAndHydrology.hydrography.catchment
      - world.waterBodyAndHydrology.hydrography.networkTopology
      - world.waterBodyAndHydrology.hydrography.aquifer
  - csn: world.waterBodyAndHydrology.regime
    displayName: "Flow regime and balance"
    layers:
      - world.waterBodyAndHydrology.regime.flowAndLevel
      - world.waterBodyAndHydrology.regime.waterBalance
      - world.waterBodyAndHydrology.regime.extremeStatistics
  - csn: world.waterBodyAndHydrology.quality
    displayName: "Water quality and status"
    layers:
      - world.waterBodyAndHydrology.quality.physicoChemical
      - world.waterBodyAndHydrology.quality.biologicalStatus
imports:
  - source: ogc-hy-features
    version: "*"
  - source: inspire
    version: "*"
  - source: iso-19156-observations-and-measurements
    version: "*"
  - source: ogc-waterml
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `hydrography` | What water bodies exist, where they are and how they connect | `waterFeature`: rivers, lakes, seas, wetlands and springs as identified features · `catchment`: drainage areas and their nesting · `networkTopology`: upstream and downstream connectivity between features and nodes · `aquifer`: subsurface water bodies, their extent and confinement |
| `regime` | How much water moves, when, and how variable it is | `flowAndLevel`: discharge, stage, tide and groundwater level observations · `waterBalance`: inflow, outflow, storage, recharge and abstraction returns over a period · `extremeStatistics`: flood and low-flow frequency, return periods and seasonality |
| `quality` | What the water contains and what state that implies | `physicoChemical`: sampled determinands, concentrations and methods · `biologicalStatus`: indicator communities and classified ecological status |

## Objects

- `waterBody`: an identified body or reach of water; key attributes: identifier, feature type, geometry, permanence (perennial, seasonal, ephemeral), salinity class
- `watershed`: a drainage area contributing to an outlet; key attributes: identifier, geometry, area, outlet node reference, parent watershed reference
- `hydroNode`: a junction, outlet, confluence or control point in the network; key attributes: coordinates, node type, upstream and downstream references
- `gaugingStation`: an installed monitoring point; key attributes: station identifier, location, measured variables, operating period, rating curve reference
- `flowObservation`: a measurement of discharge, stage or level; key attributes: timestamp, variable, value, unit, quality flag, method
- `flowRegime`: a characterization of a water body over a reference period; key attributes: period, mean flow, low flow index, seasonality pattern, variability
- `aquifer`: a subsurface unit holding recoverable water; key attributes: identifier, extent, confinement, storativity, recharge estimate
- `waterQualitySample`: a sample and its analysis; key attributes: sampling point, timestamp, determinand set, results, laboratory reference, detection limits

## Relationships

- `waterBody` -> drains -> `watershed` (n:1): each reach or body belongs to the drainage area that feeds it
- `waterBody` -> flowsInto -> `waterBody` (n:1): downstream connectivity forms the surface network
- `watershed` -> nestedIn -> `watershed` (n:1): catchments form a hierarchy from sub-catchment to basin
- `gaugingStation` -> monitors -> `waterBody` (n:1): a station reports for a named body or reach
- `flowObservation` -> measuredAt -> `gaugingStation` (n:1): every reading carries the station that produced it
- `flowRegime` -> characterizes -> `waterBody` (n:1): regimes are period-bounded summaries of a body
- `waterQualitySample` -> takenFrom -> `waterBody` (n:1): samples name the body or aquifer sampled
- `aquifer` -> underlies -> `watershed` (n:m): groundwater units cross surface catchment divides

## Events

- `gaugeReadingRecorded`: a station reported a level, discharge or groundwater value for a moment in time
- `floodStageExceeded`: an observed level crossed a defined threshold at a station
- `lowFlowThresholdCrossed`: flow fell below a stated low-flow reference for a reach
- `waterBodyDelineationRevised`: the geometry or identity of a body or catchment was redrawn after new evidence
- `channelCourseChanged`: a river changed course, or an avulsion or channel migration was mapped
- `qualitySampleAnalyzed`: laboratory results for a sample became available and were attached to the sampling point
- `ecologicalStatusReclassified`: the classified status of a body changed after an assessment cycle

## Contracts

- `hydrometricFeedContract`: terms for real-time or near-real-time delivery of station readings, including latency, quality flags and outage notice
- `qualityLaboratoryExchangeContract`: terms for laboratories submitting analyses, covering method declaration, detection limits and re-analysis
- `transboundaryBasinExchange`: terms for exchanging flow and quality data with a neighbouring register for a shared basin
- `abstractionReturnDisclosure`: terms under which operators report abstracted and returned volumes at agreed grain

## Projections

- `publicRiverLevelView`: current level, flow and threshold status by station; omits raw sensor diagnostics and provisional unvalidated values
- `catchmentBalanceSummary`: inflow, outflow, storage change and recharge per catchment and period; omits point-level observations
- `qualityStatusMap`: classified status by water body; omits sample-level results, sampler identity and site coordinates for sensitive points

## Composition

- REFERENCE `world.terrainAndLandform` (P1): catchment boundaries and flow direction derive from the published elevation surface
- REFERENCE `world.subsurfaceAndMineralResource` (P5): aquifers are hosted in geological units described there
- REFERENCE `world.soilAndAgriculturalLand` (P10): infiltration, runoff and nutrient loading link soil state to water response
- REFERENCE `world.ecosystemAndBiome` (P8): aquatic and riparian ecosystems are assessed against the bodies defined here
- REFERENCE `world.naturalPhenomenonAndHazard` (P9): flood and drought occurrences are characterized against flow regimes and thresholds
- REFERENCE `world.atmosphereWeatherAndClimate` (P4): precipitation and evaporation observations drive the water balance
- REFERENCE `world.waterAndFoodSupply` (F4) and `world.emissionAndEnvironmentalFlux` (F6): abstraction, treatment and discharge are described there and reference bodies here
- REFERENCE `world.physicalInfrastructureNetwork` (U3): dams, weirs, canals and levees are engineered structures that modify the regime
- imports: ogc-hy-features (EXTEND): the hydrologic feature and catchment backbone this model specializes
- imports: inspire (ALIGN): hydrography theme for cross-register comparability
- imports: iso-19156-observations-and-measurements (COMPOSE): the observation, procedure and result pattern used by readings and samples
- imports: ogc-waterml (ALIGN): time series exchange shape for hydrometric feeds

## Stewardship

An ecology commons steward keeps the hydrological register: it delineates bodies and catchments, operates or accredits monitoring, and publishes regimes and status classifications, without holding any claim over the water itself. Access to restricted station feeds, sensitive sampling locations or pre-validation data is granted by the steward through S2 access contracts, and reads are logged in S4.
