# EM-COM-03 local synthesis

## Disposition

- Reuse WM-ECO-020 for Order and OrderLine, including line-level allocation, despatch evidence, delivered/outstanding quantity, exceptions and closure.
- Reuse WM-ECO-022 for Subscription, plan/price versions, term, billing and renewal schedules, suspension and usage/allowance references.
- Define a thin Enterprise Order–Subscription–Entitlement profile for cross-model bindings: OfferVersionBinding, OrderSubscriptionOrigination, EntitlementBinding, RenewalAssertion, FulfilmentEvidenceBinding and SettlementBinding. The profile remains identifier-unassigned.
- Add an identifier-unassigned **Consumption Entitlement** candidate. Its right-to-consume identity and lifecycle are hypothesised independent and remain unproven pending identityGate evidence.
- Renewal remains a lifecycle assertion linking subscription versions, not a separate model.
- Reference WM-ECO-021 for exact proposal version, WM-ECO-008 for invoice/fiscal document and WM-ECO-009 for payment/settlement.
- Allocate no runtime or model identifier.

## Identity and mastership

Order identity is seller-issued and seller-scoped. OrderLine identity is composite within one order and never reused. Subscription uses provider namespace, subscription key and version lineage. Entitlement has its own subject, scope, period and grant/revocation lifecycle because it may outlive an order and remain in grace or suspended while subscription and payment states differ.

Every profile binding is append-only, pins an upstream revision or as-of time and cannot mutate its source master.

## Order and fulfilment

Order header and line states remain separately addressable; header state derives from lines. Accepted orders cite exact offer versions. Allocation records the decided outcome, firmness and inventory reservation reference; availability remains inventory-owned.

Delivered quantity changes only through line-bound despatch/fulfilment evidence. Already-despatched quantity is not patched in place. Outstanding, oversupply, backorder, hold and claim paths remain explicit.

Invoice, payment and delivery form separate directed chains. Invoice/payment state cannot change delivered or outstanding quantity. Settlement discharges a monetary obligation only.

## Subscription, entitlement and usage

Subscription relationship, entitlement, provisioning, billing, payment and usage have independent states and clocks. Active or paid status proves neither service availability nor delivered entitlement.

Entitlement records the right to consume: subject, permission/duty, scope, period, allowance and limits. Usage records measured consumption externally. Remaining allowance is a projection over entitlement and usage. Overage is a priced usage consequence and does not mutate entitlement.

## Change, suspension and renewal

Mid-cycle plan, price, term, entitlement or billing changes create successor subscription versions with reason, effective time, notice/consent and migration evidence. Issued versions remain immutable. Proration, credit, refund and overage are separate money assertions with basis, period, source and approval.

Suspension is a state assertion and does not equal cancellation or entitlement revocation. RenewalAssertion links predecessor and successor subscription versions and preserves prior prices, periods and originating offer.

## Acceptance scenario

Accepted offer Q1v2 creates Order O with goods line L1 and annual subscription line L2. L1 delivers 60 of 100; paying its invoice leaves 40 outstanding. L2 originates Subscription S v1 and Entitlement E1. Month 4 nonpayment suspends S only. Any restriction of the projected grant requires a separate authority-issued assertion with its own basis and effective time; months 1–3 remain unchanged. Month 5 may reactivate S independently. Renewal to plan B at a new price creates S v2 and a new price/entitlement binding; S v1, Q1v2, the old price and L1's outstanding quantity remain resolvable.

## Invariants

1. Order, line, subscription, entitlement, invoice and payment identities are distinct.
2. Invoice/payment state never changes delivered quantity.
3. Delivery changes only through line-bound fulfilment evidence.
4. Header state derives from line states.
5. Orders and subscriptions cite proposal versions.
6. Commercial commitment follows acceptance, before allocation/despatch.
7. Allocation does not determine availability.
8. Entitlement is subject/period-bounded and not implied by subscription state.
9. Usage is not entitlement; balance is a projection.
10. Subscription may exist without current-period payment.
11. Material changes create immutable successor versions.
12. Suspension, revocation, cancellation, termination, final bill and disposition remain separate.
13. Renewal never rewrites prior terms or prices.
14. Proration, credit, refund and overage state currency, basis, period, source and approval.
15. Profile bindings never mutate upstream masters.
16. Entitlement grant/revocation executes externally; the profile records evidence.

## Holds

Consumption Entitlement and the profile lack registry allocation; WM-ECO-020/022 have no settled relationship contract and retain single-provider/noncanonical holds; invoice/payment/offer relations are candidate or absent; WM-ECO-020 needs source and structural corrections; WM-ECO-022 needs a primary-source-derived finding surface and jurisdiction profiles; TM Forum/UBL/CPQ crosswalks, immutable pins and partial-delivery/suspension/renewal fixtures are incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
## Provider reconciliation

Grok conditionally accepts reuse and the five-way split, rejects Renewal as a type, and requires the profile to remain correspondence-only. Consumption Entitlement is retained only as an identifier-unassigned parked hypothesis. A reconstructable grant receives no key; promotion requires independent beneficiary/clock, subscription-free grant, surviving balance, transfer/split/pool lineage or external authority evidence. WM-FLW-015 owns usage; WM-ECO-024 remains unverified; proration stays invoice-owned.
## Frozen-audit remediation

Exactly one Claude Opus high no-tools audit returned ACCEPT WITH CORRECTIONS. Seventeen material defects were remediated without rerun. WM-FLW-015 is the sole usage authority; Consumption Entitlement is explicitly NO DECISION and its hypothetical objects are conditional on identityGate. Head and revision mastership are separated, revision-versus-successor rules are deterministic, and candidate exclusions bar all upstream line, subscription and payment authority.

The gate is disjunctive and evidence only opens registry adjudication. RenewalAssertion is a read-only mirror of the WM-ECO-022 link. WM-ECO-020 is the provisional fulfilment-evidence master pending WM-ECO-024. WM-ECO-008 owns refund, overage and proration lines. UsageProjectionBinding pins WM-FLW-015 plus as-of time and mints no balance. Base exclusivity is qualified by draft waivers. Thirty-five trace-linked fixtures cover the profile and allocation predicate registers; they remain declarative and non-executable.

