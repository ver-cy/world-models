# Exact unsent Grok prompt — EM-AI-02

Independent enterprise metamodel review. Do not browse, invent identifiers or claim publication readiness.

EM-AI-02 covers AIModel, ModelArtifact, TrainingRun, TrainingConfiguration and ComputeAllocation. Complete adjacent drafts cover WM-SFT-004 ML Model Artifact, WM-AI-007 AI Model Registry Entry, WM-AI-006 Training / Fine-tuning Run, WM-DAT-001 Dataset, WM-AI-005 Configuration, WM-AI-001 AI System and WM-FLW-015 Resource Consumption.

Assess this proposal: reuse WM-SFT-004 for artifacts and WM-AI-006 for runs; treat model family/architecture as classification across registry and artifact lineage; keep effective configuration run-contained; leave a separately governed reusable Training Recipe as an identifier-unassigned conditional candidate; reuse external capacity/reservation semantics for requested/granted compute and WM-FLW-015 for observed use. Allocate no other identifier.

Separate model family from registry entry, immutable weights, checkpoint, run, evaluation, deployment, endpoint and system. Separate requested, granted and observed compute. Require pinned base model, tokenizer, dataset snapshots/splits/transforms, code, dependencies, hyperparameters, seeds, environment, rights, licences, artifact digests and reproducibility limits. Weights and protected data stay outside the public catalogue.

Test two fine-tunes from one checkpoint with different dataset licences and one shared endpoint. Preserve separate lineage, restrictions and compute records. Reject treating a new endpoint as a newly trained model or equal names as equal weights.

Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; model/registry/artifact; run/configuration; data/rights/provenance; checkpoint/final artifact; compute allocation/actuals; deployment/endpoint; time/version/reproducibility; scenario; at least 10 invariants; minimum model set; blockers. Explicitly decide whether reusable Training Recipe needs independent identity.
