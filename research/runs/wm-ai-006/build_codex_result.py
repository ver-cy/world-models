#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-AI-006."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T14:35:00Z"


def src(i, title, org, url, version, kind, relevance):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": 1,
        "accessed_at": AT, "relevance": relevance,
    }


SOURCES = [
    src(1, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)", "National Institute of Standards and Technology", "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10", "NIST AI 100-1, 26 January 2023; revision in progress at access", "public-authority", "Frames governed AI lifecycle risk, accountability, measurement and documentation."),
    src(2, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile", "National Institute of Standards and Technology", "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf", "NIST AI 600-1, July 2024", "public-authority", "Adds training-data, privacy, security, content provenance, pre-deployment testing, incident and environmental risk considerations for generative AI."),
    src(3, "Secure Software Development Practices for Generative AI and Dual-Use Foundation Models", "National Institute of Standards and Technology", "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf", "NIST SP 800-218A, July 2024", "public-authority", "Extends secure development practices to model, data, component and lifecycle evidence."),
    src(4, "Regulation (EU) 2024/1689 Artificial Intelligence Act", "European Union", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj", "13 June 2024 official journal text", "legislation", "Provides an EU legal profile for data governance, technical documentation, records, transparency, risk and general-purpose AI obligations."),
    src(5, "Regulation (EU) 2016/679 General Data Protection Regulation", "European Union", "https://eur-lex.europa.eu/eli/reg/2016/679/oj", "27 April 2016; applicable from 25 May 2018", "legislation", "Provides an EU privacy profile for lawful processing, purpose, minimization, rights, security and accountability."),
    src(6, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation 30 April 2013", "ontology", "Defines entities, activities, agents, derivation, association, attribution, revision and time for run lineage."),
    src(7, "OpenLineage Object Model", "OpenLineage", "https://openlineage.io/docs/spec/object-model/", "Specification 1.53.0 current at access", "schema", "Separates Job design, Run execution, Dataset and RunEvent identities and recommends UUIDv7 run identifiers."),
    src(8, "MLflow Tracking", "MLflow", "https://mlflow.org/docs/latest/ml/tracking/", "Latest first-party documentation at access", "first-party-doc", "Defines experiments, runs, parameters, metrics, timestamps, datasets and artifacts while keeping registered models distinct."),
    src(9, "ML Metadata", "TensorFlow", "https://www.tensorflow.org/tfx/guide/mlmd", "First-party documentation current at access", "first-party-doc", "Defines Artifact, Execution, Event and Context metadata for ML pipeline lineage."),
    src(10, "Kubeflow Trainer Overview", "Kubeflow", "https://www.kubeflow.org/docs/components/trainer/overview/", "Kubeflow Trainer 2.1.0 profile current at access", "first-party-doc", "Provides a bounded distributed training runtime profile with train jobs, runtime, initializer, trainer and resources."),
    src(11, "SLSA Terminology", "Open Source Security Foundation", "https://slsa.dev/spec/v1.1/terminology", "SLSA 1.1", "standard", "Defines artifact, build, builder, dependency and provenance concepts for generated model and container artifacts."),
    src(12, "Open Container Initiative Image Format Specification", "Open Container Initiative", "https://github.com/opencontainers/image-spec/tree/v1.1.1", "OCI Image Specification 1.1.1, 3 March 2025", "standard", "Provides a release-pinned container image manifest and digest profile for runtime environments."),
    src(13, "OpenTelemetry Specification", "OpenTelemetry", "https://opentelemetry.io/docs/specs/otel/", "Specification 1.60.0; semantic conventions 1.44.0 at access", "standard", "Provides versioned traces, metrics, logs, resources and context propagation for run telemetry."),
    src(14, "MLPerf Training", "MLCommons", "https://mlcommons.org/benchmarks/training/", "MLPerf Training v6.0 current at access", "first-party-doc", "Provides a bounded benchmark profile based on dataset, quality target and time-to-quality with official rules as source of truth."),
    src(15, "Software Carbon Intensity Specification", "Green Software Foundation", "https://sci.greensoftware.foundation/", "SCI 1.1.0", "standard", "Defines a method-bound carbon intensity rate using operational emissions, embodied emissions and functional unit."),
    src(16, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339, July 2002", "standard", "Defines interoperable timestamps with seconds and an explicit UTC relationship."),
    src(17, "Reproducibility", "PyTorch", "https://docs.pytorch.org/docs/2.14/notes/randomness.html", "PyTorch 2.14 documentation, updated 14 May 2026", "first-party-doc", "States that full reproducibility is not guaranteed across releases or platforms and documents bounded controls for randomness and nondeterminism."),
]


ROWS = [
    ("run-identity-objective-method-and-authority", "Run identity, objective, method and authority", "The run is one governed execution aggregate, not the experiment definition, data master or trained model master", [
        ("run-root-experiment-parent-and-definition", "Run root, experiment, parent and definition", ["SRC-006", "SRC-007", "SRC-008", "SRC-009"], [
            ("run-root-identity-namespace-owner-revision-and-current-head", "Run root identity, namespace, owner, revision and current head", "identity", True),
            ("experiment-parent-pipeline-job-definition-and-correlation-binding", "Experiment, parent, pipeline, job definition and correlation binding", "relationship", True),
        ]),
        ("objective-training-method-risk-and-authority", "Objective, training method, risk and authority", ["SRC-001", "SRC-002", "SRC-003", "SRC-004"], [
            ("task-objective-target-hypothesis-acceptance-and-stop-plan", "Task, objective, target, hypothesis, acceptance and stop plan", "requirement", True),
            ("pretraining-finetuning-adaptation-method-risk-profile-and-accountable-authority", "Pretraining, fine-tuning, adaptation method, risk profile and accountable authority", "classification", True),
        ]),
    ]),
    ("model-data-code-configuration-and-environment-bindings", "Model, data, code, configuration and environment bindings", "Immutable or version-qualified inputs must be resolvable without copying external masters into the run", [
        ("base-model-tokenizer-dataset-and-split-bindings", "Base model, tokenizer, dataset and split bindings", ["SRC-002", "SRC-004", "SRC-006", "SRC-008", "SRC-009"], [
            ("base-model-architecture-tokenizer-initialization-freeze-and-adapter-bindings", "Base model, architecture, tokenizer, initialization, freeze and adapter bindings", "composition", True),
            ("dataset-role-snapshot-mixture-split-transform-sampling-permission-and-quality", "Dataset role, snapshot, mixture, split, transform, sampling, permission and quality", "privacy", True),
        ]),
        ("code-parameters-dependencies-and-runtime-environment", "Code, parameters, dependencies and runtime environment", ["SRC-003", "SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-017"], [
            ("source-code-revision-entrypoint-configuration-hyperparameters-and-seeds", "Source code revision, entrypoint, configuration, hyperparameters and seeds", "provenance", True),
            ("packages-images-framework-compiler-driver-hardware-and-environment", "Packages, images, framework, compiler, driver, hardware and environment", "interoperability", True),
        ]),
    ]),
    ("orchestration-distributed-execution-resources-and-progress", "Orchestration, distributed execution, resources and progress", "Desired topology, observed allocation and execution events remain distinct", [
        ("topology-workers-stages-attempts-and-state", "Topology, workers, stages, attempts and state", ["SRC-007", "SRC-009", "SRC-010", "SRC-013"], [
            ("cluster-topology-workers-ranks-parallelism-and-communication-strategy", "Cluster topology, workers, ranks, parallelism and communication strategy", "composition", False),
            ("stage-task-attempt-state-transition-retry-resume-and-idempotency", "Stage, task, attempt, state transition, retry, resume and idempotency", "state", True),
        ]),
        ("progress-optimizer-resources-cost-and-environment", "Progress, optimizer, resources, cost and environment", ["SRC-002", "SRC-008", "SRC-010", "SRC-013", "SRC-014", "SRC-015"], [
            ("steps-epochs-batches-samples-tokens-optimizer-scheduler-and-precision", "Steps, epochs, batches, samples, tokens, optimizer, scheduler and precision", "measurement", True),
            ("requested-allocated-observed-compute-storage-network-cost-energy-and-emissions", "Requested, allocated and observed compute, storage, network, cost, energy and emissions", "measurement", False),
        ]),
    ]),
    ("checkpoints-metrics-validation-quality-and-safety", "Checkpoints, metrics, validation, quality and safety", "Progress evidence and evaluation evidence must not be collapsed into a release decision", [
        ("checkpoints-progress-metrics-and-selection", "Checkpoints, progress metrics and selection", ["SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-017"], [
            ("checkpoint-identity-step-digest-completeness-reason-retention-and-resume", "Checkpoint identity, step, digest, completeness, reason, retention and resume", "evidence", True),
            ("loss-metric-series-effective-parameters-selection-rule-and-observed-best", "Loss and metric series, effective parameters, selection rule and observed best", "quality", True),
        ]),
        ("validation-data-quality-privacy-and-safety-evidence", "Validation, data quality, privacy and safety evidence", ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-014"], [
            ("validation-split-evaluation-reference-leakage-contamination-and-generalization", "Validation split, evaluation reference, leakage, contamination and generalization", "validation", True),
            ("data-quality-bias-privacy-security-safety-red-team-and-incident-references", "Data quality, bias, privacy, security, safety, red-team and incident references", "security", True),
        ]),
    ]),
    ("outputs-lineage-reproducibility-and-outcome", "Outputs, lineage, reproducibility and outcome", "Produced candidates are external artifacts linked by derivation, not embedded model masters", [
        ("candidate-final-artifacts-and-derivation", "Candidate and final artifacts and derivation", ["SRC-003", "SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-012"], [
            ("candidate-output-final-selection-packaging-format-digest-and-signature", "Candidate output, final selection, packaging, format, digest and signature", "evidence", True),
            ("base-data-code-configuration-checkpoint-builder-and-artifact-derivation", "Base, data, code, configuration, checkpoint, builder and artifact derivation", "provenance", True),
        ]),
        ("reproducibility-nondeterminism-comparison-and-acceptance", "Reproducibility, nondeterminism, comparison and acceptance", ["SRC-001", "SRC-002", "SRC-004", "SRC-014", "SRC-017"], [
            ("replay-recipe-randomness-determinism-nondeterminism-and-environment-equivalence", "Replay recipe, randomness, determinism, nondeterminism and environment equivalence", "validation", True),
            ("baseline-comparison-outcome-quality-safety-compliance-publication-and-deployment-decision", "Baseline comparison, outcome, quality, safety, compliance, publication and deployment decision", "decision", True),
        ]),
    ]),
    ("failure-governance-access-retention-correction-and-projections", "Failure, governance, access, retention, correction and projections", "Failure and governance evidence must survive cleanup and remain successor-correctable", [
        ("failure-cancel-recovery-cleanup-and-records", "Failure, cancellation, recovery, cleanup and records", ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-010"], [
            ("warning-error-failure-early-stop-cancellation-root-cause-and-impact", "Warning, error, failure, early stop, cancellation, root cause and impact", "exception", True),
            ("recovery-rollback-cleanup-retention-legal-hold-disposition-and-proof", "Recovery, rollback, cleanup, retention, legal hold, disposition and proof", "retention", True),
        ]),
        ("access-correction-audit-and-interoperability", "Access, correction, audit and interoperability", ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"], [
            ("identity-secret-data-rights-role-purpose-access-audit-correction-and-current-head", "Identity, secret, data rights, role, purpose, access, audit, correction and current head", "access", True),
            ("mlflow-mlmd-openlineage-prov-kubeflow-slsa-oci-otel-mlperf-sci-projections", "MLflow, MLMD, OpenLineage, PROV, Kubeflow, SLSA, OCI, OpenTelemetry, MLPerf and SCI projections", "interoperability", False),
        ]),
    ]),
]

KINDS = ["identity", "classification", "relationship", "authority", "requirement", "constraint", "event", "temporal", "composition", "evidence", "ownership", "measurement", "exception", "provenance", "process", "validation", "privacy", "lifecycle", "quality", "security", "retention", "interoperability", "decision", "state"]


def finding(item, number, refs):
    fid, name, primary, required = item
    low = name.lower()
    kinds = [primary, KINDS[(number + 7) % len(KINDS)], KINDS[(number + 15) % len(KINDS)]]
    return {
        "id": fid,
        "name": name,
        "description": f"Records {low} as source-qualified training-run context while dataset, source code, base model, trained model artifact, evaluation, registry, deployment, secrets, policy and infrastructure masters remain external.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"What stable identity, version-qualified values, scope and explicit unknowns establish {low}?", "kind": kinds[0], "answer_data": ["identifiers and run scope", "version-qualified values and units", "unknown and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who may declare, execute, observe, review, correct or rely on {low}, under which authority and limits?", "kind": kinds[1], "answer_data": ["human, agent, service and owner roles", "authority, policy, purpose and limits", "review, exception and escalation path"]},
            {"id": f"{fid}-q03", "text": f"Which planned, event, effective, recorded, ingested and knowledge times apply to {low}, and which evidence supports them?", "kind": kinds[2], "answer_data": ["distinct run and knowledge times", "evidence, provenance and uncertainty", "successor correction and retention"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed data for {low} with run scope, source, authority, state, unit, time, evidence and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned training evidence for {low}.", "media_or_form": ["logical model-training assertion", "configuration, event, metric, checkpoint, lineage, governance or projection record"], "serial": True, "identity_strategy": f"Run ID plus independent assertion, event or artifact ID for {fid}; model name, dataset name, timestamp, metric value, checkpoint step and file path never identify a record alone.", "source_refs": refs}],
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
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified training-run context for {lname.lower()}.", "source_refs": refs, "findings": findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed training-run context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({ref for layer in layers for ref in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-training-run", "Register a model training or fine-tuning run", ["run identity", "experiment and job definition", "owner and authority"], ["stable run aggregate"], ["namespace, objective, method, inputs and accountability are resolvable"], ["a new immutable-head run is registered without copying external masters"], ["SRC-001", "SRC-006", "SRC-007", "SRC-008", "SRC-009"]),
    ("resolve-immutable-inputs", "Resolve immutable run inputs", ["run", "base model", "datasets", "code", "configuration"], ["validated version-qualified bindings"], ["identities, versions, digests, rights and availability pass"], ["input bindings are recorded without mutating source masters"], ["SRC-002", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-011"]),
    ("declare-method-objective-and-authority", "Declare method, objective and authority", ["run", "training method", "objective", "risk and approval profile"], ["governed execution plan"], ["acceptance, stop, privacy, security, cost and resource limits pass"], ["the planned method and accountable approvals become auditable"], ["SRC-001", "SRC-002", "SRC-003", "SRC-004"]),
    ("dispatch-and-bind-execution", "Record dispatch and bind execution", ["approved plan", "runtime", "topology", "resource request"], ["dispatch and execution binding"], ["delegated execution authority and environment constraints pass"], ["dispatch is recorded; this specification grants no autonomous compute allocation"], ["SRC-007", "SRC-009", "SRC-010", "SRC-013"]),
    ("record-progress-resources-and-telemetry", "Record progress, resources and telemetry", ["run", "stage and attempt events", "measurements"], ["ordered progress and resource history"], ["units, clocks, sampling, source and aggregation methods pass"], ["observations are appended without treating planned values as observed"], ["SRC-008", "SRC-009", "SRC-010", "SRC-013", "SRC-015", "SRC-016"]),
    ("checkpoint-resume-and-retry", "Checkpoint, resume and retry", ["run", "checkpoint candidate", "retry or resume request"], ["validated checkpoint binding and successor attempt"], ["completeness, digest, compatibility, authority and idempotency pass"], ["checkpoint and attempt histories remain independently reconstructable"], ["SRC-006", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-017"]),
    ("record-metrics-validation-and-safety-evidence", "Record metrics, validation and safety evidence", ["run", "metric series", "evaluation and review references"], ["source-qualified evidence bindings"], ["split role, method, units, comparator, leakage and review status pass"], ["evidence is recorded without making a release or deployment decision"], ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-014"]),
    ("finalize-cancel-fail-or-early-stop", "Finalize, cancel, fail or early-stop a run", ["run", "terminal event", "reason and authority"], ["terminal successor state"], ["state transition, outcome, evidence, cleanup and retention duties pass"], ["the run closes without deleting external inputs or outputs"], ["SRC-001", "SRC-002", "SRC-003", "SRC-007", "SRC-010"]),
    ("bind-and-select-produced-artifact", "Bind and select a produced model artifact", ["terminal or candidate run", "artifact references", "selection evidence"], ["typed produced and selected artifact bindings"], ["digest, provenance, packaging, evaluation and accountable selection pass"], ["external model artifacts are linked by derivation; registry and deployment remain separate"], ["SRC-003", "SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-014"]),
    ("correct-project-retain-disclose-and-audit", "Correct, project, retain, disclose and audit", ["run", "target profile", "access and records policy"], ["successor, projection, disclosure, tombstone or disposition event"], ["mapping versions, loss, privacy, hold, authority and idempotency pass"], ["run context stays reconstructable and explicit about current head and projection loss"], ["SRC-001", "SRC-003", "SRC-004", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-016"]),
]


def functions():
    return [{"id": row[0], "name": row[1], "description": f"Governed operation to {row[1].lower()} without autonomous training, resource acquisition, secret retrieval, privacy decision, release, deployment or destructive cleanup.", "inputs": row[2], "outputs": row[3], "preconditions": row[4], "effects": row[5], "source_refs": row[6]} for row in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner, accountable AI owner and training mandate", "Authoritative dataset, source code, base model, trained model, evaluation, registry, deployment, infrastructure, secret, policy, provenance, audit and record registries", "Approved task, training method, jurisdiction, data-rights, privacy, security, safety, quality, cost, energy, retention and interoperability profiles", "Role, delegation, approval, incident, release, deployment and agent-operation policies"],
            "namespace_guidance": "Mint run, stage, task, attempt, event, metric-series, checkpoint, candidate, correction, disclosure and projection IDs; preserve external model, dataset, code, artifact and infrastructure identifiers.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize one run by authoritative execution-system identifier and owning namespace; never by model name, dataset name, timestamp, metric or checkpoint path alone.", "Keep experiment definition, run execution, stage, attempt, checkpoint, dataset, source code, base model, produced model, evaluation, registry entry and deployment independently identifiable."],
            "patch_rules": ["Extensions declare task, method, framework, hardware, jurisdiction, rights, privacy, security, safety, cost, energy and interoperability effects.", "Released input, state, metric, checkpoint, outcome and lineage assertions are immutable; corrections create linked successors.", "Never silently change base model, dataset, code, configuration, method, evaluation, output, authority, privacy, security, retention or provenance."],
            "compatibility_rules": ["Ignore additive fields only when run identity, input and output bindings, method, state, source, authority, units, time, privacy and provenance survive.", "Every projection pins standard, implementation, schema, semantic convention, profile and mapping versions and declares information loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each run, attempt, checkpoint, metric series, event or output binding, qualified by issuer, namespace and record kind.", "Governed globally resolvable run IRI.", "Dimension UUID or ULID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish planned, submitted, queued, started, checkpointed, observed, stopped, completed, recorded, ingested and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {run-id}--{assertion-event-or-artifact-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, record kind, run and attempt scope, input and output versions, actor, event and knowledge times, units, privacy marking and provenance.",
        },
        "policies": ["The run does not own Dataset, Source Code, Base Model, Tokenizer, Trained Model Artifact, Evaluation, Registry, Deployment, Infrastructure, Secret, Policy, Provenance, Access Audit or Records masters.", "Desired configuration, requested resources, actual allocation, observed execution, measured result, interpretation and release decision are independently sourced assertions.", "A seed does not establish reproducibility across releases, platforms or hardware; claims require bounded environment and nondeterminism evidence.", "Agents cannot allocate unrestricted compute, expose secrets or protected data, waive rights, publish or deploy a model, or destroy data and artifacts outside explicit delegated authority."],
        "crud": {
            "read": ["Resolve purpose, current head, inputs, configuration, topology, attempts, progress, resources, checkpoints, metrics, outputs, lineage, outcome, access, retention and projection loss under the permitted view."],
            "create": ["Bind stable run identity, experiment or job definition, owner, objective, method, external inputs, source, authority, initial state and submission time before execution context."],
            "update": ["Append successor plan, state, resource, progress, metric, checkpoint, failure, output, correction and disclosure assertions with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply data-rights, privacy, security, legal-hold and adopting-Dimension records policy; retire or tombstone only the run assertion without cascading to external data, code, model or artifact masters, and let authoritative systems execute physical disposition."],
        },
        "roles": [
            {"name": "AI system owner and accountable deployer", "responsibilities": ["Own purpose, risk acceptance, release boundaries and accountable use of resulting artifacts."]},
            {"name": "Model or ML engineer", "responsibilities": ["Define method and configuration, execute within delegation and preserve reproducible evidence."]},
            {"name": "Data owner and data steward", "responsibilities": ["Authorize dataset versions, roles, rights, privacy, quality and permitted transformations."]},
            {"name": "Platform or infrastructure operator", "responsibilities": ["Provide approved runtime, resource, telemetry, isolation, secret and incident controls."]},
            {"name": "Independent evaluator, safety and security reviewer", "responsibilities": ["Review evaluation, abuse, privacy, security, safety and red-team evidence without becoming the run owner."]},
            {"name": "Model registry and release steward", "responsibilities": ["Validate artifact identity, provenance, approval and promotion into separate registry and deployment systems."]},
            {"name": "Privacy, legal and records steward", "responsibilities": ["Own lawful processing, intellectual-property, disclosure, correction, hold, retention and disposition profiles."]},
        ],
        "access": {
            "default_rule": "Deny training data content, personal data, secrets, proprietary code, weights, checkpoints, security findings and restricted metrics unless a purpose-bound policy permits the minimum necessary view.",
            "scopes": ["bundle", "layer", "finding", "artifact"],
            "exceptions": ["Declared incident response, audit, legal, subject-rights, security, safety or emergency access must cite authority, scope, purpose and time limit where applicable and must be logged."],
            "audit_requirements": ["Log actor, agent, role, purpose, run and attempt scope, operation, authority, policy, RFC 3339 time, affected fields, source revision and outcome without unnecessary secret or protected-data duplication."],
        },
        "agents_bootstrap": {
            "filename": "AGENTS.md",
            "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"],
            "read_order": ["Read Dimension AI, data, compute, privacy, security, safety, cost, retention and agent policies.", "Read this run and linked dataset, source code, base model, trained model, evaluation, registry, deployment, infrastructure, provenance and records models before mutation."],
        },
    }


def coverage():
    dims = ["identity", "classification and direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability", "authority and ethics"]
    return {
        "claim": "Covers one governed model training or fine-tuning execution aggregate from objective and immutable inputs through distributed progress, resources, checkpoints, evidence, outputs, lineage, terminal outcome, correction, retention and projections.",
        "confidence": "medium",
        "checklist": [{"dimension": d, "status": "covered", "notes": f"{d.capitalize()} is explicit; task, method, framework, hardware, data-rights, jurisdiction, evaluation, release-pinned mappings and independent review remain held where applicable."} for d in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "The relation-ledger edges WM-AI-006 REFERENCE WM-DAT-001 and WM-AI-006 PRODUCES WM-SFT-004 are candidates and grant no target ownership, mutation, release or cascade authority.", "Pretraining, supervised and preference fine-tuning, continual learning, distillation, adapter tuning and other methods require explicit profiles.", "NIST AI RMF 1.0 is under revision; this result pins the inspected 1.0 publication and does not predict the revision."],
        "conflicts": ["Experiment or job definition, run, stage, task, attempt and checkpoint are not interchangeable identities.", "Base model, trained candidate, selected model artifact, registry entry and deployment are separate lifecycle objects.", "Requested resources, actual allocation, observed use, invoice cost, energy and carbon estimates use different sources and measurement methods."],
        "regional_assumptions": ["Training data rights, privacy, intellectual property, security, safety, export, environmental reporting, records and high-risk AI obligations depend on jurisdiction, industry and use case.", "The EU AI Act and GDPR are European Union profiles; NIST publications are voluntary United States public-authority guidance unless adopted by policy or contract.", "MLflow, MLMD, OpenLineage, Kubeflow, SLSA, OCI, OpenTelemetry, MLPerf, SCI and PyTorch are versioned profiles, not universal lossless schemas."],
        "adversarial_checks": ["Reject a run without stable identity, owner, objective, method, immutable input references, source, authority, state, time and current head.", "Reject a training artifact whose base, data, code, configuration, builder, checkpoint and digest lineage cannot be reconstructed.", "Reject reproducibility claims based only on a random seed or a successful rerun on a different release, platform or hardware.", "Reject autonomous resource acquisition, protected-data access, secret disclosure, model publication, deployment or destructive cleanup without delegated authority.", "Reject benchmark, quality, safety, cost, energy or carbon claims without method, units, boundary, source, uncertainty and version-qualified evidence."],
    }


def build():
    model = {
        "registry_id": "vr.wm-ai-006", "model_id": "WM-AI-006", "name": "Model Training / Fine-tuning Run", "entry_kind": "aggregate",
        "purpose": "Represent one governed execution that transforms version-qualified model, data, code and configuration inputs into candidate model artifacts with reconstructable progress, resources, evidence, lineage and outcome.",
        "scope_statement": "Owns one model training or fine-tuning run identity; objective, method and authority; immutable bindings to base model, tokenizer, datasets, code, configuration and environment; topology, stages, attempts, progress, resources, checkpoints, metrics, validation and safety evidence; produced-artifact bindings, lineage, reproducibility limits, terminal outcome, access, correction, retention and projections. Dataset, source code, base model, trained model artifact, evaluation, registry, deployment, infrastructure, secret, policy, provenance, audit and records masters remain external.",
        "in_scope": ["Run identity, experiment and job bindings, objective, method, risk, authority, input versions, configuration, environment, topology, stages, attempts and progress", "Resources, costs, energy, checkpoints, metrics, validation and safety references, candidates, derivation, reproducibility, outcome, access, correction, retention and projections"],
        "out_of_scope": ["Creating or mutating external dataset, code, base-model, trained-model, evaluation, registry, deployment, infrastructure, secret, policy, provenance, audit or records masters", "Equating a run with an experiment, checkpoint, trained model, registry entry or deployment, or equating requested resources with observed use", "Autonomous training, unrestricted compute allocation, protected-data or secret access, privacy or rights waiver, release, deployment or destructive cleanup"],
        "boundary_notes": [
            {"neighbor": "WM-DAT-001 Dataset", "distinction": "The candidate REFERENCE relation binds version-qualified dataset roles, splits, permissions and transformations. Dataset content, rights and lifecycle remain external.", "source_refs": ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-009"]},
            {"neighbor": "WM-SFT-004 produced model artifact", "distinction": "The candidate PRODUCES relation records derivation and candidate selection. The artifact master, registry promotion, release and deployment remain external.", "source_refs": ["SRC-003", "SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-012"]},
            {"neighbor": "Experiment, pipeline, job, stage, task, attempt and checkpoint", "distinction": "The run is one execution aggregate; reusable definitions and independently addressable execution children retain distinct identities and provenance.", "source_refs": ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010"]},
            {"neighbor": "AI evaluation, model registry and deployment", "distinction": "The run may reference evaluations and emit candidates, but evaluation conclusions, promotion decisions, registry state and deployment state are external authorities.", "source_refs": ["SRC-001", "SRC-002", "SRC-004", "SRC-008", "SRC-014"]},
            {"neighbor": "Infrastructure, telemetry, cost and environmental systems", "distinction": "External systems own allocation, billing, energy and carbon records. The run stores method-bound requested, allocated and observed references and summaries.", "source_refs": ["SRC-010", "SRC-013", "SRC-015"]},
            {"neighbor": "MLflow, MLMD, OpenLineage, PROV, Kubeflow, SLSA, OCI, OpenTelemetry, MLPerf, SCI and PyTorch", "distinction": "These are versioned experiment, metadata, lineage, runtime, provenance, packaging, telemetry, benchmark, carbon and framework profiles. No mapping is universally applicable or assumed lossless.", "source_refs": ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-017"]},
        ],
    }
    composition = [
        {"target": "WM-DAT-001 Dataset", "relation": "REFERENCE", "purpose": "Bind candidate training, validation, evaluation and auxiliary dataset snapshots without owning their content, rights or lifecycle.", "required": True, "source_refs": ["SRC-002", "SRC-004", "SRC-005", "SRC-006", "SRC-008", "SRC-009"]},
        {"target": "WM-SFT-004 produced model artifact", "relation": "REFERENCE", "purpose": "Represent the candidate PRODUCES ledger edge by a non-owning output reference and derivation record, without granting registry, release, deployment or cascade authority.", "required": False, "source_refs": ["SRC-003", "SRC-006", "SRC-008", "SRC-009", "SRC-011", "SRC-012"]},
        {"target": "Source code, base model, tokenizer, evaluation, registry, deployment, infrastructure, secret, policy, provenance, audit and records models", "relation": "REFERENCE", "purpose": "Resolve authoritative inputs, controls, evidence and lifecycle records without absorbing their ownership.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-003", "SRC-004", "SRC-006"]},
        {"target": "MLflow, MLMD, OpenLineage, PROV, Kubeflow, SLSA, OCI, OpenTelemetry, MLPerf, SCI and PyTorch", "relation": "ALIGN", "purpose": "Project version-pinned execution, lineage, packaging, telemetry, benchmark, environmental and reproducibility views with information-loss declarations.", "required": False, "source_refs": ["SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-014", "SRC-015", "SRC-017"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    RUN.joinpath("codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
