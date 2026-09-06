# WM-AI-007 pre-provider boundary notes

- Canonical scope: AI Model Registry Entry, sequence 141,
  registry ID `vr.wm-ai-007`, record plane `world-model`.
- Frozen purpose: deployment status, approvals, lineage and discoverability.
- Frozen catalogue entry kind `standalone-mm` is not the research schema's
  aggregate classification. The likely research entry kind is `registry`.
- `parent_ids=WM-SFT-004` is present in the unified row, but the relation ledger
  has no WM-AI-007 edge. It is only a candidate boundary signal.
- The entry owns registry identity, catalog metadata, lifecycle assertions,
  approval bindings and discoverability. Model artifact, training, evaluation,
  deployment, endpoint, dataset, code, policy, credential and audit masters stay
  external.
- Separate model family, version, artifact digest, registry record and deployment
  identities. Separate candidate, registration, approval, publication,
  deprecation, withdrawal and revocation semantics.
- Prefer official public-authority, standards-body and first-party sources.
  Version-pin implementation projections and declare their information loss.
- Provider outputs must independently resolve the boundary and may not rely on
  this note as evidence.
