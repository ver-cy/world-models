#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-FLW-015."""

import importlib.util
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
BASE_PATH = RUN.parent / "wm-flw-010" / "build_codex_result.py"
SPEC = importlib.util.spec_from_file_location("wm_flw_010_builder", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
AT = "2026-09-06T21:29:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "ISO 50001 Energy management systems", "International Organization for Standardization", "https://www.iso.org/standard/69426.html", "ISO 50001:2018, confirmed 2024", "standard", "Defines energy management, energy use, consumption and performance improvement."),
    src(2, "ISO 50006 Evaluating energy performance", "International Organization for Standardization", "https://www.iso.org/standard/79367.html", "ISO 50006:2023", "standard", "Defines energy performance indicators, energy baselines and evaluation practice."),
    src(3, "ISO 50015 Measurement and verification", "International Organization for Standardization", "https://www.iso.org/standard/60043.html", "ISO 50015:2014, confirmed 2025", "standard", "Defines principles for measurement and verification of organizational energy performance."),
    src(4, "ISO 14040 Life cycle assessment principles", "International Organization for Standardization", "https://www.iso.org/standard/37456.html", "ISO 14040:2006, confirmed 2022", "standard", "Defines goal, scope, inventory, impact assessment, interpretation and review for LCA."),
    src(5, "ISO 14044 Life cycle assessment requirements", "International Organization for Standardization", "https://www.iso.org/standard/38498.html", "ISO 14044:2006 with amendments 2017 and 2020", "standard", "Defines LCA requirements for boundaries, inventory, allocation, quality and reporting."),
    src(6, "ISO 14046 Water footprint", "International Organization for Standardization", "https://www.iso.org/standard/43263.html", "ISO 14046:2014, confirmed 2021", "standard", "Defines LCA-based water-footprint principles, requirements and guidelines."),
    src(7, "ISO 14051 Material flow cost accounting", "International Organization for Standardization", "https://www.iso.org/standard/50986.html", "ISO 14051:2011, confirmed 2025", "standard", "Defines tracing and physical quantification of material and energy flows and stocks."),
    src(8, "ISO 14052 MFCA in a supply chain", "International Organization for Standardization", "https://www.iso.org/standard/54811.html", "ISO 14052:2017, confirmed 2022", "standard", "Extends material flow cost accounting across supply-chain organizations."),
    src(9, "SEEA Central Framework", "United Nations Statistics Division", "https://seea.un.org/sites/seea.un.org/files/seea_cf_final_en.pdf", "SEEA Central Framework 2012", "public-authority", "Defines physical supply and use, stocks, inputs, products, residuals and accounting boundaries."),
    src(10, "SEEA Energy", "United Nations Statistics Division", "https://seea.un.org/en/methodology/seea-energy", "Official methodology accessed 2026-09-06", "public-authority", "Defines physical energy flow and asset accounts with joules as a common aggregation unit."),
    src(11, "SEEA Water", "United Nations Statistics Division", "https://seea.un.org/en/methodology/seea-water", "Official methodology accessed 2026-09-06", "public-authority", "Distinguishes abstraction, within-economy water flows, consumption and return flows."),
    src(12, "SEEA Material Flow Accounts", "United Nations Statistics Division", "https://seea.un.org/en/methodology/other-accounts/material-flow-accounts", "Official methodology accessed 2026-09-06", "public-authority", "Defines economy-wide material inputs, accumulation, imports, exports and outputs."),
    src(13, "Recommendation 20 Codes for Units of Measure", "UN/CEFACT", "https://unece.org/trade/uncefact/cl-recommendations", "Recommendation 20 revision accessed 2026-09-06", "standard", "Provides internationally maintained codes for units used in trade and data exchange."),
    src(14, "SOSA/SSN Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-ssn/", "W3C Recommendation, 19 October 2017", "ontology", "Defines sensors, observations, sampling, procedures, results and features of interest."),
    src(15, "OGC SensorThings API Part 1", "Open Geospatial Consortium", "https://docs.ogc.org/is/18-088/18-088.html", "OGC 18-088, version 1.1", "standard", "Defines interoperable things, sensors, observed properties, observations and datastreams."),
    src(16, "QUDT Ontologies", "QUDT.org", "https://www.qudt.org/pages/QUDToverviewPage.html", "QUDT overview accessed 2026-09-06", "ontology", "Defines quantities, quantity kinds, units, dimensions and conversion metadata."),
    src(17, "The Unified Code for Units of Measure", "Regenstrief Institute", "https://ucum.org/ucum", "UCUM specification accessed 2026-09-06", "standard", "Defines machine-processable unit expressions and conversions."),
    src(18, "RFC 3339 Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines timestamps with seconds and explicit numeric offsets or Z."),
    src(19, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entities, activities, agents, derivation, attribution, revision and invalidation."),
    src(20, "Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note, 15 December 2016", "ontology", "Defines quality measurements, annotations, policies and provenance."),
    src(21, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties and constraints for governed data use."),
    src(22, "GRI 301 Materials", "Global Reporting Initiative", "https://www.globalreporting.org/publications/documents/english/gri-301-materials-2016/", "GRI 301: Materials 2016", "standard", "Defines organizational reporting of material use by weight or volume and recycled inputs."),
    src(23, "GRI 302 Energy", "Global Reporting Initiative", "https://www.globalreporting.org/publications/documents/english/gri-302-energy-2016/", "GRI 302: Energy 2016", "standard", "Defines reporting of energy consumption, intensity and reductions."),
    src(24, "GRI 303 Water and Effluents", "Global Reporting Initiative", "https://www.globalreporting.org/standards/standards-development/topic-standard-for-water-and-effluents-gri-303/", "GRI 303: Water and Effluents 2018", "standard", "Defines reporting of withdrawal, discharge, consumption and water-related impacts."),
]


ROWS = [
    ("consumption-identity-class-and-boundary", "Consumption identity, class and boundary", "Establish one source-qualified consumption assertion and its measurement boundary before interpreting quantity.", [
        ("identity-revision-and-assertion-kind", "Identity, revision and assertion kind", ["SRC-001", "SRC-003", "SRC-009", "SRC-018", "SRC-019"], [
            ("consumption-identifier-namespace-revision-and-successor", "Consumption identifier, namespace, revision and successor", "identity"),
            ("metered-derived-allocated-estimated-modeled-planned-and-corrected-kind", "Metered, derived, allocated, estimated, modeled, planned and corrected kind", "classification")]),
        ("consumer-resource-and-system-boundary", "Consumer, resource and system boundary", ["SRC-001", "SRC-004", "SRC-005", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012"], [
            ("consumer-actor-asset-facility-process-activity-and-project-reference", "Consumer actor, asset, facility, process, activity and project reference", "relationship"),
            ("resource-class-origin-quality-organization-operation-and-life-cycle-boundary", "Resource class, origin, quality, organization, operation and life-cycle boundary", "constraint")])]),
    ("quantity-unit-measurement-and-derivation", "Quantity, unit, measurement and derivation", "Qualify every value by quantity kind, unit, method and observation lineage.", [
        ("quantity-unit-precision-and-uncertainty", "Quantity, unit, precision and uncertainty", ["SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-016", "SRC-017"], [
            ("quantity-kind-value-unit-dimension-and-conversion", "Quantity kind, value, unit, dimension and conversion", "measurement"),
            ("precision-resolution-tolerance-uncertainty-significant-digits-and-quality", "Precision, resolution, tolerance, uncertainty, significant digits and quality", "quality")]),
        ("meter-observation-counter-and-calculation", "Meter, observation, counter and calculation", ["SRC-002", "SRC-003", "SRC-014", "SRC-015", "SRC-016", "SRC-017", "SRC-019", "SRC-020"], [
            ("meter-sensor-datastream-observation-procedure-and-calibration-reference", "Meter, sensor, datastream, observation, procedure and calibration reference", "provenance"),
            ("opening-closing-counter-delta-rollover-conversion-and-derivation", "Opening, closing, counter delta, rollover, conversion and derivation", "process")])]),
    ("flow-components-and-resource-profiles", "Flow components and resource profiles", "Separate gross input and use-side components so net consumption is reproducible.", [
        ("gross-net-return-recovery-export-and-loss", "Gross, net, return, recovery, export and loss", ["SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012"], [
            ("gross-intake-withdrawal-receipt-and-use", "Gross intake, withdrawal, receipt and use", "measurement"),
            ("return-discharge-recovery-reuse-export-loss-and-net-consumption", "Return, discharge, recovery, reuse, export, loss and net consumption", "composition")]),
        ("energy-water-fuel-and-material-profile", "Energy, water, fuel and material profile", ["SRC-001", "SRC-006", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-022", "SRC-023", "SRC-024"], [
            ("energy-carrier-power-energy-fuel-and-conversion-profile", "Energy carrier, power, energy, fuel and conversion profile", "classification"),
            ("water-material-renewable-recycled-origin-grade-and-quality-profile", "Water, material, renewable, recycled, origin, grade and quality profile", "classification")])]),
    ("activity-time-allocation-and-normalization", "Activity, time, allocation and normalization", "Bind consumption to responsible context, clocks and transparent sharing rules.", [
        ("activity-location-and-time-basis", "Activity, location and time basis", ["SRC-001", "SRC-002", "SRC-003", "SRC-009", "SRC-014", "SRC-015", "SRC-018", "SRC-019"], [
            ("activity-process-output-asset-facility-place-and-operating-state", "Activity, process, output, asset, facility, place and operating state", "relationship"),
            ("interval-start-end-duration-event-observation-record-and-ingestion-time", "Interval start, end, duration, event, observation, record and ingestion time", "temporal")]),
        ("allocation-functional-unit-and-normalization", "Allocation, functional unit and normalization", ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-023"], [
            ("shared-resource-allocation-driver-rule-basis-and-residual", "Shared-resource allocation driver, rule, basis and residual", "process"),
            ("functional-unit-output-denominator-normalizing-variable-and-intensity", "Functional unit, output denominator, normalizing variable and intensity", "measurement")])]),
    ("lifecycle-reconciliation-and-performance", "Lifecycle, reconciliation and performance", "Preserve assertion states and compare performance without erasing source differences.", [
        ("status-validation-reconciliation-and-correction", "Status, validation, reconciliation and correction", ["SRC-003", "SRC-007", "SRC-009", "SRC-014", "SRC-015", "SRC-019", "SRC-020"], [
            ("observed-estimated-allocated-validated-reconciled-disputed-and-final-status", "Observed, estimated, allocated, validated, reconciled, disputed and final status", "lifecycle"),
            ("source-conflict-adjustment-correction-reversal-and-supersession", "Source conflict, adjustment, correction, reversal and supersession", "exception")]),
        ("baseline-target-variance-and-efficiency", "Baseline, target, variance and efficiency", ["SRC-001", "SRC-002", "SRC-003", "SRC-005", "SRC-023", "SRC-024"], [
            ("baseline-period-model-relevant-variable-and-normalization", "Baseline period, model, relevant variable and normalization", "measurement"),
            ("target-indicator-actual-variance-intensity-efficiency-and-significance", "Target, indicator, actual, variance, intensity, efficiency and significance", "decision")])]),
    ("governance-evidence-access-and-interoperability", "Governance, evidence, access and interoperability", "Keep authority, evidence, disclosure and standards mappings explicit and loss-aware.", [
        ("authority-evidence-quality-access-and-retention", "Authority, evidence, quality, access and retention", ["SRC-003", "SRC-005", "SRC-014", "SRC-015", "SRC-019", "SRC-020", "SRC-021"], [
            ("source-authority-method-evidence-digest-review-and-confidence", "Source authority, method, evidence, digest, review and confidence", "evidence"),
            ("purpose-role-confidentiality-minimum-disclosure-retention-and-legal-hold", "Purpose, role, confidentiality, minimum disclosure, retention and legal hold", "access")]),
        ("standards-crosswalk-conformance-and-loss", "Standards crosswalk, conformance and loss", [f"SRC-{i:03d}" for i in range(1, 25)], [
            ("iso-seea-uncefact-sosa-sensorthings-qudt-ucum-and-gri-crosswalk", "ISO, SEEA, UN/CEFACT, SOSA, SensorThings, QUDT, UCUM and GRI crosswalk", "interoperability"),
            ("profile-version-license-conformance-transformation-and-semantic-loss", "Profile, version, license, conformance, transformation and semantic loss", "validation")])]),
]


KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 8) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 17) % len(KIND_CYCLE)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {lower} as a source-qualified Resource Consumption assertion while linked resource, consumer, activity, meter, observation, finance and impact records retain external mastership.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which identity, assertion kind, consumer, resource, boundary, interval, quantity and source establish {lower}?", "kind": kinds[0], "answer_data": ["consumption identifier, namespace, revision, predecessor and assertion kind", "consumer, resource, activity, asset, facility, place and boundary references", "quantity kind, value, unit, interval, source, method and confidence"]},
            {"id": f"{fid}-q02", "text": f"Who measures, derives, allocates, owns, reviews, corrects or discloses {lower}, and under which authority?", "kind": kinds[1], "answer_data": ["consumer, operator, meter steward, allocator, reviewer, owner and disclosure roles", "measurement, calculation, allocation, correction, access and retention authority", "source system, procedure, calibration, evidence, review state and accountable decision"]},
            {"id": f"{fid}-q03", "text": f"Which components, uncertainty, conflicts, baseline, target, lineage and interoperability limits qualify {lower}?", "kind": kinds[2], "answer_data": ["gross, returned, recovered, exported, lost and net components", "uncertainty, tolerance, conflict, adjustment, successor and residual", "baseline, normalizer, indicator, target, variance, profile mapping and semantic loss"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed boundary-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Digest-addressed manifest of measurements, calculations, allocations, sources, quality, conflicts and corrections supporting {lower}.", "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative consumption, meter or source-system record identifier first, otherwise governed IRI, then Dimension UUID or ULID; include immutable revision and digest.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles, ordinal = [], 0
    for bid, bname, rationale, layers in ROWS:
        built_layers, bundle_refs = [], []
        for lid, lname, refs, findings in layers:
            bundle_refs.extend(refs)
            built = []
            for item in findings:
                ordinal += 1
                built.append(make_finding(item, ordinal, refs))
            built_layers.append({"id": lid, "name": lname, "description": f"Groups Resource Consumption context for {lname.lower()} without importing neighboring master lifecycles.", "source_refs": refs, "findings": built})
        bundles.append({"id": bid, "name": bname, "description": f"Groups the governed Resource Consumption concern for {bname.lower()}.", "rationale": rationale, "source_refs": list(dict.fromkeys(bundle_refs)), "layers": built_layers})
    return {"bundles": bundles}


FUNCTION_ROWS = [
    ("register-consumption", "Register consumption assertion", "Create one governed consumption identity, kind and revision.", ["consumer", "resource", "assertion kind"], ["consumption identifier", "initial revision"], ["active Dimension", "create authority"], ["identity, boundary and unknowns are appended"], ["SRC-001", "SRC-009", "SRC-018", "SRC-019"]),
    ("bind-consumer-resource", "Bind consumer and resource", "Bind external consumer, resource, activity, asset, facility and place identities.", ["consumption revision", "typed references"], ["validated bindings"], ["external identities resolvable"], ["bindings are versioned without importing external lifecycles"], ["SRC-001", "SRC-004", "SRC-007", "SRC-009"]),
    ("define-boundary-interval", "Define boundary and interval", "Record organizational, operational and measurement boundaries plus qualified clocks.", ["consumption revision", "boundary", "interval"], ["boundary profile"], ["time and boundary basis known"], ["boundary and clock semantics are appended"], ["SRC-003", "SRC-004", "SRC-005", "SRC-009", "SRC-018"]),
    ("record-measurement", "Record measurement", "Attach meter, observation, counter, calibration and quality references.", ["consumption revision", "observation", "unit"], ["measurement assertion"], ["source and quantity kind known"], ["source-qualified measurement is appended"], ["SRC-003", "SRC-014", "SRC-015", "SRC-016", "SRC-017"]),
    ("derive-quantity", "Derive consumption quantity", "Calculate a qualified value from observations, counters and flow components.", ["inputs", "formula", "conversion profile"], ["derived assertion", "calculation trace"], ["units compatible", "method pinned"], ["inputs and residual uncertainty remain resolvable"], ["SRC-003", "SRC-009", "SRC-013", "SRC-016", "SRC-017"]),
    ("allocate-shared-use", "Allocate shared consumption", "Allocate shared use using a declared driver, functional unit and residual policy.", ["shared quantity", "recipients", "allocation rule"], ["allocated assertions", "residual"], ["allocation authority", "driver evidence"], ["gross source and allocation lineage are preserved"], ["SRC-004", "SRC-005", "SRC-007", "SRC-008"]),
    ("reconcile-sources", "Reconcile consumption sources", "Compare meter, estimate, allocation, invoice and balance evidence without last-write-wins.", ["competing assertions", "tolerances", "precedence policy"], ["reconciliation report", "qualified state"], ["sources and clocks known"], ["conflicts, adjustments and residuals are appended"], ["SRC-003", "SRC-007", "SRC-009", "SRC-020"]),
    ("evaluate-performance", "Evaluate performance", "Compare normalized consumption with baseline, target and indicator definitions.", ["actual", "baseline", "target", "normalizers"], ["variance and significance assertion"], ["comparable boundaries and units"], ["evaluation remains source-qualified and non-causal"], ["SRC-001", "SRC-002", "SRC-003", "SRC-023", "SRC-024"]),
    ("correct-supersede", "Correct or supersede", "Append a correction, reversal or successor without overwriting prior assertions.", ["current revision", "reason", "replacement"], ["successor revision", "difference trace"], ["correction authority"], ["prior identity and evidence remain resolvable"], ["SRC-003", "SRC-019", "SRC-020"]),
    ("project-consumption", "Project consumption view", "Produce minimum-necessary standards-aligned views with declared loss.", ["consumption revision", "target profile", "purpose"], ["versioned projection", "semantic-loss declaration"], ["authorized recipient", "pinned target"], ["projection is logged and source identity preserved"], [f"SRC-{i:03d}" for i in range(1, 25)]),
]


def functions():
    keys = ["id", "name", "description", "inputs", "outputs", "preconditions", "effects", "source_refs"]
    return [dict(zip(keys, row)) for row in FUNCTION_ROWS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Declare the Dimension owner, consumption steward, resource stewards, measurement authorities, allocators and accountable decision roles.",
                "Register authoritative resource, consumer, activity, asset, facility, place, meter, observation, invoice, ledger, emission, impact, target and evidence masters.",
                "Publish quantity-kind, unit, resource-class, assertion-kind, boundary, allocation, access, retention, quality and interoperability registries.",
                "Pin organization, facility, process, resource, meter, reporting, jurisdiction, privacy and accounting profiles."
            ],
            "namespace_guidance": "Mint consumption, revision, allocation, reconciliation and projection identifiers only in the adopting Dimension namespace; preserve resource, consumer, activity, asset, facility, meter, observation, invoice, ledger, emission, impact and evidence identities as typed external references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local resource, quantity, unit, boundary, allocation, access, retention and provenance registries"]
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by registry ID, model version, authoritative source identity, consumer, resource, assertion kind, interval, boundary, revision and source profile; never use date, filename, quantity or meter number alone as identity.",
                "Keep stock, input, withdrawal, use, consumption, return, discharge, recovery, export, loss, meter reading, invoice quantity, cost, emissions, impact, baseline, target and forecast distinct."
            ],
            "patch_rules": [
                "Additive extensions use a Dimension-owned namespace and declare target node, resource profile, authority, source, rationale, access, time, unit and interoperability impact.",
                "Breaking changes require a new version, migration and crosswalk maps, compatibility declaration and continued resolution of prior consumption revisions."
            ],
            "compatibility_rules": [
                "Consumers may ignore unknown additive fields only when identity, kind, boundary, interval, quantity, unit, source, method, state, provenance and access meaning remain intact.",
                "ISO, SEEA, UN/CEFACT, SOSA, SensorThings, QUDT, UCUM and GRI mappings pin source and target versions and declare transformed, omitted or non-round-trippable values."
            ]
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for the consumption assertion and immutable revision.", "Governed globally resolvable consumption or observation IRI.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep interval, effective, event, observation, record, invoice, correction and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {consumption-id}--{artifact-kind}--{revision-or-event-id}; never use a date, meter number, resource name, quantity, filename or hash alone as identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and vocabulary versions, consumer-resource-boundary scope, clocks, provenance, uncertainty, assurance, license and access marking for each retained serial artifact."
        },
        "policies": [
            "The adopting Dimension declares who may measure, derive, allocate, validate, reconcile, correct, approve, disclose, retain and tombstone consumption assertions.",
            "Every assertion requires consumption identity and revision, assertion kind, consumer, resource, boundary, interval, qualified quantity, source, method, authority, confidence, state and lineage as applicable.",
            "Agents never infer ownership, stock, cost, emissions, impact, efficiency, compliance or legal responsibility from one consumption assertion, meter, invoice or report alone.",
            "Resource, stock, meter, observation, actor, asset, activity, facility, invoice, ledger, emissions, impact, waste, target, document and evidence remain external masters.",
            "Automated agents may append low-risk measurements, calculations, reconciliations and projections under delegation, but authoritative billing, accounting, reporting, protected disclosure and irreversible deletion require accountable external authority."
        ],
        "crud": {
            "read": ["Resolve active Dimension, purpose, role, requested revision, consumer-resource-boundary scope, assertion kind, interval, assurance, freshness, license and access policy; return the minimum permitted projection."],
            "create": ["Create stable identity, assertion kind, consumer, resource, boundary, interval, quantity basis, source, authority and explicit unknowns before adding calculations or performance claims."],
            "update": ["Append an immutable measurement, derivation, allocation, reconciliation, performance or correction revision with actor, authority, reason, RFC 3339 effective time and predecessor."],
            "delete": ["Apply operational, finance, reporting, dispute, audit, retention and legal-hold policy; tombstone eligible Resource Consumption-owned records or withdraw projections while preserving identity, material provenance and non-cascading external references."]
        },
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Consumption steward", "responsibilities": ["Own assertion kinds, boundary, calculation, allocation and correction semantics."]},
            {"name": "Resource or operations steward", "responsibilities": ["Own resource, activity, asset, facility and operating-context masters."]},
            {"name": "Measurement authority", "responsibilities": ["Own meter, sensor, observation, calibration, procedure and data-quality assertions."]},
            {"name": "Allocator or analyst", "responsibilities": ["Own declared allocation, conversion, normalization, baseline and comparison methods."]},
            {"name": "Finance or reporting authority", "responsibilities": ["Own external invoice, cost, ledger, disclosure and reporting decisions."]},
            {"name": "Reviewer or auditor", "responsibilities": ["Review boundary, evidence, uncertainty, conflict, correction and conformance without rewriting originals."]},
            {"name": "Disclosure authority", "responsibilities": ["Approve recipient, purpose, redaction and publication timing."]}
        ],
        "access": {
            "default_rule": "Deny mutation and sensitive disclosure unless active Dimension, role, purpose, operational or commercial sensitivity, license and field policy grant the action; expose the minimum necessary projection.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Emergency or regulatory access must be legally grounded, time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable consumption, correction or legal-hold evidence."],
            "audit_requirements": ["Log actor, role, purpose, consumption and revision identity, action, decision, policy and vocabulary versions, RFC 3339 timestamp with offset, affected fields, source evidence and outcome for privileged mutation or disclosure."]
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read the nearest Dimension-owner AGENTS.md, resource and measurement authorities, active organization, facility, resource, reporting, time, access, retention and licensing policies.", "Read this model AGENTS.md, pinned spec.yaml and required resource, consumer, activity, meter, observation, invoice, ledger, target, emission, impact and evidence instructions before mutation."]
        }
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Resource Consumption identity, assertion kind, consumer-resource boundary, interval, quantity, unit, measurement, derivation, flow components, allocation, reconciliation, performance, governance and interoperability.",
        "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Consumption, revision, source assertion, allocation, reconciliation, correction and projection identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Metered, derived, allocated, estimated, modeled, planned and corrected assertions are explicit."},
            {"dimension": "direct properties", "status": "covered", "notes": "Consumer, resource, boundary, interval, quantity, unit, components, method and state are covered."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Meter readings, counter deltas, estimates, allocations, invoices and reports are independent source assertions."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Observed, estimated, allocated, validated, reconciled, disputed, corrected and final states preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Consumers, resources, activities, assets, facilities, meters, observations, invoices and impacts use typed references."},
            {"dimension": "temporal", "status": "covered", "notes": "Interval, effective, event, observation, record, invoice, correction and ingestion clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Facility, place, measurement boundary and resource-flow endpoints are explicit external references."},
            {"dimension": "provenance", "status": "covered", "notes": "Sources, procedures, calibration, calculation, allocation, review, revision and invalidation are linked."},
            {"dimension": "ownership", "status": "covered", "notes": "Resource ownership, use, custody, operational responsibility and data mastership are not conflated."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, boundary, interval, unit, component, calculation, allocation, tolerance and crosswalk checks are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Role, purpose, commercial sensitivity, minimum projection and audit are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Corrections, disputes, audit or legal hold, withdrawal and tombstones are explicit and non-cascading."},
            {"dimension": "interoperability", "status": "covered", "notes": "ISO, SEEA, UN/CEFACT, SOSA, SensorThings, QUDT, UCUM, RFC, W3C and GRI mappings disclose loss."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Registration, binding, measurement, derivation, allocation, reconciliation, performance, correction and projection declare controlled effects."}
        ],
        "known_omissions": [
            "Resource, sector, facility, jurisdiction, billing, accounting, emissions, impact, privacy, licensing and retention profiles require exact current rules and competent review.",
            "Resource, stock, meter, observation, consumer, activity, asset, facility, invoice, ledger, emissions, impact, waste, target and evidence lifecycles remain in neighboring models.",
            "Certified field crosswalks, tariff and cost allocation, emission factors, LCA impact calculation, forecasting, optimization and autonomous control remain future work."
        ],
        "conflicts": [
            "Energy, water and material systems use consumption, use, withdrawal, input and loss differently; the model requires explicit resource and assertion profiles.",
            "A meter reading, counter delta, allocated amount, invoice quantity, reported value and authoritative balance can disagree without any being safely overwritten.",
            "Absolute consumption, intensity, efficiency, environmental impact, cost and compliance are different governed facts."
        ],
        "regional_assumptions": [
            "ISO and SEEA provide cross-domain management and accounting frameworks rather than universal operational or billing law.",
            "GRI defines sustainability-reporting disclosures and does not become the source master for meter, stock, invoice or impact facts.",
            "Allocation, billing, tax, resource rights, environmental reporting, privacy and retention consequences depend on organization, sector and jurisdiction."
        ],
        "adversarial_checks": [
            "Reject consumption without stable identity, revision, assertion kind, consumer, resource, boundary, interval, qualified quantity, source, method and lineage.",
            "Reject stock, receipt, withdrawal, use, discharge, recovery, export, loss, meter reading, invoice, cost, emissions, impact, forecast or target represented as consumption without a discriminator.",
            "Reject power and energy, or water withdrawal and consumption, collapsed into one quantity kind.",
            "Reject net consumption without explicit gross, return, recovery, export and loss treatment or quantity without compatible unit and conversion evidence.",
            "Reject efficiency, cost, emissions, environmental impact, compliance or causality inferred from absolute consumption alone.",
            "Reject last-write-wins when meter, estimate, allocation, invoice and balance assertions conflict; preserve source, clocks, correction and precedence.",
            "Reject billing, accounting, regulatory reporting, protected disclosure or record destruction outside delegated external authority."
        ]
    }


def build():
    model = {
        "registry_id": "vr.wm-flw-015", "model_id": "WM-FLW-015", "name": "Resource Consumption", "entry_kind": "event",
        "purpose": "Represent one governed source-qualified assertion that a consumer used a qualified quantity of a resource during a defined interval and boundary, including measurement, derivation, allocation, reconciliation and correction lineage.",
        "scope_statement": "Owns consumption identity and revision; assertion kind; consumer, resource, activity, asset, facility, place and system-boundary references; interval and clocks; quantity, unit, precision, tolerance and uncertainty; meter, observation, counter and calibration references; derivation and allocation; gross, return, recovery, export, loss and net components; resource profiles; baseline, target, normalization, intensity, efficiency and variance assertions; lifecycle, evidence, quality, conflict, correction, access, retention and loss-aware projections. Resource, stock, meter, observation, party, asset, activity, process, project, facility, place, invoice, cost, ledger, emissions, footprint, impact, waste, recovery, plan, target, document and evidence masters remain external.",
        "in_scope": ["Consumption identity, assertion kind, revision, consumer-resource-system boundary, interval and lineage", "Qualified quantity, unit, measurement, derivation, allocation, flow components, resource profiles and performance context", "Lifecycle, reconciliation, evidence, quality, governance, access, retention and interoperability"],
        "out_of_scope": ["Owning resource, inventory, meter, observation, consumer, activity, asset, facility, invoice, ledger, emission, impact, waste, target, document or evidence lifecycles", "Equating stock with flow, input with consumption, water withdrawal with consumption, power with energy, meter reading with counter delta, invoice with measured use, absolute use with efficiency, or energy with emissions", "Executing meter control, resource dispatch, billing, ledger posting, regulatory filing, environmental claim, optimization, protected disclosure or irreversible deletion"],
        "boundary_notes": [
            {"neighbor": "WM-FLW-008 Mass-balance / Material Flow", "distinction": "Resource Consumption is one use-side source-qualified flow assertion that may participate in a mass balance. Mass-balance system definition, complete input-output reconciliation and conservation analysis remain external; the candidate parent signal is held for review.", "source_refs": ["SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012"]},
            {"neighbor": "Resource and inventory masters", "distinction": "Consumption binds a resource and may explain a stock reduction, but resource identity, stock balance, ownership, availability and valuation remain external.", "source_refs": ["SRC-007", "SRC-009", "SRC-012"]},
            {"neighbor": "Meter, sensor and observation", "distinction": "Readings and observations support a consumption assertion. Device identity, datastream, calibration and observation lifecycle remain externally mastered.", "source_refs": ["SRC-003", "SRC-014", "SRC-015", "SRC-016", "SRC-017"]},
            {"neighbor": "Invoice, cost, ledger and allocation", "distinction": "Invoice quantities and costs may reconcile with consumption but do not replace its physical quantity and measurement boundary; financial records remain external.", "source_refs": ["SRC-007", "SRC-008", "SRC-009"]},
            {"neighbor": "Emissions, footprint and environmental impact", "distinction": "Consumption is an activity datum for external factor, footprint or LCA calculations. It does not own emission factors, characterization or impact conclusions.", "source_refs": ["SRC-004", "SRC-005", "SRC-006", "SRC-023", "SRC-024"]},
            {"neighbor": "Baseline, target, plan and forecast", "distinction": "The model records references and comparison assertions. Baseline models, targets, plans, forecasts and accountable performance decisions remain external masters.", "source_refs": ["SRC-001", "SRC-002", "SRC-003"]},
            {"neighbor": "Water, energy and material profiles", "distinction": "The common root preserves generic identity, boundary, quantity and provenance, while domain profiles define withdrawal, discharge, carrier, conversion, renewable, recycled and quality semantics.", "source_refs": ["SRC-006", "SRC-010", "SRC-011", "SRC-012", "SRC-022", "SRC-023", "SRC-024"]}
        ]
    }
    composition = [
        {"target": "WM-FLW-008 Mass-balance / Material Flow", "relation": "REFERENCE", "purpose": "Participate as a use-side flow assertion while the candidate parent relation remains under joint boundary review.", "required": False, "source_refs": ["SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012"]},
        {"target": "Resource, inventory, consumer, activity, asset, facility and place masters", "relation": "REFERENCE", "purpose": "Resolve subjects and context while preserving external identity and lifecycle authority.", "required": True, "source_refs": ["SRC-001", "SRC-004", "SRC-007", "SRC-009"]},
        {"target": "Meter, sensor, datastream, observation and calibration masters", "relation": "REFERENCE", "purpose": "Resolve measurement evidence without importing device or observation lifecycles.", "required": False, "source_refs": ["SRC-003", "SRC-014", "SRC-015", "SRC-016", "SRC-017"]},
        {"target": "Invoice, cost, ledger, emissions, footprint, impact, waste, plan and target masters", "relation": "REFERENCE", "purpose": "Resolve derived, financial, environmental and planning contexts without conflating them with consumption.", "required": False, "source_refs": ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-023", "SRC-024"]},
        {"target": "ISO 50001, ISO 50006 and ISO 50015", "relation": "ALIGN", "purpose": "Project energy management, baseline, indicator and measurement-verification semantics.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003"]},
        {"target": "ISO 14040, ISO 14044, ISO 14046, ISO 14051 and ISO 14052", "relation": "ALIGN", "purpose": "Project life-cycle, water-footprint, material-flow, allocation and supply-chain accounting contexts.", "required": False, "source_refs": ["SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008"]},
        {"target": "SEEA physical energy, water and material flow accounts", "relation": "ALIGN", "purpose": "Project economy-environment input, use, return, residual, stock and physical-flow accounting views.", "required": False, "source_refs": ["SRC-009", "SRC-010", "SRC-011", "SRC-012"]},
        {"target": "UN/CEFACT Recommendation 20, QUDT and UCUM", "relation": "ALIGN", "purpose": "Project quantity-kind, unit-code, dimensional and conversion semantics.", "required": False, "source_refs": ["SRC-013", "SRC-016", "SRC-017"]},
        {"target": "SOSA/SSN and OGC SensorThings", "relation": "ALIGN", "purpose": "Project sensor, observation, procedure, result and datastream references.", "required": False, "source_refs": ["SRC-014", "SRC-015"]},
        {"target": "RFC 3339, PROV-O, DQV and ODRL", "relation": "ALIGN", "purpose": "Project temporal, provenance, quality and governed-access semantics.", "required": False, "source_refs": ["SRC-018", "SRC-019", "SRC-020", "SRC-021"]},
        {"target": "GRI 301, GRI 302 and GRI 303", "relation": "ALIGN", "purpose": "Project organizational materials, energy and water disclosure views as reporting profiles.", "required": False, "source_refs": ["SRC-022", "SRC-023", "SRC-024"]}
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
