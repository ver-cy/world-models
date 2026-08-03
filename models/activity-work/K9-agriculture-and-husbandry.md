# K9 Agriculture & Husbandry

This meta-model describes farming as an activity: holdings and their fields, crops grown by season, operations applied to them, harvests gathered, and livestock kept, cared for and yielding produce. It is its own model because farming runs on biological and seasonal rhythms that generic production (K8) does not capture: a season is not a production run, a herd is not a batch, and land, weather and animal life cycles shape every record.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k9"
  csn: world.agricultureAndHusbandry
  version: 0.2.0
  displayName: "Agriculture & Husbandry"
  description: "Farms, fields, crops, seasons, harvests, livestock and their care."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.agricultureAndHusbandry
bundles:
  - csn: world.agricultureAndHusbandry.holding
    displayName: "Holding"
    layers:
      - world.agricultureAndHusbandry.holding.farmProfile
      - world.agricultureAndHusbandry.holding.fieldAndParcel
  - csn: world.agricultureAndHusbandry.cultivation
    displayName: "Cultivation"
    layers:
      - world.agricultureAndHusbandry.cultivation.cropSeason
      - world.agricultureAndHusbandry.cultivation.fieldOperation
      - world.agricultureAndHusbandry.cultivation.harvest
  - csn: world.agricultureAndHusbandry.husbandry
    displayName: "Husbandry"
    layers:
      - world.agricultureAndHusbandry.husbandry.herdAndFlock
      - world.agricultureAndHusbandry.husbandry.animalCare
      - world.agricultureAndHusbandry.husbandry.animalProduce
imports:
  - source: agrovoc
    version: "*"
  - source: fao
    version: "*"
  - source: gs1
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `holding` | The farm as a unit of land use | `farmProfile`: the holding, its kind and land use Â· `fieldAndParcel`: fields mapped onto cadastral parcels |
| `cultivation` | Growing crops through seasons | `cropSeason`: what is grown where in which season Â· `fieldOperation`: sowing, treatment, irrigation and tillage acts Â· `harvest`: gathered lots and their measures |
| `husbandry` | Keeping animals | `herdAndFlock`: animal groups and identification Â· `animalCare`: feeding, breeding and veterinary events Â· `animalProduce`: milk, eggs, wool and other recurring yields |

## Objects

- `farm`: an agricultural holding; key attributes: name, holder reference, kind (arable, livestock, mixed), total area
- `field`: a managed area of land; key attributes: identifier, area, soil class, parcel references
- `cropSeason`: a crop grown on a field in a season; key attributes: crop, variety, season, sown area, expected harvest window
- `fieldOperation`: one act of cultivation; key attributes: kind, date, inputs applied, machinery, operator
- `harvestLot`: a gathered quantity of produce; key attributes: crop season reference, quantity, quality grade, storage location
- `herd`: a managed group of animals; key attributes: species, purpose, size, identification scheme
- `animal`: an individually identified animal; key attributes: identifier, species, breed, birth date, status
- `husbandryOperation`: one act of animal care or yield collection; key attributes: kind, date, subject (herd or animal), materials, result

## Relationships

- `farm` -> comprises -> `field` (one-to-many): the land the holding manages
- `field` -> locatedOn -> `landParcel` (many-to-many): cadastral grounding of the field
- `cropSeason` -> grownOn -> `field` (many-to-one): where the crop stands
- `fieldOperation` -> appliedTo -> `cropSeason` (many-to-one): cultivation acts on the growing crop
- `harvestLot` -> gatheredFrom -> `cropSeason` (many-to-one): origin of the produce
- `animal` -> memberOf -> `herd` (many-to-one): group membership over time
- `herd` -> keptAt -> `farm` (many-to-one): where the animals live
- `husbandryOperation` -> performedOn -> `herd` (many-to-one): care and collection acts on animals

## Events

- `sowingCompleted`: a crop season was established on a field
- `treatmentApplied`: an input or intervention was applied to a crop or field
- `harvestGathered`: produce was collected into a harvest lot
- `animalRegistered`: an animal entered identification records
- `animalMoved`: an animal or herd changed farm or field
- `produceCollected`: a recurring animal yield was gathered and measured
- `seasonClosed`: a crop season ended with its harvest accounted

## Contracts

- `traceabilityDisclosure`: a buyer or food chain partner traces a lot back to field, season and operations
- `statisticalReturn`: the holding reports areas, yields and herd sizes to a statistics office per cadence
- `agronomicDataSharing`: field and operation data are shared with an adviser or research party under the holder's terms

## Projections

- `cropCalendar`: seasons and operations on a time axis per field; omits produce buyers and prices
- `holdingRegisterView`: the farm, fields and herds as a registry entry; omits operational detail
- `provenancePassport`: origin, operations and grades of a lot for its buyer; omits the rest of the holding

## Composition

- REFERENCE `world.landParcel` (P2): fields are grounded on cadastral parcels
- REFERENCE `world.site` (P5): barns, stores and yards as sites
- EXTEND `world.actAction` (K2): field and husbandry operations specialize the atomic act
- REFERENCE `world.planAndSchedule` (K7): season plans and operation schedules
- REFERENCE `world.productionAndManufacturing` (K8): downstream processing of harvested and collected produce
- REFERENCE `world.person` (H1) and `world.organization` (O1): holders and operators
- imports: agrovoc (ALIGN): multilingual concept vocabulary for crops, livestock and inputs
- imports: fao (REFERENCE): agricultural census and statistical definitions
- imports: gs1 (REFERENCE): lot identification for produce entering supply chains

## Stewardship

The farming organization or person holding the farm owns its records; animal identification may additionally answer to a public registrar. Access is granted by the holder via the catalogue's ownership and access models (S1/S2), with audit via S4.
