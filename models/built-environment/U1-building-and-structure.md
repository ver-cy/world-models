# U1 Building & Structure

This meta-model describes buildings and engineered structures as physical artifacts: their massing, load-bearing and enclosing elements, materials, installed technical systems, measured condition and energy behavior, and their lifecycle from acceptance into service to demolition. It is its own model because physical fabric persists and changes on a different cadence and under different authority than the land beneath it (P2), the usable units inside it (U2), or the temporary works that create it (U6).

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:u1"
  csn: world.buildingStructure
  version: 0.2.0
  displayName: "Building & Structure"
  description: "Buildings and engineered structures as physical artifacts, from massing and materials to condition, energy and demolition."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.buildingStructure
bundles:
  - csn: world.buildingStructure.fabric
    displayName: "Fabric"
    layers:
      - world.buildingStructure.fabric.massing
      - world.buildingStructure.fabric.elements
      - world.buildingStructure.fabric.materials
  - csn: world.buildingStructure.performance
    displayName: "Performance"
    layers:
      - world.buildingStructure.performance.condition
      - world.buildingStructure.performance.energy
  - csn: world.buildingStructure.lifecycle
    displayName: "Lifecycle"
    layers:
      - world.buildingStructure.lifecycle.provenance
      - world.buildingStructure.lifecycle.alterations
imports:
  - source: ifc
    version: "*"
  - source: citygml
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `fabric` | What the artifact physically is | `massing`: footprint, height, storeys, envelope geometry · `elements`: load-bearing and enclosing components · `materials`: what the elements are made of |
| `performance` | How the artifact holds up in use | `condition`: dated assessments of fabric state · `energy`: measured or modelled energy behavior |
| `lifecycle` | The artifact's history from birth to removal | `provenance`: construction year, builder, acceptance basis · `alterations`: extensions, retrofits, conversions over time |

## Objects

- `building`: a roofed construction usable by people; key attributes: constructionYear, storeysAboveGround, grossFloorArea, primaryMaterial, status
- `structure`: a non-building engineered construction such as a bridge, tower, dam or retaining wall; key attributes: structureClass, constructionYear, designLife, status
- `storey`: one horizontal level of a building; key attributes: level, height, floorArea
- `buildingElement`: a load-bearing or enclosing component (foundation, wall, frame, roof); key attributes: elementClass, material, installedYear
- `technicalSystem`: an installed service system (heating, ventilation, lift, fire safety); key attributes: systemClass, capacity, commissioningYear
- `conditionAssessment`: a dated expert judgement of fabric state; key attributes: assessedAt, method, grade, remainingLife
- `energyProfile`: measured or modelled energy behavior of the artifact; key attributes: ratingClass, annualDemand, assessmentDate

## Relationships

- `building` -> standsOn -> `landParcel` (n:m): the ground the building occupies; tenure over the ground is resolved in P2, not here
- `building` -> hasStorey -> `storey` (1:n): the vertical decomposition of the shell
- `buildingElement` -> partOf -> `building` (n:1): each element belongs to one building or structure
- `technicalSystem` -> serves -> `building` (n:m): a system can serve several artifacts, and one artifact hosts many systems
- `conditionAssessment` -> evaluates -> `structure` (n:1): every assessment grades exactly one building or structure
- `structure` -> carries -> `networkSegment` (n:m): bridges, tunnels and pylons carry infrastructure segments modelled in U3

## Events

- `structureCommissioned`: the artifact passed acceptance and entered service, mirroring the acceptance record in U6
- `conditionAssessed`: a condition assessment was performed and a grade recorded
- `alterationCompleted`: an extension, retrofit or conversion changed the fabric
- `systemReplaced`: a technical system was renewed or substituted
- `damageRecorded`: fire, flood, collision or subsidence damage was observed, often linked from an X3 incident
- `structureDemolished`: the artifact was removed from the world; the record is retained as history

## Contracts

- `handoverPackageContract`: transfer of as-built fabric data from a U6 works record to the owner at acceptance
- `conditionDisclosureContract`: owner-granted access for a surveyor, insurer or prospective buyer to the condition and energy layers
- `openFootprintLicense`: public release of footprint, height and construction year for mapping and city modelling

## Projections

- `cityscapeProjection`: massing envelopes and heights for city-scale visualization; omits interiors, systems and condition
- `insurerRiskProjection`: construction year, materials, condition grade and energy profile; omits occupant and interior detail
- `maintenancePlanProjection`: elements and systems with remaining life estimates; omits ownership and valuation context

## Composition

- REFERENCE `world.landParcelCadastre` (P2): every building stands on one or more parcels; ground tenure is resolved there
- REFERENCE `world.premisesSpatialUnit` (U2): interior subdivision into usable units is modelled by U2, which points back at the shell defined here
- REFERENCE `world.constructionWorks` (U6): works create and alter the fabric; the U6 acceptance record is the birth certificate of an artifact here
- REFERENCE `world.addressLocationReferencing` (U7): buildings are located by addresses and geocodes maintained there
- REFERENCE `world.incidentEmergency` (X3): harm events that damage fabric are recorded in X3 and reflected here as damageRecorded events
- REFERENCE `world.ownership` (S1): the owner of record of every building or structure
- imports: ifc (EXTEND: element, system and material typology for the fabric bundle)
- imports: citygml (ALIGN: level-of-detail massing semantics for city-scale views)

## Stewardship

The owner archetype is the registered owner of each building or structure per S1, a person or organization holding title to the artifact. Ownership means authority over the fabric record; all third-party access is granted by the owner through S2 grants, and every disclosure is auditable via S4.