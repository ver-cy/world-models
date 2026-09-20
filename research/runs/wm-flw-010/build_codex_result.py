#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-FLW-010."""

import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T20:18:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "Transmodel v6.2 Data Dictionary", "CEN Transmodel", "https://transmodel-cen.eu/wp-content/uploads/2024/09/Transmodel-v6.2-Data-Dictionary.pdf", "Transmodel v6.2, September 2024", "standard", "Defines ROUTE, LINK SEQUENCE, JOURNEY PATTERN, journey and timing concepts."),
    src(2, "Transmodel at a glance", "CEN Transmodel", "https://www.transmodel-cen.eu/wp-content/uploads/2015/01/Transmodel_at_a_-glance-1.pdf", "Overview accessed 2026-09-06", "first-party-doc", "Explains route points, physical path projection and ordered journey patterns."),
    src(3, "NeTEx", "CEN NeTEx", "https://netex-cen.eu/", "CEN TS 16614 family, site accessed 2026-09-06", "standard", "Official European exchange family for public-transport networks, schedules and related route structures."),
    src(4, "GTFS Schedule Reference", "MobilityData", "https://gtfs.org/documentation/schedule/reference/", "Living specification accessed 2026-09-06", "standard", "Defines routes, trips, stop times, shapes, calendars and transfers, with semantics distinct from Transmodel."),
    src(5, "OGC API - Routes overview", "Open Geospatial Consortium", "https://ogcapi.ogc.org/routes/overview.html", "Developing specification accessed 2026-09-06", "first-party-doc", "Describes engine-independent route requests, parameters, asynchronous execution and route profiles."),
    src(6, "OGC Routing Pilot Engineering Report", "Open Geospatial Consortium", "https://docs.ogc.org/per/19-041r3.html", "OGC 19-041r3, 2020", "first-party-doc", "Defines a pilot Route Exchange Model with definition, overview, segments, endpoints and status."),
    src(7, "WPS Routing API Engineering Report", "Open Geospatial Consortium", "https://docs.ogc.org/per/19-040.html", "OGC 19-040, 2020", "first-party-doc", "Defines route computation inputs including waypoints, temporal, height, load, obstacle, engine, algorithm and dataset choices."),
    src(8, "OGC Standards Roadmap", "Open Geospatial Consortium", "https://portal.ogc.org/public_ogc/standards/standards_workflow.php?bg=1", "Roadmap accessed 2026-09-06", "first-party-doc", "Shows OGC Route Exchange Model 21-001 as proposed rather than an approved standard."),
    src(9, "GeoSPARQL", "Open Geospatial Consortium", "https://www.ogc.org/standards/geosparql/", "GeoSPARQL 1.1, OGC 22-047r1", "standard", "Defines interoperable feature, geometry, spatial-relation and query semantics."),
    src(10, "RFC 7946: The GeoJSON Format", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc7946.html", "RFC 7946, August 2016", "standard", "Defines portable point, line, feature and feature-collection geometry encoding."),
    src(11, "ISO 19133 Geographic information - Location-based services - Tracking and navigation", "International Organization for Standardization", "https://www.iso.org/standard/32500.html", "ISO 19133:2005", "standard", "Defines conceptual schemas for tracking and navigation services and network-based routing."),
    src(12, "ISO 19141 Geographic information - Schema for moving features", "International Organization for Standardization", "https://www.iso.org/standard/41445.html", "ISO 19141:2008, confirmed 2022", "standard", "Provides the boundary between planned route and actual moving-feature trajectory."),
    src(13, "Commission Delegated Regulation (EU) 2024/490", "European Union", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R0490", "29 November 2023", "legislation", "Defines machine-readable travel itineraries, handover points and static, historic, observed and dynamic travel data."),
    src(14, "Multimodal travel information services", "European Commission", "https://transport.ec.europa.eu/transport-themes/intelligent-transport-systems/road/action-plan-and-directive/multimodal-travel-information-services_en", "Policy page accessed 2026-09-06", "public-authority", "Provides EU multimodal journey-planning and data-access context."),
    src(15, "Trip", "Schema.org Community Group", "https://schema.org/Trip", "Vocabulary page accessed 2026-09-06", "ontology", "Provides lightweight web alignment for itinerary, subtrip, provider, departure and arrival."),
    src(16, "Time Ontology in OWL", "World Wide Web Consortium", "https://www.w3.org/TR/owl-time/", "Candidate Recommendation Draft, 15 November 2022", "ontology", "Defines instants, intervals, duration, ordering, temporal position and reference systems."),
    src(17, "RFC 3339: Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines timestamps with seconds and explicit offsets."),
    src(18, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines attribution, derivation, revision, invalidation and delegation."),
    src(19, "Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note, 15 December 2016", "ontology", "Defines quality measurements, annotations, policies and provenance."),
    src(20, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties and constraints for sensitive itinerary data."),
    src(21, "OGC Moving Features standards", "Open Geospatial Consortium", "https://www.ogc.org/standards/movingfeatures/", "Standards catalogue accessed 2026-09-06", "standard", "Catalogues movement representations used to keep route plans distinct from actual trajectories."),
]


ROWS = [
    ("identity-kind-and-boundary", "Identity, kind and boundary", "Make route and itinerary jointly discoverable without collapsing their different identities or lifecycles.", [
        ("identity-version-and-successor", "Identity, version and successor", ["SRC-001", "SRC-005", "SRC-006", "SRC-018"], [
            ("route-or-itinerary-identity-namespace-version-and-kind", "Route or itinerary identity, namespace, version and mandatory kind", "identity"),
            ("revision-predecessor-successor-effective-period-and-status", "Revision, predecessor, successor, effective period and status", "lifecycle"),
        ]),
        ("scope-owner-and-plan-boundary", "Scope, owner and plan boundary", ["SRC-001", "SRC-002", "SRC-004", "SRC-013", "SRC-015"], [
            ("reusable-route-computed-route-itinerary-and-combined-plan", "Reusable route, computed route, itinerary and combined-plan boundary", "classification"),
            ("planner-operator-traveller-vehicle-cargo-and-authority-roles", "Planner, operator, traveller, vehicle, cargo and authority roles", "ownership"),
        ]),
    ]),
    ("network-path-and-ordered-structure", "Network path and ordered structure", "Represent traversal and plan composition while external networks, places and schedules retain mastership.", [
        ("endpoints-waypoints-and-network-path", "Endpoints, waypoints and network path", ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007", "SRC-009", "SRC-010", "SRC-011"], [
            ("origin-destination-via-waypoint-node-link-and-zone-reference", "Origin, destination, via waypoint, node, link and zone reference", "spatial"),
            ("directed-segment-sequence-topology-geometry-and-crs", "Directed segment sequence, topology, geometry and CRS", "composition"),
        ]),
        ("legs-stages-visits-and-transfers", "Legs, stages, visits and transfers", ["SRC-001", "SRC-003", "SRC-004", "SRC-013", "SRC-015"], [
            ("itinerary-leg-stage-call-visit-activity-and-order", "Itinerary leg, stage, call, visit, activity and order", "composition"),
            ("access-egress-transfer-handover-connection-and-wait", "Access, egress, transfer, handover, connection and wait", "relationship"),
        ]),
    ]),
    ("constraints-criteria-and-selection", "Constraints, criteria and selection", "Preserve what was requested, what was feasible and why one alternative was selected.", [
        ("request-and-feasibility-constraints", "Request and feasibility constraints", ["SRC-005", "SRC-006", "SRC-007", "SRC-011", "SRC-013", "SRC-014"], [
            ("mode-accessibility-vehicle-cargo-height-load-and-safety-constraint", "Mode, accessibility, vehicle, cargo, height, load and safety constraint", "constraint"),
            ("avoid-prefer-must-pass-time-window-permission-and-policy-constraint", "Avoid, prefer, must-pass, time-window, permission and policy constraint", "constraint"),
        ]),
        ("objective-alternatives-and-choice", "Objective, alternatives and choice", ["SRC-005", "SRC-006", "SRC-007", "SRC-013", "SRC-019"], [
            ("distance-time-cost-emissions-energy-risk-and-comfort-objective", "Distance, time, cost, emissions, energy, risk and comfort objective", "decision"),
            ("candidate-alternative-ranking-selection-rejection-and-rationale", "Candidate alternative, ranking, selection, rejection and rationale", "decision"),
        ]),
    ]),
    ("temporal-service-and-resource-plan", "Temporal, service and resource plan", "Bind plan clocks and external operational resources without treating estimates as commitments.", [
        ("validity-planned-time-and-continuity", "Validity, planned time and continuity", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-013", "SRC-016", "SRC-017"], [
            ("operating-day-validity-departure-arrival-duration-and-time-zone", "Operating day, validity, departure, arrival, duration and time zone", "temporal"),
            ("requested-planned-estimated-predicted-committed-and-slack-time", "Requested, planned, estimated, predicted, committed and slack time", "classification"),
        ]),
        ("mode-service-schedule-and-resource-bindings", "Mode, service, schedule and resource bindings", ["SRC-001", "SRC-003", "SRC-004", "SRC-013", "SRC-015"], [
            ("mode-line-route-pattern-service-trip-and-schedule-reference", "Mode, line, route pattern, service trip and schedule reference", "relationship"),
            ("vehicle-seat-booking-ticket-fare-activity-and-facility-reference", "Vehicle, seat, booking, ticket, fare, activity and facility reference", "relationship"),
        ]),
    ]),
    ("lifecycle-change-and-evaluation", "Lifecycle, change and evaluation", "Make computation, selection, invalidation and replanning auditable while preserving history.", [
        ("plan-state-disruption-and-replanning", "Plan state, disruption and replanning", ["SRC-005", "SRC-006", "SRC-007", "SRC-013", "SRC-018"], [
            ("draft-requested-computing-candidate-selected-confirmed-and-cancelled-state", "Draft, requested, computing, candidate, selected, confirmed and cancelled state", "lifecycle"),
            ("disruption-invalidity-reroute-difference-successor-and-actual-divergence", "Disruption, invalidity, reroute, difference, successor and actual divergence", "exception"),
        ]),
        ("measures-uncertainty-and-quality", "Measures, uncertainty and quality", ["SRC-005", "SRC-006", "SRC-009", "SRC-011", "SRC-019"], [
            ("distance-duration-cost-toll-energy-emissions-and-risk-estimate", "Distance, duration, cost, toll, energy, emissions and risk estimate", "measurement"),
            ("coverage-freshness-precision-confidence-uncertainty-and-validation", "Coverage, freshness, precision, confidence, uncertainty and validation", "quality"),
        ]),
    ]),
    ("provenance-access-and-interoperability", "Provenance, access and interoperability", "Make every plan reproducible, governable and safely projectable across incompatible route vocabularies.", [
        ("source-engine-algorithm-and-lineage", "Source, engine, algorithm and lineage", ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-018", "SRC-019"], [
            ("network-dataset-version-engine-algorithm-parameter-and-job-reference", "Network dataset version, engine, algorithm, parameter and job reference", "provenance"),
            ("assertion-derivation-correction-invalidation-review-and-evidence", "Assertion, derivation, correction, invalidation, review and evidence", "evidence"),
        ]),
        ("access-retention-and-crosswalks", "Access, retention and crosswalks", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-008", "SRC-009", "SRC-010", "SRC-013", "SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019", "SRC-020", "SRC-021"], [
            ("location-sensitivity-purpose-consent-access-retention-and-license", "Location sensitivity, purpose, consent, access, retention and license", "privacy"),
            ("transmodel-netex-gtfs-ogc-geojson-schema-org-time-and-provenance-crosswalk", "Transmodel, NeTEx, GTFS, OGC, GeoJSON, Schema.org, time and provenance crosswalk", "interoperability"),
        ]),
    ]),
]


KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 8) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 16) % len(KIND_CYCLE)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {lower} as typed Route / Itinerary context while journey execution, networks, places, schedules, services, assets, bookings and routing engines remain external masters.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which route or itinerary identity, kind, revision, ordered component, time basis and source establish {lower}?", "kind": kinds[0], "answer_data": ["route or itinerary identifier, mandatory kind, namespace, revision and lifecycle state", "origin, destination, ordered waypoint, segment, leg, visit or transfer references", "validity, planned clocks, source profile, confidence and external master references"]},
            {"id": f"{fid}-q02", "text": f"Who requested, computed, selected, owns, reviewed, corrected or may access {lower}, and under which authority or policy?", "kind": kinds[1], "answer_data": ["planner, requester, operator, traveller, asset steward, routing provider and reviewer roles", "delegation, purpose, constraint, jurisdiction, permission, license and access scope", "assertion owner, algorithm or method, reviewer, correction actor and disputed state"]},
            {"id": f"{fid}-q03", "text": f"Which constraints, alternatives, estimates, exceptions, evidence, uncertainty and lineage qualify {lower}?", "kind": kinds[2], "answer_data": ["requested and applied constraints, objectives, candidate ranking and selection rationale", "distance, duration, cost, energy, emissions, risk, tolerance and uncertainty", "network snapshot, engine and algorithm version, digest, successor, invalidation and semantic-loss declaration"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed route- or itinerary-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Digest-addressed manifest of definitions, requests, alternatives, selections, validations, corrections and external records supporting {lower}.", "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative route or itinerary master-system identifier first, otherwise governed IRI, then Dimension UUID or ULID; include immutable revision and digest.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles, ordinal = [], 0
    for bid, bname, rationale, layers in ROWS:
        built_layers, bundle_refs = [], []
        for lid, lname, refs, findings in layers:
            bundle_refs.extend(refs)
            built_findings = []
            for item in findings:
                ordinal += 1
                built_findings.append(make_finding(item, ordinal, refs))
            built_layers.append({"id": lid, "name": lname, "description": f"Groups Route / Itinerary context for {lname.lower()} without importing neighboring master lifecycles.", "source_refs": refs, "findings": built_findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups the governed Route / Itinerary concern for {bname.lower()}.", "rationale": rationale, "source_refs": list(dict.fromkeys(bundle_refs)), "layers": built_layers})
    return {"bundles": bundles}


FUNCTION_ROWS = [
    ("register-plan-object", "Register route or itinerary", "Create one governed route or itinerary identity with a mandatory kind and boundary.", ["kind discriminator", "origin and destination", "owner and source"], ["plan-object identifier", "initial revision"], ["active Dimension", "create authority"], ["identity and explicit unknowns are appended"], ["SRC-001", "SRC-005", "SRC-018"]),
    ("define-route", "Define directed route", "Append ordered waypoints, nodes, links, segments, topology and geometry references.", ["route identifier", "ordered path components", "network and geometry references"], ["validated route definition"], ["route kind", "network profile known"], ["route definition is versioned without importing network mastership"], ["SRC-001", "SRC-002", "SRC-006", "SRC-009", "SRC-010", "SRC-011"]),
    ("compose-itinerary", "Compose itinerary", "Append ordered legs, stages, visits, calls, transfers and activity references.", ["itinerary identifier", "ordered components", "route, place and service references"], ["validated itinerary composition"], ["itinerary kind", "stable component references"], ["composition and continuity checks are recorded"], ["SRC-001", "SRC-003", "SRC-004", "SRC-013", "SRC-015"]),
    ("bind-constraints", "Bind request constraints", "Record hard, soft, accessibility, operational, safety and permission constraints.", ["plan-object identifier", "constraint set", "authority and purpose"], ["typed constraint profile"], ["constraint semantics and units known"], ["requested and applied constraints remain separately auditable"], ["SRC-005", "SRC-006", "SRC-007", "SRC-011", "SRC-013"]),
    ("record-candidates", "Record candidate alternatives", "Register external routing request, parameters and candidate results without owning the routing engine.", ["routing request reference", "engine, algorithm and dataset versions", "candidate results"], ["candidate set", "comparison view"], ["external computation completed", "source snapshot available"], ["alternatives and estimates are appended with provenance"], ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-018", "SRC-019"]),
    ("select-plan", "Select route or itinerary", "Record selection, ranking, rejection rationale and any confirmation state.", ["candidate set", "objective weights", "decision authority"], ["selected revision", "decision trace"], ["candidates valid for the same request"], ["selection is appended without deleting alternatives"], ["SRC-005", "SRC-006", "SRC-013", "SRC-019"]),
    ("bind-services-resources", "Bind services and resources", "Bind modes, schedules, services, vehicles, facilities, bookings and activities as external references.", ["itinerary revision", "service and resource references", "planned times"], ["typed bindings"], ["external identities resolvable"], ["plan bindings are versioned without importing external lifecycles"], ["SRC-001", "SRC-003", "SRC-004", "SRC-013", "SRC-015"]),
    ("validate-plan", "Validate continuity and feasibility", "Validate order, topology, geometry, clocks, transfers, constraints, resource bindings and source freshness.", ["route or itinerary revision", "validation profile", "external snapshots"], ["validation report", "blocking and non-blocking issues"], ["pinned profile and tolerance rules"], ["validation evidence is appended; the plan is not silently repaired"], ["SRC-001", "SRC-004", "SRC-006", "SRC-009", "SRC-013", "SRC-016", "SRC-017", "SRC-019"]),
    ("supersede-replan", "Supersede or replan", "Create a successor after disruption, invalidity, changed constraint or better alternative.", ["current revision", "change evidence", "replacement definition"], ["successor revision", "difference and invalidation trace"], ["change authority", "affected scope known"], ["prior plan remains resolvable and immutable"], ["SRC-005", "SRC-006", "SRC-007", "SRC-018"]),
    ("project-plan", "Project route or itinerary", "Produce minimum-necessary standards-aligned or stakeholder views.", ["plan revision", "target profile", "access purpose"], ["versioned projection", "semantic-loss declaration"], ["authorized recipient", "pinned target version"], ["projection is logged and source identity is preserved"], ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-009", "SRC-010", "SRC-013", "SRC-015", "SRC-016", "SRC-018", "SRC-019", "SRC-020"]),
]


def functions():
    keys = ["id", "name", "description", "inputs", "outputs", "preconditions", "effects", "source_refs"]
    return [dict(zip(keys, row)) for row in FUNCTION_ROWS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, route and itinerary stewards, routing authorities and accountable decision roles.",
                "Register authoritative network, place, service, schedule, person, vehicle, booking, ticket, activity, shipment, incident, routing-engine and evidence masters.",
                "Publish route, itinerary, relation, constraint, identifier, access, retention, quality and interoperability registries.",
                "Pin mode, region, network, geometry, operating-day, timezone, accessibility, safety, privacy, licensing and exchange profiles.",
            ],
            "namespace_guidance": "Mint route, itinerary, revision, leg, segment, constraint, candidate and projection identifiers only in the adopting Dimension namespace; preserve network, place, service, schedule, person, vehicle, booking, ticket, activity, shipment, incident, engine and dataset identities as typed external references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local route, itinerary, constraint, identifier, access, retention and provenance registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, mandatory route-or-itinerary kind, authoritative master ID, immutable revision, endpoints, effective period and source profile; never use date, filename, geometry hash or endpoint pair alone as identity.",
                "Keep reusable route, computed route, itinerary, journey, line, journey pattern, segment, leg, waypoint, call, visit, computation job and trajectory distinct and preserve alternatives, corrections and successors.",
            ],
            "patch_rules": [
                "Additive extensions use a Dimension-owned namespace and declare target node, mode or jurisdiction profile, authority, source, rationale, access, time and interoperability impact.",
                "Breaking changes require a new version, migration and crosswalk maps, compatibility declaration and continued resolution of prior plan revisions and identifiers.",
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when kind, identity, endpoints, order, topology, clocks, constraint, state, provenance and access meaning remain intact.",
                "Transmodel, NeTEx, GTFS, OGC, GeoJSON, Schema.org, GeoSPARQL, OWL-Time and provenance mappings pin source and target versions and declare transformed, omitted or non-round-trippable values.",
            ],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative route or itinerary master-system identifier and immutable revision.", "Governed globally resolvable route, itinerary, segment or leg IRI.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep request, computation, planned, estimated, predicted, committed, selection, invalidation, correction and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {route-or-itinerary-id}--{artifact-kind}--{revision-or-event-id}; never use a date, endpoint, route number, traveller, vehicle, filename or hash alone as identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and vocabulary versions, plan scope, event and record times, provenance, assurance, license and access marking for each retained serial artifact.",
        },
        "policies": [
            "The adopting Dimension declares who may create, compute, select, confirm, bind, validate, supersede, disclose, retain and tombstone route or itinerary records.",
            "Every assertion requires object kind, identity and revision, path or itinerary scope, time kind, source, authority, confidence, status and lineage as applicable.",
            "Agents never infer actual movement, passenger presence, legal permission, reservation, feasibility or safety from a route, itinerary, estimate, ticket or routing status alone.",
            "Journeys, networks, places, services, schedules, people, vehicles, bookings, tickets, fares, activities, shipments, incidents, weather, engines, datasets and evidence remain external masters.",
            "Automated agents may add low-risk candidates, validations and projections under delegation, but consequential rerouting, safety decisions, protected location disclosure and irreversible deletion require accountable authority.",
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, mandatory kind, requested revision, time horizon, assurance, freshness, license and access policy; return the minimum permitted projection."],
            "create": ["Create stable identity, mandatory kind, endpoints or itinerary boundary, temporal basis, source, authority and explicit unknowns before adding path components or constraints."],
            "update": ["Append an immutable definition, constraint, candidate, selection, binding, validation or correction revision with actor, authority, reason, RFC 3339 effective time and predecessor."],
            "delete": ["Apply privacy, safety, dispute, audit, retention and legal-hold policy; tombstone eligible Route / Itinerary-owned records or withdraw projections while preserving identity, material provenance and non-cascading external references."],
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Route steward", "responsibilities": ["Own reusable or computed path boundary, topology, geometry references and revision lineage."]},
            {"name": "Itinerary steward", "responsibilities": ["Own ordered planning result, alternatives, selection and successor history."]},
            {"name": "Network or schedule steward", "responsibilities": ["Own referenced network, place, service and schedule masters."]},
            {"name": "Routing provider", "responsibilities": ["Own engine, algorithm, dataset, computation job and result assertions it issues."]},
            {"name": "Traveller, operator or asset authority", "responsibilities": ["Supply applicable preferences, constraints, permissions and accountable decisions."]},
            {"name": "Reviewer or auditor", "responsibilities": ["Review feasibility, evidence, conflicts, corrections and protected use without rewriting originals."]},
            {"name": "Disclosure authority", "responsibilities": ["Approve recipient, purpose, location exposure, redaction and publication timing."]},
        ],
        "access": {
            "default_rule": "Deny mutation and sensitive disclosure unless the active Dimension, role, purpose, object kind, location sensitivity, license and field policy grant the action; expose the minimum necessary projection.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency access must be time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable plan, correction or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, object and revision identity, action, decision, policy and vocabulary versions, RFC 3339 timestamp with offset, affected fields, source evidence and outcome for privileged mutation or disclosure."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": [
                "Read the nearest Dimension-owner AGENTS.md, route and itinerary authority, active mode, jurisdiction, time, access, retention, license and disclosure policies.",
                "Read this model AGENTS.md, pinned spec.yaml and required journey, network, place, service, schedule, person, vehicle, booking, ticket, activity, shipment, incident, engine, dataset and evidence model instructions before mutation.",
            ],
        },
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Route / Itinerary identity, ordered path and plan composition, constraints and alternatives, temporal and resource bindings, replanning and evaluation, provenance, privacy and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Route, itinerary, combined-plan, revision, segment, leg, candidate and projection identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Mandatory kind separates reusable route, computed route, itinerary and combined planning views."},
            {"dimension": "direct properties", "status": "covered", "notes": "Endpoints, order, topology, geometry, constraints, clocks, selection and plan state are covered without importing external masters."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Definition, request, computation result, selection, validation and actual-journey divergence are typed assertions."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Draft, requested, computing, candidate, selected, confirmed, invalid, superseded and cancelled states preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Networks, places, services, schedules, people, vehicles, resources, bookings, journeys and evidence use typed references."},
            {"dimension": "temporal", "status": "covered", "notes": "Operating day, validity, requested, computation, planned, estimated, predicted, committed, selection and correction clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Origin, destination, waypoints, nodes, links, segments, geometry, topology, direction, CRS and precision are explicit."},
            {"dimension": "provenance", "status": "covered", "notes": "Network dataset, engine, algorithm, parameters, computation, assertions, derivations, revisions and invalidations are linked."},
            {"dimension": "ownership", "status": "covered", "notes": "Dimension, route, itinerary, network, routing-provider, subject, reviewer and disclosure roles are separated."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, kind, order, topology, geometry, time, transfer, constraint, resource, freshness and crosswalk checks are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Role, purpose, consent, license, location sensitivity, minimum projection, emergency access and audit are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Alternatives, decisions, corrections, disputes, legal hold, withdrawal and tombstones are explicit and non-cascading."},
            {"dimension": "interoperability", "status": "covered", "notes": "Transmodel, NeTEx, GTFS, OGC, GeoJSON, ISO, EU, Schema.org, GeoSPARQL, OWL-Time, PROV, DQV and ODRL mappings disclose loss."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Registration, path definition, itinerary composition, constraints, candidates, selection, bindings, validation, replanning and projection declare controlled effects."},
        ],
        "known_omissions": [
            "Mode, region, safety, accessibility, border, traffic-law, passenger-rights, privacy, licensing and retention profiles require exact current rules and competent review.",
            "Network, place, journey, service, schedule, person, vehicle, booking, ticket, fare, activity, shipment, incident, weather, routing-engine, dataset and evidence lifecycles remain in neighboring masters.",
            "Certified field crosswalks, routing algorithms, map matching, traffic prediction, feasibility solvers and legal proof requirements remain future work.",
            "The aggregate family may require a future breaking split into separate Route and Itinerary specifications after wider implementation evidence.",
        ],
        "conflicts": [
            "Route, trip, journey pattern and itinerary have different meanings across Transmodel, GTFS, OGC, EU law and ordinary language; a mandatory kind and source profile are required.",
            "A reusable path, computed route, candidate itinerary, selected plan, scheduled service and actual journey cannot share one lifecycle or truth status.",
            "OGC API Routes and Route Exchange Model are developing or proposed material as of 2026-09-06, not approved OGC standards; implementations must pin exact drafts.",
        ],
        "regional_assumptions": [
            "EU multimodal travel-information rules are a regional profile, not universal route or itinerary law.",
            "Transmodel, NeTEx and GTFS primarily describe public passenger transport; private, freight, pedestrian, indoor, maritime, aviation and off-network plans need explicit profiles.",
            "Network restrictions, permits, accessibility, safety and privacy requirements depend on jurisdiction, mode and operating context.",
        ],
        "adversarial_checks": [
            "Reject an object without stable identity, mandatory route-or-itinerary kind, revision, boundary, source and lineage.",
            "Reject a route represented as an itinerary or journey, or an itinerary represented as actual movement evidence.",
            "Reject unordered path components, broken topology, unqualified CRS, infeasible transfers or planned clocks without operating-day and timezone basis.",
            "Reject a candidate, estimate, routing job status or ticket interpreted as a selected, feasible or legally permitted plan.",
            "Reject last-write-wins when constraints, alternatives, selections or source datasets change; preserve difference, invalidation and successor history.",
            "Reject a claim that OGC API Routes or Route Exchange Model is an approved OGC standard without checking the current OGC roadmap.",
            "Reject protected location disclosure, consequential rerouting or record destruction outside delegated authority and retention policy.",
        ],
    }


def build():
    model = {
        "registry_id": "vr.wm-flw-010", "model_id": "WM-FLW-010", "name": "Route / Itinerary", "entry_kind": "aggregate",
        "purpose": "Represent one governed reusable or computed route, or one candidate or selected itinerary, with ordered structure, constraints, plan clocks, alternatives and successor lineage without becoming its journey, network, schedule, resource or routing engine.",
        "scope_statement": "Owns mandatory route-or-itinerary kind; object and revision identity; endpoints, ordered waypoints, segments, legs, visits and transfers; route topology and geometry references; itinerary composition; requested and applied constraints; objectives, candidates, ranking and selection rationale; planned clocks and validity; service, schedule, mode and resource references; plan lifecycle, validation, replanning and actual-journey divergence references; estimates, quality, provenance, access, retention and loss-aware projections. Journey execution, networks, places, schedules, services, people, vehicles, bookings, tickets, fares, activities, shipments, incidents, weather, routing engines, source datasets and evidence masters remain external.",
        "in_scope": ["Route or itinerary identity, revision, mandatory kind, boundary, ownership and successor lineage", "Ordered route path or itinerary composition, constraints, objectives, alternatives, selected plan, clocks and external bindings", "Validation, disruption, replanning, estimates, provenance, privacy, access, retention and interoperability"],
        "out_of_scope": ["Owning journey, network, place, schedule, service, person, vehicle, booking, ticket, fare, activity, shipment, incident, weather, routing-engine, dataset, evidence or document lifecycles", "Equating route with itinerary, route or itinerary with journey, line with route, segment with leg, waypoint with visit, plan with actual movement or estimate with commitment", "Performing routing computation, autonomous consequential rerouting, safety or legal permission decisions, protected location disclosure or irreversible deletion"],
        "boundary_notes": [
            {"neighbor": "WM-FLW-009 Journey / Trip", "distinction": "Journey owns the planned or actual movement episode, observations and outcomes. Route / Itinerary owns reusable or computed path and planning-result structure; a journey references a selected plan and may diverge from it.", "source_refs": ["SRC-001", "SRC-004", "SRC-012", "SRC-013", "SRC-015"]},
            {"neighbor": "Network, Place and Stop", "distinction": "Route / Itinerary orders typed references and may carry snapshot geometry. Network topology, place identity, facilities, restrictions and authoritative geometry remain externally mastered.", "source_refs": ["SRC-001", "SRC-002", "SRC-006", "SRC-009", "SRC-010", "SRC-011"]},
            {"neighbor": "Line, Journey Pattern, Service and Schedule", "distinction": "A line groups service presentation, a route describes a path, a journey pattern orders scheduled points, and a scheduled trip instantiates service. Their identities and lifecycles remain distinct.", "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004"]},
            {"neighbor": "Routing Engine, Algorithm and Computation Job", "distinction": "The model records requests, parameters, versions and results. Execution, resource use, optimization implementation and job control remain owned by external computation masters.", "source_refs": ["SRC-005", "SRC-006", "SRC-007", "SRC-008"]},
            {"neighbor": "Booking, Ticket, Fare, Activity and Resource", "distinction": "An itinerary may reference entitlements, offers, reservations, activities, vehicles and facilities, but does not own or imply their availability, validity or lifecycle.", "source_refs": ["SRC-003", "SRC-004", "SRC-013", "SRC-015"]},
            {"neighbor": "Trajectory and Moving Feature", "distinction": "Route / Itinerary describes intended path or plan. Actual temporal geometry and movement observations remain journey or moving-feature evidence and are compared rather than merged.", "source_refs": ["SRC-012", "SRC-021"]},
        ],
    }
    composition = [
        {"target": "WM-FLW-009 Journey / Trip", "relation": "REFERENCE", "purpose": "Bind a selected plan to intended or actual movement while preserving execution observations and outcomes in Journey.", "required": False, "source_refs": ["SRC-001", "SRC-004", "SRC-012", "SRC-013", "SRC-015"]},
        {"target": "Network, Place, Stop, Service, Schedule, Person, Vehicle, Booking, Ticket, Activity, Shipment, Incident, Engine, Dataset and Evidence models", "relation": "REFERENCE", "purpose": "Resolve external masters without duplicating their identity, authority or lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-018"]},
        {"target": "Transmodel v6.2 and NeTEx", "relation": "ALIGN", "purpose": "Project European public-transport route and journey-pattern views with explicit type and version mappings.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003"]},
        {"target": "GTFS Schedule", "relation": "ALIGN", "purpose": "Project routes, trips, stop-time sequences, shapes, calendars and transfers without adopting GTFS terminology as universal.", "required": False, "source_refs": ["SRC-004"]},
        {"target": "OGC API Routes, Route Exchange Model, GeoSPARQL and GeoJSON", "relation": "ALIGN", "purpose": "Project engine-independent route requests and geometry while pinning developing OGC drafts and declared conformance.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010"]},
        {"target": "ISO 19133, ISO 19141 and OGC Moving Features", "relation": "ALIGN", "purpose": "Align navigation and planned-route concepts while keeping actual moving-feature trajectory external.", "required": False, "source_refs": ["SRC-011", "SRC-012", "SRC-021"]},
        {"target": "EU multimodal travel information and Schema.org Trip", "relation": "ALIGN", "purpose": "Project regional machine-readable itinerary and lightweight web-discovery views with explicit limitations.", "required": False, "source_refs": ["SRC-013", "SRC-014", "SRC-015"]},
        {"target": "OWL-Time, RFC 3339, PROV-O, DQV and ODRL", "relation": "ALIGN", "purpose": "Project temporal, provenance, quality and access semantics with exact pins and semantic-loss declarations.", "required": False, "source_refs": ["SRC-016", "SRC-017", "SRC-018", "SRC-019", "SRC-020"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
