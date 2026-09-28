# EM-DAT-05 local synthesis

## Disposition

**NEW MODEL candidate: cross-domain Metric Definition aggregate.** The model is required because a metric definition exists before any observation or target, is referenced by records with independent lifecycles, and must preserve immutable historical versions when its formula or population changes.

The new aggregate must not absorb observations, targets, goals, quality assessments, reports, procedures, units, code lists or populations. It governs the reusable definition that those records cite.

## Proposed object boundary

Stable identity belongs to the metric. Each activated definition version is immutable and addressable. The aggregate owns only the definition-version components necessary for interpretation and comparability:

- formula and expression-language binding;
- numerator, denominator, base and index components;
- metric kind, quantity kind, scale and comparison direction;
- unit reference with version-pinned code system;
- dimensions and additivity behavior;
- population boundary with inclusion and exclusion rules;
- method and source bindings by reference;
- null/absence semantics;
- compatibility and comparability declarations between definition versions.

External records retain their own authority:

- WM-XCT-025 supplies reusable result fields;
- WM-DAT-010 owns series and observations;
- WM-KNW-011 owns targets and objectives;
- WM-DAT-007 owns data-quality assessments;
- procedure, unit, population, classification and source-data masters are referenced.

## Lifecycle

Definition version: `draft -> active -> superseded -> withdrawn/tombstoned`. Activation freezes semantics. Editorial label corrections that do not change meaning require explicit classification; formula, method, unit, population, dimension or null-policy changes always mint a successor version. Metric identity may retire but remains resolvable.

## Required invariants

1. Stable metric identity is distinct from immutable definition-version identity.
2. An activated definition version is never modified in place.
3. A definition never stores an observed value, series head, target value or attainment verdict.
4. Ratio/rate definitions declare numerator and denominator semantics.
5. Unit code includes code-system identity and version; dimensionless is explicit.
6. Each aggregable dimension declares additivity behavior; unsupported aggregation fails closed.
7. Population unit, inclusion and exclusion boundaries are mandatory before activation.
8. Method and source bindings are version-pinned references.
9. Zero, unknown, not applicable, missing and suppressed are distinct states.
10. A change to formula, method, unit, population, dimensions or null policy requires a facet-level comparability verdict.
11. Absence of a comparability verdict means non-comparable.
12. Superseded and withdrawn versions remain resolvable and provenance-linked.

## Acceptance result

For a headcount KPI changing from method A/population P1 to method B/population P2 while its phenomenon, quantity kind and statistical unit type remain unchanged:

- the new semantics produce a new immutable definition version under the same Metric identity;
- the missing period remains a gap or coded missing result, never zero;
- recalculation emits new observations bound to the new definition version and retains the old observations;
- cross-version comparison is rejected unless an explicit reconciliation supports `comparable-with-restatement`;
- comparisons using the same definition version remain valid subject to coverage and observation-quality rules.

A change from headcount persons to FTE changes quantity kind or statistical unit type and therefore creates a new Metric identity. A correspondence or restatement mapping may relate the two metrics but cannot silently preserve identity. Aggregation and target-version refusal are declared conformance obligations for WM-DAT-010 and WM-KNW-011 consumers; this candidate does not absorb their enforcement lifecycles.

## Evidence limits

All neighboring models are reviewable drafts and several lack independent external review or frozen relations. Standards are alignment targets only. The model identifier remains unassigned. These limits permit a bounded research candidate, but not registry allocation or canonical publication.
