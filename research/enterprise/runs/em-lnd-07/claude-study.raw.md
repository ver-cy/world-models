# Verdict

Neither `OfferingLandscape` nor `OfferingPortfolioScope` earns independent identity as a subject model. Decide EM-LND-07 as **two governed profiles over existing and pending subject models**:

- **OfferingPortfolioScope** — a scope/boundary declaration profile (market scope, horizon, portfolio policy, scenario) applied to the Offering Catalogue candidate reserved in EM-PRD-01. It is a filter and governance frame, not an object with its own offerings.
- **OfferingLandscape** — a projection profile: a scenario-and-horizon-bound, non-authoritative view computed over Product Catalogue, Offering Catalogue, WM-ACT-004 (Service Definition), WM-ECO-021, WM-ECO-020, WM-ECO-022, the pending Consumption Entitlement candidate, WM-ECO-006/WM-XCT-029 and WM-ORG-014.

The registry has no target IDs for EM-LND-07, and nothing in the frozen dossier supplies a landscape master system. Both remain identifier-unassigned. The only candidate with a plausible claim to standalone identity is **OfferingPortfolioScope**, and it fails the test: its four candidate fields are all governance qualifiers with no subject of their own once the offering set is referenced.

# Evidence

`candidate_properties_from_v1` for LND-07 lists exactly four fields — `market_scope`, `horizon`, `portfolio_policy`, `scenario` — all `candidate-not-normative`. None asserts an offering, a consumer, a price or an outcome. Every substantive element the contour's scope names ("предложения, жизненных циклов, потребителей и экономики") is already mastered elsewhere:

- Offering identity, market and validity period: EM-PRD-01's Offering Catalogue candidate (invariant "Предложение имеет рынок и период").
- Service outcome and consumer scope: EM-PRD-02 / WM-ACT-004 (`service_outcome`, `consumer_scope`).
- Quoted commercial terms: WM-ECO-021, which explicitly excludes owning "Catalogue, Price List … masters".
- Orders and delivered/outstanding accounting: WM-ECO-020.
- Recurring economics and renewal: WM-ECO-022.
- Obligations: WM-XCT-029 (mixin), anchored on WM-ECO-006.
- Consumers: WM-ORG-014, which masters the seller-scoped relationship, not party identity.

`vercy_candidates` is empty and `related_research_contours` is empty. A landscape that owns nothing and is not referenced by anything is a view.

# Identity/mastership

No new identity. Mastership stays: Product/Offering Catalogue candidates (EM-PRD-01, identifier-unassigned), WM-ACT-004 for Service Definition, the commercial chain models as above. The landscape profile mints only a **view key**: `(portfolio scope ref, scenario code, horizon interval, as-of instant)`. That key identifies a computation, not a portfolio. Candidate master systems named in the dossier — "Реестр моделей, sources.yaml, vercy.lock, политики" — are model-governance artefacts, which confirms scope is policy, not subject data.

Scope declarations are effective-dated and append-only; a changed `market_scope` or `portfolio_policy` creates a successor scope version, never a silent rewrite, so a landscape computed last quarter remains reproducible.

# Portfolio boundary

Membership is **derived, not asserted**: an offering is in scope when its market, channel, availability period and policy predicates satisfy the scope version, evaluated as-of a stated instant. This avoids a hand-curated membership list that drifts from the catalogue.

In scope: offering identity and availability window, the product or service it offers, consumer segment reference, economics summary, lifecycle stage, retirement state.
Out of scope: pricing approval, order acceptance, entitlement grant, contract formation, obligation discharge, revenue recognition. The landscape reads these; it never mutates them. Internal services with no commercial offering enter through a scope predicate that admits `Offering` records with an explicit no-charge policy — EM-PRD-01 already requires free to be an explicit zero, not missing data.

# Product/service/offering

Five identities stay distinct and are not collapsed by the landscape:

| Identity | Owner | Distinguishing test |
|---|---|---|
| Product | Product Catalogue candidate | Durable managed result; survives tariff, market and edition change |
| Service | WM-ACT-004 | Provider-accountable outcome for a consumer scope; survives endpoint change |
| Offering | Offering Catalogue candidate | Scoped availability of a product/service/bundle in market × channel × period |
| Quote | WM-ECO-021 | Recipient-specific pre-contract proposal, versioned, with legal-effect profile |
| Entitlement | Consumption Entitlement candidate (EM-COM-03) | Right to consume: subject, scope, period, allowance |

The landscape row carries references to all five; it never flattens them into one "offering" record. A product with no current offering appears as a product with zero in-scope offerings, not as an absent row.

# Comparison method

Comparison is **explicit, declared per landscape version, and never implicit**. Three components:

1. **Comparison basis** — the declared axis: outcome class, consumer segment, capability delivered, cost-to-serve, or strategic-fit. Stated as a code plus definition reference.
2. **Criteria set with justification** — each criterion names its metric, unit, observation window, source master and why it applies to this offering class. Criteria need not be identical across offerings; they must each be justified against the stated basis.
3. **Comparability verdict** — one of `comparable`, `comparable-with-adjustment` (adjustment stated), `not-comparable` (reason stated). Silence is not comparability.

For a commercial product the economics term is realised or contracted revenue from WM-ECO-020/WM-ECO-022 references. For an internal service the term is an **avoided-cost or capability-value estimate** with its own method, basis and uncertainty — never zero by default and never a fabricated revenue figure. Both carry the same three-part structure, so a commercial product and an internal service are compared on a common basis using different, individually justified criteria. That is exactly what the acceptance scenario demands.

# Duplicate outcomes

Duplication is detected on **intended outcome**, not on name, code or catalogue adjacency. Evidence set per candidate pair:

- Outcome signature: `service_outcome` (WM-ACT-004) or product value proposition plus target segment (EM-PRD-01), compared as declared semantics with a stated matching method.
- Consumer overlap: intersection of consumer scope / market scope / eligibility.
- Entitlement overlap: overlapping permission, scope and period in the Consumption Entitlement candidate.
- Substitution evidence: recorded cross-offering migration, or quotes (WM-ECO-021) where both appeared as alternatives.
- Contradicting evidence: distinct regulatory class, distinct jurisdiction, distinct delivery model, distinct provider accountability.

Each pair yields `outcome_overlap_claim` = {`suspected` | `substantiated` | `refuted`} with a confidence code, the evidence references and the contradicting evidence retained. Name similarity is explicitly excluded as evidence and may only trigger a review, never a claim. A `substantiated` claim is an input to a rationalisation decision made by the portfolio authority; the landscape does not retire anything.

# Economics and value

Value terms are typed, and the type is always stated: `realised-revenue`, `contracted-revenue`, `avoided-cost`, `capability-value`, `regulatory-necessity`, `strategic-option`. Each carries currency or unit, basis, period, source master and uncertainty. An internal service with zero revenue records `realised-revenue = 0` **and** a non-revenue value term; the two are separate assertions.

The negative case is rejected on the dossier's own evidence: WM-ECO-022 holds that "active, paid or renewed status never alone proves … delivery" — the converse holds equally, that absent billing proves nothing about value. Zero revenue is a fact about the pricing model, not a measurement of worth. A landscape that reports only revenue fails the stated comparison method because it omits a declared value type for an in-scope offering.

# Retirement and obligations

Retirement is a **decision recorded against the Offering**, with cascading evidence obligations and no automatic downstream mutation:

- **Active quotes** (WM-ECO-021): issued versions are immutable. Retirement triggers withdrawal or expiry per the proposal's own lifecycle, with notice to addressed recipients. Accepted-but-unordered quotes are flagged for honour-or-negotiate decision.
- **Orders** (WM-ECO-020): open lines with outstanding quantity are unaffected by offering retirement. Delivery obligations survive and close through fulfilment, short-close or claim — never through catalogue withdrawal.
- **Subscriptions** (WM-ECO-022): retirement does not cancel. Existing subscriptions continue on their bound plan version until term end, migration or cancellation, each an explicit authorised act with notice and consent evidence.
- **Contracts and obligations** (WM-ECO-006, WM-XCT-029): survival, limitation and post-termination clauses persist. WM-XCT-029's rule that discharge requires a recorded fulfilment test or explicit discharge mode applies — withdrawal of an offering is neither.
- **Entitlements** (Consumption Entitlement candidate): grant/revocation is a separate authorised act, executed by its own master.
- **Support and retention**: the support window and retention period are declared on the retirement record, with the retention basis bound to the longest applicable enforceability or statutory period.
- **Successor and migration**: successor offering reference, migration path, entitlement conversion rule and effective window. Absence of a successor is recorded explicitly as `no-successor` with a reason, not left blank.

Retirement state is `announced` → `closed-to-new` → `closed-to-change` → `withdrawn`, each dated, each leaving prior states resolvable.

# Time/scenario

Every landscape is `(scope version, scenario code, horizon interval, as-of instant)`. Horizon is a declared interval, not an open window. Scenario is a code with a definition reference; a scenario changes assumptions, never source facts. Timestamps follow the RFC 3339 convention consistent across the dossier: seconds present, explicit offset. Event time, source as-of time and landscape computation time are distinct. Recomputing a landscape at a later instant produces a new landscape version; the prior one stays retrievable, which is what makes portfolio decisions auditable after the fact.

# Scenario

Scope `S1`: market EU, horizon 2027-01-01/2027-12-31, policy `growth-with-consolidation`, scenario `base`.

- **P-A, commercial SaaS product**, offering `O-A` (EU, direct channel, subscription pricing). Criteria: realised recurring revenue (WM-ECO-022 refs), net retention, cost-to-serve. Basis: outcome class `workflow-automation`.
- **P-B, commercial device product**, offering `O-B` (EU, partner channel, one-time price plus separate service offering). Criteria: contracted revenue (WM-ECO-020 refs), unit margin, installed-base support load. Subscription criteria are **not** applied — the device offering has no recurrence class, and forcing one would breach EM-PRD-01's invariant that subscription semantics belong to pricing, never to Product.
- **S-C, internal identity-verification service** (WM-ACT-004), offering `O-C` with explicit no-charge policy. Criteria: avoided external-vendor cost (stated method, stated uncertainty), dependent-service count via typed service dependencies, outcome reliability from observation refs. `realised-revenue = 0` recorded; value type `avoided-cost` recorded alongside.

All three are compared on basis `workflow-automation` outcome contribution with `comparable-with-adjustment`: the adjustment is that O-C's value term is avoided-cost, declared and quantified, not revenue. Duplicate-outcome check on O-A and O-C returns `suspected` on partial consumer overlap, then `refuted` — O-C's consumer scope is internal-only and its provider accountability is distinct. Three offerings, three justified criteria sets, one stated basis, zero revenue treated as a pricing fact rather than a value verdict.

# Invariants

1. Offering is not Product; neither is Service, Quote or Entitlement.
2. The comparison basis, criteria and their justification are explicit; an implicit comparison is invalid.
3. Criteria may differ across offerings; each difference carries a justification.
4. Zero revenue is a pricing fact and never a value measurement; a non-revenue value type is required where revenue is zero.
5. Duplicate-outcome claims rest on outcome, consumer, entitlement and substitution evidence with confidence and contradicting evidence; name similarity is not evidence.
6. Closure records active offers, orders, subscriptions, contracts, obligations, support, retention and successor/migration, and discharges none of them by itself.
7. Portfolio membership is derived from a versioned scope, evaluated as-of a stated instant.
8. The landscape is non-authoritative: it reads masters and mutates none.
9. Every landscape states scope version, scenario, horizon and as-of instant; prior versions remain resolvable.
10. An offering without a successor records `no-successor` with a reason.

# Minimal profile shape

`OfferingPortfolioScope` (profile on Offering Catalogue): scope ref, `market_scope`, `horizon`, `portfolio_policy`, `scenario`, membership predicate set, effective interval, authority, provenance.

`OfferingLandscape` (projection profile): view key, scope version ref, as-of instant, comparison basis, per-offering row {offering ref, product/service ref, consumer segment ref, lifecycle stage, value terms with type and uncertainty, criteria set with justification, comparability verdict}, outcome-overlap claims with evidence and confidence, retirement records with obligation-survival bindings, computation provenance, declared omissions.

# Holds

Both candidate types remain identifier-unassigned; the registry supplies no target IDs and this decision creates none. The Product Catalogue and Offering Catalogue candidates from EM-PRD-01, the Consumption Entitlement candidate from EM-COM-03 and the enterprise binding profile from EM-COM-03 are all unallocated, so every dependency of this profile is itself pending. WM-ACT-004 has no specification in the dossier (`spec_availability: false`) and is a previous-version reservation under migration review — the Service Definition boundary is asserted from EM-PRD-02's prior synthesis, not from a read specification. WM-ECO-021, WM-ECO-022, WM-ECO-020, WM-ACT-029 and WM-ORG-014 are all `reviewable-draft` with `publishableCanonical: false`; three carry single-provider waivers with no independent external review. No semantic crosswalk, rights or source-mastership confirmation has been performed; no immutable refs are pinned; no fixtures have been run. The comparison-track work named in the contour — Vercy composition/whole-object, ArchiMate/ISO 42010 view rules, and participant subject-model comparison — is not done here. This is a boundary decision only: no canonical completeness and no installability is claimed.
