# Frozen semantic audit prompt — EM-AI-03

You are the sole frozen semantic auditor for this contour. This audit runs exactly once. Use only supplied text. Do not browse, call tools, invent identifiers, claim standards conformance or propose publication of blockers.

Audit the reconciled boundary and allocation/profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence/rights semantics, nondeterministic fixtures and missing publishability holds. Preserve the intended decision unless the evidence disproves it: reuse WM-AI-003 with distinct applied-plan/run/result roles, WM-AI-009 benchmark, WM-AI-008 safety assessment, WM-AI-010 incident report and the decision triad; keep both conditional candidates identifier-unassigned without present independent identity; allocate no catalogue, model or runtime ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect exact deterministic remediation; Exact additional fixtures as a JSON array; final freeze decision. Be sceptical and concise. Never request another provider run.

## LOCAL SYNTHESIS

```text
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

```

## CLAUDE STUDY

```text
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

```

## GROK STUDY

```text
Verdict. Conditionally accept. Applied plan, run and result stay inside one WM-AI-003 evaluation occurrence only as distinct roles with separate state, time and authorship. Benchmark Specification reuses WM-AI-009. Safety Assessment reuses WM-AI-008. Deployment Decision is profiled across rationale, authorized act and issued instrument. No other identifier is allocated. Explicit decision: neither conditional candidate needs independent identity. Evaluation Protocol and standing Deployment Authorization Instrument remain identifier-unassigned.

Strongest evidence. The proposal keeps identifier economy while the required separations are realizable as roles and pinned references inside the listed drafts. A dataset-snapshot change plus a context change then cannot reuse a prior score, assessment or instrument. That matches the test: no carry-forward, and no high score as universal safety proof.

Strongest counterexample. The benchmark dataset snapshot is replaced and the deployment context shifts in intended use, population or environment. The prior score, the prior WM-AI-008 assessment and the prior authorization are treated as still valid. That fuses measurement with safety judgement and lets an approval cross unpinned context. A second failure is an undifferentiated WM-AI-003 record in which a later run rewrites the plan or overwrites the prior result.

Identity and mastership. WM-AI-003 masters the applied evaluation occurrence. Plan, run and result are roles of that occurrence, not separate masters and not a fused attribute bag. WM-AI-009 masters the benchmark contract, not the dataset. The snapshot actually scored is mastered by WM-DAT-001 and pinned. WM-AI-008 masters safety judgement, not capability scores. The decision triad masters rationale, authorized act and issued instrument. WM-AI-010 masters the incident report. Incident evidence remains WM-MAT-008 observations and WM-SFT-004 artifacts. Same plan content may be cited by a later occurrence; the applied plan role of the earlier occurrence is not reopened.

Plan, run and result. The plan states intended pins before execution. The run records execution against those pins. The result records measurements only after a completed run. A failed run does not rewrite the plan. A pin delta is a new occurrence, not an edit of the prior result.

Benchmark and dataset. The contract — tasks, metrics, acceptance criteria — is WM-AI-009. The snapshot scored is WM-DAT-001. Replacing the snapshot does not mutate the specification and does not preserve prior results.

Measurement and uncertainty. Capability scores are results. Metric, scorer, uncertainty and limitations are mandatory. A missing or unversioned pin blocks result acceptance. A score is not a safety judgement.

Safety assessment. WM-AI-008 consumes pinned results plus intended use, population, context and limitations. It does not authorize deployment. Assessment validity ends when a cited pin changes.

Deployment decision. Rationale is decision content. The authorized act is the decision event. The issued instrument is the binding record. Editing rationale after issue is a new decision. An instrument is not valid outside its stated context, intended use and population.

Contamination and context drift. Train/eval overlap, scorer leakage, population shift, environment shift or intended-use shift invalidates the occurrence. Drift is a reassessment trigger, not a silent score update.

Incident feedback. WM-AI-010 cites evidence and does not contain or replace it. A material incident can invalidate a prior assessment and instrument and requires reassessment. Evidence is not mutated inside the report.

Time, version and reassessment. Artifact, configuration, benchmark, dataset, metric, scorer, environment, context, intended use, population, uncertainty and limitations are versioned pins. A delta on dataset, scorer, configuration, environment, context, intended use or population starts a new evaluation occurrence, a new assessment and an explicit re-authorization. Prior approval does not carry forward.

Scenario. Dataset snapshot moves from the pinned version to a successor, and deployment context moves, for example from internal assist to external customer action. Required outcome: a new WM-AI-003 occurrence with a new plan role, run role and result role; a new WM-AI-008 assessment; a newly issued authorization. The old high score is retained only as historical measurement. It is not safety proof and does not extend the old instrument.

Invariants.
1. Plan, run and result are distinct roles of one WM-AI-003 occurrence.
2. A result cannot exist before its run; a run cannot rewrite its plan.
3. Benchmark contract and dataset snapshot have different masters.
4. A dataset snapshot change requires a new evaluation occurrence.
5. Capability measurement is not a safety judgement.
6. A safety assessment does not authorize deployment.
7. Decision content, authorized act and issued instrument are distinct.
8. An issued instrument is not revised by editing its rationale.
9. One score is not universal safety proof and does not transfer across dataset, context, configuration or population.
10. An incident report does not contain or replace incident evidence.
11. A change in context, intended use or population invalidates prior authorization.
12. Uncertainty and limitations are mandatory on result and on assessment.
13. Contamination or context drift triggers reassessment, not an in-place score update.
14. Missing or unversioned pins block result acceptance.
15. Neither conditional candidate is allocated an identifier unless an independent lifecycle is later shown.

Minimum model set. WM-AI-003 with plan, run and result roles; WM-AI-009; WM-DAT-001 snapshot; WM-AI-008; decision triad profile (rationale, authorized act, issued instrument); WM-SFT-004; WM-MAT-008; WM-AI-010. No Evaluation Protocol type. No standing authorization type.

Blockers. Acceptance is blocked until the role split inside WM-AI-003 is explicit; until dataset, scorer, configuration, environment, context, intended-use or population change is an invalidation rule; until non-carry-forward is explicit; until uncertainty and limitations are mandatory on measurement and assessment; until incident evidence is kept out of the report body; and until rationale cannot be edited after the instrument is issued. This review does not claim publication readiness.

```

## EVALUATION PROTOCOL

```text
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-AI-03",
  "proposedName": "Reusable Evaluation Protocol",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NO NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A protocol is independently identifiable only when a governed evaluation specification is versioned, approved and reused across evaluation instances.",
    "versionIdentity": "Changes to task contract, metric set, thresholds, scorer requirements or validity scope create immutable revisions.",
    "independentLifecycle": [
      "draft",
      "approved",
      "effective",
      "suspended",
      "superseded",
      "retired"
    ],
    "mastership": "AI evaluation-method governance authority"
  },
  "boundary": {
    "owns": [
      "stable reusable protocol identity",
      "immutable protocol revisions",
      "required task, metric, scorer and threshold contract",
      "validity scope and transfer conditions",
      "effective periods and approval lineage"
    ],
    "references": [
      {
        "target": "WM-AI-003",
        "purpose": "Evaluation instances that apply a pinned protocol revision"
      },
      {
        "target": "WM-AI-009",
        "purpose": "Benchmark specification and release contract"
      },
      {
        "target": "WM-AI-008",
        "purpose": "Safety assessments consuming evaluation evidence"
      },
      {
        "target": "WM-SFT-004",
        "purpose": "Pinned evaluated model artifact"
      },
      {
        "target": "WM-DAT-001",
        "purpose": "Pinned evaluation dataset snapshot"
      },
      {
        "target": "WM-MAT-008",
        "purpose": "Result observations and uncertainty"
      }
    ],
    "excludes": [
      "evaluation-run execution identity",
      "benchmark and dataset identity",
      "model artifact identity",
      "safety judgement",
      "deployment authorization"
    ]
  },
  "objects": {
    "EvaluationProtocol": {
      "identity": [
        "evaluationProtocolId"
      ],
      "required": [
        "name",
        "ownerRef",
        "status",
        "currentRevisionRef"
      ],
      "optional": [
        "successorRef"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "effective",
        "suspended",
        "superseded",
        "retired"
      ]
    },
    "EvaluationProtocolRevision": {
      "identity": [
        "evaluationProtocolId",
        "revision"
      ],
      "required": [
        "taskContract",
        "metricRefs",
        "scorerRequirements",
        "thresholds",
        "validityScope",
        "contentDigest",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "supersedesRevision",
        "transferConditions"
      ]
    }
  },
  "invariants": [
    "Independent identity requires governed versioning and reuse across evaluations.",
    "Every applying evaluation pins one immutable protocol revision.",
    "Protocol and thresholds are registered before results are observed.",
    "Post-hoc changes require authorized disclosure and successor evaluation evidence.",
    "A protocol revision never owns an execution outcome.",
    "Benchmark, dataset, model artifact and metric definitions retain external mastership.",
    "Every result pins artifact, configuration, benchmark, dataset, metric, scorer and environment.",
    "Split labels alone never prove non-contamination.",
    "Evaluation validity is bounded by purpose, population and deployment context.",
    "Corrections and rescoring are additive and preserve originals.",
    "Measurement never implies safety or deployment permission.",
    "Evidence is revision-bound and becomes stale by declared rule.",
    "Protected benchmark items and confidential artifacts remain outside the public catalogue.",
    "Retired protocol identifiers and revisions remain resolvable and are never recycled."
  ],
  "holds": [
    "No identifier is allocated or may be guessed.",
    "Independent Grok review complete; frozen semantic audit pending.",
    "The candidate has no present independent identity.",
    "Canonical base drafts and relations remain publication gates.",
    "No installability or publication-readiness claim is made."
  ],
  "candidateRevision": 1,
  "status": "held",
  "installable": false,
  "presentIndependentIdentity": false,
  "conditionsUnmet": [
    "independent lifecycle and mastership distinct from the reused base models",
    "registry allocation"
  ]
}

```

## DEPLOYMENT AUTHORIZATION

```text
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-AI-03",
  "proposedName": "Standing Deployment Authorization Instrument",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NO NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A standing authorization is independently identifiable only when it persists beyond one decision occurrence with its own holder, scope, validity, renewal and revocation lifecycle.",
    "versionIdentity": "Scope, conditions, accountable authority, validity or safeguards change only through a successor instrument or revision.",
    "independentLifecycle": [
      "draft",
      "issued",
      "effective",
      "suspended",
      "revoked",
      "expired",
      "superseded"
    ],
    "mastership": "competent deployment-authorization authority"
  },
  "boundary": {
    "owns": [
      "standing authorization identity",
      "holder, scope, conditions and safeguards",
      "validity, renewal, suspension and revocation",
      "issuing authority and competence evidence",
      "successor and supersession lineage"
    ],
    "references": [
      {
        "target": "WM-KNW-010",
        "purpose": "Decision options, criteria, conditions and rationale"
      },
      {
        "target": "WM-ACT-024",
        "purpose": "Authorized decision occurrence and competence"
      },
      {
        "target": "WM-REC-010",
        "purpose": "Issued record and immutable instrument evidence"
      },
      {
        "target": "WM-AI-008",
        "purpose": "Safety assessment cited as evidence"
      },
      {
        "target": "WM-AI-003",
        "purpose": "Evaluation evidence and reevaluation triggers"
      }
    ],
    "excludes": [
      "evaluation measurement",
      "safety assessment judgement",
      "decision rationale",
      "single issuance occurrence",
      "deployment or endpoint lifecycle"
    ]
  },
  "objects": {
    "DeploymentAuthorizationInstrument": {
      "identity": [
        "authorizationInstrumentId"
      ],
      "required": [
        "holderRef",
        "scope",
        "conditions",
        "authorityRef",
        "validFrom",
        "status"
      ],
      "optional": [
        "validTo",
        "renewalTerms",
        "revocationTerms",
        "successorRef"
      ],
      "lifecycle": [
        "draft",
        "issued",
        "effective",
        "suspended",
        "revoked",
        "expired",
        "superseded"
      ]
    },
    "AuthorizationRevision": {
      "identity": [
        "authorizationInstrumentId",
        "revision"
      ],
      "required": [
        "scope",
        "conditions",
        "safeguards",
        "contentDigest",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "supersedesRevision"
      ]
    }
  },
  "invariants": [
    "Independent identity requires persistence beyond one issued decision record.",
    "Every authorization names accountable authority, holder, scope, conditions and validity.",
    "Assessment acceptance never implies authorization.",
    "Evaluation measurement never implies permission.",
    "Expired, revoked or suspended authorization is not effective.",
    "Context or subject changes require scope proof, successor authorization or explicit non-applicability.",
    "Issued records remain immutable and corrections are additive.",
    "Authorization conditions never overwrite cited assessment or evaluation evidence.",
    "Decision rationale, authorized act and issued instrument retain separate mastership.",
    "Renewal creates a governed successor or revision with preserved history.",
    "Revocation records actor, authority, time and reason.",
    "Standing authorization never owns deployment or endpoint runtime lifecycle.",
    "A high score cannot widen authorization scope.",
    "Retired identifiers and revisions remain resolvable and are never recycled."
  ],
  "holds": [
    "No identifier is allocated or may be guessed.",
    "Independent Grok review complete; frozen semantic audit pending.",
    "The candidate has no present independent identity.",
    "Canonical base drafts and relations remain publication gates.",
    "No installability or publication-readiness claim is made."
  ],
  "candidateRevision": 1,
  "status": "held",
  "installable": false,
  "presentIndependentIdentity": false,
  "conditionsUnmet": [
    "independent lifecycle and mastership distinct from the reused base models",
    "registry allocation"
  ]
}

```

## PROFILE

```text
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-AI-03",
  "name": "Enterprise AI Evaluation, Safety and Deployment Decision Binding",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-AI-003",
    "WM-AI-009",
    "WM-AI-008",
    "WM-AI-010",
    "WM-SFT-004",
    "WM-DAT-001",
    "WM-MAT-008",
    "WM-KNW-010",
    "WM-ACT-024",
    "WM-REC-010"
  ],
  "constraints": [
    "WM-AI-003 owns one evaluation occurrence with distinct applied-plan, run and result roles; a run cannot rewrite its plan and a result requires a completed run.",
    "WM-AI-009 owns the benchmark contract; WM-DAT-001 owns the evaluated dataset snapshot and replacing it creates a new evaluation occurrence.",
    "Every accepted result pins model artifact, configuration, benchmark, dataset snapshot, metric, scorer, code and tool versions, environment, context, intended use, population, uncertainty and limitations.",
    "Capability measurement is not a safety judgement; WM-AI-008 consumes pinned evidence and does not authorize deployment.",
    "Deployment rationale, authorized act and issued record remain WM-KNW-010, WM-ACT-024 and WM-REC-010 roles; editing rationale after issue requires a new decision.",
    "Dataset, scorer, configuration, environment, context, intended-use or population change invalidates prior evaluation, assessment and authorization and requires new explicit evidence and decision.",
    "Contamination, leakage or context drift triggers reassessment and never an in-place score update.",
    "WM-AI-010 cites incident evidence mastered externally by WM-MAT-008 and WM-SFT-004 and never contains or replaces it.",
    "A high benchmark score is historical measurement only and cannot widen authorization scope or prove universal safety.",
    "Reusable Evaluation Protocol and Standing Deployment Authorization Instrument have no present independent identity and no assigned identifier."
  ],
  "holds": [
    "Independent Grok review complete; frozen semantic audit pending.",
    "Base relations, complete immutable pins and canonical base publication remain unresolved.",
    "Both conditional candidates are unassigned.",
    "canonicalPublishable and installable remain false."
  ],
  "candidateRevision": 1,
  "status": "held",
  "canonicalPublishable": false,
  "installable": false,
  "constraintsAreNonExhaustive": false,
  "basePins": [
    {
      "modelId": "WM-AI-003",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-AI-009",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-AI-008",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-AI-010",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-SFT-004",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-DAT-001",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-MAT-008",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-KNW-010",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-ACT-024",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    },
    {
      "modelId": "WM-REC-010",
      "version": null,
      "digest": null,
      "verification": "unverified-current-draft"
    }
  ],
  "invariants": [
    "Plan, run and result are distinct roles of one evaluation occurrence.",
    "Result follows a completed run and neither run nor result rewrites the applied plan.",
    "Benchmark contract and dataset snapshot retain separate masters.",
    "A dataset snapshot change requires a new evaluation occurrence.",
    "Capability measurement is not a safety judgement.",
    "A safety assessment does not authorize deployment.",
    "Decision rationale, authorized act and issued record remain distinct.",
    "Issued rationale is immutable; correction requires a successor decision.",
    "Scores do not transfer across dataset, configuration, context, intended use or population.",
    "Incident reports cite and never contain or replace incident evidence.",
    "Context, intended-use or population change invalidates prior authorization.",
    "Uncertainty and limitations are mandatory on result and assessment.",
    "Contamination or drift triggers reassessment, never in-place score mutation.",
    "Missing or unversioned pins block result acceptance.",
    "No conditional candidate has an assigned identifier or present independent identity."
  ]
}

```

## ALLOCATION FIXTURES EP

```text
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Reusable Evaluation Protocol",
  "cases": [
    {
      "id": "unassigned-candidate-not-referenceable",
      "kind": "negative",
      "invariants": [
        1
      ],
      "pins": {
        "allocationState": "unassigned",
        "modelId": null
      },
      "input": "A public artifact references this candidate as an identified model.",
      "expect": "Rejected; no identifier is allocated and the candidate has no present independent identity.",
      "expectedCode": "UNASSIGNED_CANDIDATE_REFERENCE"
    },
    {
      "id": "future-independent-lifecycle",
      "kind": "positive",
      "conditional": true,
      "blockedBy": "allocationState=unassigned",
      "invariants": [
        1,
        2
      ],
      "pins": {
        "allocationState": "unassigned"
      },
      "input": "A future proposal supplies independent lifecycle, mastership and reuse evidence.",
      "expect": "It remains held until registry review and allocation; this checkpoint allocates nothing."
    }
  ]
}

```

## ALLOCATION FIXTURES DA

```text
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Standing Deployment Authorization Instrument",
  "cases": [
    {
      "id": "unassigned-candidate-not-referenceable",
      "kind": "negative",
      "invariants": [
        1
      ],
      "pins": {
        "allocationState": "unassigned",
        "modelId": null
      },
      "input": "A public artifact references this candidate as an identified model.",
      "expect": "Rejected; no identifier is allocated and the candidate has no present independent identity.",
      "expectedCode": "UNASSIGNED_CANDIDATE_REFERENCE"
    },
    {
      "id": "future-independent-lifecycle",
      "kind": "positive",
      "conditional": true,
      "blockedBy": "allocationState=unassigned",
      "invariants": [
        1,
        2
      ],
      "pins": {
        "allocationState": "unassigned"
      },
      "input": "A future proposal supplies independent lifecycle, mastership and reuse evidence.",
      "expect": "It remains held until registry review and allocation; this checkpoint allocates nothing."
    }
  ]
}

```

## PROFILE FIXTURES

```text
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "contourId": "EM-AI-03",
  "cases": [
    {
      "id": "changed-dataset-and-context",
      "kind": "positive",
      "invariants": [
        4,
        9,
        11
      ],
      "pins": {
        "datasetBefore": "D1@1",
        "datasetAfter": "D1@2",
        "contextBefore": "internal-assist",
        "contextAfter": "external-customer-action"
      },
      "input": "Dataset snapshot and deployment context both change.",
      "expect": "A new WM-AI-003 occurrence, new WM-AI-008 assessment and new explicit decision are required; old approval remains historical.",
      "expectedCode": "NEW_EVALUATION_ASSESSMENT_AUTHORIZATION"
    },
    {
      "id": "high-score-universal-safety",
      "kind": "negative",
      "invariants": [
        5,
        6,
        9
      ],
      "pins": {
        "score": 0.99
      },
      "input": "A high benchmark score is used as universal safety proof and deployment permission.",
      "expect": "Rejected; measurement is neither safety judgement nor authorization.",
      "expectedCode": "MEASUREMENT_NOT_AUTHORIZATION"
    },
    {
      "id": "missing-uncertainty",
      "kind": "negative",
      "invariants": [
        12,
        14
      ],
      "pins": {
        "uncertainty": null,
        "limitations": null
      },
      "input": "A result omits uncertainty and limitations.",
      "expect": "Rejected; the result cannot be accepted.",
      "expectedCode": "RESULT_EVIDENCE_INCOMPLETE"
    },
    {
      "id": "incident-embeds-evidence",
      "kind": "negative",
      "invariants": [
        10
      ],
      "pins": {
        "incident": "I1",
        "embeddedObservation": "O1"
      },
      "input": "An incident report replaces the observation record with embedded mutable evidence.",
      "expect": "Rejected; the report must cite externally mastered immutable evidence.",
      "expectedCode": "INCIDENT_EVIDENCE_MASTERSHIP"
    },
    {
      "id": "role-ordering",
      "kind": "positive",
      "invariants": [
        1,
        2
      ],
      "pins": {
        "planAt": "2026-01-01T00:00:00+00:00",
        "runCompletedAt": "2026-01-02T00:00:00+00:00",
        "resultAt": "2026-01-02T01:00:00+00:00"
      },
      "input": "Plan is frozen before the run and result follows completion.",
      "expect": "Accepted as one occurrence with three distinct roles."
    }
  ]
}

```
