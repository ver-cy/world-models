# EM-LND-17 — Asset and Place Landscape: independent review

## Verdict

**Reuse, do not mint new physical types.** EM-LND-17 is a composed landscape over the existing spatial spine. `AssetPlaceLandscape` earns **independent identity as a governed landscape object only** — a scoped, as-of-dated, owned composition that masters *nothing* about places or assets and delegates every substantive fact. `OccupancyView` earns **no independent identity**: it is a governed projection (an ISO 42010 view) defined inside the landscape, computed from placement, use designation and capacity. Two relation types the dossier does not supply — **asset placement episode** and **operational responsibility assignment** — need first-class identity; their registry identifiers are **unassigned** and must follow registry process. Negative case rejected (below). Decision is `reuse + extend`, boundary `accepted-with-holds`.

## Evidence

Frozen dossier only. Both targets are `status: candidate`, `evidence_depth: index-and-publication-metadata`, `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`; both carry unresolved publication holds. Load-bearing facts:

- **WM-BLT-006** out-of-scope: land tenure (→ WM-BLT-008), building fabric (→ WM-BLT-001), room geometry (→ Space), component equipment records, address normalisation, **work-order execution**. Its composition to WM-BLT-008 is `required: false` (IFC permits a facility with no site). Its human-occupancy/privacy checklist entry is an explicit **gap**.
- **WM-BLT-008** policy: containment is "an authored, evidenced decision … never inferred from geometry alone"; "a reporting boundary may never redefine the managed extent"; legal/commercial constructs are referenced, never re-modelled.
- **WM-OBJ-001** already masters: location fix (read point vs business location, precision, source), containment context, **custody periods and transfer**, exceptional states (missing/stolen/seized), and references title to the ownership model. `WM-OBJ-022 VIEW WM-OBJ-001` — "no second master identity".
- **WM-XCT-010** is `entry_kind: mixin`; it owns the address record and the binding act, explicitly *not* the object addressed; it records that postal addresses "may bear no definite relation to the recipient's location" and requires role, basis, purpose and exclusivity on every binding.
- **WM-ACT-007**: an order authorizes; it never proves work occurred.
- **EM-FAC-01** precedent: composed landscape, `office` as effective-dated designation, allocation identifier deliberately unassigned.

## Identity/mastership

Six identities stay separate, each with its own master:

| Identity | Master | Never identified by |
|---|---|---|
| Gazetteer place | WM-PLC-010 | coordinates, address |
| Site / campus | WM-BLT-008 | parcel, settlement, reporting boundary |
| Facility | WM-BLT-006 | its site, its single building, an FRS-style regulatory site |
| Building / structure | WM-BLT-001 | address, owner, geometry hash |
| Interior space | WM-BLT-002 (**reserved, previous-version — must be completed**) | room number, current occupier, use designation |
| Movable asset | WM-OBJ-001 | location, holder, work order |

Address (WM-XCT-010) is a mixin value-and-binding, never an identity for any row above. `AssetPlaceLandscape` mints its own identifier for the *view*: scope, as-of, owner, publication state, disclosure class. `OccupancyView` is a named projection definition within it, not a record.

## Spatial spine

`WM-PLC-002 → WM-BLT-008 → WM-BLT-006 → WM-BLT-001 → WM-BLT-002 (recursive) → WM-OBJ-001`, with WM-PLC-005 containing sites and WM-PLC-010 supplying named-place reference. Edges are **evidenced assertions with validity, not geometric derivations**. Site→facility containment is conditional, non-exclusive and may be absent; campuses may be non-contiguous; a facility spanning multiple sites is recorded as a boundary note (deferred in WM-BLT-006, unresolved). Assets may hang off any level, including a site with no building.

## Asset placement and responsibility

Seven independent effective-dated relations; collapsing any two is a defect.

1. **Placement episode** *(new, identifier unassigned)* — asset ↔ spatial locus at declared granularity, with `mode ∈ {planned, observed}`, period, asserting party, basis, confidence.
2. **Custody** — reuse WM-OBJ-001 custody periods (holder, basis, transfer, acknowledgement). Do not duplicate.
3. **Ownership / title** — reference only, to the ownership/party model; lease interest recorded as legal-interest kind.
4. **Operational responsibility assignment** *(new, identifier unassigned)* — ISO 41011 demand-organisation ↔ service-provider split from WM-BLT-006, applied at asset scope, with delegated scope and governing agreement reference.
5. **Occupancy / use designation** — effective-dated use of a space or locus by an asset or function.
6. **Availability** — derived, never stored as truth.
7. **Maintenance** — reference to WM-ACT-007 plus asset condition assessment.

Possession never implies title; responsibility never implies custody; placement never implies access rights.

## Planned versus observed

Two assertion classes, never merged. **Observed** carries WM-OBJ-001 semantics (read point vs business location, observation time separate from ingestion time, precision, source device). **Planned** is an intent under a named plan/scenario identifier with an authorizing role. Uncertainty is explicit: positional accuracy with method, containment confidence, staleness threshold beyond which an observation stops being presented as current, and `unknown whereabouts` as a first-class state with last-known fix — never recorded as non-existence. Divergence between plan and fact is a reportable exception, not silently resolved.

## Occupancy and availability

`OccupancyView` = placement ∩ space ∩ use designation ∩ capacity, as-of a stated instant, with aggregate counts only. Availability answers "which sites are unavailable for a task" and is **computed per purpose**, disclosing its inputs: site lifecycle state, operating hours and access regime, facility operational status, regulatory standing (WM-BLT-006 blocks `in-use` on expired authorisation), hazard/contamination overlay, maintenance window, security zone. Availability for one task class is not availability for another.

## Maintenance

WM-ACT-007 authorizes and groups tasks (CONTAINS WM-ACT-006); performed-work evidence is external. "Maintenance due" is derived from condition assessment plus schedule and is **not** an availability state and **not** a custody or responsibility change. Work orders resolve back to asset, system, facility and site without duplicating execution records.

## Privacy and projections

- Personal/home locus: store at most a generalized place or jurisdiction reference; never mint a premises, facility or building record from a home address.
- Sensitive assets and sites: graded generalization with disclosure that withholding occurred (withheld ≠ absent); coarsening is one-way and not recoverable from published data.
- Default public projection omits holder identity, custodian, precise coordinates and condition detail.
- Emergency, regulator and lawful-access routes are named exceptions with audit entries.

## Time/version/scenario

Bitemporal throughout: real-world validity vs record version lifespan, with event, observation and ingestion times distinct; RFC 3339 with explicit offset. Landscape publications are as-of snapshots with a content digest; corrections supersede, real-world changes close-and-open. Scenarios are named planned-placement sets that never merge into the observed stream.

## Acceptance scenario

Leased asset moves Site A → Site B. Ownership relation is unchanged (external lessor, legal interest `leased`). Placement episode at A closes; a planned placement to B exists under a move plan; an observed placement at B opens on first fix, with in-transit containment (handling unit / vehicle) representable. Custody may transfer to a carrier and then to B's operator — independently of responsibility, which transfers from A's service provider to B's on its own effective date. Maintenance remains due: the open work order re-resolves to the new facility/system without closing. Every prior interval is retained, so the landscape is reconstructable at any past instant, and at no point is the asset's identity, the lessor's title, or either site's identity altered.

## Invariants

1. Place and asset never merge; neither is identified by the other.
2. Every placement, custody, ownership, responsibility, occupancy and maintenance link has a period and an asserting party.
3. Containment is asserted and evidenced, never inferred from geometry.
4. Planned ≠ observed; both are dated; divergence is an exception.
5. Unknown location is an explicit state, not absence or disposal.
6. Custody ≠ title ≠ operational responsibility ≠ access.
7. A registered/postal address locates a *binding*, never an asset set.
8. Availability is derived per purpose and discloses inputs.
9. Personal location is protected by policy and generalized in derived views; withheld is distinguishable from absent.
10. A landscape publication masters nothing; it cites versions.

## Minimal profile shape

`AssetPlaceLandscape`: identifier; viewpoint; `geographic_scope`, `asset_scope`, `as_of`, `maintenance_policy` (all **candidate-not-normative**, carried from LND-17 v1); included model ids with pinned versions; disclosure class; owner; publication digest.
`OccupancyView`: view definition — locus scope, period, aggregation level, suppression rules — no stored occupancy facts.
`PlacementEpisode` / `ResponsibilityAssignment`: subject ref, locus or party ref, mode, period, basis, authority, confidence, disclosure class.

## Holds

Publication holds of WM-BLT-006 and WM-BLT-008 are inherited unresolved (ISO clause text unread; IFC host/version unpinned; EPA FIDS date conflict; multi-profile validation incomplete). WM-BLT-002 is a previous-version reservation and must be migrated, not replaced. Multi-site facility apportionment is unresolved. Two relation identifiers are unassigned. No semantic crosswalk verified; no fixtures run. Privacy and employment-law review outstanding.

**No claim of canonical completeness or installability is made.** This is a research-checkpoint decision on a reviewable draft.
