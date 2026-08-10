# S2 Access Contract & Consent

This meta-model turns an owner's decision to share into a durable, machine-readable instrument: who may read what, in which shape, for what purpose, until when, and on what evidence of consent. It is its own model because permission is not a property of the data and not a property of the reader; it is an agreement with its own parties, lifecycle, evidence and revocation, and every other model in the catalogue defers to it whenever data crosses an ownership boundary.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s2"
  csn: world.accessContract
  version: 0.2.0
  displayName: "Access Contract & Consent"
  description: "Machine-readable permission to read: grantor, grantee, scope, purpose, consent evidence and revocation."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.accessContract
bundles:
  - csn: world.accessContract.agreement
    displayName: "Agreement"
    layers:
      - world.accessContract.agreement.grantTerms
      - world.accessContract.agreement.scopeSelection
      - world.accessContract.agreement.obligations
  - csn: world.accessContract.consent
    displayName: "Consent"
    layers:
      - world.accessContract.consent.expression
      - world.accessContract.consent.capacity
  - csn: world.accessContract.lifecycle
    displayName: "Lifecycle"
    layers:
      - world.accessContract.lifecycle.activation
      - world.accessContract.lifecycle.termination
imports:
  - source: mu-contract
    version: "*"
  - source: odrl
    version: "*"
  - source: kantara-consent-receipt
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `agreement` | The instrument itself: parties, permission, duties | `grantTerms`: grantor, grantee, purpose and validity window · `scopeSelection`: which objects, in which disclosure shape · `obligations`: grantee duties such as no onward sharing and retention limits |
| `consent` | The human act behind the instrument | `expression`: how and when consent was expressed, with evidence · `capacity`: who may consent, including guardians and delegates acting under S1 |
| `lifecycle` | How a grant is born, changed and dies | `activation`: proposal, acceptance, entry into force · `termination`: revocation, expiry, supersession |

## Objects

- `accessContract`: the permission instrument; key attributes: grantor reference, grantee reference, purpose, validity window, status.
- `scopeClause`: one covered slice of data; key attributes: object references, projection policy reference, read frequency limits.
- `purposeStatement`: the declared use the grant is limited to; key attributes: purpose text, purpose category, compatibility notes.
- `obligationClause`: a duty the grantee accepts; key attributes: duty kind, deadline or duration, consequence reference.
- `consentRecord`: the evidence of the grantor's assent; key attributes: channel, time, evidence artifact, acting capacity (self, guardian, delegate).
- `revocationNotice`: the act that ends a grant early; key attributes: issuer, reason, effective time, propagation status.

## Relationships

- `accessContract` -> grantedOver -> `registryEntry` (1..*): the grant covers objects registered in the ownership model (S1).
- `scopeClause` -> refines -> `accessContract` (*..1): clauses partition the grant into concrete slices.
- `scopeClause` -> shapedBy -> `projectionPolicy` (1..1): every slice leaves only in a shape defined in S3.
- `consentRecord` -> evidences -> `accessContract` (1..1): no contract is active without captured consent.
- `obligationClause` -> bindsGranteeOf -> `accessContract` (*..1): duties attach to the reader for the life of the grant and beyond.
- `revocationNotice` -> terminates -> `accessContract` (1..1): revocation ends the grant from its effective time forward.

## Events

- `contractProposed`: a would-be grantee or the grantor put a draft grant on the table.
- `consentCaptured`: the grantor, or a party with capacity to act for them, expressed assent and evidence was recorded.
- `contractActivated`: the grant entered into force and reads became permissible within scope.
- `scopeAmended`: the covered objects, shape or limits of a live grant changed by agreement.
- `contractRevoked`: the grantor withdrew the grant before its natural end.
- `contractExpired`: the validity window closed without renewal.
- `obligationDischarged`: a grantee duty, such as end-of-grant erasure, was fulfilled and evidenced.

## Contracts

- `grantVerification`: a data holder or third party checks that a specific read is covered by a live contract, receiving only validity and scope fingerprint.
- `consentReceiptDelivery`: the grantor receives a durable, portable copy of what they agreed to.
- `revocationPropagation`: every holder of data under the grant is notified of revocation and confirms cutoff.

## Projections

- `validityToken`: is the grant live and does it cover this read; omits parties, purpose and terms.
- `grantorLedger`: everything I have granted, to whom and until when; omits other grantors entirely.
- `granteeEntitlementList`: what a reader may currently access and in which shape; omits consent evidence and grantor detail.

## Composition

- REFERENCE `world.ownership` (S1): grantor authority resolves against ownership, delegation or guardianship records; a grant from a non-holder is void.
- REFERENCE `world.disclosureScope` (S3): scope clauses do not describe shapes themselves, they point at projection policies.
- REFERENCE `world.accessAudit` (S4): every exercise of a contract, and every grant and revocation, is logged there.
- REFERENCE `world.accessEnforcement` (S7): obligation violations and out-of-scope reads escalate into that model's cases.
- imports: mu-contract (EXTEND): the general contract primitive this model specializes for read permission.
- imports: odrl (ALIGN): permission, prohibition and duty vocabulary mapped onto grant terms and obligations.
- imports: kantara-consent-receipt (ALIGN): the consent receipt shape delivered to grantors.

## Stewardship

The data owner is the grantor and the steward of every contract over their objects; no registry or operator can create permission on their behalf beyond what S1 delegation records allow. Reads of contract data follow the same rule: the grantor grants, S4 logs.
