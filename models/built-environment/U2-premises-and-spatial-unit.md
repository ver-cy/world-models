# U2 Premises & Spatial Unit

This meta-model describes the units inside structures: apartments, offices, shops and rooms, their boundaries, the common parts they share, their use class, and who occupies them over time. It is its own model because units are delineated, classified, transacted and occupied independently of the building shell (U1) that contains them and of the parcel (P2) beneath them.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:u2"
  csn: world.premisesSpatialUnit
  version: 0.2.0
  displayName: "Premises & Spatial Unit"
  description: "Units within structures, their boundaries, common parts, use classes and occupancy over time."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.premisesSpatialUnit
bundles:
  - csn: world.premisesSpatialUnit.delineation
    displayName: "Delineation"
    layers:
      - world.premisesSpatialUnit.delineation.boundaries
      - world.premisesSpatialUnit.delineation.commonParts
  - csn: world.premisesSpatialUnit.use
    displayName: "Use"
    layers:
      - world.premisesSpatialUnit.use.useClass
      - world.premisesSpatialUnit.use.occupancy
  - csn: world.premisesSpatialUnit.aggregation
    displayName: "Aggregation"
    layers:
      - world.premisesSpatialUnit.aggregation.grouping
      - world.premisesSpatialUnit.aggregation.scheme
imports:
  - source: iso-19152-ladm
    version: "*"
  - source: boma
    version: "*"
  - source: ifc
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `delineation` | How units are bounded in space | `boundaries`: surveyed or declared unit boundaries in 2D or 3D Â· `commonParts`: shared spaces and facilities serving several units |
| `use` | What units are for and who is in them | `useClass`: classification of permitted and actual use Â· `occupancy`: who occupies which unit over which period |
| `aggregation` | How units combine into larger wholes | `grouping`: whole-floor lets, portfolio lots and other unit groups Â· `scheme`: condominium and co-ownership scheme membership |

## Objects

- `premise`: an individually usable unit within a building (apartment, office, shop, room); key attributes: unitNumber, floorArea, useClass, status
- `spatialUnit`: the generalization for any bounded interior space, including non-premise spaces such as corridors and plant rooms; key attributes: unitKind, volume, boundedness
- `unitBoundary`: the surveyed or declared boundary of a premise; key attributes: geometryRef, boundaryType, surveyDate
- `commonPart`: a shared space or facility serving several premises (stairwell, lobby, parking); key attributes: partKind, sharedBy
- `occupancySpell`: a continuous period during which a party occupies a premise; key attributes: startDate, endDate, occupancyBasis
- `unitGroup`: a set of premises handled as one whole; key attributes: groupKind, memberCount
- `schemeMembership`: a premise's participation in a condominium or co-ownership scheme; key attributes: schemeRef, shareQuota

## Relationships

- `premise` -> within -> `building` (n:1): every premise sits inside one shell modelled in U1
- `premise` -> boundedBy -> `unitBoundary` (1:n): a premise can carry successive boundary versions
- `premise` -> sharesUseOf -> `commonPart` (n:m): several premises share stairwells, lobbies and parking
- `occupancySpell` -> occupies -> `premise` (n:1): occupancy history accumulates as non-overlapping spells
- `unitGroup` -> aggregates -> `premise` (1:n): a group treats member premises as one unit of dealing
- `premise` -> addressedBy -> `address` (n:m): sub-addresses and unit numbers resolve in U7

## Events

- `premiseDelineated`: a new unit was carved out and its boundary registered
- `boundaryAmended`: a unit boundary was corrected or redrawn
- `useClassChanged`: the unit's use classification changed (for example office to residential)
- `occupancyStarted`: a party took up occupation of a premise
- `occupancyEnded`: an occupancy spell closed
- `premisesMerged`: two or more units were combined into one
- `premisesSplit`: one unit was divided into several

## Contracts

- `valuationAccessContract`: owner-granted access for an assessor to boundaries, areas and use class
- `occupancyDisclosureContract`: consent-based disclosure of occupancy spells to a named relying party
- `schemeDataExchange`: exchange of scheme membership and share quota data among scheme members

## Projections

- `floorPlanProjection`: boundaries and common parts per storey; omits occupants and tenure
- `lettingProjection`: use class, floor area and availability; omits owner identity
- `occupancyStatisticsProjection`: aggregated occupancy rates by area and use class; omits all identities

## Composition

- REFERENCE `world.buildingStructure` (U1): every premise sits inside a shell modelled there
- REFERENCE `world.landParcelCadastre` (P2): condominium schemes anchor unit tenure to the underlying parcel; legal space semantics align with the cadastre
- REFERENCE `world.addressLocationReferencing` (U7): sub-addresses and unit numbering resolve there
- REFERENCE `world.utilityServicePoint` (U5): service points serve premises; supply and metering context lives in U5
- REFERENCE `world.person` (H1): occupants named in occupancy spells
- REFERENCE `world.organization` (O1): organizational occupants and scheme bodies
- imports: iso-19152-ladm (EXTEND: legal space and spatial unit classes)
- imports: boma (ALIGN: floor area measurement definitions)
- imports: ifc (REFERENCE: space geometry underlying unit boundaries)

## Stewardship

The owner archetype is the unit owner per S1 for each premise; scheme-level data is stewarded jointly through scheme membership. All access, including occupancy disclosure, is granted by the owner through S2, with disclosures auditable via S4.