# P8 Ecosystem & Biome

This meta-model describes ecosystems as physical systems: the typology that names them, the mapped assets that give them extent and composition, and the condition, processes and biophysical service capacity that describe how they are doing. It is its own model because an ecosystem is more than the sum of its species records (P6, P7) and more than its substrate (P3, P10): it is a bounded functional unit whose extent and condition change and must be tracked as a stock over time. This model stays strictly biophysical, in area, condition scores and physical flows; monetary appraisal of ecosystem outputs belongs to C7.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p8"
  csn: world.ecosystemAndBiome
  version: 0.2.0
  displayName: "Ecosystem & Biome"
  description: "Ecosystem types and biomes with mapped assets, their extent, composition, condition and biophysical service capacity."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.ecosystemAndBiome
bundles:
  - csn: world.ecosystemAndBiome.typology
    displayName: "Typology"
    layers:
      - world.ecosystemAndBiome.typology.biome
      - world.ecosystemAndBiome.typology.ecosystemType
  - csn: world.ecosystemAndBiome.extent
    displayName: "Extent and composition"
    layers:
      - world.ecosystemAndBiome.extent.ecosystemAsset
      - world.ecosystemAndBiome.extent.compositionAndStructure
      - world.ecosystemAndBiome.extent.extentChange
  - csn: world.ecosystemAndBiome.condition
    displayName: "Condition and function"
    layers:
      - world.ecosystemAndBiome.condition.conditionIndicator
      - world.ecosystemAndBiome.condition.processAndFlux
      - world.ecosystemAndBiome.condition.serviceCapacity
      - world.ecosystemAndBiome.condition.pressureAndDisturbance
imports:
  - source: envo
    version: "*"
  - source: sweet
    version: "*"
  - source: iucn-global-ecosystem-typology
    version: "*"
  - source: un-seea-ecosystem-accounting
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `typology` | What kinds of ecosystem exist and how they nest | `biome`: broad climatic and functional realms · `ecosystemType`: ecosystem classes with diagnostic composition, structure and setting |
| `extent` | Which concrete units exist, where, and how they change | `ecosystemAsset`: mapped ecosystem units with area and boundary · `compositionAndStructure`: dominant taxa, layering, connectivity and fragmentation · `extentChange`: conversions between types and net area change between epochs |
| `condition` | How the system is doing and what it can supply | `conditionIndicator`: indicator definitions with reference levels and units · `processAndFlux`: productivity, water and nutrient cycling, carbon exchange · `serviceCapacity`: physical capacity to supply outputs such as timber increment, pollination, water regulation · `pressureAndDisturbance`: pressures acting on the asset and recorded disturbance |

## Objects

- `biome`: a broad ecological realm; key attributes: identifier, defining climate and functional traits, global extent reference
- `ecosystemType`: a class of ecosystem; key attributes: type identifier, definition, parent biome reference, diagnostic composition, source typology
- `ecosystemAsset`: a mapped ecosystem unit; key attributes: geometry, area, type reference, delineation epoch, mapping confidence
- `conditionIndicator`: a defined measure of ecosystem state; key attributes: indicator identifier, unit, reference level, direction of improvement, applicable types
- `conditionAssessment`: a dated evaluation of an asset; key attributes: asset reference, period, indicator scores, aggregate condition, method reference
- `serviceCapacityMeasure`: a physical supply capacity for an asset; key attributes: output kind, quantity, unit, period, estimation method, sustainability caveat
- `fluxMeasurement`: a measured or modelled process rate; key attributes: process kind, quantity, unit, period, measurement or model reference
- `disturbanceRecord`: an event that altered an asset; key attributes: disturbance kind, extent affected, severity, date, attribution

## Relationships

- `ecosystemAsset` -> classifiedAs -> `ecosystemType` (n:1): each mapped unit carries one type per delineation epoch
- `ecosystemType` -> withinBiome -> `biome` (n:1): types nest into broad realms for aggregation
- `conditionAssessment` -> evaluates -> `ecosystemAsset` (n:1): condition is a dated statement about one unit
- `conditionAssessment` -> scores -> `conditionIndicator` (n:m): assessments carry indicator level results, not just a headline
- `serviceCapacityMeasure` -> quantifiesCapacityOf -> `ecosystemAsset` (n:1): capacity is a physical property of a unit over a period
- `fluxMeasurement` -> observedIn -> `ecosystemAsset` (n:1): process rates are attributed to the unit they were measured in
- `disturbanceRecord` -> affects -> `ecosystemAsset` (n:m): a single event can cut across several units
- `ecosystemAsset` -> adjoins -> `ecosystemAsset` (n:m): adjacency supports connectivity and fragmentation analysis

## Events

- `ecosystemMapPublished`: a new delineation of assets for an area was issued for an epoch
- `ecosystemAssetReclassified`: a unit changed type after reassessment or real conversion
- `ecosystemExtentChanged`: area was gained or lost between epochs, with the conversion recorded
- `conditionAssessmentCompleted`: an assessment cycle produced indicator scores for a set of assets
- `disturbanceObserved`: fire, flood, clearing, storm or infestation altered an asset
- `restorationMilestoneObserved`: a restored unit reached a stated structural or condition threshold
- `serviceCapacityRecomputed`: a capacity estimate was updated after new condition or flux data

## Contracts

- `ecosystemAccountExchangeContract`: terms for supplying extent and condition accounts to a statistics office at a stated grain and cadence
- `monitoringPlotAccessContract`: terms for establishing and reading long-term plots on land held by another party
- `restorationReportingContract`: terms under which an operator reports condition before and after works on an asset

## Projections

- `extentAccount`: area by ecosystem type and period with opening and closing stocks; omits plot-level records and asset geometry detail
- `conditionScorecard`: indicator scores and aggregate condition by type or area; omits raw measurements and site coordinates
- `publicEcosystemMap`: asset boundaries and types for general use; omits sensitive plot locations and provisional delineations

## Composition

- REFERENCE `world.floraAndVegetation` (P6) and `world.faunaAndWildlife` (P7): composition and structure are evidenced by the taxon and cover records held there
- REFERENCE `world.waterBodyAndHydrology` (P3) and `world.soilAndAgriculturalLand` (P10): aquatic and soil substrate define and constrain many ecosystem types
- REFERENCE `world.terrainAndLandform` (P1) and `world.atmosphereWeatherAndClimate` (P4): relief and climate set the setting criteria used by the typology
- REFERENCE `world.naturalPhenomenonAndHazard` (P9): hazard occurrences supply attributed disturbance records
- REFERENCE `world.emissionAndEnvironmentalFlux` (F6): emissions and removals link to the process and flux layer without duplicating its accounting
- REFERENCE `world.resourceExtractionOperations` (K10) and `world.agricultureAndHusbandry` (K9): pressures and conversions originate from operations described there
- REFERENCE `world.officialStatisticsAndIndicators` (N10): published accounts are compiled into indicator series there
- REFERENCE `world.priceValuationAndAppraisal` (C7): monetary appraisal of ecosystem outputs is deliberately out of scope here and belongs to that model
- imports: envo (EXTEND): environment and ecosystem class vocabulary this model specializes
- imports: sweet (ALIGN): earth system process terms for the flux layer
- imports: iucn-global-ecosystem-typology (ALIGN): biome and ecosystem functional group classification
- imports: un-seea-ecosystem-accounting (COMPOSE): the extent and condition account structure used by the projections

## Stewardship

An ecology commons steward maintains the ecosystem register: it publishes the typology, delineates assets, runs or accredits condition monitoring and issues extent and condition accounts. Land holders are not displaced by this description, plot-level and sensitive data are released only through S2 access contracts granted by the steward, and reads are logged in S4.
