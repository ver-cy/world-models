## DECISION

**Combination: REUSE (4) + COMPLETE RESERVED MODEL (1) + PROFILE (1) + NEW MODEL (1). LANDSCAPE rejected.**

- **REUSE unchanged:** WM-PLC-010 Gazetteer Place (named place, geographic identifier, sensitivity/generalization mixin), WM-BLT-008 Site / Campus, WM-BLT-006 Facility, WM-BLT-001 Building / Structure. All four already carry identity, bitemporal lifecycle, address-by-reference and party-by-reference. Nothing in EM-FAC-01 requires a new physical container.
- **COMPLETE RESERVED MODEL WM-BLT-002 Premises / Spatial Unit** as the single interior-space master. Three published models already point at a space master that does not exist (WM-BLT-006 out-of-scope "Space model", WM-BLT-001 `COMPOSE` to WM-BLT-002, WM-OBJ-001 naming WM-BLT-002 master for premises identity/geometry/address semantics). This is a dangling reference, not a new idea.
- **PROFILE, not model: Use / Occupancy Designation.** "Office" is a dated designation assertion profile applied to WM-BLT-002 and WM-BLT-006. It has no identity of its own and no lifecycle beyond its validity window.
- **NEW MODEL WM-WPL-001 Workplace Allocation** (relationship/event model, `entry_kind: relationship`). Proof of independent identity below.
- **WM-PLC-009 Indoor Space: retired by merge, not kept as a synonym.**

Smallest coherent composition (containment spine): Gazetteer Place ←reference— Site/Campus —contains→ Facility —contains→ Building/Structure —composes→ Premises/Spatial Unit (recursive) ←locus— Workplace Allocation.

## BOUNDARY AND OVERLAP RESOLUTION

**WM-BLT-002 vs WM-PLC-009.** Both describe a bounded interior extent. Two identities for one room is the defect, so one entry must lose standalone status. WM-BLT-002 wins on evidence, not seniority: it has a spec (`U2-premises-and-spatial-unit.md`), an inbound `CONTAINS` from WM-BLT-001, a declared `contains_ids` to WM-OBJ-001, and a named mastership claim from WM-OBJ-001. WM-PLC-009 has no spec, no composition role, no relations file and a purpose that only records that its boundary is unresolved.

Action: set WM-PLC-009 `status: retired-superseded`, `possible_duplicate_of / superseded_by: WM-BLT-002`, `entry_kind: profile-of`. Keep `NAV.PHY.PLC.IND` as a redirect alias onto an **Indoor Topology profile of WM-BLT-002** (navigable cell, connectivity graph, indoor positioning reference). That content is a projection over the same spatial unit, so it is a profile, never a second class. Do not mint an "Indoor Space" class name as an alternate name for Premises: aliasing at class level is how synonym drift restarts.

**Other boundaries held.** Premises identity ≠ address (WM-PLC-010 / address sibling). Premises ≠ legal branch: a branch is an Organization-model construct that *references* a premises as registered or operating locus; no designation on a premises may create, imply or publish a branch, and no branch registration may mint a premises. Lease and licence terms stay in the agreement sibling (referenced by identifier only). Employment stays WM-ORG-005, which already declares it does not own workspace identity. Person, credential and access-card issuance stay in Identity/Access. Desk *reservations* stay in the Booking sibling. Facility keeps only aggregate space counts and area totals, as it already states.

**Does allocation need its own identity?** Yes, on three independent grounds. (1) The locus may not be a registry object at all — home, mobile and client-site workplaces have no premises row, so the allocation cannot be an assertion hanging off WM-BLT-002. (2) One employment period carries several concurrent allocations with different dates, exclusivity and approvers; folding them into WM-ORG-005 either flattens them or re-invents a relationship table inside Employment. (3) It must survive replacement of both endpoints (premises re-parented or split, employment record superseded) and be independently supersedable and auditable. That is an identity, not a field.

## MINIMAL CONTRACTS

**WM-BLT-002 Premises / Spatial Unit**

*Identity:* opaque persistent identifier, master-system qualified. Created when a spatial extent is separately usable or separately governed. Unit designator, storey label, address and occupier are attributes, never identifiers. Exactly one active parent containment at a time (Building, Facility or Premises), dated; re-parenting does not mint a new identifier.

*Lifecycle:* planned → shell/constructed → fit-out → available → in use → vacant → out of service / refurbishment → decommissioned / demolished; plus split and merge transitions requiring predecessor–successor lineage and reason. Bitemporal (record validity distinct from real-world validity), inherited from the existing versioning mixin.

*Core fields:* id; parent ref + period; spatial-unit kind (room, suite, floor, open area, apartment, parking bay, unallocated circulation); designator + issuing authority; geometry ref with CRS and LoD (geometry mixin); measured area with declared measurement standard, method and date; design occupant capacity; separately-governed flag; control and occupancy role refs (controller, occupant, service provider) with validity and agreement ref; use/occupancy designation assertions (dated, with asserting authority, code-occupancy kept distinct from operational designation); sensitivity class.

*Invariants:* (i) address is never sole or mandatory identifier; (ii) contained extents may not exceed the parent extent, and containment periods may not overlap across parents; (iii) designation, occupancy and control are dated assertions and never change identity; (iv) no person, credential, lease-term, employment or booking data — references only; (v) split/merge requires lineage; (vi) a premises record may not be created from a worker's residential address.

**WM-WPL-001 Workplace Allocation**

*Identity:* opaque id over (subject context, locus, workplace kind, validity window, authority). *Lifecycle:* proposed → active → suspended → ended / superseded / revoked; one authority per transition; effective-dated with supersession lineage.

*Core fields:* subject ref (employment or engagement context, not person master); locus — exactly one of premises ref, facility/site ref, or external-locus descriptor {kind: client-site | third-party | home | mobile, jurisdiction ref via WM-PLC-010, controlling org ref}; workplace kind (assigned desk, shared-desk entitlement, hotelling, office-based, remote-home, mobile, client-site); exclusivity (exclusive | shared | pooled); validity window and recurrence; approving authority; purpose; primary-work-location flag; disclosure class; status.

*Invariants:* no address string, no PII, no lease or agreement terms, no access rights, no reservation instances; must not create or imply a premises, facility or branch; at most one primary work location per subject per period; remote-home locus precision capped at jurisdiction granularity; access grants are never derived automatically from an allocation.

## ACCEPTANCE WALKTHROUGH

1. **Containment:** Gazetteer Place names the locality; Site holds managed extent and tenure refs; Facility is the operating unit; Building holds fabric; Premises holds the room. Each retains its own identifier and lifecycle.
2. **Office as role:** a Premises carries a dated `office` use designation; the branch, if any, is an Organization record referencing it. Removing the designation does not touch either identity.
3. **Address change:** Site and Premises identifiers are unchanged; the role-tagged address reference is superseded with its own validity, per existing Site lifecycle rules.
4. **Leased office / client site:** occupancy and control roles are dated refs with an agreement identifier; ownership is absent. A client site needs no premises record — it is an external-locus descriptor on the allocation.
5. **Remote worker:** allocation kind `remote-home`, locus = jurisdiction ref only. No premises, no facility, no designation, no published address.
6. **Hot desk / hotelling:** allocation with exclusivity `shared` or `pooled`, bounded window and recurrence; the daily desk reservation resolves in the Booking sibling against that entitlement.
7. **Seven-way separation:** identity (WM-BLT-002) / designation (profile) / allocation (WM-WPL-001) / lease (agreement sibling) / employment (WM-ORG-005) / access (Identity–Access) / booking (Booking sibling), each with its own authority and dates.
8. **Allocation identity:** established above; it is a model, not a profile.

WM-ACT-040's external Workspace and Facility masters now resolve to WM-WPL-001 and WM-BLT-006.

## PRIVACY AND AUTHORITY RULES

Residential addresses remain in the Party/Person master under its own access controls; allocation stores only the fact of remote work and a jurisdiction. Home loci are never publishable, never designated, never aggregated into public premises or facility inventories. Apply the WM-PLC-010 graded sensitivity mixin to premises and allocation: default non-public for occupancy, capacity and allocation; generalize rather than randomize; record what was withheld, on what basis, who may except it, and the review date. Authority: premises identity and geometry — facility/premises owner or custodian; code occupancy — authority having jurisdiction only; operational designation — facility management; allocation — employing organization's named approver; jurisdiction and place naming — external gazetteer authority. No single role may assert across two of these.

## HOLDS AND PUBLICATION RECOMMENDATION

Publish WM-BLT-002 and WM-WPL-001 as **reviewable-draft, publishableCanonical false**. The composition cannot exceed its weakest member: all four reused models are reviewable drafts with open source-pinning holds, and WM-BLT-001 is a single-provider waiver.

Inherited blockers: the unresolved IFC documentation host/build pin (WM-BLT-006 and WM-BLT-008 disagree), the Facility-contains-Building versus IfcBuilding-subtype-of-IfcFacility conflict, unread ISO clause text, and incomplete non-US/multi-profile validation.

New holds: (1) re-read and diff `U2-premises-and-spatial-unit.md` before completion — WM-BLT-002 is `described-previous-version`, so this is a migration, not a green field; (2) pin one IFC citation for IfcSpace/IfcSpatialZone and one for COBie Space/Zone; (3) IndoorGML and indoor-positioning grounding is unverified — publish the Indoor Topology profile as provisional; (4) area measurement standards (ISO 9836, IPMS) cited for existence only, so no field-level area naming; (5) WM-WPL-001 needs an employment-law and data-protection cross-check in at least one non-US jurisdiction, including works-council consultation on desk-level allocation records, before any operational use; (6) registry hygiene: record the WM-PLC-009 supersession, update `VERCY-MODEL-RELATIONS.csv`, and re-target every "Space model" reference in WM-BLT-006 and WM-BLT-001 to WM-BLT-002; the current `factor_overlap` of 0.08 on both reserved entries is contradicted by this review and should be corrected.
