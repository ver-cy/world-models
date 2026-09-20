#!/usr/bin/env python3
"""Build the source-grounded Codex fallback result for WM-ACT-023."""

from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED_AT = "2026-09-06T02:00:00Z"


def source(source_id, title, organization, url, version, source_type, relevance, tier=1):
    return {
        "id": source_id, "title": title, "organization": organization,
        "url": url, "version_or_date": version, "source_type": source_type,
        "primary_source": True, "authority_tier": tier,
        "accessed_at": ACCESSED_AT, "relevance": relevance,
    }


SOURCES = [
    source("SRC-001", "International Health Regulations (2005) as amended in 2014, 2022 and 2024", "World Health Organization", "https://www.who.int/health-topics/international-health-regulations/", "Current text effective from 19 September 2025", "legislation", "Defines internationally governed public-health event assessment, notification and response boundaries without making WHO the owner of national records."),
    source("SRC-002", "WHO Global Health Observatory Indicator Metadata Registry", "World Health Organization", "https://www.who.int/data/gho/indicator-metadata-registry/", "Current registry accessed 2026-09-06", "registry", "Demonstrates that comparable population-health indicators require governed definitions and dimensions rather than labels alone."),
    source("SRC-003", "Early Warning, Alert and Response System", "World Health Organization", "https://www.who.int/emergencies/surveillance/early-warning-alert-and-response-system-ewars/", "Current programme documentation accessed 2026-09-06", "public-authority", "Supports early-warning surveillance, signal detection and response use in emergency settings."),
    source("SRC-004", "Manual for respiratory virus vaccination coverage", "World Health Organization", "https://www.who.int/westernpacific/publications/i/item/9789240118829", "26 June 2026, ISBN 9789240118829", "public-authority", "Provides current guidance on comparable coverage indicators, data systems, equity, programme performance and reporting."),
    source("SRC-005", "How We Conduct Case Surveillance", "Centers for Disease Control and Prevention", "https://www.cdc.gov/nndss/what-is-case-surveillance/conducting.html", "Updated 12 January 2026", "public-authority", "Distinguishes mandatory local case reporting from voluntary de-identified national case notification and describes the surveillance data supply chain."),
    source("SRC-006", "Surveillance Case Definitions for Current and Historical Conditions", "Centers for Disease Control and Prevention", "https://ndc.services.cdc.gov/", "Current definitions registry accessed 2026-09-06", "registry", "States that surveillance case definitions support consistent classification and counting and are not clinical diagnostic rules."),
    source("SRC-007", "FHIR R5 MeasureReport", "Health Level Seven International", "https://www.hl7.org/fhir/R5/measurereport-definitions.html", "FHIR R5 5.0.0", "standard", "Defines a versioned measure-result structure with subject or population, period, groups, stratifiers, counts and scores.", 2),
    source("SRC-008", "FHIR R5 Immunization", "Health Level Seven International", "https://www.hl7.org/fhir/immunization.html", "FHIR R5 5.0.0", "standard", "Supplies interoperable immunization event and product terminology used only as an aggregate-source alignment in this population model.", 2),
    source("SRC-009", "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Provides entity, activity, agent, derivation, attribution and revision semantics for epidemiologic assertions and releases."),
    source("SRC-010", "RFC 3339: Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339", "RFC 3339, July 2002", "standard", "Defines interoperable event timestamps with seconds and explicit offset."),
]


# Bundle: id, name, description, rationale, refs, layers.
# Layer: id, name, description, refs, findings.
# Finding: id, name, description, question kind, refs, value kind, required, artifact.
STRUCTURE = [
    ("population-scope-and-mandate", "Population scope and mandate", "Defines the governed population-health observation frame and responsible authority.", "Population and cohort identity, geography, time and mandate must be pinned before any aggregate can be interpreted or shared.", ["SRC-001", "SRC-002", "SRC-005", "SRC-009"], [
        ("population-cohort-and-place", "Population, cohort and place", "The people-at-risk frame and its spatial and membership semantics.", ["SRC-002", "SRC-005", "SRC-007"], [
            ("target-population-and-cohort-definition", "Target population and cohort definition", "Versioned inclusion, exclusion, age, sex, risk, eligibility and denominator criteria at permitted aggregate grain.", "definition", ["SRC-002", "SRC-004", "SRC-007"], "object", True, True),
            ("geographic-area-time-period-and-grain", "Geographic area, time period and grain", "Authoritative area references, observation period, aggregation cadence and minimum publishable spatial-temporal grain.", "spatial", ["SRC-001", "SRC-002", "SRC-005", "SRC-010"], "object", True, True),
        ]),
        ("purpose-authority-and-profile", "Purpose, authority and profile", "Public-health purpose, legal mandate and applicable profile.", ["SRC-001", "SRC-005", "SRC-006"], [
            ("surveillance-purpose-and-record-authority", "Surveillance purpose and record authority", "Declared prevention, detection, monitoring, evaluation or reporting purpose plus the authority that masters the aggregate.", "authority", ["SRC-001", "SRC-005"], "object", True, True),
            ("jurisdiction-condition-and-profile-binding", "Jurisdiction, condition and profile binding", "Pinned jurisdiction, condition classification, case definition, disclosure profile and effective versions.", "requirement", ["SRC-001", "SRC-006"], "collection", True, False),
        ]),
    ]),
    ("indicator-and-series", "Indicator and series", "Defines population-health measures and preserves comparable time-series observations.", "A numeric value is uninterpretable without its measure definition, population, method, denominator, uncertainty and revision lineage.", ["SRC-002", "SRC-004", "SRC-007", "SRC-009"], [
        ("indicator-definition", "Indicator definition", "Measure identity, semantics, computation and stratification.", ["SRC-002", "SRC-004", "SRC-007"], [
            ("indicator-identity-definition-and-unit", "Indicator identity, definition and unit", "Stable code, title, concept, value type, unit, direction and versioned semantic definition.", "identity", ["SRC-002", "SRC-007"], "object", True, True),
            ("numerator-denominator-method-and-stratifiers", "Numerator, denominator, method and stratifiers", "Computation criteria, source population, standardization, weighting, stratifier definitions and exclusions.", "measurement", ["SRC-002", "SRC-004", "SRC-007"], "object", True, True),
        ]),
        ("series-observation-and-quality", "Series observation and quality", "Observed or estimated values, uncertainty, timeliness and correction.", ["SRC-002", "SRC-004", "SRC-005", "SRC-007", "SRC-009"], [
            ("value-count-rate-estimate-and-uncertainty", "Value, count, rate, estimate and uncertainty", "Keeps counts, proportions, rates, ratios, risks, modelled estimates, intervals and suppression states distinct.", "measurement", ["SRC-002", "SRC-004", "SRC-007"], "object", True, True),
            ("data-quality-delay-revision-and-release", "Data quality, delay, revision and release", "Completeness, timeliness, coverage, bias, reporting delay, provisional or final status and correction lineage.", "quality", ["SRC-004", "SRC-005", "SRC-009"], "object", True, True),
        ]),
    ]),
    ("case-surveillance-and-signals", "Case surveillance and signals", "Transforms governed notifications and other sources into aggregate surveillance signals.", "A person-level report can contribute to an aggregate, but its identity and clinical record must not cross into the population model.", ["SRC-003", "SRC-005", "SRC-006", "SRC-009"], [
        ("case-definition-and-aggregate", "Case definition and aggregate", "Surveillance classification and cohort-grain case summaries.", ["SRC-005", "SRC-006", "SRC-007"], [
            ("surveillance-case-definition-and-classification", "Surveillance case definition and classification", "Pinned criteria and classification such as suspected, probable or confirmed, separate from clinical diagnosis.", "classification", ["SRC-005", "SRC-006"], "object", True, True),
            ("aggregate-case-count-and-deduplication", "Aggregate case count and deduplication", "Count by cohort, area and period with deduplication rule, late-report handling and no person identifier.", "validation", ["SRC-005", "SRC-006", "SRC-007"], "object", True, True),
        ]),
        ("reporting-and-notification", "Reporting and notification", "Source systems, reporting routes, timing and conformance.", ["SRC-001", "SRC-005", "SRC-006", "SRC-010"], [
            ("reporter-source-and-notification-route", "Reporter source and notification route", "Reporting institution class, source system, jurisdictional route and aggregation or transformation steps.", "provenance", ["SRC-001", "SRC-005", "SRC-009"], "collection", True, False),
            ("event-specimen-report-receipt-and-publication-times", "Event, specimen, report, receipt and publication times", "Distinct epidemiologic and data-pipeline times with uncertainty and RFC 3339 representation.", "temporal", ["SRC-005", "SRC-010"], "object", True, True),
        ]),
        ("signal-detection-and-verification", "Signal detection and verification", "Thresholds, anomalies, alerts and verification decisions.", ["SRC-003", "SRC-005"], [
            ("signal-rule-baseline-threshold-and-anomaly", "Signal rule, baseline, threshold and anomaly", "Versioned detection method, expected baseline, threshold, observed deviation and sensitivity limitations.", "process", ["SRC-003", "SRC-005"], "object", False, True),
            ("signal-verification-assessment-and-disposition", "Signal verification, assessment and disposition", "Evidence-backed decision to monitor, dismiss, escalate or associate a signal with an event or outbreak.", "decision", ["SRC-001", "SRC-003", "SRC-005"], "object", False, True),
        ]),
    ]),
    ("outbreak-and-transmission", "Outbreak and transmission", "Represents a declared population-health episode and evolving assessments of its extent and effects.", "Outbreak identity and assessments must preserve declaration authority, competing evidence, uncertainty and versioned thresholds.", ["SRC-001", "SRC-003", "SRC-005", "SRC-006", "SRC-009"], [
        ("outbreak-identity-and-declaration", "Outbreak identity and declaration", "Identity continuity and authorized declaration or revocation.", ["SRC-001", "SRC-003", "SRC-005"], [
            ("outbreak-identity-aliases-and-condition", "Outbreak identity, aliases and condition", "Master identifier, external aliases, condition or syndrome binding and event grouping rationale.", "identity", ["SRC-001", "SRC-003", "SRC-006"], "object", True, True),
            ("declaration-definition-threshold-and-authority", "Declaration definition, threshold and authority", "Pinned outbreak definition, evidence, threshold, declaring authority, effective time and revocation history.", "authority", ["SRC-001", "SRC-003", "SRC-006"], "object", True, True),
        ]),
        ("extent-transmission-and-severity", "Extent, transmission and severity", "Affected scope, spread characteristics and health burden.", ["SRC-001", "SRC-003", "SRC-005"], [
            ("affected-populations-areas-and-settings", "Affected populations, areas and settings", "Confirmed, suspected or excluded scope assertions across cohorts, locations and settings with confidence.", "relationship", ["SRC-001", "SRC-003", "SRC-005"], "collection", True, True),
            ("transmission-route-dynamics-and-severity", "Transmission route, dynamics and severity", "Evidence-backed route, generation or reproduction estimates, attack rate, hospitalization, mortality and severity profile.", "evidence", ["SRC-001", "SRC-003", "SRC-005"], "object", False, True),
        ]),
        ("course-forecast-and-closure", "Course, forecast and closure", "Observed epidemic curve, forecasts and episode disposition.", ["SRC-001", "SRC-003", "SRC-009"], [
            ("course-trend-forecast-and-scenario", "Course, trend, forecast and scenario", "Separates observed trajectory, statistical nowcast, forecast and policy scenario with method and uncertainty.", "state", ["SRC-003", "SRC-009"], "collection", False, True),
            ("closure-endemic-transition-and-residual-risk", "Closure, endemic transition and residual risk", "Authorized closure or reclassification with evidence, unresolved uncertainty and recurrence monitoring plan.", "lifecycle", ["SRC-001", "SRC-003"], "object", False, True),
        ]),
    ]),
    ("immunization-programme-and-coverage", "Immunization programme and coverage", "Describes aggregate programme intent, delivery reach and equity without storing personal vaccination records.", "Coverage requires target-population accuracy, product and schedule semantics, numerator provenance and explicit uncertainty.", ["SRC-004", "SRC-007", "SRC-008"], [
        ("programme-campaign-and-product", "Programme, campaign and product", "Programme identity, target, schedule and aggregate product bindings.", ["SRC-004", "SRC-008"], [
            ("programme-campaign-target-and-period", "Programme, campaign, target and period", "Programme or campaign identity, objective, target cohort, area, responsible authority and active period.", "composition", ["SRC-004"], "object", True, True),
            ("vaccine-antigen-dose-and-schedule-binding", "Vaccine, antigen, dose and schedule binding", "Pinned product, antigen, dose number, schedule and eligibility references used to interpret aggregates.", "interoperability", ["SRC-004", "SRC-008"], "collection", True, False),
        ]),
        ("coverage-performance-and-equity", "Coverage, performance and equity", "Vaccinated counts, denominators, timeliness, dropout and disparities.", ["SRC-004", "SRC-007", "SRC-008"], [
            ("coverage-numerator-denominator-and-estimate", "Coverage numerator, denominator and estimate", "Dose or completion count, target-population estimate, coverage result, data source and uncertainty.", "measurement", ["SRC-004", "SRC-007"], "object", True, True),
            ("timeliness-dropout-access-and-equity", "Timeliness, dropout, access and equity", "Schedule timeliness, series dropout, zero-dose or under-served cohorts and stratified access differences.", "quality", ["SRC-004"], "collection", False, True),
        ]),
    ]),
    ("measures-and-evaluation", "Measures and evaluation", "Binds public-health interventions to their authority, target and observed population effects.", "Intervention decisions, implementation facts and causal effectiveness claims are different objects and must not be inferred from temporal association alone.", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-009"], [
        ("measure-definition-and-operation", "Measure definition and operation", "Measure type, authority, scope and actual implementation.", ["SRC-001", "SRC-003"], [
            ("measure-identity-purpose-authority-and-target", "Measure identity, purpose, authority and target", "Versioned intervention definition, legal or policy basis, target population, area and intended mechanism.", "authority", ["SRC-001", "SRC-003"], "object", True, True),
            ("introduction-change-lifting-and-compliance-observation", "Introduction, change, lifting and compliance observation", "Actual effective intervals, amendments, implementation variation and aggregate adherence observations.", "event", ["SRC-001", "SRC-003", "SRC-010"], "collection", False, True),
        ]),
        ("evaluation-and-learning", "Evaluation and learning", "Effectiveness, harms, equity and decision feedback.", ["SRC-002", "SRC-004", "SRC-009"], [
            ("evaluation-design-comparator-and-effect-estimate", "Evaluation design, comparator and effect estimate", "Study or analytic design, comparator or counterfactual, endpoints, effect estimate, uncertainty and limitations.", "validation", ["SRC-002", "SRC-004", "SRC-009"], "object", False, True),
            ("benefit-harm-equity-and-decision-feedback", "Benefit, harm, equity and decision feedback", "Observed benefits, adverse or displaced effects, distributional impact and the decision that used the evaluation.", "decision", ["SRC-001", "SRC-004", "SRC-009"], "collection", False, True),
        ]),
    ]),
    ("governance-provenance-and-federation", "Governance, provenance and federation", "Controls disclosure, revision, access and exchange of sensitive population-health knowledge.", "Aggregate health data can still reveal people or communities, and changing evidence must remain traceable across releases and jurisdictions.", ["SRC-001", "SRC-004", "SRC-005", "SRC-007", "SRC-009", "SRC-010"], [
        ("privacy-access-and-retention", "Privacy, access and retention", "Disclosure-risk controls and governed disposition.", ["SRC-001", "SRC-004", "SRC-005"], [
            ("small-cell-linkage-and-reidentification-risk", "Small-cell, linkage and re-identification risk", "Risk assessment for rare combinations, fine geography or time, repeated releases and cross-dataset linkage.", "privacy", ["SRC-004", "SRC-005"], "object", True, True),
            ("projection-suppression-access-retention-and-hold", "Projection, suppression, access, retention and hold", "Minimum release, suppression or perturbation rule, recipient purpose, access decision and retention or legal-hold binding.", "access", ["SRC-001", "SRC-004", "SRC-005"], "object", True, True),
        ]),
        ("provenance-versioning-and-exchange", "Provenance, versioning and exchange", "Lineage, correction, mappings and international notifications.", ["SRC-001", "SRC-005", "SRC-007", "SRC-009", "SRC-010"], [
            ("source-transformation-derivation-and-revision", "Source, transformation, derivation and revision", "Source dataset, collection activity, transformation code or method, responsible agent, predecessor and correction reason.", "provenance", ["SRC-005", "SRC-007", "SRC-009"], "collection", True, True),
            ("schema-mapping-release-and-international-report", "Schema mapping, release and international report", "Pinned target schema, jurisdiction, projection digest, loss declaration, release status and IHR notification binding.", "interoperability", ["SRC-001", "SRC-005", "SRC-007", "SRC-009"], "collection", False, False),
        ]),
    ]),
]


KIND_CYCLE = ["definition", "identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def build_finding(raw, ordinal):
    finding_id, name, description, primary_kind, refs, value_kind, required, owns_artifact = raw
    kinds = [primary_kind, KIND_CYCLE[(ordinal * 5 + 3) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal * 11 + 7) % len(KIND_CYCLE)]]
    for position in range(1, 3):
        while kinds[position] in kinds[:position]:
            kinds[position] = KIND_CYCLE[(KIND_CYCLE.index(kinds[position]) + 1) % len(KIND_CYCLE)]
    questions = [
        {"id": f"{finding_id}-q01", "text": f"What is currently asserted about {name.lower()} for this population-health context, at which cohort, place and time grain?", "kind": kinds[0], "answer_data": [name, "cohort, place and period", "assertion status or explicit unknown"]},
        {"id": f"{finding_id}-q02", "text": f"Which source, method and authority establish {name.lower()}, with what observation time, evidence and uncertainty?", "kind": kinds[1], "answer_data": ["source and authority", "method and observation time", "evidence, uncertainty and limitations"]},
        {"id": f"{finding_id}-q03", "text": f"Which validation, disclosure or revision rule may change {name.lower()} without losing prior releases and provenance?", "kind": kinds[2], "answer_data": ["validation and disclosure rule", "authorized revision event", "predecessor, correction or counterclaim reference"]},
    ]
    artifacts = []
    rationale = "This finding stores only aggregate values or typed references; person-grain source records and external master lifecycles remain outside this model."
    if owns_artifact:
        artifacts = [{"id": f"{finding_id}-artifact", "name": f"{name} record", "description": f"Versioned cohort-grain public-health record supporting {name.lower()} with provenance and disclosure marking.", "media_or_form": ["structured aggregate record", "signed or controlled release", "resolvable methodology and evidence index"], "serial": True, "identity_strategy": "Authoritative public-health master identifier first; otherwise a Dimension-governed UUID or ULID.", "source_refs": refs}]
        rationale = None
    return {"id": finding_id, "name": name, "description": description, "source_refs": refs, "questions": questions, "data_elements": [{"id": f"{finding_id}-data", "name": f"{name} assertion", "description": f"Structured cohort-grain answer data for {name.lower()}, including scope, status, time and provenance.", "value_kind": value_kind, "cardinality": "1" if required else "0..1", "required": required, "source_refs": refs}], "artifacts": artifacts, "inline_only_rationale": rationale}


def build_structure():
    bundles, ordinal = [], 0
    for bundle_id, name, description, rationale, refs, layer_rows in STRUCTURE:
        layers = []
        for layer_id, layer_name, layer_description, layer_refs, finding_rows in layer_rows:
            findings = []
            for raw in finding_rows:
                ordinal += 1
                findings.append(build_finding(raw, ordinal))
            layers.append({"id": layer_id, "name": layer_name, "description": layer_description, "source_refs": layer_refs, "findings": findings})
        bundles.append({"id": bundle_id, "name": name, "description": description, "rationale": rationale, "source_refs": refs, "layers": layers})
    return {"bundles": bundles}


FUNCTIONS = [
    ("define-surveillance-frame", "Define surveillance frame", "Pin population, cohort, place, period, purpose, authority and profiles before producing observations.", ["purpose", "population and area definitions", "profiles"], ["versioned surveillance frame"], ["record authority and disclosure profile resolve"], ["subsequent records share a reproducible interpretation frame"], ["SRC-001", "SRC-002", "SRC-005"]),
    ("register-indicator", "Register indicator", "Create a versioned population-health measure definition.", ["concept", "method", "numerator and denominator", "unit and stratifiers"], ["indicator specification"], ["measure owner and source definitions are known"], ["values can be calculated and compared under a pinned version"], ["SRC-002", "SRC-007"]),
    ("append-indicator-observation", "Append indicator observation", "Record an aggregate value or estimate with cohort, period, method, quality and uncertainty.", ["indicator", "aggregate inputs", "provenance"], ["series observation revision"], ["grain and disclosure controls permit storage"], ["provisional, corrected and final releases remain distinguishable"], ["SRC-002", "SRC-004", "SRC-007", "SRC-009"]),
    ("ingest-case-aggregate", "Ingest case aggregate", "Transform authorized source notifications into non-identifying counts under a pinned case definition.", ["source aggregate", "case definition", "deduplication and disclosure rules"], ["case-surveillance aggregate"], ["person identifiers are absent from the target record"], ["counts retain source, lag, definition and quality context"], ["SRC-005", "SRC-006"]),
    ("detect-and-assess-signal", "Detect and assess signal", "Apply a pinned method and record verification or disposition without promoting anomaly to outbreak.", ["series", "baseline and rule", "supporting evidence"], ["signal and assessment revisions"], ["method and authority resolve"], ["signal status and rationale are traceable"], ["SRC-003", "SRC-005"]),
    ("declare-or-revoke-outbreak", "Declare or revoke outbreak", "Record an authorized determination against a pinned definition and threshold.", ["signals and assessments", "definition", "authority"], ["outbreak identity and declaration revision"], ["minimum evidence and mandate are satisfied"], ["declaration, revocation and uncertainty remain historically visible"], ["SRC-001", "SRC-003", "SRC-006"]),
    ("revise-outbreak-assessment", "Revise outbreak assessment", "Update scope, transmission, severity, course or forecast with evidence and uncertainty.", ["outbreak", "new observations", "analytic method"], ["assessment revision"], ["claims are labelled observed, estimated, forecast or scenario"], ["competing assessments remain attributable"], ["SRC-001", "SRC-003", "SRC-009"]),
    ("register-immunization-programme", "Register immunization programme", "Define aggregate programme, target cohort, schedule and product bindings.", ["programme mandate", "target cohort", "product and schedule references"], ["programme revision"], ["authority and reference versions resolve"], ["coverage observations share consistent semantics"], ["SRC-004", "SRC-008"]),
    ("calculate-coverage-estimate", "Calculate coverage estimate", "Produce a coverage estimate with numerator, target denominator, stratifiers and uncertainty.", ["programme", "vaccinated aggregate", "target-population estimate"], ["coverage estimate revision"], ["grain and disclosure rules permit release"], ["performance and equity comparisons retain denominator provenance"], ["SRC-004", "SRC-007"]),
    ("bind-public-health-measure", "Bind public-health measure", "Record a measure definition, authority, target and actual effective interval.", ["measure specification", "authority", "scope and events"], ["measure revision"], ["jurisdictional profile applies"], ["intended and implemented intervention remain distinct"], ["SRC-001", "SRC-003"]),
    ("evaluate-measure-effect", "Evaluate measure effect", "Record a method-bounded effect estimate, benefits, harms and equity results.", ["measure", "outcomes", "design and comparator"], ["evaluation revision"], ["causal assumptions and uncertainty are explicit"], ["temporal association is not silently promoted to causation"], ["SRC-002", "SRC-004", "SRC-009"]),
    ("issue-governed-projection", "Issue governed projection", "Create a minimum authorized domestic, research, dashboard or international view.", ["record revisions", "recipient and purpose", "projection policy and schema"], ["digest-pinned release"], ["disclosure risk and authority permit release"], ["suppression, mapping loss and provenance are recorded"], ["SRC-001", "SRC-004", "SRC-005", "SRC-007", "SRC-009"]),
]


def build():
    return {
        "schema_version": "1.0.0",
        "model": {
            "registry_id": "vr.wm-act-023", "model_id": "WM-ACT-023", "name": "Public Health / Epidemiology", "entry_kind": "aggregate",
            "purpose": "Represent governed population and cohort-grain health surveillance, indicator series, signals, outbreaks, immunization coverage, public-health measures and epidemiologic assessments without importing person-grain health records.",
            "scope_statement": "Owns population-health frames, indicator definitions and observations, aggregate surveillance notifications, signals, outbreak determinations and assessments, immunization programme and coverage aggregates, measure bindings, evaluation results, disclosure controls and governed releases while referencing clinical, laboratory, identity, geography, policy and operational masters.",
            "in_scope": ["Cohort and population definitions, indicator series, aggregate case surveillance, signals and data-quality revisions", "Outbreak identity, declaration, extent, transmission, severity, course, forecast, closure and residual-risk assessments", "Aggregate immunization programmes and coverage, public-health measures, evaluation, disclosure, provenance and federation"],
            "out_of_scope": ["Identifiable person health, clinical-care, immunization event, identity and contact-tracing records", "Laboratory sample, pathogen genome, geography, facility, product, policy, legal-power and resource-deployment master lifecycles", "Universal case definitions, outbreak thresholds, severity scales, vaccination schedules, causal conclusions, public-health powers or reporting deadlines"],
            "boundary_notes": [
                {"neighbor": "Personal health and clinical record", "distinction": "Person-grain diagnosis, care and immunization events remain in their source models; this model receives only authorized aggregate facts and never uses a personal identifier as population-health identity.", "source_refs": ["SRC-005", "SRC-006", "SRC-008"]},
                {"neighbor": "Surveillance case and clinical diagnosis", "distinction": "A surveillance case definition exists for consistent classification and counting and is not a clinical diagnostic or treatment rule.", "source_refs": ["SRC-005", "SRC-006"]},
                {"neighbor": "Signal, public-health event and outbreak", "distinction": "A signal is an observation requiring assessment; a public-health event may trigger international assessment; an outbreak is a separately authorized determination under a pinned definition.", "source_refs": ["SRC-001", "SRC-003"]},
                {"neighbor": "Indicator and raw dataset", "distinction": "The model owns a governed measure definition and aggregate observation lineage while source systems retain person, encounter, laboratory and operational datasets.", "source_refs": ["SRC-002", "SRC-005", "SRC-007"]},
                {"neighbor": "Public-health measure and response operation", "distinction": "This model records intervention definition, authority, target, timing and effects; logistics, staffing, procurement and task execution remain in operational systems.", "source_refs": ["SRC-001", "SRC-003", "SRC-004"]},
            ],
        },
        "sources": SOURCES,
        "structure": build_structure(),
        "functions": [{"id": r[0], "name": r[1], "description": r[2], "inputs": r[3], "outputs": r[4], "preconditions": r[5], "effects": r[6], "source_refs": r[7]} for r in FUNCTIONS],
        "composition": [
            {"target": "Personal Health and Clinical Record models", "relation": "REFERENCE", "purpose": "Receives only authorized aggregate contributions and never imports person-grain identity or care lifecycle.", "required": False, "source_refs": ["SRC-005", "SRC-006", "SRC-008"]},
            {"target": "Population, Cohort, Geography and Time models", "relation": "REFERENCE", "purpose": "Pins denominators, cohort membership semantics, authoritative areas and periods.", "required": True, "source_refs": ["SRC-002", "SRC-004", "SRC-007"]},
            {"target": "Laboratory, Specimen, Pathogen and Genomic models", "relation": "REFERENCE", "purpose": "Uses aggregate or evidence references without owning sample, test, organism or sequence records.", "required": False, "source_refs": ["SRC-003", "SRC-005", "SRC-006"]},
            {"target": "Product, Vaccine, Facility and Organization models", "relation": "REFERENCE", "purpose": "Binds immunization products, sites and accountable institutions without copying master data.", "required": False, "source_refs": ["SRC-004", "SRC-008"]},
            {"target": "Policy, Legal Authority and Public Programme models", "relation": "REFERENCE", "purpose": "Pins mandates, reporting obligations and intervention authority while those systems own policy lifecycle.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-004"]},
            {"target": "Task, Supply, Workforce and Response Operations models", "relation": "REFERENCE", "purpose": "Links implementation and resource records without conflating them with epidemiologic observations or effect estimates.", "required": False, "source_refs": ["SRC-001", "SRC-003"]},
            {"target": "WHO IHR and indicator metadata", "relation": "ALIGN", "purpose": "Supports explicit jurisdictional event assessment, notification and indicator mappings with pinned versions.", "required": False, "source_refs": ["SRC-001", "SRC-002"]},
            {"target": "HL7 FHIR MeasureReport and Immunization", "relation": "ALIGN", "purpose": "Supports versioned exchange mappings while preserving the boundary between population aggregates and person compartments.", "required": False, "source_refs": ["SRC-007", "SRC-008"]},
            {"target": "W3C PROV-O", "relation": "ALIGN", "purpose": "Aligns source, activity, agent, derivation and revision semantics for releases.", "required": False, "source_refs": ["SRC-009"]},
        ],
        "service_layers": service_layers(),
        "coverage": coverage(),
    }


def service_layers():
    return {
        "dimension": {"owner_package_requirements": ["Declare the Dimension owner, public-health authority, constituencies, stewards, namespaces and delegated decision powers.", "Declare aggregate record masters, source systems, cohort and geography registries, clock policy and permitted linkage boundaries.", "Publish model, object, event, relation, indicator, case-definition, disclosure, access, retention and federation registries.", "Pin jurisdiction, condition, outbreak, immunization, intervention, statistical and international-reporting profiles."], "namespace_guidance": "Mint aggregate, series, signal, outbreak, programme and release identifiers only in the adopting Dimension's governed namespace; preserve external IDs as typed aliases with authority and version.", "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local public-health, indicator, event, policy and disclosure registries"]},
        "canon_and_patch": {"canonicalization_rules": ["Canonicalize by registry ID, model version, authoritative object ID, immutable revision, population frame and effective profile; never use disease name, place label or publication date alone as identity.", "Keep person records, source reports, aggregate observations, signals, outbreak decisions, forecasts, scenarios and interventions as distinct objects."], "patch_rules": ["Additive extensions use a Dimension-owned namespace and declare target node, population grain, source, rationale, privacy impact and migration behavior.", "Breaking changes require a new version, migration map, compatibility declaration and continued resolution of prior releases."], "compatibility_rules": ["Consumers may ignore unknown additive fields only when population scope, units, methods, provenance, privacy, authority and time meaning remain intact.", "External mappings pin source and target versions and declare suppression, transformation, aggregation, redaction and non-round-trippable information."]},
        "artifact_rules": {"identity_priority": ["Authoritative public-health master identifier and immutable revision identifier.", "Governed globally resolvable IRI or federation identifier.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."], "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep occurrence, specimen, report, receipt, detection, effective, publication and knowledge times distinct.", "serial_naming_rule": "Name serial artifacts as {aggregate-or-outbreak-id}--{artifact-kind}--{revision-or-event-id}; never use a date, place label, condition code or hash alone as identity.", "integrity_rule": "Store digest, media type, byte length, issuer, method or code version, provenance, disclosure marking and immutable version reference for each retained serial artifact."},
        "policies": ["Never store person-grain health or identity records in this model; source systems contribute only the minimum authorized aggregate or evidence reference.", "Assess small-cell, rare-combination, fine geography-time, repeated-release and cross-dataset linkage risk before every release.", "Every value identifies population, place, period, unit, method, numerator or denominator where applicable, provisional status, uncertainty and provenance.", "Automated agents may append delegated aggregate observations and run reproducible calculations, but consequential declaration, disclosure, closure and policy decisions require declared authority.", "Do not infer causality from temporal association, clinical diagnosis from surveillance classification, anonymity from removed names or legal power from a public-health recommendation."],
        "crud": {"read": ["Resolve active Dimension, purpose, role, profiles and disclosure rules; return only the minimum permitted cohort-grain projection with suppression and uncertainty intact."], "create": ["Create authoritative identity, population frame, purpose, source, method, observation and knowledge times and explicit unknowns; validate that person identifiers are absent."], "update": ["Append an immutable revision with actor, authority, reason, RFC 3339 effective time, predecessor and calculation lineage; never overwrite prior public releases."], "delete": ["Apply retention, legal hold, correction and withdrawal policy; tombstone or withdraw case-owned releases while source systems retain their governed data and references do not cascade."]},
        "roles": [{"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, interoperability, access and retention rules."]}, {"name": "Public-health authority", "responsibilities": ["Authorize surveillance frames, outbreak declarations, interventions, closure and governed releases within mandate."]}, {"name": "Epidemiologist or statistician", "responsibilities": ["Define measures, evaluate data quality, analyze trends and preserve methods, uncertainty and competing explanations."]}, {"name": "Surveillance data steward", "responsibilities": ["Maintain sources, case definitions, mappings, revisions, lineage and quality metadata."]}, {"name": "Privacy and disclosure reviewer", "responsibilities": ["Assess re-identification and community harms and approve suppression, perturbation and access projections."]}, {"name": "Immunization programme owner", "responsibilities": ["Maintain programme, product, schedule, target-population and coverage semantics."]}, {"name": "Auditor", "responsibilities": ["Review authority, calculations, provenance, access, releases and corrections without rewriting scientific truth."]}],
        "access": {"default_rule": "Deny person-grain storage and sensitive aggregate disclosure unless the active Dimension, role, purpose, population grain and disclosure-risk policy grant the action; expose the minimum necessary projection.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Emergency access remains time-limited, purpose-bound, attributable and independently reviewed and cannot bypass person-grain exclusion, immutable release history or legal hold."], "audit_requirements": ["Log actor, role, purpose, record and revision identity, action, authority, policy and method versions, RFC 3339 timestamp with offset, affected population scope and outcome for privileged mutation or disclosure."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"], "read_order": ["Read the nearest Dimension-owner AGENTS.md, public-health mandate, active profiles and disclosure policies.", "Read this model AGENTS.md, pinned spec.yaml and required population, clinical-source, geography, policy and provenance model instructions before mutation."]},
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering cohort-grain public-health frames, indicators, case surveillance, signals, outbreaks, immunization coverage, interventions, evaluation, governance and federation across WHO, CDC, HL7, W3C and IETF materials.", "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Stable aggregate, series, signal, outbreak, programme and release identity plus aliases and immutable revisions are explicit."},
            {"dimension": "classification and recognition", "status": "covered", "notes": "Conditions, case definitions, signals, outbreak thresholds and observation versus estimate status bind to versioned profiles."},
            {"dimension": "direct properties", "status": "not-applicable", "notes": "Population-health constructs are abstract aggregates; physical properties belong to referenced people, organisms, products, samples, facilities and places."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Series revisions, signal assessment, outbreak declaration and closure, programme periods, intervention changes and release correction preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Populations, places, conditions, sources, outbreaks, programmes, products, measures, evidence, policies and releases use typed bindings."},
            {"dimension": "temporal", "status": "covered", "notes": "Occurrence, specimen, report, receipt, detection, effective, publication and knowledge times remain distinct."},
            {"dimension": "spatial and population grain", "status": "covered", "notes": "Authoritative geography, cohort membership, denominator and minimum disclosure grain are explicit."},
            {"dimension": "provenance", "status": "covered", "notes": "Source datasets, collection activities, transformations, methods, responsible agents, derivations and corrections are represented."},
            {"dimension": "ownership", "status": "covered", "notes": "Dimension owner, public-health authority, data stewards, programme owners and external master systems have distinct responsibilities."},
            {"dimension": "validation and uncertainty", "status": "covered", "notes": "Definition, denominator, deduplication, quality, lag, bias, suppression, confidence and revision checks are explicit."},
            {"dimension": "access and privacy", "status": "covered", "notes": "Person-grain exclusion, linkage risk, small-cell controls, minimum projections, exceptions and audit are explicit."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Retention, legal hold, withdrawal, tombstone and non-cascading source references are defined."},
            {"dimension": "interoperability", "status": "covered", "notes": "WHO, CDC and FHIR bindings require pinned versions, aggregation and loss declarations."},
            {"dimension": "behavior and possible actions", "status": "covered", "notes": "Agent functions define surveillance and analytic operations while intervention execution remains external."},
            {"dimension": "causal and policy reasoning", "status": "covered", "notes": "Observed association, causal estimate, forecast, scenario, intervention authority and decision feedback remain distinct."},
        ],
        "known_omissions": ["Disease, jurisdiction and programme profiles must supply exact case definitions, outbreak thresholds, schedules, powers, notification content and deadlines.", "Formal statistical-disclosure algorithms, differential-privacy budgets and accepted risk thresholds remain Dimension profile work.", "Sibling model IDs and relation cardinalities for populations, places, laboratories, pathogens, products, policies and response operations remain to be pinned."],
        "conflicts": ["The previous B14 card described simple de-identification and a COMPOSE relation from personal health; this draft uses minimum aggregate REFERENCE semantics because removing identifiers alone does not eliminate linkage risk.", "Public-health and vendor vocabularies vary for cases, events, signals, outbreaks and emergency states, so every determination pins its governing definition.", "FHIR resources can contain person compartments; alignment does not authorize person-grain ingestion into this population model."],
        "regional_assumptions": ["WHO IHR bindings apply only to the effective text and reservations governing the relevant State Party; no universal legal conclusion or deadline is assumed.", "CDC case-surveillance semantics are an authoritative national profile, not a claim that United States reporting law applies globally."],
        "adversarial_checks": ["Reject any object containing a direct personal identifier, clinical narrative or linkable rare combination without an explicitly authorized source-system reference and disclosure decision.", "Reject counts, rates or coverage values lacking population, period, numerator or denominator where applicable, method, unit, revision status and uncertainty.", "Reject a signal represented as a declared outbreak, surveillance classification presented as clinical diagnosis, forecast presented as observation or correlation presented as causation.", "Reject overwritten releases, timestamps without seconds and offset, unversioned case definitions, hidden suppression and external mappings without loss declarations.", "Reject international notification, intervention, closure, disclosure or deletion without jurisdictional authority, purpose, provenance and audit."],
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
