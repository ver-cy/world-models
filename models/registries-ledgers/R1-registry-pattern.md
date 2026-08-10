# R1 Registry (pattern)

The generic register: an authoritative book of entries kept by a mandated registrar, where every entry is grounded in evidence and produces a defined legal effect. It is its own meta-model because every domain register in the catalogue (cadastre, civil register, identity register, license books) repeats the same skeleton of application, examination, entry, publicity and recourse; factoring that skeleton out once keeps the domain registers thin, comparable and mutually consistent.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:r1"
  csn: world.registry
  version: 0.2.0
  displayName: "Registry (pattern)"
  description: "The generic register pattern of entries, evidence, registrar mandate and legal effect."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.registry
bundles:
  - csn: world.registry.entryBook
    displayName: "Entry book"
    layers:
      - world.registry.entryBook.registerDefinition
      - world.registry.entryBook.entryLifecycle
  - csn: world.registry.evidence
    displayName: "Evidence"
    layers:
      - world.registry.evidence.sourceDocuments
      - world.registry.evidence.verification
  - csn: world.registry.authority
    displayName: "Authority"
    layers:
      - world.registry.authority.registrarMandate
      - world.registry.authority.decisionAndRecourse
  - csn: world.registry.effect
    displayName: "Effect"
    layers:
      - world.registry.effect.legalEffect
      - world.registry.effect.publicity
imports:
  - source: mu-registry-doctrine
    version: "*"
  - source: iso-19135
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `entryBook` | The register as a book and the life of its entries | `registerDefinition`: what the register covers, its entry schema and numbering · `entryLifecycle`: draft, registered, amended, cancelled states of an entry |
| `evidence` | Grounds on which entries stand | `sourceDocuments`: deeds, applications and instruments lodged as grounds · `verification`: how lodged evidence was examined and accepted |
| `authority` | Who keeps the register and how decisions are contested | `registrarMandate`: the registrar role and the scope of its mandate · `decisionAndRecourse`: registration decisions, refusals, objections and appeals |
| `effect` | What registration changes in the world | `legalEffect`: the presumption, priority or constitutive effect an entry carries · `publicity`: what is publicly inspectable and how third parties may rely on it |

## Objects

- `register`: an authoritative book for one subject domain; key attributes: scope, entrySchema, numberingScheme, publicityRegime
- `registerEntry`: one authoritative record in a register; key attributes: entryNumber, subjectRef, content, status, registeredAt
- `registrationApplication`: a lodged request to create, amend or cancel an entry; key attributes: applicant, requestedChange, lodgedAt, priorityStamp
- `evidenceItem`: a document or instrument grounding an entry; key attributes: kind, issuer, hash, verificationStatus
- `registrar`: the mandated keeper of the register; key attributes: mandateRef, jurisdiction, delegations
- `registrationDecision`: the registrar's determination on an application; key attributes: outcome, reasons, decidedAt, deciderRef
- `legalEffect`: the consequence an entry produces; key attributes: effectKind, commencesAt, priorityRank
- `objection`: a formal challenge to an entry or decision; key attributes: challenger, grounds, status

## Relationships

- `register` -> maintainedBy -> `registrar` (many-to-one): each register has exactly one accountable keeper
- `registerEntry` -> recordedIn -> `register` (many-to-one): entries live inside one register
- `registerEntry` -> supportedBy -> `evidenceItem` (one-to-many): every entry names the evidence it stands on
- `registrationDecision` -> resolves -> `registrationApplication` (one-to-one): each application ends in one decision
- `registerEntry` -> produces -> `legalEffect` (one-to-many): registration is what makes the effect real
- `objection` -> challenges -> `registerEntry` (many-to-one): entries can be contested after registration

## Events

- `applicationLodged`: an application to register, amend or cancel was received and priority-stamped
- `entryRegistered`: a new entry became authoritative in the register
- `entryAmended`: an existing entry was changed by a registered decision
- `entryCancelled`: an entry was closed and ceased to produce effect
- `objectionRaised`: a party formally contested an entry or a decision
- `decisionIssued`: the registrar determined an application or objection

## Contracts

- `publicInspectionContract`: open read access to the publicity layer of a register, without evidence or restricted attributes
- `certifiedExtractContract`: issuance of an authenticated snapshot of one entry as it stands at a moment
- `bulkAccessContract`: scoped machine access for authorized consumers, bound to purpose and refresh terms
- `correctionRequestContract`: the standing right of an affected party to seek rectification of an entry

## Projections

- `publicRegisterView`: the inspectable face of the register; omits evidence content, applicant details and internal notes
- `certifiedExtract`: a single entry frozen at a point in time with authenticity marks; omits history and pending applications
- `registrarWorklist`: pending applications and objections for the keeper; omits legal-effect and publicity detail

## Composition

- REFERENCE `world.identityRegister` (R4): applicants, registrars and entry subjects resolve to anchored identities
- REFERENCE `world.mandate` (A12): the registrar role is exercised under a mandate governed elsewhere
- COMPOSE `world.eventRegister` (R3): the register's change history is published as an append-only event log with integrity proofs
- EXTEND (inbound): domain registers such as `world.landParcel` (P2), `world.lifeEventsAndCivilStatus` (B12) and `world.identityRegister` (R4) specialize this pattern
- MIX-IN `world.audit` (S4): every registration act and disclosure carries the audit facet
- imports: mu-registry-doctrine (ALIGN): fixes the shared meaning of entry, evidence and effect across the catalogue
- imports: iso-19135 (ALIGN): item registration procedures and register management roles

## Stewardship

The registrar, acting under a mandate (A12), owns the register and answers for the correctness of its entries. Access to entries, evidence and extracts is always granted by the registrar through the catalogue's S1/S2 access and consent models, and every grant and disclosure is auditable via S4.
