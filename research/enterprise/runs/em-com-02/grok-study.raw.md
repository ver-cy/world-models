# Grok independent review — EM-COM-02

Source conversation: https://grok.com/c/97e608a6-1922-44c1-85cd-e3d2f7cac1ee

## Verdict

ACCEPT PROFILE with holds. EM-COM-02 is an Enterprise profile over WM-ECO-026 Lead / Opportunity, WM-ECO-021 Quote / Offer and WM-ECO-027 Campaign. It must not create a new model or runtime identity. PursuitLink, PartyLinkAssertion, ProposalBinding, AttributionClaim and OutcomeBinding are profile-local records with local identity and supersession; none receives a catalogue world-model identifier.

AttributionClaim does not justify independent world-model identity. It is seller-scoped, method-relative credit over an externally mastered outcome, not a causal or economic fact. It must carry method, version and window, remain identifier-unassigned, and never become a revenue booking instruction. Source/channel/campaign provenance on WM-ECO-026 is distinct from attribution credit.

## Boundary findings

- The profile remasters none of Party, campaign, pursuit, proposal, order, contract or revenue.
- PartyLinkAssertion carries method/version, confidence, evidence and time. It creates no Party, customer role, consent or permission; email/display-name equality never merges Party identities.
- Opportunity is a state/classification of the WM-ECO-026 pursuit. Probability and forecast remain method/calibration-qualified and are never recognized revenue.
- WM-ECO-021 proposal acceptance is neither an order nor contract formation nor revenue. ProposalBinding preserves proposal scope/version; OutcomeBinding references at most one accepted commercial result per outcome scope.
- WM-ECO-027 owns campaign identity and attribution design. Attribution is credit, not causality. Competing methods may coexist without overwriting or summing across method/version/window.
- Campaign identity resolution and deduplication never become Party same-as. Lead deduplication preserves lineage.

## Scenario

Two WM-ECO-027 campaigns link to one WM-ECO-026 pursuit. Two disjoint-scope WM-ECO-021 proposals bind to that pursuit. One proposal is accepted and one external outcome is referenced once. Either campaign may receive method-labelled credit against that same outcome, but the credit claims cannot mint a second economic fact or recognition. Forecast remains non-revenue. Negative cases reject missing method/window, causal claims without experiment evidence, duplicate OutcomeBindings, email-based Party merge and cross-method credit aggregation.

## Invariants and holds

All five profile-local record types remain identifier-unassigned. One OutcomeBinding exists per outcome scope; multiple credit claims may attach to that one outcome. Unknown and withheld Party states remain first-class. Parent cards are reviewable drafts with unsettled relation ledgers, including ACT-028/ECO-027 parentage, WM-ECO-026 to Party and WM-ECO-021 to order/contract edges. Disjoint proposal scope must be evidenced from proposal content. Forecast calibration and attribution methodology remain open. The profile must not pick parents or close missing relation rows.

