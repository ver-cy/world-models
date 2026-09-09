# WM-AI-006 bounded provider focus

Research one governed machine-learning model training or fine-tuning run. Cover
run and experiment identity, objective and method, authority and risk profile;
base-model, tokenizer, dataset, code, configuration, dependency and environment
bindings; training, validation and evaluation splits; transformations,
sampling, mixture and permissions; distributed topology, workers, accelerators,
precision, parallelism, resources, cost and environmental measurements; stages,
steps, epochs, samples or tokens, optimizer and scheduler state; checkpoints,
metrics, anomalies, retries, resumption, early stopping, failure and cancellation;
candidate outputs, final produced artifact, lineage, reproducibility, privacy,
security, access, retention, correction, audit and version-pinned projections.

Use current official primary and first-party sources. Inspect NIST AI RMF 1.0,
NIST AI 600-1 Generative AI Profile, NIST SP 800-218A, Regulation (EU)
2024/1689, W3C PROV-O, OpenLineage, MLflow Tracking and model-training APIs,
Kubeflow Training Operator, Google ML Metadata, SLSA provenance, OCI Image,
OpenTelemetry, MLCommons MLPerf Training rules and results, the Green Software
Foundation Software Carbon Intensity specification and RFC 3339. Pin versions
or access dates and treat implementation systems as profiles, not universal
semantics.

Stress-test these boundaries:

- this aggregate owns one run and its constituent stage, step, worker, attempt,
  checkpoint-binding, metric and state assertions; reusable datasets, base and
  output model artifacts, code, packages, images, compute resources, experiment
  definitions, evaluation campaigns, incidents and registries remain external;
- pretraining, continued pretraining, supervised fine-tuning, adapter tuning,
  preference optimization, reinforcement learning, distillation and other
  methods are profiles, not interchangeable labels;
- declared, resolved and actually consumed dataset snapshots remain distinct;
  train, validation, test, calibration, preference and safety datasets have
  explicit roles, permissions, transformations, mixture weights and leakage or
  contamination evidence;
- base model, tokenizer, architecture, initialization, frozen parameters,
  trainable parameters, adapter, merge and produced artifact remain distinct;
- hyperparameter declaration, resolved value, runtime mutation and observed
  effective value are separate; random seed does not prove determinism;
- scheduled, queued, started, resumed, checkpointed, completed, failed,
  cancelled and early-stopped states are event-backed and do not prove output
  quality, safety, compliance, publication or deployment readiness;
- training loss, evaluation metric, benchmark result, safety evaluation and
  downstream acceptance are distinct source-qualified claims;
- checkpoint, candidate output and selected final artifact have independent
  identities, digests, lineage and retention; a successful run may produce no
  accepted model and a failed run may retain useful checkpoints;
- resource requests, allocations and observations remain distinct; cost,
  energy and emissions measurements record method, boundary and uncertainty;
- retries and resumption preserve original attempts, checkpoint lineage,
  dataset, code, configuration, environment and side-effect differences.

Registered candidate relations are outgoing `WM-AI-006 REFERENCE WM-DAT-001`
and `WM-AI-006 PRODUCES WM-SFT-004`. They permit typed dataset bindings and a
produced-artifact link, but grant no ownership of dataset or model-artifact
lifecycle. Keep the result reviewable-draft until both relations, training
method and regulatory profiles, release-pinned projections and independent
external review are approved.

Safety boundary: no autonomous dataset acquisition, training execution,
production compute allocation, secret retrieval, rights override, privacy
decision, checkpoint release, model publication, deployment, incident closure
or destructive cleanup outside explicit delegated authority.
