#!/usr/bin/env python3
"""Build the source-grounded Codex fallback for WM-ACT-053."""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
AT = "2026-09-06T11:05:00Z"


def src(i, title, org, url, version, kind, relevance, tier=1):
    return {
        "id": f"SRC-{i:03d}", "title": title, "organization": org,
        "url": url, "version_or_date": version, "source_type": kind,
        "primary_source": True, "authority_tier": tier, "accessed_at": AT,
        "relevance": relevance,
    }


SOURCES = [
    src(1, "PROV-DM: The PROV Data Model", "World Wide Web Consortium", "https://www.w3.org/TR/prov-dm/", "W3C Recommendation, 30 April 2013", "standard", "Defines entities, activities, agents, generation, use, derivation, attribution, association, delegation, invalidation and temporal constraints for execution provenance."),
    src(2, "PROV-O: The PROV Ontology", "World Wide Web Consortium", "https://www.w3.org/TR/prov-o/", "W3C Recommendation, 30 April 2013", "ontology", "Provides interoperable RDF terms for execution, input, output, agent, revision and derivation provenance."),
    src(3, "Data Catalog Vocabulary Version 3", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dcat-3/", "W3C Recommendation, 22 August 2024", "standard", "Defines dataset, distribution, data service, version and catalog metadata used only as external data-asset projections."),
    src(4, "Data on the Web Best Practices: Data Quality Vocabulary", "World Wide Web Consortium", "https://www.w3.org/TR/vocab-dqv/", "W3C Working Group Note, 15 December 2016", "ontology", "Provides quality measurement, metric, annotation, certificate and policy terms for source-qualified quality-result projections."),
    src(5, "OpenLineage Object Model", "OpenLineage Project", "https://openlineage.io/docs/spec/object-model/", "OpenLineage 1.53.0 at access", "schema", "Separates Job, Run and Dataset identities and represents runtime state updates, design-time metadata and extensible facets."),
    src(6, "OpenTelemetry Specification", "Cloud Native Computing Foundation OpenTelemetry Project", "https://opentelemetry.io/docs/specs/otel/", "OpenTelemetry 1.60.0; semantic conventions 1.44.0 at access", "standard", "Defines traces, metrics, logs, resources, instrumentation scope, schema URLs and versioned telemetry used as external observability evidence."),
    src(7, "CloudEvents Specification", "Cloud Native Computing Foundation", "https://github.com/cloudevents/spec/tree/ce@v1.0.2", "CloudEvents 1.0.2, released 6 February 2022", "standard", "Defines interoperable event identity, source, type, subject, time, data schema and content type for trigger and lifecycle event projections."),
    src(8, "Common Workflow Language Workflow Description", "Common Workflow Language Project", "https://www.commonwl.org/v1.2/Workflow.html", "CWL 1.2.1, approved 7 August 2020", "standard", "Defines vendor-neutral workflow graphs, steps, inputs, outputs, requirements, hints and execution semantics for versioned workflow-definition bindings."),
    src(9, "Workflow Execution Service API", "Global Alliance for Genomics and Health", "https://ga4gh.github.io/workflow-execution-service-schemas/", "WES 1.1.0, released 14 September 2023", "schema", "Defines a domain-specific API profile for submitting, monitoring, cancelling and obtaining logs and outputs from portable workflow runs."),
    src(10, "OGC API - Processes - Part 1: Core", "Open Geospatial Consortium", "https://docs.ogc.org/is/18-062r2/18-062r2.html", "OGC 18-062r2, version 1.0.0, 20 December 2021", "standard", "Defines process execution, job identity, accepted, running, successful, failed and dismissed states, status times, results, exceptions and dismissal for a geospatial processing API profile."),
    src(11, "Tasks", "Apache Software Foundation", "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html", "Apache Airflow 3.3.x stable documentation at access", "first-party-doc", "Separates DAG runs, task instances, data intervals, dependencies, states, retries, rescheduling, deferral and heartbeat timeouts for an implementation profile."),
    src(12, "Jobs", "Cloud Native Computing Foundation Kubernetes Project", "https://kubernetes.io/docs/concepts/workloads/controllers/job/", "Kubernetes documentation current at access", "first-party-doc", "Defines one-off task execution, completions, parallelism, retries, suspension and cleanup for a container-orchestration implementation profile."),
    src(13, "OCI Image Format Specification", "Open Container Initiative", "https://github.com/opencontainers/image-spec/tree/v1.1.1", "OCI Image Specification 1.1.1, released 3 March 2025", "standard", "Defines content-addressed image manifests, indexes, configurations, layers and descriptors for versioned runtime-image bindings."),
    src(14, "Security and Privacy Controls for Information Systems and Organizations", "National Institute of Standards and Technology", "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final", "NIST SP 800-53 Rev. 5 Release 5.2.0, 27 August 2025", "standard", "Provides configurable security, privacy, audit, access, integrity, contingency and system-use controls; deployment tailoring remains required."),
    src(15, "Regulation (EU) 2016/679 General Data Protection Regulation", "European Union", "https://eur-lex.europa.eu/eli/reg/2016/679/oj", "27 April 2016; applicable from 25 May 2018", "legislation", "Provides a European Union privacy and accountability profile for personal data in inputs, outputs, logs, traces and retained execution evidence."),
    src(16, "Date and Time on the Internet: Timestamps", "Internet Engineering Task Force", "https://www.rfc-editor.org/info/rfc3339/", "RFC 3339, July 2002", "standard", "Provides interoperable timestamps with seconds and explicit UTC relationship for scheduling, state transitions, observations and ingestion."),
    src(17, "OpenAPI Specification 3.1.1", "OpenAPI Initiative", "https://spec.openapis.org/oas/v3.1.1.html", "OpenAPI 3.1.1, 24 October 2024", "standard", "Defines HTTP API descriptions, operations, parameters, request bodies, responses and schemas for version-pinned execution-service projections."),
]


ROWS = [
    ("run-identity-definition-trigger-and-authority", "Run identity, definition, trigger and authority", "One execution must bind stable identity, an immutable definition revision and accountable trigger without absorbing the reusable pipeline or scheduler masters", [
        ("run-root-definition-version-and-parent-pipeline", "Run root, definition version and parent pipeline", ["SRC-001", "SRC-002", "SRC-005", "SRC-008", "SRC-009", "SRC-010"], [
            ("processing-run-root-identity-namespace-owner-status-and-lineage-head", "Processing run root identity, namespace, owner, status and lineage head", "identity", True),
            ("pipeline-job-workflow-definition-revision-code-location-and-parent-reference", "Pipeline, job, workflow definition, revision, code location and parent reference", "relationship", True),
        ]),
        ("trigger-schedule-request-priority-and-execution-authority", "Trigger, schedule, request, priority and execution authority", ["SRC-005", "SRC-007", "SRC-009", "SRC-010", "SRC-011", "SRC-014"], [
            ("trigger-kind-event-schedule-manual-request-source-correlation-and-deduplication", "Trigger kind, event, schedule, manual request, source, correlation and deduplication", "event", True),
            ("requester-operator-service-account-authorization-priority-policy-and-approval", "Requester, operator, service account, authorization, priority, policy and approval", "authority", True),
        ]),
    ]),
    ("inputs-parameters-code-environment-and-effective-interval", "Inputs, parameters, code, environment and effective interval", "Reproducibility depends on resolved immutable bindings rather than mutable names or the latest available data", [
        ("declared-resolved-and-consumed-inputs-parameters-and-secrets", "Declared, resolved and consumed inputs, parameters and secrets", ["SRC-001", "SRC-003", "SRC-005", "SRC-008", "SRC-009", "SRC-014"], [
            ("declared-input-dataset-version-partition-schema-contract-and-availability", "Declared input, dataset version, partition, schema, contract and availability", "requirement", True),
            ("resolved-parameter-configuration-secret-reference-consumed-value-and-redaction", "Resolved parameter, configuration, secret reference, consumed value and redaction", "security", True),
        ]),
        ("code-package-image-runtime-environment-and-data-interval", "Code, package, image, runtime environment and data interval", ["SRC-005", "SRC-008", "SRC-009", "SRC-011", "SRC-012", "SRC-013", "SRC-016"], [
            ("source-revision-build-package-image-digest-dependency-and-entrypoint", "Source revision, build, package, image digest, dependency and entrypoint", "provenance", True),
            ("runtime-platform-environment-region-clock-locale-effective-data-interval-and-watermark", "Runtime platform, environment, region, clock, locale, effective data interval and watermark", "temporal", True),
        ]),
    ]),
    ("graph-tasks-stages-attempts-resources-and-state", "Graph, tasks, stages, attempts, resources and state", "Execution structure must preserve task and attempt identity, causal dependencies, resources and every state transition", [
        ("task-stage-graph-dependencies-mapping-and-branching", "Task, stage, graph, dependencies, mapping and branching", ["SRC-001", "SRC-005", "SRC-008", "SRC-009", "SRC-011"], [
            ("task-stage-instance-definition-binding-dependency-branch-map-index-and-order", "Task, stage instance, definition binding, dependency, branch, map index and order", "composition", True),
            ("declared-graph-resolved-graph-dynamic-expansion-condition-skip-and-block", "Declared graph, resolved graph, dynamic expansion, condition, skip and block", "process", True),
        ]),
        ("attempt-dispatch-worker-compute-resource-and-state-transitions", "Attempt, dispatch, worker, compute resource and state transitions", ["SRC-005", "SRC-006", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-014"], [
            ("task-attempt-identity-sequence-dispatch-worker-host-container-resource-and-lease", "Task attempt identity, sequence, dispatch, worker, host, container, resource and lease", "identity", True),
            ("requested-queued-started-running-heartbeat-succeeded-failed-cancelled-timed-out-and-unknown", "Requested, queued, started, running, heartbeat, succeeded, failed, cancelled, timed out and unknown", "state", True),
        ]),
    ]),
    ("outputs-lineage-validation-quality-and-observability", "Outputs, lineage, validation, quality and observability", "A process outcome, output materialization, publication and data-quality assertion are separate claims supported by attributable evidence", [
        ("declared-materialized-published-outputs-and-lineage", "Declared, materialized, published outputs and lineage", ["SRC-001", "SRC-002", "SRC-003", "SRC-005", "SRC-008", "SRC-010"], [
            ("declared-output-dataset-artifact-schema-partition-destination-and-contract", "Declared output, dataset, artifact, schema, partition, destination and contract", "requirement", True),
            ("materialized-output-version-digest-size-row-count-publication-visibility-and-derivation", "Materialized output, version, digest, size, row count, publication, visibility and derivation", "provenance", False),
        ]),
        ("validation-data-quality-logs-metrics-traces-and-evidence", "Validation, data quality, logs, metrics, traces and evidence", ["SRC-004", "SRC-005", "SRC-006", "SRC-009", "SRC-010", "SRC-011", "SRC-014", "SRC-016"], [
            ("schema-contract-reconciliation-quality-rule-metric-threshold-result-and-waiver", "Schema, contract, reconciliation, quality rule, metric, threshold, result and waiver", "validation", False),
            ("log-metric-trace-span-event-evidence-source-scope-sampling-integrity-and-retention", "Log, metric, trace, span, event, evidence source, scope, sampling, integrity and retention", "evidence", False),
        ]),
    ]),
    ("failure-retry-recovery-backfill-replay-and-outcome", "Failure, retry, recovery, backfill, replay and outcome", "Failure handling must preserve original attempts and distinguish rerun intent, data interval, side effects, compensation and final outcome", [
        ("error-failure-classification-retry-checkpoint-and-recovery", "Error, failure classification, retry, checkpoint and recovery", ["SRC-001", "SRC-005", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-014"], [
            ("error-exception-exit-status-failure-domain-root-cause-evidence-and-impact", "Error, exception, exit status, failure domain, root cause, evidence and impact", "exception", False),
            ("retry-policy-attempt-backoff-checkpoint-resume-idempotency-and-side-effect", "Retry policy, attempt, backoff, checkpoint, resume, idempotency and side effect", "lifecycle", False),
        ]),
        ("backfill-replay-rerun-cancellation-compensation-and-outcome", "Backfill, replay, rerun, cancellation, compensation and outcome", ["SRC-001", "SRC-005", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-016"], [
            ("backfill-replay-rerun-recovery-predecessor-successor-trigger-and-data-interval", "Backfill, replay, rerun, recovery, predecessor, successor, trigger and data interval", "provenance", False),
            ("cancel-timeout-cleanup-rollback-compensation-partial-result-final-outcome-and-closure", "Cancel, timeout, cleanup, rollback, compensation, partial result, final outcome and closure", "lifecycle", False),
        ]),
    ]),
    ("governance-access-retention-correction-and-interoperability", "Governance, access, retention, correction and interoperability", "Safe agent use requires protected views, append-only corrections and profile-pinned projections that declare information loss", [
        ("ownership-access-privacy-retention-legal-hold-and-disposition", "Ownership, access, privacy, retention, legal hold and disposition", ["SRC-003", "SRC-006", "SRC-014", "SRC-015", "SRC-016"], [
            ("owner-steward-operator-subject-purpose-access-redaction-disclosure-and-audit", "Owner, steward, operator, subject, purpose, access, redaction, disclosure and audit", "privacy", True),
            ("retention-class-legal-hold-tombstone-disposition-cleanup-and-external-record-policy", "Retention class, legal hold, tombstone, disposition, cleanup and external record policy", "retention", True),
        ]),
        ("correction-projection-conformance-loss-and-agent-controls", "Correction, projection, conformance, loss and agent controls", ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-017"], [
            ("amend-correct-invalidate-supersede-current-head-reason-authority-and-lineage", "Amend, correct, invalidate, supersede, current head, reason, authority and lineage", "provenance", True),
            ("openlineage-prov-otel-cloudevents-cwl-wes-ogc-airflow-kubernetes-oci-projection-and-loss", "OpenLineage, PROV, OTel, CloudEvents, CWL, WES, OGC, Airflow, Kubernetes, OCI projection and loss", "interoperability", False),
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
        "description": f"Records {low} as source-qualified execution context while keeping reusable definitions, datasets, software, infrastructure, telemetry and records in their owning systems.",
        "source_refs": refs,
        "questions": [
            {"id": f"{fid}-q01", "text": f"Which stable identities, execution scope, source-qualified values and explicit unknowns establish {low}?", "kind": kinds[0], "answer_data": ["identifiers, class and execution scope", "source-qualified values and versions", "unknown and not-applicable states"]},
            {"id": f"{fid}-q02", "text": f"Who requests, authorizes, schedules, executes, owns, observes, validates or is affected by {low}, with which policy and limits?", "kind": kinds[1], "answer_data": ["actors, services and roles", "authority, policy and limits", "validation, review and exception path"]},
            {"id": f"{fid}-q03", "text": f"Which scheduled, requested, queued, dispatched, started, heartbeat, completed, observed, ingested and knowledge times apply to {low}, and how is it corrected?", "kind": kinds[2], "answer_data": ["distinct execution and observation times", "evidence, validation and uncertainty", "successor correction and retention"]},
        ],
        "data_elements": [{"id": f"{fid}-data", "name": f"{name} data", "description": f"Typed data for {low} with identity, execution scope, source, authority, state, event and knowledge times, evidence and provenance.", "value_kind": "collection", "cardinality": "1" if required else "0..n", "required": required, "source_refs": refs}],
        "artifacts": [{"id": f"{fid}-record", "name": f"{name} record", "description": f"Immutable or successor-versioned execution evidence for {low}.", "media_or_form": ["logical processing-run assertion", "binding, task, attempt, state, input, output, validation, lineage, telemetry, failure, recovery or projection record"], "serial": True, "identity_strategy": f"Run ID plus independent task, attempt, input, output, validation, lineage, telemetry or assertion ID for {fid}; job name, dataset name, date, state and retry number never identify a record alone.", "source_refs": refs}],
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
            rendered.append({"id": lid, "name": lname, "description": f"Groups source-qualified execution context for {lname.lower()}.", "source_refs": refs, "findings": findings})
        bundles.append({"id": bid, "name": bname, "description": f"Groups governed execution context for {bname.lower()}.", "rationale": rationale + ".", "source_refs": sorted({ref for layer in layers for ref in layer[2]}), "layers": rendered})
    return {"bundles": bundles}


FUNCTIONS = [
    ("register-processing-run", "Register processing run", ["definition reference", "trigger", "requester", "owner mandate"], ["run root and constituent slots"], ["stable identity, definition version, scope and authority pass"], ["one bounded execution is registered without starting it or asserting success"], ["SRC-001", "SRC-005", "SRC-009", "SRC-010"]),
    ("resolve-definition-inputs-and-environment", "Resolve definition, inputs and environment", ["run", "definition", "input selectors", "parameters", "runtime policy"], ["immutable execution binding"], ["versions, digests, data interval, secret references and access pass"], ["the run can be reproduced without absorbing external master lifecycles"], ["SRC-003", "SRC-005", "SRC-008", "SRC-009", "SRC-013", "SRC-014"]),
    ("authorize-and-dispatch", "Authorize and dispatch", ["resolved run", "operator", "compute target", "policy"], ["authorization and dispatch event"], ["delegation, environment, quota, priority, access and idempotency pass"], ["dispatch is recorded without asserting start or execution"], ["SRC-007", "SRC-009", "SRC-010", "SRC-012", "SRC-014"]),
    ("record-task-and-attempt-events", "Record task and attempt events", ["run", "resolved graph", "task and attempt observations"], ["task, stage, attempt and state history"], ["identity, dependency, sequence, worker, event time and source pass"], ["each attempt remains independently attributable and immutable"], ["SRC-001", "SRC-005", "SRC-006", "SRC-011", "SRC-012"]),
    ("record-input-consumption-and-output-materialization", "Record input consumption and output materialization", ["attempt", "input observations", "output observations"], ["consumption, generation and derivation links"], ["dataset versions, partitions, digests, schemas, times and visibility pass"], ["declared, consumed, materialized and published assets remain separate"], ["SRC-001", "SRC-002", "SRC-003", "SRC-005"]),
    ("record-validation-quality-and-observability", "Record validation, quality and observability", ["run or attempt", "rules", "logs", "metrics", "traces"], ["source-qualified evidence and results"], ["scope, method, metric, threshold, sampling, integrity and times pass"], ["process exit and data-quality assertions remain separate"], ["SRC-004", "SRC-005", "SRC-006", "SRC-014"]),
    ("record-failure-and-retry", "Record failure and retry", ["failed attempt", "error evidence", "retry policy"], ["failure classification and successor attempt"], ["policy, limit, backoff, idempotency, side effects and authority pass"], ["the failed attempt is preserved and never overwritten by retry"], ["SRC-005", "SRC-009", "SRC-010", "SRC-011", "SRC-012"]),
    ("cancel-recover-resume-or-compensate", "Cancel, recover, resume or compensate", ["active or failed run", "authorized action", "checkpoint and side effects"], ["lifecycle event and resulting state"], ["authority, current state, checkpoint, impact, cleanup and evidence pass"], ["cancellation or cleanup does not cascade-delete external records"], ["SRC-001", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-014"]),
    ("backfill-replay-rerun-and-close", "Backfill, replay, rerun and close", ["source run", "trigger", "data interval", "definition and input bindings"], ["successor run and qualified outcome"], ["reason, predecessor, versions, interval, side effects and closure criteria pass"], ["original execution and evidence remain reconstructable"], ["SRC-001", "SRC-005", "SRC-011", "SRC-016"]),
    ("correct-project-retain-disclose-and-audit", "Correct, project, retain, disclose and audit", ["run", "target profile", "access and records policy"], ["successor, projection, disclosure, tombstone or disposition event"], ["mapping versions, loss, privacy, hold, authority and idempotency pass"], ["context stays protected, reconstructable and explicit about current head and loss"], ["SRC-001", "SRC-002", "SRC-003", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-013", "SRC-014", "SRC-015", "SRC-016", "SRC-017"]),
]


def functions():
    return [{"id": row[0], "name": row[1], "description": f"Governed operation to {row[1].lower()} without autonomous execution, production mutation, secret access or mutation of external masters.", "inputs": row[2], "outputs": row[3], "preconditions": row[4], "effects": row[5], "source_refs": row[6]} for row in FUNCTIONS]


def services():
    return {
        "dimension": {
            "owner_package_requirements": ["Dimension owner and data-processing mandate", "Authoritative pipeline, job, workflow, schedule, dataset, data product, schema, contract, code, package, image, configuration, secret, identity, compute, log, metric, trace, incident, provenance, audit and record registries", "Approved environment, authorization, data classification, quality, runtime, retry, backfill, privacy, retention and interoperability profiles", "Execution, publication, secret-use, cancellation, cleanup, compensation, disclosure and agent-operation policies"],
            "namespace_guidance": "Mint run, task, stage, attempt, binding, state, validation, materialization, failure, recovery, correction, disclosure and event IDs; preserve authoritative external master and telemetry identifiers.",
            "registry_links": ["https://ver.cy/models/", "https://ver.cy/model-agent-protocol.md"],
        },
        "canon_and_patch": {
            "canonicalization_rules": ["Canonicalize each run and constituent by authoritative orchestrator or execution-system identifier, owning namespace and record kind; never by pipeline name, schedule, date, state or retry number alone.", "Keep reusable definition, run, task or stage instance, attempt, input binding, output materialization, quality result and telemetry evidence independently identifiable."],
            "patch_rules": ["Extensions declare processing domain, orchestrator, runtime, data, quality, observability, security, privacy, retention and interoperability effects.", "Released bindings, task and attempt events, materializations, validations, failures and outcomes are immutable; corrections create linked successors.", "Never silently change definition, code, input, parameter, secret reference, environment, data interval, state, result, output, error, authority or provenance."],
            "compatibility_rules": ["Ignore additive fields only when identity, execution scope, record kind, versions, source, authority, state, time, evidence and provenance survive.", "Every projection pins specification, orchestrator, workflow, runtime, schema, telemetry and code-list versions and declares information loss."],
        },
        "artifact_rules": {
            "identity_priority": ["Authoritative master-system identifier for each run, task, attempt, binding, materialization, validation or execution event, qualified by owning execution system and record kind.", "Governed globally resolvable processing-run IRI.", "Dimension UUID or ULID when neither preceding identifier exists."],
            "timestamp_rule": "Use RFC 3339 timestamps with seconds and explicit offset or Z; distinguish scheduled, requested, queued, dispatched, started, heartbeat, completed, cancelled, source event, output materialization, observation, ingestion and knowledge times whenever they differ.",
            "serial_naming_rule": "Use {run-id}--{task-attempt-binding-output-validation-or-assertion-id}--{artifact-kind}--{revision-id}.",
            "integrity_rule": "Store digest, media type, record kind, execution scope, definition and profile versions, actor, event and knowledge times, state, access marking and provenance."},
        "policies": ["The aggregate does not own Pipeline, Job Definition, Workflow Definition, Schedule, Dataset, Data Product, Schema, Data Contract, Code, Package, Image, Configuration, Secret, Identity, Compute Resource, Log, Metric, Trace, Incident, Provenance, Access Audit or Record masters.", "Requested, queued, dispatched, started, running, retrying, succeeded, failed, cancelled, timed out, skipped and unknown are source-qualified states with independent events.", "Successful process exit does not prove output publication, completeness, correctness, schema conformance, data quality, freshness or downstream use.", "Agents cannot execute, retry, cancel, publish, clean up, access secrets, disclose protected data or mutate production systems outside explicit delegated authority."],
        "crud": {
            "read": ["Resolve purpose, run head, definition and parent references, trigger, authority, immutable bindings, graph, tasks, attempts, states, resources, inputs, outputs, lineage, validations, telemetry, failures, recovery, holds and projection loss."],
            "create": ["Bind stable run and constituent identity, definition revision, trigger, requester, data interval, owner, source, state and event time before recording execution context."],
            "update": ["Append successor state, attempt, binding, materialization, validation, failure, recovery, outcome and correction events with reason, authority, expected revision, event time and knowledge time."],
            "delete": ["Apply data, privacy, security, observability, audit, legal-hold and adopting-Dimension retention policy; retire or tombstone only the run or named constituent without cascading to pipeline, dataset, software, infrastructure or telemetry masters, and let the external records policy execute physical disposition."],
        },
        "roles": [
            {"name": "Data processing owner", "responsibilities": ["Own execution purpose, service objectives, risk acceptance and accountable outcome interpretation."]},
            {"name": "Pipeline or workflow steward", "responsibilities": ["Own reusable definitions, versions, dependencies and approved execution profiles."]},
            {"name": "Data owner or product steward", "responsibilities": ["Own input and output assets, contracts, access, publication and retention decisions."]},
            {"name": "Execution operator or orchestrator", "responsibilities": ["Own authorized dispatch, state observation, retry, cancellation and recovery within policy."]},
            {"name": "Platform and compute steward", "responsibilities": ["Own runtime, capacity, isolation, resource and infrastructure evidence."]},
            {"name": "Data quality and validation steward", "responsibilities": ["Own rules, metrics, thresholds, results, waivers and qualified acceptance."]},
            {"name": "Observability and incident steward", "responsibilities": ["Own logs, metrics, traces, alerting, incident links, sampling and evidence integrity."]},
            {"name": "Security, privacy and records steward", "responsibilities": ["Own identities, secret policy, protected views, disclosure, holds, retention and auditability."]},
        ],
        "access": {"default_rule": "Deny inputs, outputs, parameters, secrets, logs and traces unless a purpose-bound policy permits the minimum necessary view.", "scopes": ["bundle", "layer", "finding", "artifact"], "exceptions": ["Declared operator, recovery, incident, audit, subject-rights, legal or emergency access must cite authority, scope, purpose and time limit where applicable and must be logged."], "audit_requirements": ["Log actor, agent, role, purpose, run and constituent, operation, authority, policy, RFC 3339 time, affected fields, source revision and outcome without duplicating secrets or protected data unnecessarily."]},
        "agents_bootstrap": {"filename": "AGENTS.md", "required_fields": ["Name", "Type", "Specification URL", "Storage type URL", "Interface URL", "Processes URL"], "read_order": ["Read Dimension execution, authorization, data, schema, quality, runtime, secret, privacy, access, correction, retention and agent policies.", "Read this aggregate and linked pipeline, workflow, dataset, software, compute, telemetry, incident, provenance and records models before mutation."]},
    }


def coverage():
    dims = ["identity", "classification and definition", "direct properties", "recognition and observation", "capabilities and possible actions", "composition", "lifecycle", "relationships", "temporal", "spatial", "provenance", "ownership and stewardship", "validation and quality", "access and privacy", "retention and deletion", "interoperability"]
    return {
        "claim": "Covers a source-qualified data-processing execution aggregate linking immutable definition and data bindings, trigger and authority, task and attempt structure, state, inputs and outputs, lineage, validation, quality, observability, failure, retry, recovery, backfill, correction, protected use and projection.",
        "confidence": "medium",
        "checklist": [{"dimension": dim, "status": "covered", "notes": f"{dim.capitalize()} is explicit; candidate containment, runtime profiles, domain semantics, release-pinned mappings and independent review remain held where applicable."} for dim in dims],
        "known_omissions": ["Claude and Grok each timed out on one bounded attempt; no independent external result was admitted.", "The only relation-ledger edge is candidate incoming WM-DAT-005 CONTAINS WM-ACT-053; it is not treated as approved composition or cascade authority.", "Batch, streaming, event, scientific, geospatial, machine-learning, ETL, ELT and transaction-processing executions require domain and runtime profiles.", "OpenLineage, OTel, Airflow, Kubernetes, OCI, WES and OGC materials have different technical or sector scopes and require release-pinned validation."],
        "conflicts": ["A reusable definition, run, task or stage instance, attempt, input binding, output materialization, validation result and telemetry observation are not interchangeable.", "Declared, resolved, consumed, materialized and published data states remain distinct.", "Successful process exit does not prove correct, complete, conformant, fresh, published or accepted output."],
        "regional_assumptions": ["Execution authority, data protection, cross-border processing, audit, retention and incident response depend on jurisdiction, organization and data classification.", "GDPR is a European Union legal profile, and NIST controls require deployment-specific tailoring.", "Orchestrator states, retry behavior, task identity, container semantics, quality rules, telemetry schemas and API behavior require versioned profiles."],
        "adversarial_checks": ["Reject a run or constituent without stable identity, definition revision, trigger, owner, source, state, event time and lineage head.", "Reject a retry or rerun that overwrites the original attempt, loses the effective data interval or silently changes code, inputs, parameters or environment.", "Reject a success claim inferred only from exit status when output materialization, publication, validation, quality and freshness remain unknown.", "Reject lineage that copies mutable dataset or software metadata without authoritative identifiers, versions, digests and source times.", "Reject autonomous execution, secret access, production mutation, destructive cleanup or protected disclosure outside explicit delegated authority."],
    }


def build():
    model = {
        "registry_id": "vr.wm-act-053", "model_id": "WM-ACT-053",
        "name": "Data Processing Job / Pipeline Run", "entry_kind": "aggregate",
        "purpose": "Represent one governed data-processing execution so agents can reconstruct what was requested, authorized, resolved, run, observed, produced and corrected without treating orchestration state as proof of data correctness or absorbing reusable definitions and data assets.",
        "scope_statement": "Owns one processing-run identity; immutable bindings to a parent pipeline or job definition, code, parameters, input versions, environment and effective data interval; trigger and execution authority; task, stage and attempt instances; state events; output materialization and lineage context; validation, quality and telemetry references; failure, retry, recovery, backfill, cancellation and correction lineage. Pipeline, job and workflow definitions, schedules, datasets, data products, schemas, contracts, code, packages, images, configurations, secrets, identities, compute resources, logs, metrics, traces, incidents, provenance, access audits and record masters remain external.",
        "in_scope": ["Run identity and immutable execution bindings; trigger, request and authority; resolved graph, tasks, stages, attempts, resources, state and times", "Input consumption and output materialization links; lineage, validation, data quality and observability references; failure, retry, recovery, backfill, correction, access, retention and projections"],
        "out_of_scope": ["Creating or changing reusable pipeline, workflow, schedule, dataset, schema, code, package, image, secret, identity, compute, telemetry, incident or records masters", "Equating dispatch with start, process exit with correct output, materialization with publication, or success with data quality and downstream acceptance", "Autonomous execution, retry, cancellation, production mutation, secret retrieval, destructive cleanup or protected disclosure"],
        "boundary_notes": [
            {"neighbor": "WM-DAT-005 Data Pipeline", "distinction": "The candidate incoming CONTAINS relation may bind this execution to a parent pipeline and runnable graph. This aggregate cannot own, edit or cascade-delete the reusable pipeline definition.", "source_refs": ["SRC-005", "SRC-008"]},
            {"neighbor": "Dataset, data product, schema and data contract models", "distinction": "External masters own data identity, content, schema, contract, publication and lifecycle. The run stores resolved version, partition, digest, role and source-qualified consumption or generation links.", "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005"]},
            {"neighbor": "Software, package, image, configuration, secret and compute models", "distinction": "External masters own artifacts, sensitive values and infrastructure lifecycle. The run binds immutable revisions, digests, entrypoints, secret references, resource observations and environment snapshots.", "source_refs": ["SRC-008", "SRC-012", "SRC-013", "SRC-014"]},
            {"neighbor": "Logs, metrics, traces, quality results and incidents", "distinction": "Observability and quality systems own evidence content and lifecycle. The run records typed links, scope, sampling, times, integrity and bounded interpretations.", "source_refs": ["SRC-004", "SRC-006", "SRC-011", "SRC-014"]},
            {"neighbor": "Run, task, stage, attempt and retry", "distinction": "The aggregate owns one run and its execution membership. Each task or stage instance and attempt has independent identity, sequence, environment, state events and outcome; retry never overwrites failure.", "source_refs": ["SRC-005", "SRC-009", "SRC-010", "SRC-011", "SRC-012"]},
            {"neighbor": "OpenLineage, PROV, OTel, CloudEvents, CWL, WES, OGC Processes, Airflow, Kubernetes and OCI", "distinction": "These are versioned lineage, telemetry, event, workflow, API, orchestrator and runtime projections with different scopes. No mapping is assumed lossless or universally applicable.", "source_refs": ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013"]},
        ],
    }
    composition = [
        {"target": "WM-DAT-005 Data Pipeline", "relation": "REFERENCE", "purpose": "Bind the candidate parent pipeline and runnable graph without owning definition lifecycle or cascade behavior.", "required": False, "source_refs": ["SRC-005", "SRC-008"]},
        {"target": "Dataset, data product, schema, contract and source-record models", "relation": "REFERENCE", "purpose": "Resolve declared, consumed, generated and published data identities, versions and contracts without copying their lifecycles.", "required": True, "source_refs": ["SRC-001", "SRC-003", "SRC-004", "SRC-005"]},
        {"target": "Software, package, image, configuration, secret, identity and compute models", "relation": "REFERENCE", "purpose": "Resolve immutable execution artifacts, authorization and environment while external systems retain control and sensitive values.", "required": True, "source_refs": ["SRC-008", "SRC-012", "SRC-013", "SRC-014"]},
        {"target": "Log, metric, trace, quality, incident, provenance, access-audit and records models", "relation": "REFERENCE", "purpose": "Resolve evidence and governance records without absorbing observability, incident or retention execution.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-004", "SRC-006", "SRC-014", "SRC-015"]},
        {"target": "OpenLineage 1.53, PROV, OTel 1.60, CloudEvents 1.0.2, CWL 1.2, WES 1.1, OGC Processes 1.0, Airflow, Kubernetes Job, OCI Image and OpenAPI 3.1", "relation": "ALIGN", "purpose": "Project version-pinned lineage, telemetry, event, workflow, execution-service, orchestration, container and API views with scope and information-loss declarations.", "required": False, "source_refs": ["SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007", "SRC-008", "SRC-009", "SRC-010", "SRC-011", "SRC-012", "SRC-013", "SRC-017"]},
    ]
    return {"schema_version": "1.0.0", "model": model, "sources": SOURCES, "structure": structure(), "functions": functions(), "composition": composition, "service_layers": services(), "coverage": coverage()}


if __name__ == "__main__":
    RUN.joinpath("codex.result.json").write_text(json.dumps(build(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
