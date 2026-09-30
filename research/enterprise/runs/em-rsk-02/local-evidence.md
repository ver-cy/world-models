# EM-RSK-02 local synthesis

## Disposition

- Define an Enterprise audit and assurance profile over WM-ECO-035, WM-ACT-033, WM-KNW-014, WM-KNW-007 and WM-ACT-006.
- WM-ECO-035 masters the engagement mandate, terms, intended users, independence, assurance level and issuance authority. WM-ACT-033 masters execution, observations, evidence appraisal and findings. Their overlapping root semantics must be adjudicated before publication; do not publish both as parallel audit roots.
- Create no model for AssuranceOpinion. It is a sealed engagement-scoped statement on the issued engagement version.
- Reuse WM-ACT-033 for AuditFinding, align its assertion shape to WM-KNW-007 and avoid a second finding identity.
- Profile WM-ACT-006 for CorrectiveAction. Keep management response separate.
- Retain **Procedure Definition** as an identifier-unassigned candidate because a reusable procedure library entry has identity and lifecycle beyond one engagement. A performed procedure remains an execution-local entry.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Mandate, execution occurrence, reusable procedure definition and performed test are separate. Criteria text and version remain with WM-KNW-012 or an external catalogue; an engagement holds a pinned binding. WM-KNW-014 owns the organizational issue lifecycle. WM-ACT-006 owns corrective work. Risk and control state remain outside the audit aggregate.

WM-ECO-035 and WM-ACT-033 currently both claim criteria binding, evidence appraisal, findings, conclusion and reporting. This is a dual-root conflict, not a stable layering contract. Publication requires either one consolidated aggregate or a normative split with exactly one owner for every overlapping fact.

## Evidence and sampling

Observation, evidence item and finding remain distinct. Evidence records acquisition provenance and integrity; a finding applies a decision rule to observations and evidence against pinned criteria.

For each objective, record the population definition, sampling frame, frame gaps, selection method and version, sample units and size, deviations, and any projection claim. A frame gap is an explicit limitation. Statistical confidence is never implied when the method and denominator do not support it.

## Finding, issue, risk and action

A finding is an engagement-time determination. An issue is an organization-owned discrepancy with its own lifecycle. A risk is a forward-looking estimate. A task is work. Links between them are explicit, attributed and do not merge identity.

Root cause is a claim with evidence and a conclusion status, including `undetermined`. A management response records acceptance, disagreement or another stated position. It is not corrective action.

## Opinion, closure and independence

An opinion is bounded by declared scope, period, exclusions, evidence limitations, assurance level, modification and use restrictions. It is not general compliance status and does not prove absence of error, fraud or nonconformity.

Closure sequence is finding, management response, corrective-action task, task completion, independent retest and finding closure decision. Task completion closes only the task. Finding closure requires evidence against stated closure criteria. Independence and competence are evidenced separately and remain engagement-scoped.

## Acceptance result

An audit covers Process A and Process B while excluding Site 3. Criteria are pinned at version 2.1. Process A has a frame of 412 from a population of 430, so 18 unreachable units are recorded as a limitation. Finding F-1 raises Issue I-7. CorrectiveAction CA-1 completes, but F-1 remains open until independent retest R-1 satisfies its closure criteria. The opinion states the exclusion and limitation and makes no claims about Site 3 or other processes.

## Required invariants

1. Mandate, execution, procedure definition and performed test remain distinct.
2. Criteria are version-pinned before a finding is issued.
3. Observation is not evidence appraisal; evidence is not a finding.
4. Finding, issue, risk and task never merge identity.
5. Conclusions never exceed assessed scope.
6. Exclusions and sampling-frame gaps are explicit.
7. Extrapolation is explicit or absent.
8. Management response is not corrective action.
9. Task completion never closes a finding.
10. Closure requires independent retest against stated criteria.
11. Root cause has a conclusion status, including undetermined.
12. Independence and competence are evidenced separately.
13. Opinion is not compliance status.
14. Issued reports, findings and opinions are append-only and superseded explicitly.
15. Event, execution, observation, issuance, response, completion, retest and ingestion times remain distinct.

## Holds

WM-ACT-033, WM-ECO-035 and WM-KNW-014 are non-canonical provider drafts. The WM-ACT-033/WM-ECO-035 dual-root conflict blocks boundary sign-off. WM-ECO-035 parentage under WM-ACT-036 and WM-KNW-014 parentage under WM-ACT-021 remain suspect. WM-ACT-034 overlap and the WM-XCT-027 split remain unadjudicated. Procedure Definition has no allocated identifier. Relation contracts, source pins, crosswalks and fixtures are incomplete. No installable release or assurance conclusion is claimed.


## Provider reconciliation

Grok conditionally accepts the boundary and confirms ProcedureDefinition as the only independent new identity. The dual-root conflict is resolved in this candidate by exclusive composition: WM-ECO-035 owns engagement/mandate/scope/exclusions/opinion; WM-ACT-033 owns commissioned execution/test/observation/evidence/finding. One execution belongs to one engagement and never out-scopes or outlives it. Opinion limitations enumerate every exclusion and frame gap. Closure requires a new independent retest; no task, response, action or opinion closes a finding.


## Provider reconciliation

Grok conditionally accepts the boundary and confirms ProcedureDefinition as the only independent new identity. The dual-root conflict is resolved in this candidate by exclusive composition: WM-ECO-035 owns engagement/mandate/scope/exclusions/opinion; WM-ACT-033 owns commissioned execution/test/observation/evidence/finding. One execution belongs to one engagement and never out-scopes or outlives it. Opinion limitations enumerate every exclusion and frame gap. Closure requires a new independent retest; no task, response, action or opinion closes a finding.

## Frozen-audit remediation

Exactly one Claude Opus high no-tools audit conditionally passed the decisions and found twenty-four contract defects. All were remediated without rerun in revision 3: single methodology master; criteria/method separation; version-only authorization with effective non-overlap; engagement-owned criteria binding and issued report; execution-owned sampling and response; retained record semantics; engagement-scoped opinion issuance identity and supersession; issuance-authority closure; successor-cell equivalence; evidence item/package/reference split; stable engagement-scoped finding identity; complete sampling fields and vocabularies; append-only artifacts; separate timestamps; WM-KNW-012 base; and forty-five stable-id fixtures including the end-to-end scenario. Allocation and publication remain held.
