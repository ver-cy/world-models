#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-ECO-018."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T14:13:00Z"


def src(i, title, org, url, version, kind, relevance):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": 1, "accessed_at": AT,
        "relevance": relevance,
    }


SOURCES = [
    src(1, "Conceptual Framework for Financial Reporting", "IFRS Foundation", "https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/", "Revised March 2018; current 2026 issued text", "standard", "Defines reporting entity, elements, recognition, measurement, presentation, faithful representation and uncertainty."),
    src(2, "IAS 1 Presentation of Financial Statements", "IFRS Foundation", "https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements.html/", "Current at access; superseded by IFRS 18 for periods beginning on or after 1 January 2027 unless early applied", "standard", "Defines complete financial statement sets, financial position, performance, equity, cash flows, notes, comparatives and compliance."),
    src(3, "IAS 7 Statement of Cash Flows", "IFRS Foundation", "https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/", "Current at access; amended for IFRS 18 effective 2027", "standard", "Defines operating, investing and financing cash-flow presentation and reconciliation to financial-position amounts."),
    src(4, "IFRS 18 Presentation and Disclosure in Financial Statements", "IFRS Foundation", "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/", "Issued April 2024; effective 1 January 2027 with early application permitted", "standard", "Defines presentation and disclosure requirements, statement-set comparatives, profit-or-loss categories and defined subtotals."),
    src(5, "IFRS Accounting Taxonomy 2025", "IFRS Foundation", "https://www.ifrs.org/issued-standards/ifrs-taxonomy/ifrs-accounting-taxonomy-2025/", "Published 27 March 2025; remains current for 2026 reporting", "schema", "Defines digital financial-report concepts, statement groups, facts, dimensions, labels, references, entry points and formula checks."),
    src(6, "XBRL 2.1", "XBRL International", "https://specifications.xbrl.org/work-product-index-group-base-spec-base-spec.html", "Recommendation 20 February 2013; conformance suite 16 July 2025", "standard", "Defines report facts, concepts, contexts, entities, periods, scenarios, units, decimals, footnotes and validation."),
    src(7, "Inline XBRL 1.1", "XBRL International", "https://specifications.xbrl.org/work-product-index-inline-xbrl-inline-xbrl-1.1.html", "Recommendation edition 14 July 2026", "standard", "Defines embedding XBRL facts and references in human-readable HTML documents."),
    src(8, "Open Information Model 1.0", "XBRL International", "https://specifications.xbrl.org/work-product-index-open-information-model-open-information-model.html", "Recommendations 19 April 2023; xBRL-CSV Table Constraints proposed 5 May 2026", "standard", "Defines a syntax-independent XBRL report model and XML, JSON and CSV representations."),
    src(9, "Regulation S-X and disclosure rules", "United States Securities and Exchange Commission", "https://www.sec.gov/about/divisions-offices/division-corporation-finance/rules-regulations-schedules", "17 CFR Part 210 current at access", "legislation", "Defines form, content and requirements for financial statements filed with the SEC."),
    src(10, "2026 XBRL Taxonomies Update", "United States Securities and Exchange Commission", "https://www.sec.gov/newsroom/whats-new/2603-2026-xbrl-taxonomies-update", "EDGAR release 26.1 supported 16 March 2026", "public-authority", "Pins SEC-supported 2026 taxonomy versions and compatibility constraints for filings."),
    src(11, "2026 GAAP Financial Reporting Taxonomy", "Financial Accounting Standards Board", "https://xbrl.fasb.org/us-gaap/2026/", "2026 taxonomy files published December 2025", "schema", "Defines US GAAP financial-reporting concepts, statement structures, calculations, dimensions and references."),
    src(12, "Commission Delegated Regulation EU 2019/815 consolidated text", "European Union", "https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX%3A02019R0815-20260407", "Consolidated 7 April 2026", "legislation", "Requires ESEF annual-report format and markup of IFRS consolidated financial statements in scope."),
    src(13, "ESEF Reporting Manual", "European Securities and Markets Authority", "https://www.esma.europa.eu/sites/default/files/library/esma32-60-254_esef_reporting_manual.pdf", "2025 update dated 14 October 2025", "public-authority", "Provides implementation guidance for annual financial reports in ESEF format."),
    src(14, "2025 Handbook of International Public Sector Accounting Pronouncements", "International Public Sector Accounting Standards Board", "https://www.ipsasb.org/publications/2025-handbook-international-public-sector-accounting-pronouncements", "Current edition published 5 May 2025; standards as of 31 January 2025", "standard", "Defines public-sector financial reporting standards and conceptual framework as a domain profile."),
    src(15, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation 30 April 2013", "ontology", "Defines entity, activity, agent, attribution, generation, derivation, revision and qualified provenance."),
    src(16, "Data on the Web Best Practices: Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note 15 December 2016", "ontology", "Defines quality dimensions, metrics, measurements, annotations, policies and certificates."),
    src(17, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339 July 2002, updated by RFC 9557", "standard", "Defines interoperable timestamps with seconds and explicit relationship to UTC."),
]


ROWS = [
    ("report-identity-scope-framework-and-authority", "Report identity, scope, framework and authority", "Identify the report and its normative basis without absorbing the entity, filing or publication", [
        ("report-root-identity-version-purpose-and-status", "Report root identity, version, purpose and status", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-015"], [
            ("statement-id-version-head-title-type-purpose-language-and-status", "Statement ID, version, head, title, type, purpose, language and status", "identity", True),
            ("preparation-basis-framework-jurisdiction-taxonomy-entry-point-and-compliance-claim", "Preparation basis, framework, jurisdiction, taxonomy entry point and compliance claim", "authority", True),
        ]),
        ("reporting-entity-perimeter-ownership-and-responsibility", "Reporting entity, perimeter, ownership and responsibility", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-011", "SRC-014"], [
            ("reporting-entity-identifier-legal-form-domicile-address-and-authoritative-master", "Reporting entity identifier, legal form, domicile, address and authoritative master", "relationship", True),
            ("separate-consolidated-combined-perimeter-parent-subsidiary-nci-and-control-basis", "Separate, consolidated, combined perimeter, parent, subsidiary, NCI and control basis", "composition", True),
        ]),
    ]),
    ("statement-set-structure-line-items-facts-and-dimensions", "Statement set, structure, line items, facts and dimensions", "Represent human and machine structure while preserving the identity of every fact and component", [
        ("statement-set-sections-notes-and-presentation-tree", "Statement set, sections, notes and presentation tree", ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-014"], [
            ("financial-position-performance-oci-equity-cash-flow-notes-and-opening-statement", "Financial position, performance, OCI, equity, cash flow, notes and opening statement", "composition", True),
            ("section-table-axis-member-line-item-subtotal-total-note-policy-and-cross-reference", "Section, table, axis, member, line item, subtotal, total, note, policy and cross-reference", "composition", True),
        ]),
        ("facts-concepts-contexts-units-and-dimensional-qualifiers", "Facts, concepts, contexts, units and dimensional qualifiers", ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-010", "SRC-011", "SRC-013"], [
            ("fact-id-concept-value-nil-decimals-precision-unit-scale-sign-and-footnote", "Fact ID, concept, value, nil, decimals, precision, unit, scale, sign and footnote", "measurement", True),
            ("entity-period-scenario-segment-axis-member-typed-dimension-and-context-identity", "Entity, period, scenario, segment, axis, member, typed dimension and context identity", "classification", True),
        ]),
    ]),
    ("periods-currency-comparatives-restatements-and-presentation", "Periods, currency, comparatives, restatements and presentation", "Preserve time, unit and comparison semantics across versions and renderings", [
        ("reporting-period-as-of-cutoff-authorization-and-publication-time", "Reporting period, as-of, cutoff, authorization and publication time", ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-009", "SRC-017"], [
            ("annual-interim-current-prior-opening-instant-duration-and-reporting-period", "Annual, interim, current, prior, opening, instant, duration and reporting period", "temporal", True),
            ("cutoff-adjusting-event-preparation-review-authorization-issue-filing-publication-ingestion-and-knowledge-time", "Cutoff, adjusting event, preparation, review, authorization, issue, filing, publication, ingestion and knowledge time", "temporal", True),
        ]),
        ("currency-rounding-comparatives-reclassification-and-restatement", "Currency, rounding, comparatives, reclassification and restatement", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-011"], [
            ("functional-presentation-transaction-currency-unit-multiplier-rounding-and-translation", "Functional, presentation, transaction currency, unit, multiplier, rounding and translation", "measurement", True),
            ("comparative-corresponding-restated-reclassified-adjusted-reported-and-reconciliation-basis", "Comparative, corresponding, restated, reclassified, adjusted, reported and reconciliation basis", "lifecycle", True),
        ]),
    ]),
    ("policies-estimates-materiality-sources-consolidation-and-lineage", "Policies, estimates, materiality, sources, consolidation and lineage", "Explain how reported facts were selected and produced without taking ownership of accounting operations", [
        ("accounting-policies-estimates-judgements-and-materiality", "Accounting policies, estimates, judgements and materiality", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-009", "SRC-014"], [
            ("accounting-policy-recognition-measurement-presentation-disclosure-and-change", "Accounting policy, recognition, measurement, presentation, disclosure and change", "requirement", True),
            ("estimate-assumption-judgement-uncertainty-materiality-aggregation-disaggregation-and-omission", "Estimate, assumption, judgement, uncertainty, materiality, aggregation, disaggregation and omission", "decision", True),
        ]),
        ("source-ledgers-trial-balance-consolidation-and-provenance", "Source ledgers, trial balance, consolidation and provenance", ["SRC-001", "SRC-005", "SRC-006", "SRC-008", "SRC-011", "SRC-015"], [
            ("account-ledger-journal-trial-balance-position-subledger-and-source-system-binding", "Account, ledger, journal, trial balance, position, subledger and source-system binding", "provenance", True),
            ("consolidation-run-elimination-adjustment-mapping-transformation-author-and-lineage", "Consolidation run, elimination, adjustment, mapping, transformation, author and lineage", "provenance", True),
        ]),
    ]),
    ("calculations-validation-reconciliation-notes-and-assurance", "Calculations, validation, reconciliation, notes and assurance", "Keep arithmetic, semantic, disclosure and assurance claims independently testable", [
        ("calculations-invariants-validation-reconciliation-and-quality", "Calculations, invariants, validation, reconciliation and quality", ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-010", "SRC-011", "SRC-016"], [
            ("calculation-weight-total-subtotal-rollforward-equation-cross-foot-and-rounding-tolerance", "Calculation weight, total, subtotal, rollforward, equation, cross-foot and rounding tolerance", "validation", True),
            ("taxonomy-schema-formula-business-rule-reconciliation-error-warning-and-quality-metric", "Taxonomy, schema, formula, business rule, reconciliation, error, warning and quality metric", "quality", True),
        ]),
        ("notes-disclosures-evidence-audit-and-assurance-references", "Notes, disclosures, evidence, audit and assurance references", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-009", "SRC-013", "SRC-014", "SRC-015", "SRC-016"], [
            ("note-policy-risk-commitment-contingency-related-party-segment-and-subsequent-event-disclosure", "Note, policy, risk, commitment, contingency, related party, segment and subsequent-event disclosure", "evidence", True),
            ("preparer-reviewer-governance-representation-auditor-opinion-assurance-scope-and-limitation", "Preparer, reviewer, governance, representation, auditor, opinion, assurance scope and limitation", "authority", True),
        ]),
    ]),
    ("lifecycle-authorization-filing-access-retention-and-interoperability", "Lifecycle, authorization, filing, access, retention and interoperability", "Govern issue and delivery while keeping external filing and publication lifecycles separate", [
        ("preparation-review-authorization-issue-amendment-and-records", "Preparation, review, authorization, issue, amendment and records", ["SRC-001", "SRC-002", "SRC-004", "SRC-009", "SRC-012", "SRC-014", "SRC-015"], [
            ("draft-prepared-reviewed-approved-authorized-issued-amended-restated-superseded-and-withdrawn", "Draft, prepared, reviewed, approved, authorized, issued, amended, restated, superseded and withdrawn", "lifecycle", True),
            ("confidentiality-access-embargo-filing-acceptance-rejection-publication-retention-legal-hold-and-tombstone", "Confidentiality, access, embargo, filing acceptance, rejection, publication, retention, legal hold and tombstone", "access", True),
        ]),
        ("xbrl-inline-oim-esef-and-jurisdictional-projections", "XBRL, Inline, OIM, ESEF and jurisdictional projections", [f"SRC-{i:03d}" for i in range(1, 18)], [
            ("human-pdf-html-data-package-api-xbrl-inline-json-csv-and-filing-distribution", "Human, PDF, HTML, data package, API, XBRL, Inline, JSON, CSV and filing distribution", "interoperability", True),
            ("ifrs-ias-ifrs18-xbrl-oim-sec-usgaap-esef-ipsas-prov-dqv-and-time-projection", "IFRS, IAS, IFRS 18, XBRL, OIM, SEC, US GAAP, ESEF, IPSAS, PROV, DQV and time projection", "interoperability", True),
        ]),
    ]),
]

KINDS = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def finding(item, n, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(n + 7) % len(KINDS)], KINDS[(n + 16) % len(KINDS)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {low} as source-qualified statement context while entity, account, position, transaction, journal, consolidation, policy, audit, filing, publication and records masters remain independently identifiable.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What stable report and fact identity, version, framework, typed value, period, unit, scope and explicit unknown establish {low}?", "kind": kinds[0], "answer_data": ["statement, component, fact, context, concept and external master identifiers", "typed value, unit, decimals, taxonomy, framework, jurisdiction, period and schema version", "nil, unknown, omitted, disputed, estimated, restated and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who prepares, owns, asserts, reviews, governs, authorizes, assures, files, publishes or may rely on {low}, for which purpose and under what authority?", "kind": kinds[1], "answer_data": ["reporting entity, preparer, reviewer, governance body, auditor, regulator, actor and system", "purpose, framework, authority, policy, access, confidentiality, materiality and retention", "conflict, exception, segregation of duties, escalation and accountability"]},
            {"id": f"{fid}-q03", "text": f"Which reporting, as-of, preparation, review, authorization, issue, filing, publication, observation, ingestion and knowledge times, source, evidence and uncertainty qualify {low}?", "kind": kinds[2], "answer_data": ["distinct instant, duration, operational, reporting, filing and knowledge times", "ledger, position, policy, calculation, transformation, evidence, quality and limitation", "comparative, reclassification, correction, restatement, successor, legal hold and audit"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed financial-statement data for {low}, qualified by report version, framework, period, unit, authority, uncertainty and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned report evidence for {low}.", "media_or_form": ["logical financial-statement specification assertion", "report, component, fact, context, note, policy binding, calculation, validation, reconciliation, approval, filing or projection record"], "serial": True, "identity_strategy": f"Statement ID plus independent report version, component or fact ID, reporting context and artifact kind for {fid}; a title, date, value, filename or digest never identifies a statement fact alone.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles, n = [], 0
    for bid, bname, rationale, layers in ROWS:
        rendered = []
        for lid, lname, refs, items in layers:
            fs = []
            for item in items:
                n += 1
                fs.append(finding(item, n, refs))
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified financial-statement context for {lname.lower()}.", "source_refs": refs, "findings": fs})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed financial-statement context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({r for layer in layers for r in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-statement", "Register a financial statement", ["owner", "purpose", "reporting entity and framework"], ["stable statement and version head"], ["namespace, identity, authority, entity, perimeter, framework and duplicate checks pass"], ["a report aggregate exists without creating ledger facts or a filing"], ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-015"]),
    ("compose-statement-set", "Compose a statement set and presentation tree", ["statement version", "components, sections and notes", "presentation rules"], ["versioned statement structure"], ["component type, hierarchy, order, labels, references, completeness and cycle checks pass"], ["human presentation remains linked to semantic facts"], ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006"]),
    ("bind-reporting-entity-perimeter-and-period", "Bind reporting entity, perimeter and period", ["statement", "external entity and control references", "period and cutoff"], ["non-owning entity, perimeter and temporal context"], ["identity, control basis, consolidation scope, instant or duration, comparative and authority checks pass"], ["external entity and control lifecycles remain authoritative"], ["SRC-001", "SRC-002", "SRC-004", "SRC-006", "SRC-014"]),
    ("add-or-amend-fact", "Add or amend a statement fact", ["statement head", "concept, value, context and unit", "source authority"], ["successor fact assertion"], ["identity, taxonomy, datatype, entity, period, dimensions, unit, decimals, source and expected revision checks pass"], ["an issued fact is never silently overwritten"], ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-011"]),
    ("bind-policies-estimates-and-materiality", "Bind policies, estimates and materiality decisions", ["statement", "external policy or decision", "scope and effective period"], ["qualified non-owning policy and judgement binding"], ["framework, authority, applicability, change, uncertainty, materiality and evidence checks pass"], ["the statement does not make or execute accounting policy decisions"], ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-014"]),
    ("bind-sources-and-consolidation-lineage", "Bind sources and consolidation lineage", ["statement facts", "ledger, position or trial-balance references", "consolidation run"], ["fact-level lineage graph"], ["source, mapping, adjustment, elimination, transformation, actor, run, time and digest checks pass"], ["the report records lineage but does not post or consolidate"], ["SRC-001", "SRC-005", "SRC-006", "SRC-008", "SRC-011", "SRC-015"]),
    ("calculate-validate-and-reconcile", "Calculate, validate and reconcile", ["statement version", "calculation and business rules", "comparison sources"], ["validation results and reconciliation evidence"], ["rule version, weights, signs, units, periods, dimensions, tolerances, materiality and completeness checks pass"], ["errors are reported without autonomously changing facts"], ["SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-010", "SRC-011", "SRC-016"]),
    ("review-assure-and-authorize-issue", "Review, assure and authorize issue", ["statement candidate", "review and assurance evidence", "authorized decision"], ["qualified review, assurance reference and lifecycle assertion"], ["scope, standard, evidence, conflicts, representation, opinion reference, authority and expected revision checks pass"], ["the model records but does not perform audit, sign or certify"], ["SRC-001", "SRC-002", "SRC-009", "SRC-013", "SRC-014", "SRC-015"]),
    ("issue-amend-restate-or-supersede", "Issue, amend, restate or supersede", ["statement head", "authorized lifecycle decision", "change and comparative evidence"], ["immutable issued version and successor linkage"], ["authority, reason, materiality, affected facts, comparatives, authorization time, retention and disclosure checks pass"], ["prior issued versions remain resolvable"], ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-009", "SRC-015"]),
    ("query-project-file-retain-and-audit", "Query, project, file, retain and audit", ["statement", "target profile", "purpose-bound access, filing and records policy"], ["filtered projection, filing package, retention result or audit event"], ["purpose, authority, mapping, loss, confidentiality, acceptance state, digest and retention checks pass"], ["filing and publication remain external lifecycles and every projection declares loss"], [f"SRC-{i:03d}" for i in range(1, 18)]),
]


def functions():
    return [{"id": x[0], "name": x[1], "description": f"Governed operation to {x[1].lower()} without autonomous posting, consolidation, calculation-driven mutation, reclassification, valuation, audit, signing, filing, publication, restatement, access widening or records disposition.", "inputs": x[2], "outputs": x[3], "preconditions": x[4], "effects": x[5], "source_refs": x[6]} for x in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner, namespace authority, financial-reporting mandate and accountable statement owner", "Authoritative Entity, Control, Account, Ledger, Position, Transaction, Journal, Trial Balance, Consolidation, Policy, Estimate, Audit, Filing, Publication and Records registries", "Approved accounting, regulatory, public-sector, taxonomy, currency, unit, calculation, materiality, assurance, access, retention and interoperability profiles", "Role, delegation, segregation-of-duties, preparation, review, authorization, issue, filing, amendment, restatement and agent-operation policies"],
            "namespace_guidance": "Mint statement, statement-version, component, fact, context, note, policy-binding, calculation, validation, reconciliation, assurance-reference, lifecycle and projection IDs; preserve every external master identifier.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"]},
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize a statement by authoritative report identifier, owner namespace, reporting entity, perimeter, statement type, framework and reporting period, never by title, filename, publication date or digest alone.", "Keep statement, reporting entity, account, position, transaction, journal, consolidation run, policy, audit opinion, filing, publication and records independently identifiable."],
            "patch_rules": ["Extensions declare report, entity, period, currency, fact, dimension, calculation, policy, assurance, lifecycle, access and interoperability effects.", "Issued statements and facts are immutable; changes create linked amendments or restatements with reason, affected facts, comparatives, compatibility, migration and approval.", "Never silently change reporting entity, perimeter, framework, period, concept, dimensions, value, unit, decimals, presentation currency, comparative, policy, source, approval or filing state."],
            "compatibility_rules": ["Ignore additive fields only when report and fact identity, entity, period, dimensions, value, unit, framework, authority, access and provenance survive.", "Every projection pins standard, taxonomy, entry point, message or filing profile and declares fact, dimension, precision, presentation, footnote and lifecycle loss."]},
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each statement, version, component, fact, context, note, validation, approval or artifact, qualified by issuer, namespace and record kind.", "Governed globally resolvable report or fact IRI.", "Dimension UUID or ULID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish reporting-period boundaries, preparation, review, authorization, issue, filing, publication, observation, ingestion and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {statement-id}--{statement-version}--{component-fact-or-context-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, record kind, reporting entity and period, framework and taxonomy versions, actor, distinct event and knowledge times, confidentiality marking and provenance."},
        "policies": ["The statement owns report structure, facts, notes, versions, validations and projections but not external entity, account, position, transaction, journal, consolidation, policy, audit, filing, publication or records masters.", "A statement fact is qualified by concept, reporting entity, period, dimensions, unit, decimals, framework, source and provenance; it is not a free-floating number.", "Preparation, review, authorization, issue, filing acceptance, publication and audit opinion are distinct decisions or events.", "Agents cannot autonomously post, consolidate, mutate from calculations, reclassify, value, approve, audit, sign, file, publish, restate, disclose, widen access or dispose financial records without delegated authority."],
        "crud": {
            "read": ["Resolve statement head, reporting entity, perimeter, framework, period, components, facts, contexts, notes, policies, sources, calculations, validations, assurance, lifecycle, access and projection loss under the permitted view."],
            "create": ["Bind stable identity, owner, purpose, reporting entity, perimeter, framework, taxonomy entry point, period, presentation currency, source authority and initial lifecycle before facts are accepted."],
            "update": ["Append successor components, facts, contexts, notes, policy bindings, calculations, validations, reconciliations, review evidence, amendments, restatements and lifecycle assertions with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply legal hold, financial-record, regulatory, audit, privacy and adopting-Dimension retention policy; withdraw or tombstone only the catalog view without cascading to external masters, and let authoritative systems execute physical disposition."]},
        "roles": [
            {"name": "Statement owner", "responsibilities": ["Own purpose, reporting scope, framework, lifecycle, compatibility and accountable use."]},
            {"name": "Preparer and accounting controller", "responsibilities": ["Own structure, facts, contexts, policies, estimates, mappings, calculations, sources and corrections."]},
            {"name": "Consolidation and data steward", "responsibilities": ["Own entity perimeter, ledger and position bindings, eliminations, transformations, lineage and reconciliation evidence."]},
            {"name": "Governance reviewer and authorizing body", "responsibilities": ["Own review, materiality, representations, approval and authorization for issue."]},
            {"name": "Independent assurance provider", "responsibilities": ["Own external engagement, procedures, opinion and limitations; the statement stores only qualified references."]},
            {"name": "Filing, access and records authority", "responsibilities": ["Own filing, disclosure, confidentiality, publication, embargo, retention, legal hold and disposition policy."]},
            {"name": "Taxonomy and interoperability steward", "responsibilities": ["Own taxonomy entry points, extensions, labels, mappings, conformance evidence and declared loss."]}],
        "access": {
            "default_rule": "Deny draft, unreleased, confidential, personal, market-sensitive, account-level, adjustment, estimate, audit, control-deficiency, regulator-only or reconstruction-capable data unless a purpose-bound policy permits the minimum necessary view.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Declared accounting, regulatory, assurance, audit, legal, incident or subject-rights access must cite authority, scope, purpose and time limit and must be logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, statement and version, operation, authority, policy, RFC 3339 time, affected components or facts, source revision and outcome without duplicating restricted financial data."]},
        "agents_bootstrap": {
            "filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read Dimension financial-reporting, namespace, framework, taxonomy, currency, materiality, assurance, filing, access, retention and agent policies.", "Read this statement and linked entity, control, account, position, transaction, journal, consolidation, policy, audit, filing, publication and records models before mutation."]},
    }


def coverage():
    dims = ["identity", "classification and direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability", "authority and ethics"]
    return {
        "claim": "Covers one governed financial statement or statement set from identity, reporting entity and framework through structure, facts, periods, currency, comparatives, policies, lineage, calculations, notes, assurance references, lifecycle, access, filing and projections.",
        "confidence": "medium",
        "checklist": [{"dimension": d, "status": "covered" if d != "spatial" else "not-applicable", "notes": ("Spatial properties are not intrinsic; domicile, jurisdiction, exchange, branch and asset locations remain referenced context." if d == "spatial" else f"{d.capitalize()} is explicit; framework, jurisdiction, sector, filing, assurance and external-review profiles remain held where applicable.")} for d in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "The WM-REC-002 parent signal and candidate WM-ECO-017 composition are not canonically approved and grant no cascade authority.", "Insurance, banking, investment funds, tax, prudential, sustainability, segment, interim, liquidation, public-sector and jurisdiction-specific filing requirements need separate profiles.", "IFRS and FASB materials are used only within public access and licensing boundaries; restricted requirements were not inferred.", "IFRS 18 transition requires an explicit effective-period and entry-point choice; IAS 1 remains applicable until superseded for the reporting entity or early adoption occurs."],
        "conflicts": ["Financial statement, complete statement set, annual report, regulatory filing, XBRL report, audit opinion and published document are related but not interchangeable identities.", "Statement fact, account balance, financial position, transaction, journal entry, trial-balance row and calculated subtotal remain separate assertions.", "Instant facts, duration facts, reporting period, preparation, authorization, issue, filing, publication and knowledge times must not be collapsed.", "Reported, comparative, reclassified, adjusted, amended and restated facts require explicit versions and reconciliation."],
        "regional_assumptions": ["Recognition, measurement, presentation, materiality, audit, filing, disclosure, retention and compliance depend on framework, jurisdiction, regulator, entity, sector and reporting period.", "IFRS, US GAAP, SEC, ESEF and IPSAS are overlapping framework and jurisdiction profiles; none is universal."],
        "adversarial_checks": ["Reject a package that collapses the statement into its entity, accounts, positions, ledger, consolidation, audit opinion, filing or publication.", "Reject a fact without concept, entity, period, dimensions, unit, decimals or precision, framework, source and provenance.", "Reject silent calculation-driven mutation, aggregation, reclassification, currency translation, amendment, restatement or taxonomy remapping.", "Reject a compliance or assurance claim without scope, framework or standard version, responsible authority, evidence and limitations.", "Reject autonomous posting, consolidation, audit, signing, filing, publication, disclosure, access widening or records disposition.", "Reject a projection that hides taxonomy entry point, extensions, dimensions, units, decimals, footnotes, comparatives, lifecycle or information loss."]}


def build():
    model = {
        "registry_id": "vr.wm-eco-018", "model_id": "WM-ECO-018", "name": "Financial Statement", "entry_kind": "aggregate",
        "purpose": "Represent one governed financial statement or complete statement set so agents can interpret who reports, for which period and framework, which facts and disclosures are asserted, how they were prepared and validated, and which version was authorized without confusing the report with its source ledgers, audit or filing.",
        "scope_statement": "Owns report identity, versions, purpose, type and lifecycle; reporting-entity, perimeter and control references; accounting framework, jurisdiction, taxonomy and compliance claims; annual, interim, instant, duration and comparative periods; functional and presentation currency references, units and rounding; statement set, sections, lines, facts, contexts, dimensions, totals, notes, disclosures, policies and cross-references; comparatives, reclassifications, amendments and restatements; external accounting-policy, estimate, ledger, position, trial-balance, consolidation and elimination bindings; calculation, validation, reconciliation, materiality, quality and lineage evidence; preparer, reviewer, governance, auditor, authorization, filing and publication references; access, retention and version-pinned human, XBRL, Inline XBRL, OIM, ESEF and jurisdictional projections. External entity, account, position, transaction, journal, consolidation, policy, audit, filing, publication and records masters remain authoritative.",
        "in_scope": ["Statement identity, reporting entity and perimeter, framework, taxonomy, reporting and comparative periods, currencies, units, statement-set structure, facts, contexts, dimensions, notes and disclosures", "Policies and estimates bindings, source lineage, calculations, validation, reconciliation, quality, assurance references, authorization, amendments, lifecycle, access, filing and interoperability projections"],
        "out_of_scope": ["Owning Reporting Entity, Control, Account, Ledger, Position, Transaction, Journal Entry, Trial Balance, Consolidation Run, Accounting Policy, Estimate Decision, Audit Engagement, Audit Opinion, Filing, Publication or Records masters", "Treating a presented statement fact as the authoritative account, position or transaction, or treating a validation result as audit assurance", "Autonomous posting, consolidation, calculation-driven mutation, reclassification, valuation, approval, audit, signing, filing, publication, restatement, disclosure, access widening or physical records disposition"],
        "boundary_notes": [
            {"neighbor": "WM-REC-002 parent signal", "distinction": "The unfrozen record parent may provide generic record context but grants no ownership, mutation or cascade authority over the financial-statement lifecycle.", "source_refs": ["SRC-006", "SRC-015"]},
            {"neighbor": "WM-ECO-017 Financial Position / Balance", "distinction": "The candidate composition allows a statement to report positions or balances. Each position remains a time-bound quantitative master while the statement owns presentation and report-version context.", "source_refs": ["SRC-002", "SRC-005", "SRC-006"]},
            {"neighbor": "Account, transaction, journal, trial balance and consolidation", "distinction": "These objects supply operational and accounting facts or transformations. The statement binds their outputs and provenance without posting or executing consolidation.", "source_refs": ["SRC-001", "SRC-005", "SRC-006", "SRC-011", "SRC-015"]},
            {"neighbor": "Audit opinion, filing and publication", "distinction": "Independent assurance, regulator submission and public distribution have separate authorities and lifecycles. The statement stores qualified references and status observations only.", "source_refs": ["SRC-002", "SRC-009", "SRC-010", "SRC-012", "SRC-013", "SRC-014"]},
            {"neighbor": "IFRS, XBRL, SEC, US GAAP, ESEF, IPSAS, PROV, DQV and RFC profiles", "distinction": "Each source has a distinct scope, effective period and normative force. Every mapping is version-pinned, jurisdiction-qualified and loss-declaring.", "source_refs": [f"SRC-{i:03d}" for i in range(1, 18)]}],
    }
    composition = [
        {"target": "WM-REC-002", "relation": "REFERENCE", "purpose": "Resolve generic record context without granting ownership, mutation or cascade authority.", "required": False, "source_refs": ["SRC-006", "SRC-015"]},
        {"target": "WM-ECO-017", "relation": "COMPOSE", "purpose": "Report positions or balances while preserving their independent identity, measurement basis, time and provenance.", "required": False, "source_refs": ["SRC-002", "SRC-005", "SRC-006"]},
        {"target": "Reporting Entity, Control, Account, Ledger, Transaction, Journal, Trial Balance, Consolidation, Accounting Policy, Estimate, Audit, Filing, Publication and Records models", "relation": "REFERENCE", "purpose": "Resolve authoritative external identities, processes, decisions and evidence without duplicating their lifecycles.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-009", "SRC-011", "SRC-014", "SRC-015"]},
        {"target": "IFRS 2026, IAS 1, IAS 7, IFRS 18, IFRS Taxonomy 2025, XBRL 2.1, Inline XBRL 1.1, OIM 1.0, SEC Regulation S-X and 2026 taxonomy, US GAAP 2026, ESEF 2026, ESMA 2025, IPSAS 2025, PROV-O, DQV and RFC 3339", "relation": "ALIGN", "purpose": "Project version-pinned accounting, digital-reporting, filing, public-sector, provenance, quality and time views with declared loss.", "required": False, "source_refs": [f"SRC-{i:03d}" for i in range(1, 18)]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
