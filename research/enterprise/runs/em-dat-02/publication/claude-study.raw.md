# EM-DAT-02 Data Product — independent review

## Verdict

**COMPLETE WM-DAT-008 as the DataProduct root; create no new DAT-domain type for either remaining candidate.**

- `DataProduct` — **COMPLETE RESERVED** WM-DAT-008. It is an independently governed offering, described by (not identical to) a catalog record.
- `DataProductOffering` — **REUSE EXTERNAL MASTER**. Market-, channel- and validity-scoped availability plus price is the EM-PRD-01 Offering candidate plane. A data product with no commercial exposure needs no offering object; consumer scope and access route on WM-DAT-008 suffice.
- `DataConsumerAgreement` — **REUSE EXTERNAL MASTER**, with an effective-dated dependent binding. Agreement, subscription, order and delivery masters are already declared external by WM-DAT-008's own `out_of_scope`; acceptance and consumer registration already exist in WM-DAT-004.

## Evidence

WM-DAT-008 is `entryKind: aggregate`, `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, produced under a single-provider waiver with Claude and Grok both timed out. Its scope statement already asserts "separate offering identity and product semantics" and its canonicalization rules already canonicalize record and offering by different namespaces. Its `boundary_notes` already exclude dataset identity, contract lifecycle and the policy/agreement/subscription/usage masters. The reserved entry therefore does not need new types — it needs its held elements made normative and its overlaps resolved.

Supporting frozen material: WM-DAT-001 explicitly cedes the offering, its consumers and its service levels to WM-DAT-008; WM-DAT-004 owns producer/consumer parties, obligations, acceptance, service levels and consumer registration; WM-SFT-003 carries `KEEP-STANDALONE: API contract has independent version, owner and consumers`; WM-DAT-007 owns purpose-qualified fitness verdicts; WM-ACT-053 owns pipeline executions. SRC-006 (ODRL 2.2) separates Offer from Agreement as policy subtypes with parties; SRC-009 (ODPS 4.1) supplies use cases, pricing, licence, contract, access, SLA; SRC-008 (DPROD) is beta.

## Identity/mastership

| Subject | Identity | Master |
|---|---|---|
| Data product | product id + owner namespace | product/offering register |
| Product version | product id + immutable version | same |
| Catalog record | record id + catalog namespace | catalog |
| Dataset / dataset version | WM-DAT-001 keys | data holder |
| Distribution | dataset version + distribution id | WM-DAT-001 |
| Interface contract revision | WM-SFT-003 contract + revision | service owner |
| Contract/schema version | WM-DAT-004 | data steward |
| Quality assessment | WM-DAT-007 | assessor |
| Pipeline run | WM-ACT-053 | orchestrator |
| Offering (market scope, price) | EM-PRD-01 Offering candidate | offering register |
| Consumer agreement | agreement/contract master | legal/commercial |
| Entitlement binding | product + resource + consumer + effective period | access authority |

Title, URL, endpoint, score, date and digest never identify a product. A published product version is immutable; changes create linked successors.

## Catalog record versus product

Accepted, per DCAT 3's record-about-resource split: one record describes one resource head, while the offering composes resources by role. Two consequences the reserved entry does not yet settle.

First, **the dual name is a defect of presentation, not of substance.** One registry row carrying two canonical identities invites collapse. Publication must state both identities on the face of the entry, with the product as aggregate root and the catalog record as the registration facet of that root.

Second, **there is an unresolved overlap.** WM-DAT-001 keeps a `catalogue-record-and-listing` finding with its own record state and harvest datestamps; WM-DAT-008 claims catalog-record identity. That is two masters for one assertion. Resolution: catalog-record mastership belongs to the catalog plane; WM-DAT-001's facet must be demoted to a reference, or WM-DAT-008 must own product records only. Unresolved in the dossier — carried as a hold.

## Dataset/distribution/interface/pipeline boundaries

Composition is by **role + resource identity + resolution policy**, never by copy.

- Dataset and dataset-version identities stay in WM-DAT-001; the product references a version or a series head and declares which.
- Distributions are manifestations of a dataset version (EM-DAT-01); the product never owns bytes, media type or checksum.
- The API is a WM-SFT-003 contract revision with its own compatibility mode and consumer pins; the product references the revision and does not increment on endpoint rebinding (EM-TEC-03).
- Pipelines (WM-DAT-005) and runs (WM-ACT-053) are referenced as evidence; the product executes nothing.
- Quality metrics/observations follow the DQV split: WM-DAT-007 owns assessment, WM-MAT-008 owns observation records, the product carries qualified summaries only.

## Offering/agreement placement

Offering is not needed inside DAT. A data product exposed in two markets at two prices is two EM-PRD-01 Offerings over one product, exactly as a SaaS tariff change creates a new price plan and revised offering without a new Product. Duplicating that here would create a second offering plane.

Agreement is likewise external. What the product plane *does* need, and currently lacks, is a **dependent entitlement binding**: consumer, product, composed resource, contract version, access route, permitted purpose, effective period, agreement reference. This is a relation, not an identity — the EndpointBinding pattern. It is what makes "different consumer terms" expressible without minting agreements in the data domain.

## Promise and evidence

A promise is a declared target; evidence is an external measurement. Product SLO targets (freshness, availability, latency, completeness) are declared per access route and per composed resource, with a stated aggregation rule. Observed values are references to WM-DAT-007 assessments and WM-MAT-008 observations, purpose-qualified and subject-version-bound. Listed, discoverable, available, authorized, delivered, accepted, fit and used remain eight distinct assertions. A green dashboard, a completed run or a catalog badge proves none of the others.

## Lifecycle

Product: `draft → reviewed → approved → published → deprecated → withdrawn → retired`, with the record lifecycle advancing independently. Withdrawal of the product never cascades to dataset, service, agreement or records masters; the description may persist when resources are unavailable, subject to privacy and records policy. Deprecation requires successor or explicit no-successor, sunset instant, and notice to entitlement holders — derivable from the binding, which is why the binding is mandatory.

## Scenario

Product **P** composes DS-A (version-pinned, currently v3), DS-B (series head), and interface **I** revision r2.

- DS-A v3→v4 rebinds a pinned member: new **P** version, DS-A identity unchanged. DS-B head advance: no P version, but the declared promise must hold across members. Neither dataset's version series collapses into P's.
- Consumer X holds a binding to DS-A v3 + I r2, research-only, no redistribution. Consumer Y holds a binding to DS-B, commercial, with redistribution. Two agreements, two entitlement bindings, one product.
- Availability is asserted separately: I r2 uptime from the service owner; DS-B freshness from the dataset plane. P's summary states the aggregation rule; it does not overwrite either.
- Delivery differs by route — distributions for datasets, operations and responses for I — and delivery events stay external.
- Fitness stays per subject version and per purpose. P carries no single fitness verdict across three resources.

## Invariants

1. Product identity survives price, market, tariff, endpoint and member-version change.
2. Catalog-record identity, product identity and every composed resource identity are separately resolvable.
3. A published product version is immutable; change yields a linked successor.
4. Every composition entry names role, resource identity and resolution policy (pinned or head).
5. The product stores no result values, bytes, distributions, runs or measurements.
6. Every access route names its interface or distribution reference and its authorization requirement.
7. Every promise names metric, target, unit, measurement point and window; a target without a measurement definition is not a promise.
8. Rebinding a pinned member creates a product version; advancing a head member does not.
9. Every consumer term is an effective-dated binding citing an external agreement.
10. Listing implies neither discoverability, availability, authorization, delivery, acceptance, fitness nor use.
11. No product version without purpose, owner, consumer scope, use cases, composition, access route, pinned contract version, measurable promise and lifecycle state.
12. Absence of any promotion-gate element means the subject is a catalogued dataset, not a product.

## Minimal completion shape

Promote from `candidate-not-normative` to required on the product version: `consumer_scope`, `service_terms`, `access_route`, `quality_target`. Make mandatory the nine gate elements above, the composition-role triple, the aggregation rule, and the entitlement binding. Register the WM-DAT-001, WM-DAT-004, WM-DAT-007, WM-SFT-003 and WM-ACT-053 edges, which are all still `candidate`.

## Holds

Single-provider waiver with no admitted external review; `publishableCanonical: false` on WM-DAT-008, WM-DAT-001, WM-DAT-004 and WM-DAT-007, so no canonical layer can rest on them. WM-DAT-001 relation unapproved. Catalog-record mastership overlap unresolved. DPROD 1.0 is beta; ODPS, DCAT-AP and Schema.org are scoped profiles. EM-PRD-01 Offering and Agreement planes are identifier-unassigned candidates. No crosswalk, fixtures or immutable refs. No canonical completeness or installability is claimed.
