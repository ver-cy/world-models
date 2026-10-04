**Verdict.** Conditional accept of the narrowed WM-ACT-004 contour as Service Definition only. The reserved item should master durable identity, expected outcome, consumer scope, accountable provider *role type*, effective-dated realization bindings, and typed service dependencies. Do not absorb catalogue, commercial, instance, fulfilment, or observation objects. Reuse EM-PRD-01’s Offering Catalogue candidate for Service Offering. Allocate no new identifiers. This is a boundary review, not a claim of canonical completeness.

**Identity / mastership.** WM-ACT-004 is the only identity action in scope: complete the reserved definition/spec master. It does not master offerings, subscriptions, requests, fulfilments, SLAs, observations, processes, components, or endpoints. Consumer scope is an eligibility class, not a consumption occurrence. Accountable provider is a role type on the definition (e.g. Identity Verifier); the incumbent party and realizing mechanism live on effective-dated bindings. That split stops multi-provider cases from forking identity. Realization bindings and typed dependencies may have internal persistence keys; those are not public business identifiers and are not allocated here. If another contour already claims Service Definition mastership, this completion collides and must stop.

**Service / product / process / API boundary.** A service here is an outcome-named capability with consumer scope and an accountable provider role. Identity survives change of realization, channel, price, or process. It is not a SKU, workflow, deployable, contract, or metric.

- *Product* is the commercial or packageable market object. A product may bundle or meter one or more services; a service may have zero, one, or many products. Price, packaging, and catalogue presentation stay on the product/offering lineage (EM-PRD-01). Do not put commercial attributes on the definition.
- *Process* is work design that produces or supports the outcome. Many processes can realize one service; one process can support many services. Process change does not mint a new service identity unless outcome or consumer scope changes.
- *Software component* is a replaceable implementation unit. Relationship to the definition is many-to-many via realization bindings. Repo, version, or runtime identity is not service identity.
- *API endpoint* is an access surface of a realization, not the service. Endpoints may be added, versioned, retired, or swapped without changing definition identity while outcome semantics hold.

Block these collapses: HR onboarding workflow as the onboarding service; an IdP path as identity verification; a priced SKU as the definition; a new service whenever provider or stack changes.

Internal services may be explicitly unpriced. Price is an offering attribute, not a definition attribute. Unpriced does not mean undocumented, unowned, or unobserved.

**Offering and consumption.** Service Offering is catalogue presentation of one or more definitions: channel, eligibility presentation, commercial terms, optional price. One definition may have many offerings; one offering may compose several definitions. Withdrawing an offering does not retire the definition. Do not create a Service Offering identifier here.

Catalogue membership is not an invariant of WM-ACT-004. A platform/internal definition may exist with no offering row. If the service is requestable or subscribed, it must have an EM-PRD-01 offering row with explicit unpriced/internal terms. Invisibility of definition-only services is an EM-PRD-01 coverage gap, not a reason to mint a second offering master.

**Challenge — Service Consumption does not need independent identity in this PRD.** Consumption is the occurrence or entitlement state already owned by subscription/entitlement, request/case, and fulfilment/delivery. A Consumption master here would duplicate those contours and blur definition vs instance. A later “who is consuming this definition” view should be derived from those records keyed by definition + offering + party.

**Provider / realization / dependency.** One accountable role type per definition at a time, effective-dated. Multiple operational providers are realization bindings, not competing masters. Bindings point at process, component, API, platform capability, or vendor stack; they do not absorb those objects. Multiple concurrent realizations are expected. Dependencies are definition-to-definition (or definition-to-already-identified capability), typed and effective-dated (requires / composed-of / uses / substitutes). Never definition-to-endpoint. Do not freeze a dependency taxonomy here.

**Challenge — Service Dependency does not need a public business identifier in this PRD.** It needs a persistable association (source, target, type, effective interval) for history and impact. Escalate to a later contour only if change-control, assurance, or contract clauses must cite a dependency as a standalone object. The two test scenarios do not require that.

**SLA and observation.** SLA/SLO and quality observations stay on their existing candidate contours. This PRD allocates no observation identifiers. The definition may hold a reference to an existing SLA key; it must not own metrics, thresholds, or measurement streams. If those contours cannot accept a Service Definition reference, raise a join-key gap. Do not pull observation objects into WM-ACT-004.

**Invariants** (proposed, not canonical).

- Stable outcome + consumer scope ⇒ same Service Definition.
- Provider, realization, channel, or price change ⇒ binding or offering change, not new identity.
- Offering change does not retire or mint a definition.
- Unpriced ≠ unowned; definition-only ≠ unaccountable.
- Service ↛ product ↛ process ↛ component ↛ endpoint.
- Dependency target is a Service Definition or already-identified capability, not a process or API.
- No new public identifiers in this boundary.

**Scenarios.**

*HR onboarding.* One definition; shared outcome: eligible hire reaches the agreed productive / access / records state. Offerings only if exposed (new-hire vs contractor vs international). Providers: HR ops, IT, facilities, or a BPO — incumbents on bindings, not forked definitions. Realizations: Workday flow, ServiceNow flow, manual desk, regional vendor. Typed requires → identity verification, workplace access, payroll setup. The onboarding case/entitlement remains in request/case and subscription contours.

*Platform identity verification.* One definition; shared outcome: subject identity assured to a stated level for a stated consumer class. Offerings for workforce vs customer vs partner if catalogue-exposed; otherwise a valid unpriced internal definition. Providers: internal IAM and/or an external IdP. Realizations: different vendors, API stacks, in-person HR. Endpoint version and IdP tenant are realizations, not new services. HR onboarding depends on this definition by type and effective date, with no new dependency identifier.

Both scenarios fail the model if outcome semantics split by provider or stack, or if an API path is treated as the service.

**Blockers.**

- EM-PRD-01 offering schema is not visible here; cannot confirm unpriced/internal-only or multi-definition composition. If it cannot host those, reuse is incomplete — still do not mint a second offering master in this PRD.
- Identifier register is not visible; uniqueness beyond “no new IDs allocated here” cannot be asserted.
- Accountable provider role needs a role/party master already identified elsewhere; this PRD only binds.
- Realization targets (process, software, API) must already be referable; this PRD binds, it does not master them.
- If SLA/observation contours cannot reference a Service Definition, that is a join-key gap, not a licence to absorb them.
- If a later contour must cite a dependency as a contractual object, that is a separate identity decision — do not smuggle it in now.
- Ambiguous multi-provider accountability is resolved by one role type plus contributing-provider bindings; do not fork the definition.
- Collision if any existing contour already claims Service Definition mastership.

No identifiers invented. Completeness not claimed.
