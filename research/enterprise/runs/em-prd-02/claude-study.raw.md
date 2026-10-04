# Independent review — EM-PRD-02 *Service and Service Model* vs reserved WM-ACT-004 *Service*

## Verdict

**Complete the reservation as a narrowed core, and split.** Keep `WM-ACT-004` as the durable **Service** model: definition, expected outcome, provider/realization binding, and service-to-service dependency. Move the rest of the current K4 body out: **Service Offering**, **Service Consumption (entitlement)**, **Delivery Episode**, **Service Level Commitment**, **Quality Observation**, and **Request/Case** each pass an independence test on identity, lifecycle and mastership, and three of them are explicitly delegated by the contour scope. EM-PRD-02 then consumes a **profile** of the narrowed core plus references to the peers — it does not need its own type set. Peers are proposed name-only; no identifiers are assigned here.

## Evidence

The dossier supports a boundary decision but not a mapping claim. `mapping_status: conceptual-candidate` with `evidence_depth: index-and-publication-metadata`, `review_state: migration-boundary-review`, `status: described-previous-version`, and the stated limit that the spec "predates current research assurance" together mean the K4 text is input, not baseline. `relations: []` — no inbound dependencies are recorded, so restructuring K4 breaks nothing that the dossier can see. `factor_overlap: 0.09` is low, but K4's own Composition section references O1/H1/K1/K2/K3, and the contour lists EM-PRD-01 and three TEC contours as related — the real overlap risk is with product offering and with technical components, and it is not measurable from what is supplied. All four `candidate_properties_from_v1` fields (`service_outcome`, `consumer_scope`, `service_hours`, `support_model`) are free text and `candidate-not-normative`; `service_hours` and `support_model` are offering/commitment attributes misfiled onto the service. K4's manifest imports cpsv-ap, schema-org and itil at version `"*"` — unpinned, which collides with the blocking decision "choose immutable refs."

## Identity and mastership

| Concept | Identity criterion | Lifecycle | Plausible master |
|---|---|---|---|
| Service | outcome semantics + accountable provider role + consumer scope | defined → catalogued → superseded/retired | product catalogue, PLM |
| Service Offering | service × terms × validity window × audience/market | published → amended → withdrawn | catalogue/pricing, contract |
| Service Consumption | party × offering × entitlement period | granted → suspended → terminated | CRM, entitlement/billing |
| Request/Case | one demand event | submitted → closed | ITSM/case system |
| Delivery Episode | one fulfilment of one request | started → completed | operations/runtime |
| Service Level Commitment | agreement × metric × window | agreed → revised → expired | contract management |
| Quality Observation | metric × episode/window × method | recorded (immutable) | monitoring/analytics |

Seven distinct identity criteria, seven lifecycles, at least five distinct masters. That is sufficient to reject a single model, and sufficient to reject treating any of these as mere attributes of Service. It is *not* sufficient to justify seven separate contours in this wave — grouping is a packaging decision left open below.

## Service vs product/process/API

A **service** is a standing commitment to produce a named outcome for a defined consumer, borne by an accountable provider. A **product** (EM-PRD-01) is the commercial thing offered; a service may be productized, and a product may be realized by services, but neither contains the other. A **process** (K3) is the arrangement of internal work; it has no consumer-facing promise and no consumer scope, and the same service may be delivered by different processes. An **API endpoint** is a channel — K4 already models `channel` with `location or endpoint`, and that is where an endpoint belongs.

The negative case has a decisive test: **substitution**. If the endpoint is renamed, versioned or replaced and the promised outcome, consumer scope and provider accountability survive unchanged, the service is the invariant and the endpoint was never the service. An endpoint qualifies as a business service only when it independently carries outcome semantics, a consumer scope, and a provider accountable for the outcome rather than for uptime of that one interface.

## Offering and consumption

The offering is where price lives, and price must be optional. An internal service with no price is expressed as an offering whose fee basis is `none` or `internal-chargeback` — never by omitting the offering, because eligibility, channels, hours and capacity limits are still needed and are offering-level, not service-level. `service_hours` and `support_model` therefore move to offering/commitment.

**Consumption is a standing relationship, not an event.** An entitlement (party × offering × period × limits) persists between requests and can exist with zero requests; a request is an episodic event raised *against* an entitlement. K4 collapses this by routing `serviceRequest -> requests -> offer` directly, which cannot express a subscribed consumer with no open requests, nor a request made outside entitlement. Requests reference the entitlement; the entitlement references the offering.

## Provider/realization/dependency

Do not model provider or realization as a direct many-to-many from Service. Introduce an explicit **service realization binding** object: service × provider × realization × scope (region, tier, channel) × validity. This is what lets one service have several providers and implementations while outcome semantics are declared exactly once on the Service. Realizations conform to the service's outcome specification; they do not restate it. K4's `service -> providedBy -> organization (many-to-one)` is wrong for the acceptance scenario and must be replaced.

**Service Dependency** is service-to-service, directional, typed (`requires`, `optional`, `degrades-to`), and scoped to a version or offering. It is not component or infrastructure dependency — that belongs to the TEC contours and must not be imported here, or the model becomes a second discovery graph.

## SLA and observation boundary

Three separate things: **expected outcome** (on Service — what the service is *for*), **committed level** (on offering or agreement — the promised metric and target), **observed value** (on an episode or window — what was measured). K4 keeps `qualityCommitment` under `offering` and `qualityObservation` under `delivery`, which is directionally right, but the contour delegates SLAs, so EM-PRD-02 should reference a commitment by identifier and model neither the commitment's terms nor the observation series. Breach determination is a function of commitment + observation and belongs with the SLA owner, not with the service catalogue.

## Invariants

1. Consumer ≠ technical API client. A consumer is a party with an entitlement; an API client is a credentialed technical identity acting on some party's behalf, possibly many-to-one or one-to-many.
2. Service carries no runtime state copy — no current status, no instance count, no live metric value.
3. Expected outcome and measured value are distinct objects and never share a field.
4. Outcome semantics are declared once on the Service; realizations conform and may not redefine them.
5. Price is optional; offering existence is not.
6. Entitlement may exist with zero requests; a request references an entitlement, not an offering directly.
7. A channel or endpoint never carries service identity.
8. Dependency edges are service-to-service only.

## Scenarios

**HR onboarding.** Service: "new hire ready to work on day one," consumer scope = hiring managers, internal. Offering: zero-price internal, eligibility = confirmed requisition, hours = business hours. Realizations: in-house HR shared service (EU) and an outsourced provider (APAC) — same outcome specification, different bindings. Dependency: requires identity provisioning service.

**Platform identity verification.** Same shape: one outcome ("identity verified to assurance level X"), two realizations (in-house engine, external bureau), priced offering with per-call fee, endpoints modelled as channels. Both scenarios express result identically through the Service outcome specification — which is the acceptance criterion.

## Minimal completion shape

Core `WM-ACT-004`: `service` (name, purpose, outcome specification, consumer scope, classification, accountable provider role), `serviceRealizationBinding`, `serviceDependency`, `channel` (reference or local). Events: defined, realization bound/unbound, superseded, retired. Peers (identifier-unassigned, names only): Service Offering; Service Consumption/Entitlement; Service Request/Case; Delivery Episode; Service Level Commitment; Quality Observation.

## Holds

Unresolved from this dossier: overlap and possible reuse of a single offering construct with EM-PRD-01; where Request/Case routes (EM-TEC-04/05/06 contents unknown); whether CPSV-AP, schema.org and ITIL alignments are licensable and at which pinned versions; and fixture verification. None are claimed complete, canonical or installable here.
