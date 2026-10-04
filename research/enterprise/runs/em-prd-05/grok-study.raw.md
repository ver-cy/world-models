# Verdict

**ACCEPT WITH CONDITIONS.** None of IPAsset, IPRegistration, RightsClaim, or UsageGrant needs independent identity. IPAsset is a non-authoritative view of one protected subject plus its right set. IPRegistration and RightsClaim profile WM-KNW-003; registration also uses WM-REC-001. UsageGrant profiles and extends WM-ECO-006 and WM-XCT-029. Conditions: keep work/sign/invention, right, application, territorial registration, ownership claim, creator attribution, assignment and license separate; application is not grant; registration is per territory and register; license scope is declared; brand association is not trademark registration; rights claims are dated and sourced; a company logo does not imply worldwide exclusive rights.

## Strongest evidence

The required test is inexpressible if asset, registration, grant and obligation collapse. After the license ends, both territorial registrations remain live, surviving obligations persist on the spent contract, and the view still shows the sign plus two rights without treating the grant as a right.

## Strongest counterexample

Inferring one worldwide exclusive IPAsset, or worldwide exclusive rights, from a company logo or from a single territorial registration.

## Identity / mastership

Explicit decision: no candidate needs independent identity. IPAsset must not receive a durable key and is not a system of record. IPRegistration is a profile of WM-KNW-003 plus WM-REC-001; any registration number lives on the record. RightsClaim is a dated, sourced profile of WM-KNW-003 and does not mint a right. UsageGrant is not a free-floating grant master: the test case is a license with surviving obligations, which is contract plus obligation. Instrument-independent grants are not proven. Mastership stays on party masters, subject matter, WM-KNW-003, WM-REC-001, WM-ECO-006 and WM-XCT-029.

## Subject / right

Work (WM-MED-001), sign and invention are subjects and persist when rights lapse. WM-KNW-003 is the right. IPAsset = one subject ∪ 0..n rights. One subject may carry many rights; one right has one primary subject. Creator attribution attaches to the subject, not to the right or the registration. Sign and invention have no named subject master in the given list; that is a coverage gap, not a reason to promote IPAsset.

## Application / registration

Application is a request to a register. It is not a grant, not a license and not a registration. Treat it as a filing or pre-grant state of WM-KNW-003 plus WM-REC-001; do not add a type. Registration is per territory and per register. One sign in two territories is two registration profiles of two rights, each with its own record and status. Application to registration is 1:0..n.

## Ownership / claim

Keep four facts distinct: creator attribution on the subject; ownership claim over a right; assignment as a conveyance that changes holder; RightsClaim as a dated, sourced assertion. A claim is not title. Party masters identify creators, claimants, owners, registrants, licensors and licensees. Do not infer owner from registrant listing or from logo use.

## Usage grant

UsageGrant profiles WM-ECO-006 and WM-XCT-029. Scope must declare exclusivity slice, field, channel, territory, term, acts, sublicensing authority and survival (present or explicitly unbounded). Application is not grant. Grant expiry does not expire registrations or the subject. Surviving obligations remain WM-XCT-029 on the spent contract and do not extend grant status.

## Territory / time / status

Time axes are independent: subject creation, application, registration, claim date, grant term, obligation survival. Status is local to each registration and each grant. One territory does not project onto another. Grant term does not project onto registration term. Brand association has no territorial right-scope.

## Brand / trademark

Three layers: sign as subject; brand association as a party-to-sign fact with no register, term, exclusivity or territory; trademark registration as an IPRegistration profile, one territory, one register. Logo presence is association only. Worldwide logo use does not create worldwide or exclusive rights.

## Assignment / sublicense / obligations

Assignment (WM-ECO-006) conveys the ownership-claim holder on a specified right; it is not a license or a registration. Sublicense is a further UsageGrant, only if the parent states authority, and cannot exceed parent scope on any axis. Surviving obligations stay bound to the spent instrument and receive no new identity. Do not use IPAsset as the assignable or licensable object.

## Scenario

Sign S. Party P associated with S as house mark — association only. Reg-T1: S in T1, register X, registered through D1. Reg-T2: S in T2, register Y, registered through D2. License L on contract C expires D0, with D0 < D1 and D0 < D2; scope explicit; survival set {O}. After D0: L expired; both registrations remain registered; {O} persist as WM-XCT-029 on C; IPAsset view of S = S + {Reg-T1, Reg-T2}. Rejected inferences: logo ⇒ worldwide exclusive rights; one registration ⇒ the other territory; grant term ⇒ registration term; association ⇒ ownership claim.

## Invariants

1. No candidate receives a new identity key.
2. IPAsset is not system of record for subject, right, claim or grant.
3. Subject is not the right; one subject may have many rights.
4. Application is not grant and not registration.
5. Each registration is exactly one territory and one register.
6. A RightsClaim is dated and sourced, or it is not a valid instance.
7. Creator attribution ≠ ownership claim ≠ registrant listing ≠ license.
8. License scope is incomplete unless exclusivity slice, field, channel, territory, term, acts, sublicense flag and survival are explicit or explicitly unbounded.
9. Grant expiry does not change registration status or subject identity.
10. Surviving obligations persist as WM-XCT-029 after grant term; they do not extend the grant.
11. Brand association is not trademark registration and implies no exclusive or worldwide right.
12. Two registrations of one sign never merge into one worldwide right.
13. Sublicense requires parent authority and cannot exceed parent scope.
14. Assignment does not mint a registration or grant; license does not mint an ownership claim.
15. Worldwide exclusive rights shall not be inferred from a company logo or from a single-territory registration.

## Minimum model set

Subject: WM-MED-001 for works; sign and invention as distinct subject kinds without new identifiers. Right: WM-KNW-003. Record: WM-REC-001. Contract: WM-ECO-006. Obligation: WM-XCT-029. Party masters. Views/profiles only: IPAsset, IPRegistration, RightsClaim, UsageGrant.

## Blockers

B1: if a later corpus shows grants with no instrument, reopen UsageGrant identity. B2: sign and invention lack a named subject master; flag the gap; do not invent identifiers; do not promote IPAsset to master. B3: exclusivity slice, field, channel and acts are grant-profile attributes, not new types. B4: an operational portfolio number on the view is an external reference, not a new master.
