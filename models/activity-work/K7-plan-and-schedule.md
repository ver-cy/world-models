# K7 Plan & Schedule

This meta-model describes intentions bound to time: plans stating what agents intend to do, commitments that make some intentions binding, and schedules that fix intentions to dates, times, recurrences and orderings. It is its own model because intention is a distinct mode of fact about the world, neither a completed act (K2) nor a standing definition (K3), and the divergence of intention from what later happened is essential information.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k7"
  csn: world.planAndSchedule
  version: 0.2.0
  displayName: "Plan & Schedule"
  description: "Intentions, commitments and their binding to time."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.planAndSchedule
bundles:
  - csn: world.planAndSchedule.intention
    displayName: "Intention"
    layers:
      - world.planAndSchedule.intention.planContent
      - world.planAndSchedule.intention.commitment
      - world.planAndSchedule.intention.assumption
  - csn: world.planAndSchedule.timing
    displayName: "Timing"
    layers:
      - world.planAndSchedule.timing.scheduleEntry
      - world.planAndSchedule.timing.recurrence
      - world.planAndSchedule.timing.dependencyNetwork
  - csn: world.planAndSchedule.revision
    displayName: "Revision"
    layers:
      - world.planAndSchedule.revision.baseline
      - world.planAndSchedule.revision.changeLog
imports:
  - source: icalendar
    version: "*"
  - source: w3c-prov
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `intention` | What is intended and how firmly | `planContent`: intended actions and targets · `commitment`: promises that bind agents to intentions · `assumption`: conditions the plan relies on |
| `timing` | Binding intentions to time | `scheduleEntry`: dated and timed entries · `recurrence`: repeating patterns · `dependencyNetwork`: ordering constraints between planned items |
| `revision` | How the plan changed | `baseline`: frozen versions for comparison · `changeLog`: recorded plan changes and reasons |

## Objects

- `plan`: a coherent set of intentions of an agent; key attributes: name, planning agent, horizon, purpose, status
- `plannedAction`: one intended action; key attributes: intended verb, target, expected effort, priority
- `commitment`: a binding promise about an intention; key attributes: committing agent, beneficiary, terms, penalty or remedy
- `assumption`: a condition the plan relies on; key attributes: statement, sensitivity, monitoring signal
- `scheduleEntry`: a time binding for a planned action; key attributes: start, end, timezone, flexibility
- `recurrenceRule`: a repeat pattern; key attributes: frequency, interval, exceptions, until
- `dependency`: an ordering constraint; key attributes: predecessor, successor, kind (finish-start and variants), lag
- `baseline`: a frozen snapshot of the plan; key attributes: name, freeze date, approver

## Relationships

- `plan` -> contains -> `plannedAction` (one-to-many): the intentions the plan is made of
- `scheduleEntry` -> times -> `plannedAction` (many-to-one): when the intention is meant to happen
- `recurrenceRule` -> repeats -> `scheduleEntry` (one-to-many): the pattern generating occurrences
- `dependency` -> orders -> `plannedAction` (many-to-many): which intentions must precede which
- `commitment` -> binds -> `agent` (many-to-one): the promising party
- `plannedAction` -> realizedBy -> `act` (one-to-many): the recorded acts that later fulfilled the intention
- `baseline` -> freezes -> `plan` (many-to-one): the version comparisons are made against

## Events

- `planAdopted`: a plan was accepted by its planning agent as the current intention
- `commitmentMade`: an intention became a binding promise to another party
- `entryScheduled`: a planned action was fixed to a date and time
- `scheduleShifted`: a time binding was moved, with reason recorded
- `baselineFrozen`: a snapshot of the plan was fixed for later comparison
- `commitmentHonoured`: a promised intention was fulfilled by matching acts
- `planAbandoned`: a plan was dropped before completion

## Contracts

- `calendarSharing`: a consumer reads an agent's schedule entries at an agreed detail level and horizon
- `commitmentDisclosure`: a beneficiary or arbiter verifies the existence and terms of a commitment
- `coordinationFeed`: dependent parties receive changes to entries and dependencies that affect them

## Projections

- `agendaView`: upcoming entries in order; omits assumptions, baselines and change history
- `ganttView`: planned actions, times and dependencies on a bar timeline; omits commitment terms
- `freeBusyView`: availability only; omits all content of the entries

## Composition

- REFERENCE `world.actAction` (K2): acts realize planned actions, letting intention be compared with performance
- REFERENCE `world.project` (K5): projects bind their schedules and baselines from this model
- REFERENCE `world.processAndWorkflow` (K3): recurring operational schedules attach to process definitions
- REFERENCE `world.person` (H1) and `world.organization` (O1): planning and committing agents
- imports: icalendar (ALIGN): calendar entry and recurrence semantics (RFC 5545)
- imports: w3c-prov (ALIGN): the plan concept and its relation to activities

## Stewardship

The planning agent owns its plans, schedules and commitments; beneficiaries hold verification rights over commitments made to them. Access follows owner grants under the catalogue's ownership and access models (S1/S2), with audit via S4.
