#!/usr/bin/env python3
"""Build the official-source-grounded Codex fallback for WM-KNW-009."""

import importlib.util
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
BASE_PATH = RUN.parent / "wm-flw-015" / "build_codex_result.py"
SPEC = importlib.util.spec_from_file_location("wm_flw_015_builder", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
AT = "2026-09-06T21:46:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {"id": f"SRC-{i:03d}", "title": title, "organization": org, "url": url,
            "version_or_date": version, "source_type": kind, "primary_source": True,
            "authority_tier": tier, "accessed_at": AT, "relevance": relevance}


SOURCES = [
    src(1, "NIST/SEMATECH Engineering Statistics Handbook", "National Institute of Standards and Technology", "https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook", "NIST Handbook 151, page accessed 2026-09-06", "public-authority", "Explains experimental design, statistical assumptions, hypothesis tests and interpretation."),
    src(2, "Product and Process Comparisons: Introduction", "National Institute of Standards and Technology", "https://www.itl.nist.gov/div898/handbook/prc/section1/prc1.htm", "NIST e-Handbook section accessed 2026-09-06", "public-authority", "Distinguishes hypothesis tests, confidence intervals and comparative questions."),
    src(3, "ISO 3534-1 Statistics vocabulary", "International Organization for Standardization", "https://www.iso.org/standard/40145.html", "ISO 3534-1:2006, revision pending", "standard", "Defines general statistical and probability terms and symbols."),
    src(4, "International Vocabulary of Metrology", "Joint Committee for Guides in Metrology", "https://www.bipm.org/en/doi/10.59161/jcgm200-2012", "JCGM 200:2012, VIM 3rd edition", "standard", "Defines measurement, quantity, result, uncertainty, calibration and metrological concepts."),
    src(5, "Guide to the Expression of Uncertainty in Measurement", "Joint Committee for Guides in Metrology", "https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf", "JCGM 100:2008", "standard", "Defines evaluation and expression of measurement uncertainty."),
    src(6, "Protocol Registration Data Element Definitions", "United States National Library of Medicine", "https://clinicaltrials.gov/policy/protocol-definitions", "ClinicalTrials.gov definitions accessed 2026-09-06", "public-authority", "Defines study hypothesis summaries, objectives, interventions, outcomes and protocol metadata."),
    src(7, "Results Data Element Definitions", "United States National Library of Medicine", "https://clinicaltrials.gov/policy/results-definitions", "ClinicalTrials.gov definitions updated 31 December 2024", "public-authority", "Defines outcome data, statistical tests, null hypotheses, estimates and result reporting."),
    src(8, "WHO Trial Registration Data Set", "World Health Organization", "https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set", "WHO TRDS version 1.3.1", "public-authority", "Defines minimum prospective trial identity, design, intervention and outcome registration data."),
    src(9, "Create a Preregistration", "Center for Open Science", "https://help.osf.io/article/158-create-a-preregistration", "OSF guidance accessed 2026-09-06", "first-party-doc", "Defines time-stamped preregistration and frozen registration workflows."),
    src(10, "Frascati Manual 2015", "Organisation for Economic Co-operation and Development", "https://www.oecd.org/en/publications/frascati-manual-2015_9789264239012-en.html", "OECD Frascati Manual 2015", "public-authority", "Defines research and experimental development concepts and activity boundaries."),
    src(11, "Recommendation on Open Science", "UNESCO", "https://www.unesco.org/en/legal-affairs/recommendation-open-science", "UNESCO Recommendation, 23 November 2021", "public-authority", "Frames open hypothesis formulation, methods, data, evaluation, scrutiny and reproducibility."),
    src(12, "Ontology for Biomedical Investigations", "OBI Consortium", "https://obi-ontology.org/", "OBI production ontology accessed 2026-09-06", "ontology", "Defines investigations, study designs, objectives, assays, data and analyses."),
    src(13, "STATO: an Ontology of Statistical Methods", "STATO Consortium", "https://stato-ontology.org/", "STATO accessed 2026-09-06", "ontology", "Defines statistical methods, estimates, tests and links to evaluated hypotheses."),
    src(14, "Evidence and Conclusion Ontology", "ECO Consortium", "https://evidenceontology.org/", "ECO release 2025-06-23", "ontology", "Defines evidence and assertion-method classes supporting scientific conclusions."),
    src(15, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Defines entities, activities, agents, attribution, derivation, revision and invalidation."),
    src(16, "Web Annotation Data Model", "World Wide Web Consortium", "https://www.w3.org/TR/annotation-model/", "W3C Recommendation, 23 February 2017", "standard", "Defines body-target annotations, motivations, provenance and scoped selectors."),
    src(17, "Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note, 15 December 2016", "ontology", "Defines quality measurements, annotations, policies and provenance."),
    src(18, "ODRL Information Model 2.2", "World Wide Web Consortium", "https://www.w3.org/TR/odrl-model/", "W3C Recommendation, 15 February 2018", "standard", "Defines permissions, prohibitions, duties and constraints for governed knowledge use."),
    src(19, "Shapes Constraint Language", "World Wide Web Consortium", "https://www.w3.org/TR/shacl/", "W3C Recommendation, 20 July 2017", "standard", "Defines declarative validation constraints and validation reports for RDF graphs."),
    src(20, "DataCite Metadata Schema", "DataCite", "https://schema.datacite.org/", "DataCite Metadata Schema 4.7, 3 March 2026", "schema", "Defines persistent research-resource metadata, versions, relations, funding and rights."),
    src(21, "RO-Crate Specification", "RO-Crate Community", "https://www.researchobject.org/ro-crate/specification.html", "RO-Crate 1.3, current long-term release", "standard", "Defines portable research-object aggregation, contextual entities, provenance and profiles."),
    src(22, "Schema.org Claim", "Schema.org Community Group", "https://schema.org/Claim", "Schema.org vocabulary accessed 2026-09-06", "ontology", "Defines a claim as a fact-oriented assertion that can be reviewed or referenced."),
    src(23, "RFC 3339 Date and Time on the Internet", "Internet Engineering Task Force", "https://www.rfc-editor.org/rfc/rfc3339.html", "RFC 3339, July 2002", "standard", "Defines timestamps with seconds and explicit numeric offsets or Z."),
    src(24, "FAIR Guiding Principles", "Nature Scientific Data", "https://www.nature.com/articles/sdata201618", "Scientific Data 3, article 160018, 2016", "scientific", "Defines findable, accessible, interoperable and reusable research objects and metadata."),
]


ROWS = [
    ("hypothesis-identity-formulation-and-kind", "Hypothesis identity, formulation and kind", "Establish one provisional proposition and its semantic kind before evaluating it.", [
        ("identity-revision-and-related-concept-boundary", "Identity, revision and related-concept boundary", ["SRC-010", "SRC-015", "SRC-020", "SRC-022", "SRC-023"], [
            ("hypothesis-identifier-namespace-version-revision-and-successor", "Hypothesis identifier, namespace, version, revision and successor", "identity"),
            ("hypothesis-question-assumption-prediction-theory-claim-objective-and-result-distinction", "Hypothesis, question, assumption, prediction, theory, claim, objective and result distinction", "classification")]),
        ("expression-language-and-formalization", "Expression, language and formalization", ["SRC-012", "SRC-013", "SRC-016", "SRC-019", "SRC-022"], [
            ("natural-language-proposition-language-terms-and-scope-note", "Natural-language proposition, language, terms and scope note", "definition"),
            ("formal-expression-variables-quantifiers-negation-relation-and-logic-profile", "Formal expression, variables, quantifiers, negation, relation and logic profile", "constraint")])]),
    ("classification-scope-variables-and-conditions", "Classification, scope, variables and conditions", "Make the proposition type, universe of discourse and dependencies explicit.", [
        ("hypothesis-type-and-test-profile", "Hypothesis type and test profile", ["SRC-001", "SRC-002", "SRC-003", "SRC-006", "SRC-007", "SRC-013"], [
            ("scientific-statistical-causal-associational-descriptive-explanatory-and-predictive-kind", "Scientific, statistical, causal, associational, descriptive, explanatory and predictive kind", "classification"),
            ("null-alternative-directional-equivalence-noninferiority-universal-and-existential-profile", "Null, alternative, directional, equivalence, noninferiority, universal and existential profile", "classification")]),
        ("population-variables-relations-and-boundary", "Population, variables, relations and boundary", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-012", "SRC-013"], [
            ("domain-population-unit-phenomenon-context-condition-and-exclusion", "Domain, population, unit, phenomenon, context, condition and exclusion", "constraint"),
            ("independent-dependent-exposure-outcome-comparator-confounder-covariate-and-mediator", "Independent, dependent, exposure, outcome, comparator, confounder, covariate and mediator", "relationship")])]),
    ("provenance-rationale-assumptions-and-prior-evidence", "Provenance, rationale, assumptions and prior evidence", "Preserve who proposed the hypothesis, why and on which qualified premises.", [
        ("authorship-motivation-and-rationale", "Authorship, motivation and rationale", ["SRC-010", "SRC-011", "SRC-015", "SRC-016", "SRC-020", "SRC-022", "SRC-024"], [
            ("proposer-owner-contributor-source-time-and-authority", "Proposer, owner, contributor, source, time and authority", "provenance"),
            ("research-question-motivation-gap-mechanism-rationale-and-intended-use", "Research question, motivation, gap, mechanism, rationale and intended use", "definition")]),
        ("assumption-theory-prior-and-evidence-context", "Assumption, theory, prior and evidence context", ["SRC-001", "SRC-009", "SRC-012", "SRC-014", "SRC-015", "SRC-016", "SRC-024"], [
            ("background-theory-model-assumption-prior-belief-and-dependency", "Background theory, model, assumption, prior belief and dependency", "relationship"),
            ("prior-evidence-citation-support-challenge-gap-bias-and-conflict", "Prior evidence, citation, support, challenge, gap, bias and conflict", "evidence")])]),
    ("operationalization-prediction-criteria-and-evaluation-design", "Operationalization, prediction, criteria and evaluation design", "Turn an abstract proposition into a predeclared evaluable contract.", [
        ("operational-definition-measure-and-prediction", "Operational definition, measure and prediction", ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-012", "SRC-013"], [
            ("construct-indicator-operation-instrument-measure-estimand-and-unit", "Construct, indicator, operation, instrument, measure, estimand and unit", "measurement"),
            ("predicted-observation-effect-direction-range-timing-and-potential-falsifier", "Predicted observation, effect, direction, range, timing and potential falsifier", "requirement")]),
        ("criterion-protocol-study-and-preregistration", "Criterion, protocol, study and preregistration", ["SRC-001", "SRC-002", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-013"], [
            ("decision-threshold-error-rate-power-multiplicity-practical-significance-and-stop-rule", "Decision threshold, error rate, power, multiplicity, practical significance and stop rule", "decision"),
            ("protocol-study-experiment-test-dataset-analysis-plan-registration-and-deviation", "Protocol, study, experiment, test, dataset, analysis plan, registration and deviation", "process")])]),
    ("assessment-evidence-uncertainty-and-lifecycle", "Assessment, evidence, uncertainty and lifecycle", "Record source-qualified evaluations without replacing the hypothesis with a global truth flag.", [
        ("result-evidence-and-assessment", "Result, evidence and assessment", ["SRC-001", "SRC-002", "SRC-004", "SRC-005", "SRC-007", "SRC-013", "SRC-014", "SRC-015", "SRC-017"], [
            ("observation-result-estimate-effect-uncertainty-pvalue-confidence-and-bayes-factor", "Observation, result, estimate, effect, uncertainty, p-value, confidence and Bayes factor", "measurement"),
            ("support-challenge-refutation-corroboration-inconclusive-and-scope-qualified-assessment", "Support, challenge, refutation, corroboration, inconclusive and scope-qualified assessment", "validation")]),
        ("state-review-correction-and-evolution", "State, review, correction and evolution", ["SRC-009", "SRC-011", "SRC-015", "SRC-016", "SRC-017", "SRC-020", "SRC-021", "SRC-024"], [
            ("proposed-preregistered-under-test-evaluated-supported-unsupported-refuted-and-withdrawn-state", "Proposed, preregistered, under-test, evaluated, supported, unsupported, refuted and withdrawn state", "lifecycle"),
            ("review-dispute-correction-reformulation-split-merge-revision-and-supersession", "Review, dispute, correction, reformulation, split, merge, revision and supersession", "lifecycle")])]),
    ("governance-access-reuse-and-interoperability", "Governance, access, reuse and interoperability", "Keep research ethics, disclosure, retention and projections explicit and loss-aware.", [
        ("roles-ethics-quality-access-and-retention", "Roles, ethics, quality, access and retention", ["SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-015", "SRC-017", "SRC-018", "SRC-020", "SRC-024"], [
            ("owner-investigator-reviewer-steward-conflict-ethics-and-accountability", "Owner, investigator, reviewer, steward, conflict, ethics and accountability", "authority"),
            ("consent-privacy-confidentiality-openness-license-access-retention-and-legal-hold", "Consent, privacy, confidentiality, openness, license, access, retention and legal hold", "access")]),
        ("standards-crosswalk-conformance-and-loss", "Standards crosswalk, conformance and loss", [f"SRC-{i:03d}" for i in range(1, 25)], [
            ("nist-iso-jcgm-trial-obi-stato-eco-w3c-datacite-rocrate-and-fair-crosswalk", "NIST, ISO, JCGM, trial, OBI, STATO, ECO, W3C, DataCite, RO-Crate and FAIR crosswalk", "interoperability"),
            ("profile-version-license-conformance-transformation-and-semantic-loss", "Profile, version, license, conformance, transformation and semantic loss", "validation")])]),
]

KIND_CYCLE = ["identity", "classification", "composition", "relationship", "state", "lifecycle", "temporal", "spatial", "provenance", "ownership", "authority", "requirement", "constraint", "process", "event", "measurement", "evidence", "quality", "validation", "security", "privacy", "retention", "access", "exception", "interoperability", "decision"]


def make_finding(item, ordinal, refs):
    fid, name, primary_kind = item
    lower = name.lower()
    kinds = [primary_kind, KIND_CYCLE[(ordinal + 8) % len(KIND_CYCLE)], KIND_CYCLE[(ordinal + 17) % len(KIND_CYCLE)]]
    return {
        "id": fid, "name": name,
        "description": f"Records {lower} as a source-qualified Hypothesis assertion while claims, assumptions, studies, data, results, evidence, publications and decisions retain external mastership.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which identity, formulation, hypothesis kind, scope, variables, conditions and revision establish {lower}?", "kind": kinds[0], "answer_data": ["hypothesis identifier, namespace, version, predecessor and lifecycle state", "natural-language and formal proposition, language, terms and logic profile", "kind, population, unit, variables, relationship, conditions, boundary and exclusions"]},
            {"id": f"{fid}-q02", "text": f"Who proposed, owns, operationalizes, evaluates, reviews, corrects or discloses {lower}, and under which authority?", "kind": kinds[1], "answer_data": ["proposer, owner, investigator, analyst, reviewer, steward and disclosure roles", "rationale, assumption, preregistration, protocol, deviation, assessment and correction authority", "source system, timestamp, conflict declaration, ethics, consent, access and retention basis"]},
            {"id": f"{fid}-q03", "text": f"Which predictions, criteria, evidence, uncertainty, competing assessments, lineage and interoperability limits qualify {lower}?", "kind": kinds[2], "answer_data": ["operational definition, predicted observation, potential falsifier and evaluation criteria", "study, test, dataset, result, evidence, effect, uncertainty and source-qualified assessment", "conflict, inconclusive state, correction, successor, profile mapping and semantic-loss declaration"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed hypothesis-scoped values and references required to answer the governed questions for {lower}.", "value_kind": "object", "cardinality": "1", "required": True, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-artifact", "name": f"{name} evidence manifest", "description": f"Digest-addressed manifest of propositions, operationalizations, sources, protocols, predictions, results, assessments, conflicts and corrections supporting {lower}.", "media_or_form": ["application/json", "application/yaml", "text/markdown", "external reference"], "serial": True, "identity_strategy": "Authoritative hypothesis, registry or source-system record identifier first, otherwise governed IRI, then Dimension UUID or ULID; include immutable revision and digest.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


BASE.SOURCES = SOURCES
BASE.ROWS = ROWS
BASE.KIND_CYCLE = KIND_CYCLE
BASE.make_finding = make_finding


FUNCTION_ROWS = [
    ("register-hypothesis", "Register hypothesis", "Create one stable provisional-proposition identity and initial revision.", ["proposition", "owner", "source"], ["hypothesis identifier", "initial revision"], ["active Dimension", "create authority"], ["identity and explicit unknowns are appended"], ["SRC-010", "SRC-015", "SRC-020", "SRC-022", "SRC-023"]),
    ("formulate-proposition", "Formulate proposition", "Record natural-language and optional formal expressions with terminology and logic profile.", ["hypothesis revision", "expressions", "language"], ["versioned formulation"], ["terms and scope resolvable"], ["formulation history remains immutable"], ["SRC-012", "SRC-016", "SRC-019", "SRC-022"]),
    ("classify-and-scope", "Classify and scope hypothesis", "Assign hypothesis kind, domain, population, unit, variables, conditions and exclusions.", ["hypothesis revision", "kind", "scope"], ["typed scope profile"], ["classification authority"], ["kind and boundary are appended with source"], ["SRC-001", "SRC-003", "SRC-006", "SRC-013"]),
    ("record-rationale", "Record rationale and dependencies", "Bind motivation, assumptions, theory, priors, citations and prior evidence as external references.", ["hypothesis revision", "rationale", "dependencies"], ["rationale graph"], ["sources resolvable"], ["support and challenge remain independently qualified"], ["SRC-011", "SRC-014", "SRC-015", "SRC-016", "SRC-024"]),
    ("operationalize", "Operationalize hypothesis", "Define constructs, indicators, measures, estimands, predictions and potential falsifiers.", ["hypothesis revision", "operational definitions"], ["evaluation contract"], ["measurement profile known"], ["abstract and operational terms remain linked but distinct"], ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-013"]),
    ("preregister-evaluation", "Preregister evaluation", "Freeze protocol, outcomes, analysis criteria, timestamps and permitted deviations before results.", ["evaluation contract", "protocol", "registration authority"], ["preregistration reference", "digest"], ["prospective timing verified"], ["registered plan and later deviations remain auditable"], ["SRC-006", "SRC-008", "SRC-009", "SRC-011"]),
    ("bind-study-and-results", "Bind study and results", "Link external studies, tests, datasets, analyses, observations and results without importing their lifecycles.", ["hypothesis revision", "evaluation references"], ["typed evaluation bindings"], ["external identities resolvable"], ["scope and provenance are appended"], ["SRC-006", "SRC-007", "SRC-012", "SRC-013", "SRC-015"]),
    ("record-assessment", "Record assessment", "Append one source-qualified support, challenge, refutation or inconclusive assessment with uncertainty.", ["hypothesis revision", "results", "assessment method"], ["assessment assertion"], ["criteria and evidence known"], ["competing assessments remain visible"], ["SRC-001", "SRC-002", "SRC-007", "SRC-013", "SRC-014", "SRC-017"]),
    ("revise-supersede", "Revise or supersede", "Create a corrected, reformulated, split, merged or successor hypothesis without overwriting history.", ["current revision", "reason", "replacement"], ["successor revision", "difference trace"], ["revision authority"], ["prior proposition and assessments remain resolvable"], ["SRC-009", "SRC-015", "SRC-020", "SRC-021"]),
    ("project-hypothesis", "Project hypothesis view", "Produce minimum-necessary standards-aligned views with declared semantic loss.", ["hypothesis revision", "target profile", "purpose"], ["versioned projection", "semantic-loss declaration"], ["authorized recipient", "pinned target"], ["projection is logged and source identity preserved"], [f"SRC-{i:03d}" for i in range(1, 25)]),
]

BASE.FUNCTION_ROWS = FUNCTION_ROWS


def services():
    return {
        "dimension": {"owner_package_requirements": [
            "Declare the Dimension owner, hypothesis steward, knowledge owners, investigators, measurement authorities, reviewers and accountable decision roles.",
            "Register authoritative claim, assumption, theory, question, study, protocol, dataset, observation, result, evidence, citation, publication and decision masters.",
            "Publish hypothesis-kind, lifecycle, relation, evidence, assessment, uncertainty, access, retention, ethics and interoperability registries.",
            "Pin discipline, statistical, measurement, trial, ethics, jurisdiction, privacy, licensing and exchange profiles."],
            "namespace_guidance": "Mint hypothesis, revision, operationalization, assessment and projection identifiers only in the adopting Dimension namespace; preserve claim, assumption, theory, study, protocol, data, result, evidence, publication and decision identities as typed external references.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md", "Dimension-local hypothesis, relation, assessment, evidence, access, retention and provenance registries"]},
        "canon_and_patch": {"canonicalization_rules": [
            "Canonicalize by registry ID, model version, authoritative source identity, hypothesis kind, proposition revision, scope, owner and source profile; never use title, text hash, date or publication alone as identity.",
            "Keep hypothesis, question, assumption, prediction, theory, model, objective, requirement, generic claim, study, test, result, evidence, interpretation and decision distinct."],
            "patch_rules": ["Additive extensions use a Dimension-owned namespace and declare target node, discipline profile, authority, source, rationale, access, time and interoperability impact.", "Breaking changes require a new version, migration and crosswalk maps, compatibility declaration and continued resolution of prior hypothesis revisions and assessments."],
            "compatibility_rules": ["Consumers may ignore unknown additive fields only when identity, proposition, kind, scope, operationalization, criteria, state, provenance and access meaning remain intact.", "NIST, ISO, JCGM, trial-registry, OBI, STATO, ECO, W3C, DataCite, RO-Crate, Schema.org and FAIR mappings pin source and target versions and declare transformed, omitted or non-round-trippable values."]},
        "artifact_rules": {"identity_priority": ["Authoritative master-system identifier for the hypothesis and immutable proposition revision.", "Governed globally resolvable hypothesis or registration IRI.", "Adopting-Dimension UUID or ULID when no authoritative external identifier exists."],
            "timestamp_rule": "Record event timestamps in RFC 3339 with seconds and an explicit UTC offset or Z; keep proposal, registration, protocol, study, observation, analysis, assessment, review, correction and ingestion times distinct.",
            "serial_naming_rule": "Name serial artifacts as {hypothesis-id}--{artifact-kind}--{revision-or-assessment-id}; never use a date, title, author, p-value, filename or hash alone as identity.",
            "integrity_rule": "Store digest, media type, byte length, issuer, source and vocabulary versions, proposition and evaluation scope, clocks, provenance, uncertainty, assurance, license and access marking for each retained serial artifact."},
        "policies": [
            "The adopting Dimension declares who may propose, formulate, classify, operationalize, preregister, evaluate, review, revise, disclose, retain and tombstone hypotheses.",
            "Every assertion requires hypothesis identity and revision, kind, proposition, scope, source, authority, state, evidence, uncertainty and lineage as applicable.",
            "Agents never infer global truth, causality, practical significance, safety, compliance or decision authority from a p-value, interval, Bayes factor, citation count, peer review, result or status alone.",
            "Claims, assumptions, theories, questions, studies, tests, data, observations, results, evidence, publications and decisions remain external masters.",
            "Automated agents may append low-risk formulations, links, validations and projections under delegation, but human-subject decisions, protected disclosure, publication claims and irreversible deletion require accountable authority."],
        "crud": {"read": ["Resolve active Dimension, purpose, role, requested revision, hypothesis kind, scope, evaluation horizon, assurance, freshness, license and access policy; return the minimum permitted projection."],
            "create": ["Create stable identity, kind, proposition, scope, owner, source and explicit unknowns before adding evaluation or truth-related assertions."],
            "update": ["Append an immutable formulation, scope, operationalization, registration, assessment, review or correction revision with actor, authority, reason, RFC 3339 effective time and predecessor."],
            "delete": ["Apply ethics, privacy, dispute, audit, retention and legal-hold policy; tombstone eligible Hypothesis-owned records or withdraw projections while preserving identity, material provenance and non-cascading external references."]},
        "roles": [
            {"name": "Dimension owner", "responsibilities": ["Own namespace, mastership, delegation, access, retention and federation rules."]},
            {"name": "Hypothesis steward", "responsibilities": ["Own hypothesis identity, kind, formulation, lifecycle and revision policy."]},
            {"name": "Proposer or investigator", "responsibilities": ["Own formulation, rationale, assumptions, scope and declared conflicts."]},
            {"name": "Method or measurement steward", "responsibilities": ["Own operational definitions, measures, instruments, protocols and quality assertions."]},
            {"name": "Analyst or evaluator", "responsibilities": ["Own analysis method, result interpretation, uncertainty and assessment assertion."]},
            {"name": "Independent reviewer", "responsibilities": ["Review scope, preregistration, deviations, evidence, bias, conflicts and corrections without rewriting originals."]},
            {"name": "Ethics or data steward", "responsibilities": ["Own consent, privacy, confidentiality, data use and retention constraints."]},
            {"name": "Disclosure authority", "responsibilities": ["Approve recipient, purpose, redaction, publication claim and timing."]}],
        "access": {"default_rule": "Deny mutation and sensitive disclosure unless active Dimension, role, purpose, research sensitivity, consent, license and field policy grant the action; expose the minimum necessary projection.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Emergency or legally compelled access must be grounded, time-limited, purpose-bound, attributable, independently reviewed and unable to erase immutable hypothesis, assessment, correction or legal-hold evidence."], "audit_requirements": ["Log actor, role, purpose, hypothesis and revision identity, action, decision, policy and vocabulary versions, RFC 3339 timestamp with offset, affected fields, source evidence and outcome for privileged mutation or disclosure."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"], "read_order": ["Read the nearest Dimension-owner AGENTS.md, hypothesis and evidence authorities, active discipline, ethics, jurisdiction, time, access, retention and licensing policies.", "Read this model AGENTS.md, pinned spec.yaml and required claim, assumption, theory, study, protocol, data, result, evidence, publication and decision instructions before mutation."]}
    }


def coverage():
    return {
        "claim": "Source-grounded reviewable draft covering Hypothesis identity, formulation, classification, scope, variables, rationale, assumptions, operationalization, predictions, criteria, evaluation, assessment, uncertainty, lifecycle, governance and interoperability.", "confidence": "medium",
        "checklist": [
            {"dimension": "identity", "status": "covered", "notes": "Hypothesis, formulation revision, registration, assessment and successor identities remain distinct."},
            {"dimension": "classification and definition", "status": "covered", "notes": "Scientific, statistical, causal, descriptive, predictive, null, alternative and other profiles are explicit."},
            {"dimension": "direct properties", "status": "covered", "notes": "Proposition, language, logic, scope, variables, conditions, predictions, criteria and state are covered."},
            {"dimension": "recognition and observation", "status": "covered", "notes": "Operational definitions, measures, observations, results and assessments remain independently identified."},
            {"dimension": "lifecycle", "status": "covered", "notes": "Proposed, registered, under-test, evaluated, supported, unsupported, refuted, inconclusive, revised and withdrawn states preserve history."},
            {"dimension": "relationships", "status": "covered", "notes": "Questions, assumptions, theories, studies, protocols, data, results, evidence, publications and decisions use typed references."},
            {"dimension": "temporal", "status": "covered", "notes": "Proposal, registration, protocol, study, observation, analysis, assessment, review and correction clocks remain distinct."},
            {"dimension": "spatial", "status": "covered", "notes": "Population, setting, jurisdiction, study location and applicability region are explicit when relevant."},
            {"dimension": "provenance", "status": "covered", "notes": "Proposers, sources, rationale, methods, registrations, deviations, results, reviews and revisions are linked."},
            {"dimension": "ownership", "status": "covered", "notes": "Intellectual contribution, record stewardship, data ownership and decision authority are not conflated."},
            {"dimension": "validation", "status": "covered", "notes": "Identity, formulation, scope, operationalization, criteria, evidence, uncertainty, lineage and crosswalk checks are explicit."},
            {"dimension": "access", "status": "covered", "notes": "Role, purpose, consent, confidentiality, openness, minimum projection and audit are represented."},
            {"dimension": "retention and deletion", "status": "covered", "notes": "Corrections, disputes, retractions, audit or legal hold, withdrawal and tombstones are non-cascading."},
            {"dimension": "interoperability", "status": "covered", "notes": "Statistical, trial, ontology, research-object, provenance and metadata mappings disclose loss."},
            {"dimension": "capabilities and possible actions", "status": "covered", "notes": "Registration, formulation, scoping, operationalization, preregistration, evaluation, assessment, revision and projection declare controlled effects."}],
        "known_omissions": ["Discipline, study-design, statistical, Bayesian, causal-inference, machine-learning, ethics, jurisdiction, privacy, licensing and retention profiles require expert review.", "Claims, assumptions, theories, questions, studies, protocols, tests, datasets, observations, results, evidence, publications and decisions remain neighboring masters.", "Automated experiment design, causal identification, power calculation, model selection, evidence grading, replication scoring and truth adjudication remain future work."],
        "conflicts": ["Scientific disciplines use hypothesis, proposition, conjecture, model and prediction differently; the model requires explicit kind and profile.", "Null-hypothesis significance testing, confidence intervals, Bayesian evidence, likelihood and qualitative corroboration cannot share one universal acceptance rule.", "Supported, not rejected, corroborated, replicated, practically important, causal and true are different governed assessments."],
        "regional_assumptions": ["ClinicalTrials.gov and WHO are health-research profiles rather than universal hypothesis registries.", "OBI, STATO and ECO are strong scientific ontologies with biomedical roots and do not define all disciplinary practice.", "Ethics, consent, ownership, publication, retention and legal consequences depend on discipline, institution and jurisdiction."],
        "adversarial_checks": ["Reject a hypothesis without stable identity, revision, proposition, kind, scope, source, owner and lineage.", "Reject a question, assumption, theory, prediction, objective, requirement, study, result, evidence or decision represented as the hypothesis itself.", "Reject a statistical assessment without method, estimand, data scope, criteria, uncertainty and multiplicity context.", "Reject non-rejection of a null as proof of the null or statistical significance as practical importance, causality or truth.", "Reject preregistration inferred after results or deviations erased from history.", "Reject last-write-wins when studies or reviewers disagree; preserve source-qualified assessments and uncertainty.", "Reject protected disclosure, research participation, publication claims or record destruction outside delegated authority."]
    }


def build():
    model = {"registry_id": "vr.wm-knw-009", "model_id": "WM-KNW-009", "name": "Hypothesis", "entry_kind": "entity",
        "purpose": "Represent a versioned provisional proposition with explicit scope, operationalization, predictions, evaluation criteria and source-qualified assessment and revision history.",
        "scope_statement": "Owns hypothesis identity and revision; proposition expressions; hypothesis kind and profile; subject domain, population, unit, variables, relationships, conditions and boundary; proposer, owner, source, motivation, rationale, assumptions and prior-evidence references; operational definitions, measures, estimands, predictions, falsifiers and criteria; preregistration and deviations; study, test, dataset, analysis, result and evidence references; source-qualified assessments, uncertainty, conflicts, review, correction, lifecycle, access, retention and loss-aware projections. Generic claims, assumptions, theories, questions, studies, protocols, tests, data, observations, results, evidence, citations, publications, people, organizations, decisions and policies remain external masters.",
        "in_scope": ["Hypothesis identity, formulation, kind, scope, variables, conditions, revision and successor lineage", "Rationale, assumptions, prior evidence, operationalization, predictions, criteria, preregistration and evaluation bindings", "Assessment, uncertainty, conflict, lifecycle, provenance, governance, access, retention and interoperability"],
        "out_of_scope": ["Owning generic claim, assumption, theory, question, study, protocol, test, dataset, observation, result, evidence, citation, publication, party, decision or policy lifecycles", "Equating hypothesis with question, assumption, prediction, theory, model, objective, requirement, result or truth, or equating non-rejection, statistical significance, practical importance, causality and truth", "Executing research participation, experiments, protected-data access, publication, policy decisions, external system mutation or irreversible deletion"],
        "boundary_notes": [
            {"neighbor": "WM-KNW-007 Claim / Proposition", "distinction": "Hypothesis specializes a proposition as provisional and evaluable through scope, predictions and criteria. Generic claim identity and assertion lifecycle remain external; the candidate parent signal is held for review.", "source_refs": ["SRC-015", "SRC-016", "SRC-022"]},
            {"neighbor": "WM-KNW-016 Assumption", "distinction": "An assumption is a premise accepted for a bounded purpose. A hypothesis is proposed for evaluation; assumptions it depends on remain separately identifiable.", "source_refs": ["SRC-001", "SRC-012", "SRC-015"]},
            {"neighbor": "Research question, theory, model and prediction", "distinction": "A question solicits an answer, a theory or model supplies explanatory structure and a prediction states an expected observation. The hypothesis links them without importing their identities.", "source_refs": ["SRC-010", "SRC-011", "SRC-012", "SRC-013"]},
            {"neighbor": "Study, protocol, test and preregistration", "distinction": "These define or execute an evaluation. The hypothesis records typed references, criteria and deviations but not operational study lifecycle.", "source_refs": ["SRC-006", "SRC-008", "SRC-009", "SRC-012"]},
            {"neighbor": "Result, evidence and assessment", "distinction": "Results and evidence are external records. The hypothesis owns source-qualified assessment links but no context-free truth flag.", "source_refs": ["SRC-001", "SRC-002", "SRC-007", "SRC-013", "SRC-014", "SRC-017"]},
            {"neighbor": "Decision and policy", "distinction": "An assessment may inform an external decision, but the accountable choice, policy, clinical action or regulatory consequence is not owned by the hypothesis.", "source_refs": ["SRC-006", "SRC-008", "SRC-018"]},
            {"neighbor": "Research object and publication", "distinction": "RO-Crate, DataCite and FAIR projections package or identify research outputs. They do not replace the hypothesis proposition, revision or evaluation semantics.", "source_refs": ["SRC-020", "SRC-021", "SRC-024"]}]}
    composition = [
        {"target": "WM-KNW-007 Claim / Proposition", "relation": "REFERENCE", "purpose": "Resolve the broader truth-apt proposition while the candidate parent relation remains under joint boundary review.", "required": True, "source_refs": ["SRC-015", "SRC-016", "SRC-022"]},
        {"target": "WM-KNW-016 Assumption and research-question, theory, model and prediction masters", "relation": "REFERENCE", "purpose": "Resolve premises and conceptual context without conflating them with the hypothesis.", "required": False, "source_refs": ["SRC-001", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-015"]},
        {"target": "Study, protocol, experiment, test, dataset, observation, result, evidence and publication masters", "relation": "REFERENCE", "purpose": "Resolve evaluation design, execution and evidence while preserving external lifecycle authority.", "required": False, "source_refs": ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-012", "SRC-014", "SRC-020", "SRC-021"]},
        {"target": "NIST statistics, ISO 3534-1 and JCGM VIM and GUM", "relation": "ALIGN", "purpose": "Project statistical-test, measurement and uncertainty semantics as pinned methods.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005"]},
        {"target": "ClinicalTrials.gov and WHO trial registration", "relation": "ALIGN", "purpose": "Project prospective health-study hypothesis, outcome, protocol and result views as domain profiles.", "required": False, "source_refs": ["SRC-006", "SRC-007", "SRC-008"]},
        {"target": "OSF preregistration, OECD Frascati and UNESCO Open Science", "relation": "ALIGN", "purpose": "Project registration, research-activity and transparent scientific-process context.", "required": False, "source_refs": ["SRC-009", "SRC-010", "SRC-011"]},
        {"target": "OBI, STATO and ECO", "relation": "ALIGN", "purpose": "Project investigation, statistical-method, evidence and conclusion vocabulary with domain caveats.", "required": False, "source_refs": ["SRC-012", "SRC-013", "SRC-014"]},
        {"target": "PROV-O, Web Annotation, DQV, ODRL and SHACL", "relation": "ALIGN", "purpose": "Project provenance, annotation, quality, access and graph-validation semantics.", "required": False, "source_refs": ["SRC-015", "SRC-016", "SRC-017", "SRC-018", "SRC-019"]},
        {"target": "DataCite 4.7, RO-Crate 1.3, Schema.org Claim and FAIR", "relation": "ALIGN", "purpose": "Project research-resource identity, packaging, claim discovery and reuse metadata.", "required": False, "source_refs": ["SRC-020", "SRC-021", "SRC-022", "SRC-024"]},
        {"target": "RFC 3339", "relation": "ALIGN", "purpose": "Project unambiguous proposal, registration, evaluation, review and correction clocks.", "required": False, "source_refs": ["SRC-023"]}]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": BASE.structure(), "functions": BASE.functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    (RUN / "codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
