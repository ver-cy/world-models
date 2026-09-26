# EM-LND-07 local synthesis

## Disposition

- Define Offering Portfolio Scope as a versioned governance/filter profile applied to the unallocated Offering Catalogue candidate.
- Define Offering Landscape as a non-authoritative, reproducible projection over product/service catalogues, offer, order, subscription/entitlement, contract/obligation, customer and measurement masters.
- Neither candidate has independent subject identity. Allocate no runtime/model identifier.

## Identity and mastership

Product, Service, Offering, Quote and Entitlement remain distinct. Product is a durable managed result; Service a provider-accountable outcome definition; Offering a market/channel/period availability of a product, service or bundle; Quote a recipient-specific proposal; Entitlement a right to consume with subject, scope, period and allowance.

The landscape reads these masters and never mutates price, order, subscription, contract, obligation, entitlement or consumer state. A view key consists of scope version, scenario, horizon and as-of; it identifies a computation, not a business portfolio.

## Portfolio boundary and comparison

Membership is derived from versioned market, channel, availability and policy predicates. Product or service without an active offering remains visible as such. Internal no-charge services enter through an explicit offering policy; missing price is not interpreted as free.

Each landscape version declares comparison basis, criterion set and comparability verdict. Criteria name metric, unit, observation window, source and justification. Commercial offerings can use contracted/realized revenue and margin; internal services use typed non-revenue value such as avoided cost, capability value, regulatory necessity or strategic option, with method and uncertainty. Zero revenue is a pricing fact, never proof of zero value.

## Duplicate outcomes

Potential duplication compares intended-outcome semantics, consumer overlap, entitlement overlap and substitution/migration evidence while retaining contradicting regulatory, jurisdictional, delivery and accountability differences. Each claim is suspected, substantiated or refuted with method, evidence, contradictions and confidence. Name similarity can open a review but is not evidence.

## Retirement and obligations

Offering retirement follows dated announced, closed-to-new, closed-to-change and withdrawn states. It does not cancel open quotes, order lines, subscriptions, contracts, obligations or entitlements. Each dependent master records its own authorized withdrawal, completion, migration, cancellation, discharge or expiry.

The retirement record identifies support and retention windows, successor or explicit no-successor reason, migration path, entitlement conversion and affected obligations. Historic offering versions remain resolvable.

## Time, scenario and acceptance

Every view pins scope version, scenario, horizon, source as-of and computation time. Scenario assumptions never overwrite source facts.

Two commercial products and one internal service are compared on a shared intended-outcome basis with justified class-specific criteria. The SaaS uses recurring economics, the device uses contracted revenue/margin and the internal service records revenue zero plus avoided-cost and reliability evidence. All are comparable only with declared adjustment; zero revenue does not determine value.

## Invariants

1. Offering, Product, Service, Quote and Entitlement remain distinct.
2. Comparison basis and criteria are explicit and justified.
3. Class-specific criteria are allowed only with declared adjustment.
4. Zero revenue never means zero value.
5. Missing price never means free.
6. Duplicate-outcome claims require semantic and consumer evidence.
7. Name similarity never proves duplication.
8. Membership derives from a versioned scope and as-of.
9. Retirement never silently cancels downstream commitments.
10. Every retirement records successor/migration or explicit no-successor.
11. The landscape reads masters and writes none.
12. Historic scope and view versions remain reproducible.

## Minimal profile shape

Offering Portfolio Scope records market, horizon, portfolio policy, scenario, membership predicates, effective interval, authority and provenance. Offering Landscape records view key, scope reference, as-of, comparison basis, offering rows with product/service/consumer/lifecycle/value/criteria, comparability verdicts, outcome-overlap claims, retirement/obligation-survival bindings, provenance and omissions.

## Holds

Product Catalogue, Offering Catalogue and Consumption Entitlement candidates remain unallocated. WM-ACT-004 has no complete publication specification, so service semantics rely on the EM-PRD-02 checkpoint. Adjacent commercial models remain non-canonical drafts, several with single-provider waivers. Crosswalks, relationship contracts, immutable pins and fixtures are absent. This checkpoint makes no canonical completeness, installability or publication claim.
