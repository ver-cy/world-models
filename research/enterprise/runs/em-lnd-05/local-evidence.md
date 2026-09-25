# EM-LND-05 local synthesis

## Disposition

- Create a **Project, Program and Portfolio Landscape profile** over WM-ACT-029 with component resolution through WM-ACT-005.
- Do not create a catalogue/runtime identifier.
- DeliveryLandscape is a read-only projection; DeliveryScope is already owned by the corresponding program/portfolio or project.

## Boundary

The view owns no project, program, portfolio, product, team, cost, benefit, resource or membership assertion. WM-ACT-029 owns program/portfolio membership, prioritization, dependencies, allocation decisions and benefit logic. WM-ACT-005 owns project identity, baseline, cost facts, resource commitments and project scope.

A tracker project, board or epic tree is only a tooling container unless it resolves to an authoritative project or program/portfolio identifier.

## Membership and allocation

One project may participate in multiple roots. Each membership requires a role: `financial-consolidating`, `coordination-only` or `reporting-only`. At most one financial-consolidating membership may apply to a project, fiscal period and cost dimension.

Project–Product and Project–Team edges are M:N references. Products and teams retain their own masters. Resource contention is recorded against the resource owner's capacity and can only be displayed by the landscape.

Cost is asserted once by the project for a pinned baseline, period, currency, price base and data date. Views apply declared allocation shares after deduplicating the source fact. Benefit claims distinguish additive exclusive attribution from non-additive contribution.

## Invariants

1. Every node resolves to an authoritative project or program/portfolio ID.
2. Views never store monetary or benefit facts.
3. Roll-up deduplicates source facts before summation.
4. Allocation shares total at most 1.0 per fact/period/dimension.
5. Orthogonal decompositions, such as product and team, are not summed together.
6. Contribution claims are non-additive.
7. Project–Product and Project–Team remain M:N.
8. Every view declares authoritative, as-of replay or scenario class with exact time and criteria pins.
9. Scenario results cannot feed authoritative actuals or benefit realization.

## Acceptance result

One project serving two products and four teams retains one project cost fact. A product view may allocate it 60/40; a team view may separately decompose it by effort, but those views cannot be added. Shared team capacity conflicts remain owned by the resource source. A portfolio containing a program and its project directly still counts the project fact once.

## Holds

Both bases remain `publishableCanonical: false`. WM-ACT-029 relation rows are unapproved, the membership-role discriminator lacks source grounding, and cross-root deduplication scope needs validation. Program/programme artifact naming is unresolved. This checkpoint is not an installable release.
