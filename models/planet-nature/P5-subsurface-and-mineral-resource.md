# P5 Subsurface & Mineral Resource

This meta-model describes what lies beneath the surface: geological units and structures, the boreholes and samples that evidence them, the deposits of minerals, hydrocarbons and other resources they host, and the estimates that state how much is there and how confidently. It is its own model because the subsurface is a three-dimensional body of evidence, always partial and always revised, and because a resource estimate is a claim about a deposit under a stated method rather than a property of the ground. Extraction as an operation is modelled in K10, and extraction rights are held and transferred through S1.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p5"
  csn: world.subsurfaceAndMineralResource
  version: 0.2.0
  displayName: "Subsurface & Mineral Resource"
  description: "Geological units, boreholes and samples with the deposits they host and the classified estimates of those deposits."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.subsurfaceAndMineralResource
bundles:
  - csn: world.subsurfaceAndMineralResource.geology
    displayName: "Geology and evidence"
    layers:
      - world.subsurfaceAndMineralResource.geology.stratigraphyAndLithology
      - world.subsurfaceAndMineralResource.geology.structuralFeature
      - world.subsurfaceAndMineralResource.geology.boreholeAndSample
  - csn: world.subsurfaceAndMineralResource.resourceInventory
    displayName: "Resource inventory"
    layers:
      - world.subsurfaceAndMineralResource.resourceInventory.occurrenceAndDeposit
      - world.subsurfaceAndMineralResource.resourceInventory.estimateAndClassification
  - csn: world.subsurfaceAndMineralResource.subsurfaceUse
    displayName: "Subsurface use"
    layers:
      - world.subsurfaceAndMineralResource.subsurfaceUse.volumeAndTenement
      - world.subsurfaceAndMineralResource.subsurfaceUse.wellAndWorking
      - world.subsurfaceAndMineralResource.subsurfaceUse.storageAndVoid
imports:
  - source: geosciml
    version: "*"
  - source: unfc
    version: "*"
  - source: crirsco
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `geology` | What the ground is made of and what evidence says so | `stratigraphyAndLithology`: mapped units, their age, composition and contacts · `structuralFeature`: faults, folds, contacts and fracture systems that displace units · `boreholeAndSample`: drilled holes, logs, cores and their assays as the evidence base |
| `resourceInventory` | What resources the ground holds and how confidently that is known | `occurrenceAndDeposit`: identified occurrences and delineated deposits with commodity and grade · `estimateAndClassification`: tonnage and grade estimates with confidence category, cut-off and method |
| `subsurfaceUse` | How the subsurface is divided and physically used | `volumeAndTenement`: three-dimensional volumes referenced by extraction and exploration grants held elsewhere · `wellAndWorking`: wells, shafts, adits and their status · `storageAndVoid`: reservoirs, caverns and abandoned workings used for storage or left as voids |

## Objects

- `geologicalUnit`: a mapped body of rock or sediment; key attributes: unit identifier, lithology, age range, extent geometry, thickness, mapping confidence
- `structuralFeature`: a fault, fold or contact; key attributes: feature type, geometry, displacement, dip and strike, activity status
- `borehole`: a drilled hole and its record; key attributes: collar coordinates, total depth, inclination, drilling date, log references, status
- `geoSample`: material taken for analysis; key attributes: sample identifier, depth interval, source borehole or outcrop, sample type, storage location
- `deposit`: a delineated concentration of a resource; key attributes: commodity, deposit type, extent geometry, average grade, depth range
- `reserveEstimate`: a stated quantity for a deposit; key attributes: reference date, category, tonnage, grade, cut-off, method, competent assessor reference
- `subsurfaceVolume`: a bounded three-dimensional block of subsurface; key attributes: geometry, depth interval, purpose (exploration, extraction, storage), status
- `storageReservoir`: a subsurface space usable for containment; key attributes: host unit reference, capacity, seal integrity assessment, current contents class

## Relationships

- `borehole` -> intersects -> `geologicalUnit` (n:m): logged intervals attach evidence to mapped units
- `geoSample` -> takenFrom -> `borehole` (n:1): every sample traces to the hole or outcrop it came from
- `deposit` -> hostedIn -> `geologicalUnit` (n:1): a deposit is described within the unit that contains it
- `reserveEstimate` -> assesses -> `deposit` (n:1): estimates are versioned claims about one deposit
- `deposit` -> locatedWithin -> `subsurfaceVolume` (n:m): deposits are related to the blocks defined over them
- `structuralFeature` -> offsets -> `geologicalUnit` (n:m): faults displace units and complicate correlation
- `storageReservoir` -> containedIn -> `geologicalUnit` (n:1): storage space is a property of a host formation
- `subsurfaceVolume` -> underlies -> `parcel` in P2 (n:m): surface and subsurface interests are related but not identical

## Events

- `boreholeDrilled`: a hole was completed and its primary log became available
- `sampleAssayed`: analytical results for a sample were returned and attached to its interval
- `geologicalMapRevised`: unit boundaries or attributions changed after new evidence
- `depositDelineated`: a resource concentration was outlined as a named deposit
- `reserveEstimateFiled`: a new or updated quantity statement was lodged with its method and category
- `estimateReclassified`: an estimate moved between confidence categories after further work
- `wellPluggedAndAbandoned`: a well or working was closed and sealed, changing its status
- `subsidenceObserved`: surface settlement above workings or extraction volumes was measured

## Contracts

- `geologicalArchiveAccessContract`: terms for reading maps, logs and sample records from the archive, including citation and redistribution
- `explorationDataEmbargoContract`: terms of time-limited confidentiality for data submitted by an explorer, and the release schedule when it expires
- `estimateDisclosureContract`: terms under which a quantity statement is published, including method transparency and assessor accountability
- `sampleCustodyAgreement`: terms for loan, sub-sampling and return of physical core and specimens

## Projections

- `publicGeologyMap`: units, structures and outcrop as a map layer; omits confidential exploration results within embargo
- `resourceInventorySummary`: tonnage and grade by commodity and confidence category over an area; omits property-level and holder-linked detail
- `boreholeLogExtract`: the full log and assay record for named holes to an entitled requester; omits unrelated holdings

## Composition

- REFERENCE `world.landParcelAndCadastre` (P2): surface parcels overlie the volumes described here and are governed separately
- REFERENCE `world.terrainAndLandform` (P1): outcrop mapping and collar positions are expressed in the same spatial frame
- REFERENCE `world.waterBodyAndHydrology` (P3): aquifers are hosted in the geological units modelled here
- REFERENCE `world.soilAndAgriculturalLand` (P10): parent material links the weathering profile to its bedrock
- REFERENCE `world.resourceExtractionOperations` (K10): operations consume this inventory and report output against deposits
- REFERENCE `world.materialAndSubstance` (M1): commodity identity and hazard classification resolve there
- REFERENCE `world.permitLicenseAndAuthorization` (A14) and `world.metaObjectOwnershipAndStewardship` (S1): exploration and extraction grants are authorized and held there, never inlined here
- REFERENCE `world.emissionAndEnvironmentalFlux` (F6): injected or stored volumes are accounted as fluxes there
- REFERENCE `world.priceValuationAndAppraisal` (C7): monetary appraisal of a deposit is out of scope here and belongs to that model
- imports: geosciml (EXTEND): the geological feature, borehole and sample backbone this model specializes
- imports: unfc (ALIGN): the classification framework for resource and reserve categories
- imports: crirsco (ALIGN): reporting template concepts for competent assessment of estimates

## Stewardship

A geological commons steward keeps the subsurface archive: it accepts logs, samples and estimates, maintains the mapped units and publishes the inventory, without holding extraction rights itself. Those rights are held and transferred through S1, confidential submissions are released only under S2 access contracts with explicit embargo terms, and every read of embargoed material is logged in S4.
