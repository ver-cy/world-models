# X4 Situation & Condition

This meta-model describes states of affairs that hold over time: a road is closed, a building is condemned, a supply is suspended, a district is under alert. It is the complement of the occurrence model: X1 records the instants at which the world changes, while this model records what holds between those instants, bound to a subject, valued with a status and bounded by a validity interval.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:x4"
  csn: world.situationCondition
  version: 0.2.0
  displayName: "Situation & Condition"
  description: "States of affairs holding over time: subject, status, validity interval and the transitions between states."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.situationCondition
bundles:
  - csn: world.situationCondition.state
    displayName: "State"
    layers:
      - world.situationCondition.state.situationCore
      - world.situationCondition.state.status
  - csn: world.situationCondition.temporality
    displayName: "Temporality"
    layers:
      - world.situationCondition.temporality.interval
      - world.situationCondition.temporality.succession
  - csn: world.situationCondition.attachment
    displayName: "Attachment"
    layers:
      - world.situationCondition.attachment.subjectBinding
      - world.situationCondition.attachment.scope
imports:
  - source: owl-time
    version: "*"
  - source: iso-8601
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `state` | What holds and how it is valued | `situationCore`: the named state of affairs and its kind · `status`: terms drawn from governed status schemes |
| `temporality` | When the state holds and how states succeed one another | `interval`: the validity span, possibly open-ended · `succession`: transitions from one status to the next |
| `attachment` | What the state is about and how far it reaches | `subjectBinding`: the link to the catalogue entity the state holds for · `scope`: the spatial or organizational reach of the state |

## Objects

- `situation`: a named state of affairs holding for a subject over an interval; key attributes: situationKind, openedAt, closedAt, currentStatus
- `subjectBinding`: the link from the situation to the catalogue entity it holds for; key attributes: subjectRef, subjectModel, bindingBasis
- `statusValue`: a term from a governed status scheme; key attributes: scheme, term, ordering
- `validityInterval`: the time span over which the situation holds; key attributes: begin, end, openEnded
- `stateTransition`: the change from one status to the next; key attributes: occurredAt, fromStatus, toStatus, triggerRef
- `situationScope`: the spatial or organizational reach of the situation; key attributes: scopeKind, scopeRef

## Relationships

- `situation` -> boundTo -> `subjectBinding` (1:1): every situation holds for exactly one bound subject
- `situation` -> valuedAs -> `statusValue` (n:1): the current status is a term from a declared scheme
- `situation` -> holdsDuring -> `validityInterval` (1:1): the span of validity, open-ended while the state persists
- `stateTransition` -> advances -> `situation` (n:1): the ordered history of status changes
- `stateTransition` -> triggeredBy -> `occurrence` (n:1): X1 occurrences open, advance and close situations
- `situation` -> scopedBy -> `situationScope` (n:1): where or over whom the state applies

## Events

- `situationOpened`: a state of affairs began to hold for a subject
- `statusChanged`: the situation moved to a different status term
- `intervalRevised`: the validity span was corrected on better information
- `situationClosed`: the state ceased to hold and the interval was sealed
- `situationBackdated`: a state was recorded retroactively with an earlier begin

## Contracts

- `statusAttestationContract`: the subject's owner attests the current status to a named relying party
- `monitoringSubscription`: a consumer is notified on transitions of situations it is entitled to see
- `historyAccessGrant`: owner-granted access to the full transition history of a situation

## Projections

- `currentStateProjection`: the latest status per subject only; omits history and triggering evidence
- `stateHistoryProjection`: the full ledger of transitions with triggers; omits unrelated subjects entirely
- `statusBadgeProjection`: a single flag or grade for display; omits everything else

## Composition

- REFERENCE `world.occurrenceEvent` (X1): occurrences are the triggers that open, advance and close situations
- REFERENCE `world.buildingStructure` (U1): typical built subjects such as condemned or protected structures
- REFERENCE `world.physicalInfrastructureNetwork` (U3): closures and restrictions on network assets held as situations
- REFERENCE `world.observedPhenomenon` (X2): persistent phenomena mirrored as situations over an extent
- REFERENCE `world.person` (H1): personal states such as residency held for a person subject
- REFERENCE `world.organization` (O1): organizational states such as active or dissolved
- imports: owl-time (COMPOSE: interval value types for validity spans)
- imports: iso-8601 (ALIGN: interval and timestamp notation)

## Stewardship

The owner archetype is the subject's owner: whoever holds the S1 ownership of the bound entity stewards situations about it. Attestations, monitoring and history access are all granted by that owner through S2, and every transition is auditable via S4.