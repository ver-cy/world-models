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