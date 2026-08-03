# O5 Commercial Contract & Agreement

This meta-model describes agreements between parties: their formation, the obligations and milestones they create, and the record of performance, amendment, breach and remedy over their life. It is its own model because an agreement is a jointly owned multi-party record with its own lifecycle, referenced by procurement, insurance and price observation without those models needing access to its content.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:o5"
  csn: world.commercialContract
  version: 0.2.0
  displayName: "Commercial Contract & Agreement"
  description: "Formation, obligations, performance, amendment, breach and remedy of agreements between parties."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.commercialContract
bundles:
  - csn: world.commercialContract.formation
    displayName: "Formation"
    layers:
      - world.commercialContract.formation.partiesAndConsent
      - world.commercialContract.formation.termsAndClauses
  - csn: world.commercialContract.obligations
    displayName: "Obligations"
    layers:
      - world.commercialContract.obligations.commitments
      - world.commercialContract.obligations.schedule
  - csn: world.commercialContract.performance
    displayName: "Performance"
    layers:
      - world.commercialContract.performance.fulfilment
      - world.commercialContract.performance.variance
imports:
  - source: uncitral
    version: "*"
  - source: legal-xml
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `formation` | How the agreement came to exist | `partiesAndConsent`: parties, signatures, effective date Â· `termsAndClauses`: the clause structure of the agreed text |
| `obligations` | What the agreement requires | `commitments`: obligations and deliverables owed by each party Â· `schedule`: milestones, deadlines and payment terms |
| `performance` | What actually happened | `fulfilment`: discharge and acceptance of obligations Â· `variance`: amendments, breach, remedy and termination |

## Objects

- `agreement`: the agreement as a whole; key attributes: subject matter class, execution date, effective period, status.
- `contractParty`: a party position in the agreement; key attributes: role (buyer, seller, guarantor), signing capacity, referent link.
- `clause`: an addressable provision; key attributes: citation path, text or hash, clause class.
- `obligation`: a duty created by the agreement; key attributes: description, obligor, due condition, performance status.
- `milestone`: a scheduled point of performance; key attributes: due date, deliverable, acceptance criteria.
- `performanceRecord`: evidence of performance; key attributes: date, obligation link, acceptance state, evidence reference.
- `amendment`: an agreed change; key attributes: effective date, affected clauses, summary of change.
- `remedy`: an agreed or claimed response to non-performance; key attributes: kind (cure, penalty, termination right), status.

## Relationships

- `agreement` -> binds -> `contractParty` (1:n): two or more party positions per agreement.
- `contractParty` -> actsFor -> `world.organization` (n:1): the real party, an organization (O1) or a person (H1).
- `obligation` -> arisesFrom -> `clause` (n:1): the provision creating the duty.
- `obligation` -> owedBy -> `contractParty` (n:1): the obligor position.
- `milestone` -> paces -> `obligation` (n:m): schedule points attached to duties.
- `performanceRecord` -> discharges -> `obligation` (n:1): evidence that a duty was met.
- `amendment` -> modifies -> `agreement` (n:1): the change history.
- `remedy` -> respondsTo -> `obligation` (n:1): the duty whose breach it addresses.

## Events

- `agreementExecuted`: the parties signed and the agreement took effect.
- `obligationFellDue`: a duty became performable or overdue.
- `performanceRendered`: a party performed against an obligation.
- `performanceAccepted`: the counterparty accepted the performance.
- `breachDeclared`: a party declared non-performance.
- `remedyAgreed`: a cure, penalty or other remedy was settled between the parties.
- `agreementAmended`: the parties changed the agreement.
- `agreementTerminated`: the agreement ended by completion, notice or breach.

## Contracts

- `partyMirror`: each party holds the full agreement record; joint facts change only by joint events.
- `counterpartyStatusDisclosure`: consented, limited disclosure of existence and performance standing to credit or rating consumers.
- `adjudicationAccess`: disclosure of the record to a dispute resolution forum once a dispute is escalated (A19).

## Projections

- `obligationLedger`: open obligations with obligors and due dates; omits clause text.
- `performanceScorecard`: fulfilment statistics per party over time; omits amounts and terms.
- `publicSummary`: existence, parties and subject matter class for transparency registers; omits all terms.

## Composition

- REFERENCE `world.organization` (O1) and `world.person` (H1): the real parties behind party positions.
- COMPOSE `world.procurement` (O7): an award there concludes in a new agreement here.
- EXTEND note: `world.insurance` (C8) EXTENDs this model, a policy is a specialized agreement.
- REFERENCE `world.priceValuation` (C7): executed agreements serve as price observation sources under contribution contracts.
- REFERENCE `world.charter` (O4): signing capacity is verified against powers recorded there.
- REFERENCE `world.disputeResolution` (A19): escalated disputes are heard there.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): ownership and access grants over the shared record.
- MIX-IN `world.auditTrail` (S4): audit facets on execution, performance and amendment events.
- imports: uncitral (ALIGN): international contract law vocabulary.
- imports: legal-xml (ALIGN): clause and provision markup for agreed texts.

## Stewardship

The parties own the agreement record jointly, each holding a full mirror; courts and other forums obtain access only through the adjudication contract. Access is granted by the owners under the S1/S2 models of this catalogue.
