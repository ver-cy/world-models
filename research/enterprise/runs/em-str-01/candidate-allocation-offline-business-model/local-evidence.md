# EM-STR-01 local synthesis

## Disposition

- Propose four identifier-unassigned independent candidates: **Strategy**, **Business Model**, **Value Stream** and **Strategic Scenario**.
- Keep **Strategic Theme** as an addressable child of Strategy and **Value Proposition** as an addressable child of Business Model. Neither receives root identity.
- Reuse WM-KNW-011 for objectives, WM-ACT-030 for initiatives, WM-KNW-010 for rationale, WM-ACT-024 for the approval occurrence and WM-REC-010 for the issued decision record.
- Keep Capability and Process realization blocked because WM-ACT-001 and WM-ACT-003 have legacy specifications only.
- Reference the identifier-unassigned Outcome and Benefit Realization candidate from EM-STR-02.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Strategy has identity across successive choice-set revisions and across the initiatives that implement it. Business Model has identity across strategy revisions and individual offers and may span legal entities. Value Stream has identity across process redesign and organization changes because it is defined by recipient need and value-state progression. Strategic Scenario has identity because multiple strategies can cite one versioned scenario without inheriting its authority.

Strategic Theme and Value Proposition are versioned contained records. A theme groups strategic choices and supplies an alignment anchor. A value proposition states a benefit claim for a recipient segment and channel. It is not an offer, price, SKU or contract.

## Strategy and business model

A Strategy release records selected and explicitly excluded markets or segments, choice rationale, claimed basis of advantage, assumptions, causal hypotheses, horizon, decision authority and review triggers. A mission is standing purpose and a policy is a standing constraint; neither is a strategic choice. Plans, initiatives and portfolios implement strategy but do not constitute it.

A Business Model release records the value mechanism: recipient segments, channels, value propositions, revenue and cost logic, partners and resources by reference. An organization may operate many business models and one business model may span organizations. Channel, segment or mechanism changes create successor releases and preserve prior versions.

## Value stream and realization

A Value Stream begins with a recipient need and trigger and ends with a recipient-side value outcome. Each stage is a change in recipient value state with entry and exit criteria. A Process is an internal repeatable realization of one or more stages. Renaming, reorganizing or automating internal work without changing the recipient-state sequence changes the process, not the value stream.

Stage-to-process and stage-to-capability bindings remain declared but unenforceable until WM-ACT-003 and WM-ACT-001 receive current boundary-reviewed specifications. Output, outcome and benefit stay distinct; delivery completion never proves recipient value or benefit realization.

## Scenario, hypothesis and evidence

A Strategic Scenario holds versioned drivers, varied assumptions, projected states, method and uncertainty. It is a hypothesis space, never a source of record. Assumptions carry validity windows and defeat conditions. Causal hypotheses carry competing explanations and attribution limits.

Scenario results never feed authoritative actuals, target baselines or benefit realization. Forecast remains forecast until qualified observations for the phenomenon period support an outcome. Alignment and contribution links cite a rationale or evidence basis; tags, budget membership and portfolio inclusion are insufficient.

## Decision and review

WM-KNW-010 records alternatives, criteria, evaluation and rationale. WM-ACT-024 records the authorized decision occurrence. WM-REC-010 records the fixed issued expression. Strategy references these identities and never duplicates them.

Horizon, effective interval, event time, knowledge time and review cadence remain distinct. Review triggers include defeated assumptions, scenario divergence, measure breach, named segment or channel change, authority change and horizon expiry. Released versions are immutable; substantive change creates a successor with an explicit restatement and supersession link.

## Acceptance result

A startup strategy selects segment X through a direct channel and excludes a marketplace. Moving to the marketplace defeats a named assumption, restates Strategy, revises Business Model, revalidates the Value Proposition and may revise the Value Stream. Prior forecasts remain forecasts.

A multi-industry group keeps one group strategy plus distinct business models by industry, segment and channel. Exiting a named market restates the group strategy and retires the affected business model without deleting history. Shared value-proposition references remain resolvable. A project list labelled strategy is rejected because it contains no choice set, rejected alternative, value recipient, assumptions, horizon or review trigger.

## Required invariants

1. Strategy states at least one selected choice and one explicitly rejected alternative.
2. Strategy names a horizon and cites decision authority.
3. Mission and policy constrain strategy but never constitute it.
4. Initiative, project and portfolio never substitute for strategy.
5. Business Model remains distinct from organization.
6. Value Proposition remains distinct from offer and contract.
7. Every Value Stream begins with a recipient need and trigger.
8. A stage is a recipient value-state change; a process is internal realization.
9. Assumptions and causal links remain hypotheses with defeat conditions until assessed.
10. Forecast never becomes observed outcome by relabelling.
11. Scenario outputs never become authoritative actuals or baselines.
12. Alignment links require an attributable basis.
13. Released versions are immutable and superseded explicitly.
14. Blocked and unallocated referents are never silently promoted.

## Holds

Strategy, Business Model, Value Stream and Strategic Scenario lack registry allocation. Capability and Process/Workflow have legacy-only specifications. Outcome/Benefit, Metric Definition, policy/mission and several party/offer bindings are unallocated or outside the dossier. All reused current specifications remain non-canonical drafts and relationship contracts are incomplete. No crosswalk, mastership confirmation or fixtures support publication. No installability or publication-readiness claim is made.
