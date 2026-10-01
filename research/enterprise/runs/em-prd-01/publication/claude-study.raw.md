# Verdict

Split the contour three ways.

1. **RoadmapItem → bounded profile of WM-ACT-008** (`profile`, no new identifier). A roadmap item is an intention bound to time with a declared confidence; WM-ACT-008 already owns that semantics and already excludes acts, tasks, process definitions and contract formation. The profile *restricts* rather than extends.
2. **Offering price-in-a-proposal → reuse WM-ECO-021 by reference only.** No extension, no profile. The quoted price stays in the proposal; EM-PRD-01 never masters it.
3. **Product, ProductFamily, Offering, PricePlan → two identifier-unassigned candidates**, because no dossier model claims them and both bases explicitly disclaim them:
   - **Candidate A — product master**: Product, ProductFamily, edition/variant. Durable identity.
   - **Candidate B — offering master**: Offering with PricePlan as a bounded internal component (own stable internal id and version counter, shareable across offerings; not its own registry candidate).

`complete-reserved` is not available for A or B — there is no reserved registry entry to complete. It *is* the correct state for WM-ACT-008 itself, whose registry record reads `described-previous-version` / `migration-boundary-review`; the roadmap profile is conditional on that review closing.

# Evidence

- WM-ECO-021 `out_of_scope` forbids "owning Party, **Product**, Service, Right, **Catalogue**, **Price List** … masters"; its boundary note states those masters "supply identities and source terms; the proposal owns only version-specific commercial assertions and references". So it cannot host Product, ProductFamily, Offering or a reusable PricePlan — only the proposal-specific quoted price.
- WM-ECO-021 carries `publishableCanonical: false`, `single-provider-waiver` with Claude and Grok waived, and an explicit absence-of-external-review hold. Reuse must therefore be reference-only, not structural inheritance.
- WM-ACT-008 fits roadmap closely: `planningHorizon` ↔ `horizon`, entry/date-constraint binding ↔ `target_window`, `confidenceLevel` + `durationEstimateRange` ↔ `confidence`, `goalStatement` ↔ `theme`, `intentMode` (FHIR RequestIntent gradient) gives the proposal-vs-order distinction, and `f-realization-and-fulfilment-link` separates intention from the act that realised it. Its boundary notes already fence Task (WM-ACT-006), Act/Action, Process & Workflow and Project.
- WM-ACT-008 risk: `f-commitment-parties-and-terms` can bind an intention to a named beneficiary with `commitmentBasis = contractual`. The profile must close this, or a roadmap item becomes a promise.
- `vercy_candidates` evidence depth is `index-and-publication-metadata`; no semantic crosswalk is verified.

# Identity and mastership

- **Product**: durable identity for a managed result offered to a consumer. Survives edition, tariff, bundle membership, market withdrawal and end-of-sale. Mastered by product catalogue/PLM; owner *Руководитель продукта*.
- **ProductFamily**: grouping identity only — shared value proposition and roadmap home. Not a bill of material, not a configuration structure (EM-PRD-02/03 boundary), not a price container.
- **Offering**: market- and time-scoped commercial availability of one product or bundle. Identity = product/bundle ref + market/channel + eligibility + availability period + price plan ref. High churn, versioned independently of Product. Mastered by catalogue/commerce; price approval authority is separate and delegated (mirroring WM-ECO-021's authority hold).
- **PricePlan**: reusable price basis (amounts, currency, unit/quantity basis, recurrence class, tiers). Component of B, referencable from many offerings. Split trigger for a future candidate: externally mastered regulated tariffs (utility/telecom rate authority).
- **RoadmapItem**: intention mastered in discovery/product management, never in the catalogue.

# Product-family-edition rules

An edition **continues** the product when all hold: same customer-facing result and target segment; a migration or upgrade path exists; entitlements from prior editions convert; support/warranty and certification identity unchanged; one `lifecycle_stage` decision governs both.

An edition **forms a new product** when any hold: distinct `value_proposition` or `target_segment`; independent end-of-life decision; non-convertible entitlements; separate regulatory/certification identity; its own roadmap.

Distinguish **edition** (feature-scope variant of the same product, in A) from **tier** (price-scoped packaging, in B). Tiers never create editions.

# Offering and pricing

Offering holds `offering_code`, `eligibility`, `availability_period`, market/channel, and a PricePlan reference. PricePlan holds the reusable basis; the proposal-specific quoted amount — discounted, recipient-specific, validity-bounded — stays in WM-ECO-021 and references the PricePlan version it derived from. Bundles are Offering-level compositions of product references; a bundle becomes a Product only when it acquires durable identity, its own roadmap and its own lifecycle independent of its members. Subscription is a property of the price line's recurrence class, never of Product — that is what keeps devices clean.

# Roadmap boundary

RoadmapItem = `intentMode` at proposal strength or weaker, `theme`, `horizon`, `target_window` (as a flexible date constraint, never a committed date), coded `confidence` with an asserted-at time. Profile prohibitions: no contractual commitment basis; no assignee or task lifecycle (WM-ACT-006); no release or version identity; no realization claim as proof of availability. Availability is provable only by a current Offering; delivery only by a referenced act. WM-ACT-008's `confidenceLevel` is numeric percentile — the coded roadmap scale needs a declared value set and a stated mapping, otherwise the two are silently conflated.

# Invariants

1. An Offering has at least one market/channel scope and one availability period; lacking either it is a draft, not an Offering.
2. Every asserted price amount carries currency, unit or quantity basis, and recurrence class (one-time, recurring, usage).
3. Zero price is asserted as zero, never by absence; "no price recorded" is a distinct state.
4. A PricePlan revision never changes Product identity or Product version.
5. An Offering references a Product or bundle; it never restates the value proposition as its own master claim.
6. A RoadmapItem proves neither feature availability, entitlement, release, task, nor delivery.
7. A RoadmapItem carries no contractual commitment basis; a customer-facing promise is a separate authorized record that references it.
8. A Product may exist with zero Offerings; an Offering cannot exist without a Product or bundle reference.
9. Edition continuity requires a recorded rationale and entitlement-conversion statement; absent that, treat as a new Product.
10. A confidence change revises the RoadmapItem only — never Offering or Product.

# Scenarios

| Test | Expected |
|---|---|
| Edition continuity | Same product, new edition node; rationale + conversion recorded (rule set above). |
| Bundle | New Offering composing product refs; no new Product unless durable identity + own roadmap appear. |
| SaaS | Offering with recurring price line; `product_kind = software service`. |
| Device | Offering with one-time price line plus optional separate service Offering; no subscription inherited (invariant 2, 10). |
| Internal product | Product + Offering scoped to an internal market with zero/none price; passes invariant 3. |
| **Tariff change (negative case)** | New PricePlan version → new or revised Offering. Product identity and version unchanged. Creating a new Product here **fails** invariant 4. |
| Free product | Offering with explicit zero amount and currency; still has market and period. |
| Roadmap confidence change | RoadmapItem version increments; no catalogue effect (invariants 6, 10). |

# Minimal profile or candidate shape

All fields `candidate-not-normative`; no identifiers assigned.

- **Candidate A (product master)**: `product_identity`, `product_name`, `product_kind`, `value_proposition`, `target_segment`, `lifecycle_stage`, `family_ref`, `edition_of_ref`, `entitlement_conversion_note`, `version`, `owner_ref`.
- **Candidate B (offering master)**: `offering_identity`, `offering_code`, `product_or_bundle_ref`, `market_scope`, `channel`, `eligibility`, `availability_period`, `bundle_member_ref[]`, `price_plan_ref`, `version`; component **PricePlan**: `price_plan_identity`, `price_basis`, `amount[]{currency, unit_or_quantity_basis, recurrence_class, tier}`, `validity`, `approval_ref`, `version`.
- **RoadmapItem (profile of WM-ACT-008)**: `intentMode` (restricted), `theme`, `horizon`, `target_window`, `confidence` (coded + asserted_at), `subject_ref` → A or B, `commitmentBasis` prohibited.

# Holds

No canonical completeness and no installability is claimed. Both bases are non-canonical reviewable drafts; WM-ECO-021 additionally rests on a single-provider waiver with external review waived, and WM-ACT-008 carries unresolved source-verification and multi-profile-validation holds. The WM-ACT-008 registry record (`described-previous-version`) disagrees with its published draft — reconcile before profiling. Semantic crosswalks for both target models are unverified (index-and-publication metadata only); registry relations and v1 fields remain non-normative. Comparison tracks (TM Forum SID, IDTA AAS, PLM/software practice) were not executed here, so no alignment claim is made. Identifier assignment, immutable refs and fixture checks remain open for candidates A and B.
