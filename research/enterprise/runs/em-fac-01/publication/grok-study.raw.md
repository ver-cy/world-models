DECISION

Accept the proposed composition with four corrections.

The physical spine is a preferred reference path, not mandatory exclusive containment. Gazetteer Place locates; it does not parent a managed site.

Retire WM-PLC-009 as a standalone synonym. Surviving identity is WM-BLT-002 Premises / Spatial Unit. Indoor navigation and topology survive only as a WM-BLT-002 profile.

Office is an effective-dated use/designation profile, not a physical identity and not a legal branch.

Workplace Allocation is a NEW MODEL (relationship). It is not REUSE of employment, work assignment, position or premises occupancy, and not a PROFILE of those models. No numeric catalogue identifier is assigned.

PHYSICAL MODEL BOUNDARY

Gazetteer Place (WM-PLC-010) is a named real-world location whose opaque identifier survives rename, reclassification and re-delimitation. A date, name or coordinate pair is never the identifier. The model is gazetteer-centric and does not govern indoor units unless they are separately registered as named places. Cross-theme linking to built works is deferred.

Site / Campus (WM-BLT-008) is bounded land under coordinated management. It may contain facilities, infrastructure and open space; it may include discontiguous parts and third-party enclaves; its operational boundary may diverge from the legal parcel.

Facility (WM-BLT-006) is a managed aggregation of buildings, structures, systems and grounds. It is not a space and not a single asset. Site containment is conditional: IFC permits a facility with no site. Identity persists through site split or amalgamation.

Building / Structure (WM-BLT-001) is a persistent engineered artifact. Site, parcel and address are external georeferences, not identity. Premises, space and zone are referenced through spatial decomposition; the building does not absorb their mastership.

Premises / Spatial Unit (WM-BLT-002, published only as 0.2.0-legacy) is the interior identity and geometry master: independently delineated units, successive boundaries, common parts, use class and occupancy spells. A premise sits inside a building shell but is transacted and occupied independently of that shell.

Preferred path: Place locates Site; Site may contain Facility; Facility may contain Building; Building contains Premises. Allowed exceptions already present in the published models: facility without site; building without facility; premises in a building the employer does not own; workplace loci that never enter the building layer (client site, home-jurisdiction, mobile).

WM-PLC-009 Indoor Space must not be completed as a gazetteer sibling. Indoor space is a bounded built-environment unit with geometry, common parts, merge and split events. Published models already point at WM-BLT-002; WM-XCT-010 resolves floor, unit, room and seat locators to the premises model. A parallel PLC identity would split the master. No public published page for WM-PLC-009 was found.

WORKPLACE ALLOCATION BOUNDARY

Office is a use designation. A premises or site may carry an effective-dated office use class without changing identity. The same unit can be office this year and shop next year. “Registered office” remains a legal-address role on the organization (WM-ORG-001). Business establishment / branch (WM-ORG-011) is an operating-presence record with no universal equivalence to premises, site or legal entity. “Office of the CTO” is an organizational function and is out of this composition.

Workplace Allocation cannot be owned by employment or by space.

WM-ORG-005 records workplace, remote, mobile and cross-border context by reference; it does not identify concurrent allocations.
WM-ORG-016 binds an agent to a role or body of work and references a base location; one assignment commonly needs several concurrent loci.
WM-ORG-004 records a position’s default work-location arrangement, not a person-period allocation.
Legacy occupancySpell records who occupies a unit. It is premises-centric, names occupants, is silent for mobile and jurisdiction-only loci, and is unsafe for homes.

Workplace Allocation is therefore a NEW MODEL: an independently identified, effective-dated relationship between an employment or engagement context and a polymorphic locus — premises, site, client-site, home-jurisdiction or mobile. Cardinality is many concurrent allocations per engagement. Booking, hoteling and badge grants remain external. No numeric identifier is minted until registry review.

Lease, access, booking, employment and legal-branch boundaries are correctly external, as EM-FAC-01 already states. Location is not a legal branch.

ACCEPTANCE SCENARIO

A hybrid team is representable without employer building ownership and without publishing homes.

Leased office: third-party Site and/or Premises, office use designation, external lease. No employer Building master.
Pooled desks: Premises or spatial units plus dated Workplace Allocations; desk booking stays external.
Client site: referenced third-party Site, Facility or Premises; no ownership transfer.
Remote/mobile: Workplace Allocation mode with host jurisdiction and optional coarse gazetteer Place; no Building required.

Address change does not mint a new Site or Premises. Address is a WM-XCT-010 binding. Rebind the address with a validity interval; keep the prior binding; site and premises identifiers persist.

PRIVACY AND AUTHORITY

The negative case is binding: a remote employee’s home address must not be published as a company office.

Do not mint a residential WM-BLT-002 premises from home-work. Do not project street-level or unit-level residential facts into any facilities or office directory. Home-work is an allocation mode plus jurisdiction, optionally a coarse Place (city or region). Street address, if held at all, stays on the party contact profile under purpose limitation and a disclosure policy. Occupancy spells must not be used for homes. Person civil-identity fields are not required merely to collaborate. Private instance records must not be sent to the public catalogue.

HOLDS AND PUBLICATION RECOMMENDATION

Recommend the corrected composition for further research. Do not declare it canonical.

Complete WM-BLT-002 from 0.2.0-legacy to a research draft before treating it as an installable master. Unresolved requires include parcel, organization and person; it is not installable today.

Retire WM-PLC-009 by registry decision; do not publish a stub.

Do not assign a numeric identifier to Workplace Allocation in this review.

WM-PLC-010, WM-BLT-008, WM-BLT-006 and WM-BLT-001 remain reviewable-drafts with open source and coverage holds. Facility CONTAINS Building versus IFC IfcBuilding-as-subtype remains an open crosswalk.

Home-work non-publication is a hard hold on any derived office directory. Semantic fit of the published BLT models to EM-FAC-01 still requires a full crosswalk; publication of a sibling does not complete this card.