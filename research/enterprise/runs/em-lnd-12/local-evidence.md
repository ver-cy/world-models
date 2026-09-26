# EM-LND-12 local synthesis

## Disposition

- Reuse and complete WM-XCT-039 Managed IT Service Graph as the host for Service Landscape.
- Treat Service Landscape as a named, tenant-scoped, time-stamped projection with artifact identity; add no business/model identifier.
- Reject a separate Service Dependency Graph because WM-XCT-037 already owns dependency edges, traversal licenses, evidence and completeness.

## Identity and mastership

WM-XCT-039 owns graph boundary, membership assertions, per-fact mastership map and authorized projections. Each fact names exactly one owning Dimension and master; unknown ownership is pending and blocks mutation.

Service Definition, logical software system, deployed instance/runtime environment and infrastructure resource remain distinct external subjects. Replacing an instance never changes Service identity. Configuration Item is a time-qualified designation over a subject, not another node type.

## Dependency semantics

WM-XCT-037 dependency edges use dependent→prerequisite direction and record kind, nature, lifecycle phase, validity interval, determination method, evidence, confidence scale and propagation license.

Declared edges come from governed manifests/catalogues/contracts; observed edges cite time-qualified discovery/flow/trace observations; inferred edges cite derivation and remain inferred until a new accountable assertion. Silence means no assertion unless a covering closed-world completeness declaration exists. Explicit non-dependency is first-class.

## Desired and observed state

Desired state remains with deployment/policy control; observed state with discovery/observability. The landscape presents both plus drift and never merges them into one current value. Missing or timed-out observation is unknown/indeterminate, not absence or failure.

## Impact and common mode

Impact traversal follows each edge's propagation license and is bounded by depth, phase, class, tenant and stop rules. Reaching a Service Definition creates only an exposure statement; consumer outcome and SLO context determine potential business impact, while the landscape never declares breach.

Negative no-impact claims require a fresh completeness declaration covering the queried scope. Missing, stale, filtered or unauthorized edges produce incomplete impact.

Common-mode analysis uses correlation edges for shared resource, supplier, site, design or control plane. These edges identify shared-fate candidates and concentration but do not propagate direct failure unless explicitly licensed. SPOF results are regenerated with rule version and trace.

## Time, tenant, federation and incidents

Effective, observed and recorded times remain separate. Membership and hosting edges have validity intervals; views answer as-of a stated instant. Identifiers are tombstoned on retirement and never recycled.

Tenant boundary is default-deny. Same names never merge across tenants without identity evidence; cached or inferred edges cannot bypass revoked projections. Incidents remain in operational/cyber/service-case masters; the landscape only references them and emits impact projections.

## Acceptance scenario

A database cluster fails. Three services have current declared functional dependencies and yield justified impact exposure. A fourth has a stale observed flow and is exposed-unconfirmed. A fifth shares a rack and is flagged as common-mode only because propagation is withheld. Missing completeness for part of the tenant makes the result incomplete rather than no further impact.

## Invariants

1. Service, system, instance/environment and resource remain distinct.
2. Every topology assertion carries effective or observation time.
3. Every edge records nature, method, evidence and confidence.
4. Inferred edges never masquerade as asserted facts.
5. Co-location does not automatically propagate impact.
6. Negative impact requires covering completeness evidence.
7. Desired and observed state remain separate.
8. Unknown mastership blocks mutation.
9. Cross-tenant merge requires authoritative identity evidence.
10. Retired identifiers remain resolvable and are not reused.
11. Incidents remain in domain owners.
12. Every view records viewpoint, scope, freshness, completeness and policy.

## Minimal completion shape

Complete WM-XCT-039 with a named landscape-view element binding viewpoint, stakeholder concerns, declared scope, tenant, snapshot/completeness and policy to a graph revision; explicit external node-class references; mandatory completeness declaration on impact outputs; and references to service/system/runtime/SLO/observation/incident masters. Keep common-mode computation in WM-XCT-037.

## Holds

WM-XCT-039 is a non-canonical single-provider draft. WM-XCT-037 has traversal and identity contradictions, empty composition contracts and stale omissions. Current publication specs for WM-ACT-004, WM-SFT-002, WM-SFT-010 and WM-SFT-016 are absent; only research checkpoints exist. Approved relation rows, executable schemas, adapters, crosswalks and fixtures are missing. This checkpoint makes no canonical completeness, installability or publication claim.
