# A16 Border Customs & Migration

This meta-model describes what happens at and after the border: crossings of persons, travel document checks, customs declarations with their duty assessments and inspections, and the visa and residency statuses that determine who may enter and remain. It is its own model because border facts join three otherwise separate worlds (persons, goods, legal statuses) at a single point in space and time, and because it carries a distinctive guarantee: each person can always see their own status record.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a16"
  csn: world.borderMigration
  version: 0.2.0
  displayName: Border Customs & Migration
  description: Border crossings, customs declarations, visas and residency statuses.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.borderMigration
bundles:
  - csn: world.borderMigration.crossing
    displayName: Crossing
    layers:
      - world.borderMigration.crossing.entryExit
      - world.borderMigration.crossing.travelDocument
  - csn: world.borderMigration.customs
    displayName: Customs
    layers:
      - world.borderMigration.customs.goodsDeclaration
      - world.borderMigration.customs.dutyAssessment
      - world.borderMigration.customs.inspection
  - csn: world.borderMigration.migrationStatus
    displayName: Migration status
    layers:
      - world.borderMigration.migrationStatus.visa
      - world.borderMigration.migrationStatus.residency
imports:
  - source: wco-data-model
    version: "*"
  - source: icao-doc-9303
    version: "*"
  - source: iso-3166
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `crossing` | Movement of persons across the border | `entryExit`: crossing records at border points Â· `travelDocument`: document presentation and verification |
| `customs` | Movement of goods across the border | `goodsDeclaration`: declared goods and values Â· `dutyAssessment`: duties, taxes, reliefs Â· `inspection`: physical and documentary controls |
| `migrationStatus` | Permission to enter and remain | `visa`: entry permissions and their conditions Â· `residency`: residence statuses and their lifecycle |

## Objects

- `borderCrossing`: one recorded entry or exit of a person; key attributes: personRef, borderPoint, direction, timestamp, outcome
- `travelDocumentCheck`: the verification of a presented document; key attributes: documentIdentifier, issuingCountryCode, validityResult, checkedOn
- `customsDeclaration`: declared goods for import, export or transit; key attributes: declarantRef, goodsItems, declaredValue, procedureCode
- `dutyAssessment`: the duties and taxes computed on a declaration; key attributes: declarationRef, amounts, reliefsApplied, dueOn
- `inspection`: a control act on goods or documents; key attributes: targetRef, inspectionType, finding, completedOn
- `visa`: a permission to enter for a purpose and period; key attributes: holderRef, category, validity, entriesAllowed, conditions
- `residencyStatus`: a status permitting residence; key attributes: holderRef, statusClass, validity, renewalRule
- `statusApplication`: a pending request for a visa or residency status; key attributes: applicantRef, requestedStatus, filedOn, state

## Relationships

- `borderCrossing` -> crossedBy -> `personRef` (N:1): the traveler resolves to a person in P1
- `travelDocumentCheck` -> verifies -> `borderCrossing` (N:1): document checks attach to a crossing record
- `customsDeclaration` -> lodgedFor -> `borderCrossing` (N:0..1): a declaration may accompany a crossing or stand alone for a consignment
- `dutyAssessment` -> assesses -> `customsDeclaration` (1:1): each declaration receives one current assessment
- `inspection` -> examines -> `customsDeclaration` (N:1): controls accumulate on a declaration
- `visa` -> issuedTo -> `personRef` (N:1): the holder resolves to a person
- `residencyStatus` -> heldBy -> `personRef` (N:1): the resident resolves to a person
- `statusApplication` -> requests -> `residencyStatus` (N:1): an application targets one status class, visa applications analogously

## Events

- `crossingRecorded`: a person's entry or exit was recorded at a border point
- `entryRefused`: a crossing was denied and the ground recorded
- `declarationLodged`: a customs declaration was filed
- `dutyAssessed`: duties and taxes on a declaration were computed and became payable
- `inspectionCompleted`: a control act on goods or documents concluded with a finding
- `visaIssued`: an entry permission was granted with its conditions
- `visaRevoked`: an entry permission was withdrawn before expiry
- `residencyGranted`: a residence status became effective for a person

## Contracts

- `selfStatusAccess`: each person's guaranteed view of their own crossings, visas and residency records
- `carrierVerification`: yes-or-no validity checks on documents and visas for transport operators, without record disclosure
- `traderDeclarationAccount`: a declarant's standing access to its own declarations and assessments
- `interAuthorityExchange`: scoped exchange with other authorities of this catalogue under explicit grant

## Projections

- `myStatus`: a person's own statuses, applications and crossings; omits enforcement annotations
- `borderFlowStatistics`: aggregate flows of persons and goods by point and period; omits all identities
- `traderLedger`: declarations, assessments and inspection outcomes for one declarant; omits other parties

## Composition

- REFERENCE `world.person` (P1): travelers, holders and applicants resolve to persons
- EXTEND `world.authorization` (A14): statusApplication and visa issuance specialize the generic application-to-grant process
- REFERENCE `world.grantedRight` (R5): issued visas and residency statuses are recorded as granted rights
- REFERENCE `world.interstateRelations` (A15): visa-waiver and customs regimes derive from treaties in force
- REFERENCE `world.offenseEnforcement` (A18): refusals, seizures and violations hand over to enforcement
- MIX-IN `world.auditTrail` (S4): crossings, checks and assessments are append-only
- imports: wco-data-model (ALIGN): customs declaration and goods-item semantics
- imports: icao-doc-9303 (REFERENCE): machine-readable travel document structure
- imports: iso-3166 (REFERENCE): country and territory code scheme

## Stewardship

The border authority (a mandated operator under A12) stewards crossings, customs and status records. Every person is guaranteed sight of their own status; all other access, including carrier and inter-authority flows, is granted by the owner via S1 and S2.