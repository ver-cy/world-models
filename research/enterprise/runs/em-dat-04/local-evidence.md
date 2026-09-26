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

The primary and adjacent releases remain non-canonical reviewable drafts with single-provider limitations. Candidate relations and several parent contracts remain unresolved; WM-KNW-014 has no settled relationship contract; Metric Definition lacks registry allocation; source/profile pins, crosswalks and representative fixtures are incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
