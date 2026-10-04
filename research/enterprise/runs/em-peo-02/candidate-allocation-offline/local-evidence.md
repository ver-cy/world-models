# EM-PEO-02 local synthesis

## Disposition

- Reuse WM-PER-001 as the person anchor.
- Profile WM-ORG-005 for employment, contractor and agency engagement relationships.
- Reuse WM-ORG-016 for position/work assignments.
- Add EmployeeProfile as a new model candidate with identifier unassigned.
- Keep JoinerMoverLeaverCase in the process/case contour; lifecycle events remain owned by their source aggregates.

EmployeeProfile is employer-scoped, one per worker/employer, and may span several employment relationships and rehires. It carries the employer's employee number, person reference and multiple employment references. The number is unique only within employer, scheme and validity and is never a person identifier or cross-employer key.

Employer, work customer and staffing supplier are distinct roles. Agency labor uses the agency as employer and the host as work customer. Contractor status is an asserted basis with external contract reference; category labels never settle legal status.

New employment is required for a new employing party, basis change, rehire after separation or parallel distinct contract. New assignment is required for post, host, scope or authority change. Effective-dated amendment handles FTE, pattern, location or reporting changes; record version only corrects recorded error.

## Invariants

1. Person identity survives employer change.
2. Employee number is employer/scheme/validity scoped.
3. EmployeeProfile existence never proves employment status.
4. Status and determinations are jurisdiction- and purpose-qualified.
5. Every assignment resolves to one engagement context.
6. Separation records basis and effective time and preserves history.
7. Offboarding creates access-verification obligations; HR closure or JML-case closure never proves revocation.
8. Terminated relationships remain resolvable.

Dual employment produces two employments and profiles. Agency work separates employer and host. Rehire reuses the profile but creates a new employment. Incomplete offboarding remains visible with unconfirmed entitlement outcomes.

## Holds

All bases are non-canonical; WM-ORG-005 lacks independent external review; composition relations remain candidate; EmployeeProfile lacks allocation; JML/access fixtures and Employment/Membership split validation are absent.
