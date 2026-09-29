# Frozen semantic audit: EM-PEO-05 Learning, Development and Succession

You are the single independent frozen auditor. Use only the JSON below and no tools. Do not invent identifiers or external facts.

Return: 1. Verdict ACCEPT or REVISE. 2. Confirm or reject all five unassigned roots and no allocation. 3. List every defect that could collapse definition, delivery, enrollment, attendance, completion, assessment, learning result, competency, qualification, credential, plan, aspiration, career path, succession, readiness, nomination, appointment, assignment or access; lose history; breach privacy; or overclaim validation/publication. 4. Give exact remediation and one fixture expectation per defect. 5. Identify contradictions. 6. End with a closed numbered checklist.

## FROZEN RECONCILED DOSSIER
```json
{
  "contourId": "EM-PEO-05",
  "candidateRevision": 2,
  "candidates": {
    "learning-program": {
      "format": "vercy-model-allocation-candidate/v1",
      "contourId": "EM-PEO-05",
      "proposedName": "Learning Program",
      "modelId": null,
      "registryId": null,
      "allocationState": "unassigned",
      "decision": "NEW MODEL",
      "canonicalPublishable": false,
      "identityTest": {
        "stableIdentity": "A reusable curriculum definition remains identifiable independently of deliveries, enrollments and learner outcomes.",
        "versionIdentity": "Changes to objectives, curriculum, prerequisites or assessment policy create an immutable successor version.",
        "independentLifecycle": [
          "draft",
          "reviewed",
          "approved",
          "published",
          "effective",
          "deprecated",
          "superseded",
          "retired"
        ],
        "mastership": "authorized curriculum steward"
      },
      "boundary": {
        "owns": [
          "learning-program identity",
          "immutable curriculum versions",
          "learning objectives",
          "curriculum structure",
          "prerequisites",
          "assessment and completion policy",
          "successor history"
        ],
        "references": [
          {
            "target": "WM-ACT-038",
            "purpose": "Scheduled delivery",
            "contractState": "provisional"
          },
          {
            "target": "WM-PER-008",
            "purpose": "Learning result and qualification",
            "contractState": "provisional"
          },
          {
            "target": "WM-ACT-034",
            "purpose": "Assessment result",
            "contractState": "provisional"
          },
          {
            "target": "WM-KNW-013",
            "purpose": "Pinned criteria",
            "contractState": "provisional"
          }
        ],
        "excludes": [
          "delivery or cohort",
          "enrollment",
          "attendance",
          "assessment occurrence",
          "learning result",
          "credential"
        ]
      },
      "objects": {
        "LearningProgram": {
          "identity": [
            "learningProgramId"
          ],
          "required": [
            "name",
            "ownerRef",
            "status"
          ],
          "optional": [
            "successorRef"
          ]
        },
        "ProgramVersion": {
          "identity": [
            "learningProgramId",
            "version"
          ],
          "required": [
            "objectives",
            "curriculum",
            "validFrom",
            "contentDigest",
            "objectiveVersions",
            "assessmentDesignVersion"
          ],
          "optional": [
            "prerequisites",
            "assessmentPolicy",
            "validTo"
          ]
        }
      },
      "invariants": [
        "A program may exist without a delivery.",
        "Published versions are immutable.",
        "Objectives have stable version-scoped identifiers.",
        "Prerequisites are explicit.",
        "Definition and delivery remain distinct.",
        "Enrollment remains external.",
        "Completion policy never proves achievement.",
        "Assessment criteria are pinned.",
        "Supersession preserves historical results.",
        "A program grants no qualification or credential.",
        "Missing outcome evidence remains unknown.",
        "Provider delivery does not mutate curriculum authority.",
        "One Program Version may address several version-scoped objectives.",
        "Each Delivery pins exactly one immutable Program Version.",
        "Cancelling a Delivery never deletes or versions the Program.",
        "Course-versus-curriculum grain remains governed and creates no implicit Course root."
      ],
      "holds": [
        "Registry allocation is pending and no identifier may be guessed.",
        "Base specifications and approved relations remain incomplete.",
        "Package conversion and live verification are pending.",
        "One frozen semantic audit is pending."
      ],
      "candidateRevision": 2
    },
    "enrollment": {
      "format": "vercy-model-allocation-candidate/v1",
      "contourId": "EM-PEO-05",
      "proposedName": "Enrollment",
      "modelId": null,
      "registryId": null,
      "allocationState": "unassigned",
      "decision": "NEW MODEL",
      "canonicalPublishable": false,
      "identityTest": {
        "stableIdentity": "A learner admission and participation record remains identifiable independently of the scheduled delivery and survives delivery cancellation, postponement or replacement.",
        "versionIdentity": "Transfer, waitlist, withdrawal or admission correction appends an attributable successor state.",
        "independentLifecycle": [
          "requested",
          "waitlisted",
          "admitted",
          "enrolled",
          "transferred",
          "withdrawn",
          "cancelled",
          "closed"
        ],
        "mastership": "authorized learning registrar"
      },
      "boundary": {
        "owns": [
          "enrollment identity",
          "learner and program-version binding",
          "admission and prerequisite decision",
          "capacity and waitlist state",
          "delivery allocation",
          "transfer and withdrawal history",
          "learner rights"
        ],
        "references": [
          {
            "target": "WM-PER-001",
            "purpose": "Learner identity",
            "contractState": "provisional"
          },
          {
            "target": "WM-ACT-038",
            "purpose": "Delivery participation",
            "contractState": "provisional"
          },
          {
            "target": "WM-REC-010",
            "purpose": "Admission decision",
            "contractState": "provisional"
          },
          {
            "target": "WM-PER-008",
            "purpose": "Result boundary",
            "contractState": "provisional"
          }
        ],
        "excludes": [
          "program definition",
          "delivery identity",
          "attendance",
          "assessment result",
          "qualification",
          "credential"
        ]
      },
      "objects": {
        "Enrollment": {
          "identity": [
            "enrollmentId"
          ],
          "required": [
            "learnerRef",
            "programVersionRef",
            "status",
            "validFrom",
            "recordedAt"
          ],
          "optional": [
            "deliveryRef",
            "decisionRef",
            "waitlistPosition",
            "supersedesRef",
            "deliveryRef",
            "attendanceRefs",
            "completionRef",
            "resultRefs",
            "validTo"
          ]
        }
      },
      "invariants": [
        "Enrollment identity is external to delivery.",
        "Enrollment pins one program version.",
        "Admission and attendance remain distinct.",
        "Login or access never proves attendance.",
        "Cancellation of delivery does not erase enrollment.",
        "Transfer appends history.",
        "Withdrawal preserves prior participation facts.",
        "Prerequisite evaluation is attributable.",
        "Capacity state is explicit.",
        "Enrollment never proves achievement.",
        "Enrollment grants no qualification or credential.",
        "Missing attendance remains unknown.",
        "A cancelled or superseded Enrollment remains historical participation and is not an active seat.",
        "Attendance, completion and assessment are independent assertions.",
        "Enrollment is not WM-ORG-016 assignment and grants no access.",
        "Waitlist and transfer history never overwrite earlier states."
      ],
      "holds": [
        "Registry allocation is pending and no identifier may be guessed.",
        "Base specifications and approved relations remain incomplete.",
        "Package conversion and live verification are pending.",
        "One frozen semantic audit is pending."
      ],
      "candidateRevision": 2
    },
    "career-path": {
      "format": "vercy-model-allocation-candidate/v1",
      "contourId": "EM-PEO-05",
      "proposedName": "Career Path",
      "modelId": null,
      "registryId": null,
      "allocationState": "unassigned",
      "decision": "NEW MODEL",
      "canonicalPublishable": false,
      "identityTest": {
        "stableIdentity": "A reusable career-transition definition remains identifiable independently of workers, aspirations, nominations and assignments.",
        "versionIdentity": "Changes to nodes, transitions or expectations create an immutable successor version.",
        "independentLifecycle": [
          "draft",
          "reviewed",
          "approved",
          "published",
          "effective",
          "deprecated",
          "superseded",
          "retired"
        ],
        "mastership": "enterprise career architecture authority"
      },
      "boundary": {
        "owns": [
          "career-path identity",
          "immutable path versions",
          "job-family or position nodes",
          "typical transitions",
          "transition expectations",
          "applicability",
          "successor history"
        ],
        "references": [
          {
            "target": "WM-ORG-004",
            "purpose": "Position context",
            "contractState": "provisional"
          },
          {
            "target": "WM-XCT-023",
            "purpose": "Role context",
            "contractState": "provisional"
          },
          {
            "target": "WM-PER-009",
            "purpose": "Competency expectations",
            "contractState": "provisional"
          },
          {
            "target": "WM-ACT-008",
            "purpose": "Worker development plan",
            "contractState": "provisional"
          }
        ],
        "excludes": [
          "worker aspiration",
          "promotion entitlement",
          "nomination",
          "appointment",
          "position assignment",
          "compensation decision"
        ]
      },
      "objects": {
        "CareerPath": {
          "identity": [
            "careerPathId"
          ],
          "required": [
            "name",
            "ownerRef",
            "status"
          ],
          "optional": [
            "successorRef"
          ]
        },
        "CareerPathVersion": {
          "identity": [
            "careerPathId",
            "version"
          ],
          "required": [
            "nodes",
            "transitions",
            "validFrom",
            "contentDigest"
          ],
          "optional": [
            "expectations",
            "validTo"
          ]
        }
      },
      "invariants": [
        "A career path may exist without incumbents.",
        "Published versions are immutable.",
        "Nodes reference external role or position definitions.",
        "Transitions are typical possibilities, not promises.",
        "Expectations are version-pinned.",
        "Worker aspiration remains separate.",
        "A path never grants promotion.",
        "A path never creates nomination.",
        "A path never creates assignment or access.",
        "Compensation remains external.",
        "Supersession preserves historical plans.",
        "Missing transition evidence remains unknown.",
        "A Career Path is advisory unless a separately governed gate is explicitly attached.",
        "Path steps may recommend Program Versions and objective versions without owning them.",
        "Aspiration is a time-stamped person assertion and never path identity, nomination or appointment."
      ],
      "holds": [
        "Registry allocation is pending and no identifier may be guessed.",
        "Base specifications and approved relations remain incomplete.",
        "Package conversion and live verification are pending.",
        "One frozen semantic audit is pending."
      ],
      "candidateRevision": 2
    },
    "succession-plan": {
      "format": "vercy-model-allocation-candidate/v1",
      "contourId": "EM-PEO-05",
      "proposedName": "Succession Plan",
      "modelId": null,
      "registryId": null,
      "allocationState": "unassigned",
      "decision": "NEW MODEL",
      "canonicalPublishable": false,
      "identityTest": {
        "stableIdentity": "A governed talent-coverage plan remains identifiable independently of positions, people, readiness assessments and appointments.",
        "versionIdentity": "Each review cycle or changed pool, coverage or critical-position scope creates a successor revision.",
        "independentLifecycle": [
          "draft",
          "reviewed",
          "approved",
          "effective",
          "revised",
          "superseded",
          "closed",
          "archived"
        ],
        "mastership": "authorized talent governance authority"
      },
      "boundary": {
        "owns": [
          "succession-plan identity",
          "critical-position scope",
          "review cycle",
          "candidate-pool membership",
          "bench-depth and coverage state",
          "readiness references",
          "revision history"
        ],
        "references": [
          {
            "target": "WM-ORG-004",
            "purpose": "Critical position",
            "contractState": "provisional"
          },
          {
            "target": "WM-ACT-034",
            "purpose": "Readiness assessment",
            "contractState": "provisional"
          },
          {
            "target": "WM-REC-010",
            "purpose": "Nomination and appointment decisions",
            "contractState": "provisional"
          },
          {
            "target": "WM-ORG-016",
            "purpose": "Assignment",
            "contractState": "provisional"
          }
        ],
        "excludes": [
          "person or position identity",
          "readiness assessment result",
          "nomination decision",
          "appointment decision",
          "position assignment",
          "access grant"
        ]
      },
      "objects": {
        "SuccessionPlan": {
          "identity": [
            "successionPlanId"
          ],
          "required": [
            "name",
            "ownerRef",
            "status"
          ],
          "optional": [
            "successorRef"
          ]
        },
        "SuccessionPlanRevision": {
          "identity": [
            "successionPlanId",
            "revision"
          ],
          "required": [
            "criticalPositionRefs",
            "poolEntries",
            "reviewAt",
            "contentDigest"
          ],
          "optional": [
            "coverageState",
            "readinessRefs",
            "supersedesRevision"
          ]
        }
      },
      "invariants": [
        "A plan may exist without candidates.",
        "Revisions are immutable.",
        "Critical positions are explicitly scoped.",
        "Pool membership is time-bounded.",
        "Readiness remains an external assessment.",
        "Readiness criteria and scale are pinned.",
        "Pool membership confers no appointment.",
        "Nomination and appointment are separate decisions.",
        "Appointment requires a separate assignment.",
        "Revision leaves current assignments unchanged.",
        "Ratings expire and remain contestable.",
        "Sensitive data uses minimum disclosure.",
        "Every readiness reference pins the assessed position or path-step profile version.",
        "Ready-now is neither an available seat nor an access entitlement.",
        "Appointment authorizes but does not embed or replace WM-ORG-016 assignment facts."
      ],
      "holds": [
        "Registry allocation is pending and no identifier may be guessed.",
        "Base specifications and approved relations remain incomplete.",
        "Package conversion and live verification are pending.",
        "One frozen semantic audit is pending."
      ],
      "candidateRevision": 2
    },
    "learning-result": {
      "format": "vercy-model-allocation-candidate/v1",
      "contourId": "EM-PEO-05",
      "proposedName": "Learning Result",
      "modelId": null,
      "registryId": null,
      "allocationState": "unassigned",
      "decision": "NEW MODEL",
      "canonicalPublishable": false,
      "candidateRevision": 2,
      "identityTest": {
        "stableIdentity": "A learner's achieved or not-achieved result for one version-scoped learning objective remains identifiable independently of attendance, completion, assessment administration, qualification award and credential.",
        "versionIdentity": "A retake, different objective or objective version, changed assessment basis or attributable correction creates a new result or explicit successor.",
        "independentLifecycle": [
          "provisional",
          "finalized",
          "superseded",
          "voided",
          "retained",
          "disposed"
        ],
        "mastership": "authorized learning-record steward"
      },
      "boundary": {
        "owns": [
          "learning-result identity",
          "person and enrollment references",
          "program and objective-version references",
          "assessment-basis references",
          "achieved or not-achieved outcome",
          "finalization and successor history",
          "valid and recorded time",
          "retention and disposition state"
        ],
        "references": [
          {
            "target": "WM-PER-001",
            "purpose": "Learner identity",
            "contractState": "provisional"
          },
          {
            "target": "WM-ACT-034",
            "purpose": "Assessment result and basis",
            "contractState": "provisional"
          },
          {
            "target": "WM-PER-008",
            "purpose": "Optional downstream qualification award",
            "contractState": "provisional"
          },
          {
            "target": "WM-XCT-017",
            "purpose": "Optional downstream credential",
            "contractState": "provisional"
          }
        ],
        "excludes": [
          "attendance or delivery completion",
          "assessment administration or raw score ownership",
          "competency assertion",
          "qualification award",
          "credential",
          "development-plan progress",
          "appointment, assignment or access"
        ]
      },
      "objects": {
        "LearningResult": {
          "identity": [
            "learningResultId"
          ],
          "required": [
            "personRef",
            "enrollmentRef",
            "programVersionRef",
            "objectiveVersionRef",
            "assessmentBasisRefs",
            "outcome",
            "finalizedAt",
            "recordedAt",
            "status"
          ],
          "optional": [
            "assessmentResultRefs",
            "evidenceRefs",
            "validFrom",
            "validTo",
            "predecessorRef",
            "correctionReason",
            "retentionPolicyRef",
            "dispositionState"
          ],
          "outcomes": [
            "achieved",
            "not-achieved",
            "indeterminate"
          ],
          "lifecycle": [
            "provisional",
            "finalized",
            "superseded",
            "voided",
            "retained",
            "disposed"
          ]
        }
      },
      "invariants": [
        "Every result pins exactly one person, enrollment, Program Version and objective version.",
        "Every result cites an attributable assessment basis.",
        "Attendance and completion never imply achieved outcome.",
        "Failed assessment may create not-achieved Learning Result without qualification or credential.",
        "One Enrollment may yield several Learning Results for distinct objective versions.",
        "A retake appends a result and never overwrites prior results.",
        "Learning Result is neither WM-PER-008 qualification award nor WM-XCT-017 credential.",
        "Downstream award and credential are optional and never substitutes for the result.",
        "Indeterminate never collapses to not-achieved or achieved.",
        "Finalized result correction creates an attributable successor.",
        "Disposition never cascades to Person, award or credential masters.",
        "No identifier is allocated until registry reservation is approved."
      ],
      "holds": [
        "Registry allocation is pending and no identifier may be guessed.",
        "One frozen semantic audit is pending.",
        "Objective-version, assessment-basis and downstream award relation contracts require canonical approval.",
        "Privacy, retention, source pins and executable conformance remain pending."
      ]
    }
  },
  "profile": {
    "format": "vercy-enterprise-profile-candidate/v1",
    "contourId": "EM-PEO-05",
    "name": "Enterprise Learning, Development and Succession",
    "decision": "PROFILE",
    "newRuntimeId": false,
    "bases": [
      "WM-ACT-038",
      "WM-PER-008",
      "WM-ACT-008",
      "WM-ACT-034",
      "WM-REC-010",
      "WM-ORG-016"
    ],
    "constraints": [
      "Definition, delivery and enrollment remain distinct.",
      "Development Plan profiles WM-ACT-008 and grants no personnel authority.",
      "Readiness profiles WM-ACT-034 and never confers assignment or access.",
      "Appointment requires WM-REC-010 decision followed by WM-ORG-016 assignment.",
      "Learning Program owns immutable Program Versions; WM-ACT-038 is narrowed to scheduled Delivery or cohort.",
      "Enrollment is an independent root and survives Delivery cancellation as historical participation.",
      "Attendance, completion, Assessment Result, Learning Result, competency assertion, qualification award and credential remain non-equivalent.",
      "Learning Result is an identifier-unassigned root; unsuccessful results never enter WM-PER-008 award identity.",
      "Every Learning Result pins Program Version, objective version and assessment basis.",
      "Retakes append Assessment Results and Learning Results without rewriting history.",
      "Development Plan may map one Program to several objectives and grants no personnel authority.",
      "Succession Plan revision leaves WM-ORG-016 assignments unchanged.",
      "Readiness pins position or path-step profile version and confers neither seat nor access.",
      "Nomination and appointment are distinct WM-REC-010 decisions; appointment authorizes but does not embed WM-ORG-016 assignment."
    ],
    "candidateRevision": 2,
    "canonicalPublishable": false,
    "holds": [
      "Base specifications and approved relations remain incomplete.",
      "Objective-version, assessment-basis and downstream award relation contracts require canonical approval.",
      "One frozen semantic audit is pending.",
      "Package conversion and live verification are pending.",
      "Privacy, retention, source pins and executable conformance remain pending.",
      "Registry allocation is pending and no identifier may be guessed."
    ],
    "relationContracts": {
      "WM-ACT-038": "provisional",
      "WM-PER-008": "provisional",
      "WM-ACT-008": "provisional",
      "WM-ACT-034": "provisional",
      "WM-REC-010": "provisional",
      "WM-ORG-016": "provisional"
    }
  },
  "fixtures": {
    "learning-program": [
      {
        "id": "no-delivery",
        "kind": "positive",
        "input": "A curriculum is released before scheduling.",
        "expect": "It remains independently valid."
      },
      {
        "id": "successor",
        "kind": "positive",
        "input": "Objectives change next year.",
        "expect": "A successor version is appended."
      },
      {
        "id": "many-deliveries",
        "kind": "positive",
        "input": "Several providers deliver one version.",
        "expect": "The curriculum identity remains shared."
      },
      {
        "id": "completion-achievement",
        "kind": "negative",
        "input": "Delivery completion is treated as objective achievement.",
        "expect": "The inference is rejected."
      },
      {
        "id": "credential",
        "kind": "negative",
        "input": "Program publication issues a credential.",
        "expect": "The issuance is rejected."
      },
      {
        "id": "mutable-version",
        "kind": "negative",
        "input": "A released objective is overwritten.",
        "expect": "The mutation is rejected."
      },
      {
        "id": "two-objectives-one-version",
        "kind": "semantic",
        "input": "One Program Version addresses two objectives.",
        "expect": "Normatively, the version retains two objective-version identities without duplicating the Program."
      },
      {
        "id": "delivery-pins-version",
        "kind": "semantic",
        "input": "A Delivery omits Program Version pin.",
        "expect": "Normatively, the Delivery is non-conformant."
      }
    ],
    "enrollment": [
      {
        "id": "pre-delivery",
        "kind": "positive",
        "input": "A learner is admitted before a cohort exists.",
        "expect": "Enrollment remains valid without delivery."
      },
      {
        "id": "cancelled-delivery",
        "kind": "positive",
        "input": "A delivery is cancelled and replacement is offered.",
        "expect": "Enrollment survives and records transfer."
      },
      {
        "id": "withdrawal",
        "kind": "positive",
        "input": "A learner withdraws after attendance.",
        "expect": "Prior participation remains."
      },
      {
        "id": "login-attendance",
        "kind": "negative",
        "input": "Platform access is treated as attendance.",
        "expect": "The inference is rejected."
      },
      {
        "id": "achievement",
        "kind": "negative",
        "input": "Enrollment is treated as learning achievement.",
        "expect": "The inference is rejected."
      },
      {
        "id": "delivery-contained",
        "kind": "negative",
        "input": "Deleting a delivery deletes enrollment identity.",
        "expect": "The cascade is rejected."
      },
      {
        "id": "cancel-survives",
        "kind": "semantic",
        "input": "A Delivery is cancelled after attendance.",
        "expect": "Normatively, enrollment and participation history remain; active-seat state ends."
      },
      {
        "id": "attendance-failed",
        "kind": "semantic",
        "input": "A learner attends fully and fails assessment.",
        "expect": "Normatively, attendance remains true; no achievement, award or credential is inferred."
      }
    ],
    "career-path": [
      {
        "id": "vacant-path",
        "kind": "positive",
        "input": "A path is published with no incumbent users.",
        "expect": "It remains independently valid."
      },
      {
        "id": "branching",
        "kind": "positive",
        "input": "A path has technical and managerial branches.",
        "expect": "Both governed transitions remain available."
      },
      {
        "id": "successor",
        "kind": "positive",
        "input": "A role family changes.",
        "expect": "A successor path version is appended."
      },
      {
        "id": "promotion",
        "kind": "negative",
        "input": "Following the path is treated as a promotion entitlement.",
        "expect": "The inference is rejected."
      },
      {
        "id": "appointment",
        "kind": "negative",
        "input": "A transition automatically appoints a worker.",
        "expect": "The assignment is rejected."
      },
      {
        "id": "mutable-version",
        "kind": "negative",
        "input": "A published transition is overwritten.",
        "expect": "The mutation is rejected."
      },
      {
        "id": "advisory-not-entitlement",
        "kind": "semantic",
        "input": "A path step is treated as promotion entitlement.",
        "expect": "Normatively, the inference is non-conformant."
      },
      {
        "id": "aspiration-not-nomination",
        "kind": "semantic",
        "input": "A worker aspiration is treated as nomination.",
        "expect": "Normatively, the identity collapse is non-conformant."
      }
    ],
    "succession-plan": [
      {
        "id": "empty-bench",
        "kind": "positive",
        "input": "A critical position has no candidates.",
        "expect": "The coverage gap is explicit."
      },
      {
        "id": "revision",
        "kind": "positive",
        "input": "A review changes pool membership.",
        "expect": "A successor revision preserves prior state."
      },
      {
        "id": "later-appointment",
        "kind": "positive",
        "input": "A candidate is later selected.",
        "expect": "Separate nomination, appointment and assignment records are required."
      },
      {
        "id": "automatic-appointment",
        "kind": "negative",
        "input": "Ready status creates an assignment.",
        "expect": "The inference is rejected."
      },
      {
        "id": "access-grant",
        "kind": "negative",
        "input": "Pool membership grants system access.",
        "expect": "The grant is rejected."
      },
      {
        "id": "overwrite-rating",
        "kind": "negative",
        "input": "A new review overwrites prior readiness evidence.",
        "expect": "The mutation is rejected."
      },
      {
        "id": "revision-keeps-assignment",
        "kind": "semantic",
        "input": "A successor plan changes a slate.",
        "expect": "Normatively, existing WM-ORG-016 assignments remain unchanged."
      },
      {
        "id": "ready-not-access",
        "kind": "semantic",
        "input": "Ready-now is projected as access entitlement.",
        "expect": "Normatively, the inference is non-conformant."
      }
    ],
    "learning-result": [
      {
        "id": "failed-result",
        "kind": "positive",
        "input": "Attendance is complete but assessment fails objective O1.",
        "expect": "Normatively, a not-achieved Learning Result may be recorded without award or credential."
      },
      {
        "id": "two-objective-results",
        "kind": "positive",
        "input": "One course serves objective versions O1 and O2.",
        "expect": "Normatively, two distinct Learning Results share one Enrollment and Program Version."
      },
      {
        "id": "retake-appends",
        "kind": "positive",
        "input": "A learner retakes the assessment and achieves the objective.",
        "expect": "Normatively, a successor result is appended and the failed result remains resolvable."
      },
      {
        "id": "attendance-is-result",
        "kind": "negative",
        "input": "Attendance alone is used as achieved outcome.",
        "expect": "Normatively, the inference is non-conformant."
      },
      {
        "id": "award-is-result",
        "kind": "negative",
        "input": "A qualification award replaces the Learning Result.",
        "expect": "Normatively, the identity collapse is non-conformant."
      },
      {
        "id": "result-is-credential",
        "kind": "negative",
        "input": "A Learning Result is exposed as a credential.",
        "expect": "Normatively, the identity collapse is non-conformant."
      },
      {
        "id": "missing-objective-version",
        "kind": "negative",
        "input": "A result cites only an objective label.",
        "expect": "Normatively, the result is non-conformant without objective-version identity."
      },
      {
        "id": "indeterminate-not-fail",
        "kind": "negative",
        "input": "An indeterminate result is collapsed to not-achieved.",
        "expect": "Normatively, the collapse is non-conformant."
      }
    ]
  },
  "providerComparison": "# EM-PEO-05 provider comparison\n\nClaude and Grok converge on identifier-unassigned Learning Program, Enrollment, Career Path and Succession Plan roots; narrowing WM-ACT-038 to scheduled Delivery; Development Plan on WM-ACT-008; readiness on WM-ACT-034; distinct nomination and appointment decisions on WM-REC-010; and assignment remaining in WM-ORG-016. Both prohibit inferring learning from attendance, qualification from completion, appointment from readiness, or access from any plan or slate.\n\nThey diverge on Learning Result. Claude profiles successful outcome achievement on WM-PER-008. Grok's failed-assessment counterexample shows that achieved and not-achieved objective results must persist without corrupting the qualification-award register. The reconciled revision therefore keeps Learning Result as a fifth identifier-unassigned root, while qualification awards and credentials remain optional downstream records.\n",
  "sourceFacts": {
    "relations": "All cross-model relation contracts are provisional.",
    "bases": "Supplied bases remain held reviewable drafts.",
    "runtime": "Semantics and fixtures are declarative, not executable tests."
  }
}
```
