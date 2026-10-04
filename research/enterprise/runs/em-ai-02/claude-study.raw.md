# Verdict

| Candidate | Decision | Identity |
|---|---|---|
| **ModelArtifact** | REUSE WM-SFT-004 (`entity`) | Independent — required |
| **TrainingRun** | REUSE WM-AI-006 (`aggregate`) | Independent — required |
| **AIModel** (family/architecture) | PROFILE over WM-AI-007 family/version bindings + WM-SFT-004 derivation lineage | **No** independent identity |
| **TrainingConfiguration** | SPLIT: run-pinned effective configuration = REUSE (WM-AI-006, run-contained); reusable training recipe = conditional identifier-unassigned candidate, deferred to registry review | Conditional only |
| **ComputeAllocation** | REUSE: observed → WM-FLW-015; requested/granted → EM-WRK-05 demand/pool/reservation machinery. No AI-specific root | Grant only (borrowed) |

Registry entry keeps independent identity as already frozen (WM-AI-007, `registry`). No identifiers allocated here.

# Evidence

Three frozen specs: WM-SFT-004 (263 470 B, `a9f1da96…`, dual-provider, base Claude), WM-AI-007 (187 600 B, `04f21ef7…`), WM-AI-006 (183 984 B, `6a148d74…`) — the latter two `single-provider-waiver`, Codex-only, Claude and Grok timed out at 120 s. Adjacent: WM-DAT-001, WM-AI-005, WM-AI-001, WM-FLW-015. All six carry `publishableCanonical: false` / `adjudicationStatus: reviewable-draft`. Prior boundary work reused: EM-AI-01 (configuration/run/endpoint split), EM-DAT-01 (pinned contract version), EM-WRK-05 (demand/pool/reservation, quantity kinds), EM-FIN-05 (allocation runs, non-additive axes), EM-TEC-04 (runtime/endpoint mastership).

# Identity/mastership

Artifact identity = registry-of-record key first, governed IRI second, minted UUID/ULID last, digest as integrity and pinning key only (WM-SFT-004 `identity_priority`). Run identity = execution-system key; registry-entry identity = owning registry + namespace. Family name, version label, mutable alias, tag, endpoint address, digest alone and dates are never identity. Weights and protected data stay outside the public catalogue: deny-by-default on weight bytes and confidential dossier content (WM-SFT-004 `access.default_rule`), deny-by-default on training data, secrets and checkpoints (WM-AI-006).

# Model/registry/artifact

Three distinct planes, already separated in the dossier: conceptual family/architecture is a classification and identity *scope level* on the artifact record plus `model-family-version-alias-canonical-uri-duplicate-and-equivalence` on the registry entry — not a governed root. The registry entry owns registration, discoverability, approvals, lifecycle assertions and non-owning bindings. The artifact owns immutable weights, serialization, digest, manifest, licence and its own lifecycle. `entry_kind` values (`entity`, `registry`, `aggregate`) are mutually consistent; no merge or reclassification is warranted.

# Training run/configuration

The run is the execution aggregate: objective, method, authority, immutable input bindings, topology, attempts, progress, checkpoints, metrics, outcome. WM-SFT-004 correctly rejected hyperparameters at artifact level and deferred them to the run — that rule holds. Configuration is **run-contained by default**: every run pins one immutable effective configuration (code revision, entrypoint, hyperparameters, seeds, environment) by digest. Where an organisation versions and approves a reusable recipe independently of any execution, that recipe has an independent lifecycle and may later justify its own root — modelled on the WM-AI-005 pattern (immutable, content-addressed, approved separately from the run). Even then the run must pin **both** recipe version and resolved effective digest, exactly as EM-AI-01 required for base + effective configuration. A recipe never inherits a run's outcome, and two runs from one recipe are never one run.

# Data/rights/provenance

Required inputs, all version-qualified: pinned base model and tokenizer; dataset snapshots with role, split, mixture, transform, sampling and permission; code revision and entrypoint; resolved dependencies, framework, compiler, driver, hardware, environment; hyperparameters and seeds; rights, licence and purpose restrictions; artifact digests; declared reproducibility limits. Dataset content, rights and lifecycle remain WM-DAT-001-mastered; the run binds, never owns. Licence and use restrictions attach per artifact and per component, with inherited upstream terms propagated through derivation (WM-SFT-004 `fnd-derivation-lineage`). Restrictions do not merge when two artifacts share an endpoint.

# Checkpoint/final artifact

Decided: a checkpoint is **run-contained** — identity, step, digest, completeness, retention and resume semantics belong to WM-AI-006. It is not a registered artifact and carries no released lifecycle state. Promotion of a checkpoint to a released artifact creates a WM-SFT-004 revision with derivation back to that checkpoint; "observed best checkpoint" is not selection, and selection is not release. Adapters, quantizations, merges and format conversions are new artifact revisions with lineage, never in-place payload mutation.

# Compute allocation/actuals

Three independently sourced assertions, never substituted: **requested** (plan, run-owned), **granted/allocated** (a reservation or quota with its own lifecycle, expiry and authority, existing before and outside any run and expirable unused), **observed** (WM-FLW-015 source-qualified consumption with quantity kind, unit, interval, boundary, method and uncertainty). GPU-hours, wall-clock, energy, carbon and currency are different quantity kinds and are not summed; conversions are separate evidenced assertions. A compute grant implies nothing about employment, legal or agent identity, runtime deployment, or actual use — and no allocation may be inferred from observed telemetry or vice versa.

# Deployment/endpoint

Registry entry records deployable/deployed/active only as authority-qualified external observations. Serving infrastructure and endpoints are explicitly out of scope in WM-SFT-004 and WM-AI-001; per EM-AI-01 and EM-TEC-04 the endpoint is a typed reference into the runtime/compute-environment master, declared in configuration and observed at run time. Consequently: a new endpoint, a repointed alias, a new deployment or a new serving region creates **no** training run and **no** artifact revision. Equal model names, equal aliases or equal registry titles never prove equal weights; only digest verification does.

# Time/version/reproducibility

RFC 3339 with seconds and explicit offset throughout. Distinct clocks: submitted, queued, started, checkpointed, observed, stopped, completed; release vs ingestion; signing vs log inclusion; measurement vs publication; transition event vs record time; plus knowledge/ingestion time. Evidence is revision-bound and goes stale by rule when the digest changes. A seed proves nothing across releases, platforms or hardware; reproducibility is a bounded claim with declared nondeterminism, mastered by the run, referenced (not restated) by the artifact.

# Acceptance scenario

Checkpoint CK at step *n* of run R0 → runs R1 and R2, datasets D1 (permissive) and D2 (restricted). Result: two artifacts A1, A2 with distinct digests, distinct effective configuration digests, distinct dataset bindings and distinct inherited restrictions; both derive from CK, which remains R0-contained. Both are exposed through one endpoint E. E is one runtime reference; it neither merges lineage nor relaxes D2's restrictions, and requests served by A2 remain bound to A2's terms. No new run, artifact or model is created by adding E. Compute: R1 and R2 hold separate requested/observed records against a shared grant; the grant's unused remainder is residual, not consumption.

# Invariants

1. Digest verifies bytes, never business identity. 2. Equal names/aliases ≠ equal weights. 3. Every run pins one immutable effective configuration digest. 4. Every training assertion pins base model, tokenizer, dataset snapshots/splits, code revision, dependencies, hyperparameters, seeds, environment. 5. Requested ≠ granted ≠ observed compute; never inferred from one another. 6. A compute grant implies no employment, identity, deployment or use. 7. Checkpoint ≠ final artifact; selection ≠ release ≠ deployment. 8. Endpoint change creates no run and no artifact revision. 9. Restrictions and lineage never merge at a shared endpoint. 10. No in-place weight rewrite; conversion is a new revision with lineage. 11. Registry entry ≠ artifact ≠ run ≠ evaluation ≠ deployment. 12. Weights and protected data stay outside the public catalogue. 13. Reproducibility is a bounded, environment-pinned claim. 14. Quantity kinds are not summed.

# Minimal model set

WM-SFT-004 (artifact) · WM-AI-006 (run) · WM-AI-007 (registry entry) · WM-DAT-001 (dataset) · WM-FLW-015 (observed compute) · existing resource demand/pool/reservation authority (grants) · runtime/compute-environment authority (endpoint) · evaluation authority (WM-AI-003, unfrozen). Plus one conditional, identifier-unassigned reusable-training-recipe candidate.

# Holds

Contradictions found: WM-AI-007 declares `composition … WM-SFT-004 required: true` while its own boundary decision calls that parent an *unapproved* signal with no ledger edge — a required binding on an unratified relation; the relation ledger contains no WM-AI-007 edge at all. WM-AI-006 marks `WM-DAT-001 required: true` while the same edge is held as candidate. WM-SFT-004 asserts reproducibility status on the artifact while WM-AI-006 masters the replay recipe — single-master rule needed. WM-SFT-004 lists 30 sources but its holds enumerate "21 base plus three Grok", and SPDX, AI RMF, ONNX, safetensors and HF model cards each appear under two source IDs. Gaps: no frozen evaluation, deployment or endpoint model; no named master for inference endpoints inside the AI domain; WM-AI-006/WM-AI-007 boundary decisions rest on Codex alone. Inherited holds stand: EU AI Act read from reproductions, paywalled ISO clauses, MLflow stage deprecation, unpinned live sources, missing multi-profile fixtures. This review claims no canonical completeness, installability or publication readiness.
