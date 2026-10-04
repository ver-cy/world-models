# EM-LND-07 local synthesis

## Disposition

- Define Offering Portfolio Scope as a versioned governance/filter profile applied to the unallocated Offering Catalogue candidate.
- Define Offering Landscape as a non-authoritative, reproducible projection over product/service catalogues, offer, order, subscription/entitlement, contract/obligation, customer and measurement masters.
- Neither candidate has independent subject identity. Allocate no runtime/model identifier.

## Identity and mastership

Product, Service, Offering, Quote and Entitlement remain distinct. Product is a durable managed result; Service a provider-accountable outcome definition; Offering a market/channel/period availability of a product, service or bundle; Quote a recipient-specific proposal; Entitlement a right to consume with subject, scope, period and allowance.

The landscape reads these masters and never mutates or authorises price, order, subscription, contract, obligation, entitlement or consumer state. A view key consists of scope version, scenario, horizon and as-of; it identifies a computation, not a business portfolio.

## Portfolio boundary and comparison

Membership is derived from versioned market, channel, availability and policy predicates. Inclusion, exclusion, override and exception are explicit outcomes. Product or service without an active offering remains visible as such. Internal no-charge services enter through an explicit offering policy; missing price is not interpreted as free.

Each landscape version declares comparison basis, criterion set and a verdict of comparable, partial or incomparable. Criteria name metric, unit, observation window, source and justification. Partial comparison requires a justified outcome class, criteria restated per class and a stated adjustment. Commercial offerings can use contracted/realized revenue and margin; internal services use typed non-revenue value such as avoided cost, capability value, regulatory necessity or strategic option, with method and uncertainty. Zero revenue is a pricing fact, never proof of zero value and never scored as zero value.

## Duplicate outcomes

Potential duplication compares intended-outcome semantics, consumer overlap, entitlement overlap and substitution/migration evidence while retaining contradicting regulatory, jurisdictional, delivery and accountability differences. Each claim is suspected, substantiated or refuted with method, evidence, contradictions and confidence. Missing any evidence class caps the status at suspected. Name similarity can open a review but is not evidence.

## Retirement and obligations

Offering retirement follows dated announced, closed-to-new, closed-to-change and withdrawn states. It does not cancel open quotes, order lines, subscriptions, contracts, obligations or entitlements. Each dependent master records its own authorized withdrawal, completion, migration, cancellation, discharge or expiry.

The retirement record identifies support and retention windows, successor or explicit no-successor reason, migration path, entitlement conversion and affected obligations. Historic offering versions remain resolvable.

## Time, scenario and acceptance

Every view pins scope version, scenario, horizon, source as-of and computation time. Scenario assumptions never overwrite source facts. A changed predicate, market scope or policy creates a successor version, never an in-place rewrite.

Two commercial products and one internal service are compared on a shared intended-outcome basis with justified class-specific criteria. The SaaS uses recurring economics, the device uses contracted revenue/margin and the internal service records revenue zero plus avoided-cost and reliability evidence. All are partial, with the declared adjustment recorded; zero revenue does not determine value.

## Invariants

1. Neither candidate is a source of commercial commitment or entitlement.
2. Product, Service, Offering, Quote and Entitlement remain distinct subjects; none is a subtype of scope or landscape.
3. Scope membership is predicate-derived from versioned market, channel, availability and policy predicates at a stated as-of; never owned membership identity.
4. The landscape reads masters and writes none, and cannot authorise a quote, order, subscription, entitlement grant or retirement.
5. Decisions and citations reference catalogue state plus a frozen scope version, never the landscape.
6. Comparison without a declared basis, class-specific justified criteria and an explicit verdict is invalid; co-membership is not comparability.
7. A verdict is exactly one of comparable, partial, incomparable; partial requires a declared justified outcome class, restated class-specific criteria and a stated adjustment.
8. Zero external revenue never implies zero value and missing price never means free; internal services carry typed non-revenue value with method and uncertainty.
9. A duplicate-outcome claim fails if semantic, consumer, entitlement or substitution evidence is missing; name similarity is never evidence.
10. Retirement never cancels downstream commitments by inference; each closes on its own master.
11. Every retirement record states dated states, support and retention windows, migration, entitlement conversion, and successor or explicit no-successor reason.
12. Prior scope and view versions remain addressable after supersession; source as-of and computation time stay distinct; no in-place rewrite.
13. Allocated, versioned catalogue masters must exist before a scope profile is evaluated or a landscape released.

## Minimal profile shape

Offering Portfolio Scope records a configuration version identifier, profile status, effective interval, market/channel/availability/policy predicates, explicit outcomes, portfolio policy, scenario, governance owner role, targeted catalogue version, supersession link, authority and provenance. Offering Landscape records its view key, projection and computation times, audience, non-authoritative flag, refresh rule, catalogue-baseline provenance, comparison basis, offering rows, justified criteria, verdicts, overlap claims, retirement and obligation-survival bindings, declared omissions, and contains no commitment attributes.

## Holds

Product Catalogue, Offering Catalogue and Consumption Entitlement candidates remain unallocated. WM-ACT-004 has no complete publication specification, so service semantics rely on the EM-PRD-02 checkpoint. Adjacent commercial models remain non-canonical drafts, several with single-provider waivers. Crosswalks, relationship contracts and immutable pins are absent. The Grok response was provider-truncated after “WM-ACT-004 Service Definition”; no missing text is reconstructed. This checkpoint makes no canonical completeness, installability or publication claim.
