# X1 Occurrence / Event

This meta-model is the generic backbone for recording that something happened in the world: what occurred, when, where, who took part, on what evidence, and how one happening relates causally to another. It is its own model so that every timeline in the catalogue shares one shape: specialized event models such as incidents (X3) and interactions (X5) extend it rather than reinventing time, place, participation and causality.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:x1"
  csn: world.occurrenceEvent
  version: 0.2.0
  displayName: "Occurrence / Event"
  description: "Generic happenings: what occurred, when, where, who took part, on what evidence and with what causes."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.occurrenceEvent
bundles:
  - csn: world.occurrenceEvent.happening
    displayName: "Happening"
    layers:
      - world.occurrenceEvent.happening.occurrenceCore
      - world.occurrenceEvent.happening.temporality
      - world.occurrenceEvent.happening.spatiality
  - csn: world.occurrenceEvent.involvement
    displayName: "Involvement"
    layers:
      - world.occurrenceEvent.involvement.participants
      - world.occurrenceEvent.involvement.roles
  - csn: world.occurrenceEvent.explanation
    displayName: "Explanation"
    layers:
      - world.occurrenceEvent.explanation.causality
      - world.occurrenceEvent.explanation.aggregation
imports:
  - source: mu-event
    version: "*"
  - source: owl-time
    version: "*"
  - source: schema-org
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `happening` | The occurrence itself in time and space | `occurrenceCore`: kind, summary, certainty and recording basis · `temporality`: instants, intervals and fuzzy periods · `spatiality`: where it happened, at any granularity |
| `involvement` | Who or what took part | `participants`: parties and objects involved · `roles`: the capacity in which each participant acted |
| `explanation` | How happenings connect and compose | `causality`: asserted cause and contribution links · `aggregation`: episodes grouping related occurrences |

## Objects

- `occurrence`: a discrete thing that happened; key attributes: occurrenceKind, summary, certainty, recordedAt
- `participation`: one party's involvement in an occurrence; key attributes: partyRef, role, presence
- `timeSpecification`: when it happened, as an instant, interval or fuzzy period; key attributes: begin, end, precision
- `placeSpecification`: where it happened, as an address, geocode, feature or region reference; key attributes: placeRef, granularity
- `causalLink`: an asserted cause or contribution between occurrences; key attributes: linkKind, confidence, assertedBy
- `episode`: a composite occurrence grouping related occurrences into a narrative unit; key attributes: episodeKind, memberCount, span
- `sourceRecord`: the account or evidence from which the occurrence was recorded; key attributes: sourceKind, reportedAt, reliability

## Relationships

- `occurrence` -> involved -> `participation` (1:n): the set of parties and objects taking part
- `occurrence` -> happenedAt -> `timeSpecification` (1:1): every occurrence carries exactly one temporal statement
- `occurrence` -> happenedIn -> `placeSpecification` (n:1): places resolve through U7 references at the stated granularity
- `causalLink` -> relates -> `occurrence` (n:m): cause and contribution assertions form a graph over occurrences
- `episode` -> comprises -> `occurrence` (1:n): composite narrative units aggregate member occurrences
- `occurrence` -> reportedBy -> `sourceRecord` (n:m): multiple independent sources can report the same happening

## Events

- `occurrenceRecorded`: a happening was entered into the record from a source
- `occurrenceCorroborated`: an additional independent source confirmed the happening and certainty rose
- `occurrenceAmended`: the recorded facts of a happening were corrected
- `occurrenceDisputed`: a party formally contested the recorded account
- `occurrenceLinked`: a causal or episodic link between occurrences was asserted

## Contracts

- `timelineAccessGrant`: a participant grants access to occurrences they took part in, per S2
- `corroborationExchange`: registrars exchange source records to raise or resolve certainty
- `openChronicleLicense`: public occurrences released as an open chronicle

## Projections

- `personalTimelineProjection`: one party's occurrences in time order; omits other participants' private details
- `publicChronicleProjection`: public occurrences only; omits non-consenting participants entirely
- `causalGraphProjection`: occurrences and their causal links; omits participation detail

## Composition

- EXTEND (as base): `world.incidentEmergency` (X3) and `world.encounterInteraction` (X5) EXTEND this model with response and mutuality semantics respectively
- REFERENCE `world.observedPhenomenon` (X2): recurring patterns are instantiated by individual occurrences recorded here
- REFERENCE `world.situationCondition` (X4): occurrences open, advance and close situations
- REFERENCE `world.addressLocationReferencing` (U7): place specifications resolve to addresses, geocodes and POIs
- REFERENCE `world.person` (H1): human participants in participation records
- REFERENCE `world.organization` (O1): organizational participants
- REFERENCE `world.auditTrail` (S4): record-keeping actions over occurrences are audited there
- imports: mu-event (ALIGN: interoperable event vocabulary)
- imports: owl-time (COMPOSE: temporal instant and interval value types)
- imports: schema-org (ALIGN: Event typing for public chronicles)

## Stewardship

The owner archetype is the primary actor of the occurrence, or the observing registrar when no actor records it. Each participant controls disclosure of their own participation through S2 grants, and the steward's record-keeping is itself auditable via S4.