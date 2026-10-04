#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-ACT-049."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T10:03:00Z"


def src(i, title, org, url, version, kind, relevance):
    return {
        "id": f"SRC-{i:03d}",
        "title": title,
        "organization": org,
        "url": url,
        "version_or_date": version,
        "source_type": kind,
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": AT,
        "relevance": relevance,
    }


SOURCES = [
    src(1, "FHIR R5 CarePlan", "Health Level Seven International", "https://hl7.org/fhir/R5/careplan.html", "FHIR 5.0.0, 26 March 2023, maturity level 2 and Trial Use", "standard", "Defines a planning request that groups intended care, goals, participants and activity references for a subject over a period without owning execution."),
    src(2, "FHIR R5 EpisodeOfCare", "Health Level Seven International", "https://hl7.org/fhir/R5/episodeofcare.html", "FHIR 5.0.0, 26 March 2023, maturity level 2 and Trial Use", "standard", "Defines the time-bounded association and responsibility of a provider organization for a patient, status history and links to encounters, and distinguishes tracking from planning."),
    src(3, "FHIR R5 Goal", "Health Level Seven International", "https://hl7.org/fhir/R5/goal.html", "FHIR 5.0.0, 26 March 2023, maturity level 2 and Trial Use", "standard", "Defines a subject-specific desired state with lifecycle, achievement status, priority, targets, due time, source, addresses and outcome links."),
    src(4, "FHIR R5 CareTeam", "Health Level Seven International", "https://hl7.org/fhir/R5/careteam.html", "FHIR 5.0.0, 26 March 2023, maturity level 2 and Trial Use", "standard", "Defines dynamic people and organizations intended to coordinate and deliver care, participant roles, periods and on-behalf-of relationships."),
    src(5, "FHIR R5 RequestOrchestration", "Health Level Seven International", "https://hl7.org/fhir/R5/requestorchestration.html", "FHIR 5.0.0, 26 March 2023, maturity level 4 and Trial Use", "standard", "Defines related subject-specific requests, hierarchical action groups, conditions, optionality and dependencies while each request retains its own lifecycle."),
    src(6, "FHIR R5 PlanDefinition", "Health Level Seven International", "https://hl7.org/fhir/R5/plandefinition.html", "FHIR 5.0.0, 26 March 2023, maturity level 4 and Trial Use", "standard", "Defines reusable protocols, order sets and decision artifacts that may be instantiated for a subject; it is distinct from a subject-specific care plan."),
    src(7, "FHIR R5 Task", "Health Level Seven International", "https://hl7.org/fhir/R5/task.html", "FHIR 5.0.0, 26 March 2023, maturity level 3 and Trial Use", "standard", "Defines a work item and its fulfillment state, requester, owner, focus, inputs and outputs; it separates execution tracking from request authorization."),
    src(8, "FHIR R5 Workflow", "Health Level Seven International", "https://hl7.org/fhir/R5/workflow.html", "FHIR 5.0.0, 26 March 2023, maturity level 2 and Trial Use", "standard", "Defines workflow state, relationships and coordination patterns and warns that interoperable data exchange does not by itself standardize process execution."),
    src(9, "FHIR R5 ClinicalImpression", "Health Level Seven International", "https://hl7.org/fhir/R5/clinicalimpression.html", "FHIR 5.0.0, 26 March 2023, maturity level 1 and Trial Use", "standard", "Defines an attributable clinical assessment and reasoning record that may precede or revise a care plan without becoming the plan itself."),
    src(10, "FHIR R5 Condition", "Health Level Seven International", "https://hl7.org/fhir/R5/condition.html", "FHIR 5.0.0, 26 March 2023, maturity level 5 and Trial Use", "standard", "Defines conditions, problems and concerns with separate clinical and verification states; a plan references rather than owns these clinical assertions."),
    src(11, "FHIR R5 Observation", "Health Level Seven International", "https://hl7.org/fhir/R5/observation.html", "FHIR 5.0.0, 26 March 2023, Normative from FHIR 4.0.0", "standard", "Defines measurements and simple assertions used to establish baselines and evaluate progress, with source, method, time, value and interpretation."),
    src(12, "Continuity and coordination of care", "World Health Organization", "https://www.who.int/publications/i/item/9789241514033", "WHO practice brief, 7 November 2018", "public-authority", "Supports relational, informational and management continuity, coordinated transitions and person-centred care across settings and time."),
    src(13, "UHC service planning and models of care", "World Health Organization", "https://www.who.int/teams/integrated-health-services/clinical-services-and-systems/service-organizations-and-integration", "Living official page accessed 6 September 2026", "public-authority", "Supports integrated, coordinated and people-centred service models aligned to individual and community needs across providers and settings."),
    src(14, "Shared decision making", "National Institute for Health and Care Excellence", "https://www.nice.org.uk/guidance/ng197", "NICE guideline NG197, published 17 June 2021", "public-authority", "Defines shared treatment and care decisions, communication of benefits, risks and consequences, decision aids and organizational support."),
    src(15, "Dynamic Care Planning", "Integrating the Healthcare Enterprise", "https://www.ihe.net/uploadedFiles/Documents/PCC/IHE_PCC_Suppl_DCP.pdf", "IHE PCC Supplement, revised 27 September 2019", "standard", "Defines interoperable dynamic care-plan sharing, contributors, goals, interventions and updates while remaining an implementation profile rather than universal clinical policy."),
    src(16, "Task Planning Specification", "openEHR Foundation", "https://specifications.openehr.org/releases/PROC/latest/task_planning.html", "PROC Release-1.7.0, RETIRED, copyright 2017-2024", "standard", "Provides useful planning concepts such as teams, recurring tasks, decision pathways, cancellation and plan tracking, but its retired status requires an explicit non-conformance hold."),
    src(17, "Regulation (EU) 2016/679 General Data Protection Regulation", "European Union", "https://eur-lex.europa.eu/eli/reg/2016/679/oj", "27 April 2016, applicable from 25 May 2018", "legislation", "Provides purpose limitation, minimization, accuracy, security, access and correction safeguards for sensitive care-plan and episode data."),
    src(18, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Provides entity, activity, agent, attribution, delegation, derivation, revision, generation and invalidation semantics for plans and episode records."),
    src(19, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339, July 2002", "standard", "Provides interoperable timestamps with seconds and explicit UTC relationship for clinical, planning, transition, record and knowledge times."),
]


ROWS = [
    ("aggregate-identity-boundary-and-constituent-types", "Aggregate identity, boundary and constituent types", "The useful aggregate connects a planning record and a responsibility-tracking episode without collapsing their identities or states", [
        ("aggregate-profile-identifiers-versions-sources-and-lineage", "Aggregate profile, identifiers, versions, sources and lineage", ["SRC-001", "SRC-002", "SRC-015", "SRC-018"], [
            ("care-context-aggregate-profile-and-plan-episode-constituent-kinds", "Care context aggregate profile and plan or episode constituent kinds", "classification", True),
            ("aggregate-plan-and-episode-identifiers-versions-sources-and-lineage", "Aggregate, plan and episode identifiers, versions, sources and lineage", "identity", True),
        ]),
        ("subject-scope-care-setting-and-plan-episode-encounter-boundary", "Subject, scope, care setting and plan, episode or encounter boundary", ["SRC-001", "SRC-002", "SRC-007", "SRC-008", "SRC-012", "SRC-013"], [
            ("subject-population-care-setting-category-title-description-and-period", "Subject, population, care setting, category, title, description and period", "definition", True),
            ("planning-responsibility-encounter-work-item-and-performed-event-distinction", "Planning, responsibility, encounter, work item and performed-event distinction", "relationship", True),
        ]),
    ]),
    ("concerns-assessment-goals-targets-preferences-and-decisions", "Concerns, assessment, goals, targets, preferences and decisions", "Care intent is interpretable only when concerns, evidence, desired outcomes, priorities and person preferences remain attributable and separately governed", [
        ("conditions-concerns-reasons-assessment-and-supporting-evidence", "Conditions, concerns, reasons, assessment and supporting evidence", ["SRC-001", "SRC-002", "SRC-009", "SRC-010", "SRC-011", "SRC-018"], [
            ("condition-problem-concern-reason-and-health-need-references", "Condition, problem, concern, reason and health-need references", "relationship", False),
            ("clinical-impression-baseline-risk-priority-and-supporting-information", "Clinical impression, baseline, risk, priority and supporting information", "evidence", False),
        ]),
        ("goals-targets-outcomes-preferences-and-shared-decisions", "Goals, targets, outcomes, preferences and shared decisions", ["SRC-003", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015"], [
            ("goal-identity-description-priority-lifecycle-achievement-source-and-addresses", "Goal identity, description, priority, lifecycle, achievement, source and addresses", "lifecycle", True),
            ("target-measure-value-timeframe-outcome-preference-and-decision-rationale", "Target measure, value, timeframe, outcome, preference and decision rationale", "measurement", False),
        ]),
    ]),
    ("participants-responsibility-authority-and-person-centred-governance", "Participants, responsibility, authority and person-centred governance", "Named roles, responsibility periods, participation and decision authority prevent a plan from becoming an unauthored list of intentions", [
        ("care-team-participants-roles-periods-and-responsibilities", "Care-team participants, roles, periods and responsibilities", ["SRC-001", "SRC-002", "SRC-004", "SRC-012", "SRC-013", "SRC-015"], [
            ("care-team-member-role-on-behalf-of-contact-availability-and-period", "Care-team member, role, on-behalf-of, contact, availability and period", "ownership", True),
            ("care-manager-managing-organization-custodian-author-contributor-and-reviewer", "Care manager, managing organization, custodian, author, contributor and reviewer", "authority", True),
        ]),
        ("subject-participation-consent-preferences-access-and-exceptions", "Subject participation, consent, preferences, access and exceptions", ["SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-017", "SRC-018"], [
            ("subject-representative-participation-shared-decision-and-disagreement", "Subject, representative, participation, shared decision and disagreement", "decision", False),
            ("consent-purpose-access-scope-redaction-emergency-and-legal-exception", "Consent, purpose, access scope, redaction, emergency and legal exception", "privacy", True),
        ]),
    ]),
    ("planned-activities-protocols-timing-and-coordination", "Planned activities, protocols, timing and coordination", "The plan groups intended activity references and coordination constraints while requests, tasks and executable protocols retain independent ownership", [
        ("activity-intent-request-links-definitions-and-deviations", "Activity intent, request links, definitions and deviations", ["SRC-001", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-015", "SRC-016"], [
            ("planned-activity-request-reference-intent-status-owner-and-focus", "Planned activity, request reference, intent, status, owner and focus", "requirement", True),
            ("protocol-order-set-plan-definition-instantiation-version-and-deviation", "Protocol, order set, plan-definition instantiation, version and deviation", "provenance", False),
        ]),
        ("timing-recurrence-dependencies-conditions-options-and-coordination", "Timing, recurrence, dependencies, conditions, options and coordination", ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-015", "SRC-016", "SRC-019"], [
            ("planned-window-schedule-recurrence-duration-deadline-and-flexibility", "Planned window, schedule, recurrence, duration, deadline and flexibility", "temporal", False),
            ("related-action-sequence-prerequisite-condition-selection-alternative-and-stop-rule", "Related action, sequence, prerequisite, condition, selection, alternative and stop rule", "constraint", False),
        ]),
    ]),
    ("realization-progress-evaluation-transitions-and-closure", "Realization, progress, evaluation, transitions and closure", "Observed delivery, evaluation and transfer evidence must be linked without being inferred from plan or episode status", [
        ("encounters-tasks-performed-events-progress-and-goal-evaluation", "Encounters, tasks, performed events, progress and goal evaluation", ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-008", "SRC-011", "SRC-015"], [
            ("encounter-task-request-and-performed-activity-reference-with-independent-state", "Encounter, task, request and performed-activity reference with independent state", "event", True),
            ("progress-note-observation-goal-evaluation-outcome-variance-and-uncertainty", "Progress note, observation, goal evaluation, outcome, variance and uncertainty", "validation", False),
        ]),
        ("referral-handoff-transfer-responsibility-transition-and-closure", "Referral, handoff, transfer, responsibility transition and closure", ["SRC-002", "SRC-004", "SRC-007", "SRC-008", "SRC-012", "SRC-013", "SRC-015", "SRC-019"], [
            ("referral-handoff-transfer-sender-receiver-acknowledgement-and-pending-work", "Referral, handoff, transfer, sender, receiver, acknowledgement and pending work", "process", True),
            ("episode-status-history-responsibility-period-closure-outcome-and-unresolved-items", "Episode status history, responsibility period, closure, outcome and unresolved items", "lifecycle", True),
        ]),
    ]),
    ("independent-lifecycles-correction-provenance-retention-and-projection", "Independent lifecycles, correction, provenance, retention and projection", "Safe agent use requires independent status axes, append-only correction, protected views and loss-aware mappings", [
        ("plan-and-episode-status-version-change-cancellation-and-correction", "Plan and episode status, version, change, cancellation and correction", ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-008", "SRC-018", "SRC-019"], [
            ("independent-plan-episode-goal-request-task-and-activity-status-axes", "Independent plan, episode, goal, request, task and activity status axes", "state", True),
            ("amend-replace-hold-revoke-cancel-entered-in-error-supersede-and-noncascade", "Amend, replace, hold, revoke, cancel, entered-in-error, supersede and non-cascade", "exception", True),
        ]),
        ("source-quality-privacy-retention-interoperability-and-agent-controls", "Source quality, privacy, retention, interoperability and agent controls", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019"], [
            ("source-confidence-provenance-disclosure-audit-legal-hold-retention-and-disposition", "Source confidence, provenance, disclosure, audit, legal hold, retention and disposition", "retention", True),
            ("fhir-ihe-openehr-who-nice-projection-version-maturity-loss-and-round-trip", "FHIR, IHE, openEHR, WHO and NICE projection, version, maturity, loss and round trip", "interoperability", False),
        ]),
    ]),
]


KINDS = ["identity", "classification", "relationship", "authority", "requirement", "constraint", "event", "temporal", "composition", "evidence", "ownership", "measurement", "exception", "provenance", "process", "validation", "privacy", "lifecycle", "quality", "security", "retention", "interoperability", "decision", "state"]


def finding(item, number, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(number + 7) % len(KINDS)], KINDS[(number + 15) % len(KINDS)]]
    questions = [
        {"id": f"{fid}-q01", "text": f"Which stable identities, record class, source-qualified assertions and explicit unknowns establish {low}?", "kind": kinds[0], "answer_data": ["identifiers and class", "source-qualified assertions", "unknown and not-applicable states"]},
        {"id": f"{fid}-q02", "text": f"Who proposed, authored, accepted, owns, performs, reviews or is affected by {low}, with which role, authority, preference and limits?", "kind": kinds[1], "answer_data": ["actors and roles", "authority and participation", "preferences, limits and exceptions"]},
        {"id": f"{fid}-q03", "text": f"Which authored, effective, planned, scheduled, occurrence, evaluation, transition, recorded, ingested and knowledge times apply to {low}, and how is it validated or corrected?", "kind": kinds[2], "answer_data": ["distinct care and record times", "validation, progress and uncertainty", "successor correction and retention"]},
    ]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {low} as source-qualified care-planning or episode context while preserving the distinctions among intent, responsibility, encounter, work item, performance, observation and outcome.",
        "source_refs": refs,
        "questions": questions,
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed data for {low} with constituent identity, source, authority, status, clinical time, record time, evidence and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned evidence for {low}.", "media_or_form": ["logical care-context assertion", "plan, episode, goal, participant, activity, transition, evaluation or projection record"], "serial": True, "identity_strategy": f"Aggregate ID plus independent plan, episode, goal, participation, action, transition or assertion ID for {fid}; patient, title, condition and date never identify the record alone.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles = []
    number = 0
    for bid, bname, rationale, layers in ROWS:
        rendered_layers = []
        for lid, lname, refs, items in layers:
            rendered_findings = []
            for item in items:
                number += 1
                rendered_findings.append(finding(item, number, refs))
            rendered_layers.append({"id": lid, "name": lname, "description": f"Groups source-qualified care context for {lname.lower()}.", "source_refs": refs, "findings": rendered_findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed care context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({ref for layer in layers for ref in layer[2]}), "layers": rendered_layers})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-care-context-aggregate", "Register care context aggregate", ["source records", "subject", "profile", "steward authority"], ["aggregate root and constituent slots"], ["stable identity, source, subject and boundary pass"], ["one aggregate links independent plan and episode records without collapsing them"], ["SRC-001", "SRC-002", "SRC-015", "SRC-018"]),
    ("create-or-revise-care-plan", "Create or revise care plan", ["care concerns", "goals", "participants", "planned activity references"], ["versioned plan record"], ["author, custodian, subject, intent, status, period and authority pass"], ["care intent is recorded without asserting execution or outcome"], ["SRC-001", "SRC-003", "SRC-004", "SRC-014"]),
    ("open-or-track-episode", "Open or track episode", ["subject", "managing organization", "care manager", "reason", "period"], ["versioned episode record and status event"], ["provider responsibility, source, identity and episode boundary pass"], ["responsibility tracking begins or changes without creating encounters"], ["SRC-002", "SRC-012", "SRC-013"]),
    ("establish-or-evaluate-goal", "Establish or evaluate goal", ["desired state", "target", "priority", "source", "evidence links"], ["goal or goal-evaluation assertion"], ["subject, goal identity, target semantics, evaluator and evidence pass"], ["desired state and observed achievement remain distinct"], ["SRC-003", "SRC-011", "SRC-014"]),
    ("bind-care-team-and-responsibilities", "Bind care team and responsibilities", ["participants", "roles", "on-behalf-of", "periods", "responsibilities"], ["attributable participation set"], ["identity, role, authority, availability and consent pass"], ["responsibility becomes explicit without changing participant masters"], ["SRC-004", "SRC-012", "SRC-014", "SRC-017"]),
    ("coordinate-planned-requests", "Coordinate planned requests", ["activity references", "dependencies", "conditions", "timing", "options"], ["coordination graph and validation report"], ["each request retains identity, intent, owner and status; dependency graph is valid"], ["coordination is recorded without executing requests or tasks"], ["SRC-001", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-016"]),
    ("record-progress-and-link-performance", "Record progress and link performance", ["plan", "episode", "external tasks", "encounters", "performed events", "observations"], ["progress and realization links"], ["source, occurrence, performer, observation and independent status pass"], ["delivery evidence is linked without being inferred from plan status"], ["SRC-001", "SRC-002", "SRC-007", "SRC-011", "SRC-015"]),
    ("handoff-transfer-or-close-care-context", "Handoff, transfer or close care context", ["current responsibility", "receiver", "pending work", "communication evidence", "closure reason"], ["transition, acknowledgement or closure event"], ["authority, continuity, unresolved items and receiving scope pass"], ["responsibility and status change without cascading into referenced records"], ["SRC-002", "SRC-004", "SRC-012", "SRC-013", "SRC-015"]),
    ("correct-hold-cancel-or-supersede", "Correct, hold, cancel or supersede", ["target constituent", "reason", "authority", "expected revision"], ["append-only transition or successor"], ["constituent-specific transition, provenance and non-cascade impact pass"], ["history remains visible and consumers can resolve the current head"], ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-018"]),
    ("project-retain-disclose-and-audit", "Project, retain, disclose and audit", ["aggregate", "target profile", "access and retention policy"], ["projection, disclosure, tombstone or disposition event"], ["mapping versions, maturity, loss, privacy, hold and idempotency pass"], ["context stays protected, reconstructable and explicit about loss"], ["SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019"]),
]


def functions():
    return [{"id": row[0], "name": row[1], "description": f"Governed operation to {row[1].lower()} without hidden mutation or execution of external clinical masters.", "inputs": row[2], "outputs": row[3], "preconditions": row[4], "effects": row[5], "source_refs": row[6]} for row in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Dimension owner and care-governance mandate",
                "Patient, practitioner, organization, condition, observation, encounter, consent, plan, episode, goal, care-team, request, task, performed-event, communication, provenance, audit and record registries",
                "Approved clinical, terminology, measurement, workflow, shared-decision, transition, privacy, retention and interoperability profiles",
                "Jurisdiction, organization, setting, specialty, subject-participation and agent-operation policies",
            ],
            "namespace_guidance": "Mint aggregate, plan, episode, goal, participant-role, coordination, progress, evaluation, transition, correction, disclosure and event IDs; preserve every authoritative source-system and clinical identifier.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize each plan and episode by authoritative source-system identifier, source organization and constituent kind; never by patient, condition, title or date alone.",
                "Keep planning, provider responsibility, encounter, goal, request authorization, task execution, performed activity, observation and clinical outcome distinct.",
            ],
            "patch_rules": [
                "Extensions declare jurisdiction, setting, specialty, terminology, workflow, consent, privacy, retention and interoperability effects.",
                "Released plan, episode, goal, participation, coordination, transition and evaluation records are immutable; corrections create linked successors.",
                "Never silently change subject, concern, goal, target, preference, participant, authority, activity, dependency, period, status, outcome, access or provenance.",
            ],
            "compatibility_rules": [
                "Ignore additive fields only when identity, constituent kind, subject, responsibility, intent, status, time, authority, evidence and provenance survive.",
                "Every projection pins profile, terminology and source versions and declares information loss and standards maturity.",
            ],
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative master-system identifier for each care plan, episode, goal, participant assertion or transition, qualified by source organization and record kind.",
                "Governed globally resolvable care-context record IRI.",
                "Dimension UUID when neither preceding identifier exists.",
            ],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish authored, effective, planned, scheduled, occurrence, evaluation, handoff, transition, recorded, ingested and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {aggregate-id}--{plan-episode-goal-action-transition-or-assertion-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, constituent kind, subject binding, source and profile versions, actor, event and knowledge times, status, access marking and provenance.",
        },
        "policies": [
            "The aggregate does not own Patient, Practitioner, Organization, Condition, Observation, Encounter, Consent, PlanDefinition, Request, Task, Appointment, Procedure, Medication, Communication, AdverseEvent, Provenance, Audit or Record masters.",
            "Plan, episode, goal, request, task, encounter, performed event, observation and outcome remain separate assertions with independent states and times.",
            "Completed plan or episode status never proves that every activity occurred, every goal was achieved, care was effective or no harm occurred.",
            "Agents cannot diagnose, authorize care, change treatment, assign responsibility, execute clinical work, infer success, disclose protected data or dispose records outside explicit clinical and policy authority.",
        ],
        "crud": {
            "read": ["Resolve purpose, aggregate profile, plan and episode identities, subject, concerns, goals, participants, activity references, responsibilities, progress, transitions, lineage, holds and projection loss."],
            "create": ["Bind stable aggregate and constituent identity, source, subject, responsible authority, record kind, status and effective time before recording care intent or responsibility."],
            "update": ["Append successor plan, episode, goal, participation, activity, progress, evaluation, handoff, closure and correction events with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply clinical-record, continuity, privacy, legal-hold and adopting-Dimension retention policy; retire or tombstone only the aggregate or named constituent without cascading to Patient, Condition, Encounter, Request, Task, Procedure, Medication, Observation or other masters, and let the external records policy execute physical disposition."],
        },
        "roles": [
            {"name": "Care context aggregate steward", "responsibilities": ["Own aggregate boundary, namespace, composition and quality rules."]},
            {"name": "Plan author or custodian", "responsibilities": ["Own care-plan intent, concerns, goals, participants, activity references and revision basis within authority."]},
            {"name": "Episode manager or managing organization", "responsibilities": ["Own provider-responsibility periods, episode status and transfer evidence."]},
            {"name": "Subject or authorized representative", "responsibilities": ["Contribute goals, preferences, decisions, disagreement and consent within applicable capacity and policy."]},
            {"name": "Care-team participant", "responsibilities": ["Own attributable role, availability, acknowledgement and progress contributions within scope."]},
            {"name": "Clinical reviewer", "responsibilities": ["Review concerns, goals, targets, progress, variance and closure evidence without inventing outcomes."]},
            {"name": "Interoperability steward", "responsibilities": ["Own versioned FHIR, IHE and other projections with maturity and loss declarations."]},
            {"name": "Privacy, records and assurance steward", "responsibilities": ["Own protected views, disclosures, holds, retention and auditability."]},
        ],
        "access": {
            "default_rule": "Deny care-plan, episode and related clinical context unless a purpose-bound policy permits the minimum necessary view.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Declared subject, representative, care team, emergency, public-health, research, regulator, court or legally authorized access must cite authority, scope, purpose and time limit where applicable and must be logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, aggregate and constituent, operation, authority, policy, RFC 3339 time, affected fields, source revision and outcome without duplicating unnecessary clinical content."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": [
                "Read Dimension clinical, shared-decision, scope-of-practice, consent, privacy, access, correction, records and agent policies.",
                "Read this aggregate and linked patient, condition, observation, encounter, consent, goal, care-team, request, task, procedure, medication, communication, provenance, audit and record models before mutation.",
            ],
        },
    }


def coverage():
    dims = ["identity", "classification and definition", "direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability"]
    return {
        "claim": "Covers a source-qualified care-context aggregate that links but does not collapse subject-specific care planning, provider episode responsibility, goals, participants, intended activity references, progress evidence, transitions, correction, protected use and projection.",
        "confidence": "medium",
        "checklist": [{"dimension": dim, "status": "covered", "notes": f"{dim.capitalize()} is explicit; specialty, jurisdiction, institution, candidate relations and release-pinned validation remain held where applicable."} for dim in dims],
        "known_omissions": [
            "Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.",
            "WM-ACT-049 REFERENCE WM-LIV-021 and CONTAINS WM-ACT-047 and WM-ACT-048 are candidate metadata and not approved composition edges.",
            "Oncology, mental health, maternity, pediatric, geriatric, rehabilitation, palliative, public-health, social-care, veterinary and research planning require specialty profiles.",
            "FHIR R5 planning resources are Trial Use at varied maturity; IHE DCP is an implementation profile and openEHR Task Planning Release-1.7.0 is retired, so mappings require release-pinned testing.",
        ],
        "conflicts": [
            "A care plan is planning, while an episode tracks provider responsibility and an encounter records an activity; they are not interchangeable.",
            "Plan, goal, request, task, performed event and observation statuses are independent and cannot be silently synchronized.",
            "Completed plan or episode status does not prove activity completion, goal achievement, clinical effectiveness, continuity or absence of harm.",
        ],
        "regional_assumptions": [
            "Care authority, capacity, guardianship, consent, scope of practice, assignment, transfer, reporting, retention and disclosure depend on jurisdiction and setting.",
            "NICE NG197 is an England and Wales guideline and IHE DCP is an interoperability profile, not universal clinical or legal policy.",
            "Local care pathways, terminologies, role codes, responsibility rules, availability and escalation practices require versioned organization profiles.",
        ],
        "adversarial_checks": [
            "Reject an aggregate or constituent without stable identity, record kind, source, subject, responsible authority, status, effective time and lineage head.",
            "Reject a care plan represented as performed care, episode represented as encounter, goal represented as observation, or completed represented as successful.",
            "Reject activity coordination that loses request, task or performed-event identity, intent, owner, status, time, dependency or source.",
            "Reject transfer or closure that loses pending work, unresolved goals, sender, receiver, acknowledgement, responsibility period or communication evidence.",
            "Reject autonomous diagnosis, treatment authorization, assignment, execution, clinical inference, disclosure or disposition outside explicit authority.",
        ],
    }


def build():
    model = {
        "registry_id": "vr.wm-act-049",
        "model_id": "WM-ACT-049",
        "name": "Care Plan / Episode",
        "entry_kind": "aggregate",
        "purpose": "Represent a governed care-context aggregate so agents can distinguish subject-specific planning from provider episode responsibility while connecting goals, participants, intended activities, progress and transitions without treating intent as performance or outcome.",
        "scope_statement": "Owns aggregate identity and links between a care-plan record and an episode-of-care record, plus subject-specific goals, participant-role assertions, coordination context, progress summaries, transition assertions and correction lineage. Each constituent keeps independent identity, source, status, authority and times. Patient, practitioner, organization, condition, observation, encounter, consent, reusable protocol, request, task, appointment, procedure, medication, communication, adverse-event, provenance, audit and record masters remain external.",
        "in_scope": [
            "Aggregate, care-plan and episode identity; subject and setting; concerns, goals, targets and preferences; care-team and responsibility bindings; intended activity references and dependencies",
            "Independent statuses and times; progress and performed-event links; referral, handoff, transfer and closure context; correction, privacy, retention and loss-aware projections",
        ],
        "out_of_scope": [
            "Independent patient, practitioner, organization, condition, observation, encounter, consent, protocol, request, task, appointment, procedure, medication, communication, adverse-event, provenance, audit and record lifecycles",
            "Treating a plan as performed care, an episode as an encounter, a goal as an observation, a status as clinical outcome or an association as causation",
            "Providing diagnosis, care authorization, treatment change, clinical assignment, workflow execution, outcome inference or medical advice",
        ],
        "boundary_notes": [
            {"neighbor": "FHIR CarePlan and EpisodeOfCare", "distinction": "CarePlan is a planning request and EpisodeOfCare tracks provider association and responsibility. Each retains its own identity, status and period inside the aggregate.", "source_refs": ["SRC-001", "SRC-002"]},
            {"neighbor": "Encounter, Task, Request and performed clinical events", "distinction": "Encounters record activities, Tasks track work, Requests authorize intent and performed-event records evidence occurrence. The aggregate stores typed references and coordination context only.", "source_refs": ["SRC-001", "SRC-002", "SRC-007", "SRC-008"]},
            {"neighbor": "Goal, Condition, ClinicalImpression and Observation", "distinction": "Goals own desired states, conditions own concerns, clinical impressions own assessment reasoning and observations own measurements. The aggregate links them without copying clinical assertion lifecycles.", "source_refs": ["SRC-003", "SRC-009", "SRC-010", "SRC-011"]},
            {"neighbor": "CareTeam, patient, practitioner and organization masters", "distinction": "CareTeam owns dynamic participant membership and roles; party masters own identity. The aggregate records plan and episode role bindings, responsibility and effective periods.", "source_refs": ["SRC-001", "SRC-002", "SRC-004"]},
            {"neighbor": "PlanDefinition, RequestOrchestration and openEHR Task Planning", "distinction": "Reusable protocols and detailed executable orchestration stay external. The aggregate records versioned instantiation, coordination constraints and deviations; the openEHR source is retired and is not a conformance target.", "source_refs": ["SRC-005", "SRC-006", "SRC-008", "SRC-016"]},
            {"neighbor": "WM-LIV-021, WM-ACT-047 and WM-ACT-048", "distinction": "Condition, procedure and medication references may supply care context, but all three registry relations remain candidate, transfer no lifecycle ownership and permit no cascade mutation.", "source_refs": ["SRC-001", "SRC-002", "SRC-010"]},
        ],
    }
    composition = [
        {"target": "WM-LIV-021 Disease / Condition", "relation": "REFERENCE", "purpose": "Record the candidate condition relation as clinical goal context without approving the edge or copying condition lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-010"]},
        {"target": "WM-ACT-047 Medical Procedure", "relation": "REFERENCE", "purpose": "Record intended or performed procedure references while the candidate containment edge and all cascade semantics remain deferred.", "required": False, "source_refs": ["SRC-001", "SRC-007", "SRC-008"]},
        {"target": "WM-ACT-048 Medication Order / Administration", "relation": "REFERENCE", "purpose": "Record medication request and administration references while the candidate containment edge and all medication lifecycles remain deferred.", "required": False, "source_refs": ["SRC-001", "SRC-007", "SRC-008"]},
        {"target": "Patient, Practitioner, Organization, Condition, Observation, Encounter, Consent, CareTeam, Goal, Request, Task, Appointment, Communication, AdverseEvent, Provenance, Audit and Record models", "relation": "REFERENCE", "purpose": "Resolve authoritative subjects, actors, clinical assertions, work, evidence, communication and governance without copying their lifecycles.", "required": True, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-017", "SRC-018"]},
        {"target": "FHIR R5, IHE Dynamic Care Planning, openEHR Task Planning, WHO continuity guidance and NICE NG197", "relation": "ALIGN", "purpose": "Project version-pinned clinical, continuity, shared-decision and workflow views with maturity, retirement, jurisdiction and information-loss declarations.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    RUN.joinpath("codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
