# WM-ACT-053 bounded provider focus

Research the governed aggregate for one execution of a data-processing job or
pipeline. Cover immutable definition and code bindings, trigger and schedule,
parameters and configuration, input and output dataset versions, task or stage
runs, attempts, compute and runtime environment, lineage, validation, data
quality, logs, metrics, traces, errors, retry, recovery, cancellation, backfill,
replay, publication and retention while keeping externally mastered objects
distinct.

Use current official primary sources. Inspect W3C PROV-DM and PROV-O, W3C DCAT
3, OpenLineage current specification, OpenTelemetry traces and semantic
conventions, CNCF CloudEvents 1.0.2, Common Workflow Language 1.2, GA4GH Workflow
Execution Service, Apache Airflow stable documentation, Kubernetes Job API,
OCI Image and Runtime specifications, GDPR and RFC 3339. Treat implementation
systems as profiles rather than universal semantics.

Stress-test these semantics:

- the pipeline or job definition, dataset, schema, code or image, schedule,
  identity, compute resource and observability record remain external masters;
  the aggregate owns one execution identity and versioned bindings;
- requested, queued, dispatched, started, running, retrying, succeeded, failed,
  cancelled, timed out, skipped and unknown are distinct source-qualified states;
- a task, stage, attempt and retry have separate identities, sequence, times,
  environment and outcomes; retry never overwrites the failed attempt;
- declared inputs, resolved input versions, consumed observations, declared
  outputs, materialized outputs and published outputs remain distinguishable;
- successful process exit does not prove output publication, completeness,
  correctness, schema conformance, data quality, freshness or downstream use;
- lineage records code, parameters, environment, inputs, transformations,
  outputs and agents without copying the dataset or software lifecycle;
- backfill, replay, rerun, resume and recovery preserve original execution,
  trigger, effective data interval, attempt history and successor lineage;
- logs, metrics, traces, quality results and artifacts are evidence with source,
  scope, event time, observation time, ingestion time and integrity;
- cancellation, cleanup, rollback, compensation and retention do not imply
  deletion of referenced datasets, logs, code or infrastructure.

The only registered relation is candidate incoming `WM-DAT-005 CONTAINS
WM-ACT-053`. Treat it as a boundary hold: this model may reference a parent
pipeline and record execution membership, but it must not own or mutate the
pipeline definition. Keep the result reviewable-draft until relation approval,
runtime profiles, security/privacy review and independent external review.

