# Independent review request: EM-FAC-01 Place, office and workplace

Act as an independent enterprise facilities and information-architecture reviewer. Use only public information and do not request personal employee or residential data.

Review this proposed Vercy composition:

- WM-PLC-010 Gazetteer Place: https://ver.cy/models/wm-plc-010-gazetteer-place/
- WM-BLT-008 Site / Campus: https://ver.cy/models/wm-blt-008-site-campus/
- WM-BLT-006 Facility: https://ver.cy/models/wm-blt-006-facility/
- WM-BLT-001 Building / Structure: https://ver.cy/models/wm-blt-001-building-structure/
- EM-FAC-01 assignment: https://ver.cy/enterprise/models/em-fac-01/

Two reserved unpublished entries overlap: WM-BLT-002 Premises / Spatial Unit and WM-PLC-009 Indoor Space. Published models already point to WM-BLT-002 as the premises/space identity and geometry master. Local and Claude analysis proposes completing WM-BLT-002, retiring WM-PLC-009 as a standalone synonym, and preserving indoor navigation/topology as a WM-BLT-002 profile.

The same analysis treats `office` as an effective-dated use designation, not a physical identity or legal branch. It also proposes an independently identified Workplace Allocation relationship between an employment/engagement context and a premises, site, client-site, home-jurisdiction or mobile locus. No numeric identifier should be assigned until registry review.

Test:

1. Is the physical containment spine Place → Site → Facility → Building → Premises coherent?
2. Should WM-BLT-002 and WM-PLC-009 be merged, and which identity should survive?
3. Is office correctly represented as a use/designation profile?
4. Does workplace allocation require independent identity, or can an existing employment/space model own it?
5. Can leased offices, client sites, coworking, pooled desks and remote/mobile work be represented without building ownership?
6. How should address change preserve site and premises identity?
7. How should home-work context avoid creating or publishing a residential premises record?
8. Are lease, access, booking, employment and legal-branch boundaries correctly external?

Acceptance scenario: a hybrid team uses a leased office, pooled desks, remote work and a client site without the employer owning a building or publishing home addresses.

Return no more than 1000 English words with headings:

DECISION
PHYSICAL MODEL BOUNDARY
WORKPLACE ALLOCATION BOUNDARY
ACCEPTANCE SCENARIO
PRIVACY AND AUTHORITY
HOLDS AND PUBLICATION RECOMMENDATION

Explicitly choose the fate of WM-PLC-009 and say whether Workplace Allocation is REUSE, PROFILE or NEW MODEL. Do not invent a numeric model identifier.
