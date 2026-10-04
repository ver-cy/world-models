# EM-WRK-04 local synthesis

## Disposition

- Profile **Portfolio** on WM-ACT-029 under the mandatory Program / Portfolio discriminator; create no portfolio root.
- Treat PortfolioComponent, Prioritization, InvestmentAllocation and PortfolioScenario as addressable, effective-dated releases owned by the Portfolio aggregate.
- Propose an identifier-unassigned **Selection Criteria Set** root because a released set may be reused across portfolios and review cycles and must remain resolvable after portfolio closure.
- Reuse WM-ACT-005 for project masters, WM-ACT-030 for initiatives, the Program profile for program components, WM-ECO-012 for budget authority, WM-KNW-011 for objectives and the decision triad for scenario approval.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Portfolio identity persists through component turnover, criteria revisions, strategy changes and rebalances. Components retain their own identity, owner, lifecycle, baseline, actuals and evidence. Portfolio-owned assertions describe admission, ranking, allocation and scenario selection without changing the component master.

PortfolioComponent is a typed, source-qualified and effective-dated membership assertion. One component may belong to multiple portfolios, each with a different admission basis and declared share. Ending membership never closes or cancels the component.

The Selection Criteria Set has independent identity, version lifecycle and reuse across portfolios. Individual criteria, weights and constraints are contained in a released set. Observations and metric definitions remain external.

## Portfolio boundaries

A Portfolio selects, prioritizes and balances investments against strategy and constraints. Its components may be unrelated. A Program coordinates related components around a joint outcome and benefit hypothesis. A catalogue indexes items without mandate, reserved decisions, allocation or lifecycle. A Project owns its authorization and baseline. An Initiative remains upstream change intent; portfolio membership does not formalize it into delivery identity.

Portfolio membership creates no dependency, shared outcome or program semantics. Program and Portfolio profile changes require supersession with new identity.

## Criteria, scoring and prioritization

Criterion definition, weighting, observed score and prioritization release are separate. A criterion pins measure reference, scale, unit, preference direction and mandatory or compensatory status. A score cites source, observation period, method, denominator, quality and uncertainty.

A prioritization release pins the portfolio, criteria-set version, weighting version, candidate set, comparison period and authority. Rank belongs to that release and is never written as an intrinsic property of the component. Rankings from incompatible pins are not compared as if they shared one scale.

Alternative comparison includes constraints and a do-nothing comparator or justified exception. Product and project investments use a common period and incremental cost/value basis; continuous product investment acquires no artificial completion date.

## Allocation and funding

InvestmentAllocation is portfolio-scoped intent within an approved envelope. It is distinct from budget authority, funding availability, commitment, obligation, accounting actual and component funding.

Every allocation declares source, destination, amount or share, currency, price base, valuation basis, interval, restrictions, authority and residual rule. Allocations against one released source and period may not exceed the source amount. Residuals reconcile, and consolidated reporting never derives actuals, capacity, outcomes or benefits from allocation shares.

## Scenarios and decisions

PortfolioScenario is an immutable hypothesis release containing candidate composition and allocations under stated assumptions, horizon and capacity constraints. It is neither an actual nor an approved baseline.

Selection requires separate rationale, authorized decision occurrence and issued record. The resulting composition-and-allocation baseline is a distinct immutable release. Capacity is tested at scenario level; the highest-ranked set need not be selected, and any divergence requires recorded rationale.

Strategic alignment is an evidence-bearing contribution claim. It does not establish causality or prove benefit realization.

## Governance, time and rebalance

Portfolio governance owns mandate, admission/removal, criteria adoption, weighting, scenario selection, allocation within its envelope, thresholds and assurance. Component authorization and internal gates remain component-owned.

Planned, decision, event, effective, observation, ingestion and knowledge times remain distinct. Memberships, criteria pins, rankings, allocations and scenarios are effective-dated and immutable after release.

Review cadence combines a declared interval with event triggers such as funding change, constraint breach, defeated assumption, strategy restatement or authority change. Rebalance is an authorized lifecycle event that produces successor composition and allocation releases without rewriting history.

## Acceptance result

PF-1 and PF-2 both admit initiative INI-1 with shares 0.6 and 0.25, both with shareBasis capital, from distinct released funding sources. Each membership and allocation is independent and neither converts INI-1 into a project. PF-1 selects scenario SC-3, pinning criteria set CS-v2, weighting W-v1, candidates, horizon, price base and capacity. Decision D-7 approves it and issues REC-7. Later score or criteria revisions create successors; SC-3, D-7 and REC-7 remain reproducible. Consolidated reporting counts INI-1 once and no source is exceeded. Unrelated PF-1 components do not become a Program.

## Required invariants

1. Exactly one WM-ACT-029 profile discriminator is present.
2. Portfolio components need not be related.
3. Membership never transfers component mastership.
4. Portfolio lifecycle changes never cascade to component masters.
5. One component may belong to multiple portfolios.
6. Criteria, weighting, observations and ranking releases remain distinct.
7. Rank is release-scoped, never intrinsic to work.
8. Comparisons pin criteria, horizon, price base and metric revisions.
9. Portfolio allocation is distinct from authority, commitment and actuals.
10. Released source amounts are not exceeded and residuals reconcile.
11. A scenario is neither an actual nor an approved baseline.
12. Baseline approval requires an authorized decision.
13. Alignment does not prove causal benefit.
14. Rebalance creates successors and preserves history.
15. Portfolio membership does not imply Program semantics.

## Holds

Selection Criteria Set has no registry allocation. Metric Definition, Outcome / Benefit Realization, Product, Operation, Resource / Capacity and several funding referents also remain unallocated. WM-ACT-029 records WM-ACT-005 as both parent and contained model, while WM-ACT-030's project parent conflicts with initiative-is-not-project semantics. Relation rows are unapproved and reused bases remain non-canonical drafts with source and provider holds. No installability or publication-readiness claim is made.

## Audit remediation

The reconciled artifacts separate criteria and weighting identities, bind criterion fields and time axes, externalize criteria-set mastership, disable inherited Program semantics, require explicit non-exhaustive share basis, pin decision-triad references, make baseline a distinct release, hold unverified bases and Funding Source enforcement, and specify prospective handling of cancelled, split, merged or re-mastered components.
