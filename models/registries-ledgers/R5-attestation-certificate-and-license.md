# R5 Attestation Certificate & License

Issued claims with validity: certificates, licenses, permits, diplomas and other attestations in which an issuer asserts something about a subject for a bounded period, the subject holds a presentable copy, and any verifier can check validity and revocation. It is its own meta-model because the triangle of issuer, subject and verifier, with validity and revocation in the middle, recurs identically across every domain that issues formal claims.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:r5"
  csn: world.attestationCertificateAndLicense
  version: 0.2.0
  displayName: "Attestation Certificate & License"
  description: "Issuer-asserted claims about subjects with validity, revocation, holder copies and verifiable presentation."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.attestationCertificateAndLicense
bundles:
  - csn: world.attestationCertificateAndLicense.claim
    displayName: "Claim"
    layers:
      - world.attestationCertificateAndLicense.claim.claimSchema
      - world.attestationCertificateAndLicense.claim.subjectBinding
  - csn: world.attestationCertificateAndLicense.issuance
    displayName: "Issuance"
    layers:
      - world.attestationCertificateAndLicense.issuance.issuerAuthority
      - world.attestationCertificateAndLicense.issuance.issuanceProcess
  - csn: world.attestationCertificateAndLicense.validity
    displayName: "Validity"
    layers:
      - world.attestationCertificateAndLicense.validity.validityPeriod
      - world.attestationCertificateAndLicense.validity.revocationAndSuspension
  - csn: world.attestationCertificateAndLicense.presentation
    displayName: "Presentation"
    layers:
      - world.attestationCertificateAndLicense.presentation.holderPresentation
      - world.attestationCertificateAndLicense.presentation.verification
imports:
  - source: w3c-verifiable-credentials
    version: "*"
  - source: rfc-5280
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `claim` | What is being asserted and about whom | `claimSchema`: typed claim content per attestation kind · `subjectBinding`: how the claim is cryptographically and legally tied to its subject |
| `issuance` | Who may issue and how | `issuerAuthority`: the issuer's mandate for each attestation class · `issuanceProcess`: application, examination, decision and delivery of the holder copy |
| `validity` | Whether the claim currently holds | `validityPeriod`: not-before and not-after windows, renewal · `revocationAndSuspension`: early termination, suspension and status publication |
| `presentation` | Using and checking the claim | `holderPresentation`: how the holder presents, fully or selectively · `verification`: verifier checks of authenticity, binding and current status |

## Objects

- `attestation`: one issued claim instance; key attributes: kind, claimContent, issuedAt, serial, schemaRef
- `claimSchema`: the typed structure a class of attestations follows; key attributes: kind, attributes, evidenceRequirements
- `issuer`: the party mandated to issue an attestation class; key attributes: identityRef, mandateRef, statusServiceRef
- `subjectBinding`: the tie between attestation and subject; key attributes: subjectIdentityRef, bindingMethod, holderCopyRef
- `validityTerm`: the time window in which the attestation holds; key attributes: validFrom, validUntil, renewalOf
- `revocationEntry`: a published early termination or suspension; key attributes: reason, effectiveAt, kind
- `presentation`: one act of showing the attestation to a verifier; key attributes: presentedAt, disclosureScope, verifierRef
- `verificationResult`: a verifier's recorded outcome; key attributes: outcome, checksPerformed, verifiedAt

## Relationships

- `attestation` -> issuedBy -> `issuer` (many-to-one): each attestation has exactly one accountable issuer
- `attestation` -> conformsTo -> `claimSchema` (many-to-one): claim content is typed by its class schema
- `attestation` -> boundTo -> `subjectBinding` (one-to-one): every attestation is tied to exactly one subject
- `attestation` -> validDuring -> `validityTerm` (one-to-many): renewals chain successive terms on one attestation lineage
- `revocationEntry` -> terminates -> `attestation` (one-to-one): a revocation ends one specific attestation
- `presentation` -> presents -> `attestation` (many-to-one): a holder may present the same attestation many times
- `verificationResult` -> evaluates -> `presentation` (one-to-one): each presentation check yields one recorded result

## Events

- `attestationIssued`: the issuer decided positively and the claim came into force
- `holderCopyDelivered`: the subject received a presentable copy under their control
- `attestationSuspended`: the claim was temporarily taken out of force
- `attestationRevoked`: the claim was terminated before its natural expiry
- `attestationExpired`: the validity window closed without renewal
- `attestationRenewed`: a successor validity term was granted on the same lineage
- `presentationVerified`: a verifier checked a presentation and recorded the outcome

## Contracts

- `issuanceContract`: conditions under which the issuer examines applications and issues an attestation class
- `verificationContract`: a verifier's right to check authenticity and current status, typically without contacting the issuer per case
- `revocationNotificationContract`: how status changes are published or pushed to subscribed relying parties
- `holderCustodyContract`: the holder's rights over their copy, including selective disclosure and re-presentation

## Projections

- `verifierView`: claim content within disclosed scope plus validity and status; omits issuance examination internals
- `holderWalletView`: all attestations held by one subject with renewal state; omits other subjects entirely
- `issuerBookView`: the issuer's register of everything issued, suspended and revoked; omits presentation history at verifiers
- `statusListView`: current validity status by serial only; omits claim content and subject identity

## Composition

- REFERENCE `world.identityRegister` (R4): issuer and subject are anchored identities, and key bindings support subject binding
- EXTEND `world.registry` (R1): the issuer's book of issued attestations specializes the register pattern
- REFERENCE `world.mandate` (A12): the issuer's authority over an attestation class is a mandate governed elsewhere
- COMPOSE `world.eventRegister` (R3): issuance and status events are published to an integrity-proofed log that status services read
- REFERENCE (inbound) `world.lifeEventsAndCivilStatus` (B12) and `world.personalHealth` (B10): civil certificates and immunization certificates are attestations of this model
- MIX-IN `world.audit` (S4): issuance decisions and status changes carry the audit facet
- imports: w3c-verifiable-credentials (ALIGN): claim, proof, holder and status semantics
- imports: rfc-5280 (ALIGN): certificate validity period and revocation modelling

## Stewardship

The issuer owns the book of issued attestations and the status service, and answers for the truth of what it asserts; the subject owns and controls the holder copy. Verifier and third-party access beyond the public status list is granted via the S1/S2 access and consent models and audited via S4.
