# Frozen semantic audit: EM-OPS-01 Process, Procedure and Execution

+You are the single independent frozen auditor. Use only the material below and no tools. Audit the reconciled candidates after Claude/Grok boundary comparison. Do not invent identifiers or external facts.

+Required output:
+1. Verdict: ACCEPT or REVISE.
+2. Confirm or reject COMPLETE BOTH RESERVED MODELS on `vr.wm-act-003` and `vr.wm-act-009`, preserving both `0.2.0-legacy` assemblies and creating no new identifier.
+3. List every semantic defect that could cause duplicate identity, mutable historical meaning, false execution evidence, non-reproducible conformance, assignment/execution confusion or unsupported release claims.
+4. For each defect, give a concise exact remediation and fixture expectation.
+5. Identify contradictions among dossier, providers, candidates and fixtures.
+6. End with a closed numbered remediation checklist. If none, say none.
+
+Do not restate the whole model. Treat publication holds as holds, not permission to weaken semantics.
+
## FROZEN PROVIDER DOSSIER

```
{
  "contour": {
    "id": "EM-OPS-01",
    "name": "Процесс, процедура и исполнение",
    "domain": "OPS",
    "kind": "subject",
    "wave": "W1",
    "scope": "Определение процесса, шаги, процедура и конкретный экземпляр исполнения. Методология задаёт правила работы, а не новый экземпляр процесса.",
    "candidate_types": [
      "ProcessDefinition",
      "Procedure",
      "ProcessInstance",
      "ActivityExecution",
      "ProcessMethod"
    ],
    "specific_questions": [
      "Как отличить метод, модель и исполнение?",
      "Как сосуществуют варианты процесса?",
      "Как событие исполнения связано с задачей?"
    ],
    "proposed_invariants": [
      "Исполнение ссылается на версию определения",
      "Отклонение сохраняется явно",
      "Схема BPMN не доказывает фактический путь"
    ],
    "negative_case": "Обновление инструкции меняет задним числом выполненный процесс.",
    "acceptance_scenario": "Один процесс в двух вариантах, ручное исключение и новая процедура дают раздельные трассы исполнения.",
    "comparison_tracks": [
      "APQC/BPMN: определения процессов и исполнение",
      "GS1 EPCIS/SCOR: прослеживаемость и цепочка поставок",
      "IDTA AAS и практика PLM/EAM/WMS: изделие, экземпляр и обслуживание"
    ],
    "vercy_candidates": [
      {
        "model_id": "WM-ACT-003",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-ACT-009",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "OPS-01",
        "fields": [
          {
            "name": "trigger",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "input_contract",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "output_contract",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "process_version",
            "value_type": "text",
            "status": "candidate-not-normative"
          }
        ]
      },
      {
        "predecessor": "OPS-02",
        "fields": [
          {
            "name": "definition_version",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "started_at",
            "value_type": "datetime",
            "status": "candidate-not-normative"
          },
          {
            "name": "ended_at",
            "value_type": "datetime",
            "status": "candidate-not-normative"
          },
          {
            "name": "outcome",
            "value_type": "code",
            "status": "candidate-not-normative"
          }
        ]
      },
      {
        "predecessor": "OPS-03",
        "fields": [
          {
            "name": "preconditions",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "steps",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "verification",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "exception_route",
            "value_type": "text",
            "status": "candidate-not-normative"
          }
        ]
      }
    ],
    "suggested_owner": "Операционный руководитель",
    "candidate_master_systems": "BPM, ERP, WMS, PLM, EAM",
    "related_research_contours": [
      "EM-FAC-02",
      "EM-PRD-03",
      "EM-RSK-01",
      "EM-RSK-04",
      "EM-STR-03",
      "EM-TEC-05",
      "EM-WRK-01"
    ],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "queue_reservation": {
    "sequence": 28,
    "id": "EM-OPS-01",
    "status": "queued",
    "claude_status": "not-started",
    "grok_status": "not-started",
    "boundary_decision": "pending",
    "publication_urls": [],
    "remaining_scope": "Entire research brief pending",
    "target_model_ids": [
      "WM-ACT-003",
      "WM-ACT-009"
    ]
  },
  "registry_reservations": [
    {
      "registry_id": "vr.wm-act-009",
      "record_plane": "world-model",
      "model_id": "WM-ACT-009",
      "name": "Method / Procedure",
      "alternate_names": "",
      "entry_kind": "standalone-mm",
      "origin": "grok-union-current",
      "status": "described-previous-version",
      "review_state": "migration-boundary-review",
      "nav_path": "NAV.ACT.MTH",
      "domain_tags": "ACT.MTH",
      "legacy_alias": "K6",
      "existing_spec_ref": "models/activity-work/K6-practice-method-and-procedure.md",
      "parent_ids": "",
      "contains_ids": "",
      "aligned_model_ids": "",
      "purpose": "Codified ways of doing things",
      "owner_or_maintainer": "authoring organization",
      "source_url": "",
      "namespace_uri": "",
      "source_version_or_year": "2026-08-22",
      "source_group": "",
      "source_category": "",
      "source_format": "",
      "composition_role": "",
      "default_link_type": "",
      "priority_wave": "2",
      "priority_score": "63",
      "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
      "priority_confidence": "low",
      "priority_rationale": "Useful domain context after Wave 0/1 reference foundations",
      "factor_demand": "0.65",
      "factor_data": "0.65",
      "factor_reuse": "0.52",
      "factor_interop": "0.66",
      "factor_feasibility": "0.72",
      "factor_robotics": "0.00",
      "factor_overlap": "0.09",
      "possible_duplicate_of": "",
      "shared_source_with": "",
      "relations_ref": "",
      "validation_flags": "",
      "provenance": "current-112 + Grok review + Claude adversarial audit"
    },
    {
      "registry_id": "vr.wm-act-003",
      "record_plane": "world-model",
      "model_id": "WM-ACT-003",
      "name": "Process / Workflow",
      "alternate_names": "",
      "entry_kind": "standalone-mm",
      "origin": "grok-union-current",
      "status": "described-previous-version",
      "review_state": "migration-boundary-review",
      "nav_path": "NAV.ACT.PRC",
      "domain_tags": "ACT.PRC",
      "legacy_alias": "K3",
      "existing_spec_ref": "models/activity-work/K3-process-and-workflow.md",
      "parent_ids": "",
      "contains_ids": "",
      "aligned_model_ids": "",
      "purpose": "Repeatable multi-step activities",
      "owner_or_maintainer": "process owner (org or agent)",
      "source_url": "",
      "namespace_uri": "",
      "source_version_or_year": "2026-08-22",
      "source_group": "",
      "source_category": "",
      "source_format": "",
      "composition_role": "COMPOSE;REFERENCE",
      "default_link_type": "TYPED-EDGES",
      "priority_wave": "2",
      "priority_score": "63",
      "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
      "priority_confidence": "low",
      "priority_rationale": "Useful domain context after Wave 0/1 reference foundations",
      "factor_demand": "0.65",
      "factor_data": "0.65",
      "factor_reuse": "0.52",
      "factor_interop": "0.66",
      "factor_feasibility": "0.72",
      "factor_robotics": "0.00",
      "factor_overlap": "0.09",
      "possible_duplicate_of": "",
      "shared_source_with": "",
      "relations_ref": "planning/VERCY-MODEL-RELATIONS.csv",
      "validation_flags": "",
      "provenance": "current-112 + Grok review + Claude adversarial audit"
    }
  ],
  "research_status": [
    {
      "sequence": "229",
      "model_id": "WM-ACT-003",
      "name": "Process / Workflow",
      "claude_status": "queued",
      "grok_status": "queued",
      "synthesis_status": "blocked-on-providers",
      "validation_status": "not-valid-or-not-run",
      "bundles": "",
      "layers": "",
      "findings": "",
      "questions": "",
      "artifacts": "",
      "functions": ""
    },
    {
      "sequence": "231",
      "model_id": "WM-ACT-009",
      "name": "Method / Procedure",
      "claude_status": "queued",
      "grok_status": "queued",
      "synthesis_status": "blocked-on-providers",
      "validation_status": "not-valid-or-not-run",
      "bundles": "",
      "layers": "",
      "findings": "",
      "questions": "",
      "artifacts": "",
      "functions": ""
    }
  ],
  "relationship_ledger": [
    {
      "source_model_id": "WM-ACT-003",
      "relation_type": "COMPOSE",
      "target_model_id": "WM-ACT-002",
      "instance_semantics": "Process is composed of acts or activities",
      "rationale": "Behavioral composition",
      "review_state": "candidate"
    },
    {
      "source_model_id": "WM-ACT-003",
      "relation_type": "REFERENCE",
      "target_model_id": "WM-KNW-012",
      "instance_semantics": "Process is governed by policies or rules",
      "rationale": "Normative context",
      "review_state": "candidate"
    }
  ],
  "complete_candidate_specs": {
    "WM-ACT-003": "# K3 Process & Workflow\n\nThis meta-model describes repeatable multi-step activities: the process definitions that say how work flows through steps, roles and states, and the running instances that follow (or deviate from) those definitions. It is separate from the atomic act (K2) because repeatability is its essence: the same definition governs many executions, and the gap between definition and execution is itself information the world needs.\n\n## Manifest\n\n```yaml\nmuif:\n  version: \"1.0\"\nmetaModel:\n  id: \"vercy:world:k3\"\n  csn: world.processAndWorkflow\n  version: 0.2.0\n  displayName: \"Process & Workflow\"\n  description: \"Repeatable multi-step activity definitions and their executions.\"\nconformance:\n  muc: \"2.0: Conformant\"\n  mmas: A1\nnamespaces:\n  - world.processAndWorkflow\nbundles:\n  - csn: world.processAndWorkflow.definition\n    displayName: \"Definition\"\n    layers:\n      - world.processAndWorkflow.definition.processModel\n      - world.processAndWorkflow.definition.roleAssignment\n      - world.processAndWorkflow.definition.stateModel\n  - csn: world.processAndWorkflow.execution\n    displayName: \"Execution\"\n    layers:\n      - world.processAndWorkflow.execution.caseInstance\n      - world.processAndWorkflow.execution.stepPerformance\n      - world.processAndWorkflow.execution.exceptionHandling\n  - csn: world.processAndWorkflow.improvement\n    displayName: \"Improvement\"\n    layers:\n      - world.processAndWorkflow.improvement.measurement\n      - world.processAndWorkflow.improvement.revision\nimports:\n  - source: bpmn\n    version: \"*\"\n  - source: cmmn\n    version: \"*\"\n```\n\n## Bundles and layers\n\n| Bundle | Responsibility | Layers |\n|---|---|---|\n| `definition` | The repeatable model of the work | `processModel`: steps, gateways and sequence flow Â· `roleAssignment`: which roles perform which steps Â· `stateModel`: allowed states and transitions of the governed thing |\n| `execution` | Running the model in the world | `caseInstance`: one running occurrence of a process Â· `stepPerformance`: executed steps recorded as acts Â· `exceptionHandling`: deviations, escalations and compensations |\n| `improvement` | Learning from executions | `measurement`: cycle times, throughput and conformance of instances Â· `revision`: versioning and change of definitions |\n\n## Objects\n\n- `process`: a named repeatable activity definition; key attributes: name, purpose, owner reference, version, trigger\n- `step`: one unit of work within a process; key attributes: name, entry and exit conditions, expected duration\n- `gateway`: a branching or merging point; key attributes: kind (exclusive, parallel, event based), condition expressions\n- `role`: a named performer position in the process; key attributes: name, required capabilities, assignment rule\n- `state`: an allowed condition of the case subject; key attributes: name, meaning, permitted transitions\n- `processInstance`: one running or completed execution; key attributes: process version, subject reference, start, current state\n- `stepExecution`: the performance of one step within an instance; key attributes: step reference, performer, act reference, timestamps\n- `deviation`: a departure from the definition; key attributes: kind, cause, resolution, severity\n\n## Relationships\n\n- `process` -> comprises -> `step` (one-to-many): the ordered units the definition is made of\n- `step` -> performedBy -> `role` (many-to-many): which roles are eligible to execute the step\n- `processInstance` -> instanceOf -> `process` (many-to-one): the definition version being executed\n- `stepExecution` -> realizes -> `step` (many-to-one): the definitional step an execution corresponds to\n- `stepExecution` -> recordedAs -> `act` (one-to-one): each performed step is an act in K2\n- `deviation` -> departsFrom -> `process` (many-to-one): the definition the execution strayed from\n- `process` -> codifies -> `method` (many-to-one): the practice or procedure the process operationalizes\n\n## Events\n\n- `processDefined`: a new process definition or version was published\n- `instanceStarted`: an execution of a process began for a subject\n- `stepCompleted`: a step within an instance finished, with performer and outcome\n- `deviationRaised`: an execution departed from its definition and the departure was recorded\n- `instanceCompleted`: an execution reached a terminal state\n- `processRevised`: a definition was changed and a new version released\n\n## Contracts\n\n- `definitionAccess`: a consumer reads process definitions and versions, without execution data\n- `executionMonitoring`: an authorized party observes instance states and step completions for defined processes\n- `benchmarkExchange`: aggregated cycle-time and conformance measures are shared in de-identified form\n\n## Projections\n\n- `swimlaneView`: the definition arranged by role; omits execution history\n- `statusBoard`: live instances by state and age; omits step-level detail\n- `performanceDigest`: throughput, cycle time and deviation rates per version; omits individual cases\n\n## Composition\n\n- REFERENCE `world.actAction` (K2): every step execution resolves to an atomic act\n- REFERENCE `world.functionAndCapability` (K1): roles state capability requirements resolved against agent capabilities\n- REFERENCE `world.practiceMethodAndProcedure` (K6): processes operationalize codified methods and procedures\n- REFERENCE `world.organization` (O1): the process owner and the organizations supplying performers\n- imports: bpmn (ALIGN): notation and execution semantics for the process model layer\n- imports: cmmn (ALIGN): case management semantics for weakly structured workflows\n\n## Stewardship\n\nThe process owner, an organization or an individual agent, owns definitions and their instances' records. Consumers gain access through owner-granted contracts under the catalogue's ownership and access models (S1/S2), with audit via S4.\n",
    "WM-ACT-009": "# K6 Practice Method & Procedure\n\nThis meta-model describes codified ways of doing things: methods (the reasoned approach), procedures (the step-by-step instructions), the standards they implement, and the competences they demand. It is separate from process (K3) because a method is knowledge, published, versioned and adopted, whereas a process is an operationalized flow; many processes across many organizations can codify the same method.\n\n## Manifest\n\n```yaml\nmuif:\n  version: \"1.0\"\nmetaModel:\n  id: \"vercy:world:k6\"\n  csn: world.practiceMethodAndProcedure\n  version: 0.2.0\n  displayName: \"Practice Method & Procedure\"\n  description: \"Codified methods, procedures, the standards they implement and the competences they require.\"\nconformance:\n  muc: \"2.0: Conformant\"\n  mmas: A1\nnamespaces:\n  - world.practiceMethodAndProcedure\nbundles:\n  - csn: world.practiceMethodAndProcedure.codification\n    displayName: \"Codification\"\n    layers:\n      - world.practiceMethodAndProcedure.codification.methodDefinition\n      - world.practiceMethodAndProcedure.codification.procedureText\n      - world.practiceMethodAndProcedure.codification.standardReference\n  - csn: world.practiceMethodAndProcedure.applicability\n    displayName: \"Applicability\"\n    layers:\n      - world.practiceMethodAndProcedure.applicability.competenceRequirement\n      - world.practiceMethodAndProcedure.applicability.scopeOfUse\n  - csn: world.practiceMethodAndProcedure.lifecycle\n    displayName: \"Lifecycle\"\n    layers:\n      - world.practiceMethodAndProcedure.lifecycle.versioning\n      - world.practiceMethodAndProcedure.lifecycle.adoption\nimports:\n  - source: iso-management-systems\n    version: \"*\"\n  - source: iso-9001\n    version: \"*\"\n```\n\n## Bundles and layers\n\n| Bundle | Responsibility | Layers |\n|---|---|---|\n| `codification` | The documented way itself | `methodDefinition`: approach, principles and rationale Â· `procedureText`: ordered step instructions Â· `standardReference`: external norms the method implements |\n| `applicability` | Where and by whom it may be used | `competenceRequirement`: capabilities a practitioner needs Â· `scopeOfUse`: domains, conditions and limits of applicability |\n| `lifecycle` | Currency and uptake | `versioning`: editions, supersession and errata Â· `adoption`: who adopted which edition and attested conformity |\n\n## Objects\n\n- `method`: a codified approach to a class of work; key attributes: name, purpose, principles, authoring organization, domain\n- `procedure`: step-by-step instructions realizing a method; key attributes: name, preconditions, safety notes, expected result\n- `procedureStep`: one instruction; key attributes: order, action text, inputs, checks\n- `standardReference`: an external norm implemented or cited; key attributes: standard identifier, clause, relation kind\n- `competenceRequirement`: a demanded practitioner ability; key attributes: capability reference, minimum level, certification needed\n- `edition`: a published version of a method or procedure; key attributes: version, release date, change summary, status\n- `adoptionRecord`: an organization's uptake of an edition; key attributes: adopter reference, edition, date, conformity attestation\n\n## Relationships\n\n- `method` -> detailedBy -> `procedure` (one-to-many): the instructions that make the approach executable\n- `procedure` -> comprises -> `procedureStep` (one-to-many): the ordered instructions\n- `method` -> implements -> `standardReference` (many-to-many): the norms the method gives effect to\n- `method` -> requires -> `competenceRequirement` (one-to-many): who is fit to apply it\n- `edition` -> supersedes -> `edition` (one-to-one): the version lineage\n- `adoptionRecord` -> adoptedBy -> `organization` (many-to-one): the organization that took the method into use\n\n## Events\n\n- `methodPublished`: a method was released for use by its authoring organization\n- `editionReleased`: a new version of a method or procedure was issued\n- `procedureRevised`: instructions were changed within an edition cycle\n- `methodAdopted`: an organization recorded uptake of an edition\n- `methodDeprecated`: an edition or a whole method was withdrawn from recommended use\n\n## Contracts\n\n- `methodAccess`: a consumer obtains the right to read and apply a method, free or licensed, per the author's terms\n- `adoptionAttestation`: an adopter declares conformity to an edition, verifiable by third parties\n- `revisionSubscription`: an adopter receives notice of new editions, errata and deprecations\n\n## Projections\n\n- `practitionerHandbook`: the current edition's procedures for daily use; omits history and adoption data\n- `complianceMatrix`: methods mapped to the standard clauses they implement; omits procedure text\n- `trainingSyllabus`: competence requirements and steps shaped for instruction; omits versioning detail\n\n## Composition\n\n- REFERENCE `world.functionAndCapability` (K1): competence requirements resolve to capabilities and proficiency levels\n- REFERENCE `world.organization` (O1): authoring and adopting organizations\n- REFERENCE `world.processAndWorkflow` (K3): processes operationalize methods; the link is held on the process side and navigable from here\n- imports: iso-management-systems (REFERENCE): management system requirements that methods commonly implement\n- imports: iso-9001 (ALIGN): quality management vocabulary for procedures and conformity\n\n## Stewardship\n\nThe authoring organization owns each method and its editions; adopters own their adoption records. Reading and applying a method follows owner-granted contracts under the catalogue's ownership and access models (S1/S2), with audit via S4.\n"
  },
  "evidence_limits": [
    "Both candidates are reserved registry rows with described-previous-version status and migration-boundary-review state.",
    "The supplied specifications use wildcard imports and legacy K3/K6 identifiers; no executable fixtures or current publication packages were found for either candidate.",
    "Candidate properties from the Enterprise v1 registry are non-normative.",
    "Relationship-ledger rows are candidate relations and do not grant inheritance, mutation or cascade authority."
  ]
}

```

## CLAUDE STUDY

```
# EM-OPS-01 Boundary Review — Process, Procedure and Execution

## Verdict

- **WM-ACT-003 Process / Workflow — COMPLETE RESERVED MODEL.** It is the operational-flow aggregate and owns definition, variant, instance and step-execution identity. Completion is required, not a new ID.
- **WM-ACT-009 Method / Procedure — COMPLETE RESERVED MODEL.** It is the reusable knowledge artifact (method, procedure, edition, adoption). Not a duplicate of WM-ACT-003; no merge/retire.
- **ProcessInstance / ActivityExecution — no new model ID.** They stay inside WM-ACT-003's `execution` bundle. A third aggregate is not provable from this dossier: the trace has its own *lifecycle* but no independent *identity* — an instance cannot be named without a pinned definition edition. Split trigger deferred, with criteria below.
- **ProcessMethod (contour candidate type) — REUSE ONLY** as `method` in WM-ACT-009 with a domain tag. No separate type.
- **Anything beyond the two reserved rows — DEFER** pending crosswalk evidence.

## Evidence state

Both rows are `described-previous-version` / `migration-boundary-review`, `evidence_depth: index-and-publication-metadata`, `priority_confidence: low`, and both research rows are `blocked-on-providers`, `validation_status: not-valid-or-not-run`. The supplied specs carry `muc: "2.0: Conformant"` and `mmas: A1`; nothing in the dossier supports either claim, so both are treated as unsupported assertions, not evidence. Imports are wildcards (`bpmn: "*"`, `cmmn: "*"`, `iso-management-systems: "*"`, `iso-9001: "*"`) — no standards conformance, compatibility or installability is claimed here. The two relationship-ledger rows are `review_state: candidate` and grant nothing. Enterprise v1 fields (OPS-01/02/03) are `candidate-not-normative`. No fixtures exist for either candidate.

## Boundary and aggregate identities

**WM-ACT-009 owns:** `method` (approach), `procedure` and `procedureStep` (instructions), `edition` (published immutable version), `standardReference`, `competenceRequirement`, `adoptionRecord`. Its identity is *publication* identity: authored, versioned, adopted, superseded. It never owns an instance, a timestamp of work, or an outcome. It only references organizations (WM-ORG/O1) and capabilities (K1).

**WM-ACT-003 owns:** `process` (definition family), `variant`, `releasedDefinition` (the immutable triple below), `step`, `gateway`, `role`, `state`, `processInstance`, `stepExecution`, `workItem`, `deviation`. Its identity is *operational* identity. It only references a method edition in WM-ACT-009 — the link is directional and held on the process side, which both specs already agree on and which is correct: many processes in many organizations may codify one method edition.

Three boundaries need correcting in the supplied specs:

1. **Method vs procedure vs process definition.** A method is reasoning, a procedure is instruction text, a process definition is an executable flow with roles, gateways and states. The dossier's scope line is right: methodology sets rules, not a process instance. Therefore `process -> codifies -> method` must resolve to a *method edition*, never to the method family.
2. **ActivityExecution vs act (WM-ACT-002).** The K3 spec asserts `stepExecution -> recordedAs -> act (one-to-one)`. WM-ACT-002's spec is not in the dossier, so that cardinality is a hold. The defensible allocation: `stepExecution` owns the process-context identity (instance, step, variant pin, timing, performer, outcome, conformance flags) and *references* the atomic act. It does not own act identity.
3. **Task/work-item vs execution event.** Neither spec has a `workItem`. Assignment is not execution: a work item can be offered, claimed, reassigned, escalated or expire with zero `stepExecution` rows. `workItem` must be added to WM-ACT-003 as a separate object with its own state machine.

## Version/variant/adoption semantics

- **Released edition identity:** `(processId, variantKey, version)` — immutable once released. Drafts have no citable identity and no instance may reference one.
- **Version vs variant:** a new *version* supersedes along a lineage; a *variant* is a concurrently valid alternative path set under the same process family, each variant carrying its own version lineage. Two variants are not two definitions and not two versions.
- **Method edition adoption:** `adoptionRecord` stays in WM-ACT-009, owned by the adopter, and is effective from the adoption date — not from the publication date. A process pins the *edition it adopted*, resolved through the adoption record, so publishing edition 4.0 does not silently re-point live processes.
- **`procedureRevised` is a defect.** The K6 event is described as "instructions were changed within an edition cycle". That mutates a released artifact and is precisely what makes the negative case reachable. It must be retired and replaced by an errata-producing `editionReleased` with `supersedes` lineage.

## Execution and trace contract

Trace is append-only. `processInstance` pins the released-edition triple at start; each `stepExecution` re-pins the triple and the method-edition ref in force at *its* start time, so a mid-flight edition change is visible in the trace instead of rewriting it. Deviation, manual exception, escalation and compensation are all recorded as first-class facts: compensation is a new `stepExecution` linked `compensates -> stepExecution`, never a deletion or edit. Conformance is **derived**, computed over (trace, pinned edition) and materialized only in the `performanceDigest` projection — it is never stored as truth on a definition. The BPMN/CMMN model is the planned path only; an observed trace is the sole evidence of what happened. Replay is `as-of` by pinned refs and a monotonic event sequence.

Split criteria that would justify a third model ID later: trace mastership demonstrably separate from definition mastership (BPM engine vs process registry), an independent retention/erasure lifecycle, or traces citable without a resolvable definition edition. None is evidenced today.

## Invariants

1. `processInstance.definitionRef` and every `stepExecution.definitionRef` resolve to an immutable released edition triple; drafts are unreferenceable.
2. Released editions and recorded trace events are immutable; correction occurs only by new edition or new compensating event.
3. Every departure from the pinned definition is stored explicitly as a `deviation`; silence is not conformance.
4. A BPMN/CMMN model never constitutes evidence of the actual path.
5. `workItem` state changes are not `stepExecution` records, and either may exist without the other.
6. Conformance and cycle-time figures are derived projections, recomputable from pinned refs alone.
7. Method-edition effect on a process begins at adoption, not publication.

## Scenario walkthrough

**Negative — revised instruction rewrites closed history.** Procedure edition 3.0 is edited in place via `procedureRevised`, or an instance references the method *family* rather than an edition. A completed instance's steps then resolve to new instruction text, its conformance flips retroactively, and last quarter's digest changes with no event explaining it. Blocked by invariants 1, 2 and 7 plus retirement of `procedureRevised`: the change becomes edition 3.1 `supersedes` 3.0, the closed instance keeps its 3.0 pins, and replay reproduces the original result.

**Acceptance — one process, two variants, one manual exception, one new procedure edition.** Process D v2.0 releases variants A and B. Instance I1 pins (D, A, 2.0); I2 pins (D, B, 2.0). In I2 a work item is escalated and a step performed out of sequence: one `deviation` (kind `manual-exception`) plus a `compensates` execution. Mid-flight, procedure edition 4.0 is released and adopted; I1 and I2 keep 3.0 on already-started steps, later steps pin 4.0 with the adoption date recorded. Result: two separately reproducible traces, distinguishable by variant, deviation set and edition pins, with no shared mutable state.

## Migration path

1. Rename `vercy:world:k3` / `k6` and the K3/K6 spec paths to WM-ACT-003 / WM-ACT-009 identifiers; keep `legacy_alias` only.
2. Remove `muc` and `mmas` claims until independently verified; replace wildcard imports with pinned versions or drop the import.
3. Add `variant`, `releasedDefinition`, `workItem`; retire `procedureRevised`; restate conformance as derived; add `compensates`.
4. Build fixtures for the negative and acceptance scenarios, including replay-after-edition-change.
5. Only then run the APQC/BPMN, EPCIS/SCOR and AAS-PLM/EAM/WMS crosswalks, confirm mastership among BPM/ERP/WMS/PLM/EAM, and promote relations.

## Gaps and publication holds

Holds: wildcard imports; unsupported MUC 2.0 and MMAS A1 claims; both candidate relation rows (`COMPOSE -> WM-ACT-002` conflicts with the spec's REFERENCE role and would wrongly claim act identity; `REFERENCE -> WM-KNW-012` unverified); `stepExecution -> act` one-to-one cardinality pending WM-ACT-002's spec; WM-ACT-009's empty `composition_role`, `default_link_type` and `relations_ref`; no fixtures or publication packages; missing `workItem`; mutable-edition defect; unresolved mastership across BPM/ERP/WMS/PLM/EAM; `blocked-on-providers` synthesis for both rows. No publication readiness, installability, compatibility or standards conformance is asserted.

```

## GROK STUDY

```
**Verdict.** COMPLETE BOTH reserved models. No new catalogue or runtime ID. WM-ACT-009 owns method, procedure, immutable edition, competence requirements and adoption records. WM-ACT-003 owns process family, variant, immutable released definition, and — as components — instance, work item, step execution, deviation and compensation. A process references the exact adopted method edition. ProcessInstance and ActivityExecution remain 003 components; separate mastership is not proven. This is standards alignment, not a BPMN or CMMN conformance claim.

**Identity / lifecycle boundary.** Source facts: the card treats a methodology as rules of work, not a new instance. Legacy 009 (K6) already separates published knowledge from operational flow and records `editionReleased` versus `methodAdopted`. Legacy 003 (K3) already splits definition from execution and states that the gap between them is information. Neighbors that must not be remastered: WM-ACT-006 Task, WM-ORG-016 Work Assignment, WM-ACT-007 Work Order (already pins a procedure version), K2 Act.

- **009.** Identity: method-id + procedure-id + immutable edition `{id, digest, released-at, status, supersedes}`. Lifecycle of knowledge: draft → released → superseded / deprecated. Author owns editions; adopter owns AdoptionRecord `{adopter, edition, effective-from/to, attestation}`. Owns competence and scope-of-use. Fail if 009 stores running cases or observed steps.

- **003.** Identity: process-family-id + variant-id + immutable released definition `{id, digest, variant, adopted-edition-ref, released-at}`. Lifecycle of operations: family persists; variants coexist; definition versions form a supersession lineage. Fail if 003 authors procedure text or competence rules.

ProcessInstance and ActivityExecution fail the separate-aggregate test: they are `instanceOf` a 003 definition; they have no independent registrar; Task, Act and Assignment already exist as neighbors; no separate identity scheme is published. The unverified `stepExecution`↔K2-act cardinality is a 003 relation hold: if 1:N, record multiple act refs on the step component. Missing work-item structure is a 003 field gap, not a new model, and must reference 006 rather than become 006.

**Version / variant / adoption.** Version is a supersession lineage on both models. Released definitions and editions are immutable. Errata that change normative text mint a new edition, not an in-place edit. Variant is 003-only: concurrent alternative definitions of one family (standard versus express), each with its own version lineage. Variants are siblings, not predecessor/successor. Selecting a variant at start is an instance fact; changing it mid-flight is a deviation or an explicit migration event.

Adoption is effectivity. Publishing an edition does not make it applicable. A process family or variant pins the adopted edition, not “latest published.” A new adoption applies to instances that start after `effective-from`, or to in-flight instances only via an explicit cutover record. It never rewrites completed traces. BPMN engine practice is alignment only: running and completed instances stay on the version they bound.

**Assignment versus execution.** Work assignment (016 and/or 006) is who may or shall perform, including competence against 009 requirements. Observed execution (003 `stepExecution`) is who did perform, when, against which pins, with which evidence. Assignment can exist with zero execution. Execution without a surviving assignment is allowed only as a recorded deviation. Planned BPMN lane or CMMN role is definition content, not a trace. Work-item (offer/claim token) is distinct from both and stays a 003 component referencing 006.

Each instance and each step execution pins, at write time: family, variant (or explicit none), released definition id + digest, adopted method edition id + digest, adoption-record id, recorded-at. Pins are immutable on that record.

**Trace and deviation semantics.** A trace is the append-only observed record of an instance: pins + step executions + deviations + compensations. Correction is a successor event with reason, not an edit of the historical step. Deviation is an explicit departure from the pinned definition; a manual exception is a deviation kind. Compensation is an append-only response that keeps the same pins unless a remount record says otherwise.

Planned BPMN/CMMN paths do not prove actual traces. Conformance is a reproducible projection over `(pinned definition digest, pinned edition digest, observed trace)`, emitting alignment or fitness, rule-set version and execution instant. Re-running after a new edition is a new labelled projection; the historical projection stays. Do not store a floating “conformant” flag on the instance. IEEE XES / alignment practice is the public analogue, not a claimed implementation.

**Scenario results.**

*Negative — instruction update changes a completed process.* Instance I1 pins D1 / V1 / E1. Author releases E2 and D2. I1 keeps D1+V1+E1. E2 has no effect until an AdoptionRecord. Conformance of I1 remains the projection over (D1, T1). A system that mutates I1 fails the card.

*Acceptance — one family, two variants, exception, compensation, new edition.* V1 and V2 are concurrent released definitions pinning adopted E1. I1 on V1 records a manual exception and compensation; T1 stays on V1+E1. I2 on V2 yields T2 on V2+E1. After adoption of E2 and release of D3 (V1 pinning E2), I3 yields T3 on E2. T1 does not move. Recomputing “what E2 would have required of I1” is a new projection, not T1. Four reproducible artefacts; no new IDs.

**Missing fields / relations.** 009: edition digest and supersession; AdoptionRecord; competenceRequirement. 003: processFamily; variantId (absent in legacy); definition digest + adoptedEditionRef; instance pins; workItemRef → 006; stepExecution.actRefs[] → K2; append-only deviation and compensation. ConformanceResult is a 003 measurement projection, not a third model. Relation ledger must replace “latest method” with a pinned 009 edition.

**Migration steps.** Preserve both `0.2.0-legacy` assemblies as non-installable references. Open new draft versions on the same runtimes `vr.wm-act-003` and `vr.wm-act-009`. Populate the fields above. Replace wildcard imports and the circular 003↔009 require with typed REFERENCE (003 definition → 009 edition; step → K2 act; work-item → 006; assignment → 016). Add executable fixtures for the two card scenarios and for conformance replay across two editions before either runtime is installable.

**Publication blockers.** Both reserved runtimes are legacy, non-installable, and lack CRUD, roles and artifacts. Relation ledger is candidate-only. 003 has no variant object today. `stepExecution`↔act cardinality is unverified. Work-item structure is missing. Wildcard imports and unsupported BPMN/CMMN conformance claims remain. No executable fixtures. Do not invent a third process, method, instance or execution identifier.

```

## PROVIDER COMPARISON

```
# EM-OPS-01 provider comparison

+Claude and Grok independently converge on **COMPLETE BOTH RESERVED MODELS** with no new catalogue or runtime identifier. Both assign reusable authored knowledge, immutable editions, competence requirements and adoption effectivity to `vr.wm-act-009`; both assign process family, concurrent variants, released definitions, instances, work items, observed executions, deviations and compensation to `vr.wm-act-003`.

+The reconciled candidate adopts Grok's exact digest and adoption-record pins, explicit cutover for an in-flight change, plural atomic-act references, external Task and Assignment references, and reproducible immutable conformance results. It retains Claude's separation of work-item state from execution, append-only correction and compensation, and refusal of unsupported BPMN/CMMN conformance.

+No contradiction changes the boundary decision. Claude allowed later steps to bind a newly adopted edition mid-flight; Grok required explicit cutover. The candidate uses the stricter rule: an active instance changes pins only through an authorized `CutoverRecord`. `StepExecution.actRefs[]` stays zero-to-many pending the atomic-act crosswalk. Legacy assemblies remain immutable non-installable references.
+
```

## WM-ACT-003 CANDIDATE

```
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-OPS-01",
  "modelId": "WM-ACT-003",
  "registryId": "vr.wm-act-003",
  "name": "Process / Workflow",
  "version": "0.3.0-candidate.2",
  "entryKind": "aggregate",
  "status": "research-candidate",
  "purpose": "Represent immutable released operational-flow definitions and append-only instance evidence while keeping reusable procedure knowledge, task identity, assignments and atomic acts with their authoritative masters.",
  "boundary": {
    "owns": [
      "process family and concurrently valid variants",
      "immutable released definition versions",
      "steps gateways roles and state model",
      "process instances and their pinned definition references",
      "work items and assignment lifecycle",
      "step executions deviations escalations and compensations",
      "reproducible conformance projections"
    ],
    "delegates": [
      "reusable method and procedure editions to WM-ACT-009",
      "atomic act identity to WM-ACT-002 when referenced",
      "organization and performer identity to external masters",
      "policy and rule identity to external knowledge masters"
    ],
    "excludes": [
      "mutable released definitions",
      "process execution as proof of method publication",
      "assignment state as evidence of performed work",
      "BPMN or CMMN planned paths as observed trace",
      "silent retroactive conformance changes"
    ]
  },
  "objects": {
    "ProcessFamily": {
      "identity": [
        "processId"
      ],
      "required": [
        "name",
        "purpose",
        "ownerRef",
        "status"
      ]
    },
    "ProcessVariant": {
      "identity": [
        "processId",
        "variantKey"
      ],
      "required": [
        "meaning",
        "validFrom",
        "status"
      ]
    },
    "ReleasedDefinition": {
      "identity": [
        "processId",
        "variantKey",
        "version"
      ],
      "required": [
        "releasedAt",
        "contentDigest",
        "steps",
        "gateways",
        "roles",
        "stateModel",
        "methodEditionAdoptionRef",
        "status"
      ],
      "lifecycle": [
        "draft",
        "released",
        "superseded",
        "withdrawn"
      ],
      "optional": [
        "supersedesDefinitionRef",
        "withdrawnAt",
        "withdrawalReason"
      ]
    },
    "ProcessInstance": {
      "identity": [
        "instanceId"
      ],
      "required": [
        "processFamilyRef",
        "variantKeyOrNone",
        "definitionRef",
        "definitionDigest",
        "methodEditionRef",
        "methodEditionDigest",
        "adoptionRecordRef",
        "subjectRef",
        "startedAt",
        "recordedAt",
        "status"
      ],
      "optional": [
        "completedAt",
        "terminationReason",
        "cutoverRefs"
      ]
    },
    "WorkItem": {
      "identity": [
        "workItemId"
      ],
      "required": [
        "instanceId",
        "stepRef",
        "taskRef",
        "offeredAt",
        "recordedAt",
        "status"
      ],
      "optional": [
        "assignmentRef",
        "claimedAt",
        "dueAt",
        "expiredAt",
        "escalationRefs"
      ],
      "lifecycle": [
        "offered",
        "claimed",
        "assigned",
        "released",
        "completed",
        "expired",
        "cancelled"
      ]
    },
    "StepExecution": {
      "identity": [
        "executionId"
      ],
      "required": [
        "instanceId",
        "stepRef",
        "processFamilyRef",
        "variantKeyOrNone",
        "definitionRef",
        "definitionDigest",
        "methodEditionRef",
        "methodEditionDigest",
        "adoptionRecordRef",
        "startedAt",
        "recordedAt",
        "eventSequence",
        "performerRef",
        "status"
      ],
      "optional": [
        "completedAt",
        "resultRef",
        "actRefs",
        "assignmentRef",
        "correctionOfExecutionId",
        "correctionReason"
      ],
      "lifecycle": [
        "started",
        "completed",
        "failed",
        "compensated"
      ]
    },
    "Deviation": {
      "identity": [
        "deviationId"
      ],
      "required": [
        "instanceId",
        "definitionRef",
        "definitionDigest",
        "kind",
        "observedAt",
        "recordedAt",
        "reason",
        "evidenceRefs",
        "status"
      ],
      "optional": [
        "executionRef",
        "assignmentGapRef",
        "causeRef",
        "resolutionRef",
        "severity"
      ]
    },
    "Compensation": {
      "identity": [
        "compensationId"
      ],
      "required": [
        "instanceId",
        "targetExecutionRef",
        "definitionRef",
        "definitionDigest",
        "methodEditionRef",
        "methodEditionDigest",
        "recordedAt",
        "reason",
        "status"
      ],
      "optional": [
        "compensatingExecutionRefs",
        "remountRef"
      ]
    },
    "CutoverRecord": {
      "identity": [
        "cutoverId"
      ],
      "required": [
        "instanceId",
        "fromDefinitionRef",
        "fromDefinitionDigest",
        "toDefinitionRef",
        "toDefinitionDigest",
        "fromMethodEditionRef",
        "fromMethodEditionDigest",
        "toMethodEditionRef",
        "toMethodEditionDigest",
        "authorityRef",
        "reason",
        "effectiveAt",
        "recordedAt"
      ],
      "optional": [
        "affectedStepRefs"
      ]
    },
    "ConformanceResult": {
      "identity": [
        "conformanceResultId"
      ],
      "required": [
        "instanceId",
        "definitionRef",
        "definitionDigest",
        "methodEditionRef",
        "methodEditionDigest",
        "traceDigest",
        "ruleSetVersion",
        "computedAt",
        "coverage",
        "fitness",
        "alignment",
        "resultDigest",
        "counterfactual"
      ],
      "optional": [
        "gapRefs",
        "supersedesResultRef"
      ]
    }
  },
  "relations": [
    {
      "target": "vr.wm-act-009",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Pin the exact immutable method edition and adopter-owned adoption record used by a released definition and execution."
    },
    {
      "target": "vr.wm-act-006",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Reference Task identity from a work item without remastering the task."
    },
    {
      "target": "vr.wm-org-016",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Reference the authority or assignment that authorized work; execution remains observed evidence."
    },
    {
      "target": "vr.wm-act-002",
      "relation": "REFERENCE",
      "required": false,
      "cardinality": "zero-to-many pending crosswalk",
      "purpose": "Reference one or more atomic acts without transferring their identity or asserting one-to-one cardinality."
    }
  ],
  "operations": [
    {
      "id": "release-definition",
      "effect": "Issue one immutable version in a variant lineage.",
      "authority": "process owner"
    },
    {
      "id": "start-instance",
      "effect": "Create an instance pinned to one released definition.",
      "authority": "authorized initiator"
    },
    {
      "id": "offer-work",
      "effect": "Create a work item without asserting execution.",
      "authority": "workflow engine or authorized coordinator"
    },
    {
      "id": "record-execution",
      "effect": "Append observed performance with definition and method pins.",
      "authority": "authorized recorder"
    },
    {
      "id": "record-deviation",
      "effect": "Append an explicit departure or exception.",
      "authority": "authorized recorder"
    },
    {
      "id": "record-compensation",
      "effect": "Append a new execution linked to the execution it compensates.",
      "authority": "authorized coordinator"
    },
    {
      "id": "derive-conformance",
      "effect": "Compute a reproducible projection over a pinned definition and trace.",
      "authority": "authorized analyst"
    }
  ],
  "invariants": [
    "Every process instance pins process family, explicit variant or none, released-definition id and digest, method-edition id and digest, adoption-record id, and recorded-at time.",
    "Every step execution repeats its applicable family, variant, definition, method-edition, adoption and recorded-at pins.",
    "Draft definitions are not citable by instances or executions.",
    "Variants are concurrent alternatives; versions form acyclic supersession lineages within one variant.",
    "Released definitions and trace records are immutable and content-addressed.",
    "A method edition affects new instances only through an effective adoption record.",
    "An in-flight change requires an explicit authorized CutoverRecord; otherwise the original pins remain.",
    "A completed trace is never repointed by a definition, method-edition or adoption successor.",
    "A WorkItem references Task identity in vr.wm-act-006 and never becomes the Task master.",
    "Assignment and execution are separate facts; an assignment may have zero executions.",
    "Execution without a surviving applicable assignment requires an explicit deviation.",
    "A planned path never proves an observed path.",
    "Trace order is append-only and monotonic per instance.",
    "Correction is a successor execution with a reason and never mutates the historical event.",
    "Every known departure, manual exception or authorization gap is an explicit deviation.",
    "Compensation is append-only, preserves the applicable pins, and links its target execution.",
    "A remount to different pins requires an explicit CutoverRecord referenced by the compensation.",
    "StepExecution may reference zero or more atomic acts; cardinality remains a held crosswalk.",
    "Missing trace evidence yields partial or unknown coverage and never conformance pass.",
    "ConformanceResult is immutable and reproducible from definition digest, method-edition digest, trace digest and rule-set version.",
    "A counterfactual conformance replay is labelled and never replaces the historical result.",
    "No floating conformant flag is authoritative on an instance.",
    "External BPMN, CMMN and process-mining standards are alignments only until pinned crosswalk evidence exists.",
    "Publication is refused while fixturesExecuted is false, publishableCanonical is false or any release hold is open."
  ],
  "holds": [
    "The single frozen semantic audit and its one-pass remediation are pending.",
    "Legacy 0.2.0-legacy remains immutable and non-installable.",
    "CRUD, roles, artifacts and executable package conversion are absent.",
    "Relations are candidate-only until ledger approval.",
    "StepExecution-to-atomic-act cardinality and cross-system trace mastership remain unverified.",
    "External notation and standards crosswalks are alignments rather than conformance claims.",
    "Live HTTP/runtime/search/resolve/package verification is pending."
  ],
  "publishableCanonical": false,
  "legacyVersion": "0.2.0-legacy",
  "fixturesExecuted": false
}

```

## WM-ACT-009 CANDIDATE

```
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-OPS-01",
  "modelId": "WM-ACT-009",
  "registryId": "vr.wm-act-009",
  "name": "Method / Procedure",
  "version": "0.3.0-candidate.2",
  "entryKind": "knowledge-aggregate",
  "status": "research-candidate",
  "purpose": "Represent reusable authored methods and procedures, immutable editions, applicability and adopter-owned adoption records without treating publication or adoption as execution.",
  "boundary": {
    "owns": [
      "method family identity and rationale",
      "procedure identity and ordered instruction content",
      "immutable released editions and errata lineage",
      "standard and competence references",
      "scope and limits of applicability",
      "adopter-owned adoption records and effective dates"
    ],
    "delegates": [
      "operational process definitions and execution to WM-ACT-003",
      "organization identity to external masters",
      "competence and credential identity to their external masters",
      "standard identity and legal effect to external authorities"
    ],
    "excludes": [
      "process instances work items or execution outcomes",
      "in-place mutation of released instructions",
      "automatic adoption on publication",
      "claims of execution conformity",
      "wildcard standards conformance"
    ]
  },
  "objects": {
    "Method": {
      "identity": [
        "methodId"
      ],
      "required": [
        "name",
        "purpose",
        "principles",
        "authorRef",
        "domain",
        "status"
      ]
    },
    "Procedure": {
      "identity": [
        "procedureId"
      ],
      "required": [
        "methodId",
        "name",
        "preconditions",
        "expectedResult",
        "status"
      ]
    },
    "ProcedureStep": {
      "identity": [
        "procedureId",
        "stepKey"
      ],
      "required": [
        "order",
        "instruction"
      ],
      "optional": [
        "inputs",
        "checks",
        "safetyNotes"
      ]
    },
    "Edition": {
      "identity": [
        "editionId"
      ],
      "required": [
        "subjectRef",
        "version",
        "releasedAt",
        "contentDigest",
        "changeSummary",
        "status"
      ],
      "optional": [
        "supersedesEditionId",
        "erratumOfEditionId"
      ],
      "lifecycle": [
        "draft",
        "released",
        "superseded",
        "withdrawn"
      ]
    },
    "AdoptionRecord": {
      "identity": [
        "adoptionId"
      ],
      "required": [
        "adoptionId",
        "adopterRef",
        "editionId",
        "editionDigest",
        "effectiveFrom",
        "authorityRef",
        "attestationRef",
        "status"
      ],
      "optional": [
        "effectiveTo",
        "localConstraints",
        "attestationRef"
      ],
      "lifecycle": [
        "proposed",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "CompetenceRequirement": {
      "identity": [
        "editionId",
        "requirementKey"
      ],
      "required": [
        "competenceRef",
        "requiredLevel",
        "scopeOfUse"
      ],
      "optional": [
        "evidenceRuleRef",
        "validFrom",
        "validTo"
      ]
    }
  },
  "relations": [
    {
      "target": "vr.wm-act-003",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Navigate to operational definitions while the authoritative definition-to-edition binding remains process-owned."
    },
    {
      "target": "vr.wm-org-016",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Reference adopting or authoring organization identity without remastering it."
    }
  ],
  "operations": [
    {
      "id": "release-edition",
      "effect": "Issue an immutable edition or erratum with digest and lineage.",
      "authority": "authoring organization"
    },
    {
      "id": "supersede-edition",
      "effect": "Issue a successor while preserving the predecessor.",
      "authority": "authoring organization"
    },
    {
      "id": "adopt-edition",
      "effect": "Create an adopter-owned record with an effective date and authority.",
      "authority": "adopting organization"
    },
    {
      "id": "withdraw-adoption",
      "effect": "End local applicability without altering the published edition.",
      "authority": "adopting organization"
    }
  ],
  "invariants": [
    "A released edition is immutable and content-addressed.",
    "A normative correction creates an erratum or successor edition and never edits released text in place.",
    "Edition supersession lineage is acyclic.",
    "Publication does not imply adoption.",
    "Adoption takes effect on the adopter-recorded effective interval rather than publication date.",
    "An AdoptionRecord pins exactly one edition id and digest.",
    "The author owns released editions; the adopter owns its AdoptionRecord.",
    "Every effective adoption has an authority and attestation reference.",
    "Competence requirements and scope-of-use are edition-qualified.",
    "A procedure is instruction knowledge and never records work performance.",
    "A method states approach and rationale while a procedure states ordered instructions.",
    "Process definitions reference adopted editions without copying their text.",
    "Publishing a new edition never silently re-points an active or completed process.",
    "Standard and competence references do not transfer external mastership.",
    "Wildcard imports do not constitute standards conformance.",
    "Publication is refused while fixturesExecuted is false, publishableCanonical is false or any release hold is open."
  ],
  "holds": [
    "The single frozen semantic audit and its one-pass remediation are pending.",
    "Legacy 0.2.0-legacy remains immutable and non-installable.",
    "CRUD, roles, artifacts and executable package conversion are absent.",
    "Relations are candidate-only until ledger approval.",
    "External notation and standards crosswalks are alignments rather than conformance claims.",
    "Live HTTP/runtime/search/resolve/package verification is pending."
  ],
  "publishableCanonical": false,
  "legacyVersion": "0.2.0-legacy",
  "fixturesExecuted": false
}

```

## FIXTURES

```
{
  "format": "vercy-world-model-fixtures/v1",
  "contourId": "EM-OPS-01",
  "declarativeOnly": true,
  "cases": [
    {
      "id": "two-concurrent-variants",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "Two instances pin sibling variants A and B.",
      "expect": "Both traces replay independently; neither variant supersedes the other."
    },
    {
      "id": "definition-supersession",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "D2 supersedes D1 in variant A.",
      "expect": "D1 instances retain D1; new starts may pin D2."
    },
    {
      "id": "assignment-without-execution",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "A WorkItem references Task T and Assignment A, then expires.",
      "expect": "No execution or atomic act is inferred."
    },
    {
      "id": "execution-without-assignment",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "A step is recorded with no surviving assignment and no deviation.",
      "expect": "Rejected until an explicit authorization-gap deviation is appended."
    },
    {
      "id": "execution-with-deviation",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "A step is recorded after assignment evidence was lost, with a deviation.",
      "expect": "Execution remains observed evidence and the authorization gap stays explicit."
    },
    {
      "id": "one-step-many-acts",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "One step execution references two atomic acts.",
      "expect": "Both act references are retained without transferring identity."
    },
    {
      "id": "work-item-task-mastership",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "A work item attempts to create a local Task master.",
      "expect": "Rejected; it must reference vr.wm-act-006."
    },
    {
      "id": "manual-exception-compensation",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "An out-of-sequence step has a manual-exception deviation and compensation.",
      "expect": "All records append and replay with original pins."
    },
    {
      "id": "compensation-remount-without-cutover",
      "kind": "negative",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "Compensation changes definition and edition pins without a CutoverRecord.",
      "expect": "Rejected."
    },
    {
      "id": "compensation-with-cutover",
      "kind": "positive",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "Compensation changes pins and references an authorized CutoverRecord.",
      "expect": "Both pin regimes remain reproducible."
    },
    {
      "id": "retroactive-instruction-update",
      "kind": "negative",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "Released edition E1 is edited after completed I1.",
      "expect": "Rejected; issue E2 and preserve I1 pins."
    },
    {
      "id": "publication-without-adoption",
      "kind": "negative",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "E2 is published but not adopted.",
      "expect": "New and existing instances keep the prior effective adoption."
    },
    {
      "id": "new-instance-after-adoption",
      "kind": "positive",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "E2 adoption is effective before I3 starts.",
      "expect": "I3 pins E2 and its AdoptionRecord."
    },
    {
      "id": "mid-flight-change-without-cutover",
      "kind": "negative",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "An active instance silently switches from E1/D1 to E2/D2.",
      "expect": "Rejected."
    },
    {
      "id": "mid-flight-cutover",
      "kind": "positive",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "An authorized CutoverRecord moves remaining steps to E2/D2.",
      "expect": "Past steps keep old pins and later steps carry new pins."
    },
    {
      "id": "planned-path-is-not-trace",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "A planned branch has no observed event.",
      "expect": "No traversal claim is produced."
    },
    {
      "id": "missing-trace-conformance",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "Trace coverage is incomplete.",
      "expect": "ConformanceResult coverage is partial or unknown, never pass."
    },
    {
      "id": "historical-conformance",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "I1 is assessed against pinned D1/E1 and trace digest T1.",
      "expect": "Immutable result records rule-set version and computedAt."
    },
    {
      "id": "counterfactual-conformance",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "I1 is re-evaluated against successor D2/E2.",
      "expect": "A counterfactual labelled result is added and historical result remains."
    },
    {
      "id": "floating-conformance-flag",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "Instance carries conformant=true without digests.",
      "expect": "Rejected as non-reproducible."
    },
    {
      "id": "event-correction",
      "kind": "positive",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "An incorrect execution gets a successor correction with reason.",
      "expect": "Original remains; successor is ordered after it."
    },
    {
      "id": "event-in-place-edit",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "A recorder changes a completed execution timestamp.",
      "expect": "Rejected; append a correction successor."
    },
    {
      "id": "adoption-without-attestation",
      "kind": "negative",
      "targets": [
        "WM-ACT-003",
        "WM-ACT-009"
      ],
      "input": "An adoption is effective with no authority or attestation.",
      "expect": "Rejected."
    },
    {
      "id": "standards-claim",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "Candidate asserts BPMN/CMMN conformance from wildcard imports.",
      "expect": "Rejected; keep alignment-only language."
    },
    {
      "id": "legacy-installability",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "0.2.0-legacy is marked installable.",
      "expect": "Rejected; legacy remains immutable non-installable reference."
    },
    {
      "id": "release-gate",
      "kind": "negative",
      "targets": [
        "WM-ACT-003"
      ],
      "input": "Candidate is promoted while fixturesExecuted=false.",
      "expect": "Publication refused."
    }
  ]
}

```
