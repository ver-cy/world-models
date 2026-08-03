# P4 Atmosphere Weather & Climate

This meta-model describes the state of the atmosphere: what was observed, what is predicted, and what the long record says is normal. It holds observing stations and their measurements, gridded and remotely sensed fields, forecast products and the warnings drawn from them, and the homogenized series and normals that make decades comparable. It is its own model because weather is a continuously refreshed observation stream while climate is a curated statistical archive, and both must live under one identity so that a warning, a forecast and a normal for the same place can be reconciled. Hazard consequence and exposure are modelled in P9; here the subject is the atmospheric state itself.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p4"
  csn: world.atmosphereWeatherAndClimate
  version: 0.2.0
  displayName: "Atmosphere Weather & Climate"
  description: "Atmospheric observations, gridded and remotely sensed fields, forecasts and warnings, and the climate record derived from them."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.atmosphereWeatherAndClimate
bundles:
  - csn: world.atmosphereWeatherAndClimate.observation
    displayName: "Observation"
    layers:
      - world.atmosphereWeatherAndClimate.observation.stationNetwork
      - world.atmosphereWeatherAndClimate.observation.surfaceAndUpperAir
      - world.atmosphereWeatherAndClimate.observation.remoteSensing
      - world.atmosphereWeatherAndClimate.observation.atmosphericComposition
  - csn: world.atmosphereWeatherAndClimate.forecast
    displayName: "Forecast and warning"
    layers:
      - world.atmosphereWeatherAndClimate.forecast.numericalPrediction
      - world.atmosphereWeatherAndClimate.forecast.productAndBulletin
      - world.atmosphereWeatherAndClimate.forecast.warningAndAdvisory
  - csn: world.atmosphereWeatherAndClimate.climatology
    displayName: "Climatology"
    layers:
      - world.atmosphereWeatherAndClimate.climatology.homogenizedSeries
      - world.atmosphereWeatherAndClimate.climatology.normalsAndExtremes
imports:
  - source: wmo
    version: "*"
  - source: cf-conventions
    version: "*"
  - source: iso-19156-observations-and-measurements
    version: "*"
  - source: ogc-sensorthings-api
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `observation` | What was measured, by what, where and how well | `stationNetwork`: observing sites, instruments, exposure class and operating history Â· `surfaceAndUpperAir`: direct measurements at the surface and through the profile Â· `remoteSensing`: radar, satellite and lidar derived fields with their retrieval method Â· `atmosphericComposition`: aerosols, ozone and greenhouse gas concentrations |
| `forecast` | What is expected and what is communicated about it | `numericalPrediction`: model runs, ensembles, initialization and lead times Â· `productAndBulletin`: published forecast products for areas, points and routes Â· `warningAndAdvisory`: severity-graded warnings with area, onset, certainty and expiry |
| `climatology` | What the long record says | `homogenizedSeries`: quality-controlled long series with break adjustments and lineage Â· `normalsAndExtremes`: reference-period normals, records and exceedance statistics |

## Objects

- `observingStation`: a site producing atmospheric measurements; key attributes: station identifier, location, elevation, instrument set, exposure class, operating period
- `observedVariable`: the quantity being measured; key attributes: standard name, unit, sampling interval, measurement height, uncertainty
- `weatherObservation`: a measured value at a place and time; key attributes: timestamp, station reference, variable reference, value, quality flag, correction status
- `griddedField`: a spatial field of an atmospheric variable; key attributes: variable, grid geometry, valid time, source (analysis, retrieval, model), resolution
- `forecastProduct`: a published prediction for an area or point; key attributes: issue time, valid period, lead time, variables, confidence expression
- `warning`: a graded notice of expected hazardous weather; key attributes: phenomenon, severity, certainty, urgency, area geometry, onset, expiry, status
- `climateSeries`: a long, quality-controlled record for a site or area; key attributes: variable, period of record, homogenization method, break points, completeness
- `climateNormal`: a statistic over a reference period; key attributes: variable, reference period, statistic type, value, computation method

## Relationships

- `weatherObservation` -> recordedAt -> `observingStation` (n:1): each value carries the site that produced it
- `weatherObservation` -> quantifies -> `observedVariable` (n:1): values are meaningless without the standard-named quantity and unit
- `griddedField` -> assimilates -> `weatherObservation` (n:m): analyses and retrievals declare the observations behind them
- `forecastProduct` -> initializedFrom -> `griddedField` (n:m): products trace to the analysis and model run they came from
- `warning` -> derivedFrom -> `forecastProduct` (n:1): a warning names the prediction that justified it
- `climateSeries` -> aggregates -> `weatherObservation` (1:n): the long record is built from validated observations
- `climateNormal` -> computedFrom -> `climateSeries` (n:1): normals are always tied to the series and period used
- `observingStation` -> succeededBy -> `observingStation` (n:1): relocations and replacements form a traceable site lineage

## Events

- `observationRecorded`: a measurement was taken and entered the observation stream
- `observationCorrected`: a previously published value was flagged, adjusted or withdrawn after quality control
- `forecastRunCompleted`: a prediction cycle finished and its fields became available for products
- `warningIssued`: a graded notice was published for an area, with onset and expiry
- `warningUpdatedOrCancelled`: an active notice was upgraded, downgraded, extended or withdrawn
- `stationCommissionedOrRelocated`: an observing site started, moved or changed instrumentation, creating a potential series break
- `seriesHomogenizationApplied`: an adjustment was applied to a long record to remove a non-climatic break
- `recordValueSet`: an observation exceeded the previous extreme for a site or area

## Contracts

- `observationFeedContract`: terms for push or pull delivery of the observation stream, including latency, quality flags and correction handling
- `warningDisseminationContract`: terms for redistributing warnings to broadcasters and applications, including timeliness and no-alteration conditions
- `forecastProductLicense`: terms for reuse of published forecast products, including attribution and derived-product rules
- `climateArchiveAccessContract`: terms for bulk access to long series and normals, including citation of version and homogenization method

## Projections

- `publicForecastView`: point and area forecasts with plain severity language; omits model internals, ensemble members and station diagnostics
- `warningFeed`: machine-readable current warnings with area, severity, onset and expiry; omits the forecasting rationale and internal deliberation
- `climateNormalsTable`: normals and extremes per site and reference period; omits raw uncorrected observations
- `stationMetadataCatalogue`: site, instrument and exposure history for data users; omits measured values

## Composition

- REFERENCE `world.naturalPhenomenonAndHazard` (P9): warnings and observed severity feed hazard occurrence and alerting
- REFERENCE `world.waterBodyAndHydrology` (P3): precipitation and evaporation fields drive catchment balance and flood response
- REFERENCE `world.ecosystemAndBiome` (P8) and `world.agricultureAndHusbandry` (K9): condition and growing-season models consume normals and observations
- REFERENCE `world.spaceAndOrbitalObjects` (P11): satellite platforms and space weather bound the upper end of this model
- REFERENCE `world.energy` (F1) and `world.passengerMobilityAndTransit` (F7): operational consumers of forecasts and warnings
- REFERENCE `world.observedPhenomenon` (X2): recurring atmospheric patterns are described there using series published here
- REFERENCE `world.timeAndCalendarReference` (N11): valid times, reference periods and time zones resolve there
- REFERENCE `world.officialStatisticsAndIndicators` (N10): climate indicators are compiled from these series under statistical methodology
- imports: wmo (EXTEND): observing practice, station identification and warning grading this model specializes
- imports: cf-conventions (ALIGN): standard names and units for every observed and modelled variable
- imports: iso-19156-observations-and-measurements (COMPOSE): the observation, procedure and result pattern
- imports: ogc-sensorthings-api (REFERENCE): a delivery shape for sensor-sourced observation streams

## Stewardship

An ecology commons steward operates the observing and forecasting register: it runs or accredits stations, publishes forecasts, warnings and the climate archive, and states the quality of each product. Restricted feeds, pre-validation data and commercially licensed products are released through S2 access contracts granted by the steward, and reads are recorded in S4.
