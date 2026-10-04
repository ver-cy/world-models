#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-OBJ-007."""

from __future__ import annotations

import json
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent
ACCESSED_AT = "2026-09-06T00:45:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {"id": i, "title": title, "organization": org, "url": url, "version_or_date": version, "source_type": kind, "primary_source": True, "authority_tier": tier, "accessed_at": ACCESSED_AT, "relevance": relevance}


SOURCES = [
    src("SRC-001", "Consolidated Resolution on the Construction of Vehicles (R.E.3)", "United Nations Economic Commission for Europe", "https://unece.org/transport/vehicle-regulations/wp29/resolutions", "ECE/TRANS/WP.29/78/Rev.7 listed 2026", "public-authority", "Defines road-vehicle categories and construction terminology under the international vehicle-regulation framework."),
    src("SRC-002", "ISO 3779:2009 Road vehicles, Vehicle identification number", "International Organization for Standardization", "https://www.iso.org/standard/52200.html", "Edition 4, confirmed 2024", "standard", "Defines worldwide VIN content and structure for road motor vehicles, towed vehicles, motorcycles and mopeds."),
    src("SRC-003", "Vehicle Manufacturers and vPIC", "National Highway Traffic Safety Administration", "https://www.nhtsa.gov/vehicle-manufacturers", "Current service accessed 2026-09-06", "public-authority", "Provides manufacturer-reported vehicle product and identifier data and VIN decoding context."),
    src("SRC-004", "Regulation (EU) 2018/858", "European Union", "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32018R0858", "Consolidated legal text accessed 2026-09-06", "legislation", "Defines road vehicle and trailer categories, type, variant, version, approval, conformity and market-surveillance concepts."),
    src("SRC-005", "IMO identification number schemes", "International Maritime Organization", "https://www.imo.org/en/ourwork/msas/pages/imo-identification-number-scheme.aspx", "Current scheme page accessed 2026-09-06", "public-authority", "Defines permanent ship and registered owner or company identifiers and distinguishes identity from name, flag and ownership changes."),
    src("SRC-006", "Aircraft Nationality and Registration Marks", "International Civil Aviation Organization", "https://www.icao.int/nationality-marks", "Annex 7 overview accessed 2026-09-06", "public-authority", "Defines aircraft nationality, common and registration marks and their registering authority."),
    src("SRC-007", "European Vehicle Register", "European Union Agency for Railways", "https://www.era.europa.eu/registers/evr_en", "Production register guidance accessed 2026-09-06", "public-authority", "Defines rail-vehicle numbers, keepers, registration entities and registration updates."),
    src("SRC-008", "Semantic Sensor Network Ontology", "World Wide Web Consortium and Open Geospatial Consortium", "https://www.w3.org/TR/vocab-ssn/", "W3C Recommendation, 19 October 2017", "ontology", "Defines systems, platforms, deployments, capabilities, operating ranges, sensors, observations, actuators, procedures and results."),
    src("SRC-009", "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entity, activity, agent, attribution, source, derivation, revision and invalidation provenance."),
    src("SRC-010", "RFC 3339: Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339", "RFC 3339, July 2002", "standard", "Defines interoperable event timestamps with seconds and an explicit UTC offset."),
]


# bundle: id, name, description, rationale, refs, layers
# layer: id, name, description, refs, findings
# finding: id, name, description, kind, refs, value kind, required, artifact
STRUCTURE = [
    ("identity-classification-and-registry", "Identity, classification and registry", "Identifies the vehicle independently of its type, name, operator and registration.", "VIN, IMO number, aircraft mark, rail number and local asset ID have different authorities and applicability.", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007"], [
        ("vehicle-master-identity", "Vehicle master identity", "Stable instance identity, authority and aliases.", ["SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-007"], [
            ("authoritative-instance-identifier", "Authoritative instance identifier", "Records the master identifier, scheme, issuing authority, validation, assignment time and prior identifiers.", "identity", ["SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-007"], "object", True, "Vehicle identity record"),
            ("registration-mark-serial-and-display-identity", "Registration mark, serial and display identity", "Records mutable marks, manufacturer serial, fleet number, plate, name and marking location.", "identity", ["SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-007"], "collection", False, "Identity marking inventory"),
        ]),
        ("mode-class-purpose-and-boundary", "Mode, class, purpose and boundary", "Functional and regulatory classification with explicit applicability.", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-007"], [
            ("transport-mode-vehicle-category-and-role", "Transport mode, vehicle category and role", "Classifies road, rail, water, air or other mode, powered status, carriage purpose and source vocabulary.", "classification", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-007"], "collection", True, "Vehicle classification profile"),
            ("instance-type-component-cargo-and-event-boundary", "Instance, type, component, cargo and event boundary", "Separates the vehicle from design type, component, carried subject, journey, permit and maintenance event.", "relationship", ["SRC-004", "SRC-005", "SRC-007", "SRC-008"], "collection", True, "Vehicle boundary decision"),
        ]),
    ]),
    ("physical-form-composition-and-construction", "Physical form, composition and construction", "Describes geometry, quantities, materials, assemblies and installed systems.", "Direct physical properties must remain distinct from type-design limits and changing observations.", ["SRC-001", "SRC-004", "SRC-008"], [
        ("geometry-dimensions-mass-and-pose", "Geometry, dimensions, mass and pose", "Measured or declared physical extent and spatial configuration.", ["SRC-001", "SRC-004", "SRC-008"], [
            ("geometry-dimensions-volume-and-clearance", "Geometry, dimensions, volume and clearance", "Records coordinate frame, shape, length, width, height, draft, envelope, clearances, units and tolerance.", "measurement", ["SRC-001", "SRC-004", "SRC-008"], "collection", True, "Dimensional survey"),
            ("mass-balance-centre-of-gravity-and-pose", "Mass, balance, centre of gravity and pose", "Records empty, operating, payload and maximum masses, loads, balance, centre of gravity and orientation.", "measurement", ["SRC-001", "SRC-004", "SRC-008"], "collection", True, "Mass and pose record"),
        ]),
        ("structure-materials-and-assemblies", "Structure, materials and assemblies", "Body and load-bearing construction across modes.", ["SRC-001", "SRC-004", "SRC-008"], [
            ("body-chassis-hull-airframe-and-running-gear", "Body, chassis, hull, airframe and running gear", "References load-bearing structure, body, hull, airframe, bogies, axles, landing gear or equivalent assemblies.", "composition", ["SRC-001", "SRC-004", "SRC-007", "SRC-008"], "collection", True, "Structural assembly manifest"),
            ("materials-coatings-joints-and-integrity", "Materials, coatings, joints and integrity", "Records materials, construction, coatings, critical joints, corrosion or fatigue zones, hardness and fragility.", "composition", ["SRC-001", "SRC-004"], "collection", False, "Material and integrity profile"),
        ]),
        ("installed-systems-and-payload-interface", "Installed systems and payload interface", "Whole-part configuration and carriage interfaces.", ["SRC-004", "SRC-008"], [
            ("installed-subsystems-components-and-configuration", "Installed subsystems, components and configuration", "References propulsion, energy, control, navigation, braking, communication, safety, sensor and actuator assemblies.", "composition", ["SRC-004", "SRC-008"], "collection", True, "Installed system configuration"),
            ("occupant-cargo-coupling-and-loading-interface", "Occupant, cargo, coupling and loading interface", "Describes seats, holds, doors, ramps, attachment points, couplers, restraints and loading constraints.", "composition", ["SRC-001", "SRC-004"], "collection", False, "Carriage interface plan"),
        ]),
    ]),
    ("propulsion-energy-and-environmental-performance", "Propulsion, energy and environmental performance", "Represents movement generation, energy storage and condition-dependent performance.", "Propulsion capability and consumption cannot be inferred from registration class alone.", ["SRC-001", "SRC-004", "SRC-008"], [
        ("propulsion-drive-and-control", "Propulsion, drive and control", "Prime movers, transmission and movement controls.", ["SRC-001", "SRC-004", "SRC-008"], [
            ("prime-mover-propulsor-and-drivetrain", "Prime mover, propulsor and drivetrain", "References engines, motors, sails, propellers, rotors, wheels, tracks, transmissions and thrust paths.", "composition", ["SRC-001", "SRC-004", "SRC-008"], "collection", False, "Propulsion architecture"),
            ("steering-braking-stability-and-control-authority", "Steering, braking, stability and control authority", "Records steering, guidance, stopping, stability, manual, remote or automated authority and degraded behavior.", "state", ["SRC-001", "SRC-004", "SRC-008"], "collection", True, "Control and stopping capability"),
        ]),
        ("energy-consumption-emissions-and-range", "Energy, consumption, emissions and range", "Energy storage, replenishment and performance.", ["SRC-001", "SRC-004", "SRC-008"], [
            ("fuel-battery-energy-storage-and-replenishment", "Fuel, battery, energy storage and replenishment", "Records energy stores, capacity, chemistry or carrier, connectors, replenishment limits and observed state.", "measurement", ["SRC-004", "SRC-008"], "collection", False, "Energy system state"),
            ("consumption-emissions-efficiency-and-range", "Consumption, emissions, efficiency and range", "Records declared and observed consumption, emissions, efficiency, endurance and range with conditions.", "measurement", ["SRC-001", "SRC-004", "SRC-008"], "collection", False, "Performance observation series"),
        ]),
    ]),
    ("capacity-capabilities-and-affordances", "Capacity, capabilities and affordances", "Defines what the vehicle can carry or do and where it can operate.", "Safe action requires operating limits, prerequisites, hazards and failure modes.", ["SRC-001", "SRC-004", "SRC-008"], [
        ("capacity-and-load-envelope", "Capacity and load envelope", "Occupant, cargo, towing and distributed-load limits.", ["SRC-001", "SRC-004"], [
            ("occupant-cargo-and-volume-capacity", "Occupant, cargo and volume capacity", "Records seating, standing, berth, accessibility, mass, volume and special-cargo capacity.", "measurement", ["SRC-001", "SRC-004"], "collection", True, "Capacity certificate"),
            ("towing-coupling-axle-and-structural-load-limits", "Towing, coupling, axle and structural load limits", "Records tow, coupling, axle, deck, floor, wing or structural load limits and compatibility requirements.", "constraint", ["SRC-001", "SRC-004"], "collection", False, "Load limit matrix"),
        ]),
        ("mobility-operating-envelope-and-interaction", "Mobility, operating envelope and interaction", "Movement performance, allowed conditions and interfaces.", ["SRC-001", "SRC-004", "SRC-008"], [
            ("speed-manoeuvre-terrain-medium-and-weather-envelope", "Speed, manoeuvre, terrain, medium and weather envelope", "Records speed, acceleration, grade, turning, depth, altitude, route infrastructure, terrain and weather limits.", "constraint", ["SRC-001", "SRC-004", "SRC-008"], "collection", True, "Operating envelope"),
            ("boarding-loading-driving-command-and-service-affordances", "Boarding, loading, driving, command and service affordances", "Describes actions, required interfaces, tools, permissions, effects, reversibility, hazards and failure modes.", "process", ["SRC-004", "SRC-008"], "collection", True, "Affordance and action catalogue"),
        ]),
    ]),
    ("recognition-observation-and-operational-state", "Recognition, observation and operational state", "Supports real-world identification and time-bound state.", "Mutable pose, load and health require observation context, confidence and evidence.", ["SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-010"], [
        ("appearance-markings-and-recognition", "Appearance, markings and recognition", "Visual, electronic and machine-readable identity signals.", ["SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-007"], [
            ("colour-shape-livery-markings-and-distinguishing-features", "Colour, shape, livery, markings and distinguishing features", "Records observed colour, shape, livery, damage, decals, plates and distinguishing features.", "classification", ["SRC-003", "SRC-005", "SRC-006", "SRC-007", "SRC-008"], "collection", True, "Vehicle recognition profile"),
            ("electronic-identifier-signal-and-recognition-confidence", "Electronic identifier, signal and recognition confidence", "Records transponder, beacon, tag or radio observations, sensor, position, match candidates and spoofing risk.", "security", ["SRC-005", "SRC-006", "SRC-007", "SRC-008"], "collection", False, "Electronic recognition event"),
        ]),
        ("location-motion-and-telemetry", "Location, motion and telemetry", "Time-bound state observations.", ["SRC-008", "SRC-010"], [
            ("position-orientation-velocity-and-route-state", "Position, orientation, velocity and route state", "Records coordinate reference, position, altitude or depth, heading, attitude, speed, route and uncertainty.", "spatial", ["SRC-008", "SRC-010"], "collection", False, "Position and motion observation"),
            ("sensor-telemetry-source-quality-and-freshness", "Sensor telemetry, source, quality and freshness", "Records observed property, sensor, procedure, unit, result, phenomenon time, quality, latency and access.", "measurement", ["SRC-008", "SRC-010"], "collection", False, "Telemetry observation bundle"),
        ]),
        ("condition-damage-fault-and-operability", "Condition, damage, fault and operability", "Current health and readiness evidence.", ["SRC-004", "SRC-008", "SRC-009", "SRC-010"], [
            ("condition-integrity-damage-wear-and-contamination", "Condition, integrity, damage, wear and contamination", "Records zone condition, damage geometry, wear, corrosion, contamination, severity and safe-use impact.", "state", ["SRC-004", "SRC-008", "SRC-009"], "collection", True, "Vehicle condition assessment"),
            ("fault-operability-availability-and-degraded-mode", "Fault, operability, availability and degraded mode", "Records faults, diagnostics, operational state, affected capability, workaround and next action.", "state", ["SRC-004", "SRC-008", "SRC-009", "SRC-010"], "collection", True, "Operability status record"),
        ]),
    ]),
    ("lifecycle-ownership-and-operational-context", "Lifecycle, ownership and operational context", "Connects manufacture, configuration, party roles, service and retirement.", "Identity persists through changes of mark, flag, owner, keeper, operator, location and components.", ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-009", "SRC-010"], [
        ("manufacture-commissioning-modification-and-retirement", "Manufacture, commissioning, modification and retirement", "Physical lifecycle and configuration succession.", ["SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-009"], [
            ("manufacturer-build-place-date-and-conformity", "Manufacturer, build place, date and conformity", "Records manufacturer, production site, completion date, type reference, initial configuration and conformity evidence.", "provenance", ["SRC-003", "SRC-004", "SRC-005", "SRC-009"], "collection", True, "Build and conformity record"),
            ("commissioning-modification-rebuild-and-retirement", "Commissioning, modification, rebuild and retirement", "Records service entry, material changes, conversions, baselines, succession and disposal events.", "lifecycle", ["SRC-004", "SRC-005", "SRC-007", "SRC-009", "SRC-010"], "collection", True, "Vehicle lifecycle event log"),
        ]),
        ("ownership-custody-registration-and-service", "Ownership, custody, registration and service", "Party roles, authority records and upkeep.", ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-009"], [
            ("owner-keeper-operator-custodian-and-occupant-role", "Owner, keeper, operator, custodian and occupant role", "Records distinct party roles, authority, purpose, interval, evidence and contested status.", "ownership", ["SRC-004", "SRC-005", "SRC-007", "SRC-009"], "collection", True, "Vehicle party-role ledger"),
            ("registration-title-permit-inspection-maintenance-and-recall", "Registration, title, permit, inspection, maintenance and recall", "References external governed records, issuer, status, validity, restrictions, service and recall applicability.", "lifecycle", ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007"], "collection", True, "Compliance and service dossier"),
        ]),
    ]),
    ("safety-compliance-and-interoperability", "Safety, compliance and interoperability", "Governs hazards, evidence, profiles, access, retention and projections.", "A multimodal base cannot treat one jurisdiction or mode as universal.", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009"], [
        ("hazards-safety-and-compliance", "Hazards, safety and compliance", "Risk controls and source-qualified approvals.", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008"], [
            ("hazard-operating-risk-emergency-and-safing", "Hazard, operating risk, emergency and safing", "Records collision, fire, energy, stability, environmental and access hazards, controls and safe state.", "security", ["SRC-001", "SRC-004", "SRC-008"], "collection", True, "Vehicle hazard and safing plan"),
            ("approval-certificate-rule-conformance-and-exception", "Approval, certificate, rule conformance and exception", "Records authority, rule, approval, certificate, test, exception, condition, validity and decision.", "validation", ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-007"], "collection", True, "Vehicle conformance matrix"),
        ]),
        ("mode-profiles-access-provenance-and-projections", "Mode profiles, access, provenance and projections", "Specialization and exchange across registries.", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009"], [
            ("road-rail-maritime-aviation-and-special-mode-profile", "Road, rail, maritime, aviation and special-mode profile", "Declares authoritative classifications, identifiers, measurements, approvals, registries and non-applicable fields.", "interoperability", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007"], "collection", True, "Mode-specific extension profile"),
            ("access-provenance-retention-and-exchange-projection", "Access, provenance, retention and exchange projection", "Defines field access, sensitive location or owner data, provenance, retention and loss-aware projections.", "access", ["SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-008", "SRC-009"], "collection", True, "Vehicle exchange and access pack"),
        ]),
    ]),
]


def finding(row):
    fid, name, description, kind, refs, value_kind, required, artifact_name = row
    return {
        "id": fid, "name": name, "description": description, "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What exact design and observed values must be recorded for {name.lower()}, with units, tolerance and applicability where relevant?", "kind": kind, "answer_data": [name, "Design or declared value", "Observed value and unit", "Applicability or not-applicable reason"]},
            {"id": f"{fid}-q02", "text": f"Which source, authority, method and evidence establish {name.lower()}, at what time and with what confidence?", "kind": "evidence", "answer_data": ["Authority and master-system reference", "Method and evidence", "Phenomenon and record times", "Confidence and uncertainty"]},
            {"id": f"{fid}-q03", "text": f"How is {name.lower()} validated, related and changed without confusing the vehicle with its type, components, parties or events?", "kind": "validation", "answer_data": ["Validation result", "Typed external references", "Predecessor or successor", "Conflict, exception and retention decision"]},
        ],
        "data_elements": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Structured source-qualified values for {name.lower()} including authority, units, conditions, time, provenance and uncertainty.", "value_kind": value_kind, "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": artifact_name, "description": f"Versioned evidence or exchange artifact supporting {name.lower()} without replacing its authoritative master record.", "media_or_form": ["JSON", "YAML", "RDF or CSV when mapped", "Human-readable record"], "serial": True, "identity_strategy": "Use the authoritative vehicle ID plus immutable assertion or event ID; never use a date, filename, registration mark or hash alone as vehicle identity.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles = []
    for bid, bname, bdesc, rationale, brefs, layers in STRUCTURE:
        built = []
        for lid, lname, ldesc, lrefs, findings in layers:
            built.append({"id": lid, "name": lname, "description": ldesc, "source_refs": lrefs, "findings": [finding(x) for x in findings]})
        bundles.append({"id": bid, "name": bname, "description": bdesc, "rationale": rationale, "source_refs": brefs, "layers": built})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-vehicle", "Register vehicle", "Create stable vehicle identity and initial configuration.", ["Authority", "Identifier scheme", "Instance identifiers", "Mode profile"], ["Vehicle master record", "Validation result"], ["Identity authority is resolved"], ["Registers one physical vehicle independently of type and mutable marks"], ["SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-007"]),
    ("classify-vehicle", "Classify vehicle", "Bind functional and regulatory categories.", ["Vehicle", "Classification source", "Category"], ["Classification assertion"], ["Profile version is pinned"], ["Adds source-qualified class without universalizing one mode"], ["SRC-001", "SRC-004", "SRC-005", "SRC-006", "SRC-007"]),
    ("record-physical-specification", "Record physical specification", "Attach measured or declared physical properties.", ["Vehicle", "Property set", "Method", "Conditions"], ["Physical specification record"], ["Units and frame are declared"], ["Preserves design-versus-observation status"], ["SRC-001", "SRC-004", "SRC-008"]),
    ("configure-installed-system", "Configure installed system", "Record component installation or configuration.", ["Vehicle", "Component", "Position", "Time"], ["Configuration revision"], ["Identities are resolved"], ["Creates a successor configuration"], ["SRC-004", "SRC-008", "SRC-009"]),
    ("declare-capability-and-envelope", "Declare capability and envelope", "Record capacity, movement and limits.", ["Vehicle", "Capability", "Conditions", "Evidence"], ["Capability assertion"], ["Design and state are distinguished"], ["Adds prerequisites, limits and hazards"], ["SRC-001", "SRC-004", "SRC-008"]),
    ("observe-vehicle-state", "Observe vehicle state", "Record recognition, pose, telemetry, condition or fault.", ["Vehicle", "Property", "Observer", "Procedure", "Time"], ["Observation", "Quality assessment"], ["Vehicle match is available"], ["Appends state without overwriting design truth"], ["SRC-008", "SRC-009", "SRC-010"]),
    ("assign-party-role", "Assign party role", "Record owner, keeper, operator or custodian role.", ["Vehicle", "Party", "Role", "Authority"], ["Role assignment"], ["Party is resolved"], ["Preserves role distinctions"], ["SRC-004", "SRC-005", "SRC-007", "SRC-009"]),
    ("record-lifecycle-event", "Record lifecycle event", "Append manufacture, transfer, modification, service, incident or retirement.", ["Vehicle", "Event type", "Actor", "Evidence"], ["Lifecycle event", "State reference"], ["Authority is known"], ["Preserves immutable history"], ["SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-009", "SRC-010"]),
    ("bind-registration-or-certificate", "Bind registration or certificate", "Reference an external governed record.", ["Vehicle", "External record", "Issuer"], ["Governed record binding"], ["Issuer is resolved"], ["Adds status without replacing identity"], ["SRC-004", "SRC-005", "SRC-006", "SRC-007"]),
    ("validate-vehicle-record", "Validate vehicle record", "Check identity, quantities, composition, state and lifecycle.", ["Vehicle record", "Mode profile"], ["Validation report"], ["Pinned rules exist"], ["Reports conflicts without silent repair"], ["SRC-001", "SRC-004", "SRC-008"]),
    ("assess-operability-and-risk", "Assess operability and risk", "Derive readiness, restrictions and safe actions.", ["Vehicle", "Configuration", "Condition", "Context"], ["Operability assessment", "Restrictions"], ["Fresh evidence exists"], ["Never equates existence with operability"], ["SRC-004", "SRC-008", "SRC-009"]),
    ("publish-vehicle-projection", "Publish vehicle projection", "Produce an access-filtered projection.", ["Vehicle version", "Profile", "Access scope"], ["Projection", "Digest", "Loss report"], ["Policy permits disclosure"], ["Exports data without changing identity"], ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008"]),
]

def service_layers():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension identity, owner, vehicle steward and namespace", "Vehicle, type, component, party, place, journey, registration, maintenance, evidence and event registries", "Master-system mappings for VIN, IMO, aircraft, rail and local asset identifiers", "Authority, safety, access, retention, telemetry and publication policies"],
            "namespace_guidance": "Mint vehicle, configuration revision, observation and lifecycle-event identifiers in the adopting Dimension namespace only when no authoritative external identifier exists; preserve types, components, parties, locations, journeys, registrations, certificates and evidence as typed references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local vehicle, component, registration, maintenance, telemetry and provenance registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize by authoritative mode-specific vehicle identifier, issuing authority and scheme, never by registration mark, plate, name, type, timestamp or hash alone.", "Keep instance, type, variant, component, party role, journey, registration, certificate, observation and maintenance event distinct."],
            "patch_rules": ["Additive extensions declare target bundle, layer or finding, mode and jurisdiction profile, source, authority, units, safety and interoperability impact.", "Identity, physical-boundary or relation-semantics changes require an explicit successor, migration map, rollback path and continued resolution of prior records."],
            "compatibility_rules": ["Consumers may ignore unknown additive fields only when vehicle identity, composition, quantities, operating limits, safety, access and lifecycle meaning remain intact.", "Road, rail, maritime, aviation, sensor and registry projections pin source and target versions and disclose transformed, omitted or non-round-trippable values."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative mode-specific permanent vehicle identifier from its master registry or manufacturer scheme.", "Governed globally resolvable vehicle IRI qualified by scheme and issuing authority.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep manufacture, registration, effective, phenomenon, result, ingestion, service, transfer, incident and retirement times distinct.",
            "serial_naming_rule": "Name serial artifacts as {vehicle-id}--{artifact-kind}--{assertion-or-event-id}; never use a mutable registration mark, date, filename or hash alone as vehicle identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and profile versions, effective time, provenance, assurance, licence and access marking for every retained serial artifact.",
        },
        "policies": [
            "The adopting Dimension declares who may register, classify, inspect, configure, operate, maintain, certify, transfer, disclose and retire vehicle records.",
            "Every quantity states unit, tolerance, method, condition, source and whether it is design, declared, observed, estimated or derived.",
            "Agents never infer ownership from custody, registration from an identifier, compliance from a certificate reference, or operability from vehicle existence.",
            "Vehicle types, components, parties, journeys, shipments, registrations, titles, permits, certificates, maintenance work and telemetry remain in their owning systems and are referenced.",
            "Automated agents may read, validate, reconcile and append low-risk observations within policy, while control actions, safety overrides, ownership changes, restricted tracking disclosure and destructive retirement require accountable authority.",
        ],
        "crud": {
            "read": ["Resolve active Dimension, vehicle identity, mode profile, current configuration, requested valid time, evidence freshness and access scope; return the minimum permitted projection."],
            "create": ["Create stable instance identity, source authority, class, physical boundary, initial configuration, provenance and explicit unknowns before operational use."],
            "update": ["Append an observation, event or successor configuration with actor, authority, reason, RFC 3339 time, evidence and before-and-after validation; never overwrite a cited fact or event."],
            "delete": ["Apply registration, safety, incident, legal-hold and retention policy; prefer retirement or tombstone, preserve identity and history, and never cascade into referenced components, parties, journeys, certificates or evidence."],
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, autonomy, access, retention and federation rules."]},
            {"name": "Vehicle owner or asset steward", "responsibilities": ["Own intended use, asset policy, disposition and accountability."]},
            {"name": "Manufacturer or integrator", "responsibilities": ["Own build identity, type references, configuration and conformity evidence."]},
            {"name": "Registrar or approval authority", "responsibilities": ["Own registration, number allocation, approval, restriction and certificate lifecycle."]},
            {"name": "Keeper, operator or custodian", "responsibilities": ["Own possession, operation, condition reporting and operational compliance within role."]},
            {"name": "Inspector or maintainer", "responsibilities": ["Own inspections, diagnostics, service work and configuration changes."]},
            {"name": "Safety and compliance authority", "responsibilities": ["Govern hazards, limits, permits, incidents, recalls and emergency controls."]},
            {"name": "Data and telemetry steward", "responsibilities": ["Own sensor mappings, observation quality, sensitive tracking, provenance and retention."]},
        ],
        "access": {
            "default_rule": "Deny mutation, control and disclosure of precise live location, occupants, owner data or security-sensitive configuration unless active Dimension, role, purpose and field policy grant it; expose the minimum necessary projection.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency safety access must be purpose-bound, time-limited, attributable, independently reviewed and unable to erase original telemetry, incidents, configuration or audit evidence."],
            "audit_requirements": ["Log actor, agent, role, purpose, vehicle and configuration identity, action, policy and mode profile, RFC 3339 timestamp with offset, affected scope, requested and effective authority, evidence and outcome."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read the nearest Dimension-owner AGENTS.md, vehicle mastership, safety, control, location-privacy, access, retention and federation policies.", "Read this model AGENTS.md, pinned spec.yaml and required type, component, party, place, journey, registration, certificate, maintenance, evidence, observation and incident model instructions before mutation or action."],
        },
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering multimodal vehicle identity, physical structure, propulsion, energy, capacity, capabilities, recognition, observation, condition, lifecycle, parties, safety, compliance and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Permanent identifiers, mutable registrations, serials, fleet labels and aliases are separated."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Mode, powered status, purpose, regulatory class, type and instance boundaries are explicit."},
            {"dimension": "direct physical properties", "status": "covered", "notes": "Geometry, mass, materials, construction, systems, energy and condition include units and method."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Appearance, marks, signals, pose, telemetry, method, time, uncertainty and confusing matches are represented."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Carriage, towing, movement, control, boarding, loading and service include prerequisites, limits and hazards."},
            {"dimension": "composition", "status": "covered", "notes": "Structure, propulsion, energy, controls, sensors, safety systems and payload interfaces use typed whole-part references."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Manufacture, commissioning, configuration, registration, transfer, modification, service, incident and retirement preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Types, components, parties, places, journeys, cargo, registrations, certificates, observations and events remain distinct references."},
            {"dimension": "temporal", "status": "covered", "notes": "Manufacture, effective, registration, phenomenon, result, ingestion, service, incident and retirement times remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Coordinate frame, geometry, pose, location, route or network, altitude or depth and uncertainty are explicit."},
            {"dimension": "provenance", "status": "covered", "notes": "Manufacturer, issuer, observer, method, source, revision, event and projection provenance are retained."},
            {"dimension": "ownership", "status": "covered", "notes": "Owner, keeper, operator, custodian, occupant, maintainer and authority roles are separated."},
            {"dimension": "validation and quality", "status": "covered", "notes": "Identity, unit, composition, cycle, range, safety, profile, observation and lineage checks are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Precise location, occupants, ownership, security configuration and telemetry use purpose-bound field access."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Retirement and tombstones preserve identity, safety, incident, maintenance and compliance history without cascading."},
            {"dimension": "interoperability", "status": "covered", "notes": "Road, rail, maritime, aviation, sensor and registry profiles pin source versions and disclose loss."},
        ],
        "known_omissions": ["Autonomous driving, remote operation, unmanned aircraft, spacecraft, bicycles, micro-mobility and specialized industrial vehicles require detailed profiles.", "Vehicle type, component, party, journey, shipment, registration, certificate, maintenance, incident and telemetry lifecycles remain in neighboring masters.", "Certified per-mode field crosswalks, unit profiles, conformance fixtures, safety cases and jurisdiction-specific retention rules remain future work."],
        "conflicts": ["VIN, IMO number, aircraft registration and rail vehicle number differ in permanence, issuer, format, applicability and relationship to mutable marks.", "Road categories, rail registers, maritime schemes and aviation classifications are mode-specific and cannot be combined into one universal legal class.", "Design capability and approval evidence do not prove current condition, operability, authority to operate or suitability for a particular task."],
        "regional_assumptions": ["EU road and rail rules are authoritative only for their legal scope and are included as profiles, not universal law.", "UNECE vehicle construction vocabulary is road-focused and does not define maritime, aviation or all special modes.", "IMO and ICAO identity schemes apply to specified classes and do not replace national registers or ownership records."],
        "adversarial_checks": ["Reject a vehicle identity based only on a mutable plate, registration mark, fleet label, name or current owner.", "Reject quantities without unit, method, condition, source and design-versus-observation status.", "Reject operability or compliance inferred from a type, registration or certificate reference without fresh condition and scope evidence.", "Reject ownership inferred from keeper, operator, custodian, occupant or registration roles.", "Reject automated control or safety-critical action that exceeds active Dimension authority, operating envelope or verified vehicle state."],
    }


def build():
    return {
        "schema_version": "1.0.0",
        "model": {
            "registry_id": "vr.wm-obj-007", "model_id": "WM-OBJ-007", "name": "Vehicle", "entry_kind": "entity",
            "purpose": "Represent an individual multimodal vehicle as a physical system with stable identity, measurable form, composition, capabilities, observed state and governed lifecycle so agents can recognize, reason about and act safely around it.",
            "scope_statement": "Owns vehicle instance identity, mode and class assertions, physical composition, intrinsic specifications, installed systems, propulsion and energy, capacities, capabilities, recognition profile, observed state, configuration and lifecycle history, party-role references, safety and interoperability projections while external systems own type designs, components, parties, journeys, cargo, registrations, certificates, maintenance work and telemetry events.",
            "in_scope": ["Vehicle instance identity, mode, category, purpose, geometry, dimensions, mass, materials, construction and installed configuration", "Propulsion, energy, capacity, operating envelope, affordances, recognition, position, telemetry, condition, faults and operability", "Manufacture, commissioning, modification, ownership and custody roles, registrations, service, safety, compliance, access, retention and per-mode projections"],
            "out_of_scope": ["Vehicle type, model, variant, component, engine, battery, sensor, party, occupant, cargo, shipment, journey, route, registration, title, permit, certificate, maintenance work order or incident master lifecycle", "Universal legal categorization or approval across every road, rail, maritime, aviation, space, industrial and micro-mobility regime", "Automatic authority to operate, control, track, disclose or modify a vehicle based on technical capability or record access alone"],
            "boundary_notes": [
                {"neighbor": "Vehicle Type, Model, Variant and Version", "distinction": "Design and regulatory classes define shared properties and approvals; this model represents one physical instance and records which class applied when.", "source_refs": ["SRC-001", "SRC-004"]},
                {"neighbor": "Component and System", "distinction": "Engines, batteries, sensors, controls and structural assemblies have separate identity and lifecycle and are linked through versioned installation configuration.", "source_refs": ["SRC-004", "SRC-008"]},
                {"neighbor": "Party and Role", "distinction": "Owner, keeper, operator, custodian, occupant, manufacturer and maintainer are separate parties and time-bound roles, not attributes that determine vehicle identity.", "source_refs": ["SRC-004", "SRC-005", "SRC-007", "SRC-009"]},
                {"neighbor": "Journey, Movement, Shipment and Cargo", "distinction": "The vehicle provides carriage capability and may participate in movements; trip plan, execution, cargo and custody histories remain external events and objects.", "source_refs": ["SRC-001", "SRC-004"]},
                {"neighbor": "Registration, Approval, Certificate and Maintenance", "distinction": "These governed records and processes reference the vehicle but retain their own issuer, scope, validity, status and lifecycle.", "source_refs": ["SRC-004", "SRC-005", "SRC-006", "SRC-007"]},
                {"neighbor": "Sensor Observation and Telemetry", "distinction": "The vehicle is the feature of interest or platform; sensors, procedures, observations and results remain event records with phenomenon and result time.", "source_refs": ["SRC-008", "SRC-010"]},
            ],
        },
        "sources": SOURCES,
        "structure": structure(),
        "functions": [{"id": r[0], "name": r[1], "description": r[2], "inputs": r[3], "outputs": r[4], "preconditions": r[5], "effects": r[6], "source_refs": r[7]} for r in FUNCTIONS],
        "composition": [
            {"target": "Vehicle Type, Component, System, Sensor and Energy Storage models", "relation": "REFERENCE", "purpose": "Resolve designs and installed whole-part configuration without importing their lifecycle.", "required": True, "source_refs": ["SRC-001", "SRC-004", "SRC-008"]},
            {"target": "Party, Place, Journey, Movement, Cargo, Registration, Certificate, Maintenance, Incident, Evidence and Provenance models", "relation": "REFERENCE", "purpose": "Connect operational and governance context while retaining external mastership.", "required": False, "source_refs": ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-009"]},
            {"target": "UNECE R.E.3 and EU 2018/858", "relation": "ALIGN", "purpose": "Support road-vehicle categories, types, variants, versions, construction and approval profiles.", "required": False, "source_refs": ["SRC-001", "SRC-004"]},
            {"target": "ISO 3779 and NHTSA vPIC", "relation": "ALIGN", "purpose": "Support road-vehicle instance and manufacturer identity while preserving jurisdiction and source limits.", "required": False, "source_refs": ["SRC-002", "SRC-003"]},
            {"target": "IMO, ICAO and European rail vehicle registers", "relation": "ALIGN", "purpose": "Support permanent or registration identifiers and authority-specific lifecycle projections across maritime, aviation and rail modes.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-007"]},
            {"target": "SSN and SOSA", "relation": "ALIGN", "purpose": "Support systems, deployments, capabilities, sensors, observations, actuations and operating ranges without collapsing the vehicle into telemetry.", "required": False, "source_refs": ["SRC-008"]},
        ],
        "service_layers": service_layers(),
        "coverage": coverage(),
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
