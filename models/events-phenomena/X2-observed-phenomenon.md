# X2 Observed Phenomenon

This meta-model describes recurring natural and social patterns as observed things: the phenomenon definition, the observation series that track it, the methods behind those series, the spatial extent over which it manifests, and the trends and anomalies derived from the data. It is its own model because patterns differ from happenings: an individual heavy rainfall is an X1 occurrence, while the rainfall regime it belongs to lives here, with its own methods, series and stewardship.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:x2"
  csn: world.observedPhenomenon
  version: 0.2.0
  displayName: "Observed Phenomenon"
  description: "Recurring natural and social patterns, the observation series that track them and the trends derived from them."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.observedPhenomenon
bundles:
  - csn: world.observedPhenomenon.phenomenon
    displayName: "Phenomenon"
    layers:
      - world.observedPhenomenon.phenomenon.definition
      - world.observedPhenomenon.phenomenon.extent
  - csn: world.observedPhenomenon.observation
    displayName: "Observation"
    layers:
      - world.observedPhenomenon.observation.series
      - world.observedPhenomenon.observation.method
  - csn: world.observedPhenomenon.analysis
    displayName: "Analysis"
    layers:
      - world.observedPhenomenon.analysis.trend
      - world.observedPhenomenon.analysis.anomaly
imports:
  - source: w3c-ssn
    version: "*"
  - source: sdmx
    version: "*"
  - source: iso-19156-om
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `phenomenon` | What the recurring pattern is and where it holds | `definition`: the pattern, its kind and unit of measure · `extent`: the territory over which it manifests |
| `observation` | How the pattern is measured | `series`: ordered observation sets under one method · `method`: protocols, instruments and uncertainty |
| `analysis` | What the measurements say | `trend`: direction and rate estimates over periods · `anomaly`: departures from the established pattern |

## Objects

- `phenomenon`: a recurring natural or social pattern worth observing (rainfall regime, migration flow, traffic congestion); key attributes: phenomenonKind, definition, unitOfMeasure
- `observationSeries`: an ordered set of observations of one phenomenon under one method; key attributes: cadence, startedAt, status
- `observation`: one dated measurement or count; key attributes: observedAt, value, quality
- `observationMethod`: the protocol and instrumentation by which observations are made; key attributes: methodKind, instrumentRef, uncertainty
- `spatialExtent`: the territory a series covers or the phenomenon manifests over; key attributes: extentRef, resolution
- `trendEstimate`: a derived statement of direction and rate over a period; key attributes: period, direction, rate, confidence
- `anomaly`: a departure of observations from the established pattern; key attributes: detectedAt, magnitude, persistence

## Relationships

- `observationSeries` -> observes -> `phenomenon` (n:1): several series under different methods can track one pattern
- `observation` -> belongsTo -> `observationSeries` (n:1): every value sits in exactly one series
- `observationSeries` -> follows -> `observationMethod` (n:1): a series is defined by one method; method changes start a new series or a revision
- `observationSeries` -> covers -> `spatialExtent` (n:1): the territory the series is valid for
- `trendEstimate` -> derivedFrom -> `observationSeries` (n:m): trends can combine several series
- `anomaly` -> departsFrom -> `trendEstimate` (n:1): an anomaly is stated against an established trend
- `phenomenon` -> instantiatedBy -> `occurrence` (n:m): individual X1 occurrences instantiate the recurring pattern

## Events

- `seriesEstablished`: a new observation series was set up with a declared method and extent
- `observationRecorded`: a dated value entered a series
- `methodRevised`: the protocol behind a series changed, with a break marker recorded
- `trendPublished`: a trend estimate was derived and released
- `anomalyDetected`: observations departed from the established pattern beyond threshold
- `seriesDiscontinued`: a series was closed and archived

## Contracts

- `openObservationLicense`: public release of series and trends under open terms
- `researchAccessAgreement`: steward-granted access to raw observations and method detail for research
- `feedSubscriptionContract`: continuous delivery of new observations and anomaly notices to a subscriber

## Projections

- `indicatorDashboardProjection`: latest values and trend direction per phenomenon; omits raw observations and method detail
- `longRunSeriesProjection`: full historical series for analysis; omits provisional and unvalidated values
- `extentMapProjection`: where each phenomenon currently manifests; omits time series depth

## Composition

- REFERENCE `world.occurrenceEvent` (X1): individual occurrences instantiating the pattern are recorded there
- REFERENCE `world.situationCondition` (X4): a persistent manifestation over an extent can be mirrored as a situation while it holds
- REFERENCE `world.settlementUrbanForm` (U4): social and urban phenomena often take settlements and districts as their extents
- REFERENCE `world.auditTrail` (S4): method revisions and series breaks are audited there
- imports: w3c-ssn (EXTEND: observation, sensor and procedure semantics)
- imports: iso-19156-om (ALIGN: observation and measurement structure)
- imports: sdmx (ALIGN: statistical series exchange for publication)

## Stewardship

The owner archetype is the observing steward: an observatory, monitoring service or statistics office that defines phenomena and maintains series. The steward grants access per S1/S2; open publication happens under the open observation license with method and break metadata intact.