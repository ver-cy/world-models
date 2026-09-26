# EM-PRD-05 local synthesis

## Disposition

- Create an Enterprise IP and usage-rights profile over legacy WM-KNW-003, WM-MED-001, WM-ECO-006, WM-XCT-029 and WM-REC-001.
- Treat **IP Asset** as a view combining protected subject matter with a managed set of rights; it is not a new identity.
- Reuse/profile WM-KNW-003 for **IP Registration** and **Rights Claim**.
- Treat **Usage Grant** as a profile/extension of WM-ECO-006 with permissions, prohibitions and duties bound through WM-XCT-029. Reconsider standalone identity only if grants independent of any instrument are evidenced.
- Allocate no new catalogue/runtime identifier.

## Identity and mastership

Protected work/sign/invention, legal right, application, territorial registration, rights claim, creator attribution, assignment instrument and usage grant remain separate. The subject matter is mastered by WM-MED-001 or another relevant domain model. WM-KNW-003 masters right/application/registration lifecycle. WM-REC-001 masters filing, certificate and recordal evidence. Parties remain WM-ORG-001/WM-PER-001.

A right-holder statement is a dated sourced claim, not an unquestioned fact. Registered holder, asserted beneficial owner and creator attribution remain distinct. Assignment changes ownership under its basis; license grants permission and does not transfer ownership.

## Application, registration and territory

Application identity is office plus application number and survives refusal. It seeks a right but is not the right. Priority attaches to the application. Registration is per register, number and territory. Grant, renewal, lapse, expiry, revocation and invalidation are distinct events with separate effects and times.

Right kind, territory and classes use versioned schemes. A right may arise without registration where the applicable basis permits it; lack of a registration is then not proof of no right.

## Usage grant

The grant names the licensed right set and exact scope: exclusive/sole/non-exclusive slice, field of use, channel, territory, term, volume limits, permitted/prohibited acts, sublicensing rule and parent grant where applicable. A sublicense cannot exceed its parent. Surviving obligations such as final reporting/payment, audit, confidentiality, sell-off, attribution and return/destruction remain WM-XCT-029 obligations after grant termination.

## Brand and trademark boundary

Brand is a commercial association. A trademark registration is a territorial legal record for a specific sign and classes. One brand may map to multiple signs, applications and registrations. Use of a logo is evidence of use, not proof of registration, ownership, exclusivity or worldwide scope.

## Acceptance result

One brand references one sign and two territorial registrations. A non-exclusive license covers both territories but expires in 2027; registrations expire in 2029 and 2032. In 2028 the grant is terminated while both registrations remain live and surviving duties continue. In 2030 only one registration remains. All timelines are independently queryable and no status silently propagates across them.

## Required invariants

1. Right and protected subject matter have independent identities.
2. Application is not a granted right.
3. Registration is territory- and register-scoped.
4. Priority attaches to an application.
5. Creator attribution never proves ownership.
6. License never transfers ownership.
7. Sublicense never exceeds parent scope.
8. Exclusivity always names field, channel, territory and term.
9. Brand association never proves trademark registration.
10. Grant and registration lifecycles do not mutate each other.
11. Rights claims are dated and sourced.
12. Surviving obligations are explicit.

## Holds

WM-KNW-003 and WM-MED-001 lack current complete specifications and remain migration-boundary records. All adjacent specifications are non-canonical drafts. Field crosswalks, subject-matter boundary, code lists, unregistered rights, moral rights, collective management, work-for-hire, trade secrets and security interests remain unresolved. Usage Grant standalone status lacks sufficient evidence. No installable release or legal conclusion is claimed.
