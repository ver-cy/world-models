# K11 Maintenance & Repair

This meta-model describes the upkeep of assets and infrastructure: knowing the condition of a thing, planning its maintenance, ordering the work, performing it and recording the change in condition that resulted. It is its own model because upkeep is a standing relationship between an agent and an asset over the asset's whole life, with its own vocabulary of condition, failure, work order and intervention that neither generic acts (K2) nor services (K4) carry.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k11"
  csn: world.maintenanceAndRepair
  version: 0.2.0
  displayName: "Maintenance & Repair"
  description: "Asset condition, maintenance programs, interventions and condition change."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.maintenanceAndRepair
bundles:
  - csn: world.maintenanceAndRepair.assetCondition
    displayName: "Asset condition"
    layers:
      - world.maintenanceAndRepair.assetCondition.conditionAssessment
      - world.maintenanceAndRepair.assetCondition.failureMode
  - csn: world.maintenanceAndRepair.program
    displayName: "Program"
    layers:
      - world.maintenanceAndRepair.program.maintenancePlan
      - world.maintenanceAndRepair.program.workOrder
  - csn: world.maintenanceAndRepair.intervention
    displayName: "Intervention"
    layers:
      - world.maintenanceAndRepair.intervention.maintenanceAct
      - world.maintenanceAndRepair.intervention.conditionDelta
      - world.maintenanceAndRepair.intervention.sparePartUsage
imports:
  - source: iso-55000
    version: "*"
  - source: en-13306
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `assetCondition` | Knowing the state of the asset | `conditionAssessment`: inspections and measured condition · `failureMode`: defects, degradation patterns and their causes |
| `program` | Deciding and ordering upkeep | `maintenancePlan`: strategies, intervals and triggers per asset class · `workOrder`: authorized, scheduled maintenance tasks |
| `intervention` | Doing the work and its effect | `maintenanceAct`: performed inspection, service or repair · `conditionDelta`: before and after condition change · `sparePartUsage`: parts and materials consumed |

## Objects

- `conditionAssessment`: a dated judgement of an asset's state; key attributes: asset reference, method, measured values, condition grade
- `defect`: an identified fault; key attributes: asset reference, description, severity, detection date, status
- `failureMode`: a recurring pattern of degradation; key attributes: name, mechanism, symptoms, affected asset classes
- `maintenancePlan`: the upkeep strategy for an asset or class; key attributes: strategy kind (preventive, condition based, corrective), intervals, triggers
- `workOrder`: an authorized maintenance task; key attributes: asset reference, task, priority, planned window, assigned performer
- `maintenanceAct`: performed maintenance work; key attributes: work order reference, performer, start and end, findings
- `conditionDelta`: the state change an act produced; key attributes: prior grade, posterior grade, measures, residual issues
- `sparePartUsage`: material consumed in an act; key attributes: part identifier, quantity, source lot, cost basis

## Relationships

- `conditionAssessment` -> assesses -> `asset` (many-to-one): the owned thing whose state is judged, resolved via the ownership register
- `defect` -> exhibits -> `failureMode` (many-to-one): the pattern a fault instantiates
- `workOrder` -> plannedBy -> `maintenancePlan` (many-to-one): the strategy that generated the task
- `maintenanceAct` -> executes -> `workOrder` (many-to-one): the performance of the ordered task
- `maintenanceAct` -> remedied -> `defect` (many-to-many): faults the intervention addressed
- `conditionDelta` -> resultOf -> `maintenanceAct` (one-to-one): the effect of the work on the asset's state
- `sparePartUsage` -> consumedIn -> `maintenanceAct` (many-to-one): materials the work used

## Events

- `assessmentPerformed`: an asset's condition was inspected and graded
- `defectDetected`: a fault was found and logged
- `workOrderIssued`: a maintenance task was authorized and scheduled
- `maintenanceCompleted`: an intervention finished with findings recorded
- `conditionDeltaRecorded`: the before and after state change was captured
- `partReplaced`: a component was exchanged during an intervention
- `assetReturnedToService`: the asset resumed operation after work

## Contracts

- `maintenanceServiceAgreement`: an owner engages a contracted operator to maintain defined assets to a plan and response times
- `conditionDataSharing`: condition histories are shared with insurers, buyers or engineers under the owner's terms
- `warrantyClaimSupport`: acts, parts and deltas for a covered asset are disclosed to a warrantor for a claim

## Projections

- `assetHealthDashboard`: current condition grades and open defects across a portfolio; omits work order internals
- `backlogView`: open and overdue work orders by priority; omits historical acts
- `historyLog`: the full intervention and condition record of one asset; omits other assets

## Composition

- EXTEND `world.actAction` (K2): maintenance acts specialize the atomic act with condition effect
- REFERENCE `world.ownership` (S1): the asset and its owner are resolved through the ownership register, never duplicated here
- REFERENCE `world.planAndSchedule` (K7): maintenance intervals and windows bind to schedules
- REFERENCE `world.practiceMethodAndProcedure` (K6): task procedures behind work orders
- REFERENCE `world.service` (K4): contracted maintenance delivered as a service offering
- REFERENCE `world.organization` (O1): contracted operators and part suppliers
- imports: iso-55000 (ALIGN): asset management vocabulary and lifecycle framing
- imports: en-13306 (ALIGN): maintenance terminology for acts, strategies and failures

## Stewardship

The asset owner owns the maintenance record; a contracted operator holds delegated write access for the assets it services. All access flows from owner grants under the catalogue's ownership and access models (S1/S2), with audit via S4.
