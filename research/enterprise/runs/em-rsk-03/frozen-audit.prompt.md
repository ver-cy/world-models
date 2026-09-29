You are the single frozen no-tools semantic auditor for EM-RSK-03. Use only the frozen material below. Audit revision 2 for identity, independent lifecycle, mastership, identity-register/account/role/assignment/grant/review/credential/secret boundaries, delegation attenuation, justification and revocation behavior, stable rule IDs and concrete fixtures. Decide whether keeping one explicitly unresolved candidate cluster as an offline allocation artifact is honest and non-publishable, while not claiming it is one proven root. Confirm no identifier is allocated and no publication readiness is claimed. Return PASS or REVISE first, then one closed numbered defect checklist. Do not invent identifiers or another provider study.

===== provider-comparison.md =====
# EM-RSK-03 provider comparison

Claude and Grok agree on the principal boundaries: WM-PER-002 and WM-XCT-016 describe an identity-register anchor rather than a login account; WM-VRT-005 is the account direction; WM-XCT-002 is limited to consent and read/disclosure justification; WM-ACT-034 may host an Access Review profile; credential secrets never enter registry records or projections.

Grok conditionally accepts retirement of WM-PER-002 into WM-XCT-016 only after registry-owner alias confirmation, while Claude preferred scope-narrowing until that confirmation. The reconciled artifact therefore records a duplicate-retirement proposal, never an accomplished migration.

The providers also expose a live allocation boundary. Claude separates AccessRole and PermissionGrant as independent candidates; Grok calls the current Authorization Domain / Access Grant material a candidate cluster and explicitly says it is not one proven type. Revision 2 therefore preserves a single offline cluster solely for allocation research, models Domain, Role, Assignment, Grant and Delegation as distinct objects and lifecycles, and forbids any claim that the cluster is one allocated root. Registry allocation must resolve whether it splits before conversion.

Credential metadata remains an account component and references WM-XCT-017 only for issued attestation/credential identity. Authenticator issuance and secret storage remain external unresolved boundaries. No identifier, runtime binding or publication readiness is claimed.


===== claude-study.raw.md =====
# Independent Review — EM-RSK-03 over WM-PER-002 / WM-XCT-002

## Verdict

**Split decision. No single reuse; no duplicate-retirement.**

- **WM-PER-002 — reuse with profile, scope-narrowed.** It is the subject-identity anchor (`identityRecord`, `identifierBinding`, `keyBinding`, `assuranceAssessment`). It is *not* an account model, despite its reservation name. Recommended action: retitle the reservation to drop "/ Account" and keep the anchor scope; this is a naming defect, not a merge trigger.
- **WM-XCT-002 — reuse by reference, not adoption.** It owns the consent/disclosure grant instrument for *read/disclosure* only, by its own `out_of_scope` ("Write, modify, delete and licensing… the normative core is read/disclosure"). It cannot carry IAM authorization.
- **WM-VRT-005 Online Account — profile.** Existing `KEEP-BOTH` flag and `REFERENCE → WM-PER-002` relation already encode the required account/identity split. DigitalAccount is a profile here, not a new type.
- **WM-XCT-001 — reuse for delegation mastership.** Its purpose states "transfers, delegation, guardianship"; WM-XCT-002 verifies authority *against* it. Delegation is mastered there; EM-RSK-03 profiles attenuation rules.
- **WM-ACT-034 Assessment/Evaluation — profile for AccessReview** (subject, criteria, evidence, conclusion maps directly).
- **WM-XCT-004 — reuse (audit); WM-XCT-007 — reuse (enforcement/breach).**
- **Identifier-unassigned candidates (three):** AccessRole, PermissionGrant, CredentialMetadata. No reservation in the dossier owns IAM role, non-read permission grant, or account-scoped secret metadata. Do not mint identifiers in this review.

## Evidence

Both target reservations are `described-previous-version` / `migration-boundary-review`, `conceptual-candidate`, `evidence_depth: index-and-publication-metadata`, `priority_confidence: low`. WM-XCT-002 is `published` but `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, with five open publication holds. WM-PER-002 is legacy markdown v0.2.0 with validation flag "не регистр, а субъект". All v1 fields (`principal_kind`, `resource_scope`, `permission`, `expiry_at`) are `candidate-not-normative`. No crosswalk has been executed; every mapping below is a boundary proposal requiring semantic crosswalk before adoption.

## Identity/account boundary

Four separated layers:

1. **Subject** (Person/Organization/Thing) — external, referenced.
2. **Identity anchor** — WM-PER-002; asserts existence and same-subject continuity, "deliberately says as little else as possible"; `REFERENCE world.person (H1)`, never inlines.
3. **Account** — WM-VRT-005; a credential-bearing principal within one service, mastered by the platform operator. Many accounts per anchor; accounts may exist with no anchor (service/machine accounts) and anchors with no account.
4. **Principal reference on a grant** — `principal_kind` distinguishes account, anchor, role, or non-human agent.

Account↔anchor uses the existing `REFERENCE` relation with a binding record (`bound_at`, `binding_assurance`, `unbound_at`) — never an identity field on the account, and never equality. Person is never a grant principal directly; grants bind to accounts or roles.

## Role/grant/delegation

- **AccessRole** — a named bundle of permissions in an IAM authority domain. Mastered in IAM. It has no organizational semantics: no reports-to, no headcount, no employment effect. Assignment of a role to an account is a distinct, time-bounded record (`role_assignment`), separate from the role definition and from any HR position.
- **PermissionGrant** — the effective authorization: principal × action × `resource_scope` × conditions × validity. Distinct from role (definition) and from assignment (binding). Each grant carries a mandatory `justification_ref` and an `authority_basis_ref`.
- **Delegation** — mastered by WM-XCT-001; EM-RSK-03 records the attenuation envelope: `delegator_grant_ref`, `delegate_principal_ref`, `attenuation` (action set ⊆, scope ⊆, validity ⊆, conditions ⊇), `max_depth`, `revoked_at`. WM-XCT-002's deferred research explicitly records that multi-hop delegation chains "[have] no primary encoding in either pack" — attenuation must therefore be minted here as a profile invariant and flagged as unsourced.
- **Policy decision/enforcement** — decision surface semantics align to WM-XCT-002's `coverage-decision-exchange` and `fail-closed-handling` for consent-conditioned reads; enforcement/breach casework is WM-XCT-007. EM-RSK-03 retains only `decision_correlation_id`.

## Consent vs authorization

They are different instruments and must not collapse. Consent (WM-XCT-002) is a *basis* asserted by a grantor over their own data, with notice version, capture context, withdrawal method and receipt; its model itself states consent is "one possible basis of a grant, not a mandatory precondition". IAM authorization is an operator-side capability decision over resources. Composition rule: a PermissionGrant over personal data may carry `basis_ref → WM-XCT-002 instrument`; withdrawal there makes the grant's condition unsatisfied, not the grant malformed. An IAM grant never substitutes for consent, and consent never creates an IAM capability.

## Access review/revocation

AccessReview profiles WM-ACT-034: campaign scope, criteria, reviewer (not the grant holder), per-grant decision (`affirm | revoke | modify`), evidence refs, conclusion time. Review decisions are inputs; the revocation event is on the grant. Revocation is event-sourced: `revoked_at`, `revocation_reason`, `effective_at`, plus downstream cutoff status — the same partial-propagation problem WM-XCT-002 models as `propagation_status` (partial is "a first-class state, not a success"). Cached tokens/sessions must expire no later than grant validity. All review, decision and revocation events log to WM-XCT-004.

## Credential metadata

Registry and all projections hold metadata only: `credential_kind`, `key_material_ref` (opaque locator into a vault/HSM), `purpose`, `valid_from`, `not_after`, `rotated_at`, `revoked_at`, `revocation_reason`, `attestation_ref`, `algorithm_id`, `public_fingerprint` where the credential type makes one non-secret. WM-PER-002 already demonstrates the pattern — `keyBinding{keyMaterialRef, purpose, validFrom, revokedAt}` and `keyRotated` — and covers anchor control keys; account-scoped credentials need the separate candidate. Rotation/revocation is proved by the state transition plus an evidence reference (attestation, vault event id, audit record), never by exposing or comparing values. No projection may derive a value, and no reversible digest of one may be stored.

## Invariants

1. Account ≠ Person ≠ identity anchor; binding only, never equality.
2. IAM role ≠ organizational position; a position may appear only as a grant *condition*, never as an implicit grant.
3. Delegation attenuates: action ⊆, scope ⊆, validity ⊆, conditions at least as strict; depth bounded; a delegation cannot outlive its source grant.
4. No secret values or reversible digests in registry or projections; only metadata and protected references.
5. Every grant carries a justification and an authority basis; unjustified grants are invalid, not merely flagged.
6. Consent withdrawal unsatisfies conditioned grants; it does not delete them or their history.
7. Fail-closed: unevaluable ≠ unsatisfied, and unevaluable must alert.
8. Revocation is effective-dated and propagated; partial propagation is a recorded non-success state.

## Scenario

Account A (bound to anchor P) moves from an HR-managing assignment to operations.

- Grants conditioned on the HR assignment (`condition: assignment_ref = HR-mgr`) become unsatisfied at `effective_at` of the assignment change; each emits a revocation event with reason `assignment-changed`, cascading to delegations issued from them.
- Grants with an independent `justification_ref` (e.g. a named incident-response grant, or a read conditioned on a live WM-XCT-002 consent instrument) are untouched; the review record must show each was evaluated and affirmed.
- Credentials: any key scoped to the revoked grants is marked `revoked_at` with an evidence ref; rotation proves out via metadata state change and vault event id.
- Projections return grant/credential *metadata* and outcomes only; no secret value appears, and the negative case (manager position auto-granting all HR data) is rejected by invariants 2 and 5.

## Minimal profile/candidate shape

`DigitalAccount` (profile of WM-VRT-005): account_id, operator_ref, status, anchor_binding_ref[0..1], binding_assurance, opened_at, closed_at.
`AccessRole` (candidate): role_id, authority_domain, permission_set[], scope_template, non_position_assertion.
`PermissionGrant` (candidate): grant_id, principal_ref, principal_kind, action[], resource_scope, condition[], basis_ref[0..1], justification_ref, valid_from, expiry_at, state, decision_correlation_id.
`Delegation` (profile of WM-XCT-001): as in Role/grant/delegation above.
`AccessReview` (profile of WM-ACT-034): review_id, campaign_ref, target_grant_ref, reviewer_ref, criteria_ref, decision, evidence_ref[], concluded_at.
`CredentialMetadata` (candidate): as in Credential metadata above.

## Holds

No canonical completeness or installability is claimed. Blocking before any publication claim: (a) execute the full semantic crosswalk for WM-PER-002 and WM-XCT-002; (b) resolve the WM-PER-002 name/scope mismatch and confirm mastership (IAM vs identity registrar vs platform operator) per type; (c) WM-XCT-002's five publication holds remain open and its security dimension is self-declared a gap — the credential/key owner must be named, not assumed; (d) delegation attenuation and multi-hop closure are unsourced in the dossier; (e) fixture checks and immutable refs are not run. Identifier assignment for the three candidates is deferred.


===== grok-study.raw.md =====
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


===== candidate-allocation-offline\allocation-candidate.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-RSK-03",
  "proposedName": "Authorization Domain / Access Grant",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "allocationBoundaryState": "unresolved-cluster",
  "decision": "NEW MODEL CANDIDATE CLUSTER",
  "canonicalPublishable": false,
  "candidateRevision": 2,
  "identityTest": {
    "stableIdentityRule": "EM-RSK-03.AD-04",
    "versionIdentityRule": "EM-RSK-03.AD-05",
    "mastership": "identity and access management authority, subject to registry boundary split",
    "independentLifecycle": [
      "draft",
      "approved",
      "active",
      "suspended",
      "expired",
      "revoked",
      "superseded"
    ],
    "stableIdentity": "Authorization domains, role definitions, assignments and grants remain separately identifiable across account changes, employment changes, access reviews and credential rotation.",
    "normativeRuleAuthority": "invariantRules"
  },
  "boundary": {
    "owns": [
      "candidate authorization-domain identity and policy namespace",
      "candidate reusable access-role definitions and immutable revisions",
      "candidate time-bounded role assignments",
      "candidate issued permission-grant identity and lifecycle",
      "candidate delegated-grant ancestry and attenuation",
      "revocation, expiry and propagation state"
    ],
    "references": [
      {
        "target": "WM-XCT-016",
        "purpose": "identity-register anchor"
      },
      {
        "target": "WM-VRT-005",
        "purpose": "digital account profile direction; usable specification absent"
      },
      {
        "target": "WM-XCT-002",
        "purpose": "consent or read/disclosure justification only"
      },
      {
        "target": "WM-XCT-001",
        "purpose": "holder/steward and scoped control mandate only"
      },
      {
        "target": "WM-ACT-034",
        "purpose": "Access Review activity profile"
      },
      {
        "target": "WM-XCT-004",
        "purpose": "append-only audit evidence; usable specification absent"
      },
      {
        "target": "WM-XCT-007",
        "purpose": "enforcement neighbor; usable specification absent"
      },
      {
        "target": "WM-XCT-017",
        "purpose": "issued credential or attestation identity, distinct from account authenticator metadata"
      }
    ],
    "excludes": [
      "person, identity-register or account identity",
      "organizational role or position mastership",
      "consent lifecycle and legal-basis determination",
      "review conclusion as automatic revocation",
      "credential secret values or reversible representations",
      "authenticator issuance and secret-store lifecycle",
      "security incident and enforcement lifecycle"
    ]
  },
  "objects": {
    "AuthorizationDomain": {
      "identity": [
        "authorizationDomainId"
      ],
      "required": [
        "ownerRef",
        "policyBoundaryRef",
        "status"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "active",
        "suspended",
        "retired",
        "superseded"
      ]
    },
    "AccessRole": {
      "identity": [
        "authorizationDomainId",
        "accessRoleId"
      ],
      "required": [
        "roleRevision",
        "actionSet",
        "resourceScope",
        "contentDigest",
        "status"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "active",
        "suspended",
        "retired",
        "superseded"
      ]
    },
    "RoleAssignment": {
      "identity": [
        "roleAssignmentId"
      ],
      "required": [
        "accountRef",
        "accessRoleRevisionRef",
        "justificationRefs",
        "validFrom",
        "status"
      ],
      "optional": [
        "validTo",
        "workAssignmentRef"
      ],
      "lifecycle": [
        "proposed",
        "active",
        "suspended",
        "expired",
        "revoked"
      ]
    },
    "PermissionGrant": {
      "identity": [
        "grantId"
      ],
      "required": [
        "principalRef",
        "actions",
        "resourceScope",
        "authorityBasisRef",
        "justificationRefs",
        "validFrom",
        "status"
      ],
      "optional": [
        "conditions",
        "purpose",
        "attributeConstraints",
        "validTo",
        "sourceGrantRef",
        "roleAssignmentRef",
        "consentRef"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "active",
        "suspended",
        "expired",
        "revoked",
        "superseded"
      ]
    },
    "DelegationState": {
      "identity": [
        "grantId"
      ],
      "required": [
        "sourceGrantRef",
        "depth",
        "subdelegationPermitted",
        "attenuationProofRef"
      ],
      "optional": [
        "propagationDeadline"
      ]
    },
    "CredentialMetadata": {
      "ownership": "account component, not candidate root",
      "required": [
        "type",
        "issuerRef",
        "status",
        "protectedReference"
      ],
      "optional": [
        "validFrom",
        "validTo",
        "assurance",
        "keyIdentifier",
        "bindingRef",
        "issuedCredentialRef"
      ],
      "prohibited": [
        "secretValue",
        "privateKey",
        "password",
        "reversibleDigest"
      ]
    }
  },
  "invariantRules": [
    {
      "id": "EM-RSK-03.AD-01",
      "text": "Person, identity anchor, digital account and principal reference remain linked but never equated."
    },
    {
      "id": "EM-RSK-03.AD-02",
      "text": "WM-PER-002 duplicate retirement into WM-XCT-016 is a proposal that requires registry-owner alias confirmation and creates no account identity."
    },
    {
      "id": "EM-RSK-03.AD-03",
      "text": "An IAM access role is never inferred from an organizational role, title or position."
    },
    {
      "id": "EM-RSK-03.AD-04",
      "text": "Authorization Domain, Access Role, Role Assignment, Permission Grant and Delegated Grant have distinct identity and lifecycle semantics; this offline cluster does not prove one aggregate root."
    },
    {
      "id": "EM-RSK-03.AD-05",
      "text": "Every effective grant states principal, authority basis, one or more live justifications, actions, resource scope, conditions and validity."
    },
    {
      "id": "EM-RSK-03.AD-06",
      "text": "A delegated grant is a strict or equal subset of source actions, resource scope, purpose, attributes and validity and preserves or strengthens source conditions."
    },
    {
      "id": "EM-RSK-03.AD-07",
      "text": "Grant widening creates a new root grant with independent authority and justification; it never mutates a delegated child."
    },
    {
      "id": "EM-RSK-03.AD-08",
      "text": "Revoking or expiring a source grant invalidates all active descendants; revoking a child does not revoke its parent or separately justified siblings."
    },
    {
      "id": "EM-RSK-03.AD-09",
      "text": "Delegation records depth, expiry and whether sub-delegation is permitted, and rejects cycles."
    },
    {
      "id": "EM-RSK-03.AD-10",
      "text": "Consent may justify a read or disclosure grant but never creates general IAM capability or proves write/action authorization."
    },
    {
      "id": "EM-RSK-03.AD-11",
      "text": "Removing a role or work assignment invalidates only grants for which that assignment was the sole remaining live justification."
    },
    {
      "id": "EM-RSK-03.AD-12",
      "text": "An Access Review conclusion records retain, revoke, recertify or escalate and changes access only through a separate effective grant transition."
    },
    {
      "id": "EM-RSK-03.AD-13",
      "text": "Reviewer authority and delegation are governance authority and never create access rights."
    },
    {
      "id": "EM-RSK-03.AD-14",
      "text": "Credential metadata stores type, issuer, validity, assurance, status, key identifier, binding and protected reference only; secret values and reversible representations are prohibited."
    },
    {
      "id": "EM-RSK-03.AD-15",
      "text": "Identity-register keyBinding, account authenticator metadata and WM-XCT-017 issued credential or attestation remain separate and cross-referenced."
    },
    {
      "id": "EM-RSK-03.AD-16",
      "text": "Credential-status revocation, grant revocation, assignment termination, consent withdrawal and review decision are separate events with explicit causal links."
    },
    {
      "id": "EM-RSK-03.AD-17",
      "text": "Cached sessions and tokens cannot remain authorized beyond the supporting grant validity or revocation propagation deadline."
    },
    {
      "id": "EM-RSK-03.AD-18",
      "text": "Every approval, exercise, review, suspension, expiry and revocation correlates to append-only audit evidence without secret material."
    },
    {
      "id": "EM-RSK-03.AD-19",
      "text": "Projections contain only grant, justification and status metadata allowed by disclosure policy and never grant authority by their existence."
    },
    {
      "id": "EM-RSK-03.AD-20",
      "text": "Retired domain, role, assignment and grant identifiers remain resolvable and are never recycled."
    }
  ],
  "holds": [
    "The candidate cluster is not one proven aggregate type; registry allocation must resolve Domain/Role/Assignment/Grant root boundaries.",
    "No registry namespace or identifier is allocated and none may be guessed.",
    "WM-PER-002 duplicate retirement requires registry-owner alias confirmation.",
    "WM-VRT-005 and WM-XCT-004/007 lack usable complete specifications.",
    "WM-ACT-034 has no approved Access Review profile.",
    "Credential Metadata versus identity-register keyBinding versus WM-XCT-017 requires an approved semantic crosswalk.",
    "Approved relations, rights controls, package conversion and live conformance remain pending."
  ],
  "publicationStatement": "Research candidate cluster only; not canonically publishable, installable, allocated or verified.",
  "invariants": [
    "Person, identity anchor, digital account and principal reference remain linked but never equated.",
    "WM-PER-002 duplicate retirement into WM-XCT-016 is a proposal that requires registry-owner alias confirmation and creates no account identity.",
    "An IAM access role is never inferred from an organizational role, title or position.",
    "Authorization Domain, Access Role, Role Assignment, Permission Grant and Delegated Grant have distinct identity and lifecycle semantics; this offline cluster does not prove one aggregate root.",
    "Every effective grant states principal, authority basis, one or more live justifications, actions, resource scope, conditions and validity.",
    "A delegated grant is a strict or equal subset of source actions, resource scope, purpose, attributes and validity and preserves or strengthens source conditions.",
    "Grant widening creates a new root grant with independent authority and justification; it never mutates a delegated child.",
    "Revoking or expiring a source grant invalidates all active descendants; revoking a child does not revoke its parent or separately justified siblings.",
    "Delegation records depth, expiry and whether sub-delegation is permitted, and rejects cycles.",
    "Consent may justify a read or disclosure grant but never creates general IAM capability or proves write/action authorization.",
    "Removing a role or work assignment invalidates only grants for which that assignment was the sole remaining live justification.",
    "An Access Review conclusion records retain, revoke, recertify or escalate and changes access only through a separate effective grant transition.",
    "Reviewer authority and delegation are governance authority and never create access rights.",
    "Credential metadata stores type, issuer, validity, assurance, status, key identifier, binding and protected reference only; secret values and reversible representations are prohibited.",
    "Identity-register keyBinding, account authenticator metadata and WM-XCT-017 issued credential or attestation remain separate and cross-referenced.",
    "Credential-status revocation, grant revocation, assignment termination, consent withdrawal and review decision are separate events with explicit causal links.",
    "Cached sessions and tokens cannot remain authorized beyond the supporting grant validity or revocation propagation deadline.",
    "Every approval, exercise, review, suspension, expiry and revocation correlates to append-only audit evidence without secret material.",
    "Projections contain only grant, justification and status metadata allowed by disclosure policy and never grant authority by their existence.",
    "Retired domain, role, assignment and grant identifiers remain resolvable and are never recycled."
  ]
}


===== candidate-allocation-offline\profile-candidate.json =====
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-RSK-03",
  "name": "Enterprise Identity, Account and Authorization Binding",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "candidateRevision": 2,
  "canonicalPublishable": false,
  "bases": [
    "WM-XCT-016",
    "WM-VRT-005",
    "WM-XCT-002",
    "WM-XCT-001",
    "WM-ACT-034",
    "WM-XCT-004",
    "WM-XCT-007",
    "WM-XCT-017"
  ],
  "constraintRules": [
    {
      "id": "EM-RSK-03.EP-01",
      "text": "WM-PER-002 duplicate retirement into WM-XCT-016 is conditional on registry-owner alias confirmation and creates no digital account."
    },
    {
      "id": "EM-RSK-03.EP-02",
      "text": "Person, identity register and WM-VRT-005 Digital Account remain separate identities joined by effective assurance-qualified bindings."
    },
    {
      "id": "EM-RSK-03.EP-03",
      "text": "WM-XCT-002 supplies consent and read/disclosure justification only and never becomes an operational IAM role, assignment or grant."
    },
    {
      "id": "EM-RSK-03.EP-04",
      "text": "WM-XCT-001 supplies holder/steward authority and scoped control mandates only and never hosts an IAM grant catalogue."
    },
    {
      "id": "EM-RSK-03.EP-05",
      "text": "WM-ACT-034 profiles Access Review activity over an account and explicit grant or assignment set, with retain, revoke, recertify or escalate outputs."
    },
    {
      "id": "EM-RSK-03.EP-06",
      "text": "A review output never changes access until a separate grant transition is effective and auditable."
    },
    {
      "id": "EM-RSK-03.EP-07",
      "text": "WM-XCT-004 and WM-XCT-007 are conceptual audit and enforcement neighbors only until complete specifications and approved relations exist."
    },
    {
      "id": "EM-RSK-03.EP-08",
      "text": "Account authenticator metadata is a component; WM-XCT-017 remains the issued credential or attestation master and secret storage remains external."
    },
    {
      "id": "EM-RSK-03.EP-09",
      "text": "No projection or credential-status record grants authorization by its existence."
    }
  ],
  "holds": [
    "The candidate cluster is not one proven aggregate type; registry allocation must resolve Domain/Role/Assignment/Grant root boundaries.",
    "No registry namespace or identifier is allocated and none may be guessed.",
    "WM-PER-002 duplicate retirement requires registry-owner alias confirmation.",
    "WM-VRT-005 and WM-XCT-004/007 lack usable complete specifications.",
    "WM-ACT-034 has no approved Access Review profile.",
    "Credential Metadata versus identity-register keyBinding versus WM-XCT-017 requires an approved semantic crosswalk.",
    "Approved relations, rights controls, package conversion and live conformance remain pending."
  ],
  "publicationStatement": "Research candidate cluster only; not canonically publishable, installable, allocated or verified."
}


===== candidate-allocation-offline\fixtures.json =====
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "contourId": "EM-RSK-03",
  "candidateName": "Authorization Domain / Access Grant",
  "candidateRevision": 2,
  "canonicalPublishable": false,
  "executable": false,
  "cases": [
    {
      "id": "EM-RSK-03.FX-001",
      "kind": "negative",
      "input": "An implementation contradicts: Person, identity anchor, digital account and principal reference remain linked but never equated.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-01.",
      "rules": [
        "EM-RSK-03.AD-01"
      ]
    },
    {
      "id": "EM-RSK-03.FX-002",
      "kind": "negative",
      "input": "An implementation contradicts: WM-PER-002 duplicate retirement into WM-XCT-016 is a proposal that requires registry-owner alias confirmation and creates no account identity.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-02.",
      "rules": [
        "EM-RSK-03.AD-02"
      ]
    },
    {
      "id": "EM-RSK-03.FX-003",
      "kind": "negative",
      "input": "An implementation contradicts: An IAM access role is never inferred from an organizational role, title or position.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-03.",
      "rules": [
        "EM-RSK-03.AD-03"
      ]
    },
    {
      "id": "EM-RSK-03.FX-004",
      "kind": "negative",
      "input": "An implementation contradicts: Authorization Domain, Access Role, Role Assignment, Permission Grant and Delegated Grant have distinct identity and lifecycle semantics; this offline cluster does not prove one aggregate root.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-04.",
      "rules": [
        "EM-RSK-03.AD-04"
      ]
    },
    {
      "id": "EM-RSK-03.FX-005",
      "kind": "negative",
      "input": "An implementation contradicts: Every effective grant states principal, authority basis, one or more live justifications, actions, resource scope, conditions and validity.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-05.",
      "rules": [
        "EM-RSK-03.AD-05"
      ]
    },
    {
      "id": "EM-RSK-03.FX-006",
      "kind": "negative",
      "input": "An implementation contradicts: A delegated grant is a strict or equal subset of source actions, resource scope, purpose, attributes and validity and preserves or strengthens source conditions.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-06.",
      "rules": [
        "EM-RSK-03.AD-06"
      ]
    },
    {
      "id": "EM-RSK-03.FX-007",
      "kind": "negative",
      "input": "An implementation contradicts: Grant widening creates a new root grant with independent authority and justification; it never mutates a delegated child.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-07.",
      "rules": [
        "EM-RSK-03.AD-07"
      ]
    },
    {
      "id": "EM-RSK-03.FX-008",
      "kind": "negative",
      "input": "An implementation contradicts: Revoking or expiring a source grant invalidates all active descendants; revoking a child does not revoke its parent or separately justified siblings.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-08.",
      "rules": [
        "EM-RSK-03.AD-08"
      ]
    },
    {
      "id": "EM-RSK-03.FX-009",
      "kind": "negative",
      "input": "An implementation contradicts: Delegation records depth, expiry and whether sub-delegation is permitted, and rejects cycles.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-09.",
      "rules": [
        "EM-RSK-03.AD-09"
      ]
    },
    {
      "id": "EM-RSK-03.FX-010",
      "kind": "negative",
      "input": "An implementation contradicts: Consent may justify a read or disclosure grant but never creates general IAM capability or proves write/action authorization.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-10.",
      "rules": [
        "EM-RSK-03.AD-10"
      ]
    },
    {
      "id": "EM-RSK-03.FX-011",
      "kind": "negative",
      "input": "An implementation contradicts: Removing a role or work assignment invalidates only grants for which that assignment was the sole remaining live justification.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-11.",
      "rules": [
        "EM-RSK-03.AD-11"
      ]
    },
    {
      "id": "EM-RSK-03.FX-012",
      "kind": "negative",
      "input": "An implementation contradicts: An Access Review conclusion records retain, revoke, recertify or escalate and changes access only through a separate effective grant transition.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-12.",
      "rules": [
        "EM-RSK-03.AD-12"
      ]
    },
    {
      "id": "EM-RSK-03.FX-013",
      "kind": "negative",
      "input": "An implementation contradicts: Reviewer authority and delegation are governance authority and never create access rights.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-13.",
      "rules": [
        "EM-RSK-03.AD-13"
      ]
    },
    {
      "id": "EM-RSK-03.FX-014",
      "kind": "negative",
      "input": "An implementation contradicts: Credential metadata stores type, issuer, validity, assurance, status, key identifier, binding and protected reference only; secret values and reversible representations are prohibited.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-14.",
      "rules": [
        "EM-RSK-03.AD-14"
      ]
    },
    {
      "id": "EM-RSK-03.FX-015",
      "kind": "negative",
      "input": "An implementation contradicts: Identity-register keyBinding, account authenticator metadata and WM-XCT-017 issued credential or attestation remain separate and cross-referenced.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-15.",
      "rules": [
        "EM-RSK-03.AD-15"
      ]
    },
    {
      "id": "EM-RSK-03.FX-016",
      "kind": "negative",
      "input": "An implementation contradicts: Credential-status revocation, grant revocation, assignment termination, consent withdrawal and review decision are separate events with explicit causal links.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-16.",
      "rules": [
        "EM-RSK-03.AD-16"
      ]
    },
    {
      "id": "EM-RSK-03.FX-017",
      "kind": "negative",
      "input": "An implementation contradicts: Cached sessions and tokens cannot remain authorized beyond the supporting grant validity or revocation propagation deadline.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-17.",
      "rules": [
        "EM-RSK-03.AD-17"
      ]
    },
    {
      "id": "EM-RSK-03.FX-018",
      "kind": "negative",
      "input": "An implementation contradicts: Every approval, exercise, review, suspension, expiry and revocation correlates to append-only audit evidence without secret material.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-18.",
      "rules": [
        "EM-RSK-03.AD-18"
      ]
    },
    {
      "id": "EM-RSK-03.FX-019",
      "kind": "negative",
      "input": "An implementation contradicts: Projections contain only grant, justification and status metadata allowed by disclosure policy and never grant authority by their existence.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-19.",
      "rules": [
        "EM-RSK-03.AD-19"
      ]
    },
    {
      "id": "EM-RSK-03.FX-020",
      "kind": "negative",
      "input": "An implementation contradicts: Retired domain, role, assignment and grant identifiers remain resolvable and are never recycled.",
      "expect": "The contradiction is rejected under EM-RSK-03.AD-20.",
      "rules": [
        "EM-RSK-03.AD-20"
      ]
    },
    {
      "id": "EM-RSK-03.FX-021",
      "kind": "positive",
      "input": "Account Acc is linked to Person P. G1 has only assignment A as justification; G2 has A and live consent C. A ends.",
      "expect": "G1 and descendants are revoked; G2 remains reviewable because C is still a live independent justification.",
      "rules": [
        "EM-RSK-03.AD-01",
        "EM-RSK-03.AD-11"
      ]
    },
    {
      "id": "EM-RSK-03.FX-022",
      "kind": "positive",
      "input": "Parent grant permits read and update for 30 days. Child permits read on one dataset for 7 days with no sub-delegation.",
      "expect": "Child passes attenuation and records depth, expiry and sub-delegation flag.",
      "rules": [
        "EM-RSK-03.AD-06",
        "EM-RSK-03.AD-09"
      ]
    },
    {
      "id": "EM-RSK-03.FX-023",
      "kind": "negative",
      "input": "A manager title automatically grants payroll write access.",
      "expect": "Authorization is rejected because organizational position is not IAM authority.",
      "rules": [
        "EM-RSK-03.AD-03"
      ]
    },
    {
      "id": "EM-RSK-03.FX-024",
      "kind": "negative",
      "input": "A child grant adds delete, broadens region and outlives the parent.",
      "expect": "Delegation is rejected; widening requires a separately justified root grant.",
      "rules": [
        "EM-RSK-03.AD-06",
        "EM-RSK-03.AD-07"
      ]
    },
    {
      "id": "EM-RSK-03.FX-025",
      "kind": "negative",
      "input": "Credential metadata includes an API secret and reversible encrypted password in a report projection.",
      "expect": "Record and projection are rejected; only safe metadata and a protected reference may appear.",
      "rules": [
        "EM-RSK-03.AD-14",
        "EM-RSK-03.AD-19"
      ]
    },
    {
      "id": "EM-RSK-03.FX-026",
      "kind": "positive",
      "input": "Access Review recommends revocation and delegated reviewer approval; grant transition has not executed.",
      "expect": "Review and reviewer delegation create no access change until the separate grant transition becomes effective.",
      "rules": [
        "EM-RSK-03.AD-12",
        "EM-RSK-03.AD-13"
      ]
    }
  ]
}
