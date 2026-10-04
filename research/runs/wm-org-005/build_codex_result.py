#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-ORG-005."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent

SOURCES = [
    {"id":"SRC-001","title":"Employment Relationship Recommendation, 2006 (No. 198)","organization":"International Labour Organization","url":"https://www.ilo.org/resource/other/r198-employment-relationship-recommendation-2006","version_or_date":"Recommendation No. 198, 2006","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Requires national policy to clarify employment relationships, combat disguised relationships, use facts about work and remuneration over party labels, provide indicators, access to determination and effective dispute settlement."},
    {"id":"SRC-002","title":"International Classification of Status in Employment (ICSE-18) Manual","organization":"International Labour Organization","url":"https://www.ilo.org/publications/international-classification-status-employment-icse-18-manual","version_or_date":"ICSE-18 Manual, 2023","source_type":"classifier","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Defines statistical status categories using authority and economic-risk dimensions, including employees and dependent contractors; it informs classification evidence but is not a universal legal determination."},
    {"id":"SRC-003","title":"Resolution concerning statistics on work relationships","organization":"International Labour Organization","url":"https://www.ilo.org/resource/conference-paper/resolution-concerning-statistics-work-relationships","version_or_date":"20th ICLS resolution, 17 October 2018","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Provides the international statistical concepts of work relationships and the ICSE-18 and ICSaW-18 classifications, supporting explicit purpose and profile qualification."},
    {"id":"SRC-004","title":"International Standard Classification of Occupations 2008","organization":"International Labour Organization","url":"https://isco.ilo.org/en/isco-08/","version_or_date":"ISCO-08, endorsed March 2008; current ILO edition","source_type":"classifier","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Distinguishes a job as tasks and duties performed or meant to be performed by one person from an occupation as a class of similar jobs, preventing occupation concepts from becoming employment identity."},
    {"id":"SRC-005","title":"The ESCO Classification","organization":"European Commission","url":"https://esco.ec.europa.eu/en/classification","version_or_date":"ESCO v1.2.1, updated 10 December 2025","source_type":"classifier","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Provides versioned multilingual occupation and skill concepts mapped to ISCO-08; useful for typed occupation and skill references, not employment-status determination."},
    {"id":"SRC-006","title":"Directive (EU) 2019/1152 on transparent and predictable working conditions","organization":"European Union","url":"https://eur-lex.europa.eu/eli/dir/2019/1152/oj","version_or_date":"Directive (EU) 2019/1152, 20 June 2019","source_type":"legislation","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Provides an EU profile for timely information about parties, workplace, role, start, duration, probation, remuneration, working time, training and termination procedure while deferring worker status to Member State law and practice."},
    {"id":"SRC-007","title":"Directive 2008/104/EC on temporary agency work","organization":"European Union","url":"https://eur-lex.europa.eu/eli/dir/2008/104/oj","version_or_date":"Directive 2008/104/EC, 19 November 2008","source_type":"legislation","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Provides an EU multi-party profile distinguishing temporary-work agency, worker and user undertaking and supporting assignment-specific equal-treatment context."},
    {"id":"SRC-008","title":"Termination of Employment Convention, 1982 (No. 158)","organization":"International Labour Organization","url":"https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C158","version_or_date":"Convention No. 158, adopted 22 June 1982; in force 23 November 1985","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Defines a ratification-dependent profile for valid reason, procedure, notice, challenge and remedy around employer-initiated termination; applicability must be explicitly pinned."},
    {"id":"SRC-009","title":"The Organization Ontology","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/vocab-org/","version_or_date":"W3C Recommendation, 16 January 2014","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Provides interoperable organization, role, post, membership and interval patterns. Employment may align as a qualified relationship, but this model excludes generic membership and keeps posts and roles external."},
    {"id":"SRC-010","title":"PROV-O: The PROV Ontology","organization":"World Wide Web Consortium","url":"https://www.w3.org/TR/prov-o/","version_or_date":"W3C Recommendation, 30 April 2013","source_type":"ontology","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Supports agents, entities, activities, attribution, derivation, revision and qualified relationships for party assertions, evidence and immutable correction lineage."},
    {"id":"SRC-011","title":"General Data Protection Regulation","organization":"European Union","url":"https://eur-lex.europa.eu/eli/reg/2016/679/oj","version_or_date":"Regulation (EU) 2016/679, 27 April 2016","source_type":"legislation","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Provides an EU privacy profile for purpose limitation, data minimization, accuracy, retention, security, access and rectification of person-linked employment records."},
    {"id":"SRC-012","title":"Date and Time on the Internet: Timestamps","organization":"Internet Engineering Task Force","url":"https://www.rfc-editor.org/rfc/rfc3339","version_or_date":"RFC 3339, July 2002","source_type":"standard","primary_source":True,"authority_tier":1,"accessed_at":"2026-09-06T01:06:00Z","relevance":"Defines interoperable timestamps with seconds and an explicit relationship to UTC for lifecycle and knowledge-time records."},
]

BUNDLES = [
    ("relationship-identity-parties-and-authority", "Relationship identity, parties and authority", "Identifies the employment relationship and the parties and authorities around it.", "A relationship must remain resolvable independently of mutable jobs, assignments, labels and organizations' internal records.", ["SRC-001","SRC-006","SRC-009","SRC-010"], [
        ("relationship-master-identity", "Relationship master identity", "Stable identity, aliases, source systems and duplicate or successor handling.", ["SRC-001","SRC-009","SRC-010"], [
            ("authoritative-relationship-identifier-and-master-system", "Authoritative relationship identifier and master system", "The stable identifier, issuer, namespace, master system, status and typed aliases for one employment relationship.", "identity", ["SRC-001","SRC-009","SRC-010"], "identifier", True),
            ("duplicate-merge-split-transfer-and-successor-lineage", "Duplicate, merge, split, transfer and successor lineage", "Rules and evidence that reconcile duplicates or create successors without erasing cited relationship identities.", "lifecycle", ["SRC-001","SRC-010"], "object", False),
        ]),
        ("party-topology-and-authority", "Party topology and authority", "Worker, employer and other party roles, their effective intervals and authority sources.", ["SRC-001","SRC-006","SRC-007","SRC-010"], [
            ("worker-and-employing-party-bindings", "Worker and employing party bindings", "Typed references to worker and employing party with asserted and effective role intervals and identity provenance.", "relationship", ["SRC-001","SRC-006","SRC-010"], "object", True),
            ("agency-host-client-paymaster-platform-and-authority-roles", "Agency, host, client, paymaster, platform and authority roles", "Allows multi-party work without treating every operational or payment party as the legal employer.", "authority", ["SRC-001","SRC-007"], "collection", False),
        ]),
    ]),
    ("legal-classification-jurisdiction-and-recognition", "Legal classification, jurisdiction and recognition", "Separates evidence, statistical classifications, party assertions and legally effective determinations.", "Employment status is jurisdiction-bound and may be disputed, retroactively determined or different for different purposes.", ["SRC-001","SRC-002","SRC-003","SRC-006"], [
        ("basis-jurisdiction-and-instruments", "Basis, jurisdiction and instruments", "The asserted basis, applicable territory, purpose and governing instruments.", ["SRC-001","SRC-006","SRC-008"], [
            ("contractual-statutory-factual-and-appointment-basis", "Contractual, statutory, factual and appointment basis", "References the instrument or facts said to create employment and records who asserts that basis.", "authority", ["SRC-001","SRC-006"], "object", True),
            ("jurisdiction-scope-applicable-law-and-collective-instruments", "Jurisdiction, scope, applicable law and collective instruments", "Pins territorial, personal and subject scope plus applicable legal, collective, policy and ratification profiles.", "constraint", ["SRC-001","SRC-006","SRC-008"], "collection", True),
        ]),
        ("status-classification-and-indicators", "Status classification and indicators", "Records purpose-qualified categories and the evidence used for them.", ["SRC-001","SRC-002","SRC-003"], [
            ("employee-worker-dependent-contractor-and-self-employed-assertions", "Employee, worker, dependent-contractor and self-employed assertions", "Parallel party, statistical, administrative and legal status assertions with scheme, purpose, time and confidence.", "classification", ["SRC-001","SRC-002","SRC-003"], "collection", True),
            ("control-dependence-remuneration-risk-and-integration-indicators", "Control, dependence, remuneration, risk and integration indicators", "Observable indicators and counter-indicators with method, source and applicability, never a label-only conclusion.", "evidence", ["SRC-001","SRC-002"], "collection", False),
        ]),
        ("determination-dispute-and-recognition", "Determination, dispute and recognition", "Recognition criteria, competent determinations, competing assertions and correction.", ["SRC-001","SRC-002","SRC-010"], [
            ("competent-status-determination-scope-and-effect", "Competent status determination, scope and effect", "Authority, decision reference, legal basis, effective period, appeal state and exact purposes for which a determination controls.", "decision", ["SRC-001","SRC-010"], "object", False),
            ("misclassification-dispute-appeal-and-retroactive-correction", "Misclassification dispute, appeal and retroactive correction", "Contested status, claims, decisions, remedies and bitemporal corrections while prior assertions remain visible.", "validation", ["SRC-001","SRC-010"], "object", False),
        ]),
    ]),
    ("commencement-terms-and-working-context", "Commencement, terms and working context", "Captures when the relationship begins and which external terms and work-context assertions apply.", "Transparent working conditions require versioned, time-qualified bindings rather than copied contract or payroll payloads.", ["SRC-001","SRC-006","SRC-007"], [
        ("commencement-probation-and-time", "Commencement, probation and time", "Agreed, recorded, effective and recognized beginning and probation facts.", ["SRC-006","SRC-012"], [
            ("agreement-appointment-start-and-antecedent-service", "Agreement, appointment, start and antecedent service", "Creation basis, agreed and actual start, credited prior service, seniority anchor and evidence references.", "temporal", ["SRC-006","SRC-010","SRC-012"], "object", True),
            ("probation-trial-confirmation-and-rescission", "Probation, trial, confirmation and rescission", "Probation basis, limits, extensions, outcome and relationship effect without confusing probation with employment identity.", "lifecycle", ["SRC-006"], "object", False),
        ]),
        ("term-bindings-and-precedence", "Term bindings and precedence", "Versioned references to individual, collective, statutory and policy terms.", ["SRC-006","SRC-008","SRC-010"], [
            ("duration-renewal-notice-and-precedence", "Duration, renewal, notice and precedence", "Open-ended or fixed duration, end condition, renewal, notice method and precedence among applicable term sources.", "constraint", ["SRC-006","SRC-008"], "object", True),
            ("remuneration-benefit-training-and-expense-references", "Remuneration, benefit, training and expense references", "Bindings to compensation, benefit, training and reimbursable-expense masters with effective time and disclosure class.", "relationship", ["SRC-005","SRC-006"], "collection", False),
        ]),
        ("working-time-place-and-pattern", "Working time, place and pattern", "Capacity and location context that qualifies the relationship without replacing schedules or attendance.", ["SRC-006","SRC-007"], [
            ("capacity-working-time-pattern-overtime-and-predictability", "Capacity, working-time pattern, overtime and predictability", "Contracted capacity, standard pattern, predictability, reference hours and applicable overtime or minimum-notice rules.", "measurement", ["SRC-006"], "quantity", False),
            ("workplace-remote-mobile-and-cross-border-context", "Workplace, remote, mobile and cross-border context", "Primary and permitted places, remote or mobile mode, host territory, travel expectation and jurisdiction implications by reference.", "spatial", ["SRC-006","SRC-007"], "collection", False),
        ]),
    ]),
    ("role-assignment-and-occupation-binding", "Role, assignment and occupation binding", "Connects employment to positions, assignments, occupations and skills without importing their lifecycles.", "A relationship can continue through several jobs or assignments, and an occupation is a classifier rather than the relationship itself.", ["SRC-004","SRC-005","SRC-007","SRC-009"], [
        ("position-role-and-assignment", "Position, role and assignment", "Time-qualified realization links to externally mastered organizational work records.", ["SRC-007","SRC-009"], [
            ("position-unit-role-and-reporting-references", "Position, unit, role and reporting references", "References formal positions, organizational units, role concepts and reporting structures without copying them into employment.", "relationship", ["SRC-009"], "collection", False),
            ("assignment-realization-validity-and-concurrency", "Assignment realization, validity and concurrency", "Links one employment relationship to concurrent or sequential WM-ORG-016 assignments and records link validity only.", "composition", ["SRC-007","SRC-009"], "collection", False),
        ]),
        ("job-occupation-and-skill-context", "Job, occupation and skill context", "Separates the concrete job from reusable occupation and skill concepts.", ["SRC-004","SRC-005"], [
            ("job-task-duty-and-occupation-classification-reference", "Job, task, duty and occupation-classification reference", "Binds current or historic job and assignment references to versioned ISCO, ESCO or local occupation concepts.", "classification", ["SRC-004","SRC-005"], "collection", False),
            ("required-used-and-developed-skill-references", "Required, used and developed skill references", "Purpose-qualified links to skill concepts and evidence while qualifications and assessments remain external.", "relationship", ["SRC-004","SRC-005"], "collection", False),
        ]),
    ]),
    ("lifecycle-continuity-and-separation", "Lifecycle, continuity and separation", "Represents relationship state and change independently of assignment, payroll or access-system activity.", "Employment may continue through leave, transfer or employer succession and may end through several governed bases, so changes need explicit effect and authority.", ["SRC-001","SRC-006","SRC-007","SRC-008","SRC-010"], [
        ("status-continuity-and-succession", "Status, continuity and succession", "Current and historic relationship state, continuity and successor employer bindings.", ["SRC-001","SRC-006","SRC-010"], [
            ("active-inactive-disputed-and-unknown-relationship-state", "Active, inactive, disputed and unknown relationship state", "Time-qualified state assertion, source, confidence and validation that never derives state from one operational system alone.", "state", ["SRC-001","SRC-010"], "object", True),
            ("employer-succession-transfer-and-service-continuity", "Employer succession, transfer and service continuity", "Predecessor and successor parties, authority, continuity decision, credited service and unchanged or changed term bindings.", "lifecycle", ["SRC-006","SRC-010"], "object", False),
        ]),
        ("interruption-change-and-resumption", "Interruption, change and resumption", "Relationship-level effects of leave, suspension, secondment and material amendment.", ["SRC-006","SRC-007","SRC-010"], [
            ("leave-suspension-secondment-and-nonperformance-effect", "Leave, suspension, secondment and nonperformance effect", "References the external event and records whether employment, service, pay, benefits, assignment and notice clocks continue or pause.", "event", ["SRC-006","SRC-007"], "collection", False),
            ("term-amendment-consent-authority-and-effective-change", "Term amendment, consent, authority and effective change", "The proposed and effective change, source instrument, affected bindings, party acknowledgements and dispute state.", "process", ["SRC-006","SRC-010"], "object", False),
        ]),
        ("separation-and-post-employment", "Separation and post-employment", "End basis, procedure, contest and surviving bindings.", ["SRC-006","SRC-008","SRC-010"], [
            ("resignation-expiry-dismissal-mutual-end-and-other-basis", "Resignation, expiry, dismissal, mutual end and other basis", "Qualified separation basis, initiating party, decision or notice references, stated reason, effective time and uncertainty.", "lifecycle", ["SRC-006","SRC-008"], "object", False),
            ("notice-challenge-remedy-and-surviving-obligation-references", "Notice, challenge, remedy and surviving-obligation references", "Notice compliance, appeal, reinstatement or compensation outcome and surviving confidentiality or other obligation bindings.", "decision", ["SRC-008","SRC-010"], "collection", False),
        ]),
    ]),
    ("assertions-evidence-privacy-and-trust", "Assertions, evidence, privacy and trust", "Keeps both parties' assertions, authoritative determinations and minimum-disclosure access auditable.", "Employment data is sensitive and power-asymmetric; provenance and access rights cannot be collapsed into employer ownership of the truth.", ["SRC-001","SRC-010","SRC-011"], [
        ("party-assertions-evidence-and-quality", "Party assertions, evidence and quality", "Attribution, acknowledgement, discrepancies and evidence quality for relationship facts.", ["SRC-001","SRC-010"], [
            ("worker-employer-third-party-and-authority-assertions", "Worker, employer, third-party and authority assertions", "Parallel attributable statements with purpose, valid time, knowledge time, confidence, acknowledgement and contest status.", "provenance", ["SRC-001","SRC-010"], "collection", True),
            ("evidence-attestation-freshness-quality-and-reconciliation", "Evidence, attestation, freshness, quality and reconciliation", "Evidence references, issuer, collection method, freshness, reliability, conflicts and explicit reconciliation outcome.", "quality", ["SRC-001","SRC-010"], "collection", False),
        ]),
        ("privacy-access-retention-and-verification", "Privacy, access, retention and verification", "Purpose-bound access, correction, retention and minimum employment verification.", ["SRC-006","SRC-011"], [
            ("purpose-access-correction-portability-and-restriction", "Purpose, access, correction, portability and restriction", "Field and artifact access by role and purpose, worker access, correction route, portability profile and lawful restrictions.", "access", ["SRC-011"], "object", True),
            ("retention-deletion-legal-hold-and-minimal-verification", "Retention, deletion, legal hold and minimal verification", "Per-field retention and tombstone rules plus consent or authority bound verification of only necessary relationship facts.", "retention", ["SRC-001","SRC-011"], "object", True),
        ]),
    ]),
    ("interoperability-governance-and-agent-operations", "Interoperability, governance and agent operations", "Controls profiles, projections, autonomous checks and safe relationship change.", "Machine exchange must preserve authority, time, disagreement, privacy and information-loss semantics across HR, statistical and linked-data projections.", ["SRC-002","SRC-004","SRC-005","SRC-009","SRC-010","SRC-012"], [
        ("profiles-projections-and-agent-control", "Profiles, projections and agent control", "Versioned mappings and permissioned agent actions.", ["SRC-002","SRC-004","SRC-005","SRC-009","SRC-010","SRC-012"], [
            ("jurisdiction-statistical-hr-and-linked-data-profiles", "Jurisdiction, statistical, HR and linked-data profiles", "Pinned source and target versions, mapping scope, transformed or omitted values, validation and non-round-trip declarations.", "interoperability", ["SRC-002","SRC-004","SRC-005","SRC-009"], "collection", False),
            ("agent-operation-authority-validation-and-audit", "Agent operation authority, validation and audit", "Allowed read, append, reconcile, propose, confirm and forbidden actions with preconditions, effects, rollback and audit evidence.", "security", ["SRC-001","SRC-010","SRC-011"], "object", True),
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
            {"id": f"{fid}-q01", "text": f"What exact values, references, qualifiers and explicit unknowns must be recorded for {name.lower()}?", "kind": kind, "answer_data": ["value or reference", "scheme and scope", "valid time", "explicit unknowns"]},
            {"id": f"{fid}-q02", "text": f"Which party, authority, source and evidence establishes {name.lower()}, at what asserted, effective and knowledge time, and with what confidence?", "kind": "evidence", "answer_data": ["asserting party", "authority and basis", "source and evidence", "times", "confidence"]},
            {"id": f"{fid}-q03", "text": f"How may {name.lower()} be validated, contested, corrected, superseded, retained or disclosed without erasing prior assertions or importing a neighboring model's lifecycle?", "kind": "validation", "answer_data": ["validation rule", "challenge or correction route", "successor or tombstone", "access and retention effect"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Structured, source-qualified answer data for {name.lower()}.", "value_kind": value_kind, "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Versioned evidence-bearing record for {name.lower()} with authority, valid time, knowledge time, provenance and access marking.", "media_or_form": ["logical record", "signed or attributable evidence reference"], "serial": True, "identity_strategy": f"Employment relationship identifier plus {fid} assertion or event identifier; mutable names, dates and file hashes never identify the relationship.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    return {"bundles": [{"id": bid, "name": name, "description": description, "rationale": rationale, "source_refs": refs, "layers": [{"id": lid, "name": lname, "description": ldescription, "source_refs": lrefs, "findings": [finding(item) for item in findings]} for lid, lname, ldescription, lrefs, findings in layers]} for bid, name, description, rationale, refs, layers in BUNDLES]}


FUNCTIONS = [
    ("register-employment", "Register employment", "Create or attest one employment relationship with stable identity, party bindings, asserted basis and explicit unknowns.", ["worker and employer references", "basis and jurisdiction", "source evidence"], ["employment relationship revision"], ["actor has register or attest authority", "duplicate check completed"], ["new relationship identity and provenance are recorded"], ["SRC-001","SRC-006","SRC-010"]),
    ("assert-or-determine-status", "Assert or determine status", "Record a purpose-qualified party assertion, statistical classification or competent legal determination without collapsing them.", ["relationship", "classification scheme", "indicator evidence", "authority"], ["status assertion or determination"], ["scheme, purpose and jurisdiction are pinned"], ["parallel status views remain attributable and queryable"], ["SRC-001","SRC-002","SRC-003"]),
    ("bind-term-version", "Bind term version", "Attach a versioned external term source with precedence, validity and party acknowledgement.", ["relationship", "term source", "scope and precedence"], ["term binding revision"], ["term source is resolvable", "authority and effective time are known"], ["prior binding remains preserved and the active view is recomputed"], ["SRC-006","SRC-010"]),
    ("link-assignment-realization", "Link assignment realization", "Link a WM-ORG-016 assignment that realizes the relationship without importing assignment execution.", ["relationship", "assignment reference", "valid interval"], ["typed realization link"], ["identities and non-overlap policy validate"], ["assignment becomes discoverable from employment while retaining external mastership"], ["SRC-007","SRC-009"]),
    ("record-commencement", "Record commencement", "Append agreed, actual and effective start facts plus probation and credited-service references.", ["relationship", "commencement evidence"], ["commencement event"], ["relationship exists", "times and sources are qualified"], ["relationship lifecycle begins without overwriting antecedent evidence"], ["SRC-006","SRC-012"]),
    ("suspend-or-resume", "Suspend or resume", "Record relationship-level effect of leave, suspension, secondment or resumption.", ["relationship", "external event", "effect map"], ["interruption or resumption event"], ["authority and current state permit transition"], ["continuity, affected clocks and assignments are explicitly qualified"], ["SRC-006","SRC-007","SRC-010"]),
    ("record-employer-succession", "Record employer succession", "Create a predecessor or successor employer binding with a continuity decision and changed-term map.", ["relationship", "predecessor and successor", "authority evidence"], ["succession event and bindings"], ["party identities are distinct", "continuity basis is cited"], ["relationship history remains continuous or explicitly closes and succeeds"], ["SRC-006","SRC-010"]),
    ("amend-relationship", "Amend relationship", "Append an authorized relationship revision and preserve party acknowledgements and disagreement.", ["relationship", "proposed change", "authority"], ["new relationship revision"], ["change scope and effective time are valid"], ["prior revision remains citable and contested fields stay visible"], ["SRC-006","SRC-010"]),
    ("record-separation", "Record separation", "Record end basis, notice, reason, effective time, challenge state and surviving references.", ["relationship", "separation basis", "notice or decision"], ["separation event"], ["actor authority and applicable profile validate"], ["relationship enters ended or disputed-end state without cascading deletion"], ["SRC-006","SRC-008","SRC-010"]),
    ("reconcile-assertions", "Reconcile assertions", "Compare party and authority assertions and append agreement, disagreement or unresolved reconciliation.", ["assertion set", "evidence", "reconciliation policy"], ["reconciliation record"], ["sources and authority scopes are known"], ["no source is silently overwritten and conflict remains queryable"], ["SRC-001","SRC-010"]),
    ("issue-minimal-verification", "Issue minimal verification", "Create a purpose-bound projection of necessary employment facts under consent or legal authority.", ["relationship", "requester and purpose", "authority", "field policy"], ["digest-pinned verification projection"], ["identity, authority and minimum-necessary fields validate"], ["disclosure is attributable, scoped, expiring and auditable"], ["SRC-001","SRC-011"]),
    ("project-employment-profile", "Project employment profile", "Transform a validated revision into a pinned statistical, HR or linked-data profile with declared loss.", ["relationship revision", "target profile"], ["validated exchange projection"], ["source and target versions are pinned"], ["mapping lineage, omissions and round-trip limits are recorded"], ["SRC-002","SRC-004","SRC-005","SRC-009","SRC-010"]),
]

def service_layers():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Dimension identity, owner, employment-record steward, worker-rights authority and namespace",
                "Person, organization, position, assignment, occupation, contract, policy, payroll, evidence, access and lifecycle-event registries",
                "Master-system mappings for worker, employer, relationship, assignment, status determination and authoritative instrument identifiers",
                "Jurisdiction, classification, privacy, correction, retention, federation and autonomous-agent policies"
            ],
            "namespace_guidance": "Mint employment relationship and assertion identifiers in the adopting Dimension namespace only when no authoritative master identifier exists; preserve parties, assignments, occupations, contracts, payroll, benefits, instruments, evidence and decisions as typed references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local employment, relationship-assertion, status-determination, access and provenance registries"]
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by authoritative employment relationship identifier, issuer and master system, never by worker-employer pair, contract number, position, payroll account, start date or hash alone.",
                "Keep employment, membership, assignment, position, occupation, contract, payroll, attendance, benefit, tax, social-insurance and evidence lifecycles distinct."
            ],
            "patch_rules": [
                "Additive extensions declare target bundle, layer or finding, jurisdiction and worker category, source, authority, privacy, rights and interoperability impact.",
                "Identity, party-role, status-effect or lifecycle-semantics changes require a successor version, bitemporal migration map, rollback path and continued resolution of prior records."
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when relationship identity, party roles, classification scope, valid time, authority, disagreement, access and lifecycle meaning remain intact.",
                "Statistical, HR, legal and linked-data projections pin source and target versions and disclose transformed, omitted, aggregated or non-round-trippable values."
            ]
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative employment master-system identifier qualified by issuer and relationship namespace.",
                "Governed globally resolvable employment relationship IRI with explicit worker and employing-party references.",
                "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."
            ],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep asserted, agreed, effective, observed, decision, knowledge, notice and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {employment-id}--{artifact-kind}--{assertion-or-event-id}; never use a person's name, employer name, date, job title, contract number, filename or hash alone as relationship identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and profile versions, authority, valid and knowledge times, provenance, assurance, licence and access marking for every retained serial artifact."
        },
        "policies": [
            "The adopting Dimension declares who may attest, register, classify, determine, amend, suspend, transfer, separate, verify, disclose, correct, retain and tombstone employment records.",
            "Employment status is jurisdiction-bound: statistical categories, contract labels, payroll entries and operational indicators are evidence, not universally dispositive legal conclusions.",
            "The worker-employer relationship is power-asymmetric; bilateral provenance never grants either party unilateral authority to erase the other's lawful record, block access or suppress a dispute.",
            "Persons, organizations, positions, assignments, occupations, contracts, payroll, attendance, benefits, tax, social insurance, qualifications, recruitment and work products remain in their owning systems and are referenced.",
            "Automated agents may read, validate, reconcile and append low-risk observations within policy; legal-status determinations, adverse changes, wider disclosure, separation and destructive retirement require accountable authority."
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, jurisdiction profile, requested valid and knowledge time, evidence freshness and access scope; return the minimum permitted projection with disputed and unknown fields intact."],
            "create": ["Create stable relationship identity, worker and employing-party references, asserted basis, jurisdiction, source provenance and explicit unknowns before attaching terms or assignments."],
            "update": ["Append an assertion, event or successor revision with actor, authority, reason, RFC 3339 time, evidence and before-and-after validation; never overwrite a cited assertion, determination or event."],
            "delete": ["Apply worker-rights, legal-hold, dispute, payroll, tax, social-insurance and retention policy; prefer end state or tombstone, preserve identity and history, and never cascade into referenced parties, assignments, contracts, payments or evidence."]
        },
        "roles": [
            {"name":"Dimension owner","responsibilities":["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name":"Worker or worker-authorized steward","responsibilities":["Attest worker-side facts, exercise access and correction rights, acknowledge changes and preserve contested assertions."]},
            {"name":"Employer or employing authority","responsibilities":["Attest employer-side basis, terms, status events and statutory records within mandate."]},
            {"name":"HR or relationship registrar","responsibilities":["Maintain identifiers, party bindings, effective terms, assignment links and lifecycle records without making unauthorized legal conclusions."]},
            {"name":"Competent status or labour authority","responsibilities":["Determine status, scope, effective period, remedy and appeal effect within jurisdiction."]},
            {"name":"Worker representative or collective-bargaining steward","responsibilities":["Maintain representative authority and collective-instrument bindings and support dispute evidence."]},
            {"name":"Privacy and access steward","responsibilities":["Apply purpose limitation, minimum disclosure, access, correction, portability, retention and security rules."]},
            {"name":"Independent auditor","responsibilities":["Review authority, changes, disclosures, corrections and provenance without rewriting party evidence."]}
        ],
        "access": {
            "default_rule": "Deny mutation and disclosure of person-linked terms, compensation, health, dispute, separation or performance-related data unless active Dimension, role, purpose, jurisdiction and field policy grant it; expose the minimum necessary projection.",
            "scopes": ["bundle","layer","finding","artifact"],
            "exceptions": ["Statutory, judicial, labour-inspection or emergency access must cite authority, be purpose-bound, attributable and reviewable, and must not erase original assertions, disputes, decisions or audit evidence."],
            "audit_requirements": ["Log actor, agent, role, purpose, relationship and party identities, action, policy and jurisdiction profile, RFC 3339 timestamp with offset, affected scope, requested and effective authority, evidence and outcome."]
        },
        "agents_bootstrap": {
            "filename":"AGENTS.md",
            "required_fields":["Name","Type","Specification URL","Storage type URL","Interface URL","Processes URL"],
            "read_order":[
                "Read the nearest Dimension-owner AGENTS.md, employment mastership, worker-rights, jurisdiction, privacy, correction, retention, dispute and federation policies.",
                "Read this model AGENTS.md, pinned spec.yaml and required person, organization, assignment, position, occupation, contract, policy, payroll, evidence, access and decision model instructions before mutation or disclosure."
            ]
        }
    }


def coverage():
    dims = [
        ("identity", "Stable relationship identity, issuer, aliases, duplicates and successor lineage are explicit."),
        ("classification and definition", "Employment is separated from membership, assignment and self-employment while jurisdiction and purpose qualify status."),
        ("direct relational properties", "Party topology, basis, terms, capacity and relationship-owned state are represented; physical properties are not applicable."),
        ("recognition and observation", "Indicators, counter-indicators, methods, determination authority, confidence and confusing neighboring classes are covered."),
        ("capabilities and possible actions", "Register, classify, bind, link, amend, suspend, transfer, separate, reconcile, verify and project operations are governed."),
        ("composition", "Assignments realize employment through a typed candidate relation while all neighboring master lifecycles remain external."),
        ("lifecycle", "Commencement, probation, continuity, interruption, succession, amendment and separation retain immutable history."),
        ("relationships", "Worker, employer, agency, host, client, paymaster, platform, authority, assignment and instrument roles are typed and time-qualified."),
        ("temporal", "Asserted, agreed, effective, observed, decision, notice and knowledge times remain distinct and use RFC 3339 for events."),
        ("spatial", "Workplace, remote, mobile, host-territory and cross-border context are referenced with jurisdiction implications."),
        ("provenance", "Party and authority assertions, evidence, derivation, revision and reconciliation are attributable."),
        ("ownership and stewardship", "Bilateral evidence and power asymmetry are explicit; each referenced record retains its master system."),
        ("validation and quality", "Duplicates, status scope, indicator sufficiency, stale state, conflicting assertions and projection loss are checked."),
        ("access and privacy", "Purpose limitation, minimum disclosure, correction, restriction, worker access and audit are covered."),
        ("retention and deletion", "Per-field retention, legal hold, tombstone and non-cascading deletion preserve lawful evidence and history."),
        ("interoperability", "ICSE, ISCO, ESCO, W3C ORG, HR and jurisdiction profiles are pinned and loss-aware.")
    ]
    return {
        "claim": "Covers a general employment relationship from identity and legal classification through terms, assignments, continuity, separation, evidence, privacy and exchange, with explicit jurisdiction and neighboring-model boundaries.",
        "confidence": "medium",
        "checklist": [{"dimension": d, "status": "covered", "notes": n} for d, n in dims],
        "known_omissions": [
            "National and subnational labour-law, public-service, military, seafarer, domestic-work, child-work, platform-work, apprenticeship and collective-bargaining profiles require specialist treatment.",
            "Contract, assignment, payroll, compensation, benefits, attendance, leave, tax, social insurance, qualification, recruitment and performance lifecycles remain in neighboring models.",
            "Certified HR-schema, ICSE-18, ISCO-08, ESCO and jurisdictional crosswalks, conformance suites and rights-impact fixtures remain future work."
        ],
        "conflicts": [
            "Employment status may differ between statistical, tax, social-insurance and labour-law purposes and must never be collapsed into one unqualified category.",
            "The employer, agency, host, client, paymaster, platform and beneficial controller may differ in multi-party work.",
            "An assignment, payroll event, workplace credential or contract label may exist without proving current employment status or legal effect."
        ],
        "regional_assumptions": [
            "EU Directives 2019/1152 and 2008/104/EC and the GDPR provide European profiles and do not create universal global legal obligations.",
            "ILO Convention No. 158 is applicable only where its ratification and implementation scope is verified; Recommendation No. 198 remains guidance for national policy.",
            "ICSE-18 and ISCO-08 are statistical classifications and ESCO is a European semantic classification, not direct legal-status authorities."
        ],
        "adversarial_checks": [
            "Reject any Employment record that includes generic organizational membership or treats worker-employer pair, job title, contract number or payroll account as unique identity.",
            "Reject a legal-status conclusion inferred solely from party label, contract type, payment method, occupation, one control indicator or ICSE category.",
            "Reject ownership inferred from record custody and reject employer-only control over worker access, correction, dispute, portability or lawful retention.",
            "Reject active-status inference from an assignment, payroll event, building access or old contract without qualified current evidence.",
            "Reject mutation, verification or separation beyond the actor's jurisdiction, purpose, field scope and authority and preserve prior assertions bitemporally."
        ]
    }


def build():
    return {
        "schema_version":"1.0.0",
        "model": {
            "registry_id":"vr.wm-org-005",
            "model_id":"WM-ORG-005",
            "name":"Employment",
            "entry_kind":"relationship",
            "purpose":"Represent one governed, jurisdiction-qualified employment relationship between a worker party and an employing party, including identity, classification evidence, terms, assignment realization, continuity, separation, disagreement and provenance without depending on storage or interface format.",
            "scope_statement":"Owns employment relationship identity, party-role topology, asserted basis and jurisdiction, purpose-qualified classification assertions and determinations, effective term bindings, assignment realization links, relationship state, continuity and separation events, party assertions, evidence quality, privacy and interoperability projections while external systems own parties, positions, assignments, occupations, contracts, payroll, attendance, benefits, tax, social insurance, qualifications, recruitment, access grants and evidence objects.",
            "in_scope":["Employment relationship identity, worker and employing-party bindings, multi-party roles, basis, jurisdiction, classification assertions, determinations and recognition indicators", "Commencement, probation, term bindings, working-time and workplace context, position, assignment, occupation and skill references", "Relationship state, continuity, interruption, succession, separation, disputes, evidence, privacy, retention, verification, provenance and exchange"],
            "out_of_scope":["Generic organizational membership and affiliation, which belong to WM-ORG-006 Membership", "Person, organization, unit, position, occupation, assignment, contract, payroll, compensation, attendance, benefits, tax, social insurance, qualification, recruitment, performance and work-product master lifecycles", "A universal legal definition of employee, worker or self-employment, or automatic authority for an agent to determine status, change terms, disclose sensitive data or end employment"],
            "boundary_notes":[
                {"neighbor":"Membership", "distinction":"Employment is a work relationship with asserted legal or factual basis, terms and labour effects; generic belonging, affiliation and member standing are owned by WM-ORG-006.", "source_refs":["SRC-001","SRC-009"]},
                {"neighbor":"Work Assignment", "distinction":"WM-ORG-016 owns assignment identity, scope, duties, execution and lifecycle; Employment owns only the typed, time-qualified link showing which assignments realize the relationship.", "source_refs":["SRC-004","SRC-007","SRC-009"]},
                {"neighbor":"Position, Role and Occupation", "distinction":"A position can exist vacant, a role is a reusable concept and an occupation classifies similar jobs; none is an employment relationship or proves its legal status.", "source_refs":["SRC-004","SRC-005","SRC-009"]},
                {"neighbor":"Contract, Policy, Law and Collective Agreement", "distinction":"Normative instruments retain independent identity, text, authority, version and lifecycle; Employment stores versioned applicability and precedence bindings.", "source_refs":["SRC-001","SRC-006","SRC-008"]},
                {"neighbor":"Payroll, Compensation, Attendance, Benefits, Tax and Social Insurance", "distinction":"Transactions and accounts remain external evidence or consequences; their existence or absence alone never proves relationship identity, status or continuity.", "source_refs":["SRC-001","SRC-002","SRC-006"]},
                {"neighbor":"Recruitment and Onboarding", "distinction":"Candidate selection and operational onboarding or offboarding are processes that may create or implement employment but do not own the relationship's continuing legal and evidential record.", "source_refs":["SRC-001","SRC-006"]}
            ]
        },
        "sources": SOURCES,
        "structure": structure(),
        "functions": [{"id":r[0],"name":r[1],"description":r[2],"inputs":r[3],"outputs":r[4],"preconditions":r[5],"effects":r[6],"source_refs":r[7]} for r in FUNCTIONS],
        "composition":[
            {"target":"WM-ORG-016 Work Assignment", "relation":"COMPOSE", "purpose":"Represent assignments as typed external realizations of employment without importing their execution or lifecycle.", "required":False, "source_refs":["SRC-004","SRC-007","SRC-009"]},
            {"target":"Person, Organization, Organizational Unit, Position, Occupation, Skill, Contract, Policy, Payroll, Benefit, Tax, Social Insurance, Qualification, Evidence and Access models", "relation":"REFERENCE", "purpose":"Connect governed employment context while retaining source ownership and independent lifecycle.", "required":True, "source_refs":["SRC-001","SRC-004","SRC-005","SRC-006","SRC-010","SRC-011"]},
            {"target":"ILO Recommendation No. 198", "relation":"ALIGN", "purpose":"Qualify employment-recognition indicators, disguised relationships, party labels, determination and dispute principles.", "required":True, "source_refs":["SRC-001"]},
            {"target":"ICSE-18 and ISCO-08", "relation":"ALIGN", "purpose":"Project statistical status and occupation classifications without granting them universal legal effect.", "required":False, "source_refs":["SRC-002","SRC-003","SRC-004"]},
            {"target":"ESCO", "relation":"ALIGN", "purpose":"Reference versioned multilingual occupation and skill concepts.", "required":False, "source_refs":["SRC-005"]},
            {"target":"W3C ORG and PROV-O", "relation":"ALIGN", "purpose":"Project qualified organization relationships, roles, intervals, assertions, derivation and revision while excluding generic membership from the Employment boundary.", "required":False, "source_refs":["SRC-009","SRC-010"]}
        ],
        "service_layers": service_layers(),
        "coverage": coverage()
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
