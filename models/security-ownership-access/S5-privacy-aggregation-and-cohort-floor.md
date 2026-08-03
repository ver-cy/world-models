# S5 Privacy Aggregation & Cohort Floor

This meta-model describes how the state of a population is sensed without exposing any person in it: statistics are computed over cohorts, never below a minimum cohort size, with suppression and noise where counts run thin. It is its own model because aggregation is a distinct trade with its own artifacts: cohort definitions, k-floors, noise budgets and disclosure review are reusable machinery that many consumers rely on, and the guarantees only hold if that machinery is modelled and checked in one place.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s5"
  csn: world.privacyAggregation
  version: 0.2.0
  displayName: "Privacy Aggregation & Cohort Floor"
  description: "Population sensing at cohort grain: k-anonymity floors, suppression, noise budgets and reviewed statistical releases."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.privacyAggregation
bundles:
  - csn: world.privacyAggregation.cohort
    displayName: "Cohort"
    layers:
      - world.privacyAggregation.cohort.definition
      - world.privacyAggregation.cohort.floors
  - csn: world.privacyAggregation.computation
    displayName: "Computation"
    layers:
      - world.privacyAggregation.computation.measures
      - world.privacyAggregation.computation.protection
  - csn: world.privacyAggregation.release
    displayName: "Release"
    layers:
      - world.privacyAggregation.release.review
      - world.privacyAggregation.release.publication
imports:
  - source: differential-privacy-practice
    version: "*"
  - source: sdmx
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `cohort` | Which population slices may be looked at | `definition`: dimensions, membership rules and validity windows of cohorts Â· `floors`: minimum cohort sizes per sensitivity of the underlying data |
| `computation` | Turning members into numbers safely | `measures`: statistics computed over cohorts and their methods Â· `protection`: cell suppression, noise addition and privacy budget accounting |
| `release` | What actually leaves | `review`: pre-release disclosure checks against floors and budgets Â· `publication`: released series with method and provenance attached |

## Objects

- `cohort`: a population subset defined by dimensions; key attributes: dimensions, membership rule, member count, validity window.
- `kFloor`: a minimum cohort size rule; key attributes: threshold, applicable sensitivity tier, rationale, review cadence.
- `aggregateMeasure`: one statistic computed over a cohort; key attributes: measure kind, value, period, method reference.
- `suppressionRule`: the condition under which cells are withheld or merged; key attributes: trigger, action (suppress, merge, coarsen), scope.
- `noiseBudget`: privacy loss accounting for a source over a period; key attributes: budget, spent, period, accounting method.
- `releaseCandidate`: an assembled set of measures awaiting disclosure review; key attributes: contents, requested by, review state.
- `publishedSeries`: a released statistical series; key attributes: series identity, periods, method summary, provenance.

## Relationships

- `aggregateMeasure` -> computedOver -> `cohort` (*..1): every number names the cohort it summarizes.
- `cohort` -> constrainedBy -> `kFloor` (*..1): a cohort below its floor yields no measure at all.
- `releaseCandidate` -> assembles -> `aggregateMeasure` (1..*): releases bundle measures, and review judges the bundle, not each cell alone.
- `releaseCandidate` -> shapedBy -> `suppressionRule` (0..*): thin cells are suppressed, merged or coarsened before review.
- `releaseCandidate` -> spends -> `noiseBudget` (0..1): noisy releases draw down the budget of their source.
- `publishedSeries` -> releasedFrom -> `releaseCandidate` (1..*): a series is the accumulation of passed reviews over time.

## Events

- `cohortDefined`: a new population slice was defined and its membership counted.
- `floorAdjusted`: a minimum cohort size was raised or lowered with recorded rationale.
- `measureComputed`: a statistic was computed over a cohort inside the protected environment.
- `cellSuppressed`: a thin cell was withheld or merged before release.
- `budgetSpent`: a release drew down a noise budget, or a budget ran out and blocked further sensing for the period.
- `reviewPassed`: a release candidate cleared disclosure review against floors and budgets.
- `seriesPublished`: reviewed aggregates were released with method and provenance.

## Contracts

- `seriesSubscription`: a consumer receives published series and their revisions; never anything below the published grain.
- `sensingRequest`: a party commissions a new aggregate over defined cohorts; honored only above floors and within budgets.
- `methodAudit`: an auditor examines cohort definitions, floors, budgets and methods; microdata is never in scope.

## Projections

- `publicStatistics`: published series only; omits cohorts under floor, suppressed cells and all member-level data.
- `methodologySheet`: definitions, floors, suppression and noise methods per series; omits the values' underlying sources.
- `budgetLedger`: budget allocation and spend per source and period; omits what the queries were about.

## Composition

- REFERENCE `world.ownership` (S1): aggregation never transfers control; source objects remain their holders' throughout.
- REFERENCE `world.accessContract` (S2): sensing requests and series subscriptions are themselves access contracts.
- REFERENCE `world.disclosureScope` (S3): the aggregation grains that S3 policies point to are defined and enforced here.
- REFERENCE `world.accessAudit` (S4): every sensing run, review and release is logged.
- REFERENCE `world.person` (H1): population registers of the person model are the typical cohort source.
- imports: differential-privacy-practice (ALIGN): noise addition and budget accounting semantics.
- imports: sdmx (ALIGN): the exchange shape of published statistical series.

## Stewardship

A statistics office steward archetype operates the model within its statutory mandate: it computes and releases, but the underlying data stays with its owners, and the steward's own reads run under S2 contracts and land in the S4 log like anyone else's.
