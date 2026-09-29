# Frozen semantic audit: EM-PEO-02 Work Relations and Assignments

You are the single independent frozen auditor. Use only the JSON below and no tools. Do not invent identifiers or external facts.

Return:
1. Verdict ACCEPT or REVISE.
2. Confirm or reject: PROFILE over WM-PER-001/WM-ORG-005/WM-ORG-016 plus identifier-unassigned EmployeeProfile candidate; no new runtime ID.
3. List every defect that could collapse Person, EmployeeProfile, Employment, Assignment, employer, host, supplier, JML or access authority; lose history; misclassify workers; misuse employee numbers; infer revocation; or overclaim validation/publication.
4. Give exact remediation and one fixture expectation for each defect.
5. Identify contradictions.
6. End with a closed numbered remediation checklist.

## FROZEN RECONCILED DOSSIER
```json
{
  "decision": {
    "format": "vercy-enterprise-profile-candidate/v1",
    "contourId": "EM-PEO-02",
    "candidateRevision": 2,
    "name": "Work Relations and Assignments",
    "decision": "PROFILE_PLUS_IDENTIFIER_UNASSIGNED_NEW_MODEL_CANDIDATE",
    "newRuntimeId": false,
    "bases": [
      "WM-PER-001",
      "WM-ORG-005",
      "WM-ORG-016"
    ],
    "referencedNeighbors": [
      "WM-ACT-040",
      "EM-RSK-03",
      "EM-OPS-01",
      "EM-XCT-01"
    ],
    "profileTypes": [
      "PersonReference",
      "EmploymentProfile",
      "WorkAssignmentReference"
    ],
    "unassignedCandidates": [
      "EmployeeProfile"
    ],
    "rejectedNewMasters": [
      "Engagement",
      "LifecycleEvent",
      "JoinerMoverLeaverCase"
    ],
    "constraints": [
      "A profile is scoped to exactly one Person and one employing party.",
      "A new employing party creates a new profile and never changes the Person anchor.",
      "Employee numbers are unique only within employing party, numbering scheme and validity interval.",
      "A numbering scheme declares reuse policy; prior bindings remain historically resolvable.",
      "An employee number is never a Person identifier, Employment identity, Assignment identity, account identifier or cross-employer join key.",
      "Profile existence never proves active Employment, employee status, contractor status or legal classification.",
      "Worker category is a purpose and jurisdiction-qualified sourced assertion with effective interval and dispute path.",
      "Employment owns relationship identity, terms, classification evidence, continuity, separation and disagreement.",
      "Assignment owns post, host, scope, conveyed authority, allocation, lifecycle and handover.",
      "Every Assignment resolves to exactly one explicit Employment or engagement context.",
      "Employer, work customer, staffing supplier, paymaster, platform and host roles are not collapsed.",
      "A new employing party, governed basis change, rehire after closed service or parallel contract creates a new Employment unless evidenced legal succession preserves continuity.",
      "A material post, host, scope or conveyed-authority change creates a new Assignment.",
      "Ordinary effective changes retain identity through amendments; corrections use record versioning and do not rewrite real-world history.",
      "One Employment can realize concurrent or sequential Assignments and one Person can hold concurrent Employments.",
      "Rehire at the same employer reuses EmployeeProfile, creates a new Employment and follows explicit number-reuse policy.",
      "Closing Employment never deletes Person, EmployeeProfile, earlier Employment, number history or Assignments.",
      "Offboarding creates access-verification obligations and never proves entitlement revocation.",
      "JML desired, requested, executed and independently verified states remain distinct.",
      "Employment or JML case closure cannot set access-revocation success without access-authority evidence.",
      "WM-ORG-005 COMPOSE WM-ORG-016 remains a draft relation until approved.",
      "The candidate has no model or runtime identifier until registry allocation."
    ]
  },
  "allocationCandidate": {
    "format": "vercy-model-allocation-candidate/v1",
    "contourId": "EM-PEO-02",
    "candidateRevision": 2,
    "proposedName": "Employee Profile",
    "modelId": null,
    "registryId": null,
    "allocationState": "unassigned",
    "decision": "NEW MODEL CANDIDATE",
    "canonicalPublishable": false,
    "identityTest": {
      "stableIdentity": "One employer-scoped continuity profile binds one Person to one employing party across successive Employment spells, employee-number changes, assignments, separation and rehire.",
      "versionIdentity": "Effective-dated profile content and number bindings change without replacing Person, Employment or Assignment records.",
      "independentLifecycle": [
        "proposed",
        "active",
        "inactive",
        "closed",
        "superseded"
      ],
      "mastership": "employing-party workforce master-data authority"
    },
    "boundary": {
      "owns": [
        "employer-scoped EmployeeProfile identity",
        "effective-dated EmployeeProfile versions",
        "one Person and one employing-party binding",
        "dated employee-number bindings by explicit numbering scheme",
        "references to zero or more successive or concurrent Employment records",
        "purpose and jurisdiction-qualified worker-category assertions",
        "rehire continuity and profile succession history"
      ],
      "references": [
        {
          "target": "WM-PER-001",
          "purpose": "durable Person anchor"
        },
        {
          "target": "WM-ORG-005",
          "purpose": "Employment and engagement relationship master"
        },
        {
          "target": "WM-ORG-016",
          "purpose": "Work Assignment master"
        },
        {
          "target": "WM-ACT-040",
          "purpose": "join, move, leave and rejoin coordination with separately verified access execution"
        },
        {
          "target": "EM-RSK-03",
          "purpose": "DigitalAccount, AccessRole and AccessReview masters"
        },
        {
          "target": "EM-OPS-01",
          "purpose": "process-definition master"
        },
        {
          "target": "EM-XCT-01",
          "purpose": "identifier-scheme authority"
        }
      ],
      "excludes": [
        "Person or cross-employer worker identity",
        "Employment contract, relationship or engagement lifecycle",
        "Work Assignment, post, host, scope or authority lifecycle",
        "access entitlement, account, revocation or review authority",
        "JML case or workflow identity",
        "legal classification inferred from a profile or category label",
        "Engagement, LifecycleEvent or JoinerMoverLeaverCase as additional masters"
      ]
    },
    "objects": {
      "EmployeeProfile": {
        "identity": [
          "employeeProfileId"
        ],
        "required": [
          "employerRef",
          "personRef",
          "status"
        ],
        "optional": [
          "successorRef",
          "closedAt"
        ],
        "lifecycle": [
          "proposed",
          "active",
          "inactive",
          "closed",
          "superseded"
        ]
      },
      "EmployeeProfileVersion": {
        "identity": [
          "employeeProfileId",
          "version"
        ],
        "required": [
          "employmentRefs",
          "effectiveFrom",
          "contentDigest",
          "status"
        ],
        "optional": [
          "effectiveTo",
          "supersedesVersion",
          "categoryAssertions"
        ],
        "lifecycle": [
          "draft",
          "active",
          "superseded",
          "withdrawn"
        ]
      },
      "EmployeeNumberBinding": {
        "identity": [
          "numberBindingId"
        ],
        "required": [
          "employeeProfileRef",
          "employerRef",
          "numberSchemeRef",
          "number",
          "validFrom"
        ],
        "optional": [
          "validTo",
          "sourceRef",
          "reusePolicyRef"
        ]
      },
      "WorkerCategoryAssertion": {
        "identity": [
          "assertionId"
        ],
        "required": [
          "employeeProfileVersionRef",
          "category",
          "purpose",
          "jurisdictionRef",
          "sourceRef",
          "validFrom"
        ],
        "optional": [
          "validTo",
          "determinationRef",
          "disputeRef"
        ]
      }
    },
    "invariants": [
      "A profile is scoped to exactly one Person and one employing party.",
      "A new employing party creates a new profile and never changes the Person anchor.",
      "Employee numbers are unique only within employing party, numbering scheme and validity interval.",
      "A numbering scheme declares reuse policy; prior bindings remain historically resolvable.",
      "An employee number is never a Person identifier, Employment identity, Assignment identity, account identifier or cross-employer join key.",
      "Profile existence never proves active Employment, employee status, contractor status or legal classification.",
      "Worker category is a purpose and jurisdiction-qualified sourced assertion with effective interval and dispute path.",
      "Employment owns relationship identity, terms, classification evidence, continuity, separation and disagreement.",
      "Assignment owns post, host, scope, conveyed authority, allocation, lifecycle and handover.",
      "Every Assignment resolves to exactly one explicit Employment or engagement context.",
      "Employer, work customer, staffing supplier, paymaster, platform and host roles are not collapsed.",
      "A new employing party, governed basis change, rehire after closed service or parallel contract creates a new Employment unless evidenced legal succession preserves continuity.",
      "A material post, host, scope or conveyed-authority change creates a new Assignment.",
      "Ordinary effective changes retain identity through amendments; corrections use record versioning and do not rewrite real-world history.",
      "One Employment can realize concurrent or sequential Assignments and one Person can hold concurrent Employments.",
      "Rehire at the same employer reuses EmployeeProfile, creates a new Employment and follows explicit number-reuse policy.",
      "Closing Employment never deletes Person, EmployeeProfile, earlier Employment, number history or Assignments.",
      "Offboarding creates access-verification obligations and never proves entitlement revocation.",
      "JML desired, requested, executed and independently verified states remain distinct.",
      "Employment or JML case closure cannot set access-revocation success without access-authority evidence.",
      "WM-ORG-005 COMPOSE WM-ORG-016 remains a draft relation until approved.",
      "The candidate has no model or runtime identifier until registry allocation."
    ],
    "holds": [
      "Registry allocation for EmployeeProfile is pending; no identifier may be guessed.",
      "WM-ORG-005 COMPOSE WM-ORG-016 remains candidate-only.",
      "Parent models and required neighboring profiles retain canonical publication holds.",
      "Cross-model source, rights and immutable-reference gates remain open.",
      "Declarative fixtures are authored but not executed because this package has no runtime semantics.",
      "Package conversion and live verification remain pending."
    ]
  },
  "fixtures": {
    "format": "vercy-model-allocation-fixtures/v1",
    "contourId": "EM-PEO-02",
    "candidateRevision": 2,
    "declarative": true,
    "fixturesExecuted": false,
    "proposedName": "Employee Profile",
    "cases": [
      {
        "id": "dual-employment",
        "kind": "positive",
        "input": "One Person is concurrently employed by two legal employers.",
        "expect": "Two Employment records and two employer-scoped EmployeeProfiles reference one Person; employee numbers never merge across employers."
      },
      {
        "id": "parallel-contract-same-employer",
        "kind": "positive",
        "input": "One Person has two concurrent governed contracts with one employer.",
        "expect": "One EmployeeProfile references two distinct Employment records and any concurrent Assignments resolve to one explicit context each."
      },
      {
        "id": "agency-labor",
        "kind": "positive",
        "input": "A staffing supplier legally employs a worker placed at a work customer.",
        "expect": "Employer, supplier, host and work customer roles remain explicit; the host Assignment resolves to the supplier Employment."
      },
      {
        "id": "freelancer-misclassification",
        "kind": "negative",
        "input": "A profile category says freelancer although control and integration evidence conflict.",
        "expect": "The label cannot establish status; sourced assertions, competent determination and dispute history remain visible."
      },
      {
        "id": "rehire",
        "kind": "positive",
        "input": "A separated worker returns to the same employer.",
        "expect": "The same Person and EmployeeProfile are reused, a new Employment and Assignment are created, and number reuse follows scheme policy."
      },
      {
        "id": "new-employer",
        "kind": "positive",
        "input": "A Person changes legal employer without evidenced succession.",
        "expect": "A new employer-scoped EmployeeProfile and Employment are created while Person identity is unchanged."
      },
      {
        "id": "employer-succession",
        "kind": "positive",
        "input": "A legal succession decision preserves employment continuity.",
        "expect": "The Employment relationship may continue with explicit succession evidence; the event is not silently treated as rehire."
      },
      {
        "id": "assignment-host-change",
        "kind": "positive",
        "input": "The worker moves to a materially different host.",
        "expect": "A new Assignment is created; Person, EmployeeProfile and Employment are preserved."
      },
      {
        "id": "ordinary-amendment",
        "kind": "positive",
        "input": "FTE and reporting line change without material post, host, scope or authority change.",
        "expect": "An effective-dated amendment preserves Employment and Assignment identity."
      },
      {
        "id": "record-correction",
        "kind": "positive",
        "input": "A previously recorded title is corrected without a real-world event.",
        "expect": "Record versioning corrects provenance without inventing a lifecycle transition."
      },
      {
        "id": "incomplete-offboarding",
        "kind": "negative",
        "input": "Employment and JML case are closed but two access outcomes remain unverified.",
        "expect": "Employment may be inactive while access obligations remain open; revocation and completion are not inferred."
      },
      {
        "id": "profile-proves-status",
        "kind": "negative",
        "input": "A consumer treats EmployeeProfile existence as employee status.",
        "expect": "The assertion is rejected because status belongs to sourced, qualified Employment determinations."
      },
      {
        "id": "employee-number-person-key",
        "kind": "negative",
        "input": "Two employers issue the same employee number and a consumer merges the people.",
        "expect": "The merge is rejected because number scope includes employer, scheme and validity."
      },
      {
        "id": "number-reuse-overlap",
        "kind": "negative",
        "input": "One scheme reissues a number while an earlier binding is still valid.",
        "expect": "Validation fails unless the scheme and non-overlapping validity permit reuse."
      },
      {
        "id": "history-delete",
        "kind": "negative",
        "input": "Rehire processing attempts to overwrite the former Employment and number binding.",
        "expect": "The write is rejected; predecessor history remains resolvable."
      },
      {
        "id": "assignment-without-context",
        "kind": "negative",
        "input": "A Work Assignment lacks an Employment or engagement context.",
        "expect": "The Assignment is invalid for this profile."
      },
      {
        "id": "case-closure-as-revocation",
        "kind": "negative",
        "input": "A closed offboarding case is used as proof of access revocation.",
        "expect": "The claim fails without independently verified access-authority evidence."
      },
      {
        "id": "candidate-id-invention",
        "kind": "negative",
        "input": "A generator assigns an EmployeeProfile model ID without registry allocation.",
        "expect": "Generation fails closed and the candidate remains identifier-unassigned."
      }
    ]
  },
  "sourceFacts": {
    "WM-PER-001": "Person master; enterprise roles and employment remain external.",
    "WM-ORG-005": "Employment/engagement relationship master; reviewable draft and relation to assignment not approved.",
    "WM-ORG-016": "Work Assignment master; owns post, host, scope, authority, allocation and history.",
    "registry": "EmployeeProfile has no allocated identifier; no ID may be invented.",
    "runtime": "No executable semantics are proposed; fixtures are declarative and unexecuted."
  },
  "providerComparison": "# EM-PEO-02 provider comparison\n\nClaude and Grok converge on reuse of `WM-PER-001` Person, an Enterprise profile over `WM-ORG-005` Employment, reuse of `WM-ORG-016` Work Assignment, and an identifier-unassigned `EmployeeProfile` candidate. Both distinguish employer, work customer/host and staffing supplier; make worker classification evidence-bearing; preserve one Person across employers; reuse an employer-scoped profile across rehire while creating a new Employment; and forbid treating offboarding or case closure as proof of access revocation.\n\nClaude sharpened the independent identity test for EmployeeProfile, the distinction between amendments and record corrections, relationship succession, employee-number reuse policy and effective clocks. Grok sharpened neighbor ownership (`WM-ACT-040`, `EM-RSK-03`, `EM-OPS-01`, `EM-XCT-01`), rejected extra Engagement/LifecycleEvent/JML masters, and required access-authority evidence for completion. References not present in the frozen dossier are explanatory only and remain held.\n"
}
```
