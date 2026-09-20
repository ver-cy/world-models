#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-ECO-017."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T13:59:00Z"


def src(i, title, org, url, version, kind, relevance):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": 1, "accessed_at": AT,
        "relevance": relevance,
    }


SOURCES = [
    src(1, "Conceptual Framework for Financial Reporting", "IFRS Foundation",
        "https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/", "Revised March 2018; current 2026 issued text", "standard",
        "Defines reporting entity, assets, liabilities, equity, recognition, derecognition, measurement, presentation and uncertainty concepts."),
    src(2, "IAS 1 Presentation of Financial Statements", "IFRS Foundation",
        "https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements.html/", "Current at access; IFRS 18 effective for annual periods beginning 1 January 2027", "standard",
        "Defines statement-of-financial-position presentation, comparatives, classification, offsetting and compliance boundaries."),
    src(3, "IFRS 13 Fair Value Measurement", "IFRS Foundation",
        "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-13-fair-value-measurement/", "Issued May 2011; current at access", "standard",
        "Defines fair value as an exit price and separates measurement framework from requirements to measure an item at fair value."),
    src(4, "IFRS Accounting Taxonomy 2025", "IFRS Foundation",
        "https://www.ifrs.org/issued-standards/ifrs-taxonomy/ifrs-accounting-taxonomy-2025/", "Published 27 March 2025; remains current for 2026 reporting", "schema",
        "Defines digital reporting concepts, instant monetary facts, statement-of-financial-position classifications and versioned validation relationships."),
    src(5, "Bank-to-Customer Cash Management Message Definition Report", "ISO 20022 Registration Authority",
        "https://www.iso20022.org/sites/default/files/documents/messages/mdr_part_2/ISO20022_MDRPart2_BankToCustomerCashManagement_2018_2019_v1_0.pdf", "Maintenance 2018-2019; approved 21 January 2019", "standard",
        "Defines account report and statement messages, booked and pending entries, balance information and account-owner or authorized-recipient boundaries."),
    src(6, "XBRL 2.1", "XBRL International",
        "https://specifications.xbrl.org/work-product-index-group-base-spec-base-spec.html", "Recommendation 20 February 2013; conformance suite 16 July 2025", "standard",
        "Defines facts, concepts, contexts, units, instant and duration periods, debit or credit balance attributes and validation."),
    src(7, "XBRL Link Role Registry", "XBRL International",
        "https://specifications.xbrl.org/registries/lrr-2.0/index.html", "Registry 2.0 current at access; accounting arcroles dated 4 January 2023", "registry",
        "Defines instant-to-flow and contra relationships used for rollforwards and accounting balance semantics."),
    src(8, "Integrated Balance of Payments and International Investment Position Manual Seventh Edition", "International Monetary Fund",
        "https://www.imf.org/-/media/Files/Data/Statistics/BPM6/draft-bpm7-wcv.ashx", "BPM7 white-cover pre-edited version March 2025", "public-authority",
        "Defines external financial positions, assets, liabilities, counterparties, currency breakdowns and stock-flow reconciliation."),
    src(9, "Government Finance Statistics Manual 2014", "International Monetary Fund",
        "https://www.imf.org/external/np/sta/gfsm/pdf/text14.pdf", "GFSM 2014", "public-authority",
        "Defines balance-sheet stocks, financial and nonfinancial assets, liabilities, net worth and economic versus legal ownership."),
    src(10, "Manual on MFI balance sheet statistics", "European Central Bank",
        "https://www.ecb.europa.eu/pub/pdf/other/ecb.manualmfibalancesheetstatistics202402~8e4fc2ccca.en.pdf", "February 2024", "public-authority",
        "Defines balance-sheet positions, transactions, reclassifications, exchange-rate and other valuation adjustments for monetary financial institutions."),
    src(11, "2026 XBRL Taxonomies Update", "United States Securities and Exchange Commission",
        "https://www.sec.gov/newsroom/whats-new/2603-2026-xbrl-taxonomies-update", "EDGAR release 26.1 supported 16 March 2026", "public-authority",
        "Pins current SEC-supported reporting taxonomy versions and compatibility constraints for a jurisdictional projection."),
    src(12, "LEI Common Data File Format 3.1", "Global Legal Entity Identifier Foundation",
        "https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-lei-cdf-3-1-format", "Version 3.1 published May 2021; current at access", "registry",
        "Defines authoritative legal-entity identity and reference data without making the position model own party identity."),
    src(13, "Global Financial Data Standards and ISO 4217 Currency Codes", "SIX Group",
        "https://www.six-group.com/en/products-services/financial-information/market-reference-data/data-standards.html", "ISO 4217 Maintenance Agency lists current at access", "registry",
        "Provides the authoritative maintained currency and funds code list, numeric codes and minor units."),
    src(14, "PROV-O: The PROV Ontology", "World Wide Web Consortium",
        "https://www.w3.org/TR/prov-o/", "W3C Recommendation 30 April 2013", "ontology",
        "Defines entity, activity, agent, attribution, derivation, revision and qualified provenance."),
    src(15, "Data on the Web Best Practices: Data Quality Vocabulary", "World Wide Web Consortium",
        "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note 15 December 2016", "ontology",
        "Defines quality dimensions, metrics, measurements, annotations, policies and certificates."),
    src(16, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force",
        "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339 July 2002, updated by RFC 9557", "standard",
        "Defines interoperable timestamps with seconds and explicit relationship to UTC."),
]


ROWS = [
    ("position-identity-boundary-subjects-and-authority", "Position identity, boundary, subjects and authority", "Identify one position assertion without absorbing accounts, instruments, parties or reports", [
        ("position-root-identity-version-scope-and-authority", "Position root identity, version, scope and authority", ["SRC-001", "SRC-004", "SRC-006", "SRC-008", "SRC-014"], [
            ("position-id-version-head-status-purpose-scope-and-owner", "Position ID, version, head, status, purpose, scope and owner", "identity", True),
            ("as-of-snapshot-granularity-materiality-authority-and-master-system", "As-of snapshot, granularity, materiality, authority and master system", "authority", True),
        ]),
        ("subject-account-portfolio-instrument-and-party-references", "Subject, account, portfolio, instrument and party references", ["SRC-001", "SRC-005", "SRC-008", "SRC-009", "SRC-010", "SRC-012"], [
            ("reporting-entity-holder-owner-beneficiary-issuer-counterparty-and-custodian", "Reporting entity, holder, owner, beneficiary, issuer, counterparty and custodian", "relationship", True),
            ("account-ledger-portfolio-fund-instrument-contract-lot-and-position-boundary", "Account, ledger, portfolio, fund, instrument, contract, lot and position boundary", "relationship", True),
        ]),
    ]),
    ("classification-quantity-monetary-measurement-and-balance-semantics", "Classification, quantity, monetary measurement and balance semantics", "Separate what is held or owed from how much it is worth and how the balance is labelled", [
        ("economic-accounting-risk-and-instrument-classification", "Economic, accounting, risk and instrument classification", ["SRC-001", "SRC-002", "SRC-004", "SRC-008", "SRC-009", "SRC-010"], [
            ("asset-liability-equity-claim-obligation-off-balance-and-exposure-class", "Asset, liability, equity, claim, obligation, off-balance and exposure class", "classification", True),
            ("current-noncurrent-maturity-liquidity-seniority-sector-residency-and-instrument-class", "Current, noncurrent, maturity, liquidity, seniority, sector, residency and instrument class", "classification", False),
        ]),
        ("quantity-amount-unit-currency-sign-and-balance-type", "Quantity, amount, unit, currency, sign and balance type", ["SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-010", "SRC-013"], [
            ("quantity-unit-lot-face-value-nominal-and-contractual-amount", "Quantity, unit, lot, face value, nominal and contractual amount", "measurement", True),
            ("monetary-amount-currency-multiplier-rounding-debit-credit-gross-and-net", "Monetary amount, currency, multiplier, rounding, debit, credit, gross and net", "measurement", True),
        ]),
    ]),
    ("recognition-availability-valuation-and-inputs", "Recognition, availability, valuation and inputs", "Explain why a position exists, what portion is usable and how any monetary value was determined", [
        ("recognition-ownership-control-availability-and-restrictions", "Recognition, ownership, control, availability and restrictions", ["SRC-001", "SRC-002", "SRC-005", "SRC-008", "SRC-009"], [
            ("recognition-derecognition-economic-ownership-legal-title-control-and-custody", "Recognition, derecognition, economic ownership, legal title, control and custody", "state", True),
            ("ledger-available-blocked-reserved-pledged-encumbered-frozen-and-collateralized", "Ledger, available, blocked, reserved, pledged, encumbered, frozen and collateralized", "state", False),
        ]),
        ("measurement-basis-price-rate-accrual-and-valuation-evidence", "Measurement basis, price, rate, accrual and valuation evidence", ["SRC-001", "SRC-003", "SRC-004", "SRC-006", "SRC-008", "SRC-010", "SRC-014"], [
            ("cost-carrying-fair-market-amortized-present-settlement-and-liquidation-value", "Cost, carrying, fair, market, amortized, present, settlement and liquidation value", "classification", True),
            ("price-source-fx-rate-accrual-interest-model-input-assumption-level-and-valuation-run", "Price source, FX rate, accrual, interest, model input, assumption, level and valuation run", "provenance", True),
        ]),
    ]),
    ("temporal-semantics-balance-types-movements-and-reconciliation", "Temporal semantics, balance types, movements and reconciliation", "Keep stock instants, flow periods and operational clocks distinct and traceable", [
        ("as-of-reference-trade-settlement-booking-and-knowledge-time", "As-of, reference, trade, settlement, booking and knowledge time", ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-010", "SRC-016"], [
            ("opening-closing-interim-current-forward-and-available-balance-time", "Opening, closing, interim, current, forward and available balance time", "temporal", True),
            ("trade-effective-settlement-booking-valuation-reporting-observation-ingestion-and-knowledge-time", "Trade, effective, settlement, booking, valuation, reporting, observation, ingestion and knowledge time", "temporal", True),
        ]),
        ("movements-rollforward-reconciliation-and-breaks", "Movements, rollforward, reconciliation and breaks", ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-010", "SRC-014"], [
            ("opening-addition-reduction-transfer-accrual-fx-price-volume-and-closing-rollforward", "Opening, addition, reduction, transfer, accrual, FX, price, volume and closing rollforward", "process", False),
            ("ledger-subledger-custodian-instrument-statement-reconciliation-break-and-adjustment", "Ledger, subledger, custodian, instrument, statement reconciliation, break and adjustment", "validation", True),
        ]),
    ]),
    ("exposure-risk-quality-estimates-provenance-and-correction", "Exposure, risk, quality, estimates, provenance and correction", "Qualify risk and fitness claims without turning the record into a risk engine or audit log", [
        ("exposure-netting-concentration-allowance-and-uncertainty", "Exposure, netting, concentration, allowance and uncertainty", ["SRC-001", "SRC-003", "SRC-008", "SRC-009", "SRC-010", "SRC-015"], [
            ("gross-net-exposure-netting-set-counterparty-collateral-haircut-and-concentration", "Gross, net exposure, netting set, counterparty, collateral, haircut and concentration", "measurement", False),
            ("impairment-provision-allowance-reserve-uncertainty-confidence-and-sensitivity", "Impairment, provision, allowance, reserve, uncertainty, confidence and sensitivity", "quality", False),
        ]),
        ("source-quality-estimate-revision-restatement-and-audit", "Source, quality, estimate, revision, restatement and audit", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-010", "SRC-014", "SRC-015"], [
            ("source-evidence-method-actor-system-quality-dimension-metric-and-limitation", "Source, evidence, method, actor, system, quality dimension, metric and limitation", "evidence", True),
            ("estimate-provisional-adjusted-corrected-revised-restated-superseded-and-retracted", "Estimate, provisional, adjusted, corrected, revised, restated, superseded and retracted", "lifecycle", True),
        ]),
    ]),
    ("lifecycle-reporting-access-retention-and-interoperability", "Lifecycle, reporting, access, retention and interoperability", "Govern publication and projections without confusing a position with its report or transport", [
        ("lifecycle-approval-disclosure-access-and-records", "Lifecycle, approval, disclosure, access and records", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-011", "SRC-014"], [
            ("captured-validated-reconciled-approved-reported-restated-closed-and-superseded", "Captured, validated, reconciled, approved, reported, restated, closed and superseded", "lifecycle", True),
            ("confidentiality-purpose-access-embargo-license-retention-legal-hold-tombstone-and-audit", "Confidentiality, purpose, access, embargo, license, retention, legal hold, tombstone and audit", "access", True),
        ]),
        ("statement-regulatory-message-and-linked-data-projections", "Statement, regulatory, message and linked-data projections", [f"SRC-{i:03d}" for i in range(1, 17)], [
            ("financial-statement-line-account-report-regulatory-return-and-analytical-view-binding", "Financial statement line, account report, regulatory return and analytical view binding", "interoperability", True),
            ("ifrs-iso20022-xbrl-imf-ecb-sec-lei-currency-prov-dqv-and-time-projection", "IFRS, ISO 20022, XBRL, IMF, ECB, SEC, LEI, currency, PROV, DQV and time projection", "interoperability", True),
        ]),
    ]),
]

KINDS = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def finding(item, n, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(n + 6) % len(KINDS)], KINDS[(n + 15) % len(KINDS)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {low} as source-qualified position context while account, instrument, party, transaction, journal, valuation, statement, policy, audit and records masters remain independently identifiable.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What stable identity, position version, class, amount or quantity, unit, scope and explicit unknown establish {low}?", "kind": kinds[0], "answer_data": ["position, subject, account, instrument and external master identifiers", "typed quantity or amount, currency or unit, classification, valuation and schema version", "unknown, disputed, estimated, provisional, restricted and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who owns, holds, controls, custodies, measures, asserts, reviews, approves, reports or may use {low}, for which purpose and under what authority?", "kind": kinds[1], "answer_data": ["reporting entity, holder, owner, issuer, counterparty, custodian, actor and system", "purpose, accounting or statistical basis, authority, policy, access, confidentiality and retention", "conflict, exception, escalation, segregation of duties and accountability"]},
            {"id": f"{fid}-q03", "text": f"Which as-of, trade, effective, settlement, booking, valuation, reporting, observation, ingestion and knowledge times, source, method and uncertainty qualify {low}?", "kind": kinds[2], "answer_data": ["distinct stock, flow, operational, reporting and knowledge times", "source, method, valuation run, evidence, quality, confidence and limitation", "movement, correction, restatement, successor, legal hold and audit"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed position data for {low}, qualified by subject, version, as-of time, unit, basis, authority, uncertainty and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned position evidence for {low}.", "media_or_form": ["logical financial-position specification assertion", "snapshot, classification, quantity, valuation, restriction, movement, reconciliation, quality, correction, approval or projection record"], "serial": True, "identity_strategy": f"Position ID plus independent position version, subject and account or instrument references, as-of time, valuation or reporting basis and artifact kind for {fid}; an amount, date, label, account number or digest never identifies a position alone.", "source_refs": refs}],
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
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified financial-position context for {lname.lower()}.", "source_refs": refs, "findings": fs})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed financial-position context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({r for layer in layers for r in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-position", "Register a financial position", ["owner", "purpose", "subject and position boundary"], ["stable position and version head"], ["namespace, identity, authority, subject, account or instrument and duplicate checks pass"], ["a position aggregate exists without posting a transaction or creating an account"], ["SRC-001", "SRC-004", "SRC-006", "SRC-014"]),
    ("capture-position-snapshot", "Capture a position snapshot", ["position head", "quantity or amount", "as-of time and source"], ["successor position snapshot"], ["subject, key, class, unit, time, basis, source, status and expected revision checks pass"], ["a qualified snapshot is appended without rewriting history"], ["SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-010"]),
    ("bind-parties-accounts-instruments-and-portfolios", "Bind parties, accounts, instruments and portfolios", ["position", "external master identifiers", "relationship authority"], ["non-owning relationship set"], ["role, direction, cardinality, validity, provenance and master-system checks pass"], ["external lifecycles remain authoritative"], ["SRC-001", "SRC-005", "SRC-008", "SRC-009", "SRC-012"]),
    ("classify-and-recognize-position", "Classify and recognize or derecognize a position", ["position", "classification and recognition basis", "authorized decision"], ["successor classification or recognition assertion"], ["scheme, version, reporting basis, evidence, authority and effective-time checks pass"], ["classification and recognition do not post entries or alter external masters"], ["SRC-001", "SRC-002", "SRC-004", "SRC-008", "SRC-009"]),
    ("record-quantity-and-valuation", "Record quantity and monetary valuation", ["position", "quantity and unit", "valuation basis and inputs"], ["qualified measurement assertion"], ["currency, unit, price, FX rate, multiplier, rounding, basis, method, run, uncertainty and source checks pass"], ["quantity and valuation stay separate and no rate or fair value is autonomously approved"], ["SRC-001", "SRC-003", "SRC-004", "SRC-006", "SRC-013"]),
    ("record-availability-and-encumbrance", "Record availability and encumbrance", ["position", "restriction assertion", "external authority"], ["qualified availability state"], ["restriction type, amount, priority, beneficiary, legal basis, effective interval and evidence checks pass"], ["legal title, economic ownership, custody and usability remain distinct"], ["SRC-001", "SRC-005", "SRC-008", "SRC-009"]),
    ("record-movement-and-rollforward", "Record movement and rollforward bindings", ["opening and closing positions", "transaction or adjustment references", "rollforward basis"], ["movement bridge and exception evidence"], ["stock, flow, currency, unit, sign, event type, time, source and completeness checks pass"], ["the model binds movements but does not post, settle or recalculate them"], ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-010"]),
    ("reconcile-assess-quality-and-correct", "Reconcile, assess quality and correct", ["position version", "comparison source and quality rules", "authorized correction decision"], ["reconciliation result, quality assertion and successor correction"], ["scope, tolerance, metric, source, reason, authority, revision, evidence and audit checks pass"], ["breaks and corrections are appended without silently rewriting issued values"], ["SRC-004", "SRC-005", "SRC-006", "SRC-010", "SRC-014", "SRC-015"]),
    ("approve-report-restate-or-supersede", "Approve, report, restate or supersede a position", ["position head", "review evidence", "authorized lifecycle decision"], ["successor lifecycle and reporting assertion"], ["expected revision, approval, reporting basis, materiality, disclosure, effective time and retention checks pass"], ["position lifecycle remains distinct from statement and filing lifecycles"], ["SRC-001", "SRC-002", "SRC-004", "SRC-011", "SRC-014"]),
    ("query-project-retain-and-audit", "Query, project, retain and audit", ["position", "target profile", "purpose-bound access and records policy"], ["filtered projection, retention result or audit event"], ["purpose, authority, mapping, loss, confidentiality, hold, digest and retention checks pass"], ["restricted financial data stays governed and projections declare loss"], [f"SRC-{i:03d}" for i in range(1, 17)]),
]


def functions():
    return [{"id": x[0], "name": x[1], "description": f"Governed operation to {x[1].lower()} without autonomous posting, settlement, reclassification, netting, valuation approval, impairment, write-off, restatement, disclosure, certification, access widening or records disposition.", "inputs": x[2], "outputs": x[3], "preconditions": x[4], "effects": x[5], "source_refs": x[6]} for x in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner, namespace authority, financial governance mandate and accountable position owner", "Authoritative Party, Account, Ledger, Portfolio, Instrument, Contract, Transaction, Journal, Valuation, Price, FX Rate, Statement, Filing, Policy, Audit and Records registries", "Approved accounting, statistical, regulatory, currency, unit, taxonomy, valuation, reconciliation, privacy, access, retention and interoperability profiles", "Role, delegation, segregation-of-duties, approval, reporting, correction, restatement, withdrawal and agent-operation policies"],
            "namespace_guidance": "Mint position, position-version, snapshot, quantity, valuation, restriction, movement, reconciliation, quality, correction, approval and projection IDs; preserve every external master identifier.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize a position by authoritative position identifier, owner namespace, subject, account or instrument scope, position class, reporting or valuation basis and as-of time, never by amount, title, date or digest alone.", "Keep position, account, instrument, party, transaction, journal entry, valuation, financial statement, filing, audit and records independently identifiable."],
            "patch_rules": ["Extensions declare identity, classification, quantity, valuation, temporal, restriction, risk, quality, access, lifecycle and interoperability effects.", "Reported or approved snapshots are immutable; changes create linked successors or explicit new measurement or reporting bases with reason, compatibility, migration and review.", "Never silently change subject, account, instrument, class, amount, quantity, currency, unit, sign, as-of time, recognition, valuation basis, source, restriction, netting or quality state."],
            "compatibility_rules": ["Ignore additive fields only when identity, subject, classification, amount, unit, time, basis, authority, access and provenance survive.", "Every projection pins standard, taxonomy, message, currency-list and mapping versions and declares aggregation, precision, timing and semantic loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each position, snapshot, valuation, reconciliation, correction, approval or artifact, qualified by issuer, namespace and record kind.", "Governed globally resolvable position IRI.", "Dimension UUID or ULID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish as-of, trade, effective, settlement, booking, valuation, reporting, observation, ingestion and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {position-id}--{position-version}--{as-of-time}--{valuation-or-reporting-basis}--{artifact-kind}.",
            "integrity_rule": "Store digest, media type, record kind, subject and account or instrument scope, amount and unit, taxonomy and policy versions, actor, distinct event and knowledge times, confidentiality marking and provenance."},
        "policies": ["The position owns time-bound quantitative assertions, qualifiers, versions and projections but not external account, instrument, party, transaction, journal, valuation-run, statement, filing, policy, audit or records masters.", "A balance is qualified by subject, scope, class, unit, as-of time, recognition and valuation basis, restrictions, source and provenance; it is not timeless ground truth.", "Legal title, economic ownership, control, custody, availability and collateral status must remain distinguishable.", "Agents cannot autonomously post, settle, reclassify, net, value, impair, write off, restate, disclose, certify, widen access or dispose financial records without delegated authority."],
        "crud": {
            "read": ["Resolve position head, subject, account or instrument, class, amount, quantity, unit, time, recognition, valuation, restriction, movement, reconciliation, quality, lifecycle, access and projection loss under the permitted view."],
            "create": ["Bind stable identity, owner, purpose, subject, account or instrument, position class, unit, as-of time, measurement or reporting basis, source authority and initial lifecycle before accepting a snapshot."],
            "update": ["Append successor snapshots, classifications, valuations, restrictions, movement links, reconciliations, quality assertions, corrections, approvals, restatements and lifecycle events with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply legal hold, financial-record, regulatory, audit, privacy and adopting-Dimension retention policy; withdraw or tombstone only the catalog view without cascading to external masters, and let authoritative systems execute physical disposition."]},
        "roles": [
            {"name": "Position owner", "responsibilities": ["Own purpose, scope, reporting basis, lifecycle, compatibility and accountable use."]},
            {"name": "Account or portfolio steward", "responsibilities": ["Own account, portfolio and ledger references, position keys, balance types and reconciliation scope."]},
            {"name": "Instrument and reference-data steward", "responsibilities": ["Own instrument, issuer, counterparty, currency, unit, classification and identifier references."]},
            {"name": "Valuation and risk authority", "responsibilities": ["Own measurement bases, prices, FX rates, models, assumptions, uncertainty, exposures, allowances and approvals."]},
            {"name": "Controller and quality reviewer", "responsibilities": ["Own recognition, classification, materiality, rollforward, reconciliation, exceptions, corrections and restatements."]},
            {"name": "Access, regulatory and records authority", "responsibilities": ["Own disclosure, confidentiality, purpose, access, filing, embargo, retention, legal hold and disposition policy."]},
            {"name": "Interoperability steward", "responsibilities": ["Own taxonomy and message versions, currency code lists, mappings, conformance evidence and declared loss."]}],
        "access": {
            "default_rule": "Deny unreleased, confidential, personal, market-sensitive, account-level, counterparty, valuation-input, collateral, netting, risk, regulatory or reconstruction-capable data unless a purpose-bound policy permits the minimum necessary view.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Declared regulatory, accounting, risk, audit, legal, incident or subject-rights access must cite authority, scope, purpose and time limit and must be logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, position and version, operation, authority, policy, RFC 3339 time, affected measurements or references, source revision and outcome without duplicating restricted financial data."]},
        "agents_bootstrap": {
            "filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read Dimension financial governance, namespace, accounting or statistical basis, taxonomy, valuation, privacy, access, retention and agent policies.", "Read this position and linked party, account, ledger, portfolio, instrument, transaction, journal, valuation, statement, filing, audit and records models before mutation."]},
    }


def coverage():
    dims = ["identity", "classification and direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability", "authority and ethics"]
    return {
        "claim": "Covers one governed financial position or balance from identity and subject scope through classification, quantity, monetary amount, recognition, availability, valuation, time, movement, reconciliation, exposure, quality, correction, lifecycle, access, reporting and projections.",
        "confidence": "medium",
        "checklist": [{"dimension": d, "status": "covered" if d != "spatial" else "not-applicable", "notes": ("Spatial properties are not intrinsic; jurisdiction, market, branch, custody and asset locations remain references when relevant." if d == "spatial" else f"{d.capitalize()} is explicit; accounting, statistical, regulatory, valuation, risk, jurisdiction and external-review profiles remain held where applicable.")} for d in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "The candidate WM-ECO-015 parent and WM-ECO-004 reference plus incoming WM-ECO-018 composition remain unapproved relation-ledger proposals.", "Banking capital, insurance solvency, derivatives margin, securities settlement, tax, treasury, fund accounting, crypto assets and jurisdiction-specific filings require separate profiles.", "IFRS text and taxonomy are used only within their public licensing and access boundaries; no restricted clause was inferred.", "BPM7 is cited as the March 2025 white-cover pre-edited version and must be repinned when the final edited publication is adopted."],
        "conflicts": ["Financial position, account balance, statement of financial position, instrument holding, exposure, journal balance and regulatory return are related but not interchangeable identities.", "Quantity, nominal amount, carrying amount, fair value, market value, available balance and risk exposure require distinct measures and bases.", "Legal title, economic ownership, control, custody, availability, pledge, collateral and netting rights require distinct relationships or states.", "Stock at an instant, flow during a period, transaction date, settlement date, booking time, valuation time, report time and knowledge time must not be collapsed."],
        "regional_assumptions": ["Recognition, valuation, offsetting, presentation, prudential treatment, disclosure, confidentiality, retention and certification depend on framework, jurisdiction, regulator, entity and reporting period.", "IFRS, ISO 20022, XBRL, IMF, ECB and SEC are overlapping accounting, messaging, statistical, central-bank and filing profiles; none is universal."],
        "adversarial_checks": ["Reject a package that collapses a position into its account, instrument, transaction, journal entry, valuation or financial statement.", "Reject an amount without subject and scope, position class, currency or unit, as-of time, measurement or reporting basis, source and provenance.", "Reject silent netting, offsetting, unit conversion, FX translation, valuation, impairment, correction, restatement or exposure calculation.", "Reject a timestamp without seconds and explicit offset or Z, or a model that collapses event and knowledge time.", "Reject autonomous posting, settlement, reclassification, valuation approval, disclosure, certification, access widening or records disposition.", "Reject a projection that hides taxonomy, currency-list, precision, dimensions, sign, balance type, basis, restrictions, provenance or information loss."]}


def build():
    model = {
        "registry_id": "vr.wm-eco-017", "model_id": "WM-ECO-017", "name": "Financial Position / Balance", "entry_kind": "aggregate",
        "purpose": "Represent one governed, time-bound asset, liability, equity, holding, account-balance or exposure position so agents can interpret what is held or owed, by whom, how much, at what time and on which basis without confusing the position with its account, instrument, transaction, valuation or report.",
        "scope_statement": "Owns position identity, versions, class and lifecycle; subject, holder, reporting entity, account, ledger, portfolio, fund, instrument, issuer, counterparty and custodian references; quantity, amount, unit, currency, sign and balance type; recognition, ownership, control, availability, restrictions and encumbrances; measurement and valuation bases, inputs, prices, FX rates, accruals, assumptions and uncertainty; as-of, trade, settlement, booking, valuation, reporting, observation, ingestion and knowledge times; movement and rollforward bindings; reconciliation, exposure, risk, quality, correction and restatement evidence; access, retention and version-pinned reporting and interoperability projections. External party, account, instrument, transaction, journal, valuation-run, statement, filing, policy, audit and records masters remain independently authoritative.",
        "in_scope": ["Position identity, subject and account or instrument scope, classification, quantity, monetary amount, currency, unit, sign, balance type, recognition, availability and valuation", "Multiple time axes, movements, reconciliation, exposure qualifiers, quality, corrections, lifecycle, access, reporting bindings and interoperability projections"],
        "out_of_scope": ["Owning Party, Financial Account, Ledger, Portfolio, Fund, Money or Instrument, Contract, Transaction, Journal Entry, Valuation Run, Financial Statement, Filing, Policy, Audit or Records masters", "Treating a reported amount as timeless ground truth or collapsing quantity, carrying amount, fair value, available balance and risk exposure", "Autonomous posting, settlement, reclassification, netting, valuation approval, impairment, write-off, restatement, disclosure, certification, access widening or physical records disposition"],
        "boundary_notes": [
            {"neighbor": "WM-ECO-015 Financial Account", "distinction": "The candidate parent owns account identity, parties, currency, state and operating rules. The position owns a time-bound measured balance or holding and stores a non-owning account reference.", "source_refs": ["SRC-005", "SRC-006", "SRC-014"]},
            {"neighbor": "WM-ECO-004 Money / Instrument", "distinction": "The candidate reference owns the currency, monetary unit or transferable instrument identity. The position owns subject, amount or quantity, basis and as-of state.", "source_refs": ["SRC-005", "SRC-008", "SRC-013"]},
            {"neighbor": "WM-ECO-018 Financial Statement", "distinction": "A statement is a governed report over entities, accounts, classifications and a reporting period. A position is one time-bound quantitative assertion that a statement line may aggregate or present.", "source_refs": ["SRC-002", "SRC-004", "SRC-006"]},
            {"neighbor": "Transaction, journal entry, valuation and reconciliation", "distinction": "Transactions and entries are flows or postings, valuation is a governed measurement activity, and reconciliation is a comparison process. The position binds their outputs and evidence without executing them.", "source_refs": ["SRC-001", "SRC-003", "SRC-005", "SRC-007", "SRC-008", "SRC-010", "SRC-014"]},
            {"neighbor": "IFRS, ISO 20022, XBRL, IMF, ECB, SEC, GLEIF, ISO 4217, PROV, DQV and RFC profiles", "distinction": "Each source has distinct scope and normative force. Every mapping is version-pinned, jurisdiction-qualified and loss-declaring.", "source_refs": [f"SRC-{i:03d}" for i in range(1, 17)]}],
    }
    composition = [
        {"target": "WM-ECO-015", "relation": "REFERENCE", "purpose": "Resolve the candidate Financial Account parent while keeping account identity, parties, currency, state and rules external.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-014"]},
        {"target": "WM-ECO-004", "relation": "REFERENCE", "purpose": "Resolve currency, monetary unit or instrument identity while retaining position-specific subject, quantity, amount, basis and as-of state.", "required": True, "source_refs": ["SRC-005", "SRC-008", "SRC-013"]},
        {"target": "WM-ECO-018", "relation": "REFERENCE", "purpose": "Allow a Financial Statement to compose or aggregate positions without making the position own statement presentation or filing lifecycle.", "required": False, "source_refs": ["SRC-002", "SRC-004", "SRC-006"]},
        {"target": "Party, Ledger, Portfolio, Fund, Contract, Transaction, Journal Entry, Valuation, Price, FX Rate, Reconciliation, Filing, Policy, Audit and Records models", "relation": "REFERENCE", "purpose": "Resolve authoritative external identities, operations, decisions and evidence without duplicating their lifecycles.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-005", "SRC-008", "SRC-009", "SRC-010", "SRC-012", "SRC-014"]},
        {"target": "IFRS 2026 and Accounting Taxonomy 2025, ISO 20022 cash management, XBRL 2.1, IMF BPM7 and GFSM 2014, ECB MFI 2024, SEC 2026, LEI-CDF 3.1, ISO 4217, PROV-O, DQV and RFC 3339", "relation": "ALIGN", "purpose": "Project version-pinned accounting, messaging, digital-reporting, statistical, regulatory, identity, currency, provenance, quality and time views with declared loss.", "required": False, "source_refs": [f"SRC-{i:03d}" for i in range(1, 17)]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
