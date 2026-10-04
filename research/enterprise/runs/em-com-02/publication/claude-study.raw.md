# EM-COM-02 — Independent review (frozen dossier only)

## Verdict
**PROFILE (conditional)** — publish a bounded *Enterprise Sales and Marketing Interaction Profile*. Not `REUSE ONLY`: no frozen model owns the cross-model joins this contour needs (pursuit↔proposal, campaign↔pursuit credit, outcome↔recognition), and the relation ledger contains exactly one candidate edge (WM-ECO-019 REFERENCE WM-ECO-021). Not `NEW MODEL`: Lead, Opportunity, Quote and Campaign are already mastered by WM-ECO-026, WM-ECO-021 and WM-ECO-027; re-minting them would create a second authority for pursuit stage, proposal validity and audience definition. **AttributionClaim is the one genuinely unowned concept** — WM-ECO-027 owns attribution *design* (window, model version, loss), WM-ECO-026 owns pursuit-side *source/channel* assertions, neither owns the cross-model *claim*. Hold it profile-owned and flag the registry gap rather than escalating to a new world model inside this contour.

## Evidence
All three targets are `status: published` but `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, produced under `single-provider-waiver` with Codex only and Claude/Grok waived after timeouts. `evidence_depth` for every vercy candidate is `index-and-publication-metadata`; each carries an explicit absence-of-external-review hold. Parents are provisional in all three cases (WM-ORG-014 for 026, WM-ACT-028 for 027, WM-OBJ-003 unapproved for 021) with no settled edge. Predecessor fields from COM-04/COM-05/COM-08 are `candidate-not-normative`. Consequence: the boundary below is a design decision on frozen text, not conformance evidence, and it inherits every upstream hold.

## Identity/mastership
Profile identity is `(observerDimensionRef, subjectRef)` — the EM-COM-01 pattern, so two enterprises observing the same pursuit or campaign cannot collide. The profile owns five record kinds and no entity identity:

- **PursuitLink** — binds a WM-ECO-026 pursuit revision into the enterprise view; never sets stage, probability or outcome.
- **PartyLinkAssertion** — see Lead/party.
- **ProposalBinding** — binds a WM-ECO-021 proposal version to a pursuit and a commercial scope key.
- **AttributionClaim** — method- and window-qualified credit assertion.
- **OutcomeBinding** — binds an accepted proposal to external order/contract/revenue refs.

Mastership is closed: pursuit lifecycle → WM-ECO-026; proposal profile, validity, response evidence → WM-ECO-021; audience, channel, metric and attribution *design* → WM-ECO-027; Party identity, role, scope, endpoint, segmentation → EM-COM-01 over WM-ORG-014/WM-ORG-015/WM-PER-010; offering definition → EM-PRD-01. All bindings cite exact upstream version or `asOf`.

## Lead/party
A Lead is a WM-ECO-026 pursuit in lead-signal or qualified-lead profile. It **may** reference a Party when, and only when, a `PartyLinkAssertion` carries: `partyRef` resolvable under the adopting Dimension's Party identity policy (via EM-COM-01's set), match method + version, confidence, evidence refs, `assertedAt`, validity interval, supersession. The assertion is append-only and non-authoritative. It does **not**: create or merge a Party; create a `CommercialRoleBinding` (a prospect is not a customer — customer role stays WM-ORG-014-side); create a `ContactAssignment` or any consent, lawful basis or channel permission; upgrade lead-signal to known-party classification, which is WM-ECO-026's own axis. An anonymous signal keeps `partyRef` unknown rather than inventing one.

## Opportunity/forecast
Probability, score, stage, forecast category and outcome are five separate axes per WM-ECO-026 and none proves another. A probability assertion is admissible only with method/model version, permitted features, evidence, confidence, calibration reference and `asOf`; `expected_value` requires amount type, currency, range, recurrence and basis. Forecast is a projection over as-of pursuit revisions with declared method — never a stored total that survives revision. `probability × expected_value` is a *weighted forecast* and may never be labelled, aggregated with, or reconciled against recognized revenue; recognition lives in external finance masters reached through `OutcomeBinding`, and the profile has no posting capability.

## Quote/offer/contract
Three transitions, three authorities:

1. **Quote → offer**: WM-ECO-021 profile change to `offer`, requiring declared intent, definiteness, addressed recipient, validity (`valid_until`), `terms_version`, pricing/signing authority and a communication/receipt event on its own clock. No label, click, acknowledgement or status effects this.
2. **Offer → order**: an external order master (WM-ECO-019, currently a *candidate* REFERENCE edge) is created citing the accepted proposal version. The order is a distinct object; the quote is not converted.
3. **Offer → binding contract**: only an external contract master plus a legal-effect determination. Neither WM-ECO-021 nor this profile decides formation or enforceability — the profile stores the determination *reference*, never the conclusion.

## Campaign/attribution
An `AttributionClaim` is `(observerDimensionRef, subjectRef, campaignRevisionRef, methodRef+version, windowKind, windowStart, windowEnd, touchpointEvidenceRefs, creditFraction, confidence, asOf, supersedes)`. `subjectRef` names exactly one level — pursuit, proposal, order or revenue outcome — and claims at different levels are never summed. Claims under different method versions coexist as parallel views; they are never combined or averaged. Every touchpoint's event time must fall inside both the campaign revision's `campaign_period` and the declared window. Credit is model-relative: it is not delivery, not response, not causality, and not revenue. The negative case fails structurally — a single click yields `creditFraction 1.0` only under a declared single-touch method, and even then the claim carries no causal force absent WM-ECO-027 experiment evidence (treatment, control, contamination, uncertainty).

## Conversion and deduplication
Conversion is WM-ECO-026 successor lineage, not identity collapse. Matching email, phone or account name is *candidate evidence* for a `PartyLinkAssertion`, never an identity key and never a merge trigger; merge/split decisions are authorized upstream and the profile only follows lineage. Duplicate suppression is per `(observerDimensionRef, subjectRef, methodRef+version, windowKind, window)` for claims and per `(pursuitRef, proposalVersionRef)` for bindings. Two enterprises, two campaigns or two methods producing similar claims are not duplicates.

## Scenario
Campaigns **C1** (content, view+click) and **C2** (paid search, click) each at a pinned revision. One lead **L** captured from a C2 click, `partyRef` unknown; a later `PartyLinkAssertion` binds an existing Party at confidence 0.8 without creating a customer role. L qualifies into pursuit **P**. Two independent proposals: **Q1** (scope key *platform*) and **Q2** (scope key *services*), each its own WM-ECO-021 lifecycle and `valid_until`.

Attribution: under method *last-click, 30-day, click-only* → C2 = 1.0 on `subjectRef = P`. Under method *linear, 90-day, view+click* → C1 = 0.4, C2 = 0.6 on the same subject. Both persist; neither is summed with the other; a dashboard showing only one must declare the method.

Outcome: Q1 accepted → order O1 → recognition in the finance master, bound once via `OutcomeBinding`. Q2 expires unaccepted; its `quoted_total` never reaches any outcome or forecast total. Had both been accepted, disjoint scope keys yield two orders, each recognized once in its own master, with claims re-expressed per order subject rather than duplicated from one touchpoint set. Forecast before close remains a weighted as-of projection, distinct from and never reconciled against O1's recognized amount.

## Invariants
1. Forecast is never recognized revenue; no weighted amount is aggregated with a finance total.
2. Every attribution claim declares method, version, window kind and window bounds.
3. Conversion never merges persons on email or any contact identifier.
4. Credit fractions sum to ≤1 only within one subject, method version and window; cross-method sums are invalid.
5. At most one accepted proposal per `(pursuit, commercial scope key)` may be outcome-bound; scope keys must be disjoint.
6. Recognized amounts derive from order/contract/revenue masters, never from `quoted_total`.
7. A lead may reference a Party without creating Party, role, endpoint, consent or customer status.
8. Quote, offer, order and contract remain four distinct objects with distinct clocks.
9. Attribution is not causality; causal claims require WM-ECO-027 experiment evidence.
10. All records are append-only with supersession; nothing is silently overwritten.
11. No profile record mutates an upstream master or cascades deletion.

## Minimal completion shape
`PursuitLink(observerDimensionRef, pursuitRevisionRef, asOf)`; `PartyLinkAssertion(…, partyRef?, method+version, confidence, evidenceRefs, validity, supersedes)`; `ProposalBinding(pursuitRef, proposalVersionRef, scopeKey, role ∈ {quotation, offer}, validity)`; `AttributionClaim(subjectRef, campaignRevisionRef, methodRef+version, windowKind, windowStart, windowEnd, touchpointEvidenceRefs, creditFraction, confidence, asOf, supersedes)`; `OutcomeBinding(proposalVersionRef, outcomeKind, externalMasterRef, scopeKey, determinationRef?, asOf)`. Projections only: `rolesAt(t)` (delegated to EM-COM-01), `weightedForecast(asOf, method)`, `creditFor(subject, method, window)`, `recognizedFor(subject)` sourced externally.

## Holds
Upstream assurance is reviewable-draft under a single-provider waiver; publication does not evidence independent review. No settled relation exists for WM-ECO-026, WM-ECO-021 or WM-ECO-027; WM-ECO-019→WM-ECO-021 is candidate only. Semantic crosswalks for all three vercy candidates are unverified. **AttributionClaim has no reserved world-model authority — registry reservation or escalation is required before promotion.** Legal-effect, formation, enforceability, tax and consumer questions are out of scope and jurisdiction-qualified. Consent, ePrivacy, CAN-SPAM and profiling constraints remain with WM-ECO-027 and EM-COM-01; the profile authorizes no contact. Attribution and probability methods require organization-specific definition, calibration and bias review. EM-COM-01's unresolved WM-PER-010 / WM-XCT-024 endpoint ownership conflict is inherited. Blocking decisions from the dossier — boundary reuse/extend/new, source mastership, immutable refs, fixture checks — remain open. This is a design review: no claim of canonical completeness, publication readiness or installability.
