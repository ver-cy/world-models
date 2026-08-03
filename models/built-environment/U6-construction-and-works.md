# U6 Construction & Works

This meta-model describes construction projects and works in progress: the definition of an undertaking, its permits, staged execution, inspections, acceptance and defects. It is its own model because works are temporary undertakings with their own parties, authorizations and risks, whose finished products graduate into the permanent records of U1 buildings and U3 networks.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:u6"
  csn: world.constructionWorks
  version: 0.2.0
  displayName: "Construction & Works"
  description: "Construction projects and works in progress: definition, permitting, staged execution, acceptance and defects."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.constructionWorks
bundles:
  - csn: world.constructionWorks.undertaking
    displayName: "Undertaking"
    layers:
      - world.constructionWorks.undertaking.workDefinition
      - world.constructionWorks.undertaking.permitting
  - csn: world.constructionWorks.execution
    displayName: "Execution"
    layers:
      - world.constructionWorks.execution.stages
      - world.constructionWorks.execution.progress
  - csn: world.constructionWorks.completion
    displayName: "Completion"
    layers:
      - world.constructionWorks.completion.acceptance
      - world.constructionWorks.completion.defects
imports:
  - source: ifc
    version: "*"
  - source: iso-19650
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `undertaking` | What is to be built and under what authorization | `workDefinition`: the scope, kind and planned timeline of the work Â· `permitting`: authorizations, their conditions and validity |
| `execution` | How the work advances on site | `stages`: defined phases from groundworks to fit out Â· `progress`: dated statements of physical completion |
| `completion` | How the work concludes and its quality is settled | `acceptance`: the act admitting the product into service Â· `defects`: nonconformities found in execution and warranty |

## Objects

- `work`: a construction or civil engineering undertaking; key attributes: workKind, plannedStart, plannedEnd, status
- `permit`: an authorization to carry out defined works; key attributes: permitKind, issuedAt, validUntil, conditions
- `stage`: a defined phase of a work; key attributes: sequence, plannedInterval, status
- `progressRecord`: a dated statement of physical completion; key attributes: recordedAt, percentComplete, method
- `inspection`: a formal examination of works at a point in time; key attributes: inspectedAt, scope, verdict
- `acceptanceRecord`: the act closing a work and admitting its product into service; key attributes: acceptedAt, acceptedBy, reservations
- `defect`: a nonconformity found during execution or warranty; key attributes: foundAt, severity, rectifiedAt

## Relationships

- `work` -> authorizedBy -> `permit` (n:m): a work can require several permits; a permit can cover several works
- `work` -> producesOrAlters -> `building` (n:m): the U1 artifacts the work creates, alters or demolishes
- `work` -> occursOn -> `landParcel` (n:m): the P2 parcels forming the site
- `stage` -> partOf -> `work` (n:1): the phase breakdown of the undertaking
- `inspection` -> examines -> `stage` (n:1): each inspection targets a work or one of its stages
- `defect` -> foundDuring -> `inspection` (n:1): defects trace back to the examination that surfaced them
- `acceptanceRecord` -> concludes -> `work` (1:1): one closing act per work

## Events

- `permitGranted`: an authorization was issued for defined works
- `worksCommenced`: physical execution started on site
- `stageCompleted`: a defined phase reached completion
- `inspectionHeld`: a formal examination took place and a verdict was recorded
- `worksSuspended`: execution was halted, with the ground for suspension recorded
- `worksAccepted`: the product was admitted into service and handed over
- `defectRectified`: a recorded nonconformity was corrected and verified

## Contracts

- `permitStatusDisclosure`: public disclosure of permit and works status for a site
- `contractorDataExchange`: exchange of stage, progress and defect data between the developer and its contractors
- `handoverPackageContract`: delivery of as-built data to the U1 record of the resulting artifact at acceptance

## Projections

- `publicWorksBoardProjection`: what is being built where, with permit status; omits commercial terms and party detail
- `completionCertificateProjection`: the acceptance record with reservations; omits execution history
- `siteTimelineProjection`: stages and progress in time order; omits defect detail

## Composition

- REFERENCE `world.buildingStructure` (U1): the permanent artifacts produced or altered; acceptance here raises the structureCommissioned event there
- REFERENCE `world.landParcelCadastre` (P2): the site parcels and any easements needed for the works
- REFERENCE `world.addressLocationReferencing` (U7): site addresses and access points
- REFERENCE `world.incidentEmergency` (X3): site incidents during execution are recorded there
- REFERENCE `world.organization` (O1): developer, contractor and inspecting parties
- REFERENCE `world.publicMandate` (A cluster): permits are issued under a public permitting mandate recorded there
- imports: ifc (EXTEND: process, task and work schedule entities)
- imports: iso-19650 (ALIGN: information management over the delivery phase)

## Stewardship

The owner archetype is the developer organization, which stewards the work record from definition to acceptance; permits are stewarded by the permitting authority under its public mandate (A cluster). At acceptance the as-built data passes to the S1 owner of the resulting artifact, and all access along the way is granted per S1/S2.