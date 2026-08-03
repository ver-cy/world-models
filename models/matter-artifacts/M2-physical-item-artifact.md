# M2 Physical Item / Artifact

This meta-model describes any individual physical thing as a distinguishable instance: its identity marks, the class it instantiates, its condition, where it is, and who holds it. It is the instance backbone of the Matter & Artifacts cluster: class-level descriptions live in sibling models (materials, goods, machine models), while this model carries the one-of-a-kind history that only an individual thing can have, and the specialized item models (equipment, vehicles, devices, cultural artifacts) extend it.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m2"
  csn: world.physicalItem
  version: 0.2.0
  displayName: "Physical Item / Artifact"
  description: Individual physical things with serial identity, kind, condition, location and custody history.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.physicalItem
bundles:
  - csn: world.physicalItem.identity
    displayName: Identity
    layers:
      - world.physicalItem.identity.itemIdentity
      - world.physicalItem.identity.kindReference
  - csn: world.physicalItem.state
    displayName: State
    layers:
      - world.physicalItem.state.condition
      - world.physicalItem.state.lifecycle
  - csn: world.physicalItem.whereabouts
    displayName: Whereabouts
    layers:
      - world.physicalItem.whereabouts.location
      - world.physicalItem.whereabouts.custody
imports:
  - source: schema-org
    version: "*"
  - source: iso-55000
    version: "*"
  - source: gs1-epcis
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `identity` | Telling this item apart from every other item | `itemIdentity`: serial numbers, engraved marks, tags and other instance identifiers Â· `kindReference`: the link from the instance to its class (good, model, design, pattern) |
| `state` | What shape the item is in and where it stands in life | `condition`: condition grades, wear, damage and repair state as assessed over time Â· `lifecycle`: statuses from produced through in use, stored, lost, recovered, disposed |
| `whereabouts` | Where the item is and who holds it | `location`: current and historical location fixes resolved against places Â· `custody`: holding records and transfers between holders |

## Objects

- `item`: one individual physical thing; key attributes: native identifier, kind reference, lifecycle status, first-seen date.
- `serialIdentity`: one instance identifier borne by the item; key attributes: scheme, value, marking method, legibility.
- `kindReference`: the resolved class of the item; key attributes: target model, target identifier, resolution confidence.
- `conditionAssessment`: a dated judgement of the item's condition; key attributes: grade, defects, assessor reference, method.
- `locationFix`: a dated statement of where the item was; key attributes: place reference, precision, source (sighting, scan, declaration).
- `custodyRecord`: a period during which a named party held the item; key attributes: holder reference, start, end, basis of holding.
- `componentLink`: membership of the item in an assembly; key attributes: parent item, position or role, installed date.
- `disposalRecord`: how the item left the world of tracked things; key attributes: disposal mode, date, evidence reference.

## Relationships

- `item` -> identifiedBy -> `serialIdentity` (0..*): an item can carry several identifiers from different schemes.
- `item` -> instanceOf -> `kindReference` (many-to-one): every item instantiates at most one resolved class.
- `item` -> assessedBy -> `conditionAssessment` (0..*): assessments accumulate as a condition history.
- `item` -> lastSeenAt -> `locationFix` (0..1 current, 0..* historical): the newest fix is the current whereabouts.
- `item` -> heldUnder -> `custodyRecord` (0..* over time): at most one custody record is open at any moment.
- `item` -> partOf -> `item` (0..1 via `componentLink`): assemblies and component hierarchies of items.

## Events

- `itemProduced`: an individual thing came into existence or entered tracking.
- `itemMarked`: a serial identity was applied to or discovered on the item.
- `conditionAssessed`: an assessment of the item's condition was recorded.
- `itemRelocated`: a new location fix superseded the previous whereabouts.
- `custodyTransferred`: holding of the item passed from one party to another.
- `itemReportedLost`: the item's whereabouts became unknown to its holder.
- `itemRecovered`: a lost item was found and re-entered normal tracking.
- `itemDisposed`: the item was destroyed, recycled or otherwise permanently retired.

## Contracts

- `itemPassportAccess`: owner-granted read access to identity, kind and condition of a single item (a buyer, a repairer, a valuer).
- `custodyAttestation`: a holder attests, to a named party, the custody chain of an item for a stated period.
- `serialLookup`: narrow query contract answering whether a given serial identity exists and its lifecycle status, without exposing location or holder.

## Projections

- `publicPassportView`: serial identity, kind and lifecycle status; omits location, holder and condition detail.
- `custodyChainView`: ordered custody records for provenance checks; omits condition and technical detail.
- `inventoryView`: items grouped by holder and location for stock-taking; omits historical fixes and past custodians.

## Composition

- REFERENCE `world.materialSubstance` (M1): what the item is made of resolves to material classes, never restated locally.
- REFERENCE `world.tradableGood` (M3): the kind reference resolves to a good when the item is a serialized market product.
- REFERENCE `world.place` (P1): location fixes resolve to place identities.
- EXTEND (inbound): `world.equipment` (M6), `world.vehicle` (M7), `world.deviceHardware` (M8) and `world.culturalArtifact` (M9) specialize this item core with their domain semantics.
- imports: schema-org (ALIGN): schema:Product and schema:IndividualProduct anchor the kind and instance distinction.
- imports: iso-55000 (ALIGN): asset lifecycle vocabulary for the lifecycle layer.
- imports: gs1-epcis (ALIGN): event vocabulary for observation, aggregation and custody steps.

## Stewardship

Each item record is stewarded by the item's owner as established in the catalogue's S1 ownership model; all access by other parties is granted by that owner through S1/S2, and every change is traceable through S4 audit.
