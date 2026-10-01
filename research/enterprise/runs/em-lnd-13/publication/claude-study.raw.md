# Verdict

**PROFILE, not new model.** EM-LND-13 is a governed viewpoint over existing masters. Neither candidate type earns independent identity:

- **DataLandscape** — a *projection*: a version-pinned, as-of query over WM-DAT-008 (catalog/product), WM-DAT-001 (dataset), WM-DAT-004 (schema/contract), WM-DAT-005 (pipeline definition), WM-DAT-006 (lineage), WM-REC-002 (report), the unassigned Metric Definition candidate (EM-DAT-05) and WM-ACT-036/WM-KNW-007 (analysis/claim). It has no lifecycle of its own that its constituents lack.
- **AnalyticalLineageView** — a *governed profile of WM-DAT-006*, narrowed to the metric→report→finding path. WM-DAT-006 is already declared a pattern with granularity, perimeter and confidence as first-class; a second lineage master would create two provenance authorities for one graph.

The landscape therefore gets a viewpoint record (scope, as-of, semantic_version, freshness_policy from the v1 candidate fields, all still `candidate-not-normative`) plus conformance constraints. No runtime identity, no model ID allocation.

# Evidence

All four target specs are `published` but `publishableCanonical: false` / `adjudicationStatus: reviewable-draft`; WM-DAT-005 and WM-DAT-008 are single-provider Codex waivers, WM-DAT-006 a single-provider Claude waiver. All four registry rows are `boundary-review-required` or `migration-boundary-review`, and every relation in the ledger is `review_state: candidate`. WM-REC-002 has `spec_availability: false` — Report/Statement exists only as the EM-DAT-06 reservation. Metric Definition has no allocated identifier. Three of the four mapping notes are `index-and-publication-metadata` depth; only WM-DAT-008 is `boundary-reviewed`.

Positive evidence for a projection verdict: WM-DAT-001 explicitly delegates the full derivation graph to WM-DAT-006 and product packaging to WM-DAT-008; WM-DAT-005 declares lineage a non-owning reference; WM-DAT-006 declares itself composed *into* WM-DAT-001 and WM-DAT-005; WM-DAT-008 forbids collapsing CatalogRecord, DataProduct, Dataset, Distribution and DataService identities. Four independent specs already draw the boundary the landscape needs — so the landscape need only *read* it.

# Identity/mastership

Distinct identities, none interchangeable: catalog record; data product/offering; dataset; dataset version; distribution; schema/contract version; pipeline definition version; deployment; scheduler registration; pipeline run (WM-ACT-053); task attempt; lineage assertion; metric definition version; observation (WM-MAT-008); report definition version; report issue; analysis method version; study (WM-ACT-036); finding/claim (WM-KNW-007). Mastership stays with each owning model; the landscape holds only resolvable references plus its own `as_of` and `semantic_version`. Candidate master systems (model registry, `sources.yaml`, `vercy.lock`, policies) govern the viewpoint record, not the referenced objects. Identity priority throughout: authoritative master-system identifier → governed IRI → Dimension UUID/ULID. Never a title, date, digest or KPI label.

# Definition/run separation

Four independent clocks, per prior EM-DAT-03/05/06 findings:

| Definition | Execution / release |
|---|---|
| Metric definition version (formula, numerator/denominator, unit+code-system version, population, dimensions, null policy) | Observation / measurement record bound to exactly that version |
| Report definition version (parameters, grain, measure bindings) | Report issue pinning definition version, parameters, period, cutoff, as-of, input snapshots, run reference |
| Pipeline definition version (topology, ports, contracts, logic digests) | Pipeline run + task attempts with resolved inputs/outputs |
| Analysis method version (estimator, assumptions, admissible inputs) | Study application → estimate → finding/claim |

Released definitions and recorded executions are immutable. Corrections append successors; retries never overwrite failed attempts. Run success proves neither quality, freshness, publication, acceptance nor fitness.

# Lineage and impact

The AnalyticalLineageView profile requires every edge to carry relation type, dependency mode (direct/indirect), transformation subtype, masking flag, granularity, capture method, producer + schema version, confidence grade and evidence reference — all already WM-DAT-006 elements. Name similarity, temporal adjacency and co-occurrence may appear only as low-confidence *inferred* evidence and never establish direct derivation.

Impact analysis is `analyse-change-impact` over the profile, joined to metric→report→finding bindings. Its output is qualified by coverage, not asserted complete.

# Semantic comparability

Identical KPI titles are not comparability evidence — the negative case is rejected outright. Comparability requires identity of *definition version*, or an explicit facet-level reconciliation verdict (`comparable`, `comparable-with-restatement`, `non-comparable`) across formula, method, unit+code-system version, population boundary, dimensions/additivity and null policy. **Absence of a verdict means non-comparable.** The landscape surfaces same-title/different-definition-version clusters as findings, never as equivalences.

# Reports and analytics

A report issue pins one report definition version and enumerates input dataset versions, partitions and digests; period, cutoff, as-of and issue time stay distinct. A dashboard live view is not a report issue (no frozen cutoff or evidence tuple); a citable snapshot mints one. Findings are WM-KNW-007 claims with scope, assumptions, defeaters and evidence bindings — association never auto-upgrades to causation, and a report never substitutes for a finding's justification. Recommendations are deontic claims with no effect absent WM-KNW-010 content plus a WM-ACT-024 occurrence.

# Completeness/freshness

Lineage completeness is meaningful only against a versioned perimeter declaration with stated denominator, supported granularities, opaque segments and recognised manual steps. Default is open-world: a missing edge means *unobserved*, not *no dependency*. Absence claims are valid only inside an explicitly closed perimeter. Unknown gaps are first-class: unresolved paths, opaque external inputs (boundary nodes, unresolved-upstream status, cause code), manual-correction dependencies (propagated flag), and unclassified new elements after schema drift. Freshness uses `freshness_policy` plus each layer's own observation/ingestion time; stale means *any* of schema, classification, cohort-floor or snapshot drift. Reproducibility requires the immutable run binding set — definition/component revision, code and dependency digests, parameters, input pins with digests, interval/watermark, environment, attempts, output digest, nondeterminism declaration. Missing any element downgrades the claim to *explainable* or *partially reproducible*.

# Access and projection

Projections inherit source-fact rights. WM-XCT-003 governs the permitted leaving shape; each served landscape view records the policy-version identifier, template fingerprint, binding identifier, source-schema version and compilation timestamp, with WM-XCT-004 owning the audit entry. Suppressed slices record policy version and reason without leaking withheld values; aggregate-only views require a resolvable WM-XCT-005 cohort-floor reference (never a local default). Withheld segments are marked withheld, never rendered as absent. The landscape evaluates and enforces nothing — WM-XCT-038 decides.

# Scenario

Headcount KPI changes from `count(headcount)/method A/population P1` to `sum(FTE)/method B/population P2`.

1. New semantics → new metric definition version `v2`; `v1` remains resolvable.
2. Impact query returns affected definitions: report definition versions binding `v1`; the derived ratio definition using it as denominator; and the analysis method application in the study that consumed it.
3. Concrete report releases, differing in method:
 - **Issue A** — pins report definition `v1.2`, metric `v1`, snapshots `A@s41/B@s17`, run R1, cutoff Q2. Method A, headcount, P1.
 - **Issue B** — pins report definition `v1.3`, metric `v2`, snapshots `A@s42/B@s17`, run R2, cutoff Q2. Method B, FTE, P2.
4. Both bear the same KPI title. The landscape emits `non-comparable` (formula, unit, method and population all differ; no reconciliation exists), flags the shared title as a comparability hazard, and reports the one period with no `v2` observation as a coded gap — not zero.
5. Conclusions in the study citing Issue A are marked stale-input, scoped to `v1`, and retained rather than rewritten.

# Invariants

1. Definition and run/release identities are distinct and separately immutable.
2. Lineage is asserted with capture method, producer, granularity, confidence and evidence — never invented or inferred from correlation.
3. Missing edges imply absence only inside an explicit closed perimeter.
4. Projections carry the rights, policy version and fingerprint of their source facts.
5. Identical titles never establish comparability; absence of a reconciliation verdict means non-comparable.
6. Every report issue pins definition version, parameters, period, cutoff, as-of and input snapshots.
7. Observations bind to exactly one metric definition version.
8. Unknown, zero, not-applicable, missing and suppressed are distinct states.
9. Run success proves nothing about quality, freshness, publication or fitness.
10. Corrections append successors; released artifacts are never rewritten.
11. Association never auto-upgrades to causation; findings state applicability scope.
12. The landscape references masters and reproduces none.

# Minimal profile shape

Viewpoint record: `analytical_scope`, `as_of`, `semantic_version`, `freshness_policy`, perimeter declaration reference, crosswalk edition + digest, projection policy reference. Constraint set: the twelve invariants as validation shapes. Two derived reports: same-title/different-definition clusters; conclusions-on-stale-or-incomplete-input. No new identity, no state machine, no stored instance data.

# Holds

All four bases are non-canonical reviewable drafts; three rest on single-provider waivers. Every relation is candidate. WM-REC-002 has no specification and Metric Definition has no allocated identifier — both are prerequisites, so the acceptance scenario is satisfiable in structure but not yet in registry. WM-DAT-006's perimeter-versioning defect and unresolved WM-XCT-012 parent, WM-DAT-001's DataCite 4.6/4.7 divergence, and WM-DAT-008's beta DPROD pin remain open. No fixtures were run. This review claims no canonical completeness and no installability.
