# K2 Act / Action

This meta-model describes atomic actions in the world: who did what, to what, when, where, and with what outcome. It is the smallest unit of activity and the backbone every other activity model builds on: processes, projects, production runs, farm operations and care encounters are all, at bottom, structured collections of acts. Keeping the act atomic and separately modelled lets every domain record activity in one comparable shape.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k2"
  csn: world.actAction
  version: 0.2.0
  displayName: "Act / Action"
  description: "Atomic actions with actor, object, time, place and outcome."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.actAction
bundles:
  - csn: world.actAction.occurrence
    displayName: "Occurrence"
    layers:
      - world.actAction.occurrence.actRecord
      - world.actAction.occurrence.context
      - world.actAction.occurrence.outcome
  - csn: world.actAction.participation
    displayName: "Participation"
    layers:
      - world.actAction.participation.actorRole
      - world.actAction.participation.objectInvolvement
  - csn: world.actAction.accountability
    displayName: "Accountability"
    layers:
      - world.actAction.accountability.attribution
      - world.actAction.accountability.derivation
imports:
  - source: w3c-prov
    version: "*"
  - source: mu-event
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `occurrence` | The act as a dated, placed happening | `actRecord`: actor, verb, object, time, place of the act Â· `context`: setting, instrument, motive or trigger Â· `outcome`: result, effect and completion status |
| `participation` | Who and what took part | `actorRole`: roles agents played in the act Â· `objectInvolvement`: things acted upon, consumed or used |
| `accountability` | Responsibility and lineage | `attribution`: responsibility and delegation for the act Â· `derivation`: which acts caused, informed or followed which |

## Objects

- `act`: one atomic action; key attributes: verb, start and end time, place reference, status, description
- `actClass`: the typed verb an act instantiates; key attributes: name, definition, domain, expected participants
- `participation`: an agent's involvement in an act; key attributes: agent reference, role, degree of involvement
- `involvedObject`: a thing the act touched; key attributes: object reference, involvement kind (target, instrument, input, output)
- `outcome`: the observed result of the act; key attributes: result kind, description, measurements, success flag
- `attributionRecord`: assignment of responsibility; key attributes: responsible agent, delegating agent, basis
- `derivationLink`: a lineage tie between two acts; key attributes: source act, derived act, derivation kind

## Relationships

- `act` -> instanceOf -> `actClass` (many-to-one): the verb taxonomy the act belongs to
- `participation` -> involves -> `agent` (many-to-one): the person or organization that took part
- `act` -> actedUpon -> `involvedObject` (one-to-many): the things targeted, consumed or used
- `act` -> occurredAt -> `place` (many-to-one): where the act happened, resolved against place models
- `act` -> producedOutcome -> `outcome` (one-to-many): what resulted
- `derivationLink` -> derivesFrom -> `act` (many-to-one): the earlier act this one was caused or informed by
- `attributionRecord` -> assignsResponsibilityTo -> `agent` (many-to-one): who answers for the act

## Events

- `actRecorded`: an act was captured into the record with its participants, time and place
- `outcomeObserved`: the result of a previously recorded act was observed and attached
- `attributionAsserted`: responsibility for an act was assigned or delegated
- `derivationEstablished`: a lineage link between two acts was recorded
- `actCorrected`: a recorded act was amended, with the prior version preserved
- `actRetracted`: a recorded act was withdrawn as erroneous

## Contracts

- `actLogAccess`: a consumer reads a defined slice of an agent's act log for a stated purpose and period
- `provenanceQuery`: a consumer traverses derivation links to answer where a result came from, without seeing unrelated acts
- `correctionSubmission`: a participant submits corrections or retractions to acts it took part in, under review by the record owner

## Projections

- `timelineView`: chronological acts of an agent or object; omits attribution and derivation internals
- `provenanceGraph`: the derivation network around a chosen act or outcome; omits context detail
- `activitySummary`: counts and rates of acts by class and period; omits individual acts

## Composition

- REFERENCE `world.person` (H1): persons as actors and responsible parties
- REFERENCE `world.organization` (O1): organizations as actors and delegators
- REFERENCE `world.site` (P5): sites and places where acts occurred
- REFERENCE `world.functionAndCapability` (K1): the verb an act instantiates presumes a capability of the actor
- imports: w3c-prov (ALIGN): activity, agent and derivation semantics aligned with PROV
- imports: mu-event (ALIGN): the standard's core event concept, so acts publish as timeline-recordable events

## Stewardship

The acting agent owns the record of its own acts; participants hold correction rights over their participation. Access to act logs and provenance is granted by the owner via the catalogue's ownership and access models (S1/S2), with audit via S4.
