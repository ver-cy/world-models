# EM-PRD-01 local synthesis

## Disposition

- Create an identifier-unassigned **Product Catalogue** candidate owning Product, Product Family and Edition identity and lifecycle.
- Create an identifier-unassigned **Offering Catalogue** candidate owning market- and time-scoped Offering identity; keep Price Plan as a non-addressable versioned component reached only through Offering identity, unique plan name and version ordinal.
- Reuse WM-ECO-021 only for proposal-specific quoted prices and terms. It explicitly excludes product, catalogue and price-list master lifecycles.
- Profile WM-ACT-008 for Roadmap Item. The profile restricts intent to non-contractual planning and creates no runtime identifier.

Product remains stable across tariff changes, market withdrawal and ordinary editions. A new Product is justified by an independently governed value proposition, target segment, entitlement boundary, certification identity, roadmap or end-of-life decision. Product Family groups durable product identities and is not a bundle, bill of material or price container.

Offering is a scoped availability assertion for one product or bundle in a market, channel and validity interval. Its Price Plan component records currency, unit or quantity basis, recurrence class, tiers and approval provenance. A recipient-specific quote remains in WM-ECO-021 and references the Price Plan version from which it was derived.

Roadmap Item uses WM-ACT-008 intent, schedule, confidence, version and realization-link semantics. It cannot carry contractual commitment basis and never proves feature availability, release, entitlement, task completion or delivery. Availability is evidenced by an authoritative Offering or release record; delivery by an act record.

## Invariants

1. Product identity does not change because price, tariff, bundle membership or availability changes.
2. An Offering identifies its product or bundle, market or channel, eligibility and availability period.
3. Every price amount declares currency, unit or quantity basis and recurrence class; free is explicit zero, not missing data.
4. Subscription instance mastership belongs to an external agreement/billing domain. Every agreement pins Offering identity plus its contained Price Plan path; a WM-ECO-021 quote is only an additional price/term overlay and cannot introduce entitlement.
5. Product may exist without an Offering; Offering cannot exist without a product or bundle reference.
6. Edition continuity requires recorded rationale and entitlement conversion; an independently governed lifecycle creates a new Product.
7. A bundle is an Offering composition unless it gains durable identity, its own roadmap and independent lifecycle.
8. Roadmap confidence changes revise only the Roadmap Item.
9. Roadmap Item proves neither availability nor contractual obligation.
10. All identities, versions, authority and provenance remain source-mastered and effective-dated.

## Scenario result

SaaS, devices and internal products share Product semantics. SaaS may use recurring pricing; a device may use one-time pricing plus a separate service Offering; an internal product may have an internal Offering with explicit zero or no-charge policy. A tariff change creates a new Price Plan version and revised Offering, never a new software Product. A roadmap confidence or target-window change revises the plan only.

## Holds

Both base specifications are pinned non-canonical reviewable drafts. Registry allocations, relation contracts, agreement authority, crosswalks and executable fixtures remain absent. Price Plan is explicitly non-addressable; any future cross-Offering reuse requires a new allocation review. No publication or installability claim is made.
