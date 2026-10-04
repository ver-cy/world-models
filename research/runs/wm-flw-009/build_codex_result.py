#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-FLW-009."""

import json
from pathlib import Path


RUN = Path(__file__).resolve().parent
AT = "2026-09-06T19:58:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "Transmodel v6.2 Data Dictionary", "CEN Transmodel", "https://transmodel-cen.eu/wp-content/uploads/2024/09/Transmodel-v6.2-Data-Dictionary.pdf", "Transmodel v6.2, September 2024", "standard", "Defines passenger trips, trip patterns, legs, vehicle journeys, service journeys, calls and related transport concepts."),
    src(2, "Passenger Information Tutorial", "CEN Transmodel", "https://transmodel-cen.eu/index.php/passenger-information-tutorial/", "Tutorial accessed 2026-09-06", "first-party-doc", "Explains that a passenger trip is movement between places, may contain consecutive legs and differs from a vehicle journey."),
    src(3, "Transmodel at a glance", "CEN Transmodel", "https://transmodel-cen.eu/index.php/transmodel-at-a-glance/", "Transmodel v6 overview accessed 2026-09-06", "first-party-doc", "Separates service journey, vehicle journey, dead run, journey pattern and operating block."),
    src(4, "GTFS Schedule Reference", "MobilityData", "https://gtfs.org/documentation/schedule/reference/", "Living specification accessed 2026-09-06", "standard", "Defines routes, trips, service dates, stops, stop sequences, shapes, frequencies and scheduled passing times."),
    src(5, "GTFS Realtime Reference", "MobilityData", "https://gtfs.org/documentation/realtime/reference/", "GTFS Realtime 2.0, accessed 2026-09-06", "standard", "Defines trip updates, vehicle positions, stop-time predictions, schedule relationships, service alerts and observation timestamps."),
    src(6, "GTFS Realtime Trip Updates", "MobilityData", "https://gtfs.org/documentation/realtime/feed-entities/trip-updates/", "Guidance accessed 2026-09-06", "first-party-doc", "Distinguishes scheduled trips, predictions, measured past events, cancellation, addition, rerouting and uncertainty."),
    src(7, "OGC Moving Features standards", "Open Geospatial Consortium", "https://www.ogc.org/standards/movingfeatures/", "Standards catalogue accessed 2026-09-06", "standard", "Catalogues format-neutral movement concepts and XML, CSV, JSON and API projections."),
    src(8, "OGC API Moving Features Part 1 Core", "Open Geospatial Consortium", "https://docs.ogc.org/is/22-003r3/22-003r3.html", "OGC 22-003r3, version 1.0, 24 October 2024", "standard", "Defines moving-feature collections, static identity and access to temporal geometry and temporal properties."),
    src(9, "OGC Moving Features Access", "Open Geospatial Consortium", "https://docs.ogc.org/is/16-120r3/16-120r3.html", "OGC 16-120r3, version 1.0, 2017", "standard", "Defines trajectory operations including position, time and velocity queries and conformance tests."),
    src(10, "ISO 19141 Geographic information - Schema for moving features", "International Organization for Standardization", "https://www.iso.org/standard/41445.html", "ISO 19141:2008, confirmed 2022", "standard", "Defines geometric movement, planned-route deviation and moving-feature interactions while excluding non-spatial lifecycle change."),
    src(11, "Glossary for Transport Statistics, sixth edition", "UNECE, Eurostat and International Transport Forum", "https://unece.org/info/Transport/pub/411667", "Sixth edition, February 2026", "classifier", "Provides current harmonized transport terminology and statistical definitions across modes."),
    src(12, "National Travel Survey 2024: notes and definitions", "United Kingdom Department for Transport", "https://www.gov.uk/government/statistics/national-travel-survey-2024/nts-2024-notes-and-definitions", "Accredited Official Statistics, 2024 release", "public-authority", "Defines a trip as one-way travel with one main purpose and stages by mode or vehicle change."),
    src(13, "International Recommendations for Tourism Statistics 2008", "United Nations Statistics Division", "https://unstats.un.org/unsd/tradeserv/IRTS%202008%20edited%20whitecover.pdf", "ST/ESA/STAT/SER.M/83/Rev.1, 2010", "standard", "Defines tourism-trip purpose, origin, destination, duration, mode, travel party and the boundary between travel and tourism."),
    src(14, "Commission Delegated Regulation (EU) 2024/490", "European Union", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R0490", "29 November 2023, published 13 February 2024", "legislation", "Amends EU multimodal travel-information rules and distinguishes static, historic, observed and dynamic data."),
    src(15, "Trip", "Schema.org Community Group", "https://schema.org/Trip", "Vocabulary page accessed 2026-09-06", "ontology", "Provides a lightweight web alignment for trip, itinerary, subtrip, provider, departure and arrival."),
    src(16, "GeoSPARQL", "Open Geospatial Consortium", "https://www.ogc.org/standards/geosparql/", "GeoSPARQL 1.1, OGC 22-047r1", "standard", "Defines interoperable geospatial feature, geometry and query semantics for place and path projections."),
    src(17, "Time Ontology in OWL", "World Wide Web Consortium", "https://www.w3.org/TR/owl-time/", "Candidate Recommendation Draft, 15 November 2022", "ontology", "Defines instants, intervals, duration, ordering, temporal position, reference systems and precision."),
    src(18, "RFC 3339: Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines interoperable timestamps with seconds and explicit offsets for journey event and observation clocks."),
    src(19, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines attribution, derivation, revision, invalidation and delegation for journey assertions and evidence."),
    src(20, "Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note, 15 December 2016", "ontology", "Defines quality measurements, annotations, policies and provenance for schedule, trajectory and reconciliation data."),
    src(21, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties and constraints for sensitive trip and live-location data."),
]


# bundle id, name, rationale, layers; layer id, name, refs, findings;
# finding id, name, primary question kind
ROWS = [
    ("journey-identity-class-and-subject", "Journey identity, class and subject", "Establish one movement episode without collapsing traveller, vehicle, route, itinerary or service masters.", [
        ("identity-scope-and-version", "Identity, scope and version", ["SRC-001", "SRC-002", "SRC-004", "SRC-011", "SRC-019"], [
            ("journey-identity-namespace-version-and-successor", "Journey identity, namespace, version and successor", "identity"),
            ("journey-boundary-origin-destination-and-completion-rule", "Journey boundary, origin, destination and completion rule", "definition"),
        ]),
        ("kind-subject-purpose-and-grouping", "Kind, subject, purpose and grouping", ["SRC-001", "SRC-002", "SRC-003", "SRC-011", "SRC-012", "SRC-013"], [
            ("person-trip-vehicle-journey-service-journey-and-dead-run-kind", "Person trip, vehicle journey, service journey and dead run kind", "classification"),
            ("traveller-vehicle-trip-purpose-wider-travel-and-subtrip", "Traveller, vehicle, trip purpose, wider travel and subtrip", "relationship"),
        ]),
    ]),
    ("places-paths-legs-and-modes", "Places, paths, legs and modes", "Represent ordered movement composition while places, routes, networks and transport assets retain external authority.", [
        ("endpoints-calls-and-path", "Endpoints, calls and path", ["SRC-001", "SRC-002", "SRC-004", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-016"], [
            ("origin-destination-via-place-stop-call-and-activity-place", "Origin, destination, via place, stop, call and activity place", "spatial"),
            ("route-journey-pattern-shape-trajectory-and-deviation-reference", "Route, journey pattern, shape, trajectory and deviation reference", "relationship"),
        ]),
        ("ordered-legs-modes-and-transfers", "Ordered legs, modes and transfers", ["SRC-001", "SRC-002", "SRC-004", "SRC-011", "SRC-012"], [
            ("leg-stage-sequence-mode-vehicle-service-and-predecessor", "Leg, stage, sequence, mode, vehicle, service and predecessor", "composition"),
            ("access-egress-transfer-connection-wait-and-interchange", "Access, egress, transfer, connection, wait and interchange", "process"),
        ]),
    ]),
    ("plan-time-and-traveller-constraints", "Plan, time and traveller constraints", "Keep plans and time assertions typed so a prediction or routing result cannot overwrite observed movement.", [
        ("time-basis-passing-and-duration", "Time basis, passing and duration", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-011", "SRC-017", "SRC-018"], [
            ("operating-day-time-zone-start-end-passing-and-duration", "Operating day, time zone, start, end, passing and duration", "temporal"),
            ("requested-planned-target-estimated-predicted-observed-and-actual-time", "Requested, planned, target, estimated, predicted, observed and actual time", "classification"),
        ]),
        ("plan-choice-and-constraints", "Plan choice and constraints", ["SRC-001", "SRC-002", "SRC-004", "SRC-012", "SRC-014", "SRC-015"], [
            ("journey-request-routing-result-selected-plan-itinerary-and-alternative", "Journey request, routing result, selected plan, itinerary and alternative", "decision"),
            ("accessibility-preference-party-luggage-mode-and-transfer-constraint", "Accessibility, preference, party, luggage, mode and transfer constraint", "constraint"),
        ]),
    ]),
    ("execution-progress-and-observation", "Execution, progress and observation", "Record what was reported or observed during the journey while operational services and sensors remain external masters.", [
        ("lifecycle-state-and-progress", "Lifecycle state and progress", ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-011", "SRC-019"], [
            ("proposed-confirmed-ready-started-in-progress-arrived-and-completed-state", "Proposed, confirmed, ready, started, in-progress, arrived and completed state", "lifecycle"),
            ("current-leg-call-stop-sequence-progress-and-completion-evidence", "Current leg, call, stop sequence, progress and completion evidence", "state"),
        ]),
        ("movement-observation-and-trajectory", "Movement observation and trajectory", ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-019"], [
            ("position-fix-bearing-speed-odometer-observation-time-and-device", "Position fix, bearing, speed, odometer, observation time and device", "measurement"),
            ("actual-trajectory-temporal-geometry-gap-interpolation-and-confidence", "Actual trajectory, temporal geometry, gap, interpolation and confidence", "evidence"),
        ]),
    ]),
    ("deviation-outcome-and-measures", "Deviation, outcome and measures", "Preserve disruption, outcome and measurement evidence without converting estimates into facts or incidents into journey identity.", [
        ("disruption-change-and-outcome", "Disruption, change and outcome", ["SRC-004", "SRC-005", "SRC-006", "SRC-010", "SRC-014", "SRC-019"], [
            ("delay-cancellation-diversion-interruption-missed-connection-and-recovery", "Delay, cancellation, diversion, interruption, missed connection and recovery", "exception"),
            ("boarding-alighting-no-show-abandonment-partial-completion-and-arrival-outcome", "Boarding, alighting, no-show, abandonment, partial completion and arrival outcome", "event"),
        ]),
        ("distance-performance-and-impact", "Distance, performance and impact", ["SRC-005", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-020"], [
            ("travelled-network-and-straight-line-distance-duration-wait-and-speed", "Travelled, network and straight-line distance, duration, wait and speed", "measurement"),
            ("occupancy-cost-energy-emissions-accessibility-and-service-quality-view", "Occupancy, cost, energy, emissions, accessibility and service-quality view", "quality"),
        ]),
    ]),
    ("governance-provenance-and-interoperability", "Governance, provenance and interoperability", "Make journey memory correctable, privacy-aware and safely projectable across incompatible vocabularies.", [
        ("provenance-reconciliation-and-lineage", "Provenance, reconciliation and lineage", ["SRC-004", "SRC-005", "SRC-006", "SRC-017", "SRC-018", "SRC-019", "SRC-020"], [
            ("source-actor-method-event-time-record-time-ingestion-time-and-assurance", "Source, actor, method, event time, record time, ingestion time and assurance", "provenance"),
            ("schedule-observation-conflict-correction-split-merge-and-successor", "Schedule-observation conflict, correction, split, merge and successor", "validation"),
        ]),
        ("access-retention-and-projections", "Access, retention and projections", ["SRC-001", "SRC-004", "SRC-005", "SRC-007", "SRC-008", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019", "SRC-020", "SRC-021"], [
            ("traveller-location-sensitivity-consent-purpose-access-legal-hold-and-retention", "Traveller location sensitivity, consent, purpose, access, legal hold and retention", "privacy"),
            ("transmodel-gtfs-moving-features-statistical-schema-org-time-and-provenance-projection", "Transmodel, GTFS, Moving Features, statistical, Schema.org, time and provenance projection", "interoperability"),
        ]),
    ]),
]


KIND_CYCLE = [
    "identity", "classification", "composition", "relationship", "state",
    "lifecycle", "temporal", "spatial", "provenance", "ownership",
    "authority", "constraint", "process", "event", "measurement", "evidence",
    "quality", "validation", "security", "privacy", "retention", "access",
    "exception", "interoperability", "decision",
]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 7) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 15) % len(KIND_CYCLE)]]
    questions = [
        {
            "id": f"{fid}-q01",
            "text": f"Which journey identity, class, subject, endpoint, leg, time basis and source establish {lower}?",
            "kind": kinds[0],
            "answer_data": ["journey and revision identifier, namespace, kind and lifecycle status", "traveller, vehicle, operator, service, route, place and leg references", "planned, predicted, observed and actual time with source and confidence"],
        },
        {
            "id": f"{fid}-q02",
            "text": f"Who planned, undertook, operated, observed, asserted, corrected or may access {lower}, and under what role or authority?",
            "kind": kinds[1],
            "answer_data": ["traveller, driver, operator, planner, observer, steward and authority roles", "delegation, consent, purpose, access scope, jurisdiction and applicable policy", "assertion owner, evidence issuer, reviewer, correction actor and disputed state"],
        },
        {
            "id": f"{fid}-q03",
            "text": f"Which ordered components, measurements, uncertainties, exceptions, evidence and lineage qualify {lower}?",
            "kind": kinds[2],
            "answer_data": ["origin, destination, calls, stages, modes, connections, sequence and dependencies", "distance, duration, waiting, speed, occupancy, gap, tolerance and uncertainty", "source snapshot, digest, event and ingestion clocks, conflict, correction and semantic-loss declaration"],
        },
    ]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {lower} as source-qualified Journey / Trip context while route, itinerary, service, schedule, place, person, vehicle, booking, ticket, shipment, incident and sensor masters remain external.",
        "source_refs": refs,
        "questions": questions,
        "data_elements": [{
            "id": f"{fid}-data", "name": f"{name} data",
            "description": f"Typed journey-scoped values and references needed to answer the governed questions for {lower}.",
            "value_kind": "object", "cardinality": "1", "required": True,
            "source_refs": refs,
        }],
        "artifacts": [{
            "id": f"{fid}-artifact", "name": f"{name} evidence manifest",
            "description": f"Digest-addressed manifest of plans, observations, mappings, corrections and external records supporting {lower}.",
            "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"],
            "serial": True,
            "identity_strategy": "Authoritative journey master-system identifier first, otherwise governed IRI, then Dimension UUID or ULID; include immutable revision and digest.",
            "source_refs": refs,
        }],
        "inline_only_rationale": None,
    }


def structure():
    bundles = []
    ordinal = 0
    for bid, bname, rationale, layers in ROWS:
        built_layers = []
        bundle_refs = []
        for lid, lname, refs, findings in layers:
            bundle_refs.extend(refs)
            built_findings = []
            for item in findings:
                ordinal += 1
                built_findings.append(make_finding(item, ordinal, refs))
            built_layers.append({
                "id": lid, "name": lname,
                "description": f"Groups Journey / Trip context for {lname.lower()} without importing neighboring master lifecycles.",
                "source_refs": refs, "findings": built_findings,
            })
        bundles.append({
            "id": bid, "name": bname,
            "description": f"Groups the governed Journey / Trip concern for {bname.lower()}.",
            "rationale": rationale,
            "source_refs": list(dict.fromkeys(bundle_refs)),
            "layers": built_layers,
        })
    return {"bundles": bundles}


FUNCTION_ROWS = [
    ("register-journey", "Register journey", "Create one governed journey identity and boundary.", ["subject and role references", "origin and destination", "journey kind and time basis"], ["journey identifier", "initial revision"], ["active Dimension", "create authority"], ["journey identity and explicit unknowns are appended"], ["SRC-001", "SRC-002", "SRC-004", "SRC-019"]),
    ("bind-participants", "Bind participants", "Bind traveller, driver, operator, vehicle and service roles without importing their lifecycles.", ["journey identifier", "party, vehicle and service references", "role intervals"], ["typed participant bindings"], ["resolved master identities"], ["role-qualified references are appended"], ["SRC-001", "SRC-003", "SRC-004"]),
    ("compose-legs", "Compose ordered legs", "Append stages, modes, endpoints, calls and connection dependencies.", ["journey identifier", "leg definitions", "route and place references"], ["validated ordered leg graph"], ["stable journey revision"], ["leg composition is versioned without mutating route masters"], ["SRC-001", "SRC-002", "SRC-004", "SRC-012"]),
    ("record-plan", "Record selected plan", "Record requested, proposed or selected movement plan and alternatives.", ["journey request", "routing result", "selection rationale"], ["typed plan assertion", "successor relation"], ["planner authority", "time and accessibility constraints"], ["plan is appended and remains distinct from actual movement"], ["SRC-001", "SRC-002", "SRC-014"]),
    ("record-observation", "Record journey observation", "Append calls, passing times, position fixes and other journey-scoped observations.", ["journey identifier", "observation", "source and clocks"], ["immutable observation assertion"], ["recognized subject", "source provenance"], ["evidence is appended without erasing plan or prediction"], ["SRC-005", "SRC-006", "SRC-008", "SRC-019"]),
    ("derive-progress", "Derive progress and state", "Derive current leg, progress and lifecycle state from qualified evidence.", ["journey revision", "plans", "observations"], ["derived state view", "derivation trace"], ["deterministic state policy"], ["view is refreshed without rewriting evidence"], ["SRC-004", "SRC-005", "SRC-006", "SRC-019"]),
    ("reconcile-times", "Reconcile journey times", "Compare requested, planned, predicted, observed and actual times.", ["time assertions", "operating-day basis", "tolerance policy"], ["reconciliation result", "conflict set"], ["timezone and source known"], ["differences and precedence are recorded"], ["SRC-001", "SRC-004", "SRC-005", "SRC-017", "SRC-018", "SRC-020"]),
    ("handle-deviation", "Handle deviation", "Register disruption, impact, recovery, diversion or successor plan without overwriting history.", ["journey identifier", "exception evidence", "authorized response"], ["exception record", "successor plan reference"], ["response authority", "affected scope"], ["deviation and recovery lineage are appended"], ["SRC-005", "SRC-006", "SRC-010", "SRC-014", "SRC-019"]),
    ("calculate-measures", "Calculate journey measures", "Calculate qualified distance, duration, wait, speed and impact views.", ["trajectory or leg data", "method", "units and uncertainty"], ["versioned measurement view"], ["declared method and source coverage"], ["measurements remain derivations rather than journey identity"], ["SRC-009", "SRC-010", "SRC-011", "SRC-020"]),
    ("project-journey", "Project journey", "Produce minimum-necessary standards-aligned or stakeholder views.", ["journey revision", "target profile", "access purpose"], ["versioned projection", "semantic-loss declaration"], ["authorized recipient", "pinned target version"], ["projection is logged and source identity is preserved"], ["SRC-001", "SRC-004", "SRC-005", "SRC-007", "SRC-008", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-019", "SRC-020", "SRC-021"]),
]


def functions():
    keys = ["id", "name", "description", "inputs", "outputs", "preconditions", "effects", "source_refs"]
    return [dict(zip(keys, row)) for row in FUNCTION_ROWS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, responsible stewards and authority for personal, organizational, fleet and public-service journey records.",
                "Register authoritative person, vehicle, operator, route, itinerary, service, schedule, place, booking, ticket, shipment, incident, sensor and evidence masters.",
                "Publish journey, relation, event, identifier, access, retention, assurance and interoperability registries.",
                "Pin mode, region, operating-day, time-zone, accessibility, privacy, safety and exchange profiles.",
            ],
            "namespace_guidance": "Mint journey, revision, leg, observation, exception and projection identifiers only in the adopting Dimension namespace; preserve person, vehicle, operator, route, itinerary, service, schedule, place, booking, ticket, shipment, incident and sensor identities as typed external references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local journey, identifier, event, access, retention and provenance registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, authoritative journey master ID, immutable revision, journey kind, subject, origin, destination and time basis; never use date, route, ticket, vehicle, filename or hash alone as identity.",
                "Keep person trip, vehicle journey, service journey, route, itinerary, leg, stage, call, position observation, trajectory and wider travel distinct and preserve corrections and successors.",
            ],
            "patch_rules": [
                "Additive extensions use a Dimension-owned namespace and declare target node, mode or jurisdiction profile, authority, source, rationale, access, time and interoperability impact.",
                "Breaking changes require a new version, migration and crosswalk maps, compatibility declaration and continued resolution of prior journey revisions and identifiers.",
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when journey identity, kind, subject, endpoints, leg order, time kind, status, authority, provenance and access meaning remain intact.",
                "Transmodel, GTFS, Moving Features, statistical, Schema.org, GeoSPARQL, OWL-Time and provenance mappings pin source and target versions and declare transformed, omitted or non-round-trippable values.",
            ],
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative journey master-system identifier and immutable revision identifier.",
                "Governed globally resolvable journey, leg or observation IRI.",
                "Adopting-Dimension UUID or ULID when no authoritative external identifier exists.",
            ],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep requested, planned, target, estimated, predicted, observed, actual, record, correction and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {journey-id}--{artifact-kind}--{revision-or-event-id}; never use a date, route, place, vehicle, traveller, ticket, filename or hash alone as journey identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and vocabulary versions, journey scope, event and record times, provenance, assurance and access marking for each retained serial artifact.",
        },
        "policies": [
            "The adopting Dimension declares who may create, plan, bind, observe, correct, derive, disclose, retain and tombstone journey records.",
            "Every journey assertion requires journey and revision identity, kind, subject or vehicle, endpoint or leg scope, time kind, source, authority, confidence, status and lineage as applicable.",
            "Agents never infer actual movement, passenger presence, boarding, completion, incident causality or entitlement from a plan, prediction, ticket, position fix or status label alone.",
            "Route, itinerary, person, vehicle, service, schedule, place, booking, ticket, shipment, incident, payment, sensor and evidence masters remain external.",
            "Automated agents may append low-risk observations, reconciliations and projections under delegation, but consequential rerouting, safety action, protected live-location disclosure and irreversible deletion require accountable authority.",
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, journey kind, subject scope, time horizon, requested revision, assurance, freshness and access policy; return the minimum permitted projection."],
            "create": ["Create stable journey identity, kind, subject, origin, destination, temporal basis, source, authority and explicit unknowns before adding plans or observations."],
            "update": ["Append an immutable plan, observation, state or correction revision with actor, authority, reason, RFC 3339 effective time and predecessor; validate composition, clocks, evidence and access."],
            "delete": ["Apply privacy, safety, dispute, audit, retention and legal-hold policy; tombstone eligible Journey-owned records or withdraw projections while preserving identity, material provenance and non-cascading external references. The adopting Dimension retention policy owns execution."],
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Journey steward", "responsibilities": ["Own journey boundary, composition, plan assertions, status derivation and reconciliation."]},
            {"name": "Traveller or vehicle steward", "responsibilities": ["Maintain authoritative subject identity, consent, role and permitted journey linkage."]},
            {"name": "Transport operator", "responsibilities": ["Own service, schedule, vehicle-journey and operational observations it performs."]},
            {"name": "Observation or data steward", "responsibilities": ["Govern devices, sources, clocks, quality, mappings and correction lineage."]},
            {"name": "Safety or regulatory authority", "responsibilities": ["Own restrictions, interventions and jurisdictional decisions outside Journey mastership."]},
            {"name": "Reviewer or auditor", "responsibilities": ["Review evidence, conflicts, corrections and protected use without rewriting originals."]},
            {"name": "Disclosure authority", "responsibilities": ["Approve recipient, purpose, location exposure, redaction and publication timing."]},
        ],
        "access": {
            "default_rule": "Deny mutation and sensitive disclosure unless the active Dimension, role, purpose, journey kind, subject, location sensitivity and field policy grant the action; expose the minimum necessary projection.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency access must be time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable journey, correction or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, journey and revision identity, action, decision, policy and vocabulary versions, RFC 3339 timestamp with offset, affected fields, source evidence and outcome for privileged mutation or disclosure."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": [
                "Read the nearest Dimension-owner AGENTS.md, journey authority, active mode, jurisdiction, time, access, retention and disclosure policies.",
                "Read this model AGENTS.md, pinned spec.yaml and required person, vehicle, route, itinerary, service, schedule, place, booking, ticket, shipment, incident, sensor and evidence model instructions before mutation.",
            ],
        },
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Journey / Trip identity, subject and purpose, endpoints and ordered legs, plans and clocks, execution observations, trajectory, deviations, measures, provenance, privacy, retention and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Journey, revision, wider travel, subtrip, leg, call, observation, exception and projection identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Person trip, vehicle journey, service journey, dead run, wider travel and statistical profiles are typed rather than merged."},
            {"dimension": "direct properties", "status": "covered", "notes": "Journey-owned kind, endpoints, composition, time assertions, state and outcome are covered while external masters retain their direct properties."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Plan, prediction, report, measured position, passing event, actual trajectory and correction are distinguished by type, source and clocks."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Proposed, selected, confirmed, ready, started, in-progress, interrupted, diverted, cancelled, arrived, completed, corrected and tombstoned states preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Subjects, parties, vehicles, services, routes, itineraries, places, legs, bookings, tickets, shipments, incidents, sensors and evidence use typed bindings."},
            {"dimension": "temporal", "status": "covered", "notes": "Operating day, time zone, requested, planned, target, predicted, observed, actual, record, correction and ingestion clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Origin, destination, via places, stops, calls, paths, shapes, trajectories, CRS, gaps and uncertainty are explicit."},
            {"dimension": "provenance", "status": "covered", "notes": "Sources, actors, methods, evidence snapshots, derivations, revisions and invalidations are linked."},
            {"dimension": "ownership", "status": "covered", "notes": "Dimension owner, journey steward, traveller or vehicle steward, operator, data steward, authority, reviewer and disclosure authority have separate responsibilities."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, leg order, endpoint continuity, clock, route, schedule, trajectory, state, correction and crosswalk checks are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Role, purpose, consent, delegation, location sensitivity, minimum projection, emergency access and audit are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Immutable observations, corrections, disputes, legal hold, withdrawal and tombstones are explicit and non-cascading."},
            {"dimension": "interoperability", "status": "covered", "notes": "Transmodel, GTFS, OGC, ISO, statistical, Schema.org, GeoSPARQL, OWL-Time, PROV, DQV and ODRL mappings pin versions and disclose loss."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Registration, binding, composition, planning, observation, state derivation, time reconciliation, deviation handling, measurement and projection functions declare controlled effects."},
        ],
        "known_omissions": [
            "Mode, jurisdiction, safety, immigration, border, accessibility, passenger-rights, employment-travel, privacy and retention profiles require exact current rules and competent review.",
            "Person, organization, vehicle, route, itinerary, network, place, service, schedule, booking, ticket, fare, shipment, incident, payment, sensor and evidence lifecycles remain in neighboring masters.",
            "Certified field crosswalks, trajectory-matching algorithms, trip-segmentation rules, prediction benchmarks and legal proof requirements remain future work.",
        ],
        "conflicts": [
            "Trip and journey have different meanings across Transmodel, GTFS, transport statistics, tourism and ordinary language; the model requires an explicit journey kind and source profile.",
            "A person trip, passenger boarding, vehicle journey, service journey and wider return journey cannot share one count or identity without declared aggregation semantics.",
            "Planned route, routing result, selected itinerary, scheduled service, predicted movement, position samples and actual trajectory are different assertion classes.",
        ],
        "regional_assumptions": [
            "EU multimodal information rules and UK travel-survey definitions are regional profiles, not universal journey law.",
            "Transmodel and GTFS primarily describe passenger transport and service data; private, pedestrian, freight-linked and non-service vehicle journeys need explicit profiles.",
            "Tourism-statistics purpose and duration definitions apply only when the relevant statistical population and usual-environment tests are satisfied.",
        ],
        "adversarial_checks": [
            "Reject a journey without stable identity or declared composite key, kind, subject, origin, destination, temporal basis, source and revision lineage.",
            "Reject a route, itinerary, booking, ticket, vehicle, service or position fix represented as the journey itself.",
            "Reject planned, target, predicted, observed and actual times collapsed into one timestamp or interpreted without operating-day and timezone rules.",
            "Reject a passenger boarding or vehicle run counted as a whole personal trip without declared aggregation and purpose semantics.",
            "Reject last-write-wins when schedule and observations conflict; preserve source, event time, record time, uncertainty, correction and precedence.",
            "Reject protected live-location disclosure, consequential rerouting or record destruction outside delegated authority and retention policy.",
        ],
    }


def build():
    model = {
        "registry_id": "vr.wm-flw-009", "model_id": "WM-FLW-009",
        "name": "Journey / Trip", "entry_kind": "aggregate",
        "purpose": "Represent one governed planned or actual movement of a person or vehicle between declared endpoints with ordered legs, typed clocks, observations and correction lineage without becoming its route, itinerary, service, subject or booking.",
        "scope_statement": "Owns journey and revision identity, kind and boundary; subject and journey-role bindings; origin, destination, calls and journey-scoped endpoint assertions; ordered leg or stage composition; purpose and wider-travel relationships; requested, planned, target, estimated, predicted, observed and actual clocks; selected-plan references and journey constraints; lifecycle and progress assertions; position and trajectory evidence links; disruption, outcome, measurement, provenance, reconciliation, access, retention and loss-aware projections. Person, vehicle, organization, route, itinerary, network, place, stop, service, schedule, booking, ticket, fare, shipment, incident, weather, payment, sensor, evidence and document masters remain external.",
        "in_scope": [
            "Journey identity, revision, kind, subject roles, origin, destination, purpose, wider travel and subtrip relationships",
            "Ordered legs, stages, modes, calls, route and service references, selected plan, typed times, execution state, progress and trajectory evidence",
            "Deviations, outcomes, derived measures, reconciliation, provenance, privacy, access, retention and interoperability",
        ],
        "out_of_scope": [
            "Owning person, organization, vehicle, route, itinerary, network, place, stop, service, schedule, booking, ticket, fare, shipment, incident, weather, payment, sensor, evidence or document master lifecycles",
            "Equating a person trip with a vehicle journey, a route with an itinerary, a plan with actual movement, a position fix with a trajectory, boarding with a whole trip or a statistical count with operational truth",
            "Autonomous consequential rerouting, safety intervention, passenger-rights determination, border or regulatory decision, protected live-location disclosure or irreversible deletion",
        ],
        "boundary_notes": [
            {"neighbor": "WM-FLW-007 Passenger Mobility / Transit", "distinction": "Passenger Mobility owns transit networks, services, schedules, fares and aggregate mobility context. Journey / Trip owns one movement episode and may reference transit service or passenger-trip views without assuming inheritance.", "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004"]},
            {"neighbor": "WM-FLW-010 Route / Itinerary", "distinction": "A route is a reusable or selected spatial path and an itinerary is a planning result or ordered visit plan. A journey is the identity-bearing intended or undertaken movement that references them and preserves actual divergence.", "source_refs": ["SRC-001", "SRC-002", "SRC-010", "SRC-014", "SRC-015"]},
            {"neighbor": "Person, Vehicle, Organization and Transport Service", "distinction": "The journey assigns journey-scoped roles and references. Subject identity, vehicle lifecycle, operator authority, network, schedule and service operation remain externally mastered.", "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005"]},
            {"neighbor": "WM-FLW-011 Shipment / Consignment", "distinction": "A shipment may reference one or more transport journeys. Cargo, consignment, custody and logistics lifecycle remain shipment-owned and do not become journey composition.", "source_refs": ["SRC-010", "SRC-011"]},
            {"neighbor": "Observation, Sensor, Incident and Evidence", "distinction": "The journey binds source-qualified position, passing, disruption and completion assertions. Sensor streams, generic incidents and evidentiary records retain independent identity and authority.", "source_refs": ["SRC-005", "SRC-006", "SRC-008", "SRC-009", "SRC-019"]},
            {"neighbor": "Travel, Tour and Tourism Trip", "distinction": "A wider travel episode or return journey may contain multiple one-way trips and activities. Tourism status depends on purpose, destination, usual environment and duration under a statistical profile.", "source_refs": ["SRC-011", "SRC-012", "SRC-013"]},
        ],
    }
    composition = [
        {"target": "WM-FLW-007 Passenger Mobility / Transit", "relation": "REFERENCE", "purpose": "Resolve transit network, service, schedule, fare and mobility context without inheriting the broader model's lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"]},
        {"target": "WM-FLW-010 Route / Itinerary", "relation": "REFERENCE", "purpose": "Resolve reusable paths and planning results while preserving journey identity and actual divergence.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-010", "SRC-014", "SRC-015"]},
        {"target": "Person, Vehicle, Organization, Place, Service, Schedule, Booking, Ticket, Shipment, Incident, Sensor and Evidence models", "relation": "REFERENCE", "purpose": "Resolve external masters without duplicating their identity, authority or lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-004", "SRC-005", "SRC-008", "SRC-010", "SRC-019"]},
        {"target": "Transmodel v6.2 and GTFS Schedule and Realtime", "relation": "ALIGN", "purpose": "Project passenger-trip and vehicle-journey views with explicit vocabulary and version mappings.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006"]},
        {"target": "OGC and ISO Moving Features and GeoSPARQL", "relation": "ALIGN", "purpose": "Project actual movement, temporal geometry and spatial-query views with CRS, gap and conformance controls.", "required": False, "source_refs": ["SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-016"]},
        {"target": "UNECE transport statistics, UN tourism statistics and Schema.org Trip", "relation": "ALIGN", "purpose": "Project statistical and web-discovery views without treating their trip boundaries as universal.", "required": False, "source_refs": ["SRC-011", "SRC-012", "SRC-013", "SRC-015"]},
        {"target": "OWL-Time, RFC 3339, PROV-O, DQV and ODRL", "relation": "ALIGN", "purpose": "Project temporal, provenance, quality and access semantics with exact pins and semantic-loss declarations.", "required": False, "source_refs": ["SRC-017", "SRC-018", "SRC-019", "SRC-020", "SRC-021"]},
    ]
    return {
        "schema_version": "1.0.0", "model": model, "sources": SOURCES,
        "structure": structure(), "functions": functions(),
        "composition": composition, "service_layers": services(),
        "coverage": coverage(),
    }


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(
        json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

