# EM-TEC-04 local synthesis

## Disposition

- Complete reserved WM-SFT-010 as **Runtime / Compute Environment**, owning RuntimeEnvironment, InfrastructureResource, DeployedInstance and effective-dated HostingRelation semantics.
- Keep WM-SFT-002 as the logical Software System / Business Application master and WM-SFT-009 as Deployment occurrence. Migrate the coarse legacy `environment` and `deployedSystem` structures out of WM-SFT-002.
- Reuse WM-XCT-039 by reference for per-fact mastership, desired-versus-observed separation, identity anchors and bounded impact projections. It does not become an inventory or CMDB.
- Model ConfigurationItem as an effective-dated designation over a referenced subject, under a configuration-control authority. It is not a duplicate twin of the resource or instance.
- Keep financial and physical asset records in their own masters; relate them to configuration items with evidenced, effective-dated links.
- Allocate no new runtime or model identifier.

## Identity and lifecycle

| Subject | Stable identity and lifecycle |
|---|---|
| RuntimeEnvironment | Governed environment key; commissioned, changed and retired independently of members |
| InfrastructureResource | Provider or hardware-master key; provisioned and released |
| DeployedInstance | Runtime-issued instance key plus service scope; started and terminated |
| ConfigurationItem designation | Referenced subject, control authority and validity interval; asserted and withdrawn |
| HostingRelation | Reified subject-host edge with kind, validity, source and assertion kind |

Environment kind, region, capacity, isolation policy, hostname and network address are attributes or observations, not eternal identifiers. Every DeployedInstance references a pinned artifact version and, when known, the WM-SFT-009 deployment occurrence.

Desired state belongs to Git or deployment control; observed state belongs to discovery and observability; CI designation belongs to the CMDB; provider resource identity belongs to the provider inventory. Unknown mastership remains pending and blocks mutation.

## Temporal topology and ephemeral history

HostingRelation represents runs-on, member-of, backed-by and served-by edges with `validFrom`, `validTo`, declared/observed/inferred status, source, confidence and observation time. Current topology is a projection of this temporal graph.

Ephemeral resources receive non-recycled identifiers. Termination closes their interval and retains a tombstone containing the key, artifact, environment, region, terminal state and durable parent references. A replacement receives a new key and an explicit succession link. Missing observation means unknown, not absent.

## Asset and cluster boundaries

A fixed asset and a configuration item remain separate even when they refer to the same physical unit. They have different masters, granularity and lifecycle. A chassis may relate to several CIs; a logical cluster CI may span many assets; cloud resources may have no owned asset. The relation carries identity evidence and an effective period.

A logical cluster is an InfrastructureResource, or an environment when it is itself the governed execution context. Its identity does not depend on nodes or control-plane endpoints. Nodes join and leave through temporal membership edges. Services depend on the cluster by declared topology and on nodes by observed placement.

## Acceptance scenario

One service retains its WM-SFT-002 identity across EU and US environments. A global logical cluster has regional resource pools; node N1 is replaced by N2 while deployment and instance histories retain their original intervals. An impact query as of T1 returns N1 and its instances; the same query at T3 returns N2 and successor instances. The service, environments and cluster keep their identities. Missing or stale edges reduce declared completeness instead of producing a false no-impact answer.

## Invariants

1. Every DeployedInstance references exactly one pinned artifact version.
2. Every observation carries time, source and method; effective, observed and recorded times remain distinct.
3. Address change does not change identity.
4. Every HostingRelation has a validity interval and assertion kind.
5. Identifiers are never recycled; retirement retains a tombstone.
6. Environment and cluster identity are independent of member resources.
7. A CI designation and asset record do not share an identifier.
8. Desired and observed state remain separate and drift is retained.
9. Impact answers are time-qualified and state their completeness boundary.
10. Environment identity is distinct from service identity.

## Holds

WM-SFT-010 has no current specification; WM-SFT-002 remains a shared legacy migration source; the WM-SFT-010 relation to WM-XCT-039 is absent; WM-SFT-009 relationship rows remain candidate; crosswalks, source pins and temporal fixtures are incomplete. WM-XCT-039 and WM-SFT-009 retain their own provider and validation holds. This checkpoint makes no canonical completeness, installability or publication claim.
