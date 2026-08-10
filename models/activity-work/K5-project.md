# K5 Project

This meta-model describes bounded undertakings: endeavours with a stated goal, a beginning and an intended end, structured into deliverables, milestones and work packages, and resourced by allocations of people, money and assets. It is distinct from process (K3) because a project is unique rather than repeatable, and distinct from plan (K7) because a project is the undertaking itself, not only the intention.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k5"
  csn: world.project
  version: 0.2.0
  displayName: "Project"
  description: "Bounded undertakings with goals, structure, resources and progress."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.project
bundles:
  - csn: world.project.intent
    displayName: "Intent"
    layers:
      - world.project.intent.goal
      - world.project.intent.scope
  - csn: world.project.structure
    displayName: "Structure"
    layers:
      - world.project.structure.breakdown
      - world.project.structure.resourceAllocation
  - csn: world.project.progress
    displayName: "Progress"
    layers:
      - world.project.progress.milestoneTracking
      - world.project.progress.riskAndIssue
imports:
  - source: w3c-prov
    version: "*"
  - source: pmbok
    version: "*"
  - source: iso-21502
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `intent` | Why the undertaking exists and where it ends | `goal`: objectives and success criteria · `scope`: deliverables, boundaries and exclusions |
| `structure` | How the undertaking is organized and fed | `breakdown`: phases, milestones and work packages · `resourceAllocation`: people, budget and assets assigned to work |
| `progress` | How the undertaking is actually going | `milestoneTracking`: reached and slipped milestones · `riskAndIssue`: threats, problems and their handling |

## Objects

- `project`: the bounded undertaking; key attributes: name, sponsor reference, charter date, planned start and end, status
- `goal`: an objective with success criteria; key attributes: statement, measure, target, priority
- `deliverable`: a defined output; key attributes: name, acceptance criteria, due milestone, state
- `milestone`: a dated checkpoint; key attributes: name, planned date, actual date, gate criteria
- `workPackage`: a unit of assignable work; key attributes: name, scope, effort estimate, responsible role
- `resourceAllocation`: assignment of a resource to work; key attributes: resource reference, work package, quantity, period
- `risk`: an uncertain threat to the undertaking; key attributes: description, likelihood, impact, response, owner
- `statusReport`: a periodic account of progress; key attributes: period, accomplishments, forecast, concerns

## Relationships

- `project` -> pursues -> `goal` (one-to-many): the objectives the undertaking exists for
- `project` -> comprises -> `workPackage` (one-to-many): the breakdown of the work
- `workPackage` -> targets -> `milestone` (many-to-one): the checkpoint the work drives toward
- `deliverable` -> producedBy -> `workPackage` (many-to-one): where the output comes from
- `resourceAllocation` -> assigns -> `agent` (many-to-one): the person, team or asset committed
- `project` -> sponsoredBy -> `organization` (many-to-one): who charters and funds the undertaking
- `workPackage` -> executedThrough -> `act` (one-to-many): the recorded acts that performed the work
- `risk` -> threatens -> `milestone` (many-to-many): which checkpoints the risk endangers

## Events

- `projectChartered`: the undertaking was authorized with goals, scope and sponsor
- `milestoneReached`: a checkpoint was passed, with actual date and gate result
- `allocationChanged`: resources were added, moved or withdrawn
- `riskRaised`: a new threat was identified and logged
- `deliverableAccepted`: an output met its acceptance criteria
- `projectClosed`: the undertaking ended, whether completed, merged or abandoned

## Contracts

- `charterAccess`: a consumer reads goals, scope and structure of a project
- `progressReporting`: the sponsor or an oversight body receives periodic status per agreed cadence and detail
- `resourceCommitment`: a resource-owning party binds an allocation of people, funds or assets to the project for a period

## Projections

- `portfolioView`: many projects by status, spend and milestone health; omits work-package detail
- `roadmapView`: milestones and deliverables on a time axis; omits allocations and risks
- `sponsorReport`: progress against goals with top risks; omits day-to-day execution records

## Composition

- REFERENCE `world.organization` (O1): the sponsoring organization and contributing parties
- REFERENCE `world.person` (H1): members engaged through allocations
- REFERENCE `world.planAndSchedule` (K7): the project's plan and schedule are held in the plan model and bound here
- REFERENCE `world.actAction` (K2): performed work resolves to acts
- REFERENCE `world.processAndWorkflow` (K3): repeatable procedures used inside the unique undertaking
- imports: w3c-prov (ALIGN): plans, activities and attribution semantics
- imports: pmbok (REFERENCE): project management practice vocabulary for breakdown and risk
- imports: iso-21502 (ALIGN): project governance and lifecycle terminology

## Stewardship

The sponsoring organization owns the project record; contributing parties own their own allocation data. Access is granted by the owner through the catalogue's ownership and access models (S1/S2), with audit via S4.
