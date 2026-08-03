# R4 Identity Register

The anchoring of identity for persons, organizations and things: one authoritative record per subject, to which identifiers, keys and assurance evidence are bound, and against which the rest of the world resolves "who or what is this". It is its own meta-model because identity anchoring, identifier binding and assurance are a distinct discipline from any profile data about the subject: the register says that a subject exists and is the same one over time, and deliberately says as little else as possible.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:r4"
  csn: world.identityRegister
  version: 0.2.0
  displayName: "Identity Register"
  description: "Authoritative anchoring of identities of persons, organizations and things, with identifier and key bindings, assurance and status."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.identityRegister
bundles:
  - csn: world.identityRegister.anchor
    displayName: "Anchor"
    layers:
      - world.identityRegister.anchor.subjectKind
      - world.identityRegister.anchor.identityLifecycle
  - csn: world.identityRegister.binding
    displayName: "Binding"
    layers:
      - world.identityRegister.binding.identifierSchemes
      - world.identityRegister.binding.keyAndCredentialBinding
  - csn: world.identityRegister.assurance
    displayName: "Assurance"
    layers:
      - world.identityRegister.assurance.proofingEvidence
      - world.identityRegister.assurance.assuranceLevel
  - csn: world.identityRegister.resolution
    displayName: "Resolution"
    layers:
      - world.identityRegister.resolution.resolutionService
      - world.identityRegister.resolution.privacyControls
imports:
  - source: w3c-did
    version: "*"
  - source: iso-iec-24760
    version: "*"
  - source: nist-sp-800-63
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `anchor` | The identity record itself | `subjectKind`: person, organization and thing subjects and what an anchor asserts for each Â· `identityLifecycle`: registered, active, suspended, retired states and same-subject continuity |
| `binding` | What attaches to an anchor | `identifierSchemes`: bindings of scheme-governed identifiers to the anchor Â· `keyAndCredentialBinding`: cryptographic keys and authenticators bound for proof of control |
| `assurance` | How strongly identity is established | `proofingEvidence`: the evidence trail from identity proofing Â· `assuranceLevel`: graded confidence attached to the anchor and its bindings |
| `resolution` | Answering lookups without oversharing | `resolutionService`: identifier to status-and-keys resolution Â· `privacyControls`: minimal-disclosure rules, verification without attribute release |

## Objects

- `identityRecord`: the anchor for one subject; key attributes: subjectKind, status, registeredAt, registerRef
- `identifierBinding`: an externally schemed identifier attached to an anchor; key attributes: scheme, value, boundAt, status
- `keyBinding`: a key or authenticator proving control of the anchor; key attributes: keyMaterialRef, purpose, validFrom, revokedAt
- `assuranceAssessment`: a graded judgment of how well the subject was proofed; key attributes: level, method, assessedAt, evidenceRefs
- `identityStatus`: the current standing of the anchor; key attributes: state, reason, effectiveAt
- `linkageAssertion`: a recorded claim that two anchors denote the same subject; key attributes: confidence, basis, assertedBy
- `resolutionPolicy`: what a resolver may disclose to whom; key attributes: audienceClass, disclosedAttributes, verificationOnlyFlag

## Relationships

- `identifierBinding` -> bindsTo -> `identityRecord` (many-to-one): a subject can carry identifiers from several schemes
- `keyBinding` -> provesControlOf -> `identityRecord` (many-to-one): control keys rotate over one stable anchor
- `assuranceAssessment` -> evaluates -> `identityRecord` (many-to-one): assurance is re-assessed over the anchor's life
- `linkageAssertion` -> links -> `identityRecord` (many-to-many): duplicate or successor anchors are joined by explicit assertion, never merged silently
- `identityRecord` -> resolvedUnder -> `resolutionPolicy` (many-to-one): disclosure at lookup follows a declared policy
- `identityRecord` -> hasStatus -> `identityStatus` (one-to-many): status history is kept, current status is derived

## Events

- `identityRegistered`: a new anchor was created for a proofed subject
- `identifierBound`: an external identifier was attached to an anchor
- `identifierRetired`: an identifier binding was ended without ending the anchor
- `keyRotated`: a control key was replaced and the old one retired
- `assuranceRaised`: re-proofing lifted the anchor's assurance level
- `identitySuspended`: the anchor was temporarily barred from resolution and use
- `identityRetired`: the anchor was closed, typically on death or dissolution, with continuity preserved for history
- `recordsLinked`: two anchors were asserted to denote the same subject

## Contracts

- `resolutionContract`: which attributes a class of relying parties may obtain when resolving an identifier
- `verificationContract`: yes/no confirmation of a claimed binding or status without releasing attributes
- `registrarUpdateContract`: who may create, bind, suspend and retire anchors, under which evidence rules
- `subjectAccessContract`: the subject's standing right to see their own full record and its access history

## Projections

- `publicResolverView`: identifier to current status and public keys; omits personal attributes and evidence
- `relyingPartyView`: status plus assurance level for an authorized verifier; omits proofing evidence content
- `subjectSelfView`: the complete own record including bindings, assessments and access history

## Composition

- EXTEND `world.registry` (R1): the identity register is a specialization of the register pattern, with anchoring as its legal effect
- REFERENCE `world.person` (H1): a person anchor points to, and never inlines, the person's profile kept elsewhere
- REFERENCE `world.organization` (O1): organization anchors resolve to organization records governed in their own model
- REFERENCE (inbound) `world.attestationCertificateAndLicense` (R5): issuers and subjects of attestations are anchored here
- REFERENCE (inbound) `world.lifeEventsAndCivilStatus` (B12): birth registration creates a person anchor, death registration retires it
- MIX-IN `world.audit` (S4): every resolution and update carries the audit facet
- imports: w3c-did (ALIGN): decentralized identifier syntax, resolution and key rotation semantics
- imports: iso-iec-24760 (ALIGN): identity management vocabulary and lifecycle framing
- imports: nist-sp-800-63 (ALIGN): identity proofing and assurance level semantics

## Stewardship

The identity registrar owns the anchors and their bindings and answers for uniqueness and continuity, while each subject holds inspection rights over their own record. Any resolution or disclosure beyond the public resolver view is granted through the S1/S2 access and consent models and audited via S4.
