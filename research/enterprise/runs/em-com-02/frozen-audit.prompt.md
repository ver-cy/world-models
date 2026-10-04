You are the sole frozen independent semantic auditor for EM-COM-02. Use no tools. Review the reconciled direction and current package for identity, mastership, profile-local record semantics, attribution-versus-causality, outcome deduplication, Party safety, forecast semantics, proposal/order/contract separation, fixtures, holds and accidental new IDs. Return: verdict; blocking defects; non-blocking defects; exact remediation; required fixtures; publication disposition. Do not invent identifiers or claim canonical completeness.

## Claude boundary study
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


## Grok independent review transcript
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



## Provider reconciliation
# Provider comparison — EM-COM-02

Claude and Grok agree that EM-COM-02 is a profile over WM-ECO-026, WM-ECO-021 and WM-ECO-027. Both preserve external mastership for Party, campaign, pursuit, proposal, order, contract and revenue; separate lead from Party/customer/consent; keep opportunity forecast method-qualified and non-revenue; distinguish quote, offer, order and contract; and require attribution method/version/window with credit separated from causality.

Grok rejects the initial `NEW MODEL` disposition for Attribution Claim. The reconciled direction demotes it to an identifier-unassigned profile-local record: stable local identity and supersession are allowed, but catalogue world-model authority is not. PursuitLink, PartyLinkAssertion, ProposalBinding and OutcomeBinding follow the same rule. WM-ECO-026 source provenance remains distinct from attribution credit.

The scenario is tightened to one WM-ECO-026 pursuit, two WM-ECO-027 campaigns, two disjoint-scope WM-ECO-021 proposals and exactly one externally mastered accepted outcome. Multiple method-labelled credit claims may reference that outcome, while duplicate outcome recognition, email-based Party merge, cross-method aggregation and forecast-as-revenue are rejected.

Publication remains held because the parent cards and relation ledger are not canonical, disjoint proposal scope lacks a published invariant, and organization-neutral forecast/attribution methodology is unresolved. No model or runtime identifier is created.


## Current package: profile-candidate.json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-COM-02","name":"Enterprise Sales and Marketing Interaction Binding","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ECO-026","WM-ECO-021","WM-ECO-027"],"constraints":["WM-ECO-026 owns Lead and Opportunity lifecycle while WM-ECO-021 owns proposal identity, scope and validity.","WM-ECO-027 owns campaign, audience, channel, touchpoint design and experiment evidence.","Party links are append-only assertions with match method, version, confidence, evidence and time and never create Party, role, consent or permission.","Opportunity stage, probability, score, forecast category and outcome remain separate.","Proposal acceptance binds to a distinct order and any contract effect remains externally determined.","Weighted forecast is a projection and never recognized revenue."],"holds":["Attribution Claim remains identifier-unassigned.","Upstream relation, order, legal-effect, consent and communication bindings remain incomplete.","Independent Grok review and frozen audit remain pending."]}


## Current package: allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-COM-02","proposedName":"Attribution Claim","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"An attribution claim remains independently citable across method changes, reporting views, outcome corrections and competing claims.","versionIdentity":"Method, window, evidence, subject level, credit or supersession changes append a new claim rather than mutating the prior claim.","independentLifecycle":["draft","asserted","reviewed","superseded","withdrawn","retired"],"mastership":"authorized commercial analytics or attribution authority"},
"boundary":{"owns":["stable claim identity","subject level and referenced outcome","campaign and touchpoint evidence","method and model version","attribution window, credit fraction and confidence","as-of time and supersession lineage"],"references":[{"target":"WM-ECO-027","purpose":"Campaign revision, audience, channel and experiment evidence"},{"target":"WM-ECO-026","purpose":"Lead or opportunity subject"},{"target":"WM-ECO-021","purpose":"Proposal subject and version"},{"target":"EM-COM-01","purpose":"Party references and commercial roles"}],"excludes":["campaign identity","lead and opportunity lifecycle","proposal, order, contract or revenue identity","party identity and role","causal conclusion without experiment evidence"]},
"objects":{"AttributionClaim":{"identity":["attributionClaimId"],"required":["subjectKind","subjectRef","campaignRevisionRef","methodRef","methodVersion","window","touchpointEvidenceRefs","creditFraction","confidence","asOf","status"],"optional":["supersedesClaimRef","experimentEvidenceRef","limitations"],"lifecycle":["draft","asserted","reviewed","superseded","withdrawn","retired"]}},
"invariants":["Attribution names method, version and exact window.","Pursuit, proposal, order and revenue claims remain distinct.","Claims under different methods coexist and are never averaged or summed together.","Credit fractions are bounded only within one subject, method version and window.","Attribution is model-relative credit and never causality by itself.","Causal claims cite separate experiment evidence.","Every claim pins upstream revisions or as-of time.","Claims never mutate campaign, pursuit, proposal, order, contract or revenue masters.","Recognized amounts come only from external authoritative masters.","Corrections append successor claims and preserve originals.","Independent enterprise dimensions scope claim identity and prevent collision.","Confidence, calibration and limitations remain explicit.","Withdrawal never cascade-deletes upstream evidence.","Claim identifiers are never recycled."],
"holds":["Registry authority and identifier allocation are pending.","Independent Grok review is pending.","Order, contract, revenue, consent and legal-effect bindings remain external and incomplete.","Calibration, bias review, frozen audit and crosswalks remain pending."]}


## Current package: fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Attribution Claim","cases":[{"id":"parallel-methods","kind":"positive","input":"Last-click and linear models attribute the same proposal to campaigns C1 and C2.","expect":"Parallel method-labelled claims coexist and reconcile only within their own subject, method and window."},{"id":"lead-party-link","kind":"positive","input":"Lead L is linked with confidence to an existing Party.","expect":"The append-only assertion preserves match evidence without creating a customer role or consent."},{"id":"proposal-outcome","kind":"positive","input":"Q1 is accepted and linked once to an external order while Q2 expires.","expect":"Only Q1 receives an outcome binding and recognized amounts remain externally mastered."},{"id":"forecast-is-revenue","kind":"negative","input":"Weighted opportunity forecast is reported as recognized revenue.","expect":"The substitution is rejected."},{"id":"email-merges-party","kind":"negative","input":"Matching email addresses automatically merge two Party identities.","expect":"The merge is rejected; contact values are evidence only."},{"id":"methods-summed","kind":"negative","input":"Last-click and linear credits are summed into 180 percent credit.","expect":"The aggregation is rejected across different method versions."},{"id":"attribution-is-causality","kind":"negative","input":"A model-relative credit is stated as causal lift without experiment evidence.","expect":"The causal conclusion is rejected."}]}


## Current package: local-evidence.md
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
