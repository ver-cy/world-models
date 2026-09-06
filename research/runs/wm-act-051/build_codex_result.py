#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-ACT-051."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T10:20:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier, "accessed_at": AT,
        "relevance": relevance,
    }


SOURCES = [
    src(1, "Compliance management systems - Requirements with guidance for use", "International Organization for Standardization", "https://www.iso.org/standard/75080.html", "ISO 37301:2021", "standard", "Defines requirements and guidance for establishing, developing, implementing, evaluating, maintaining and improving a compliance management system; full normative text is access-restricted."),
    src(2, "Risk management - Guidelines", "International Organization for Standardization", "https://www.iso.org/standard/65694.html", "ISO 31000:2018", "standard", "Provides principles and a process for identifying, analyzing, evaluating, treating, monitoring and communicating risk; full normative text is access-restricted."),
    src(3, "Guidelines for auditing management systems", "International Organization for Standardization", "https://www.iso.org/standard/70017.html", "ISO 19011:2018", "standard", "Provides guidance on audit-program management and management-system audits; audit execution remains a sibling process and full text is access-restricted."),
    src(4, "Security and Privacy Controls for Information Systems and Organizations", "National Institute of Standards and Technology", "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final", "NIST SP 800-53 Rev. 5 Release 5.2.0, 27 August 2025", "standard", "Provides a customizable control catalog linked to mission, law, regulation, policy and risk; it is a security and privacy profile rather than a universal control set."),
    src(5, "Assessing Security and Privacy Controls in Information Systems and Organizations", "National Institute of Standards and Technology", "https://csrc.nist.gov/pubs/sp/800/53/a/r5/final", "NIST SP 800-53A Rev. 5 Release 5.2.0, 27 August 2025", "standard", "Defines customizable assessment procedures, assessment plans and analysis of control-assessment results within a risk-management framework."),
    src(6, "Open Security Controls Assessment Language", "National Institute of Standards and Technology", "https://pages.nist.gov/OSCAL/", "OSCAL 1.2.3, released 7 August 2026", "schema", "Provides machine-readable catalogs, profiles, system plans, assessment plans, results and plans of action and milestones in XML, JSON and YAML."),
    src(7, "Evaluation of Corporate Compliance Programs", "United States Department of Justice", "https://www.justice.gov/criminal-fraud/page/file/937501/dl?inline", "Updated September 2024", "public-authority", "Provides a prosecutorial evaluation profile covering design, resourcing and effectiveness, including risk assessment, policies, training, reporting, investigation, third parties, incentives, discipline and improvement."),
    src(8, "Annotated 2025 Chapter 8, section 8B2.1 Effective Compliance and Ethics Program", "United States Sentencing Commission", "https://www.ussc.gov/guidelines/2025-guidelines-manual/annotated-2025-chapter-8", "2025 Guidelines Manual, effective 1 November 2025", "legislation", "Provides a United States organizational compliance profile covering standards, oversight, due diligence, communication, monitoring, reporting, incentives, discipline, response and periodic risk assessment."),
    src(9, "Recommendation of the Council on Public Integrity", "Organisation for Economic Co-operation and Development", "https://legalinstruments.oecd.org/public/doc/353/353.en.pdf", "OECD/LEGAL/0435, adopted 26 January 2017", "public-authority", "Supports integrity systems, risk management, standards, leadership, accountability, participation, enforcement and monitoring in the public sector."),
    src(10, "An Anti-Corruption Ethics and Compliance Programme for Business: A Practical Guide", "United Nations Office on Drugs and Crime", "https://www.unodc.org/documents/corruption/Publications/2013/13-84498_Ebook.pdf", "United Nations, 2013", "public-authority", "Provides a practical anti-corruption compliance profile for risk assessment, support, controls, reporting, training, review and remediation."),
    src(11, "Business Process Model and Notation", "Object Management Group", "https://www.omg.org/spec/BPMN/2.0.2/About-BPMN", "BPMN 2.0.2, formal specification, January 2014", "standard", "Provides process, participant, activity, event, gateway, message and exception notation for projections, not compliance semantics."),
    src(12, "Structured Assurance Case Metamodel", "Object Management Group", "https://www.omg.org/spec/SACM/2.3/About-SACM", "SACM 2.3, formal specification", "standard", "Structures claims, argumentation and evidence used to communicate a defensible assurance case among operators, suppliers, acquirers and regulators."),
    src(13, "Static Analysis Results Interchange Format", "OASIS Open", "https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html", "SARIF 2.1.0, OASIS Standard, 27 March 2020", "schema", "Defines portable tool-result, rule, location, severity, baseline and suppression records; use is limited to applicable automated-analysis findings."),
    src(14, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Models permissions, prohibitions, duties, constraints, parties and assets for policy-expression projections, not legal applicability decisions."),
    src(15, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Provides entity, activity, agent, attribution, delegation, derivation, revision, generation and invalidation semantics for compliance evidence and decisions."),
    src(16, "Regulation (EU) 2016/679 General Data Protection Regulation", "European Union", "https://eur-lex.europa.eu/eli/reg/2016/679/oj", "27 April 2016, applicable from 25 May 2018", "legislation", "Provides a jurisdictional accountability example including principles, responsibility, records, security, data-subject rights and evidence of compliance."),
    src(17, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339, July 2002", "standard", "Provides interoperable timestamps with seconds and explicit UTC relationship for source, evidence, finding, remediation and decision times."),
]


ROWS = [
    ("programme-identity-scope-authority-and-regulatory-context", "Programme identity, scope, authority and regulatory context", "Compliance claims are meaningful only for a versioned subject, scope, jurisdiction, source set, owner and evaluation period", [
        ("programme-profile-identifiers-subject-scope-and-governance", "Programme profile, identifiers, subject, scope and governance", ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-015"], [
            ("compliance-programme-profile-root-identity-subject-and-boundary", "Compliance programme profile, root identity, subject and boundary", "identity", True),
            ("owner-governing-body-steward-responsible-functions-resources-and-independence", "Owner, governing body, steward, responsible functions, resources and independence", "ownership", True),
        ]),
        ("regulatory-sources-jurisdiction-effective-period-and-change", "Regulatory sources, jurisdiction, effective period and change", ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-014", "SRC-016", "SRC-017"], [
            ("authority-source-instrument-provision-version-jurisdiction-and-language", "Authority, source instrument, provision, version, jurisdiction and language", "provenance", True),
            ("publication-effective-transition-repeal-supersession-change-impact-and-watch", "Publication, effective, transition, repeal, supersession, change impact and watch", "temporal", False),
        ]),
    ]),
    ("obligations-applicability-risk-and-control-mapping", "Obligations, applicability, risk and control mapping", "The aggregate records attributable interpretations and mappings while authoritative obligations, risks and control definitions remain external masters", [
        ("requirements-obligations-applicability-and-interpretation", "Requirements, obligations, applicability and interpretation", ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-014", "SRC-016"], [
            ("requirement-obligation-prohibition-duty-right-and-authoritative-text-reference", "Requirement, obligation, prohibition, duty, right and authoritative-text reference", "requirement", True),
            ("applicability-subject-activity-threshold-exemption-interpretation-and-rationale", "Applicability, subject, activity, threshold, exemption, interpretation and rationale", "decision", True),
        ]),
        ("risk-controls-objectives-ownership-and-traceability", "Risk, controls, objectives, ownership and traceability", ["SRC-001", "SRC-002", "SRC-004", "SRC-007", "SRC-008", "SRC-009", "SRC-010"], [
            ("compliance-risk-cause-event-consequence-likelihood-impact-and-tolerance-reference", "Compliance risk, cause, event, consequence, likelihood, impact and tolerance reference", "relationship", False),
            ("control-objective-definition-owner-type-frequency-mapping-and-coverage", "Control objective, definition, owner, type, frequency, mapping and coverage", "composition", True),
        ]),
    ]),
    ("implementation-evidence-monitoring-and-control-assurance", "Implementation, evidence, monitoring and control assurance", "Design and operating assertions require source-qualified implementation and evidence records rather than unsupported declarations", [
        ("control-implementation-design-operation-and-responsibility", "Control implementation, design, operation and responsibility", ["SRC-001", "SRC-004", "SRC-006", "SRC-007", "SRC-008", "SRC-010"], [
            ("implementation-description-component-owner-operator-scope-and-dependency", "Implementation description, component, owner, operator, scope and dependency", "definition", True),
            ("design-effectiveness-operating-effectiveness-frequency-execution-and-failure", "Design effectiveness, operating effectiveness, frequency, execution and failure", "validation", False),
        ]),
        ("evidence-collection-quality-freshness-and-continuous-monitoring", "Evidence collection, quality, freshness and continuous monitoring", ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-012", "SRC-013", "SRC-015", "SRC-017"], [
            ("evidence-identity-source-method-coverage-period-integrity-access-and-lineage", "Evidence identity, source, method, coverage period, integrity, access and lineage", "evidence", True),
            ("monitoring-signal-metric-threshold-sample-frequency-alert-anomaly-and-gap", "Monitoring signal, metric, threshold, sample, frequency, alert, anomaly and gap", "measurement", False),
        ]),
    ]),
    ("assessment-findings-nonconformities-exceptions-and-waivers", "Assessment, findings, nonconformities, exceptions and waivers", "Assessment results, findings and exceptions remain attributable, contestable and independently versioned", [
        ("assessment-audit-test-scope-method-results-and-review", "Assessment, audit, test, scope, method, results and review", ["SRC-003", "SRC-005", "SRC-006", "SRC-007", "SRC-012", "SRC-013", "SRC-015"], [
            ("assessment-engagement-plan-criteria-procedure-sample-assessor-and-independence", "Assessment engagement, plan, criteria, procedure, sample, assessor and independence", "process", False),
            ("test-result-observation-conclusion-confidence-limit-and-contradiction", "Test result, observation, conclusion, confidence, limit and contradiction", "quality", True),
        ]),
        ("finding-disposition-root-cause-exception-and-waiver", "Finding disposition, root cause, exception and waiver", ["SRC-001", "SRC-005", "SRC-007", "SRC-008", "SRC-010", "SRC-012", "SRC-013"], [
            ("finding-nonconformity-severity-affected-scope-source-status-and-dispute", "Finding, nonconformity, severity, affected scope, source, status and dispute", "state", True),
            ("exception-waiver-authority-rationale-scope-compensating-control-expiry-and-review", "Exception, waiver, authority, rationale, scope, compensating control, expiry and review", "exception", True),
        ]),
    ]),
    ("remediation-verification-attestation-reporting-and-regulator-interface", "Remediation, verification, attestation, reporting and regulator interface", "Corrective action, verification, declaration, submission and external acceptance are separate stages with separate authorities", [
        ("remediation-planning-execution-verification-and-closure", "Remediation planning, execution, verification and closure", ["SRC-001", "SRC-005", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-015"], [
            ("remediation-action-owner-priority-due-date-resource-dependency-and-progress", "Remediation action, owner, priority, due date, resource, dependency and progress", "lifecycle", True),
            ("acceptance-criteria-independent-verification-residual-risk-reopen-and-closure", "Acceptance criteria, independent verification, residual risk, reopen and closure", "validation", True),
        ]),
        ("attestation-disclosure-reporting-submission-and-response", "Attestation, disclosure, reporting, submission and response", ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-012", "SRC-015", "SRC-016"], [
            ("compliance-status-claim-scope-basis-qualifier-signer-authority-and-assurance", "Compliance-status claim, scope, basis, qualifier, signer, authority and assurance", "authority", True),
            ("report-notification-submission-recipient-deadline-receipt-acceptance-and-followup", "Report, notification, submission, recipient, deadline, receipt, acceptance and follow-up", "event", False),
        ]),
    ]),
    ("lifecycle-governance-correction-retention-and-interoperability", "Lifecycle, governance, correction, retention and interoperability", "Safe agent operation requires append-only decisions, current-head resolution, protected evidence and mappings that declare scope and loss", [
        ("programme-cycle-status-review-change-correction-and-supersession", "Programme cycle status, review, change, correction and supersession", ["SRC-001", "SRC-002", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-015", "SRC-017"], [
            ("cycle-status-review-period-trigger-material-change-and-continuous-improvement", "Cycle status, review period, trigger, material change and continuous improvement", "lifecycle", True),
            ("correct-amend-withdraw-supersede-reopen-appeal-and-noncascade-lineage", "Correct, amend, withdraw, supersede, reopen, appeal and non-cascade lineage", "provenance", True),
        ]),
        ("access-retention-assurance-projection-and-agent-controls", "Access, retention, assurance, projection and agent controls", ["SRC-004", "SRC-005", "SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017"], [
            ("purpose-access-redaction-privilege-confidentiality-legal-hold-retention-and-disposition", "Purpose, access, redaction, privilege, confidentiality, legal hold, retention and disposition", "privacy", True),
            ("oscal-bpmn-sacm-sarif-odrl-prov-projection-version-scope-loss-and-round-trip", "OSCAL, BPMN, SACM, SARIF, ODRL and PROV projection, version, scope, loss and round trip", "interoperability", False),
        ]),
    ]),
]


KINDS = ["identity", "classification", "relationship", "authority", "requirement", "constraint", "event", "temporal", "composition", "evidence", "ownership", "measurement", "exception", "provenance", "process", "validation", "privacy", "lifecycle", "quality", "security", "retention", "interoperability", "decision", "state"]


def finding(item, number, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(number + 7) % len(KINDS)], KINDS[(number + 15) % len(KINDS)]]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {low} as source-qualified compliance context while keeping authoritative rules, controls, assessments, evidence, work and external decisions in their owning systems.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which stable identities, class, scope, source-qualified assertions and explicit unknowns establish {low}?", "kind": kinds[0], "answer_data": ["identifiers, class and scope", "source-qualified assertions", "unknown and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who owns, interprets, performs, reviews, approves, disputes or is affected by {low}, with which authority, independence and limits?", "kind": kinds[1], "answer_data": ["actors, roles and separation of duties", "authority, independence and limits", "review, dispute and exception path"]},
            {"id": f"{fid}-q03", "text": f"Which source-effective, evidence-coverage, assessment, finding, remediation, verification, decision, recorded, ingested and knowledge times apply to {low}, and how is it corrected?", "kind": kinds[2], "answer_data": ["distinct regulatory and record times", "evidence, validation and uncertainty", "successor correction and retention"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed data for {low} with identity, scope, source, authority, status, event and knowledge times, evidence and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned compliance evidence for {low}.", "media_or_form": ["logical compliance assertion", "scope, mapping, implementation, evidence, assessment, finding, exception, remediation, attestation or projection record"], "serial": True, "identity_strategy": f"Programme ID plus independent source, obligation, control-mapping, evidence, finding, exception, remediation, attestation or assertion ID for {fid}; organization, rule title, date and status never identify a record alone.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles = []
    number = 0
    for bid, bname, rationale, layers in ROWS:
        rendered_layers = []
        for lid, lname, refs, items in layers:
            findings = []
            for item in items:
                number += 1
                findings.append(finding(item, number, refs))
            rendered_layers.append({"id": lid, "name": lname, "description": f"Groups source-qualified compliance context for {lname.lower()}.", "source_refs": refs, "findings": findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed compliance context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({ref for layer in layers for ref in layer[2]}), "layers": rendered_layers})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-compliance-cycle", "Register compliance cycle", ["subject", "scope", "authority sources", "owner mandate"], ["programme root and constituent slots"], ["stable identity, subject, jurisdiction, scope, period and authority pass"], ["one bounded compliance cycle is registered without asserting compliance"], ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010"]),
    ("register-regulatory-source-change", "Register regulatory source change", ["authoritative source", "version", "effective dates", "change notice"], ["source revision and impact-review trigger"], ["authenticity, jurisdiction, language, dates and predecessor pass"], ["the programme can reassess applicability without copying or rewriting the law"], ["SRC-001", "SRC-007", "SRC-008", "SRC-014", "SRC-016"]),
    ("assess-applicability", "Assess applicability", ["source provisions", "subject facts", "thresholds", "interpreter authority"], ["versioned applicability decision"], ["facts, jurisdiction, scope, rationale, uncertainty and reviewer pass"], ["an attributable interpretation is recorded without becoming legal authority"], ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-016"]),
    ("map-obligations-risks-and-controls", "Map obligations, risks and controls", ["applicable obligations", "risk references", "control definitions"], ["traceability and coverage map"], ["external identities, versions, mapping rationale, owner and gaps pass"], ["coverage assertions are visible without absorbing obligation, risk or control masters"], ["SRC-001", "SRC-002", "SRC-004", "SRC-006"]),
    ("record-implementation-and-monitoring-evidence", "Record implementation and monitoring evidence", ["control mapping", "implementation assertions", "evidence", "monitoring observations"], ["source-qualified implementation and evidence index"], ["coverage period, method, source, integrity, access, freshness and contradictions pass"], ["design and operation claims become inspectable but not automatically effective"], ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-012", "SRC-015"]),
    ("commission-or-link-assessment", "Commission or link assessment", ["scope", "criteria", "assessor", "procedures", "evidence references"], ["assessment binding and result intake"], ["independence, authority, criteria version, sample and limitations pass"], ["audit or assessment remains external while its result is incorporated by reference"], ["SRC-003", "SRC-005", "SRC-006", "SRC-012"]),
    ("record-finding-or-exception", "Record finding or exception", ["assessment result", "affected scope", "severity", "authority", "rationale"], ["finding, exception or waiver record"], ["source, status, dispute, compensating control, expiry and review pass"], ["the obligation and prior evidence remain intact and contestable"], ["SRC-005", "SRC-007", "SRC-008", "SRC-010", "SRC-013"]),
    ("plan-track-and-verify-remediation", "Plan, track and verify remediation", ["finding", "action references", "owner", "criteria", "due dates"], ["remediation status and independent verification"], ["authority, dependencies, evidence, residual risk and closure criteria pass"], ["action completion stays separate from accepted remediation closure"], ["SRC-001", "SRC-005", "SRC-007", "SRC-008", "SRC-010"]),
    ("attest-report-submit-and-record-response", "Attest, report, submit and record response", ["bounded status claim", "evidence basis", "signer", "recipient", "deadline"], ["attestation, report, receipt and response links"], ["scope, qualifier, authority, assurance level, disclosure and recipient profile pass"], ["submission, receipt, acceptance, certification and continuing compliance remain separate"], ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-012", "SRC-016"]),
    ("correct-project-retain-disclose-and-audit", "Correct, project, retain, disclose and audit", ["programme", "target profile", "access and retention policy"], ["successor, projection, disclosure, tombstone or disposition event"], ["mapping versions, loss, privacy, privilege, legal hold and idempotency pass"], ["context stays protected, reconstructable and explicit about current head and loss"], ["SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017"]),
]


def functions():
    return [{"id": row[0], "name": row[1], "description": f"Governed operation to {row[1].lower()} without hidden legal interpretation, enforcement or mutation of external masters.", "inputs": row[2], "outputs": row[3], "preconditions": row[4], "effects": row[5], "source_refs": row[6]} for row in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner and compliance-governance mandate", "Authoritative law, regulation, obligation, policy, risk, control, organization, asset, assessment, evidence, finding, incident, task, attestation, submission, provenance, audit and record registries", "Approved jurisdiction, sector, control, assessment, reporting, privacy, retention and interoperability profiles", "Legal-interpretation, independence, escalation, privilege, disclosure and agent-operation policies"],
            "namespace_guidance": "Mint programme, scope, applicability, mapping, implementation, evidence, monitoring, finding, exception, remediation, verification, attestation, submission, correction, disclosure and event IDs; preserve authoritative source and sibling-model identifiers.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize each programme and constituent by authoritative master-system identifier, owning organization and record kind; never by organization, regulation title, date or status alone.", "Keep authoritative source, obligation, applicability interpretation, control definition, implementation assertion, evidence, assessment, finding, exception, remediation, attestation, submission and external response distinct."],
            "patch_rules": ["Extensions declare jurisdiction, sector, subject, control, evidence, assessment, reporting, privacy, retention and interoperability effects.", "Released applicability, mapping, evidence, finding, exception, remediation, verification and attestation records are immutable; corrections create linked successors.", "Never silently change scope, source version, applicability, obligation, control, evidence period, result, finding, exception, action, status, authority, disclosure or provenance."],
            "compatibility_rules": ["Ignore additive fields only when identity, scope, authoritative source, constituent kind, authority, status, time, evidence and provenance survive.", "Every projection pins profile, source and classification versions and declares jurisdiction, sector, assurance level and information loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each compliance programme, applicability decision, mapping, evidence item, finding, exception, remediation, attestation or submission, qualified by owning organization and record kind.", "Governed globally resolvable compliance-record IRI.", "Dimension UUID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish source publication and effective, evidence coverage, assessment, finding, remediation, verification, attestation, submission, response, recorded, ingested and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {programme-id}--{scope-mapping-evidence-finding-remediation-attestation-or-assertion-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, record kind, scope, authoritative source and profile versions, actor, event and knowledge times, status, access marking and provenance."},
        "policies": ["The aggregate does not own Law, Regulation, Obligation, Policy, Risk, Control, Organization, Asset, Audit, Assessment, Evidence, Incident, Task, Attestation, Regulator Submission, Provenance, Access Audit or Record masters.", "Applicability, implementation, effectiveness, finding, exception, remediation, attestation, certification, submission and regulator response remain separate claims with independent sources and times.", "A closed remediation, submitted report or signed attestation never proves regulator acceptance, certification or continuing compliance.", "Agents cannot issue legal interpretations, certify compliance, approve exceptions, enforce controls, file regulator submissions, alter external statuses, disclose privileged evidence or dispose records outside explicit authority."],
        "crud": {
            "read": ["Resolve purpose, programme profile, subject and scope, source revisions, applicability, mappings, implementation, evidence, assessments, findings, exceptions, remediation, attestations, lineage, holds and projection loss."],
            "create": ["Bind stable programme and constituent identity, subject, jurisdiction, scope, owner, authoritative source, status and effective time before recording a compliance assertion."],
            "update": ["Append successor applicability, mapping, implementation, evidence, finding, exception, remediation, verification, attestation, submission, response and correction events with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply legal, regulatory, privilege, evidence, audit, litigation-hold and adopting-Dimension retention policy; retire or tombstone only the programme or named constituent without cascading to Law, Obligation, Risk, Control, Assessment, Evidence, Incident, Task, Submission or other masters, and let the external records policy execute physical disposition."],
        },
        "roles": [
            {"name": "Compliance programme owner", "responsibilities": ["Own programme purpose, scope, resources, governance and accountable status claims."]},
            {"name": "Legal or regulatory interpreter", "responsibilities": ["Own attributable applicability interpretation and uncertainty within professional authority."]},
            {"name": "Control owner and operator", "responsibilities": ["Own control mapping, implementation and operating evidence within scope."]},
            {"name": "Independent assessor or auditor", "responsibilities": ["Own assessment criteria, method, evidence use, result, limitations and independence declaration."]},
            {"name": "Finding and remediation owner", "responsibilities": ["Own response, action coordination, due dates, escalation and closure evidence."]},
            {"name": "Attestor or reporting officer", "responsibilities": ["Own bounded declarations, disclosures and submissions within signing authority."]},
            {"name": "Interoperability steward", "responsibilities": ["Own versioned projections with jurisdiction, profile, maturity and loss declarations."]},
            {"name": "Privacy, privilege, records and assurance steward", "responsibilities": ["Own protected views, privilege handling, disclosures, holds, retention and auditability."]},
        ],
        "access": {"default_rule": "Deny compliance evidence, findings, legal interpretations and privileged context unless a purpose-bound policy permits the minimum necessary view.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Declared legal, regulator, auditor, subject-rights, investigation, court or emergency access must cite authority, scope, purpose, privilege treatment and time limit where applicable and must be logged."], "audit_requirements": ["Log actor, agent, role, purpose, programme and constituent, operation, authority, policy, RFC 3339 time, affected fields, source revision and outcome without duplicating protected evidence unnecessarily."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"], "read_order": ["Read Dimension legal-authority, compliance, evidence, assessment, independence, privilege, privacy, access, correction, records and agent policies.", "Read this aggregate and linked regulation, obligation, policy, risk, control, organization, asset, audit, assessment, evidence, incident, task, attestation, submission, provenance and record models before mutation."]},
    }


def coverage():
    dims = ["identity", "classification and definition", "direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability"]
    return {
        "claim": "Covers a source-qualified regulatory-compliance-cycle aggregate linking bounded scope, authoritative sources, applicability, obligation-control mapping, implementation evidence, monitoring, assessment intake, findings, exceptions, remediation, verification, attestation, reporting, correction, protected use and projection.",
        "confidence": "medium",
        "checklist": [{"dimension": dim, "status": "covered", "notes": f"{dim.capitalize()} is explicit; jurisdiction, sector, missing relations, access-restricted ISO clauses and release-pinned validation remain held where applicable."} for dim in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "No relation-ledger edge is registered for WM-ACT-051, so links to obligation, risk/control, audit, assessment, assurance, incident, task, attestation and record models remain candidate boundary notes.", "Financial services, healthcare, product safety, environment, labor, tax, privacy, anti-corruption, competition, export control, AI and other regimes require jurisdiction and sector profiles.", "ISO normative clauses are access-restricted; NIST, DOJ, USSC, OECD, UNODC, GDPR, OSCAL and SARIF each have sectoral, jurisdictional or technical scope and require release-pinned validation."],
        "conflicts": ["Authoritative requirement and attributable applicability interpretation are not interchangeable.", "Control design, implementation, operation, assessment result and operating effectiveness are separate assertions.", "Remediation action completion, finding closure, attestation, submission, certification, regulator acceptance and continuing compliance are not equivalent."],
        "regional_assumptions": ["Legal effect, applicability, professional privilege, regulator authority, reporting, certification, retention and disclosure depend on jurisdiction, sector and facts.", "DOJ and USSC are United States profiles, GDPR is European Union law and OECD or UNODC guidance is not itself binding law.", "Local control libraries, regulatory taxonomies, severity scales, assurance levels, evidence rules and exception authorities require versioned profiles."],
        "adversarial_checks": ["Reject a programme or constituent without stable identity, scope, authoritative source, responsible authority, status, effective time and lineage head.", "Reject a compliance status that lacks evaluation scope, time, evidence basis, qualifiers, uncertainty and accountable signer.", "Reject applicability or control mapping that copies altered legal text, hides interpretation, loses source version or treats guidance as binding law.", "Reject finding closure that relies only on action completion and lacks independent verification against acceptance criteria and residual risk.", "Reject autonomous legal interpretation, certification, exception approval, regulator filing, control enforcement, privileged disclosure or disposition outside explicit authority."],
    }


def build():
    model = {
        "registry_id": "vr.wm-act-051", "model_id": "WM-ACT-051",
        "name": "Regulatory Compliance Process", "entry_kind": "aggregate",
        "purpose": "Represent a governed compliance cycle so agents can connect authoritative sources, bounded applicability, obligations, controls, evidence, findings and remediation without treating a process status, attestation or submission as timeless proof of compliance.",
        "scope_statement": "Owns one compliance-cycle identity and bounded subject, jurisdiction, scope and period; source-revision watch; attributable applicability decisions; obligation-risk-control mappings; implementation, evidence and monitoring context; assessment result intake; finding, exception, remediation, verification, attestation and reporting links; and correction lineage. Law, regulation, obligation, policy, risk, control, organization, asset, audit, assessment, evidence, incident, task, attestation, regulator submission, provenance, access audit and record masters remain external.",
        "in_scope": ["Programme identity, subject and scope, source versions and changes, applicability interpretations, obligation-risk-control traceability, implementation and monitoring assertions", "Assessment result intake, findings and exceptions, remediation and verification coordination, bounded status claims, attestations, reporting, correction, privacy, retention and loss-aware projections"],
        "out_of_scope": ["Creating or changing law, authoritative obligations, generic policies, risks, control definitions, organizations, assets, audit engagements, assessments, evidence items, incidents, work tasks, regulator submissions or records", "Treating compliance as a universal binary fact or equating action completion, finding closure, attestation, submission, certification, acceptance and continuing compliance", "Providing legal advice, certification, enforcement, exception approval, regulator filing or destructive evidence handling"],
        "boundary_notes": [
            {"neighbor": "Law, regulation and WM-XCT-029 Obligation / Commitment", "distinction": "Authoritative sources and obligations remain external. The aggregate stores versioned references and attributable applicability and mapping decisions without rewriting authoritative text.", "source_refs": ["SRC-001", "SRC-007", "SRC-008", "SRC-014", "SRC-016"]},
            {"neighbor": "WM-KNW-015 Risk / Opportunity and WM-XCT-027 Risk / Control", "distinction": "Risk and control masters own their definitions and lifecycles. The aggregate owns compliance-specific mappings, implementation assertions, coverage and gaps.", "source_refs": ["SRC-002", "SRC-004", "SRC-006"]},
            {"neighbor": "WM-ACT-033 Review / Inspection / Audit, WM-ACT-034 Assessment / Evaluation and WM-ECO-035 Audit / Assurance Engagement", "distinction": "Specialist models own engagement, method, evidence gathering, testing, results and assurance. This aggregate records commissioning, result intake, response and closure context.", "source_refs": ["SRC-003", "SRC-005", "SRC-012"]},
            {"neighbor": "Evidence, incident, task and work-order models", "distinction": "External masters own evidence content, incidents and remediation work. The aggregate keeps integrity-qualified references, compliance disposition, acceptance criteria and verification status.", "source_refs": ["SRC-005", "SRC-006", "SRC-007", "SRC-013", "SRC-015"]},
            {"neighbor": "Attestation, certification, submission and regulator response", "distinction": "A status claim, signed declaration, independent certification, filing receipt and regulator decision each retain independent authority and state. None proves continuing compliance by itself.", "source_refs": ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-012", "SRC-016"]},
            {"neighbor": "BPMN, OSCAL, SACM, SARIF, ODRL and PROV", "distinction": "These are versioned process, control-assessment, assurance, tool-result, policy and provenance projections with different scopes. No mapping is assumed lossless or universally applicable.", "source_refs": ["SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015"]},
        ],
    }
    composition = [
        {"target": "WM-XCT-029 Obligation / Commitment, law, regulation and policy models", "relation": "REFERENCE", "purpose": "Resolve authoritative requirements and obligations while keeping applicability interpretation attributable and local to the cycle.", "required": True, "source_refs": ["SRC-001", "SRC-007", "SRC-008", "SRC-014", "SRC-016"]},
        {"target": "WM-KNW-015 Risk / Opportunity and WM-XCT-027 Risk / Control", "relation": "REFERENCE", "purpose": "Bind versioned risk and control masters to compliance-specific coverage, implementation and gap assertions.", "required": True, "source_refs": ["SRC-002", "SRC-004", "SRC-006"]},
        {"target": "WM-ACT-033 Review / Inspection / Audit, WM-ACT-034 Assessment / Evaluation and WM-ECO-035 Audit / Assurance Engagement", "relation": "REFERENCE", "purpose": "Bind assessment and assurance work without owning its execution, independence or evidence-gathering lifecycle.", "required": False, "source_refs": ["SRC-003", "SRC-005", "SRC-012"]},
        {"target": "Evidence, incident, task, work-order, attestation, regulator-submission, provenance, access-audit and record models", "relation": "REFERENCE", "purpose": "Resolve evidence, remediation execution, declarations, external interactions and records without copying their lifecycles.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-007", "SRC-012", "SRC-013", "SRC-015", "SRC-016"]},
        {"target": "OSCAL 1.2.3, BPMN 2.0.2, SACM 2.3, SARIF 2.1.0, ODRL 2.2 and PROV-O", "relation": "ALIGN", "purpose": "Project version-pinned control, process, assurance, tool-result, policy and provenance views with scope and information-loss declarations.", "required": False, "source_refs": ["SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    RUN.joinpath("codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
