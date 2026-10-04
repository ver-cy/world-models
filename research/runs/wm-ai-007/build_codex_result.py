#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-AI-007."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T14:55:00Z"


def src(i, title, org, url, version, kind, relevance):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": 1,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)", "National Institute of Standards and Technology", "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10", "NIST AI 100-1, 26 January 2023; revision in progress at access", "public-authority", "Frames governed AI lifecycle risk, accountability, measurement and documentation."),
    src(2, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile", "National Institute of Standards and Technology", "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf", "NIST AI 600-1, July 2024", "public-authority", "Adds training-data, privacy, security, provenance, pre-deployment testing, incident and environmental considerations for generative AI."),
    src(3, "Secure Software Development Practices for Generative AI and Dual-Use Foundation Models", "National Institute of Standards and Technology", "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf", "NIST SP 800-218A, July 2024", "public-authority", "Extends secure development practices to model, data, component, provenance and release evidence."),
    src(4, "Regulation (EU) 2024/1689 Artificial Intelligence Act", "European Union", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj", "13 June 2024 official journal text", "legislation", "Provides an EU legal profile for technical documentation, records, transparency, risk and general-purpose AI obligations."),
    src(5, "Regulation (EU) 2016/679 General Data Protection Regulation", "European Union", "https://eur-lex.europa.eu/eli/reg/2016/679/oj", "27 April 2016; applicable from 25 May 2018", "legislation", "Provides an EU privacy profile for lawful processing, purpose, minimization, rights, security and accountability."),
    src(6, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation 30 April 2013", "ontology", "Defines entities, activities, agents, attribution, association, derivation, revision and time for registry lineage."),
    src(7, "Data Catalog Vocabulary (DCAT) Version 3", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dcat-3/", "W3C Recommendation 22 August 2024", "ontology", "Separates a catalog record from the cataloged resource and defines discoverability, version, distribution, rights and qualified relations."),
    src(8, "Model Registry Workflows", "MLflow", "https://mlflow.org/docs/latest/ml/model-registry/workflow/", "Latest first-party documentation at access; stages deprecated since 2.9.0", "first-party-doc", "Defines registered models, model versions, aliases, tags, source runs and access-controlled environments while deprecating fixed stages."),
    src(9, "Model Cards", "Hugging Face", "https://huggingface.co/docs/hub/model-cards", "Hub documentation current at access", "first-party-doc", "Defines discoverable model-card metadata for task, library, language, license, datasets, base model, evaluation and newer-version links."),
    src(10, "Model Cards for Model Reporting", "Google Research", "https://research.google/pubs/model-cards-for-model-reporting/", "2019 publication", "scientific", "Defines transparent model reporting for intended use, limitations, evaluation conditions and relevant subgroups."),
    src(11, "SPDX Specification AI Profile", "SPDX", "https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/", "SPDX 3.0.1", "standard", "Defines an AI profile for model and system packages with licensing, provenance, metrics, limitations and sensitive-information metadata."),
    src(12, "CycloneDX Bill of Materials Specification", "OWASP CycloneDX", "https://github.com/CycloneDX/specification", "CycloneDX 1.7, 21 October 2025", "standard", "Defines ML-BOM component, model-card, dataset, dependency, distribution, license, provenance and cryptographic-assurance views."),
    src(13, "SLSA Terminology", "Open Source Security Foundation", "https://slsa.dev/spec/v1.1/terminology", "SLSA 1.1", "standard", "Defines artifact, build, builder, dependency and provenance concepts for release integrity."),
    src(14, "OCI Distribution Specification", "Open Container Initiative", "https://github.com/opencontainers/distribution-spec/releases/tag/v1.1.1", "OCI Distribution Specification 1.1.1", "standard", "Defines a content-addressed registry distribution API and release-pinned artifact discovery profile."),
    src(15, "Verifying Signatures", "Sigstore", "https://docs.sigstore.dev/cosign/verifying/verify/", "Cosign first-party documentation current at access", "first-party-doc", "Defines bounded signature and identity verification for artifacts without equating a valid signature with model quality or safety."),
    src(16, "OpenLineage Object Model", "OpenLineage", "https://openlineage.io/docs/spec/object-model/", "Specification 1.53.0 current at access", "schema", "Separates Job, Run, Dataset and RunEvent identities for source training and lineage references."),
    src(17, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339, July 2002", "standard", "Defines interoperable timestamps with seconds and an explicit UTC relationship."),
]


ROWS = [
    ("registry-identity-scope-ownership-and-discovery", "Registry identity, scope, ownership and discovery", "A registry entry has its own governed identity and registration provenance distinct from the cataloged model resource", [
        ("entry-root-registry-scope-family-and-version", "Entry root, registry scope, family and version", ["SRC-006", "SRC-007", "SRC-008"], [
            ("entry-identity-registry-namespace-issuer-owner-revision-and-current-head", "Entry identity, registry namespace, issuer, owner, revision and current head", "identity", True),
            ("model-family-version-alias-canonical-uri-duplicate-and-equivalence", "Model family, version, alias, canonical URI, duplicate and equivalence", "relationship", True),
        ]),
        ("catalog-description-classification-and-stewardship", "Catalog description, classification and stewardship", ["SRC-001", "SRC-004", "SRC-007", "SRC-008", "SRC-009"], [
            ("title-summary-keywords-task-modality-language-domain-and-search-facets", "Title, summary, keywords, task, modality, language, domain and search facets", "classification", True),
            ("creator-provider-publisher-steward-contact-jurisdiction-and-attribution", "Creator, provider, publisher, steward, contact, jurisdiction and attribution", "ownership", True),
        ]),
    ]),
    ("model-artifact-technical-contract-and-compatibility", "Model artifact, technical contract and compatibility", "The entry binds immutable artifacts and technical claims without becoming their master", [
        ("artifact-release-packaging-and-integrity", "Artifact release, packaging and integrity", ["SRC-003", "SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015"], [
            ("artifact-reference-version-format-distribution-digest-size-and-signature", "Artifact reference, version, format, distribution, digest, size and signature", "evidence", True),
            ("architecture-base-model-tokenizer-framework-runtime-hardware-and-dependencies", "Architecture, base model, tokenizer, framework, runtime, hardware and dependencies", "composition", True),
        ]),
        ("interface-capability-intended-use-and-limits", "Interface, capability, intended use and limits", ["SRC-001", "SRC-002", "SRC-004", "SRC-009", "SRC-010", "SRC-011", "SRC-012"], [
            ("task-input-output-signature-modality-capability-and-behavior-contract", "Task, input, output, signature, modality, capability and behavior contract", "requirement", True),
            ("intended-supported-out-of-scope-prohibited-use-limitations-and-failure-modes", "Intended, supported, out-of-scope and prohibited use, limitations and failure modes", "constraint", True),
        ]),
    ]),
    ("development-lineage-rights-and-transparency", "Development lineage, rights and transparency", "Development evidence, rights and transparency documents remain source-qualified bindings", [
        ("training-data-code-build-and-supply-chain-lineage", "Training, data, code, build and supply-chain lineage", ["SRC-002", "SRC-003", "SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-016"], [
            ("training-run-dataset-code-configuration-build-builder-and-provenance", "Training run, dataset, code, configuration, build, builder and provenance", "provenance", True),
            ("developers-funders-contributors-tools-environment-and-source-documentation", "Developers, funders, contributors, tools, environment and source documentation", "ownership", False),
        ]),
        ("license-rights-distribution-and-transparency-documents", "License, rights, distribution and transparency documents", ["SRC-003", "SRC-004", "SRC-005", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-012"], [
            ("license-copyright-ownership-ip-data-rights-export-and-use-terms", "License, copyright, ownership, intellectual property, data rights, export and use terms", "authority", True),
            ("model-card-system-card-technical-documentation-disclosure-and-version", "Model card, system card, technical documentation, disclosure and version", "evidence", True),
        ]),
    ]),
    ("evaluation-risk-safety-security-and-approval", "Evaluation, risk, safety, security and approval", "Measured evidence, risk assessment and accountable approval are distinct assertions", [
        ("evaluation-benchmark-quality-and-comparability", "Evaluation, benchmark, quality and comparability", ["SRC-001", "SRC-002", "SRC-004", "SRC-009", "SRC-010", "SRC-011", "SRC-012"], [
            ("evaluation-dataset-task-metric-threshold-subgroup-robustness-and-result", "Evaluation dataset, task, metric, threshold, subgroup, robustness and result", "measurement", True),
            ("evidence-source-method-version-freshness-uncertainty-comparator-and-limit", "Evidence source, method, version, freshness, uncertainty, comparator and limit", "quality", True),
        ]),
        ("risk-control-review-and-accountable-decision", "Risk, control, review and accountable decision", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-010"], [
            ("risk-privacy-security-safety-bias-misuse-red-team-and-incident-reference", "Risk, privacy, security, safety, bias, misuse, red-team and incident reference", "security", True),
            ("reviewer-approval-rejection-exception-human-oversight-and-decision-evidence", "Reviewer, approval, rejection, exception, human oversight and decision evidence", "decision", True),
        ]),
    ]),
    ("lifecycle-promotion-publication-and-deployment-bindings", "Lifecycle, promotion, publication and deployment bindings", "Registry lifecycle must not collapse publication, deployability and observed deployment into one status", [
        ("entry-state-events-correction-and-supersession", "Entry state events, correction and supersession", ["SRC-001", "SRC-004", "SRC-006", "SRC-007", "SRC-008", "SRC-009"], [
            ("candidate-registered-reviewed-approved-published-deprecated-withdrawn-and-revoked", "Candidate, registered, reviewed, approved, published, deprecated, withdrawn and revoked", "lifecycle", True),
            ("transition-event-reason-authority-time-correction-merge-split-and-supersession", "Transition event, reason, authority, time, correction, merge, split and supersession", "event", True),
        ]),
        ("promotion-alias-release-and-deployment-observation", "Promotion, alias, release and deployment observation", ["SRC-001", "SRC-003", "SRC-004", "SRC-008", "SRC-014"], [
            ("promotion-gate-release-decision-alias-champion-channel-and-rollout-intent", "Promotion gate, release decision, alias, champion, channel and rollout intent", "authority", False),
            ("deployable-deployed-active-environment-endpoint-compatibility-and-observation", "Deployable, deployed, active, environment, endpoint, compatibility and observation", "state", False),
        ]),
    ]),
    ("distribution-access-retention-audit-and-projections", "Distribution, access, retention, audit and projections", "Discovery and distribution require purpose-filtered views, auditability and version-pinned mappings", [
        ("availability-distribution-access-and-use-signals", "Availability, distribution, access and use signals", ["SRC-005", "SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-014", "SRC-015"], [
            ("landing-page-api-package-oci-location-mirror-availability-and-access-tier", "Landing page, API, package, OCI location, mirror, availability and access tier", "access", True),
            ("weight-availability-download-use-adoption-popularity-staleness-and-observation", "Weight availability, download, use, adoption, popularity, staleness and observation", "measurement", False),
        ]),
        ("governance-records-audit-and-interoperability", "Governance, records, audit and interoperability", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017"], [
            ("role-purpose-access-disclosure-audit-retention-hold-tombstone-and-proof", "Role, purpose, access, disclosure, audit, retention, hold, tombstone and proof", "retention", True),
            ("dcat-mlflow-huggingface-spdx-cyclonedx-oci-slsa-prov-openlineage-projection", "DCAT, MLflow, Hugging Face, SPDX, CycloneDX, OCI, SLSA, PROV and OpenLineage projection", "interoperability", False),
        ]),
    ]),
]

KINDS = ["identity", "classification", "relationship", "authority", "requirement", "constraint", "event", "temporal", "composition", "evidence", "ownership", "measurement", "exception", "provenance", "process", "validation", "privacy", "lifecycle", "quality", "security", "retention", "interoperability", "decision", "state"]


def finding(item, number, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(number + 6) % len(KINDS)], KINDS[(number + 14) % len(KINDS)]]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {low} as source-qualified registry context while model artifact, training, dataset, code, evaluation, deployment, endpoint, policy, credential and audit masters remain external.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What stable identity, registry scope, version-qualified values and explicit unknowns establish {low}?", "kind": kinds[0], "answer_data": ["entry, registry and model identifiers", "version-qualified values and classifications", "unknown and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who may assert, review, approve, correct or rely on {low}, under which authority, purpose and limits?", "kind": kinds[1], "answer_data": ["creator, provider, publisher, steward and reviewer roles", "authority, policy, purpose and limits", "exception, contest and escalation path"]},
            {"id": f"{fid}-q03", "text": f"Which event, effective, observed, recorded, ingested and knowledge times apply to {low}, and which evidence supports them?", "kind": kinds[2], "answer_data": ["distinct lifecycle and knowledge times", "evidence, provenance and uncertainty", "successor correction and retention"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed data for {low} with entry scope, source, authority, state, time, evidence and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned registry evidence for {low}.", "media_or_form": ["logical AI model registry assertion", "identity, metadata, artifact, lineage, evaluation, approval, lifecycle, distribution or projection record"], "serial": True, "identity_strategy": f"Registry-entry ID plus independent assertion, decision, event or artifact ID for {fid}; model name, alias, version label, timestamp, URL and digest never identify a registry assertion alone.", "source_refs": refs}],
        "inline_only_rationale": None,
    }


def structure():
    bundles = []
    number = 0
    for bid, bname, rationale, layers in ROWS:
        rendered = []
        for lid, lname, refs, items in layers:
            findings = []
            for item in items:
                number += 1
                findings.append(finding(item, number, refs))
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified registry context for {lname.lower()}.", "source_refs": refs, "findings": findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed registry context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({ref for layer in layers for ref in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-model-entry", "Register an AI model entry", ["owning registry", "model family or artifact reference", "owner and authority"], ["stable registry entry"], ["namespace, scope, source, stewardship and duplicate checks pass"], ["a new entry head is created without copying or mutating the model artifact"], ["SRC-006", "SRC-007", "SRC-008"]),
    ("bind-family-version-and-artifacts", "Bind family, version and artifacts", ["entry", "model family", "model version", "artifact references"], ["version-qualified model bindings"], ["identifiers, digests, formats, provenance and compatibility pass"], ["external artifacts remain independently identifiable and immutable"], ["SRC-003", "SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]),
    ("describe-contract-use-and-limitations", "Describe contract, use and limitations", ["entry", "task", "input and output contract", "use assertions"], ["discoverable capability and limitation profile"], ["source, author, scope, version and evidence pass"], ["supported and prohibited use remain explicit claims rather than inferred permissions"], ["SRC-001", "SRC-002", "SRC-004", "SRC-009", "SRC-010"]),
    ("attach-lineage-rights-and-transparency", "Attach lineage, rights and transparency", ["entry", "training and build references", "rights", "documentation"], ["source-qualified lineage and disclosure bindings"], ["versions, issuers, legal scope, provenance and access pass"], ["the entry links evidence without replacing source masters or granting rights"], ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-016"]),
    ("attach-evaluation-risk-and-safety", "Attach evaluation, risk and safety evidence", ["entry", "evaluation results", "risk and control references"], ["bounded evidence profile"], ["method, dataset, metric, comparator, uncertainty, freshness and reviewer pass"], ["evidence is recorded without implying approval, publication or deployment"], ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-010"]),
    ("review-approve-reject-or-except", "Review, approve, reject or except", ["entry", "review packet", "accountable decision"], ["immutable decision assertion"], ["decision authority, criteria, conflicts, conditions and evidence pass"], ["the registry records the decision and conditions without autonomously making a high-impact approval"], ["SRC-001", "SRC-002", "SRC-004"]),
    ("publish-deprecate-withdraw-revoke-or-supersede", "Publish, deprecate, withdraw, revoke or supersede", ["entry", "authorized transition", "reason and successor"], ["successor lifecycle state"], ["prior state, authority, effective time, notifications and retention pass"], ["discoverability changes without deleting artifact, evidence or prior history"], ["SRC-004", "SRC-006", "SRC-007", "SRC-008", "SRC-009"]),
    ("bind-deployment-observations", "Bind deployment observations", ["entry", "environment and deployment references", "observation"], ["source-qualified deployment view"], ["deployment authority, source, environment, time and freshness pass"], ["deployed or active status remains external observation, not registry ownership"], ["SRC-001", "SRC-003", "SRC-004", "SRC-008"]),
    ("correct-merge-split-and-resolve-identity", "Correct, merge, split and resolve identity", ["entry heads", "evidence", "authorized correction plan"], ["successor entries and equivalence decisions"], ["expected revisions, affected assertions, redirects and audit pass"], ["prior assertions remain reconstructable and ambiguous equivalence stays contested"], ["SRC-006", "SRC-007", "SRC-008"]),
    ("query-project-disclose-retain-and-audit", "Query, project, disclose, retain and audit", ["entry", "query or target profile", "access and records policy"], ["filtered result, projection, disclosure, tombstone or audit event"], ["purpose, access, mapping version, loss, hold and idempotency pass"], ["registry context remains purpose-filtered, reconstructable and explicit about current head and loss"], ["SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017"]),
]


def functions():
    return [{"id": row[0], "name": row[1], "description": f"Governed operation to {row[1].lower()} without autonomous approval, publication, access expansion, signing, revocation, deployment, disclosure or destructive cleanup.", "inputs": row[2], "outputs": row[3], "preconditions": row[4], "effects": row[5], "source_refs": row[6]} for row in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner, registry mandate and accountable AI owner", "Authoritative model artifact, training, dataset, code, build, evaluation, deployment, endpoint, policy, credential, provenance, audit and records registries", "Approved model class, task, jurisdiction, data-rights, licensing, export, privacy, security, safety, quality, release, retention and interoperability profiles", "Role, delegation, approval, publication, revocation, incident, disclosure and agent-operation policies"],
            "namespace_guidance": "Mint registry, entry, family-binding, version-binding, alias, metadata, artifact-binding, evidence, review, decision, transition, correction, disclosure and projection IDs; preserve external model and evidence identifiers.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize one registry entry by authoritative registry identifier and namespace; never by display name, alias, version label, digest, URL, task or lifecycle status alone.", "Keep registry, entry, model family, model version, artifact, training run, evaluation, decision, deployment, endpoint and documentation independently identifiable."],
            "patch_rules": ["Extensions declare model class, task, modality, jurisdiction, rights, privacy, security, safety, quality, release and interoperability effects.", "Released artifact, evidence, approval and lifecycle assertions are immutable; corrections create linked successors.", "Never silently change model binding, digest, intended use, limitation, license, approval, publication, revocation, access, retention or provenance."],
            "compatibility_rules": ["Ignore additive fields only when entry identity, model and artifact bindings, source, authority, state, time, rights, access and provenance survive.", "Every projection pins standard, implementation, schema, vocabulary, profile and mapping versions and declares information loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each registry entry, assertion, decision, event or projection, qualified by issuer, namespace and record kind.", "Governed globally resolvable registry-entry IRI.", "Dimension UUID or ULID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish created, registered, reviewed, approved, published, deprecated, withdrawn, revoked, observed, recorded, ingested and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {entry-id}--{assertion-decision-event-or-artifact-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, record kind, registry and model scope, artifact and evidence versions, actor, event and knowledge times, access marking and provenance.",
        },
        "policies": ["The entry does not own Model Artifact, Training Run, Dataset, Source Code, Build, Evaluation, Deployment, Endpoint, Model Card, Policy, Credential, Provenance, Access Audit or Records masters.", "Registered, reviewed, approved, published, deployable, deployed, active, deprecated, withdrawn and revoked are independent authority-qualified assertions.", "A digest or valid signature supports byte identity or signer evidence but does not prove safety, quality, ownership, authorization or fitness for use.", "Agents cannot approve, publish, sign, revoke, widen access, disclose restricted material, deploy or destroy records outside explicit delegated authority."],
        "crud": {
            "read": ["Resolve purpose, current head, family and version scope, artifact, contract, lineage, rights, evaluations, risk, approvals, lifecycle, deployment observations, access, retention and projection loss under the permitted view."],
            "create": ["Bind stable entry identity, owning registry, model family or artifact reference, owner, source, authority, initial state and registration time before catalog metadata."],
            "update": ["Append successor metadata, artifact, evidence, decision, lifecycle, deployment-observation, correction and disclosure assertions with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply rights, privacy, security, legal-hold and adopting-Dimension records policy; retire or tombstone only the registry entry without cascading to model, evidence or deployment masters, and let authoritative systems execute physical disposition."],
        },
        "roles": [
            {"name": "AI system owner and accountable deployer", "responsibilities": ["Own purpose, risk acceptance, release boundaries and accountable use of registered models."]},
            {"name": "Model provider or developer", "responsibilities": ["Supply version-qualified artifacts, technical contract, lineage, rights, use and limitation claims."]},
            {"name": "Registry owner and steward", "responsibilities": ["Own entry identity, duplicate resolution, metadata quality, lifecycle history, discoverability and projection integrity."]},
            {"name": "Independent evaluator, safety and security reviewer", "responsibilities": ["Review evaluation, abuse, privacy, security, safety and red-team evidence without becoming the artifact owner."]},
            {"name": "Release and approval authority", "responsibilities": ["Make attributable approval, exception, publication, withdrawal and revocation decisions within mandate."]},
            {"name": "Deployment and platform operator", "responsibilities": ["Provide source-qualified environment, deployment, endpoint, compatibility and observed-state references."]},
            {"name": "Legal, privacy and records steward", "responsibilities": ["Own license, data-rights, IP, export, disclosure, correction, hold, retention and disposition profiles."]},
        ],
        "access": {
            "default_rule": "Deny restricted weights, training data, source code, personal data, secrets, security findings, unpublished evaluations and confidential approvals unless a purpose-bound policy permits the minimum necessary view.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Declared incident response, audit, legal, subject-rights, security, safety or emergency access must cite authority, scope, purpose and time limit where applicable and must be logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, registry and entry scope, operation, authority, policy, RFC 3339 time, affected fields, source revision and outcome without unnecessary secret or restricted-artifact duplication."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read Dimension AI, registry, release, data-rights, privacy, security, safety, access, retention and agent policies.", "Read this entry and linked model artifact, training, dataset, code, evaluation, deployment, endpoint, provenance and records models before mutation."],
        },
    }


def coverage():
    dims = ["identity", "classification and direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability", "authority and ethics"]
    return {
        "claim": "Covers one governed AI model registry entry from registration and model binding through discoverable technical metadata, lineage, rights, evaluations, risk, approvals, lifecycle, deployment observations, access, correction, retention and projections.",
        "confidence": "medium",
        "checklist": [{"dimension": d, "status": "covered", "notes": f"{d.capitalize()} is explicit; model class, task, jurisdiction, rights, release-pinned mappings, provider-specific lifecycle and independent review remain held where applicable."} for d in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "The unified row parent_ids WM-SFT-004 has no frozen relation-ledger edge and grants no composition, ownership, mutation, release or cascade authority.", "Model registries differ on family, version, alias, environment, approval, deletion and access semantics and require explicit profiles.", "NIST AI RMF 1.0 is under revision; this result pins the inspected 1.0 publication and does not predict the revision."],
        "conflicts": ["Registry entry, model family, version, immutable artifact, model card, evaluation, deployment and endpoint are not interchangeable identities.", "Registered, approved, published, deployable, deployed, active, deprecated, withdrawn and revoked are not one universal lifecycle axis.", "Digest, signature, provenance, license, approval, quality, safety and fitness-for-use establish different claims."],
        "regional_assumptions": ["Technical documentation, data rights, privacy, intellectual property, export, security, safety, disclosure, retention and high-risk AI obligations depend on jurisdiction, industry and use case.", "The EU AI Act and GDPR are European Union profiles; NIST publications are voluntary United States public-authority guidance unless adopted by policy or contract.", "DCAT, MLflow, Hugging Face, SPDX, CycloneDX, OCI, SLSA, Sigstore, PROV and OpenLineage are versioned profiles, not universal lossless schemas."],
        "adversarial_checks": ["Reject an entry without stable registry identity, owning registry, model binding, owner, source, authority, lifecycle state, registration time and current head.", "Reject artifact identity based only on name, alias, URL or version label; require authoritative reference and digest where bytes are distributed.", "Reject safety, quality, ownership, authenticity or fitness claims inferred only from registration, popularity, digest, signature or deployment.", "Reject autonomous approval, publication, signature, revocation, access expansion, disclosure, deployment or destructive cleanup without delegated authority.", "Reject projection or import that collapses family, version, artifact, approval, publication and deployment states or hides information loss."],
    }


def build():
    model = {
        "registry_id": "vr.wm-ai-007", "model_id": "WM-AI-007", "name": "AI Model Registry Entry", "entry_kind": "registry",
        "purpose": "Represent one governed, discoverable registry record that binds an AI model family or version to artifacts, technical metadata, lineage, rights, evaluations, approvals, lifecycle and distribution views without absorbing their external masters.",
        "scope_statement": "Owns one registry-entry identity; owning registry, namespace, family and version bindings; catalog description, classifications and stewardship; artifact, technical-contract, lineage, rights, documentation, evaluation, risk, approval, lifecycle, promotion, deployment-observation, availability, access, correction, retention, audit and projection assertions. Model artifact, training run, dataset, source code, build, evaluation, deployment, endpoint, model card, policy, credential, provenance, audit and records masters remain external.",
        "in_scope": ["Entry identity, registry scope, family and version bindings, aliases, discovery metadata, stewardship, artifact and technical-contract references, lineage, rights and transparency", "Evaluation, risk, safety, security, approvals, lifecycle, promotion, deployment observations, availability, access, correction, retention, audit and projections"],
        "out_of_scope": ["Creating or mutating external model artifact, training, dataset, code, build, evaluation, deployment, endpoint, policy, credential, provenance, audit or records masters", "Equating registry entry with model artifact, model card, approval or deployment, or equating digest, signature or popularity with quality and safety", "Autonomous approval, publication, signing, revocation, access expansion, disclosure, deployment or destructive cleanup"],
        "boundary_notes": [
            {"neighbor": "WM-SFT-004 ML Model Artifact", "distinction": "The unified parent_ids value is an unapproved boundary signal because no relation-ledger edge exists. The entry may reference immutable artifacts but cannot own or mutate their bytes, provenance or lifecycle.", "source_refs": ["SRC-003", "SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]},
            {"neighbor": "WM-AI-006 Model Training / Fine-tuning Run", "distinction": "Training owns execution history. The registry entry stores source-qualified run, dataset, code and builder references and bounded lineage summaries.", "source_refs": ["SRC-003", "SRC-006", "SRC-013", "SRC-016"]},
            {"neighbor": "AI Model Evaluation", "distinction": "External evaluation masters own datasets, procedures, measurements and conclusions. The entry stores versioned evidence bindings, summaries and approval use.", "source_refs": ["SRC-001", "SRC-002", "SRC-004", "SRC-009", "SRC-010"]},
            {"neighbor": "Deployment and endpoint", "distinction": "Deployment systems own environment, rollout, endpoint and observed runtime state. The registry records source-qualified references and observations without treating approval or publication as deployment.", "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-008", "SRC-014"]},
            {"neighbor": "Model card, system card and technical documentation", "distinction": "These are versioned transparency artifacts or projections. The registry entry binds them and selected summaries but does not make every card the canonical record.", "source_refs": ["SRC-002", "SRC-004", "SRC-009", "SRC-010", "SRC-011", "SRC-012"]},
            {"neighbor": "DCAT, MLflow, Hugging Face, SPDX, CycloneDX, OCI, SLSA, Sigstore, PROV and OpenLineage", "distinction": "These are catalog, registry, card, BOM, distribution, provenance, verification and lineage profiles with different scopes. No mapping is universally applicable or assumed lossless.", "source_refs": ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]},
        ],
    }
    composition = [
        {"target": "WM-SFT-004 ML Model Artifact", "relation": "REFERENCE", "purpose": "Represent the unfrozen parent boundary as a non-owning artifact and version binding without composition, mutation, release or cascade authority.", "required": True, "source_refs": ["SRC-003", "SRC-006", "SRC-011", "SRC-012", "SRC-013", "SRC-014"]},
        {"target": "WM-AI-006 Model Training / Fine-tuning Run and AI Model Evaluation", "relation": "REFERENCE", "purpose": "Resolve authoritative development lineage and evaluation evidence without absorbing execution or measurement masters.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-006", "SRC-016"]},
        {"target": "Deployment, endpoint, dataset, code, build, policy, credential, provenance, audit and records models", "relation": "REFERENCE", "purpose": "Resolve authoritative lifecycle, control and evidence records without absorbing their ownership.", "required": False, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006"]},
        {"target": "DCAT 3, MLflow, Hugging Face, SPDX 3.0.1 AI, CycloneDX 1.7, OCI 1.1.1, SLSA 1.1, Sigstore, PROV-O and OpenLineage 1.53.0", "relation": "ALIGN", "purpose": "Project release-pinned catalog, registry, card, BOM, distribution, provenance, verification and lineage views with information-loss declarations.", "required": False, "source_refs": ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    RUN.joinpath("codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
