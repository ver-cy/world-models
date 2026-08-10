# N10 Official Statistics & Indicators

This meta-model describes official statistics: indicators and the series that measure them, observations with vintages and revisions, the censuses and surveys that collect the raw material, the methodologies that make figures comparable, and the releases that publish them under embargo discipline. It is its own model because statistical production has semantics no generic dataset model carries: reference periods, provisional versus final status, revision policy, methodology binding and release calendars.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n10"
  csn: world.officialStatistics
  version: 0.2.0
  displayName: "Official Statistics & Indicators"
  description: "Indicators, statistical series, observations, collections, methodology and disciplined release."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.officialStatistics
bundles:
  - csn: world.officialStatistics.collection
    displayName: "Collection"
    layers:
      - world.officialStatistics.collection.censusAndSurvey
      - world.officialStatistics.collection.methodologyAndClassification
  - csn: world.officialStatistics.series
    displayName: "Series"
    layers:
      - world.officialStatistics.series.indicatorDefinition
      - world.officialStatistics.series.observationAndVintage
  - csn: world.officialStatistics.dissemination
    displayName: "Dissemination"
    layers:
      - world.officialStatistics.dissemination.releaseCalendar
      - world.officialStatistics.dissemination.revisionAndCorrection
imports:
  - source: sdmx
    version: "*"
  - source: ddi
    version: "*"
  - source: gsbpm
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `collection` | Gathering and grounding the numbers | `censusAndSurvey`: collection operations, instruments, coverage · `methodologyAndClassification`: methods, classifications, revision policy |
| `series` | The measured world over time | `indicatorDefinition`: indicators, units, formulas · `observationAndVintage`: time series, observations, vintages |
| `dissemination` | Publishing under discipline | `releaseCalendar`: scheduled releases and embargoes · `revisionAndCorrection`: revisions, corrections, discontinuations |

## Objects

- `indicator`: a defined measurable phenomenon; key attributes: indicatorId, definition, unitRef, computationFormula.
- `statisticalSeries`: a keyed time series measuring an indicator; key attributes: seriesKey, frequency, geographyRef, startPeriod.
- `observation`: one value for one period in a series; key attributes: period, value, statusFlag, vintage.
- `collectionOperation`: a census or survey producing source data; key attributes: operationType, referencePeriod, coverage, responseRate.
- `methodology`: the documented method behind series; key attributes: methodologyDocRef, classificationRefs, revisionPolicy.
- `statisticalRelease`: a scheduled publication act; key attributes: releasedAt, embargoUntil, edition.
- `revision`: a recorded change to a published observation; key attributes: previousValue, newValue, reason, revisedAt.

## Relationships

- `indicator` -> measuredBy -> `statisticalSeries` (1:N): one indicator, many geographies and breakdowns.
- `statisticalSeries` -> contains -> `observation` (1:N): the series body over periods.
- `statisticalSeries` -> sourcedFrom -> `collectionOperation` (N:N): where the numbers come from.
- `statisticalSeries` -> documentedBy -> `methodology` (N:1): the method that makes the series comparable.
- `statisticalRelease` -> publishes -> `statisticalSeries` (N:N): which series each release updates.
- `revision` -> revises -> `observation` (N:1): the audit trail of published numbers.
- `indicator` -> derivedFrom -> `indicator` (N:N): composite indices built from component indicators.

## Events

- `collectionConducted`: a census or survey completed its field phase.
- `seriesEstablished`: a new statistical series was defined and keyed.
- `releasePublished`: a scheduled release made observations public.
- `embargoLifted`: pre-release access restrictions ended at the scheduled moment.
- `observationRevised`: a published value was revised with reason.
- `methodologyChanged`: the documented method behind series changed, breaking or bridging comparability.
- `seriesDiscontinued`: a series stopped being produced.

## Contracts

- `openDisseminationContract`: standard public terms for released aggregate statistics.
- `microdataAccessContract`: controlled research access to underlying microdata under confidentiality obligations.
- `preReleaseAccessContract`: strictly limited embargoed access before publication.

## Projections

- `headlineDashboard`: latest observations of headline indicators; omits vintages and methodology detail.
- `sdmxDataflowExport`: machine-readable series and observations with structure references; omits narrative context.
- `researcherMicrodataView`: anonymized unit-level data under contract; omits direct identifiers and pre-release values.

## Composition

- COMPOSE `world.dataset` (N3): every release is catalogued as a dataset with distributions, while statistical semantics remain here.
- REFERENCE `world.reportStatement` (N2): reported figures from organizations are inputs to series production.
- REFERENCE `world.timeCalendar` (N11): reference periods, frequencies and release calendars.
- REFERENCE `world.documentRecord` (N1): methodology documents are governed records.
- REFERENCE `world.place` (P1): the geographies that key series and collections.
- imports: sdmx (ALIGN): data structure definitions, codelists and dataflows.
- imports: ddi (ALIGN): study and instrument documentation for collection operations.
- imports: gsbpm (ALIGN): the production process phases behind this model's events.

## Stewardship

The neutral owner archetype is the statistics steward, the statistics office class bound as S5 in this catalogue, which owns series, releases and methodology while respondents retain ownership of their source data. Access is always granted through the catalogue's S1/S2 ownership and access models, with microdata and pre-release access audited via S4.
