# P1 Terrain & Landform

This meta-model describes the solid relief of a territory: the measured shape of the ground surface, the quantities derived from that shape (slope, aspect, curvature), and the landforms that people name, map and reason about. It is its own model because relief is a persistent physical substrate that many other models depend on but none of them owns: parcels, catchments, soils, settlements and hazards all sit on terrain and would otherwise each re-model elevation in an incompatible way. Terrain here is described as geometry and measurement, not as land tenure (P2) or land condition (P10).

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p1"
  csn: world.terrainAndLandform
  version: 0.2.0
  displayName: "Terrain & Landform"
  description: "Physical relief of a territory as measured elevation surfaces, derived morphometry and delineated landforms."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.terrainAndLandform
bundles:
  - csn: world.terrainAndLandform.relief
    displayName: "Relief and morphometry"
    layers:
      - world.terrainAndLandform.relief.elevationSurface
      - world.terrainAndLandform.relief.morphometry
      - world.terrainAndLandform.relief.surfaceChange
  - csn: world.terrainAndLandform.landformInventory
    displayName: "Landform inventory"
    layers:
      - world.terrainAndLandform.landformInventory.landformTaxonomy
      - world.terrainAndLandform.landformInventory.namedFeature
  - csn: world.terrainAndLandform.spatialFraming
    displayName: "Spatial framing"
    layers:
      - world.terrainAndLandform.spatialFraming.referenceSystem
      - world.terrainAndLandform.spatialFraming.regionGeometry
imports:
  - source: ogc-geosparql
    version: "*"
  - source: inspire
    version: "*"
  - source: dem
    version: "*"
  - source: iso-19111-crs
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `relief` | The continuous ground surface as measured, derived and changing over time | `elevationSurface`: gridded and point elevation coverages with their vertical reference · `morphometry`: quantities computed from the surface such as slope, aspect, curvature and roughness · `surfaceChange`: differences between surfaces of two epochs, uplift, subsidence, erosion and accumulation |
| `landformInventory` | Discrete relief features as named, classified objects | `landformTaxonomy`: the classification scheme of landform kinds and their defining criteria · `namedFeature`: individual delineated landforms with names, extents and prominence |
| `spatialFraming` | The geodetic and geometric frame in which relief is expressed | `referenceSystem`: horizontal and vertical coordinate reference systems, datums and epochs · `regionGeometry`: the footprints, tiles and region polygons that delimit described areas |

## Objects

- `elevationModel`: a coverage of ground or surface heights over an area; key attributes: resolution, coverage geometry, vertical datum reference, model kind (terrain or surface), acquisition epoch, accuracy statement
- `elevationSurvey`: an acquisition campaign that produced height measurements; key attributes: method (levelling, photogrammetry, laser scanning, radar), operator reference, period, nominal accuracy
- `spotHeight`: a monumented or measured point of known height; key attributes: identifier, coordinates, height, datum reference, monument condition, last check date
- `morphometricSurface`: a derived raster of a terrain quantity; key attributes: quantity (slope, aspect, curvature, roughness), unit, source model reference, computation method
- `landform`: a delineated relief feature; key attributes: extent geometry, class reference, relative relief, prominence, orientation, confidence of delineation
- `landformClass`: a term in the landform taxonomy; key attributes: term identifier, definition, parent term, diagnostic criteria
- `terrainRegion`: an area sharing a dominant relief character; key attributes: geometry, dominant landform classes, elevation range, mean slope
- `verticalDatum`: the height reference a surface is expressed against; key attributes: identifier, realization epoch, type (geoid, ellipsoid, tidal), transformation notes

## Relationships

- `elevationModel` -> derivedFrom -> `elevationSurvey` (n:1): every published surface traces to the campaign that measured it
- `morphometricSurface` -> computedFrom -> `elevationModel` (n:1): derived quantities carry the identity of their source surface and method
- `elevationModel` -> referencedTo -> `verticalDatum` (n:1): heights are meaningless without the datum they are expressed against
- `spotHeight` -> monumentedWithin -> `terrainRegion` (n:1): control points are located within the region whose relief they help fix
- `landform` -> classifiedAs -> `landformClass` (n:1): each delineated feature carries one taxonomy term at a time
- `landform` -> containedIn -> `terrainRegion` (n:m): features nest into regional relief units, with partial containment allowed
- `landform` -> adjacentTo -> `landform` (n:m): neighbouring features share a delineation edge, supporting continuity checks
- `terrainRegion` -> nestedIn -> `terrainRegion` (n:1): regions form a hierarchy from coarse relief provinces to local units

## Events

- `elevationSurveyCompleted`: a measurement campaign finished and its raw observations became available
- `elevationModelPublished`: a new or revised height surface was issued for an area at a stated resolution and accuracy
- `verticalDatumRealizationChanged`: the height reference was re-realized, so previously published heights shifted
- `spotHeightRemeasured`: a control point was checked and its height or monument condition was updated
- `landformDelineated`: a relief feature was outlined and entered into the inventory
- `landformReclassified`: an existing feature moved to a different taxonomy term after review
- `terrainChangeDetected`: comparison of two epochs showed elevation gain or loss beyond the detection threshold

## Contracts

- `elevationDataAccessContract`: terms on which tiles or whole coverages are read, including resolution ceiling, redistribution rights and attribution
- `derivedProductLicense`: terms for publishing morphometric or visual products computed from a source surface, including required lineage statements
- `surveyCommissionAgreement`: terms under which a requester commissions a new survey of an area and how the resulting model enters the catalogue

## Projections

- `publicReliefView`: hillshade, contours and coarse elevation for general use; omits raw point clouds, sensor diagnostics and per-tile accuracy internals
- `engineeringTerrainExtract`: full resolution clipped surface plus accuracy metadata for a defined works area; omits everything outside the requested footprint
- `regionalReliefSummary`: mean elevation, elevation range and slope bands per terrain region; omits geometry detail and individual features

## Composition

- REFERENCE `world.landParcelAndCadastre` (P2): parcels are located on relief, and boundary geometry is often surveyed against the same control network
- REFERENCE `world.waterBodyAndHydrology` (P3): catchment delineation and flow direction are derived from the elevation surface published here
- REFERENCE `world.soilAndAgriculturalLand` (P10): slope and aspect are inputs to soil capability and erosion assessment
- REFERENCE `world.naturalPhenomenonAndHazard` (P9): slope, curvature and relative relief feed landslide and flood susceptibility characterization
- REFERENCE `world.settlementAndUrbanForm` (U4) and `world.physicalInfrastructureNetwork` (U3): built form and network alignment are described against this relief frame
- ALIGN `world.addressAndLocationReferencing` (U7): shared coordinate reference systems keep positions comparable across models
- imports: ogc-geosparql (ALIGN): geometry and topology vocabulary for features and regions
- imports: inspire (ALIGN): elevation and geographical grid themes for cross-register comparability
- imports: dem (COMPOSE): the digital elevation model product pattern for gridded height coverages
- imports: iso-19111-crs (REFERENCE): coordinate and vertical reference system identifiers rather than local copies

## Stewardship

A commons steward for territory holds the terrain register: it commissions or accepts surveys, publishes elevation surfaces and maintains the landform inventory, without claiming any right over the land itself. Ownership records for that land live in P2 and S1, access to restricted resolutions or embargoed surveys is granted by the steward through S2 access contracts, and reads are logged in S4.
