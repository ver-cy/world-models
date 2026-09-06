# WM-AI-006 verified source notes

Accessed 2026-09-06. Official public-authority, standards-body and first-party
sources were checked at their canonical pages. Provider wrappers are not sources.

- NIST AI RMF 1.0, the NIST Generative AI Profile and NIST SP 800-218A establish
  lifecycle risk, accountable development, training-data, privacy, security,
  provenance, evaluation, incident and environmental evidence. AI RMF 1.0 is
  visibly pinned because NIST reports that a revision is in progress.
- The EU AI Act and GDPR are bounded European Union legal profiles. Their duties
  cannot be generalized to every jurisdiction, industry or use case.
- W3C PROV-O, OpenLineage 1.53.0, MLflow Tracking and TensorFlow ML Metadata
  establish complementary activity, run, artifact, dataset, context and lineage
  concepts. They do not make one universal lossless schema.
- Kubeflow Trainer 2.1.0, SLSA 1.1, OCI Image 1.1.1 and OpenTelemetry 1.60.0 are
  release-pinned runtime, provenance, packaging and telemetry profiles.
- MLPerf Training v6.0 and SCI 1.1.0 require method-bound quality, time, energy
  and emissions claims rather than unlabeled scalar values.
- PyTorch 2.14 explicitly warns that complete reproducibility is not guaranteed
  across releases, commits or platforms. Seeds are therefore evidence, not proof.
- RFC 3339 supplies the timestamp profile with seconds and explicit UTC relation.
