# U7 Address & Location Referencing

This meta-model describes the referencing fabric of the built world: civic and postal addresses, thoroughfares, geocodes and their reference systems, points of interest and place names. It is its own model because referencing schemes are governed independently of the things they locate: an address outlives occupants, a geocode outlives a building, and the same location is referenced by many models across the catalogue.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:u7"
  csn: world.addressLocationReferencing
  version: 0.2.0
  displayName: "Address & Location Referencing"
  description: "Addresses, thoroughfares, geocodes, reference systems, points of interest and place names."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.addressLocationReferencing
bundles:
  - csn: world.addressLocationReferencing.addressing
    displayName: "Addressing"
    layers:
      - world.addressLocationReferencing.addressing.civicAddresses
      - world.addressLocationReferencing.addressing.thoroughfares
      - world.addressLocationReferencing.addressing.postalDelivery
  - csn: world.addressLocationReferencing.geocoding
    displayName: "Geocoding"
    layers:
      - world.addressLocationReferencing.geocoding.geocodes
      - world.addressLocationReferencing.geocoding.referenceSystems
  - csn: world.addressLocationReferencing.placesOfInterest
    displayName: "Places of interest"
    layers:
      - world.addressLocationReferencing.placesOfInterest.poiCatalogue
      - world.addressLocationReferencing.placesOfInterest.placeNames
imports:
  - source: iso-19160
    version: "*"
  - source: upu-s42
    version: "*"
  - source: iso-19112
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `addressing` | Civic and postal designation of locations | `civicAddresses`: structured addresses and their assignment lifecycle Â· `thoroughfares`: named streets, roads and waterways used in addressing Â· `postalDelivery`: postal formatting and delivery ordering |
| `geocoding` | Coordinate and code representation of locations | `geocodes`: coordinate and code values with precision Â· `referenceSystems`: the systems geocodes are expressed in |
| `placesOfInterest` | Named places used for orientation and discovery | `poiCatalogue`: points of interest with categories and lifecycle Â· `placeNames`: toponyms with language and status |

## Objects

- `address`: a structured civic or postal designation of a location; key attributes: addressComponents, status, assignedAt
- `thoroughfare`: a named street, road or waterway used in addressing; key attributes: name, thoroughfareKind, extent
- `addressAssignment`: the act record binding an address to an addressable object; key attributes: objectRef, assignedAt, basis
- `geocode`: a coordinate or code representation of a location; key attributes: value, precision, method
- `referenceSystem`: a coordinate or grid system in which geocodes are expressed; key attributes: systemId, authority, kind
- `poi`: a named point of interest usable for orientation or discovery; key attributes: name, category, status
- `placeName`: a toponym with language and lifecycle; key attributes: name, language, nameStatus

## Relationships

- `address` -> onThoroughfare -> `thoroughfare` (n:1): the street context of a civic address
- `addressAssignment` -> binds -> `address` (n:1): assignments attach addresses to buildings (U1), premises (U2) and parcels (P2)
- `geocode` -> encodes -> `address` (n:1): a location can carry several geocodes of differing precision
- `geocode` -> expressedIn -> `referenceSystem` (n:1): every geocode declares its system
- `poi` -> situatedAt -> `address` (n:m): points of interest resolve to one or more addresses
- `placeName` -> names -> `poi` (n:m): toponyms name POIs, thoroughfares and settlements (U4)

## Events

- `addressAssigned`: a new address was assigned to an addressable object
- `addressRetired`: an address was withdrawn from use but kept as history
- `thoroughfareRenamed`: a street or road received a new official name
- `geocodeRevised`: a geocode value or precision was corrected
- `poiRegistered`: a point of interest entered the catalogue
- `poiClosed`: a point of interest ceased to exist or operate

## Contracts

- `openGazetteerLicense`: public release of the authoritative address and place name list
- `geocodingServiceContract`: resolution of addresses to geocodes and back for a consuming service
- `poiListingAgreement`: a subject owner lists or updates its own POI entry

## Projections

- `gazetteerProjection`: the authoritative address list with status; omits occupancy and ownership
- `deliveryRoutingProjection`: postal formatting and delivery ordering; omits historic names and assignment provenance
- `navigationProjection`: POIs, place names and geocodes for wayfinding; omits retired records

## Composition

- REFERENCE `world.buildingStructure` (U1): buildings as addressable objects
- REFERENCE `world.premisesSpatialUnit` (U2): premises addressed by sub-address and unit number
- REFERENCE `world.landParcelCadastre` (P2): parcels as addressable objects where no building stands
- REFERENCE `world.settlementUrbanForm` (U4): settlements and districts as address context and named places
- REFERENCE `world.publicMandate` (A12): the registrar's mandate to assign and retire addresses
- imports: iso-19160 (EXTEND: address class structure and lifecycle)
- imports: upu-s42 (ALIGN: postal address templates and formatting)
- imports: iso-19112 (REFERENCE: geographic identifier schemes)

## Stewardship

The owner archetype is the address registrar operating under a public mandate (A12), which stewards addresses, thoroughfares and geocodes as a reference asset. POI entries can be stewarded by their subject owners per S1, with publication and updates granted through S2.