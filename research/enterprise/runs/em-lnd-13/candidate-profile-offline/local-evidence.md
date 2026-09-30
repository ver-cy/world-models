# EM-LND-13 reconciled local evidence

## Decision

Data Landscape is an issued-at, version-pinned snapshot projection. Analytical Lineage View is a WM-DAT-006 profile. Neither receives independent identity or a runtime/model identifier. A published projection uses an existing WM-DAT-008 Data Product identity; reusable handles own no lineage edges.

## Semantics

Issued-at and as-of are separate pins, and issued-at fixes an immutable observed set. Definitions remain separate from observations, issues, runs, studies and claims. Formula changes, corrections and retries append successors.

Lineage edges carry type, granularity, capture method, producer, confidence and evidence with version- or partition-addressed endpoints. Inferred edges are explicitly marked and cannot establish absence or comparability. Impact returns four labelled sets: affected definitions, affected issues/runs, affected findings/claims and unresolved coverage.

Comparability examines formula or method, unit and code-system version, population, dimensions and null policy. Missing verdict means non-comparable. Report issues pin definitions, parameters, period, cutoff, as-of, issued-at, input versions/partitions/digests and run reference. Live dashboards require a frozen issue for citation.

Missing edges remain unobserved unless a closed, scoped, time-bounded and edition-pinned perimeter covers the issued observed set. Freshness separately evaluates schema, classification, cohort/privacy and snapshot state. Stale and incomplete markers propagate to dependent findings. Gap classes remain distinct.

Rights policy version and fingerprint are pinned at issue time. Policy or crosswalk changes mark an issue stale and require a successor for re-evaluation. Withheld slices remain marked and must be protected against recovery by differencing.

## Conditional dependencies and holds

Metric-facing rules wait for EM-DAT-05 allocation. Report rules wait for a WM-REC-002 publication specification. Absence rules wait for reconciled WM-DAT-006 perimeter semantics. Pipeline run/task-attempt and analysis-method mastership remain uncovered. Target bases remain non-canonical and relation rows candidate. No ID is minted to bridge these gaps.
