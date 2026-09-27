# EM-LND-13 local synthesis

## Disposition

- Define Data Landscape as a governed, version-pinned projection over dataset, schema/contract, pipeline, lineage, data-product, report, metric, analysis and claim masters.
- Define Analytical Lineage View as a profile of WM-DAT-006 narrowed to metric→report→analysis→claim paths.
- Neither candidate has an independent lifecycle or subject identity; allocate no runtime/model identifier.

## Identity and mastership

Catalog record, data product, dataset/version, distribution, schema/contract version, pipeline definition/deployment/run/task attempt, lineage assertion, metric definition version, observation, report definition/issue, analysis method/study and finding/claim remain distinct identities under their owning models. The landscape holds only references, pins, scope, as-of, semantic edition and freshness policy.

## Definition and execution separation

Metric definition versions own formula, population, dimensions, unit and null policy; observations bind to one exact definition. Report definitions own parameters, grain and measure bindings; report issues pin definition, parameters, period, cutoff, as-of, inputs and run. Pipeline definitions own topology/contracts/logic; runs and attempts own resolved execution. Analysis method versions own estimator/assumptions; study applications and claims own results and conclusions.

Released definitions and executions remain immutable. Corrections and retries append successors. Successful execution proves neither quality, freshness nor acceptance.

## Lineage, impact and comparability

Every lineage edge records relation/dependency type, transformation subtype, masking, granularity, capture method, producer/schema version, confidence and evidence. Name similarity, time adjacency and co-occurrence can only support low-confidence inference and never prove direct derivation.

Impact analysis traverses metric-definition, report-definition/release and analysis/finding bindings and reports coverage. Missing edges mean unobserved unless a closed, versioned completeness perimeter permits an absence claim.

Same KPI title never proves comparability. Definitions require a facet reconciliation across formula/method, unit/code-system version, population, dimensions/additivity and null policy. Verdict is comparable, comparable-with-restatement or non-comparable; missing verdict means non-comparable.

## Reports, analytics, completeness and freshness

A report issue pins input versions/partitions/digests plus period, cutoff, as-of and issue time. A live dashboard becomes citable only through a frozen snapshot issue. Findings remain claims with scope, assumptions, defeaters and evidence; association never becomes causation automatically.

Completeness declares denominator, supported granularities, opaque segments and manual steps. Unknown gaps, external inputs, manual corrections and schema-drift elements are first-class. Freshness evaluates schema, classification, cohort/privacy and snapshot states. Reproducibility requires definitions, code/dependency digests, parameters, input pins, watermarks, environment, attempts, output digest and nondeterminism statement.

## Access and projection

Views inherit source rights. WM-XCT-003 supplies leaving shape, policy version, fingerprint, binding and schema pin; withheld segments remain marked withheld, never absent. Aggregate views reference cohort/privacy controls. The landscape does not execute enforcement.

## Acceptance scenario

A KPI changes from headcount Method A/population P1 to FTE Method B/population P2, creating metric version v2. Impact traversal identifies report definitions using v1, a derived metric and a study method application. Report Issue A pins v1 and earlier snapshots; Issue B pins v2 and later snapshots. Same title produces a non-comparable finding, missing v2 observation remains a coded gap and conclusions based on Issue A become stale-input without being rewritten.

## Invariants

1. Definition and execution/release identities remain distinct.
2. Lineage records method, granularity, confidence and evidence.
3. Correlation or naming never proves derivation.
4. Missing edges imply absence only in a closed declared perimeter.
5. Identical KPI titles never prove comparability.
6. Observations bind to one metric definition version.
7. Report issues pin definition, parameters, times and inputs.
8. Unknown, zero, not-applicable, missing and suppressed remain distinct.
9. Run success never proves quality or fitness.
10. Corrections append successors.
11. Findings retain scope, assumptions and evidence.
12. Projections preserve source rights and withholding.

## Minimal profile shape

The viewpoint records analytical scope, as-of, semantic edition, freshness policy, completeness perimeter, crosswalk edition/digest, source pins and projection policy. Validation shapes enforce the invariants; derived findings identify same-title/different-definition clusters and conclusions based on stale or incomplete inputs.

## Holds

All target bases remain non-canonical drafts and relation rows are candidate. WM-REC-002 has no published specification and Metric Definition remains unallocated, blocking full registry realization. WM-DAT-006 perimeter versioning and parent issues, external source-version divergences and data-product source pins remain unresolved. No fixtures were run. This checkpoint makes no canonical completeness, installability or publication claim.
