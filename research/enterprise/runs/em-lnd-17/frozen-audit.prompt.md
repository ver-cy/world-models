# Frozen no-tools semantic audit — EM-LND-17
You are the sole final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, allocate registry IDs, grant publication authority, or ask for a rerun.
Audit the two identifier-unassigned relation candidates and the shared held landscape/projection boundary. Asset Place Landscape has only local governed artifact identity; Occupancy View has no independent identity. Asset Placement Episode and Operational Responsibility Assignment are proposed as independently identified relation roots. Test identity, lifecycle, time, authority, containment, privacy, maintenance, custody/title/responsibility separation and reproducible history.
Return at most 1600 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Material defects (number each real defect); Required fixes; Additional fixtures (one fenced JSON array only; every case has target `AssetPlacementEpisode`, `OperationalResponsibilityAssignment`, or `LandscapeProjection`, id, kind positive|negative, input object, expect object, and expectedCode when negative); Freeze decision. Explicitly state the identifier decision. Base and registry gaps are holds unless they make the candidate unsafe. This is the one frozen audit and will not be repeated.
## Asset Placement Episode candidate
```json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-LND-17","proposedName":"Asset Placement Episode","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"One governed placement episode remains identifiable while the asset, locus description, evidence, confidence and disclosure rendition evolve during the same effective interval.","versionIdentity":"Corrections, evidence additions and disclosure changes create versions of the episode; a new effective placement interval or materially different locus creates a successor episode.","independentLifecycle":["planned","observed","effective","corrected","superseded","closed","unknown"],"mastership":"asset placement authority or evidence-governance authority"},"boundary":{"owns":["persistent placement-episode identity","asset and locus references with explicit spatial granularity","planned or observed placement mode","effective interval and observation time","asserting party, governing basis and source evidence","confidence, precision and disclosure class","planned-versus-observed divergence","correction, supersession and closure lineage"],"references":[{"target":"WM-OBJ-001","purpose":"Physical asset identity and custody boundary"},{"target":"WM-BLT-006","purpose":"Facility locus"},{"target":"WM-BLT-008","purpose":"Site or campus locus"},{"target":"WM-BLT-001","purpose":"Building locus"},{"target":"WM-PLC-010","purpose":"Generalized place or jurisdiction locus"},{"target":"WM-XCT-010","purpose":"Address binding without identity inference"},{"target":"WM-ACT-007","purpose":"Maintenance work reference without completion inference"}],"excludes":["asset, place, site, facility, building or interior-space identity","custody, possession, ownership, title or lease rights","operational responsibility or employment assignment","physical or logical access authorization","occupancy, utilization or availability facts","maintenance execution or work completion"]},"objects":{"AssetPlacementEpisode":{"identity":["assetPlacementEpisodeId"],"required":["assetRef","locusRef","locusKind","placementMode","validFrom","assertingPartyRef","status"],"optional":["validTo","observationTime","ingestionTime","basisRef","evidenceRefs","precision","confidence","disclosureClass","scenarioRef","supersedesRef"],"lifecycle":["planned","observed","effective","corrected","superseded","closed","unknown"]}},"invariants":["Every placement episode identifies exactly one asset and one explicit locus at a declared spatial granularity.","An address never proves that an asset is placed at the addressed site, facility or building.","Geometry overlap, shared address and reporting boundary never imply containment or placement.","Planned and observed placements remain distinct and may coexist with an explicit divergence state.","Observed placement records observation time, ingestion time, source, precision and confidence.","A new effective locus closes or supersedes the prior episode without erasing history.","Placement never grants custody, title, operational responsibility, access or maintenance authority.","Custody, ownership and responsibility changes do not silently rewrite placement.","Unknown whereabouts is explicit and may retain a separately qualified last-known locus.","Withheld location is distinct from unknown, absent, disposed and never observed.","Personal and sensitive loci are generalized or withheld according to disclosure policy.","A projection never reconstructs a finer location than its authorized source rendition.","Maintenance context may reference placement but never proves that work was performed or completed.","Corrections append provenance and preserve the assertion that was previously effective."],"holds":["Registry namespace and identifier allocation are pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","WM-BLT-002 completion and multi-site facility semantics require reconciliation.","Source crosswalks, privacy review and canonical validation remain pending.","Package conversion and live verification are pending."]}

```
## Asset Placement Episode fixtures
```json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Asset Placement Episode","cases":[{"id":"leased-asset-move","kind":"positive","input":"A leased asset moves from Site A to Site B while title remains with the lessor.","expect":"The Site A episode closes, planned and observed Site B episodes remain distinguishable, and title is unchanged."},{"id":"plan-observation-divergence","kind":"positive","input":"A plan places an asset in Facility B but telemetry still observes it in Facility A.","expect":"Both assertions remain traceable and the divergence is explicit."},{"id":"unknown-whereabouts","kind":"positive","input":"Current whereabouts are unknown but the last verified locus is retained.","expect":"Unknown current placement and qualified last-known placement remain separate."},{"id":"address-implies-placement","kind":"negative","input":"A registered company address is used to place every company asset there.","expect":"The inference is rejected."},{"id":"placement-implies-rights","kind":"negative","input":"Observed placement is used to infer custody, title, access and operational responsibility.","expect":"All four inferences are rejected."},{"id":"overwrite-move-history","kind":"negative","input":"A Site B observation overwrites the prior Site A placement.","expect":"The update is rejected; the prior episode must be closed or superseded."},{"id":"privacy-reconstruction","kind":"negative","input":"A public occupancy view reconstructs a precise home location from generalized inputs.","expect":"The disclosure is rejected."}]}

```
## Operational Responsibility Assignment candidate
```json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-LND-17","proposedName":"Operational Responsibility Assignment","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"One authorized responsibility assignment remains identifiable across changes to operational placement, custody, asset condition and evidence during its effective interval.","versionIdentity":"Scope, role, authority, basis or validity changes create effective-dated assignment versions; transfer to a different responsible party creates a successor assignment.","independentLifecycle":["proposed","authorized","active","suspended","transferred","ended","revoked"],"mastership":"asset operations governance authority"},"boundary":{"owns":["persistent operational-responsibility assignment identity","responsible party and asset-scope references","operational role or capacity","effective interval and status","governing basis and authorizing authority","scope limitations and delegation constraints","transfer, suspension, revocation and termination history","assignment evidence and provenance"],"references":[{"target":"WM-OBJ-001","purpose":"Physical asset and custody boundary"},{"target":"WM-BLT-006","purpose":"Facility scope when responsibility is locus-qualified"},{"target":"WM-BLT-008","purpose":"Site scope when responsibility is locus-qualified"},{"target":"WM-ACT-007","purpose":"Authorized maintenance work without completion inference"},{"target":"WM-XCT-010","purpose":"Address binding without responsibility inference"}],"excludes":["party, asset, place, site or facility identity","custody, possession, ownership, title or lease rights","asset placement or occupancy","employment, position or general organizational membership","physical or logical access authorization","maintenance event, work order execution or completion evidence"]},"objects":{"OperationalResponsibilityAssignment":{"identity":["operationalResponsibilityAssignmentId"],"required":["responsiblePartyRef","assetScopeRef","responsibilityRole","validFrom","authorityRef","status"],"optional":["validTo","governingBasisRef","locusScopeRef","delegationConstraints","evidenceRefs","successorRef"],"lifecycle":["proposed","authorized","active","suspended","transferred","ended","revoked"]}},"invariants":["Every assignment names one responsible party, one explicit asset scope and one operational role.","Responsibility requires an authorizing authority and governing basis.","Responsibility is effective-dated and historical assignments remain resolvable.","Custody, possession, title, lease, employment and placement never imply operational responsibility.","Operational responsibility never grants physical or logical access.","A transfer closes or supersedes the prior assignment without overwriting it.","Responsibility may be locus-qualified, but an address or containment edge never creates it.","A maintenance work order may be addressed to a responsible party but does not redefine the standing assignment.","A responsibility assignment does not prove that maintenance was performed or completed.","Delegation preserves the accountable assignment and records the permitted delegated scope.","Suspension and revocation are distinct and retain authority provenance.","Placement and custody may change independently without silently changing responsibility."],"holds":["Registry namespace and identifier allocation are pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Party authority and asset-scope crosswalks require canonical reconciliation.","Package conversion and live verification are pending."]}

```
## Operational Responsibility Assignment fixtures
```json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Operational Responsibility Assignment","cases":[{"id":"carrier-custody-separate","kind":"positive","input":"A carrier has custody during transit while the operator remains operationally responsible.","expect":"Custody and responsibility remain separate effective assignments."},{"id":"responsibility-transfer","kind":"positive","input":"Responsibility transfers from Site A operations to Site B operations after commissioning.","expect":"The prior assignment closes and a successor starts with authority and history."},{"id":"delegated-maintenance","kind":"positive","input":"The accountable operator delegates a bounded inspection task to a contractor.","expect":"Delegation is recorded without replacing accountability or asserting work completion."},{"id":"custody-implies-responsibility","kind":"negative","input":"The current custodian is automatically made operationally responsible.","expect":"The inference is rejected."},{"id":"address-implies-responsibility","kind":"negative","input":"A company's registered address makes that office responsible for all assets.","expect":"The inference is rejected."},{"id":"work-order-proves-completion","kind":"negative","input":"A work order addressed to the responsible party is treated as completed maintenance.","expect":"The inference is rejected."},{"id":"silent-transfer","kind":"negative","input":"A placement move silently rewrites the responsible party.","expect":"The update is rejected without an authorized successor assignment."}]}

```
## Local synthesis
# EM-LND-17 local synthesis

## Disposition

- Reuse the existing spatial and physical-item masters. Do not create a new place, facility, building or asset type.
- Treat **Asset Place Landscape** as a governed landscape declaration with local artifact identity for scope, viewpoint, owner, pinned inputs, as-of time, disclosure policy and publication digest. No catalogue/runtime identifier is allocated without a registry reservation.
- Treat **Occupancy View** as a named, reproducible projection inside that declaration; it has no independent identity.
- Raise **Asset Placement Episode** and **Operational Responsibility Assignment** as identifier-unassigned relation candidates. They have independent validity and lifecycle, but registry allocation and boundary review are still required.

## Mastership and spatial spine

Gazetteer place, site/campus, facility, building/structure, interior spatial unit and movable physical item remain separate identities. The composed spine is place/parcel → site → facility → building → spatial unit, with movable items attachable at any appropriate level. Address is a binding/value object and never the identity of a place, facility or asset.

Containment is an authored, evidenced and effective-dated assertion. Geometry overlap, common address or reporting boundary cannot create containment. Site-to-facility membership may be absent or non-exclusive. A registered company address never locates all company assets.

## Placement, custody and responsibility

Placement, custody, title, operational responsibility, occupancy/use, availability and maintenance are distinct:

- placement records asset, locus, granularity, planned or observed mode, validity, basis, asserting party, confidence and disclosure class;
- custody remains owned by WM-OBJ-001;
- ownership/title and lease interest remain external legal/economic relations;
- operational responsibility relates a responsible party to an asset scope for a validity interval and governing basis;
- occupancy/use is an effective-dated designation or relation;
- availability is derived for a stated purpose;
- maintenance references work orders and condition evidence.

Possession does not imply title, responsibility does not imply custody, and placement does not grant access.

## Planned, observed and available

Planned placement belongs to a named plan/scenario and authorizing context. Observed placement carries observation time, ingestion time, source, precision and confidence. Divergence is an explicit exception. Unknown whereabouts is a state with an optional last-known fix; it is not absence or disposal.

Occupancy View computes effective placement intersected with space, use designation and capacity at a stated instant. Availability additionally depends on purpose, operating hours, access regime, operational/regulatory state, hazard overlays and maintenance windows. It is never stored as a timeless fact.

## Acceptance result

A leased asset moves from Site A to Site B. The A placement closes; a planned B placement exists under the move scenario; an observed B placement opens when evidence arrives. Ownership remains with the lessor. Custody may pass through a carrier. Operational responsibility transfers on its own effective date. An open maintenance order remains due and re-resolves to the new operational context without proving work completion. Every historical interval remains reconstructable.

## Privacy invariants

Personal/home loci are represented only at the authorized generalized place or jurisdiction level. Sensitive asset and site coordinates are coarsened or withheld according to policy. Withheld and absent remain distinct. Derived views cannot reconstruct finer location from released data, and exceptional access is purpose-bound and audited.

## Holds

WM-BLT-006 and WM-BLT-008 remain `publishableCanonical: false` with unresolved source, IFC, crosswalk and validation holds. WM-BLT-002 still needs completion as the interior-space authority. Multi-site facility apportionment and the two proposed relation boundaries remain unresolved. No new identifier is allocated, and no installable release is claimed.

## Initial Claude study
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

## Exact Grok response
Verdict: Accept with conditions. Reuse the existing spatial and asset masters. Asset Place Landscape stays a governed declaration with local artifact identity only. Occupancy View stays a projection. Asset Placement Episode and Operational Responsibility Assignment require independent identity; their identifiers remain unassigned and must not be invented here. No standards conformance is claimed.

Strongest evidence. The leased-asset move separates every axis the proposal keeps distinct. Title stays with the lessor. Placement changes from Site A to Site B only by an evidenced episode. Custody and operational responsibility can change on their own clocks. Maintenance remains due under WM-ACT-007. History is reconstructable only if those facts are not collapsed into the asset, the site, or the landscape declaration.

Strongest counterexample. Inferring that a company’s registered address locates all of its assets. A shared WM-XCT-010 address, a shared organisation, or geometric overlap does not place WM-OBJ-001 items, does not prove containment in a WM-BLT-008 site, WM-BLT-006 facility, or WM-BLT-001 building, and does not transfer custody, title, or responsibility. That inference is rejected.

Identity and mastership. Place (WM-PLC-010), site/campus (WM-BLT-008), facility (WM-BLT-006), building (WM-BLT-001), interior space, and movable asset (WM-OBJ-001) keep separate masters. Address is a cross-reference, not a location master. Asset Place Landscape is a local governed artifact: scope, viewpoint, owner, pinned inputs, as-of, disclosure, digest. It gets no catalogue or runtime ID. Occupancy View is derived and has no independent identity. Asset Placement Episode and Operational Responsibility Assignment are the only candidates that require independent identity: each is a time-bounded, multi-party, referenceable fact that must survive changes to declarations and views.

Spatial spine. Gazetteer place, site/campus, facility, building, and interior space remain separate identities. Containment is an evidenced relation, never inferred from geometry, nesting of names, or a common address. A site does not contain a facility unless an evidenced containment says so. A building does not contain an interior space unless evidenced. A movable asset is not inside any of them unless a placement episode says so.

Placement, custody, title, responsibility. Placement is where the item is put, planned or observed. Custody is who holds it. Title is who owns it; on a lease it stays with the lessor. Operational responsibility is who must act. None implies another. A placement episode may name a site or facility without asserting containment.

Planned versus observed. A planned placement is an intention with its own interval. An observed placement is an evidenced fact. They are not versions of one record. Closing a plan does not create an observation. An observation does not retire a plan unless that effect is stated.

Occupancy and availability. Occupancy View is a projection over evidenced occupancy, not a master. Availability is derived per purpose: an item can be occupied, reserved, under maintenance, and still available for a different purpose. No single availability flag is authoritative.

Maintenance. A due work order (WM-ACT-007) survives a change of site, custody, or responsibility. Completing or transferring custody does not clear the obligation. Maintenance history stays addressable after the move.

Privacy. Personal and sensitive locations are generalized or withheld in the landscape declaration, in every Occupancy View, and in any digest. A projection must not re-expose a location the declaration withheld.

Scenario. A leased asset moves from Site A to Site B. Title remains with the lessor. An Asset Placement Episode records the evidenced move; a later return is a new episode. Custody may pass to the lessee at Site B without a title change. Operational Responsibility Assignment may pass to a local operator on a different effective time. The maintenance work order stays due against the asset. Reconstructing the history requires the episode and the assignment as independently identifiable facts. The lessor’s registered address locates none of this.

Invariants.

1. Place, site, facility, building, interior space, and movable asset identities are never merged.
2. Address does not locate an asset.
3. Containment is evidenced; geometry and co-address do not imply it.
4. Title, custody, placement, responsibility, occupancy, availability, and maintenance are separate facts.
5. A lease does not transfer title.
6. Custody change does not change title, placement, or maintenance due.
7. Responsibility change does not change custody or title.
8. Planned and observed placements are distinct and separately closed.
9. Availability is derived per purpose and is not stored as a master flag.
10. A maintenance obligation survives relocation and custody change.
11. Personal and sensitive locations stay generalized or withheld in every projection.
12. Landscape declarations pin inputs and as-of; they do not allocate asset or place identity.
13. History of move, custody, and responsibility is reconstructable without reading the current site of the asset.

Minimum profile shape. Masters: WM-PLC-010, WM-BLT-008, WM-BLT-006, WM-BLT-001, interior space, WM-OBJ-001, WM-XCT-010 as address only. Local artifact: Asset Place Landscape (scope, viewpoint, owner, pinned inputs, as-of, disclosure, digest). Projection: Occupancy View. Independently identifiable relations, IDs still unassigned: Asset Placement Episode (asset, from-place, to-place, planned/observed, interval, evidence); Operational Responsibility Assignment (asset, party, role, interval, evidence). Boundary: WM-ACT-007 remains the maintenance master. No new catalogue type for the landscape or the view.

Blockers. Identifiers for Asset Placement Episode and Operational Responsibility Assignment are unassigned; do not ship them under a borrowed ID. Containment evidence is unspecified, so geometry must not fill the gap. Disclosure rules for sensitive locations are not yet pinned to every projection path. Until those three are closed, the profile is a declaration and a projection only, not an operational placement store.
