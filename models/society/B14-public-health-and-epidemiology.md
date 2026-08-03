# B14 Public Health & Epidemiology

The health of populations: indicator series, notifiable case surveillance, outbreaks and their transmission characteristics, immunization campaigns and coverage, and the public health measures taken in response, all held at cohort grain and never at person grain. It is its own meta-model because population health has its own objects, cadences and disclosure discipline, entirely distinct from the person-owned health record (B10) it statistically summarizes.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:b14"
  csn: world.publicHealthAndEpidemiology
  version: 0.2.0
  displayName: "Public Health & Epidemiology"
  description: "Cohort-grain population health surveillance, outbreaks, immunization and public health measures."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.publicHealthAndEpidemiology
bundles:
  - csn: world.publicHealthAndEpidemiology.surveillance
    displayName: "Surveillance"
    layers:
      - world.publicHealthAndEpidemiology.surveillance.indicatorSeries
      - world.publicHealthAndEpidemiology.surveillance.caseReporting
      - world.publicHealthAndEpidemiology.surveillance.signalDetection
  - csn: world.publicHealthAndEpidemiology.outbreak
    displayName: "Outbreak"
    layers:
      - world.publicHealthAndEpidemiology.outbreak.outbreakLifecycle
      - world.publicHealthAndEpidemiology.outbreak.transmissionCharacterization
  - csn: world.publicHealthAndEpidemiology.immunization
    displayName: "Immunization"
    layers:
      - world.publicHealthAndEpidemiology.immunization.campaign
      - world.publicHealthAndEpidemiology.immunization.coverage
  - csn: world.publicHealthAndEpidemiology.measure
    displayName: "Measure"
    layers:
      - world.publicHealthAndEpidemiology.measure.measureDefinition
      - world.publicHealthAndEpidemiology.measure.effectMonitoring
imports:
  - source: who-icd
    version: "*"
  - source: hl7-fhir
    version: "*"
  - source: who-ihr
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `surveillance` | Watching population health continuously | `indicatorSeries`: time series of health indicators by cohort and area Â· `caseReporting`: intake of de-identified notifiable case reports Â· `signalDetection`: thresholds and anomalies raised from series and reports |
| `outbreak` | Episodes of elevated disease activity | `outbreakLifecycle`: declaration, course and closure of an outbreak Â· `transmissionCharacterization`: cohort-grain transmission patterns, severity and reproduction estimates |
| `immunization` | Preventive campaigns and their reach | `campaign`: planned and running immunization campaigns Â· `coverage`: coverage estimates by cohort, area and antigen |
| `measure` | Interventions and whether they work | `measureDefinition`: defined public health measures and their scope Â· `effectMonitoring`: observed indicator response after introduction and lifting |

## Objects

- `populationHealthIndicator`: one tracked series; key attributes: indicatorCode, cohortDefinition, area, cadence
- `notifiableCaseReport`: a de-identified report of a notifiable condition; key attributes: conditionCode, cohortBand, area, reportedAt, reporterClass
- `healthSignal`: an anomaly raised from surveillance; key attributes: source, detectedAt, severityGrade, status
- `outbreak`: a declared episode of elevated activity; key attributes: conditionCode, declaredAt, affectedArea, phase, closedAt
- `transmissionAssessment`: a cohort-grain characterization of spread; key attributes: outbreakRef, route, reproductionEstimate, severityProfile
- `immunizationCampaign`: a planned preventive effort; key attributes: antigen, targetCohort, area, period
- `coverageEstimate`: measured reach of immunization; key attributes: campaignRef, cohortBand, area, coverageRate, estimatedAt
- `publicHealthMeasure`: an intervention taken; key attributes: kind, scope, introducedAt, liftedAt, legalBasisRef

## Relationships

- `notifiableCaseReport` -> contributesTo -> `populationHealthIndicator` (many-to-many): reports aggregate into several series
- `healthSignal` -> detectedFrom -> `populationHealthIndicator` (many-to-one): signals cite the series that raised them
- `outbreak` -> substantiatedBy -> `healthSignal` (one-to-many): a declaration rests on one or more signals
- `transmissionAssessment` -> characterizes -> `outbreak` (many-to-one): assessments are revised over an outbreak's course
- `publicHealthMeasure` -> respondsTo -> `outbreak` (many-to-one): measures cite the episode they address
- `coverageEstimate` -> measures -> `immunizationCampaign` (many-to-one): coverage is estimated repeatedly per campaign

## Events

- `caseNotified`: a de-identified notifiable case report was received into surveillance
- `signalRaised`: surveillance detected an anomaly worth attention
- `outbreakDeclared`: an episode was formally declared on the basis of signals
- `measureIntroduced`: a public health measure came into force for a scope
- `measureLifted`: a measure was ended
- `campaignLaunched`: an immunization campaign began for a target cohort
- `coverageEstimated`: a coverage figure was computed and published for a cohort
- `outbreakClosed`: a declared episode was formally ended

## Contracts

- `notificationIntakeContract`: terms under which care providers submit notifiable reports, de-identified at intake
- `researchAccessContract`: cohort-grain access for accredited researchers under disclosure control
- `publicDashboardContract`: open publication terms for aggregate indicators
- `internationalReportingContract`: notification of qualifying events to international health bodies

## Projections

- `publicDashboardView`: open aggregate indicators and active measures; omits any small-cell or re-identifiable slice
- `epidemiologistView`: fine-cohort series and outbreak detail under disclosure control; omits person-grain data, which never exists in this model
- `internationalReportView`: the notification subset required across borders; omits domestic operational detail

## Composition

- COMPOSE `world.personalHealth` (B10): consented or legally mandated notifiable facts arrive de-identified and are composed into cohort aggregates; the person-grain record never crosses into this model
- MIX-IN `world.statisticalDisclosure` (S5): cohort-grain aggregation, minimum cell sizes and suppression rules applied to every published series
- COMPOSE `world.eventRegister` (R3): surveillance series and outbreak timelines are kept as append-only event logs
- REFERENCE `world.attestationCertificateAndLicense` (R5): immunization certificates exist at person grain in R5/B10 and are only counted here at cohort grain
- REFERENCE `world.identityRegister` (R4): reporting institutions, not persons, resolve to anchored identities
- imports: who-icd (REFERENCE): condition classification as an externally governed code scheme
- imports: hl7-fhir (ALIGN): alignment of case and immunization semantics with clinical resource definitions
- imports: who-ihr (ALIGN): international notification obligations and event assessment vocabulary

## Stewardship

The public health authority owns the surveillance series, outbreak records and measures, at cohort grain only: this model never holds person-grain data, and the S5 disclosure rules are part of its published shape. Access beyond open dashboards is granted via the S1/S2 access and consent models and audited via S4.
