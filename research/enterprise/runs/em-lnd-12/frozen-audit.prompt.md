# Frozen no-tools semantic audit — EM-LND-12

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

Disposition: PROFILE. Reuse and minimally complete WM-XCT-039 with named service-landscape views; WM-XCT-037 remains sole dependency-edge semantic authority. ServiceLandscape and ServiceDependencyGraph receive no new model or runtime identity. A second graph is rejected.

Reconciled boundary:
1. WM-XCT-039 hosts the tenant-bounded graph boundary, membership, ownership map, projection and named views; views are reproducible internal projections with no edge store, write authority or privilege.
2. WM-XCT-037 owns edge kind, nature, direction, time, evidence, confidence, propagation licence, polarity and completeness semantics; 039 exposes but does not copy them.
3. Service, software system, runtime/instance/environment, resource, SLO, observation and incident remain external masters.
4. Declared, observed and inferred edge populations are disjoint. Stale observed remains historical; inference never closes topology gaps.
5. Confirmation and propagation licence are distinct. Current impact uses only edges current at the evaluation clock and licensed for the requested polarity.
6. Common-mode/co-location/shared-site/resource/control-plane edges default to withheld propagation and identify shared fate rather than direct failure.
7. Negative or exhaustive impact requires completeness evidence for named population, tenant and time. Incomplete topology leaves an open blast radius.
8. Desired and observed are separate labeled overlays; neither overwrites the other.
9. Tenant access is default-deny at every node, edge, inference and result hop. A view name grants nothing. Federation needs an explicit 039 projection grant and creates no union graph.
10. Incident, observation and SLO owners remain external; impact projections cannot mint or mutate them.

Scenario: shared node S has three confirmed dependencies, one stale observed edge, one co-location edge and incomplete topology. Only the subset of confirmed edges with current propagation licences yields partial exposure; no dependent failure is automatic. The stale edge stays historical, co-location raises common-mode watch only, topology remains incomplete, exhaustive or unaffected claims are forbidden, and incidents stay external.

Audit questions:
- Is any hidden root, graph or identifier introduced despite `newRuntimeId=false`?
- Are graph boundary, membership, view, edge and impact-result mastership unambiguous?
- Can confirmation, licence, common mode, completeness, tenant or federation semantics still cause false propagation or disclosure?
- Are node classes and incident/SLO/observation boundaries safe?
- Identify contradictions that make even a held profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the profile.

## Candidate

```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-LND-12",
  "name": "Enterprise Service Landscape and Dependency Impact View",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-XCT-039",
    "WM-XCT-037",
    "WM-XCT-001",
    "WM-XCT-003",
    "WM-MAT-008",
    "WM-ACT-021",
    "WM-ACT-020",
    "WM-SFT-002",
    "WM-SFT-010",
    "WM-SFT-016",
    "WM-ACT-019",
    "WM-ACT-004"
  ],
  "constraints": [
    "Service Landscape is a named tenant-scoped time-stamped projection hosted by WM-XCT-039 and never receives a new business or runtime identifier.",
    "WM-XCT-037 owns dependency edge direction, type, validity, determination method, evidence, confidence and propagation license.",
    "Service definitions, logical software systems, deployed instances, runtime environments and infrastructure resources retain separate external identities.",
    "Configuration Item is an effective-dated designation over an existing subject rather than a duplicate node identity.",
    "Declared, observed and inferred dependencies remain distinguishable; inference never becomes an asserted fact without accountable authority.",
    "Silence means unknown unless a covering closed-world completeness declaration exists; explicit non-dependency is first-class.",
    "Desired and observed state remain separate and a missing or stale observation is unknown rather than absence or failure.",
    "Impact traversal obeys each edge propagation license and records depth, lifecycle phase, class, tenant and stop rules.",
    "Reaching a service creates an exposure statement only; service outcomes and SLO context determine potential business impact.",
    "Negative no-impact conclusions require fresh completeness evidence covering the full queried scope.",
    "Common-mode edges identify shared-fate candidates but do not propagate direct failure without an explicit license.",
    "Tenant access is default-deny, identifiers are never recycled and incidents remain mastered by their source domains.",
    "Named landscape views are WM-XCT-039-internal reproducible projections, not independent graphs, roots, edge stores or privileges; view caches never accept writes.",
    "WM-XCT-039 is the sole graph-boundary, membership, ownership-map and projection host; WM-XCT-037 is the sole dependency-edge semantic authority.",
    "Declared, observed and inferred edge populations are disjoint; stale observed edges remain historical observations and inferred edges never close topology gaps.",
    "Confirmation and propagation licence are distinct; only an edge current at the evaluation clock and explicitly licensed for the requested polarity may carry current impact.",
    "Common-mode, shared-site, shared-resource and shared-control-plane edges default to no propagation licence and identify shared-fate candidates only.",
    "Completeness evidence is scoped by named population, tenant and evaluation time; incomplete topology keeps the blast radius open and forbids exhaustive or unaffected claims.",
    "A view name grants no access; every hop, inference and result remains default-deny by tenant and federation requires an explicit WM-XCT-039 projection grant.",
    "Federation is a governed projection over existing masters and edges, never a union graph or reason to allocate identity.",
    "An impact projection or incompleteness warning is neither an observation, SLO evaluation nor incident record and cannot mint, own or close any of them."
  ],
  "holds": [
    "WM-XCT-039 and WM-XCT-037 require canonical completion and contradiction reconciliation.",
    "Adjacent base publications and approved relation rows remain incomplete.",
    "Executable schemas, adapters and field-level crosswalks remain pending.",
    "Grok Heavy accepted reuse of WM-XCT-039/037, rejected both new identities and required explicit projection, edge-population, licence, completeness and federation constraints."
  ],
  "version": "0.1.0-candidate.2"
}
```

## Fixtures

```json
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Service Landscape and Dependency Impact View",
  "cases": [
    {
      "id": "declared-service-impact",
      "kind": "positive",
      "input": "A failed database has current declared functional dependencies to three services, each with licensed propagation.",
      "expect": "The view reports three evidence-backed impact exposures and preserves every source edge."
    },
    {
      "id": "stale-observed-flow",
      "kind": "positive",
      "input": "A fourth service has only a stale observed flow to the failed database.",
      "expect": "The service is exposed-unconfirmed; stale evidence is visible and no current dependency is asserted."
    },
    {
      "id": "shared-rack-only",
      "kind": "positive",
      "input": "A fifth service shares a rack but its correlation edge has no failure-propagation license.",
      "expect": "The view reports a common-mode candidate without direct service impact."
    },
    {
      "id": "missing-completeness",
      "kind": "negative",
      "input": "Part of the tenant graph has no current completeness declaration and traversal finds no further edges.",
      "expect": "The result is incomplete rather than no further impact."
    },
    {
      "id": "desired-observed-collapse",
      "kind": "negative",
      "input": "A deployment manifest declares an instance healthy while monitoring is absent, and the view emits one healthy current state.",
      "expect": "The view is rejected because desired and observed state were collapsed and absence was treated as health."
    },
    {
      "id": "cross-tenant-name-match",
      "kind": "negative",
      "input": "Two identically named services in different tenants are merged without authoritative identity evidence.",
      "expect": "The merge is blocked by tenant isolation."
    },
    {
      "id": "incident-minting",
      "kind": "negative",
      "input": "A graph traversal creates a new incident record from an exposure result.",
      "expect": "The mutation is rejected; incidents remain externally mastered and the landscape returns only a projection."
    },
    {
      "id": "view-cache-write",
      "kind": "negative",
      "input": "A named landscape view writes a locally edited dependency into a view cache.",
      "expect": "The write is rejected; authoritative changes go to WM-XCT-039 membership or WM-XCT-037 edge masters."
    },
    {
      "id": "confirmed-without-license",
      "kind": "negative",
      "input": "A current confirmed functional edge lacks a propagation licence for negative impact.",
      "expect": "The edge is not traversed for that impact polarity."
    },
    {
      "id": "inferred-closes-topology",
      "kind": "negative",
      "input": "Inferred edges fill missing topology and the view reports an exhaustive blast radius.",
      "expect": "The conclusion is rejected; inference never supplies completeness evidence."
    },
    {
      "id": "federated-view-no-grant",
      "kind": "negative",
      "input": "A view unions two tenants through a shared control plane without an explicit projection grant.",
      "expect": "Cross-tenant nodes, edges and inferences remain non-visible and non-traversable."
    },
    {
      "id": "view-name-privilege",
      "kind": "negative",
      "input": "A caller sees restricted edges because it may open a named executive view.",
      "expect": "Access is denied; the view inherits the caller's tenant projection and source rights."
    },
    {
      "id": "current-confirmed-licensed",
      "kind": "positive",
      "input": "One declared and two current observed edges are confirmed and licensed at evaluation time.",
      "expect": "Only those three edges produce a partial impact exposure set, without asserting dependent failure."
    },
    {
      "id": "shared-control-plane-common-mode",
      "kind": "positive",
      "input": "Three services share a control plane through correlation edges with propagation withheld.",
      "expect": "Report common-mode exposure without propagating direct failure."
    },
    {
      "id": "landscape-mints-incident",
      "kind": "negative",
      "input": "An incomplete impact projection attempts to open and close an incident.",
      "expect": "The mutation is rejected; only the domain owner controls incident lifecycle."
    }
  ],
  "version": "0.1.0-candidate.2"
}
```

## Claude study

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


## Grok study

# Verdict

Accept the proposal. Reuse and minimally complete WM-XCT-039 with named landscape views. Allocate no new identifier. Reject a second dependency graph. Neither ServiceLandscape nor ServiceDependencyGraph requires a new model identity.

## Strongest evidence

WM-XCT-039 already owns the tenant-bounded managed service graph and already composes WM-XCT-037 Dependency/Impact plus ownership/projection. Named landscape views are that projection work. A second graph would dual-master the same declared, observed, and inferred edges and split impact evaluation. Service, software system, runtime/instance, resource, SLO, observation, and incident remain external; 039 holds references and membership, not definitional copies.

## Strongest counterexample

Operators want one picture of a shared platform that spans tenants (control-plane, site, multi-tenant resource). Default-deny makes that picture feel like a new landscape type. The need is a federated projection grant on 039 plus 037 common-mode edges, not a new graph and not ServiceDependencyGraph. An independently versioned published view-artifact is still a projection object inside 039. Minting an identity would hide a projection gap instead of completing 039.

## Identity / mastership

Neither ServiceLandscape nor ServiceDependencyGraph requires a new model identity. WM-XCT-039 masters the tenant-bounded managed service graph, node inventory, ownership, projection, and named landscape views. WM-XCT-037 masters edge semantics: kind (declared | observed | inferred), nature, time, evidence, confidence, propagation license, impact polarity, and completeness evidence for negative claims. 039 composes 037 and must not redefine 037 fields. View objects may carry local names and publication metadata inside 039; they are 039-internal named projections, not a graph and not a new model identity. A view cache is not master. Writes go to 039/037, never to the view.

## Node boundaries

Keep four external types distinct: Service (offered capability); software system (design-time/deployable); runtime/instance/environment (running manifestation); resource (consumed or shared capacity, site, or control-plane). Collapsing any pair makes common mode indistinguishable from functional dependency. A shared node is a resource or shared runtime/control-plane; dependents do not retype it as Service. SLO, observation, and incident stay off the graph as first-class members. 039 references external types and does not absorb their mastership.

## Dependency semantics

Edges belong to three disjoint populations: declared, observed, inferred. Every edge records nature, time, evidence, confidence, and propagation license. Confirmed means live membership in declared or currently-valid observed population plus evidence and confidence above threshold. Confirmation is not a propagation license. Nature is independent of population. Inferred edges are hypotheses; they never substitute for declared or observed and cannot close a topology during evaluation.

## Desired / observed state

Desired is declared topology, intended view membership, and intended licenses. Observed is discovered edges with last-evidence time and staleness. Populations do not overwrite each other; divergence is a first-class condition. Views may project either or both, labeled as such, and must not collapse them. Stale observed remains observed, with time and confidence decay; it cannot be promoted to declared.

## Impact / common mode

Impact polarity travels only along edges that are confirmed at the evaluation clock, carry an explicit propagation license for that polarity, and survive tenant default-deny. Negative impact is illegal without completeness evidence for the named population and time window. Shared-resource, site, and control-plane edges identify a shared failure domain. They do not automatically propagate failure. Common mode is not functional dependency and is not a licensed impact path. Incomplete topology yields an open blast radius; “unaffected” and exhaustive-dependent claims are forbidden.

## Time / tenant / federation

Every edge carries time; impact is evaluated at an explicit clock; completeness is time-scoped. Tenant boundary is default-deny for nodes, edges, views, inferences, and impact traversal. Absence of grant is non-visible, non-traversable, and not impact-eligible. Observed discovery on a shared plane does not punch a tenant boundary. Inferences cannot cross tenants. A view name is not a privilege; views inherit the caller’s tenant projection. Federation is an explicit 039 projection grant, not a union graph and not a new identity.

## Incident boundary

Incident, observation, and SLO stay with domain owners. 039 and its views may be consumed by an incident process; they do not mint, own, or close incidents. Node failure plus impact assessment plus incompleteness warning is not an incident record.

## Scenario

Shared node S is a resource/site/control-plane, not a Service. Three confirmed dependencies are impact-eligible only if each still carries a current propagation license; licensed dependents are candidates, not automatically failed. One stale observed edge is excluded from the confirmed set and from current impact; it remains historical observed. One co-location edge raises a common-mode watch on peers and does not propagate S’s failure unless it separately carries a license (by default it does not). Topology is incomplete, so there is no completeness evidence: negative impact is forbidden, the blast radius stays open, “only three dependents” is not exhaustive, and inferred fill-in during the incident is forbidden. Result: partial licensed impact set from a subset of the three confirmed edges, common-mode watch on co-location, explicit incompleteness warning. Incidents remain with domain owners.

## Invariants

1. Neither candidate is allocated a new model identity.
2. WM-XCT-039 is sole master of the tenant-bounded managed service graph, node inventory, ownership, projection, and named landscape views.
3. WM-XCT-037 is sole master of edge semantics.
4. Service ≠ software system ≠ runtime/instance/environment ≠ resource; 039 does not absorb their mastership.
5. SLO, observation, and incident remain external.
6. A named landscape view has no independent graph, edge store, or privilege.
7. Tenant boundary is default-deny for nodes, edges, views, inferences, and impact traversal.
8. Declared, observed, and inferred edges are disjoint; neither overwrites another.
9. Desired and observed remain separate overlays; views must label the projected population.
10. Confirmed ≠ licensed; only currently confirmed and licensed edges may carry current impact.
11. Stale observed ≠ confirmed; it cannot carry current impact or be rewritten as declared.
12. Negative impact requires completeness evidence for a named population and time window; incomplete topology cannot yield “no impact” or a closed blast radius.

## Minimum completion shape

Complete 039 only: named landscape view records (name, audience, filter predicate, tenant scope, as-of time, projected population label, completeness declaration); node-role constraints for the four external types; default-deny projection rules (view name ≠ grant); composition surface that exposes 037 fields without copying them; observed-edge validity/staleness window owned by 037 and projected by 039; impact evaluation using 037 licenses plus completeness evidence, with the 039 view supplying the scoped population; common-mode natures defaulting to no propagation license; external reference slots only. No second edge store. No ServiceDependencyGraph type.

## Blockers

Allocating an identity to either candidate. Dual-writing edges into a view-local graph. 039 redefining 037 fields. Collapsing Service/system/instance/resource. Treating common-mode or co-location as auto-failure-propagation. Negative impact without completeness evidence, or a closed blast radius on incomplete topology. Counting stale observed or inferred edges as confirmed or current impact paths. Absorbing incident, SLO, or observation. Cross-tenant visibility or inference without an explicit 039 grant. Unlabeled collapse of desired and observed. Using a view name as a privilege bypass. Treating federation need as justification for a new identity.

