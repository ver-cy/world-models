#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-ACT-052."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T11:00:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier, "accessed_at": AT,
        "relevance": relevance,
    }


SOURCES = [
    src(1, "Tax Administration 2025", "Organisation for Economic Co-operation and Development", "https://www.oecd.org/en/publications/tax-administration-2025_cc015ce8-en.html", "Published 17 November 2025; DOI 10.1787/cc015ce8-en", "public-authority", "Comparative tax-administration context for electronic filing, taxpayer services, collection, disputes and digital transformation across 58 jurisdictions."),
    src(2, "Tax Administration 3.0: The Digital Transformation of Tax Administration", "Organisation for Economic Co-operation and Development", "https://www.oecd.org/en/publications/tax-administration-3-0_ca274cc5-en.html", "Published 8 December 2020; DOI 10.1787/ca274cc5-en", "public-authority", "Frames tax administration embedded in natural systems, event-driven data exchange, identity, assurance and trustworthy digital processes."),
    src(3, "OECD International Compliance Assurance Programme", "Organisation for Economic Co-operation and Development", "https://www.oecd.org/en/about/programmes/icap.html", "ICAP Handbook 2021; programme page current at access", "public-authority", "Provides a bounded cooperative-assurance profile with selection, risk assessment, documentation, outcomes and follow-up; it is not a universal filing or assessment process."),
    src(4, "International VAT/GST Guidelines", "Organisation for Economic Co-operation and Development", "https://www.oecd.org/en/publications/international-vat-gst-guidelines_9789264271401-en.html", "12 April 2017; DOI 10.1787/9789264271401-en", "public-authority", "Provides internationally agreed VAT/GST principles for cross-border trade while leaving domestic legal implementation jurisdiction-specific."),
    src(5, "Modernized e-File schemas and business rules", "United States Internal Revenue Service", "https://www.irs.gov/e-file-providers/modernized-e-file-mef-schemas-and-business-rules", "Current filing-season resources at access", "schema", "Publishes tax-year and processing-year schemas and business rules, supporting explicit version binding and separation of schema validation from business-rule validation."),
    src(6, "Modernized e-File Guide for Software Developers and Transmitters", "United States Internal Revenue Service", "https://www.irs.gov/pub/irs-pdf/p4164.pdf", "Publication 4164, Processing Year 2026, Rev. 12-2025", "public-authority", "Defines MeF transmission, submission, acknowledgement, reject and acceptance concepts for a United States e-file implementation profile."),
    src(7, "Authorized IRS e-file Providers of Individual Income Tax Returns", "United States Internal Revenue Service", "https://www.irs.gov/pub/irs-pdf/p1345.pdf", "Publication 1345, Rev. 12-2025", "public-authority", "Covers taxpayer information handling, identity verification, signatures, transmission, electronic postmarks, acknowledgements, resubmission, record keeping, payments and refunds for a United States individual-return profile."),
    src(8, "VAT (MTD) API", "HM Revenue and Customs", "https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0", "Version 1.0 beta; last updated 5 August 2026", "first-party-doc", "Exposes obligation retrieval, VAT return submission and retrieval, and liability, payment and penalty retrieval for a United Kingdom implementation profile."),
    src(9, "VAT Notice 700/22: Making Tax Digital for VAT", "HM Revenue and Customs", "https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat", "Updated 1 April 2022", "public-authority", "Defines a United Kingdom profile for digital records, compatible software, digital links, declaration, submission and receipt confirmation."),
    src(10, "Council Directive 2006/112/EC on the common system of value added tax", "European Union", "https://eur-lex.europa.eu/eli/dir/2006/112/oj", "28 November 2006; consolidated implementation must be checked by jurisdiction", "legislation", "Provides an European Union legal VAT frame; transposition, amendments, national procedure and effective text must be resolved separately."),
    src(11, "XBRL 2.1", "XBRL International", "https://specifications.xbrl.org/work-product-index-group-base-spec-base-spec.html", "Recommendation 20 February 2013; conformance suite 16 July 2025", "standard", "Defines instance, taxonomy, concept, context, unit and fact structures for version-pinned reporting projections."),
    src(12, "Universal Business Language 2.4", "OASIS Open", "https://docs.oasis-open.org/ubl/os-UBL-2.4/UBL-2.4.html", "OASIS Standard, 20 June 2024", "standard", "Defines document models, schemas and validation artifacts relevant to source commercial documents and taxation projections."),
    src(13, "XML Signature Syntax and Processing Version 1.1", "World Wide Web Consortium", "https://www.w3.org/TR/xmldsig-core1/", "W3C Recommendation, 11 April 2013", "standard", "Provides XML signature, reference, transform, digest and validation semantics where an adopted filing profile uses XML signatures."),
    src(14, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Provides entity, activity, agent, attribution, delegation, derivation, revision, generation and invalidation semantics for return and assessment lineage."),
    src(15, "Regulation (EU) 2016/679 General Data Protection Regulation", "European Union", "https://eur-lex.europa.eu/eli/reg/2016/679/oj", "27 April 2016; applicable from 25 May 2018", "legislation", "Provides a European Union privacy and accountability profile for personal tax data, access, minimization, security and rights."),
    src(16, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339, July 2002", "standard", "Provides interoperable timestamps with seconds and explicit UTC relationship for filing, acknowledgement, assessment, payment and knowledge times."),
    src(17, "Forms and publications about your appeal rights", "United States Internal Revenue Service", "https://www.irs.gov/appeals/forms-and-publications-about-your-appeal-rights", "Current at access; linked Publication 5 Rev. 4-2021", "public-authority", "Provides a United States profile for examination disputes, administrative appeals, refund claims and collection appeals without generalizing its deadlines or procedures."),
]


ROWS = [
    ("case-identity-tax-scope-parties-and-authority", "Case identity, tax scope, parties and authority", "A filing and assessment case requires stable identity and a versioned legal and administrative scope without absorbing taxpayer, account, obligation or law masters", [
        ("case-profile-taxpayer-representation-and-authority", "Case profile, taxpayer, representation and authority", ["SRC-001", "SRC-002", "SRC-006", "SRC-007", "SRC-008", "SRC-014"], [
            ("filing-assessment-case-root-identity-owner-status-and-lineage", "Filing and assessment case root identity, owner, status and lineage", "identity", True),
            ("taxpayer-registration-account-representative-role-and-authority-references", "Taxpayer, registration, account, representative, role and authority references", "authority", True),
        ]),
        ("tax-type-jurisdiction-period-obligation-form-and-version", "Tax type, jurisdiction, period, obligation, form and version", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-010"], [
            ("tax-type-jurisdiction-administration-office-and-obligation-reference", "Tax type, jurisdiction, administration, office and obligation reference", "classification", True),
            ("tax-period-due-date-form-schedule-schema-business-rule-and-law-version", "Tax period, due date, form, schedule, schema, business rule and law version", "temporal", True),
        ]),
    ]),
    ("source-data-declaration-calculation-and-return-composition", "Source data, declaration, calculation and return composition", "Return values must retain traceability to source records, versioned calculation rules and a bounded declaration", [
        ("books-transactions-source-documents-ledgers-and-data-cut", "Books, transactions, source documents, ledgers and data cut", ["SRC-004", "SRC-007", "SRC-009", "SRC-012", "SRC-014"], [
            ("source-record-ledger-transaction-document-and-master-system-lineage", "Source record, ledger, transaction, document and master-system lineage", "provenance", True),
            ("source-period-extract-data-cut-reconciliation-adjustment-and-evidence-quality", "Source period, extract, data cut, reconciliation, adjustment and evidence quality", "quality", True),
        ]),
        ("taxable-events-bases-rates-reliefs-currency-and-computation", "Taxable events, bases, rates, reliefs, currency and computation", ["SRC-004", "SRC-005", "SRC-009", "SRC-010", "SRC-011", "SRC-012"], [
            ("taxable-event-category-place-time-base-rate-relief-credit-and-exemption", "Taxable event, category, place, time, base, rate, relief, credit and exemption", "requirement", True),
            ("calculation-expression-input-output-currency-rounding-total-and-reconciliation", "Calculation expression, input, output, currency, rounding, total and reconciliation", "measurement", True),
        ]),
    ]),
    ("validation-signature-submission-and-acknowledgement", "Validation, signature, submission and acknowledgement", "Technical validation, declaration, transmission, receipt and legal acceptance are independent outcomes with separate evidence", [
        ("structural-business-cross-field-and-eligibility-validation", "Structural, business, cross-field and eligibility validation", ["SRC-005", "SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-012"], [
            ("schema-code-list-datatype-cardinality-and-signature-validation", "Schema, code list, datatype, cardinality and signature validation", "validation", True),
            ("business-rule-cross-field-eligibility-consistency-warning-error-and-correction", "Business rule, cross-field, eligibility, consistency, warning, error and correction", "constraint", True),
        ]),
        ("declaration-signature-transmission-receipt-and-acceptance", "Declaration, signature, transmission, receipt and acceptance", ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-013", "SRC-016"], [
            ("declaration-signer-capacity-consent-signature-method-and-evidence", "Declaration, signer, capacity, consent, signature method and evidence", "authority", True),
            ("submission-channel-message-postmark-receipt-acknowledgement-acceptance-and-rejection", "Submission, channel, message, postmark, receipt, acknowledgement, acceptance and rejection", "event", True),
        ]),
    ]),
    ("assessment-adjustment-notice-and-liability", "Assessment, adjustment, notice and liability", "Taxpayer calculation and authority determination remain source-qualified and contestable, and a notice is not the same record as a liability or collection action", [
        ("self-assessment-authority-determination-examination-and-adjustment", "Self-assessment, authority determination, examination and adjustment", ["SRC-001", "SRC-003", "SRC-010", "SRC-014", "SRC-017"], [
            ("self-assessed-return-position-amount-basis-uncertainty-and-reservation", "Self-assessed return position, amount, basis, uncertainty and reservation", "decision", True),
            ("authority-assessment-adjustment-reason-provision-calculation-difference-and-review", "Authority assessment, adjustment, reason, provision, calculation, difference and review", "decision", True),
        ]),
        ("notice-effective-date-finality-rights-and-liability", "Notice, effective date, finality, rights and liability", ["SRC-001", "SRC-008", "SRC-010", "SRC-016", "SRC-017"], [
            ("assessment-notice-issuer-recipient-method-service-date-content-and-authenticity", "Assessment notice, issuer, recipient, method, service date, content and authenticity", "evidence", True),
            ("liability-component-principal-interest-penalty-currency-due-date-finality-and-balance", "Liability component, principal, interest, penalty, currency, due date, finality and balance", "state", True),
        ]),
    ]),
    ("settlement-refund-penalty-interest-and-dispute", "Settlement, refund, penalty, interest and dispute", "Money movement and adjudication remain external processes while the case records typed allocations, notices, rights and outcomes", [
        ("payment-allocation-refund-interest-and-penalty-links", "Payment, allocation, refund, interest and penalty links", ["SRC-001", "SRC-007", "SRC-008", "SRC-016", "SRC-017"], [
            ("payment-reference-allocation-amount-currency-value-date-status-and-reversal", "Payment reference, allocation, amount, currency, value date, status and reversal", "relationship", False),
            ("refund-credit-offset-interest-penalty-calculation-notice-and-status-reference", "Refund, credit, offset, interest, penalty calculation, notice and status reference", "relationship", False),
        ]),
        ("objection-appeal-dispute-deadline-suspension-and-outcome", "Objection, appeal, dispute, deadline, suspension and outcome", ["SRC-003", "SRC-010", "SRC-014", "SRC-017"], [
            ("disputed-item-position-ground-evidence-representative-and-filing-deadline", "Disputed item, position, ground, evidence, representative and filing deadline", "exception", False),
            ("review-appeal-hearing-stay-outcome-remedy-finality-and-further-rights", "Review, appeal, hearing, stay, outcome, remedy, finality and further rights", "lifecycle", False),
        ]),
    ]),
    ("lifecycle-correction-governance-retention-and-interoperability", "Lifecycle, correction, governance, retention and interoperability", "Agents need append-only correction, protected access and version-pinned projections that expose loss and current-head semantics", [
        ("status-amendment-replacement-withdrawal-and-noncascade-lineage", "Status, amendment, replacement, withdrawal and noncascade lineage", ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-014", "SRC-016"], [
            ("draft-filed-received-accepted-rejected-processed-assessed-closed-and-reopened", "Draft, filed, received, accepted, rejected, processed, assessed, closed and reopened", "lifecycle", True),
            ("amend-correct-supersede-replace-withdraw-predecessor-successor-reason-and-effect", "Amend, correct, supersede, replace, withdraw, predecessor, successor, reason and effect", "provenance", True),
        ]),
        ("access-retention-projection-round-trip-and-agent-controls", "Access, retention, projection, round trip and agent controls", ["SRC-005", "SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"], [
            ("purpose-access-confidentiality-redaction-disclosure-legal-hold-retention-and-disposition", "Purpose, access, confidentiality, redaction, disclosure, legal hold, retention and disposition", "privacy", True),
            ("mef-hmrc-xbrl-ubl-xml-signature-prov-projection-version-scope-loss-and-round-trip", "MeF, HMRC, XBRL, UBL, XML Signature, PROV projection, version, scope, loss and round trip", "interoperability", False),
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
        "description": f"Records {low} as source-qualified tax-case context while keeping taxpayer, obligation, law, payment, audit, dispute and authority records in their owning systems.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which stable identities, tax scope, source-qualified values and explicit unknowns establish {low}?", "kind": kinds[0], "answer_data": ["identifiers, tax type, jurisdiction and period", "source-qualified values and versions", "unknown and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who declares, submits, validates, determines, owns, reviews, disputes or is affected by {low}, under which authority and limits?", "kind": kinds[1], "answer_data": ["actors, roles and representation", "authority, delegation and limits", "review, dispute and exception paths"]},
            {"id": f"{fid}-q03", "text": f"Which source-effective, due, signed, submitted, received, accepted, assessed, paid, appealed, recorded, ingested and knowledge times apply to {low}, and how is it corrected?", "kind": kinds[2], "answer_data": ["distinct legal, business and system times", "validation, evidence and uncertainty", "successor correction and retention"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed data for {low} with identity, tax scope, source, authority, status, event and knowledge times, evidence and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned tax-case evidence for {low}.", "media_or_form": ["logical tax-case assertion", "return, schedule, attachment, validation, declaration, submission, acknowledgement, assessment, notice, allocation, dispute or projection record"], "serial": True, "identity_strategy": f"Case ID plus independent return, submission, acknowledgement, assessment, liability, payment, refund, penalty, dispute or assertion ID for {fid}; taxpayer, period, date, amount and status never identify a record alone.", "source_refs": refs}],
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
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified tax-case context for {lname.lower()}.", "source_refs": refs, "findings": findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed tax-case context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({ref for layer in layers for ref in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-tax-case", "Register tax case", ["taxpayer reference", "tax type", "jurisdiction", "period", "owner mandate"], ["case root and constituent slots"], ["stable identity, scope, obligation and authority pass"], ["one bounded filing and assessment case exists without asserting filing or tax status"], ["SRC-001", "SRC-002", "SRC-008"]),
    ("bind-obligation-taxpayer-and-authority", "Bind obligation, taxpayer and authority", ["case", "taxpayer, registration and account references", "obligation", "form and versions"], ["versioned scope binding"], ["master identities, jurisdiction, period, roles and versions pass"], ["external masters remain independent and resolvable"], ["SRC-001", "SRC-005", "SRC-008", "SRC-010"]),
    ("assemble-and-calculate-return", "Assemble and calculate return", ["source data cut", "taxable events", "rules", "form"], ["return, schedules, attachments and reconciliation"], ["source lineage, units, currency, rounding and rule versions pass"], ["a source-qualified self-assessed position is prepared without filing it"], ["SRC-004", "SRC-005", "SRC-009", "SRC-011", "SRC-012"]),
    ("validate-return", "Validate return", ["return", "schema", "code lists", "business rules"], ["separate validation results and correction requests"], ["profiles and versions are pinned and every result is attributable"], ["technical and business outcomes remain separate from legal acceptance"], ["SRC-005", "SRC-006", "SRC-008", "SRC-011", "SRC-012"]),
    ("declare-sign-and-submit", "Declare, sign and submit", ["validated return", "declaration", "signer authority", "channel"], ["signature and transmission records"], ["consent, capacity, signature profile, destination and idempotency pass"], ["submission is recorded without asserting receipt or acceptance"], ["SRC-006", "SRC-007", "SRC-009", "SRC-013"]),
    ("record-acknowledgement-and-acceptance", "Record acknowledgement and acceptance", ["submission", "authority response"], ["receipt, acknowledgement, acceptance or rejection record"], ["message identity, authenticity, status, reason and times pass"], ["receipt, filing acceptance and processing remain distinguishable"], ["SRC-006", "SRC-007", "SRC-008", "SRC-009"]),
    ("record-assessment-and-adjustment", "Record assessment and adjustment", ["return position", "authority notice", "adjustments"], ["assessment, differences, notice and liability references"], ["issuer authority, provision, calculation, service, rights and finality pass"], ["self-assessment and authority determination remain separate"], ["SRC-001", "SRC-010", "SRC-017"]),
    ("link-settlement-refund-and-penalty", "Link settlement, refund and penalty", ["liability", "payment, refund, interest or penalty records"], ["typed allocations and status references"], ["identity, amount, currency, value date, source and reversals pass"], ["money movement stays external and no universal satisfaction is inferred"], ["SRC-007", "SRC-008", "SRC-017"]),
    ("dispute-amend-and-supersede", "Dispute, amend and supersede", ["case head", "grounds", "evidence", "successor return or appeal"], ["dispute or successor lineage"], ["authority, deadline, reason, predecessor, scope and effect pass"], ["original return, receipt, rules and decisions remain reconstructable"], ["SRC-005", "SRC-006", "SRC-014", "SRC-017"]),
    ("project-retain-disclose-and-audit", "Project, retain, disclose and audit", ["case", "target profile", "access and records policy"], ["projection, disclosure, tombstone or disposition event"], ["version, loss, privacy, legal hold, authority and audit pass"], ["context stays protected, reconstructable and explicit about loss"], ["SRC-005", "SRC-008", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]),
]


def functions():
    return [{"id": row[0], "name": row[1], "description": f"Governed operation to {row[1].lower()} without autonomous tax advice, filing, payment, authority decision or mutation of external masters.", "inputs": row[2], "outputs": row[3], "preconditions": row[4], "effects": row[5], "source_refs": row[6]} for row in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner and tax-data mandate", "Authoritative taxpayer, registration, account, obligation, law, form, source-document, ledger, evidence, payment, refund, penalty, audit, assessment, dispute, collection, provenance, access-audit and record registries", "Approved jurisdiction, tax type, filing season, schema, business-rule, signature, currency, privacy, retention and interoperability profiles", "Legal interpretation, representation, signing, submission, payment, dispute, disclosure and agent-operation policies"],
            "namespace_guidance": "Mint case, return, schedule, attachment, calculation, validation, declaration, submission, acknowledgement, assessment, notice, allocation, dispute, correction, disclosure and event IDs; preserve authoritative master and authority identifiers.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize each case and constituent by authoritative master-system identifier, tax administration and record kind; never by taxpayer, period, form, date, amount or status alone.", "Keep return, schedule, attachment, declaration, submission, acknowledgement, assessment notice, liability, payment, refund, penalty and dispute independently identifiable."],
            "patch_rules": ["Extensions declare jurisdiction, tax type, filing season, form, schema, business-rule, signature, privacy, retention and interoperability effects.", "Released returns, submissions, acknowledgements, assessments, notices, allocations and dispute records are immutable; corrections create linked successors.", "Never silently change taxpayer, obligation, period, source values, calculation, declaration, signature, status, amount, reason, deadline, authority or provenance."],
            "compatibility_rules": ["Ignore additive fields only when identity, tax scope, record kind, source, authority, status, time, evidence and provenance survive.", "Every projection pins jurisdiction, tax type, filing season, form, schema, business rules, signature profile and code-list versions and declares information loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative tax-administration or master-system identifier for each case, return, submission, acknowledgement, assessment, liability, payment, refund, penalty, dispute or notice, qualified by administration and record kind.", "Governed globally resolvable tax-record IRI.", "Dimension UUID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish tax period, source effective, due, signed, submitted, postmarked, received, acknowledged, accepted, processed, assessed, served, paid, appealed, recorded, ingested and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {case-id}--{return-submission-acknowledgement-assessment-payment-dispute-or-assertion-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, record kind, tax scope, form and rule versions, actor, authority, event and knowledge times, status, access marking and provenance.",
        },
        "policies": ["The aggregate does not own Taxpayer, Registration, Tax Account, Tax Obligation, Law, Form, Source Document, Ledger, Evidence, Payment, Refund, Penalty, Audit, Examination, Dispute, Collection, Enforcement, Adjudication, Provenance, Access Audit or Record masters.", "Technical validation, business validation, transmission receipt, filing acceptance, processing, self-assessment, authority assessment, payment and dispute outcome remain separate assertions.", "Receipt does not prove validity or acceptance; acceptance does not prove assessment finality, payment, absence of penalties or dispute resolution.", "Agents cannot give tax advice, sign declarations, file returns, initiate payments, change authority decisions, waive appeal rights, disclose tax data or dispose records outside explicit delegated authority."],
        "crud": {
            "read": ["Resolve purpose, case head, taxpayer and obligation references, tax scope, versions, source lineage, calculations, validations, declaration, submission, responses, assessment, settlement links, dispute, holds and projection loss."],
            "create": ["Bind stable case and constituent identity, taxpayer and obligation references, tax type, jurisdiction, period, owner, source, status and effective time before recording an assertion."],
            "update": ["Append successor return, validation, submission, acknowledgement, assessment, allocation, dispute and correction events with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply tax, privacy, evidence, audit, litigation-hold and adopting-Dimension retention policy; retire or tombstone only the case or named constituent without cascading to external masters, and let the external records policy execute physical disposition."],
        },
        "roles": [
            {"name": "Taxpayer or liable party", "responsibilities": ["Own source facts, bounded declarations and decisions within legal capacity."]},
            {"name": "Authorized representative or preparer", "responsibilities": ["Prepare, explain or transmit within explicit representation, signature and disclosure authority."]},
            {"name": "Tax administration case owner", "responsibilities": ["Own administrative processing and attributable authority records within jurisdiction."]},
            {"name": "Assessment or examination officer", "responsibilities": ["Own determination, adjustments, reasons, evidence use, notices and rights within authority."]},
            {"name": "Payment and refund steward", "responsibilities": ["Own money-movement records and allocations in the authoritative financial system."]},
            {"name": "Appeals or dispute officer", "responsibilities": ["Own independent review, procedural deadlines, outcomes and further-rights notices."]},
            {"name": "Tax technology and interoperability steward", "responsibilities": ["Own form, schema, business-rule, signature and projection versions with conformance and loss evidence."]},
            {"name": "Privacy, security and records steward", "responsibilities": ["Own protected views, disclosures, access logs, holds, retention and disposition."]},
        ],
        "access": {"default_rule": "Deny tax returns, assessments and supporting evidence unless a purpose-bound policy permits the minimum necessary view.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Declared taxpayer, representative, tax-authority, auditor, appeal, court, statutory or emergency access must cite authority, scope, purpose and time limit where applicable and must be logged."], "audit_requirements": ["Log actor, agent, role, purpose, case and constituent, operation, authority, policy, RFC 3339 time, affected fields, source revision and outcome without duplicating protected tax data unnecessarily."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"], "read_order": ["Read Dimension tax-authority, representation, signing, filing, payment, dispute, privacy, access, correction, records and agent policies.", "Read this aggregate and linked taxpayer, obligation, law, form, source, evidence, payment, audit, assessment, dispute, provenance and records models before mutation."]},
    }


def coverage():
    dims = ["identity", "classification and definition", "direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability"]
    return {
        "claim": "Covers a source-qualified tax filing and assessment case linking scope, source records, calculation, validation, declaration, submission, acknowledgement, self-assessment, authority determination, settlement references, dispute, correction, protected use and projection.",
        "confidence": "medium",
        "checklist": [{"dimension": dim, "status": "covered", "notes": f"{dim.capitalize()} is explicit; jurisdiction, tax type, missing relations, authority profile and release-pinned validation remain held where applicable."} for dim in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "No relation-ledger edge is registered for WM-ACT-052, so links to taxpayer, obligation, document, evidence, payment, audit, assessment, dispute and records models remain candidate boundary notes.", "Income, corporate, payroll, withholding, consumption, property, customs and other taxes require jurisdiction and tax-type profiles.", "OECD sources are comparative or advisory; IRS and HMRC are jurisdiction-specific; XBRL, UBL and XML Signature require implementation-profile and conformance validation."],
        "conflicts": ["A return, submission, acknowledgement, assessment notice, liability, payment, refund, penalty and dispute are not interchangeable.", "Structural validation, business-rule validation, transmission receipt, filing acceptance, processing and legal acceptance are separate outcomes.", "Self-assessed and authority-determined values must retain their sources, and payment does not prove satisfaction of every obligation."],
        "regional_assumptions": ["Tax liability, filing, assessment, penalties, interest, dispute, finality, retention and disclosure depend on jurisdiction, tax type, period and facts.", "IRS sources are United States profiles, HMRC sources are United Kingdom profiles, and the VAT Directive and GDPR are European Union profiles.", "OECD guidance is not domestic law; forms, schemas, business rules, code lists, signature methods and administrative procedures must be versioned."],
        "adversarial_checks": ["Reject a case or constituent without stable identity, taxpayer and obligation references, tax type, jurisdiction, period, authority, status and lineage head.", "Reject a filing claim that equates transmission, receipt, acceptance, processing, assessment or payment.", "Reject an assessment that overwrites the return position or lacks issuer authority, provision, calculation, reason, notice, effective time and review rights.", "Reject an amendment or replacement that loses original return, submission receipt, governing versions or predecessor-successor lineage.", "Reject autonomous tax advice, declaration signature, filing, payment, authority decision, appeal waiver, protected disclosure or disposition outside explicit authority."],
    }


def build():
    model = {
        "registry_id": "vr.wm-act-052", "model_id": "WM-ACT-052",
        "name": "Tax Filing / Assessment Process", "entry_kind": "aggregate",
        "purpose": "Represent a governed tax filing and assessment case so agents can connect return preparation, validation, declaration, submission, authority determination, settlement references and dispute without treating any transport or workflow state as proof of legal finality or payment.",
        "scope_statement": "Owns one filing-and-assessment case identity for a defined taxpayer reference, tax type, jurisdiction and period; return composition and source lineage; calculation and validation results; declaration, submission and acknowledgement links; self-assessed and authority-determined positions; adjustments, notice and liability references; settlement, penalty and dispute links; and correction lineage. Taxpayer, registration, account, obligation, law, form, source document, ledger, evidence, payment, refund, penalty, audit, examination, dispute, collection, enforcement, adjudication, provenance, access audit and record masters remain external.",
        "in_scope": ["Case identity and tax scope; return, schedule and attachment composition; source lineage, calculations, validations, declaration, submission and acknowledgement", "Self-assessment, authority assessment and adjustment context; notice and liability references; payment, refund, penalty and dispute links; correction, privacy, retention and loss-aware projections"],
        "out_of_scope": ["Creating or changing taxpayer, tax account, obligation, law, form, source record, payment, refund, penalty, examination, dispute, collection, enforcement or court masters", "Equating receipt with acceptance, acceptance with processing, self-assessment with authority assessment, payment with full satisfaction, or notice with finality", "Providing tax advice, signing or filing without authority, moving money, deciding an assessment or appeal, or destructively handling tax evidence"],
        "boundary_notes": [
            {"neighbor": "Taxpayer, registration, tax account, obligation and law models", "distinction": "These masters retain authoritative identity and lifecycle. The case stores typed, versioned references and a bounded filing scope without rewriting them.", "source_refs": ["SRC-001", "SRC-002", "SRC-004", "SRC-010"]},
            {"neighbor": "Return, schedule, attachment, declaration, submission and acknowledgement", "distinction": "Each record has independent identity, authority, status and time. A technical receipt is not a legal acceptance or assessment.", "source_refs": ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009"]},
            {"neighbor": "Audit, examination, assessment, collection, enforcement and adjudication", "distinction": "Specialist processes own selection, evidence gathering, decisions and enforcement. This aggregate records links, notices, amounts, reasons, deadlines and status intake.", "source_refs": ["SRC-001", "SRC-003", "SRC-017"]},
            {"neighbor": "Payment, refund, interest and penalty models", "distinction": "Authoritative financial systems own money movement and balances. The case stores typed allocation and status references without inferring universal satisfaction.", "source_refs": ["SRC-007", "SRC-008", "SRC-017"]},
            {"neighbor": "Dispute and appeal models", "distinction": "Specialist models own proceedings and outcomes. This aggregate retains the disputed items, grounds, evidence links, deadlines, stays and result references.", "source_refs": ["SRC-010", "SRC-017"]},
            {"neighbor": "MeF, HMRC VAT API, XBRL, UBL, XML Signature and PROV", "distinction": "These are versioned jurisdictional or technical projections with different scopes. No mapping is assumed lossless or universally applicable.", "source_refs": ["SRC-005", "SRC-006", "SRC-008", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]},
        ],
    }
    composition = [
        {"target": "Taxpayer, registration, tax account, obligation, law and form models", "relation": "REFERENCE", "purpose": "Resolve authoritative filing scope and legal basis without absorbing master identity or lifecycle.", "required": True, "source_refs": ["SRC-001", "SRC-002", "SRC-004", "SRC-010"]},
        {"target": "Source document, transaction, ledger, evidence and provenance models", "relation": "REFERENCE", "purpose": "Trace return values, adjustments and claims to protected source records and transformations.", "required": True, "source_refs": ["SRC-004", "SRC-007", "SRC-009", "SRC-012", "SRC-014"]},
        {"target": "Payment, refund, interest, penalty and financial-account models", "relation": "REFERENCE", "purpose": "Bind authoritative money movement and allocation without owning settlement execution.", "required": False, "source_refs": ["SRC-007", "SRC-008", "SRC-017"]},
        {"target": "Audit, examination, dispute, appeal, collection, enforcement and adjudication models", "relation": "REFERENCE", "purpose": "Bind specialist authority processes, notices, rights and outcomes without absorbing their execution.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-010", "SRC-017"]},
        {"target": "MeF, HMRC VAT API, XBRL 2.1, UBL 2.4, XML Signature 1.1 and PROV-O", "relation": "ALIGN", "purpose": "Project version-pinned filing, reporting, source-document, signature and provenance views with jurisdiction, scope and loss declarations.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-008", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    RUN.joinpath("codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
