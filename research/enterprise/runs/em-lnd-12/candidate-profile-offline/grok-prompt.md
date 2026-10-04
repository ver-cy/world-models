# Exact unsent Grok prompt — EM-LND-12

Independent enterprise metamodel review. Do not browse, invent identifiers or claim standards conformance.

EM-LND-12 covers ServiceLandscape and ServiceDependencyGraph. WM-XCT-039 already owns a tenant-bounded managed service graph and composes WM-XCT-037 Dependency / Impact plus ownership/projection models. Service, software system, runtime/instance, resource, SLO, observation and incident boundaries are external.

Assess this proposal: reuse and minimally complete WM-XCT-039 with named landscape views; allocate no new ID; reject a second dependency graph because WM-XCT-037 owns edge semantics. Keep Service, system, instance/environment and resource distinct. Edges are declared, observed or inferred and record nature, time, evidence, confidence and propagation license. Negative impact requires completeness evidence. Shared-resource/site/control-plane edges identify common mode without automatically propagating failure. Tenant boundary is default-deny, desired and observed state remain separate, and incidents stay with domain owners.

Test failure of a shared node with three confirmed dependencies, one stale observed edge, one co-location edge and incomplete topology. Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; node boundaries; dependency semantics; desired/observed state; impact/common mode; time/tenant/federation; incident boundary; scenario; at least 10 invariants; minimum completion shape; blockers. Explicitly decide whether either candidate requires a new model identity.
