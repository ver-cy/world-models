#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-BLT-001."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED_AT = "2026-09-06T02:00:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {"id": i, "title": title, "organization": org, "url": url, "version_or_date": version, "source_type": kind, "primary_source": True, "authority_tier": tier, "accessed_at": ACCESSED_AT, "relevance": relevance}


SOURCES = [
    src("SRC-001", "IFC 4.3.2 Documentation", "buildingSMART International", "https://ifc43-docs.standards.buildingsmart.org/", "IFC 4.3.2.0 current documentation accessed 2026-09-06", "standard", "Defines an open built-asset information schema, lifecycle scope, identity, property, quantity, geometry and exchange concepts."),
    src("SRC-002", "IfcBuilding semantic definition", "buildingSMART International", "https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcBuilding.htm", "IFC 4.3.2.0", "standard", "Defines a building as a sheltering construction and specifies composition, spatial hierarchy, systems and base quantities."),
    src("SRC-003", "IFC spatial structure", "buildingSMART International", "https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/concepts/Object_Connectivity/Spatial_Structure/content.html", "IFC 4.3.2.0", "standard", "Provides hierarchical decomposition and containment rules for site, building, storey, space and physical elements."),
    src("SRC-004", "IFC material resource", "buildingSMART International", "https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/ifcmaterialresource/content.html", "IFC 4.3.2.0", "standard", "Defines material designation, properties, layers, profiles, constituents and associations to elements."),
    src("SRC-005", "OGC CityGML Part 1: Conceptual Model Standard", "Open Geospatial Consortium", "https://docs.ogc.org/is/20-010/20-010.html", "OGC 20-010, CityGML 3.0.0", "standard", "Defines platform-independent urban objects, building parts, geometry, topology, appearance, levels of detail and change over time."),
    src("SRC-006", "ISO 16739-1:2024 Industry Foundation Classes", "International Organization for Standardization", "https://www.iso.org/standard/84123.html", "ISO 16739-1:2024, Edition 2", "standard", "Confirms current IFC scope across buildings, infrastructure works, physical and spatial components, analysis, process, actors and lifecycle exchange."),
    src("SRC-007", "Directive (EU) 2024/1275 on the energy performance of buildings", "European Union", "https://eur-lex.europa.eu/eli/dir/2024/1275/oj", "Directive (EU) 2024/1275, 24 April 2024", "legislation", "Defines building energy-performance, lifecycle global-warming, renovation, technical-system, inspection and certification concepts as a regional profile."),
    src("SRC-008", "Selected methods for condition assessment of existing buildings", "National Institute of Standards and Technology", "https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir80-2171.pdf", "NBSIR 80-2171", "public-authority", "Provides an official condition-assessment reference across structural and building-service systems.", 2),
    src("SRC-009", "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Provides portable entity, activity, agent, derivation, attribution and revision semantics for building observations and records."),
    src("SRC-010", "RFC 3339: Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339", "RFC 3339, July 2002", "standard", "Defines interoperable timestamps with seconds and explicit offset for lifecycle events and observations."),
]


# Bundle, layer and finding tuples are compiled into the research schema below.
STRUCTURE = [
    ("identity-classification-and-boundary", "Identity, classification and boundary", "Establishes the persistent physical artifact and its class boundary.", "A stable building or structure identity must survive ownership, use, geometry and condition changes without absorbing facility or project identities.", ["SRC-001", "SRC-002", "SRC-005", "SRC-006"], [
        ("artifact-identity", "Artifact identity", "Authoritative identity, aliases and continuity.", ["SRC-001", "SRC-002", "SRC-005", "SRC-009"], [
            ("authoritative-identity-namespace-and-version", "Authoritative identity, namespace and version", "Master-system identifier, namespace, immutable revision and record authority for the physical artifact.", "identity", ["SRC-001", "SRC-002", "SRC-009"], "identifier", True, True),
            ("aliases-complex-parts-merge-and-split", "Aliases, complex parts, merge and split", "External IDs and identity continuity when a complex is decomposed, connected buildings are grouped or records are corrected.", "relationship", ["SRC-002", "SRC-003", "SRC-005"], "collection", False, True),
        ]),
        ("classification-and-recognition", "Classification and recognition", "Class, intended function and distinguishing features.", ["SRC-002", "SRC-005", "SRC-006"], [
            ("building-structure-class-and-intended-function", "Building or structure class and intended function", "Versioned taxonomy and purpose that distinguish roofed buildings from bridges, towers, dams, tunnels and other engineered works.", "classification", ["SRC-002", "SRC-005", "SRC-006"], "object", True, True),
            ("recognition-features-neighbor-classes-and-confidence", "Recognition features, neighboring classes and confidence", "Observed visual, geometric, material or functional features and the evidence that distinguishes the artifact from temporary works, equipment, sites and facilities.", "evidence", ["SRC-002", "SRC-005"], "object", False, True),
        ]),
    ]),
    ("geometry-location-and-spatial-composition", "Geometry, location and spatial composition", "Represents current and historical shape, pose and hierarchical subdivisions.", "Geometry is an observation or representation with coordinate system, accuracy, level of detail and time, not a timeless intrinsic truth.", ["SRC-001", "SRC-002", "SRC-003", "SRC-005"], [
        ("georeference-and-placement", "Georeference and placement", "Location, coordinate reference and pose.", ["SRC-001", "SRC-002", "SRC-005"], [
            ("site-parcel-address-and-geographic-references", "Site, parcel, address and geographic references", "Typed external location references with jurisdiction and master authority, without importing tenure or address lifecycle.", "spatial", ["SRC-002", "SRC-005"], "collection", True, False),
            ("coordinate-reference-origin-orientation-and-pose", "Coordinate reference, origin, orientation and pose", "Coordinate reference system, local datum, placement transform, elevation reference, orientation, accuracy and observation time.", "spatial", ["SRC-001", "SRC-002", "SRC-005"], "object", True, True),
        ]),
        ("shape-extent-and-representation", "Shape, extent and representation", "Footprint, volume, dimensions and alternate geometries.", ["SRC-001", "SRC-002", "SRC-005"], [
            ("footprint-height-area-volume-and-extents", "Footprint, height, area, volume and extents", "Measured or derived quantities with unit, boundary convention, tolerance, method and validity time.", "measurement", ["SRC-002", "SRC-005"], "object", True, True),
            ("designed-as-built-surveyed-current-and-lod", "Designed, as-built, surveyed, current and level of detail", "Distinct representations with purpose, level of detail, accuracy, source, capture time and transformation lineage.", "provenance", ["SRC-001", "SRC-005", "SRC-009"], "collection", True, True),
        ]),
        ("spatial-decomposition", "Spatial decomposition", "Complex, building parts, storeys, spaces or segments and zones.", ["SRC-002", "SRC-003", "SRC-005"], [
            ("complex-building-part-storey-and-segment", "Complex, building part, storey and segment", "Hierarchical decomposition with role, composition type, parent, order and effective interval.", "composition", ["SRC-002", "SRC-003", "SRC-005"], "collection", False, True),
            ("premises-space-zone-and-containment-boundary", "Premises, space, zone and containment boundary", "References to interior units and functional zones plus the boundary or rule by which elements are contained.", "composition", ["SRC-003", "SRC-005"], "collection", False, False),
        ]),
    ]),
    ("fabric-structure-envelope-and-materials", "Fabric, structure, envelope and materials", "Describes what the physical artifact is made of and how loads and separation are achieved.", "Elements, systems and materials need typed decomposition and observed properties while their product catalog or equipment lifecycle stays external.", ["SRC-001", "SRC-003", "SRC-004", "SRC-006"], [
        ("structural-system-and-load-path", "Structural system and load path", "Foundation, frame, stability and supported actions.", ["SRC-001", "SRC-006", "SRC-008"], [
            ("foundation-frame-bearing-system-and-connections", "Foundation, frame, bearing system and connections", "System topology and member-role references for foundations, frames, walls, slabs, shells, cables and connections.", "composition", ["SRC-001", "SRC-008"], "collection", True, True),
            ("load-path-actions-capacity-and-design-basis", "Load path, actions, capacity and design basis", "Declared design actions, combinations, load transfer, resistance, serviceability and code or engineering basis without asserting current safety.", "constraint", ["SRC-001", "SRC-006", "SRC-008"], "object", False, True),
        ]),
        ("envelope-and-openings", "Envelope and openings", "Exterior separation, thermal boundary and controlled openings.", ["SRC-001", "SRC-005", "SRC-007"], [
            ("roof-facade-ground-boundary-and-continuity", "Roof, facade, ground boundary and continuity", "Envelope surfaces, layers, junctions, continuity and exterior or interior side semantics.", "composition", ["SRC-001", "SRC-005", "SRC-007"], "collection", True, True),
            ("door-window-opening-penetration-and-interface", "Door, window, opening, penetration and interface", "Typed openings and interfaces with dimensions, operation, adjacency, sealing and external component references.", "relationship", ["SRC-001", "SRC-005"], "collection", False, False),
        ]),
        ("materials-and-physical-properties", "Materials and physical properties", "Substances, assemblies and measured intrinsic properties.", ["SRC-001", "SRC-004", "SRC-007"], [
            ("material-layer-profile-constituent-and-source", "Material layer, profile, constituent and source", "Material identity or classification, assembly order, thickness, proportion, manufacturer or source reference and confidence.", "composition", ["SRC-004"], "collection", True, True),
            ("density-mass-hardness-strength-fragility-and-surface", "Density, mass, hardness, strength, fragility and surface", "Relevant measured properties with units, tolerance, anisotropy, moisture, temperature, method, sample and validity conditions.", "measurement", ["SRC-004", "SRC-008"], "collection", False, True),
        ]),
    ]),
    ("systems-capabilities-affordances-and-safety", "Systems, capabilities, affordances and safety", "Connects installed systems to supported uses, actions, constraints and hazards.", "The structure owns system and capability bindings while maintainable component details and operational work remain in equipment and facility systems.", ["SRC-001", "SRC-002", "SRC-003", "SRC-007"], [
        ("installed-systems-and-services", "Installed systems and services", "Technical, distribution, transport, fire and control systems.", ["SRC-001", "SRC-002", "SRC-007"], [
            ("system-identity-function-scope-and-topology", "System identity, function, scope and topology", "References to systems and components with served areas, ports, networks, function and operational boundary.", "relationship", ["SRC-001", "SRC-002"], "collection", False, False),
            ("capacity-availability-control-and-dependency", "Capacity, availability, control and dependency", "Rated and observed capacity, service state, control authority, utilities, upstream dependencies and failure propagation.", "state", ["SRC-001", "SRC-007"], "object", False, True),
        ]),
        ("use-affordance-and-hazard", "Use, affordance and hazard", "Supported occupancy or function, actions, access and failure modes.", ["SRC-002", "SRC-005", "SRC-007", "SRC-008"], [
            ("supported-use-occupancy-load-access-and-egress", "Supported use, occupancy, load, access and egress", "Permitted or designed uses, occupancy and load limits, accessibility, circulation, entry, exit and evacuation affordances.", "process", ["SRC-002", "SRC-005", "SRC-007"], "collection", False, True),
            ("hazard-vulnerability-protection-and-failure-mode", "Hazard, vulnerability, protection and failure mode", "Exposure, vulnerability, protective feature, foreseeable failure, trigger, consequence and safe operating restriction.", "security", ["SRC-007", "SRC-008"], "collection", False, True),
        ]),
    ]),
    ("condition-and-performance", "Condition and performance", "Records dated observations and assessments of current fabric and behavior.", "Condition grades and performance certificates are method-bound evidence, not permanent direct properties or universal safety decisions.", ["SRC-001", "SRC-007", "SRC-008", "SRC-009"], [
        ("inspection-condition-and-damage", "Inspection, condition and damage", "Observation scope, defects, damage and restrictions.", ["SRC-008", "SRC-009", "SRC-010"], [
            ("inspection-method-scope-access-and-limitations", "Inspection method, scope, access and limitations", "Inspector, competence, method, covered and inaccessible parts, instruments, conditions, time, evidence and limitations.", "evidence", ["SRC-008", "SRC-009", "SRC-010"], "object", True, True),
            ("defect-damage-condition-grade-and-restriction", "Defect, damage, condition grade and restriction", "Localized observation, cause hypothesis, extent, severity, confidence, assessment scheme and resulting use restriction.", "quality", ["SRC-008", "SRC-009"], "collection", False, True),
        ]),
        ("functional-environmental-and-energy-performance", "Functional, environmental and energy performance", "Measured or modelled behavior under declared conditions.", ["SRC-001", "SRC-007", "SRC-008"], [
            ("structural-serviceability-function-and-reliability", "Structural, serviceability, function and reliability", "Capacity or performance assessment, demand, margin, reliability basis, functional failure and remaining-life estimate.", "validation", ["SRC-001", "SRC-008"], "object", False, True),
            ("energy-carbon-indoor-environment-and-resource-profile", "Energy, carbon, indoor environment and resource profile", "Metered or calculated energy, emissions, lifecycle warming, indoor environmental quality and resource performance with regional method binding.", "measurement", ["SRC-007"], "collection", False, True),
        ]),
    ]),
    ("lifecycle-change-and-provenance", "Lifecycle, change and provenance", "Preserves origin, acceptance, alteration, use change, decommissioning and demolition.", "The physical artifact record persists after demolition, while projects and work orders own delivery execution.", ["SRC-001", "SRC-006", "SRC-007", "SRC-009", "SRC-010"], [
        ("origin-design-construction-and-handover", "Origin, design, construction and handover", "Design intent, as-built evidence and acceptance into service.", ["SRC-001", "SRC-006", "SRC-009"], [
            ("design-authority-basis-and-approved-representation", "Design authority, basis and approved representation", "Designer or responsible authority, requirement and code basis, approved model or document references and issue status.", "authority", ["SRC-001", "SRC-006", "SRC-009"], "collection", False, False),
            ("construction-completion-commissioning-and-acceptance", "Construction completion, commissioning and acceptance", "References to works, completion, tests, commissioning, handover package and acceptance event that establish as-built state.", "event", ["SRC-001", "SRC-006", "SRC-010"], "collection", True, True),
        ]),
        ("alteration-use-change-and-end-of-life", "Alteration, use change and end of life", "Versioned change to fabric, function or physical existence.", ["SRC-001", "SRC-005", "SRC-007", "SRC-009"], [
            ("alteration-renovation-repair-and-change-of-use", "Alteration, renovation, repair and change of use", "Before and after fabric or function states, work and authorization references, effective time and updated performance assumptions.", "lifecycle", ["SRC-001", "SRC-005", "SRC-007", "SRC-009"], "collection", False, True),
            ("decommission-demolition-removal-and-residual-record", "Decommission, demolition, removal and residual record", "Physical cessation, partial retention, material-recovery references, evidence, status and continuing historical or legal references.", "retention", ["SRC-001", "SRC-005", "SRC-009"], "object", False, True),
        ]),
    ]),
    ("governance-access-and-interoperability", "Governance, access and interoperability", "Controls authority, disclosure, integrity, retention and exchange.", "Built-asset records span many owners and systems, so agents need explicit mastership, projection and crosswalk rules.", ["SRC-001", "SRC-005", "SRC-006", "SRC-009", "SRC-010"], [
        ("ownership-custody-access-and-retention", "Ownership, custody, access and retention", "External party bindings and minimum authorized views.", ["SRC-001", "SRC-009"], [
            ("owner-operator-custodian-and-record-authority", "Owner, operator, custodian and record authority", "Time-bounded external party roles and distinct authority over fabric, operation, data and decisions.", "ownership", ["SRC-001", "SRC-009"], "collection", True, False),
            ("projection-security-retention-and-legal-hold", "Projection, security, retention and legal hold", "Field and artifact disclosure, sensitive geometry controls, permitted purpose, retention, hold and tombstone rules.", "access", ["SRC-001", "SRC-009"], "object", True, True),
        ]),
        ("provenance-and-exchange", "Provenance and exchange", "Revision lineage, validation and versioned mappings.", ["SRC-001", "SRC-005", "SRC-006", "SRC-009"], [
            ("observation-revision-derivation-and-confidence", "Observation, revision, derivation and confidence", "Actor, activity, source, method, observation time, derivation, uncertainty, predecessor and correction reason.", "provenance", ["SRC-009", "SRC-010"], "collection", True, True),
            ("ifc-citygml-schema-crosswalk-and-loss", "IFC, CityGML, schema crosswalk and loss", "Pinned source and target versions, model view or level of detail, field mappings, extension namespace, validation and round-trip loss.", "interoperability", ["SRC-001", "SRC-005", "SRC-006"], "collection", False, False),
        ]),
    ]),
]


KINDS = ["definition", "identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def finding(raw, n):
    fid, name, desc, primary, refs, value_kind, required, has_artifact = raw
    kinds = [primary, KINDS[(n * 5 + 2) % len(KINDS)], KINDS[(n * 11 + 8) % len(KINDS)]]
    for p in range(1, 3):
        while kinds[p] in kinds[:p]:
            kinds[p] = KINDS[(KINDS.index(kinds[p]) + 1) % len(KINDS)]
    questions = [
        {"id": f"{fid}-q01", "text": f"What is the current governed value of {name.lower()} for this building or structure, and which subtype or scope does it apply to?", "kind": kinds[0], "answer_data": [name, "artifact subtype and scope", "assertion status or explicit unknown"]},
        {"id": f"{fid}-q02", "text": f"Which observation, source, method and authority establish {name.lower()}, at what time, accuracy and confidence?", "kind": kinds[1], "answer_data": ["source and authority", "method, units and observation time", "accuracy, tolerance, confidence and evidence"]},
        {"id": f"{fid}-q03", "text": f"Which validation, access or change rule may revise {name.lower()} while preserving the prior physical-state history?", "kind": kinds[2], "answer_data": ["validation and access rule", "authorized revision event", "predecessor, correction or counterclaim reference"]},
    ]
    artifacts = []
    rationale = "This finding stores only typed references or inline bindings; the external model owns the related payload and independent lifecycle."
    if has_artifact:
        artifacts = [{"id": f"{fid}-artifact", "name": f"{name} record", "description": f"Versioned building-owned record supporting {name.lower()} with provenance and access marking.", "media_or_form": ["structured built-asset record", "survey, assessment or controlled statement", "resolvable evidence index"], "serial": True, "identity_strategy": "Authoritative built-asset master identifier first; otherwise a Dimension-governed UUID or ULID.", "source_refs": refs}]
        rationale = None
    return {"id": fid, "name": name, "description": desc, "source_refs": refs, "questions": questions, "data_elements": [{"id": f"{fid}-data", "name": f"{name} assertion", "description": f"Structured built-asset answer data for {name.lower()}, including scope, status, time and provenance.", "value_kind": value_kind, "cardinality": "1" if required else "0..1", "required": required, "source_refs": refs}], "artifacts": artifacts, "inline_only_rationale": rationale}


def structure():
    bundles, n = [], 0
    for bid, name, desc, rationale, refs, layer_rows in STRUCTURE:
        layers = []
        for lid, lname, ldesc, lrefs, rows in layer_rows:
            fs = []
            for row in rows:
                n += 1
                fs.append(finding(row, n))
            layers.append({"id": lid, "name": lname, "description": ldesc, "source_refs": lrefs, "findings": fs})
        bundles.append({"id": bid, "name": name, "description": desc, "rationale": rationale, "source_refs": refs, "layers": layers})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-built-artifact", "Register built artifact", "Create the authoritative building or structure identity and boundary without inventing unavailable fabric facts.", ["source identity", "class", "location references"], ["built-artifact record"], ["record authority and namespace resolve"], ["stable identity and explicit unknowns exist"], ["SRC-001", "SRC-002", "SRC-005"]),
    ("classify-and-recognize-artifact", "Classify and recognize artifact", "Apply a pinned taxonomy and evidence-backed distinguishing features.", ["artifact", "taxonomy", "observations"], ["classification revision"], ["taxonomy and observation provenance resolve"], ["building, structure and neighbor-class uncertainty stays visible"], ["SRC-002", "SRC-005", "SRC-006"]),
    ("attach-geometric-representation", "Attach geometric representation", "Bind a designed, as-built, surveyed or current geometry with CRS, accuracy and level of detail.", ["artifact", "geometry reference", "representation metadata"], ["geometry binding revision"], ["CRS, purpose and source resolve"], ["alternate representations remain distinguishable"], ["SRC-001", "SRC-005"]),
    ("compose-spatial-and-fabric-parts", "Compose spatial and fabric parts", "Add or revise typed complex, part, storey, space, element or material membership.", ["artifact", "part references", "composition rule"], ["composition revision"], ["parentage and containment validate"], ["decomposition remains acyclic and historically traceable"], ["SRC-002", "SRC-003", "SRC-004"]),
    ("bind-installed-system", "Bind installed system", "Reference a serving system, component register and served scope.", ["artifact", "system reference", "scope and function"], ["system binding"], ["system master and topology resolve"], ["building context expands without copying equipment lifecycle"], ["SRC-001", "SRC-002"]),
    ("record-physical-property", "Record physical property", "Append a measured or derived geometry, material or performance quantity.", ["subject", "value and unit", "method and conditions"], ["physical-property observation"], ["unit, tolerance and observation time are present"], ["direct property remains attributable and time-bounded"], ["SRC-001", "SRC-004", "SRC-008"]),
    ("record-condition-assessment", "Record condition assessment", "Capture inspection scope, defect observations, grade, restrictions and limitations.", ["artifact", "inspection evidence", "assessment profile"], ["condition assessment revision"], ["assessor authority and method resolve"], ["observation, judgement and safety decision remain separate"], ["SRC-008", "SRC-009"]),
    ("assess-performance-and-capability", "Assess performance and capability", "Evaluate loads, serviceability, energy, environmental quality or supported use under a pinned method.", ["artifact", "observations", "method and requirements"], ["performance assessment"], ["scope and method versions resolve"], ["result does not overclaim current safety or legal compliance"], ["SRC-001", "SRC-007", "SRC-008"]),
    ("record-alteration-or-use-change", "Record alteration or use change", "Link before and after physical or functional states to authorized work and acceptance evidence.", ["artifact", "change set", "work and authorization references"], ["change revision"], ["effective time and acceptance basis exist"], ["current state changes without erasing prior fabric"], ["SRC-001", "SRC-005", "SRC-009"]),
    ("decommission-or-demolish-artifact", "Decommission or demolish artifact", "Record physical cessation while retaining historical identity and residual references.", ["artifact", "decision", "completion evidence"], ["end-of-life revision"], ["authority and retention policy permit action"], ["artifact becomes historical rather than disappearing"], ["SRC-001", "SRC-009"]),
    ("issue-built-asset-projection", "Issue built-asset projection", "Produce a minimum authorized geometry, condition, performance or handover view.", ["artifact revision", "recipient and purpose", "projection policy"], ["digest-pinned projection"], ["access and sensitive-geometry decision permit release"], ["redaction, provenance and omitted content are explicit"], ["SRC-001", "SRC-005", "SRC-009"]),
    ("map-external-built-asset-schema", "Map external built-asset schema", "Transform a pinned IFC, CityGML or partner representation with validation and loss declaration.", ["source representation", "versioned crosswalk", "target profile"], ["mapped projection and report"], ["versions and model view resolve"], ["extensions, omissions and round-trip limits are recorded"], ["SRC-001", "SRC-005", "SRC-006"]),
]


def service_layers():
    return {
        "dimension": {"owner_package_requirements": ["Declare the Dimension owner, built-asset registry authority, stewards, coordinate and unit policies and delegated engineering decision roles.", "Declare building, site, parcel, space, equipment, works, permit, party, incident and document master systems.", "Publish model, object, event, relation, classification, access, retention and interoperability registries.", "Pin building or structure subtype, geometry, inspection, performance, energy, safety and jurisdiction profiles."], "namespace_guidance": "Mint building and structure identifiers only in the adopting Dimension's governed namespace; preserve cadastral, address, IFC, CityGML, permit and facility IDs as typed aliases or references with authority and time.", "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local built-asset, geometry, event, policy and relation registries"]},
        "canon_and_patch": {"canonicalization_rules": ["Canonicalize by registry ID, model version, built-asset master ID, immutable revision and explicit authority; do not use address, owner, geometry hash or mutable name as identity.", "Keep designed, approved, as-built, surveyed and current observed state distinct and preserve conflicting representations."], "patch_rules": ["Additive extensions use a Dimension-owned namespace and declare target node, subtype, source, units, rationale, safety and access impact.", "Breaking changes require a new version, migration and crosswalk maps, compatibility declaration and continued resolution of prior asset revisions."], "compatibility_rules": ["Consumers may ignore unknown additive fields only when identity, units, CRS, time, provenance, safety and access meaning remain intact.", "IFC, CityGML and partner mappings pin source and target versions, model view or level of detail and declare transformed, omitted or non-round-trippable values."]},
        "artifact_rules": {"identity_priority": ["Authoritative built-asset master-system identifier and immutable revision identifier.", "Governed globally resolvable asset IRI or federation identifier.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."], "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep design, approval, construction, observation, effective, publication and ingestion times distinct.", "serial_naming_rule": "Name serial artifacts as {asset-id}--{artifact-kind}--{revision-or-event-id}; never use an address, date, filename or hash alone as asset identity.", "integrity_rule": "Store digest, media type, byte length, issuer or surveyor, method and software version, CRS, units, provenance, access marking and immutable reference for every retained serial artifact."},
        "policies": ["The adopting Dimension declares who may register, classify, survey, assess, alter, disclose, restrict, decommission and tombstone a built artifact.", "Safety, capacity, compliance and fitness-for-use claims require competent authority, declared scope, method, evidence, effective time and limitations.", "Agents never infer current safety from age, appearance, design capacity, energy certificate or generic condition grade.", "Site, tenure, parties, spaces, equipment, projects, permits, incidents, valuations, documents and work execution remain in their owning systems and are referenced.", "Automated agents may enrich low-risk measurements and mappings under delegation but must propose consequential restrictions, disclosure, demolition, safety and compliance decisions."],
        "crud": {"read": ["Resolve active Dimension, purpose, role, profiles, asset revision and external masters; return the minimum permitted view and preserve representation status and uncertainty."], "create": ["Create master identity, class, authority, location references and explicit unknowns before attaching fabric, geometry or performance claims."], "update": ["Append an immutable revision with actor, authority, reason, RFC 3339 effective time and predecessor; validate identity, containment, units, CRS, evidence, safety and access before and after mutation."], "delete": ["Apply retention, legal hold and end-of-life policy; tombstone built-asset records or withdraw projections while maintaining historical identity and avoiding cascading deletion of external records."]},
        "roles": [{"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, classification, access, retention and federation rules."]}, {"name": "Built-asset owner or custodian", "responsibilities": ["Maintain accountable fabric record and authorize permitted disclosure and change."]}, {"name": "Designer or engineering authority", "responsibilities": ["Issue design basis, capacity, safety and alteration assessments within competence and mandate."]}, {"name": "Surveyor or inspector", "responsibilities": ["Record geometry and condition evidence with method, scope, accuracy and limitations."]}, {"name": "Operator or facility representative", "responsibilities": ["Supply current use, system, restriction and performance context without changing fabric authority."]}, {"name": "Records and information steward", "responsibilities": ["Maintain revisions, provenance, crosswalks, access, retention and handover integrity."]}, {"name": "Auditor", "responsibilities": ["Review decisions, evidence, changes and access without rewriting physical truth."]}],
        "access": {"default_rule": "Deny mutation and sensitive disclosure unless the active Dimension, role, purpose, asset class and field or geometry policy grant the action; expose the minimum necessary projection.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Emergency access must be time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable history, evidence, safety restrictions or legal hold."], "audit_requirements": ["Log actor, role, purpose, asset and revision identity, action, decision, profile version, RFC 3339 timestamp with offset, affected scope and outcome for privileged mutation or disclosure."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"], "read_order": ["Read the nearest Dimension-owner AGENTS.md, asset authority, active engineering profiles and access policies.", "Read this model AGENTS.md, pinned spec.yaml and required site, space, equipment, works, incident and document model instructions before mutation."]},
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering building and engineered-structure identity, geometry, composition, fabric, materials, systems, affordances, condition, performance, lifecycle, governance and exchange across IFC, CityGML and official engineering references.", "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Master identity, aliases, complex and part continuity, merge or split and immutable revisions are explicit."},
            {"dimension": "classification and recognition", "status": "covered", "notes": "Building and engineered-structure subtypes, intended function, distinguishing features, neighbor classes and confidence are represented."},
            {"dimension": "direct properties", "status": "covered", "notes": "Geometry, dimensions, mass, materials, density, strength, surface and other measured properties carry units, conditions and time."},
            {"dimension": "spatial", "status": "covered", "notes": "Site references, CRS, placement, pose, footprint, extents, levels of detail and hierarchical decomposition are explicit."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Design, construction, commissioning, alteration, repair, use change, decommissioning and demolition preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Sites, parcels, spaces, elements, materials, systems, equipment, works, parties, permits, incidents and documents use typed bindings."},
            {"dimension": "temporal", "status": "covered", "notes": "Design, approval, construction, observation, effective, publication and ingestion times remain distinct."},
            {"dimension": "provenance", "status": "covered", "notes": "Designed, as-built, surveyed and observed representations identify source, method, actor, software, derivation and confidence."},
            {"dimension": "ownership", "status": "covered", "notes": "Owner, operator, custodian, record authority, engineering authority and external master systems have distinct roles."},
            {"dimension": "validation and safety", "status": "covered", "notes": "Identity, containment, units, CRS, geometry, evidence, capacity, limitations, state and access validation are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Granular projections, sensitive geometry, emergency access, purpose, audit and role-bound mutation are covered."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Historical identity, legal hold, tombstone, withdrawal and non-cascading external references are explicit."},
            {"dimension": "interoperability", "status": "covered", "notes": "IFC and CityGML mappings pin versions, model views or levels of detail, validation and loss."},
            {"dimension": "capabilities and affordances", "status": "covered", "notes": "Supported use, occupancy, loads, access, egress, system capacity, hazards, protections and failure modes are represented."},
        ],
        "known_omissions": ["Building-code, structural-system, bridge, tunnel, tower, dam and regional safety profiles must supply exact classes, loads, limits, tests and legal decisions.", "Component-level equipment, product, maintenance, work-order, permit, valuation and occupancy semantics remain in neighboring models.", "Certified IFC and CityGML exchange crosswalks, model-view profiles and round-trip tests remain future work."],
        "conflicts": ["IFC defines IfcBuilding as a subtype of IfcFacility while the Vercy registry uses operational Facility CONTAINS Building; the draft keeps Vercy aggregation and records IFC type hierarchy as an alignment conflict.", "The previous card said every building stands on parcels, but buildings can span or lack resolved cadastral links; parcel and site bindings are required only where an adopting profile mandates them.", "Current condition, safety and performance cannot be inferred from as-designed or as-built information and require dated evidence."],
        "regional_assumptions": ["EU energy and carbon concepts are a regional profile under Directive (EU) 2024/1275 and do not create universal metrics or certification duties.", "NIST condition-assessment material is methodological evidence, not a current universal building-code or legal requirement."],
        "adversarial_checks": ["Reject address, owner, geometry hash or project number used as the sole building identity and reject silent identity change after subdivision or connection.", "Reject geometry or physical quantities without units, CRS where relevant, representation status, tolerance, method, observation time and provenance.", "Reject design capacity, age, appearance or generic condition grade presented as proof of current safety, compliance or fitness for use.", "Reject copied site, tenure, party, space, equipment, work, permit, incident or document lifecycles when governed references are sufficient.", "Reject demolition, safety restriction, sensitive-geometry disclosure or external schema export without authority, purpose, preserved history and loss declaration."],
    }


def build():
    return {
        "schema_version": "1.0.0",
        "model": {"registry_id": "vr.wm-blt-001", "model_id": "WM-BLT-001", "name": "Building / Structure", "entry_kind": "aggregate", "purpose": "Represent a persistent building or engineered structure as a governed physical artifact with identity, geometry, composition, fabric, materials, systems, capabilities, condition, performance and lifecycle evidence independent of any storage or exchange format.", "scope_statement": "Owns built-artifact identity, class, geometry bindings, spatial and fabric decomposition, material and installed-system bindings, measured physical properties, recognition features, affordances, hazards, condition and performance assessments, lifecycle changes and exchange projections while referencing facility, site, space, equipment, works, party, permit, incident and document masters.", "in_scope": ["Building and engineered-structure identity, classification, recognition, geometry, pose and spatial decomposition", "Structural system, envelope, materials, physical properties, installed-system bindings, capabilities, affordances and hazards", "Condition, performance, design and as-built provenance, alteration, end of life, access, retention and interoperability"], "out_of_scope": ["Facility operations, land and site tenure, postal address authority, room occupancy and tenancy, individual equipment and product master lifecycles", "Construction-project and work-order execution, party identity, permits, incidents, finance, valuation, insurance and document payloads", "Universal building-code, safety, load, energy, condition or structure-subtype vocabularies"], "boundary_notes": [
            {"neighbor": "Facility WM-BLT-006", "distinction": "Building or structure owns physical fabric; Facility owns the managed operational aggregation. A facility may contain buildings even though IFC uses a different type hierarchy.", "source_refs": ["SRC-001", "SRC-002", "SRC-006"]},
            {"neighbor": "Site, land parcel and address", "distinction": "The artifact references location, cadastral and address authorities but does not own land tenure, site management or address normalization.", "source_refs": ["SRC-002", "SRC-005"]},
            {"neighbor": "Premises, space and spatial unit WM-BLT-002", "distinction": "This model owns the outer artifact and decomposition bindings; independently usable or governed interior units retain their own identity and lifecycle.", "source_refs": ["SRC-003", "SRC-005"]},
            {"neighbor": "Equipment and installed product", "distinction": "The structure owns serving-system, interface and scope bindings while equipment serial identity, maintenance, warranty and spare-parts lifecycle stay external.", "source_refs": ["SRC-001", "SRC-003"]},
            {"neighbor": "Construction works and project", "distinction": "Works create or alter the artifact, but schedules, contracts, resources, cost and execution remain in project and work models; accepted outputs update the physical record.", "source_refs": ["SRC-001", "SRC-006"]},
            {"neighbor": "Incident, defect and repair", "distinction": "An incident occurs externally, a defect or damage observation is recorded here, an engineering assessment interprets it, and repair execution remains a referenced work record.", "source_refs": ["SRC-008", "SRC-009"]},
        ]},
        "sources": SOURCES,
        "structure": structure(),
        "functions": [{"id": r[0], "name": r[1], "description": r[2], "inputs": r[3], "outputs": r[4], "preconditions": r[5], "effects": r[6], "source_refs": r[7]} for r in FUNCTIONS],
        "composition": [
            {"target": "WM-BLT-006 Facility", "relation": "REFERENCE", "purpose": "Binds operational aggregation while the building retains independent physical identity and fabric lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-002"]},
            {"target": "WM-BLT-002 Premises / Spatial Unit", "relation": "COMPOSE", "purpose": "Provides the candidate spatial matryoshka for independently governed interior units while preserving their typed identities.", "required": False, "source_refs": ["SRC-003", "SRC-005"]},
            {"target": "Site, Land Parcel, Address and Geography models", "relation": "REFERENCE", "purpose": "Locates the physical artifact without importing cadastral, tenure or address mastership.", "required": True, "source_refs": ["SRC-002", "SRC-005"]},
            {"target": "Equipment, Product and Material models", "relation": "REFERENCE", "purpose": "Binds installed components and material classifications while external masters own serial, product and supply lifecycles.", "required": False, "source_refs": ["SRC-001", "SRC-004"]},
            {"target": "Construction Works, Project and Work Order models", "relation": "REFERENCE", "purpose": "Links creation and alteration evidence while execution remains independently governed.", "required": False, "source_refs": ["SRC-001", "SRC-006"]},
            {"target": "Person, Organization, Ownership, Permit and Document models", "relation": "REFERENCE", "purpose": "Binds parties, interests, authorizations and evidence without absorbing their lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-009"]},
            {"target": "Incident and Hazard models", "relation": "REFERENCE", "purpose": "Links damaging events and external hazards while storing only building-local observations and assessments.", "required": False, "source_refs": ["SRC-008", "SRC-009"]},
            {"target": "IFC 4.3 and ISO 16739-1:2024", "relation": "ALIGN", "purpose": "Supports pinned built-asset exchange mappings without making IFC serialization the logical model identity.", "required": False, "source_refs": ["SRC-001", "SRC-006"]},
            {"target": "CityGML 3.0", "relation": "ALIGN", "purpose": "Supports platform-independent city-scale semantics and level-of-detail projections with declared loss.", "required": False, "source_refs": ["SRC-005"]},
        ],
        "service_layers": service_layers(),
        "coverage": coverage(),
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
