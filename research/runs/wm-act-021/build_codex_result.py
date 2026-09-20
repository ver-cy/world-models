#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-ACT-021."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED_AT = "2026-09-06T01:00:00Z"


SOURCES = [
    {
        "id": "SRC-001",
        "title": "ISO 10002:2018 Quality management - Customer satisfaction - Guidelines for complaints handling in organizations",
        "organization": "International Organization for Standardization",
        "url": "https://www.iso.org/standard/71580.html",
        "version_or_date": "Edition 3, confirmed 2023",
        "source_type": "standard",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Defines an authoritative complaints-handling profile and explicitly limits that profile, preventing all service cases from being treated as complaints.",
    },
    {
        "id": "SRC-002",
        "title": "Help organizations manage and optimize their case to resolution processes with Dynamics 365",
        "organization": "Microsoft",
        "url": "https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/case-to-resolution-introduction",
        "version_or_date": "Updated 2024-04-26",
        "source_type": "first-party-doc",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Describes generic logging, assignment, investigation, resolution, closure, stakeholders, channels and integrations across customer and employee cases.",
    },
    {
        "id": "SRC-003",
        "title": "Resolve, cancel, and reassign cases",
        "organization": "Microsoft",
        "url": "https://learn.microsoft.com/en-us/dynamics365/customer-service/use/customer-service-hub-user-guide-resolve-cancel-reassign-a-case",
        "version_or_date": "Updated 2026-08-31",
        "source_type": "first-party-doc",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Provides concrete lifecycle, assignment, merge, parent-child, resolution, cancellation and reopening semantics.",
    },
    {
        "id": "SRC-004",
        "title": "Overview of service-level agreements",
        "organization": "Microsoft",
        "url": "https://learn.microsoft.com/en-us/dynamics365/customer-service/use/overview-service-level-agreements",
        "version_or_date": "Current documentation accessed 2026-09-06",
        "source_type": "first-party-doc",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Distinguishes support entitlement and SLA policy from case-bound KPI timers, schedules and measured service performance.",
    },
    {
        "id": "SRC-005",
        "title": "Jira Cloud platform REST API v3 - Issues",
        "organization": "Atlassian",
        "url": "https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/",
        "version_or_date": "Cloud REST API v3 accessed 2026-09-06",
        "source_type": "schema",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Supplies a widely deployed issue representation with keys, fields, transitions, comments, attachments, links, properties and update semantics.",
    },
    {
        "id": "SRC-006",
        "title": "Zendesk Tickets API",
        "organization": "Zendesk",
        "url": "https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/",
        "version_or_date": "Current API documentation accessed 2026-09-06",
        "source_type": "schema",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Provides mature ticket fields, requester and submitter roles, assignee and group ownership, status, priority, comments, collaborators, tags and safe-update controls.",
    },
    {
        "id": "SRC-007",
        "title": "PROV-O: The PROV Ontology",
        "organization": "World Wide Web Consortium",
        "url": "https://www.w3.org/TR/prov-o/",
        "version_or_date": "W3C Recommendation, 30 April 2013",
        "source_type": "ontology",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Provides interoperable entity, activity, agent, derivation and attribution semantics for case assertions and revisions.",
    },
    {
        "id": "SRC-008",
        "title": "RFC 3339: Date and Time on the Internet: Timestamps",
        "organization": "Internet Engineering Task Force",
        "url": "https://www.rfc-editor.org/rfc/rfc3339",
        "version_or_date": "RFC 3339, July 2002",
        "source_type": "standard",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Defines the timestamp representation required for interoperable case events and artifact naming metadata.",
    },
]


# Bundle: id, name, description, rationale, sources, layers.
# Layer: id, name, description, sources, findings.
# Finding: id, name, description, question kind, sources, value kind, required, owns artifact.
STRUCTURE = [
    (
        "identity-classification-and-relations", "Identity, classification and relations",
        "Establishes the governed case aggregate and how it is recognized, classified and linked.",
        "Identity and classification must remain stable enough for routing and federation while allowing profile-specific case types and revisions.",
        ["SRC-002", "SRC-003", "SRC-005", "SRC-006"],
        [
            ("case-identity", "Case identity", "Authoritative and federated identity of the case aggregate.", ["SRC-005", "SRC-006", "SRC-007"], [
                ("authoritative-case-identity", "Authoritative case identity", "Master-system identifier, namespace, immutable revision and record authority.", "identity", ["SRC-005", "SRC-006", "SRC-007"], "identifier", True, True),
                ("aliases-and-external-references", "Aliases and external references", "Human-readable keys, imported identifiers and resolvable references without changing mastership.", "interoperability", ["SRC-005", "SRC-006"], "collection", False, False),
            ]),
            ("case-classification", "Case classification", "Profile-bound type, subject and prioritization.", ["SRC-001", "SRC-002", "SRC-005", "SRC-006"], [
                ("case-type-category-and-subject", "Case type, category and subject", "Type such as inquiry, request, issue or complaint plus category and concise subject under pinned schemes.", "classification", ["SRC-001", "SRC-002", "SRC-005", "SRC-006"], "object", True, True),
                ("impact-urgency-priority-and-tags", "Impact, urgency, priority and tags", "Profile-specific routing and prioritization assertions with scheme, rationale and history.", "classification", ["SRC-002", "SRC-005", "SRC-006"], "collection", False, True),
            ]),
            ("case-relationships", "Case relationships", "Identity-preserving relations among cases and originating subjects.", ["SRC-003", "SRC-005", "SRC-006"], [
                ("parent-child-and-related-cases", "Parent, child and related cases", "Typed case-to-case relationships with cardinality, direction and lifecycle effect declared by policy.", "relationship", ["SRC-003", "SRC-005"], "collection", False, False),
                ("duplicates-merge-and-originating-subject", "Duplicates, merge and originating subject", "Duplicate or merged identity continuity and links to the event, request, product, service or other object that caused intake.", "composition", ["SRC-003", "SRC-005", "SRC-006"], "collection", False, True),
            ]),
        ],
    ),
    (
        "parties-ownership-and-participation", "Parties, ownership and participation",
        "Records the roles by which external identities participate in the case.",
        "The case owns time-bounded role bindings and contact choices, while person and organization master records remain external.",
        ["SRC-002", "SRC-005", "SRC-006"],
        [
            ("originating-parties", "Originating parties", "Requester, submitter, represented party and beneficiary distinctions.", ["SRC-002", "SRC-006"], [
                ("requester-submitter-and-represented-party", "Requester, submitter and represented party", "Separate references for who needs the outcome, who created the record and on whose behalf it was submitted.", "ownership", ["SRC-002", "SRC-006"], "object", True, False),
                ("contact-preferences-consent-and-availability", "Contact preferences, consent and availability", "Case-specific channel, language, availability, consent and accessibility constraints without copying the party profile.", "privacy", ["SRC-002", "SRC-006"], "object", False, True),
            ]),
            ("handling-parties", "Handling parties", "Accountable owner, working assignment and bounded collaboration.", ["SRC-002", "SRC-003", "SRC-005", "SRC-006"], [
                ("owner-queue-group-and-assignee", "Owner, queue, group and assignee", "Distinguishes accountable case owner and queue or group from the current working assignee.", "ownership", ["SRC-002", "SRC-003", "SRC-006"], "object", True, True),
                ("collaborators-followers-and-observers", "Collaborators, followers and observers", "Time-bounded participation, visibility and notification roles that do not imply ownership.", "access", ["SRC-005", "SRC-006"], "collection", False, False),
            ]),
        ],
    ),
    (
        "intake-triage-and-coverage", "Intake, triage and coverage",
        "Captures how the case entered the system and the decisions that make it actionable.",
        "Intake facts are preserved separately from triage decisions, entitlement policy and downstream work execution.",
        ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006"],
        [
            ("intake", "Intake", "Submission channel, times, description and initial evidence.", ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-008"], [
                ("source-channel-and-intake-times", "Source, channel and intake times", "Originating system and channel with submitted, received, observed and acknowledged times kept distinct.", "temporal", ["SRC-002", "SRC-005", "SRC-006", "SRC-008"], "object", True, True),
                ("description-symptoms-request-and-initial-evidence", "Description, symptoms, request and initial evidence", "The reporter's description, requested outcome, observed symptoms and referenced intake attachments without asserting they are verified facts.", "evidence", ["SRC-001", "SRC-002", "SRC-005", "SRC-006"], "object", True, True),
            ]),
            ("triage-and-coverage", "Triage and coverage", "Acceptance, routing and service-coverage bindings.", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006"], [
                ("accept-reject-redirect-and-routing", "Accept, reject, redirect and routing", "Authorized triage outcome, target queue, rationale and confidence without erasing the original submission.", "decision", ["SRC-001", "SRC-002", "SRC-005"], "object", True, True),
                ("entitlement-contract-product-and-service-binding", "Entitlement, contract, product and service binding", "References to the coverage authority and supported object that govern eligibility and service commitments.", "requirement", ["SRC-002", "SRC-004"], "collection", False, False),
            ]),
        ],
    ),
    (
        "lifecycle-assignment-and-escalation", "Lifecycle, assignment and escalation",
        "Tracks case-owned state, work coordination and escalation decisions.",
        "The case records coordination state and references tasks; it does not absorb generic workflow, work-order or resource-allocation lifecycles.",
        ["SRC-002", "SRC-003", "SRC-005", "SRC-006"],
        [
            ("case-state", "Case state", "Current state, status reason and append-only transition history.", ["SRC-003", "SRC-005", "SRC-006"], [
                ("state-status-reason-and-transition", "State, status reason and transition", "Profile-bound state with allowed transition, actor, effective time, reason and previous revision.", "state", ["SRC-003", "SRC-005", "SRC-006"], "object", True, True),
                ("pending-waiting-and-blocking-condition", "Pending, waiting and blocking condition", "Why progress is paused, what external response or condition is awaited and which clock effects apply.", "constraint", ["SRC-003", "SRC-004", "SRC-005", "SRC-006"], "object", False, True),
            ]),
            ("assignment-and-escalation", "Assignment and escalation", "Assignment history and governed escalation.", ["SRC-002", "SRC-003", "SRC-005", "SRC-006"], [
                ("assignment-reassignment-and-routing-history", "Assignment, reassignment and routing history", "Every ownership or queue movement with source rule, actor, reason and effective interval.", "lifecycle", ["SRC-002", "SRC-003", "SRC-005", "SRC-006"], "collection", True, True),
                ("escalation-level-trigger-and-target", "Escalation level, trigger and target", "Case-specific escalation request or decision with threshold evidence, destination and acknowledgement.", "process", ["SRC-002", "SRC-004", "SRC-006"], "object", False, True),
            ]),
        ],
    ),
    (
        "communications-evidence-and-knowledge", "Communications, evidence and knowledge",
        "Indexes case communications, evidence and relevant knowledge without taking over their payload lifecycles.",
        "Case context needs chronology and visibility bindings, but message, document, evidence and knowledge masters stay in their native systems.",
        ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007"],
        [
            ("case-communications", "Case communications", "Thread membership, audience, visibility and delivery events.", ["SRC-001", "SRC-002", "SRC-005", "SRC-006"], [
                ("message-thread-and-visibility-bindings", "Message thread and visibility bindings", "References to messages and conversations with direction, participant role and public, internal or restricted visibility.", "relationship", ["SRC-002", "SRC-005", "SRC-006"], "collection", False, False),
                ("acknowledgement-update-and-notification-events", "Acknowledgement, update and notification events", "What update was issued or received, to whom, by which channel and with what delivery result.", "event", ["SRC-001", "SRC-002", "SRC-006"], "collection", False, True),
            ]),
            ("evidence-and-knowledge", "Evidence and knowledge", "Attachment provenance and knowledge applicability.", ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007"], [
                ("attachment-document-and-evidence-references", "Attachment, document and evidence references", "Resolvable content references with digest, provenance, relevance, access and retention bindings.", "provenance", ["SRC-005", "SRC-006", "SRC-007"], "collection", False, False),
                ("knowledge-reference-and-applicability", "Knowledge reference and applicability", "Versioned knowledge-article or answer references with suggested use, limitations and observed usefulness.", "interoperability", ["SRC-002", "SRC-005"], "collection", False, False),
            ]),
        ],
    ),
    (
        "commitments-resolution-and-feedback", "Commitments, resolution and feedback",
        "Binds applicable service commitments and records outcome, closure, reopening and feedback.",
        "The case owns the applied commitment instance and outcome assertions while policy design, calendars, work execution and corrective-action programs remain external.",
        ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006"],
        [
            ("service-commitments", "Service commitments", "Applied SLA policy and measured KPI instances.", ["SRC-004"], [
                ("sla-policy-kpi-and-calendar-binding", "SLA policy, KPI and calendar binding", "Pinned entitlement, SLA item, KPI and business-calendar references applied to the case.", "requirement", ["SRC-004"], "collection", False, False),
                ("target-clock-pause-and-breach-instance", "Target, clock, pause and breach instance", "Case-bound target time, start, pause, resume, success or breach observations and calculation provenance.", "measurement", ["SRC-004", "SRC-008"], "collection", False, True),
            ]),
            ("resolution-and-remedy", "Resolution and remedy", "Resolution assertion and referenced remedial work.", ["SRC-001", "SRC-002", "SRC-003", "SRC-005", "SRC-006"], [
                ("resolution-type-summary-and-outcome", "Resolution type, summary and outcome", "The proposed or delivered answer, disposition and observed result with authority and supporting references.", "decision", ["SRC-001", "SRC-002", "SRC-003", "SRC-006"], "object", False, True),
                ("remedy-root-cause-and-corrective-action-bindings", "Remedy, root cause and corrective-action bindings", "References to delivered remedy, investigation, root-cause analysis, problem record and corrective-action program.", "relationship", ["SRC-001", "SRC-002", "SRC-005"], "collection", False, False),
            ]),
            ("closure-reopen-and-feedback", "Closure, reopen and feedback", "Governed completion and post-resolution signals.", ["SRC-001", "SRC-002", "SRC-003", "SRC-006"], [
                ("closure-cancellation-and-acceptance", "Closure, cancellation and acceptance", "Decision, authority, prerequisite checks, outcome acceptance and unresolved obligations for closing or cancelling the case.", "lifecycle", ["SRC-001", "SRC-003"], "object", False, True),
                ("reopen-appeal-satisfaction-and-feedback", "Reopen, appeal, satisfaction and feedback", "Reopening or appeal basis plus consented satisfaction and feedback signals linked to the prior outcome.", "quality", ["SRC-001", "SRC-002", "SRC-003"], "collection", False, True),
            ]),
        ],
    ),
    (
        "governance-provenance-and-interoperability", "Governance, provenance and interoperability",
        "Protects sensitive case data and preserves trustworthy exchange and mutation semantics.",
        "Agents need explicit access, retention, provenance, concurrency and mapping rules because case fields are mutable and often shared across systems.",
        ["SRC-005", "SRC-006", "SRC-007", "SRC-008"],
        [
            ("access-privacy-and-retention", "Access, privacy and retention", "Minimum projections, exceptions and disposition controls.", ["SRC-005", "SRC-006", "SRC-007"], [
                ("visibility-access-and-privacy-projection", "Visibility, access and privacy projection", "Field and artifact visibility, purpose, recipient, redaction and exceptional-access decision.", "access", ["SRC-005", "SRC-006"], "object", True, True),
                ("retention-legal-hold-deletion-and-tombstone", "Retention, legal hold, deletion and tombstone", "Pinned retention authority, hold status, permitted erasure and non-cascading reference disposition.", "retention", ["SRC-005", "SRC-006", "SRC-007"], "object", True, True),
            ]),
            ("provenance-concurrency-and-federation", "Provenance, concurrency and federation", "Trustworthy revision history and cross-system mapping.", ["SRC-005", "SRC-006", "SRC-007", "SRC-008"], [
                ("revision-provenance-etag-and-safe-update", "Revision provenance, ETag and safe update", "Who or what generated each revision, from which inputs, with optimistic concurrency and conflict handling.", "validation", ["SRC-005", "SRC-006", "SRC-007"], "object", True, True),
                ("external-schema-mapping-and-projection", "External schema mapping and projection", "Pinned field mappings, transform loss, extension namespace and digest for exported or imported case projections.", "interoperability", ["SRC-005", "SRC-006", "SRC-007"], "collection", False, False),
            ]),
        ],
    ),
]


KIND_CYCLE = [
    "definition", "identity", "classification", "composition", "relationship", "state",
    "lifecycle", "temporal", "provenance", "ownership", "authority", "requirement",
    "constraint", "process", "event", "measurement", "evidence", "quality",
    "validation", "security", "privacy", "retention", "access", "exception",
    "interoperability", "decision",
]


def build_finding(raw: tuple, ordinal: int) -> dict:
    finding_id, name, description, primary_kind, refs, value_kind, required, owns_artifact = raw
    kinds = [
        primary_kind,
        KIND_CYCLE[(ordinal * 5 + 3) % len(KIND_CYCLE)],
        KIND_CYCLE[(ordinal * 11 + 9) % len(KIND_CYCLE)],
    ]
    for position in range(1, 3):
        while kinds[position] in kinds[:position]:
            kinds[position] = KIND_CYCLE[(KIND_CYCLE.index(kinds[position]) + 1) % len(KIND_CYCLE)]
    questions = [
        {
            "id": f"{finding_id}-q01",
            "text": f"What is the current governed value of {name.lower()} for this service case, and which parts are unknown or disputed?",
            "kind": kinds[0],
            "answer_data": [name, "assertion status", "applicable scope or explicit unknown"],
        },
        {
            "id": f"{finding_id}-q02",
            "text": f"Which source, participant or authority establishes {name.lower()}, at what effective and observation times, and with what evidence?",
            "kind": kinds[1],
            "answer_data": ["source or authority reference", "effective and observation timestamps", "evidence and confidence"],
        },
        {
            "id": f"{finding_id}-q03",
            "text": f"Which validation, authorization or conflict rule may revise {name.lower()} while preserving case history?",
            "kind": kinds[2],
            "answer_data": ["validation and authorization rule", "revision event and reason", "predecessor or counterclaim reference"],
        },
    ]
    artifacts = []
    inline_rationale = "This finding stores only typed references and case-local bindings; the referenced system owns the payload and independent lifecycle."
    if owns_artifact:
        artifacts = [{
            "id": f"{finding_id}-artifact",
            "name": f"{name} record",
            "description": f"Versioned case-owned record supporting {name.lower()} with provenance and access marking.",
            "media_or_form": ["structured case record", "signed or controlled statement", "resolvable supporting index"],
            "serial": True,
            "identity_strategy": "Authoritative case master-system identifier first; otherwise a Dimension-governed UUID or ULID.",
            "source_refs": refs,
        }]
        inline_rationale = None
    return {
        "id": finding_id,
        "name": name,
        "description": description,
        "source_refs": refs,
        "questions": questions,
        "data_elements": [{
            "id": f"{finding_id}-data",
            "name": f"{name} assertion",
            "description": f"Structured case-local answer data for {name.lower()}, including status, effective time and provenance where applicable.",
            "value_kind": value_kind,
            "cardinality": "1" if required else "0..1",
            "required": required,
            "source_refs": refs,
        }],
        "artifacts": artifacts,
        "inline_only_rationale": inline_rationale,
    }


def build_structure() -> dict:
    bundles = []
    ordinal = 0
    for bundle_id, name, description, rationale, refs, layer_rows in STRUCTURE:
        layers = []
        for layer_id, layer_name, layer_description, layer_refs, finding_rows in layer_rows:
            findings = []
            for raw in finding_rows:
                ordinal += 1
                findings.append(build_finding(raw, ordinal))
            layers.append({"id": layer_id, "name": layer_name, "description": layer_description, "source_refs": layer_refs, "findings": findings})
        bundles.append({"id": bundle_id, "name": name, "description": description, "rationale": rationale, "source_refs": refs, "layers": layers})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-case", "Register case", "Create a case from an authorized submission without inventing missing facts.", ["submission", "source and channel", "requester or submitter reference"], ["case identity", "intake revision"], ["intake purpose and record authority are known"], ["an attributable case with explicit unknowns exists"], ["SRC-001", "SRC-002", "SRC-005", "SRC-006"]),
    ("validate-and-triage-case", "Validate and triage case", "Check minimum data, duplicates, scope, eligibility and routing rules.", ["case", "triage profile", "coverage references"], ["triage decision", "routing target"], ["profile and decision authority resolve"], ["acceptance, rejection or redirect is preserved with rationale"], ["SRC-001", "SRC-002", "SRC-004"]),
    ("classify-and-prioritize-case", "Classify and prioritize case", "Apply pinned type, category, impact, urgency and priority schemes.", ["case", "classification schemes", "evidence"], ["classification revision"], ["schemes are versioned"], ["routing inputs are reproducible without a universal vocabulary"], ["SRC-002", "SRC-005", "SRC-006"]),
    ("link-or-merge-case", "Link or merge case", "Create a typed case relation or merge a duplicate while preserving aliases.", ["case identities", "relation type", "authority and evidence"], ["relationship or merge decision"], ["identities resolve and merge policy permits the action"], ["predecessor identities and history remain resolvable"], ["SRC-003", "SRC-005", "SRC-006"]),
    ("assign-or-route-case", "Assign or route case", "Bind or change the accountable owner, queue and working assignee.", ["case", "target role or queue", "routing reason"], ["assignment revision"], ["target is eligible and actor is authorized"], ["current assignment and full routing history are distinguishable"], ["SRC-002", "SRC-003", "SRC-005", "SRC-006"]),
    ("transition-case-state", "Transition case state", "Apply a permitted state transition with reason and effective time.", ["case", "current state", "proposed state", "evidence"], ["state transition revision"], ["transition profile and authority permit the change"], ["case state changes without rewriting prior revisions"], ["SRC-003", "SRC-005", "SRC-006"]),
    ("record-case-communication", "Record case communication", "Link a message or delivery event with audience and visibility metadata.", ["case", "message reference", "participants and visibility"], ["communication binding"], ["content and audience are permitted"], ["chronology is updated while the message system retains mastership"], ["SRC-001", "SRC-002", "SRC-005", "SRC-006"]),
    ("bind-evidence-or-knowledge", "Bind evidence or knowledge", "Attach a governed reference to evidence, a document or knowledge item.", ["case", "external object reference", "relevance and provenance"], ["typed binding"], ["reference resolves and access is allowed"], ["case context expands without copying the external lifecycle"], ["SRC-005", "SRC-006", "SRC-007"]),
    ("evaluate-case-commitment", "Evaluate case commitment", "Record case-bound SLA KPI timing using external policy and calendar results.", ["case", "SLA and entitlement references", "timer events"], ["commitment instance revision"], ["policy, KPI and calendar versions resolve"], ["target, pause and breach status are reproducible"], ["SRC-004", "SRC-008"]),
    ("resolve-close-or-cancel-case", "Resolve, close or cancel case", "Record an authorized outcome and completion decision separately.", ["case", "resolution or cancellation reason", "prerequisite checks"], ["outcome revision", "closure decision"], ["state profile and authority permit the action"], ["resolution, acceptance, closure and cancellation remain distinct"], ["SRC-001", "SRC-002", "SRC-003"]),
    ("reopen-or-appeal-case", "Reopen or appeal case", "Create a governed continuation from new evidence, failed outcome or appeal.", ["closed case", "basis and evidence", "authority"], ["reopen or appeal revision"], ["policy permits continuation"], ["prior outcome remains immutable and linked"], ["SRC-001", "SRC-003"]),
    ("issue-case-projection", "Issue case projection", "Produce a minimum authorized view for a recipient, purpose or external schema.", ["case revision", "recipient and purpose", "projection policy"], ["digest-pinned projection"], ["access decision permits disclosure"], ["redaction, mapping version and provenance are recorded"], ["SRC-005", "SRC-006", "SRC-007"]),
]


def build() -> dict:
    return {
        "schema_version": "1.0.0",
        "model": {
            "registry_id": "vr.wm-act-021",
            "model_id": "WM-ACT-021",
            "name": "Service Case / Ticket",
            "entry_kind": "aggregate",
            "purpose": "Represent a governed request, inquiry, issue or complaint that an organization receives, owns, coordinates and brings to an evidence-backed outcome across channels and systems.",
            "scope_statement": "Owns case identity, classification, participation roles, intake, triage, case state, assignment, case-local communication and evidence indexes, applied commitment instances, outcome, closure, reopening and governed projections while referencing external parties, content, policies and work execution.",
            "in_scope": [
                "Case identity, intake, classification, relationships, requester and handling roles, state and assignment history",
                "Case-local communication, evidence and knowledge bindings, applied service commitments, outcome, closure, feedback and federation",
                "Typed references to parties, products, services, contracts, messages, documents, tasks, policies, calendars and knowledge",
            ],
            "out_of_scope": [
                "Person or organization identity, message and document payloads, generic workflow, work-order execution, knowledge lifecycle and policy evaluation engines",
                "Universal status, priority, entitlement, SLA, complaint, resolution or retention vocabularies",
                "Access enforcement, audit-log persistence and master data owned by external systems",
            ],
            "boundary_notes": [
                {"neighbor": "Request, inquiry, issue and complaint", "distinction": "These are profile-bound case types. A complaint may follow ISO 10002, but that complaints profile does not define every service case.", "source_refs": ["SRC-001", "SRC-002"]},
                {"neighbor": "Incident or problem", "distinction": "A case is a handling aggregate initiated around a need or issue; the underlying incident, defect, problem or affected object keeps its own identity and lifecycle.", "source_refs": ["SRC-002", "SRC-005"]},
                {"neighbor": "Task, work order and workflow", "distinction": "The case owns coordination status and assignments but references independently governed execution tasks and workflows.", "source_refs": ["SRC-002", "SRC-003", "SRC-005"]},
                {"neighbor": "SLA policy and calendar", "distinction": "The case stores the pinned policy binding and observed KPI timer instance, while policy definition and business-time calculation remain external.", "source_refs": ["SRC-004"]},
                {"neighbor": "Communication, document and knowledge", "distinction": "The case indexes relevance, chronology and visibility; external systems own message, file, evidence and knowledge payload lifecycles.", "source_refs": ["SRC-002", "SRC-005", "SRC-006", "SRC-007"]},
            ],
        },
        "sources": SOURCES,
        "structure": build_structure(),
        "functions": [
            {"id": row[0], "name": row[1], "description": row[2], "inputs": row[3], "outputs": row[4], "preconditions": row[5], "effects": row[6], "source_refs": row[7]}
            for row in FUNCTIONS
        ],
        "composition": [
            {"target": "Person and Organization models", "relation": "REFERENCE", "purpose": "Binds requester, submitter, beneficiary, owner, assignee and collaborator identities without duplicating their master records.", "required": True, "source_refs": ["SRC-002", "SRC-006"]},
            {"target": "Product, Service, Asset and Entitlement models", "relation": "REFERENCE", "purpose": "Identifies the supported or affected object and coverage authority without importing those lifecycles.", "required": False, "source_refs": ["SRC-002", "SRC-004"]},
            {"target": "Communication and Message models", "relation": "REFERENCE", "purpose": "Maintains case chronology, participant and visibility bindings while the communication system owns content and delivery records.", "required": False, "source_refs": ["SRC-002", "SRC-005", "SRC-006"]},
            {"target": "Document and Evidence models", "relation": "REFERENCE", "purpose": "Indexes case evidence with integrity, provenance and access bindings while the repository owns content and custody.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-007"]},
            {"target": "Task, Work Order and Workflow models", "relation": "REFERENCE", "purpose": "Links executable work without conflating case state with task completion or resource allocation.", "required": False, "source_refs": ["SRC-002", "SRC-003", "SRC-005"]},
            {"target": "SLA Policy and Business Calendar models", "relation": "REFERENCE", "purpose": "Pins policy, KPI and calendar versions used to calculate case commitment instances.", "required": False, "source_refs": ["SRC-004"]},
            {"target": "Knowledge Article model", "relation": "REFERENCE", "purpose": "Binds suggested or applied knowledge with version and applicability without owning article publication.", "required": False, "source_refs": ["SRC-002", "SRC-005"]},
            {"target": "Jira issue and Zendesk ticket schemas", "relation": "ALIGN", "purpose": "Supports versioned import and export mappings with explicit loss and extension handling.", "required": False, "source_refs": ["SRC-005", "SRC-006"]},
            {"target": "W3C PROV-O", "relation": "ALIGN", "purpose": "Aligns case entities, revisions, activities and accountable agents for portable provenance.", "required": False, "source_refs": ["SRC-007"]},
        ],
        "service_layers": {
            "dimension": {
                "owner_package_requirements": [
                    "Declare the Dimension owner, case namespace, case master systems, constituencies, stewards and delegated decision authorities.",
                    "Publish model, object, event, relation, policy and role registries plus channel, time, privacy, retention and federation rules.",
                    "Pin case-type, status, priority, entitlement, SLA, calendar, closure and appeal profiles used by each case.",
                    "Declare external party, product, service, communication, document, work, knowledge and audit masters.",
                ],
                "namespace_guidance": "Mint case identities only in the adopting Dimension's governed namespace; preserve human keys and provider IDs as typed aliases with authority, tenant scope and history.",
                "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local case, object, event, policy and role registries"],
            },
            "canon_and_patch": {
                "canonicalization_rules": [
                    "Canonicalize by registry ID, model version, case master identifier, immutable revision and explicit authority; never use mutable title or status as identity.",
                    "Keep request facts, triage decisions, case state, work state, resolution, acceptance and closure as distinct concepts.",
                ],
                "patch_rules": [
                    "Additive extensions use a Dimension-owned namespace and declare target node, case profile, source, rationale, access impact and migration behavior.",
                    "Breaking changes require a new model version, migration map, compatibility declaration and continued resolution of prior case revisions.",
                ],
                "compatibility_rules": [
                    "Consumers may ignore unknown additive fields only when identity, authority, provenance, access and temporal meaning remain intact.",
                    "Vendor and partner mappings pin API or schema versions and declare omitted, transformed, redacted or non-round-trippable values.",
                ],
            },
            "artifact_rules": {
                "identity_priority": [
                    "Authoritative case master-system identifier and immutable revision identifier.",
                    "Governed globally resolvable case IRI or federation identifier.",
                    "Adopting-Dimension UUID or ULID when no authoritative external identifier exists.",
                ],
                "timestamp_rule": "Record all event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep submitted, received, observed, effective, due and ingestion times distinct.",
                "serial_naming_rule": "Name serial artifacts as {case-id}--{artifact-kind}--{revision-or-event-id}; never use a date, filename or hash alone as case identity.",
                "integrity_rule": "Store digest, media type, byte length, issuer or collector, provenance, access marking and immutable version reference for every retained serial artifact.",
            },
            "policies": [
                "The adopting Dimension declares who may register, triage, classify, assign, escalate, disclose, resolve, close, cancel, merge, reopen and delete a case.",
                "Every material case assertion keeps source, effective time, observation time, confidence where applicable and revision history.",
                "Agents minimize personal and sensitive data and use the narrowest permitted projection for the active purpose and recipient.",
                "Messages, documents, evidence, policies, calendars, tasks, knowledge, access enforcement and audit persistence remain in their owning systems and are referenced.",
                "Automated agents may perform delegated low-risk enrichment but must honor Dimension policy for consequential disclosure, denial, closure, deletion and cross-Dimension transfer.",
            ],
            "crud": {
                "read": ["Resolve the active Dimension, model and profile versions, role, purpose, access policy and external masters; return only the permitted case projection and explicit unknowns."],
                "create": ["Create the authoritative identity, source, intake time, requester or submitter binding, description and explicit unknowns; do not imply acceptance, entitlement or resolution."],
                "update": ["Append an immutable revision with actor, authority, reason and RFC 3339 effective time; validate identity, concurrency, state, references and access before and after mutation."],
                "delete": ["Apply retention, legal hold and erasure policy; tombstone case-owned records or use approved erasure while external systems retain their own copies and references never cascade automatically."],
            },
            "roles": [
                {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, profiles, delegation, federation, access and retention rules."]},
                {"name": "Case owner", "responsibilities": ["Remain accountable for triage, coordination, outcome and closure within mandate."]},
                {"name": "Case agent or assignee", "responsibilities": ["Maintain evidence-backed case context, communication bindings, progress and proposed outcome."]},
                {"name": "Requester or represented party", "responsibilities": ["Supply the need and evidence, receive permitted updates and respond to proposed outcomes."]},
                {"name": "Supervisor or escalation authority", "responsibilities": ["Approve escalations, exceptions, reassignment and high-impact disposition decisions."]},
                {"name": "Privacy, legal or records steward", "responsibilities": ["Review disclosure, consent, legal hold, retention, deletion and regulated complaint bindings."]},
                {"name": "Auditor", "responsibilities": ["Review decisions, provenance, access and revisions without rewriting operational truth."]},
            ],
            "access": {
                "default_rule": "Deny mutation and sensitive disclosure unless the active Dimension, role, purpose, case type and field or artifact policy grant the action; expose the minimum necessary projection.",
                "scopes": ["bundle", "layer", "finding", "artifact"],
                "exceptions": ["Emergency or break-glass access is time-limited, purpose-bound, attributable, independently reviewed and cannot erase immutable history or legal hold."],
                "audit_requirements": ["Log actor, role, purpose, case and revision identity, action, decision, policy version, RFC 3339 timestamp with offset, affected scope and outcome for each privileged mutation or disclosure."],
            },
            "agents_bootstrap": {
                "filename": "AGENTS.md",
                "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
                "read_order": ["Read the nearest Dimension-owner AGENTS.md, role, purpose, case profiles and access policies.", "Read this model AGENTS.md, then pinned spec.yaml and required party, content, work, commitment and audit model instructions before mutation."],
            },
        },
        "coverage": {
            "claim": "Source-grounded reviewable draft covering generic service-case identity, classification, participants, intake, triage, lifecycle, communications, evidence, service commitments, outcomes, governance and federation across standards and mature service platforms.",
            "confidence": "medium",
            "checklist": [
                {"dimension": "identity", "status": "covered", "notes": "Master identity, aliases, tenant scope, revision, duplicate merge and parent-child continuity are explicit."},
                {"dimension": "classification and recognition", "status": "covered", "notes": "Case type, category, subject, tags, impact, urgency and priority bind to versioned profiles."},
                {"dimension": "lifecycle", "status": "covered", "notes": "Intake, triage, assignment, transitions, resolution, closure, cancellation, reopening and appeal preserve history."},
                {"dimension": "relationships", "status": "covered", "notes": "Parties, affected subjects, cases, communications, evidence, work, policies and knowledge use typed references."},
                {"dimension": "temporal", "status": "covered", "notes": "Submitted, received, acknowledged, observed, effective, due, paused, resumed and closed times remain distinct."},
                {"dimension": "provenance", "status": "covered", "notes": "Sources, authorities, evidence, confidence, derivation and revision lineage are represented per material assertion."},
                {"dimension": "ownership", "status": "covered", "notes": "Requester, submitter, represented party, case owner, queue, assignee and external masters have distinct roles."},
                {"dimension": "validation", "status": "covered", "notes": "Identity, duplicate, required data, transition, concurrency, reference, access and pre or post mutation checks are explicit."},
                {"dimension": "access and privacy", "status": "covered", "notes": "Default deny, participant visibility, minimum projections, consent, redaction and exceptional access are explicit."},
                {"dimension": "retention and deletion", "status": "covered", "notes": "Retention authority, legal hold, tombstone, approved erasure and non-cascading references are defined."},
                {"dimension": "interoperability", "status": "covered", "notes": "Vendor and partner mappings require pinned versions, transform provenance and declared information loss."},
                {"dimension": "direct properties", "status": "not-applicable", "notes": "The case is an abstract aggregate; physical and intrinsic properties belong to referenced products, assets, people and services."},
                {"dimension": "behavior and possible actions", "status": "covered", "notes": "Case state and authorized functions are represented without conflating them with external work execution."},
                {"dimension": "service commitments", "status": "covered", "notes": "Entitlement and policy references, KPI targets, clocks, pauses and observed breaches are separated from policy design."},
            ],
            "known_omissions": [
                "Sector, organization and jurisdiction profiles must supply exact case types, states, priorities, entitlements, SLA rules, closure tests and retention periods.",
                "Sibling model identifiers and cardinality contracts for parties, products, services, communications, documents, evidence, work, knowledge, policies and calendars remain to be pinned as the catalogue matures.",
                "Clause and field-level mappings to ISO 10002, Jira, Zendesk, Dynamics 365 and other case platforms remain profile work.",
            ],
            "conflicts": [
                "Case, ticket, issue, request, complaint and incident overlap across platforms; this draft treats them as profile-bound case classifications and does not claim one universal vocabulary.",
                "Vendor status and priority fields are not semantically identical, so mappings must preserve original codes and declare loss rather than silently normalize them.",
                "A resolved case is not automatically accepted, closed, compliant or factually corrected; each assertion has separate authority and evidence.",
            ],
            "regional_assumptions": [
                "ISO 10002 is an optional complaints profile and does not make every service case a complaint or apply external-dispute rules universally.",
                "No universal privacy, consumer, employment, public-records, SLA or retention rule is assumed; the active Dimension and jurisdiction supply these profiles.",
            ],
            "adversarial_checks": [
                "Reject tickets that omit authoritative identity, source, intake time or requester and submitter distinctions while claiming operational completeness.",
                "Reject silent status normalization, overwritten assignment history, unsupported priority, invented entitlement, inferred acceptance or closure without authority.",
                "Reject copied party, communication, document, evidence, task, policy, calendar and knowledge lifecycles when governed references are sufficient.",
                "Reject timestamps without seconds and explicit offset, unsafe last-write-wins updates, broken aliases and external mappings without pinned versions and loss declarations.",
                "Reject disclosure, merge, closure, cancellation, reopening and deletion decisions that lack purpose, authority, access review and preserved provenance.",
            ],
        },
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
