# EM-ORG-05 local synthesis

## Disposition

- Profile WM-ORG-003 for single-organization teams, inter-company teams and communities of practice.
- Reuse WM-ORG-006 as the master of governed membership relationships.
- Rename WM-ORG-003's nested membership record to `TeamAssignment`; it remains a team-scoped staffing/participation fact.
- Create no new model ID for Collective, CommunityOfPractice, WorkingAgreement or TechnicalDomain.

## Roots and mastership

WM-ORG-003 owns collective identity, mission/charter, lifecycle and team assignments. WM-ORG-006 owns admission-based belonging with scheme, decision, standing, validity, terms, role binding and evidence. Assignment ends with the team context; membership can outlive an assignment. A person may hold one membership and one assignment concurrently, linked but never merged.

Employment, post occupancy, project participation, subscriptions and access grants remain external. Participant records are references rather than copied person data.

## Inter-company and community profiles

The base's exactly-one containing organization is unsuitable for peer-sponsored collectives. The collaboration profile uses optional containment, one or more sponsors, zero or more managing organizations and exactly one record-authority organization. Sponsorship, management, obligation-bearing and record authority are distinct roles.

A CommunityOfPractice is a standing collaboration whose participants have WM-ORG-006 memberships. It has no delivery mandate or mandatory capacity allocation. Temporary delivery teams use TeamAssignments and may have no membership relationship.

WorkingAgreement is an owned charter component when specific to the collective. Reusable templates and multi-party binding instruments are referenced. TechnicalDomain is a scheme-qualified classifier; the community that stewards a domain carries governance and lifecycle.

## Invariants

1. Membership requires identity, parties, scheme/type, admission basis, validity, standing, role and provenance.
2. Assignment and membership are separate facts and lifecycles.
3. Neither membership nor assignment grants employment, funding, product access or authority.
4. Exactly one record authority exists per collective; containment is optional for collaborations.
5. Participants are referenced once and may hold concurrent relationships.
6. Corrections append and preserve event versus knowledge time.
7. Entitlement inheritance cannot cross organization/authority boundaries.
8. Collective dissolution does not end employment, other memberships or external grants.
9. TechnicalDomain classifiers cannot own members or charters.

## Scenario result

A temporary team sponsored by two firms records one authority for the team record, both sponsors and participant assignments with employer references; no membership is invented. A permanent practice community records governed WM-ORG-006 memberships. The same person can participate in both. Ending the team changes neither community standing nor employment. Community membership grants no access to member firms' products; only explicit owner-issued grants can do that.

## Holds

Both bases are non-canonical. WM-ORG-003 contains a conflict between mandatory single containment and optional/multiple management. WM-ORG-006 lacks independent external review and approved relation rows. Employment separation and the assignment-to-membership reference need cross-model validation, and scenario fixtures are absent. This checkpoint is not an installable release.

## Provider reconciliation and frozen audit (2026-09-29T09:38:33.858004Z)

Claude and Grok confirm PROFILE/no-new-ID and assignment/membership separation. Grok added the four independent temporal planes and access non-inference. The frozen audit returned REVISE: zero-containment collaboration and sponsor/record-authority/obligation-bearer roles exceed current profile authority. Revision 3 converts them to explicit base gaps, restores complete temporal, authorization, identity and history rules, carries all eleven inherited holds, and binds 45 declarative fixtures to the two immutable base hashes. Inter-company and CommunityOfPractice composition remain publication-held and non-constructible on the frozen bases.
