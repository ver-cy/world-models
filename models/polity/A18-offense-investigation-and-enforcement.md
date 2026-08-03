# A18 Offense Investigation & Enforcement

This meta-model describes the enforcement path from a recorded offense to a completed correction: classification and incident records, investigations with their evidence custody, charges and their referral into adjudication (A19), and the penalties and correction measures that follow a decision. It is its own model because enforcement records carry the strictest due-process constraints in the catalogue: their subjects hold adversarial rights over them, evidence must keep an unbroken chain of custody, and adjudication itself deliberately lives in a separate model.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a18"
  csn: world.offenseEnforcement
  version: 0.2.0
  displayName: Offense Investigation & Enforcement
  description: Offenses, investigations, charges, penalties and corrections in the enforcement path.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.offenseEnforcement
bundles:
  - csn: world.offenseEnforcement.offense
    displayName: Offense
    layers:
      - world.offenseEnforcement.offense.classification
      - world.offenseEnforcement.offense.incidentRecord
  - csn: world.offenseEnforcement.investigation
    displayName: Investigation
    layers:
      - world.offenseEnforcement.investigation.conduct
      - world.offenseEnforcement.investigation.evidenceCustody
      - world.offenseEnforcement.investigation.chargeAndReferral
  - csn: world.offenseEnforcement.sanction
    displayName: Sanction
    layers:
      - world.offenseEnforcement.sanction.penalty
      - world.offenseEnforcement.sanction.corrections
imports:
  - source: ecris
    version: "*"
  - source: un-iccs
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `offense` | What happened and how it is classified | `classification`: offense types mapped to the reference classification Â· `incidentRecord`: recorded offenses and involved parties |
| `investigation` | Establishing the facts | `conduct`: investigation lifecycle and measures Â· `evidenceCustody`: items, chain of custody, admissibility state Â· `chargeAndReferral`: charges and handover to adjudication |
| `sanction` | Consequences after decision | `penalty`: imposed penalties and their terms Â· `corrections`: execution and supervision of penalties |

## Objects

- `offense`: a recorded instance of prohibited conduct; key attributes: classificationCode, occurredOn, location, involvedPartyRefs, reportingSource
- `investigation`: the inquiry into one or more offenses; key attributes: leadOfficeRef, openedOn, state, measuresTaken
- `evidenceItem`: an item held under chain of custody; key attributes: description, collectedOn, custodyChain, admissibilityState
- `charge`: a formal accusation against a party; key attributes: accusedRef, offenseRefs, filedOn, status
- `caseReference`: the pointer to the adjudication case in A6; key attributes: caseRef, referredOn, outcomeSnapshot
- `penalty`: a sanction imposed through an adjudicated outcome; key attributes: penaltyType, terms, imposedOn, appealState
- `correctionMeasure`: the execution of a penalty; key attributes: penaltyRef, regime, supervisorRef, progressState

## Relationships

- `investigation` -> investigates -> `offense` (N:M): one inquiry may cover several offenses and one offense may see several inquiries
- `evidenceItem` -> heldIn -> `investigation` (N:1): custody attaches to the inquiry that collected the item
- `charge` -> arisesFrom -> `investigation` (N:1): accusations are grounded in investigative findings
- `charge` -> referredAs -> `caseReference` (N:1): a filed charge becomes a case in A6
- `penalty` -> imposedThrough -> `caseReference` (N:1): sanctions are read back from the adjudicated outcome
- `correctionMeasure` -> executes -> `penalty` (N:1): execution and supervision follow the imposed sanction
- `offense` -> classifiedBy -> `offenseClassRef` (N:1): the classification resolves to a code of the reference scheme

## Events

- `offenseRecorded`: an incident was recorded and classified as an offense
- `investigationOpened`: an inquiry was opened into one or more offenses
- `evidenceLogged`: an item entered the chain of custody
- `chargeFiled`: a formal accusation was filed against a party
- `caseReferred`: a charge was handed over to adjudication
- `penaltyImposed`: a sanction from the adjudicated outcome was recorded
- `correctionStarted`: execution of a penalty began under supervision
- `correctionCompleted`: a penalty was fully executed and the record closed to updates

## Contracts

- `subjectDisclosure`: due-process access for the accused and their counsel to charges and disclosable evidence, under rules defined in A6 and enforced as S2 grants
- `interAuthorityConvictionExchange`: structured exchange of final conviction records with counterpart authorities, in the manner of criminal-records exchange systems
- `anonymizedStatisticsExtract`: aggregate extracts by classification, period and area for the statistics office

## Projections

- `convictionRecord`: final penalties per person with their legal state; omits investigation material and dismissed charges
- `crimeStatistics`: aggregates by classification code, period and area; omits all identities
- `caseworkQueue`: open investigations and pending referrals for the enforcement body; omits closed and adjudicated matter

## Composition

- REFERENCE `world.disputeResolution` (A19): charges become cases there, penalties are read back from its outcomes, and due-process rules are defined there
- REFERENCE `world.person` (P1): suspects, victims and witnesses resolve to persons
- REFERENCE `world.publicOffice` (A11): investigative and enforcement powers attach to offices
- REFERENCE `world.authorization` (A14): convictions may ground revocation of grants
- REFERENCE `world.borderMigration` (A16): border violations enter as offenses and outcomes flow back
- MIX-IN `world.auditTrail` (S4): chain of custody and every procedural act are append-only and traceable
- imports: ecris (ALIGN): conviction-exchange record structure
- imports: un-iccs (REFERENCE): the offense classification scheme, referenced by code, never copied

## Stewardship

The enforcement authority stewards investigations and sanctions as a mandated operator. Subjects hold guaranteed due-process access defined in A6 and delivered as S2 grants; all other access, including conviction exchange and statistics, is granted by the owner via S1 and S2 with S4 audit.