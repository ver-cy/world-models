# Grok independent study — EM-RSK-03

## Verdict
Conditionally accept the proposed direction as a boundary plan for EM-RSK-03. Do not accept it as a completed mapping, installable closure, or canonical model set. The card is queued; research brief pending. No identifiers minted.

## Duplicate / account boundary
WM-PER-002 (“Digital Identity / Account”, 0.2.0-legacy) resolves to R4 Identity Register: subject anchor (`identityRecord`, identifier/key bindings, assurance, linkage), not subscriber/login account. WM-XCT-016 is published Identity Register 0.3.0-research.1 reviewable draft with same anchoring purpose, not account model. Retiring duplicate pointer WM-PER-002 into WM-XCT-016 justified if registry owner confirms alias. Collapse does not produce DigitalAccount.

DigitalAccount distinct from Person WM-PER-001, identity register, CRM Customer/Account Relationship WM-ORG-014. WM-XCT-011 excludes subscriber-account creation, authenticator binding, authorization decisions. WM-VRT-005 exists as unversioned Online Account stub whose one-liner states account in service/virtual environment distinct from federated identity. Profiling as Digital Account is right direction; complete account spec not shown.

## Role / grant / delegation
Keep one identifier-unassigned Authorization Domain / Access Grant candidate cluster, not one proven type. Domain is policy/namespace; Grant is issued entitlement instance. Keep distinct:
- AccessRole reusable template, not org position.
- Assignment role-to-account binding, usually conditioned on work/org assignment.
- PermissionGrant issued entitlement with explicit justifications.
- Attenuated delegated grant derived child subset of parent on actions, objects, purpose, time, attributes.
Widening is a new root grant. Parent revocation cascades to descendants; child revocation does not revoke parent or separately justified siblings. Depth, expiry, sub-delegation explicit.
Reuse WM-XCT-001 only for holder/steward authority and scoped control mandates. It defers runtime authorization and must not host IAM grant catalogue.

## Consent
Reuse WM-XCT-002 only for consent/read-disclosure instruments. Purpose is permission-to-read. Write/action grants, enforcement, secrets, multi-hop delegation out of scope. Consent is justification input that can independently keep a grant alive after assignment drops; not role, assignment, grant.

## Review / revocation
Profile WM-ACT-034 as Access Review activity: subject account plus grant/assignment set; criteria still-justified/least-privilege/separation of duties; outputs retain/revoke/recertify/escalate. Live WM-ACT-034 generic and does not mention recertification. Must not become grant, role or credential. Reviewer delegation is governance correction, not access delegation. WM-XCT-004/007 conceptual neighbors for audit and enforcement but legacy stubs.
Revocation paths distinct: assignment drop; review decision; consent/instrument withdrawal; parent delegated grant revoke; credential-status revoke (adjacent, not grant revoke).

## Credential metadata
Keep as account/anchor component: type, issuer, validity, assurance, status, key identifier, binding, protected reference only. Secret material never in account, grant, review, metadata, projection.
Independent credential subject already exists outside card: R4 keyBinding on anchor; WM-XCT-017 Attestation/Credential issued-claim identity, validity, status, revocation without secret. Not same as account authenticator metadata. Do not create new Credential inside EM-RSK-03 and do not merge R4 keyBinding, account authenticator metadata, WM-XCT-017. Authenticator issuance/secret store unresolved adjacent boundary.

## Invariants
1. IAM role not position; manager post must not auto-grant HR data.
2. Delegation does not extend original right; child subset parent.
3. Only metadata/protected reference stored; credential values absent.
4. Register != Account != Role != Assignment != Grant != Review != Credential metadata != Secret.
5. WM-XCT-002 is justification input, not operational grant.
6. Grants explicit justifications; assignment change drops only grants whose sole remaining justification is that assignment.
7. Review, revocation, assignment change, projection operate on grant+justification+status metadata only.
8. Reviewer mandate != access mandate.
9. Unassigned Authorization Domain / Access Grant object remains candidate cluster, not one proven type.

## Scenario
Account Acc bound to Person P, not equated. Role R1 assigned via employment Assignment A. Grant G1 justified only by A. G2 justified by A and independent consent C and/or Role R2. Delegated child D of G1 attenuated. Credential metadata M on Acc points to protected secret ref. A removed. Access Review runs. Projection produced.
Then G1 revoked; D falls; G2 retained. Review records retain/revoke against grants; reviewer delegation creates no access. M unchanged except public status fields. Projection metadata/protected ref only. Audit records justification drop/review outcome, never secret.

## Blockers
WM-VRT-005 and WM-XCT-004/007 lack usable specs. WM-ACT-034 has no Access Review profile. Domain vs Role vs Assignment vs Grant vs delegated grant unresolved inside unassigned cluster. Credential Metadata vs R4 keyBinding vs WM-XCT-017 adjacent split not closed. Semantic crosswalk, mastership, fixtures required. No canonical completeness claim.
