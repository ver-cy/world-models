#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-ACT-036."""

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ACCESSED = "2026-09-06T06:42:33Z"


def source(source_id, title, organization, url, version, source_type, relevance):
    return {
        "id": source_id,
        "title": title,
        "organization": organization,
        "url": url,
        "version_or_date": version,
        "source_type": source_type,
        "primary_source": True,
        "authority_tier": 1,
        "accessed_at": ACCESSED,
        "relevance": relevance,
    }


SOURCES = [
    source("SRC-001", "Frascati Manual 2015", "Organisation for Economic Co-operation and Development", "https://www.oecd.org/en/publications/frascati-manual-2015_9789264239012-en.html", "OECD Guidelines for Collecting and Reporting Data on Research and Experimental Development, 2015", "standard", "Defines research and experimental development as creative and systematic work undertaken to increase knowledge and devise new applications across scientific and scholarly fields."),
    source("SRC-002", "DDI Lifecycle 3.3 DataCollection", "DDI Alliance", "https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/DataCollection/", "DDI Lifecycle 3.3 official model documentation", "schema", "Structures methodology, capture, collection events, instruments, questions, processing, sampling, development activities and coverage for study data collection."),
    source("SRC-003", "DDI Lifecycle maintainable structures", "DDI Alliance", "https://docs.ddialliance.org/DDI-Lifecycle/guide/Structural%20Features/Maintainable%20structures/", "DDI Lifecycle 3.3 official guide", "standard", "Defines StudyUnit as a publication structure that can combine identification, administrative and bibliographic material with collection, logical product, physical product, archive and profile modules."),
    source("SRC-004", "WHO Trial Registration Data Set", "World Health Organization", "https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set", "WHO TRDS version 1.3.1", "standard", "Defines the minimum registration items used to identify and describe a clinical trial, its sponsor, design, outcomes, recruitment and individual participant data sharing."),
    source("SRC-005", "ClinicalTrials.gov Protocol Registration Data Element Definitions", "United States National Library of Medicine", "https://clinicaltrials.gov/policy/protocol-definitions", "Official definitions, last updated 24 April 2025", "registry", "Defines study identification, status, sponsors, oversight, description, design, arms, interventions, outcomes, eligibility, contacts, locations and participant-data-sharing elements for registered studies."),
    source("SRC-006", "Observations, Measurements, and Samples", "Open Geospatial Consortium", "https://www.ogc.org/standards/om/", "OGC 20-082r4 and ISO 19156:2023", "standard", "Provides conceptual semantics for observations, observed features, procedures, results and sampling across scientific and technical domains."),
    source("SRC-007", "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entities, activities, agents, plans, usage, generation, derivation, association, attribution, revision and invalidation for attributable research records."),
    source("SRC-008", "Data Catalog Vocabulary, Version 3", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dcat-3/", "W3C Recommendation, 22 August 2024", "ontology", "Defines datasets, distributions, data services, series, catalog records, versions and provenance while keeping a conceptual dataset separate from its representations."),
    source("SRC-009", "DataCite Metadata Schema 4.6 properties", "DataCite", "https://datacite-metadata-schema.readthedocs.io/en/4.6/properties/", "DataCite Metadata Schema 4.6", "schema", "Defines identifiers, creators, titles, publisher, dates, subjects, contributors, related identifiers, resource type, version, rights, descriptions, geolocation and funding metadata."),
    source("SRC-010", "DataCite Metadata Schema release history", "DataCite", "https://schema.datacite.org/versions.html", "Release history through Metadata Schema 4.7, released 3 March 2026", "registry", "Provides authoritative schema-version history needed to pin mappings and flag a 4.6 property crosswalk for review against the current 4.7 release."),
    source("SRC-011", "NIH Policy for Data Management and Sharing", "United States National Institutes of Health", "https://grants.nih.gov/grants/guide/notice-files/not-od-21-013.html", "Policy effective 25 January 2023", "public-authority", "Requires prospective planning for management and sharing of scientific data, with justified limitations and attention to validation and replication."),
    source("SRC-012", "Best Practices for Protecting Participant Privacy", "United States National Institutes of Health", "https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/privacy/best-practices", "Official best-practices guidance accessed 6 September 2026", "public-authority", "Grounds privacy planning, de-identification and controls for sharing research data involving participants."),
    source("SRC-013", "45 CFR Part 46: Protection of Human Subjects", "United States Electronic Code of Federal Regulations", "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46", "Current electronic regulation, accessed 6 September 2026", "legislation", "Defines regulated human-subject research, institutional review, approval, consent and additional safeguards within its United States jurisdictional scope."),
    source("SRC-014", "NIST Privacy Framework", "National Institute of Standards and Technology", "https://www.nist.gov/privacy-framework", "Privacy Framework 1.0 with later evolution materials", "public-authority", "Provides a voluntary, risk-based structure for identifying and managing privacy risk across a data-processing ecosystem."),
    source("SRC-015", "Disposing of records", "The National Archives, United Kingdom", "https://www.nationalarchives.gov.uk/information-management/manage-information/policy-process/disposal/", "Official records-management guidance accessed 6 September 2026", "public-authority", "Grounds retention and responsible disposition decisions in business, legal, accountability and historical requirements."),
    source("SRC-016", "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339", "RFC 3339, July 2002", "standard", "Defines an unambiguous Internet timestamp profile with seconds and explicit UTC offset."),
]


# Bundle: id, name, description, rationale, refs, layers.
# Layer: id, name, description, refs, findings.
# Finding: id, name, description, primary question kind, refs, value kind, required.
STRUCTURE = [
    ("identity-purpose-and-protocol", "Identity, purpose and protocol", "Defines the inquiry as a stable, versioned aggregate and binds its scientific intent to released protocol content.", "A study can be understood only when its identity, disciplinary profile, questions, design and protocol lineage remain distinguishable from the project that supports it and the activities it contains.", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-007"], [
        ("study-identity-classification-and-lineage", "Study identity, classification and lineage", "Establishes the root identity, profile, registration references and revision family.", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-009"], [
            ("research-study-definition-profile-and-neighbor-boundary", "Research study definition, profile and neighbor boundary", "Source-qualified definition, discipline, research type, method family, inclusion and exclusion rules, and distinctions from project, experiment, trial, assessment, dataset and publication.", "classification", ["SRC-001", "SRC-003", "SRC-004", "SRC-005"], "object", True),
            ("study-identifier-title-acronym-registration-version-and-lineage", "Study identifier, title, acronym, registration, version and lineage", "Authoritative and alternate identifiers, public and scientific titles, acronym, registry records, sponsor protocol number, semantic version, predecessor, correction and supersession lineage.", "identity", ["SRC-004", "SRC-005", "SRC-007", "SRC-009", "SRC-010"], "object", True),
        ]),
        ("questions-hypotheses-design-and-protocol", "Questions, hypotheses, design and protocol", "Keeps research intent, prospective design and actual changes versioned and attributable.", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-007"], [
            ("research-question-objective-hypothesis-theory-and-priority", "Research question, objective, hypothesis, theory and priority", "Primary and secondary questions, objectives, hypotheses, theoretical or conceptual basis, directional status, outcome linkage and priority.", "requirement", ["SRC-001", "SRC-002", "SRC-004", "SRC-005"], "collection", True),
            ("protocol-design-method-revision-preregistration-amendment-and-deviation", "Protocol, design, method, revision, preregistration, amendment and deviation", "Released protocol and method, design classification, preregistration, effective revision, amendment rationale, actual deviation and impact assessment.", "process", ["SRC-002", "SRC-004", "SRC-005", "SRC-007"], "collection", True),
        ]),
    ]),
    ("governance-ethics-and-roles", "Governance, ethics and roles", "Records who sponsors, conducts, oversees and may change the study, with ethics and privacy controls where applicable.", "Study ownership, institutional responsibility, scientific authorship, ethics review, participant rights and data stewardship are separate authorities and must not be collapsed into a single owner field.", ["SRC-004", "SRC-005", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-014"], [
        ("sponsorship-funding-institutions-and-roles", "Sponsorship, funding, institutions and roles", "Binds accountable parties and resources while preserving external organization, project, grant and person masters.", ["SRC-004", "SRC-005", "SRC-007", "SRC-009"], [
            ("sponsor-investigator-institution-collaborator-role-authority-and-accountability", "Sponsor, investigator, institution, collaborator, role, authority and accountability", "External actor identities, study-scoped roles, principal investigator, responsible party, delegation, contribution, independence, conflicts and accountable decisions.", "authority", ["SRC-004", "SRC-005", "SRC-007", "SRC-009"], "collection", True),
            ("project-award-funding-budget-resource-site-and-facility-binding", "Project, award, funding, budget, resource, site and facility binding", "Typed references to supporting project, award, funder, resource envelope, research sites and facilities, with effective periods and restrictions.", "relationship", ["SRC-005", "SRC-007", "SRC-009", "SRC-010"], "collection", False),
        ]),
        ("ethics-oversight-participant-rights-and-privacy", "Ethics, oversight, participant rights and privacy", "Represents study-scoped approvals, obligations and safeguards without copying person-level masters.", ["SRC-005", "SRC-011", "SRC-012", "SRC-013", "SRC-014"], [
            ("ethics-review-approval-exemption-condition-safety-conflict-and-oversight", "Ethics review, approval, exemption, condition, safety, conflict and oversight", "Review body reference, decision, jurisdiction, conditions, expiry, continuing review, safety monitoring, conflicts, noncompliance and corrective actions.", "authority", ["SRC-005", "SRC-013", "SRC-014"], "collection", False),
            ("participant-category-consent-assent-withdrawal-privacy-and-deidentification", "Participant category, consent, assent, withdrawal, privacy and de-identification", "Study-scoped participant categories, consent or waiver requirements, assent and representative rules, withdrawal effects, privacy plan, identifiers, de-identification and re-identification risk.", "privacy", ["SRC-005", "SRC-011", "SRC-012", "SRC-013", "SRC-014"], "collection", False),
        ]),
    ]),
    ("design-population-and-conduct", "Design, population and conduct", "Defines who or what is studied, how units are selected or assigned, and what was actually done.", "Population, sample, participant, specimen, intervention, instrument and site masters remain external; the study owns scoped inclusion, assignment, usage and conduct assertions.", ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-013"], [
        ("study-design-population-sampling-and-power", "Study design, population, sampling and power", "Pins study design and the basis for inclusion, allocation and inferential scope.", ["SRC-002", "SRC-004", "SRC-005", "SRC-006"], [
            ("study-type-design-comparator-randomization-masking-and-control", "Study type, design, comparator, randomization, masking and control", "Observational, experimental or other design; prospective or retrospective timing; comparator; allocation; randomization; masking; crossover; unit and control strategy.", "classification", ["SRC-002", "SRC-004", "SRC-005"], "object", True),
            ("population-cohort-eligibility-sampling-sample-size-power-and-representativeness", "Population, cohort, eligibility, sampling, sample size, power and representativeness", "Target and accessible populations, inclusion and exclusion criteria, sampling frame and method, planned and actual size, power or precision rationale, attrition and representativeness limits.", "measurement", ["SRC-002", "SRC-004", "SRC-005", "SRC-006"], "collection", True),
        ]),
        ("sites-materials-interventions-exposures-and-conduct", "Sites, materials, interventions, exposures and conduct", "Records the conditions, resources and study activities that can influence observations.", ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-016"], [
            ("site-environment-instrument-material-specimen-and-resource-use", "Site, environment, instrument, material, specimen and resource use", "External site and resource identities, environment conditions, instruments and versions, material or specimen selection and preparation, custody, calibration and suitability.", "composition", ["SRC-002", "SRC-005", "SRC-006", "SRC-007"], "collection", False),
            ("intervention-exposure-arm-group-experiment-link-conduct-and-timeline", "Intervention, exposure, arm, group, experiment link, conduct and timeline", "Interventions or exposures, arms and groups, contained experiments or trials, assignment, dose or intensity, schedule, actual conduct, deviations and event times.", "event", ["SRC-002", "SRC-004", "SRC-005", "SRC-007", "SRC-016"], "collection", False),
        ]),
    ]),
    ("data-collection-observations-and-quality", "Data collection, observations and quality", "Separates collection intent, source observations, managed data products and quality assertions.", "A dataset is not the study, an observation is not a finding, and completeness alone does not establish validity or fitness for an analysis.", ["SRC-002", "SRC-006", "SRC-007", "SRC-008", "SRC-011", "SRC-012", "SRC-016"], [
        ("collection-instruments-variables-observations-and-measurements", "Collection, instruments, variables, observations and measurements", "Describes what was collected, how, from what feature and at which times.", ["SRC-002", "SRC-006", "SRC-007", "SRC-016"], [
            ("collection-event-mode-instrument-question-variable-outcome-and-schedule", "Collection event, mode, instrument, question, variable, outcome and schedule", "Collection event plan and occurrence, mode, instrument or questionnaire revision, question and variable definitions, primary and secondary outcomes, schedule and permitted windows.", "measurement", ["SRC-002", "SRC-004", "SRC-005", "SRC-006"], "collection", True),
            ("observation-measurement-property-value-unit-time-location-procedure-and-uncertainty", "Observation, measurement, property, value, unit, time, location, procedure and uncertainty", "External observation references with observed feature, property, value, unit or scale, result and phenomenon time, location, procedure, observer or sensor, quality and uncertainty.", "measurement", ["SRC-002", "SRC-006", "SRC-007", "SRC-016"], "collection", True),
        ]),
        ("data-management-provenance-integrity-and-quality", "Data management, provenance, integrity and quality", "Binds data plans and products to transformations, controls and fitness assessments.", ["SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-014"], [
            ("data-management-sharing-plan-dataset-schema-codebook-lineage-and-access", "Data management and sharing plan, dataset, schema, codebook, lineage and access", "Prospective plan, external dataset and distribution references, schema and codebook versions, transformations, responsible agents, storage, sharing, restrictions and participant-data commitments.", "provenance", ["SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012"], "collection", True),
            ("quality-missingness-bias-protocol-deviation-monitoring-audit-and-remediation", "Quality, missingness, bias, protocol deviation, monitoring, audit and remediation", "Completeness and missing-data patterns, measurement quality, bias risks, deviations, monitoring findings, audit references, queries, remediation and residual limitations.", "quality", ["SRC-002", "SRC-005", "SRC-007", "SRC-011", "SRC-014"], "collection", True),
        ]),
    ]),
    ("analysis-findings-and-outputs", "Analysis, findings and outputs", "Preserves the path from a versioned analysis plan through executions and estimates to bounded interpretations and public or controlled outputs.", "Methods, code, datasets, estimates, uncertainty, hypothesis relations, interpretation and publication are distinct objects with separate revisions and provenance.", ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011"], [
        ("analysis-plan-execution-results-and-inference", "Analysis plan, execution, results and inference", "Makes analytic choices and result assertions inspectable without presenting statistical evidence as self-proving truth.", ["SRC-007", "SRC-008", "SRC-009", "SRC-011"], [
            ("analysis-plan-method-population-estimand-software-code-and-execution", "Analysis plan, method, population, estimand, software, code and execution", "Prospective and amended plans, analysis populations, estimands or target quantities, method assumptions, preprocessing, software and code versions, parameters, environment and execution provenance.", "process", ["SRC-007", "SRC-008", "SRC-009", "SRC-011"], "collection", True),
            ("estimate-effect-uncertainty-test-multiplicity-sensitivity-and-result-assertion", "Estimate, effect, uncertainty, test, multiplicity, sensitivity and result assertion", "Descriptive or inferential estimates, effect measures, intervals, tests, multiplicity control, sensitivity analyses, model diagnostics and source-qualified result assertions.", "evidence", ["SRC-001", "SRC-007", "SRC-009", "SRC-011"], "collection", True),
        ]),
        ("findings-interpretation-limitations-and-knowledge-outputs", "Findings, interpretation, limitations and knowledge outputs", "Relates results to questions while bounding causal, generalization and reproducibility claims.", ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011"], [
            ("finding-question-hypothesis-relation-interpretation-causal-limit-and-generalizability", "Finding, question and hypothesis relation, interpretation, causal limit and generalizability", "Finding identity and status, result references, relation to questions and hypotheses, interpretation, alternatives, causal qualification, generalizability, limitations, confidence, contradiction and review.", "validation", ["SRC-001", "SRC-007", "SRC-011"], "collection", True),
            ("dataset-software-material-publication-output-reproducibility-correction-and-retraction", "Dataset, software, material and publication output, reproducibility, correction and retraction", "External output identifiers, versions and availability, release relationships, reproducibility or replication evidence, post-publication correction, withdrawal or retraction and residual validity.", "lifecycle", ["SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011"], "collection", False),
        ]),
    ]),
    ("lifecycle-interoperability-access-and-agents", "Lifecycle, interoperability, access and agents", "Controls state transitions, mappings, disclosure, retention and safe machine operations.", "A study must be discoverable and exchangeable without erasing profile differences, privacy obligations, released history or the authority boundaries of linked systems.", ["SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"], [
        ("lifecycle-registration-provenance-and-interoperability", "Lifecycle, registration, provenance and interoperability", "Keeps state, registry history and version-pinned crosswalks attributable.", ["SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-016"], [
            ("proposal-design-registration-approval-recruitment-collection-analysis-completion-and-archive", "Proposal, design, registration, approval, recruitment, collection, analysis, completion and archive", "Profile-specific lifecycle event, prior and next state, actor, authority, rationale, effective and recorded times, evidence, amendment, termination, withdrawal, publication and archive status.", "lifecycle", ["SRC-004", "SRC-005", "SRC-007", "SRC-016"], "collection", True),
            ("ddi-who-clinicaltrials-oms-prov-dcat-datacite-crosswalk-and-loss", "DDI, WHO, ClinicalTrials.gov, OMS, PROV, DCAT and DataCite crosswalk and loss", "Pinned source and target versions, identity, study, design, collection, observation, dataset, output, agent, provenance and relation mappings, omissions, conflicts and round-trip classification.", "interoperability", ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010"], "collection", False),
        ]),
        ("access-disclosure-retention-and-safe-agent-operation", "Access, disclosure, retention and safe agent operation", "Controls purpose-bound reading, mutation, sharing and disposition for people and agents.", ["SRC-007", "SRC-008", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"], [
            ("role-view-purpose-access-sharing-embargo-redaction-exception-and-audit", "Role view, purpose, access, sharing, embargo, redaction, exception and audit", "Purpose-bound views, access decisions, sharing commitments, embargoes, controlled-access terms, field redaction, exceptions, expiry and tamper-evident access events.", "access", ["SRC-008", "SRC-011", "SRC-012", "SRC-013", "SRC-014"], "collection", True),
            ("retention-trigger-hold-disposition-tombstone-agent-authority-idempotency-and-postcheck", "Retention trigger, hold, disposition, tombstone, agent authority, idempotency and post-check", "Retention class and trigger, legal or ethics hold, deletion eligibility, minimum tombstone, delegated agent scope, preconditions, dry run, idempotency key, expected revision and post-condition verification.", "retention", ["SRC-007", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"], "collection", True),
        ]),
    ]),
]


KIND_CYCLE = ["definition", "identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def build_finding(raw, ordinal):
    finding_id, name, description, primary_kind, refs, value_kind, required = raw
    kinds = [primary_kind, KIND_CYCLE[(ordinal * 7 + 3) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal * 13 + 5) % len(KIND_CYCLE)]]
    for position in range(1, 3):
        while kinds[position] in kinds[:position]:
            kinds[position] = KIND_CYCLE[(KIND_CYCLE.index(kinds[position]) + 1) % len(KIND_CYCLE)]
    subject = name.lower()
    questions = [
        {"id": f"{finding_id}-q01", "text": f"What study-scoped identities, classifications, definitions, versions, values and explicit unknowns establish {subject}?", "kind": kinds[0], "answer_data": ["identifiers and classifications", "definitions and version", "values, scope and explicit unknowns"]},
        {"id": f"{finding_id}-q02", "text": f"Which authority, source, method, evidence, event time, knowledge time, uncertainty and limitations support {subject}?", "kind": kinds[1], "answer_data": ["authority and source", "method and evidence", "event and knowledge time", "uncertainty, contradiction and limitations"]},
        {"id": f"{finding_id}-q03", "text": f"How may {subject} be validated, accessed, amended, contested, corrected, related, retained or disposed without losing prior study history?", "kind": kinds[2], "answer_data": ["validation and access rules", "authorized change and dispute", "typed relations and lineage", "retention, hold and disposition"]},
    ]
    return {
        "id": finding_id,
        "name": name,
        "description": description,
        "source_refs": refs,
        "questions": questions,
        "data_elements": [{"id": f"{finding_id}-data", "name": f"{name} data", "description": f"Structured research-study data for {subject} with scope, provenance, time, confidence and access marking.", "value_kind": value_kind, "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{finding_id}-record", "name": f"{name} record", "description": f"Versioned evidence-bearing research-study record for {subject} with authority, time, provenance and access marking.", "media_or_form": ["logical research-study assertion", "protocol, plan, event, observation, result, finding, output or governance reference"], "serial": True, "identity_strategy": f"Study identifier plus {finding_id} assertion, artifact or event identifier; title, date, timestamp and digest never identify the study alone.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def build_structure():
    bundles = []
    ordinal = 0
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
    ("register-research-study", "Register research study", "Create a stable study identity, classify its inquiry profile and resolve duplicates and neighboring aggregates.", ["study intent", "source authority", "disciplinary profile", "candidate identifiers"], ["versioned research study root"], ["identity, duplicate, authority, profile and boundary checks pass"], ["one inquiry aggregate exists without copying its project, experiments, datasets or publications"], ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-009"]),
    ("release-questions-design-and-protocol", "Release questions, design and protocol", "Freeze research questions, hypotheses, outcomes, methods and the protocol revision before governed conduct.", ["study root", "questions and hypotheses", "design", "protocol"], ["protocol release"], ["scope, definitions, versions, outcomes, analysis intent and amendment rules validate"], ["intent remains distinguishable from later conduct and findings"], ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-007"]),
    ("authorize-roles-ethics-and-privacy", "Authorize roles, ethics and privacy", "Bind accountable roles, oversight decisions, participant safeguards and privacy controls for the applicable profile.", ["protocol release", "actor references", "ethics and privacy requirements"], ["governance and authorization release"], ["delegation, conflicts, approvals, conditions, consent requirements and access rules validate"], ["governed study activity can begin within explicit authority"], ["SRC-004", "SRC-005", "SRC-012", "SRC-013", "SRC-014"]),
    ("define-population-sample-and-assignment", "Define population, sample and assignment", "Pin target population, eligibility, sampling, size rationale, cohort or arm structure and assignment method.", ["protocol release", "population masters", "sampling frame", "design assumptions"], ["population and sampling release"], ["eligibility, unit, representativeness, power or precision and assignment checks pass"], ["inferential scope and selection limitations are inspectable"], ["SRC-002", "SRC-004", "SRC-005", "SRC-006"]),
    ("coordinate-study-conduct", "Coordinate study conduct", "Record sites, resources, interventions or exposures and actual lifecycle and conduct events without rewriting the plan.", ["authorized study", "sites and resources", "activity schedule"], ["conduct event stream"], ["resource, safety, timing, assignment, deviation and evidence rules validate"], ["planned and actual conduct remain attributable and comparable"], ["SRC-002", "SRC-004", "SRC-005", "SRC-007", "SRC-016"]),
    ("capture-observations-and-manage-data", "Capture observations and manage data", "Bind source observations and datasets to instruments, procedures, variables, transformations, quality and sharing plans.", ["study conduct", "collection events", "instruments", "source observations"], ["collection, observation and data-product release"], ["feature, property, value, unit, time, method, uncertainty, provenance, privacy and quality checks pass"], ["source evidence remains distinct from analysis and interpretation"], ["SRC-002", "SRC-006", "SRC-007", "SRC-008", "SRC-011", "SRC-012"]),
    ("execute-analysis-and-assert-results", "Execute analysis and assert results", "Run or record a pinned analysis and issue estimates and bounded result assertions.", ["analysis plan", "dataset revisions", "software and code", "method parameters"], ["analysis execution and result release"], ["population, estimand, assumptions, versions, multiplicity, diagnostics, uncertainty and provenance validate"], ["results can be reviewed without treating significance as truth or association as causation"], ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-011"]),
    ("review-and-release-findings-and-outputs", "Review and release findings and outputs", "Relate results to questions and release findings, datasets, software, materials or publications with limitations.", ["result release", "questions and hypotheses", "review", "output references"], ["finding and output release"], ["evidence, interpretation, causal scope, generalizability, contradiction, rights, identifiers and access validate"], ["knowledge outputs remain connected to methods, evidence and study lineage"], ["SRC-001", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011"]),
    ("amend-correct-withdraw-or-supersede", "Amend, correct, withdraw or supersede", "Preserve released history while appending protocol amendments, corrections, disputes, terminations, withdrawals or retractions.", ["current study head", "new evidence or decision", "actor authority", "reason"], ["new release and lifecycle event"], ["expected revision, impact, authority, affected scope and residual-validity checks pass"], ["later learning never silently erases prior intent, conduct, evidence or outputs"], ["SRC-004", "SRC-005", "SRC-007", "SRC-009", "SRC-015", "SRC-016"]),
    ("project-disclose-retain-and-audit", "Project, disclose, retain and audit", "Create version-pinned external views and perform controlled access, sharing and information-lifecycle operations.", ["study revision", "target profile", "purpose", "policy"], ["projection, disclosure, disposition or audit event"], ["mapping loss, access, privacy, embargo, hold, tombstone, idempotency and post-checks validate"], ["research context remains interoperable, protected and accountable"], ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]),
]


def service_layers():
    return {
        "dimension": {
            "owner_package_requirements": [
                "Dimension identity, owner, research sponsor, scientific authority, ethics, privacy, data and records stewards",
                "Research-study type, discipline, protocol, lifecycle, role, ethics, data, output, interoperability, access and retention registries",
                "Master mappings for projects, grants, experiments, trials, people, participants, populations, sites, specimens, instruments, observations, datasets, software, publications, ethics decisions, artifacts and audit records",
                "Protocol release, ethics, conduct, analysis, finding, publication, disclosure, correction, retention and agent-operation policies",
            ],
            "namespace_guidance": "Mint stable IDs for study roots, releases, questions, hypotheses, protocol revisions, study-scoped bindings, conduct events, analysis executions, result and finding assertions, outputs and lifecycle events. Preserve authoritative external project, person, participant, specimen, observation, dataset, publication and ethics identities; never use a title, date or digest as study identity.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local research, protocol, ethics, data, output and policy registries"],
        },
        "canon_and_patch": {
            "canonicalization_rules": [
                "Canonicalize by authoritative source plus study identifier and lineage head, not by title, acronym, sponsor, registration date or digest.",
                "Keep protocol intent, actual conduct, observation, analysis execution, result, statistical evidence, interpretation, finding and publication as distinct assertion classes.",
            ],
            "patch_rules": [
                "Extensions declare discipline and method profile, target bundle or finding, semantics, authority, lifecycle, ethics, privacy, quality and interoperability effects.",
                "Released protocols, conduct events, observations, analyses, results, findings and output bindings are immutable; corrections and amendments create successors.",
                "A patch must never silently change research questions, eligibility, sampling, outcomes, intervention, analysis method, source data, consent state or original evidence.",
            ],
            "compatibility_rules": [
                "Unknown additive fields may be ignored only when study identity, questions, protocol, design, population, conduct, evidence, analysis, findings, lifecycle and provenance remain intact.",
                "DDI, WHO, ClinicalTrials.gov, OMS, PROV, DCAT and DataCite mappings pin source and target versions and declare omissions, semantic conflicts and round-trip limits.",
            ],
        },
        "artifact_rules": {
            "identity_priority": [
                "Authoritative master-system study identifier from a registry, institution or sponsor, qualified by source and study class.",
                "Governed globally resolvable study IRI under a controlled namespace.",
                "Dimension UUID when no authoritative or governed global identifier exists.",
            ],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; separate planned, effective, event, observation, result, release, ingestion and knowledge times and preserve source precision.",
            "serial_naming_rule": "Use {study-id}--{protocol-or-release}--{artifact-kind}--{assertion-or-event-id}; never use title, date, timestamp or digest alone.",
            "integrity_rule": "Store digest, media type, study and release binding, source and profile versions, protocol and dataset revisions, generating actor or tool, event and knowledge times, access marking and provenance.",
        },
        "policies": [
            "A Research Study is not the supporting Research Project, one Experiment or Trial, a Dataset, a Publication, a Participant, a Specimen or an Analysis Procedure.",
            "Protocol intent, actual conduct, raw observation, analysis execution, estimate, statistical evidence, interpretation, finding and policy or clinical conclusion remain separate source-qualified assertions.",
            "Study ownership does not transfer ownership of project, grant, person, participant, population, site, specimen, instrument, observation, dataset, software, publication, ethics-decision, artifact or audit masters. Study disposition never cascades to linked masters.",
            "Agents may validate, link and project allowlisted data, but participant contact, consent, intervention assignment, hazardous conduct, protected disclosure, scientific signoff and disposition require delegated authority and applicable policy controls.",
        ],
        "crud": {
            "read": ["Resolve Dimension policies, study identity and lineage, profile, questions, protocol, design, population, roles, ethics, conduct, observations, data, analyses, findings, outputs, provenance and access purpose."],
            "create": ["Record study identity, research purpose, questions, protocol and design, population and sampling, roles, ethics and privacy requirements, data and analysis plans and provenance before governed conduct."],
            "update": ["Append protocol, ethics, conduct, observation, data, analysis, result, finding, output, review, correction, withdrawal or supersession events with actor, authority, rationale, event and knowledge time and expected revision; never overwrite released history."],
            "delete": ["Apply ethics, participant-rights, data-sharing, records, retention and legal-hold policy; cancel, terminate, withdraw or retract separately from deleting eligible working copies, preserve required evidence lineage and a minimum tombstone, and never cascade deletion to linked masters."],
        },
        "roles": [
            {"name": "Research sponsor or accountable authority", "responsibilities": ["Own purpose, resources, responsible-party appointment, applicable policy and accountable disposition."]},
            {"name": "Principal investigator or study director", "responsibilities": ["Own scientific conduct, protocol compliance, delegated work and truthful reporting within authority."]},
            {"name": "Protocol and method steward", "responsibilities": ["Own questions, design, outcomes, instruments, analysis intent, amendments and method definitions."]},
            {"name": "Ethics, safety or independent oversight body", "responsibilities": ["Issue external decisions and conditions, monitor applicable safeguards and preserve independent authority."]},
            {"name": "Participant, population, site, sample or resource custodian", "responsibilities": ["Own external identities, permissions, custody, suitability and source assertions used by the study."]},
            {"name": "Data, analysis and software steward", "responsibilities": ["Protect collection semantics, dataset and code versions, transformations, quality, analysis execution and reproducibility evidence."]},
            {"name": "Reviewer, author or publication steward", "responsibilities": ["Review evidence and limitations, govern findings and outputs, and correct or retract without rewriting history."]},
            {"name": "Privacy, access and records steward", "responsibilities": ["Control protected views, sharing, embargo, retention, holds, disposition and access auditability."]},
        ],
        "access": {
            "default_rule": "Deny direct participant identifiers, sensitive attributes, consent records, confidential sponsor material, protected locations, unpublished hypotheses, embargoed outputs and raw evidence unless a purpose-bound Dimension policy permits the minimum necessary view. Field redaction is a governed projection, not a separate access scope.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Investigator, participant-rights responder, ethics body, safety responder, data custodian, reviewer, auditor, regulator or court access cites authority and remains minimum-necessary, time-limited and separately logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, study, operation, policy, RFC 3339 time, release or affected fields, source revision and outcome without copying protected source data unnecessarily."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": [
                "Read Dimension research, ethics, safety, privacy, access, retention and agent-operation policies.",
                "Read this model and linked project, grant, experiment, trial, person, participant, population, site, sample, instrument, observation, dataset, software, publication, ethics, artifact and audit models before mutation.",
            ],
        },
    }


def coverage():
    rows = [
        ("identity", "Study, release, protocol, question, hypothesis, binding, analysis, result, finding, output and lifecycle identities are distinct."),
        ("classification and definition", "Cross-disciplinary profiles and project, experiment, trial, assessment, dataset and publication boundaries are explicit."),
        ("direct properties", "Purpose, protocol, design, roles, population, ethics, conduct, evidence, analyses, findings and outputs are first-class."),
        ("recognition and observation", "Observed feature, property, value, unit, method, time, quality and uncertainty are source-qualified."),
        ("capabilities and possible actions", "Register, release, authorize, sample, conduct, collect, analyse, assert, review, amend, project and retain are governed."),
        ("composition", "Projects, grants, experiments, participants, samples, sites, instruments, observations, datasets, software, publications, ethics decisions and audit masters remain external."),
        ("lifecycle", "Proposal, design, registration, approval, recruitment, collection, analysis, completion, termination, withdrawal, publication, correction, retraction and archive preserve history."),
        ("relationships", "Questions, hypotheses, protocols, assignments, usage, generation, derivation, outputs and crosswalks use typed relations."),
        ("temporal", "Planned, effective, conduct, observation, analysis, result, release, ingestion and knowledge times remain distinct."),
        ("spatial", "Sites, environments, collection locations and observed-feature locations remain source-qualified and access-controlled."),
        ("provenance", "Plans, agents, used and generated entities, observations, analyses, findings, revisions and invalidations preserve provenance."),
        ("ownership and stewardship", "Sponsor, investigator, method, ethics, participant, data, analysis, publication, privacy and records duties are separated."),
        ("validation and quality", "Identity, revision, eligibility, sampling, timing, method, evidence, bias, uncertainty, limitation and stale-head checks are explicit."),
        ("access and privacy", "Purpose-bound views, participant safeguards, embargoes, protected evidence and field-redacted projections are explicit."),
        ("retention and deletion", "Termination or retraction, working-copy deletion, retained evidence, holds and minimum tombstones are distinguished."),
        ("interoperability", "DDI, WHO, ClinicalTrials.gov, OMS, PROV, DCAT and DataCite projections are versioned and loss-aware."),
    ]
    return {
        "claim": "Covers a cross-disciplinary Research Study aggregate from questions and immutable protocol intent through governance, design, conduct, observations, managed data, analyses, bounded findings, outputs, interoperability and governed disposition.",
        "confidence": "medium",
        "checklist": [{"dimension": dimension, "status": "gap" if dimension in {"composition", "interoperability"} else "covered", "notes": notes + (" Proposed relations or mapping versions remain held for review." if dimension in {"composition", "interoperability"} else "")} for dimension, notes in rows],
        "known_omissions": [
            "No successful independent Claude or Grok result was available; disciplinary, statistical, ethics, regional, legal and controlled-data review is required before canonical promotion.",
            "Research Study has no single universal cross-domain vocabulary. This package defines a shared inquiry kernel and requires discipline and method profiles.",
            "No approved relation rows were supplied. The registry Experiment or Trial parent link and proposed project, participant, specimen, dataset, publication and output relations remain holds.",
            "WHO TRDS and ClinicalTrials.gov are clinical-trial profiles and must not be treated as universal requirements for all research.",
            "The DataCite property crosswalk is pinned to 4.6 while the official release history lists 4.7 as current. A 4.7 delta review is required before canonical interoperability claims.",
            "45 CFR Part 46 applies within a United States regulatory context. Other jurisdictions, disciplines and institutions require their own ethics, consent, privacy, safety, retention and disclosure profiles.",
        ],
        "conflicts": [
            "Some systems use study, project, investigation, experiment and trial interchangeably. Vercy preserves separate roots and typed containment or reference relations.",
            "Preregistration, registry publication, protocol release, ethics approval, recruitment start, data lock, completion and publication are different events and can disagree across sources.",
            "Open data, participant privacy, sponsor confidentiality, reproducibility, archival accountability and withdrawal rights can impose competing obligations.",
        ],
        "regional_assumptions": [
            "Human-subject, animal, environmental, export-control, privacy, intellectual-property, clinical, research-integrity and records obligations vary by jurisdiction, institution and discipline.",
            "OECD Frascati supplies a statistical R&D boundary rather than a universal operational lifecycle for every form of scholarship.",
            "DDI is strongest for social, behavioural and economic data; WHO and ClinicalTrials.gov are clinical-trial profiles; OMS is observation-oriented; DCAT and DataCite focus discovery and outputs.",
        ],
        "adversarial_checks": [
            "Reject a study without stable identity, explicit questions or purpose, pinned protocol and design, accountable authority, inferential population and evidence lineage.",
            "Reject consent inferred from enrolment, hypothesis support inferred from significance, causality inferred from association, generalizability inferred from sample size or reproducibility inferred from one study.",
            "Reject an amendment or correction that overwrites released questions, eligibility, sampling, outcomes, conduct, source observations, analyses, findings or publications.",
            "Reject copied participant, specimen, observation, dataset, publication, ethics or project masters whose independent identity, authority and lifecycle are lost.",
            "Reject agent contact, intervention assignment, protected disclosure, scientific signoff or disposition outside delegated authority, ethics, safety, privacy, retention and post-check controls.",
        ],
    }


def build():
    return {
        "schema_version": "1.0.0",
        "model": {
            "registry_id": "vr.wm-act-036",
            "model_id": "WM-ACT-036",
            "name": "Research Study",
            "entry_kind": "aggregate",
            "purpose": "Represent one governed, versioned inquiry aggregate that pursues declared research questions or hypotheses through a protocol and design, defined populations, materials or phenomena, data collection, analysis and bounded findings.",
            "scope_statement": "Owns study identity and lineage, source-qualified classification, questions and hypotheses, protocol and design releases, study-scoped role, funding, site, ethics and privacy bindings, population and sampling assertions, cohorts, arms, interventions or exposures, conduct events, collection and analysis plans, result and finding assertions, registration and amendment history, output links, limitations, interoperability, access and retention. Research Project, Grant or Award, Experiment or Trial, Test Execution, Person, Participant, Population, Sample or Specimen, Site, Instrument, Observation, Measurement, Dataset, Software, Publication, Ethics Decision, Artifact and Audit masters remain external.",
            "in_scope": [
                "Study identity, classification, questions, hypotheses, protocol, design, roles, funding and accountable authority",
                "Ethics, privacy, population, eligibility, sampling, cohorts, sites, resources, interventions, exposures, conduct, observations and managed data",
                "Analysis plans and executions, estimates, uncertainty, findings, limitations, registration, outputs, reproducibility, lifecycle, interoperability, access, retention and safe agents",
            ],
            "out_of_scope": [
                "Independent project, grant, experiment, trial, test execution, person, participant, population, specimen, site, instrument, observation, dataset, software, publication, ethics-decision, artifact or audit master lifecycles",
                "Inferring consent from participation, causality from association, truth from significance, generalizability from one sample, data fitness from completeness or reproducibility from one study",
                "Implementing a laboratory, clinical-trial management system, electronic data capture system, statistical environment, repository, ethics board, registry or universal legal-compliance regime",
            ],
            "boundary_notes": [
                {"neighbor": "Research Project, Programme, Grant or Award", "distinction": "These organize objectives, funding, portfolios, schedules and delivery. A study is the inquiry aggregate with questions, protocol, evidence and findings and can be supported by several projects or awards.", "source_refs": ["SRC-001", "SRC-003", "SRC-007", "SRC-009"]},
                {"neighbor": "Experiment, Trial or Test Execution", "distinction": "These are contained or referenced conduct components with their own occurrence identity. The study owns broader design and synthesis but does not rewrite their evidence.", "source_refs": ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007"]},
                {"neighbor": "Participant, Population, Sample, Specimen, Site or Instrument", "distinction": "The study owns scoped eligibility, selection, assignment and usage assertions. External masters retain identity, custody, lifecycle and source authority.", "source_refs": ["SRC-002", "SRC-005", "SRC-006", "SRC-013"]},
                {"neighbor": "Observation, Measurement, Dataset or Software", "distinction": "The study binds exact source and derived versions and records transformations and use. Observation and data-product masters retain their own semantics and provenance.", "source_refs": ["SRC-002", "SRC-006", "SRC-007", "SRC-008", "SRC-011"]},
                {"neighbor": "Finding, Scholarly Publication or other Output", "distinction": "A study can issue bounded finding assertions and link released outputs. A publication is a separate authored and disseminated record and may contain claims not controlled by the study master.", "source_refs": ["SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011"]},
                {"neighbor": "Ethics Decision, Assessment or Audit Record", "distinction": "Independent bodies and processes issue their own decisions and evidence. The study binds their exact versions and conditions without becoming the decision master.", "source_refs": ["SRC-005", "SRC-007", "SRC-013", "SRC-014"]},
            ],
        },
        "sources": SOURCES,
        "structure": build_structure(),
        "functions": [{"id": row[0], "name": row[1], "description": row[2], "inputs": row[3], "outputs": row[4], "preconditions": row[5], "effects": row[6], "source_refs": row[7]} for row in FUNCTIONS],
        "composition": [
            {"target": "Research Project, Programme, Grant and Award models", "relation": "REFERENCE", "purpose": "Resolve organizational sponsorship, portfolio, funding and delivery context while keeping inquiry identity separate.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-007", "SRC-009"]},
            {"target": "Experiment, Trial and Test Execution models", "relation": "COMPOSE", "purpose": "Relate study-scoped conduct components without absorbing their occurrence identity, evidence or lifecycle.", "required": False, "source_refs": ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-007"]},
            {"target": "Participant, Population, Sample, Specimen, Site, Instrument and Resource models", "relation": "REFERENCE", "purpose": "Bind study-scoped selection, assignment and use while preserving external identity, custody and authority.", "required": False, "source_refs": ["SRC-002", "SRC-005", "SRC-006", "SRC-013"]},
            {"target": "Observation, Measurement, Dataset, Software, Artifact and Audit models", "relation": "REFERENCE", "purpose": "Link source and derived evidence with exact versions, transformations, integrity and provenance.", "required": True, "source_refs": ["SRC-002", "SRC-006", "SRC-007", "SRC-008", "SRC-011"]},
            {"target": "Scholarly Publication and other Research Output models", "relation": "REFERENCE", "purpose": "Link datasets, software, materials, protocols and publications as separately versioned outputs with access and correction history.", "required": False, "source_refs": ["SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011"]},
            {"target": "DDI Lifecycle 3.3, WHO TRDS 1.3.1, ClinicalTrials.gov protocol definitions, OGC OMS, W3C PROV-O and DCAT 3, and DataCite Metadata Schema", "relation": "ALIGN", "purpose": "Project study, collection, trial, observation, provenance, dataset and output views through version-pinned mappings with declared loss and non-equivalence.", "required": False, "source_refs": ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010"]},
        ],
        "service_layers": service_layers(),
        "coverage": coverage(),
    }


if __name__ == "__main__":
    (RUN_DIR / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
