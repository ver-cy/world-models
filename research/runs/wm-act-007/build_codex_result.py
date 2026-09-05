#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-ACT-007."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED_AT = "2026-09-06T00:00:00Z"


SOURCES = [
    {
        "id": "SRC-001",
        "title": "ANSI/ISA-95.00.05-2018 preview: Business-to-Manufacturing Transactions",
        "organization": "International Society of Automation",
        "url": "https://www.isa.org/getmedia/bbc0eb3e-d047-440d-88fc-642b14bd8d40/ISA-95-00-05-2018-preview.pdf",
        "version_or_date": "2018 preview",
        "source_type": "standard",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Defines transaction and information-model boundaries around work schedules, work performance and work records.",
    },
    {
        "id": "SRC-002",
        "title": "ISA-95 Standard overview",
        "organization": "International Society of Automation",
        "url": "https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard",
        "version_or_date": "current page accessed 2026-09-06",
        "source_type": "first-party-doc",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Establishes the enterprise-control integration scope in which work-order information is exchanged.",
    },
    {
        "id": "SRC-003",
        "title": "OPC UA for ISA-95, Part 4: Job Control",
        "organization": "OPC Foundation",
        "url": "https://reference.opcfoundation.org/specs/OPC-10031-4/4.1",
        "version_or_date": "OPC 10031-4, section 4.1",
        "source_type": "standard",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Defines job-order control concepts, parameters, resource requirements and state-oriented interfaces aligned with ISA-95.",
    },
    {
        "id": "SRC-004",
        "title": "PLCS WorkOrder template",
        "organization": "OASIS Open",
        "url": "https://docs.oasis-open.org/plcs/plcslib/v1.0/cs01/data/contexts/OASIS/templates/WorkOrder/template.html",
        "version_or_date": "PLCSlib 1.0 CS01",
        "source_type": "schema",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Models a work order as authority to undertake work with classification, issue date and unique identity.",
    },
    {
        "id": "SRC-005",
        "title": "PLCS concept model definitions",
        "organization": "OASIS Open",
        "url": "https://docs.oasis-open.org/plcs/plcslib/v1.0/cs01/data/PLCS/concept_model/model_definitions.html",
        "version_or_date": "PLCSlib 1.0 CS01",
        "source_type": "ontology",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Separates a work request from the authority and commitment represented by a work order.",
    },
    {
        "id": "SRC-006",
        "title": "PLCS Aviation Maintenance DEX information model",
        "organization": "OASIS Open",
        "url": "https://docs.oasis-open.org/plcs/dexlib/R1/dexlib/data/dex/aviation_maintenance/sys/plcs_info_model.htm",
        "version_or_date": "DEXlib R1",
        "source_type": "schema",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Shows the maintenance-domain binding between authorization, reportable items, task references and resulting records.",
    },
    {
        "id": "SRC-007",
        "title": "PLCS Referencing Task template",
        "organization": "OASIS Open",
        "url": "https://docs.oasis-open.org/plcs/dexlib/cs01/data/templates/referencing_task/sys/section.htm",
        "version_or_date": "DEXlib CS01",
        "source_type": "schema",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Provides the versioned external-task-reference boundary used instead of copying procedure semantics into an order.",
    },
    {
        "id": "SRC-008",
        "title": "UN/EDIFACT Job Order message (JOBOFF)",
        "organization": "United Nations Economic Commission for Europe",
        "url": "https://unece.org/fileadmin/DAM/trade/untdid/d97b/trmd/joboff_c.htm",
        "version_or_date": "UN/EDIFACT D.97B",
        "source_type": "standard",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Supplies a cross-organizational job-order message precedent for identity, parties, dates, references and line-level instructions.",
    },
]


# bundle id/name/description/rationale/sources, followed by layers and findings.
STRUCTURE = [
    (
        "authority-and-origin", "Authority and origin",
        "Establishes what the order is, why it exists and who is empowered to issue it.",
        "An executable work instruction must be distinguishable from a request and traceable to an authorized issuer.",
        ["SRC-004", "SRC-005", "SRC-008"],
        [
            ("order-identity", "Order identity", "Stable identity and classification of the governed order.", ["SRC-004", "SRC-008"], [
                ("authoritative-identity", "Authoritative identity", "The master-system identifier, aliases and revision-qualified identity of the work order.", "identity", ["SRC-004", "SRC-008"], "identifier", True),
                ("classification-and-kind", "Classification and kind", "The governed order class, profile and criteria that distinguish this order from neighboring instruction types.", "classification", ["SRC-004", "SRC-005"], "code", False),
            ]),
            ("request-and-rationale", "Request and rationale", "The initiating demand and reason for converting it into authorized work.", ["SRC-005", "SRC-008"], [
                ("originating-request", "Originating request", "Reference to the demand, request or triggering condition from which the order was derived.", "relationship", ["SRC-005", "SRC-008"], "reference", False),
                ("business-or-operational-rationale", "Business or operational rationale", "The stated need, risk, obligation or desired benefit that justifies ordering the work.", "decision", ["SRC-001", "SRC-005"], "text", False),
            ]),
            ("authorization", "Authorization", "The issuer's authority, effective scope and limitations.", ["SRC-004", "SRC-006"], [
                ("issuing-authority", "Issuing authority", "The person, organization or delegated role that issued the authoritative revision and the basis of that authority.", "authority", ["SRC-004", "SRC-006"], "reference", True),
                ("authorization-scope", "Authorization scope", "The work, targets, resources, period and limits covered by the issued authority.", "constraint", ["SRC-004", "SRC-006"], "object", True),
            ]),
        ],
    ),
    (
        "ordered-work-definition", "Ordered work definition",
        "Defines the authorized scope, intended outcome, task composition and target context.",
        "The order owns the instruction envelope while task, procedure, asset and location semantics stay in referenced models.",
        ["SRC-001", "SRC-003", "SRC-006", "SRC-007"],
        [
            ("scope-and-outcome", "Scope and outcome", "Authorized inclusions, exclusions and expected result.", ["SRC-001", "SRC-004"], [
                ("authorized-scope", "Authorized scope", "The explicit work boundary, including included and excluded activities and affected subjects.", "composition", ["SRC-001", "SRC-004"], "object", True),
                ("required-outcome", "Required outcome", "The deliverable, condition or service level that the authorized work is expected to produce.", "requirement", ["SRC-001", "SRC-003"], "object", True),
            ]),
            ("task-composition", "Task composition", "Contained task references and immutable work-master bindings.", ["SRC-003", "SRC-006", "SRC-007"], [
                ("contained-task-references", "Contained task references", "Ordered references to tasks with order-local parameters and dependency bindings, without importing task execution state.", "composition", ["SRC-003", "SRC-006"], "collection", False),
                ("procedure-or-work-master-reference", "Procedure or work-master reference", "A pinned reference to the approved procedure, recipe or work-master version governing execution.", "interoperability", ["SRC-003", "SRC-007"], "reference", False),
            ]),
            ("target-context", "Target context", "The affected subject and the operational place in which the instruction applies.", ["SRC-003", "SRC-006", "SRC-008"], [
                ("subject-or-target-reference", "Subject or target reference", "Reference to the asset, product, case, service or other object whose state or condition is to be changed.", "relationship", ["SRC-003", "SRC-006"], "reference", True),
                ("location-and-operational-context", "Location and operational context", "Applicable site, functional location, hierarchy boundary and operating conditions relevant to execution.", "spatial", ["SRC-003", "SRC-008"], "object", False),
            ]),
        ],
    ),
    (
        "planning-and-constraints", "Planning and constraints",
        "Captures order-level priority, timing, dependencies and mandatory controls.",
        "These commitments constrain planning and release but do not replace a detailed schedule or an external permit-enforcement system.",
        ["SRC-001", "SRC-003", "SRC-008"],
        [
            ("priority-and-time", "Priority and time", "Priority, criticality and authorized planning window.", ["SRC-001", "SRC-003", "SRC-008"], [
                ("priority-and-criticality", "Priority and criticality", "The ranked urgency, consequence class and authority responsible for prioritization or escalation.", "classification", ["SRC-001", "SRC-003"], "code", False),
                ("planned-window-and-deadline", "Planned window and deadline", "Earliest and latest start, due time, commitment window and the timezone basis for those values.", "temporal", ["SRC-001", "SRC-008"], "object", False),
            ]),
            ("dependencies-and-holds", "Dependencies and holds", "Predecessors, release conditions, permits and quality or safety gates.", ["SRC-001", "SRC-003", "SRC-006"], [
                ("predecessors-and-blockers", "Predecessors and blockers", "Referenced orders, tasks, events or conditions that must be satisfied before release or continuation.", "relationship", ["SRC-001", "SRC-003"], "collection", False),
                ("permit-safety-quality-constraints", "Permit, safety and quality constraints", "Applicable permits, isolations, safety controls, inspection points and quality gates bound to the order.", "security", ["SRC-003", "SRC-006"], "collection", False),
            ]),
        ],
    ),
    (
        "resource-requirements", "Resource requirements",
        "Defines responsibility and the capabilities, equipment, materials and commercial bounds required by the order.",
        "The order records requirements and bindings while referenced people, inventory, equipment, contracts and cost ledgers remain authoritative for their own data.",
        ["SRC-001", "SRC-003", "SRC-006", "SRC-008"],
        [
            ("responsibility", "Responsibility", "Accountability, assignment and acknowledgement.", ["SRC-001", "SRC-003", "SRC-008"], [
                ("responsible-party", "Responsible party", "The accountable organizational unit, role or party for delivery and order administration.", "ownership", ["SRC-001", "SRC-008"], "reference", True),
                ("assignment-and-acknowledgement", "Assignment and acknowledgement", "Assignee references and their time-stamped acceptance, refusal or reassignment response.", "event", ["SRC-003", "SRC-008"], "collection", False),
            ]),
            ("required-resources", "Required resources", "Capabilities and consumable or reusable resources needed for execution.", ["SRC-001", "SRC-003", "SRC-006"], [
                ("personnel-capability-requirements", "Personnel capability requirements", "Required roles, competencies, certifications, quantities and availability constraints without duplicating worker records.", "requirement", ["SRC-001", "SRC-003"], "collection", False),
                ("equipment-material-asset-requirements", "Equipment, material and asset requirements", "Required equipment classes, tools, materials, quantities, units and reservation references.", "measurement", ["SRC-001", "SRC-003", "SRC-006"], "collection", False),
            ]),
            ("commercial-bounds", "Commercial bounds", "Estimated effort, authorized cost bounds and governing agreements.", ["SRC-001", "SRC-008"], [
                ("estimated-effort-and-cost-bound", "Estimated effort and cost bound", "Order-level estimates, ceilings, currencies, approval thresholds and uncertainty, not a replacement for cost transactions.", "measurement", ["SRC-001", "SRC-008"], "object", False),
                ("service-contract-reference", "Service contract reference", "Pinned reference to the agreement, entitlement, warranty or service level governing the ordered work.", "relationship", ["SRC-001", "SRC-008"], "reference", False),
            ]),
        ],
    ),
    (
        "lifecycle-and-change-control", "Lifecycle and change control",
        "Governs administrative state, release, revisions, suspension, cancellation and exceptions.",
        "Issued meaning and authority must be historically reconstructable, and order state must not be confused with evidence that work occurred.",
        ["SRC-001", "SRC-003", "SRC-004", "SRC-008"],
        [
            ("order-state", "Order state", "Administrative lifecycle state and dispatch interface.", ["SRC-001", "SRC-003", "SRC-008"], [
                ("lifecycle-state", "Lifecycle state", "The current administrative state, allowed transition, responsible actor and effective transition event.", "state", ["SRC-001", "SRC-003"], "code", True),
                ("release-and-dispatch", "Release and dispatch", "The controlled release to an execution context, dispatch destination and acknowledgement reference.", "process", ["SRC-003", "SRC-008"], "object", False),
            ]),
            ("change-control", "Change control", "Immutable revisions and controlled termination or temporary inhibition.", ["SRC-003", "SRC-004"], [
                ("revision-and-supersession", "Revision and supersession", "Revision identity, changed scope, reason, approver and explicit predecessor or successor relation.", "lifecycle", ["SRC-003", "SRC-004"], "object", True),
                ("suspension-cancellation-and-expiry", "Suspension, cancellation and expiry", "Authority, reason, time and residual obligations when authorization is paused, withdrawn or expires.", "lifecycle", ["SRC-003", "SRC-004"], "object", False),
            ]),
            ("exception-management", "Exception management", "Deviation, escalation and conflicting-order handling.", ["SRC-001", "SRC-003", "SRC-008"], [
                ("deviation-and-escalation", "Deviation and escalation", "Requested or approved deviations, unresolved blockers, escalation paths and disposition deadlines.", "exception", ["SRC-001", "SRC-003"], "collection", False),
                ("conflict-and-duplicate-resolution", "Conflict and duplicate resolution", "Relations to duplicate or contradictory orders and the authoritative resolution decision.", "decision", ["SRC-003", "SRC-008"], "collection", False),
            ]),
        ],
    ),
    (
        "acceptance-closure-and-governance", "Acceptance, closure and governance",
        "Connects completion evidence to acceptance and closure while preserving provenance, ownership, access and retention controls.",
        "Completion is an external claim until evaluated against declared criteria; the order retains its decision and references instead of absorbing performed-work evidence.",
        ["SRC-001", "SRC-003", "SRC-006", "SRC-008"],
        [
            ("completion-interface", "Completion interface", "References to performed work and the criteria for acceptance.", ["SRC-001", "SRC-003", "SRC-006"], [
                ("completion-claim-reference", "Completion claim reference", "Reference to a work-performance, work-record or completion claim and the issuer and time of that claim.", "evidence", ["SRC-001", "SRC-003", "SRC-006"], "reference", False),
                ("acceptance-criteria", "Acceptance criteria", "Measurable conditions, tolerances, evidence requirements and verifier authority used to evaluate completion.", "validation", ["SRC-001", "SRC-003"], "collection", True),
            ]),
            ("closure-and-disposition", "Closure and disposition", "Acceptance decision, rejection, rework and final retention disposition.", ["SRC-001", "SRC-003", "SRC-008"], [
                ("acceptance-or-rejection", "Acceptance or rejection", "The authorized evaluation decision, defects, exceptions and referenced corrective or rework order.", "decision", ["SRC-001", "SRC-003"], "object", False),
                ("closure-and-retention", "Closure and retention", "Closure reason, unresolved obligations, retention class, legal hold and tombstone or erasure authority.", "retention", ["SRC-001", "SRC-008"], "object", True),
            ]),
            ("evidence-and-access", "Evidence and access", "Provenance, quality, ownership, disclosure and scoped access.", ["SRC-001", "SRC-004", "SRC-008"], [
                ("provenance-and-quality", "Provenance and quality", "Source lineage, capture method, freshness, confidence and validation results for order facts and attached evidence.", "provenance", ["SRC-001", "SRC-004"], "object", True),
                ("ownership-disclosure-and-access", "Ownership, disclosure and access", "Record owner, stewardship, delegated writers, disclosure policy, access scopes and approved exceptions.", "access", ["SRC-001", "SRC-008"], "object", True),
            ]),
        ],
    ),
]


QUESTION_KIND_CYCLE = [
    "definition", "identity", "classification", "composition", "relationship", "state",
    "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority",
    "requirement", "constraint", "process", "event", "measurement", "evidence",
    "quality", "validation", "security", "retention", "access", "exception",
    "interoperability", "decision",
]


def build_finding(raw: tuple, ordinal: int) -> dict:
    finding_id, name, description, primary_kind, refs, value_kind, required = raw
    kinds = [primary_kind, QUESTION_KIND_CYCLE[(ordinal * 3 + 5) % len(QUESTION_KIND_CYCLE)], QUESTION_KIND_CYCLE[(ordinal * 5 + 11) % len(QUESTION_KIND_CYCLE)]]
    # Preserve three distinct kinds in the unlikely event that the cycle lands on the primary kind.
    for position in range(1, 3):
        while kinds[position] in kinds[:position]:
            kinds[position] = QUESTION_KIND_CYCLE[(QUESTION_KIND_CYCLE.index(kinds[position]) + 1) % len(QUESTION_KIND_CYCLE)]
    questions = [
        {
            "id": f"{finding_id}-q01",
            "text": f"What is the governed value of {name.lower()} for this work order?",
            "kind": kinds[0],
            "answer_data": [name, "applicable qualifier or explicit unknown", "source and effective version"],
        },
        {
            "id": f"{finding_id}-q02",
            "text": f"Who or what authoritative source establishes {name.lower()} for this work order?",
            "kind": kinds[1],
            "answer_data": ["authority or source reference", "effective timestamp", "provenance and confidence"],
        },
        {
            "id": f"{finding_id}-q03",
            "text": f"How is {name.lower()} validated, changed and historically preserved?",
            "kind": kinds[2],
            "answer_data": ["validation rule", "authorized change event", "prior-value or supersession reference"],
        },
    ]
    return {
        "id": finding_id,
        "name": name,
        "description": description,
        "source_refs": refs,
        "questions": questions,
        "data_elements": [{
            "id": f"{finding_id}-data",
            "name": f"{name} record",
            "description": f"Structured answer data for {name.lower()}, including authority, effective time and provenance where applicable.",
            "value_kind": value_kind,
            "cardinality": "1" if required else "0..1",
            "required": required,
            "source_refs": refs,
        }],
        "artifacts": [{
            "id": f"{finding_id}-artifact",
            "name": f"{name} evidence",
            "description": f"Versioned evidence or authoritative reference supporting the recorded {name.lower()}.",
            "media_or_form": ["structured record", "signed or controlled document", "resolvable external reference"],
            "serial": True,
            "identity_strategy": "Authoritative master-system identifier first; otherwise a Dimension-governed UUID or ULID.",
            "source_refs": refs,
        }],
        "inline_only_rationale": None,
    }


def build_structure() -> dict:
    bundles = []
    ordinal = 0
    for bundle_id, name, description, rationale, refs, layer_rows in STRUCTURE:
        layers = []
        for layer_id, layer_name, layer_description, layer_refs, findings in layer_rows:
            built_findings = []
            for finding in findings:
                ordinal += 1
                built_findings.append(build_finding(finding, ordinal))
            layers.append({
                "id": layer_id,
                "name": layer_name,
                "description": layer_description,
                "source_refs": layer_refs,
                "findings": built_findings,
            })
        bundles.append({
            "id": bundle_id,
            "name": name,
            "description": description,
            "rationale": rationale,
            "source_refs": refs,
            "layers": layers,
        })
    return {"bundles": bundles}


FUNCTIONS = [
    ("create-draft-order", "Create draft order", "Establish a proposed order identity, origin and scope without granting authority.", ["request reference", "proposed scope", "draft owner"], ["draft work order"], ["request or authorized drafting purpose exists"], ["a traceable but non-authorized order draft exists"], ["SRC-004", "SRC-005"]),
    ("validate-order-boundary", "Validate order boundary", "Check required order facts, external references and separation from request, procedure and execution records.", ["work order revision", "validation profile"], ["validation report"], ["order revision is resolvable"], ["boundary, reference and semantic failures are recorded"], ["SRC-001", "SRC-003", "SRC-005"]),
    ("authorize-order", "Authorize order", "Issue an immutable revision under a verified authority and effective scope.", ["validated draft", "issuer authority", "effective time"], ["authorized order revision"], ["validation passed", "issuer authority is current"], ["authorization event and immutable issued meaning are recorded"], ["SRC-004", "SRC-006"]),
    ("release-order", "Release order", "Expose an authorized revision to its declared dispatch or execution context.", ["authorized order", "dispatch destination"], ["release event", "dispatch reference"], ["order is authorized", "release constraints are satisfied"], ["order becomes available to the declared execution context"], ["SRC-001", "SRC-003", "SRC-008"]),
    ("revise-order", "Revise order", "Create a traceable successor without overwriting an issued revision.", ["current revision", "change request", "approver"], ["successor revision", "change record"], ["change authority is valid"], ["old and new meaning remain reconstructable"], ["SRC-003", "SRC-004"]),
    ("suspend-or-resume-order", "Suspend or resume order", "Temporarily inhibit or restore administrative availability under named authority and reason.", ["order", "transition request", "authority"], ["state-transition event"], ["transition is allowed", "authority is valid"], ["administrative availability changes without erasing history"], ["SRC-001", "SRC-003"]),
    ("cancel-order", "Cancel order", "Withdraw remaining authorization while preserving evidence and residual obligations.", ["order", "cancellation reason", "authority"], ["cancellation event", "residual-obligation record"], ["cancellation policy permits the transition"], ["future authorization ends and historical references remain resolvable"], ["SRC-003", "SRC-004"]),
    ("record-completion-claim", "Record completion claim", "Bind external performed-work evidence without silently asserting acceptance.", ["work order", "performed-work reference", "claiming party"], ["completion-claim binding"], ["external evidence is resolvable"], ["completion claim becomes reviewable separately from order state"], ["SRC-001", "SRC-003", "SRC-006"]),
    ("accept-or-reject-result", "Accept or reject result", "Evaluate referenced evidence against the issued acceptance criteria and record the authorized decision.", ["order", "completion claim", "acceptance evidence"], ["acceptance decision"], ["criteria and verifier authority are explicit"], ["accepted, rejected or conditional disposition is recorded"], ["SRC-001", "SRC-003"]),
    ("close-order", "Close order", "Finalize disposition, unresolved exceptions and retention metadata after an authorized decision.", ["order", "acceptance decision", "retention class"], ["closure event", "retention disposition"], ["closure prerequisites are satisfied"], ["order is closed but its identity, history and references remain governed"], ["SRC-001", "SRC-008"]),
]


def build() -> dict:
    return {
        "schema_version": "1.0.0",
        "model": {
            "registry_id": "vr.wm-act-007",
            "model_id": "WM-ACT-007",
            "name": "Work Order",
            "entry_kind": "aggregate",
            "purpose": "Represent an authoritative, versioned instruction that authorizes and constrains one or more units of work while preserving boundaries to requests, procedures, schedules and performed-work evidence.",
            "scope_statement": "Owns order identity, authorization, scope, requirements, administrative lifecycle, change control, acceptance criteria and closure disposition; references execution and domain records governed elsewhere.",
            "in_scope": [
                "Order identity, class, authority, scope, requirements, constraints and order-level planning commitments",
                "Administrative state transitions, revisions, cancellation, acceptance decision, closure and governance metadata",
                "Typed references to tasks, procedures, targets, resources, contracts, schedules and performed-work evidence",
            ],
            "out_of_scope": [
                "Task execution semantics, detailed scheduling, inventory transactions, cost accounting, access enforcement and proof that physical work occurred",
                "Lifecycle ownership of referenced assets, people, organizations, locations, contracts, procedures or evidence records",
            ],
            "boundary_notes": [
                {"neighbor": "Work request", "distinction": "A request proposes or demands work and can be rejected; a work order is an authorized instruction with controlled scope and lifecycle.", "source_refs": ["SRC-004", "SRC-005"]},
                {"neighbor": "Task or procedure", "distinction": "The order may contain task references and pin procedure versions, but task execution semantics and reusable instructions remain in their own models.", "source_refs": ["SRC-003", "SRC-006", "SRC-007"]},
                {"neighbor": "Work performance or work record", "distinction": "A work order authorizes work; performed-work records and evidence establish what actually happened and are only referenced here.", "source_refs": ["SRC-001", "SRC-003"]},
                {"neighbor": "Schedule", "distinction": "The order may carry windows and commitments, but resource-level sequencing and calendar optimization belong to a schedule model.", "source_refs": ["SRC-001", "SRC-003"]},
            ],
        },
        "sources": SOURCES,
        "structure": build_structure(),
        "functions": [
            {"id": row[0], "name": row[1], "description": row[2], "inputs": row[3], "outputs": row[4], "preconditions": row[5], "effects": row[6], "source_refs": row[7]}
            for row in FUNCTIONS
        ],
        "composition": [
            {"target": "WM-ACT-006 Task", "relation": "COMPOSE", "purpose": "Groups typed task references and order-local parameters without claiming ownership of task execution semantics.", "required": False, "source_refs": ["SRC-003", "SRC-006"]},
            {"target": "Procedure or work-master model", "relation": "REFERENCE", "purpose": "Pins the executable instruction version while keeping reusable procedure content outside the order.", "required": False, "source_refs": ["SRC-003", "SRC-007"]},
            {"target": "Schedule or calendar model", "relation": "REFERENCE", "purpose": "Delegates detailed sequencing and capacity allocation while retaining order-level timing commitments.", "required": False, "source_refs": ["SRC-001", "SRC-003"]},
            {"target": "Asset, location, person, organization, material and inventory models", "relation": "REFERENCE", "purpose": "Uses authoritative domain identities without copying their properties or lifecycles.", "required": True, "source_refs": ["SRC-003", "SRC-006", "SRC-008"]},
            {"target": "Contract, entitlement and cost models", "relation": "REFERENCE", "purpose": "Binds governing agreements and commercial limits without turning the order into a ledger.", "required": False, "source_refs": ["SRC-001", "SRC-008"]},
            {"target": "Performed-work and evidence models", "relation": "REFERENCE", "purpose": "Separates authorization from claims and proof of actual execution.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-006"]},
            {"target": "ISA-95, OPC UA ISA-95, PLCS and UN/EDIFACT concepts", "relation": "ALIGN", "purpose": "Maintains documented semantic mappings without claiming conformance to any one implementation profile.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-008"]},
        ],
        "service_layers": {
            "dimension": {
                "owner_package_requirements": [
                    "Declare the Dimension owner, accountable stewards and authority delegation chain.",
                    "Declare the Dimension namespace, identity master systems and authoritative work-order repository.",
                    "Publish registries for models, objects, events and relation types plus applicable retention and access policies.",
                    "Pin this model version and any jurisdictional or industry profile used for validation.",
                ],
                "namespace_guidance": "Mint identifiers only inside the adopting Dimension's governed namespace; preserve upstream master-system identifiers and aliases without silently re-keying them.",
                "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local model, object and event registries"],
            },
            "canon_and_patch": {
                "canonicalization_rules": [
                    "Canonicalize by registry ID, model version, stable node IDs and explicit value units; never infer execution from administrative order state.",
                    "Issued revisions are immutable and superseded by linked successors rather than overwritten.",
                ],
                "patch_rules": [
                    "Additive extensions use a Dimension-owned namespace and declare their target bundle, layer, finding or artifact plus source and rationale.",
                    "Breaking changes require a new model version, migration mapping, compatibility declaration and preserved access to prior versions.",
                ],
                "compatibility_rules": [
                    "Consumers ignore unknown additive fields only when required semantics and access controls remain intact.",
                    "Mappings to external job or work-order schemas must declare lossy fields, code-list versions and timezone handling.",
                ],
            },
            "artifact_rules": {
                "identity_priority": [
                    "Authoritative master-system work-order identifier and immutable issued-revision identifier.",
                    "Governed globally resolvable IRI or federation identifier.",
                    "Adopting-Dimension UUID or ULID when no authoritative external identifier exists.",
                ],
                "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep event, effective, observation and ingestion times distinct.",
                "serial_naming_rule": "Name serial artifacts as {order-id}--{artifact-kind}--{revision-or-event-id}; never use a date alone as identity.",
                "integrity_rule": "Store a cryptographic digest, media type, byte length, issuer, provenance and immutable version reference for every retained serial artifact.",
            },
            "policies": [
                "The adopting Dimension defines who may draft, authorize, release, revise, cancel, accept and close each order class.",
                "Facts, hypotheses and unknown values remain explicitly distinct and carry source, observation time and confidence where applicable.",
                "Safety, privacy, commercial confidentiality, export control and legal-hold policies are evaluated before disclosure or mutation.",
                "External references are resolved by pinned identity and version, with stale, missing or lossy bindings reported rather than guessed.",
            ],
            "crud": {
                "read": ["Resolve the model version, owner policy and referenced master systems; apply field- and artifact-level access rules and record material reads where policy requires."],
                "create": ["Create a draft only under an authorized purpose, allocate identity by priority, validate required boundary facts and keep it non-executable until an authorization event."],
                "update": ["Create an immutable successor revision for issued meaning, record actor, authority, reason and effective time, and validate references and transitions before and after the change."],
                "delete": ["Apply retention, legal-hold and deletion policy; tombstone issued orders or use approved cryptographic erasure while preserving minimum identity and non-cascading reference integrity."],
            },
            "roles": [
                {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, retention, access and delegation policy for work-order records."]},
                {"name": "Order issuer", "responsibilities": ["Authorize scope and effective revision within documented authority."]},
                {"name": "Order steward", "responsibilities": ["Maintain classification, references, lifecycle integrity and conflict resolution."]},
                {"name": "Assignee or executing party", "responsibilities": ["Acknowledge assignment and publish execution claims to the proper performed-work model."]},
                {"name": "Verifier or acceptor", "responsibilities": ["Evaluate evidence against acceptance criteria and record an authorized disposition."]},
                {"name": "Auditor", "responsibilities": ["Review provenance, authorization, access, changes, retention and unresolved exceptions without editing operational truth."]},
            ],
            "access": {
                "default_rule": "Deny mutation and restricted disclosure unless the active Dimension, role and order-class policy grants the action; expose only the minimum authorized projection.",
                "scopes": ["bundle", "layer", "finding", "artifact"],
                "exceptions": ["Emergency access must be time-limited, purpose-bound, attributable, independently reviewed and must not bypass legal hold or immutable history."],
                "audit_requirements": ["Log actor, role, purpose, order and revision identity, action, decision, policy version, timestamp with offset, affected scope and result for every privileged mutation or disclosure."],
            },
            "agents_bootstrap": {
                "filename": "AGENTS.md",
                "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
                "read_order": ["Read the nearest Dimension-owner AGENTS.md and policies.", "Read this model AGENTS.md, then the pinned spec.yaml and all referenced model contracts before mutation."],
            },
        },
        "coverage": {
            "claim": "Source-grounded, cross-domain reviewable draft covering the authoritative Work Order envelope across maintenance, manufacturing and inter-organizational exchange, with profile-specific state vocabularies intentionally delegated.",
            "confidence": "medium",
            "checklist": [
                {"dimension": "identity", "status": "covered", "notes": "Authoritative identity, aliases, revision identity and namespace priority are explicit."},
                {"dimension": "lifecycle", "status": "covered", "notes": "Administrative states, transitions, revision, suspension, cancellation and closure are modeled."},
                {"dimension": "relationships", "status": "covered", "notes": "Typed composition and references keep neighboring model ownership explicit."},
                {"dimension": "temporal", "status": "covered", "notes": "Planning, effective and event time semantics use explicit timezone rules."},
                {"dimension": "provenance", "status": "covered", "notes": "Source lineage, confidence, capture and artifact integrity are represented."},
                {"dimension": "ownership", "status": "covered", "notes": "Dimension, record stewardship, issuer and responsible-party roles are separated."},
                {"dimension": "validation", "status": "covered", "notes": "Boundary, transition, reference, acceptance and before-and-after checks are defined."},
                {"dimension": "access", "status": "covered", "notes": "Default deny, granular scopes, emergency exception and audit requirements are defined."},
                {"dimension": "retention and deletion", "status": "covered", "notes": "Retention, legal hold, tombstone and approved erasure rules preserve reference integrity."},
                {"dimension": "interoperability", "status": "covered", "notes": "ISA-95, OPC UA, PLCS and UN/EDIFACT alignments and lossy mapping requirements are stated."},
                {"dimension": "authority", "status": "covered", "notes": "Issuer authority, authorization scope, delegation and lifecycle action authority are explicit."},
                {"dimension": "requirements and constraints", "status": "covered", "notes": "Outcome, resources, timing, permits, safety, quality and commercial bounds are represented."},
                {"dimension": "evidence and acceptance", "status": "covered", "notes": "Completion claims remain external and are evaluated through explicit criteria and decisions."},
            ],
            "known_omissions": [
                "Industry and jurisdiction profiles must supply exact state code lists, mandatory signatures, permit semantics, retention periods and cancellation effects.",
                "Exact sibling catalogue IDs for schedules, procedures, performed work, contracts, resources and access/audit bindings remain to be pinned as those models mature.",
                "The candidate relation to WM-ACT-006 is represented as COMPOSE rather than lifecycle ownership and needs later cross-model harmonization.",
            ],
            "conflicts": [
                "Standards use both work-order and job-order terminology and vary in state names; this model preserves a neutral administrative lifecycle plus explicit external mappings.",
            ],
            "regional_assumptions": [
                "No universal legal retention period, signature method, worker-qualification rule, safety permit regime or tax treatment is assumed.",
            ],
            "adversarial_checks": [
                "Reject any inference that a released, dispatched or closed order proves that the ordered work occurred.",
                "Reject copied asset, person, organization, inventory, contract or evidence lifecycles when a governed reference is sufficient.",
                "Reject cancellation, deletion, access expansion or acceptance decisions that lack explicit authority and preserved provenance.",
                "Reject timestamps without seconds and explicit offset, date-only artifact identity and destructive overwrites of issued revisions.",
                "Reject universal state vocabularies or retention periods presented without an industry or jurisdiction profile.",
            ],
        },
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(
        json.dumps(build(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
