# WM-AI-006 Codex pre-provider note

This is preparatory boundary evidence, not provider research and not a
publication artifact.

- Registry identity: `vr.wm-ai-006`, model `WM-AI-006`, name Model Training /
  Fine-tuning Run.
- Registry record plane: `world-model`; catalogue entry kind:
  `standalone-mm`; candidate subject-schema kind: `aggregate`.
- Purpose: represent one governed model-training execution, not a reusable
  dataset, trained-model artifact, experiment definition, evaluation campaign,
  compute fleet, software package or registry entry.
- Candidate outgoing relations: `REFERENCE WM-DAT-001` for typed dataset
  bindings and `PRODUCES WM-SFT-004` for the output artifact. Both remain
  boundary signals only and grant no target lifecycle or cascade authority.
- Expected external masters: dataset, model artifact, base model, tokenizer,
  code, package, image, configuration, secret, compute resource, experiment,
  evaluation, benchmark, incident, provenance, access audit and records policy.
- Required direct properties: method and objective, immutable input bindings,
  code and environment, distributed topology, stages and attempts, resources,
  hyperparameters, progress, metrics, checkpoints, outputs, failure, recovery,
  reproducibility, cost and environmental evidence, access and retention.
- Required safety boundary: no autonomous data acquisition, training launch,
  compute mutation, secret access, privacy or rights override, checkpoint or
  model release, deployment, incident closure or destructive cleanup.
- Required time format: RFC 3339 with seconds and explicit offset or `Z`, with
  scheduled, requested, queued, started, resumed, checkpointed, completed,
  observed, recorded, ingested and knowledge times distinct.
