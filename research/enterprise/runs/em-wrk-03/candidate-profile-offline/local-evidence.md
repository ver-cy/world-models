# EM-WRK-03 local synthesis

## Disposition

- Profile **Program** on the existing WM-ACT-029 Program / Portfolio aggregate and require the profile discriminator.
- Keep **Portfolio** as the sibling WM-ACT-029 profile with different admission and sequencing rules.
- Model ProgramComponent, Tranche and BenefitDependency as addressable program-owned assertions, not independent roots.
- Profile **Transition Plan** on WM-ACT-008 while WM-ACT-029 owns the program-specific readiness and handover bindings.
- Reuse WM-ACT-005 for project masters, WM-ACT-034 for acceptance and benefit reviews, WM-KNW-011 for objectives, WM-ACT-030 for upstream initiatives and WM-ORG-016 for assignments.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

The Program root has independent aggregate identity. Component masters keep their own identifiers, owners, lifecycles, plans, baselines and evidence. WM-ACT-029 owns only membership, coordination, dependency, sequencing, governance and results-chain assertions.

ProgramComponent is a typed, effective-dated membership assertion. Removing it ends membership without closing or deleting the referenced component. A program lifecycle transition never cascades into component lifecycle state, and program governance cannot overwrite project baselines, actuals, task state or risk facts.

## Program, portfolio, project and initiative

A Program coordinates related components against a joint outcome and explicit benefit hypothesis. A Portfolio selects, prioritizes and balances investments; its members may be unrelated. Changing the discriminator is supersession with new identity, not an in-place conversion.

A Project owns its authorization and internal baseline. A Program coordinates across component boundaries without becoming a super-project. An Initiative is upstream change intent and mints a new identity when formalized as a program or project.

An arbitrary folder of projects fails both profiles when it has no joint benefit hypothesis, dependency graph, mandate, accountable owner, admission criteria or reserved decisions.

## Components, tranches and transition

Components may be projects, products, operations, campaigns or other governed work. Non-project components do not acquire project semantics.

A Tranche is a program-level sequencing band across components, ending in a program gate for continue, rebalance or stop. It is distinct from a project phase and cannot authorize a project phase transition.

A Transition Plan is an independently versioned WM-ACT-008 plan that binds a capability, receiving operational owner, readiness criteria, affected groups and handover. Operational acceptance is a separate authorized decision by the receiving owner. Sustainment obligations survive program closure and remain operationally mastered.

## Benefits, dependencies and attribution

Output, capability, outcome, benefit and disbenefit are separate facts. A BenefitDependency is a typed, directed, validity-bounded assertion between results-chain nodes or components. It does not become a standalone aggregate.

A joint benefit requires a falsifiable hypothesis, owner, baseline, target, indicator, period and realization plan. Attribution states method, uncertainty and causal limits. Adjudicated shares for one benefit and period must not exceed 1.0, and program-level and project-level reporting must not double count the same benefit.

The Outcome / Benefit Realization aggregate required as the external benefit master remains identifier-unassigned.

## Governance, time and closure

Program governance owns mandate, governance model, membership changes, sequencing, allocation within its envelope, thresholds, assurance and program gates. Component authorization, baselines and internal gates remain component-owned. Escalation references a decision; it does not transfer mastership.

Planned, decision, event, effective, observation, ingestion and knowledge time remain distinct. Released mandates, memberships, allocations, plans, decisions and observations are immutable and corrected by successors.

Program closure records handover, benefit owner and residual obligations. It does not imply that every component is closed or that a benefit is realized. A program may close while benefits remain forecast and under operational observation.

## Acceptance result

Program PGM-1 contains projects P-A and P-B plus transition to operation OPS-1. Benefit B-J depends on both project outputs and sustained operational adoption. P-A closes first; its membership ends, but B-J remains forecast with `measurement-pending` because project closure proves neither outcome nor benefit. P-B continues. The program tranche gate does not affect either project's phase gates. OPS-1 later accepts the pinned transition-plan release; realization observations start only after adoption. Attribution remains unadjudicated until shares reconcile, and a support-load increase is recorded separately as a disbenefit.

## Required invariants

1. Exactly one WM-ACT-029 profile discriminator is present.
2. Program components are not limited to projects.
3. Membership never transfers component mastership.
4. Program lifecycle changes do not cascade to component masters.
5. Project closure proves neither outcome nor benefit.
6. Output, outcome, benefit, disbenefit and attribution remain separate.
7. A joint benefit has an explicit falsifiable hypothesis.
8. Adjudicated attribution shares do not exceed 1.0 per benefit and period.
9. Program and project views do not double count one benefit.
10. A tranche gate is not a project phase gate.
11. Transition plan, operational acceptance and sustainment remain distinct.
12. Released assertions are immutable and superseded explicitly.
13. An arbitrary container is neither a Program nor a Portfolio.

## Holds

The external Outcome / Benefit Realization master has no registry allocation. WM-ACT-029 is recorded with WM-ACT-005 as both parent and contained model, creating a containment contradiction that must be resolved. Relevant relation rows remain unapproved, and reused bases remain non-canonical drafts with source and provider holds. No installability or publication-readiness claim is made.
