**Verdict.** PROFILE WM-ORG-003 and REUSE WM-ORG-006. No new catalogue or runtime ID. Team, Collective and CommunityOfPractice are 003 profiles. TeamAssignment is the renamed 003 nested staffing record, not a second membership type. Membership stays 006. WorkingAgreement is a 003 charter component or a referenced instrument. TechnicalDomain is a classifier. This is standards alignment, not a W3C ORG, FHIR or SCIM conformance claim.

**Assignment / membership mastership.** Source facts: the card forbids conflating membership with employment or authority; rights and funding are not derived from the member list. 003 already stores time-bounded participation (role, period, allocation, `onBehalfOf`) and states that entitlements are relationships to resources, not the team. 006 already owns scheme, admission, standing, validity, terms, role and evidence, and typed non-equivalence to employment, office, subscription, licence and access.

- **TeamAssignment (003 component).** Staffing/participation of an agent on a team instance: `agentRef`, `teamRef`, team-scoped role, valid interval, allocation/FTE, employer or `onBehalfOf`, assignment status. Does not own admission scheme, community standing, dues, access grants or employment. Lifecycle is bound to the team; retiring the team closes open assignments. It does not end 006 memberships elsewhere.

- **Membership (006).** Governed belonging to a scheme-bearing body. Owns scheme, admission decision/basis, standing (proposed/active/suspended/ended/revoked), validity, terms, membership-role and evidence. May **outlive** any TeamAssignment. One agent may hold many 006 memberships and many 003 assignments (card invariant).

Temporary project/delivery teams: TeamAssignment is sufficient; 006 is optional. CommunityOfPractice / standing collaboration with admission rules: participants hold 006 memberships; TeamAssignment exists only if they also staff a working team. Fail if 003 copies a 006 member list, or if adding an assignment silently admits the agent to a community scheme.

**Verdict per type.**

| Type | Disposition |
|---|---|
| Team | 003 subject. Stable collective identity. Boundary class unit / collaboration / cohort. |
| Collective | 003 collaboration profile. Not a second master. |
| CommunityOfPractice | 003 standing-collaboration profile whose participants hold 006 memberships. |
| Membership | REUSE 006. Not nested in 003. |
| TeamAssignment | Renamed 003 nested record. PROFILE component, not a new ID. |
| WorkingAgreement | Owned charter component or referenced instrument. Not a new ID. |
| TechnicalDomain | Classifier. Governance stays with the stewarding community. |

**Inter-company cardinalities.** A two-company team is a 003 collaboration profile.

1. **Containment** — 0..1 FormalOrganization / tenant. A cross-company delivery team often has none. Containment is not administrative placement of a 002 unit (EM-ORG-04 already forbids that).
2. **Sponsors** — 1..n organizations that authorize, fund or charter the collective. Sponsor ≠ automatic employer of participants.
3. **Managing organizations** — 0..n. Day-to-day coordination. May be a subset of sponsors or a third-party PMO. Distinct from containing org and from each participant’s 005 employer.
4. **Record authority** — exactly 1. Steward of the 003 record. Dual authority is refused.

Participants are not those four slots; they appear as TeamAssignments and/or 006 memberships. Fail if sponsor is inferred from the roster, or if containment is invented so the team can sit on an admin org-chart axis. W3C ORG alignment: `org:OrganizationalCollaboration` is neither a FormalOrganization nor a sub-unit.

**Community profile.** A CoP has its own purpose and standing lifecycle — named, versioned charter, not a project with a baked-in end date. Participants hold 006 memberships. A person may belong to several communities and hold concurrent assignments. Product access, repo entitlements and budget lines are external grant records. Membership standing ≠ entitlement.

**Working-agreement / domain boundary.** WorkingAgreement is an owned 003 charter component when the text is collective-specific (this team’s ways of working, this CoP’s admission bylaws), versioned with the collective. It is a referenced instrument when reusable or multi-party (company-wide framework, multi-sponsor MoU, executed contract): the collective stores a pin (instrument id + edition), not a copy of normative text.

TechnicalDomain classifies the community (and optionally agreement scope). It is not an aggregate and not a second collective. Who may change methods or admit experts lives on 006 roles plus the community’s WorkingAgreement, not on the classifier code. Split trigger: a domain that needs its own lifecycle, methods and stewards as a practice object — and it still must not reuse the community’s 003 id.

**Access prohibitions.** Roster union never grants rights. Card invariant: rights and funding are not derived from the member list. 003 already treats entitlements as resource relationships.

1. 006 membership in community C authorises only what C’s own WorkingAgreement / entitlement records name. It does not union other members’ product ACLs, repositories, tenants or contracts.
2. TeamAssignment to temporary team T authorises only T’s scoped resources. It does not inherit other assignees’ employer entitlements.
3. Access grant is a separately dated fact. Grant validity is independent of membership standing and of assignment interval. Revoking membership does not silently delete a separately issued grant; ending a grant does not end membership.
4. Funding and cost-centre rights are likewise not inferred from the roster.

**Scenario results.**

*Negative — CoP member gains access to other members’ products.* Engineer E of member-org M1 joins CoP C. M2 also belongs and owns product P. Correct: E receives only C-scoped entitlements. No grant to P is minted. Building a P ACL from the CoP roster fails the card.

*Acceptance — temporary two-company team T + permanent community C.* T: two TeamAssignments (E1 `onBehalfOf` Co-A, E2 `onBehalfOf` Co-B), intervals I1/I2, no 006 required, optional referenced multi-party WorkingAgreement, exactly one record authority, sponsors ≥1. C: 006 memberships with scheme + admission + standing; community-specific charter owned as a WorkingAgreement component. Employment 005 of E1 at Co-A starts before T and may continue after T ends. Access: T-resource grants dated to I1/I2; C-resource grants dated to membership standing; Co-A product grants unchanged by T or C.

Four independently dated planes: employment (005), TeamAssignment (003), membership (006), access grant. As-of queries apply one `(valid-time, knowledge-time)` pair to each plane. Missing on one plane is `unknown`, not copied. `onBehalfOf` does not create 005 employment. 006 standing does not create employment with sponsors. Ending 005 employment may trigger review of open assignments/memberships/grants; it does not auto-rewrite them.

**Migration relations.**

- 003 nested membership-assignment → rename TeamAssignment. Fields stay on 003.
- Admission / standing / terms jammed into that nested record → optional 006 reference.
- Collective *is* the 003 instance; it does not copy members from 003 or 006.
- Do not treat WM-ORG-016 as the team roster unless an assignment is explicitly work assigned *to the team as a body of work*; 016 remains that master and 003 holds a team-side index.
- No new IDs for TeamAssignment, Collective, CommunityOfPractice, WorkingAgreement or TechnicalDomain.

**Publication blockers.** Both bases are non-canonical reviewable drafts. 006 has no independent external review and an empty relation ledger — community-profile reuse is therefore a hold, not a closed composition. 003 still names the nested record “membership assignment,” which collides with 006 until the TeamAssignment rename lands. No executable fixtures for: assignment-only temp team; CoP requiring 006; inter-company cardinalities (0..1 / 1..n / 0..n / exactly 1); independently dated 005 / assignment / 006 / grant planes; CoP roster that must not mint product ACLs. Alignments to W3C ORG, FHIR CareTeam and SCIM Group are alignments only. Do not invent Vercy identifiers.