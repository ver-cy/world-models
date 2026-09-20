#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-DAT-010."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T13:42:00Z"


def src(i, title, org, url, version, kind, relevance):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": 1, "accessed_at": AT,
        "relevance": relevance,
    }


SOURCES = [
    src(1, "SDMX Technical Specifications", "SDMX",
        "https://sdmx.org/standards-2/", "SDMX 3.1 released May 2025", "standard",
        "Defines syntax-neutral statistical structures, series keys, observations, attributes and versioned exchange projections."),
    src(2, "Observations, measurements and samples", "Open Geospatial Consortium",
        "https://docs.ogc.org/as/20-082r4/20-082r4.html", "OGC 20-082r4 version 3.0.0 published 26 May 2023; identical technical content to ISO 19156:2023", "standard",
        "Defines observation acts, results, procedures, observed properties, features of interest and sampling features."),
    src(3, "Semantic Sensor Network Ontology 2023 Edition", "World Wide Web Consortium",
        "https://www.w3.org/TR/vocab-ssn-2023/", "W3C Recommendation 5 December 2024", "ontology",
        "Defines observations, sensors, procedures, properties, features and ObservationCollection semantics including time-series examples."),
    src(4, "The RDF Data Cube Vocabulary", "World Wide Web Consortium",
        "https://www.w3.org/TR/vocab-data-cube/", "W3C Recommendation 16 January 2014", "ontology",
        "Defines datasets, observations, dimensions, measures, attributes, slices and integrity constraints for multidimensional data."),
    src(5, "Time Ontology in OWL", "World Wide Web Consortium and Open Geospatial Consortium",
        "https://www.w3.org/TR/owl-time/", "W3C Candidate Recommendation Draft 15 November 2022; OGC 16-071r3", "ontology",
        "Defines instants, intervals, duration, ordering, temporal position, calendars and alternative temporal reference systems."),
    src(6, "PROV-O: The PROV Ontology", "World Wide Web Consortium",
        "https://www.w3.org/TR/prov-o/", "W3C Recommendation 30 April 2013", "ontology",
        "Defines entities, activities, agents, attribution, generation, derivation, revision and qualified provenance."),
    src(7, "Data on the Web Best Practices: Data Quality Vocabulary", "World Wide Web Consortium",
        "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note 15 December 2016", "ontology",
        "Defines quality dimensions, metrics, measurements, annotations, policies and certificates."),
    src(8, "Data Catalog Vocabulary DCAT Version 3", "World Wide Web Consortium",
        "https://www.w3.org/TR/vocab-dcat-3/", "W3C Recommendation 22 August 2024", "ontology",
        "Defines datasets, distributions, data services, versions, temporal coverage and catalog interoperability."),
    src(9, "Model for Tabular Data and Metadata on the Web", "World Wide Web Consortium",
        "https://www.w3.org/TR/tabular-data-model/", "W3C Recommendation 17 December 2015", "standard",
        "Defines annotated tables, schemas, datatypes, nulls, foreign keys and metadata needed for CSV projections."),
    src(10, "Generic Statistical Information Model version 2.0 User Guide", "United Nations Economic Commission for Europe",
        "https://unece.org/info/publications/pub/400014", "GSIM 2.0 released December 2023; User Guide November 2024", "public-authority",
        "Defines reusable statistical information classes, variables, data structures, datasets and production relationships."),
    src(11, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force",
        "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339 July 2002, updated by RFC 9557", "standard",
        "Defines interoperable Internet timestamps with seconds and explicit relationship to UTC."),
    src(12, "Date and time - Representations for information interchange - Part 1", "International Organization for Standardization",
        "https://www.iso.org/standard/70907.html", "ISO 8601-1:2019 confirmed 2024; Amendment 1:2022", "standard",
        "Public metadata grounds machine-readable date, time and UTC-shift representation; restricted text was not inferred."),
    src(13, "DataCite Metadata Schema", "DataCite",
        "https://schema.datacite.org/", "Metadata Schema 4.7 released 3 March 2026", "standard",
        "Defines current dataset citation, creator, publisher, version, relation, rights, dates and coverage metadata."),
    src(14, "NetCDF Climate and Forecast Metadata Conventions", "CF Conventions Committee",
        "https://cfconventions.org/conventions.html", "CF 1.13 released December 2025", "standard",
        "Defines multidimensional scientific variables, coordinates, time units, calendars, bounds, missing values and quality flags."),
    src(15, "Observation - FHIR R5", "Health Level Seven International",
        "https://hl7.org/fhir/R5/observation-definitions.html", "FHIR R5 5.0.0 generated 26 March 2023", "standard",
        "Healthcare profile distinguishes effective time, issued time, status, value, data-absent reason, method, device and derivation."),
]


ROWS = [
    ("series-identity-semantics-and-dimensional-structure", "Series identity, semantics and dimensional structure", "Make each collection and series definition stable, comparable and independently governed", [
        ("collection-series-identity-version-and-authority", "Collection and series identity, version and authority", ["SRC-001", "SRC-004", "SRC-008", "SRC-010", "SRC-013"], [
            ("collection-series-id-version-head-status-owner-and-purpose", "Collection, series ID, version, head, status, owner and purpose", "identity", True),
            ("series-key-boundary-membership-profile-and-compatibility", "Series key, boundary, membership profile and compatibility", "constraint", True),
        ]),
        ("variable-measure-unit-dimensions-and-classifications", "Variable, measure, unit, dimensions and classifications", ["SRC-001", "SRC-004", "SRC-010", "SRC-014", "SRC-015"], [
            ("variable-indicator-observed-property-measure-unit-scale-and-datatype", "Variable, indicator, observed property, measure, unit, scale and datatype", "measurement", True),
            ("dimension-key-coordinate-classification-code-list-and-concept", "Dimension, key, coordinate, classification, code list and concept", "classification", True),
        ]),
    ]),
    ("observation-membership-values-and-states", "Observation membership, values and states", "Represent ordered observations without confusing a value with its meaning or collection", [
        ("observation-identity-membership-order-and-integrity", "Observation identity, membership, order and integrity", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-010"], [
            ("observation-id-series-membership-dimension-key-and-order", "Observation ID, series membership, dimension key and order", "composition", True),
            ("collection-cardinality-completeness-duplicate-gap-and-overlap", "Collection cardinality, completeness, duplicate, gap and overlap", "validation", True),
        ]),
        ("result-value-status-flags-and-missingness", "Result value, status, flags and missingness", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-014", "SRC-015"], [
            ("result-value-type-unit-precision-resolution-range-and-component", "Result value, type, unit, precision, resolution, range and component", "measurement", True),
            ("status-flag-missing-not-applicable-suppressed-confidential-and-provisional", "Status, flag, missing, not applicable, suppressed, confidential and provisional", "state", True),
        ]),
    ]),
    ("temporal-semantics-frequency-calendars-and-vintages", "Temporal semantics, frequency, calendars and vintages", "Keep real-world, observation, publication and system times distinct", [
        ("reference-phenomenon-validity-period-and-calendar", "Reference, phenomenon, validity period and calendar", ["SRC-001", "SRC-002", "SRC-003", "SRC-005", "SRC-011", "SRC-012", "SRC-014", "SRC-015"], [
            ("phenomenon-reference-effective-validity-instant-interval-and-bounds", "Phenomenon, reference, effective, validity, instant, interval and bounds", "temporal", True),
            ("frequency-periodicity-cadence-calendar-time-zone-offset-and-precision", "Frequency, periodicity, cadence, calendar, time zone, offset and precision", "temporal", True),
        ]),
        ("result-availability-release-revision-vintage-and-knowledge-time", "Result, availability, release, revision, vintage and knowledge time", ["SRC-001", "SRC-005", "SRC-006", "SRC-008", "SRC-011", "SRC-012", "SRC-015"], [
            ("result-issued-available-release-embargo-and-publication-time", "Result, issued, available, release, embargo and publication time", "temporal", True),
            ("revision-vintage-recorded-ingestion-transaction-and-knowledge-time", "Revision, vintage, recorded, ingestion, transaction and knowledge time", "provenance", True),
        ]),
    ]),
    ("coverage-sampling-transformations-and-forecast-qualifiers", "Coverage, sampling, transformations and forecast qualifiers", "Describe what a sequence covers and how values were formed or projected", [
        ("feature-population-space-sample-and-granularity", "Feature, population, space, sample and granularity", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-008", "SRC-010", "SRC-013", "SRC-014"], [
            ("feature-of-interest-population-domain-spatial-and-thematic-coverage", "Feature of interest, population, domain, spatial and thematic coverage", "relationship", True),
            ("sample-frame-specimen-sampling-method-cadence-granularity-and-weight", "Sample frame, specimen, sampling method, cadence, granularity and weight", "measurement", False),
        ]),
        ("aggregation-transformation-adjustment-forecast-and-scenario", "Aggregation, transformation, adjustment, forecast and scenario", ["SRC-001", "SRC-004", "SRC-006", "SRC-007", "SRC-010", "SRC-014"], [
            ("aggregation-weighting-index-base-normalization-seasonal-adjustment-and-chain", "Aggregation, weighting, index base, normalization, seasonal adjustment and chain", "process", False),
            ("observed-estimated-nowcast-forecast-scenario-horizon-quantile-and-confidence", "Observed, estimated, nowcast, forecast, scenario, horizon, quantile and confidence", "classification", True),
        ]),
    ]),
    ("source-provenance-quality-and-revision", "Source, provenance, quality and revision", "Make every value traceable and every quality or correction claim evidence-qualified", [
        ("source-procedure-sensor-run-and-lineage", "Source, procedure, sensor, run and lineage", ["SRC-001", "SRC-002", "SRC-003", "SRC-006", "SRC-010", "SRC-014", "SRC-015"], [
            ("source-dataset-api-sensor-device-procedure-method-and-feature-binding", "Source dataset, API, sensor, device, procedure, method and feature binding", "provenance", True),
            ("collection-processing-run-software-operator-input-output-and-lineage", "Collection, processing run, software, operator, input, output and lineage", "provenance", True),
        ]),
        ("validation-quality-uncertainty-anomaly-and-correction", "Validation, quality, uncertainty, anomaly and correction", ["SRC-001", "SRC-002", "SRC-006", "SRC-007", "SRC-010", "SRC-014", "SRC-015"], [
            ("validation-rule-quality-dimension-metric-uncertainty-confidence-anomaly-and-outlier", "Validation rule, quality dimension, metric, uncertainty, confidence, anomaly and outlier", "quality", True),
            ("revision-correction-benchmark-restatement-backcast-retraction-and-supersession", "Revision, correction, benchmark, restatement, backcast, retraction and supersession", "lifecycle", True),
        ]),
    ]),
    ("lifecycle-access-distribution-and-interoperability", "Lifecycle, access, distribution and interoperability", "Publish usable projections while preserving governance, history and semantic loss", [
        ("lifecycle-release-access-rights-and-records", "Lifecycle, release, access, rights and records", ["SRC-001", "SRC-006", "SRC-007", "SRC-008", "SRC-010", "SRC-013"], [
            ("draft-validated-released-superseded-withdrawn-and-data-availability", "Draft, validated, released, superseded, withdrawn and data availability", "lifecycle", True),
            ("access-privacy-license-embargo-retention-legal-hold-tombstone-and-audit", "Access, privacy, license, embargo, retention, legal hold, tombstone and audit", "access", True),
        ]),
        ("distribution-api-packaging-integrity-and-projections", "Distribution, API, packaging, integrity and projections", [f"SRC-{i:03d}" for i in range(1, 16)], [
            ("distribution-format-media-type-api-query-pagination-chunk-compression-and-checksum", "Distribution, format, media type, API, query, pagination, chunk, compression and checksum", "interoperability", True),
            ("sdmx-oms-ssn-data-cube-time-prov-dqv-dcat-csvw-gsim-rfc-iso-datacite-cf-and-fhir-projection", "SDMX, OMS, SSN, Data Cube, Time, PROV, DQV, DCAT, CSVW, GSIM, RFC, ISO, DataCite, CF and FHIR projection", "interoperability", True),
        ]),
    ]),
]

KINDS = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def finding(item, n, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(n + 8) % len(KINDS)], KINDS[(n + 17) % len(KINDS)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {low} as source-qualified collection context while observation, sensor, procedure, feature, statistical unit, source dataset, processing run, release and records masters remain independently identifiable.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What stable identity, version, typed value, dimensions, unit, scope and explicit unknown establish {low}?", "kind": kinds[0], "answer_data": ["collection, series, observation, dimension and external master identifiers", "typed value, unit, scale, vocabulary, schema, profile and algorithm version", "unknown, missing, suppressed, provisional, disputed and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who owns, observes, supplies, transforms, asserts, reviews, approves or may use {low}, for which purpose and under what authority?", "kind": kinds[1], "answer_data": ["actor, agent, role, organization, sensor, software and contact", "purpose, authority, policy, access, license, confidentiality and retention", "conflict, exception, escalation and accountability"]},
            {"id": f"{fid}-q03", "text": f"Which phenomenon, reference, result, availability, release, revision, recorded, ingestion and knowledge times, evidence and uncertainty qualify {low}?", "kind": kinds[2], "answer_data": ["distinct real-world, observation, publication, revision and system times", "source, procedure, method, run, lineage, metric, confidence and limitation", "successor, correction, supersession, legal hold and audit"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed time-series data for {low}, qualified by series key, version, time, unit, authority, uncertainty and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned evidence for {low}.", "media_or_form": ["logical time-series specification assertion", "definition, observation, value, flag, method, quality, correction, release or projection record"], "serial": True, "identity_strategy": f"Series ID plus independent series version, observation ID or dimension-key and phenomenon time, then revision or vintage ID and artifact kind for {fid}; a timestamp, row number, label or digest never identifies an observation alone.", "source_refs": refs}],
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
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified time-series context for {lname.lower()}.", "source_refs": refs, "findings": fs})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed collection context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({r for layer in layers for r in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-series", "Register a time series or observation collection", ["owner", "purpose", "series definition and initial scope"], ["stable collection and series version head"], ["namespace, identity, authority, purpose, variable, unit and duplicate checks pass"], ["a versioned collection exists without creating observations"], ["SRC-001", "SRC-003", "SRC-004", "SRC-010"]),
    ("define-series-structure", "Define series dimensions, measures and keys", ["series version", "variables", "dimensions and code lists"], ["versioned series structure"], ["measure, unit, dimension, classification, key uniqueness and profile checks pass"], ["permitted observation coordinates become explicit"], ["SRC-001", "SRC-004", "SRC-010", "SRC-014"]),
    ("append-observation", "Append or bind an observation", ["series head", "observation assertion", "source authority"], ["successor membership assertion"], ["identity, dimension key, value, unit, time, status, source and expected revision checks pass"], ["the observation becomes a qualified member without rewriting history"], ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-015"]),
    ("validate-order-gaps-and-duplicates", "Validate order, gaps, overlaps and duplicates", ["collection version", "frequency and calendar", "validation rules"], ["validation and exception evidence"], ["time, key, cadence, boundary, missing-state and rule-version checks pass"], ["issues are asserted without imputing or deleting values"], ["SRC-001", "SRC-004", "SRC-007", "SRC-014"]),
    ("qualify-time-and-vintage", "Qualify temporal semantics and vintage", ["observation or series", "temporal assertion", "clock and calendar profile"], ["multi-time and vintage binding"], ["phenomenon, result, release, revision, recorded, ingestion and knowledge times are disambiguated"], ["later knowledge does not overwrite earlier vintages"], ["SRC-001", "SRC-005", "SRC-011", "SRC-012", "SRC-014", "SRC-015"]),
    ("record-transformation", "Record aggregation, adjustment or derivation", ["input observations", "method and parameters", "processing run"], ["derived series or observations with lineage"], ["algorithm, version, unit, weighting, base, calendar, input, output and uncertainty checks pass"], ["derived values remain separate from source observations"], ["SRC-001", "SRC-006", "SRC-007", "SRC-010", "SRC-014"]),
    ("record-forecast-or-scenario", "Record forecast, nowcast or scenario values", ["series definition", "model run", "scenario and horizon"], ["qualified projected observation collection"], ["estimate class, cutoff, horizon, scenario, quantile, confidence, run and source checks pass"], ["projected values cannot masquerade as observed facts"], ["SRC-001", "SRC-006", "SRC-007", "SRC-010"]),
    ("assess-quality-and-correct", "Assess quality and issue a correction", ["collection version", "quality evidence", "authorized correction decision"], ["quality assertion and successor correction"], ["metric, method, scope, confidence, reason, authority, revision and audit checks pass"], ["issued observations remain immutable and successors are linked"], ["SRC-001", "SRC-006", "SRC-007", "SRC-010", "SRC-015"]),
    ("release-supersede-or-withdraw", "Release, supersede or withdraw a collection", ["collection head", "review evidence", "authorized lifecycle decision"], ["successor lifecycle and availability assertion"], ["expected revision, approval, rights, access, embargo, effective time and retention checks pass"], ["data lifecycle stays distinct from distribution availability"], ["SRC-001", "SRC-006", "SRC-008", "SRC-013"]),
    ("query-project-retain-and-audit", "Query, project, retain and audit", ["collection", "target profile", "purpose-bound access and records policy"], ["filtered projection, retention result or audit event"], ["purpose, authority, mapping, loss, confidentiality, hold, checksum and retention checks pass"], ["protected values stay governed and projections declare loss"], [f"SRC-{i:03d}" for i in range(1, 16)]),
]


def functions():
    return [{"id": x[0], "name": x[1], "description": f"Governed operation to {x[1].lower()} without autonomous ingestion, imputation, recalculation, revision, suppression, release, certification, unit change, access widening or records disposition.", "inputs": x[2], "outputs": x[3], "preconditions": x[4], "effects": x[5], "source_refs": x[6]} for x in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner, namespace authority, data governance mandate and accountable series owner", "Authoritative Series, Observation, Variable, Classification, Unit, Sensor, Procedure, Feature, Population, Source Dataset, Processing Run, Release, Audit and Records registries", "Approved terminology, units, calendars, quality, privacy, access, retention and interoperability profiles", "Role, delegation, validation, correction, publication, withdrawal and agent-operation policies"],
            "namespace_guidance": "Mint collection, series, series-version, observation, dimension-key, vintage, processing-run, quality, correction, release, distribution and projection IDs; preserve every external master identifier.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize a series by authoritative series identifier, owner namespace, versioned structure and series key, never by title, URL, timestamp or file digest alone.", "Keep collection, series definition, observation, variable, sensor, procedure, feature, source dataset, processing run, release, vintage and distribution independently identifiable."],
            "patch_rules": ["Extensions declare dimension, measure, unit, time, value, quality, provenance, privacy, lifecycle and interoperability effects.", "Released series and observations are immutable; changes create linked successors or explicit new vintages with reason, compatibility, migration and review.", "Never silently change a series key, dimension, classification, measure, unit, calendar, frequency, value, flag, missing state, source, method or time semantics."],
            "compatibility_rules": ["Ignore additive fields only when identity, dimensions, measure, unit, time, value, status, authority, privacy and provenance survive.", "Every projection pins standard, schema, vocabulary, calendar, unit and mapping versions and declares information loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each collection, series, observation, run, vintage, release, distribution or artifact, qualified by issuer, namespace and record kind.", "Governed globally resolvable series or observation IRI.", "Dimension UUID or ULID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish phenomenon, reference, validity, result, availability, release, revision, recorded, ingestion, transaction and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {series-id}--{series-version}--{observation-id-or-dimension-key}--{vintage-or-revision-id}--{artifact-kind}.",
            "integrity_rule": "Store digest, media type, record kind, series and coverage scope, schema and profile versions, actor or process, distinct event and knowledge times, confidentiality marking and provenance.",
        },
        "policies": ["The collection owns series definitions, observation membership, qualified values, versions and projections but not external variable, sensor, procedure, feature, statistical unit, source dataset, processing run, release, audit or records masters.", "An observation value is an assertion qualified by property, unit, time, method, source, quality, uncertainty, status and provenance; it is not timeless ground truth.", "Observed, estimated, imputed, adjusted, nowcast, forecast and scenario values must remain distinguishable.", "Agents cannot autonomously ingest, impute, recalculate, revise, suppress, publish, certify, change units, widen access or dispose records without delegated authority."],
        "crud": {
            "read": ["Resolve collection head, series structure, observations, distinct times, vintages, values, flags, coverage, transformations, provenance, quality, access, lifecycle and projection loss under the permitted view."],
            "create": ["Bind stable identity, owner, purpose, series key, variable, measure, unit, dimensions, calendars, source authority and initial lifecycle before observations are accepted."],
            "update": ["Append successor definitions, observations, vintages, flags, methods, quality assertions, corrections, releases and lifecycle events with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply legal hold, reproducibility, privacy, security and adopting-Dimension records policy; withdraw or tombstone only the catalog view without cascading to external masters, and let authoritative systems execute physical disposition."],
        },
        "roles": [
            {"name": "Series owner", "responsibilities": ["Own purpose, scope, series definitions, lifecycle, compatibility and accountable use."]},
            {"name": "Data steward", "responsibilities": ["Own identifiers, dimensions, variables, units, classifications, missing states and metadata quality."]},
            {"name": "Method and measurement owner", "responsibilities": ["Own sampling, sensor, procedure, transformation, adjustment, forecast and uncertainty semantics."]},
            {"name": "Source and pipeline custodian", "responsibilities": ["Own source bindings, processing runs, lineage, ingestion evidence, checksums and operational controls."]},
            {"name": "Quality reviewer", "responsibilities": ["Own validation rules, quality metrics, anomaly review, limitations, corrections and certification decisions."]},
            {"name": "Access, privacy and records authority", "responsibilities": ["Own purpose, confidentiality, access, license, embargo, retention, legal hold and disposition policy."]},
            {"name": "Publication and interoperability steward", "responsibilities": ["Own releases, withdrawals, distributions, APIs, projection versions, declared loss and auditability."]},
        ],
        "access": {
            "default_rule": "Deny unreleased, confidential, personal, security-sensitive, embargoed, fine-grained or reconstruction-capable values unless a purpose-bound policy permits the minimum necessary view.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Declared research, safety, incident, privacy, legal, audit or subject-rights access must cite authority, scope, purpose and time limit and must be logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, collection and series version, operation, authority, policy, RFC 3339 time, affected observations or keys, source revision and outcome without duplicating restricted values."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read Dimension data governance, namespace, variable, unit, calendar, privacy, access, retention and agent policies.", "Read this collection and linked observation, sensor, procedure, feature, population, source dataset, processing run, release, audit and records models before mutation."],
        },
    }


def coverage():
    dims = ["identity", "classification and direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability", "authority and ethics"]
    return {
        "claim": "Covers one governed time series or observation collection from identity and dimensional structure through observations, values, multi-time semantics, vintages, coverage, transformations, forecasts, provenance, quality, corrections, lifecycle, access, distributions and projections.",
        "confidence": "medium",
        "checklist": [{"dimension": d, "status": "covered", "notes": f"{d.capitalize()} is explicit; domain, jurisdiction, measurement, forecast, quality, privacy and external-review profiles remain held where applicable."} for d in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "No relation row is frozen; the WM-MAT-008 parent signal grants no approved ownership or cascade behavior.", "Financial market ticks, industrial telemetry, climate grids, clinical observations, event sourcing, streaming systems and jurisdiction-specific statistics require separate profiles.", "ISO 8601-1:2019 is used only from public scope and lifecycle metadata; access-restricted requirements were not inferred.", "SSN ObservationCollection is identified by its 2023 Edition text as non-normative pending implementation experience and is treated as an alignment profile, not sole canon."],
        "conflicts": ["Series definition, observation collection, individual observation, sensor, feature, statistical unit, source dataset, processing run, release, vintage and distribution are not interchangeable identities.", "Phenomenon, reference, validity, result, availability, release, revision, recorded, ingestion, transaction and knowledge times are not one timestamp.", "Observed, estimated, imputed, adjusted, nowcast, forecast and scenario values require distinct classes and provenance.", "Missing, not applicable, suppressed, confidential, below detection, invalid, provisional and absent require distinct states."],
        "regional_assumptions": ["Privacy, confidentiality, disclosure control, embargo, retention, audit, legal hold and certification depend on jurisdiction, organization, population and domain.", "SDMX, OMS, SSN, RDF Data Cube, CF and FHIR are overlapping statistical, geospatial, sensor, linked-data, climate and healthcare profiles; none is universal."],
        "adversarial_checks": ["Reject a package that collapses the series definition, collection and observation into one identity.", "Reject a value without measure or observed property, unit or datatype, dimensions, time semantics, status, source and provenance.", "Reject a timestamp without seconds and explicit offset or Z, or a model that collapses event and knowledge time.", "Reject silent imputation, aggregation, unit conversion, seasonal adjustment, revision, suppression or forecast-to-observation conversion.", "Reject autonomous ingestion, recalculation, publication, certification, access widening or records disposition.", "Reject a projection that hides dimensions, units, calendars, missing states, vintages, provenance, quality or information loss."],
    }


def build():
    model = {
        "registry_id": "vr.wm-dat-010", "model_id": "WM-DAT-010", "name": "Time Series / Observation Collection", "entry_kind": "aggregate",
        "purpose": "Represent one governed, versioned collection of ordered observations so agents can interpret values, dimensions, time, vintages, quality and provenance without confusing a series definition, individual observation, release or forecast.",
        "scope_statement": "Owns collection and series identity, versions, keys and lifecycle; variable, indicator, measure, unit, dimension and classification bindings; observation membership and order; qualified values, components, status, flags and missingness; phenomenon, reference, validity, result, availability, release, revision, recorded, ingestion and knowledge times; frequency, calendars and time zones; coverage, sampling and granularity; transformations, adjustments, forecasts and uncertainty; source, procedure, sensor, processing and lineage bindings; validation, quality, anomaly, correction and restatement evidence; access, retention, distribution and interoperability projections. External variable, sensor, procedure, feature, statistical unit, source dataset, processing run, release, audit and records masters remain independently authoritative.",
        "in_scope": ["Collection and series identity, structure, dimensions, variables, measures, units, observations, order, values, flags, missingness and multi-time semantics", "Vintages, coverage, sampling, transformations, forecasts, provenance, quality, corrections, lifecycle, access, distributions and interoperability projections"],
        "out_of_scope": ["Owning Variable, Classification, Unit, Sensor, Procedure, Feature of Interest, Statistical Unit, Population, Source Dataset, Processing Run, Release, Audit or Records masters", "Treating an observation assertion as timeless ground truth or collapsing observed, estimated, imputed, adjusted, forecast and scenario values", "Autonomous ingestion, imputation, recalculation, revision, suppression, publication, certification, unit change, access widening or physical records disposition"],
        "boundary_notes": [
            {"neighbor": "WM-MAT-008 parent signal", "distinction": "The unfrozen parent signal may identify a matrix or tabular context, but no approved relation row exists and it grants no ownership, mutation or cascade authority.", "source_refs": ["SRC-001", "SRC-004", "SRC-010"]},
            {"neighbor": "Series definition, observation collection and observation", "distinction": "The definition fixes meaning and key space, the collection governs membership and versions, and each observation is a separately qualified assertion.", "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004"]},
            {"neighbor": "Sensor, procedure, feature, statistical unit, source dataset and processing run", "distinction": "These external masters explain what produced or is described by values; the collection stores non-owning references and lineage only.", "source_refs": ["SRC-002", "SRC-003", "SRC-006", "SRC-010", "SRC-015"]},
            {"neighbor": "Release, vintage, revision and distribution", "distinction": "Release and availability decisions, knowledge vintages, correction lineage and transport packages are distinct from the semantic collection head.", "source_refs": ["SRC-001", "SRC-006", "SRC-008", "SRC-013"]},
            {"neighbor": "SDMX, OMS, SSN, RDF Data Cube, OWL-Time, PROV, DQV, DCAT, CSVW, GSIM, RFC 3339, ISO 8601, DataCite, CF and FHIR profiles", "distinction": "Each source has a distinct scope and normative force. Every mapping is version-pinned, profile-qualified and loss-declaring.", "source_refs": [f"SRC-{i:03d}" for i in range(1, 16)]},
        ],
    }
    composition = [
        {"target": "WM-MAT-008", "relation": "REFERENCE", "purpose": "Represent the unfrozen matrix or tabular context without approved ownership, mutation or cascade authority.", "required": False, "source_refs": ["SRC-001", "SRC-004", "SRC-010"]},
        {"target": "Variable, Classification, Code List and Unit models", "relation": "REFERENCE", "purpose": "Resolve independently governed observation meaning, dimensions and units.", "required": True, "source_refs": ["SRC-001", "SRC-004", "SRC-010", "SRC-014", "SRC-015"]},
        {"target": "Observation, Sensor, Procedure, Feature, Statistical Unit, Population and Source Dataset models", "relation": "REFERENCE", "purpose": "Resolve authoritative observations, producers, subjects, populations and sources without absorbing their lifecycles.", "required": False, "source_refs": ["SRC-002", "SRC-003", "SRC-006", "SRC-010", "SRC-015"]},
        {"target": "Processing Run, Release, Audit and Records models", "relation": "REFERENCE", "purpose": "Resolve derivation, operational publication, audit and disposition authorities.", "required": False, "source_refs": ["SRC-001", "SRC-006", "SRC-008", "SRC-010", "SRC-013"]},
        {"target": "SDMX 3.1, OMS 3.0, SSN 2023, RDF Data Cube, OWL-Time, PROV-O, DQV, DCAT 3, CSVW, GSIM 2.0, RFC 3339, ISO 8601-1:2019, DataCite 4.7, CF 1.13 and FHIR R5", "relation": "ALIGN", "purpose": "Project version-pinned statistical, observation, sensor, linked-data, temporal, provenance, quality, catalog, tabular, citation, scientific and health views with declared loss.", "required": False, "source_refs": [f"SRC-{i:03d}" for i in range(1, 16)]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
