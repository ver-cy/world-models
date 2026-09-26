# EM-COM-02 local synthesis

## Disposition

- Define an Enterprise Sales and Marketing Interaction profile over WM-ECO-026 Sales Lead / Opportunity, WM-ECO-021 Offer / Quote and WM-ECO-027 Marketing Campaign.
- Keep Lead and Opportunity lifecycle in WM-ECO-026, proposal identity/validity in WM-ECO-021 and campaign/audience/channel/attribution-design facts in WM-ECO-027.
- The profile owns cross-model bindings and projections, not the underlying entities: PursuitLink, PartyLinkAssertion, ProposalBinding, AttributionClaim and OutcomeBinding.
- Treat AttributionClaim as a profile-owned record with independent claim identity. Its world-model authority remains identifier-unassigned pending registry review.
- Keep Party identity/roles in EM-COM-01, offerings in EM-PRD-01 and orders/contracts/revenue in their external masters.
- Allocate no runtime or model identifier.

## Identity and mastership

Profile records are scoped by the observing Dimension and subject reference so independent enterprises do not collide. Every link pins an upstream revision or `asOf` time and cannot mutate its source master.

A Lead may reference a Party only through an append-only PartyLinkAssertion carrying match method/version, confidence, evidence, asserted time, validity and supersession. This reference does not create or merge a Party, customer role, contact assignment, consent or communication permission. Email and phone are evidence, never identity keys.

Opportunity stage, probability, score, forecast category and outcome remain separate. Probability requires method/model version, features, evidence, calibration and as-of time. Weighted forecast is a projection and never recognized revenue.

## Quote, offer and binding outcome

Quote becomes an offer only through a proposal-profile change with intent, definiteness, recipient, validity, terms version, authority and communication/receipt evidence. Acceptance creates or references a distinct order. Contract formation requires a separate contract master and jurisdiction-qualified legal-effect determination. Neither proposal nor this profile converts itself into an order or contract.

OutcomeBinding links one accepted proposal version to the authoritative order, contract or recognized-revenue record. Quoted totals never flow directly into finance.

## Campaign and attribution

AttributionClaim identifies one subject level, campaign revision, attribution method/version, window, touchpoint evidence, credit fraction, confidence, as-of time and supersession. Claims for pursuit, proposal, order and revenue are different. Claims under different methods coexist and are never averaged or summed together.

Attribution is model-relative credit, not causality. A causal claim additionally requires experiment evidence from WM-ECO-027. Credit fractions are bounded only within one subject, method version and window.

## Acceptance scenario

Campaigns C1 and C2 lead to one Lead L, later linked with confidence to an existing Party without creating customer status. L qualifies into pursuit P. Proposal Q1 covers platform scope and Q2 services scope. Last-click and linear attribution methods produce parallel, method-labelled claims. Q1 is accepted and bound once to order/revenue masters; Q2 expires and contributes no recognized sale. Forecast remains separate from the recognized outcome.

## Invariants

1. Forecast is never recognized revenue.
2. Attribution names method/version and exact window.
3. Conversion never merges people on contact identifiers.
4. Credits sum within one subject/method/window only.
5. At most one accepted proposal per pursuit and commercial scope key is outcome-bound.
6. Recognized amounts come only from external order/contract/revenue masters.
7. A Lead-to-Party link creates no Party, role, consent or permission.
8. Quote, offer, order and contract remain distinct objects and clocks.
9. Attribution is not causality.
10. Profile records are append-only with supersession.
11. Profile records never mutate or cascade-delete upstream masters.

## Holds

AttributionClaim lacks registry authority; base models retain single-provider and noncanonical holds; relation rows and semantic crosswalks are incomplete; order linkage is candidate-only; legal effect, consent and communication permissions remain external and jurisdiction-qualified; probability and attribution methods need calibration/bias review and fixtures. This checkpoint makes no canonical completeness, installability or publication claim.
