# WM-ACT-053 verified source notes

Accessed 2026-09-06. All 17 official source URLs returned HTTP 200. These are
primary or first-party sources used by the Codex fallback; provider wrappers
are not sources.

- W3C PROV-DM and PROV-O provide the main activity, entity, agent, use,
  generation, derivation, association, revision and time frame for execution
  provenance. DCAT 3 and DQV provide external dataset, distribution, version,
  quality measurement and metric projections.
- OpenLineage 1.53.0 separates Job, Run, Dataset and runtime versus design-time
  events. It supports the central boundary between reusable definition,
  execution identity and data assets.
- OpenTelemetry 1.60.0 and semantic conventions 1.44.0 provide versioned trace,
  metric, log, resource, instrumentation and schema concepts. Telemetry remains
  source-qualified evidence and is not itself execution truth.
- CloudEvents 1.0.2 provides portable trigger and lifecycle event envelopes.
  CWL 1.2.1 provides portable workflow graphs, inputs, outputs, steps and
  requirements. GA4GH WES 1.1.0 and OGC API Processes 1.0 provide bounded
  execution-service profiles for submission, status, cancellation, results,
  logs and exceptions.
- Apache Airflow 3.3.x and Kubernetes Job documentation provide implementation
  profiles for task instances, data intervals, dependencies, retries,
  heartbeats, parallel completion, suspension and cleanup. Their states and
  controller behavior are not generalized as universal semantics.
- OCI Image 1.1.1 provides digest-addressed image bindings. NIST SP 800-53,
  GDPR, RFC 3339 and OpenAPI 3.1.1 support tailored security and privacy,
  explicit timestamps and versioned service-description projections.

