# Independent review request: EM-LND-05 Project, program and portfolio landscape

Review this Enterprise boundary independently. Use public portfolio/program/project and allocation practice where useful. Distinguish standards evidence from design inference. Do not invent a Vercy identifier.

Current candidates:

- WM-ACT-029 Program / Portfolio owns root identity, membership, dependencies, prioritization, allocation decisions, benefit logic and aggregate evaluation while component masters remain external.
- WM-ACT-005 Project owns project identity, scope, baseline, cost facts, resource commitments and lifecycle.
- Both are published reviewable drafts with publication holds.

Proposed decision: **PROFILE**, no new ID. DeliveryLandscape is a read-only projection. DeliveryScope stays with the owning root. A tracker container is not a project unless it resolves to an authoritative WM-ACT-005/029 identity.

Membership roles are proposed as `financial-consolidating`, `coordination-only` and `reporting-only`. One project may belong to multiple roots, but only one financial-consolidating membership may apply per fiscal period and cost dimension. Project–Product and Project–Team edges are M:N references.

Cost is asserted once by the project for a pinned baseline/period/currency/data date. Every view deduplicates source facts before applying allocation shares. Product and team allocations are orthogonal decompositions and cannot be added. Benefits distinguish additive exclusive attribution from non-additive contribution claims.

Test:

1. A portfolio contains a project directly and through a program; naive traversal counts its budget twice.
2. One project serves two products using four teams while retaining one cost fact.
3. A team is overcommitted across projects.
4. A scenario view is mistaken for authoritative actuals.

Return at most 1000 words with: Verdict; identity/lifecycle test for Landscape and Scope; membership/allocation semantics; cost and benefit rules; scenario results; missing relations/fields; publication blockers.
