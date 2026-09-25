# Independent boundary review — EM-ORG-05 vs WM-ORG-003 / WM-ORG-006

## Verdict per model/type

| Candidate type | Verdict |
|---|---|
| Team | **PROFILE** of WM-ORG-003 (two profiles: single-org unit; inter-company collaboration) |
| Temporary inter-company team | **PROFILE** of WM-ORG-003 — blocked until the containing-organization cardinality conflict below is resolved |
| Collective | **REUSE ONLY** — no independent identity or lifecycle is shown; it is an abstraction over WM-ORG-003 `boundary_class` + `permanence`, not a model |
| CommunityOfPractice | **PROFILE** composing WM-ORG-003 (identity, charter, lifecycle) with WM-ORG-006 (participation). Independent identity/lifecycle is *not* proven on this dossier, so a new identifier is refused; escalation test stated below |
| Membership | **REUSE ONLY** WM-ORG-006, subject to its holds |
| WM-ORG-003 nested membership-assignment | **PROFILE / rename**, not a duplicate to retire — distinct identity and lifecycle (see Membership mastership) |
| WorkingAgreement | **REUSE ONLY** — owned charter component in WM-ORG-003, with external-instrument reference; no model |
| TechnicalDomain | **REUSE ONLY** — classifier; never a model (test below) |

## Evidence state

Both specs are `reviewable-draft`, `publishableCanonical: false`. WM-ORG-006 is single-provider (Codex) with Claude and Grok waived, so it carries no independent external review; its registry row is `described-previous-version` / `migration-boundary-review` and still points at the legacy O3 card that fused Employment with Membership. WM-ORG-003 is dual-provider but rests heavily on tier‑2 vendor documentation for exactly the accepted additions used here (nesting, IdP sync, entitlements). The `relationship_ledger` contains no WM-ORG-006 row at all and no WM-ORG-003↔WM-ORG-006 row, so every mapping below is a draft proposal, not an approved relation. Vercy candidate linkage is `conceptual-candidate` at index depth. Nothing here is canonical, approved or installable.

**Material spec conflict found inside WM-ORG-003:** `composition` and the `team-boundary-and-entity-distinction` finding require exactly one containing organization (cardinality 1, required), while the later accepted `containing-and-managing-organization` finding sets containing organization to 0..1 and managing organizations to 0..n. The frozen spec is internally inconsistent on its single most load-bearing edge.

## Root identities and lifecycle

Three distinct roots survive the test:

1. **Collective root (WM-ORG-003)** — identity from a master-system key or governed IRI; lifecycle `proposed → active → suspended → inactive`, plus `entered-in-error`, with formation/merge/split/transfer/dissolution events. Purpose and mandate are its own.
2. **Membership relationship root (WM-ORG-006)** — identity of one governed belonging under a named scheme; lifecycle proposed → pending → active → suspended → ended/rejected/revoked, with renewal, reinstatement, appeal and surviving history.
3. **Person/Worker and Employment roots** — external; referenced only.

Collective and CommunityOfPractice fail the independent-root test against WM-ORG-003: nothing in the dossier gives them an identity rule, a state machine or change events that WM-ORG-003 does not already carry. **Escalation test for a future CoP identifier:** it must survive the dissolution of every hosting organization, admit members with no collective-scoped assignment, and hold a lifecycle event class (e.g. charter succession across sponsors) that WM-ORG-003's event set cannot express. Until such evidence exists, no identifier may be minted.

## Membership mastership

WM-ORG-003's nested record and WM-ORG-006 are **not duplicates**, and the collision is in the *name*, not the referent.

- **Team assignment (WM-ORG-003, aggregate child):** staffing/participation. Carries in-team role, period, allocation, coverage, position and on-behalf-of. It has no meaning outside its team root, dies with the team, and grants no standing. It is not admitted, not suspended for discipline, not appealable, not attested.
- **Membership (WM-ORG-006, relationship root):** governed belonging. Carries scheme, admission basis and decision, standing, terms, renewal, appeal, attestation, provenance and bilateral assertions. It outlives any assignment and is referenced, never embedded.

Rule: rename the nested record to **team assignment** in profile; mastership of assignment stays with WM-ORG-003, mastership of scheme-governed membership stays with WM-ORG-006. Where a collective admits people under a scheme (community, association, panel), the admission fact **must** be a WM-ORG-006 record referenced by the collective — participants are never copied. Where staffing is by employment or contract with no scheme admission, no WM-ORG-006 record exists. A single person in a community who is also staffed on its working group has exactly one membership and one assignment, linked, not merged.

## Inter-company and community profile

Exactly-one containing organization does prevent an inter-company collective: no single formal organization contains a team drawn from peers, and forcing one misstates legal containment and obligation-bearing. The profile fix, consistent with the boundary note that already admits `org:OrganizationalCollaboration` as a `boundary_class`:

- `containing_organization_ref` → **0..1**, populated only when `boundary_class = organizational unit`.
- `sponsor_organization_ref` **1..n** and `managing_organization_ref` **0..n** for the collaboration profile, each with its own period and mandate instrument.
- `record_authority_org_ref` **exactly 1**, always — the single organization whose system of record writes the collective record. This preserves single record authority without asserting legal containment, and is the invariant that replaces the discarded one.
- Obligation bearer must be named separately; a collaboration bears none by itself.

CommunityOfPractice = collaboration profile with `permanence = standing`, admission via WM-ORG-006, no allocation or capacity floors, and no delivery mandate. The base spec's requirement of enumerated, identified members holds for both profiles; directory rules must materialise enumerated members.

## Working agreement and technical domain

**WorkingAgreement** is an owned, versioned component of the charter layer when it states this collective's own conduct and is approved with the charter (it maps to the non-normative v1 `working_agreement` field and sits under `charter_effective_period`). It becomes a **referenced** artifact in two cases: a reusable template owned elsewhere, and a multi-party inter-company agreement, which is an instrument and binds via `mandate_obligation_ref`. Inter-company profiles will normally have both: a referenced instrument plus an owned local agreement.

**TechnicalDomain test:** a domain is a governed practice subject only if something can be *admitted to it, suspended from it, or dissolve it*. A concept in a versioned scheme cannot. Therefore TechnicalDomain is always a scheme-qualified classifier (SKOS concept, ESCO/ISCO URI, or local scheme with version); governance, stewardship and lifecycle attach to the community that stewards the domain, which references the code. Never carry a steward, charter or members on the classifier.

## Invariants

1. Membership has identity, member ref, organization/group ref, scheme, type, admission basis, validity interval, standing, role binding and provenance; missing any one = not a membership.
2. No membership, assignment or participant list confers employment, funding, product access or authority. Entitlement is a separate grant with its own authority and validity.
3. Access decisions may read membership as input; membership never guarantees, and effective-member resolution output must not be used as an authorization grant.
4. Participants are referenced, never duplicated between a collective and a membership record.
5. Exactly one record-authority organization per collective; containment is optional and only for units.
6. Every assignment and membership separates event time from observation/knowledge time; corrections append, never overwrite.
7. A member may hold many memberships and many assignments concurrently; total assignment allocation is checked, membership count is not.
8. Entitlement inheritance follows only an explicit parent-child tree inside one record-authority domain; it never crosses organizations.
9. Ending an assignment does not end a membership; ending a membership does not end employment; dissolving a collective does not revoke members' other relationships.
10. A classifier cannot be admitted, suspended or dissolved.

## Scenario walkthrough

**Negative case.** A community member claims access to all products of other members' employers. Blocked at four points: membership is a belonging relationship whose benefits are external references (invariant 2/3); the community is a collaboration with no containing organization and therefore owns nothing belonging to member firms; entitlements in WM-ORG-003 are permissions the *collective* holds on named resources, not permissions members hold; and inheritance is tree-scoped inside one authority domain (invariant 8). The only conforming path is an explicit grant per product by each owning firm, with its own basis and validity. Any implementation that resolves the participant list into a grant is a conformance failure, not a configuration choice.

**Acceptance case.** Two firms (illustrative, unnamed) form a six-month joint team: `boundary_class = organizational collaboration`, `permanence = time-boxed`, sponsors = both firms, record authority = one firm, charter with an inter-company agreement referenced as the mandate instrument. Staffing is assignments with `on_behalf_of` naming each participant's employer, allocation fractions, and no scheme admission — no WM-ORG-006 records are created. Employment stays with each employer and is untouched by dissolution; at dissolution, assignments close and each firm revokes its own grants on its own clock. In parallel, a permanent practice community: standing, sponsor-hosted, admission per scheme, each participant holding one WM-ORG-006 membership with standing and validity; two of them are also on the joint team, so they hold one membership plus one assignment each, independently dated. Changing standing in the community changes nothing on the team; ending the team changes nothing in the community; neither changes employment or any grant.

## Migration/profile shape

- Profile A: WM-ORG-003 single-organization unit (base, unchanged).
- Profile B: WM-ORG-003 inter-company collaboration — sponsor/managing/record-authority cardinalities as above; capacity and qualification optional.
- Profile C: CommunityOfPractice — Profile B plus mandatory WM-ORG-006 reference for every participant; assignment records prohibited except within working groups.
- Rename the nested child to team assignment; add a prohibition on scheme, admission basis and standing fields appearing on it.
- Map v1 `ORG-06` fields (team_kind → category; mission → purpose; working_agreement → charter component; active_period → charter/validity) and `PEO-11` fields (membership_kind → scheme type; valid_period → validity; role_ref → role binding; admission_basis → admission basis) onto WM-ORG-006, all candidate-not-normative.
- Draft relation rows required before any of this is usable: WM-ORG-003 → WM-ORG-006 REFERENCE, and WM-ORG-006 → Agent/Organization/Access/Evidence.

## Gaps and publication holds

Carry forward every existing hold on both specs. Add: (1) the containing-organization cardinality contradiction inside WM-ORG-003 must be adjudicated before any collaboration profile is written; (2) WM-ORG-006 has no approved relation rows, so the assignment↔membership link is unproven; (3) WM-ORG-006 lacks independent review and still shadows the fused O3 employment/membership card — the Employment boundary must be confirmed against its own model, which is not in this dossier; (4) no fixtures exist for dual-held membership-plus-assignment, inter-company dissolution, or the negative access case; (5) Collective and CommunityOfPractice have no source-grounded evidence pack in this dossier at all, so their profile verdicts rest on WM-ORG-003 evidence only. No canonical status, approved relation or installability is claimed.
