# Frozen semantic audit: EM-PEO-04 Recruitment and Hiring

You are the single independent frozen auditor. Use only the JSON below and no tools. Do not invent identifiers or external facts.

Return:
1. Verdict ACCEPT or REVISE.
2. Confirm or reject the complete minimum model set and the decision to allocate no new identifier now.
3. List every defect that could collapse approved need, requisition, position, derived vacancy, asserted opening, posting, person, candidacy, campaign, stage, interview, assessment, recommendation, decision, offer, contract, assignment or employment; lose history; exceed seat authority; breach privacy or fairness; or overclaim validation/publication.
4. Give exact remediation and one fixture expectation for every defect.
5. Identify contradictions.
6. End with a closed numbered remediation checklist.

## FROZEN RECONCILED DOSSIER
```json
{
  "contourId": "EM-PEO-04",
  "candidateRevision": 2,
  "recruitmentRequisition": {
    "format": "vercy-model-allocation-candidate/v1",
    "contourId": "EM-PEO-04",
    "proposedName": "Recruitment Requisition",
    "modelId": null,
    "registryId": null,
    "allocationState": "unassigned",
    "decision": "NEW MODEL",
    "canonicalPublishable": false,
    "identityTest": {
      "stableIdentity": "A standing, authorized recruitment demand remains identifiable across zero or more openings, campaigns, postings, candidacies and fills while approved scope evolves.",
      "versionIdentity": "Changes to headcount, reason, position scope, budget, target start or authority create immutable requisition versions; a different hiring need creates a new requisition.",
      "independentLifecycle": [
        "draft",
        "submitted",
        "approved",
        "funded",
        "open",
        "partially-filled",
        "filled",
        "cancelled",
        "closed"
      ],
      "mastership": "employer workforce-demand authority"
    },
    "boundary": {
      "owns": [
        "persistent recruitment-requisition identity",
        "requested headcount and hiring reason",
        "position or role scope",
        "budget and authority references",
        "target start and priority",
        "approval and funding history",
        "opening and fill trace links",
        "partial-fill, cancellation and closure status",
        "effective interval and recorded-at provenance",
        "authorized-seat cap and attributable cap-change history"
      ],
      "references": [
        {
          "target": "WM-ORG-004",
          "purpose": "Position and authorized-capacity master"
        },
        {
          "target": "WM-ORG-008",
          "purpose": "Asserted Vacancy or Opening"
        },
        {
          "target": "WM-ACT-039",
          "purpose": "Recruitment campaign or process"
        },
        {
          "target": "WM-REC-010",
          "purpose": "Approval decision record"
        },
        {
          "target": "WM-ORG-005",
          "purpose": "Employment created downstream"
        }
      ],
      "excludes": [
        "position, opening, posting or person identity",
        "candidacy or recruitment-process identity",
        "interview, assessment or selection decision",
        "offer, contract, assignment or employment",
        "budget authority or accounting commitment",
        "derived vacant-capacity calculation",
        "approved-need decision identity",
        "stage definition or occurrence",
        "posting publication identity"
      ]
    },
    "objects": {
      "RecruitmentRequisition": {
        "identity": [
          "recruitmentRequisitionId"
        ],
        "required": [
          "employerRef",
          "requestedHeadcount",
          "reason",
          "ownerRef",
          "validFrom",
          "recordedAt",
          "status"
        ],
        "optional": [
          "positionRefs",
          "budgetRef",
          "authorityRef",
          "targetStart",
          "priority",
          "successorRef",
          "validTo",
          "approvalDecisionRefs",
          "openingRefs",
          "campaignRefs",
          "fillRefs"
        ],
        "lifecycle": [
          "draft",
          "submitted",
          "approved",
          "funded",
          "open",
          "partially-filled",
          "filled",
          "cancelled",
          "closed"
        ]
      }
    },
    "invariants": [
      "One requisition may authorize several openings and seats.",
      "Requisition identity remains separate from position, opening, posting and candidacy identity.",
      "Approval records an attributable act and never replaces the standing authorization.",
      "Requested headcount, reason, budget and target start are versioned.",
      "Derived vacant capacity never creates an asserted opening automatically.",
      "Opening or posting closure never silently closes the requisition.",
      "Partial fill preserves remaining authorized headcount explicitly.",
      "Approval never creates an offer, contract, employment or assignment.",
      "Budget reference never substitutes for funding authority or commitment.",
      "Cancellation preserves prior versions, approvals, openings and fills.",
      "A later rehire uses a new requisition or justified remaining authorization without duplicating Person.",
      "Historical requisitions remain resolvable after closure.",
      "Approved need is an attributable decision record and never the requisition identity.",
      "A standing requisition may exist with zero asserted openings and zero campaigns.",
      "Asserted opening is not required for internal mobility or appointment paths.",
      "Non-cancelled fills plus outstanding accepted offers never exceed the authorized seat cap unless an attributable change raises it.",
      "One opening per distinguishable seat is preferred; quantity greater than one is allowed only for interchangeable seats.",
      "Valid time and recorded time are preserved separately; correction appends a successor rather than rewriting history."
    ],
    "holds": [
      "Registry allocation is pending and no identifier may be guessed.",
      "WM-ORG-008 completion and WM-ORG-016 reservation require canonical reconciliation.",
      "Jurisdictional workforce and fairness review remain pending.",
      "One frozen semantic audit is pending.",
      "Opening quantity versus seat-level identity requires canonical governance."
    ],
    "candidateRevision": 2
  },
  "candidacy": {
    "format": "vercy-model-allocation-candidate/v1",
    "contourId": "EM-PEO-04",
    "proposedName": "Candidacy",
    "modelId": null,
    "registryId": null,
    "allocationState": "unassigned",
    "decision": "NEW MODEL",
    "canonicalPublishable": false,
    "identityTest": {
      "stableIdentity": "One person's purpose-scoped participation in one hiring effort remains identifiable across stages, assessments, offers, withdrawal and outcome, including internal mobility without a public opening.",
      "versionIdentity": "Status, documents, declarations and stage outcomes append versions to the same candidacy; a later application creates a new candidacy linked to the same person.",
      "independentLifecycle": [
        "sourced",
        "submitted",
        "received",
        "screening",
        "assessing",
        "selected",
        "rejected",
        "withdrawn",
        "offered",
        "closed"
      ],
      "mastership": "employer applicant-tracking authority under stated privacy purpose"
    },
    "boundary": {
      "owns": [
        "persistent candidacy identity",
        "person, opening and recruitment-process references",
        "submission and receipt times",
        "supplied document and declaration bindings",
        "stage and status history",
        "withdrawal and outcome",
        "controller, purpose, lawful basis and notice version",
        "retention, legal-hold and disposition triggers",
        "application artifact binding without separate root identity",
        "valid and transaction time",
        "stage-occurrence history pinned to process release"
      ],
      "references": [
        {
          "target": "WM-PER-001",
          "purpose": "Person anchor"
        },
        {
          "target": "WM-ORG-008",
          "purpose": "Asserted opening"
        },
        {
          "target": "WM-ACT-039",
          "purpose": "Recruitment process and stage design"
        },
        {
          "target": "WM-ACT-025",
          "purpose": "Interview session"
        },
        {
          "target": "WM-ACT-034",
          "purpose": "Assessment result"
        },
        {
          "target": "WM-ECO-021",
          "purpose": "Employment offer"
        }
      ],
      "excludes": [
        "person, position, opening or requisition identity",
        "recruitment campaign or stage-definition identity",
        "interview or assessment-result identity",
        "selection decision or recommendation",
        "offer, contract, assignment or employment",
        "unlimited consent or indefinite talent-pool rights",
        "matching score as opening attribute",
        "person biography as candidacy-owned dossier"
      ]
    },
    "objects": {
      "Candidacy": {
        "identity": [
          "candidacyId"
        ],
        "required": [
          "personRef",
          "controllerRef",
          "purpose",
          "lawfulBasis",
          "validFrom",
          "recordedAt",
          "status"
        ],
        "optional": [
          "requisitionRef",
          "openingRef",
          "processRef",
          "campaignRef",
          "submittedAt",
          "receivedAt",
          "applicationArtifactRef",
          "documentRefs",
          "declarations",
          "noticeVersion",
          "retentionPolicyRef",
          "legalHoldRef",
          "validTo",
          "successorRef"
        ],
        "lifecycle": [
          "sourced",
          "submitted",
          "received",
          "screening",
          "assessing",
          "selected",
          "rejected",
          "withdrawn",
          "offered",
          "closed"
        ],
        "scopeRule": "At least one of requisitionRef, openingRef, processRef or campaignRef is required; openingRef is optional for internal mobility, succession and appointment paths."
      }
    },
    "invariants": [
      "One candidacy binds one person, one opening, one recruitment process and an interval.",
      "Candidate role never creates a second person identity.",
      "Name, email or birth date never justify automatic person merge.",
      "A later application creates a new candidacy while reusing the person anchor.",
      "Every stage occurrence pins the exact process-design release.",
      "Score, recommendation and decision remain distinct assertions.",
      "Interview session and assessment result retain separate identity and evidence.",
      "Offer acceptance never creates contract, employment or assignment automatically.",
      "CV possession never grants unlimited consent or indefinite retention.",
      "Purpose, controller, lawful basis, notice and rights route are explicit.",
      "Withdrawal and disposition never cascade to person or employment masters.",
      "Legal hold suspends disposition without changing candidacy outcome.",
      "At least one recruiting-effort scope reference exists, but an asserted opening is not mandatory.",
      "Application is an originating artifact of Candidacy and never a sibling root or Opening attribute.",
      "Matching is a purpose-qualified evaluation or process result, never an Opening attribute.",
      "At most one active candidacy exists for the same Person and Opening; no-opening paths use the declared effort scope instead.",
      "Candidacy closure or CV disposition never deletes Person, Decision or Employment records.",
      "Candidacy close, withdrawal or fill starts retention unless a recorded legal hold suspends disposition.",
      "Standing requisition does not authorize an indefinite talent pool.",
      "Rehire reuses Person, creates a new Candidacy and never resurrects a purged CV.",
      "Valid time and recorded time remain distinct and corrections are attributable successors."
    ],
    "holds": [
      "Registry allocation is pending and no identifier may be guessed.",
      "Privacy, retention, fairness and cross-company reuse require jurisdictional review.",
      "WM-ORG-008 and relation contracts require canonical completion.",
      "One frozen semantic audit is pending.",
      "No-opening internal-mobility uniqueness requires canonical governance."
    ],
    "candidateRevision": 2
  },
  "profile": {
    "format": "vercy-enterprise-profile-candidate/v1",
    "contourId": "EM-PEO-04",
    "name": "Enterprise Recruitment, Selection and Offer",
    "decision": "PROFILE",
    "newRuntimeId": false,
    "bases": [
      "WM-ORG-008",
      "WM-ACT-039",
      "WM-ACT-025",
      "WM-ACT-034",
      "WM-ECO-021",
      "WM-PER-001",
      "WM-ORG-004",
      "WM-ORG-005"
    ],
    "constraints": [
      "WM-ORG-008 is narrowed to asserted Vacancy or Opening and no longer owns applications, matching or placement.",
      "WM-ACT-039 owns the recruitment process, frozen stage definitions and per-candidacy stage occurrences.",
      "Interview Assessment separates WM-ACT-025 session evidence from WM-ACT-034 assessment results.",
      "Selection decision remains an authorized record distinct from score and recommendation.",
      "Employment Offer profiles immutable WM-ECO-021 versions; acceptance, contract, employment and assignment remain separate.",
      "Candidate is a purpose-scoped role over WM-PER-001 and never a second person identity.",
      "Approved need is a decision record; Recruitment Requisition is the standing authorization.",
      "Derived seat vacancy is a projection and never auto-creates an asserted Opening.",
      "Posting and Application are dependent artifacts, not allocated roots.",
      "Candidacy may support internal mobility without an asserted Opening when another recruiting-effort scope is explicit.",
      "Matching is a WM-ACT-034 or WM-ACT-039 result, never an Opening attribute.",
      "Stage occurrence belongs to Candidacy and pins the exact WM-ACT-039 design release.",
      "Offer acceptance does not create Contract, Employment or Assignment.",
      "Placement is downstream Employment plus Assignment and never a Vacancy state.",
      "CV retention is purpose-, controller-, basis- and schedule-bound, with explicit legal-hold handling.",
      "Fairness audit uses attributable decisions and assessment results without retaining unrestricted biographies."
    ],
    "candidateRevision": 2
  },
  "fixtures": {
    "requisition": [
      {
        "id": "two-seat-request",
        "kind": "positive",
        "input": "One approved requisition authorizes two seats and two openings.",
        "expect": "One authorization traces to two openings without merging their identities."
      },
      {
        "id": "partial-fill",
        "kind": "positive",
        "input": "One seat is filled while the second remains open.",
        "expect": "The requisition becomes partially filled and preserves the remaining count."
      },
      {
        "id": "cancel-after-opening",
        "kind": "positive",
        "input": "The employer cancels the remaining need after one fill.",
        "expect": "Cancellation preserves the filled employment and historical opening."
      },
      {
        "id": "derived-vacancy-is-opening",
        "kind": "negative",
        "input": "Calculated vacant capacity automatically creates an asserted opening.",
        "expect": "The transition is rejected."
      },
      {
        "id": "approval-is-employment",
        "kind": "negative",
        "input": "Approval of the requisition creates employment.",
        "expect": "The inference is rejected."
      },
      {
        "id": "posting-is-requisition",
        "kind": "negative",
        "input": "A public posting is used as the authorization master.",
        "expect": "The identity merge is rejected."
      },
      {
        "id": "standing-no-opening",
        "kind": "positive",
        "input": "An approved standing requisition has no current opening or campaign.",
        "expect": "The requisition remains valid without minting an opening."
      },
      {
        "id": "seat-cap-overrun",
        "kind": "negative",
        "input": "Two fills and one outstanding accepted offer are recorded against a two-seat authorization.",
        "expect": "The state is rejected unless an attributable cap increase exists."
      },
      {
        "id": "internal-mobility-no-opening",
        "kind": "positive",
        "input": "An internal appointment proceeds under a requisition and decision without a public opening.",
        "expect": "The path remains valid and does not mint an opening."
      },
      {
        "id": "approval-decision-not-root",
        "kind": "negative",
        "input": "A decision record is reused as the requisition identity.",
        "expect": "The identity collapse is rejected."
      },
      {
        "id": "recorded-time-correction",
        "kind": "positive",
        "input": "An authorized-headcount correction is recorded after its valid date.",
        "expect": "Valid and recorded time remain distinct and history is preserved."
      }
    ],
    "candidacy": [
      {
        "id": "three-candidates",
        "kind": "positive",
        "input": "Three people apply to two openings under one recruitment process.",
        "expect": "Three candidacies reference three person anchors without duplicating people."
      },
      {
        "id": "withdrawn-offer",
        "kind": "positive",
        "input": "An issued offer is withdrawn with authority and reason.",
        "expect": "The offer version and withdrawal remain immutable while candidacy outcome changes."
      },
      {
        "id": "later-rehire",
        "kind": "positive",
        "input": "A prior applicant applies again years later.",
        "expect": "A new candidacy reuses the person anchor and preserves lineage."
      },
      {
        "id": "email-merges-person",
        "kind": "negative",
        "input": "Two records sharing an email are automatically merged as one person.",
        "expect": "The merge is rejected without authorized evidence."
      },
      {
        "id": "score-is-decision",
        "kind": "negative",
        "input": "Highest assessment score automatically becomes the selection decision.",
        "expect": "The inference is rejected."
      },
      {
        "id": "cv-is-permanent-consent",
        "kind": "negative",
        "input": "Possession of a CV authorizes indefinite cross-company reuse.",
        "expect": "The use is rejected without a separate scoped basis."
      },
      {
        "id": "internal-mobility-scope",
        "kind": "positive",
        "input": "A person participates in an internal-mobility campaign without an asserted opening.",
        "expect": "A candidacy is valid with explicit campaign or process scope."
      },
      {
        "id": "application-is-artifact",
        "kind": "negative",
        "input": "An application is minted as a sibling root and owned by the opening.",
        "expect": "The identity and ownership collapse is rejected."
      },
      {
        "id": "matching-on-opening",
        "kind": "negative",
        "input": "A match score is stored as an opening property.",
        "expect": "The score is rejected unless represented as an attributable evaluation or process result."
      },
      {
        "id": "duplicate-active-candidacy",
        "kind": "negative",
        "input": "The same person has two active candidacies for the same opening.",
        "expect": "The duplicate active scope is rejected."
      },
      {
        "id": "purge-keeps-lineage",
        "kind": "positive",
        "input": "A closed candidacy reaches disposition while its hiring decision must be retained.",
        "expect": "CV material is minimized or purged while Person and Decision lineage remains."
      },
      {
        "id": "rehire-no-cv-resurrection",
        "kind": "negative",
        "input": "A later rehire silently restores a previously purged CV.",
        "expect": "The restoration is rejected; a new scoped submission is required."
      }
    ]
  },
  "providerComparison": "# EM-PEO-04 provider comparison\n\nClaude and Grok converge on two identifier-unassigned roots, `Recruitment Requisition` and `Candidacy`; completion and narrowing of reserved `WM-ORG-008` to an asserted Opening; reuse of `WM-ACT-039`; a split Interview Assessment profile over `WM-ACT-025` and `WM-ACT-034`; and an Employment Offer profile over `WM-ECO-021`. Both prohibit allocating a new identifier, duplicating Person on rehire, treating derived vacancy as asserted Opening, collapsing score into decision, or inferring Employment from offer acceptance.\n\nClaude sharpened the standing-authorization identity, provisional Person linking, immutable stage design, employment-offer reuse constraints and data-class retention. Grok sharpened the internal-mobility counterexample, optional Opening scope for Candidacy, seat-cap arithmetic, Application and Posting as dependent artifacts, and the separation of matching and placement from Opening. The reconciled draft keeps source, relation, jurisdiction, privacy, fairness and base-publication gaps as explicit holds.\n",
  "sourceFacts": {
    "WM-ORG-008": "Reserved identifier exists; current spec and source are missing; completion must narrow it to asserted Opening.",
    "bases": "All relevant bases remain reviewable drafts with inherited holds.",
    "relations": "No approved relation row covers WM-ORG-008 or WM-ACT-039.",
    "runtime": "Semantics are declarative; fixtures are not executable tests."
  }
}
```
