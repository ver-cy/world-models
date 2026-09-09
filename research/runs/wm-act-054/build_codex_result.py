#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-ACT-054."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T11:10:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "ICH E6(R3) Guideline for Good Clinical Practice", "International Council for Harmonisation", "https://database.ich.org/sites/default/files/ICH_E6%28R3%29_Step4_FinalGuideline_2025_0106_ErrorCorrections_2025_1024.pdf", "Step 4 final 6 January 2025; error corrections 24 October 2025", "standard", "Defines participant protection, informed consent, IRB or IEC review, investigator and sponsor responsibilities, safety, data governance and essential records for human clinical trials."),
    src(2, "ICH E8(R1) General Considerations for Clinical Studies", "International Council for Harmonisation", "https://database.ich.org/sites/default/files/ICH_E8-R1_Guideline_Step4_2021_1006.pdf", "Step 4 final 6 October 2021", "standard", "Defines participant protection, quality by design, study population, design and critical-to-quality factors across clinical studies."),
    src(3, "WMA Declaration of Helsinki", "World Medical Association", "https://www.wma.net/policies-post/wma-declaration-of-helsinki/", "Current official revision 19 October 2024", "standard", "Provides ethical principles for medical research involving human participants, identifiable material or identifiable data."),
    src(4, "45 CFR Part 46 Protection of Human Subjects", "United States Office of the Federal Register", "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46", "Current eCFR as of 3 September 2026", "legislation", "Provides the United States Common Rule profile for human-subject research, consent, IRB review and additional protections."),
    src(5, "The Belmont Report", "United States Department of Health and Human Services", "https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html", "18 April 1979; HHS page reviewed 22 June 2026", "public-authority", "Provides respect for persons, beneficence and justice and distinguishes research from practice."),
    src(6, "Regulation (EU) No 536/2014 on clinical trials", "European Union", "https://eur-lex.europa.eu/eli/reg/2014/536/oj", "16 April 2014; consolidated legal record at access", "legislation", "Provides an EU medicinal-product clinical-trial profile for subject protection, authorization, consent, safety and records."),
    src(7, "WHO Trial Registration Data Set", "World Health Organization", "https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set", "Version 1.3.1 current at access", "registry", "Defines the minimum public trial-registration dataset and keeps public study registration distinct from participant-level records."),
    src(8, "FHIR R5 ResearchSubject", "HL7 International", "https://hl7.org/fhir/R5/researchsubject.html", "FHIR 5.0.0 R5, Trial Use", "schema", "Defines study-specific subject identity, subject and study references, progress, period, assigned and actual comparison groups, and consent references."),
    src(9, "FHIR R5 ResearchStudy", "HL7 International", "https://hl7.org/fhir/R5/researchstudy.html", "FHIR 5.0.0 R5, Trial Use", "schema", "Defines the external research-study resource used by the participation aggregate."),
    src(10, "FHIR R5 Consent", "HL7 International", "https://hl7.org/fhir/R5/consent.html", "FHIR 5.0.0 R5, Trial Use", "schema", "Defines source-linked permission and denial choices, actors, purposes, periods and provisions without defining enforcement."),
    src(11, "Operational Data Model", "Clinical Data Interchange Standards Consortium", "https://www.cdisc.org/standards/data-exchange/odm-xml/odm-v2-0", "ODM 2.0 published 23 August 2023", "schema", "Defines platform-neutral clinical-study data, metadata, administrative data, reference data and audit information for interchange and archival."),
    src(12, "CDASH Implementation Guide", "Clinical Data Interchange Standards Consortium", "https://www.cdisc.org/standards/foundational/cdash/cdashig-v2-2", "CDASHIG 2.2 published 28 September 2021", "standard", "Provides a versioned clinical-data acquisition profile; detailed normative files require authorized access."),
    src(13, "ISO 14155 Clinical investigation of medical devices for human subjects", "International Organization for Standardization", "https://www.iso.org/standard/14155", "ISO 14155:2026 edition 4, published March 2026", "standard", "Official catalogue metadata describes current good clinical practice for medical-device investigations; normative text is access-restricted."),
    src(14, "HIPAA de-identification guidance", "United States Department of Health and Human Services", "https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html", "Guidance page reviewed 3 February 2025", "public-authority", "Defines the United States HIPAA Expert Determination and Safe Harbor profiles and warns that residual re-identification risk is not zero."),
    src(15, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation 30 April 2013", "ontology", "Defines entities, activities, agents, attribution, association, revision, invalidation and time for provenance and corrections."),
    src(16, "Regulation (EU) 2016/679 General Data Protection Regulation", "European Union", "https://eur-lex.europa.eu/eli/reg/2016/679/oj", "27 April 2016; applicable from 25 May 2018", "legislation", "Provides an EU privacy, lawful-processing, purpose, minimization, rights, security and accountability profile."),
    src(17, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339 July 2002", "standard", "Provides interoperable timestamps with seconds and explicit UTC relationship."),
    src(18, "ClinicalTrials.gov Study Data Structure", "United States National Library of Medicine", "https://clinicaltrials.gov/data-api/about-api/study-data-structure", "Modernized API model current at access; API page updated 26 August 2025", "registry", "Provides a public study-level registry projection and participant-flow aggregates, not individual participant records."),
]


ROWS = [
    ("participation-identity-subject-profile-and-study-binding", "Participation identity, subject profile and study binding", "The aggregate must identify exactly one subject-to-study participation without absorbing either external master", [
        ("participation-root-and-study-protocol-binding", "Participation root and study or protocol binding", ["SRC-001", "SRC-002", "SRC-008", "SRC-009", "SRC-015"], [
            ("participation-root-identity-namespace-owner-and-current-head", "Participation root identity, namespace, owner and current head", "identity", True),
            ("study-protocol-site-cohort-and-jurisdiction-binding", "Study, protocol, site, cohort and jurisdiction binding", "relationship", True),
        ]),
        ("subject-kind-profile-and-protected-identity", "Subject kind, profile and protected identity", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-008", "SRC-016"], [
            ("subject-kind-unit-of-analysis-species-and-population-profile", "Subject kind, unit of analysis, species and population profile", "classification", True),
            ("external-subject-master-study-identifiers-pseudonym-and-link-key", "External subject master, study identifiers, pseudonym and link key", "security", True),
        ]),
    ]),
    ("recruitment-screening-eligibility-and-consent", "Recruitment, screening, eligibility and consent", "Contact, evaluation, permission and enrolment are separate sourced events and decisions", [
        ("recruitment-prescreening-and-screening", "Recruitment, prescreening and screening", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006"], [
            ("recruitment-source-contact-permission-prescreening-and-candidate-state", "Recruitment source, contact permission, prescreening and candidate state", "process", False),
            ("screening-event-procedure-result-status-failure-and-rescreening", "Screening event, procedure, result, status, failure and rescreening", "event", False),
        ]),
        ("eligibility-and-permission", "Eligibility and permission", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-010", "SRC-013"], [
            ("criterion-evaluation-eligibility-decision-waiver-authority-and-evidence", "Criterion evaluation, eligibility decision, waiver authority and evidence", "decision", True),
            ("consent-assent-representative-permission-reconsent-refusal-and-source", "Consent, assent, representative permission, reconsent, refusal and source", "authority", True),
        ]),
    ]),
    ("enrolment-allocation-blinding-and-participation-plan", "Enrolment, allocation, blinding and participation plan", "Entry into a study, assignment and the planned path require independent identity, authority and timing", [
        ("enrolment-randomization-allocation-and-blinding", "Enrolment, randomization, allocation and blinding", ["SRC-001", "SRC-004", "SRC-006", "SRC-007", "SRC-008", "SRC-013"], [
            ("enrolment-event-identifier-site-date-authority-and-prerequisites", "Enrolment event, identifier, site, date, authority and prerequisites", "lifecycle", True),
            ("randomization-stratum-allocation-concealment-assigned-arm-and-blinding", "Randomization, stratum, allocation concealment, assigned arm and blinding", "security", False),
        ]),
        ("planned-path-periods-visits-and-activities", "Planned path, periods, visits and activities", ["SRC-001", "SRC-002", "SRC-008", "SRC-009", "SRC-011", "SRC-012"], [
            ("planned-arm-cohort-comparison-group-and-participation-period", "Planned arm, cohort, comparison group and participation period", "composition", False),
            ("planned-visit-activity-intervention-observation-and-window", "Planned visit, activity, intervention, observation and window", "requirement", False),
        ]),
    ]),
    ("actual-participation-safety-adherence-and-compensation", "Actual participation, safety, adherence and compensation", "What happened must remain distinct from assignments, expected activities and conclusions", [
        ("actual-activities-exposure-adherence-and-deviation", "Actual activities, exposure, adherence and deviation", ["SRC-001", "SRC-002", "SRC-006", "SRC-008", "SRC-011", "SRC-012", "SRC-015"], [
            ("actual-visit-activity-intervention-exposure-dose-and-observation-reference", "Actual visit, activity, intervention, exposure, dose and observation reference", "evidence", False),
            ("attendance-adherence-nonadherence-protocol-deviation-and-impact", "Attendance, adherence, nonadherence, protocol deviation and impact", "quality", False),
        ]),
        ("safety-incidents-medical-care-and-compensation", "Safety, incidents, medical care and compensation", ["SRC-001", "SRC-003", "SRC-004", "SRC-006", "SRC-013"], [
            ("safety-observation-adverse-event-seriousness-causality-and-report-reference", "Safety observation, adverse event, seriousness, causality and report reference", "evidence", False),
            ("research-injury-medical-care-compensation-reimbursement-and-payment-reference", "Research injury, medical care, compensation, reimbursement and payment reference", "relationship", False),
        ]),
    ]),
    ("status-outcome-withdrawal-followup-and-data-use", "Status, outcome, withdrawal, follow-up and data use", "Participation status and exit semantics must preserve scope, reason, authority and post-exit obligations", [
        ("states-milestones-holds-and-study-effects", "States, milestones, holds and study effects", ["SRC-001", "SRC-004", "SRC-006", "SRC-008", "SRC-013", "SRC-015"], [
            ("candidate-screened-eligible-consented-enrolled-active-and-followup-state", "Candidate, screened, eligible, consented, enrolled, active and follow-up state", "state", True),
            ("milestone-hold-suspension-site-closure-study-termination-and-subject-effect", "Milestone, hold, suspension, site closure, study termination and subject effect", "event", False),
        ]),
        ("withdrawal-discontinuation-loss-completion-and-disposition", "Withdrawal, discontinuation, loss, completion and disposition", ["SRC-001", "SRC-003", "SRC-004", "SRC-006", "SRC-008", "SRC-010", "SRC-016"], [
            ("refusal-withdrawal-scope-intervention-discontinuation-and-reason", "Refusal, withdrawal scope, intervention discontinuation and reason", "lifecycle", False),
            ("lost-to-followup-completion-off-study-death-reference-and-outcome", "Lost to follow-up, completion, off-study, death reference and outcome", "state", False),
        ]),
    ]),
    ("privacy-deidentification-correction-retention-and-interoperability", "Privacy, de-identification, correction, retention and interoperability", "Protected use requires purpose-bound views, successor corrections and version-pinned projections", [
        ("data-specimen-use-privacy-and-linkage", "Data or specimen use, privacy and linkage", ["SRC-001", "SRC-003", "SRC-004", "SRC-010", "SRC-014", "SRC-016"], [
            ("data-specimen-future-contact-secondary-use-withdrawal-and-retention-scope", "Data, specimen, future contact, secondary use, withdrawal and retention scope", "privacy", True),
            ("pseudonymization-deidentification-linkage-reidentification-risk-and-authority", "Pseudonymization, de-identification, linkage, re-identification risk and authority", "security", True),
        ]),
        ("access-correction-retention-and-projections", "Access, correction, retention and projections", ["SRC-001", "SRC-004", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-015", "SRC-016", "SRC-017", "SRC-018"], [
            ("role-purpose-access-disclosure-audit-correction-hold-and-disposition", "Role, purpose, access, disclosure, audit, correction, hold and disposition", "access", True),
            ("fhir-cdisc-who-clinicaltrials-registry-projection-version-and-loss", "FHIR, CDISC, WHO, ClinicalTrials registry projection, version and loss", "interoperability", False),
        ]),
    ]),
]

KINDS = ["identity", "classification", "relationship", "authority", "requirement", "constraint", "event", "temporal", "composition", "evidence", "ownership", "measurement", "exception", "provenance", "process", "validation", "privacy", "lifecycle", "quality", "security", "retention", "interoperability", "decision", "state"]


def finding(item, number, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(number + 6) % len(KINDS)], KINDS[(number + 14) % len(KINDS)]]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {low} as source-qualified participation context while keeping person, study, protocol, consent artifact, intervention, observation, safety, payment and identity-linkage masters external.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What stable identity, subject-to-study scope, source-qualified values and explicit unknowns establish {low}?", "kind": kinds[0], "answer_data": ["identifiers, class and participation scope", "source-qualified values and versions", "unknown and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who may assert, review, correct or rely on {low}, under which authority, purpose and limits?", "kind": kinds[1], "answer_data": ["participant, representative and research roles", "authority, policy, purpose and limits", "review, exception and escalation path"]},
            {"id": f"{fid}-q03", "text": f"Which event, effective, recorded, ingested and knowledge times apply to {low}, and which evidence supports them?", "kind": kinds[2], "answer_data": ["distinct event and knowledge times", "evidence, provenance and uncertainty", "successor correction and retention"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed data for {low} with identity, study scope, source, authority, state, time, evidence and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned participation evidence for {low}.", "media_or_form": ["logical research-participation assertion", "identity, permission, state, activity, safety, outcome, privacy or projection record"], "serial": True, "identity_strategy": f"Participation ID plus independent assertion or event ID for {fid}; subject name, study name, date, state, pseudonym and arm never identify a record alone.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles = []
    number = 0
    for bid, bname, rationale, layers in ROWS:
        rendered = []
        for lid, lname, refs, items in layers:
            findings = []
            for item in items:
                number += 1
                findings.append(finding(item, number, refs))
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified participation context for {lname.lower()}.", "source_refs": refs, "findings": findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed participation context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({ref for layer in layers for ref in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-participation", "Register research participation", ["subject master reference", "study reference", "subject profile", "authority"], ["stable participation aggregate"], ["study, subject, protocol, site and jurisdiction are resolved", "creation is authorized"], ["a new subject-to-study participation head is created without copying external masters"], ["SRC-001", "SRC-004", "SRC-008", "SRC-015"]),
    ("bind-identifiers-and-profile", "Bind identifiers and subject profile", ["participation", "identifier assertions", "subject profile"], ["scoped identifier bindings"], ["issuer, namespace, purpose, sensitivity and validity are known"], ["public, operational, pseudonymous and restricted identifiers remain distinguishable"], ["SRC-004", "SRC-008", "SRC-014", "SRC-016"]),
    ("record-recruitment-and-screening", "Record recruitment and screening", ["participation", "contact authority", "screening events"], ["recruitment and screening history"], ["approved procedures, source, actor and times are present"], ["candidate and screening evidence is appended without implying consent or enrolment"], ["SRC-001", "SRC-003", "SRC-004", "SRC-006"]),
    ("record-eligibility-decision", "Record eligibility decision", ["criteria version", "evaluations", "authorized decision"], ["source-qualified eligibility decision"], ["criteria, evaluator, evidence, waivers and jurisdiction pass"], ["eligibility is recorded without autonomous clinical or enrolment action"], ["SRC-001", "SRC-004", "SRC-006", "SRC-007"]),
    ("bind-consent-assent-and-permission", "Bind consent, assent and permission", ["participation", "source consent artifacts", "grantor and representative authority"], ["scoped permission bindings"], ["version, process, actor, capacity, scope, period and verification pass"], ["permission state is linked without replacing source artifacts or enforcement"], ["SRC-001", "SRC-003", "SRC-004", "SRC-010"]),
    ("enroll-allocate-and-blind", "Record enrolment, allocation and blinding", ["eligible and permitted participation", "allocation event", "blinding policy"], ["enrolment and assignment events"], ["prerequisites, authority, method, concealment and views pass"], ["planned assignment is recorded separately from actual exposure"], ["SRC-001", "SRC-004", "SRC-006", "SRC-008"]),
    ("record-participation-activities", "Record participation activities", ["participation", "planned activities", "actual event references"], ["actual participation history"], ["activity, visit, exposure, observation, actor, source and time pass"], ["actual events, adherence and deviations are appended without rewriting plans"], ["SRC-001", "SRC-002", "SRC-008", "SRC-011", "SRC-012"]),
    ("record-safety-and-compensation-links", "Record safety and compensation links", ["participation", "safety, care, injury or payment references"], ["typed protected links"], ["urgency, authority, privacy, causality source and reporting status pass"], ["external safety, medical and payment masters remain authoritative"], ["SRC-001", "SRC-003", "SRC-004", "SRC-006", "SRC-013"]),
    ("withdraw-discontinue-followup-or-close", "Withdraw, discontinue, follow up or close", ["participation", "scope", "reason", "authorized event"], ["successor status and disposition"], ["intervention, participation, contact, data and specimen scopes are explicit"], ["exit semantics and post-exit duties remain distinct and auditable"], ["SRC-001", "SRC-003", "SRC-004", "SRC-006", "SRC-010"]),
    ("correct-project-retain-disclose-and-audit", "Correct, project, retain, disclose and audit", ["participation", "target profile", "access and records policy"], ["successor, projection, disclosure, tombstone or disposition event"], ["mapping versions, loss, privacy, hold, authority and idempotency pass"], ["protected context stays reconstructable and explicit about current head and loss"], ["SRC-001", "SRC-007", "SRC-008", "SRC-010", "SRC-011", "SRC-012", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-018"]),
]


def functions():
    return [{"id": r[0], "name": r[1], "description": f"Governed operation to {r[1].lower()} without autonomous recruitment, consent, clinical decision, intervention, disclosure, re-identification or deletion.", "inputs": r[2], "outputs": r[3], "preconditions": r[4], "effects": r[5], "source_refs": r[6]} for r in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner and research-processing mandate", "Authoritative subject, study, protocol, site, ethics, consent, intervention, observation, safety, payment, identity-linkage, provenance, audit and record registries", "Approved research-type, jurisdiction, recruitment, eligibility, consent, allocation, safety, privacy, retention and interoperability profiles", "Role, delegation, emergency, unblinding, re-identification, disclosure and agent-operation policies"],
            "namespace_guidance": "Mint participation, identifier-binding, screening, decision, permission, enrolment, allocation, state, activity, deviation, safety-link, withdrawal, correction, disclosure and event IDs; preserve external master identifiers.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize one participation by authoritative research-system identifier, subject reference, study reference and owning namespace; never by name, pseudonym, arm, state or date alone.", "Keep person or other subject, research study, participation, consent artifact, eligibility decision, allocation event, intervention, observation, adverse event and payment independently identifiable."],
            "patch_rules": ["Extensions declare research type, subject kind, jurisdiction, ethics, privacy, retention and interoperability effects.", "Released identity, permission, allocation, state, activity, safety, withdrawal and disclosure assertions are immutable; corrections create linked successors.", "Never silently change subject or study binding, consent scope, eligibility, assignment, exposure, safety, withdrawal, privacy, retention or provenance."],
            "compatibility_rules": ["Ignore additive fields only when participation identity, subject and study scope, record kind, source, authority, state, time, privacy and provenance survive.", "Every projection pins standard, implementation guide, profile, code-list and mapping versions and declares information loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each participation, assertion, decision, permission or event, qualified by issuer, namespace and record kind.", "Governed globally resolvable research-participation IRI.", "Dimension UUID or ULID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish recruitment, screening, decision, consent, enrolment, allocation, activity, observation, safety, withdrawal, recorded, ingested and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {participation-id}--{assertion-or-event-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, record kind, study and subject scope, protocol and profile versions, actor, event and knowledge times, privacy marking and provenance.",
        },
        "policies": ["The aggregate does not own Person, Animal, Organization, Specimen, Device, Study, Protocol, Consent Artifact, Eligibility Criterion, Intervention, Observation, Adverse Event, Payment, Identity Linkage, Ethics Decision, Provenance, Access Audit or Record masters.", "Recruitment, screening, eligibility, consent, enrolment, allocation, participation, exposure, adherence, safety, withdrawal and completion are independently sourced states or events.", "Pseudonymization and de-identification do not prove anonymity or eliminate re-identification risk.", "Agents cannot recruit, decide eligibility, obtain consent, enroll, allocate, intervene, unblind, re-identify, make safety decisions, compensate, disclose or delete outside explicit delegated authority."],
        "crud": {
            "read": ["Resolve purpose, current head, subject and study binding, identifiers, recruitment, screening, eligibility, permission, enrolment, allocation, activities, safety, state, withdrawal, privacy, retention, evidence and projection loss under the permitted view."],
            "create": ["Bind stable participation identity, external subject and study references, profile, owner, jurisdiction, source, authority, initial state and event time before adding participation context."],
            "update": ["Append successor decision, permission, state, activity, safety, withdrawal, correction and disclosure events with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply consent, research, privacy, legal-hold and adopting-Dimension retention policy; retire or tombstone only the participation assertion without cascading to subject, study or evidence masters, and let the external records policy execute physical disposition."],
        },
        "roles": [
            {"name": "Research participant or authorized representative", "responsibilities": ["Exercise applicable information, permission, refusal, withdrawal and rights processes without being treated as the data owner by default."]},
            {"name": "Principal investigator and site investigator", "responsibilities": ["Own qualified subject protection, clinical oversight, protocol conduct and source-qualified decisions within delegation."]},
            {"name": "Sponsor and research owner", "responsibilities": ["Own study purpose, quality system, oversight, risk management and accountable trial responsibilities."]},
            {"name": "IRB or independent ethics committee", "responsibilities": ["Provide independent ethical review and continuing oversight according to applicable rules."]},
            {"name": "Research coordinator and delegated staff", "responsibilities": ["Perform documented recruitment, screening, consent support, visits and data capture within delegated scope."]},
            {"name": "Safety and medical monitor", "responsibilities": ["Review safety evidence and perform authorized reporting and medical escalation without autonomous agent substitution."]},
            {"name": "Privacy, data and records steward", "responsibilities": ["Own protected views, linkage controls, data use, disclosures, corrections, holds, retention and auditability."]},
        ],
        "access": {
            "default_rule": "Deny participant identity, linkage, consent, eligibility, allocation, safety, health, payment and contact data unless a purpose-bound policy permits the minimum necessary view.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Declared care, safety, monitoring, audit, inspection, subject-rights, legal or emergency access must cite authority, scope, purpose and time limit where applicable and must be logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, participation, subject and study scope, operation, authority, policy, RFC 3339 time, affected fields, source revision and outcome without unnecessary identity duplication."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read Dimension research, ethics, consent, identity, safety, privacy, access, correction, retention and agent policies.", "Read this aggregate and linked subject, study, protocol, consent, intervention, observation, safety, payment, provenance and records models before mutation."],
        },
    }


def coverage():
    dims = ["identity", "classification and direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability", "authority and ethics"]
    return {
        "claim": "Covers one source-qualified research subject-to-study participation aggregate from candidate identification through screening, permission, enrolment, allocation, actual participation, safety, exit, protected data use, correction, retention and projection.",
        "confidence": "medium",
        "checklist": [{"dimension": d, "status": "covered", "notes": f"{d.capitalize()} is explicit; candidate containment, research-type and jurisdiction profiles, ethics and privacy review, release-pinned mappings and independent review remain held where applicable."} for d in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "The only relation-ledger edge is candidate incoming WM-ACT-036 CONTAINS WM-ACT-054; it is not approved composition or cascade authority.", "Human clinical, observational, behavioral, public-health, device, animal, specimen, product, group and other research require explicit profiles.", "The ISO 14155:2026 normative text and detailed CDISC files are access-restricted; only official public metadata was used for their bounded claims."],
        "conflicts": ["Participant, human subject, animal subject, specimen, product, device, household, cluster and organization are not interchangeable subject profiles.", "Recruitment, screening, eligibility, consent, enrolment, allocation and participation are distinct events or decisions.", "Assigned arm, actual exposure and adherence remain distinct; withdrawal from intervention, participation, future contact, future data use and specimen use are not equivalent."],
        "regional_assumptions": ["Research authorization, consent, representative authority, privacy, safety reporting, compensation, retention and subject rights depend on jurisdiction, research type, institution and protocol.", "45 CFR 46 and HIPAA are United States profiles; Regulation 536/2014 and GDPR are European Union profiles; ICH, WMA and ISO adoption still requires local validation.", "FHIR R5 ResearchSubject is Trial Use, and CDISC, WHO and ClinicalTrials.gov mappings require release-pinned profiles and scope limits."],
        "adversarial_checks": ["Reject participation without stable identity, external subject and study references, profile, owner, source, authority, state, event time and current head.", "Reject enrolment inferred from screening, eligibility or consent alone, and reject actual exposure inferred from assignment.", "Reject autonomous recruitment, eligibility, consent, allocation, unblinding, re-identification, safety, compensation, disclosure or deletion.", "Reject withdrawal handling that automatically deletes or retains all data and specimens without scoped consent, protocol, law, ethics and records policy.", "Reject anonymity claims based only on pseudonymization or de-identification labels without method, context, risk, authority and evidence."],
    }


def build():
    model = {
        "registry_id": "vr.wm-act-054", "model_id": "WM-ACT-054", "name": "Research Subject / Participant", "entry_kind": "aggregate",
        "purpose": "Represent one governed subject-to-study participation so agents can reconstruct who or what participated, under which profile, permission, assignment, activities, protections and outcome without absorbing external subject, study or evidence masters.",
        "scope_statement": "Owns one study-specific participation identity; subject and study bindings; subject profile and scoped identifiers; recruitment, screening, eligibility, consent, assent and representative-permission context; enrolment, allocation, blinding and planned path; actual activities, exposure, adherence, safety links, state, withdrawal, outcome, protected data use, corrections and projections. Person, animal, organization, specimen, device, study, protocol, consent artifact, criterion, intervention, observation, adverse event, payment, identity-linkage, ethics, provenance, audit and records masters remain external.",
        "in_scope": ["Participation identity, subject profile, protected identifiers, study and protocol bindings, recruitment, screening, eligibility, permission, enrolment and allocation", "Planned and actual participation, adherence, safety and compensation links, state, withdrawal, follow-up, data and specimen use, privacy, retention, correction and projections"],
        "out_of_scope": ["Creating or changing external subject, study, protocol, consent artifact, criterion, intervention, observation, adverse event, payment, identity linkage, ethics, provenance, audit or records masters", "Equating screening with eligibility, consent with enrolment, assignment with exposure, completion with benefit, or pseudonymization with anonymity", "Autonomous recruitment, eligibility, consent, enrolment, allocation, intervention, unblinding, re-identification, safety decision, compensation, disclosure or deletion"],
        "boundary_notes": [
            {"neighbor": "WM-ACT-036 Research Study", "distinction": "The candidate incoming CONTAINS relation may bind participation membership to a parent study. This aggregate cannot own, edit or cascade-delete study protocol, governance or results.", "source_refs": ["SRC-001", "SRC-002", "SRC-008", "SRC-009"]},
            {"neighbor": "Person, animal, organization, specimen, device and product subject models", "distinction": "External masters own the subject and its general lifecycle. This aggregate owns only the study-specific participation profile, identifiers and typed reference.", "source_refs": ["SRC-004", "SRC-005", "SRC-008"]},
            {"neighbor": "Consent, assent and representative-permission artifacts", "distinction": "External repositories own source artifacts and legal or ethical validity. Participation stores versioned bindings, process, scope, actors, verification, state and times.", "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-010"]},
            {"neighbor": "Intervention, observation, adverse event, medical-care and payment models", "distinction": "External masters own clinical, behavioral, safety, care and financial records. Participation stores typed planned or actual links and bounded interpretations.", "source_refs": ["SRC-001", "SRC-006", "SRC-008", "SRC-011", "SRC-012", "SRC-013"]},
            {"neighbor": "Identity linkage, privacy and records systems", "distinction": "Protected systems own direct identifiers, linkage keys, re-identification controls and physical disposition. Participation stores purpose-bound pseudonymous references, access markings, holds and auditable decisions.", "source_refs": ["SRC-004", "SRC-014", "SRC-016"]},
            {"neighbor": "FHIR, CDISC, WHO and ClinicalTrials.gov", "distinction": "These are versioned healthcare, clinical-data and public study-level projections with different scopes and maturity. No mapping is universally applicable or assumed lossless.", "source_refs": ["SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-018"]},
        ],
    }
    composition = [
        {"target": "WM-ACT-036 Research Study", "relation": "REFERENCE", "purpose": "Bind candidate parent study membership without owning study governance, protocol or results.", "required": True, "source_refs": ["SRC-001", "SRC-002", "SRC-008", "SRC-009"]},
        {"target": "Person, animal, organization, specimen, device or product subject model", "relation": "REFERENCE", "purpose": "Resolve who or what participates while preserving the external subject lifecycle.", "required": True, "source_refs": ["SRC-004", "SRC-005", "SRC-008"]},
        {"target": "Protocol, ethics, consent, criterion, intervention, observation, adverse-event, care, payment, identity-linkage, provenance, audit and records models", "relation": "REFERENCE", "purpose": "Resolve authoritative research and evidence records without absorbing their ownership or lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-006", "SRC-010", "SRC-015", "SRC-016"]},
        {"target": "FHIR R5, CDISC ODM 2.0, CDASHIG 2.2, WHO TRDS 1.3.1 and ClinicalTrials.gov", "relation": "ALIGN", "purpose": "Project version-pinned clinical and registry views with maturity, scope and information-loss declarations.", "required": False, "source_refs": ["SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-018"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    RUN.joinpath("codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
