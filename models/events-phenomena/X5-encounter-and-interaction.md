# X5 Encounter & Interaction

This meta-model describes meetings, transactions and encounters between agents: bounded interactions with two or more parties, the channel they used, what passed between them, the outcome they reached, and the mutually acknowledged record of it all. It is its own model, extending the generic occurrence (X1), because interactions are inherently multi-perspective: each party owns its own view, and the countersigned mutual record is a first-class artifact that no single-actor event model provides.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:x5"
  csn: world.encounterInteraction
  version: 0.2.0
  displayName: "Encounter & Interaction"
  description: "Meetings, transactions and encounters between agents: parties, channel, exchanged items, outcomes and mutual records."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.encounterInteraction
bundles:
  - csn: world.encounterInteraction.interaction
    displayName: "Interaction"
    layers:
      - world.encounterInteraction.interaction.interactionCore
      - world.encounterInteraction.interaction.channel
  - csn: world.encounterInteraction.parties
    displayName: "Parties"
    layers:
      - world.encounterInteraction.parties.partyRoles
      - world.encounterInteraction.parties.mutuality
  - csn: world.encounterInteraction.outcome
    displayName: "Outcome"
    layers:
      - world.encounterInteraction.outcome.outcomes
      - world.encounterInteraction.outcome.followUp
imports:
  - source: w3c-prov
    version: "*"
  - source: schema-org
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `interaction` | The encounter itself and its medium | `interactionCore`: kind, bounds and status of the encounter Â· `channel`: in person, telephone, written or online medium |
| `parties` | Who took part and how the record is shared | `partyRoles`: each party's role and joining time Â· `mutuality`: countersigned records both sides acknowledge |
| `outcome` | What came of it and what follows | `outcomes`: agreed or observed results Â· `followUp`: links to continuing interactions |

## Objects

- `interaction`: a bounded encounter between two or more parties; key attributes: interactionKind, openedAt, closedAt, status
- `partyRole`: one party's role in the interaction (initiator, respondent, witness, intermediary); key attributes: partyRef, role, joinedAt
- `channel`: the medium of the encounter; key attributes: channelKind, endpointRef
- `exchangedItem`: something passed between parties (message, document, goods reference, commitment); key attributes: itemKind, direction, passedAt
- `outcome`: the agreed or observed result of the interaction; key attributes: outcomeKind, agreedBy, statedAt
- `mutualRecord`: the countersigned bilateral record both parties acknowledge; key attributes: countersignedAt, contentDigest, status
- `followUpLink`: the connection to a subsequent interaction continuing this one; key attributes: linkKind, nextRef

## Relationships

- `interaction` -> between -> `partyRole` (1:n): at least two party roles per encounter
- `interaction` -> via -> `channel` (n:1): the medium the encounter took place through
- `exchangedItem` -> passedIn -> `interaction` (n:1): the items that changed hands or minds
- `interaction` -> yielded -> `outcome` (1:n): one encounter can produce several results
- `mutualRecord` -> attests -> `interaction` (1:1): at most one countersigned record per encounter
- `followUpLink` -> continues -> `interaction` (n:1): chains of related encounters form threads
- `interaction` -> occurredAt -> `placeSpecification` (n:1): meeting places resolve through U7 references

## Events

- `interactionOpened`: an encounter began between identified parties
- `partyJoined`: an additional party entered an open interaction
- `itemExchanged`: a message, document, goods reference or commitment passed between parties
- `outcomeStated`: a result was stated or agreed by the parties
- `interactionClosed`: the encounter ended and its bounds were sealed
- `recordCountersigned`: both parties acknowledged the mutual record

## Contracts

- `bilateralRecordPact`: the parties co-hold the mutual record while each perspective remains separately owned
- `disclosureConsentGrant`: a party consents per S2 to disclose an interaction to a named third party
- `aggregateInteractionLicense`: release of anonymized contact and volume statistics

## Projections

- `myEncountersProjection`: one party's view of its interactions; omits the counterparty's private annotations
- `sharedMinutesProjection`: the countersigned mutual record only; omits unilateral notes
- `interactionGraphProjection`: anonymized aggregate of who-met-whom volumes; omits all content

## Composition

- EXTEND `world.occurrenceEvent` (X1): an interaction is an occurrence with party-perspective and mutuality semantics added
- REFERENCE `world.person` (H1): human parties in party roles
- REFERENCE `world.organization` (O1): organizational parties and intermediaries
- REFERENCE `world.addressLocationReferencing` (U7): meeting places and channel endpoints
- REFERENCE `world.situationCondition` (X4): an ongoing relationship built from repeated encounters can be registered as a situation
- REFERENCE `world.auditTrail` (S4): countersigning and disclosure actions are audited there
- imports: w3c-prov (MIX-IN: attribution and derivation facets on records and exchanged items)
- imports: schema-org (ALIGN: Action and Event typing)

## Stewardship

The owner archetype is the parties themselves: each party owns its perspective of the interaction per S1, and the countersigned mutual record is governed bilaterally. Any disclosure to a third party requires the S2 consent of every named party, with disclosures auditable via S4.