# EM-COM-03 — Order, Subscription and Consumption Entitlement

## Verdict

Reuse both target models and add one thin profile; allocate no runtime identifier.

- **Reuse WM-ECO-020** for Order and OrderLine, including line-level allocation, delivered/outstanding/oversupply accounting, despatch linkage, claims and closure.
- **Reuse WM-ECO-022** for Subscription, plan/price bindings, billing and renewal schedules, suspension states and usage/allowance references.
- **Reference WM-ECO-021** for the proposal version an order or subscription cites; **WM-ECO-008** for the priced fiscal document; **WM-ECO-009** for settlement.
- **Create an Enterprise Order–Subscription–Entitlement profile** (identifier-unassigned) owning only cross-model bindings: `OfferVersionBinding`, `OrderSubscriptionOrigination`, `EntitlementBinding`, `RenewalAssertion`, `FulfilmentEvidenceBinding`, `SettlementBinding`.
- **Create an identifier-unassigned Consumption Entitlement candidate.** Neither target model owns Entitlement: WM-ECO-022 lists "owning … Entitlement … masters" as out of scope and makes grant/revocation external; WM-ECO-020 never mentions it. Entitlement therefore has no master in the frozen registry and cannot be absorbed into either aggregate.
- **Renewal is not a model.** It is a lifecycle assertion inside WM-ECO-022 plus a profile `RenewalAssertion` binding predecessor to successor version. No independent identity or lifecycle is evidenced.

## Evidence

WM-ECO-020 (`f53e990c…`) is an aggregate keyed by the seller-assigned sales order identifier, 24 findings, 14 artifacts, 8 functions, `publishableCanonical: false`, Claude-only with Grok waived. Its own `known_omissions` state that "subscription, recurring and standing-order specialisations, and service orders for non-goods deliverables, are only lightly covered by the commercial pattern classification" — direct support for keeping recurrence out of Order.

WM-ECO-022 (`2088c4e7…`) is an aggregate, 24 findings, 24 artifacts, 10 functions, Codex-only with Claude and Grok both waived, `publishableCanonical: false`. Its findings are templated: three near-identical questions per finding and one boilerplate identity strategy repeated across all 24 artifacts. The scope statement and holds are usable; the finding surface is not evidence of depth.

Frozen relations are sparse and all `candidate`: WM-ECO-019→WM-ECO-021, WM-ECO-024→WM-ECO-008, WM-ECO-008→WM-ECO-009, WM-ECO-009→WM-ECO-016, WM-ECO-009→WM-ECO-004. **There is no frozen relation from WM-ECO-020 or WM-ECO-022 to any of these.** Every boundary below is therefore a profile binding published as prose, consistent with WM-ECO-020's own relationship-contract hold.

## Identity/mastership

Order is keyed by the seller-assigned sales order identifier scoped to the issuing seller entity; buyer order references and customer references are cross-references and never promoted. OrderLine identity is composite (order + line), never reused within a version. Subscription is keyed by subscription identifier plus provider namespace and version head; party, plan name, invoice, payment and start date never identify it.

Entitlement needs an identity independent of both: a subscription may be suspended while an entitlement persists in grace, and an order line may deliver a right that outlives the order. Until the registry allocates it, `EntitlementBinding` carries scope subject, period, source (order line or subscription version), grant reference and supersession, scoped by observing Dimension.

Candidate master systems are CRM, order system and service desk. No profile record may mutate or cascade-delete an upstream master; all bindings are append-only with supersession and pin an upstream revision or `asOf` time.

## Order/line

WM-ECO-020 carries what EM-COM-03 needs: `de-order-line-id`, ordered quantity with pinned unit code, header and line state as separately addressable vocabularies (`de-header-state`, `de-line-state`), derived header state from mixed line states (`sm-header-derivation`), version counter plus supersession pointer, and the rule that a patch touching an already-despatched quantity is rejected and routed to the post-delivery claim path.

Order state is model-owned: no retrieved primary source publishes a normative seller-side state machine, and the Schema.org status enumeration is explicitly a lossy alignment target, not the internal machine. Any mapping asserted downstream must be recorded as lossy.

The offer-version constraint holds structurally through `de-upstream-doc-reference` plus `odr-restatement-rule` precedence, but it is a profile binding: the only frozen quote relation is WM-ECO-019→WM-ECO-021.

## Subscription/entitlement/usage

Three axes stay separate, and WM-ECO-022's own state-axis hold requires it: agreement, entitlement, provisioning, billing, payment and usage states and clocks must never be collapsed. Active or paid status proves neither entitlement delivery nor service availability.

- **Entitlement** is the right to consume: subject, permission/prohibition/duty, scope, period, allowance, cap, limit. Bounded by subject and period.
- **Usage** is measured consumption: usage event, meter, unit, source, period, aggregation, correction, confidence — masters external to both models.
- **Allowance balance** (quota, consumed, remaining, rollover, overage) is a projection over entitlement and usage, never an entitlement itself.

Overage is a priced consequence of usage exceeding entitlement; it is not evidence that entitlement changed.

## Fulfilment/invoice/payment

Four distinct chains, none implying another:

1. **Order line → despatch linkage → delivered/outstanding/oversupply** (WM-ECO-020, from the despatch profile).
2. **Fulfilment → invoice** (WM-ECO-024→WM-ECO-008) — a reference from fulfilment to billing evidence, not the reverse.
3. **Invoice → payment** (WM-ECO-008→WM-ECO-009), then payment → postings (WM-ECO-016).
4. **Entitlement/usage** — independent of all three.

The negative case fails on direction alone. Delivered quantity increases only via `record-despatch-against-order`. No edge runs from payment or invoice to an order line's delivered quantity, and WM-ECO-020 places invoice, tax determination and settlement out of scope. Settling an invoice discharges a monetary obligation; it cannot raise `de-delivered-quantity` or lower `de-outstanding-quantity` on any line.

Order-level tax and anticipated totals are indicative; the invoice is the compliance-bearing document and may legitimately diverge.

Allocation: WM-ECO-020's adjudication already narrowed this — the order holds the recorded allocation outcome, firmness flag and reservation pointer; availability determination and stock reservation belong to the inventory model, and cross-order contention records the outcome plus deciding authority only.

## Change/renewal/proration

Mid-cycle plan or price change produces a **successor subscription version** with reason, affected items, entitlements, bills, notices, compatibility, migration and approval. Issued versions are immutable and remain resolvable; nothing is overwritten. Request time, effective time and external execution stay distinct. Proration, credit and refund are separate economic values, each requiring currency, quantity or usage basis, period, source and approval.

Suspension is a state assertion with reason, not a version rewrite, and not entitlement revocation — those are separate evidence and authority. A subscription may remain active with no payment for the current cycle.

Renewal at a new price is a `RenewalAssertion` plus a successor version binding a new plan/price version. Prior term periods, prior price versions and the originating offer version remain readable at their own effective times.

## Lifecycle

Order: captured → validated → dispositioned (accepted / amended / rejected / counter-offer) → allocated → despatched → reconciled → closed, with holds and claims as first-class exception paths. Acceptance is the only act creating commercial commitment; no allocation or despatch may precede it.

Subscription: registered → plan/participants bound → activated → served, with pause/suspension/grace/reactivation, term and renewal windows, cancellation request → effective cancellation → termination completion → entitlement revocation → final bill → refund → export → disposition, each separately attributable.

Entitlement: granted → active → constrained/exhausted → suspended → revoked → expired, keyed independently of both.

## Scenario

Offer version Q1v2 (WM-ECO-021) is accepted. Order O has line L1 (100 units goods) and line L2 (12-month subscription). L1 despatches 60: `de-delivered-quantity` 60, `de-outstanding-quantity` 40, outstanding reason backorder, further delivery planned; L1 state partly despatched, header state derived as partly fulfilled. Invoice I1 for the despatched 60 is settled in full by payment P1 — L1's outstanding 40 is unchanged and O does not close.

L2 originates subscription S (version 1, plan A, monthly) via `OrderSubscriptionOrigination`; S binds Q1v2 through `OfferVersionBinding`. Entitlement E1 is bound to S v1, scoped to plan A features, period month 1–12.

Month 4: non-payment suspends S. S v1 stays immutable; a suspension assertion with reason and effective time is appended. E1 moves to suspended without revocation; usage after suspension is recorded against E1's suspended window and does not retroactively alter months 1–3. S remains active-as-a-relationship with no month-4 payment.

Month 5: remediation reactivates S. Month 12: renewal onto plan B at a new price creates S v2 with an effective-from instant, a new plan/price binding, notice and consent evidence, and a `RenewalAssertion` pointing at S v1. Q1v2, O, L1's residual 40, months 1–12 prices and E1's period all remain readable at their original values. Partial delivery, suspension and repriced renewal are all satisfied without rewriting history.

## Invariants

1. Order, OrderLine, Subscription, Entitlement, Invoice and Payment identities are distinct and never substituted.
2. Payment or invoice state never changes any line's delivered or outstanding quantity.
3. Delivered quantity changes only via a despatch linkage bound to that line.
4. Order and line states are separately addressable; header state is derived, never asserted independently of its lines.
5. An order or subscription cites an offer **version**, not an offer.
6. Acceptance is the only act creating commercial commitment; allocation and despatch require it.
7. Allocation records an outcome and a reservation pointer; it never determines availability.
8. Entitlement is bounded by subject and period, and is not implied by subscription status.
9. Usage is never entitlement; allowance balance is a projection over both.
10. A subscription may exist and remain active without the current period's payment.
11. Plan, price, term, entitlement and billing changes create successor versions; issued versions are immutable and remain resolvable.
12. Suspension, entitlement revocation, cancellation request, effective cancellation, termination completion, final bill and data disposition are separate assertions with separate authority.
13. Renewal at a new price never alters prior periods, prior prices or the originating offer version.
14. Proration, credit, refund and overage each carry currency, basis, period, source and approval.
15. Profile records are append-only with supersession and never mutate or cascade-delete an upstream master.
16. Entitlement grant and revocation are executed externally; the profile records bindings and evidence only.

## Minimal completion shape

Register the profile and the Consumption Entitlement candidate as identifier-unassigned. Populate the relationship contract for WM-ECO-020 and WM-ECO-022 — order↔offer version, order line↔subscription origination, entitlement↔subscription/order line, order/subscription↔invoice, invoice↔payment — since all currently publish as prose. Resolve WM-ECO-020's `entry_kind` (registry `standalone-mm` vs result `aggregate`) and composition role beneath WM-ECO-006. Add hold apply/release and post-delivery claim capture functions, and split `order-claim-and-closure-record` into repeating claims and a singleton closure. Re-derive WM-ECO-022's finding surface from primary sources rather than templates. Complete semantic crosswalks against TM Forum SID, UBL and CPQ/order-management practice, pin immutable source refs, and run fixtures for partial delivery, suspension and repriced renewal.

## Holds

Both targets are reviewable drafts with `publishableCanonical: false` and single-provider waivers — WM-ECO-020 Claude-only with Grok waived, WM-ECO-022 Codex-only with Claude and Grok waived; EM-COM-03 inherits both absence-of-independent-review holds. WM-ECO-021, WM-ECO-008 and WM-ECO-009 add their own: Codex-only waiver, and `described-previous-version` under `migration-boundary-review` for the two legacy entries. Every frozen relation is `review_state: candidate`, and no relation exists between the two targets. WM-ECO-020's source re-tiering hold (SRC-010, SRC-011, SRC-012 are overview, portal and summary pages), its coverage-checklist restatement hold and its consumer-protection evidence gap remain open. WM-ECO-022's jurisdiction, legal-effect and sector-profile holds remain open; its checklist marks every dimension covered on boilerplate notes and should not be relied on. Entitlement has no registered master. Legal effect, consent, notice and tax treatment stay external and jurisdiction-qualified. Mapping to TM Forum SID, UBL and OASIS remains unverified and must be recorded as lossy where asserted.

This review is a research checkpoint. It makes no claim of canonical completeness, conformance to any external specification, or installability.
