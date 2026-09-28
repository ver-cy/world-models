# Frozen no-tools semantic audit — EM-PRD-02

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

The result completes reserved WM-ACT-004 as a narrowed Service Definition. No new runtime/model identifier is proposed. Service Realization Binding and Service Dependency are owned associations with tuple identity and optional internal persistence keys, not public enterprise roots.

Reconciled boundary:
1. Service identity is the stable expected outcome, eligible consumer scope and accountable-provider role type.
2. One accountable-provider role type applies at an effective time. Provider parties and realizing mechanisms are external masters joined through effective-dated bindings.
3. Provider, implementation, workflow, endpoint, channel, price or process changes do not mint a Service while outcome, consumer scope and accountability remain stable.
4. Product, process, software component, API, endpoint, deployment and Service are distinct masters.
5. Service Offering is reused from the unallocated EM-PRD-01 Offering Catalogue candidate. It owns catalogue presentation, commercial terms, optional price, channels and eligibility presentation.
6. One definition may have many offerings and one offering may compose several definitions. Offering withdrawal never retires or mints a Service.
7. Catalogue membership is not a Service identity invariant. A non-requestable internal Service may have no offering; a requestable or subscribed Service must resolve an external offering row.
8. Service Consumption is derived from entitlement, request and fulfilment records keyed by Service, offering and party. No consumption root is created here.
9. Realization Binding pins one immutable definition version and records external provider and realization targets, kind, scope, validity and authority. It owns no provider, process, component, API or endpoint identity.
10. Service Dependency is a directional, typed, scoped, effective-dated owned association. It has no public business identifier. It targets a Service definition or already-identified capability, never a process, component or API endpoint.
11. Dependency types are illustrative until an external vocabulary authority is approved.
12. Expected outcome, committed level and observed result remain separate. SLA/SLO and observation authorities must reference Service by join key; missing join capability is a publication hold.
13. Request, entitlement, fulfilment, SLA and observation events never mutate Service identity automatically.
14. Retired Services and superseded bindings remain resolvable. Access to references is no broader than access to linked consumer, provider, realization, agreement and evidence records.
15. No new public model, runtime, binding, dependency or consumption identifier is allocated.

Scenarios: HR onboarding keeps one identity across EU internal and APAC outsourced providers. Platform identity verification keeps one identity across internal IAM, external IdP, API versions and in-person realization. An internal non-requestable Service may be explicitly accountable without an offering. A requestable Service without an offering is held. A dependency to an API endpoint is rejected. SLA data without a Service join key is not copied into WM-ACT-004.

Audit questions:
- Is there a hidden aggregate or identifier despite `newRuntimeId=false`?
- Are definition, offering, binding, dependency, consumption and external-master boundaries unambiguous?
- Do multi-provider, unpriced internal, requestable and composed-offering cases preserve identity correctly?
- Are SLA/observation, dependency-target and access semantics safe?
- Identify any contradiction that makes even a held completion candidate unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the candidate.
