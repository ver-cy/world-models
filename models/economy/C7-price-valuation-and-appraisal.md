# C7 Price Valuation & Appraisal

This meta-model describes how the world records what things cost and what they are judged to be worth: individual price observations, professional appraisals of specific subjects, composite price indices, and the methodologies behind all three. It is its own model because price knowledge is produced by observers, appraisers and index compilers, is distinct from the transactions it describes, and is consumed by insurance, procurement and statistics as an independent evidence stream.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:c7"
  csn: world.priceValuation
  version: 0.2.0
  displayName: "Price Valuation & Appraisal"
  description: "Price observations, appraisals, indices and the methodologies that produce them."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.priceValuation
bundles:
  - csn: world.priceValuation.observation
    displayName: "Observation"
    layers:
      - world.priceValuation.observation.pricePoint
      - world.priceValuation.observation.sourcing
  - csn: world.priceValuation.appraisal
    displayName: "Appraisal"
    layers:
      - world.priceValuation.appraisal.engagement
      - world.priceValuation.appraisal.opinionOfValue
  - csn: world.priceValuation.index
    displayName: "Index"
    layers:
      - world.priceValuation.index.seriesDefinition
      - world.priceValuation.index.release
  - csn: world.priceValuation.methodology
    displayName: "Methodology"
    layers:
      - world.priceValuation.methodology.methodSpecification
imports:
  - source: sdmx
    version: "*"
  - source: appraisal-standards
    version: "*"
  - source: iso-4217
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `observation` | Single recorded prices | `pricePoint`: observed transaction prices, quotes and listings Â· `sourcing`: sources, sampling frames and collection runs |
| `appraisal` | Judged worth of a specific subject | `engagement`: the assignment, its subject and purpose Â· `opinionOfValue`: the concluded value, its basis and date |
| `index` | Composite price series | `seriesDefinition`: index scope, basket and weighting Â· `release`: compiled values, revisions and rebasing |
| `methodology` | How numbers are produced | `methodSpecification`: approaches, models and standards conformance |

## Objects

- `priceObservation`: a single recorded price; key attributes: amount, currency, observed date, observation kind (transaction, quote, listing).
- `priceSource`: where observations come from; key attributes: source kind, coverage, reliability grade.
- `appraisalEngagement`: a commissioned valuation assignment; key attributes: client reference, purpose, effective date, scope.
- `valuationSubject`: the thing being valued; key attributes: subject kind, external referent link, description as inspected.
- `valueOpinion`: the concluded professional opinion; key attributes: amount, currency, basis of value, opinion date, validity.
- `priceIndex`: a defined composite series; key attributes: name, scope, base period, frequency.
- `indexRelease`: one compiled publication of an index; key attributes: period, value, revision state, release date.
- `methodology`: a documented method; key attributes: approach, version, standards conformance, adoption date.

## Relationships

- `priceObservation` -> collectedFrom -> `priceSource` (n:1): provenance of every observation.
- `appraisalEngagement` -> concerns -> `valuationSubject` (n:1): what the assignment values.
- `valuationSubject` -> resolvesTo -> `world.landParcel` (n:1): the external referent, for example a parcel (P2), an organization asset (O1) or another catalogue entity.
- `valueOpinion` -> concludes -> `appraisalEngagement` (1:1): the outcome of the assignment.
- `indexRelease` -> publishes -> `priceIndex` (n:1): each release instantiates one series for one period.
- `priceObservation` -> aggregatedInto -> `indexRelease` (n:m): observations feeding a compiled value.
- `appraisalEngagement` -> governedBy -> `methodology` (n:1): the method applied; indices are governed the same way.

## Events

- `priceObserved`: a price point was recorded from a source.
- `observationCorrected`: a recorded observation was corrected or invalidated.
- `appraisalCommissioned`: a valuation assignment was accepted.
- `valueOpinionIssued`: a concluded opinion was delivered.
- `indexReleased`: an index value for a period was published.
- `indexRevised`: a published index value was revised or the series was rebased.
- `methodologyAdopted`: a method or its new version came into use.

## Contracts

- `observationContribution`: sources contribute price points under agreed terms and quality rules.
- `indexSubscription`: consumers receive index releases and a defined depth of history.
- `appraisalReliance`: named third parties may rely on a value opinion within its stated scope and validity.

## Projections

- `marketBoard`: headline index values and movements; omits underlying observations.
- `appraisalSummary`: concluded value, basis and date; omits working papers and comparables.
- `researchExtract`: anonymized observation series for analysis; omits source identities.

## Composition

- REFERENCE `world.organization` (O1): observing, appraising and index-compiling organizations, and organizations whose assets are valued.
- REFERENCE `world.commercialContract` (O5): executed agreements are a class of price source under contribution contracts.
- REFERENCE `world.landParcel` (P2): parcels and buildings as frequent valuation subjects.
- REFERENCE note: `world.insurance` (C8) REFERENCEs this model for insured values and loss quantification.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): ownership and access grants over observations, opinions and series.
- MIX-IN `world.auditTrail` (S4): audit facets on corrections, revisions and method changes.
- imports: sdmx (ALIGN): statistical data and metadata exchange shapes for series and releases.
- imports: appraisal-standards (ALIGN): appraisal practice vocabulary including bases of value.
- imports: iso-4217 (REFERENCE): currency codes on every amount.

## Stewardship

The observing, appraising or compiling organization owns its observations, opinions and indices; subjects of valuation are identified by reference and do not own the opinion. Access is granted by the owner under the S1/S2 models of this catalogue.
