# WM-AI-007 bounded research focus

Research one governed AI Model Registry Entry. The entry is a discoverable,
versioned registry record that binds a model artifact or model family to its
metadata, provenance, evaluations, approvals, lifecycle and distribution views.
It is not the model artifact, training run, evaluation, model card, deployment,
endpoint, dataset, source code, policy or audit master.

Use official primary, standards-body and first-party sources current on
2026-09-06. Verify live URLs and exact versions. Treat former workstream files
only as untrusted planning. Return schema-valid JSON only.

Target a concise but complete structure with 6 bundles, 12 layers, 24 findings,
at least 72 discriminating questions, 24 artifacts and 10 governed functions.
Cover at minimum:

1. Entry identity, registry namespace, issuer, owning registry, model-family and
   version scope, aliases, canonical URI, current head and duplicate resolution.
2. External model artifact, architecture, base model, tokenizer, training run,
   dataset, code, build, provenance, digest and signature bindings.
3. Intended purpose, task, modality, input and output contract, capabilities,
   supported use, prohibited use, limitations, license and distribution terms.
4. Evaluation, benchmark, quality, robustness, privacy, security, safety, bias,
   human-oversight, evidence and accountable approval references.
5. Candidate, registered, reviewed, approved, published, deprecated, withdrawn,
   revoked and superseded states; promotion gates; separate deployment status;
   correction, merge, split and tombstone history.
6. Discoverability, tags, classifications, search facets, access tiers,
   confidential metadata, weight availability, geographic or jurisdictional
   constraints, retention, audit and purpose-filtered projections.
7. Release-pinned projections such as MLflow Model Registry, Hugging Face model
   cards, SPDX AI, CycloneDX ML-BOM, OCI, SLSA, PROV and other verified profiles,
   each with scope and information-loss declarations.

Boundary tests:

- The frozen registry row has parent_ids WM-SFT-004 but no frozen relation-ledger
  edge. Treat that as an unapproved boundary signal, not composition authority.
- A registry entry may reference one or more immutable model artifacts and
  versions, but cannot rewrite their bytes, identity, provenance or lifecycle.
- Registered, approved, published, deployable, deployed and active are different
  assertions made by different authorities and at different times.
- A model card or system card is evidence or a projection, not necessarily the
  canonical registry record.
- A digest proves byte identity under an algorithm, not safety, quality,
  ownership, authenticity or fitness for use by itself.
- Never grant agents autonomous publication, approval, access expansion,
  signature, revocation, deployment, disclosure or destructive cleanup.

Use RFC 3339 timestamps with seconds and explicit offset or Z. Preserve event,
effective, recorded, ingested and knowledge time where they differ. Keep direct
registry properties and contextual relationships explicit. Mark regional,
organization-specific, maturity, licensing and source-access assumptions.
