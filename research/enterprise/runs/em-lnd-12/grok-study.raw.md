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
