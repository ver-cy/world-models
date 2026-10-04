# Frozen audit request: EM-DAT-02

Independently review only the frozen materials below. No tools or browsing. Return Verdict (ACCEPT / ACCEPT WITH LIMITS / REVISE / REJECT), blocking findings, non-blocking findings, invariant/fixture gaps and exact minimal remediations. Challenge identity, Catalog Record/Product coexistence, entitlement-object containment, external offering/agreement/authorization mastership, version triggers and lifecycle independence. Do not invent identifiers or claim publication readiness.

## Candidate
```json
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-DAT-02",
  "modelId": "WM-DAT-008",
  "registryId": "vr.wm-dat-008",
  "name": "Data Product with Catalog Record facet",
  "version": "0.3.1-candidate.2",
  "entryKind": "aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent a governed data product and immutable product versions, with a separately identified catalog record describing each product head or version, without absorbing dataset, distribution, interface, execution, observation, assessment, offering or agreement lifecycles.",
  "boundary": {
    "owns": [
      "stable data-product identity",
      "immutable published product versions and successor lineage",
      "product purpose, consumer scope and bounded use cases",
      "non-owning resource composition by role and resolution policy",
      "access-route declarations and pinned contract references",
      "measurable product promises and declared aggregation rules",
      "product-scoped catalog-record identity and lifecycle",
      "identified effective-dated consumer-entitlement binding objects that reference external terms and access authority"
    ],
    "delegates": [
      "dataset, dataset-version and distribution identity to WM-DAT-001",
      "schema and data-contract versions to WM-DAT-004",
      "quality assessments to WM-DAT-007",
      "observations and measurements to WM-MAT-008",
      "API and interface-contract revisions to WM-SFT-003",
      "pipeline and processing-run execution to WM-ACT-053",
      "market, channel, price and validity offering semantics to the shared Offering authority",
      "legal or commercial agreement lifecycle to the applicable agreement authority"
    ],
    "excludes": [
      "dataset bytes and storage",
      "distribution custody and fixity",
      "pipeline execution or retry state",
      "observation values and assessment verdicts",
      "authorization evaluation and credential material",
      "price, tariff, market and sales-channel lifecycle",
      "agreement, order, subscription, delivery or payment lifecycle"
    ]
  },
  "identities": {
    "product": [
      "productId",
      "ownerNamespace"
    ],
    "productVersion": [
      "productId",
      "productVersionId",
      "version"
    ],
    "productCatalogRecord": [
      "catalogId",
      "catalogRecordId"
    ],
    "memberResource": "external identity only",
    "consumerEntitlementBinding": [
      "entitlementBindingId"
    ]
  },
  "catalogRecordBoundary": {
    "rule": "WM-DAT-008 owns catalog records only when the described resource is a data product or data-product version. WM-DAT-001 owns catalog records whose described resource is a dataset, dataset series or distribution. Record namespaces and described-resource types must make the two masters disjoint.",
    "recordLifecycle": [
      "draft",
      "listed",
      "hidden",
      "withdrawn",
      "tombstoned"
    ],
    "coexistenceRule": "Catalog Record and Data Product may share a publication facade only as separately identified members with independent mastership and lifecycle; one product may have many records and a record may predate completion or survive withdrawal."
  },
  "productVersion": {
    "required": [
      "purpose",
      "accountableOwnerRef",
      "stewardRef",
      "consumerScope",
      "boundedUseCases",
      "resourceComposition",
      "accessRoutes",
      "dataContractRefs",
      "qualityOrServiceTargets",
      "termsAndAuthorizationRefs",
      "lifecycleState",
      "deprecationPolicy",
      "measurablePromiseDefinitions",
      "versionTriggerPolicy"
    ],
    "lifecycle": [
      "draft",
      "reviewed",
      "approved",
      "published",
      "deprecated",
      "withdrawn",
      "retired"
    ]
  },
  "resourceComposition": {
    "requiredPerMember": [
      "role",
      "resourceRef",
      "resourceType",
      "resolutionPolicy"
    ],
    "resolutionPolicies": [
      "pinned-version",
      "declared-series-head"
    ],
    "versionRule": "Rebinding a pinned member creates a successor product version. Advancement of a declared series head does not change product-version identity, but every declared promise must remain satisfied."
  },
  "consumerEntitlementBinding": {
    "classification": "identified dependent governed object inside the Data Product aggregate; not a bare relation, independent aggregate, agreement, authorization grant or new model identity",
    "required": [
      "entitlementBindingId",
      "consumerRef",
      "productVersionId",
      "resourceRef",
      "contractVersionRef",
      "accessRouteRef",
      "permittedPurpose",
      "effectiveFrom",
      "agreementRef",
      "authorityRef",
      "approvalRef",
      "status",
      "recordedAt"
    ],
    "optional": [
      "effectiveTo",
      "revocationRef",
      "constraints",
      "suspendedAt",
      "expiredAt",
      "auditRefs"
    ],
    "effect": "Records the governed consumer-product-version-resource-purpose terms association; it neither creates external terms nor grants access.",
    "lifecycle": [
      "proposed",
      "approved",
      "active",
      "suspended",
      "expired",
      "revoked"
    ],
    "identityRule": "Identity is stable across status changes; external agreement and product-version references remain independently versioned."
  },
  "relations": [
    {
      "target": "WM-DAT-001",
      "relation": "REFERENCE",
      "purpose": "Resolve datasets, versions, series and distributions without importing their lifecycle.",
      "required": true
    },
    {
      "target": "WM-DAT-004",
      "relation": "REFERENCE",
      "purpose": "Pin schema and data-contract versions and consumer obligations.",
      "required": true
    },
    {
      "target": "WM-DAT-007",
      "relation": "REFERENCE",
      "purpose": "Resolve purpose-qualified quality assessments without copying verdict state.",
      "required": false
    },
    {
      "target": "WM-MAT-008",
      "relation": "REFERENCE",
      "purpose": "Resolve external measurements supporting product promises.",
      "required": false
    },
    {
      "target": "WM-SFT-003",
      "relation": "REFERENCE",
      "purpose": "Pin API or interface-contract revisions for access routes.",
      "required": false
    },
    {
      "target": "WM-ACT-053",
      "relation": "REFERENCE",
      "purpose": "Resolve execution evidence without importing run state.",
      "required": false
    }
  ],
  "operations": [
    {
      "id": "register-product",
      "effect": "Mint a stable product identity and draft version only after the promotion gate is complete.",
      "authority": "data-product owner or delegated steward"
    },
    {
      "id": "publish-product-version",
      "effect": "Freeze the product version, composition, contract pins, promises and deprecation policy.",
      "authority": "data-product approval authority"
    },
    {
      "id": "register-product-catalog-record",
      "effect": "Create or revise the independently identified record describing a product or product version.",
      "authority": "catalog operator"
    },
    {
      "id": "bind-consumer-entitlement",
      "effect": "Record an effective-dated relation to external agreement and access authority.",
      "authority": "access or agreement authority"
    },
    {
      "id": "deprecate-or-withdraw-product",
      "effect": "Advance product lifecycle and notify binding holders without cascading changes to resources or agreements.",
      "authority": "data-product owner"
    }
  ],
  "invariants": [
    "Catalog record, data product and every composed resource have separate resolvable identities.",
    "A product catalog record describes only a product or product version; dataset catalog records remain WM-DAT-001-owned.",
    "Published product versions are immutable and successor-linked.",
    "Every member declares role, resource identity, resource type and pinned-versus-head resolution policy.",
    "Rebinding a pinned member creates a successor product version.",
    "Advancing a declared series head does not change product-version identity.",
    "The product stores no dataset bytes, distributions, pipeline runs, observations or assessment results.",
    "Every access route identifies its interface or distribution and authorization requirement.",
    "Every promise identifies metric definition, target, unit, window, measurement point and aggregation rule.",
    "Consumer terms cite an external agreement, authority and effective period.",
    "A consumer-entitlement binding neither creates an agreement nor grants access by itself.",
    "Listing, discoverability, availability, authorization, delivery, acceptance, fitness and use are independent assertions.",
    "Withdrawal does not cascade to datasets, services, agreements or records.",
    "A dataset missing any promotion-gate element is not a Data Product.",
    "One product may have many Catalog Records, and delisting or hiding one record never retires the product.",
    "Catalog Record and Data Product may share only a publication facade; fields and lifecycle transitions never overwrite across identities.",
    "Consumer-entitlement binding has its own identity, approval, status history, effective interval and audit references.",
    "Consumer-entitlement binding is neither the external agreement nor an authorization grant and cannot grant access by itself.",
    "Distinct consumers may hold distinct bindings to the same product version under different external terms.",
    "Catalog-record, product-version and entitlement-binding intervals advance independently.",
    "Pipeline runs and quality observations never create product versions.",
    "Historical Catalog Records and expired bindings remain addressable after product withdrawal."
  ],
  "holds": [
    "Offering and agreement authorities remain identifier-unassigned and are referenced descriptively, never locally mastered.",
    "Metric-definition authority remains pending EM-DAT-05.",
    "Candidate relation rows confer no mutation or cascade authority.",
    "External standards and product projections are alignment mappings, not conformance claims.",
    "Grok accepted the boundary with an identified dependent entitlement object; final frozen audit remains to be reconciled.",
    "Catalog Record/Data Product coexistence requires registry-facing dual-identity presentation and must not become a merged type."
  ],
  "offeringAgreementPlacement": {
    "offering": "external commercial master; effective-dated binding only",
    "consumerAgreement": "external legal/commercial master; effective-dated binding only",
    "rule": "No price, SKU or legal text is copied into WM-DAT-008."
  },
  "versionTriggers": {
    "createsSuccessorProductVersion": [
      "pinned member rebinding",
      "pinned interface-contract revision change",
      "declared purpose or consumer-scope change",
      "quality or SLO promise change"
    ],
    "doesNotCreateProductVersion": [
      "advance of a declared-series-head member while the pin policy is unchanged",
      "catalog-record status change",
      "entitlement-binding status change",
      "pipeline run",
      "quality observation"
    ]
  }
}
```

## Fixtures
```json
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-DAT-008",
  "version": "0.3.1-candidate.2",
  "cases": [
    {
      "id": "promotion-gate-failure",
      "kind": "negative",
      "input": "A table has a title and owner but no consumer scope, access route, pinned contract or measurable promise.",
      "expect": "It remains a catalogued dataset and cannot be registered as a Data Product.",
      "expectRule": "INV-001"
    },
    {
      "id": "pinned-member-change",
      "kind": "negative",
      "input": "Product P pins dataset A v3; the owner proposes rebinding A to v4.",
      "expect": "A successor product version is required while dataset identity remains unchanged.",
      "expectRule": "INV-002"
    },
    {
      "id": "series-head-advance",
      "kind": "positive",
      "input": "Product P references dataset B by declared series head and B advances.",
      "expect": "P keeps its product-version identity, but all declared promises must still hold for the new head.",
      "expectRule": "INV-003"
    },
    {
      "id": "two-consumers-two-terms",
      "kind": "positive",
      "input": "Consumers X and Y use different resources and purposes under different agreements.",
      "expect": "Two effective-dated entitlement bindings reference external agreements; no agreement is minted in WM-DAT-008.",
      "expectRule": "INV-004"
    },
    {
      "id": "catalog-record-separation",
      "kind": "positive",
      "input": "The same dataset and the product wrapping it are listed in one catalog.",
      "expect": "WM-DAT-001 owns the dataset record; WM-DAT-008 owns the product record; distinct identifiers and described-resource types prevent collision.",
      "expectRule": "INV-005"
    },
    {
      "id": "availability-is-not-fitness",
      "kind": "negative",
      "input": "The API route is available but the latest dataset fails a purpose-qualified quality assessment.",
      "expect": "Availability and fitness remain separate; the product does not display a single inferred green status.",
      "expectRule": "INV-006"
    },
    {
      "id": "withdrawal-no-cascade",
      "kind": "positive",
      "input": "Product P is withdrawn while consumers retain recordkeeping duties and datasets remain valid.",
      "expect": "P lifecycle advances and holders are notified; dataset, agreement and record lifecycles do not cascade.",
      "expectRule": "INV-007"
    },
    {
      "id": "two-catalog-records",
      "kind": "positive",
      "input": "Product P is listed in C1 and C2; C2 delists it.",
      "expect": "P and C1 record survive; only C2 record changes state",
      "expectRule": "INV-015"
    },
    {
      "id": "record-product-field-overwrite",
      "kind": "negative",
      "input": "A catalog withdrawnAt update overwrites product withdrawnAt.",
      "expect": "Reject cross-identity field overwrite",
      "expectRule": "INV-016"
    },
    {
      "id": "binding-bare-relation",
      "kind": "negative",
      "input": "Consumer terms are placed on an unversioned product-consumer edge.",
      "expect": "Reject; create an identified governed dependent binding object",
      "expectRule": "INV-017"
    },
    {
      "id": "binding-not-grant",
      "kind": "negative",
      "input": "An approved entitlement binding is treated as sufficient IAM authorization.",
      "expect": "Reject access; resolve the external authorization decision",
      "expectRule": "INV-018"
    },
    {
      "id": "two-consumers-same-version",
      "kind": "positive",
      "input": "X and Y bind to P v5 under different external terms.",
      "expect": "Retain two binding identities and one product-version identity",
      "expectRule": "INV-019"
    },
    {
      "id": "binding-suspension-no-product-change",
      "kind": "positive",
      "input": "Y binding is suspended while X remains active.",
      "expect": "No product, catalog or X-binding lifecycle changes",
      "expectRule": "INV-020"
    },
    {
      "id": "quality-run-no-version",
      "kind": "negative",
      "input": "A failed pipeline run or quality observation proposes a new product version.",
      "expect": "Reject version creation; retain external evidence",
      "expectRule": "INV-021"
    },
    {
      "id": "withdraw-history",
      "kind": "positive",
      "input": "Product is withdrawn with an expired binding and prior catalog record.",
      "expect": "All historical record and binding identities remain addressable",
      "expectRule": "INV-022"
    },
    {
      "id": "offering-inline-price",
      "kind": "negative",
      "input": "A price and SKU are copied into the product version.",
      "expect": "Reject copied commercial master data",
      "expectRule": "INV-007"
    },
    {
      "id": "floating-api-contract",
      "kind": "negative",
      "input": "An API route lacks a pinned interface-contract revision.",
      "expect": "Reject product publication",
      "expectRule": "INV-002"
    }
  ]
}
```

## Claude study
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


## Grok study
**Verdict.** Accept the proposed disposition. Data Product completes reserved WM-DAT-008 as the governed composition-and-promise root. Catalog Record remains a separately identified registration facet. DataProductOffering and DataConsumerAgreement stay in external commercial/legal masters; WM-DAT-008 owns only effective-dated bindings. Catalog Record and Data Product may share a publication aggregate only as a facade of two identities; they must not merge into one type or one lifecycle. Consumer-entitlement binding is an independently governed object, not a relation attribute.



**Strongest supporting evidence.** Catalog-entry metadata (who listed it, when, in which catalog, listing status) is not product-promise metadata (purpose, owner, pin-set, contract, SLO). That split is why a catalog record exists as its own object: listing issued/modified/status can differ from the described resource, and different resource types keep different lifecycles. A table is inventory until purpose, accountable owner, consumer scope, use cases, resource composition, access route, pinned contract, measurable quality/SLO, and lifecycle are declared; product literature treats that package—not the raw asset—as the unit of value. Commercial instruments (price plan/SKU, MSA/DPA/consumer agreement) have distinct mastership; a catalog binds to them and does not own them.



**Strongest counterexample.** Product P pins Dataset D1 v3 (series head now v4), Dataset D2 v1, and API contract I1 v2. Consumer X holds a research-free binding; Consumer Y holds a paid-SLA binding. Collapse failures: D1’s series-head advance silently mutates P’s promise; changing Y’s price or suspending Y delists P or revokes X; delisting P from catalog C2 retires P or unpublishes C1’s record; a pipeline-run quality observation is treated as product fitness or listing availability.



**Identity / mastership**



| Object | Master | Owns identity & lifecycle | WM-DAT-008 holds |

|---|---|---|---|

| Catalog Record | catalog/registry | listing, discoverability, catalog-local status | the record + pointer to product/resource |

| Data Product | product owner via WM-DAT-008 | purpose, owner, scope, pin-set, SLO, product version | root |

| Dataset / DatasetVersion | data resource master | independent version chain / series head | pinned member refs |

| Distribution | distribution master | manifestation | access-route refs |

| API / Interface Contract | contract master | interface pin | pinned contract ref |

| Pipeline / run | ops/orchestration | execution instance | optional lineage refs |

| Quality assessment / observation | quality system | measured result | optional fitness-evidence refs |

| Authorization | IAM/policy | grant/deny | not the grant |

| Legal/commercial agreement | legal/commercial masters | Offering, Consumer Agreement | effective-dated bindings only |

| Entitlement binding | product context; terms from external masters | own id, approval, interval, consumer, terms-ref, product-version-ref | the binding object |



**Offering / agreement placement.** Do not complete DataProductOffering or DataConsumerAgreement inside WM-DAT-008. Keep market/price Offering and Consumer Agreement in their external masters. WM-DAT-008 stores only effective-dated bindings: product or product-version → offering-ref and/or agreement-ref, plus scope and validity interval. Inlining price, legal text, or SKU into the catalog slot mixes market, legal, and registry lifecycles.



**Versioning rules.** A Data Product version is created by a change to the pinned member set, a pinned interface contract, declared purpose/scope, or the SLO promise. A declared series-head advance of an independently versioned dataset does not create a product version unless that series head is the pinned member and the pin moves. Catalog Record version/status is listing provenance. Binding version/status is entitlement lifecycle. Pipeline runs and quality observations never version the product.



**Scenario result.** P remains one product identity. D1 and D2 keep independent version chains; P stays pinned to D1 v3 and D2 v1 while D1’s series head advances to v4. I1 v2 remains the pinned API. Two entitlement-binding objects attach X (research-free) and Y (paid-SLA) to the same product version and to different external term masters. Catalog Records may differ per catalog. Listing, discoverability, availability, authorization, delivery, acceptance, fitness, and use stay distinct predicates.



**Invariants**

1. Catalog Record ≠ Data Product ≠ Dataset ≠ DatasetVersion ≠ Distribution ≠ API/Interface Contract ≠ pipeline/run ≠ quality observation ≠ authorization grant ≠ legal/commercial agreement ≠ entitlement binding.

2. A table is not a product until purpose, accountable owner, consumer scope, use cases, composition, access route, pinned contract, measurable SLO, and lifecycle are declared.

3. One product may pin many independently versioned members; member version ≠ product version.

4. Series-head advance without pin move does not version the product.

5. Pin-set or pinned-contract change does version the product.

6. One product may have many Catalog Records; delist ≠ retire.

7. Offering and Consumer Agreement are not owned by WM-DAT-008.

8. Entitlement binding is a governed object, not an attribute of Product or Record.

9. Distinct consumers may hold distinct bindings on the same product version.

10. Authorization grant ≠ entitlement binding ≠ listing ≠ delivery.

11. Quality observation ≠ SLO promise; evidence may support fitness but does not replace the promise.

12. Pipeline/run identity is operational and is not product or catalog identity.

13. Binding effective interval is independent of product-version interval and listing interval.

14. Listing, discoverability, availability, authorization, delivery, acceptance, fitness, and use are distinct predicates.

15. Historical Catalog Record and expired binding remain addressable after product withdrawal.



**Minimum completion shape.** Stable product identity and product version; purpose; accountable owner; consumer scope; use cases; declared member composition with pins (not floating series heads); access route; pinned interface/API contract; measurable quality/SLO promise; lifecycle state; at least one Catalog Record pointing at the product; at least one effective-dated terms binding (including internal-use / no-fee); explicit non-identity of dataset versions, pipeline runs, quality observations, and authz grants.



**Publication blockers.** Catalog Record missing or folded into product fields; Offering or Consumer Agreement inlined; entitlement modeled only as a relation/attribute; unpinned members; SLO not measurable or not owned; ordinary table treated as the product; pipeline run or quality observation used as product version; one merged type sharing a single lifecycle across record and product; any claim of external-standard conformance.



**Coexistence decision.** Catalog Record and Data Product can safely coexist in one publication aggregate only as a facade that holds two members with distinct identifiers, states, and mastership. They cannot safely coexist as one type. A record’s primary topic may be a Data Product (or a Dataset, Distribution, or API). One product may have many records; a record may exist before the product is complete or after it is withdrawn. Shared fields such as issued/listed/withdrawn must not overwrite purpose, owner, pin-set, or SLO.



**Entitlement decision.** The consumer-entitlement binding is an independently governed object (own identity, approval, suspension, effective interval, audit), not a bare relation. A relation cannot carry per-consumer terms, outlive a product version, or support the dual-term test without becoming an object. It is not the Agreement master; it points at the external agreement, the product version, and the consumer. No new reserved identifier is minted.