## Verdict

**ACCEPT WITH LIMITS.** The limits below are blocking for publication, not advisory. Disposition PROFILE and `newRuntimeId=false` hold on this packet.

## Critical findings

1. **Constraint 19 is over-broad.** "Expiry of one never mutates the others" is stated absolutely, yet constraint 7 admits revocation and invalidation as distinct effects. Invalidation is commonly retroactive: it removes the right basis *ab initio*, which does bear on a grant whose scope references that right. As written, 19 would force a grant to be reported as unaffected by the destruction of its own basis. Must be narrowed to expiry, lapse and renewal; invalidation/revocation propagation is a hold.
2. **Right-lapse effect on live grant scope is unspecified.** The independence axioms cover grant→registration but not registration→grant. A grant referencing an "exact right set" can outlive a member of that set with no stated consequence.
3. **Two dangling subject references.** Sign and invention have no named subject authority (acknowledged), and *brand* appears in fixture `two-territorial-registrations` with no base, no master and no typed relation beyond "association". The IPAsset view requires "exactly one protected subject"; for the scenario's sign, that reference resolves to nothing. This is the highest-risk path to an implicit root: any local sign or brand key created to make the view resolvable would be a hidden identifier.
4. **Identifying keys split from mastership.** Application identity (office + number) and registration identity (register + number + territory) are constituted from values the profile assigns to WM-REC-001. Mastership of the identifying tuple is therefore ambiguous between WM-KNW-003 and WM-REC-001.
5. **Sublicence assumes a separate instrument.** "Sublicense is another UsageGrant" plus contract-only addressability fails for sublicences issued under the parent contract without their own instrument.

## Required holds

- WM-KNW-003 and WM-MED-001 specifications (carried; missing, not contradictory).
- Subject authority for sign and invention; brand as a typed concept with a named master.
- Retroactivity semantics for invalidation and revocation, and their effect on grants and sublicences.
- Effect of right lapse or expiry on an unexpired grant's scope.
- Register/territory code lists and versions; unregistered-rights paths.
- Standalone UsageGrant identity, reopened only on evidence of instrument-independent grants — now including intra-contract sublicences.

## Scenario result

Passes as stated. Grant expired; both registrations governed by their own states with independent expiries; surviving reporting, audit and confidentiality duties active as WM-XCT-029 on the spent contract without extending grant status; IPAsset view = one subject + two rights, non-authoritative, unkeyed. No worldwide exclusivity inferred from logo or from either single registration. The pass depends on the sign being resolvable upstream; on this packet it is not, so the scenario passes under the sign-authority hold rather than on evidence.

## Identifier decision

No new root, model or runtime identifier is allocated or implied. Office/application numbers, register/registration numbers and any portfolio number remain external read-only references and must never serve as the profile's own primary key. IPAsset stays unkeyed, non-assignable and non-licensable.
