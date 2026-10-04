# EM-ORG-06 Independent Review — Positions, Roles and Accountability

Independent boundary review of the live card *Positions, Roles and Responsibility* (EM-ORG-06), using the brief’s Accountability language without renaming the contour. WM-ORG-004 and WM-XCT-023 are non-canonical reviewable drafts. No Vercy identifier is invented. Standards evidence and design inference are labeled.

## Verdicts per type

| Type | Verdict |
|---|---|
| Position — reuse WM-ORG-004 | **Accept with holds** |
| PartyRole profile of WM-XCT-023 for Accountability, held Decision Rights, RACI | **Accept with holds** |
| BusinessRole as versioned concept scheme | **Defer** — identifier unassigned |
| HeadcountPlan | **Defer** as a separate planning candidate — identifier unassigned |
| Accountability / DecisionRight / RaciAssignment as sibling entities | **Reject** — constrain as profiles of WM-XCT-023 |

## Position / occupancy boundary

**Evidence.** W3C ORG REC: `org:Post` “exists independently of the person or persons filling it”; vacant posts are first-class; posts may report to posts. `org:Membership` “does not exist unless there is an Agent.” UK Civil Service position management treats a position as an ERP “chair” that may be vacant under pre-approved budget. US OPM practice classifies the position, not the occupant; 5 CFR 330 treats a vacancy as a vacant *position* the agency is recruiting against. Position-control HRIS practice (Oracle HCM and peers) keeps the position as the budgetary planning unit whether filled or vacant. WM-ORG-004 already models durable seat identity, unit placement, job/grade refs, authorized FTE/headcount, single vs pooled type, overlap/max holders, budgeted amount/period, funding source, and seat-level authority. Vacancy state is derived (vacant / partly filled / fully filled / over-established). Occupants are not stored on the seat. WM-ORG-016 is the time-bounded binding that consumes FTE. EM-PEO-04 Vacancy is a recruitment instrument whose owners for person, position, budget and employment are external.

**Inference.** Reuse WM-ORG-004 for the durable vacant-capable seat. Occupancy stays external on WM-ORG-016; Employment (WM-ORG-005 / EM-PEO-02) is the legal relationship and does not own the seat. Four layers must not collapse: Job/class template ≠ Position/seat ≠ Occupancy/assignment ≠ BusinessRole concept. Two vacancy senses must not collapse: derived seat state on WM-ORG-004 versus the EM-PEO-04 recruitment Vacancy. EM-ORG-06 owns only the derivation rule and points the recruitment object out.

## Role concept / assertion boundary

**Evidence.** ORG separates `org:Role` (abstract concept) from `org:Membership` / `org:holds` (assertion). WM-XCT-023 is a mixin: a reified n-ary assertion joining player, host, role type and validity, with scope, authority basis, constraints and provenance. Players include parties *and* unfilled posts. Standing assignment is not activity-instance participation. NIST NICE: a work role is a grouping of work, not a job title or occupation.

**Inference.** BusinessRole is the versioned concept scheme (`org:Role` analogue). Leave its identifier unassigned; do not silently fold it into WM-XCT-023. PartyRole is the assertion. A Position may be the player so a vacant seat can carry Accountable/Responsible without an occupant. One party may hold many PartyRole assertions against many hosts.

## Accountability / RACI rules

**Evidence.** COBIT: exactly one Accountable per practice, at least one Responsible; A-without-R is a failure mode. ISO/IEC 38500: responsibility requires clear roles and decision rights matched to competence. COSO IC Principles 3 and 5 plus SoD as a control activity; compensating controls when SoD is infeasible. ISO/IEC 27001 A.5.3: SoD exceptions must be explicit. The live card already requires RACI to pin subject, role, period and permitted conflicts. WM-XCT-023 already carries incompatible-role pairs, static vs dynamic exclusion, and time-limited exceptions.

**Inference.** RACI, Accountability and held Decision Rights are constrained profiles of WM-XCT-023, not new types. Each RACI assertion pins host, role concept, player (party or position), period and conflict policy. “One Accountable and at least one Responsible per host/period” is a *profile invariant*, not a core PartyRole axiom — the mixin is general-purpose. SoD exceptions are explicit, scoped, temporary, and require a compensating control. Three-way authority must stay split: seat-level authority on Position; held Decision Rights as a PartyRole profile; assignment-time conveyance on WM-ORG-016.

## IAM distinction

**Evidence.** INCITS 359 RBAC and NIST SP 800-162 ABAC are enforcement models (users, roles, permissions, sessions, request-time attributes). Enterprise RBAC practice separates business roles from technical/IT roles; technical roles should not be assigned directly as the business concept. The live card invariant is “a business role is not an access role.” WM-XCT-023 holds NIST 800-162 as deferred research.

**Inference.** BusinessRole and PartyRole may be policy *input* to IAM. They must not mint grants, entitlements, sessions or permissions. Enforcement remains outside EM-ORG-06.

## Headcount-plan test

**Evidence.** ISO 30409:2016 (confirmed 2022) is a planning *process* (current workforce → demand → supply → gap → actions), not a HeadcountPlan entity and not an FTE formula. Industry practice distinguishes authorized headcount from funded headcount. WM-ORG-004 capacity/funding is an authorization on the seat. WM-ORG-002 treats a staffing snapshot as a measurement event, not a plan; it already holds that unit-grain authorized complement is local control. WM-ORG-016 declares FTE metrics ungrounded. WM-ECO-012 treats workforce as a budget assumption driver, not as owner of position funding.

**Inference.** Keep HeadcountPlan a separate planning candidate with identifier unassigned. Position FTE/budget are projections from an *approved* plan, not the plan itself. Four layers: Plan (intent) ≠ Seat authorization ≠ Occupancy ≠ Measurement snapshot.

## Scenario results

1. Occupant change preserves Position — **Pass** (ORG Post, Civil Service chair, WM-ORG-004 identity).
2. Vacant seat remains valid; vacancy derived — **Pass**.
3. One person holds two roles — **Pass** (two PartyRole assertions over BusinessRole concepts; not 1:1 with Position).
4. Two 0.5 FTE assignments fill one allowed pooled seat — **Pass** iff type=pooled, overlap allowed, and consumed FTE ≤ authorized FTE; otherwise over-established.
5. Deleting an employee deletes the seat and budget — **Correctly rejected** (negative case). Deletion ends the assignment; seat identity, authorized capacity and budget remain.

## Required relations

- Position —placed-in→ OrganizationalUnit (WM-ORG-002)
- Position —classified-by→ Job/grade (external scheme)
- Position —authorized-capacity/funding-from→ approved HeadcountPlan / Budget (references only; plan id unassigned)
- WorkAssignment —occupies→ Position and consumes FTE (WM-ORG-016)
- PartyRole —player→ Party **or** Position; —host→ subject; —roleConcept→ BusinessRole scheme (id unassigned)
- RACI / Accountability / DecisionRight = constrained profiles of WM-XCT-023
- PartyRole —policy-input-to→ external IAM (no grants)
- Employment —references→ Position; does not own it (WM-ORG-005)
- EM-PEO-04 Vacancy —refers-to→ Position; does not replace derived vacancy

## Publication blockers

1. WM-ORG-004 and WM-XCT-023 remain reviewable drafts; EM-ORG-06 cannot claim canonical reuse.
2. BusinessRole and HeadcountPlan identifiers stay unassigned — do not invent.
3. Occupancy and assignment-time authority must stay on WM-ORG-016; absorbing them into Position or PartyRole fails the vacant-seat and occupant-change tests.
4. Derived vacancy (WM-ORG-004) and recruitment Vacancy (EM-PEO-04) must be named as distinct objects.
5. Seat-level authority, held Decision Rights, and assignment-time conveyance must not collapse.
6. “One A and ≥1 R” is a RACI-profile invariant, not a PartyRole core axiom; SoD exception lifecycle must be specified in the profile, not left as deferred research.
7. Inherited source/coverage holds travel with reuse: ISO 30400 paywall, 5 CFR/eCFR re-verification, FHIR PractitionerRole occupancy lean (align, do not equate), ISO 20022 BusinessRole / FIBO PartyInRole / NIST 800-162 deferred, job-share fractions source-weak, unit-grain establishment as local control.
8. Position funding is an authorization record, not a WM-ECO-012 budget line and not a plan.