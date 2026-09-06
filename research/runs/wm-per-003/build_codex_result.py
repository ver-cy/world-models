#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-PER-003."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED = "2026-09-06T01:38:00Z"

SOURCES = [
    {"id":"SRC-001","title":"PROV-DM: The PROV Data Model","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/prov-dm/","version_or_date":"W3C Recommendation, 30 April 2013","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Defines Agent, SoftwareAgent, attribution, association, delegation and responsibility for activities and entities without assigning legal personhood or liability."},
    {"id":"SRC-002","title":"PROV-O: The PROV Ontology","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/prov-o/","version_or_date":"W3C Recommendation, 30 April 2013","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Provides machine-readable agent, software-agent, activity, entity, association, attribution, delegation, specialization and revision relations."},
    {"id":"SRC-003","title":"AI Risk Management Framework: Audience","organization":"National Institute of Standards and Technology","url":"https://airc.nist.gov/airmf-resources/airmf/2-sec-audience/","version_or_date":"AI RMF 1.0 resource, accessed 6 September 2026","source_type":"public-authority","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Separates AI lifecycle actors and responsibilities and supports explicit governance, oversight and accountability bindings for AI-related profiles."},
    {"id":"SRC-004","title":"A2A Protocol Specification","organization":"A2A Project under the Linux Foundation","url":"https://a2a-protocol.org/latest/specification/","version_or_date":"Latest public specification, accessed 6 September 2026","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Defines agent discovery through Agent Cards, skills, capabilities, interfaces, authentication and authorization, tasks, messages and artifacts for an optional protocol projection."},
    {"id":"SRC-005","title":"Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence","organization":"European Union","url":"https://eur-lex.europa.eu/eli/reg/2024/1689/oj","version_or_date":"Regulation (EU) 2024/1689, 13 June 2024","source_type":"legislation","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Supplies an EU AI profile for provider and deployer roles, record keeping, transparency, human oversight, robustness, cybersecurity and post-market duties without defining all non-human agents."},
    {"id":"SRC-006","title":"ODRL Information Model 2.2","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/odrl-model/","version_or_date":"W3C Recommendation, 15 February 2018","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Provides policies, permissions, prohibitions, duties, parties, actions and constraints for expressing referenced authority envelopes without turning capability into permission."},
    {"id":"SRC-007","title":"Verifiable Credentials Data Model v2.0","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/vc-data-model-2.0/","version_or_date":"W3C Recommendation, 15 May 2025","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Provides issuer, credential subject, validity, status, schema, evidence and terms-of-use patterns for portable agent or delegation attestations while credentials remain evidence."},
    {"id":"SRC-008","title":"Time Ontology in OWL","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/owl-time/","version_or_date":"W3C Recommendation, 19 October 2017; current 15 November 2022 edition","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Provides instants, intervals, durations and temporal relations for identity, delegation, activation, observation and lifecycle validity."},
    {"id":"SRC-009","title":"Web of Things Thing Description 1.1","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/wot-thing-description11/","version_or_date":"W3C Recommendation, 5 December 2023","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Defines affordance-oriented descriptions of properties, actions, events, forms and security metadata useful for an optional embodied or networked agent interface projection."},
    {"id":"SRC-010","title":"Date and Time on the Internet: Timestamps","organization":"Internet Engineering Task Force","url":"https://www.rfc-editor.org/rfc/rfc3339","version_or_date":"RFC 3339, July 2002","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":ACCESSED,"relevance":"Defines interoperable timestamps with seconds and explicit UTC relation for delegation, activation, attribution, observation and lifecycle events."},
]

BUNDLES = [
    ("identity-kind-and-instance-boundary", "Identity, kind and instance boundary", "Identifies the persistent governed agent and separates it from implementations, deployments, endpoints and sessions.", "Attribution and governance fail when an agent name, executable, model, device, endpoint and run identifier are treated as one identity.", ["SRC-001","SRC-002","SRC-004","SRC-008"], [
        ("persistent-identity-and-lineage", "Persistent identity and lineage", "Stable identifiers, aliases, versions and successor history for the governed actor.", ["SRC-001","SRC-002","SRC-008"], [
            ("authoritative-agent-identifier-and-master-system", "Authoritative agent identifier and master system", "The stable actor identifier, issuing authority, namespace, master system, resolution state and local bindings.", "identity", ["SRC-001","SRC-002"], "identifier", True),
            ("aliases-version-specialization-and-successor-lineage", "Aliases, version, specialization and successor lineage", "Names, protocol identifiers, definition versions, specializations, replacements, merges and retirement lineage without identity collapse.", "lifecycle", ["SRC-002","SRC-004"], "collection", False),
        ]),
        ("kind-composition-and-boundary", "Kind, composition and boundary", "Classification criteria and the distinction among actor, definition, deployment, endpoint, embodiment and session.", ["SRC-001","SRC-002","SRC-004","SRC-009"], [
            ("nonhuman-agent-kind-and-classification-criteria", "Non-human agent kind and classification criteria", "Profile-qualified kind such as software, embodied, hybrid or collective machine actor, with observable criteria and prohibited subjecthood inferences.", "classification", ["SRC-001","SRC-003","SRC-009"], "collection", True),
            ("agent-definition-deployment-endpoint-embodiment-session-boundary", "Agent, definition, deployment, endpoint, embodiment and session boundary", "Typed component and realization references with separate identifiers, masters, versions and lifecycles.", "composition", ["SRC-001","SRC-002","SRC-004","SRC-009"], "collection", True),
        ]),
    ]),
    ("control-accountability-and-stakeholders", "Control, accountability and stakeholders", "Records who creates, controls, operates, benefits from and remains answerable for the agent.", "Non-human agency must not hide the natural persons and organizations that configure, authorize, operate or benefit from it.", ["SRC-001","SRC-003","SRC-005"], [
        ("control-and-operating-parties", "Control and operating parties", "Time-qualified bindings for parties with technical or organizational control.", ["SRC-001","SRC-003","SRC-005"], [
            ("owner-controller-provider-and-deployer-bindings", "Owner, controller, provider and deployer bindings", "External party references, role basis, control surface, jurisdiction, validity and change history.", "relationship", ["SRC-003","SRC-005"], "collection", True),
            ("operator-beneficiary-customer-and-affected-party-bindings", "Operator, beneficiary, customer and affected-party bindings", "Operational, beneficiary, service-recipient and affected-party roles with scope, time and source.", "relationship", ["SRC-003","SRC-005"], "collection", False),
        ]),
        ("accountability-and-responsibility", "Accountability and responsibility", "Answerability, escalation and the boundary between provenance responsibility and legal conclusions.", ["SRC-001","SRC-002","SRC-003","SRC-005"], [
            ("accountable-party-oversight-owner-and-escalation-contact", "Accountable party, oversight owner and escalation contact", "Who answers for deployment and use, receives escalation and has power to intervene, with delegated scope and availability.", "authority", ["SRC-003","SRC-005"], "object", True),
            ("activity-responsibility-attribution-versus-liability-and-personhood", "Activity responsibility attribution versus liability and personhood", "PROV responsibility claims and explicit non-inference of intention, consciousness, legal personality, rights, duties or liability.", "provenance", ["SRC-001","SRC-002"], "object", True),
        ]),
    ]),
    ("authority-mandate-and-delegation", "Authority, mandate and delegation", "Defines the purpose-bound authority under which the agent may act.", "A capability describes what an agent can do; only a current mandate, delegation and policy can establish what it may do.", ["SRC-001","SRC-002","SRC-006","SRC-007","SRC-008"], [
        ("principal-mandate-and-delegation-chain", "Principal, mandate and delegation chain", "The accountable principal, mandate, purpose and traceable chain of acting on behalf of another.", ["SRC-001","SRC-002","SRC-006","SRC-008"], [
            ("principal-mandate-purpose-resource-jurisdiction-and-interval", "Principal, mandate, purpose, resource, jurisdiction and interval", "The source authority, permitted purposes and targets, territorial or logical scope and validity interval.", "authority", ["SRC-001","SRC-006","SRC-008"], "object", True),
            ("delegation-chain-subdelegation-conditions-and-revocation", "Delegation chain, subdelegation, conditions and revocation", "Each delegator, delegate, allowed onward delegation, conditions, expiry, suspension and revocation effect.", "relationship", ["SRC-001","SRC-002","SRC-006"], "collection", True),
        ]),
        ("permission-credentials-and-policy", "Permission, credentials and policy", "External policy and credential evidence that constrains actions at decision time.", ["SRC-006","SRC-007","SRC-008"], [
            ("permission-prohibition-duty-constraint-and-approval-gate", "Permission, prohibition, duty, constraint and approval gate", "Referenced policy rules, actions, targets, conditions, duties, exceptions and human or organizational confirmation class.", "security", ["SRC-006"], "collection", True),
            ("credential-scope-audience-holder-validity-and-status", "Credential scope, audience, holder, validity and status", "Credential references and observations with issuer, subject, audience, proof, expiry and status while secrets stay external.", "evidence", ["SRC-007","SRC-008"], "collection", False),
        ]),
    ]),
    ("capability-behaviour-constraints-and-dependencies", "Capability, behaviour, constraints and dependencies", "Describes what the agent can do, how it behaves and the envelope in which claims remain valid.", "Declarations, observations, permissions and safety claims are different evidence classes and must remain separately attributable.", ["SRC-003","SRC-004","SRC-006","SRC-009"], [
        ("capabilities-skills-and-interfaces", "Capabilities, skills and interfaces", "Declared and observed action surfaces plus machine-readable access bindings.", ["SRC-004","SRC-009"], [
            ("declared-observed-and-verified-capability-surface", "Declared, observed and verified capability surface", "Actions, inputs, outputs, quality limits, confidence, evaluation basis and contexts in which the capability is available.", "requirement", ["SRC-003","SRC-004","SRC-009"], "collection", True),
            ("skill-protocol-interface-action-property-and-event-bindings", "Skill, protocol, interface, action, property and event bindings", "Versioned A2A, WoT or domain binding references with authentication, media, schema and negotiation metadata.", "interoperability", ["SRC-004","SRC-009"], "collection", False),
        ]),
        ("behaviour-state-and-transition", "Behaviour, state and transition", "Observable response patterns and governed operational states.", ["SRC-003","SRC-004","SRC-008"], [
            ("behaviour-policy-mode-trigger-and-observable-signature", "Behaviour policy, mode, trigger and observable signature", "Expected responses under stated conditions, recognizable signatures, confidence, prohibited inference and drift indicators.", "process", ["SRC-003","SRC-004"], "collection", True),
            ("registered-configured-ready-active-paused-degraded-and-stopped-state", "Registered, configured, ready, active, paused, degraded and stopped state", "Current state, allowed transitions, actor and authority, reason, event and valid times, safe-state target and history.", "state", ["SRC-003","SRC-008"], "object", True),
        ]),
        ("dependencies-envelope-hazards-and-failure", "Dependencies, envelope, hazards and failure", "Conditions and components on which capability and safe behaviour depend.", ["SRC-003","SRC-004","SRC-005","SRC-009"], [
            ("tool-model-memory-service-and-embodiment-dependencies", "Tool, model, memory, service and embodiment dependencies", "Pinned external component references, trust state, version, availability, data boundary and degraded-mode effect.", "composition", ["SRC-003","SRC-004","SRC-009"], "collection", True),
            ("operating-envelope-prohibition-hazard-failure-and-recovery", "Operating envelope, prohibition, hazard, failure and recovery", "Resource, time, cost, environment and safety limits, forbidden actions, failure signatures, containment and recovery path.", "constraint", ["SRC-003","SRC-005","SRC-009"], "collection", True),
        ]),
    ]),
    ("operation-attribution-and-oversight", "Operation, attribution and oversight", "Connects agent state and execution context to activities, outputs and intervention controls.", "The durable actor must remain distinct from each run while activity and output provenance still resolves to the exact operational context.", ["SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-008"], [
        ("activation-deployment-and-session-context", "Activation, deployment and session context", "Which approved configuration is active where and how executions correlate to it.", ["SRC-001","SRC-004","SRC-008"], [
            ("deployment-configuration-release-and-activation-binding", "Deployment, configuration, release and activation binding", "Pinned external deployment and configuration references, approval, environment, activation authority and effective interval.", "composition", ["SRC-003","SRC-004","SRC-008"], "collection", True),
            ("session-run-correlation-and-temporal-context", "Session, run, correlation and temporal context", "External session and run references, correlation identifiers and distinct event, valid, observation, knowledge and ingestion times.", "temporal", ["SRC-001","SRC-002","SRC-008","SRC-010"], "collection", False),
        ]),
        ("activity-and-output-attribution", "Activity and output attribution", "Traceable associations among agent, activity, principal, plan, inputs and outputs.", ["SRC-001","SRC-002"], [
            ("activity-association-plan-role-and-delegation-attribution", "Activity association, plan, role and delegation attribution", "Which agent was associated with an activity, in which role, under which plan and on whose behalf.", "provenance", ["SRC-001","SRC-002"], "collection", True),
            ("output-entity-generation-attribution-and-derivation", "Output entity generation, attribution and derivation", "Generated or influenced output references, activity, sources, agent version and provenance bundle.", "provenance", ["SRC-001","SRC-002"], "collection", True),
        ]),
        ("oversight-intervention-and-safe-state", "Oversight, intervention and safe state", "Approval, monitoring, interruption, handoff and containment controls.", ["SRC-003","SRC-005","SRC-006"], [
            ("human-or-organizational-oversight-approval-and-intervention", "Human or organizational oversight, approval and intervention", "Oversight role, competence reference, information supplied, approval gates, intervention controls and response evidence.", "authority", ["SRC-003","SRC-005","SRC-006"], "collection", True),
            ("monitoring-alert-escalation-suspension-handoff-and-failsafe", "Monitoring, alert, escalation, suspension, handoff and fail-safe", "Signals, thresholds, accountable recipient, timeout, suspension authority, safe-state behavior and recovery confirmation.", "process", ["SRC-003","SRC-005"], "collection", True),
        ]),
    ]),
    ("assurance-evidence-privacy-and-lifecycle", "Assurance, evidence, privacy and lifecycle", "Records bounded assurance claims, observations, incidents and durable lifecycle governance.", "Evaluation and credentials are evidence with scope and expiry, not proof of universal safety, authority, identity or legal compliance.", ["SRC-002","SRC-003","SRC-005","SRC-007","SRC-008"], [
        ("assurance-monitoring-and-incidents", "Assurance, monitoring and incidents", "Risk, evaluation, limitation, telemetry and incident references.", ["SRC-002","SRC-003","SRC-005"], [
            ("risk-evaluation-assurance-limitation-and-acceptance", "Risk, evaluation, assurance, limitation and acceptance", "External assessment references, test context, metrics, thresholds, residual risks, approver, validity and non-claims.", "validation", ["SRC-003","SRC-005"], "collection", True),
            ("monitoring-drift-anomaly-incident-impact-and-corrective-action", "Monitoring, drift, anomaly, incident, impact and corrective action", "Observed signals and externally mastered incident or corrective-action references with severity, scope and status.", "evidence", ["SRC-003","SRC-005"], "collection", False),
        ]),
        ("privacy-retention-and-agent-lifecycle", "Privacy, retention and agent lifecycle", "Purpose-bound disclosure and governed suspension, retirement and tombstoning.", ["SRC-002","SRC-005","SRC-007","SRC-008"], [
            ("data-category-purpose-access-disclosure-retention-and-deletion", "Data category, purpose, access, disclosure, retention and deletion", "Field and artifact sensitivity, purpose, audience, access policy, retention class, legal hold and disposition evidence.", "privacy", ["SRC-005","SRC-007"], "collection", True),
            ("suspension-revocation-retirement-replacement-and-tombstone", "Suspension, revocation, retirement, replacement and tombstone", "Authorized lifecycle endings, surviving delegations and credentials, successor, endpoint withdrawal, retention and durable identity tombstone.", "lifecycle", ["SRC-002","SRC-007","SRC-008"], "object", True),
        ]),
    ]),
    ("interoperability-governance-and-agent-operations", "Interoperability, governance and agent operations", "Controls projections, mapping loss and safe automated maintenance.", "Protocol cards and ontology projections are views of the governed actor and must never become the sole source of identity, authority or lifecycle truth.", ["SRC-001","SRC-002","SRC-004","SRC-006","SRC-007","SRC-009","SRC-010"], [
        ("profiles-projections-and-mapping-loss", "Profiles, projections and mapping loss", "Versioned external representations and explicit non-equivalence.", ["SRC-001","SRC-002","SRC-004","SRC-007","SRC-009"], [
            ("prov-agent-softwareagent-association-and-delegation-projection", "PROV Agent, SoftwareAgent, association and delegation projection", "Loss-aware mapping of agent identity, activity association, attribution and acted-on-behalf-of relations.", "interoperability", ["SRC-001","SRC-002"], "collection", True),
            ("a2a-agent-card-wot-description-and-credential-projection", "A2A Agent Card, WoT description and credential projection", "Versioned discovery, affordance and proof projections with authentication, disclosure, omission and round-trip limits.", "interoperability", ["SRC-004","SRC-007","SRC-009"], "collection", False),
        ]),
        ("safe-agent-control-and-validation", "Safe agent control and validation", "Authorized operations, invariants, concurrency and recovery.", ["SRC-002","SRC-003","SRC-005","SRC-006","SRC-010"], [
            ("operation-authority-purpose-preconditions-idempotency-and-evidence", "Operation authority, purpose, preconditions, idempotency and evidence", "Classifies each read, bind, delegate, activate, suspend, attribute, disclose and retire action with proof and effect.", "security", ["SRC-003","SRC-006"], "object", True),
            ("prewrite-postwrite-validation-conflict-concurrency-and-recovery", "Pre-write and post-write validation, conflict, concurrency and recovery", "Identity, boundary, authority, state, time, provenance, privacy, stale-head and rollback checks with immutable audit evidence.", "validation", ["SRC-002","SRC-005","SRC-010"], "collection", True),
        ]),
    ]),
]


def finding(row):
    fid, name, description, kind, refs, value_kind, required = row
    return {
        "id": fid,
        "name": name,
        "description": description,
        "source_refs": refs,
        "questions": [
            {"id":f"{fid}-q01","text":f"What exact values, references, qualifiers and explicit unknowns must be recorded for {name.lower()}?","kind":kind,"answer_data":["value or typed reference","profile and scope","valid time","explicit unknowns"]},
            {"id":f"{fid}-q02","text":f"Which controller, operator, principal, authority, observation and evidence establishes {name.lower()}, at what event, valid and knowledge time, and with what confidence?","kind":"evidence","answer_data":["asserting actor","authority and basis","source and evidence","times","confidence"]},
            {"id":f"{fid}-q03","text":f"How may {name.lower()} be validated, challenged, changed, superseded, retained or disclosed without conflating capability with permission or importing a neighboring model lifecycle?","kind":"validation","answer_data":["validation rule","challenge route","successor or tombstone","access and retention effect"]},
        ],
        "data_elements":[{"id":f"{fid}-data","name":f"{name} data","description":f"Structured, source-qualified answer data for {name.lower()}.","value_kind":value_kind,"cardinality":"1" if required else "0..n","required":required,"source_refs":refs}],
        "artifacts":[{"id":f"{fid}-record","name":f"{name} record","description":f"Versioned evidence-bearing record for {name.lower()} with authority, event, valid and knowledge time, provenance and access marking.","media_or_form":["logical record","signed or attributable evidence reference"],"serial":True,"identity_strategy":f"Agent identifier plus {fid} assertion or event identifier; mutable names, endpoint URLs, dates, session identifiers and file hashes never identify the governed actor.","source_refs":refs}],
        "inline_only_rationale":None,
    }


def structure():
    return {"bundles":[{"id":bid,"name":name,"description":description,"rationale":rationale,"source_refs":refs,"layers":[{"id":lid,"name":lname,"description":ldescription,"source_refs":lrefs,"findings":[finding(item) for item in findings]} for lid,lname,ldescription,lrefs,findings in layers]} for bid,name,description,rationale,refs,layers in BUNDLES]}


FUNCTIONS = [
    ("register-agent", "Register non-human agent", "Create the persistent actor identity, kind, master binding and explicit boundaries.", ["issuer","agent kind","master reference","composition references"], ["registered agent revision"], ["issuer has registration authority","duplicate and boundary checks pass"], ["stable identity and provenance become resolvable"], ["SRC-001","SRC-002"]),
    ("bind-control-and-accountability", "Bind control and accountability parties", "Append time-qualified owner, controller, provider, deployer, operator and accountable-party bindings.", ["agent","party references","role basis","interval"], ["stakeholder binding revision"], ["parties resolve","binding authority is recorded"], ["control and escalation responsibilities become explicit"], ["SRC-003","SRC-005"]),
    ("grant-delegation", "Grant purpose-bound delegation", "Attach an authorized mandate with principal, purpose, resources, interval, constraints and subdelegation rule.", ["agent","principal","mandate","policy references"], ["active delegation revision"], ["principal authority validates","agent identity is active"], ["permitted action envelope becomes queryable"], ["SRC-001","SRC-002","SRC-006"]),
    ("constrain-or-revoke-delegation", "Constrain, suspend or revoke delegation", "Reduce or end delegated authority without erasing prior grants or activity provenance.", ["delegation","authority","reason","effective time"], ["delegation transition event"], ["actor may change delegation","affected actions are identified"], ["future authorization sees the new state and history remains citable"], ["SRC-002","SRC-006","SRC-008"]),
    ("declare-capability-and-limits", "Declare capability and limits", "Record declared, observed or verified ability with context, evidence, confidence and prohibitions.", ["agent","capability profile","evidence","operating envelope"], ["capability assertion"], ["source and evaluation context resolve"], ["ability is documented without implying permission"], ["SRC-003","SRC-004","SRC-009"]),
    ("bind-interface-and-dependency", "Bind interface and dependency", "Pin a protocol, skill, tool, model, memory, service or embodiment and state its trust and degraded-mode effect.", ["agent","external component","version","binding profile"], ["dependency binding revision"], ["component identity and version resolve","access and data boundaries validate"], ["operational dependencies and failure effects become explicit"], ["SRC-004","SRC-009"]),
    ("transition-operational-state", "Transition operational state", "Activate, pause, degrade, suspend, stop or recover the agent under a valid transition and authority.", ["agent","current head","target state","authority","evidence"], ["state transition event"], ["transition is allowed","delegation and controls are current"], ["new state is effective without overwriting history"], ["SRC-003","SRC-005","SRC-008","SRC-010"]),
    ("attribute-activity-or-output", "Attribute activity or output", "Link an external activity or entity to the exact agent, role, plan, delegation, version and execution context.", ["agent","activity or entity","association or attribution evidence"], ["PROV-compatible attribution revision"], ["identities and timestamps resolve","claim authority is known"], ["responsibility provenance is queryable without inferring liability"], ["SRC-001","SRC-002"]),
    ("request-approval-or-escalate", "Request approval or escalate", "Route an action, ambiguity, threshold breach or loss-of-control condition to the accountable authority.", ["agent","proposed action or signal","policy","deadline"], ["approval request or escalation event"], ["recipient and fallback resolve"], ["operation waits, narrows or enters fail-safe according to policy"], ["SRC-003","SRC-005","SRC-006"]),
    ("attach-assurance-or-incident", "Attach assurance or incident evidence", "Reference an evaluation, limitation, risk acceptance, monitoring observation, incident or corrective action.", ["agent","external record","scope","validity"], ["assurance or incident binding"], ["record digest, issuer and scope validate"], ["bounded evidence is available without converting it to universal compliance"], ["SRC-003","SRC-005","SRC-007"]),
    ("project-agent-profile", "Project agent profile", "Produce a purpose-bound PROV, A2A, WoT or credential view with explicit omissions and mapping loss.", ["agent revision","target profile","requester and purpose"], ["validated expiring projection"], ["versions, access and minimum disclosure validate"], ["projection is linked to source digest and cannot replace the master"], ["SRC-001","SRC-004","SRC-007","SRC-009"]),
    ("retire-agent", "Retire non-human agent", "End authority and operation, withdraw discoverability, reconcile credentials and preserve a durable tombstone.", ["agent","retirement authority","successor","retention decision"], ["retirement event and tombstone"], ["agent is not active","holds and dependent delegations are resolved"], ["new operation is blocked while prior identity and attribution remain resolvable"], ["SRC-002","SRC-007","SRC-008"]),
]


def service_layers():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Dimension identity, owner, agent registrar, delegation authority, oversight owner and namespace",
                "Person, organization, agent, software, AI system, model, embodiment, activity, policy, credential, incident and evidence registries",
                "Master-system mappings for agent, deployment, endpoint, session, delegation, activity, output and lifecycle-event identifiers",
                "Agent classification, delegation, approval, safety, privacy, retention, incident, federation and autonomous-operation policies",
            ],
            "namespace_guidance": "Mint governed agent and assertion identifiers in the adopting Dimension only when no authoritative master identifier exists; preserve parties, software, AI systems, models, embodiments, tasks, activities, outputs, policies, credentials, incidents and evidence as typed external references.",
            "registry_links": ["https://ver.cy/models/","https://ver.cy/model-agent-protocol.md","Dimension-local agent, delegation, capability, activation, attribution, assurance and lifecycle registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by authoritative persistent agent identifier and issuer, never by display name, executable, model, device, endpoint, credential, session, date or content hash alone.",
                "Keep persistent agent, definition, deployment, endpoint, embodiment, session, task, activity and output identities and lifecycles distinct.",
            ],
            "patch_rules": [
                "Additive extensions declare target bundle, layer or finding, agent-kind profile, source, authority, safety, privacy and interoperability impact.",
                "Identity, boundary, controller, delegation, capability, state-transition or attribution semantic changes require a successor version, migration map, rollback path and continued resolution of prior records.",
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when identity, kind, component boundary, control, authority, capability, state, attribution, oversight, access and lifecycle meaning remain intact.",
                "PROV, A2A, WoT, ODRL and credential projections pin source and target versions and disclose transformed, omitted, aggregated and non-round-trippable values.",
            ],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for the governed agent, qualified by issuer.","Governed globally resolvable agent IRI with explicit master-system binding.","Adopting-Dimension UUID or ULID when no authoritative external identifier exists."],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep event, decision, effective, observation, knowledge, issuance and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {agent-id}--{artifact-kind}--{assertion-or-event-id}; never use an agent name, model name, endpoint, session, date, filename or hash alone as agent identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and profile versions, authority, valid and knowledge times, provenance, assurance, licence and access marking for every retained serial artifact.",
        },
        "policies": [
            "The adopting Dimension declares who may register, classify, configure, delegate to, activate, suspend, attribute, disclose, replace and retire a non-human agent.",
            "Capability never implies permission, PROV responsibility never establishes liability, and technical autonomy never establishes consciousness, personhood, rights or moral agency.",
            "Controller, provider, deployer, operator, beneficiary and accountable party remain externally mastered, separately attributable and time-qualified.",
            "Software, AI system, model, embodiment, task, activity, output, credential, policy, incident and evidence lifecycles remain in their owning systems and are referenced.",
            "Automated agents may read, validate, index and append low-risk observations within policy; widening delegation, activation in a consequential scope, adverse suspension, public attestation and destructive disposition require accountable authority.",
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, requested valid and knowledge time, delegation and evidence freshness; return the minimum permitted view without leaking private agent existence, capability or endpoint data."],
            "create": ["Create stable persistent identity, kind, master binding, controller and accountable-party references and explicit unknowns before capability, delegation or activation claims."],
            "update": ["Append an assertion, binding, event or successor revision with actor, authority, reason, RFC 3339 time, evidence and before-and-after validation; never overwrite a cited attribution, delegation or event."],
            "delete": ["Apply authority, incident, legal-hold, credential-status and retention policy; prefer retired state or tombstone, preserve identity and attribution history, and never cascade into referenced parties, software, models, embodiments, activities or evidence."],
        },
        "roles": [
            {"name":"Dimension owner","responsibilities":["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name":"Agent registrar","responsibilities":["Maintain persistent identity, kind, boundary, aliases and successor lineage."]},
            {"name":"Controller or provider","responsibilities":["Declare the controlled agent and maintain accurate configuration, capability and limitation references."]},
            {"name":"Deployer or operator","responsibilities":["Operate only within current delegation and envelope and preserve activation, oversight and incident evidence."]},
            {"name":"Delegating principal","responsibilities":["Grant, constrain, suspend and revoke purpose-bound authority within its own authority."]},
            {"name":"Accountable and oversight owner","responsibilities":["Review consequential action, intervene, receive escalation and accept or reject residual risk."]},
            {"name":"Safety, privacy and access steward","responsibilities":["Apply minimum disclosure, monitoring, incident, retention and security controls."]},
            {"name":"Independent auditor","responsibilities":["Review identity, delegation, state, attribution, controls and evidence without rewriting source records."]},
        ],
        "access": {
            "default_rule": "Deny mutation and disclosure of private agent existence, endpoint, capability, delegation, state or evidence unless active Dimension, actor role, purpose and field policy grant it; expose the minimum necessary projection.",
            "scopes": ["bundle","layer","finding","artifact"],
            "exceptions": ["Statutory, judicial, safeguarding or emergency access must cite authority, be purpose-bound, attributable and reviewable, and must not erase original delegations, incidents, disputes or audit evidence."],
            "audit_requirements": ["Log actor, calling agent, role, purpose, agent and principal identities, action, policy, RFC 3339 timestamp with offset, requested and effective authority, affected scope, evidence and outcome."],
        },
        "agents_bootstrap": {
            "filename":"AGENTS.md",
            "required_fields":["Name","Type","Specification URL","Storage type URL","Interface URL","Processes URL"],
            "read_order":["Read the nearest Dimension-owner AGENTS.md, agent mastership, delegation, oversight, safety, privacy, incident, retention and federation policies.","Read this model AGENTS.md, pinned spec.yaml and required party, software, AI system, model, embodiment, activity, policy, credential, incident and evidence model instructions before mutation, activation or disclosure."],
        },
    }


def coverage():
    dims = [
        ("identity", "Persistent agent identity, issuer, aliases, versions and successor lineage are explicit."),
        ("classification and definition", "Software, embodied, hybrid and other profiled non-human kinds are allowed without subjecthood inference."),
        ("direct properties", "Native computational, organizational and virtual properties are first-class; physical properties are delegated to an embodiment."),
        ("recognition and observation", "Identifiers, interface and behaviour signatures, methods, evidence, confidence, drift and confusing neighboring identities are covered."),
        ("capabilities and possible actions", "Capabilities, behaviours, permissions, operations, affordances, constraints, hazards and failure modes remain distinct."),
        ("composition", "Software, models, memory, tools, services and embodiment are pinned external references with separate masters."),
        ("lifecycle", "Registration, configuration, activation, pause, degradation, suspension, recovery, retirement and tombstone preserve history."),
        ("relationships", "Controllers, providers, deployers, operators, principals, beneficiaries, affected parties and accountable owners are time-qualified."),
        ("temporal", "Event, decision, valid, observation, knowledge, issuance and ingestion times remain distinct and events use RFC 3339."),
        ("spatial", "Physical, network, jurisdictional and logical operating scopes are referenced when the profile requires them."),
        ("provenance", "Association, attribution, delegation, derivation, revision and conflicting assertions remain separately attributable."),
        ("ownership and stewardship", "Identity, control, data, components and evidence retain their owning master systems and stewards."),
        ("validation and quality", "Duplicate identity, stale delegation, state transitions, dependency drift, boundary confusion and projection loss are checked."),
        ("access and privacy", "Private existence, endpoint, capability, delegation, affected-party data and minimum disclosure are covered."),
        ("retention and deletion", "Per-artifact retention, legal hold, credential withdrawal, retirement and durable tombstone are explicit."),
        ("interoperability", "PROV, A2A, WoT, ODRL and credential projections are versioned, purpose-bound and loss-aware."),
    ]
    return {
        "claim":"Covers a generic governed non-human actor from identity, kind, control and delegation through capability, operation, attribution, oversight, assurance, lifecycle and exchange without asserting subjecthood.",
        "confidence":"medium",
        "checklist":[{"dimension":d,"status":"covered","notes":n} for d,n in dims],
        "known_omissions":[
            "No independent Claude or Grok result was available; this source-grounded Codex fallback requires later external review before canonical promotion.",
            "WM-AI-002 AI Agent, software, AI system, model, robot or embodiment, task, activity, credential, access, incident and evidence models retain their own detailed semantics.",
            "Animal, swarm, autonomous vehicle, industrial robot, legal electronic person and other jurisdiction or embodiment profiles require specialist review and must not be inferred from this common core.",
            "The frozen relation ledger contains no approved WM-PER-003 dependency rows; composition targets remain descriptive holds until registry relations are reviewed.",
            "Certified PROV, A2A, WoT, ODRL and credential crosswalks, conformance fixtures and round-trip tests remain future work.",
        ],
        "conflicts":[
            "W3C PROV uses Agent broadly for responsibility attribution, while this model narrows the subject to a persistently governed non-human actor and forbids legal or moral inferences.",
            "A2A Agent Cards describe discoverable protocol capabilities, while this model treats each card as a projection that may omit private controls, delegation, lifecycle and evidence.",
            "The generic Non-human Agent overlaps WM-AI-002 unless AI-specific model, memory, tool and regulatory semantics remain in that narrower specialization.",
        ],
        "regional_assumptions":[
            "The EU AI Act supplies an EU AI-system profile and does not govern every non-human agent or create universal subject status.",
            "PROV responsibility attribution is a provenance relation and does not decide legal accountability or liability in any jurisdiction.",
            "A2A, WoT, ODRL and Verifiable Credentials are optional interoperability profiles, not mandatory storage or interface formats.",
        ],
        "adversarial_checks":[
            "Reject any agent identifier derived only from name, executable, AI model, device, endpoint, credential, session or date.",
            "Reject permission inferred from capability, successful execution, credential possession or protocol advertisement alone.",
            "Reject consciousness, intention, personhood, rights, moral responsibility or liability inferred from autonomy or PROV classification.",
            "Reject activation when delegation, accountable party, required dependencies, oversight channel or safe-state behavior is absent or stale.",
            "Reject mutation, disclosure, subdelegation, attribution or retirement beyond actor authority, purpose, state preconditions and confirmation class.",
        ],
    }


def build():
    return {
        "schema_version":"1.0.0",
        "model": {
            "registry_id":"vr.wm-per-003",
            "model_id":"WM-PER-003",
            "name":"Non-human Agent",
            "entry_kind":"entity",
            "purpose":"Represent a persistent governed non-human actor with explicit identity, control, delegated authority, capabilities, operating state, attribution, oversight and lifecycle while remaining independent of storage and interface format.",
            "scope_statement":"Owns the generic actor identity and kind, definition and instance boundary, control and accountable-party bindings, mandate and delegation envelope, capability and behavior assertions, dependency references, operating state, activity and output attribution, oversight, assurance references, privacy, lifecycle and loss-aware projections. External systems own persons, organizations, software, AI systems and models, embodiments, tasks, activities, outputs, policies, credentials, incidents and evidence objects.",
            "in_scope":["Persistent non-human agent identity, issuer, kind, aliases, versions, components and successor lineage","Controller, provider, deployer, operator, principal, beneficiary, affected-party and accountable-party bindings","Mandate, delegation, permission references, capabilities, behavior, dependencies, operating envelope, states, attribution, oversight, assurance, privacy, lifecycle and exchange"],
            "out_of_scope":["Human person, organization, software product, AI system, AI model, physical embodiment, task, activity, output, credential, policy, access decision, incident and evidence master lifecycles","Claims that the agent is conscious, sentient, intentional, a legal person, a rights-holder or itself legally liable","AI Agent details already owned by WM-AI-002, physical robotics semantics, universal authorization rules or deployment-specific compliance conclusions"],
            "boundary_notes":[
                {"neighbor":"WM-AI-002 AI Agent","distinction":"AI Agent is a specialization that owns AI-specific model, memory, tools, protocols, evaluation and regulatory context; this model supplies the common non-human actor identity, delegation, attribution and lifecycle core.","source_refs":["SRC-003","SRC-005"]},
                {"neighbor":"Software, AI System and AI Model","distinction":"Software and models are components or implementations; the governed actor has its own persistent identity, controller, authority and state and may change components without silent identity replacement.","source_refs":["SRC-001","SRC-002","SRC-003"]},
                {"neighbor":"Robot, Device and Embodiment","distinction":"A physical body owns geometry, material, pose, mechanics and safety details; this model records only the agent-to-embodiment binding and delegated physical operating envelope.","source_refs":["SRC-009"]},
                {"neighbor":"Session, Run, Task and Activity","distinction":"These are bounded execution or work records; the agent is the durable actor referenced from each and keeps only correlation and attribution links.","source_refs":["SRC-001","SRC-002","SRC-004"]},
                {"neighbor":"Credential, Access and Policy","distinction":"Credentials and policies provide evidence and authorization inputs; possession or technical ability does not establish current permission.","source_refs":["SRC-006","SRC-007"]},
                {"neighbor":"Legal or moral subject","distinction":"Technical autonomy and provenance responsibility do not establish consciousness, intention, rights, duties, personhood or liability; those conclusions require external law, evidence and authority.","source_refs":["SRC-001","SRC-005"]},
            ],
        },
        "sources":SOURCES,
        "structure":structure(),
        "functions":[{"id":r[0],"name":r[1],"description":r[2],"inputs":r[3],"outputs":r[4],"preconditions":r[5],"effects":r[6],"source_refs":r[7]} for r in FUNCTIONS],
        "composition":[
            {"target":"WM-AI-002 AI Agent","relation":"CHILD","purpose":"Reuse the generic governed actor core while AI-specific model, memory, tool, protocol, evaluation and regulation semantics stay in the specialization.","required":False,"source_refs":["SRC-003","SRC-005"]},
            {"target":"Person, Organization, Software, AI System, AI Model, Embodiment, Task, Activity, Output, Policy, Credential, Incident and Evidence models","relation":"REFERENCE","purpose":"Connect the agent to externally mastered parties, components, executions, rules and evidence without identity or lifecycle duplication.","required":True,"source_refs":["SRC-001","SRC-002","SRC-003","SRC-005","SRC-006","SRC-007","SRC-009"]},
            {"target":"W3C PROV-DM and PROV-O","relation":"ALIGN","purpose":"Project agent, SoftwareAgent, association, attribution, delegation, specialization and revision provenance.","required":True,"source_refs":["SRC-001","SRC-002"]},
            {"target":"A2A Protocol Specification","relation":"ALIGN","purpose":"Publish an optional discovery and protocol projection through Agent Cards, skills, capabilities and interfaces.","required":False,"source_refs":["SRC-004"]},
            {"target":"ODRL Information Model 2.2 and Verifiable Credentials Data Model 2.0","relation":"ALIGN","purpose":"Represent purpose-bound authority policy and portable evidence without importing authorization or credential lifecycles.","required":False,"source_refs":["SRC-006","SRC-007"]},
            {"target":"Web of Things Thing Description 1.1","relation":"ALIGN","purpose":"Project optional properties, actions, events, forms and security metadata for networked or embodied agent interfaces.","required":False,"source_refs":["SRC-009"]},
        ],
        "service_layers":service_layers(),
        "coverage":coverage(),
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
