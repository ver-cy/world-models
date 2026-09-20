# WM-DAT-005 verified source notes

Accessed 2026-09-06. Official standards-body, public-authority and first-party
project sources were checked at their canonical public pages. Provider wrappers
are not sources.

- OpenLineage separates reusable Job and Dataset identities from RunEvent
  observations and supplies extensible facets. This model therefore keeps the
  pipeline definition distinct from each deployment, scheduler registration,
  run, task attempt and emitted lineage event.
- Apache Airflow defines a DAG as schedule, tasks and dependencies, while a DAG
  run is a time-bounded instance. Its logical date and data interval are not the
  actual start time, and versioned DAG bundles remain runtime-specific profiles.
- CWL v1.2.1 grounds portable workflow inputs, outputs, steps, requirements and
  execution setup, while BPMN 2.0.2 grounds process and control-flow projection.
  Neither vocabulary is assumed to be a lossless universal pipeline master.
- PROV-O grounds attributable entities, activities, agents, derivations and
  revisions. DCAT 3 and DQV ground dataset or data-service catalog projections
  and quality metadata. SHACL and JSON Schema ground validation profiles.
- CloudEvents 1.0.2 provides a portable event envelope. OpenTelemetry semantic
  conventions 1.44.0 provide versioned telemetry naming profiles whose status
  varies by domain. They do not define pipeline success or data quality.
- Kubernetes Job describes finite workload execution and retry behavior; the
  OCI Image Specification describes immutable content-addressable runtime
  artifacts. Both remain deployment profiles outside the pipeline definition.
- NIST SSDF 1.1 supports governed software change and provenance practices.
  OWL-Time and RFC 3339 preserve temporal semantics and timestamp interoperability.
- Intended topology and static lineage are not proof of runtime execution.
  A successful run is not proof of accepted data quality, freshness, publication
  or downstream consumption. Exactly-once delivery is never presumed.
