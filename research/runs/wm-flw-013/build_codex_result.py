#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-FLW-013."""

import importlib.util
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
BASE_PATH = RUN.parent / "wm-flw-010" / "build_codex_result.py"
SPEC = importlib.util.spec_from_file_location("wm_flw_010_builder", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
AT = "2026-09-06T21:18:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "EPCIS Standard", "GS1", "https://ref.gs1.org/standards/epcis/2.0.1/", "EPCIS 2.0.1, 1 July 2025", "standard", "Defines interoperable visibility events, event and record clocks, sources, destinations, queries and error declarations."),
    src(2, "Core Business Vocabulary Standard", "GS1", "https://ref.gs1.org/standards/cbv/2.0.0/", "CBV 2.0.0, June 2022", "standard", "Defines controlled business steps, dispositions, source and destination types used with EPCIS."),
    src(3, "GS1 Global Traceability Standard", "GS1", "https://ref.gs1.org/standards/global-traceability/2.0.0/", "Release 2.0, August 2017", "standard", "Defines traceable objects, critical tracking events, key data elements and one-up one-down responsibilities."),
    src(4, "EPCIS ObjectEvent linked-data definition", "GS1", "https://ref.gs1.org/epcis/ObjectEvent", "EPCIS linked-data model accessed 2026-09-06", "ontology", "Defines instance and class-level observations, actions, locations, quantities and business context."),
    src(5, "EPCIS AggregationEvent linked-data definition", "GS1", "https://ref.gs1.org/epcis/AggregationEvent", "EPCIS linked-data model accessed 2026-09-06", "ontology", "Defines time-qualified parent-child aggregation and disaggregation assertions."),
    src(6, "EPCIS TransformationEvent linked-data definition", "GS1", "https://ref.gs1.org/epcis/TransformationEvent", "EPCIS linked-data model accessed 2026-09-06", "ontology", "Defines input-output transformation events and transformation identifiers."),
    src(7, "Integrated Track and Trace for Multi-Modal Transportation BRS", "UN/CEFACT", "https://unece.org/trade/documents/2022/09/business-requirements-specifications-brs-integrated-track-and-trace-multi", "Approved version 1.1, 14 September 2022", "standard", "Defines cross-industry tracking of identified trade and transport objects across multimodal journeys."),
    src(8, "White Paper on Integrated Track and Trace for Multimodal Transportation", "UN/CEFACT", "https://unece.org/trade/publications/white-paper-integrated-track-and-trace-multimodal-transportation-ecetrade466", "ECE/TRADE/466, January 2022", "public-authority", "Explains end-to-end visibility across shipments, consignments, assets, modes and organizations."),
    src(9, "Visibility and Collaborative Planning in Multimodal Supply Chain Operations BRS", "UN/CEFACT", "https://unece.org/trade/documents/2026/07/standards/brs-visibility-and-collaborative-planning-multimodal-supply-chain", "BRS published July 2026", "standard", "Defines a transport event registry and scoped auditable delegation for multimodal visibility."),
    src(10, "ISO 22095:2020 Chain of custody", "International Organization for Standardization", "https://www.iso.org/standard/72532.html", "ISO 22095:2020 with Amendment 1:2026 noted", "standard", "Defines generic chain-of-custody terminology, system design and models for materials and products."),
    src(11, "ISO 22095-2:2026 Chain of custody mass balance", "International Organization for Standardization", "https://www.iso.org/standard/84427.html", "ISO 22095-2:2026", "standard", "Defines mass-balance system boundaries, attribution, conversion factors, credit methods and claims."),
    src(12, "ISO 22005:2007 Feed and food traceability", "International Organization for Standardization", "https://www.iso.org/standard/36297.html", "ISO 22005:2007, confirmed 2022", "standard", "Defines principles and requirements for determining product or component history and location."),
    src(13, "ISO 28000:2022 Security and resilience", "International Organization for Standardization", "https://www.iso.org/standard/79612.html", "ISO 28000:2022 with Amendment 1:2024", "standard", "Defines supply-chain-relevant security management requirements and controls."),
    src(14, "FSMA Food Traceability Final Rule", "United States Food and Drug Administration", "https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods", "21 CFR Part 1 Subpart S; page accessed 2026-09-06", "legislation", "Defines food critical tracking events, key data elements, traceability lots and record provision duties."),
    src(15, "Regulation EU 2024/1781 Ecodesign for Sustainable Products", "European Union", "https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng", "Regulation EU 2024/1781, consolidated 28 June 2024", "legislation", "Defines Digital Product Passport identity, item or batch scope, open interoperability, access and retention duties."),
    src(16, "Track and Trace Standard Documentation", "Digital Container Shipping Association", "https://dcsa.org/standards/track-and-trace/standard-documentation-track-and-trace", "Track and Trace 2.2 documentation accessed 2026-09-06", "standard", "Defines container-shipping event semantics and interoperable cross-carrier tracking phases and APIs."),
    src(17, "ONE Record", "International Air Transport Association", "https://www.iata.org/one-record/", "Standard overview accessed 2026-09-06", "standard", "Defines a federated air-cargo data-sharing model, secured API and shared shipment record."),
    src(18, "ONE Record Ontology", "International Air Transport Association", "https://onerecord.iata.org/ns/cargo/3.2.0", "Ontology revision 3.2.0, modified 24 June 2025", "ontology", "Defines linked air-cargo objects, events, logistics actions, parties and shipment data."),
    src(19, "RFC 3339 Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines timestamps with seconds and explicit numeric offsets or Z."),
    src(20, "RFC 8785 JSON Canonicalization Scheme", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc8785.html", "RFC 8785, June 2020", "standard", "Defines deterministic JSON canonicalization for repeatable hashing and signing."),
    src(21, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entities, activities, agents, attribution, derivation, delegation, revision and invalidation."),
    src(22, "Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note, 15 December 2016", "ontology", "Defines quality measurements, annotations, policies and provenance."),
    src(23, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties and constraints for governed trace data use."),
    src(24, "Verifiable Credential Data Integrity 1.0", "World Wide Web Consortium", "https://www.w3.org/TR/vc-data-integrity/", "W3C Recommendation, 15 May 2025", "standard", "Defines integrity proofs and verification material for constrained digital documents."),
]


ROWS = [
    ("trace-identity-scope-and-semantic-kind", "Trace identity, scope and semantic kind", "Define the trace graph, query result and chain-of-custody claim boundaries before linking evidence.", [
        ("trace-identity-revision-and-result-kind", "Trace identity, revision and result kind", ["SRC-001", "SRC-003", "SRC-007", "SRC-008", "SRC-019", "SRC-021"], [
            ("trace-graph-scope-identifier-namespace-and-revision", "Trace graph scope, identifier, namespace and revision", "identity"),
            ("persistent-graph-query-request-result-snapshot-and-claim-kind", "Persistent graph, query request, result, snapshot and claim kind", "classification"),
        ]),
        ("coverage-objective-profile-and-system-boundary", "Coverage objective, profile and system boundary", ["SRC-003", "SRC-007", "SRC-008", "SRC-010", "SRC-011", "SRC-012", "SRC-014", "SRC-015"], [
            ("traceability-objective-subject-range-depth-and-direction", "Traceability objective, subject range, depth and direction", "requirement"),
            ("physical-segregation-controlled-blending-mass-balance-and-book-and-claim-profile", "Physical segregation, controlled blending, mass balance and book-and-claim profile", "classification"),
        ]),
    ]),
    ("traceable-object-event-and-composition-graph", "Traceable-object, event and composition graph", "Link externally mastered objects and events through time-qualified aggregation and transformation edges.", [
        ("object-identity-class-and-membership", "Object identity, class and membership", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-014", "SRC-015", "SRC-018"], [
            ("product-material-lot-serial-item-handling-unit-shipment-and-asset-reference", "Product, material, lot, serial, item, handling-unit, shipment and asset reference", "relationship"),
            ("aggregation-disaggregation-containment-and-membership-interval", "Aggregation, disaggregation, containment and membership interval", "composition"),
        ]),
        ("critical-event-transformation-and-causality", "Critical event, transformation and causality", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-014", "SRC-016", "SRC-018", "SRC-021"], [
            ("commission-observe-pack-ship-receive-store-use-return-and-dispose-event", "Commission, observe, pack, ship, receive, store, use, return and dispose event", "event"),
            ("transformation-input-output-process-step-causality-and-yield", "Transformation input, output, process step, causality and yield", "process"),
        ]),
    ]),
    ("location-party-and-custody-chain", "Location, party and custody chain", "Represent where and by whom assertions arise while custody and ownership remain independent.", [
        ("read-point-business-location-source-and-destination", "Read point, business location, source and destination", ["SRC-001", "SRC-002", "SRC-004", "SRC-007", "SRC-008", "SRC-009", "SRC-014", "SRC-016", "SRC-018"], [
            ("event-read-point-business-location-jurisdiction-and-facility", "Event read point, business location, jurisdiction and facility", "spatial"),
            ("source-destination-business-step-disposition-and-movement-reference", "Source, destination, business step, disposition and movement reference", "relationship"),
        ]),
        ("party-role-custody-and-handover", "Party role, custody and handover", ["SRC-003", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-017", "SRC-021"], [
            ("owner-custodian-possessor-controller-responsible-party-and-steward", "Owner, custodian, possessor, controller, responsible party and steward", "ownership"),
            ("custody-interval-transfer-handover-acceptance-refusal-and-exception", "Custody interval, transfer, handover, acceptance, refusal and exception", "lifecycle"),
        ]),
    ]),
    ("time-evidence-integrity-and-correction", "Time, evidence, integrity and correction", "Keep clocks, sources, proof, quality and correction lineage explicit for every trace assertion.", [
        ("clocks-source-provenance-and-attribution", "Clocks, source, provenance and attribution", ["SRC-001", "SRC-003", "SRC-007", "SRC-014", "SRC-016", "SRC-018", "SRC-019", "SRC-021"], [
            ("event-effective-observation-record-ingestion-and-publication-time", "Event, effective, observation, record, ingestion and publication time", "temporal"),
            ("asserting-agent-source-system-method-authority-and-delegation", "Asserting agent, source system, method, authority and delegation", "provenance"),
        ]),
        ("evidence-proof-quality-conflict-and-correction", "Evidence, proof, quality, conflict and correction", ["SRC-001", "SRC-013", "SRC-014", "SRC-019", "SRC-020", "SRC-021", "SRC-022", "SRC-024"], [
            ("evidence-artifact-digest-signature-credential-and-verification-result", "Evidence artifact, digest, signature, credential and verification result", "evidence"),
            ("completeness-confidence-gap-duplicate-conflict-error-declaration-and-successor", "Completeness, confidence, gap, duplicate, conflict, error declaration and successor", "quality"),
        ]),
    ]),
    ("trace-query-exposure-recall-and-federation", "Trace query, exposure, recall and federation", "Return qualified graph slices and risk sets without turning analysis into an external decision.", [
        ("backward-forward-history-and-path-query", "Backward, forward, history and path query", ["SRC-001", "SRC-003", "SRC-007", "SRC-008", "SRC-012", "SRC-014", "SRC-016", "SRC-017", "SRC-018"], [
            ("one-up-one-down-backward-forward-and-end-to-end-trace", "One-up one-down, backward, forward and end-to-end trace", "process"),
            ("object-event-party-location-time-and-relationship-filter", "Object, event, party, location, time and relationship filter", "constraint"),
        ]),
        ("exposure-recall-impact-and-qualified-result", "Exposure, recall, impact and qualified result", ["SRC-003", "SRC-006", "SRC-007", "SRC-008", "SRC-012", "SRC-014", "SRC-015", "SRC-021", "SRC-022"], [
            ("affected-lot-item-party-location-shipment-and-downstream-set", "Affected lot, item, party, location, shipment and downstream set", "decision"),
            ("recall-investigation-alert-status-action-reference-and-residual-uncertainty", "Recall, investigation, alert, status, action reference and residual uncertainty", "exception"),
        ]),
    ]),
    ("governance-access-retention-and-interoperability", "Governance, access, retention and interoperability", "Federate minimum-necessary trace data and project profiles without hiding authority or semantic loss.", [
        ("federation-discovery-access-privacy-and-retention", "Federation, discovery, access, privacy and retention", ["SRC-001", "SRC-003", "SRC-009", "SRC-013", "SRC-014", "SRC-015", "SRC-017", "SRC-021", "SRC-023"], [
            ("registry-endpoint-query-routing-availability-and-freshness", "Registry, endpoint, query routing, availability and freshness", "interoperability"),
            ("purpose-role-consent-confidentiality-minimum-disclosure-retention-and-legal-hold", "Purpose, role, consent, confidentiality, minimum disclosure, retention and legal hold", "access"),
        ]),
        ("standards-crosswalk-conformance-and-loss", "Standards crosswalk, conformance and loss", ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019", "SRC-020", "SRC-021", "SRC-022", "SRC-023", "SRC-024"], [
            ("gs1-uncefact-iso-fda-eu-dcsa-iata-and-provenance-crosswalk", "GS1, UN/CEFACT, ISO, FDA, EU, DCSA, IATA and provenance crosswalk", "interoperability"),
            ("profile-version-license-conformance-transformation-and-semantic-loss", "Profile, version, license, conformance, transformation and semantic loss", "validation"),
        ]),
    ]),
]


KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 7) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 16) % len(KIND_CYCLE)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {lower} as a typed Supply-chain Trace assertion while objects, events, movements, parties, places, claims, decisions and evidence retain external mastership.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which trace identity, result kind, object and event scope, graph edge, clocks and source establish {lower}?", "kind": kinds[0], "answer_data": ["trace scope identifier, namespace, revision, persistent-graph or result kind and query basis", "traceable-object, event, aggregation, transformation, location, party and custody references", "event, observation, record and ingestion clocks plus source profile and confidence"]},
            {"id": f"{fid}-q02", "text": f"Who owns, holds, observes, asserts, verifies, corrects, queries, discloses or acts on {lower}, and under which authority?", "kind": kinds[1], "answer_data": ["owner, custodian, possessor, controller, operator, source steward, verifier and decision roles", "business step, transfer, delegation, purpose, jurisdiction, confidentiality and access basis", "master system, signature or credential issuer, reviewer, correction actor and disputed state"]},
            {"id": f"{fid}-q03", "text": f"Which evidence, completeness, gap, conflict, exposure, uncertainty and lineage qualify {lower}?", "kind": kinds[2], "answer_data": ["evidence artifact, digest, proof, verification method and quality measurement", "missing link, duplicate, contradiction, error declaration, retraction, successor and residual uncertainty", "backward or forward path, affected set, recall reference, profile mapping and semantic-loss declaration"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed trace-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Digest-addressed manifest of objects, events, graph edges, sources, proofs, gaps, conflicts, query results and corrections supporting {lower}.", "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative trace or source-system event identifier first, otherwise governed IRI, then Dimension UUID or ULID; include immutable revision and digest.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


BASE.SOURCES = SOURCES
BASE.ROWS = ROWS
BASE.KIND_CYCLE = KIND_CYCLE
BASE.make_finding = make_finding


FUNCTION_ROWS = [
    ("register-trace-scope", "Register trace scope", "Create one governed trace-graph or result identity with an explicit semantic kind and objective.", ["trace kind", "subject range", "owner and source"], ["trace identifier", "initial revision"], ["active Dimension", "create authority"], ["identity, system boundary and unknowns are appended"], ["SRC-003", "SRC-007", "SRC-010", "SRC-012", "SRC-019", "SRC-021"]),
    ("bind-traceable-objects", "Bind traceable objects", "Bind product, material, lot, serial, item, handling-unit, shipment and asset identities without importing their lifecycles.", ["trace revision", "object references", "validity scope"], ["typed object bindings"], ["external identities resolvable"], ["membership remains source-qualified and time-aware"], ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-014", "SRC-015"]),
    ("append-critical-event", "Append critical event", "Link an externally mastered event with business, spatial, temporal, party and evidence context.", ["trace revision", "event reference", "critical data elements"], ["immutable graph event edge"], ["event identity and source known"], ["assertion is appended without overwriting the event master"], ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-007", "SRC-014", "SRC-016", "SRC-018"]),
    ("link-composition-transformation", "Link composition or transformation", "Append aggregation, disaggregation or input-output transformation edges with validity and yield context.", ["trace revision", "input and output or parent and child references", "event and time"], ["typed composition or transformation edge"], ["subjects and event resolvable"], ["prior membership and provenance remain visible"], ["SRC-001", "SRC-005", "SRC-006", "SRC-014", "SRC-021"]),
    ("record-custody-assertion", "Record custody assertion", "Append custody, possession, control, responsibility or handover assertions without inferring ownership.", ["trace revision", "party and object references", "role interval and evidence"], ["custody-chain edge"], ["asserting authority known"], ["acceptance, refusal and exceptions remain source-qualified"], ["SRC-003", "SRC-007", "SRC-010", "SRC-012", "SRC-013", "SRC-014", "SRC-021"]),
    ("attach-evidence-proof", "Attach evidence and proof", "Bind evidence artifacts, digests, signatures, credentials, verification results and quality statements.", ["trace assertion", "evidence reference", "verification method"], ["evidence binding", "verification assertion"], ["media type, issuer and scope known"], ["proof status never substitutes for claim truth or authority"], ["SRC-013", "SRC-020", "SRC-021", "SRC-022", "SRC-024"]),
    ("correct-or-contest", "Correct or contest trace assertion", "Append error declaration, retraction, competing assertion or successor without deleting the original.", ["trace revision", "affected assertion", "reason and authority"], ["correction or contested-set revision"], ["affected scope known"], ["history, source and conflict remain resolvable"], ["SRC-001", "SRC-019", "SRC-020", "SRC-021", "SRC-022"]),
    ("trace-path", "Trace backward or forward", "Return a qualified graph slice across object, event, party, location and time filters.", ["trace scope", "anchor", "direction, depth and filters"], ["versioned trace result", "gap set"], ["authorized query", "source freshness known"], ["result preserves evidence, uncertainty and omitted-scope declaration"], ["SRC-001", "SRC-003", "SRC-007", "SRC-008", "SRC-012", "SRC-014", "SRC-016", "SRC-017"]),
    ("compute-exposure-set", "Compute qualified exposure set", "Derive candidate affected objects, parties, locations and shipments without making a recall or enforcement decision.", ["trace result", "hazard or affected anchor", "inclusion and exclusion rules"], ["qualified exposure set", "residual uncertainty"], ["rules, graph horizon and evidence thresholds known"], ["analysis is attributable and decision remains external"], ["SRC-003", "SRC-006", "SRC-007", "SRC-012", "SRC-014", "SRC-021", "SRC-022"]),
    ("project-trace-view", "Project authorized trace view", "Produce minimum-necessary standards-aligned trace, custody, regulatory or modal views.", ["trace revision or result", "target profile", "access purpose"], ["versioned projection", "semantic-loss declaration"], ["authorized recipient", "pinned target version"], ["projection is logged and source identities preserved"], ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019", "SRC-020", "SRC-021", "SRC-022", "SRC-023", "SRC-024"]),
]
BASE.FUNCTION_ROWS = FUNCTION_ROWS


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, trace steward, source authorities, custodians, verifiers, query operators and accountable decision roles.",
                "Register authoritative product, lot, serial, handling-unit, shipment, inventory-movement, journey, place, party, event, observation, handover, document, credential, recall, claim and evidence masters.",
                "Publish trace-object, event-type, business-step, disposition, location, custody-role, quality, access, retention and interoperability registries.",
                "Pin chain-of-custody model, sector, jurisdiction, claim, certification, security, privacy, licensing and exchange profiles.",
            ],
            "namespace_guidance": "Mint trace-scope, graph-revision, edge, gap, contested-set, query-result, exposure-set and projection identifiers only in the adopting Dimension namespace; preserve external master identities as typed references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local trace, event, custody-role, classifier, source, access, retention and provenance registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, trace scope, mandatory semantic kind, authoritative source IDs, immutable graph revision, query basis and source profile; never use date, lot code, barcode, party, location, document or hash alone as identity.",
                "Keep trace graph, query, result, snapshot, custody claim, object, event, aggregation, transformation, handover, evidence, exposure analysis and recall decision distinct and preserve corrections and successors.",
            ],
            "patch_rules": [
                "Additive extensions use a Dimension-owned namespace and declare target node, chain-of-custody or sector profile, authority, source, rationale, access, time and interoperability impact.",
                "Breaking changes require a new version, migration and crosswalk maps, compatibility declaration and continued resolution of prior graph revisions, query results and identifiers.",
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when trace identity, semantic kind, object and event scope, edge meaning, clocks, authority, provenance and access remain intact.",
                "GS1, UN/CEFACT, ISO, FDA, EU, DCSA, IATA and provenance mappings pin source and target versions and declare transformed, omitted or non-round-trippable values.",
            ],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative traceability master-system identifier and immutable revision.", "Governed globally resolvable trace, edge, query-result or exposure-set IRI.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."],
            "timestamp_rule": "Record timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep event, effective, observation, record, ingestion, publication and correction times distinct.",
            "serial_naming_rule": "Name serial artifacts as {trace-id}--{artifact-kind}--{revision-or-event-id}; never use a date, lot code, barcode, party, location, filename or hash alone as identity.",
            "integrity_rule": "Store digest, canonicalization profile, media type, byte length, issuer, source and vocabulary versions, graph scope, event and record times, provenance, verification, assurance, license and access marking for each retained artifact.",
        },
        "policies": [
            "The adopting Dimension declares who may register scope, bind objects, append events, assert custody, attach proofs, correct, query, derive exposure sets, disclose, retain and tombstone trace records.",
            "Every assertion requires trace and graph revision, semantic kind, subject and edge scope, source, authority, clocks, confidence, quality, access and lineage as applicable.",
            "Agents never infer ownership, custody, product characteristic, safety, compliance, authenticity, recall scope or legal responsibility from location, event, document, digest, signature or credential alone.",
            "Objects, events, movements, parties, places, handovers, observations, documents, credentials, claims, recall actions and evidence remain external masters.",
            "Automated agents may append low-risk source-qualified edges, gap reports, queries and projections under delegation, but custody acceptance, certification, recall, enforcement, protected disclosure and irreversible deletion require accountable external authority.",
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, trace scope and revision, object and time horizon, source freshness, quality, assurance, license and access policy; return the minimum permitted graph projection."],
            "create": ["Create stable trace scope, semantic kind, objective, object range, direction, source authorities, chain-of-custody profile and explicit unknowns before adding graph edges."],
            "update": ["Append an immutable object binding, event edge, custody assertion, proof, gap, conflict or correction with actor, authority, reason, RFC 3339 clocks and predecessor."],
            "delete": ["Apply safety, certification, regulatory, dispute, audit, retention, disposition and legal-hold policy; tombstone eligible Trace-owned records or withdraw projections while preserving identity, material provenance and non-cascading external references. The adopting Dimension policy owns execution."],
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Traceability steward", "responsibilities": ["Own trace scope, graph semantics, chain-of-custody profiles, quality and correction policy."]},
            {"name": "Source-system authority", "responsibilities": ["Own object, event, clock, location and business assertions within its system boundary."]},
            {"name": "Custodian or operator", "responsibilities": ["Assert custody, possession, handling and handover evidence within delegated scope."]},
            {"name": "Evidence issuer or verifier", "responsibilities": ["Own artifacts, digests, proof methods, verification results and limitations."]},
            {"name": "Query or investigation operator", "responsibilities": ["Run authorized backward, forward, path and exposure analyses with declared rules."]},
            {"name": "Recall or regulatory authority", "responsibilities": ["Own recall, enforcement, certification or regulatory decisions outside the trace pattern."]},
            {"name": "Disclosure reviewer", "responsibilities": ["Review recipient, purpose, minimum disclosure, redaction and publication timing."]},
        ],
        "access": {
            "default_rule": "Deny mutation and sensitive disclosure unless active Dimension, role, purpose, commercial confidentiality, location, personal data, security, license and field policy grant the action; expose the minimum necessary graph slice.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency or regulatory access must be legally grounded, time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable trace, conflict, correction or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, trace and revision identity, query or action, decision, policy and vocabulary versions, RFC 3339 timestamp with offset, affected graph scope, source evidence and outcome for privileged mutation or disclosure."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read the nearest Dimension-owner AGENTS.md, trace and source authorities, active custody model, sector, jurisdiction, time, access, retention, licensing and disclosure policies.", "Read this model AGENTS.md, pinned spec.yaml and required object, event, movement, party, place, handover, document, credential, recall, claim and evidence instructions before mutation."],
        },
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Supply-chain Trace / Chain of Custody identity, scope, object-event graph, composition, transformation, location, parties, custody, clocks, evidence, integrity, quality, correction, query, exposure, federation, access, retention and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Trace scope, graph revision, query request, result, snapshot, claim, edge and exposure-set identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Trace objective, direction, coverage and chain-of-custody profile are mandatory and versioned."},
            {"dimension": "direct properties", "status": "covered", "notes": "Graph scope, edge semantics, gaps, conflicts and query basis are covered without importing external masters."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Authoritative identity, physical observation, business assertion, document, signature and verification result are distinguished."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Registration, append, validation, contest, correction, supersession, withdrawal, retention and tombstone preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Objects, events, aggregation, transformation, locations, parties, movements, handovers, documents and decisions use typed edges."},
            {"dimension": "temporal", "status": "covered", "notes": "Event, effective, observation, record, ingestion, publication and correction clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Read point, business location, source, destination, facility and jurisdiction functions are explicit."},
            {"dimension": "provenance", "status": "covered", "notes": "Sources, agents, methods, delegations, evidence, derivations, revisions and invalidations are linked."},
            {"dimension": "ownership", "status": "covered", "notes": "Ownership, custody, possession, control, responsibility and data mastership are not conflated."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, edge, clock, composition, transformation, custody, proof, quality, path and crosswalk checks are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Role, purpose, confidentiality, personal data, location sensitivity, minimum graph projection and audit are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Corrections, contested sets, recall or legal hold, withdrawal and tombstones are explicit and non-cascading."},
            {"dimension": "interoperability", "status": "covered", "notes": "GS1, UN/CEFACT, ISO, FDA, EU, DCSA, IATA, RFC, PROV, DQV, ODRL and Data Integrity mappings disclose loss."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Scope registration, object and event linking, custody assertion, proof, correction, query, exposure and projection declare controlled effects."},
        ],
        "known_omissions": [
            "Sector, jurisdiction, chain-of-custody claim, certification, customs, dangerous-goods, safety, privacy, security, licensing and retention profiles require exact current rules and competent review.",
            "Objects, events, movements, parties, places, handovers, observations, documents, credentials, claims, recall actions and evidence lifecycles remain in neighboring models.",
            "Certified field crosswalks, identity resolution, graph completeness metrics, secure federation, signature suites, exposure algorithms, recall decision rules and legal evidence requirements remain future work.",
        ],
        "conflicts": [
            "Traceability covers product history and relationship paths, tracking often emphasizes current location or status, and chain of custody governs characteristic attribution; the model requires an explicit semantic kind and profile.",
            "Physical segregation, controlled blending, mass balance and book-and-claim permit different relationships between physical material and attributed characteristics and cannot share one inference rule.",
            "An event assertion, document, digest, signature, credential and successful verification establish different properties and do not by themselves prove real-world truth, custody or product conformity.",
        ],
        "regional_assumptions": [
            "FDA food traceability and EU Digital Product Passport are jurisdictional and product-scope profiles rather than universal supply-chain rules.",
            "DCSA and IATA are maritime-container and air-cargo modal profiles and do not define all transport or custody contexts.",
            "Recall, certification, title, custody, privacy, security, retention and evidential consequences depend on sector, contract and jurisdiction.",
        ],
        "adversarial_checks": [
            "Reject a trace without stable scope identity, semantic kind, revision, object and event range, graph basis, source authority and lineage.",
            "Reject traceability, tracking, chain of custody, provenance, audit log, shipment history and distributed software trace treated as universal aliases.",
            "Reject custody inferred from location, ownership inferred from custody, conformity inferred from a signature or recall inferred from an exposure result.",
            "Reject aggregation and transformation collapsed into one relationship or membership represented without a validity interval and source.",
            "Reject event, observation, record, ingestion and correction times collapsed into one timestamp.",
            "Reject last-write-wins when sources conflict; preserve competing assertions, gaps, evidence, correction and precedence policy.",
            "Reject protected graph disclosure, certification, recall, enforcement or record destruction outside delegated authority.",
        ],
    }


def build():
    model = {
        "registry_id": "vr.wm-flw-013", "model_id": "WM-FLW-013", "name": "Supply-chain Trace / Chain of Custody", "entry_kind": "pattern",
        "purpose": "Provide a reusable governed pattern for linking traceable objects, events, custody assertions, transformations, locations, parties and evidence into a federated time-aware trace graph with qualified queries, gaps and corrections.",
        "scope_statement": "Owns trace scope, semantic kind and graph revision; trace objective, range, direction and chain-of-custody profile; typed bindings to objects, events, parties, places, movements and evidence; aggregation, transformation and custody edges; qualified clocks, sources, proof and quality; gaps, duplicates, conflicts, error declarations and successors; backward, forward, path and exposure query results; federation, access, retention and loss-aware projections. Products, lots, serials, handling units, shipments, inventory movements, journeys, locations, parties, generic events, observations, custody handovers, documents, credentials, incidents, recall actions, claims and evidence masters remain external.",
        "in_scope": ["Trace scope, graph and result identity, objective, range, direction, semantic kind, revision and successor lineage", "Typed object-event graph, aggregation, transformation, location, party, custody, clock, source, evidence, proof, quality, gap and conflict assertions", "Backward and forward query, exposure analysis, federation, privacy, access, retention, audit and interoperability"],
        "out_of_scope": ["Owning product, lot, serial, handling unit, shipment, movement, journey, place, party, event, observation, handover, document, credential, incident, recall action, claim or evidence lifecycles", "Equating traceability with tracking, custody with ownership, aggregation with transformation, event assertion with verified fact, physical flow with mass balance or book-and-claim, or exposure result with recall decision", "Executing physical custody, product certification, identity issuance, evidence storage, recall, enforcement, protected disclosure or irreversible deletion"],
        "boundary_notes": [
            {"neighbor": "WM-FLW-004 Goods Movement / Logistics", "distinction": "Goods Movement owns physical logistics flow. Trace / Chain of Custody links source-qualified histories across movements and organizations; the candidate parent signal remains under review.", "source_refs": ["SRC-003", "SRC-007", "SRC-008", "SRC-016"]},
            {"neighbor": "WM-ACT-015 Occurrence / Event", "distinction": "The trace pattern composes typed event references and graph edges. Generic event identity, occurrence semantics and lifecycle remain external; the candidate COMPOSE relation is accepted only in that limited sense.", "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-021"]},
            {"neighbor": "WM-FLW-011 Shipment / Consignment", "distinction": "Shipment / Consignment owns commercial or transport grouping and status assertions. The trace graph references it as an object and event context without importing that lifecycle.", "source_refs": ["SRC-007", "SRC-008", "SRC-016", "SRC-017", "SRC-018"]},
            {"neighbor": "WM-FLW-012 Inventory Movement", "distinction": "Inventory Movement owns one stock-affecting transition and external posting reference. The trace graph links movements across organizations but does not calculate stock positions or post ledgers.", "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-014"]},
            {"neighbor": "Custody handover and ownership", "distinction": "The pattern links custody intervals, transfers, acceptance and refusal assertions. The handover event and legal ownership remain independently mastered and must not be inferred from location alone.", "source_refs": ["SRC-003", "SRC-010", "SRC-012", "SRC-013", "SRC-021"]},
            {"neighbor": "Evidence, credential and certification", "distinction": "Artifacts, digests, signatures, credentials and verification results are references that support assertions. Their issuance, storage, cryptographic validity, certification scope and legal effect remain external.", "source_refs": ["SRC-013", "SRC-020", "SRC-021", "SRC-022", "SRC-024"]},
            {"neighbor": "Recall, investigation and enforcement", "distinction": "The pattern may derive a qualified affected set with gaps and uncertainty. Accountable domain authorities own recall, alert, enforcement, remedy and public-disclosure decisions.", "source_refs": ["SRC-003", "SRC-006", "SRC-012", "SRC-014", "SRC-015"]},
        ],
    }
    composition = [
        {"target": "WM-FLW-004 Goods Movement / Logistics", "relation": "REFERENCE", "purpose": "Resolve broader logistics flow while the candidate parent relation remains under joint boundary review.", "required": False, "source_refs": ["SRC-003", "SRC-007", "SRC-008", "SRC-016"]},
        {"target": "WM-ACT-015 Occurrence / Event", "relation": "COMPOSE", "purpose": "Compose typed event references into the trace graph without importing generic event identity or lifecycle.", "required": True, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-021"]},
        {"target": "WM-FLW-011 Shipment / Consignment and WM-FLW-012 Inventory Movement", "relation": "REFERENCE", "purpose": "Resolve logistics groupings and stock-affecting transitions while trace owns only cross-source graph linkage.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-007", "SRC-008", "SRC-014", "SRC-016", "SRC-017"]},
        {"target": "Product, lot, serial, handling-unit, place and party masters", "relation": "REFERENCE", "purpose": "Resolve traceable objects and participants while preserving external identity and lifecycle authority.", "required": True, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-014", "SRC-015"]},
        {"target": "Custody handover, document, credential, claim, recall and evidence masters", "relation": "REFERENCE", "purpose": "Resolve supporting records and accountable decisions without converting them into trace-owned payloads.", "required": False, "source_refs": ["SRC-003", "SRC-010", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-021", "SRC-024"]},
        {"target": "GS1 EPCIS 2.0.1, CBV 2.0.0 and Global Traceability 2.0", "relation": "ALIGN", "purpose": "Project critical events, objects, aggregation, transformation, locations, business context, queries and error declarations.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006"]},
        {"target": "UN/CEFACT Integrated Track and Trace", "relation": "ALIGN", "purpose": "Project cross-industry multimodal visibility and delegated event-registry views.", "required": False, "source_refs": ["SRC-007", "SRC-008", "SRC-009"]},
        {"target": "ISO 22095, ISO 22095-2, ISO 22005 and ISO 28000", "relation": "ALIGN", "purpose": "Project generic custody models, mass-balance attribution, food traceability and security management as pinned profiles.", "required": False, "source_refs": ["SRC-010", "SRC-011", "SRC-012", "SRC-013"]},
        {"target": "FDA Food Traceability Rule and EU Digital Product Passport", "relation": "ALIGN", "purpose": "Project jurisdiction-specific trace records, lots, critical events, product identifiers, access and retention duties.", "required": False, "source_refs": ["SRC-014", "SRC-015"]},
        {"target": "DCSA Track and Trace and IATA ONE Record", "relation": "ALIGN", "purpose": "Project container-shipping and air-cargo event and federation views as modal profiles.", "required": False, "source_refs": ["SRC-016", "SRC-017", "SRC-018"]},
        {"target": "RFC 3339, RFC 8785, PROV-O, DQV, ODRL and Data Integrity", "relation": "ALIGN", "purpose": "Project temporal, canonicalization, provenance, quality, access and proof semantics with exact pins and loss declarations.", "required": False, "source_refs": ["SRC-019", "SRC-020", "SRC-021", "SRC-022", "SRC-023", "SRC-024"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": BASE.structure(), "functions": BASE.functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
