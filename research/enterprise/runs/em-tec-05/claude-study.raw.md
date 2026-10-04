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
