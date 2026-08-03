# K10 Resource Extraction Operations

This meta-model describes mining, drilling, logging and fishing as operations: the authorization to extract from a commons, the quotas and conditions attached, the campaigns and outputs of extraction, and the restoration duties that follow. It is its own model because extraction is activity against a finite shared stock: the grant, the cap and the duty to restore are as much part of the record as the operation itself.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k10"
  csn: world.resourceExtractionOperations
  version: 0.2.0
  displayName: "Resource Extraction Operations"
  description: "Authorized extraction operations, their outputs, quotas and restoration duties."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.resourceExtractionOperations
bundles:
  - csn: world.resourceExtractionOperations.authorization
    displayName: "Authorization"
    layers:
      - world.resourceExtractionOperations.authorization.grant
      - world.resourceExtractionOperations.authorization.quota
      - world.resourceExtractionOperations.authorization.conditions
  - csn: world.resourceExtractionOperations.operation
    displayName: "Operation"
    layers:
      - world.resourceExtractionOperations.operation.operationRecord
      - world.resourceExtractionOperations.operation.outputMeasurement
  - csn: world.resourceExtractionOperations.restoration
    displayName: "Restoration"
    layers:
      - world.resourceExtractionOperations.restoration.restorationDuty
      - world.resourceExtractionOperations.restoration.restorationProgress
imports:
  - source: unfc
    version: "*"
  - source: fao-fisheries-standards
    version: "*"
  - source: crirsco
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `authorization` | The right to extract and its limits | `grant`: the commons grant or licence under which extraction is allowed Â· `quota`: permitted volumes and periods Â· `conditions`: environmental and safety conditions attached |
| `operation` | The extraction itself | `operationRecord`: mining, drilling, logging or fishing campaigns Â· `outputMeasurement`: extracted volumes, grades and catches |
| `restoration` | What is owed afterwards | `restorationDuty`: obligations to restore or offset Â· `restorationProgress`: acts discharging the duties |

## Objects

- `grant`: the authorization to extract; key attributes: grantor reference, holder reference, resource kind, area or stock, validity
- `quota`: a cap on extraction; key attributes: quantity, unit, period, allocation basis
- `operatingCondition`: an attached obligation; key attributes: kind (environmental, safety, reporting), text, monitoring rule
- `extractionOperation`: a campaign of extraction; key attributes: kind (mine, well, harvest block, fishing trip), site reference, start and end, status
- `outputLot`: a measured quantity extracted; key attributes: resource, quantity, grade or species, date, destination
- `incidentRecord`: an unplanned harmful occurrence; key attributes: kind, severity, date, response
- `restorationDuty`: an obligation triggered by extraction; key attributes: scope, standard to restore to, deadline, security posted
- `restorationAct`: work performed against a duty; key attributes: duty reference, description, date, verified result

## Relationships

- `grant` -> authorizes -> `extractionOperation` (one-to-many): operations run under a grant
- `quota` -> caps -> `grant` (many-to-one): the volume limits attached to the authorization
- `extractionOperation` -> conductedAt -> `site` (many-to-one): where the extraction happens
- `outputLot` -> extractedBy -> `extractionOperation` (many-to-one): the origin of each measured output
- `extractionOperation` -> boundBy -> `restorationDuty` (one-to-many): what the operation owes the commons
- `restorationAct` -> discharges -> `restorationDuty` (many-to-one): progress against the obligation
- `extractionOperation` -> operatedBy -> `organization` (many-to-one): the extracting organization

## Events

- `grantIssued`: an authorization to extract was granted with quotas and conditions
- `operationCommenced`: a campaign of extraction began at a site
- `outputRecorded`: an extracted quantity was measured and logged
- `quotaExceeded`: cumulative output passed a permitted cap
- `incidentReported`: a harmful occurrence during operations was recorded
- `restorationCompleted`: a restoration duty was discharged and verified
- `grantSuspended`: the authorization was paused or withdrawn

## Contracts

- `complianceReturn`: the operator reports outputs against quota and condition adherence to the grantor per cadence
- `publicDisclosure`: grants, quotas and restoration status are published in a public register form
- `siteAccessAgreement`: inspectors or researchers obtain access to operation sites and records under defined terms

## Projections

- `regulatorView`: quota utilization, condition compliance and incidents per grant; omits commercial destinations of output
- `publicRegister`: who may extract what where, and restoration standing; omits operational logs
- `productionStatistics`: aggregate extracted volumes by resource and region; omits individual operators

## Composition

- REFERENCE `world.site` (P5): extraction sites, referenced not duplicated
- REFERENCE `world.ownership` (S1): the commons ownership under which grants are issued
- REFERENCE `world.accessGrant` (S2): the grant instrument itself as an access right over the commons stock
- EXTEND `world.actAction` (K2): operations and restoration acts specialize the atomic act
- REFERENCE `world.productionAndManufacturing` (K8): downstream processing of extracted outputs
- imports: unfc (ALIGN): resource and reserve classification framework
- imports: fao-fisheries-standards (REFERENCE): catch and effort reporting definitions for fishing operations
- imports: crirsco (ALIGN): mineral reporting template vocabulary

## Stewardship

The extracting organization owns its operation records but operates under a commons grant recorded through the catalogue's ownership model (S1); the grantor holds oversight rights defined in the grant. All further access is owner-granted via S1/S2, with audit via S4.
