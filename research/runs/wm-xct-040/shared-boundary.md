# Independent study: Vercy EM-KRN-01 composition and installation contract

The owner asks Codex, Claude and Grok to deeply research one reusable Enterprise meta-model, implement it, test it and publish it on ver.cy. This request authorizes research of public standards and generic synthetic examples. No private company records are supplied. Your output is evidence, not publication authority. Do not delegate to another model.

Study boundary: a domain-neutral Composition Resolution / Model Installation Contract for a sovereign Vercy Dimension. The kernel owns identity, provenance, authority and runtime records. This contract records requested model versions, exact dependency closure, verified bytes, semantic-vs-executable readiness, compatibility and installation outcomes. Enterprise Landscape is a domain composition above the kernel, not a replacement kernel. ELMM is a repository proposal, not currently a verified installable runtime package.

Candidate concepts, to accept/split/reuse/reject with reasons: ModelReleaseReference, DependencyEdge, ResolutionRequest, ResolutionPlan, RuntimeBinding, InstallationReceipt, KernelBoundaryDecision. They may be records in one bounded resolution aggregate rather than seven standalone models. Keep package dependency graph, object relationship graph and deployment/file graph distinct. Do not make the kernel import Employee, SoftwareProduct or Contract just to be universal. A proposed new catalogue ID is not assigned yet; an extension or shared contract is also acceptable.

Observed public implementation issue (treat as supplied evidence, verify where accessible): the Vercy 0.4 reconcile_models.py downloads AGENTS.md and spec.yaml, verifies spec SHA-256 and writes vercy.lock. Its registry entry only has id/name/version/status/location. The current V1-V3 validator requires id/version/agents/specification/runtimeSchema/specificationDigest, resolves local files, verifies spec digest and evaluates explicitly declared runtime fact paths. Most published semantic specifications do not contain a native runtime binding. Generating an empty or permissive runtime schema merely to pass would be misleading. Native V3 validation validates top-level fact value type and unit, not arbitrary nested domain-object semantics. A separate domain validator is necessary for structured snapshots. The existing downloader also updates four files sequentially, has no shared writer lock, allows a sanitized filename collision and silently repins versions without migration. We need a robust bounded replacement or successor, not weaker validation.

Public Vercy references, inspect when accessible and label inaccessible rather than inventing content:
- https://ver.cy/AGENTS.md
- https://ver.cy/enterprise/RESEARCH-PROTOCOL.md
- https://ver.cy/enterprise/models/em-krn-01/brief.json
- https://ver.cy/model-agent-protocol.md
- https://ver.cy/models/runtime-index.json
- https://ver.cy/skills/vercy/scripts/reconcile_models.py
- https://ver.cy/skills/vercy/scripts/validate_dimension.py
- https://ver.cy/schemas/dimension/1.0/runtime-model.schema.json
- https://ver.cy/models/wm-org-017-performance-objective-review/NATIVE-REFERENCE.md

Compare at least three approaches using primary sources: JSON Schema 2020-12 resolution/dialects, OCI content descriptors/image manifests or package lockfile practice, W3C PROV / semantic provenance. Consider SemVer limits, digest integrity versus publisher authenticity, trusted registry origin, schema reference closure, cyclic required dependencies, optional dependencies, unknown dependencies, namespace collision, version conflict, downgrade, mutable aliases, stale plans, same-version changed bytes, path traversal, partial writes, concurrent installs, policy denial and offline verification. Do not claim certification or legal guarantees.

Acceptance profiles: (1) three-person startup adds one company model with no HR/ERP; (2) international group resolves two compatible independent model families with scoped namespaces; (3) AI organization adds a model with nested structured facts and must run its companion validator. Use fictional identifiers only. Domain models are external inputs, never imports into the composition kernel.

Requested substantive output (roughly 2500-4500 words, compact tables welcome):
1. Object boundary and reuse/extend/new decision; type definitions, identities, lifecycle and cardinalities.
2. At least 15 concrete research/use questions and artifact routes; minimal versus extended profile.
3. Exact proposed contract fields and a small valid JSON example. Distinguish specification version, contract version, object revision, release lifecycle and research assurance.
4. State machine and guards; writer/mastership, purpose/access, valid/knowledge time, provenance, conflicts; per-type whole-object five-facet coverage.
5. At least 12 executable invariants, including at least 10 nontrivial negative fixtures, plus positive profiles, historical correction, repeated import, policy denial, round-trip and explicit migration/refusal cases.
6. Precise recommendation for semantic-only versus native-ready installation: where records live, whether native registry should include packages without bindings, how lock metadata stays explicit, how readiness evidence is scoped, how a transaction and recovery work. Preserve existing validator strength.
7. Source ledger with exact URLs, document versions/sections, observed versus inference/proposal/unverified. State what you could actually read. Give licensing cautions for copied schemas; original implementation is preferred.
8. Most dangerous weaknesses and the smallest credible publishable implementation. Distinguish demonstrated readiness from future production integrations.

You are an independent researcher. Do not echo an imagined consensus. Challenge this boundary and recommend a smaller one if necessary. An honest explicit limitation is better than a universal claim.
