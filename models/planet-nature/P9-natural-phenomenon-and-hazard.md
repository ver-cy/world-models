# P9 Natural Phenomenon & Hazard

This meta-model describes hazards and what they do: the kinds of hazard and where they can originate, the occurrences that actually happened with their measured intensity and attributed impact, the zones and elements exposed to them, and the alerts issued to people at risk. It is its own model because a hazard is a standing property of a place while an occurrence is a dated event and an alert is a communication act, and confusing the three is the classic failure of risk data. Response operations and casualty management belong to X3, and the atmospheric or hydrological measurements themselves stay in P4 and P3.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p9"
  csn: world.naturalPhenomenonAndHazard
  version: 0.2.0
  displayName: "Natural Phenomenon & Hazard"
  description: "Hazard types and source zones, dated occurrences with intensity and impact, exposure and risk, and issued alerts."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.naturalPhenomenonAndHazard
bundles:
  - csn: world.naturalPhenomenonAndHazard.hazardCharacterization
    displayName: "Hazard characterization"
    layers:
      - world.naturalPhenomenonAndHazard.hazardCharacterization.hazardType
      - world.naturalPhenomenonAndHazard.hazardCharacterization.sourceAndSusceptibility
      - world.naturalPhenomenonAndHazard.hazardCharacterization.intensityMeasure
  - csn: world.naturalPhenomenonAndHazard.occurrence
    displayName: "Occurrence and impact"
    layers:
      - world.naturalPhenomenonAndHazard.occurrence.occurrenceRecord
      - world.naturalPhenomenonAndHazard.occurrence.impactAndLoss
  - csn: world.naturalPhenomenonAndHazard.exposure
    displayName: "Exposure and risk"
    layers:
      - world.naturalPhenomenonAndHazard.exposure.exposureZone
      - world.naturalPhenomenonAndHazard.exposure.elementAtRisk
      - world.naturalPhenomenonAndHazard.exposure.riskScenario
  - csn: world.naturalPhenomenonAndHazard.alerting
    displayName: "Alerting"
    layers:
      - world.naturalPhenomenonAndHazard.alerting.alertMessage
      - world.naturalPhenomenonAndHazard.alerting.disseminationChannel
imports:
  - source: oasis-cap
    version: "*"
  - source: em-dat
    version: "*"
  - source: undrr-isc-hazard-information-profiles
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `hazardCharacterization` | What can happen here and how it is measured | `hazardType`: the catalogue of hazard kinds with definitions and onset behaviour Â· `sourceAndSusceptibility`: source zones, fault traces, susceptibility surfaces and triggering conditions Â· `intensityMeasure`: the scales and units in which severity is expressed |
| `occurrence` | What actually happened and what it cost | `occurrenceRecord`: dated events with location, extent and measured intensity Â· `impactAndLoss`: attributed damage, disruption and affected counts |
| `exposure` | Who and what stands in the way | `exposureZone`: mapped zones for a hazard type and return level Â· `elementAtRisk`: the assets, networks and population units within a zone Â· `riskScenario`: modelled combinations of hazard level and exposure with expected consequence |
| `alerting` | What was communicated, to whom and when | `alertMessage`: graded alerts with area, onset, certainty, expiry and status Â· `disseminationChannel`: the routes an alert travelled and their delivery confirmations |

## Objects

- `hazardType`: a kind of hazard; key attributes: identifier, definition, onset speed, typical duration, source classification
- `hazardSourceZone`: an area or feature capable of generating a hazard; key attributes: geometry, hazard type reference, recurrence characterization, susceptibility class
- `hazardOccurrence`: a dated event; key attributes: hazard type reference, start and end time, footprint geometry, peak intensity, confidence of attribution
- `intensityObservation`: a measurement of severity during an occurrence; key attributes: measure reference, value, location, timestamp, source of measurement
- `exposureZone`: an area exposed at a stated level; key attributes: geometry, hazard type reference, return level, delineation method, version
- `elementAtRisk`: a thing exposed within a zone; key attributes: element reference, element class, vulnerability class, replacement or capacity descriptor
- `riskScenario`: a modelled hazard and exposure combination; key attributes: hazard level, exposure set, expected consequence, model reference, assumptions
- `impactRecord`: attributed consequence of an occurrence; key attributes: impact category, quantity, unit, area, attribution confidence, reporting source
- `alert`: a graded public notice; key attributes: hazard type, severity, urgency, certainty, area, onset, expiry, status, message reference

## Relationships

- `hazardOccurrence` -> ofType -> `hazardType` (n:1): every event is an instance of a catalogued hazard kind
- `hazardOccurrence` -> originatesIn -> `hazardSourceZone` (n:1): events are attributed to a source where one is identifiable
- `intensityObservation` -> measures -> `hazardOccurrence` (n:1): severity values attach to the event, with their own measurement source
- `exposureZone` -> delineatedFor -> `hazardType` (n:1): zones are always zone for a specific hazard and return level
- `elementAtRisk` -> locatedIn -> `exposureZone` (n:m): an element can fall in several zones for different hazards
- `impactRecord` -> attributedTo -> `hazardOccurrence` (n:1): losses are booked against the event that caused them
- `alert` -> warnsOf -> `hazardType` (n:1): alerts name the hazard and the area they cover
- `riskScenario` -> combines -> `elementAtRisk` (n:m): scenarios join a hazard level with a defined exposure set

## Events

- `hazardOccurrenceDetected`: monitoring or report established that an event was underway
- `alertIssued`: a graded notice was published for an area with onset, certainty and expiry
- `alertUpdated`: severity, area or timing of an active notice changed
- `alertCancelled`: an active notice was withdrawn or allowed to expire
- `hazardOccurrenceClosed`: the event was declared over and its footprint finalized
- `impactAssessmentFiled`: attributed damage and affected counts were reported for an occurrence
- `exposureZoneRevised`: a zone was redrawn after new occurrence data or a new model version
- `returnPeriodRecalculated`: frequency statistics for a hazard and area were updated with a longer record

## Contracts

- `alertFeedContract`: terms for redistribution of alerts to broadcasters, applications and neighbouring registers, including no-alteration and timeliness conditions
- `exposureContributionContract`: terms under which asset registers contribute elements at risk, including grain, refresh and confidentiality limits
- `lossReportingContract`: terms for reporting attributed impact into the occurrence record, including definitions and revision windows
- `sensorAndDetectionFeedContract`: terms for real-time detection feeds from monitoring networks operated by others

## Projections

- `publicAlertFeed`: current alerts with area, severity and plain-language guidance; omits internal deliberation and contributing sensor diagnostics
- `planningHazardZoneMap`: zones and return levels for planning use; omits identified elements at risk and their holders
- `lossStatisticsSeries`: impact totals per occurrence and period; omits per-holder and per-address detail

## Composition

- REFERENCE `world.atmosphereWeatherAndClimate` (P4): meteorological warnings and observed intensities feed occurrence and alerting here
- REFERENCE `world.waterBodyAndHydrology` (P3): flood and drought occurrences are characterized against flow regimes and thresholds
- REFERENCE `world.terrainAndLandform` (P1) and `world.soilAndAgriculturalLand` (P10): slope, relief and soil state underpin susceptibility surfaces
- REFERENCE `world.subsurfaceAndMineralResource` (P5): seismic and volcanic source zones rest on the structures modelled there
- REFERENCE `world.ecosystemAndBiome` (P8): disturbance records there are the ecological face of occurrences here
- REFERENCE `world.buildingAndStructure` (U1), `world.physicalInfrastructureNetwork` (U3) and `world.populationGroupAndCommunity` (H3): elements at risk are referenced, never copied in full
- REFERENCE `world.incidentAndEmergency` (X3): response, deployment and casualty management continue there from the occurrence recorded here
- REFERENCE `world.insuranceAndRiskPooling` (C8): pooled cover and claims consume scenarios and loss records without being part of this model
- REFERENCE `world.disclosureScopeAndProjectionPolicy` (S3): the aggregation rules protecting exposed parties are defined there
- imports: oasis-cap (EXTEND): the alert message structure, severity, urgency and certainty this model specializes
- imports: em-dat (ALIGN): event and loss recording categories for comparability of occurrence statistics
- imports: undrr-isc-hazard-information-profiles (REFERENCE): the hazard type catalogue referenced rather than re-invented

## Stewardship

A hazard monitoring steward maintains the characterization, occurrence and exposure register and an emergency management operator issues and withdraws alerts, each accountable for what it publishes. Exposure contributions stay owned by the registers that supplied them under S1, disclosure of identified elements at risk happens only through S2 access contracts shaped by S3, and every read is logged in S4.
