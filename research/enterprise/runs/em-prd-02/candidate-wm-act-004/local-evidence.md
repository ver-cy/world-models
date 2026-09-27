# EM-PRD-02 local synthesis

## Disposition

- **Complete the reserved WM-ACT-004 boundary** as Service Definition: durable service identity, expected outcome, consumer scope, accountable provider role, classifications, realization bindings and typed service-to-service dependencies.
- Reuse the identifier-unassigned Offering Catalogue candidate from EM-PRD-01 for Service Offering; the offered subject may be a product, service or bundle. Do not create a second offering model.
- Delegate recurring consumption to WM-ECO-022 Subscription where applicable and generic rights to the rights/entitlement contour. A generic Service Consumption crosswalk remains unproven and receives no identifier here.
- Reference WM-ACT-021 or WM-REC-009 for request/case records, WM-ECO-024 and act records for fulfilment, WM-SFT-016 and contract/agreement models for service-level commitments, and observation models for measured quality. These are candidate mappings, not accepted composition relations.

The legacy K4 specification correctly distinguishes standing promise from performed reality, but combines seven identities and several source masters. The completion narrows WM-ACT-004 rather than publishing that legacy aggregate unchanged. Service Offering, request, fulfilment, SLA and observation retain their own lifecycles outside the core.

Service is a provider-accountable commitment to produce a defined outcome for a consumer scope. Product is a managed result that may be offered; process is a repeatable method; an API endpoint is a technical channel or realization interface. Replacing an endpoint without changing outcome, consumer scope or provider accountability leaves Service identity unchanged.

Provider and implementation multiplicity use an effective-dated Service Realization Binding: service, provider, realization, scope, validity and authority. It references implementations and processes without copying runtime state. Service Dependency is a typed, directional, scoped relation between services and must not become a duplicate infrastructure dependency graph.

## Invariants

1. Consumer and technical API client are distinct roles.
2. Service owns expected outcome semantics; realization and process do not restate them.
3. Service contains no runtime status, endpoint state, instance count or live metric copy.
4. Offering carries eligibility, channels, hours, capacity and optional price; internal services may explicitly have no price.
5. Expected outcome, committed level and measured result remain separate facts.
6. One Service may have multiple effective providers and realizations through qualified bindings.
7. An endpoint, workflow or software component does not become a Service without outcome, consumer scope and accountable provider.
8. Service dependencies are directional, typed and validity-scoped.
9. Request, entitlement, fulfilment, SLA and observation lifecycle events never mutate Service identity automatically.
10. Retired services and superseded realization bindings remain resolvable.

## Scenario result

An HR onboarding service and a platform identity-verification service use the same Service outcome structure. Each can bind regional or outsourced providers and distinct implementations. The HR offering may be internal and explicitly unpriced; the platform offering may be usage-priced. API endpoints stay channel/interface references. A changed implementation or endpoint does not create a new Service while the promised outcome and accountability remain stable.

## Holds

WM-ACT-004 remains under migration review, but a narrowed completion candidate now defines immutable service versions, realization bindings, typed dependencies, six external relations and seven fixtures. Wildcard imports and unsupported conformance claims are excluded. The shared Offering Catalogue still requires EM-PRD-01 allocation adjudication; exact Grok comparison, one frozen semantic audit, package conversion and live verification remain required. No canonical or installability claim is made yet.
