## Verdict

Reuse, do not create. Four of five candidate types map onto frozen models without a new root; the fifth is a profile across the existing decision triad. **Independent identity is required for, and already supplied by**: BenchmarkSpecification (WM-AI-009), SafetyAssessment (WM-AI-008), and the deployment authorization (WM-KNW-010 + WM-ACT-024 + WM-REC-010). **Independent identity is not warranted for**: EvaluationPlan (instance-contained registered protocol in WM-AI-003) and EvaluationRun (serial, instance-scoped execution record in WM-AI-003). Two identifier-unassigned conditional candidates are recorded, not allocated: a *reusable evaluation protocol* independently versioned and approved across instances, and a *standing deployment authorization instrument* with its own holder, validity and renewal. No identifiers are allocated.

## Evidence

WM-AI-003 owns protocol registration, subject and dataset binding, run execution, scoring, results, uncertainty, findings, evidence sealing, waiver, tiered reporting and re-evaluation triggers, with the root fixed at one bounded evaluation instance and campaign grouping explicitly deferred. WM-AI-009 owns benchmark identity, release, items, split roles, protocol contract, metrics and validation, and disclaims ownership of runs, results and leaderboards. WM-AI-008 owns one dated, signed judgement about a named system version: classification, applicability, residual risk, acceptance authority, conditions and reassessment triggers. WM-AI-010 owns a versioned reporting case, not the incident. WM-KNW-010, WM-ACT-024 and WM-REC-010 separate decision content, decision occurrence and issued record.

## Identity/mastership

Artifact identity is WM-SFT-004 (registry key first; digest pins bytes, never business identity). Benchmark release identity is WM-AI-009; source dataset identity is WM-DAT-001. Measurement records are WM-MAT-008. Assessment identity is the WM-AI-008 record, revisions beneath it, one authoritative at a time. Decision identity splits three ways: rationale (WM-KNW-010), act (WM-ACT-024), instrument (WM-REC-010). Benchmark name, score, leaderboard rank, endpoint, alias and date are never identifiers.

## Plan/run/result

Protocol is registered and immutable before any result is observed; the run executes it; the result is computed from item scores by a versioned scorer. Three distinct things, three distinct records, all inside one WM-AI-003 instance. A post-hoc threshold change requires a dated, authorised change record disclosing that results were known. Re-scoring preserves the original value, scorer version, actor and reason. A protocol reused verbatim across subjects remains the same *text* but yields separate instances; only if it is independently versioned and approved does the conditional reusable-protocol candidate apply.

## Benchmark/dataset

BenchmarkSpecification (WM-AI-009 release: task contract, split roles, metric definitions, scoring, thresholds) is separate from the dataset snapshot (item set, digests, sampling, hidden-test controls) and from the source dataset master (WM-DAT-001). WM-AI-003 holds only a version-pinned reference, split designation, checksum and contamination-check result. One split label proves nothing about non-overlap.

## Measurement/uncertainty

Required pins on every result: model artifact identity and digest; inference configuration and endpoint pin; benchmark release and dataset snapshot digest; metric definition identifier from a governed catalogue (semantic change forces a new identifier, not a version); scorer/code and package versions; environment manifest and bounded non-determinism; intended use and deployment context; population and disaggregation factors with minimum subgroup size; uncertainty (sample size, intervals, significance, multiplicity control); declared limitations and validity threats. Judge-model scores carry judge quality evidence. Refusals log separately from task failure.

## Safety assessment

WM-AI-008 consumes evaluation results as cited evidence with integrity digest, executing party, evaluated subject version and a sufficiency judgement; it does not re-measure. Capability measurement answers *what the system does*; the assessment answers *what risk remains in a declared context under declared safeguards*. Evidence whose evaluated subject version differs from the bound subject is re-run or explicitly justified as transferable. Residual risk is point-in-time, bounded by its as-of time, non-authoritative for the risk register.

## Deployment decision

Not a new type. The assessment's residual-risk acceptance is a judgement, not an authorization to deploy. Authorization requires: WM-KNW-010 for the option set, criteria, chosen option, conditions and rationale; WM-ACT-024 for the authorized occurrence, competence, delegation limits and participation; WM-REC-010 for the issued instrument, validity window, service and supersession. The assessment is an input; approval is a separate act with its own authority and its own revocation path.

## Contamination/context drift

Leakage evidence: n-gram/exact-match overlap against training corpora, canary-string detection, holdout exposure counter incremented per binding, membership-inference probes, and transcript scanning for evaluation awareness and harness failure. Distribution shift is a declared gap between the benchmark population and the deployment population. Construct validity asks whether the metric measures the harm it stands for. Context drift is change in intended use, population, operating conditions or integration surface. Staleness is an interval after which evidence is marked stale rather than silently carried.

## Incident feedback

Incident evidence (facts, timeline, causal assessment) stays with WM-AI-010 and its external masters; the report is a communication case, not the occurrence. Incidents enter this contour only as triggers: re-evaluation in WM-AI-003 and reassessment in WM-AI-008. Evaluation emits findings, never incident reports. A receipt from an authority proves neither causality nor remediation effectiveness.

## Time/version/reassessment

Event, observation and ingestion times stay distinct (RFC 3339, explicit offset). Approval, publication and effective instants differ. Reassessment triggers: subject or configuration change, benchmark or dataset release change, metric or scorer change, deployment-context or intended-use change, population shift, incident, contamination discovery, waiver expiry, scheduled cadence, digest mismatch. Expiry without renewal reverts the authorization.

## Acceptance scenario

Benchmark release B v1 → evaluation instance E1 → assessment A1 → authorization D1 for context C1. Release B v2 (changed items and splits) and context C2 (new population, new intended use) fire two triggers. E1 cannot be amended: the dataset binding is part of the immutable protocol, so a new instance E2 registers before results are observed. A1's subject and context bindings are invalidated; A2 is a new revision with its own residual-risk position. D1 does not extend to C2: a new WM-ACT-024 occurrence, new WM-KNW-010 content and a new WM-REC-010 instrument are required. Carrying D1 forward is rejected. **Negative case rejected**: a high score on B v2 is a bounded observation about one population, one metric construct and one configuration; it supports no universal safety claim, and no conformity statement may issue without a decision rule, uncertainty and a named context.

## Invariants

1. Result pins model artifact, configuration, benchmark release, dataset snapshot, metric, scorer, environment. 2. Evaluation validity is context-bounded. 3. Every decision names an accountable authority, scope, conditions and validity. 4. Protocol and thresholds precede results. 5. Measurement never implies permission. 6. Assessment never implies authorization. 7. Absence of a metric is not absence of risk. 8. Split labels do not prove non-contamination. 9. Evidence is revision-bound and goes stale by rule. 10. Corrections are additive; issued records are never rewritten.

## Minimal model set

WM-AI-003, WM-AI-009, WM-AI-008, WM-AI-010, WM-SFT-004, WM-DAT-001, WM-MAT-008, WM-KNW-010, WM-ACT-024, WM-REC-010.

## Holds

Contradictions: (a) WM-AI-003 and WM-AI-009 both define protocol and metric ownership — benchmark-level contract versus instance-level applied protocol must be arbitrated; (b) three models mint a decision (WM-AI-003 approval/waiver, WM-AI-008 acceptance, the triad) — collapse to gate-decision versus authorization; (c) WM-AI-009's WM-DAT-001 parent edge is unapproved, so dataset ownership is unenforced; (d) WM-AI-003's incident and risk siblings are unregistered and WM-AI-010's edges are unapproved. Gaps: no master identifier for the evaluation instance itself (deferred in WM-AI-003); no frozen deployment/endpoint model, so deployment context has no master; Croissant 1.0/1.1 conflict affects split and hash semantics; continual-learning and closed-API reproducibility unresolved. WM-AI-009 and WM-AI-010 are codex-only with no external review; WM-AI-008 is Claude-only; all four carry paywalled-ISO and source-pin holds. No claim of canonical completeness, installability or publication readiness.
