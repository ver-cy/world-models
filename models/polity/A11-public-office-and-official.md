# A11 Public Office & Official

This meta-model describes public offices as durable positions of authority and the people who hold them: how an office is established and empowered, how a person is appointed or seated into it, how tenure runs and ends, and the accountability instruments (oaths, declarations, integrity rules) that attach to holding it. It is its own model because an office outlives any holder and any single administration, and because the office register is the reference point that lawmaking (A10), elections (A13), permitting (A14) and enforcement (A18) all resolve officeholders against.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a11"
  csn: world.publicOffice
  version: 0.2.0
  displayName: Public Office & Official
  description: Public offices, their holders, appointments, tenure and accountability instruments.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.publicOffice
bundles:
  - csn: world.publicOffice.officeStructure
    displayName: Office structure
    layers:
      - world.publicOffice.officeStructure.definition
      - world.publicOffice.officeStructure.powers
  - csn: world.publicOffice.tenure
    displayName: Tenure
    layers:
      - world.publicOffice.tenure.appointment
      - world.publicOffice.tenure.termAndSuccession
  - csn: world.publicOffice.accountability
    displayName: Accountability
    layers:
      - world.publicOffice.accountability.declaration
      - world.publicOffice.accountability.integrityRules
imports:
  - source: w3c-org
    version: "*"
  - source: cpsv
    version: "*"
  - source: popolo
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `officeStructure` | What an office is and may do | `definition`: establishment, title, seat count, seat of the office Â· `powers`: mandate, competences, signing authority |
| `tenure` | Who holds an office and when | `appointment`: acts of appointing or seating a person Â· `termAndSuccession`: terms, vacancies, acting arrangements |
| `accountability` | Duties that attach to holding office | `declaration`: asset and interest declarations of holders Â· `integrityRules`: incompatibilities, recusal duties, sanctions |

## Objects

- `office`: a durable position of public authority; key attributes: title, establishingActRef, bodyRef, seatCount, status
- `officeholder`: one person's holding of an office over an interval; key attributes: personRef, officeRef, start, end, basis
- `appointment`: the act that fills an office; key attributes: appointingAuthorityRef, appointeeRef, instrument, effectiveOn
- `oath`: the sworn assumption of duties; key attributes: text, swornOn, witnessRef
- `declaration`: a periodic asset or interest declaration; key attributes: period, filedOn, scope, visibilityClass
- `delegation`: a temporary transfer of specific powers between offices; key attributes: fromOfficeRef, toOfficeRef, scope, validity
- `vacancy`: an interval in which an office is unfilled; key attributes: officeRef, cause, start, end, actingArrangement

## Relationships

- `office` -> establishedBy -> `enactmentRef` (N:1): offices are created and abolished by enacted law recorded in A10
- `office` -> belongsTo -> `governmentBodyRef` (N:1): each office sits within a branch body of A2
- `officeholder` -> holds -> `office` (N:1): a tenure record binds one office at a time
- `officeholder` -> identifies -> `personRef` (N:1): the holder resolves to a person in P1
- `appointment` -> fills -> `office` (N:1): an appointment act seats a person into one office
- `declaration` -> filedBy -> `officeholder` (N:1): accountability filings attach to a specific tenure
- `delegation` -> delegatesFrom -> `office` (N:1): delegated powers trace back to the delegating office

## Events

- `officeEstablished`: a new office was created by enactment
- `appointmentMade`: an appointing authority issued an instrument filling an office
- `oathTaken`: a holder formally assumed the duties of office
- `tenureStarted`: a person's holding of an office became effective
- `tenureEnded`: a tenure ended by expiry, resignation, removal or death
- `declarationFiled`: a holder filed an asset or interest declaration
- `delegationGranted`: specific powers were temporarily delegated to another office
- `officeAbolished`: an office ceased to exist

## Contracts

- `publicOfficeDirectory`: open access to the register of offices and current holders, public per the A12 mandate
- `holderAttestation`: verification that a given person held a given office at a given time
- `declarationDisclosure`: scoped access to declarations, graded by the visibility class set in integrity rules

## Projections

- `whoHoldsWhat`: current offices and their holders; omits history, declarations and delegations
- `officeHistory`: the full succession timeline of one office; omits declaration content
- `integrityDossier`: declarations and integrity findings for oversight bodies; omits unrelated tenure detail

## Composition

- REFERENCE `world.person` (P1): every holder, appointee and witness resolves to a person
- REFERENCE `world.publicOffice` (A11): offices are positioned within branch bodies
- REFERENCE `world.lawmaking` (A10): establishment, empowerment and abolition trace to enactments
- REFERENCE `world.election` (A13): elected offices are filled by mandate grants issued there
- REFERENCE `world.registryMandate` (A12): the office register operates as a mandated public register
- MIX-IN `world.auditTrail` (S4): appointments, tenures and declarations carry append-only provenance
- imports: w3c-org (EXTEND): posts, roles and memberships as the structural backbone of office and tenure
- imports: cpsv (ALIGN): public organization and service vocabulary
- imports: popolo (ALIGN): person, post and membership interchange with civic data consumers

## Stewardship

The appointing authority for each office family acts as registrar of this model; the register itself is public per its A12 mandate. Declarations and other graded layers are opened only by owner grant through S1 ownership and S2 access rules.