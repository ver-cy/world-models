# EM-TEC-04 — Independent Review

## Verdict
**Extend-by-completion into WM-SFT-010, not new, not WM-SFT-002.** EM-TEC-04 is the subject home for `RuntimeEnvironment`, `InfrastructureResource`, `DeployedInstance` and `HostingRelation`. `ConfigurationItem` is rejected as a fifth class and readmitted as an effective-dated *designation* over a referenced subject. WM-SFT-010 is reserved, wave-1, parented to WM-SFT-002, and has **no specification file**, so this contour supplies its missing content rather than founding a competing model. WM-XCT-039 is `REFERENCE`/compose-only (mastership, projection, bounded impact), never the inventory. WM-SFT-009 stays the deployment *occurrence*. Boundary decision: `extend` (complete the reserved candidate); no new registry ID is proposed or invented.

## Evidence
WM-SFT-009 explicitly out-of-scopes "runtime environment definition, topology, capacity, infrastructure inventory and environment lifecycle (owned by WM-SFT-010)" and keeps `de-instance-refs` / `de-placement-regions` inline as correlation keys only — a declared hole exactly the size of EM-TEC-04. The frozen relation rows already give `WM-SFT-009 → WM-SFT-010` ("Deployment targets a runtime environment"), both `candidate`. Legacy WM-SFT-002 carries only `environment` (environmentType, locationRef, platform) and `deployedSystem` with a single `hostedIn` edge — too coarse, and EM-TEC-02 already resolved installations *out* of WM-SFT-002 into current deployment plus runtime environment. WM-XCT-039 supplies per-fact mastership, desired-versus-observed retention, identity-anchor and bounded-impact semantics, but scope_statement forbids it becoming "a competing CMDB", and its coverage marks validation a `gap`.

## Identity/mastership
- **RuntimeEnvironment** — governed, long-lived logical execution context. Identity from the environment registry/CMDB master; `environment_kind`, `region`, `capacity`, `isolation_policy` are attributes, not keys. Independent of member resources.
- **InfrastructureResource** — capacity-bearing node, VM, volume, cluster or network. Identity from the provider/hardware master (cloud resource id, Redfish-class identity per SRC-005 pattern). Hostname and address are observed attributes.
- **DeployedInstance** — one running incarnation. Identity is `instance_key` minted by the runtime, plus `service_scope`; masters are the orchestrator and observability. Mandatory pinned reference to an artifact version and, where known, the deployment occurrence.
- **ConfigurationItem** — a control assertion ("this referenced subject is under configuration control"), with its own validity interval, declaring authority and CMDB mastership. It designates; it does not exist alongside its subject as a twin.
- **HostingRelation** — reified, effective-dated, source-qualified edge, never a derived join of current state.

Routing follows WM-XCT-039: desired state → Git/CI-CD; observed state → observability/discovery; CI designation and control scope → CMDB; commercial/physical facts → asset and finance masters. Exactly one master per fact path; unknown mastership is `pending` and blocks mutation.

## Environment/resource/instance/CI
Four different lifecycles, deliberately not collapsed. An environment is *commissioned and retired* by governance; a resource is *provisioned and released* by a provider; an instance is *started and terminated* by a scheduler; a CI designation is *asserted and withdrawn* by a control regime. `operational_status` belongs to each separately and must not be propagated upward. A healthy environment can contain failed instances; a retired environment can retain live CI designations pending decommission evidence.

## Hosting and topology
`HostingRelation` carries subject, host, relation kind (runs-on, member-of, backed-by, served-by), `validFrom`/`validTo`, assertion kind (declared / observed / inferred), confidence and `observed_at` with source. Topology is therefore a temporal graph; "what hosts X now" is a projection, not stored truth. Placement facts reported by WM-SFT-009 (`de-placement-regions`) are *per-occurrence outcomes* and must not accrete into environment inventory — that direction of drift is the specific leak to police.

## Ephemeral history
Ephemeral resources are handled by append-only records with closed intervals, never by deletion or identifier reuse. Rules: identifiers are minted once and retired with a tombstone retaining `instance_key`, artifact version reference, environment reference, `region`, interval and terminal status; a successor gets a new identity plus an explicit succession edge; short-lived instances anchor to durable parents (environment plus `service_scope`), so history survives even when every instance has turned over. Aggregate views may summarise generations, but the ledger, not the summary, answers historical impact. Absence of an observation is not absence of a resource.

## Asset boundary
They **reference**; they do not merge. Distinct masters (fixed-asset register versus CMDB/discovery), distinct lifecycles (capitalisation, depreciation, disposal versus commissioning, decommission), distinct granularity (one chassis asset ↔ many CIs; one logical-cluster CI ↔ many assets; leased or cloud resources have no owned asset at all). They *coincide referentially* only when a single owned physical unit is simultaneously capitalised and under configuration control — and even then two records persist, joined by an effective-dated co-designation link carrying identity evidence. Sharing one identifier imports finance disposal semantics into operations and would let a depreciated-but-running node vanish from the impact graph. Financial questions route to EM-FIN-05; EM-TEC-04 holds only the link and its evidence.

## Cluster/node
A logical cluster is a first-class `InfrastructureResource` (or environment, by `environment_kind`) with its own identity, declared `capacity` and `isolation_policy`. Nodes are members through effective-dated `HostingRelation` membership. Cluster identity never depends on the member set, so full node replacement is a membership change, not re-identification. Services depend on the cluster by *declaration* and on nodes by *observation*; both edges are kept, distinguished by assertion kind. A cluster must not be aliased to its control-plane endpoint or VIP.

## Scenario
Service S (WM-SFT-002) has environments `prod-eu` and `prod-us` (`region` differs, `service_scope` shared). A shared cluster C is referenced by both via `HostingRelation` — cross-region reference, not duplication. At T1 node N1 is a member and hosts instances I1..I3; at T2 N1 is retired and N2 joins; at T3 new instances I4..I6 run the same artifact version. Impact as-of T1 returns C, N1, I1..I3; as-of T3 returns C, N2, I4..I6; S's identity, and each environment's identity, are unchanged throughout. An incident at T1 stays attributable to N1 after retirement because the interval and tombstone survive. Where an edge is missing or stale the answer is *incomplete impact*, never *no impact*.

**Negative case rejected.** IP as sole eternal server identity fails on reassignment, DHCP, dual-stack, multi-homing, shared VIPs, overlay reuse and cross-tenant address recycling — the last producing a false merge across tenants. Address is an effective-dated observed endpoint binding, consistent with EM-TEC-03.

## Invariants
1. Every `DeployedInstance` references exactly one pinned artifact version.
2. Every observation carries `observed_at`, source and method; effective, observed and recording time stay separate.
3. Address or endpoint change never changes identity; identity change requires a new record plus a succession edge.
4. Every `HostingRelation` carries validity interval and assertion kind.
5. Identifiers are never recycled; retirement produces a tombstone, not a delete.
6. Environment and cluster identity are independent of member resources.
7. A CI designation and an asset record never share an identifier.
8. Desired and observed state are stored separately; discrepancies are retained.
9. Impact answers are as-of-time and carry a completeness boundary.
10. One environment per region-scoped context; environment identity is not service identity.

## Minimal completion shape
For the WM-SFT-010 specification: (1) identity and classification of environment, resource and instance; (2) inventory, `capacity` and `isolation_policy`; (3) effective-dated hosting and membership topology; (4) desired-versus-observed state with retained drift; (5) designation and asset-linkage layer (CI plus co-designation evidence); (6) history, retirement and tombstones; (7) mastership, projection and access, composed from WM-XCT-039; (8) alignment records (no conformance claims). Registry actions: deprecate the legacy WM-SFT-002 `environment` and `deployedSystem` objects with a migration mapping; promote the two candidate WM-SFT-009 relation rows; add the missing WM-SFT-010 ↔ WM-XCT-039 ledger row — it does not exist in the frozen relations and must not be assumed.

## Holds
WM-SFT-010 has no specification file, so every mapping here is a conceptual candidate on index and publication metadata only; the semantic crosswalk is unverified. WM-XCT-039 is a single-provider Codex-only reviewable draft with external review waived and executable validation deferred; WM-SFT-009 is a Claude-only reviewable draft with live source re-pin, ledger and coverage-downgrade holds; WM-SFT-002 is a described-previous-version record under migration boundary review. No fixtures were run. This review claims neither canonical completeness nor installability.
