# Grok independent review — EM-PRD-01

Source conversation: https://grok.com/c/a4277525-4696-4d28-bc06-bdc303b762ff

## Verdict

Accept with conditions. Durable Product identity, market/time Offering identity, proposal-only quoted commercial assertions and a non-committing Roadmap Item profile form the correct split. Product Family does not need independent commercial identity or lifecycle. Price Plan remains a named, versioned Offering Catalogue component unless a promotion trigger proves independent reuse. No identifier is assigned and no canonical completeness is claimed.

Hard rejects: a Roadmap Item becoming orderable, priced or a new runtime identity; tariff change minting Product; Product Family owning price, contract or subscription; WM-ECO-021 mastering list price; and a SaaS commercial tier becoming Edition by default.

## Identity and mastership

Product Catalogue masters durable Product identity and Product-scoped Edition identity. Product remains the stable referent for support, installed base, successor relations, compliance and entitlement scope. Product Family is a classification key only. Re-familying does not change Product identity and retiring a Family cannot retire its Products.

Offering Catalogue masters market, time, channel and segment scoped Offering identity. Price Plan is initially a versioned, referenceable component. WM-ECO-021 owns only proposal-specific prices and terms and may cite the Offering and Price Plan version; it never mints or revises catalogue identity. Roadmap Item profiles WM-ACT-008 and has no catalogue mastership. Subscription instance mastership remains outside both catalogues.

## Product, edition and family

Product survives tariff, bundle, availability, channel and market-name changes. Edition is a constrained capability generation such as an architecture break, hardware revision or incompatible generation. A commercial tier, term, currency, seat or usage cut and discount live on Offering and Price Plan. Device model is Product; generation or revision may be Edition; physical serial instance remains downstream. A SaaS Edition exists only for a structurally distinct generation.

## Offering and price boundary

Offering is the sellable presentation with eligibility, standard terms, market/time window and catalogue price basis. A rate-only change keeps Product and Offering identities and creates a Price Plan version. Packaging, entitled cut, eligibility or market-promise changes create a successor Offering.

Do not permanently prohibit Price Plan promotion. Promote it within the Offering Catalogue candidate only if: one plan is reused by multiple Offerings; one Offering supports concurrent plans; a regulated tariff outlives one Offering; or a subscription changes plans mid-term without changing Offering. Until then, no Price Plan master identifier is justified.

Subscription does not belong to Product or Price Plan. It belongs to a separate commercial-agreement or billing domain and references the sold Offering plus either the catalogue Price Plan version or an accepted WM-ECO-021 quote. Bundles default to Offering composition; a composition becomes Product only when it is an engineered durable unit with its own identity and lifecycle.

## Roadmap and commitment

Roadmap Item is non-contractual planning intent. It cannot own orderability, price, eligibility, SLA, entitlement or subscription bindings. A roadmap row may target a Product or Edition candidate, while sellability requires a separate Offering and customer-specific terms require WM-ECO-021. Confidence changes, schedule slips and cancellation never mutate Product identity, Offering validity, quotes or subscriptions. Customer-facing roadmap publication is a non-binding projection; any contractual promise must be rewritten as Offering or quote terms.

## Invariants

1. Product and Edition survive tariff, bundle, channel, availability and Price Plan changes; Family is only classification.
2. Offering is the market/time commercial identity.
3. Catalogue price is an Offering-scoped Price Plan version; negotiated terms remain WM-ECO-021.
4. Subscription references Offering plus a price basis and never uses Product alone, Family or Roadmap Item as commercial basis.
5. Roadmap Item has no new runtime identity and is never an order, entitlement or invoice basis.
6. Internal and free products still require Product identity when they are operable or entitled units.
7. Bundle composition preserves constituent Product identities.
8. WM-ECO-021 never masters catalogue list price.
9. No identifiers are assigned by this review.

## Blockers

WM-ACT-008 and WM-ECO-021 constraints need explicit adoption in the candidate. A decision tree for Product versus Edition versus Offering successor versus Price Plan version is absent. Edition must be separated from commercial tier before allocation. Family must remain classification-only. Price Plan promotion triggers are recorded but unexecuted. The subscription dual-master sentence must be replaced with the external agreement/billing rule. Public roadmap-promise projection lacks a named owner. Device, SaaS, internal and free scenarios are design tests rather than observed evidence. Bundle-as-Product exception criteria must be explicit.
