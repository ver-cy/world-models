# EM-AI-02 local synthesis

## Disposition

- Reuse WM-SFT-004 as the independently identified model artifact master.
- Reuse WM-AI-006 as the independently identified training or fine-tuning run aggregate.
- Treat conceptual AI model family and architecture as a profile and classification scope across WM-AI-007 registry entries and WM-SFT-004 derivation lineage, not a new root.
- Keep effective Training Configuration run-contained in WM-AI-006. A separately governed reusable Training Recipe remains an identifier-unassigned conditional candidate.
- Reuse EM-WRK-05 demand, pool and reservation semantics for requested and granted compute, and WM-FLW-015 for observed consumption. Create no AI-specific ComputeAllocation root.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Artifact identity follows the registry-of-record key, governed IRI or minted identifier; digest verifies bytes and pins content but is not business identity by itself. TrainingRun identity comes from the execution system. WM-AI-007 registry entries retain their existing independent registry identity.

Family name, version label, mutable alias, endpoint address, digest alone and timestamps never identify the model or artifact. Weights, protected data, checkpoints and confidential dossiers remain outside the public catalogue and deny-by-default.

## Model, registry and artifact

Conceptual family and architecture classify artifact lineage. WM-AI-007 owns discoverability, registration, approvals and registry lifecycle. WM-SFT-004 owns immutable weights or other payload, serialization, manifest, digest, licence and artifact lifecycle.

Registry entry, artifact, training run, evaluation, deployment and endpoint remain distinct. Equal names or aliases do not prove equal weights; verified digest comparison is required.

## Training run and configuration

WM-AI-006 owns one execution: objective, method, authority, immutable input bindings, topology, attempts, progress, checkpoints, metrics and outcome.

Every run pins one immutable effective configuration digest covering code revision, entrypoint, hyperparameters, seeds, dependencies and environment. A reusable Training Recipe needs a separate root only when it is independently versioned, approved and reused across executions; that candidate remains unallocated. A run using a recipe pins both recipe version and resolved effective configuration.

Two runs from one recipe remain two runs, and recipe identity never inherits execution outcomes.

## Data, rights and provenance

Reconstructability requires pinned base model and tokenizer, dataset snapshots and roles, splits, transforms and sampling, code revision, resolved dependencies, framework/compiler/driver/hardware environment, hyperparameters, seeds, rights and purpose restrictions, artifact digests and stated reproducibility limits.

WM-DAT-001 owns dataset identity, content, rights and lifecycle. The run records version-qualified bindings without copying data. Licence and use restrictions remain per input and per resulting artifact and propagate through derivation. A shared endpoint never merges or relaxes them.

## Checkpoint and final artifact

A checkpoint is run-contained with step, digest, completeness, retention and resume semantics. It is not a released artifact merely because it is observed as best.

Promotion creates a WM-SFT-004 artifact revision with derivation back to the checkpoint. Selection, release and deployment are distinct acts. Adapter, quantization, merge or format conversion creates a new artifact revision and lineage; payload bytes are never mutated in place.

## Compute allocation and actuals

Requested compute is a run-owned planning assertion. Granted compute is an external reservation or quota with authority, effective period and expiry. Observed compute is WM-FLW-015 consumption with quantity kind, unit, interval, method and uncertainty.

Requested, granted and observed quantities are never inferred from each other. GPU-hours, elapsed time, energy, emissions and currency remain separate quantity kinds. A grant implies no employment, agent identity, deployment or actual use.

## Deployment and endpoint

WM-SFT-004 and WM-AI-007 may reference external deployment observations but do not own serving infrastructure or endpoint lifecycle. A new endpoint, alias repoint, region or deployment creates no training run and no artifact revision.

One endpoint may serve multiple artifacts, and one artifact may be served by multiple endpoints. Runtime routing preserves the selected artifact digest and its restrictions per invocation.

## Time, version and reproducibility

Submitted, queued, started, checkpointed, observed, stopped, completed, released, ingested and knowledge times remain distinct. Evidence is revision-bound and becomes stale when a referenced digest changes.

A seed alone does not establish reproducibility across software, hardware or platform revisions. Reproducibility is a bounded WM-AI-006 claim with pinned inputs, environment, nondeterminism and known limitations.

## Acceptance result

Checkpoint CK from run R0 seeds fine-tunes R1 and R2. R1 uses dataset D1 under a permissive licence; R2 uses D2 under restrictions. The outputs A1 and A2 have different digests, configuration pins, dataset lineage and inherited restrictions. Both are exposed through endpoint E, which neither merges lineage nor relaxes D2 terms. Adding E creates no run or artifact. R1 and R2 retain separate requested and observed compute against a shared external grant, whose unused residual is not consumption.

## Required invariants

1. Digest verifies bytes but does not replace governed identity.
2. Equal names or aliases do not prove equal weights.
3. Every run pins one immutable effective configuration digest.
4. Training pins base model, tokenizer, data, code, dependencies, seeds and environment.
5. Requested, granted and observed compute remain distinct.
6. Compute grant implies no employment, identity, deployment or use.
7. Checkpoint, final artifact, selection, release and deployment remain distinct.
8. Endpoint changes create no run or artifact revision.
9. Rights and lineage do not merge at a shared endpoint.
10. Weight transformations create successor artifacts with lineage.
11. Registry entry, artifact, run, evaluation and deployment remain separate.
12. Protected weights and data stay outside the public catalogue.
13. Reproducibility is bounded and environment-pinned.
14. Different compute quantity kinds are never summed.

## Holds

Reusable Training Recipe is an identifier-unassigned conditional candidate. WM-AI-007 requires WM-SFT-004 while its relation remains unapproved; WM-AI-006 similarly requires WM-DAT-001 through a held candidate relation. Reproducibility ownership overlaps between WM-SFT-004 and WM-AI-006. No frozen deployment or endpoint model was available in this contour. WM-AI-006 and WM-AI-007 are single-provider drafts, and source, crosswalk and fixture holds remain. No installability or publication-readiness claim is made.
