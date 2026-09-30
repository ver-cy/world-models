# Frozen semantic audit prompt — EM-AI-02

You are the sole frozen semantic auditor for this contour. This audit is run exactly once. Use only the supplied text. Do not browse, call tools, invent identifiers, claim standards conformance or propose publication of blockers.

Audit the reconciled EM-AI-02 boundary and allocation/profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence/rights semantics, non-deterministic fixtures and missing publishability holds. Preserve the intended decision unless the supplied evidence disproves it: reuse WM-AI-007 for registry identity, WM-SFT-004 for artifacts, WM-AI-006 for runs and run-contained effective configuration, WM-DAT-001 for datasets, WM-AI-001 for systems, WM-FLW-015 for observed consumption and external demand/capacity/reservation for requested and granted compute; keep family/architecture classificatory; keep Reusable Training Recipe only as a conditional identifier-unassigned candidate without present independent identity; allocate no catalogue, model or runtime ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect give exact deterministic remediation; Exact additional fixtures as a JSON array; and a final freeze decision. Be sceptical and concise. If there are no material defects, say so explicitly. Never request another provider run.

## LOCAL SYNTHESIS

```text
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

```

## CLAUDE FROZEN STUDY

```text
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

```

## EXACT GROK RESPONSE

```text
Verdict. Accept the reuse-only proposal. Map registry identity to WM-AI-007, artifacts to WM-SFT-004, runs and effective configuration to WM-AI-006, datasets to WM-DAT-001, systems to WM-AI-001, observed use to WM-FLW-015, and requested/granted compute to external capacity/reservation. Treat model family/architecture as classification only. Keep effective configuration run-contained. Allocate no other identifier. A reusable Training Recipe does not need independent identity in this increment; keep it as an identifier-unassigned conditional candidate. Blockers are capability gaps on reused masters, not grounds to mint codes. This review does not claim publication readiness.

Strongest evidence. Two fine-tunes from one checkpoint with different dataset licences cannot share one registry identity, one artifact, or one rights bundle. WM-SFT-004 already masters immutable artifacts and digests; WM-AI-006 already masters the run; WM-DAT-001 already masters dataset snapshots. Family, display name, and a shared endpoint cannot collapse those records. Requested ≠ granted ≠ observed is independently shown by reservation versus WM-FLW-015 actuals on the same run.

Strongest counterexample. Two artifacts share a display name and one endpoint. Operators treat the endpoint or family as “the model,” merge licences, and omit a second run. That hides the stricter dataset licence, collapses lineage, and treats a serving change as training. Equal names are not equal weights. A new endpoint is not a newly trained model.

Identity/mastership. WM-AI-007 masters catalogue identity. WM-SFT-004 masters immutable artifacts. WM-AI-006 masters the training/fine-tune event and its effective configuration. WM-DAT-001 masters datasets. WM-AI-005 is generic configuration, not the effective training record. WM-AI-001 masters the AI system, not weights. WM-FLW-015 masters observed consumption. Requested and granted compute reuse external capacity/reservation. No new identifier for family, recipe, TrainingConfiguration, or ComputeAllocation. Family/architecture classifies across registry and artifact lineage; it does not identify.

Model/registry/artifact. AIModel in this increment is the WM-AI-007 registry entry, not a parallel master. Registry entry ≠ artifact ≠ family. Display name is a label; identity of weights is the artifact digest. The catalogue may reference artifacts and runs; it must not embed weights or protected data. Two names may point at different artifacts; one name must not collapse two digests.

Run/configuration. Effective TrainingConfiguration is contained by WM-AI-006 and frozen at run start: pinned hyperparameters, seeds, environment, code, dependencies, tokenizer, base-model reference, and reproducibility limits. WM-AI-005 is not a second run identity. Two runs that share a checkpoint and even hyperparameters remain two WM-AI-006 instances when dataset, rights, or seeds differ. A recipe is reusable intent only and must not substitute for the run snapshot.

Data/rights/provenance. Each run pins WM-DAT-001 snapshot, splits, and transforms; it does not copy payload into the catalogue. Rights and licences bind to the data used in that run, then to the resulting artifact and any registry publication of that artifact. They do not inherit from the parent checkpoint, family classification, shared endpoint, or a sibling run. Weights and protected data stay outside the public catalogue. Provenance is checkpoint artifact → run → new artifact, with restriction sets remaining distinct.

Checkpoint/final artifact. Both are WM-SFT-004 instances. A checkpoint is an intermediate immutable artifact consumed or emitted by a run. A final artifact is the selected output of a completed run. Same type, different lineage role. Parent checkpoint C can seed runs that emit A1 and A2; C, A1, and A2 remain three artifacts. Promotion to registry does not mutate bytes. Digests, licences, and reproducibility limits travel with each artifact, not with the endpoint or family.

Compute allocation/actuals. Do not allocate an identifier for ComputeAllocation. Map requested and granted to external capacity/reservation; map observed use to WM-FLW-015 bound to the WM-AI-006 run, and only then to the produced artifact. Keep three facts distinct: requested quota, granted reservation, observed consumption. A run may be granted less than requested and consume less than granted. Chargeback, SLA, and reproducibility claims use observed, not requested. Do not store actuals on the registry entry or endpoint. A shared endpoint must not share compute records.

Deployment/endpoint. Endpoint and deployment belong to serving, not training. Bind an endpoint to a digest-pinned WM-SFT-004 artifact, not to a family, registry label, or recipe. WM-AI-001 may expose one or more endpoints. Sharing an endpoint across two fine-tunes does not merge artifacts, runs, licences, or compute. Standing up or retargeting an endpoint creates no TrainingRun and no new artifact. Serving policy must consult artifact/run rights before bind; divergent dataset licences can forbid co-serving even under one hostname. Evaluation remains separate and unassigned here.

Time/version/reproducibility. A run has start and end. An artifact is immutable once digested; a new digest is a new WM-SFT-004 instance. A registry entry may carry catalogue versioning without implying new weights. Deployment time is not training time. Reproducibility requires the full pin set: base model, tokenizer, dataset snapshots/splits/transforms, code, dependencies, hyperparameters, seeds, environment, rights, licences, artifact digests, and stated reproducibility limits. Missing pins make the run non-reproducible; they do not authorize merging identities.

Scenario. Parent checkpoint C (WM-SFT-004). Fine-tune A: licence L1 → run R1 with effective config CFG1 and snapshot S1 → artifact A1 with L1 restrictions; requested/granted compute for R1; observed use on WM-FLW-015 bound to R1. Fine-tune B: licence L2 → R2 / CFG2 / S2 → A2 with L2 restrictions and separate compute records. Family/architecture classification may be shared. Endpoint E may serve A1 and/or A2. Required: separate lineages, restriction sets, and compute records. Forbidden: treating E as a newly trained model; treating A1 ≡ A2 because names match; merging L1 and L2; sharing one actuals record; promoting E or family to registry-equivalent identity.

Invariants.

1. Family/architecture classifies; it does not identify registry, artifact, run, endpoint, or system.
2. WM-AI-007 ≠ WM-SFT-004 ≠ WM-AI-006 ≠ WM-AI-001.
3. Equal names are not equal weights; identity of weights is the artifact digest.
4. Checkpoint and final artifact are distinct WM-SFT-004 instances.
5. A run is not an artifact, registry entry, evaluation, deployment, endpoint, or system.
6. Effective configuration is run-contained; TrainingConfiguration has no new identifier.
7. Reusable Training Recipe has no assigned identifier in this increment.
8. Requested compute ≠ granted compute ≠ observed use (WM-FLW-015).
9. Dataset licences on WM-DAT-001 constrain derived artifacts and do not transfer by shared serving.
10. Two fine-tunes from one checkpoint yield two runs and two artifact lineages even if they share one endpoint.
11. A new endpoint is not a newly trained model and creates neither artifact nor registry identity.
12. Weights and protected data stay outside the public catalogue.
13. A run must pin base model, tokenizer, dataset snapshots/splits/transforms, code, dependencies, hyperparameters, seeds, environment, rights, licences, artifact digests, and reproducibility limits.
14. Observed use records actuals; it does not grant capacity.
15. Evaluation, deployment, and endpoint are not training products and must not be recorded as new models.

Minimum model set. WM-AI-007 registry entry; WM-SFT-004 artifact (checkpoint and final weights as roles/lineage, not new codes); WM-AI-006 run with run-contained effective configuration; WM-DAT-001 dataset snapshots/splits/transforms; WM-AI-005 as generic configuration type only; WM-AI-001 system; WM-FLW-015 observed consumption; external capacity/reservation for requested/granted. Family/architecture = classification only. Training Recipe = unassigned conditional candidate. Evaluation, endpoint-as-entity, and ComputeAllocation as a new master are out.

Blockers. (1) WM-AI-006 must accept the full pin set or the run is not auditable. (2) WM-SFT-004 must carry digest, role (checkpoint vs final), parent-artifact lineage, and restriction/licence references without becoming a registry entry. (3) WM-FLW-015 must bind to a run without minting ComputeAllocation. (4) Shared-endpoint plus divergent licences needs a bind-time rights check; if neither WM-SFT-004 nor WM-AI-001 can hold that constraint, serving compliance is a gap—still do not invent an identifier. (5) The public catalogue must reference artifacts without embedding weights or protected data. (6) No adjacent draft covers evaluation; keep it separate and identifier-unassigned. Revisit Training Recipe identity only if later evidence shows a reusable recipe with its own lifecycle, rights, and approval path distinct from WM-AI-005 and from pinned run config.

```

## PROVIDER COMPARISON

```text
# EM-AI-02 provider comparison

Claude and Grok agree on the reuse-only boundary: WM-AI-007 owns registry identity, WM-SFT-004 owns immutable model artifacts, WM-AI-006 owns training or fine-tuning runs and their resolved effective configuration, WM-DAT-001 owns dataset snapshots, WM-AI-001 owns the AI system, WM-FLW-015 owns observed consumption, and requested or granted compute stays with external demand, capacity and reservation authorities. Model family and architecture remain classifications. No catalogue, model or runtime identifier is allocated.

Both reviews keep registry entry, artifact, checkpoint role, run, evaluation, deployment, endpoint and system distinct. Equal names do not prove equal weights; artifact digests pin bytes without replacing governed identity. Two fine-tunes from one checkpoint remain two runs and two artifact lineages even when served through one endpoint. Dataset rights, licences and restrictions remain bound to each run and derived artifact and never merge through shared serving.

The apparent Training Recipe difference is resolved conservatively. Claude says a reusable recipe may justify independent identity only when evidence demonstrates a lifecycle, governance, approval and reuse independent of executions. Grok finds no such evidence in this increment and says the recipe does not need independent identity now. Therefore Reusable Training Recipe remains a conditional identifier-unassigned allocation candidate, not an allocated root or current independent identity. Every run still pins its complete resolved configuration; a recipe can never substitute for that snapshot.

Grok sharpens serving and compute semantics: endpoint bindings must pin an artifact digest and pass rights checks; endpoint creation or retargeting creates neither a run nor an artifact; requested, granted and observed compute remain separately mastered and a shared endpoint cannot share run actuals. It also requires the full reconstruction pin set and treats missing pins as non-reproducibility rather than permission to merge identities.

Publication remains held by unapproved required relations, unresolved reproducibility ownership, missing frozen evaluation/deployment/endpoint authorities, incomplete rights-at-bind enforcement, single-provider base drafts and the conditional unallocated recipe candidate. The result is a reviewable profile-plus-conditional-allocation dossier with no installability or publication-readiness claim.

```

## ALLOCATION CANDIDATE

```json
{
  "format":"vercy-model-allocation-candidate/v1",
  "contourId":"EM-AI-02",
  "proposedName":"Reusable Training Recipe",
  "modelId":null,
  "registryId":null,
  "allocationState":"unassigned",
  "decision":"NEW MODEL",
  "canonicalPublishable":false,
  "identityTest":{
    "stableIdentity":"A recipe is independently identifiable only when a governed reusable training specification persists across multiple execution runs and resolved configurations.",
    "versionIdentity":"Changes to objective, method, required inputs, configuration schema or approval basis create immutable recipe revisions with explicit effective periods.",
    "independentLifecycle":["draft","approved","effective","suspended","superseded","retired"],
    "mastership":"AI engineering method-governance authority"
  },
  "boundary":{
    "owns":["stable reusable recipe identity","immutable approved recipe revisions","required input roles and configuration schema","effective periods and governance approvals","declared reproducibility intent and known limitations"],
    "references":[
      {"target":"WM-AI-006","purpose":"Training runs that pin a recipe revision and resolved effective configuration"},
      {"target":"WM-SFT-004","purpose":"Produced model artifacts and derivation lineage"},
      {"target":"WM-AI-007","purpose":"AI registry entries and discoverability"},
      {"target":"WM-DAT-001","purpose":"Version-qualified training and evaluation datasets"},
      {"target":"WM-AI-005","purpose":"Configuration values without transferring run ownership"},
      {"target":"WM-FLW-015","purpose":"Observed compute and resource consumption"}
    ],
    "excludes":["training-run execution identity","resolved run configuration","model artifact payload or digest identity","dataset identity or protected content","compute reservation or consumption","deployment and endpoint lifecycle"]
  },
  "objects":{
    "TrainingRecipe":{"identity":["trainingRecipeId"],"required":["name","ownerRef","status","currentRevisionRef"],"optional":["successorRef"],"lifecycle":["draft","approved","effective","suspended","superseded","retired"]},
    "TrainingRecipeRevision":{"identity":["trainingRecipeId","revision"],"required":["objective","method","requiredInputRoles","configurationSchema","contentDigest","effectiveFrom"],"optional":["effectiveTo","supersedesRevision","knownLimitations"]}
  },
  "invariants":[
    "A recipe receives independent identity only when it is governed, versioned and reused across executions.",
    "Every run that uses a recipe pins one immutable recipe revision and one resolved effective-configuration digest.",
    "Two executions of one recipe remain two independently identified training runs.",
    "Recipe identity never inherits execution outcomes, checkpoints, metrics or resource actuals.",
    "Digest verifies recipe content but does not replace governed recipe identity.",
    "Training-run configuration remains run-owned even when derived from a recipe.",
    "Base model, tokenizer, dataset snapshots, code, dependencies, seeds and environment remain version-qualified external or run bindings.",
    "Dataset rights and purpose restrictions propagate through derivation and never merge at a shared endpoint.",
    "Checkpoint, final artifact, release, deployment and endpoint remain distinct identities.",
    "Requested, granted and observed compute remain distinct assertions.",
    "Reproducibility claims state pinned scope, nondeterminism and known limitations.",
    "Recipe revision changes never rewrite completed runs or produced artifacts.",
    "Protected data, weights and confidential configuration values stay outside the public catalogue.",
    "Retired recipe identifiers and revisions remain resolvable and are never recycled."
  ],
  "holds":["The candidate is conditional on demonstrated independent governance and reuse across executions.","Independent Grok review is pending.","Registry namespace and identifier allocation are pending and no identifier may be guessed.","Required base relations, reproducibility ownership and deployment authority remain unresolved.","Frozen audit, immutable pins, crosswalks and fixtures remain publication gates."]
}

```

## PROFILE CANDIDATE

```json
{
  "format":"vercy-enterprise-profile-candidate/v1",
  "contourId":"EM-AI-02",
  "name":"Enterprise AI Model Artifact and Training Binding",
  "decision":"PROFILE",
  "newRuntimeId":false,
  "bases":["WM-SFT-004","WM-AI-007","WM-AI-006","WM-DAT-001","WM-AI-005","WM-AI-001","WM-FLW-015"],
  "constraints":[
    "WM-SFT-004 owns immutable model artifacts while WM-AI-006 owns individual training or fine-tuning executions.",
    "WM-AI-007 owns registry identity, discoverability, approvals and registry lifecycle.",
    "Conceptual model family and architecture classify registry entries and artifact lineage without forming another root.",
    "Every run pins one immutable effective-configuration digest covering code, entrypoint, parameters, seeds, dependencies and environment.",
    "Requested compute is run-owned planning, granted compute is external reservation and observed compute is WM-FLW-015 consumption.",
    "Endpoint changes create neither a training run nor an artifact revision and preserve selected artifact digest and restrictions per invocation."
  ],
  "holds":["Reusable Training Recipe remains a conditional identifier-unassigned candidate.","Required relation approvals and reproducibility ownership reconciliation are pending.","Independent Grok review and frozen audit remain pending."]
}

```

## FIXTURES

```json
{
  "format":"vercy-enterprise-allocation-fixtures/v1",
  "candidateName":"Reusable Training Recipe",
  "cases":[
    {"id":"shared-recipe-two-runs","kind":"positive","input":"Runs R1 and R2 use the same approved recipe revision with different datasets and resolved configurations.","expect":"The recipe is shared while R1 and R2 remain distinct runs with separate lineage, rights, configuration digests and outcomes."},
    {"id":"checkpoint-promotion","kind":"positive","input":"A run checkpoint is selected and promoted into a release artifact.","expect":"Promotion creates a WM-SFT-004 artifact revision linked to the checkpoint; selection, release and deployment remain separate."},
    {"id":"shared-compute-grant","kind":"positive","input":"Two runs draw from one external compute reservation and report different observed GPU-hours.","expect":"The grant, each run request and WM-FLW-015 actuals remain distinct and unused capacity is not inferred as consumption."},
    {"id":"recipe-is-run","kind":"negative","input":"A reusable recipe and each execution share one identifier and lifecycle.","expect":"The merge is rejected because reusable specification and execution occurrence have independent identity and lifecycle."},
    {"id":"digest-only-identity","kind":"negative","input":"An artifact digest is used as the sole business identity for model, artifact and registry entry.","expect":"The merge is rejected; digest verifies bytes while governed identities remain distinct."},
    {"id":"seed-only-reproducibility","kind":"negative","input":"A run claims reproducibility because it records one random seed but omits software and hardware pins.","expect":"The claim is rejected as unbounded and under-specified."},
    {"id":"endpoint-merges-rights","kind":"negative","input":"Artifacts trained under different dataset restrictions are served by one endpoint and their restrictions are collapsed.","expect":"The collapse is rejected; shared serving never merges lineage or relaxes rights."}
  ]
}

```
