# K8 Production & Manufacturing

This meta-model describes the transformation of materials into goods: product specifications, bills of materials and routings on the definition side, and production runs, batches, material consumption, yield and quality on the execution side. It is its own model because industrial transformation has structures no generic act or process captures: lot genealogy, yield accounting and the strict pairing of a recipe with its runs.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k8"
  csn: world.productionAndManufacturing
  version: 0.2.0
  displayName: "Production & Manufacturing"
  description: "Product definitions, production runs, batches, yield and quality."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.productionAndManufacturing
bundles:
  - csn: world.productionAndManufacturing.definition
    displayName: "Definition"
    layers:
      - world.productionAndManufacturing.definition.productSpecification
      - world.productionAndManufacturing.definition.billOfMaterials
      - world.productionAndManufacturing.definition.routing
  - csn: world.productionAndManufacturing.execution
    displayName: "Execution"
    layers:
      - world.productionAndManufacturing.execution.productionRun
      - world.productionAndManufacturing.execution.batchAndLot
      - world.productionAndManufacturing.execution.resourceUsage
  - csn: world.productionAndManufacturing.performance
    displayName: "Performance"
    layers:
      - world.productionAndManufacturing.performance.yieldAndScrap
      - world.productionAndManufacturing.performance.qualityControl
imports:
  - source: isa-95
    version: "*"
  - source: gs1
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `definition` | What to make and how | `productSpecification`: the good and its required properties Â· `billOfMaterials`: components and quantities per unit Â· `routing`: ordered operations on work centres |
| `execution` | Making it | `productionRun`: orders and runs executing a specification Â· `batchAndLot`: traceable produced units Â· `resourceUsage`: materials consumed, machine and labour time |
| `performance` | What the making yielded | `yieldAndScrap`: good output versus loss Â· `qualityControl`: tests, results and dispositions |

## Objects

- `productSpecification`: the definition of a good; key attributes: name, identifier, required properties, unit of measure, version
- `billOfMaterials`: the component recipe; key attributes: specification reference, component lines with quantities, effectivity
- `routingOperation`: one manufacturing step; key attributes: sequence, work centre, duration standard, instructions reference
- `productionRun`: one execution of a specification; key attributes: order reference, plant reference, planned and actual quantity, start and end
- `batch`: a traceable unit of output; key attributes: lot identifier, quantity, production run reference, expiry or shelf data
- `materialConsumption`: input drawn during a run; key attributes: input lot reference, quantity, operation, time
- `yieldRecord`: the output accounting of a run; key attributes: good quantity, scrap quantity, loss reasons
- `qualityTest`: an inspection of a batch or run; key attributes: test kind, sample, result, disposition

## Relationships

- `billOfMaterials` -> specifies -> `productSpecification` (many-to-one): the recipe for the good
- `routingOperation` -> sequencedFor -> `productSpecification` (many-to-one): the ordered making steps
- `productionRun` -> executes -> `productSpecification` (many-to-one): the definition a run realizes
- `productionRun` -> conductedAt -> `site` (many-to-one): the plant where making happened
- `batch` -> producedBy -> `productionRun` (many-to-one): the origin of each traceable lot
- `materialConsumption` -> drewFrom -> `batch` (many-to-one): input lot genealogy
- `qualityTest` -> inspected -> `batch` (many-to-one): quality evidence per lot
- `productionRun` -> performedBy -> `organization` (many-to-one): the producing organization

## Events

- `runStarted`: a production run began against a specification and routing
- `operationCompleted`: one routing operation of a run finished
- `materialConsumed`: an input lot was drawn into a run
- `batchProduced`: a traceable output lot came into existence
- `testResultRecorded`: a quality test on a batch or run was concluded
- `runClosed`: a run ended with its yield accounted
- `batchRecalled`: a produced lot was withdrawn after release

## Contracts

- `traceabilityQuery`: an authorized party traverses lot genealogy from a batch to its inputs and back, without cost or recipe detail
- `productionReporting`: aggregate output and yield are disclosed to a statistics office or supply chain partner per cadence
- `recipeLicense`: a specification, bill of materials and routing are licensed to another producer under the author's terms

## Projections

- `genealogyTrace`: the input-to-output lot tree around a batch; omits costs and recipes
- `plantDashboard`: runs, yields and quality by line and shift; omits partner-facing identifiers
- `complianceReport`: quality results and dispositions shaped for oversight; omits commercial quantities

## Composition

- EXTEND `world.actAction` (K2): production runs and operations specialize the atomic act with industrial structure
- REFERENCE `world.site` (P5): plants and work centres as sites
- REFERENCE `world.organization` (O1): producing organizations and supply chain partners
- REFERENCE `world.processAndWorkflow` (K3): routings operationalized as executable workflows
- REFERENCE `world.practiceMethodAndProcedure` (K6): work instructions behind routing operations
- REFERENCE `world.planAndSchedule` (K7): production schedules binding runs to time
- imports: isa-95 (ALIGN): manufacturing operations terminology and level model
- imports: gs1 (REFERENCE): identifier schemes for products, lots and locations (GTIN, GLN, SSCC)

## Stewardship

The producing organization owns its specifications, runs and lot records. Trace, reporting and licensing access is granted by the owner via the catalogue's ownership and access models (S1/S2), with audit via S4.
