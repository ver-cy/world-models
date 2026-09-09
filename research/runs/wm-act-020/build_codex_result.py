#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-ACT-020."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED_AT = "2026-09-06T00:00:00Z"


SOURCES = [
    {
        "id": "SRC-001",
        "title": "NIST SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management",
        "organization": "National Institute of Standards and Technology",
        "url": "https://csrc.nist.gov/pubs/sp/800/61/r3/final",
        "version_or_date": "Final, April 2025",
        "source_type": "public-authority",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Provides the current NIST cybersecurity-incident definition and risk-management context while separating the incident from response activities.",
    },
    {
        "id": "SRC-002",
        "title": "Computer Security Incident glossary entry",
        "organization": "National Institute of Standards and Technology",
        "url": "https://csrc.nist.gov/glossary/term/Computer_Security_Incident",
        "version_or_date": "Current glossary entry accessed 2026-09-06",
        "source_type": "public-authority",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Records the occurrence-based definition, including actual or imminent jeopardy and policy or law violations.",
    },
    {
        "id": "SRC-003",
        "title": "RFC 7970: The Incident Object Description Exchange Format Version 2",
        "organization": "Internet Engineering Task Force",
        "url": "https://www.rfc-editor.org/rfc/rfc7970.html",
        "version_or_date": "RFC 7970, November 2016",
        "source_type": "standard",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Defines incident identity, alternative IDs, status, times, assessment, history, event data, contacts, restrictions and exchange semantics.",
    },
    {
        "id": "SRC-004",
        "title": "STIX Version 2.1",
        "organization": "OASIS Open",
        "url": "https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html",
        "version_or_date": "OASIS Standard, 10 June 2021",
        "source_type": "standard",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Supplies CTI identity, versioning, marking and relationship rules, while explicitly declaring its Incident object a limited extension point.",
    },
    {
        "id": "SRC-005",
        "title": "CSIRT Services Framework Version 2.1",
        "organization": "Forum of Incident Response and Security Teams",
        "url": "https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1",
        "version_or_date": "Version 2.1",
        "source_type": "first-party-doc",
        "primary_source": True,
        "authority_tier": 2,
        "accessed_at": ACCESSED_AT,
        "relevance": "Distinguishes event qualification, incident analysis, scope, impact, correlation, evidence and response-service execution.",
    },
    {
        "id": "SRC-006",
        "title": "Directive (EU) 2022/2555 on measures for a high common level of cybersecurity across the Union",
        "organization": "European Union",
        "url": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj",
        "version_or_date": "Directive (EU) 2022/2555, 14 December 2022",
        "source_type": "legislation",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Defines incident, near miss and large-scale incident and provides significance and reporting-information criteria for governed bindings.",
    },
    {
        "id": "SRC-007",
        "title": "Regulation (EU) 2016/679 General Data Protection Regulation",
        "organization": "European Union",
        "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj",
        "version_or_date": "Regulation (EU) 2016/679, consolidated official text accessed 2026-09-06",
        "source_type": "legislation",
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED_AT,
        "relevance": "Defines personal-data breach and the facts, effects and remedial-action information that controllers must document.",
    },
]


# Bundle: id, name, description, rationale, sources, layers.
# Layer: id, name, description, sources, findings.
# Finding: id, name, description, primary question kind, sources,
#          value kind, required, owns serial artifact.
STRUCTURE = [
    (
        "identity-and-determination", "Identity and determination",
        "Establishes the incident record, the qualification decision and identity continuity.",
        "A potential event becomes a cyber incident only through evidence-backed qualification under a declared definition and authority.",
        ["SRC-001", "SRC-002", "SRC-003", "SRC-005"],
        [
            ("incident-identity", "Incident identity", "Stable identity, aliases and cross-system correlation.", ["SRC-003", "SRC-004"], [
                ("authoritative-incident-identity", "Authoritative incident identity", "The master-system identifier, record authority, version and namespace of the incident aggregate.", "identity", ["SRC-003", "SRC-004"], "identifier", True, True),
                ("aliases-and-correlation-keys", "Aliases and correlation keys", "Alternative incident identifiers, external references and bounded correlation keys used across organizations and tools.", "interoperability", ["SRC-003", "SRC-004"], "collection", False, False),
            ]),
            ("qualification-and-declaration", "Qualification and declaration", "The evidence-based transition from reported event to declared incident.", ["SRC-001", "SRC-002", "SRC-005", "SRC-006"], [
                ("incident-definition-binding", "Incident definition binding", "The pinned organizational, statutory or profile definition against which the occurrence is qualified.", "classification", ["SRC-001", "SRC-002", "SRC-006"], "reference", True, False),
                ("qualification-and-declaration-decision", "Qualification and declaration decision", "The determination, authority, rationale, confidence and effective time for declaring, rejecting or revoking incident status.", "decision", ["SRC-001", "SRC-005"], "object", True, True),
            ]),
            ("identity-continuity", "Identity continuity", "Duplicate resolution, merge, split, supersession and reopening.", ["SRC-003", "SRC-004", "SRC-005"], [
                ("duplicate-merge-and-split", "Duplicate, merge and split", "Governed relations and rationale when reports or event groups are deduplicated, merged into one incident or split into several incidents.", "relationship", ["SRC-003", "SRC-004", "SRC-005"], "collection", False, True),
                ("supersession-and-reopening", "Supersession and reopening", "Identity-preserving rules for a corrected successor, revoked determination, recurring activity or reopened incident record.", "lifecycle", ["SRC-003", "SRC-004"], "object", False, True),
            ]),
        ],
    ),
    (
        "occurrence-and-chronology", "Occurrence and chronology",
        "Represents constituent events, ordering and the distinct clocks by which an incident becomes known.",
        "Incident chronology is evidence about what occurred, not the action log of the response process.",
        ["SRC-001", "SRC-003", "SRC-005"],
        [
            ("constituent-events", "Constituent events", "Incident membership and relationships among observed cyber events.", ["SRC-003", "SRC-005"], [
                ("event-membership", "Event membership", "References to cyber events accepted, suspected or rejected as constituents of the incident, with membership rationale.", "composition", ["SRC-003", "SRC-005"], "collection", True, False),
                ("causal-and-sequence-relations", "Causal and sequence relations", "Observed ordering, concurrency, dependency and claimed causal links among incident events without promoting hypotheses to facts.", "relationship", ["SRC-003", "SRC-005"], "collection", False, False),
            ]),
            ("incident-time", "Incident time", "Occurrence, detection, observation, declaration and knowledge times.", ["SRC-001", "SRC-003", "SRC-005", "SRC-006"], [
                ("temporal-markers", "Temporal markers", "Distinct start, end, detection, report, declaration, recovery, observation and ingestion timestamps with uncertainty.", "temporal", ["SRC-003", "SRC-005", "SRC-006"], "object", True, True),
                ("ongoing-imminent-and-recurring", "Ongoing, imminent and recurring occurrence", "Whether compromise is ongoing, imminent, intermittent or recurring, including the evidence and interval basis.", "state", ["SRC-001", "SRC-002", "SRC-006"], "object", False, False),
            ]),
        ],
    ),
    (
        "affected-scope", "Affected scope",
        "Describes direct and propagated reach using governed references and explicit assertion status.",
        "The incident owns scope assertions but not the lifecycle or direct properties of affected systems, people, organizations or information assets.",
        ["SRC-003", "SRC-005", "SRC-006", "SRC-007"],
        [
            ("affected-subjects", "Affected subjects", "Directly affected technical and organizational subjects.", ["SRC-003", "SRC-005", "SRC-007"], [
                ("affected-systems-services-and-networks", "Affected systems, services and networks", "References to systems, services, networks, accounts and computer-controlled infrastructure with role and affected interval.", "relationship", ["SRC-003", "SRC-005", "SRC-006"], "collection", True, False),
                ("affected-information-identities-and-parties", "Affected information, identities and parties", "References and bounded counts for information, records, credentials, people and organizations affected or exposed.", "privacy", ["SRC-003", "SRC-005", "SRC-007"], "collection", False, False),
            ]),
            ("scope-reach-and-certainty", "Scope reach and certainty", "Dependency propagation and changing confidence in affected-scope claims.", ["SRC-003", "SRC-005", "SRC-006"], [
                ("dependency-and-supply-chain-reach", "Dependency and supply-chain reach", "Potential or confirmed propagation through service, supplier, tenant, identity and data dependencies.", "relationship", ["SRC-005", "SRC-006"], "collection", False, False),
                ("scope-assertion-status", "Scope assertion status", "Confirmed, suspected, disputed or disproven affected-scope assertions with assessor, method, confidence and history.", "quality", ["SRC-003", "SRC-005"], "collection", True, True),
            ]),
        ],
    ),
    (
        "security-effect-and-impact", "Security effect and impact",
        "Separates the security property affected from technical, operational, human and legal consequences.",
        "Severity and regulatory significance are versioned assessments, not universal intrinsic properties of the incident.",
        ["SRC-001", "SRC-003", "SRC-005", "SRC-006", "SRC-007"],
        [
            ("security-effects", "Security effects", "Compromised security properties and policy or legal violations.", ["SRC-001", "SRC-002", "SRC-003", "SRC-006"], [
                ("confidentiality-integrity-availability-authenticity", "Confidentiality, integrity, availability and authenticity", "Observed or threatened compromise of security properties, affected objects, degree and supporting evidence.", "security", ["SRC-001", "SRC-002", "SRC-006"], "collection", True, True),
                ("policy-law-and-authority-effect", "Policy, law and authority effect", "The alleged or confirmed security-policy, acceptable-use, legal or lawful-authority condition implicated by the occurrence.", "authority", ["SRC-001", "SRC-002", "SRC-006", "SRC-007"], "collection", False, False),
            ]),
            ("impact-domains", "Impact domains", "Consequences beyond the immediate technical effect.", ["SRC-003", "SRC-005", "SRC-006", "SRC-007"], [
                ("operational-safety-and-privacy-impact", "Operational, safety and privacy impact", "Service disruption, physical-safety implications and effects on rights or personal data, with actual versus potential status.", "measurement", ["SRC-003", "SRC-005", "SRC-006", "SRC-007"], "collection", False, True),
                ("financial-societal-and-cross-border-impact", "Financial, societal and cross-border impact", "Material and non-material damage, financial loss, constituency reach and cross-border effect assertions.", "measurement", ["SRC-003", "SRC-005", "SRC-006"], "collection", False, True),
            ]),
            ("severity-and-significance", "Severity and significance", "Profile-bound prioritization and regulatory classifications.", ["SRC-003", "SRC-005", "SRC-006", "SRC-007"], [
                ("severity-assessment", "Severity assessment", "Severity or priority value together with scheme, version, assessor, inputs, confidence and effective time.", "classification", ["SRC-003", "SRC-005"], "object", False, True),
                ("regulatory-significance-bindings", "Regulatory significance bindings", "Jurisdiction and regime-specific determinations such as significant incident or personal-data breach, with threshold evidence and obligation reference.", "requirement", ["SRC-006", "SRC-007"], "collection", False, True),
            ]),
        ],
    ),
    (
        "mechanism-and-attribution", "Mechanism and attribution",
        "Records evidence-backed causal, exploit, technique and actor assertions without absorbing neighboring security-object lifecycles.",
        "Causation and attribution often remain contested and must retain alternatives, confidence and revision history.",
        ["SRC-003", "SRC-004", "SRC-005"],
        [
            ("cause-and-exploit", "Cause and exploit", "Root-cause hypotheses and referenced weaknesses or exposures.", ["SRC-003", "SRC-005"], [
                ("cause-and-enabling-condition-hypotheses", "Cause and enabling-condition hypotheses", "Competing root-cause, misconfiguration, failure, human-action and enabling-condition hypotheses with evidence and confidence.", "provenance", ["SRC-003", "SRC-005"], "collection", False, True),
                ("vulnerability-and-exposure-references", "Vulnerability and exposure references", "References to exploited or suspected vulnerabilities and concrete exposures without owning disclosure, scoring or remediation state.", "relationship", ["SRC-003", "SRC-005"], "collection", False, False),
            ]),
            ("technique-indicator-and-attribution", "Technique, indicator and attribution", "Observed mechanisms and bounded claims about responsible activity.", ["SRC-003", "SRC-004", "SRC-005"], [
                ("technique-indicator-and-observable-references", "Technique, indicator and observable references", "References to attack patterns, indicators, observables, tools and infrastructure with observed role and time.", "evidence", ["SRC-003", "SRC-004"], "collection", False, False),
                ("actor-campaign-and-attribution-claims", "Actor, campaign and attribution claims", "Competing links to actors, campaigns or intrusion sets with source, analytic basis, confidence and disclosure marking.", "provenance", ["SRC-003", "SRC-004"], "collection", False, True),
            ]),
        ],
    ),
    (
        "evidence-provenance-and-governance", "Evidence, provenance and governance",
        "Makes observations, evidence references, epistemic status and controlled disclosure explicit.",
        "Incident data is sensitive and mutable; agents must preserve source, evidence integrity, uncertainty, access and retention without duplicating external evidence or audit systems.",
        ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007"],
        [
            ("observations-and-evidence", "Observations and evidence", "Source reports, technical observations and preserved evidence bindings.", ["SRC-003", "SRC-004", "SRC-005"], [
                ("reports-observations-and-discovery", "Reports, observations and discovery", "Source reports, discovery methods, observations, sensor or analyst provenance, reliability and observation conditions.", "provenance", ["SRC-003", "SRC-005"], "collection", True, True),
                ("evidence-integrity-and-custody-references", "Evidence integrity and custody references", "References to forensic artifacts and custody records with digest, collector, preservation state and access boundary.", "evidence", ["SRC-003", "SRC-005"], "collection", False, False),
            ]),
            ("epistemic-and-disclosure-controls", "Epistemic and disclosure controls", "Truth status, markings, access, retention and projections.", ["SRC-003", "SRC-004", "SRC-005", "SRC-007"], [
                ("fact-assessment-allegation-and-unknown", "Fact, assessment, allegation and unknown", "Explicit epistemic status for each material assertion, including contradiction sets and the authority able to resolve them.", "quality", ["SRC-003", "SRC-004", "SRC-005"], "object", True, True),
                ("disclosure-access-privacy-and-retention", "Disclosure, access, privacy and retention", "Information marking, permitted projection, privacy constraints, legal hold and retention or deletion binding.", "access", ["SRC-003", "SRC-004", "SRC-006", "SRC-007"], "object", True, True),
            ]),
        ],
    ),
    (
        "state-resolution-and-federation", "State, resolution and federation",
        "Tracks incident-owned factual state and closure while connecting external response cases and exchange representations.",
        "Incident state must stay distinct from responder workflow state and from legal or business claims that are owned elsewhere.",
        ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006"],
        [
            ("incident-state-and-resolution", "Incident state and resolution", "Current incident condition, impact cessation and residual exposure.", ["SRC-001", "SRC-003", "SRC-005"], [
                ("incident-factual-state", "Incident factual state", "Profile-bound incident state, allowed transition, triggering evidence, actor and effective time, separate from response-task status.", "state", ["SRC-003", "SRC-005"], "object", True, True),
                ("impact-cessation-residual-exposure-and-recurrence", "Impact cessation, residual exposure and recurrence", "Evidence that harmful effects ceased or persist, remaining exposure, recurrence indicators and uncertainty.", "validation", ["SRC-001", "SRC-003", "SRC-005"], "object", False, True),
            ]),
            ("closure-and-external-bindings", "Closure and external bindings", "Closure basis, response-case linkage and exchange mappings.", ["SRC-003", "SRC-004", "SRC-005", "SRC-006"], [
                ("closure-reclassification-and-disposition", "Closure, reclassification and disposition", "The evidence-backed decision to close, revoke, reclassify or reopen the incident and its unresolved facts or obligations.", "lifecycle", ["SRC-003", "SRC-005"], "object", False, True),
                ("response-case-and-federation-bindings", "Response-case and federation bindings", "References to response cases, reporting workflows and external incident representations with mapping, projection and correlation rules.", "interoperability", ["SRC-003", "SRC-004", "SRC-005", "SRC-006"], "collection", False, False),
            ]),
        ],
    ),
]


KIND_CYCLE = [
    "definition", "identity", "classification", "composition", "relationship",
    "state", "lifecycle", "temporal", "spatial", "provenance", "ownership",
    "authority", "requirement", "constraint", "process", "event", "measurement",
    "evidence", "quality", "validation", "security", "privacy", "retention",
    "access", "exception", "interoperability", "decision",
]


def build_finding(raw: tuple, ordinal: int) -> dict:
    finding_id, name, description, primary_kind, refs, value_kind, required, owns_artifact = raw
    kinds = [
        primary_kind,
        KIND_CYCLE[(ordinal * 3 + 7) % len(KIND_CYCLE)],
        KIND_CYCLE[(ordinal * 7 + 13) % len(KIND_CYCLE)],
    ]
    for position in range(1, 3):
        while kinds[position] in kinds[:position]:
            kinds[position] = KIND_CYCLE[(KIND_CYCLE.index(kinds[position]) + 1) % len(KIND_CYCLE)]
    questions = [
        {
            "id": f"{finding_id}-q01",
            "text": f"What is currently asserted about {name.lower()} for this cyber incident, and is it confirmed, suspected, disputed or unknown?",
            "kind": kinds[0],
            "answer_data": [name, "epistemic status", "applicable scope or explicit unknown"],
        },
        {
            "id": f"{finding_id}-q02",
            "text": f"Which source, observer or authority supports {name.lower()}, at what event and observation times, and with what confidence?",
            "kind": kinds[1],
            "answer_data": ["source or authority reference", "event and observation timestamps", "confidence and evidence reference"],
        },
        {
            "id": f"{finding_id}-q03",
            "text": f"Which validation, contradiction or change rule can revise {name.lower()} without destroying its history?",
            "kind": kinds[2],
            "answer_data": ["validation or conflict rule", "authorized revision event", "predecessor, successor or counterclaim reference"],
        },
    ]
    artifacts = []
    rationale = (
        "This finding stores only typed references and incident-local bindings; the referenced model owns the artifact payload and lifecycle."
    )
    if owns_artifact:
        artifacts = [{
            "id": f"{finding_id}-artifact",
            "name": f"{name} record",
            "description": f"Versioned incident-owned record supporting {name.lower()} with provenance and access marking.",
            "media_or_form": ["structured incident record", "signed or controlled statement", "resolvable evidence index"],
            "serial": True,
            "identity_strategy": "Authoritative incident master-system identifier first; otherwise a Dimension-governed UUID or ULID.",
            "source_refs": refs,
        }]
        rationale = None
    return {
        "id": finding_id,
        "name": name,
        "description": description,
        "source_refs": refs,
        "questions": questions,
        "data_elements": [{
            "id": f"{finding_id}-data",
            "name": f"{name} assertion",
            "description": f"Structured incident-local answer data for {name.lower()}, including status, effective time and provenance where applicable.",
            "value_kind": value_kind,
            "cardinality": "1" if required else "0..1",
            "required": required,
            "source_refs": refs,
        }],
        "artifacts": artifacts,
        "inline_only_rationale": rationale,
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
            layers.append({
                "id": layer_id,
                "name": layer_name,
                "description": layer_description,
                "source_refs": layer_refs,
                "findings": findings,
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
    ("register-potential-incident", "Register potential incident", "Create a non-confirmed incident candidate from a report or event cluster without claiming qualification.", ["report or event references", "receiving authority"], ["potential incident record"], ["authorized intake purpose exists"], ["candidate identity and provenance are recorded"], ["SRC-003", "SRC-005"]),
    ("qualify-and-declare-incident", "Qualify and declare incident", "Evaluate the candidate against a pinned definition and record the authorized determination.", ["candidate record", "evidence", "definition binding"], ["qualification decision", "declared incident revision"], ["qualified authority and evidence are available"], ["incident status is confirmed, rejected or remains uncertain with rationale"], ["SRC-001", "SRC-002", "SRC-005", "SRC-006"]),
    ("link-constituent-event", "Link constituent event", "Add or remove a typed event membership assertion with evidence and historical trace.", ["incident", "event reference", "membership rationale"], ["event membership revision"], ["incident and event identities resolve"], ["incident chronology and scope can be recomputed"], ["SRC-003", "SRC-005"]),
    ("merge-or-split-incident", "Merge or split incident", "Resolve duplicate or over-grouped incident identities without losing prior references.", ["incident identities", "correlation evidence", "authority"], ["merge or split decision", "successor identity relations"], ["identity authority and conflict policy permit the decision"], ["aliases and predecessor records remain resolvable"], ["SRC-003", "SRC-004", "SRC-005"]),
    ("revise-affected-scope", "Revise affected scope", "Add, confirm, dispute or remove an affected-scope assertion as knowledge changes.", ["incident", "subject references", "scope evidence"], ["scope assessment revision"], ["source and observation time are available"], ["current and historical scope assertions remain distinguishable"], ["SRC-003", "SRC-005", "SRC-006", "SRC-007"]),
    ("assess-impact-and-significance", "Assess impact and significance", "Record technical and nontechnical impact, severity and profile-specific significance without universalizing a score.", ["incident", "impact evidence", "assessment profiles"], ["impact assessment", "significance bindings"], ["assessor authority and scheme versions resolve"], ["actual and potential impacts remain separately traceable"], ["SRC-003", "SRC-005", "SRC-006", "SRC-007"]),
    ("record-causal-or-attribution-hypothesis", "Record causal or attribution hypothesis", "Add an evidence-backed, confidence-bearing explanation or attribution without promoting it to fact.", ["incident", "hypothesis", "supporting and contradicting evidence"], ["versioned hypothesis assertion"], ["epistemic status is explicit"], ["competing explanations remain visible"], ["SRC-003", "SRC-004", "SRC-005"]),
    ("transition-incident-factual-state", "Transition incident factual state", "Change the incident-owned condition under a pinned state profile and triggering evidence.", ["incident", "current state", "proposed state", "evidence"], ["state transition record"], ["transition and actor are authorized"], ["incident state changes without changing response-task state"], ["SRC-003", "SRC-005"]),
    ("bind-response-case", "Bind response case", "Reference the independently governed incident-response case that handles this incident.", ["incident", "response case reference"], ["typed incident-to-response binding"], ["both identities resolve and disclosure policy allows the link"], ["handling workflow stays outside the incident aggregate"], ["SRC-001", "SRC-005"]),
    ("issue-incident-projection", "Issue incident projection", "Produce a minimum authorized view for coordination, reporting or threat-intelligence exchange.", ["incident revision", "recipient and purpose", "projection policy"], ["digest-pinned incident projection"], ["access and disclosure decision permits release"], ["sensitive fields are minimized and projection provenance is recorded"], ["SRC-003", "SRC-004", "SRC-006", "SRC-007"]),
]


def build() -> dict:
    return {
        "schema_version": "1.0.0",
        "model": {
            "registry_id": "vr.wm-act-020",
            "model_id": "WM-ACT-020",
            "name": "Cyber Incident",
            "entry_kind": "aggregate",
            "purpose": "Represent an occurrence or linked set of occurrences determined to have actually or imminently compromised protected digital systems, information, services or computer-controlled infrastructure, together with evolving evidence-backed scope, impact and resolution facts.",
            "scope_statement": "Owns incident identity, qualification, constituent-event grouping, chronology, affected-scope assertions, security effects, impact assessments, hypotheses, factual state, evidence indexes, disclosure controls and closure decisions while referencing response workflow and neighboring security objects.",
            "in_scope": [
                "Incident identity, qualification authority, chronology, affected scope, security effects, impact and factual lifecycle",
                "Evidence-backed cause and attribution hypotheses, incident-owned assessments, external bindings and controlled projections",
                "Typed references to vulnerabilities, events, indicators, actors, systems, evidence and response cases",
            ],
            "out_of_scope": [
                "Incident-response workflow, responder tasks, containment or recovery execution, notifications, playbooks and lessons-learned processes",
                "Vulnerability disclosure, scoring and remediation lifecycle or the lifecycle of threats, indicators, controls, assets, people and organizations",
                "Generic evidence custody, access enforcement, audit persistence and legal adjudication beyond incident-local bindings",
            ],
            "boundary_notes": [
                {"neighbor": "Cyber event or alert", "distinction": "An event or alert is an observation or signal; a cyber incident is a qualified occurrence aggregate that meets a pinned definition and carries a governed declaration decision.", "source_refs": ["SRC-001", "SRC-002", "SRC-005"]},
                {"neighbor": "Cyber incident response", "distinction": "The incident represents what happened and what is currently known; response cases, tasks and mitigation or recovery execution are independently governed and linked by reference.", "source_refs": ["SRC-001", "SRC-005"]},
                {"neighbor": "Vulnerability or exposure", "distinction": "A vulnerability or exposure may enable an incident, but its disclosure, scoring, affected-version and remediation lifecycle stays in WM-SFT-006 or another authoritative security model.", "source_refs": ["SRC-003", "SRC-005"]},
                {"neighbor": "Personal-data breach or significant incident", "distinction": "These are regime-specific classifications of facts and impact; the incident stores a versioned determination binding but does not own the reporting workflow or legal conclusion lifecycle.", "source_refs": ["SRC-006", "SRC-007"]},
                {"neighbor": "STIX Incident", "distinction": "STIX 2.1 provides a deliberately limited Incident extension point, so Vercy aligns exchange identity and markings without claiming that the STIX stub defines this full logical model.", "source_refs": ["SRC-004"]},
            ],
        },
        "sources": SOURCES,
        "structure": build_structure(),
        "functions": [
            {"id": row[0], "name": row[1], "description": row[2], "inputs": row[3], "outputs": row[4], "preconditions": row[5], "effects": row[6], "source_refs": row[7]}
            for row in FUNCTIONS
        ],
        "composition": [
            {"target": "WM-SFT-006 Vulnerability Record", "relation": "REFERENCE", "purpose": "Binds exploited or suspected vulnerabilities and exposures without copying vulnerability lifecycle, scoring or remediation state.", "required": False, "source_refs": ["SRC-003", "SRC-005"]},
            {"target": "WM-ACT-042 Incident Response", "relation": "REFERENCE", "purpose": "Links the independently governed handling case and keeps response execution outside the incident factual aggregate.", "required": False, "source_refs": ["SRC-001", "SRC-005"]},
            {"target": "Cyber event, observation and evidence models", "relation": "REFERENCE", "purpose": "Groups incident-local membership and provenance assertions while external records own raw event and evidence lifecycles.", "required": True, "source_refs": ["SRC-003", "SRC-005"]},
            {"target": "System, service, network, information, identity, person and organization models", "relation": "REFERENCE", "purpose": "Expresses affected scope through authoritative identities without duplicating direct properties or mastership.", "required": True, "source_refs": ["SRC-003", "SRC-005", "SRC-006", "SRC-007"]},
            {"target": "Threat actor, campaign, attack pattern, indicator and observable models", "relation": "REFERENCE", "purpose": "Carries evidence-backed incident-local attribution and mechanism links without owning CTI object lifecycles.", "required": False, "source_refs": ["SRC-003", "SRC-004"]},
            {"target": "NIST SP 800-61 Rev. 3 and FIRST CSIRT Services Framework", "relation": "ALIGN", "purpose": "Aligns qualification, analysis and response boundaries without treating guidance as a storage schema.", "required": False, "source_refs": ["SRC-001", "SRC-005"]},
            {"target": "IODEF Version 2 and STIX Version 2.1", "relation": "ALIGN", "purpose": "Supports explicit, potentially lossy exchange mappings with version and marking preservation.", "required": False, "source_refs": ["SRC-003", "SRC-004"]},
            {"target": "NIS2 and GDPR obligation profiles", "relation": "REFERENCE", "purpose": "Binds regime-specific classification and reporting obligations while keeping legal workflow outside the incident model.", "required": False, "source_refs": ["SRC-006", "SRC-007"]},
        ],
        "service_layers": {
            "dimension": {
                "owner_package_requirements": [
                    "Declare the Dimension owner, incident record authority, constituency, stewards and declaration or closure delegation.",
                    "Declare the incident namespace, authoritative case or incident master system, event and evidence repositories and clock policy.",
                    "Publish model, object, event and relation registries plus applicable disclosure, privacy, retention and legal-hold policies.",
                    "Pin incident-definition, state, severity, reporting and jurisdiction profiles used for each governed determination.",
                ],
                "namespace_guidance": "Mint incident identifiers only in the adopting Dimension's governed namespace; preserve external CSIRT, regulator and partner IDs as typed aliases with authority and correlation history.",
                "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local incident, event, evidence and policy registries"],
            },
            "canon_and_patch": {
                "canonicalization_rules": [
                    "Canonicalize by registry ID, model version, incident master ID, immutable revision and explicit source authority; do not collapse contested assertions.",
                    "Keep incident factual state separate from response workflow state, reporting status and vulnerability remediation state.",
                ],
                "patch_rules": [
                    "Additive extensions use a Dimension-owned namespace and declare target node, incident profile, source, rationale and access impact.",
                    "Breaking changes require a new version, migration map, compatibility declaration and continued resolution of prior incident revisions.",
                ],
                "compatibility_rules": [
                    "Consumers may ignore unknown additive fields only when identity, marking, evidence, authority and temporal meaning remain intact.",
                    "IODEF, STIX, regulator and partner mappings must pin version and declare omitted, transformed or redacted values.",
                ],
            },
            "artifact_rules": {
                "identity_priority": [
                    "Authoritative master-system incident identifier and immutable revision identifier.",
                    "Governed globally resolvable incident IRI or federation identifier.",
                    "Adopting-Dimension UUID or ULID when no authoritative external identifier exists.",
                ],
                "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep occurrence, detection, observation, declaration, effective and ingestion times distinct.",
                "serial_naming_rule": "Name serial artifacts as {incident-id}--{artifact-kind}--{revision-or-event-id}; never use a date, filename or hash alone as incident identity.",
                "integrity_rule": "Store digest, media type, byte length, issuer or collector, capture method, provenance, access marking and immutable version reference for each retained serial artifact.",
            },
            "policies": [
                "The adopting Dimension declares who may register, qualify, merge, split, assess, disclose, reclassify, close and reopen an incident.",
                "Every material statement is labelled fact, observation, assessment, hypothesis, allegation, contradiction or unknown with source and knowledge time.",
                "Collection, correlation and disclosure minimize personal, operational and security-sensitive data and preserve source sharing restrictions.",
                "Response execution, regulatory notification, access enforcement, evidence custody and audit persistence are delegated to their owning systems and referenced.",
                "Automated agents may update low-risk incident-local assertions only within explicit delegation and must propose or confirm high-impact disclosure, closure and destructive actions.",
            ],
            "crud": {
                "read": ["Resolve model and profile versions, owner policy, information markings and external master systems; return only a minimum authorized projection and preserve purpose constraints."],
                "create": ["Create a potential incident with master identity, provenance and unknowns; require a separate authorized qualification decision before representing it as confirmed."],
                "update": ["Append immutable assertion or decision revisions with actor, authority, reason, event and observation times; validate references, contradictions, state and access before and after mutation."],
                "delete": ["Apply retention, legal hold and deletion policy; tombstone or use approved cryptographic erasure for incident-owned records while external evidence and audit systems retain their own governed copies and references do not cascade."],
            },
            "roles": [
                {"name": "Dimension owner", "responsibilities": ["Own incident namespace, mastership, profile selection, delegation, access and retention policy."]},
                {"name": "Incident authority", "responsibilities": ["Qualify, declare, merge, split, reclassify, close or reopen incidents within mandate."]},
                {"name": "Incident analyst", "responsibilities": ["Maintain chronology, scope, impact, hypotheses, confidence and supporting references without overstating certainty."]},
                {"name": "Evidence custodian", "responsibilities": ["Preserve external evidence identity, integrity, custody and access references without transferring mastership into the incident record."]},
                {"name": "Response coordinator", "responsibilities": ["Bind the independently governed response case and communicate factual updates without editing evidence authority."]},
                {"name": "Privacy or legal reviewer", "responsibilities": ["Evaluate personal-data, regulatory, disclosure, retention and legal-hold bindings."]},
                {"name": "Auditor", "responsibilities": ["Review decisions, provenance, changes, access and unresolved contradictions without rewriting operational truth."]},
            ],
            "access": {
                "default_rule": "Deny mutation and sensitive disclosure unless the active Dimension, role, purpose, incident class and information marking grant the action; expose the minimum necessary projection.",
                "scopes": ["bundle", "layer", "finding", "artifact"],
                "exceptions": ["Emergency access must be time-limited, purpose-bound, attributable, independently reviewed and unable to bypass immutable history, evidence integrity or legal hold."],
                "audit_requirements": ["Log actor, role, purpose, incident and revision identity, action, decision, policy version, RFC 3339 timestamp with offset, affected scope and outcome for each privileged mutation or disclosure."],
            },
            "agents_bootstrap": {
                "filename": "AGENTS.md",
                "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
                "read_order": ["Read the nearest Dimension-owner AGENTS.md, incident mandate and disclosure policies.", "Read this model AGENTS.md, then the pinned spec.yaml and every required incident, evidence, response and policy profile before mutation."],
            },
        },
        "coverage": {
            "claim": "Source-grounded reviewable draft covering cyber-incident identity, qualification, chronology, scope, impact, hypotheses, evidence governance, factual state and federation across NIST, IETF, OASIS, FIRST and European Union perspectives.",
            "confidence": "medium",
            "checklist": [
                {"dimension": "identity", "status": "covered", "notes": "Master identity, aliases, versioning, correlation and merge or split continuity are explicit."},
                {"dimension": "lifecycle", "status": "covered", "notes": "Qualification, declaration, state, reclassification, closure, supersession and reopening preserve history."},
                {"dimension": "relationships", "status": "covered", "notes": "Constituent events, affected subjects, vulnerabilities, CTI objects, evidence and response cases are typed references."},
                {"dimension": "temporal", "status": "covered", "notes": "Occurrence, detection, observation, declaration, reporting, effective, recovery and ingestion times are separated."},
                {"dimension": "provenance", "status": "covered", "notes": "Sources, observers, methods, confidence, contradictions and evidence bindings are carried per assertion."},
                {"dimension": "ownership", "status": "covered", "notes": "Dimension owner, incident authority, analyst, evidence custodian and external master systems have distinct responsibilities."},
                {"dimension": "validation", "status": "covered", "notes": "Qualification, reference, transition, evidence, conflict, profile and pre or post mutation validation are explicit."},
                {"dimension": "access", "status": "covered", "notes": "Default deny, granular scopes, projection minimization, markings, emergency exception and audit are defined."},
                {"dimension": "retention and deletion", "status": "covered", "notes": "Retention, legal hold, tombstone, approved erasure and non-cascading external reference rules are explicit."},
                {"dimension": "interoperability", "status": "covered", "notes": "IODEF, STIX, NIS2, GDPR and partner mappings require pinned versions and loss declarations."},
                {"dimension": "classification and recognition", "status": "covered", "notes": "Definition binding, qualification evidence, false-positive boundary, severity and significance schemes are represented."},
                {"dimension": "direct properties", "status": "not-applicable", "notes": "The incident is an abstract occurrence aggregate; physical properties belong to referenced affected objects, while incident-owned descriptive and temporal properties remain modeled."},
                {"dimension": "behavior and possible actions", "status": "covered", "notes": "Ongoing or recurring occurrence, factual transitions and agent record operations are separated from response actions and authorization policy."},
                {"dimension": "impact and scope", "status": "covered", "notes": "Technical, operational, safety, privacy, financial, societal and cross-border effects use evidence-bearing assertions."},
            ],
            "known_omissions": [
                "Sector, organization and jurisdiction profiles must supply exact event, incident-state, severity, significance, reporting and closure vocabularies.",
                "The exact identifiers and dependency contracts for event, evidence, affected-object, threat-intelligence, legal-obligation and response-case sibling models remain to be pinned as the catalogue matures.",
                "Clause-level mappings to IODEF, STIX extensions, national NIS2 implementations and regulator reporting schemas remain profile work.",
            ],
            "conflicts": [
                "The candidate registry edge says COMPOSE WM-ACT-042 while its rationale requires incident and response-process separation; this draft uses a REFERENCE binding and leaves the ledger correction for registry reconciliation.",
                "Cyber-incident definitions vary across lawful-authority, policy-violation, authenticity, near-miss and personal-data-breach boundaries, so every qualification pins its governing definition rather than claiming one universal threshold.",
                "STIX 2.1 explicitly defines Incident as a stub, so it cannot by itself support the richer Vercy structure and is treated only as an alignment and extension boundary.",
            ],
            "regional_assumptions": [
                "NIS2 and GDPR bindings apply only where the relevant European Union law and local implementation govern the incident; no universal reporting deadline or legal conclusion is assumed.",
                "NIST terminology is used as an authoritative profile, not as a claim that United States legal definitions apply globally.",
            ],
            "adversarial_checks": [
                "Reject alerts, anomalous events, near misses and unqualified reports represented as confirmed incidents without a declaration decision and pinned definition.",
                "Reject incident state transitions that silently assert response-task completion, successful containment, legal compliance or proof of recovery.",
                "Reject copied vulnerability, asset, identity, CTI, evidence, response or notification lifecycles when an authoritative typed reference is sufficient.",
                "Reject source-free attribution, causal certainty, universal severity scores, overwritten contradictions and timestamps without seconds and explicit offset.",
                "Reject disclosure, closure, deletion, merge or split decisions that lack authority, purpose, access review and preserved provenance.",
            ],
        },
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(
        json.dumps(build(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
