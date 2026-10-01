## Verdict

**Extend, do not create.** All four candidate types resolve onto reserved models; no new model or identifier is needed.

| Candidate | Disposition |
|---|---|
| DataQualityRule | **Reuse WM-KNW-013** as rule master; WM-DAT-007 holds a version-pinned binding + dimension facet |
| QualityEvaluation | **WM-DAT-007 root**, specialising WM-ACT-034's assessment machinery; observations reuse WM-MAT-008 |
| QualityIssue | **Reuse WM-KNW-014** as issue master; WM-DAT-007 holds non-owning finding references |
| CoverageAssessment | **Assessment kind inside WM-DAT-007**, gated on a mandatory declared frame — not a separate master |

EM-DAT-04's contour scope is satisfied by WM-DAT-007 plus four reference edges. The one substantive gap is that coverage currently has no mandatory frame object and no unknown-denominator state.

## Evidence

WM-DAT-007 already carries, in its own structure, the layers this contour needs: `rules-thresholds-tolerances-and-requirements`, `campaign-window-trigger-and-sampling-design`, `population-frame-sample-stratum-coverage-weight-bias-and-representativeness`, `observations-values-uncertainty-and-rule-results`, `violations-aggregation-score-and-fitness-decision`, and `defects-causes-actions-and-reassessment`. Its scope statement already externalises "metric registry, issue, remediation, certificate, audit and records masters." Its adjudication already records "accepted-external" for issue/remediation and "accepted-with-method-hold" for sampling and uncertainty. So the boundary work here is confirming reuse, not inventing structure.

Counter-evidence for reuse is thin but real: WM-DAT-007's `metric-definition-indicator-formula-direction-scale-unit-and-aggregation` finding overlaps the Metric Definition aggregate proposed in prior research EM-DAT-05. That overlap must be resolved by reference, not by both owning formulas.

## Identity/mastership

- **Rule identity** → WM-KNW-013 (`rule id + namespace + immutable revision`). WM-DAT-007 pins the revision; it never edits the predicate.
- **Metric identity** → the EM-DAT-05 metric-definition candidate (stable metric id + immutable definition version). WM-DAT-007 must downgrade its metric finding to a version-pinned reference; otherwise two masters own numerator/denominator/unit semantics.
- **Observation identity** → WM-MAT-008 (act identity; measurand triple immutable — change of property, procedure or feature is a new observation, not a version).
- **Issue identity** → WM-KNW-014 (canonical record + supersession; duplicates retired with derivation links).
- **Assessment identity** → WM-DAT-007 (`assessment id + version`, distinct from subject-version, definition, observation, result and verdict ids, per its own `identity_strategy`).
- **Dataset/schema identity** → WM-DAT-001 / WM-DAT-004.

WM-ACT-034 is the generic assessment pattern (purpose, criteria binding, decision rule, conclusion, validity, assurance). Treat it as the inherited shape, not a second store of the same conclusion.

## Rule/metric/observation boundaries

Four distinct things, four owners:

1. **Rule** (WM-KNW-013): normative predicate, modality, operands, datatype, unit, tolerance, applicability, severity, threshold. Reusable across datasets and purposes.
2. **Metric definition** (EM-DAT-05 aggregate): formula, numerator/denominator, population boundary, additivity, null semantics, comparability between versions.
3. **Observation** (WM-MAT-008): one measured or counted result with feature, property, procedure, value, unit, phenomenon time, result time, uncertainty, absent/censored reason.
4. **Evaluation** (WM-DAT-007): the purpose-qualified judgement that binds 1–3 to a subject version, sample, threshold and verdict.

A rule *evaluation state* (satisfied / violated / indeterminate / not-applicable / not-run / waived) belongs to WM-DAT-007's result layer. The rule itself has no state.

## Dimensions and denominators

Every dimension is purpose-qualified: it names a consumer, use case, decision and time, and none is an intrinsic dataset property.

| Dimension | Measures | Denominator |
|---|---|---|
| Completeness | presence of a value where an obligation rule requires one | required-value slots under the pinned contract (WM-DAT-004) × in-scope rows |
| Accuracy | agreement with declared reference truth | adjudicated comparison pairs, not rows |
| Validity | conformance to a pinned WM-KNW-013 predicate | evaluated **and applicable** rows; not-applicable and not-run excluded, never scored |
| Freshness | elapsed time between two named clocks vs a purpose latency budget | none — it is a duration against a budget, not a ratio |
| Coverage | share of the declared target population represented | the **frame**, which may be unknown |

**Unknown denominators** get three explicit states: `known-exact`, `estimated` (method + interval + bias direction), `unknown`. With `unknown`, no ratio may be published — only counts, plus an optional lower bound from a named proxy frame with its identity, version and bias direction. A coverage ratio is never defaulted to 1.0.

**Sampling frames** require frame identity + version, frame-to-target gap (undercoverage, overcoverage, duplication), design, strata, inclusion probabilities, weights, planned vs achieved n, and missingness.

**Uncertainty**: interval, method, coverage probability; sampling error, measurement error and reference-truth error stated separately. A sampled point estimate without an interval is inadmissible.

**Reference truth**: source identity + version, authority, matching rule, adjudication, its own error rate, and an independence assertion. If the reference derives from the assessed dataset, the accuracy claim is rejected and downgraded to internal consistency.

**Time**: phenomenon time, reference period, ingest time, execution time, result time, effective time, published time, knowledge time, correction time — kept distinct. Freshness must name which pair it measures.

## Evaluation and verdict

An evaluation pins: subject + version, purpose, rule/metric revisions, plan, frame, sample, method, engine, input snapshot digest, clocks. It emits per-dimension results with denominator state and uncertainty, then a purpose-qualified fitness verdict with limitations. Aggregation is optional and must declare its model, weights and treatment of not-run/unknown; a composite score never travels without that model. No dimension result implies another: passing validity says nothing about accuracy, and completeness says nothing about truth.

## Issue/remediation

A violation is a WM-DAT-007 result. A **QualityIssue** is a WM-KNW-014 record referencing that result — created only when a discrepancy is recognised as needing disposition, with its own severity, cause analysis and disposition owned there. WM-DAT-007 holds the reference plus a consequent acceptance status; it does not close issues, execute remediation, or infer effectiveness from status. Remediation retest is a **new** evaluation, linked as successor.

## Lifecycle

Assessment: `draft → reviewed → approved → published → (expired | superseded | withdrawn)`. Published versions are immutable. A correction mints a successor citing predecessor, reason, scope and the retained prior verdict; the earlier assessment stays resolvable with its own inputs and knowledge time. Rule and metric revisions do not retro-apply to issued assessments. Independent clocks: assessment version, rule revision, metric definition version, dataset version, issue supersession.

## Scenario

**A — fully populated, stale.** Completeness 100% (denominator = required slots, `known-exact`). Validity satisfied. Freshness **violated**: 41 h against a 4 h budget for purpose P (real-time pricing). Accuracy `not-measured` — no reference truth bound. Coverage: frame as-of an old reference period, so coverage against the current target is `denominator-unknown`. Verdict: **not fit for P**; possibly fit for purpose Q (historical trend) as a separate assessment. 100% field population cannot become 100% truth because accuracy holds `not-measured`, a state distinct from `satisfied`, and aggregation is forbidden from imputing it.

**B — partial, high accuracy.** Coverage 4% of frame F@v2. Accuracy 99.2% ±0.6 (95%) on 1,200 adjudicated pairs against independent reference R@v3. Freshness satisfied. Completeness partial. Verdict: accuracy valid **within sample scope only**; no dataset-wide inference without weights and frame closure; not fit for a census purpose. A and B remain two assessments with independent verdicts — never blended into one score.

## Invariants

1. Rule, metric definition, observation, result, verdict, issue and remediation identities stay distinct.
2. Every evaluation pins rule/metric revision, subject version, sample and clocks.
3. Denominator state is explicit; `unknown` blocks ratio publication.
4. Not-applicable, not-run, unknown, missing, suppressed, satisfied, violated, waived are distinct and never collapsed.
5. Field population never implies accuracy; validity never implies accuracy; accuracy requires independent reference truth.
6. Freshness is meaningless without a named clock pair and a purpose budget.
7. Coverage requires a versioned frame and a stated frame-to-target gap.
8. Sampled estimates carry interval, method and error decomposition.
9. Published assessments are immutable; corrections append successors and never rewrite a prior verdict.
10. WM-DAT-007 references but does not own rule, metric, dataset, schema, run, issue, remediation, certificate, audit or records masters.

## Minimal completion shape

Assessment id + version; subject ref + version; purpose (consumer, use case, decision, time); framework profile; per-dimension: rule/metric ref + revision, denominator + state, numerator, result value, uncertainty, clocks, evidence ref; frame ref + version and sample design where sampled; reference-truth ref + independence where accuracy claimed; verdict + limitations; issue refs; lifecycle state; predecessor link.

## Holds

WM-DAT-007, WM-MAT-008, WM-KNW-013, WM-KNW-014 and WM-ACT-034 are all reviewable drafts under single-provider waivers with absence-of-external-review holds. The WM-DAT-001 COMPOSE edge is candidate, not frozen; WM-KNW-013's WM-REC-006 parent and WM-ACT-034's WM-ACT-009 parent are unresolved; WM-KNW-014's relationship contract is empty. The metric-ownership overlap with EM-DAT-05 is unresolved. No canonical completeness or installability is claimed.
