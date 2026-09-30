# Frozen audit prompt — EM-RSK-02

Audit only the frozen material below. Use no tools and no outside knowledge. Do not invent identifiers or claim standards compliance.

Return a concise verdict and enumerate only material defects. Check independent identity, exclusive dual-root mastership, commission composition, procedure authorization/version pins, sampling frame/method/sample/cell, evidence and finding identity, opinion scope/limitations, corrective-action separation, retest independence, closure authority, immutability, correspondence-only profile and fixture traceability. For each defect give the smallest remediation. End with the exact additional fixtures required. This is the one frozen audit; do not request a second audit.

## LOCAL EVIDENCE
```
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

```
## PROVIDER COMPARISON
```
# EM-RSK-02 provider comparison

Claude and Grok agree that ProcedureDefinition is the only independently identified new-model candidate. A performed test is execution-local and pins one authorised procedure version plus criteria. They agree that AssuranceOpinion is engagement-scoped, CorrectiveAction profiles WM-ACT-006, management response is separate, and finding, issue, risk, control and task retain distinct identities.

The reconciled dual-root contract adopts Grok's exclusive composition: WM-ECO-035 alone masters Engagement, Mandate, declared scope, exclusions and AssuranceOpinion. WM-ACT-033 alone masters commissioned Execution, performed tests, observations, evidence packages and AuditFinding. Engagement commissions Execution; one Execution belongs to one Engagement and cannot exceed its scope or life. Shared wording is reference, never duplicate storage or identity.

Sampling is execution-local and explicit: population, frame, frame gaps, method, sample and sampling cell. Evidence is bound to one performed test and cell. Criteria are pinned before evaluation. Opinion range is limited to declared scope minus exclusions and frame gaps, and every limitation is stated. One-system evidence never proves group-wide conformity.

Finding closure requires a new independent retest against the same pinned criteria and cell, or an explicitly declared successor cell. Task completion, corrective-action completion, management response and opinion never close a finding. No identifier or runtime ID is allocated; publication remains held on registry allocation and canonical dual-root adjudication.

```
## ALLOCATION CANDIDATE
```json
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-RSK-02",
  "proposedName": "Procedure Definition",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A reusable assurance procedure remains identifiable across engagements, performers and individual executions while its approved method evolves through controlled revisions.",
    "versionIdentity": "Changes to objective, prerequisites, steps, evidence requirements, sampling method or decision rule create immutable procedure versions; materially different assurance objectives create separate procedures.",
    "independentLifecycle": [
      "draft",
      "reviewed",
      "approved",
      "effective",
      "suspended",
      "superseded",
      "retired"
    ],
    "mastership": "audit methodology or assurance procedure authority"
  },
  "boundary": {
    "owns": [
      "persistent reusable procedure-definition identity",
      "assurance objective and applicability",
      "prerequisites and ordered method steps",
      "required evidence and integrity expectations",
      "population and sampling method specification",
      "decision rule and result vocabulary",
      "competence and independence requirements",
      "approval, versioning, supersession and retirement history",
      "closed sampling-method vocabulary and frame-gap representation",
      "procedure-version authorization bindings",
      "closed sampling-method vocabulary and frame-gap representation",
      "procedure-version authorization bindings"
    ],
    "references": [
      {
        "target": "WM-ECO-035",
        "purpose": "Assurance engagement mandate and intended use"
      },
      {
        "target": "WM-ACT-033",
        "purpose": "Performed execution, observation, appraisal and finding"
      },
      {
        "target": "WM-KNW-012",
        "purpose": "Pinned criteria or governing method expression"
      },
      {
        "target": "WM-KNW-007",
        "purpose": "Claim and finding assertion shape"
      },
      {
        "target": "WM-KNW-014",
        "purpose": "Organization-owned issue lifecycle"
      },
      {
        "target": "WM-ACT-006",
        "purpose": "Corrective work lifecycle"
      }
    ],
    "excludes": [
      "engagement mandate, assurance level or issuance authority",
      "performed procedure or execution occurrence",
      "observation, evidence item, appraisal or finding identity",
      "organizational issue, risk or control state",
      "management response or corrective-action task",
      "assurance opinion or general compliance status",
      "sampling frame, method, sample or cell for a performed test",
      "finding closure or opinion limitation state",
      "sampling frame, method, sample or cell for a performed test",
      "finding closure or opinion limitation state"
    ]
  },
  "objects": {
    "ProcedureDefinition": {
      "identity": [
        "procedureDefinitionId"
      ],
      "required": [
        "name",
        "objective",
        "ownerRef",
        "status"
      ],
      "optional": [
        "successorRef",
        "retiredAt"
      ],
      "lifecycle": [
        "draft",
        "reviewed",
        "approved",
        "effective",
        "suspended",
        "superseded",
        "retired"
      ]
    },
    "ProcedureVersion": {
      "identity": [
        "procedureDefinitionId",
        "version"
      ],
      "required": [
        "steps",
        "evidenceRequirements",
        "decisionRule",
        "validFrom",
        "contentDigest",
        "status"
      ],
      "optional": [
        "validTo",
        "applicability",
        "prerequisites",
        "samplingMethod",
        "competenceRequirements",
        "independenceRequirements",
        "criteriaRef",
        "supersedesVersion"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "effective",
        "superseded",
        "withdrawn"
      ]
    }
  },
  "holds": [
    "Registry namespace and identifier allocation are pending and no identifier may be guessed.",
    "Independent Grok review and one frozen semantic audit are pending.",
    "WM-ACT-033 and WM-ECO-035 dual-root ownership must be normatively resolved before publication.",
    "Criteria, evidence and sampling relation contracts require canonical reconciliation.",
    "Package conversion and live verification are pending."
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-single-frozen-audit",
  "publishable": false,
  "invariantRules": [
    {
      "id": "I01",
      "rule": "ProcedureDefinition and performed test never share identity; performed test is WM-ACT-033 execution-local."
    },
    {
      "id": "I02",
      "rule": "Every performed test pins one authorised immutable procedure version and pinned criteria before evaluation."
    },
    {
      "id": "I03",
      "rule": "Method, evidence, sampling or decision-rule change creates an immutable successor ProcedureVersion."
    },
    {
      "id": "I04",
      "rule": "ProcedureDefinition owns no engagement, execution, finding, opinion, response, action or closure identity."
    },
    {
      "id": "I05",
      "rule": "Population, frame, gaps, method, sample units and sampling cell are explicit on every performed test."
    },
    {
      "id": "I06",
      "rule": "Evidence is bound to one performed test and sampling cell; observation alone is neither evidence nor finding."
    },
    {
      "id": "I07",
      "rule": "Finding requires pinned criteria, cell-bound evidence and evaluation."
    },
    {
      "id": "I08",
      "rule": "One-system or one-site evidence never extrapolates across an exclusion or frame gap."
    },
    {
      "id": "I09",
      "rule": "Competence and independence requirements are separate and evidenced per engagement and execution."
    },
    {
      "id": "I10",
      "rule": "Procedure completion, task completion, corrective action, management response and opinion never close a finding."
    },
    {
      "id": "I11",
      "rule": "Retired and superseded versions remain immutable and resolvable for issued work."
    },
    {
      "id": "I12",
      "rule": "A reusable definition is catalog-owned and is never cloned into an engagement or execution."
    }
  ]
}
```
## PROFILE CANDIDATE
```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-RSK-02",
  "name": "Enterprise Audit and Assurance",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ECO-035",
    "WM-ACT-033",
    "WM-KNW-014",
    "WM-KNW-007",
    "WM-ACT-006"
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-single-frozen-audit",
  "publishable": false,
  "profileRole": "exclusive composition and correspondence-only seam",
  "basePlaceholders": [
    {
      "name": "Procedure Definition",
      "modelId": null,
      "registryId": null,
      "allocationState": "unassigned",
      "required": true
    }
  ],
  "instantiable": false,
  "constraintRules": [
    {
      "id": "P01",
      "rule": "WM-ECO-035 exclusively masters Engagement, Mandate, declared scope, exclusions and AssuranceOpinion."
    },
    {
      "id": "P02",
      "rule": "WM-ACT-033 exclusively masters commissioned Execution, performed test, observation, evidence package and AuditFinding."
    },
    {
      "id": "P03",
      "rule": "Engagement commissions Execution; one Execution belongs to one Engagement and cannot out-scope or outlive it."
    },
    {
      "id": "P04",
      "rule": "No merged Audit root, third Audit master or same-instance dual mastership is permitted."
    },
    {
      "id": "P05",
      "rule": "AuditFinding reuses WM-ACT-033 and aligns to WM-KNW-007 without a second identity; WM-KNW-014 Issue remains distinct."
    },
    {
      "id": "P06",
      "rule": "AssuranceOpinion is engagement-scoped, lists all exclusions and frame gaps, and never proves general compliance or closes a finding."
    },
    {
      "id": "P07",
      "rule": "CorrectiveAction profiles WM-ACT-006; management response is a separate assertion attached to the finding."
    },
    {
      "id": "P08",
      "rule": "Finding, issue, risk, control, task, opinion, response and action retain distinct identities and attributed links."
    },
    {
      "id": "P09",
      "rule": "Closure requires a new independent performed test against the same pinned criteria and cell or declared successor cell."
    },
    {
      "id": "P10",
      "rule": "Retest executor differs from corrective-action actor; performed-test executor differs from process owner; opinion issuer is independent of audited management."
    },
    {
      "id": "P11",
      "rule": "Original performed tests, evidence, findings and issued opinions are immutable; changes append successors or withdrawals."
    },
    {
      "id": "P12",
      "rule": "The profile mints no subject identity and cannot mutate or cascade-delete any master."
    }
  ]
}
```
## FIXTURES
```json
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Procedure Definition",
  "cases": [
    {
      "id": "version-pinned-execution",
      "kind": "positive",
      "covers": [
        "I01",
        "I02",
        "I03"
      ],
      "input": "An engagement performs Procedure v2.1 and the method later changes.",
      "expect": "Execution remains pinned to v2.1; successor governs future work."
    },
    {
      "id": "sampling-frame-gap",
      "kind": "positive",
      "covers": [
        "I05",
        "I08"
      ],
      "input": "Population 430, frame 412.",
      "expect": "18 unreachable units are a limitation; no unsupported extrapolation."
    },
    {
      "id": "independent-retest",
      "kind": "positive",
      "covers": [
        "I10",
        "P09",
        "P10"
      ],
      "input": "Action completes and an independent retest satisfies the same criteria and cell.",
      "expect": "Task closes first; finding closes only after retest decision."
    },
    {
      "id": "two-process-one-excluded-site",
      "kind": "positive",
      "covers": [
        "P01",
        "P02",
        "P03",
        "P06"
      ],
      "input": "Engagement covers A and B at Site Y, excludes Site X, and tests A/Y only.",
      "expect": "Opinion is limited to tested A/Y and lists X exclusion plus B frame gap."
    },
    {
      "id": "performed-test-new-definition",
      "kind": "negative",
      "covers": [
        "I01",
        "I12"
      ],
      "input": "Every test mints a reusable definition.",
      "expect": "Rejected as duplicate identity."
    },
    {
      "id": "task-closes-finding",
      "kind": "negative",
      "covers": [
        "I10",
        "P09"
      ],
      "input": "Task completion closes the finding.",
      "expect": "Rejected without independent retest."
    },
    {
      "id": "opinion-general-compliance",
      "kind": "negative",
      "covers": [
        "I08",
        "P06"
      ],
      "input": "Scoped opinion becomes group-wide compliance.",
      "expect": "Rejected."
    },
    {
      "id": "management-response-is-action",
      "kind": "negative",
      "covers": [
        "P07",
        "P08"
      ],
      "input": "Management acceptance is corrective action.",
      "expect": "Rejected."
    },
    {
      "id": "same-actor-retest",
      "kind": "negative",
      "covers": [
        "P09",
        "P10"
      ],
      "input": "Corrective-action actor performs closure retest.",
      "expect": "Rejected as non-independent."
    },
    {
      "id": "execution-outscopes-engagement",
      "kind": "negative",
      "covers": [
        "P03"
      ],
      "input": "Execution adds excluded Site X.",
      "expect": "Rejected."
    },
    {
      "id": "missing-sampling-cell",
      "kind": "negative",
      "covers": [
        "I05",
        "I06"
      ],
      "input": "Evidence lacks process-site-unit cell.",
      "expect": "Rejected; evidence cannot support a finding."
    },
    {
      "id": "observation-is-finding",
      "kind": "negative",
      "covers": [
        "I06",
        "I07"
      ],
      "input": "Observation automatically creates finding.",
      "expect": "Rejected; criteria, evidence and evaluation required."
    },
    {
      "id": "finding-issue-identity-merge",
      "kind": "negative",
      "covers": [
        "P05",
        "P08"
      ],
      "input": "Finding key is reused as Issue identity.",
      "expect": "Rejected."
    },
    {
      "id": "criteria-changed-on-retest",
      "kind": "negative",
      "covers": [
        "P09"
      ],
      "input": "Retest changes criteria and closes original finding.",
      "expect": "Rejected unless successor cell/criteria creates a new adjudicated path."
    },
    {
      "id": "opinion-omits-gap",
      "kind": "negative",
      "covers": [
        "P06"
      ],
      "input": "Opinion omits excluded site or frame gap.",
      "expect": "Rejected."
    },
    {
      "id": "profile-cascade-delete",
      "kind": "negative",
      "covers": [
        "P12"
      ],
      "input": "Deleting binding deletes finding or engagement.",
      "expect": "Rejected."
    }
  ]
}
```
