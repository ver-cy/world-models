# Frozen audit prompt — EM-COM-03

Audit only the frozen material below. Use no tools and no outside knowledge. Do not invent identifiers or claim standards compliance.

Return a concise verdict and enumerate only material defects. Check the identityGate, anti-dual-mastership, source pins, state/lifecycle separation, line quantity authority, subscription versioning, fulfilment boundary, usage authority, proration ownership, correspondence-only profile, unsupported model references and fixture traceability. For each defect give the smallest remediation. End with the exact additional fixtures required. This is the one frozen audit; do not request a second audit.

## LOCAL EVIDENCE

```
# EM-COM-03 local synthesis

## Disposition

- Reuse WM-ECO-020 for Order and OrderLine, including line-level allocation, despatch evidence, delivered/outstanding quantity, exceptions and closure.
- Reuse WM-ECO-022 for Subscription, plan/price versions, term, billing and renewal schedules, suspension and usage/allowance references.
- Define a thin Enterprise Order–Subscription–Entitlement profile for cross-model bindings: OfferVersionBinding, OrderSubscriptionOrigination, EntitlementBinding, RenewalAssertion, FulfilmentEvidenceBinding and SettlementBinding. The profile remains identifier-unassigned.
- Add an identifier-unassigned **Consumption Entitlement** candidate. Its right-to-consume identity and lifecycle are independent from Order, Subscription and actual Usage.
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

Accepted offer Q1v2 creates Order O with goods line L1 and annual subscription line L2. L1 delivers 60 of 100; paying its invoice leaves 40 outstanding. L2 originates Subscription S v1 and Entitlement E1. Month 4 nonpayment suspends S and E1 without rewriting months 1–3 or revoking the grant. Month 5 reactivates them. Renewal to plan B at a new price creates S v2 and a new price/entitlement binding; S v1, Q1v2, the old price and L1's outstanding quantity remain resolvable.

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


```

## PROVIDER COMPARISON

```
# EM-COM-03 provider comparison

Claude and Grok agree on reuse of WM-ECO-020 for Order and OrderLine, WM-ECO-022 for Subscription versions, WM-ECO-021 for pinned offer versions, WM-ECO-008 for invoice-side monetary consequences and WM-ECO-009 for payment allocation. They agree that fulfilment, invoice, payment, entitlement and usage are separate directed facts; paid never means delivered, entitled or used. Renewal is a typed predecessor-to-successor subscription-version link, not an entity or model. Mid-cycle price changes create immutable successor versions and proration remains invoice-owned.

The reconciled shape adopts Grok's stricter identity challenge. Consumption Entitlement remains an identifier-unassigned parked hypothesis rather than an assumed peer master. A grant reconstructed completely from subscription version, offer item, beneficiary, period and grant source receives no independent key. Promotion requires evidence of an independently surviving grant, such as separate beneficiaries or clocks, a grant without subscription, balance surviving cancellation, transfer/split/pool lineage, or an external licence authority. Evidence does not itself allocate an identifier.

The Enterprise profile is correspondence-only. It mints no identity, version head, quantity, balance, lifecycle state or proration fact. WM-FLW-015 owns actual usage events; usage never creates a grant. WM-ECO-024 remains an unverified fulfilment boundary. All bindings are append-only and source-pinned. The candidate and profile are explicitly non-publishable while base relation ledgers, crosswalks and executable fixtures remain unresolved.

```

## ALLOCATION CANDIDATE

```
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-COM-03",
  "proposedName": "Consumption Entitlement",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A granted right to consume remains identifiable across order closure, subscription version changes, provisioning, payment changes, suspension, grace, usage and renewal.",
    "versionIdentity": "Changes to subject, permission, scope, period, allowance, limits or grant basis create immutable entitlement revisions or successors while preserving prior consumption evidence.",
    "independentLifecycle": [
      "proposed",
      "granted",
      "active",
      "suspended",
      "grace",
      "expired",
      "revoked",
      "terminated",
      "superseded"
    ],
    "mastership": "entitlement or service-access authority"
  },
  "boundary": {
    "owns": [
      "conditional independent consumption-entitlement identity only after identityGate evidence",
      "entitled subject and beneficiary bindings",
      "permission or duty, resource scope and consuming purpose",
      "effective period, allowance, limits and reset rules",
      "grant, activation, suspension, grace, revocation, expiry and termination state",
      "successor lineage and external execution evidence bindings"
    ],
    "references": [
      {
        "target": "WM-ECO-020",
        "purpose": "Originating order and order line"
      },
      {
        "target": "WM-ECO-022",
        "purpose": "Subscription version and plan context"
      },
      {
        "target": "WM-ECO-021",
        "purpose": "Accepted proposal or offer version"
      },
      {
        "target": "WM-MAT-008",
        "purpose": "Measured usage observations used for allowance projections"
      },
      {
        "target": "WM-ECO-008",
        "purpose": "Invoice or fiscal document references"
      },
      {
        "target": "WM-ECO-009",
        "purpose": "Payment or settlement references"
      },
      {
        "target": "WM-FLW-015",
        "purpose": "Actual resource-consumption events and corrections"
      }
    ],
    "excludes": [
      "order, subscription, offer, invoice or payment identity",
      "service provisioning and runtime-availability state",
      "usage observation and meter mastership",
      "remaining allowance as stored authoritative fact",
      "automatic grant from active, paid or provisioned status",
      "subscription-derived grants that are fully reconstructable from pinned source facts",
      "renewal as an entity or lifecycle master",
      "proration, credit, debit and invoice-line mastership"
    ]
  },
  "objects": {
    "ConsumptionEntitlement": {
      "identity": [
        "entitlementId"
      ],
      "required": [
        "subjectRef",
        "permission",
        "resourceScope",
        "validFrom",
        "grantBasisRef",
        "status"
      ],
      "optional": [
        "validTo",
        "purpose",
        "allowance",
        "limits",
        "resetRule",
        "successorRef"
      ],
      "lifecycle": [
        "proposed",
        "granted",
        "active",
        "suspended",
        "grace",
        "expired",
        "revoked",
        "terminated",
        "superseded"
      ]
    },
    "EntitlementRevision": {
      "identity": [
        "entitlementId",
        "revision"
      ],
      "required": [
        "permission",
        "resourceScope",
        "period",
        "contentDigest",
        "effectiveFrom"
      ],
      "optional": [
        "allowance",
        "limits",
        "resetRule",
        "effectiveTo",
        "supersedesRevision"
      ]
    }
  },
  "invariants": [
    "Order, line, subscription, entitlement, invoice, payment and usage observation retain distinct identities.",
    "Entitlement is bounded by subject, permission, scope and period and is never implied by active or paid subscription state.",
    "Every entitlement cites an authoritative grant basis and exact originating revision where applicable.",
    "Usage is measured externally and never mutates entitlement identity or issued revision.",
    "Remaining allowance is a projection over entitlement terms and qualified usage observations.",
    "Overage is a priced usage consequence and never silently expands entitlement allowance.",
    "Suspension, grace, revocation, cancellation, termination and expiry remain distinct states.",
    "Service availability and provisioning never prove that an entitlement is active.",
    "Material changes to scope, allowance, limits or period create immutable successor revisions or entitlements.",
    "Renewal links predecessor and successor entitlement or subscription versions and never rewrites prior terms.",
    "External grant or revocation execution records are evidence and never replace the governed entitlement transition.",
    "Retired entitlement identifiers and all prior revisions remain resolvable and are never recycled."
  ],
  "holds": [
    "Independent Consumption Entitlement identity is unproven and remains a parked identifier-unassigned hypothesis.",
    "Registry namespace and identifier allocation are forbidden until identityGate evidence passes.",
    "WM-ECO-020/022 relation ledgers, WM-ECO-024 fulfilment boundary and WM-FLW-015 usage edge are unresolved.",
    "Base models remain reviewable drafts under waiver; crosswalks and executable fixtures are absent.",
    "Package is declarative and non-publishable."
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-single-frozen-audit",
  "publishable": false,
  "identityConclusion": "PARKED HYPOTHESIS: independent identity remains unproven until a fixture demonstrates a grant that cannot be reconstructed from a pinned subscription version, offer item, beneficiary, period and grant source.",
  "identityGate": {
    "default": "project entitlement from pinned subscription-version plus offer-item, beneficiary, period and grant-source; do not mint identity",
    "promotionEvidenceRequired": [
      "independent beneficiary or clock within one subscription version",
      "prepaid or promotional grant without a subscription",
      "remaining balance surviving subscription cancellation",
      "transfer, split or pooled grant with independent lineage",
      "external licence or authorization master distinct from the commercial instrument"
    ],
    "antiDualMastership": "A reconstructable grant cannot receive a second authoritative key."
  }
}

```

## PROFILE CANDIDATE

```
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-COM-03",
  "name": "Enterprise Order, Subscription and Entitlement Binding",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ECO-020",
    "WM-ECO-022",
    "WM-ECO-021",
    "WM-ECO-008",
    "WM-ECO-009",
    "WM-FLW-015"
  ],
  "constraints": [
    "Profile mints no identity, lifecycle state, quantity, balance, version head or monetary consequence.",
    "WM-ECO-020 exclusively owns seller-side Order, OrderLine and line quantity progress.",
    "WM-ECO-022 exclusively owns Subscription identity, version chain, terms, suspension and renewal clocks.",
    "WM-ECO-021 owns the pinned offer or proposal version.",
    "WM-ECO-008 owns issued invoice, credit, debit and proration lines; profile stores no proration state.",
    "WM-ECO-009 owns payment allocation, residual and settlement exceptions.",
    "WM-FLW-015 owns actual usage events and corrections; usage never creates a grant.",
    "Goods-line fulfilment changes only through line-bound fulfilment evidence; payment cannot change line residuals.",
    "Subscription-originating lines close by creating or activating a subscription version, not by shipment.",
    "Renewal and mid-cycle change are typed predecessor-to-successor version links, never types or models.",
    "One effective subscription version exists per instrument and instant; effective versions are immutable.",
    "Suspension is reversible and distinct from entitlement revocation, cancellation and termination.",
    "Paid, delivered, entitled and used remain independent claims with independent authority.",
    "Every binding pins source identity, revision or valid/as-of time and is append-only with supersession.",
    "Reconstructable grants remain projections; only identityGate evidence permits a future independent entitlement candidate.",
    "Profile cannot cascade-delete or mutate any upstream master."
  ],
  "holds": [
    "Consumption Entitlement is a parked unassigned hypothesis, not a profile member with implicit identity.",
    "Base relationship contracts and WM-ECO-024 fulfilment boundary remain unresolved.",
    "Independent Grok review is reconciled; one frozen audit is pending.",
    "No runtime ID, registry allocation or publication is allowed."
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-single-frozen-audit",
  "publishable": false,
  "profileRole": "correspondence-only, non-mastering subject seam"
}

```

## FIXTURES

```
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Consumption Entitlement",
  "cases": [
    {
      "id": "goods-partial-delivery",
      "kind": "positive",
      "covers": [
        "P08"
      ],
      "input": "Order line quantity 10 has line-bound fulfilment evidence for 6.",
      "expect": "Delivered is 6 and outstanding is 4; invoice and payment facts remain independent."
    },
    {
      "id": "paid-outstanding-goods",
      "kind": "negative",
      "covers": [
        "P08",
        "P13"
      ],
      "input": "Invoice for quantity 10 is fully settled while only 6 were fulfilled.",
      "expect": "Payment closes no fulfilment residual; outstanding remains 4."
    },
    {
      "id": "subscription-origin",
      "kind": "positive",
      "covers": [
        "P02",
        "P03",
        "P09"
      ],
      "input": "Accepted subscription order line pins an offer version and activates Subscription S v1.",
      "expect": "Order line and subscription retain distinct identities and the line closes by activation, not shipment."
    },
    {
      "id": "subscription-suspension",
      "kind": "positive",
      "covers": [
        "P11",
        "P12"
      ],
      "input": "S v1 is suspended mid-term and later reactivated.",
      "expect": "Same immutable version remains; reversible suspension does not imply revocation or cancellation."
    },
    {
      "id": "renewal-new-price",
      "kind": "positive",
      "covers": [
        "P05",
        "P10",
        "P11"
      ],
      "input": "Renewal selects a new offer price for the next term.",
      "expect": "Successor subscription version pins the new offer; prior version and invoices remain unchanged; any proration is invoice-owned."
    },
    {
      "id": "renewal-as-model",
      "kind": "negative",
      "covers": [
        "P10"
      ],
      "input": "A standalone Renewal identity is minted.",
      "expect": "Rejected; renewal is a typed predecessor-successor link."
    },
    {
      "id": "usage-creates-grant",
      "kind": "negative",
      "covers": [
        "P07",
        "P13"
      ],
      "input": "Observed usage is treated as proof of entitlement.",
      "expect": "Rejected; usage is externally mastered and creates no grant."
    },
    {
      "id": "active-implies-entitled",
      "kind": "negative",
      "covers": [
        "P13",
        "P15"
      ],
      "input": "Active subscription is treated as an independently keyed entitlement.",
      "expect": "Rejected unless identityGate evidence proves a non-reconstructable grant."
    },
    {
      "id": "derived-grant-no-key",
      "kind": "positive",
      "covers": [
        "P15"
      ],
      "input": "Grant is fully reconstructable from subscription version, offer item, beneficiary, period and source.",
      "expect": "It remains a projection and receives no independent key."
    },
    {
      "id": "multi-beneficiary-independent-clocks",
      "kind": "positive",
      "covers": [
        "P15"
      ],
      "input": "One subscription version grants separately suspended seat rights to different beneficiaries.",
      "expect": "Recorded as evidence supporting but not automatically allocating an independent entitlement identity."
    },
    {
      "id": "promo-no-subscription",
      "kind": "positive",
      "covers": [
        "P15"
      ],
      "input": "A promotional consumption grant exists without a subscription.",
      "expect": "Recorded as identityGate evidence; identifier remains unassigned pending registry adjudication."
    },
    {
      "id": "balance-survives-cancellation",
      "kind": "positive",
      "covers": [
        "P12",
        "P15"
      ],
      "input": "Prepaid remaining balance survives subscription cancellation.",
      "expect": "Cancellation does not erase the candidate grant; evidence is preserved for boundary adjudication."
    },
    {
      "id": "transfer-split-pool",
      "kind": "positive",
      "covers": [
        "P15"
      ],
      "input": "A grant is transferred and split into a pooled balance with independent lineage.",
      "expect": "Evidence supports independent lifecycle without changing allocation state."
    },
    {
      "id": "profile-stores-balance",
      "kind": "negative",
      "covers": [
        "P01",
        "P15"
      ],
      "input": "The profile stores authoritative remaining allowance.",
      "expect": "Rejected as stealth mastership."
    },
    {
      "id": "profile-stores-version-head",
      "kind": "negative",
      "covers": [
        "P01",
        "P03"
      ],
      "input": "The profile advances the subscription version head.",
      "expect": "Rejected; WM-ECO-022 exclusively owns it."
    },
    {
      "id": "proration-in-profile",
      "kind": "negative",
      "covers": [
        "P01",
        "P05"
      ],
      "input": "Profile records proration as its own state.",
      "expect": "Rejected; economic consequence is materialized on WM-ECO-008 lines."
    },
    {
      "id": "suspension-equals-revocation",
      "kind": "negative",
      "covers": [
        "P12"
      ],
      "input": "Suspension permanently revokes the right and cancels the subscription.",
      "expect": "Rejected; clocks and authorities are separate."
    },
    {
      "id": "offer-unpinned",
      "kind": "negative",
      "covers": [
        "P04",
        "P14"
      ],
      "input": "Order or subscription references an offer name without version or valid time.",
      "expect": "Rejected as non-reproducible."
    },
    {
      "id": "cascade-delete",
      "kind": "negative",
      "covers": [
        "P16"
      ],
      "input": "Deleting the profile deletes an order or subscription master.",
      "expect": "Rejected; bindings never cascade-delete masters."
    },
    {
      "id": "usage-correction",
      "kind": "positive",
      "covers": [
        "P07",
        "P14"
      ],
      "input": "A usage event is corrected after billing.",
      "expect": "Correction remains WM-FLW-015-owned and triggers downstream recomputation without mutating entitlement or subscription history."
    }
  ]
}

```
