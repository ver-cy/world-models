# EM-AI-03 local synthesis

## Disposition

- Reuse WM-AI-003 for one bounded evaluation instance containing its applied Evaluation Plan, Evaluation Run and results.
- Reuse WM-AI-009 for independently identified Benchmark Specification and evaluation-dataset releases.
- Reuse WM-AI-008 for independently identified Safety Assessment.
- Profile Deployment Decision across WM-KNW-010 rationale, WM-ACT-024 authorized occurrence and WM-REC-010 issued instrument; create no new root.
- Keep an independently governed reusable Evaluation Protocol and a standing Deployment Authorization Instrument as conditional identifier-unassigned candidates only when they have lifecycles outside one evaluation or decision occurrence.
- Reuse WM-AI-010 only as incident-report feedback and trigger evidence.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

WM-AI-003 owns one evaluation instance, applied protocol, execution records, scoring, results, uncertainty, findings and reevaluation triggers. WM-AI-009 owns benchmark identity, release, task contract, item/split rules, metrics and validation. WM-AI-008 owns one dated assessment judgement for a pinned system and context.

Artifact identity stays in WM-SFT-004, dataset identity in WM-DAT-001 and measurements in WM-MAT-008. Decision content, decision occurrence and issued instrument remain separate masters. Scores, ranks, endpoint addresses and dates are never identifiers.

## Plan, run and result

The applied Evaluation Plan or protocol is registered immutably before results are observed. Evaluation Run executes it. Results are produced through a pinned scorer. These are distinct records within one evaluation instance.

Post-hoc threshold changes require an authorized change record that discloses prior result visibility. Rescoring creates an additive successor while preserving the original score, scorer version, actor and reason.

A protocol needs a separate root only when it is independently versioned, approved and reused across evaluation instances. Otherwise the applied protocol remains WM-AI-003-contained.

## Benchmark and dataset

WM-AI-009 Benchmark Specification defines the task contract, split roles, metric references, scoring and thresholds. The benchmark release is distinct from its dataset snapshot, item digests, hidden-test controls and the source dataset master.

WM-AI-003 pins benchmark release, dataset snapshot, split designation and checksum. A split label alone does not prove non-overlap or non-contamination.

## Measurement and uncertainty

Every result pins model artifact and digest, inference configuration, benchmark and dataset release, metric definition, scorer/code/packages, environment, intended use, deployment context, population, disaggregation factors, sample size, intervals, significance method, multiplicity control, limitations and validity threats.

Judge-model scores cite judge quality evidence. Refusal is recorded separately from task failure. A high score remains a bounded observation and never proves universal capability, safety or permission.

## Safety assessment

WM-AI-008 consumes evaluation results as cited evidence and records their sufficiency for a named system version, intended purpose, population, deployment context and safeguards. It does not repeat measurement.

Capability measurement asks what occurred under an evaluation protocol. Safety Assessment asks what residual risk remains in a declared context. Evidence for a different subject or context requires rerun or explicit transfer justification. Residual risk is time-bounded and does not replace the risk register.

## Deployment decision

Assessment acceptance is not deployment authorization. WM-KNW-010 holds options, criteria, conditions and rationale; WM-ACT-024 holds the authorized act and competence; WM-REC-010 holds the issued instrument, scope, validity and supersession.

The assessment is evidence for the decision. Authorization has its own accountable authority, conditions, revocation and expiry. A standing instrument needs an independent candidate only if it persists with holder, renewal and validity beyond one issued record.

## Contamination, drift and incident feedback

Leakage evidence includes exact/n-gram overlap, canaries, holdout exposure counters, membership-inference probes and transcript inspection for evaluation awareness. Distribution shift compares benchmark and deployment populations. Construct validity asks whether the metric measures the claimed capability or harm.

Changes in intended use, population, integration surface, operating conditions, model, configuration, benchmark, dataset, metric or scorer trigger reevaluation or reassessment. WM-AI-010 incident reports remain separate reporting cases and supply trigger evidence; authority receipt proves neither causality nor remediation effectiveness.

## Time, version and reassessment

Event, observation, ingestion, approval, publication and effective times remain distinct. Evidence is revision-bound and becomes stale by declared rule. Expired authorization returns to unauthorized unless a valid successor exists.

Reassessment triggers include digest mismatch, subject/configuration change, benchmark/dataset release, metric/scorer change, context/population drift, incident, contamination discovery, waiver expiry and scheduled cadence.

## Acceptance result

Benchmark B-v1 supports evaluation E1, assessment A1 and authorization D1 for context C1. Benchmark B-v2 changes items and splits while deployment context C2 changes population and intended use. E1 remains immutable; E2 registers a new protocol before results. A2 creates a new residual-risk judgement, and D1 does not extend to C2. New rationale, authorized act and issued instrument are required. A high B-v2 score alone cannot authorize C2 or establish universal safety.

## Required invariants

1. Results pin artifact, configuration, benchmark, dataset, metric, scorer and environment.
2. Evaluation validity is context-bounded.
3. Every authorization names authority, scope, conditions and validity.
4. Protocol and thresholds precede observed results.
5. Measurement never implies permission.
6. Assessment never implies authorization.
7. Missing metrics do not prove missing risk.
8. Split labels do not prove non-contamination.
9. Evidence is revision-bound and becomes stale by rule.
10. Corrections are additive and issued records are immutable.
11. Capability, safety judgement and deployment authorization remain separate.
12. Context change triggers explicit transfer justification or new work.

## Holds

WM-AI-003 and WM-AI-009 overlap on protocol and metric ownership and need an applied-protocol versus benchmark-contract split. WM-AI-003, WM-AI-008 and the decision triad contain overlapping decision concepts that require gate-versus-authorization rules. WM-AI-009's WM-DAT-001 relation is unapproved. Evaluation-instance master identity and frozen endpoint/deployment authority remain gaps. Conditional reusable protocol and standing authorization candidates have no allocations. All target drafts retain source, provider and fixture holds. No installability or publication-readiness claim is made.
