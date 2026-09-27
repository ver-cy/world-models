# EM-DAT-02 local synthesis

## Disposition

- Complete reserved **WM-DAT-008** with Data Product as the aggregate root and Catalog Record as its separately identified registration facet.
- Reuse the identifier-unassigned EM-PRD-01 Offering candidate for market-, channel-, validity- and price-scoped Data Product offerings. Do not create a second DAT offering plane.
- Keep Data Consumer Agreement in the external legal/commercial or data-contract authority. Add only an effective-dated consumer-entitlement binding from product/resource/access route to the pinned agreement and purpose.
- Reuse WM-DAT-001 for datasets, versions and distributions; WM-DAT-004 for contract/schema versions and consumer obligations; WM-DAT-007 and WM-MAT-008 for assessment and observation evidence; WM-SFT-003 for logical API contracts; pipelines and runs remain external.
- Allocate no runtime or model identifier.

## Identity and mastership

Data Product has a stable owner-scoped identity and immutable published versions. Catalog Record has an independent catalog-scoped identity and lifecycle. Every composed dataset, dataset version, distribution and interface contract remains independently resolvable in its source master.

Composition records role, resource identity and resolution policy. A pinned member version change creates a new product version; advancement of a declared series head does not, although the product promise must continue to hold. Title, URL, endpoint, score, date and digest never identify the product.

The WM-DAT-001 and WM-DAT-008 catalog-record surfaces are disjoint by described-resource type and namespace: WM-DAT-001 owns records describing datasets, dataset series and distributions; WM-DAT-008 owns records describing data products and product versions. Neither model may mint a record for the other's governed resource type.

## Promotion gate

An ordinary dataset or table becomes a Data Product only when one immutable product version declares:

1. intended purpose and bounded use cases;
2. accountable owner and steward;
3. consumer scope;
4. independently identified resource composition;
5. at least one access route;
6. a pinned schema/data-contract version;
7. measurable quality or service targets with metric, unit, window and measurement point;
8. terms and authorization requirements;
9. lifecycle state, version lineage and deprecation policy.

Missing any gate element leaves the object a catalogued dataset or resource rather than a Data Product.

## Promise and evidence

Targets are promises; observations and assessments are evidence. Product summaries reference externally mastered observations and quality assessments, state their aggregation rule and remain subject-, version- and purpose-qualified. Listed, discoverable, available, authorized, delivered, accepted, fit and used are separate assertions.

Consumer terms are expressed by an effective-dated binding containing consumer, product version, composed resource, contract version, access route, permitted purpose, agreement reference and authority. The binding neither creates the agreement nor grants access by itself.

## Acceptance scenario

Product P composes dataset A at pinned version v3, dataset B by series head and API contract revision r2. Moving A to v4 creates a successor P version; advancing B's head does not change P identity or version. Consumers X and Y use different resources and purposes under separate agreements and entitlement bindings. Dataset and API delivery evidence, authorization, availability and fitness remain external and independently timed. A product summary cannot collapse these states into one badge.

## Invariants

1. Catalog Record, Data Product and every composed resource have separate resolvable identities.
2. Published product versions are immutable and successor-linked.
3. Product identity survives ordinary price, market, endpoint and member-version changes.
4. Every member declares role and pinned-versus-head resolution.
5. Rebinding a pinned member creates a product version.
6. The product stores no dataset bytes, distributions, pipeline runs, observations or assessment results.
7. Every access route identifies its interface/distribution and authorization requirement.
8. Every target identifies metric definition, unit, window and measurement point.
9. Consumer terms cite an external agreement and effective period.
10. Listing proves none of discoverability, availability, authorization, delivery, acceptance, fitness or use.
11. Withdrawal does not cascade to datasets, services, agreements or records.
12. A table or dataset without the complete promotion gate is not automatically a Data Product.

## Holds

WM-DAT-008 and its principal neighbors remain non-canonical reviewable drafts. Six reference rows are recorded but remain candidate. Offering and agreement authorities are not registry-settled; release pins and crosswalks remain incomplete. The candidate now includes seven fixtures and resolves catalog-record mastership by resource type. The existing release also carries a single-provider waiver. This checkpoint makes no canonical completeness, installability or publication claim.
