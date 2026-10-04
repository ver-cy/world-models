#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-FLW-012."""

import importlib.util
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
BASE_PATH = RUN.parent / "wm-flw-010" / "build_codex_result.py"
SPEC = importlib.util.spec_from_file_location("wm_flw_010_builder", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
AT = "2026-09-06T21:05:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "EPCIS Standard", "GS1", "https://ref.gs1.org/standards/epcis/2.0.1/", "EPCIS 2.0.1, 1 July 2025", "standard", "Defines visibility events, object and quantity scope, event and record clocks, locations, sources, destinations and corrections."),
    src(2, "EPCIS ObjectEvent linked-data definition", "GS1", "https://ref.gs1.org/epcis/ObjectEvent", "EPCIS linked-data model accessed 2026-09-06", "ontology", "Defines instance and class-level object observations, quantities, actions, business steps, dispositions and endpoints."),
    src(3, "EPCIS AggregationEvent linked-data definition", "GS1", "https://ref.gs1.org/epcis/AggregationEvent", "EPCIS linked-data model accessed 2026-09-06", "ontology", "Defines parent-child aggregation changes used as evidence for handling-unit composition."),
    src(4, "EPCIS TransformationEvent linked-data definition", "GS1", "https://ref.gs1.org/epcis/TransformationEvent", "EPCIS linked-data model accessed 2026-09-06", "ontology", "Separates transformation inputs and outputs from ordinary relocation or stock transfer."),
    src(5, "Core Business Vocabulary Standard", "GS1", "https://ref.gs1.org/standards/cbv/2.0.0/", "CBV 2.0.0, June 2022", "standard", "Defines controlled business steps and dispositions including shipping, receiving, storing, picking and stocking."),
    src(6, "GS1 Global Traceability Standard", "GS1", "https://ref.gs1.org/standards/global-traceability/2.0.0/", "Release 2.0, August 2017", "standard", "Defines critical tracking events and key data elements for traceability across supply chains."),
    src(7, "Universal Business Language Version 2.4", "OASIS Open", "https://docs.oasis-open.org/ubl/os-UBL-2.4/UBL-2.4.html", "OASIS Standard, 20 June 2024", "standard", "Defines inventory, despatch and receipt document structures and fulfilment business rules."),
    src(8, "UBL 2.4 Inventory Report schema", "OASIS Open", "https://docs.oasis-open.org/ubl/os-UBL-2.4/mod/summary/reports/UBL-InventoryReport-2.4.html", "UBL 2.4, 20 June 2024", "schema", "Defines inventory-report lines, quantities, periods, locations and item references."),
    src(9, "UBL 2.4 Receipt Advice schema", "OASIS Open", "https://docs.oasis-open.org/ubl/os-UBL-2.4/mod/summary/reports/UBL-ReceiptAdvice-2.4.html", "UBL 2.4, 20 June 2024", "schema", "Supports receipt confirmation, received, short and rejected quantities and rejection reasons."),
    src(10, "UBL 2.4 Despatch Advice schema", "OASIS Open", "https://docs.oasis-open.org/ubl/os-UBL-2.4/mod/summary/reports/UBL-DespatchAdvice-2.4.html", "UBL 2.4, 20 June 2024", "schema", "Supports full and partial despatch, order-line references and transport handling units."),
    src(11, "UN/EDIFACT code list 4501 Inventory movement direction", "UN/CEFACT", "https://service.unece.org/trade/uncefact/vocabulary/uncl4501/", "UNCL 4501 vocabulary accessed 2026-09-06", "classifier", "Distinguishes movement into inventory from movement out of inventory."),
    src(12, "UN/EDIFACT data element 4499 Inventory movement reason", "UN/CEFACT", "https://service.unece.org/trade/untdid/d21a/tred/tred4499.htm", "D.21A", "classifier", "Defines coded reasons for inventory movement."),
    src(13, "UN/EDIFACT data element 4503 Inventory balance method", "UN/CEFACT", "https://service.unece.org/trade/untdid/d21a/tred/tred4503.htm", "D.21A", "classifier", "Defines methods used to establish inventory balance."),
    src(14, "UN/EDIFACT data element 6063 Quantity type code qualifier", "UN/CEFACT", "https://service.unece.org/trade/untdid/d21a/tred/tred6063.htm", "D.21A", "classifier", "Includes inventory movement, opening balance, closing balance and replenishment quantity semantics."),
    src(15, "Recommendation No. 20 Codes for Units of Measure", "UN/CEFACT", "https://unece.org/trade/uncefact/cl-recommendations", "Recommendation 20 and current code lists accessed 2026-09-06", "classifier", "Defines coded units required for interoperable inventory quantities and measurements."),
    src(16, "UN/CEFACT Core Component Library", "UN/CEFACT", "https://unece.org/trade/uncefact/core-component-library", "Current CCL overview accessed 2026-09-06", "standard", "Provides syntax-neutral reusable business information components for supply-chain exchange."),
    src(17, "ISA-95 Standard: Enterprise-Control System Integration", "International Society of Automation", "https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard", "ISA-95 series overview accessed 2026-09-06", "standard", "Defines abstract information exchange boundaries between enterprise and manufacturing control functions."),
    src(18, "IEC 62264-2:2013 Enterprise-control system integration", "International Electrotechnical Commission", "https://webstore.iec.ch/en/publication/6675", "IEC 62264-2:2013", "standard", "Defines object and attribute models for enterprise-control integration, including material information exchanges."),
    src(19, "RFC 3339 Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines timestamps with seconds and explicit numeric offsets or Z."),
    src(20, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines activities, entities, agents, attribution, derivation, revision and invalidation."),
    src(21, "Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note, 15 December 2016", "ontology", "Defines quality measurements, annotations, policies and provenance."),
    src(22, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties and constraints for governed data use."),
    src(23, "XML Schema Part 2: Datatypes Second Edition", "World Wide Web Consortium", "https://www.w3.org/TR/xmlschema-2/", "W3C Recommendation, 28 October 2004", "standard", "Defines decimal, dateTime and datatype semantics used by standards projections."),
    src(24, "ISO 8000-110:2021 Data quality", "International Organization for Standardization", "https://www.iso.org/standard/80264.html", "ISO 8000-110:2021", "standard", "Provides master-data exchange requirements relevant to identifiers, provenance and quality declarations."),
]


ROWS = [
    ("identity-class-and-posting-boundary", "Identity, class and posting boundary", "Separate one inventory-movement assertion from its request, execution, observation, posting and resulting balances.", [
        ("movement-identity-revision-idempotency-and-lineage", "Movement identity, revision, idempotency and lineage", ["SRC-001", "SRC-019", "SRC-020", "SRC-024"], [
            ("movement-identifier-namespace-version-and-deduplication-key", "Movement identifier, namespace, version and deduplication key", "identity"),
            ("original-correction-reversal-successor-split-and-merge-lineage", "Original, correction, reversal, successor, split and merge lineage", "provenance"),
        ]),
        ("movement-class-direction-reason-and-authority", "Movement class, direction, reason and authority", ["SRC-005", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-017", "SRC-018"], [
            ("receipt-issue-transfer-adjustment-return-consumption-and-output-class", "Receipt, issue, transfer, adjustment, return, consumption and output class", "classification"),
            ("planned-physical-observed-posted-and-reconciled-assertion-kind", "Planned, physical, observed, posted and reconciled assertion kind", "classification"),
        ]),
    ]),
    ("stock-subject-quantity-and-measurement", "Stock subject, quantity and measurement", "Bind the stock subject and qualified amount without importing product, lot, unit or inventory-position masters.", [
        ("item-lot-serial-and-handling-unit-scope", "Item, lot, serial and handling-unit scope", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-006", "SRC-007", "SRC-010", "SRC-016", "SRC-018"], [
            ("product-material-item-lot-batch-and-serial-reference", "Product, material, item, lot, batch and serial reference", "relationship"),
            ("handling-unit-container-package-and-aggregation-scope", "Handling unit, container, package and aggregation scope", "composition"),
        ]),
        ("quantity-unit-precision-and-value-context", "Quantity, unit, precision and value context", ["SRC-001", "SRC-002", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-014", "SRC-015", "SRC-021", "SRC-023"], [
            ("moved-received-issued-rejected-short-and-damaged-quantity", "Moved, received, issued, rejected, short and damaged quantity", "measurement"),
            ("unit-precision-tolerance-conversion-base-and-alternate-measure", "Unit, precision, tolerance, conversion, base and alternate measure", "measurement"),
        ]),
    ]),
    ("source-destination-and-stock-state", "Source, destination and stock state", "Represent the asserted transition between location and stock buckets while positions and balances remain external.", [
        ("source-destination-location-and-position-binding", "Source, destination, location and position binding", ["SRC-001", "SRC-002", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-016"], [
            ("site-warehouse-zone-bin-virtual-location-and-read-point", "Site, warehouse, zone, bin, virtual location and read point", "spatial"),
            ("source-destination-stock-position-and-balance-reference", "Source, destination, stock-position and balance reference", "relationship"),
        ]),
        ("owner-custodian-status-and-condition-transition", "Owner, custodian, status and condition transition", ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007", "SRC-011", "SRC-012", "SRC-016"], [
            ("owner-custodian-possession-control-and-responsibility-binding", "Owner, custodian, possession, control and responsibility binding", "ownership"),
            ("available-reserved-blocked-quarantine-quality-and-disposition-change", "Available, reserved, blocked, quarantine, quality and disposition change", "state"),
        ]),
    ]),
    ("trigger-execution-lifecycle-and-time", "Trigger, execution, lifecycle and time", "Keep commercial and operational triggers, execution evidence, posting state and clocks independently attributable.", [
        ("request-order-reservation-task-and-process-trigger", "Request, order, reservation, task and process trigger", ["SRC-005", "SRC-007", "SRC-009", "SRC-010", "SRC-016", "SRC-017", "SRC-018", "SRC-020"], [
            ("order-fulfilment-reservation-warehouse-task-and-shipment-reference", "Order, fulfilment, reservation, warehouse-task and shipment reference", "relationship"),
            ("production-consumption-output-return-adjustment-and-count-trigger", "Production, consumption, output, return, adjustment and count trigger", "process"),
        ]),
        ("lifecycle-state-clock-and-posting", "Lifecycle, state, clock and posting", ["SRC-001", "SRC-002", "SRC-005", "SRC-007", "SRC-009", "SRC-010", "SRC-017", "SRC-018", "SRC-019", "SRC-020"], [
            ("requested-planned-released-executing-completed-failed-and-cancelled-state", "Requested, planned, released, executing, completed, failed and cancelled state", "lifecycle"),
            ("planned-effective-event-observation-record-posting-and-correction-time", "Planned, effective, event, observation, record, posting and correction time", "temporal"),
        ]),
    ]),
    ("evidence-exceptions-and-reconciliation", "Evidence, exceptions and reconciliation", "Make movement assertions auditable and reconcile disagreements without overwriting source-qualified facts.", [
        ("execution-evidence-observation-and-document", "Execution evidence, observation and document", ["SRC-001", "SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-009", "SRC-010", "SRC-020", "SRC-021", "SRC-024"], [
            ("scan-count-sensor-observation-operator-confirmation-and-proof", "Scan, count, sensor observation, operator confirmation and proof", "evidence"),
            ("receipt-despatch-transfer-posting-and-adjustment-document-reference", "Receipt, despatch, transfer, posting and adjustment document reference", "evidence"),
        ]),
        ("exception-conflict-and-reconciliation", "Exception, conflict and reconciliation", ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-014", "SRC-020", "SRC-021", "SRC-024"], [
            ("shortage-excess-damage-mismatch-partial-and-failed-movement", "Shortage, excess, damage, mismatch, partial and failed movement", "exception"),
            ("source-destination-shipment-count-ledger-and-balance-reconciliation", "Source, destination, shipment, count, ledger and balance reconciliation", "validation"),
        ]),
    ]),
    ("governance-access-and-interoperability", "Governance, access and interoperability", "Control authority, audit and standards projection while disclosing profile limits and information loss.", [
        ("roles-authority-controls-access-and-retention", "Roles, authority, controls, access and retention", ["SRC-017", "SRC-018", "SRC-020", "SRC-021", "SRC-022", "SRC-024"], [
            ("requester-executor-observer-poster-approver-and-reconciler-role", "Requester, executor, observer, poster, approver and reconciler role", "authority"),
            ("segregation-of-duties-access-retention-legal-hold-and-audit", "Segregation of duties, access, retention, legal hold and audit", "access"),
        ]),
        ("standards-crosswalk-quality-and-loss", "Standards crosswalk, quality and loss", ["SRC-001", "SRC-002", "SRC-005", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019", "SRC-020", "SRC-021", "SRC-022", "SRC-023", "SRC-024"], [
            ("gs1-ubl-uncefact-isa95-iec62264-and-unit-crosswalk", "GS1, UBL, UN/CEFACT, ISA-95, IEC 62264 and unit crosswalk", "interoperability"),
            ("source-profile-version-quality-confidence-license-and-semantic-loss", "Source profile, version, quality, confidence, license and semantic loss", "quality"),
        ]),
    ]),
]


KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 8) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 17) % len(KIND_CYCLE)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {lower} as typed Inventory Movement context while stock position, product, location, order, task, shipment, ledger, document and evidence retain external mastership.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which movement identity, class, revision, stock subject, quantity, location transition, clocks and source establish {lower}?", "kind": kinds[0], "answer_data": ["movement identifier, namespace, assertion kind, revision and idempotency key", "item, lot, serial, handling-unit, source and destination position references", "quantity, unit, precision, event time, posting time, source profile and confidence"]},
            {"id": f"{fid}-q02", "text": f"Who requests, executes, observes, posts, approves, owns, holds, corrects, reconciles or may access {lower}, and under which authority?", "kind": kinds[1], "answer_data": ["requester, executor, observer, poster, approver, owner, custodian, steward and reconciler roles", "order, reservation, task, production, shipment, policy, jurisdiction and segregation-of-duties basis", "assertion owner, master system, reviewer, correction actor and disputed state"]},
            {"id": f"{fid}-q03", "text": f"Which lifecycle state, evidence, exception, reconciliation, uncertainty and lineage qualify {lower}?", "kind": kinds[2], "answer_data": ["requested, planned, released, executing, completed, posted, failed, cancelled, reversed and corrected state", "scan, count, observation, document, posting, balance and shipment evidence references", "shortage, excess, damage, mismatch, tolerance, conflict, correction, successor and semantic-loss declaration"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed movement-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Digest-addressed manifest of movement assertions, references, observations, postings, conflicts and corrections supporting {lower}.", "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative inventory or warehouse master-system movement identifier first, otherwise governed IRI, then Dimension UUID or ULID; include immutable revision and digest.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


BASE.SOURCES = SOURCES
BASE.ROWS = ROWS
BASE.KIND_CYCLE = KIND_CYCLE
BASE.make_finding = make_finding


FUNCTION_ROWS = [
    ("register-movement", "Register inventory movement", "Create one governed movement identity and immutable initial assertion.", ["movement class", "stock subject", "source and authority"], ["movement identifier", "initial revision"], ["active Dimension", "create authority"], ["identity, boundary and unknowns are appended"], ["SRC-001", "SRC-011", "SRC-019", "SRC-020", "SRC-024"]),
    ("classify-movement", "Classify movement", "Record direction, reason, assertion kind and industry profile without changing execution or ledger state.", ["movement identifier", "direction and reason", "profile"], ["versioned classification"], ["classifier versions known"], ["classification remains source-qualified"], ["SRC-005", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]),
    ("bind-stock-subject", "Bind stock subject and quantity", "Bind item, lot, serial, handling-unit and qualified quantity references.", ["movement revision", "subject references", "quantity and unit"], ["validated subject binding"], ["external identities resolvable", "unit known"], ["scope is appended without importing masters"], ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-014", "SRC-015"]),
    ("define-transition", "Define source and destination transition", "Record source, destination, owner, custodian, status and disposition before-and-after references.", ["movement revision", "source state", "destination state"], ["typed transition assertion"], ["positions and locations resolvable"], ["balances remain external and unmodified"], ["SRC-001", "SRC-002", "SRC-005", "SRC-011", "SRC-016"]),
    ("plan-or-reserve", "Plan or reserve movement", "Bind request, order, reservation, warehouse task, production or shipment triggers and planned clocks.", ["movement identifier", "trigger references", "planned quantity and time"], ["planned movement revision"], ["trigger authority known"], ["plan remains distinct from execution and posting"], ["SRC-005", "SRC-007", "SRC-010", "SRC-017", "SRC-018"]),
    ("record-execution", "Record execution evidence", "Append physical handling, scan, count, observation and completion assertions.", ["movement identifier", "evidence reference", "event and record time"], ["execution assertion"], ["evidence source known"], ["observation does not silently post inventory"], ["SRC-001", "SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-019", "SRC-020"]),
    ("record-posting", "Record authoritative posting reference", "Register a posting performed by the external inventory master or ledger without executing it locally.", ["movement revision", "posting identifier", "posting authority and time"], ["posting-reference assertion"], ["external posting succeeded", "posting authority verified"], ["resulting balance remains externally mastered"], ["SRC-007", "SRC-008", "SRC-013", "SRC-014", "SRC-017", "SRC-018", "SRC-020"]),
    ("reverse-or-correct", "Reverse or correct movement", "Append compensating or successor assertions while preserving the original event and posting lineage.", ["movement revision", "reason", "correction or reversal reference"], ["successor revision", "lineage map"], ["correction authority", "affected scope known"], ["history remains immutable and linked"], ["SRC-001", "SRC-009", "SRC-020", "SRC-024"]),
    ("reconcile-movement", "Reconcile movement", "Compare request, execution, receipt, shipment, count, posting and position assertions under tolerance rules.", ["movement revision", "comparison assertions", "tolerance and precedence policy"], ["reconciliation result", "conflict set"], ["units, sources and clocks known"], ["differences remain visible and source-qualified"], ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-014", "SRC-021"]),
    ("project-movement", "Project inventory movement", "Produce minimum-necessary standards-aligned visibility, inventory, fulfilment or manufacturing views.", ["movement revision", "target profile", "access purpose"], ["versioned projection", "semantic-loss declaration"], ["authorized recipient", "pinned target version"], ["projection is logged and source identity preserved"], ["SRC-001", "SRC-005", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019", "SRC-020", "SRC-021", "SRC-022", "SRC-023", "SRC-024"]),
]
BASE.FUNCTION_ROWS = FUNCTION_ROWS


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, inventory steward, warehouse operator, posting authority, approver and accountable reconciliation roles.",
                "Register authoritative product, lot, serial, handling-unit, location, stock-position, order, reservation, task, production, shipment, ledger, document, observation and evidence masters.",
                "Publish movement-type, reason, location, stock-status, unit, access, retention, quality and interoperability registries.",
                "Pin industry, jurisdiction, warehouse, manufacturing, accounting, valuation, safety, privacy, licensing and exchange profiles.",
            ],
            "namespace_guidance": "Mint movement, revision, transition, execution-assertion, posting-reference, reconciliation and projection identifiers only in the adopting Dimension namespace; preserve external identities as typed references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local movement, stock-status, location, unit, posting, access, retention and provenance registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, authoritative movement ID, immutable revision, assertion kind, stock-subject scope, source-destination transition and source profile; never use date, document number, barcode, quantity, endpoint pair or hash alone as identity.",
                "Keep request, plan, reservation, physical execution, observation, posting, resulting stock position, correction and reconciliation distinct and preserve causal links.",
            ],
            "patch_rules": [
                "Additive extensions use a Dimension-owned namespace and declare target node, movement or industry profile, authority, source, rationale, access, time and interoperability impact.",
                "Breaking changes require a new version, migration and crosswalk maps, compatibility declaration and continued resolution of prior movement revisions, postings and identifiers.",
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when identity, assertion kind, stock subject, quantity, transition, clocks, authority, provenance and access meaning remain intact.",
                "GS1, UBL, UN/CEFACT, ISA-95, IEC 62264, units and provenance mappings pin source and target versions and declare transformed, omitted or non-round-trippable values.",
            ],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative inventory or warehouse master-system movement identifier and immutable revision.", "Governed globally resolvable movement, transition, posting or reconciliation IRI.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."],
            "timestamp_rule": "Record timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep planned, effective, event, observation, record, posting, correction and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {movement-id}--{artifact-kind}--{revision-or-event-id}; never use a date, document number, barcode, quantity, location, filename or hash alone as identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and vocabulary versions, subject and transition scope, event and record times, provenance, assurance, license and access marking for each retained serial artifact.",
        },
        "policies": [
            "The adopting Dimension declares who may request, plan, reserve, execute, observe, post, approve, reverse, correct, reconcile, disclose, retain and tombstone inventory movements.",
            "Every assertion requires movement identity and revision, assertion kind, stock subject, qualified quantity, transition scope, time kind, source, authority, confidence, status and lineage as applicable.",
            "Agents never infer inventory balance, ownership, custody, availability, quality, shipment completion, financial value or legal permission from one movement, scan, document, event or posting reference alone.",
            "Product, lot, serial, handling unit, location, stock position, order, task, shipment, ledger, valuation, document, observation, incident and evidence remain external masters.",
            "Automated agents may append low-risk plans, observations, reconciliations and projections under delegation, but authoritative inventory posting, reversal, protected disclosure and irreversible deletion require explicit external authority.",
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, requested revision, stock-subject scope, assertion kind, status horizon, assurance, freshness, license and access policy; return the minimum permitted projection."],
            "create": ["Create stable identity, movement class, stock-subject scope, qualified quantity, source-destination transition, source, authority and explicit unknowns before adding execution or posting assertions."],
            "update": ["Append an immutable plan, execution, posting, exception, reconciliation or correction revision with actor, authority, reason, RFC 3339 effective time and predecessor."],
            "delete": ["Apply safety, finance, dispute, audit, retention, disposition and legal-hold policy; tombstone eligible Inventory Movement-owned records or withdraw projections while preserving identity, material provenance and non-cascading external references. The adopting Dimension policy owns execution."],
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Inventory steward", "responsibilities": ["Own movement semantics, classifiers, stock-position references and reconciliation policy."]},
            {"name": "Requester or planner", "responsibilities": ["Own request, order, reservation, task, planned quantity and timing assertions."]},
            {"name": "Warehouse or process executor", "responsibilities": ["Own physical execution and operator-confirmed movement evidence within delegated scope."]},
            {"name": "Observer or evidence steward", "responsibilities": ["Own scan, count, sensor, document, quality and correction lineage."]},
            {"name": "Inventory posting authority", "responsibilities": ["Own authoritative posting, reversal and resulting balance in the external master system."]},
            {"name": "Approver or reconciler", "responsibilities": ["Review segregation of duties, exceptions, conflicts, tolerance and closure."]},
            {"name": "Disclosure authority", "responsibilities": ["Review protected use, recipient, purpose, redaction and publication timing."]},
        ],
        "access": {
            "default_rule": "Deny mutation and sensitive disclosure unless active Dimension, role, purpose, stock and location sensitivity, safety or finance rule, license and field policy grant the action; expose the minimum necessary projection.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency or regulatory access must be legally grounded, time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable movement, correction, reversal or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, movement and revision identity, action, decision, policy and vocabulary versions, RFC 3339 timestamp with offset, affected fields, source evidence and outcome for privileged mutation or disclosure."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read the nearest Dimension-owner AGENTS.md, inventory and posting authority, active industry, jurisdiction, time, access, retention, licensing and disclosure policies.", "Read this model AGENTS.md, pinned spec.yaml and required product, lot, serial, handling-unit, location, stock-position, order, task, shipment, ledger, document, observation and evidence instructions before mutation."],
        },
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Inventory Movement identity, class, stock subject, quantity, location and stock-bucket transition, triggers, execution, posting references, clocks, evidence, exceptions, reconciliation, governance and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Movement, revision, execution assertion, posting reference, correction, reversal and projection identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Direction, reason, movement class and planned, physical, observed, posted or reconciled assertion kind are explicit."},
            {"dimension": "direct properties", "status": "covered", "notes": "Subject scope, quantity, transition, state and event-specific evidence are covered without importing external masters."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Request, physical execution, scan, count, document, posting and resulting balance are independently recognized."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Requested, planned, reserved, released, executing, completed, posted, failed, cancelled, reversed and corrected states preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Stock subjects, locations, positions, orders, tasks, shipments, postings, documents and evidence use typed references."},
            {"dimension": "temporal", "status": "covered", "notes": "Planned, effective, event, observation, record, posting, correction and ingestion clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Source and destination site, warehouse, zone, bin, virtual location and read-point functions are explicit."},
            {"dimension": "provenance", "status": "covered", "notes": "Sources, actors, methods, observations, postings, derivations, revisions and invalidations are linked."},
            {"dimension": "ownership", "status": "covered", "notes": "Inventory ownership, custody, possession, control, responsibility and data mastership are not conflated."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, quantity, unit, transition, clock, role, posting, balance, evidence and crosswalk checks are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Role, purpose, segregation of duties, commercial sensitivity, minimum projection and audit are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Corrections, reversals, disputes, audit or legal hold, withdrawal and tombstones are explicit and non-cascading."},
            {"dimension": "interoperability", "status": "covered", "notes": "GS1, UBL, UN/CEFACT, ISA-95, IEC 62264, RFC, PROV, DQV, ODRL and ISO mappings disclose loss."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Registration, classification, binding, planning, evidence, posting reference, correction, reconciliation and projection declare controlled effects."},
        ],
        "known_omissions": [
            "Industry, warehouse, manufacturing, accounting, valuation, customs, dangerous-goods, safety, privacy, licensing and retention profiles require exact current rules and competent review.",
            "Product, lot, serial, handling unit, location, stock position, order, task, shipment, ledger, document, observation, incident and evidence lifecycles remain in neighboring models.",
            "Certified field crosswalks, balance calculation, costing, allocation algorithms, warehouse execution, autonomous robotics and legal evidence requirements remain future work.",
        ],
        "conflicts": [
            "Warehouse systems may call a request, task, physical action, scan or ledger posting a movement; the model requires an explicit assertion kind and source profile.",
            "GS1 EPCIS captures visibility events and UBL exchanges fulfilment documents, but neither is assumed to be the universal authoritative inventory ledger.",
            "A physical transfer, ownership transfer, custody transfer, status change, valuation posting and accounting entry may correlate but are different governed facts.",
        ],
        "regional_assumptions": [
            "UN/CEFACT and UBL are cross-domain exchange sources rather than universal inventory law or warehouse execution policy.",
            "ISA-95 and IEC 62264 are manufacturing integration profiles and do not define all retail, healthcare, customs or field-service movements.",
            "Inventory posting, valuation, tax, title, custody, safety and retention consequences depend on organization, industry and jurisdiction.",
        ],
        "adversarial_checks": [
            "Reject a movement without stable identity, revision, assertion kind, stock subject, qualified quantity, transition, source, authority and lineage.",
            "Reject a request, reservation, warehouse task, scan, shipment event, inventory balance or accounting entry represented as the movement itself without a discriminator.",
            "Reject physical execution and authoritative inventory posting collapsed into one state or timestamp.",
            "Reject quantity without unit, precision and subject scope or a location transition without source and destination roles.",
            "Reject ownership, custody, availability, quality, financial value or shipment completion inferred from one movement or document alone.",
            "Reject last-write-wins when request, execution, receipt, posting, count or balance assertions conflict; preserve source, clocks, correction and precedence.",
            "Reject authoritative posting, reversal, protected disclosure or record destruction outside delegated external authority.",
        ],
    }


def build():
    model = {
        "registry_id": "vr.wm-flw-012", "model_id": "WM-FLW-012", "name": "Inventory Movement", "entry_kind": "event",
        "purpose": "Represent one governed stock-affecting movement assertion, its subject, quantity, source-destination transition, execution and posting references, evidence and correction lineage without becoming the inventory position, ledger, product, location, task or shipment.",
        "scope_statement": "Owns movement identity and revision; assertion kind, class, direction and reason; idempotency and correction lineage; item, lot, serial and handling-unit scope references; qualified quantity; source and destination position, location, owner, custodian, status and disposition references; request, order, reservation, task, production and shipment triggers; lifecycle and clocks; execution observations; external authoritative posting references; exceptions, reconciliation, provenance, access, retention and loss-aware projections. Product, lot, serial, handling unit, location, stock position and balance, order, warehouse task, production, shipment, journey, chain of custody, ledger, valuation, accounting, document, observation, incident and evidence masters remain external.",
        "in_scope": ["Movement identity, class, assertion kind, revision, idempotency, direction, reason and successor lineage", "Stock-subject scope, qualified quantity, source-destination and stock-bucket transition references, triggers, execution and posting assertions", "Lifecycle clocks, evidence, exceptions, reconciliation, governance, access, retention and interoperability"],
        "out_of_scope": ["Owning product, material, lot, serial, handling unit, place, inventory position, stock balance, order, reservation, task, production, shipment, journey, trace, ledger, valuation, accounting, document, observation, incident or evidence lifecycles", "Equating request with execution, physical movement with posting, custody with ownership, location with stock status, position with movement, count discrepancy with adjustment or shipment milestone with inventory receipt", "Executing warehouse operations, inventory ledger mutation, accounting posting, autonomous physical handling, safety decisions, protected disclosure or irreversible deletion"],
        "boundary_notes": [
            {"neighbor": "WM-OBJ-020 Inventory Stock Position", "distinction": "Inventory Movement references before-and-after positions and may support an externally calculated balance change. Position identity, balance computation and snapshot lifecycle remain external; the candidate parent signal is held for review.", "source_refs": ["SRC-007", "SRC-008", "SRC-013", "SRC-014", "SRC-017", "SRC-018"]},
            {"neighbor": "WM-FLW-011 Shipment / Consignment", "distinction": "A shipment groups goods and logistics obligations. Inventory Movement owns a stock-affecting transition that may be triggered or evidenced by despatch or receipt but does not own the shipment.", "source_refs": ["SRC-001", "SRC-005", "SRC-007", "SRC-009", "SRC-010"]},
            {"neighbor": "WM-FLW-013 Supply-chain Trace / Chain of Custody", "distinction": "Inventory Movement owns one movement assertion and its correction lineage. Cross-organizational critical-event graphs and custody proof remain externally mastered.", "source_refs": ["SRC-001", "SRC-006", "SRC-020"]},
            {"neighbor": "Product, lot, serial and handling unit", "distinction": "The movement binds subject identities and aggregation scope. Their descriptive properties, composition, condition and independent lifecycles remain external.", "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-006"]},
            {"neighbor": "Order, reservation, warehouse task and production", "distinction": "These objects trigger or authorize planned work. Inventory Movement records their references and observed effects but not their workflow or resource scheduling.", "source_refs": ["SRC-005", "SRC-007", "SRC-017", "SRC-018"]},
            {"neighbor": "Inventory ledger, valuation and accounting", "distinction": "The model records external posting identity, authority, time and result reference. It does not calculate balances, cost inventory or create accounting entries.", "source_refs": ["SRC-008", "SRC-013", "SRC-014", "SRC-017", "SRC-018"]},
            {"neighbor": "Observation, document, incident and evidence", "distinction": "Scans, counts, sensor readings, receipt or despatch documents and incident records are independently governed evidence references, not the movement identity or automatic master truth.", "source_refs": ["SRC-001", "SRC-002", "SRC-007", "SRC-009", "SRC-010", "SRC-020", "SRC-021"]},
        ],
    }
    composition = [
        {"target": "WM-OBJ-020 Inventory Stock Position", "relation": "REFERENCE", "purpose": "Resolve source and destination positions and resulting balances while the candidate parent relation remains under joint boundary review.", "required": True, "source_refs": ["SRC-007", "SRC-008", "SRC-013", "SRC-014", "SRC-017", "SRC-018"]},
        {"target": "WM-FLW-011 Shipment / Consignment", "relation": "REFERENCE", "purpose": "Resolve despatch, receipt and logistics grouping triggers without importing shipment lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-005", "SRC-007", "SRC-009", "SRC-010"]},
        {"target": "WM-FLW-013 Supply-chain Trace / Chain of Custody", "relation": "REFERENCE", "purpose": "Resolve cross-organizational event graphs and custody evidence without duplicating them.", "required": False, "source_refs": ["SRC-001", "SRC-006", "SRC-020"]},
        {"target": "Product, lot, serial, handling unit and location masters", "relation": "REFERENCE", "purpose": "Resolve stock subjects and spatial context while preserving external identity and lifecycle authority.", "required": True, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-006", "SRC-016"]},
        {"target": "Order, reservation, warehouse task and production masters", "relation": "REFERENCE", "purpose": "Resolve request, authorization and execution context without owning operational workflows.", "required": False, "source_refs": ["SRC-005", "SRC-007", "SRC-017", "SRC-018"]},
        {"target": "Inventory ledger, valuation and accounting masters", "relation": "REFERENCE", "purpose": "Resolve authoritative posting and resulting balance without local financial or inventory mutation.", "required": False, "source_refs": ["SRC-008", "SRC-013", "SRC-014", "SRC-017", "SRC-018"]},
        {"target": "GS1 EPCIS 2.0.1 and CBV 2.0.0", "relation": "ALIGN", "purpose": "Project visibility events, object and quantity scope, locations, business steps, dispositions and corrections without treating observations as ledger truth.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006"]},
        {"target": "OASIS UBL 2.4", "relation": "ALIGN", "purpose": "Project inventory report, despatch and receipt views with pinned document semantics.", "required": False, "source_refs": ["SRC-007", "SRC-008", "SRC-009", "SRC-010"]},
        {"target": "UN/CEFACT code lists and Core Component Library", "relation": "ALIGN", "purpose": "Project direction, reason, balance, quantity and unit semantics with exact release pins.", "required": False, "source_refs": ["SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]},
        {"target": "ISA-95 and IEC 62264-2", "relation": "ALIGN", "purpose": "Project manufacturing enterprise-control exchange semantics as an industry profile.", "required": False, "source_refs": ["SRC-017", "SRC-018"]},
        {"target": "RFC 3339, PROV-O, DQV, ODRL, XML Schema and ISO 8000", "relation": "ALIGN", "purpose": "Project temporal, provenance, quality, access, datatype and master-data semantics with semantic-loss declarations.", "required": False, "source_refs": ["SRC-019", "SRC-020", "SRC-021", "SRC-022", "SRC-023", "SRC-024"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": BASE.structure(), "functions": BASE.functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
