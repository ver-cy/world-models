# EM-LND-12 — Service and Infrastructure Landscape: boundary decision

## Verdict

**Reuse and complete WM-XCT-039; allocate no new model identifier for either candidate type.**

- **ServiceLandscape** — no independent identity. It is a viewpoint-bound, tenant-scoped, time-stamped *projection* of WM-XCT-039, produced by `project-graph` under WM-XCT-003 disclosure policy. WM-XCT-039 must be **completed** with an explicit named-view element (viewpoint, stakeholder concerns, declared scope, snapshot reference, completeness) so the landscape is a first-class citable artifact rather than an ad-hoc query result.
- **ServiceDependencyGraph** — **rejected as a separate object.** Edge grammar, direction, typing, conditions, evidence, propagation licences and completeness are already owned by WM-XCT-037, which WM-XCT-039 composes as `required: true`. A second graph model would fork edge identity and completeness semantics.

WM-XCT-039 is the correct host because its accepted boundary already names tenant isolation, service/asset references, dependencies, desired-versus-observed state, per-fact mastership and authorised projections, and explicitly refuses to become a competing CMDB.

## Evidence

WM-XCT-039 spec (sha256 40cf1331…, 85 495 B), `boundary-reviewed`, `entry_kind: aggregate`, composition to `vr.wm-xct-001`, `vr.wm-xct-003`, `vr.wm-xct-037` all required; bundles `boundary-bundle`, `graph-bundle`, `mastership-bundle`, `exchange-bundle`. WM-XCT-037 spec (sha256 5b2c9f81…) supplies `dep-tech-relation-nature`, `dep-tech-propagation`, `dep-graph-completeness-declaration`, `dep-graph-propagation-exclusion`, `dep-evd-completeness-unknown`, `dep-res-redundancy-correlation`, `dep-res-spof-concentration`. Prior contours EM-PRD-02, EM-TEC-02, EM-TEC-04, EM-TEC-05, EM-TEC-06 fix the adjacent node boundaries; EM-TEC-04 already directs WM-SFT-010 to reuse WM-XCT-039 by reference. Both target specs are `publishableCanonical: false`, single-provider.

## Identity/mastership

Landscape identity = tenant + declared service scope + graph revision. View identity = graph revision + viewpoint + recipient/purpose + generation instant, pinned by digest. Neither identity is derived from a node name, an address or a date.

Per-fact mastership follows WM-XCT-039 `master-layer`: exactly one owning Dimension and master system per fact; unknown ownership is **pending** and blocks mutation of that fact. Service Definition facts master in WM-ACT-004; logical system/application facts in WM-SFT-002; runtime, resource, instance and hosting facts in WM-SFT-010; deployment occurrences in WM-SFT-009; SLO policy and evaluations in WM-SFT-016; observations in WM-MAT-008; edges in WM-XCT-037. The landscape masters only the graph boundary, the membership assertions, the mastership map and its own projections.

## Node boundaries

Four node classes stay disjoint, each with its own key and lifecycle:

1. **Service Definition** (WM-ACT-004) — provider-accountable promise: expected outcome, consumer scope, accountable provider. Carries no runtime state.
2. **Software system / business application** (WM-SFT-002) — operator-side logical boundary with named owner, purpose, criticality; many-to-many with both services and installations.
3. **Deployed instance / runtime environment** (WM-SFT-010) — `DeployedInstance` (runtime-issued key + pinned artifact version) and `RuntimeEnvironment` (governed environment key), joined by effective-dated `HostingRelation`.
4. **Infrastructure resource** (WM-SFT-010) — provider or hardware-master key; provisioned/released.

Replacing an endpoint or instance does not change Service identity. A ConfigurationItem is an effective-dated *designation* over a referenced subject, not a fifth node.

## Dependency semantics

Every edge is a WM-XCT-037 assertion in canonical direction dependent → prerequisite, carrying: kind, **nature** (functional requirement / resource consumption / compatibility constraint / ordering / co-location-correlation), lifecycle phase, validity interval, determination method, evidence reference, confidence with named scale, and a propagation licence.

- **Asserted (declared)** — stated in a manifest, service catalogue, topology declaration or contract.
- **Observed (discovered)** — derived from a WM-MAT-008 observation, discovery scan, flow record or trace, with `phenomenonTime` and `resultTime` distinct.
- **Inferred** — heuristic or model-derived; modality discriminator plus derivation basis mandatory; never promotable to direct without a fresh agent assertion.

Silence is not absence: an unstated edge is `noAssertion` unless a covering completeness declaration with closed-world flag exists. Explicit non-dependency is a first-class negative assertion.

## Desired/observed state

Desired state masters in deployment/policy control; observed state masters in discovery and observability; the landscape stores both plus the drift, never a merged "current" value. Only authoritative confirmation updates the observed projection. An API timeout is **indeterminate**, not proof of failure — reconcile before retrying non-idempotent operations. A missing observation is unknown, not absent. `observed_at` and `desired_state` from the v1 property set map onto `state-layer` and remain candidate-not-normative.

## Impact and common mode

Impact traverses edges in the direction the per-kind licence permits — generally opposite to the dependency arrow — bounded by depth, phase, referent class and tenant boundary, with stop conditions at platform-provided targets and Dimension boundaries. Reaching a Service Definition converts reachability into a business-outcome statement only through that service's expected outcome and consumer scope, and degradation is expressed against WM-SFT-016 objectives, never asserted as breach by the landscape.

The controlling asymmetry: a positive reachability claim needs only the traversal record; **any** no-impact or not-affected claim additionally requires a resolvable completeness declaration covering the queried scope. Missing, stale, filtered or inaccessible dependencies yield *incomplete impact*, never an unsupported negative.

Common-mode detection uses `dep-res-redundancy-correlation`: shared resource, shared supplier, shared site, shared design or shared control plane reducing effective independence, with concentration measures and a regenerated (not patched) SPOF determination carrying its rule version and trace. Co-location and correlation edges carry a **withheld** propagation licence and are reported as shared-fate candidates, not as impact.

## Time/tenant/federation

Effective, observed and recorded time are kept separate; all instants RFC 3339 with seconds and explicit offset. Topology is a temporal projection: every membership and hosting edge has a validity interval, so an impact query is answered *as of* a stated instant, and retired identifiers are tombstoned, never recycled. Tenant boundary is default-deny: identical asset names in different tenants must not merge without authoritative identity evidence, inferred edges are subject to the same projection rights as asserted ones, and a cached or inferred edge must not bypass a revoked projection.

## Incident boundary

Incidents stay with their domain owners: WM-ACT-020 for cyber incidents, WM-ACT-019 (profiled) for operational incidents, WM-ACT-021 for service cases, with problem and defect records outside this contour. The landscape holds typed references and impact projections only; an impact projection is not an incident declaration, and incident closure never mutates graph facts.

## Scenario

A shared database cluster node fails at T. The landscape resolves, as of T: declared edges from three services to the cluster (functional requirement, runtime phase), one observed edge from a fourth service seen in a flow record 41 days old, and one co-location edge for a fifth service on the same rack.

Result: the three declared dependents yield justified impact with named consumer scopes and SLO exposure. The fourth is returned as **exposed-unconfirmed** — stale beyond horizon, confidence stated, not counted as impacted. The fifth is reported as shared-fate/common-mode only, with propagation licence withheld. Two services in the tenant carry no completeness declaration, so the answer is `incomplete`, not "no further impact". Common-mode analysis flags the cluster as a concentration point for all three, with the SPOF verdict regenerated and contestable.

## Invariants

1. Service and instance are distinct identities; an instance is never a service.
2. Every topology and membership assertion carries an observation or effective date.
3. Incidents are stored by their domain owner; the landscape references only.
4. Every edge declares nature, determination method and evidence; co-location never propagates.
5. Unknown mastership is pending and blocks mutation of the affected fact.
6. No negative impact claim without a covering, current completeness declaration.
7. Desired and observed state are never merged; drift is retained.
8. Identifiers are not recycled; retirement leaves a resolvable tombstone.
9. Cross-tenant merge requires authoritative identity evidence.
10. Every projection records viewpoint, scope, completeness, freshness and policy version.

**Negative case rejected:** a server link — hosting, network reachability, shared rack, or a single observed connection — does not prove full service dependency. It establishes at most a resource or co-location relation of stated nature and confidence, phase-scoped and time-bounded; promotion to functional requirement requires a declared or evidenced functional edge.

## Minimal completion shape

Add to WM-XCT-039, without new identifiers: (a) a named landscape-view element under `exchange-bundle` binding viewpoint, concerns, declared scope and completeness to a graph revision; (b) explicit node-class typing in `boundary-bundle` referencing WM-ACT-004, WM-SFT-002 and WM-SFT-010; (c) a completeness-declaration requirement on every impact projection in `impact-layer`; (d) common-mode and concentration reporting delegated by reference to WM-XCT-037 rather than restated; (e) REFERENCE links to WM-ACT-004, WM-SFT-002, WM-SFT-010, WM-SFT-016, WM-MAT-008, WM-ACT-019, WM-ACT-020, WM-ACT-021.

## Holds

WM-XCT-039 is single-provider (Codex) with Claude and Grok waived, `publishableCanonical: false`, and defers executable schemas and adapters. WM-XCT-037 carries an unresolved internal contradiction between its traversal-forbidding scope and its traversal-performing functions, an identity-strength contradiction, an empty composition contract and a stale omissions register. WM-ACT-004, WM-SFT-002, WM-SFT-010 and WM-SFT-016 have no current specification; the relation ledger holds no approved EM-LND-12 edges. Crosswalks to ArchiMate and ISO 42010 are unverified. No canonical completeness and no installability is claimed.
