# K3 Process & Workflow

This meta-model describes repeatable multi-step activities: the process definitions that say how work flows through steps, roles and states, and the running instances that follow (or deviate from) those definitions. It is separate from the atomic act (K2) because repeatability is its essence: the same definition governs many executions, and the gap between definition and execution is itself information the world needs.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k3"
  csn: world.processAndWorkflow
  version: 0.2.0
  displayName: "Process & Workflow"
  description: "Repeatable multi-step activity definitions and their executions."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.processAndWorkflow
bundles:
  - csn: world.processAndWorkflow.definition
    displayName: "Definition"
    layers:
      - world.processAndWorkflow.definition.processModel
      - world.processAndWorkflow.definition.roleAssignment
      - world.processAndWorkflow.definition.stateModel
  - csn: world.processAndWorkflow.execution
    displayName: "Execution"
    layers:
      - world.processAndWorkflow.execution.caseInstance
      - world.processAndWorkflow.execution.stepPerformance
      - world.processAndWorkflow.execution.exceptionHandling
  - csn: world.processAndWorkflow.improvement
    displayName: "Improvement"
    layers:
      - world.processAndWorkflow.improvement.measurement
      - world.processAndWorkflow.improvement.revision
imports:
  - source: bpmn
    version: "*"
  - source: cmmn
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `definition` | The repeatable model of the work | `processModel`: steps, gateways and sequence flow · `roleAssignment`: which roles perform which steps · `stateModel`: allowed states and transitions of the governed thing |
| `execution` | Running the model in the world | `caseInstance`: one running occurrence of a process · `stepPerformance`: executed steps recorded as acts · `exceptionHandling`: deviations, escalations and compensations |
| `improvement` | Learning from executions | `measurement`: cycle times, throughput and conformance of instances · `revision`: versioning and change of definitions |

## Objects

- `process`: a named repeatable activity definition; key attributes: name, purpose, owner reference, version, trigger
- `step`: one unit of work within a process; key attributes: name, entry and exit conditions, expected duration
- `gateway`: a branching or merging point; key attributes: kind (exclusive, parallel, event based), condition expressions
- `role`: a named performer position in the process; key attributes: name, required capabilities, assignment rule
- `state`: an allowed condition of the case subject; key attributes: name, meaning, permitted transitions
- `processInstance`: one running or completed execution; key attributes: process version, subject reference, start, current state
- `stepExecution`: the performance of one step within an instance; key attributes: step reference, performer, act reference, timestamps
- `deviation`: a departure from the definition; key attributes: kind, cause, resolution, severity

## Relationships

- `process` -> comprises -> `step` (one-to-many): the ordered units the definition is made of
- `step` -> performedBy -> `role` (many-to-many): which roles are eligible to execute the step
- `processInstance` -> instanceOf -> `process` (many-to-one): the definition version being executed
- `stepExecution` -> realizes -> `step` (many-to-one): the definitional step an execution corresponds to
- `stepExecution` -> recordedAs -> `act` (one-to-one): each performed step is an act in K2
- `deviation` -> departsFrom -> `process` (many-to-one): the definition the execution strayed from
- `process` -> codifies -> `method` (many-to-one): the practice or procedure the process operationalizes

## Events

- `processDefined`: a new process definition or version was published
- `instanceStarted`: an execution of a process began for a subject
- `stepCompleted`: a step within an instance finished, with performer and outcome
- `deviationRaised`: an execution departed from its definition and the departure was recorded
- `instanceCompleted`: an execution reached a terminal state
- `processRevised`: a definition was changed and a new version released

## Contracts

- `definitionAccess`: a consumer reads process definitions and versions, without execution data
- `executionMonitoring`: an authorized party observes instance states and step completions for defined processes
- `benchmarkExchange`: aggregated cycle-time and conformance measures are shared in de-identified form

## Projections

- `swimlaneView`: the definition arranged by role; omits execution history
- `statusBoard`: live instances by state and age; omits step-level detail
- `performanceDigest`: throughput, cycle time and deviation rates per version; omits individual cases

## Composition

- REFERENCE `world.actAction` (K2): every step execution resolves to an atomic act
- REFERENCE `world.functionAndCapability` (K1): roles state capability requirements resolved against agent capabilities
- REFERENCE `world.practiceMethodAndProcedure` (K6): processes operationalize codified methods and procedures
- REFERENCE `world.organization` (O1): the process owner and the organizations supplying performers
- imports: bpmn (ALIGN): notation and execution semantics for the process model layer
- imports: cmmn (ALIGN): case management semantics for weakly structured workflows

## Stewardship

The process owner, an organization or an individual agent, owns definitions and their instances' records. Consumers gain access through owner-granted contracts under the catalogue's ownership and access models (S1/S2), with audit via S4.
