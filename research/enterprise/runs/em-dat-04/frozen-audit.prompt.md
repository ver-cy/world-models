You are the sole frozen independent semantic auditor for EM-DAT-04. Use no tools. Review the reconciled completion of reserved WM-DAT-007 for identity, mastership, dimension separation, denominator and uncertainty semantics, frame/version binding, lifecycle, fixtures, holds and accidental new identity. Return verdict; blocking defects; non-blocking defects; exact remediation; required fixtures; publication disposition. Do not invent identifiers or claim canonical completeness.

## Claude study
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


## Grok review
# Grok independent review — EM-DAT-04

Source conversation: https://grok.com/c/16c983bd-7369-422f-a401-8f02f4ff0333

## Verdict

Accept the proposed completion of reserved WM-DAT-007 with holds. WM-DAT-007 owns the purpose-qualified quality evaluation and verdict. Reusable rules, metric definitions and formulas, observations and issues remain externally mastered. CoverageAssessment does not need independent model identity; it is a QualityEvaluation kind with additional mandatory completion constraints. WM-DAT-007 may bind metric formula revisions but must not author or master formulas.

## Identity and mastership

One evaluation has one purpose, one subject, one evaluation-as-of time and at most one current verdict. A changed frame version creates a distinct evaluation. WM-KNW-013 owns reusable rules, WM-MAT-008 owns observations, WM-KNW-014 owns issues, the identifier-unassigned Metric Definition candidate owns formulas, and WM-ACT-034 supplies the generic assessment shape. A frame is a referenced versioned subject rather than a WM-DAT-007-owned entity. CoverageAssessment is a kind discriminator plus mandatory frame and denominator fields.

## Dimension and denominator findings

Completeness, accuracy, validity, freshness and coverage are pairwise non-substitutable. Accuracy requires independent reference truth. Freshness requires a data-as-of clock, an evaluation/purpose-need clock and a purpose-owned latency budget. Coverage compares the evaluated population with a versioned intended frame; sample rate is not coverage.

Denominator states are exact, estimated or unknown. Exact alone supports an unqualified population ratio. Estimated requires a disclosed estimation method and uncertainty and remains estimate-qualified. Unknown blocks ratios and population claims that require the denominator. Any ratio-bearing evaluation, not only coverage-kind, must cite a versioned frame and explicit denominator state. Sample observations do not become population denominators without a declared expansion method.

## Lifecycle and scenario

Lifecycle is draft, bound, observed, evaluated, verdict/deferred and superseded. Corrections and remediation retests create successor evaluations; predecessor identity, evidence and verdict remain immutable. External issues survive supersession.

A fully populated but stale dataset may pass completeness and validity while freshness fails and accuracy remains unevaluable without independent truth. Scores are not netted. A 4% sample may support sample-conditioned accuracy only; it neither establishes population completeness nor coverage. Population inference is estimated only with a design-based method and frame size, otherwise unknown. Population claims require a separate evaluation and never inherit the sample verdict.

## Blockers

Metric Definition remains identifier-unassigned, leaving formula mastership without a canonical home. Frame-versioning authority is not named. Parent and relation rows remain research-only. No new identifier or canonical-completeness claim is justified.



## Provider comparison
# Provider comparison — EM-DAT-04

Claude and Grok agree that reserved WM-DAT-007 is the correct assessment aggregate and that reusable rule, metric formula, observation, issue and remediation authorities remain external. Both preserve separate completeness, accuracy, validity, freshness and coverage dimensions; require independent truth for accuracy; require two clocks plus a purpose budget for freshness; forbid ratios with unknown denominators; and require immutable successor evaluations for corrections and retests.

Grok resolves the two explicit questions: CoverageAssessment is a constrained QualityEvaluation kind, not a new independently identified model, and WM-DAT-007 may bind but never own metric formulas. It strengthens the completion rule so every ratio-bearing evaluation cites a versioned frame and explicit denominator state, not only coverage-kind. It also makes frame version part of evaluation identity and requires estimated denominators to disclose method and uncertainty.

The reconciled candidate completes the existing WM-DAT-007 reservation without a new model or runtime ID. Publication remains held because Metric Definition is identifier-unassigned, frame-versioning authority is unnamed, parent/relation assurance is incomplete and the package remains a research candidate.


## Current package: candidate.json
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-DAT-04",
  "modelId": "WM-DAT-007",
  "registryId": "vr.wm-dat-007",
  "name": "Data Quality Evaluation",
  "version": "0.3.1-candidate.1",
  "entryKind": "aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent a purpose-qualified, versioned evaluation of data quality and its verdict while keeping reusable rules, metric definitions, observations, issues and remediation under independent authorities.",
  "boundary": {
    "owns": [
      "assessment identity and immutable versions",
      "subject/version, purpose, consumer and decision context",
      "evaluation plan, sampling frame and sample design pins",
      "rule and metric revision bindings",
      "per-dimension evaluation results and denominator state",
      "uncertainty, evidence references and purpose-qualified verdict",
      "successor lineage for corrections and retests"
    ],
    "delegates": [
      "reusable rule predicates and thresholds to WM-KNW-013",
      "metric formulas, populations, units and comparability to Metric Definition",
      "measurement records and uncertainty to WM-MAT-008",
      "recognized issue identity and disposition to WM-KNW-014",
      "generic assessment shape to WM-ACT-034",
      "dataset and schema identity to WM-DAT-001 and WM-DAT-004"
    ],
    "excludes": [
      "metric-definition mastership",
      "source data mutation",
      "pipeline execution and retry state",
      "issue closure or remediation execution",
      "certification or universal fitness",
      "policy enforcement and access widening"
    ]
  },
  "assessmentVersion": {
    "identity": [
      "assessmentId",
      "assessmentVersionId",
      "version"
    ],
    "required": [
      "subjectRef",
      "subjectVersionRef",
      "purpose",
      "consumerRef",
      "decisionContext",
      "ruleBindings",
      "metricBindings",
      "evaluationPlan",
      "frameState",
      "sampleDesign",
      "inputSnapshotRefs",
      "resultClocks",
      "dimensionResults",
      "verdict",
      "limitations",
      "lifecycleState"
    ],
    "lifecycle": [
      "draft",
      "reviewed",
      "approved",
      "published",
      "expired",
      "superseded",
      "withdrawn"
    ]
  },
  "dimensionContracts": {
    "completeness": "Required values present over required slots and in-scope rows under a pinned contract.",
    "accuracy": "Agreement with independently governed versioned reference truth over adjudicated comparison pairs.",
    "validity": "Conformance to pinned rules over evaluated applicable subjects; not-applicable and not-run are excluded.",
    "freshness": "Duration between two named clocks compared with a purpose-specific latency budget.",
    "coverage": "Represented target population against a declared versioned frame with explicit frame-to-target gaps."
  },
  "denominatorStates": {
    "known-exact": "Exact denominator and derivation are recorded.",
    "estimated": "Method, interval and bias direction are recorded.",
    "unknown": "Ratio publication is prohibited; counts or a labeled proxy lower bound may be reported."
  },
  "resultStates": [
    "satisfied",
    "violated",
    "indeterminate",
    "not-applicable",
    "not-run",
    "waived"
  ],
  "relations": [
    {
      "target": "WM-KNW-013",
      "relation": "REFERENCE",
      "purpose": "Pin reusable rule and threshold revisions without editing them.",
      "required": true
    },
    {
      "target": "WM-MAT-008",
      "relation": "REFERENCE",
      "purpose": "Resolve observations, measured values, methods and uncertainty.",
      "required": true
    },
    {
      "target": "WM-KNW-014",
      "relation": "REFERENCE",
      "purpose": "Reference a governed issue only after a discrepancy record is opened.",
      "required": false
    },
    {
      "target": "WM-ACT-034",
      "relation": "REFERENCE",
      "purpose": "Reuse the generic assessment shape without duplicating its conclusion store.",
      "required": false
    },
    {
      "target": "WM-DAT-001",
      "relation": "REFERENCE",
      "purpose": "Pin assessed dataset and version identities.",
      "required": true
    },
    {
      "target": "WM-DAT-004",
      "relation": "REFERENCE",
      "purpose": "Pin schema, contract and required-value obligations.",
      "required": false
    }
  ],
  "operations": [
    {
      "id": "plan-evaluation",
      "effect": "Freeze subject, purpose, rule/metric revisions, frame, sample, clocks and evidence plan.",
      "authority": "quality assessment owner"
    },
    {
      "id": "record-result",
      "effect": "Record dimension result, denominator state, uncertainty and evidence without mutating external observations.",
      "authority": "authorized evaluator"
    },
    {
      "id": "issue-verdict",
      "effect": "Create a purpose-qualified verdict and limitations for one assessment version.",
      "authority": "quality decision authority"
    },
    {
      "id": "correct-assessment",
      "effect": "Create a successor with reason and scope while preserving the predecessor.",
      "authority": "quality assessment owner"
    },
    {
      "id": "retest-after-remediation",
      "effect": "Create a new evaluation linked to prior result and external issue/remediation references.",
      "authority": "authorized evaluator"
    }
  ],
  "invariants": [
    "Rule, metric definition, observation, assessment, result, verdict, issue and remediation identities remain distinct.",
    "Every evaluation pins rule and metric revisions, subject version, frame, sample, clocks and input snapshots.",
    "Unknown denominator blocks ratio publication.",
    "Estimated denominator records method, interval and bias direction.",
    "Not-applicable, not-run, indeterminate, waived, satisfied and violated never collapse.",
    "Completeness and validity never imply accuracy.",
    "Accuracy requires independent reference truth, matching rules and adjudication evidence.",
    "Freshness names both clocks and a purpose-specific budget.",
    "Coverage names a frame version and frame-to-target gap.",
    "Sampled estimates include interval, method and separate sampling, measurement and reference-truth error.",
    "Published assessments are immutable; correction creates a successor and preserves the prior verdict.",
    "Rule or metric revisions never retroactively change issued assessments.",
    "Composite scores retain weights, aggregation model and unknown/not-run treatment.",
    "WM-DAT-007 cannot close issues, execute remediation or certify universal fitness."
  ],
  "holds": [
    "Independent Grok review and reconciliation are pending.",
    "A frozen no-tools semantic audit of the final candidate is pending.",
    "Metric Definition remains identifier-unassigned under EM-DAT-05; formulas are external descriptive references until allocation.",
    "Candidate relation rows confer no mutation or cascade authority.",
    "External method and standards mappings are scoped alignments, not conformance claims."
  ]
}


## Current package: fixtures.json
{"format":"vercy-world-model-fixtures/v1","modelId":"WM-DAT-007","version":"0.3.1-candidate.1","cases":[
  {"id":"complete-but-stale","kind":"positive","input":"All required fields are populated, but the dataset is 41 hours old against a four-hour budget.","expect":"Completeness may pass while freshness fails; accuracy remains not-run without independent truth."},
  {"id":"unknown-coverage-denominator","kind":"negative","input":"Current target-population size is unknown and only a stale proxy frame exists.","expect":"No ratio is published; only counts or a labelled lower bound with proxy bias may be reported."},
  {"id":"partial-high-accuracy","kind":"positive","input":"A 4 percent stratified sample shows 99.2 percent accuracy plus or minus 0.6 at 95 percent confidence.","expect":"The result stays sample-scoped unless frame closure and weights justify inference."},
  {"id":"derived-reference-truth","kind":"negative","input":"The proposed accuracy reference was generated from the assessed dataset.","expect":"Accuracy is rejected or downgraded to internal consistency."},
  {"id":"metric-revision-after-publication","kind":"positive","input":"Metric definition v3 appears after assessment A used v2.","expect":"Assessment A remains interpreted under v2 and is never rewritten."},
  {"id":"remediation-retest","kind":"positive","input":"An external issue is remediated and a retest is requested.","expect":"A new evaluation is created; WM-DAT-007 does not close the issue."},
  {"id":"composite-with-not-run","kind":"negative","input":"A composite score has one satisfied and one not-run result without a declared treatment.","expect":"Publication is rejected until aggregation and not-run treatment are explicit."}
]}


## Current package: local-evidence.md
# EM-DAT-04 local synthesis

## Disposition

- Complete reserved WM-DAT-007 as the Data Quality Evaluation aggregate, using WM-ACT-034 only as the generic assessment shape.
- Reuse WM-KNW-013 for reusable Data Quality Rules, WM-MAT-008 for observations and WM-KNW-014 for Quality Issues.
- Treat Coverage Assessment as a WM-DAT-007 assessment kind with a mandatory frame and denominator state, not as a new master.
- Reference the identifier-unassigned EM-DAT-05 Metric Definition candidate for formulas, populations, units, null semantics and comparability. Remove overlapping metric-definition ownership from WM-DAT-007.
- Allocate no runtime or model identifier.

## Identity and boundary

Rule, metric definition, observation, assessment, result, verdict, issue and remediation retain separate identities and lifecycles. An assessment version pins its subject/version, purpose, consumer, rule and metric revisions, plan, frame, sample, method, engine, input snapshot, clocks and evidence. Published assessment versions are immutable.

Rules own predicates and thresholds. Metric definitions own reusable formulas and population semantics. Observations own measured values and uncertainty. WM-DAT-007 owns the purpose-qualified evaluation and verdict. A violation is an evaluation result; it becomes a WM-KNW-014 issue only when a governed discrepancy record is opened.

## Dimensions and denominators

- Completeness measures required values present over required slots and in-scope rows.
- Accuracy measures agreement with an independent, versioned reference truth over adjudicated comparison pairs.
- Validity measures conformance to a pinned rule over evaluated applicable subjects.
- Freshness measures a named pair of clocks against a purpose-specific latency budget.
- Coverage measures represented target population against a declared versioned frame.

Denominator state is `known-exact`, `estimated` with method/interval/bias, or `unknown`. Unknown denominators block ratio publication. A proxy can yield a labeled lower bound, never an assumed 100% result. Sampling records frame gaps, strata, inclusion probabilities, weights, planned/achieved size and missingness. Sampled estimates include intervals and separate sampling, measurement and reference-truth error.

## Assessment, correction and remediation

Rule evaluation states include satisfied, violated, indeterminate, not-applicable, not-run and waived. These states never collapse. Aggregated scores identify weights, model and treatment of unknown/not-run results.

Corrections create successor assessments with reason, scope and retained predecessor verdict. Rule or metric revisions never retroactively change issued assessments. Remediation retest is a new evaluation and issue closure remains issue-owned.

## Acceptance scenario

A fully populated dataset scores 100% completeness but is 41 hours old against a four-hour budget. Accuracy remains not measured and current-population coverage has an unknown denominator, so it is not fit for real-time pricing. A second assessment covers 4% of frame F v2 and shows 99.2% accuracy ±0.6 at 95% confidence against independent reference R v3. That result is valid only for the sample unless the design supports population inference. The two assessments and their purpose-qualified verdicts stay separate.

## Invariants

1. Rule, metric, observation, assessment, result, verdict, issue and remediation identities are distinct.
2. Every evaluation pins rule/metric revisions, subject version, sample and clocks.
3. Unknown denominator blocks ratio publication.
4. Not-applicable, not-run, unknown, missing, suppressed, satisfied, violated and waived remain distinct.
5. Completeness or validity never implies accuracy.
6. Accuracy requires independently governed reference truth and matching/adjudication rules.
7. Freshness names both clocks and a purpose budget.
8. Coverage names a frame version and frame-to-target gap.
9. Sampled estimates include interval, method and error decomposition.
10. Corrections append successors and never rewrite prior verdicts.
11. Composite scores retain their aggregation model and unknown treatment.
12. WM-DAT-007 cannot close issues, execute remediation or certify universal fitness.

## Holds

The primary and adjacent releases remain non-canonical reviewable drafts with single-provider limitations. The incorrect WM-DAT-001 parent signal is removed and six reference rows are recorded as candidates. WM-KNW-014 now has a corrected candidate reference boundary; Metric Definition still lacks registry allocation. Source/profile pins and crosswalks remain incomplete, while seven representative fixtures are present. This checkpoint makes no canonical completeness, installability or publication claim.


## Current package: sync-plan.json
{"format":"vercy-offline-sync-plan/v1","target":"R:/02_PROJECTS/02_Meta_Models_Platforms/Ver.cy/current/ver-cy/world-models","targetCandidatePath":"research/enterprise/runs/em-dat-04/candidate-wm-dat-007","registryChanges":{"WM-DAT-007":{"name":"Data Quality Evaluation","entry_kind":"aggregate","purpose":"Purpose-qualified versioned evaluation of data quality and its verdict with external rule metric observation issue and remediation authorities","composition_role":"REFERENCE","default_link_type":"TYPED-EDGES","relations_ref":"planning/VERCY-MODEL-RELATIONS.csv"}},"preserve":["research/enterprise/CONTINUATION.md","research/single-stream/STATE.json","research/status.csv","tools/build_enterprise_program.py","research/enterprise/i18n","research/runs/wm-pol-017"]}
