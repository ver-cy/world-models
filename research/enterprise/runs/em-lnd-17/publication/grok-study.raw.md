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
