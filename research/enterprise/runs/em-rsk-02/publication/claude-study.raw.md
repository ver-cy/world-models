# EM-RSK-02 — Audit, Review and Finding: independent review

## Verdict

Reuse two masters, profile three, add one, and refuse two of the five candidate types as models.

- **Audit** — reuse. Split across the two existing aggregates: **WM-ECO-035** masters the *engagement/mandate* (appointment, terms, intended users, independence, assurance level, report issuance authority); **WM-ACT-033** masters the *execution occurrence* (plan, fieldwork, observations, evidence appraisal, findings). No third audit model.
- **AuditProcedure** — split. The reusable **ProcedureDefinition** (test library, method step) has identity and lifecycle outside any engagement → **new, identifier-unassigned candidate**, referenced by the engagement. The **performed test** has no identity outside the engagement → inline execution-log entry plus observation in WM-ACT-033. Two names, two owners.
- **AuditFinding** — reuse WM-ACT-033. Engagement-owned, criteria/condition/cause/effect, determination, severity, recurrence key. Align its assertion shape to **WM-KNW-007** (scope, evidence binding, asserter, supersession); do not instantiate findings as Claim records, which would fork identity.
- **AssuranceOpinion** — refuse as a model. It is a sealed, engagement-level statement on WM-ECO-035, typed by assurance level and modification, with use restrictions. It has no lifecycle independent of the engagement version that issued it.
- **CorrectiveAction** — not in any of the three targets; all three explicitly exclude action execution. Profile **WM-ACT-006 Task** with a CAPA action-kind vocabulary (containment / correction / corrective / preventive) plus root-cause and verification references. Management response is *not* this: it is a responsible-party assertion, recorded on the finding.

No identifiers allocated. All dispositions are conditional on the duplication adjudication below.

## Evidence

WM-ACT-033 (0.3.0-research.1, aggregate, single-provider Claude, Grok waived, `publishableCanonical: false`) and WM-ECO-035 (0.3.0-research.1, aggregate, Codex-only, Claude and Grok waived) both root on "one engagement" and both claim criteria binding, evidence appraisal, findings, conclusion, reporting and follow-up. This is a **genuine two-master conflict, not a layering**, and it is the blocking decision for this contour. WM-ECO-035's boundary note concedes only that WM-ACT-033 "may be referenced". WM-ECO-035's registry parent **WM-ACT-036 (Research Study)** is recorded as semantically suspect and held; it cannot be used to derive containment.

WM-KNW-014 (aggregate, Claude-only, entry_kind reclassified entity→aggregate) masters the recognized discrepancy with a lifecycle that outlives engagements. Its declared parent WM-ACT-021 is unresolved and its relationship contract is empty.

Reserved-but-uncanonical neighbours: WM-ACT-034 (Assessment/Evaluation), WM-KNW-007 (Claim), WM-KNW-012 (Policy/Rule), WM-XCT-027 (Risk/Control, ownership split unresolved), WM-ACT-006 (Task, dual-provider).

## Identity/mastership

- Engagement identity and mandate: WM-ECO-035. Execution occurrence identity: WM-ACT-033, referencing the engagement — **or**, if the adjudication collapses them, one root with mandate as a bundle. Do not publish both as parallel roots.
- Criteria text and version: WM-KNW-012 / external catalogue. The engagement holds a **binding with a pinned version**, never the text.
- Issue/problem record: WM-KNW-014. Findings reference it; it is not created by finding construction.
- Corrective action record: WM-ACT-006 profile. Control state and effectiveness: WM-XCT-027 profile + control assessment (per EM-RSK-01), never authored by the audit.
- Assessment boundary: WM-ACT-034 and WM-ACT-033 overlap on criteria→evidence→determination→conclusion. Treat WM-ACT-034 as the generic criterion-referenced assessment record and WM-ACT-033 as the engagement specialization, or merge. Flagged, not resolved here.

## Engagement/audit/procedure

Four separable things, four homes: **mandate** (WM-ECO-035), **plan/program** (WM-ACT-033 planning bundle), **procedure definition** (new library candidate), **performed test** (WM-ACT-033 execution log + observation, with performer, start/end, method, result). A procedure that was planned and not performed is a plan deviation, not a null result.

## Sampling and evidence

Record, per objective: population definition, **sampling frame** (frame ≠ population; the gap is a limitation), selection method and its version, sample size and units, deviations found, and whether projection to the population is claimed. Observation, evidence item and finding stay three records: observation asserts no conformity; evidence carries custody and an acquisition digest; finding applies the decision rule. Evidence sufficiency is appraised (relevance, reliability, sufficiency) and its limitations propagate to the conclusion. WM-ACT-033 declares statistical sampling a gap; WM-ECO-035 supplies the population/frame/method/size/projection slots. Until one owner is fixed, sampling is recorded structurally and no statistical confidence is asserted.

## Finding/issue/risk

A **finding** is an engagement-time determination against a pinned criterion. An **issue** is an organization-owned discrepancy with its own lifecycle, closure criteria and recurrence. A **risk** is a forward-looking estimate. A **task** is work. None derives another automatically: a finding may raise an issue, an issue may seed a task, a finding may inform a risk estimate — each by explicit, attributed link. Root cause is a **claim** with its own basis, conclusion status and an explicit "undetermined" value distinguishable from an unfinished investigation; it is not a field set by the auditor's narrative.

## Opinion and scope

The opinion is bounded by declared scope, period, exclusions and evidence limitations, and carries assurance level, modification, emphasis and use restrictions. An unmodified opinion is not proof of absence of fraud, error or noncompliance, and is **not a compliance status**: general compliance is evidenced obligation fulfilment with its own denominator (per EM-LND-15) and is never inferred from an opinion. Agreed-upon factual findings are not an assurance conclusion.

## Corrective action and closure

Sequence: finding → management response (agree / disagree / accept) → corrective action (Task profile, owned by the responsible party) → action completion → **independent re-test** → closure decision. Task completion closes the task only. Finding closure requires evidenced satisfaction of stated closure criteria, verified by a party independent of the performer, with a recorded verification method, evidence and time. Promised action never closes a finding.

## Independence

Independence and competence are separately evidenced, engagement-scoped, declared before fieldwork and re-declared on change. An undeclared conflict discovered later invalidates reliance on affected findings until reviewed. The re-test verifier must not be the action performer; the closure approver must not be the responsible-party liaison. Approval is not independence.

## Time/version/scenario

Separate: condition/event time, procedure execution time, observation time, report issuance time, response time, action completion time, re-test time, record ingestion time. All RFC 3339 with seconds and explicit offset. Criteria versions are pinned at binding and frozen; issued reports and findings are append-only, corrected only by erratum, re-issue or withdrawal naming the superseded version.

## Acceptance scenario

Audit of Process A and Process B, Site 3 excluded. Criteria pinned at v2.1. Sampling: A — frame 412 of population 430 (18 unreachable, recorded as a frame limitation), sample 25; B — sample 15. Finding F-1 (major, Process A, criterion 4.2) raises Issue I-7. Response: agreed. CorrectiveAction CA-1 completes and closes as a task. Re-test R-1, by a verifier independent of CA-1's performer, samples 20 post-remediation items, finds zero deviations, and satisfies F-1's closure criteria; F-1 closes, I-7 closes on its own criteria. The opinion covers Processes A and B **excluding Site 3**, states the frame limitation, and asserts nothing about Site 3 or other processes. CA-1's completion alone would have closed nothing.

## Invariants

1. Mandate, execution, procedure definition and performed test remain distinct records.
2. Criteria are version-pinned at binding; findings exist only against bound criteria.
3. Observation asserts no determination; evidence is not a finding.
4. Finding, issue, risk and task are never mutually derived without an attributed link.
5. Conclusion scope ≤ assessed scope; exclusions are stated, never implied by silence.
6. Extrapolation to an unsampled population is explicit or absent.
7. Sampling frame gaps are recorded as limitations, not ignored.
8. Management response is not a corrective action.
9. Task completion never closes a finding; closure requires independent verification against stated criteria.
10. Root cause carries a conclusion status, including undetermined.
11. Independence and competence are separately evidenced and engagement-scoped.
12. An unmodified opinion is not a compliance status and proves no absence.
13. Issued findings, opinions and reports are append-only.
14. Event, activity, observation, response, verification and record times stay distinct.
15. Audits cite control effectiveness determinations; they do not master control state.

## Minimal model set

WM-ECO-035 (engagement/mandate/opinion profile) · WM-ACT-033 (execution/observation/evidence/finding profile) · WM-KNW-014 (issue master) · WM-ACT-006 (corrective-action profile) · WM-KNW-012 (criteria reference) · WM-XCT-027 + control assessment (reference) · WM-KNW-007 (claim alignment for determination and root cause) · new ProcedureDefinition candidate (identifier-unassigned).

## Holds

All three targets are non-canonical single-provider reviewable drafts with visible waivers (`publishableCanonical: false`). **The WM-ACT-033 / WM-ECO-035 dual-root conflict is unresolved and blocks boundary sign-off.** WM-ECO-035's WM-ACT-036 parent is semantically suspect; WM-KNW-014's WM-ACT-021 parent is unresolved; relationship contracts are empty across targets. WM-ACT-034 is a candidate and its overlap with WM-ACT-033 is unadjudicated; WM-XCT-027's ownership split is open; ProcedureDefinition and the CAPA profile lack identifiers. Statistical sampling, ISO audit vocabulary, sensitivity classification and cross-engagement finding identity remain declared gaps. Source pins, crosswalks and fixtures are unverified. This review is not legal advice and claims no canonical completeness, publication readiness or installability.
