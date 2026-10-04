# EM-PRD-02 local synthesis

## Disposition

- Complete reserved WM-ACT-004 as Service Definition: durable identity, immutable expected-outcome semantics, eligible consumer scope and accountable-provider role type.
- Use effective-dated owned associations for operational providers and realizations. Provider parties, processes, software, APIs, endpoints, platforms and vendor stacks remain externally mastered.
- Reuse the identifier-unassigned Offering Catalogue candidate from EM-PRD-01. It owns catalogue presentation, eligibility presentation, optional price, commercial terms and channels. One definition may have many offerings and one offering may compose several definitions.
- A non-requestable internal Service may exist without an offering row. A requestable or subscribed Service must resolve an external offering; missing catalogue coverage is a hold and never creates a second offering master.
- Delegate subscription, entitlement and consumption to WM-ECO-022 or the applicable rights/request/fulfilment masters. Service Consumption is a derived view keyed by Service, offering and party, not a root in this contour.
- Keep Service Dependency as a directional, typed, effective-dated owned association without a public business identifier. Its target is a Service definition or already-identified capability, never a process, component or API endpoint. Dependency vocabulary remains externally governed.
- Keep SLA/SLO, measurements and breach decisions external. Their authorities must support a Service-definition join key; missing join capability blocks publication and does not authorize copying data into WM-ACT-004.

Service identity survives provider, implementation, workflow, endpoint, channel, price and process changes while outcome, consumer scope and accountability remain stable. Product is a packageable/commercial subject; process is work design; component is an implementation unit; endpoint is an access surface. None substitutes for Service identity.

## Scenario result

HR onboarding retains one Service identity across EU internal and APAC outsourced providers. Platform identity verification retains one identity across internal IAM, external IdP, different API stacks and in-person verification. Providers and realizations change through bindings. A requestable variant resolves a shared offering; a non-requestable internal Service can remain definition-only. Direct dependency to an endpoint and copying SLA data into the definition are rejected.

## Reconciliation

Claude and Grok independently support the narrowed completion and no-new-identifier decision. Grok sharpened offering optionality, composed offerings, one effective provider role type, consumption as a derived view, dependency as a non-public association, and join-key holds. The reconciled candidate contains 38 constraints, six external relations and 28 fixtures.

## Holds

The shared Offering Catalogue remains unallocated; role/party and realization masters require confirmed references; dependency vocabulary has no approved authority; SLA/observation join keys and registry collision checks remain unverified. External standards are not conformance claims. Package conversion and live HTTP/runtime/search/package verification remain pending. No canonical or installability claim is made.
