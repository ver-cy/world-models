# Frozen audit request: EM-TEC-05

You are the final independent semantic auditor. No tools or browsing. Review only the frozen materials below. Return: Verdict (ACCEPT / ACCEPT WITH LIMITS / REVISE / REJECT); blocking findings; non-blocking findings; invariant and fixture gaps; exact minimal remediations. Challenge identity, lifecycle, mastership, same-occurrence cyber handling, RootCauseClaim containment, clocks and non-cascade behavior. Do not invent identifiers or claim publication readiness.

## Candidate
```json
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-TEC-05",
  "modelId": "WM-ACT-019",
  "registryId": "vr.wm-act-019",
  "name": "Operational / Service Incident",
  "version": "0.1.0-candidate.2",
  "entryKind": "incident-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Extend and rewrite the reserved legacy WM-ACT-019 boundary for authority-declared operational or service incidents while preserving separate observation, cyber qualification, problem, defect, task and communication masters.",
  "disposition": {
    "kind": "complete-reserved-model-by-rewrite",
    "newModelId": false,
    "reason": "The legacy physical-emergency specification does not support the required service-incident semantics and cannot be treated as a thin profile."
  },
  "boundary": {
    "owns": [
      "one incident declaration identity per determined occurrence",
      "definition-pinned declaration and revision history",
      "severity and revisioned incident impact assertions",
      "containment restoration resolution closure and reopen history",
      "incident review findings and recommendations"
    ],
    "delegates": [
      "observations and occurrence evidence to WM-MAT-008 and WM-ACT-015",
      "cyber qualification and regulatory clocks to WM-ACT-020",
      "persistent discrepancy problem and root-cause claims to WM-KNW-014",
      "version-pinned product nonconformity to reserved WM-SFT-014",
      "containment restoration and remediation work to WM-ACT-006",
      "public or addressed communications to WM-ACT-027"
    ],
    "excludes": [
      "automatic incident identity from an alert",
      "a second peer incident master for cyber qualification",
      "problem defect or task lifecycle",
      "cause-claim overwrite",
      "closure cascade across aggregates",
      "priority derived from severity"
    ]
  },
  "objects": {
    "Incident": {
      "identity": [
        "incidentId"
      ],
      "required": [
        "incidentClass",
        "definitionRevisionRef",
        "declaredAt",
        "declarationDecisionRef",
        "authorityRef",
        "ownerRef",
        "status"
      ],
      "optional": [
        "reportedAt",
        "detectedAt",
        "observedAt",
        "containedAt",
        "restoredAt",
        "resolvedAt",
        "closedAt",
        "problemRefs",
        "cyberQualificationRef"
      ],
      "lifecycle": [
        "reported",
        "declared",
        "contained",
        "restored",
        "resolved",
        "closed",
        "withdrawn",
        "reopened"
      ],
      "rule": "One declaration identity exists per determined incident occurrence; specialization or correspondence never mints a peer incident master."
    },
    "DeclarationDecision": {
      "identity": [
        "declarationDecisionId"
      ],
      "required": [
        "candidateEventRefs",
        "definitionRevisionRef",
        "authorityRef",
        "decision",
        "effectiveAt",
        "rationale",
        "recordedAt"
      ],
      "optional": [
        "confidence",
        "supersedesDecisionId"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    },
    "SeverityAssessment": {
      "identity": [
        "severityAssessmentId"
      ],
      "required": [
        "incidentRef",
        "scaleRef",
        "grade",
        "assessorRef",
        "assessedAt",
        "basisRefs"
      ],
      "optional": [
        "supersedesAssessmentId",
        "confidence"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    },
    "ImpactAssessment": {
      "identity": [
        "impactAssessmentId"
      ],
      "required": [
        "incidentRef",
        "impactDomain",
        "actuality",
        "method",
        "assessorRef",
        "effectiveAt",
        "recordedAt",
        "basisRefs"
      ],
      "optional": [
        "quantity",
        "unitRef",
        "affectedSubjectRefs",
        "supersedesAssessmentId"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ],
      "rule": "Identified revisioned child of exactly one incident; no implicit roll-up to Problem."
    },
    "IncidentStateTransition": {
      "identity": [
        "transitionId"
      ],
      "required": [
        "incidentRef",
        "fromStatus",
        "toStatus",
        "effectiveAt",
        "authorityRef",
        "evidenceRefs",
        "recordedAt"
      ],
      "optional": [
        "reason"
      ],
      "rule": "Transitions append; reopening and correction preserve all prior state, impact and review records."
    },
    "ResolutionRecord": {
      "identity": [
        "resolutionRecordId"
      ],
      "required": [
        "incidentRef",
        "outcome",
        "resolvedAt",
        "authorityRef",
        "residualRiskRef",
        "evidenceRefs"
      ],
      "optional": [
        "restorationTaskRefs",
        "problemRefs",
        "followUpRefs"
      ],
      "lifecycle": [
        "proposed",
        "effective",
        "superseded"
      ]
    },
    "IncidentReview": {
      "identity": [
        "reviewId"
      ],
      "required": [
        "incidentRef",
        "reviewedAt",
        "reviewerRefs",
        "evidenceRefs",
        "findings",
        "recommendations"
      ],
      "optional": [
        "actionTaskRefs",
        "publicationRef"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "superseded"
      ]
    },
    "IncidentCorrespondence": {
      "identity": [
        "correspondenceId"
      ],
      "required": [
        "incidentRef",
        "peerRecordRef",
        "peerModelRef",
        "representationRole",
        "sameOccurrenceBasisRefs",
        "assertedAt",
        "authorityRef"
      ],
      "optional": [
        "confidence",
        "validTo"
      ],
      "rule": "REFERENCE only; correspondence never proves identity or creates another master."
    }
  },
  "problemProfile": {
    "base": "WM-KNW-014",
    "rootCauseClaim": {
      "identity": [
        "problemRef",
        "claimId"
      ],
      "required": [
        "statement",
        "status",
        "confidence",
        "evidenceRefs",
        "assertedAt",
        "assertedBy"
      ],
      "optional": [
        "incidentRefs",
        "defectRef",
        "supersedesClaimId"
      ],
      "statuses": [
        "asserted",
        "supported",
        "disputed",
        "withdrawn",
        "endorsed"
      ],
      "rule": "First-class namespaced child of Problem; competing claims coexist and are never represented by overwriting one root-cause field."
    },
    "closureRule": "Problem may close only under its own disposition authority; incident restoration or closure has no cascade effect."
  },
  "cyberQualification": {
    "base": "WM-ACT-020",
    "identityRule": "Specializes or qualifies the same incident declaration identity; if an implementation retains a separate record, IncidentCorrespondence is mandatory and the record is not a peer incident master.",
    "owns": [
      "cyber determination",
      "regulatory reporting clocks",
      "evidence custody",
      "attribution and disclosure markings"
    ]
  },
  "relations": [
    {
      "target": "WM-ACT-015",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve occurrence evidence used by declaration."
    },
    {
      "target": "WM-MAT-008",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve observations without copying identity."
    },
    {
      "target": "WM-ACT-020",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve cyber qualification under the single-declaration rule."
    },
    {
      "target": "WM-KNW-014",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve persistent problems and their cause claims."
    },
    {
      "target": "WM-SFT-014",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve version-pinned defects; reserved external boundary only."
    },
    {
      "target": "WM-ACT-006",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve containment restoration and remediation tasks."
    },
    {
      "target": "WM-ACT-027",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve communication delivery records."
    }
  ],
  "clockSemantics": [
    "occurrenceAt",
    "detectedAt",
    "observedAt",
    "declaredAt",
    "containedAt",
    "restoredAt",
    "resolvedAt",
    "closedAt",
    "recordedAt"
  ],
  "invariants": [
    "INV-001 Observation event alarm or report never becomes an incident without an authorized definition-pinned declaration decision.",
    "INV-002 One determined occurrence has at most one incident declaration identity across operational cyber and AI qualifications.",
    "INV-003 Cyber qualification may specialize a declaration but never creates a peer incident master.",
    "INV-004 If a separate cyber record is retained it requires explicit same-occurrence correspondence with representation role and evidence.",
    "INV-005 Incident Problem Defect Task Communication and observation identities never merge.",
    "INV-006 Severity assessments name their scale and append rather than overwrite.",
    "INV-007 Task priority is independently asserted and is never copied or derived from incident severity.",
    "INV-008 ImpactAssessment is an identified revisioned incident child and distinguishes actual from potential impact.",
    "INV-009 Problem impact is never an implicit roll-up of incident impact.",
    "INV-010 RootCauseClaim is a namespaced Problem child with evidence confidence status and provenance.",
    "INV-011 Supported disputed and other competing cause claims coexist.",
    "INV-012 A cause claim may reference a defect but can never be the defect.",
    "INV-013 WM-SFT-014 defect identity and lifecycle remain external and version pinned.",
    "INV-014 Containment restoration and permanent remediation are separate WM-ACT-006 tasks.",
    "INV-015 Restoration never proves cause elimination or permanent remediation completion.",
    "INV-016 Incident restore resolve close reopen or merge never closes deletes or mutates Problem Defect Task Claim or Communication.",
    "INV-017 Temporary restoration may permit incident closure under incident authority while Problem and permanent remediation remain open.",
    "INV-018 Problem closure requires its own authority and cannot be inferred from incident or task state.",
    "INV-019 Incident state Problem disposition Claim status Defect state and Task state remain independent.",
    "INV-020 Occurrence detection observation declaration restoration ingestion and recording clocks remain distinct.",
    "INV-021 Reopen supersession correction and merge preserve all declaration severity impact resolution review and correspondence history.",
    "INV-022 Correspondence relationship and role assignment do not prove identity execution completion or causation.",
    "INV-023 Unknown missing and stale evidence remain explicit and never mean absence.",
    "INV-024 Personal sensitive and regulated evidence is exposed only through governed projections.",
    "INV-025 No cascade delete crosses aggregate boundaries."
  ],
  "holds": [
    "WM-ACT-019 is a semantic rewrite of a legacy physical-emergency model and requires registry review before publication.",
    "WM-SFT-014 has a reservation but no live complete specification and remains reference-only.",
    "WM-KNW-014 Problem specialization and its incident relations require registry approval.",
    "WM-ACT-034 versus incident-child ImpactAssessment remains an explicit neighbor decision.",
    "Observation-plane identity and the physical/service/cyber/AI incident neighbor set remain unresolved.",
    "Canonical publication runtime search resolve and package verification are pending."
  ]
}
```

## Fixtures
```json
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-ACT-019",
  "version": "0.1.0-candidate.2",
  "cases": [
    {
      "id": "alarm-not-incident",
      "kind": "negative",
      "input": "A monitoring alert fires without an authorized declaration.",
      "expect": "Reject incident creation; retain the external observation or alert.",
      "expectRule": "INV-001"
    },
    {
      "id": "dual-master-cyber",
      "kind": "negative",
      "input": "One outage is entered as peer operational and cyber incident masters.",
      "expect": "Reject the second master; retain one declaration identity and a cyber qualification or correspondence record.",
      "expectRule": "INV-002"
    },
    {
      "id": "cyber-record-no-correspondence",
      "kind": "negative",
      "input": "A separate cyber record claims the same occurrence without correspondence evidence.",
      "expect": "Reject the record as an ungoverned duplicate.",
      "expectRule": "INV-004"
    },
    {
      "id": "three-incidents-one-problem",
      "kind": "positive",
      "input": "Three declarations reference one persistent Problem.",
      "expect": "All incident identities and the Problem identity remain distinct.",
      "expectRule": "INV-005"
    },
    {
      "id": "temporary-restoration",
      "kind": "positive",
      "input": "Rollback restores service while a suspected defect and permanent-fix task remain open.",
      "expect": "Incident may restore or close under its own authority; Problem, Defect and permanent task remain open.",
      "expectRule": "INV-017"
    },
    {
      "id": "close-no-cascade",
      "kind": "negative",
      "input": "Incident closure attempts to close its Problem and all tasks.",
      "expect": "Reject every cross-aggregate cascade.",
      "expectRule": "INV-016"
    },
    {
      "id": "restore-closes-problem",
      "kind": "negative",
      "input": "A restoration task completes and the Problem is auto-closed.",
      "expect": "Reject Problem closure without its own authority.",
      "expectRule": "INV-018"
    },
    {
      "id": "claim-without-evidence",
      "kind": "negative",
      "input": "A RootCauseClaim is asserted without evidence or confidence.",
      "expect": "Reject the incomplete claim.",
      "expectRule": "INV-010"
    },
    {
      "id": "competing-claims",
      "kind": "positive",
      "input": "One supported claim and one disputed claim address the same Problem.",
      "expect": "Retain both addressable claims with separate evidence confidence and status.",
      "expectRule": "INV-011"
    },
    {
      "id": "claim-overwrite",
      "kind": "negative",
      "input": "A supported claim overwrites a prior disputed claim.",
      "expect": "Reject overwrite and append the new claim or status transition.",
      "expectRule": "INV-011"
    },
    {
      "id": "claim-is-defect",
      "kind": "negative",
      "input": "A cause claim is assigned the defect identifier.",
      "expect": "Reject identity collapse and retain a version-pinned defect reference.",
      "expectRule": "INV-012"
    },
    {
      "id": "severity-regrade",
      "kind": "positive",
      "input": "Severity changes after new impact evidence.",
      "expect": "Append a superseding assessment and preserve the prior one.",
      "expectRule": "INV-006"
    },
    {
      "id": "priority-from-severity",
      "kind": "negative",
      "input": "Task priority is silently set from incident severity.",
      "expect": "Reject the derived priority without its own assertion.",
      "expectRule": "INV-007"
    },
    {
      "id": "potential-to-actual-impact",
      "kind": "positive",
      "input": "Potential customer impact is later verified as actual.",
      "expect": "Retain separate revisioned ImpactAssessment records.",
      "expectRule": "INV-008"
    },
    {
      "id": "impact-rollup",
      "kind": "negative",
      "input": "Problem impact is computed as authoritative from incident children without a rule.",
      "expect": "Reject implicit roll-up.",
      "expectRule": "INV-009"
    },
    {
      "id": "unfinished-remediation",
      "kind": "positive",
      "input": "Incident is closed after recovery while permanent remediation remains unfinished.",
      "expect": "Keep remediation Task and Problem open and preserve the closure evidence.",
      "expectRule": "INV-017"
    },
    {
      "id": "reopen-preserves-history",
      "kind": "positive",
      "input": "A closed incident recurs and is reopened.",
      "expect": "Append transition and preserve all earlier impact resolution and review records.",
      "expectRule": "INV-021"
    },
    {
      "id": "clock-collapse",
      "kind": "negative",
      "input": "Detection observation and declaration are stored as one timestamp.",
      "expect": "Reject loss of clock semantics.",
      "expectRule": "INV-020"
    },
    {
      "id": "missing-observation-source",
      "kind": "negative",
      "input": "A stale source is absent from a coverage window.",
      "expect": "Report unknown or incomplete coverage rather than no event.",
      "expectRule": "INV-023"
    }
  ]
}
```

## Claude study
## Verdict

EM-TEC-05 resolves as **reuse + profile, no new subject model**. Disposition per candidate type:

| Contour candidate | Disposition | Carrier |
|---|---|---|
| Incident (cyber) | **reuse** as-is | WM-ACT-020 |
| Incident (operational/service) | **profile**, requires spec rewrite | WM-ACT-019 |
| Problem | **profile** of a reserved candidate | WM-KNW-014 |
| Defect | **profile** of a reserved candidate | WM-SFT-014 |
| ResponseAction | **do not mint**; fold into task + response case | WM-ACT-006 (+ the response-case neighbour WM-ACT-020 already references) |
| ImpactAssessment | **identity yes, mastership incident-local** | inside the incident aggregate |
| RootCauseClaim | **independent identity required**, mastered by the problem | inside WM-KNW-014, referenced by incidents |

No new registry identifier is proposed, and none is invented here.

## Evidence

Asymmetric evidence depth, and it drives the verdict. WM-ACT-020 carries a structured 0.3.0-research.1 document (7 bundles, 16 layers, 32 findings, 10 functions) grounded in seven tier-1/2 sources, with `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, `providerMode: single-provider-waiver`, and five open publication holds. WM-ACT-019 has only the legacy X3 markdown (6244 bytes, sha256 `13057f1b…`), version 0.2.0, built on OASIS-CAP and ISO 22320 — i.e. physical harm and emergency response, not service degradation. WM-KNW-014, WM-SFT-014 and WM-ACT-006 have **no specification at all** (`missing_specs`). Both vercy_candidates are `conceptual-candidate` at `index-and-publication-metadata` depth with an explicit crosswalk caveat. Two ledger defects are visible: the `WM-ACT-020 COMPOSE WM-ACT-042` edge contradicts the incident/response separation the same draft asserts (the draft already rejects it in favour of REFERENCE), and both WM-KNW-014 and WM-SFT-014 declare `parent_ids: WM-ACT-021`, a model absent from the dossier.

## Identity/mastership

Four distinct mastered identities: **operational incident** (service-desk/ITSM record), **cyber incident** (CSIRT/case master), **problem** (problem-management record), **defect** (issue tracker). Observation and event mastership sits in observability/SIEM and is referenced, never copied — WM-ACT-020's `event-membership` finding is the correct pattern: incident-local membership assertions over externally mastered events. The contour's `candidate_master_systems` (software catalogue, Git, CI/CD, CMDB, observability) covers detection and defect but names **no incident or problem master system**; that gap must be closed before any mastership claim.

WM-ACT-019 and WM-ACT-020 stay separate models, not one with a `domain` discriminator: their authorities, disclosure regimes (GDPR/NIS2 vs public alerting under CAP), and closure vocabularies differ. WM-AI-010 already REFERENCEs WM-ACT-019 as the general incident context, so any re-scoping of X3 is a downstream-breaking change and needs a migration map.

## Event/incident/cyber boundary

Three gates, each testable:

1. **Observation → event**: an observation has an observer, a subject reference and an observation time. No declaration, no severity, no owner obligation.
2. **Event → incident**: requires a *declaration decision* — authority, pinned definition binding, rationale, confidence, effective time. WM-ACT-020's `incident-definition-binding` + `qualification-and-declaration-decision` are the reusable shape and should be lifted into the WM-ACT-019 profile verbatim in structure. Alert volume alone never promotes.
3. **Incident → cyber incident**: qualification against a security definition asserting compromise of confidentiality, integrity, availability or authenticity, or a policy/law effect. Dual-qualified occurrences (a ransomware outage) produce **two records, one occurrence**, linked by a typed correlation edge with a stated primary authority — not a merge.

Near-miss and false-positive are qualification *outcomes*, not incident states.

## Problem/defect/task

**Problem** (WM-KNW-014) is the persistent underlying condition: independent identity, independent lifecycle, many-to-many with incidents (one problem can explain three incidents; one incident can implicate two problems). It outlives every incident it explains. **Defect** (WM-SFT-014) is a specific software fault in a versioned artifact, resolved by a software change (its existing REFERENCE to WM-SFT-013). A defect may *be* the cause a problem asserts, but is not the problem: a problem may have a process or configuration cause with no defect. **Task** (WM-ACT-006) carries all work — triage, containment, temporary restoration, permanent remediation — and owns `priority`, assignment and completion. Restoration tasks attach to the incident; permanent remediation tasks attach to the problem. WM-ACT-006's existing edges (project CONTAINS task, work order CONTAINS task, task REFERENCE plan) are sufficient; no ResponseAction type is needed.

## Impact and root cause

**ImpactAssessment** needs record identity but not independent mastership: it is an incident-scoped, revisioned, assessor-attributed assertion (domain, actual vs potential, quantity, method, effective time) — exactly WM-ACT-020's impact findings and legacy X3's `impactRecord`. It cannot float free of its incident.

**RootCauseClaim** needs **independent identity**, for four reasons: its subject may be a problem *or* an incident; competing claims must coexist without one overwriting another; it has its own status lifecycle (`proposed | supported | disputed | superseded | rejected`) driven by evidence, not by incident state; and it must survive incident closure. Master it in the problem record; incidents hold typed references. Note the overlap to reconcile: WM-ACT-020 already owns `cause-and-enabling-condition-hypotheses` incident-locally. Rule — incident-local hypotheses are permitted while no problem exists; once a problem is opened, the claim is promoted to the problem and the incident retains a reference.

## Lifecycle

Incident: `reported → declared → (contained) → restored → closed`. Problem: `open → cause-claimed → remediation-planned → remediated → closed`. Task: its own state, with `priority` never derived from `severity`. `restored_at` marks service restoration only. Problem closure requires (a) at least one cause claim at `supported`, and (b) all remediation tasks terminal. Neither condition is satisfied by incident closure.

## Scenario

Incidents A, B, C, three separate declarations and three severity assessments, each linked to one problem. A is restored by a temporary workaround: A reaches `restored`, then `closed`; the problem stays `cause-claimed`. Two cause claims compete on the problem — one `supported`, one `disputed` — both retained with evidence and confidence; neither is promoted to fact. The permanent remediation task remains open, referencing a defect. All three incidents close; the problem does not. The negative case (`closing incident deletes unfinished root-cause fix`) fails by construction: closure writes no cascade to problem, claim, or task.

## Invariants

1. Every cause claim carries ≥1 evidence reference and an explicit confidence; source-free causation is rejected.
2. Competing claims coexist; supersession is recorded, never overwritten.
3. Incident closure never closes a problem, cancels a task, or retracts a claim.
4. Problem closure requires a supported claim plus terminal remediation tasks.
5. Severity (incident-owned, scheme + version + assessor) and priority (task-owned) are independent fields; mappings are documented, not enforced.
6. Restoration and cause elimination are separate assertions with separate timestamps.
7. Incident status requires a declaration decision naming authority and definition.
8. Observations and events are referenced, never mastered inside an incident.

## Minimal completion shape

WM-ACT-019 profile: identity, definition binding, declaration decision, `detected_at`/`declared_at`/`restored_at`/`closed_at`, severity assessment, impact assessments, affected-scope references, factual state, problem reference, task references. WM-KNW-014: identity, statement, incident membership set, cause-claim set, remediation-task references, closure decision with evidence. WM-SFT-014: identity, affected artifact version, change reference, state. WM-ACT-006: identity, priority, assignee, subject reference, state. Elevate the four v1 TEC-09 fields (`severity`, `detected_at`, `restored_at`, `impact`) from `candidate-not-normative` only after `impact` is split into typed assessments — a free-text `impact` cannot carry assessor or actual-vs-potential status.

## Holds

No canonical completeness and no installability is claimed. Blocking: pin the event/observation and evidence models by identifier; name the incident and problem master systems; reconcile the `COMPOSE → REFERENCE` ledger edge; resolve the unpinned `WM-ACT-021` parent shared by WM-KNW-014 and WM-SFT-014; author specs for the three reserved candidates; rewrite WM-ACT-019 from 0.2.0 with a WM-AI-010 migration map; obtain independent review for WM-ACT-020, whose external review is currently waived; complete semantic crosswalks — publication status is not evidence of boundary adjudication.


## Grok study
**EM-TEC-05 independent boundary review**  

Scope: the proposed split only. Catalogue facts used as evidence of current shape, not as a completed crosswalk. No new identifiers. No completeness claim. All named models are legacy or reviewable-draft.



**Verdict**  

Conditional accept with holds. Keep observation/event, incident declaration, cyber qualification, problem, defect and task as distinct roles. Reuse WM-ACT-020 for cyber incidents. Treat rewritten WM-ACT-019 as an extend/rewrite of a physical-emergency legacy model, not a thin profile. Profile reserved WM-KNW-014 for persistent Problem. Hold versioned Defect as a reserved reference toward EM-TEC-08; do not remaster it here. Reuse WM-ACT-006 for response and remediation work. Keep ImpactAssessment as a revisioned incident child. Give RootCauseClaim independent *record* identity inside Problem, with evidence/confidence/status, without a new model ID.  

Reject two peer incident masters for one occurrence. Reject collapsing operational and cyber determination into one undifferentiated type.



**Identity / mastership**  

Each declared incident, problem, defect and task keeps its own master-system identifier and lifecycle. Observation/event records are not incidents. A Problem may reference many incidents; it does not inherit their identity. A claim is addressable under the Problem root (issue identifier + claim/artifact sub-namespace + ordinal), not as a federated master and not as a silent field overwrite.  

WM-KNW-014 already ranks master-system ID first, then governed IRI, then minted UUIDv7; fingerprints are matching aids only. That priority should apply to Problem and to claim children. Correspondence across ops incident, cyber record, problem and defect is REFERENCE with representation role (originating / master / mirror). Relationship does not prove identity. Projection does not create a second master.  

WM-ACT-019 today is `world.x3-incident-and-emergency` 0.2.0-legacy, not installable, physical-harm/emergency (ISO 22320 / CAP), extending occurrence X1. Calling that a “profile” understates the rewrite. WM-ACT-020 is 0.3.0-research.1, installable, reviewable-draft. WM-ACT-006 is live 0.3.0-research.1 and can carry work via `based_on` / `focus_ref` without owning incident or problem state. WM-SFT-014 was not retrievable as a live spec; reserved ID only.



**Event / incident / cyber boundary**  

Observation or event is a detected occurrence or alert. Incident is a competent declaration that an unwanted interruption or compromise has been determined. Cyber qualification is a further determination that protected digital systems, information or computer-controlled infrastructure are actually or imminently compromised. Those three acts must not share one record type or one close action.  

WM-ACT-020 already separates constituent events from incident determination and excludes problem management and response execution. Rewritten WM-ACT-019 must do the same for operational/service interruption. Regulatory clocks, evidence custody, attribution and disclosure markings belong on the cyber qualification, not on a generic outage.  

Operational and cyber incidents should stay separate *as qualifications*, not as two peer masters of one occurrence. Dual declaration of the same event on rewritten WM-ACT-019 and WM-ACT-020 is the failure mode. Preferred rule: one declaration identity per determined incident; cyber may specialize a prior ops declaration onto WM-ACT-020 without minting a second incident identity, or originate on WM-ACT-020 when SOC detection is first. If both records exist, same-occurrence correspondence is mandatory. WM-AI-010 is another specialized sibling and needs the same rule, or it becomes a third master. Over-merge into one incident type would bury reporting duty and custody. Dual-master would split impact, close and legal hold.



**Problem / defect / task**  

Problem (WM-KNW-014 profile) is the persistent discrepancy and known-error knowledge: observed vs expected, recurrence, workaround knowledge, causal analysis, disposition. It references incidents; it does not run them. WM-KNW-014 already excludes incident operations and work execution and holds only a candidate REFERENCE to WM-ACT-021. That exclusion must survive the profile.  

Defect is a version-pinned product nonconformity. It belongs with EM-TEC-08 / reserved WM-SFT-014, not as an EM-TEC-05 owned type. A supported cause claim may *point at* a defect; it must not *be* the defect.  

Task (WM-ACT-006) is the assignable unit for containment, temporary restore and permanent remediation. ResponseAction on this card should be retired in favor of Task, with Work Order (WM-ACT-007) or Case (WM-ACT-021) only where authorization or requester coordination is required. Task state is not incident state and not problem disposition.



**Impact / root cause**  

ImpactAssessment stays an identified, revisioned child of the incident that owns the impact assertion. Three incidents can carry three impact revisions. Problem impact is not an automatic rollup. WM-ACT-034 exists; reuse vs incident-child remains an open neighbor, not a new ID.  

RootCauseClaim belongs *inside* Problem. Independent record identity does not require a new model ID if Problem is the aggregate root and claims are namespaced children. Current WM-KNW-014 causal-analysis-report is a serial investigation artifact plus inline `root_cause` / `causal_conclusion_status` / `contested_claim`. That shape fails competing supported vs disputed claims if treated as successive revisions of one report. The required extension is first-class claim children: asserted / supported / disputed / withdrawn / endorsed, each with evidence refs, confidence, status, incident refs, optional defect ref. Do not reinvent support semantics; align to existing evidence/rationale practice. A claim may reference incidents; closing an incident must not retract the claim. If a later wave needs one claim as shared master across Problems *and* Defects, that is a correspondence hold, not a model ID now.



**Lifecycle**  

Clocks stay distinct: occurrence, detection, observation, declaration, restore, ingestion. Incident factual state ≠ task state ≠ problem disposition ≠ claim status ≠ defect state. Temporary restore may close a containment task and may allow an incident to close on service recovery; it must not close the Problem, endorse a claim, or complete permanent remediation. Known-error / workaround *knowledge* may sit on Problem; execution sits on Task. Reopen, supersession and merge preserve child ImpactAssessment revisions, claims and outbound work refs. Cascade delete across aggregates is forbidden.



**Scenario**  

Three incidents against one service: I1 operational declaration from monitoring; I2 recurrence after partial restore; I3 later cyber-qualified (same occurrence correspondence, no second master). Events that were not declared remain events. Temporary restore Task T-restore completes; I1 may close. One Problem P references I1–I3. Claim C-supported (config drift / versioned defect ref) and claim C-disputed (capacity) remain simultaneously live with evidence and confidence. Permanent-remediation Task T-fix stays unfinished.  

Required outcomes: P open; C-disputed still disputed; T-fix open; defect ref untouched; I1 close does not delete P, claims, ImpactAssessment revisions or T-fix. Mixed cyber+ops must not fork P. Severity and priority remain separately asserted on incident vs work.



**Invariants**  

1. Observation ≠ incident declaration ≠ cyber qualification ≠ problem ≠ defect ≠ task.  

2. A cause claim has evidence, confidence and status; competing claims coexist.  

3. Restore or incident close does not close Problem, claims, Defect or unfinished Task.  

4. Severity ≠ priority; incident state ≠ task state ≠ problem disposition.  

5. Closing or merging an incident cannot destroy child impact revisions, claims or referenced work.  

6. Same-occurrence correspondence never mints a second incident master.  

7. Relationship and role assignment do not prove identity or execution.  

8. Unknown is not null; schema, revision and state stay distinct.



**Blockers**  

WM-ACT-019 rewrite is a research obligation, not a profile overlay; semantic fit for service incidents is unproven. WM-SFT-014 has no live spec. Shared relation ledger is empty; WM-KNW-014 still points at an unnamed incident/occurrence model, not 019/020. WM-ACT-020 COMPOSE-vs-REFERENCE conflict with response neighbor must stay REFERENCE. WM-KNW-014 ITSM problem/known-error reading is a declared tier-4 gap; keep discrepancy as the primitive. Observation-plane identity (legacy X1 vs a live observation model) is unresolved. WM-ACT-034 vs incident-child ImpactAssessment is undecided. Fixtures and field-level crosswalk do not exist; the card is still queued. Physical emergency, service incident, cyber and AI-incident remain an open neighbor set. Publication-ready status is not reached.