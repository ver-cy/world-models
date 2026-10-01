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
