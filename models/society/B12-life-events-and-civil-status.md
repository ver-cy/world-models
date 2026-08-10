# B12 Life Events & Civil Status

The registrable turning points of a human life, birth, marriage, divorce, death, name change, and the civil status that follows from them, together with the certificates that prove them. It is its own meta-model because civil status is a derived, jurisdiction-recognized state with its own registration discipline: the person owns their life story, while the civil registrar keeps the authoritative register the story is anchored in.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:b12"
  csn: world.lifeEventsAndCivilStatus
  version: 0.2.0
  displayName: "Life Events & Civil Status"
  description: "Registrable life events, the civil status derived from them and the certificates that prove them."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.lifeEventsAndCivilStatus
bundles:
  - csn: world.lifeEventsAndCivilStatus.lifeEvent
    displayName: "Life event"
    layers:
      - world.lifeEventsAndCivilStatus.lifeEvent.vitalEvent
      - world.lifeEventsAndCivilStatus.lifeEvent.unionEvent
      - world.lifeEventsAndCivilStatus.lifeEvent.nameAndIdentityChange
  - csn: world.lifeEventsAndCivilStatus.civilStatus
    displayName: "Civil status"
    layers:
      - world.lifeEventsAndCivilStatus.civilStatus.statusDerivation
      - world.lifeEventsAndCivilStatus.civilStatus.statusHistory
  - csn: world.lifeEventsAndCivilStatus.certification
    displayName: "Certification"
    layers:
      - world.lifeEventsAndCivilStatus.certification.certificateReference
      - world.lifeEventsAndCivilStatus.certification.crossJurisdictionRecognition
imports:
  - source: civil-registration-standards
    version: "*"
  - source: un-crvs
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `lifeEvent` | The registrable occurrences themselves | `vitalEvent`: birth and death with place, time and attendants · `unionEvent`: marriage, partnership, divorce and dissolution · `nameAndIdentityChange`: registered changes of name and recorded sex or gender marker where the jurisdiction registers them |
| `civilStatus` | The state a person is in as a result | `statusDerivation`: how current status follows from the event sequence · `statusHistory`: the full status timeline with effective dates |
| `certification` | Proving events and status | `certificateReference`: links to issued certificates for each event · `crossJurisdictionRecognition`: recognition of foreign events and certificates |

## Objects

- `lifeEvent`: one registrable occurrence in a person's life; key attributes: kind, occurredAt, place, participants, registrationRef
- `civilStatus`: a person's derived status in a period; key attributes: status, effectiveFrom, effectiveUntil, derivedFromEvents
- `union`: a marriage or registered partnership as an ongoing state; key attributes: parties, establishedAt, dissolvedAt, regime
- `nameChange`: a registered change of legal name; key attributes: previousName, newName, effectiveAt, grounds
- `registrationRef`: the anchor of an event in the civil register; key attributes: registerRef, entryNumber, registeredAt
- `certificateRef`: the pointer to an issued certificate attesting an event; key attributes: attestationRef, issuedAt, kind
- `jurisdictionRecognition`: acceptance of a foreign event or certificate; key attributes: jurisdiction, recognizedAt, basis, limitations

## Relationships

- `lifeEvent` -> concerns -> `world.person` person (many-to-many): a birth concerns child and parents, a marriage concerns two parties
- `civilStatus` -> derivedFrom -> `lifeEvent` (many-to-many): status is computed from the ordered event set
- `union` -> establishedBy -> `lifeEvent` (one-to-one): each union starts with one union event
- `union` -> dissolvedBy -> `lifeEvent` (one-to-one): dissolution, where it occurs, is itself a registered event
- `certificateRef` -> certifies -> `lifeEvent` (many-to-one): an event can be certified by several successive certificates
- `lifeEvent` -> anchoredBy -> `registrationRef` (one-to-one): only registered events carry civil effect
- `jurisdictionRecognition` -> recognizes -> `certificateRef` (many-to-one): a foreign certificate may be recognized in several jurisdictions

## Events

- `birthRegistered`: a birth was entered in the civil register and a person's civil existence began
- `marriageConcluded`: a marriage or partnership was concluded and registered
- `unionDissolved`: a divorce or dissolution was granted and registered
- `deathRegistered`: a death was entered in the civil register
- `nameChanged`: a change of legal name took effect by registration
- `certificateIssued`: a certificate attesting a registered event was issued
- `foreignEventRecognized`: an event registered abroad was recognized domestically

## Contracts

- `certificateIssuanceContract`: the person's (or an entitled party's) right to obtain certificates of registered events
- `statusVerificationContract`: yes/no confirmation of a person's current civil status without event details
- `interAgencyNotificationContract`: automatic notice of registered births and deaths to entitled downstream models
- `genealogyAccessContract`: time-embargoed archival access to historical entries for research after protection periods lapse

## Projections

- `currentStatusView`: the person's present civil status only; omits the events behind it
- `certificateView`: one event as attested, for presentation; omits the rest of the person's history
- `genealogicalView`: post-embargo historical entries for research; omits entries still under protection

## Composition

- REFERENCE `world.person` (H1): every event concerns persons governed in their own model
- EXTEND `world.registry` (R1): the civil register specializes the register pattern, with civil effect as its legal effect
- REFERENCE `world.identityRegister` (R4): birth registration creates the person's identity anchor and death registration retires it
- REFERENCE `world.attestationCertificateAndLicense` (R5): certificates are attestations issued by the civil registrar
- COMPOSE `world.eventRegister` (R3): registrations are published to an integrity-proofed event log that downstream models subscribe to
- REFERENCE (inbound) `world.socialProvisionAndBenefit` (B13): registered life events trigger entitlement reviews there
- imports: civil-registration-standards (ALIGN): civil registration process and record vocabulary
- imports: un-crvs (ALIGN): vital event definitions and vital statistics recommendations

## Stewardship

The person owns their life story and controls its disclosure; the civil registrar owns and answers for the authoritative register the story is anchored in. Certificates, verifications and notifications are granted through the S1/S2 access and consent models, with registrar acts and disclosures audited via S4.
