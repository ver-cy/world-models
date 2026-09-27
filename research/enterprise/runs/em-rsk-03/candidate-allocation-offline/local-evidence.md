# EM-RSK-03 local synthesis

## Disposition

- Propose duplicate retirement of WM-PER-002 into WM-XCT-016 Identity Register: both reservations point to the same legacy R4 specification. Update the candidate WM-VRT-005 relation to reference WM-XCT-016.
- Complete/profile reserved WM-VRT-005 Online Account as Digital Account. Account and identity anchor remain distinct and are linked by an effective, assurance-qualified binding.
- Reuse WM-XCT-002 only for read/disclosure grants and consent. It explicitly excludes general write, modify, delete and IAM authorization.
- Add one identifier-unassigned **Authorization Domain / Access Grant** candidate containing Access Role, Role Assignment, Permission Grant and attenuated delegated-grant records under one IAM master.
- Profile WM-ACT-034 for Access Review; reuse WM-XCT-001 for source delegation authority, WM-XCT-004 for audit and WM-XCT-007 for breach/enforcement.
- Keep Credential Metadata as an account/identity-anchor component for now; no separate model boundary is justified until cross-account or external credential mastership is demonstrated.

Subject, identity anchor, account and principal reference are separate. One person may have several accounts; service and machine accounts may have no person binding. An account-to-anchor binding records validity and assurance and never asserts equality. Organizational position may condition a grant but never creates an IAM role assignment or grant automatically.

Authorization Domain owns reusable access roles, time-bounded role assignments and effective permission grants. A permission grant binds principal, actions, resource scope, conditions, basis, justification and validity. Delegation references the source grant and may only narrow actions, scope and validity while preserving or strengthening conditions; it cannot outlive or survive revocation of its source.

Consent is a possible legal or governance basis for a disclosure grant. Consent does not create an IAM capability, and an IAM grant does not establish consent. Withdrawal makes the conditioned grant unevaluable or unsatisfied according to policy while preserving history.

Credential Metadata stores type, purpose, validity, public fingerprint where safe, protected vault/HSM reference, rotation/revocation time and evidence reference. Secret values and reversible digests never enter the registry or projections. Revocation is proven by an authoritative state transition and audit/evidence reference.

## Invariants

1. Person, identity anchor, account and principal are linked, never equated.
2. IAM role is not an organizational role or position.
3. Every grant has explicit authority basis, justification, scope, actions, conditions and validity.
4. Delegated rights are a subset of source rights and validity and cannot outlive the source grant.
5. Secret values and reversible representations are prohibited in all registry records and projections.
6. Consent and authorization remain separate instruments.
7. Access-review conclusions do not revoke access until an effective grant transition is recorded.
8. Revocation propagation may be partial; partial is a first-class non-success state.
9. Cached sessions/tokens cannot remain valid beyond their supporting grant.
10. All decisions, exercises, rotations and revocations correlate to append-only audit evidence.

## Scenario result

When a worker leaves an HR-manager assignment, grants explicitly conditioned on that assignment become unsatisfied and are revoked effective at the assignment change; derived delegations are also cut off. Separately justified incident-response or consent-conditioned grants are reviewed and may remain. Credentials scoped only to revoked grants are revoked or rotated through metadata transitions and vault-event evidence. No secret appears in any projection.

## Holds

The duplicate-retirement and relation rewrite are proposals only. WM-VRT-005 has no current specification. WM-XCT-002 is non-canonical and limited to read/disclosure. The Authorization candidate lacks registry allocation; delegation attenuation, review crosswalk, credential ownership and propagation fixtures are unverified. No runtime or installability claim is made.
