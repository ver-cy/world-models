# P2 Land Parcel & Cadastre

This meta-model describes land as registrable spatial objects: parcels with surveyed boundaries, the rights, restrictions and responsibilities recorded against them, and the planning classifications that condition their use. It is its own model because a parcel is not simply a polygon, it is a legal-spatial unit whose identity persists through subdivision, transfer and reclassification, and whose description must be defensible in a dispute. Physical relief (P1) and soil condition (P10) describe the same ground from other angles, and the identity of holders and the mechanics of granting access live in S1 and S2.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:p2"
  csn: world.landParcelAndCadastre
  version: 0.2.0
  displayName: "Land Parcel & Cadastre"
  description: "Land units as registrable spatial objects with surveyed boundaries, recorded rights and planning classification."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.landParcelAndCadastre
bundles:
  - csn: world.landParcelAndCadastre.tenure
    displayName: "Tenure and interests"
    layers:
      - world.landParcelAndCadastre.tenure.rightsAndRestrictions
      - world.landParcelAndCadastre.tenure.shareAndTenancy
      - world.landParcelAndCadastre.tenure.encumbrance
  - csn: world.landParcelAndCadastre.survey
    displayName: "Survey and spatial description"
    layers:
      - world.landParcelAndCadastre.survey.boundaryGeometry
      - world.landParcelAndCadastre.survey.monumentAndMeasurement
      - world.landParcelAndCadastre.survey.accuracyAndLineage
  - csn: world.landParcelAndCadastre.planning
    displayName: "Planning and use"
    layers:
      - world.landParcelAndCadastre.planning.landUseClass
      - world.landParcelAndCadastre.planning.zoningDesignation
      - world.landParcelAndCadastre.planning.developmentConstraint
imports:
  - source: iso-19152-ladm
    version: "*"
  - source: iso-19107-spatial-schema
    version: "*"
  - source: inspire
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `tenure` | What interests exist over a parcel and who holds them | `rightsAndRestrictions`: recorded rights, restrictions and responsibilities with their basis and validity · `shareAndTenancy`: co-holding shares, undivided interests and tenancy arrangements · `encumbrance`: mortgages, easements, liens and caveats that burden an interest |
| `survey` | How the parcel is described in space and how well that description holds | `boundaryGeometry`: boundary lines, corners and the resulting parcel polygons · `monumentAndMeasurement`: physical marks, observed bearings and distances behind the geometry · `accuracyAndLineage`: positional accuracy, survey plan references and the chain of amendments |
| `planning` | How use of the parcel is classified and conditioned | `landUseClass`: the recorded present use category · `zoningDesignation`: designations assigned by a planning instrument · `developmentConstraint`: protective, hazard or servitude constraints that limit development |

## Objects

- `parcel`: a land unit with a persistent cadastral identity; key attributes: parcel identifier, geometry, computed area, status (active, superseded, provisional), creation basis
- `boundary`: a shared line between parcels or against a natural feature; key attributes: geometry, boundary type (fixed, general, natural), agreed status, evidence references
- `boundaryMonument`: a physical mark defining a boundary point; key attributes: mark identifier, coordinates, mark type, condition, last inspection
- `surveyPlan`: the lodged document that evidences a boundary description; key attributes: plan number, surveyor reference, lodgement date, method, accuracy class
- `rightRecord`: an interest recorded against a parcel; key attributes: right type, holder reference, share, commencement, expiry, registration basis
- `encumbrance`: a burden on an interest; key attributes: encumbrance type, beneficiary reference, amount or extent, priority rank, discharge status
- `landUseClass`: a term describing recorded present use; key attributes: term identifier, definition, parent term, source classification
- `zoningDesignation`: a designation applied by a planning instrument; key attributes: designation code, instrument reference, effective period, permitted and prohibited uses

## Relationships

- `parcel` -> boundedBy -> `boundary` (1:n): a parcel is defined by the ordered set of boundaries that close its polygon
- `boundary` -> evidencedBy -> `surveyPlan` (n:m): a boundary can rest on several plans, and one plan can evidence many boundaries
- `boundary` -> markedBy -> `boundaryMonument` (1:n): monuments materialize boundary points on the ground
- `rightRecord` -> attachesTo -> `parcel` (n:1): every recorded interest names the parcel it burdens or benefits
- `encumbrance` -> restricts -> `rightRecord` (n:1): burdens attach to an interest rather than to the land directly
- `parcel` -> classifiedAs -> `landUseClass` (n:1): a parcel carries one recorded present use at a time
- `parcel` -> subjectTo -> `zoningDesignation` (n:m): several designations may overlap on the same parcel
- `parcel` -> derivedFrom -> `parcel` (n:m): subdivision and consolidation create traceable lineage between superseded and successor parcels

## Events

- `parcelRegistered`: a new land unit entered the register with an identity and a spatial description
- `parcelSubdivided`: one parcel was replaced by two or more successors, and the predecessor was superseded
- `parcelsConsolidated`: several parcels merged into a single successor unit
- `boundaryAdjusted`: a boundary description changed after resurvey, agreement or correction
- `rightRegistered`: an interest was recorded against a parcel with effect from a stated moment
- `rightTransferred`: a recorded interest passed from one holder to another
- `encumbranceDischarged`: a burden was released and stopped restricting the interest
- `landUseReclassified`: the recorded present use or an applicable designation changed

## Contracts

- `cadastralSearchContract`: terms for a single-parcel search returning geometry, status and, where entitled, the current interests
- `bulkCadastreExtractContract`: terms for periodic bulk extracts to a planning, valuation or statistics consumer, with update cadence and redistribution limits
- `surveyLodgementContract`: terms under which a qualified surveyor lodges plans and the register accepts, queries or rejects them
- `noticeSubscriptionContract`: terms for subscribing to change notices affecting a nominated parcel or area

## Projections

- `publicParcelView`: identifier, geometry, area and use class; omits holder identity, consideration and encumbrance detail
- `titleAbstract`: interests, shares and encumbrances in priority order for an entitled requester; omits internal examination notes
- `cadastralIndexMap`: boundaries and identifiers as a continuous map layer; omits all tenure content
- `landUseStatistics`: area totals by use class and designation over an area; omits parcel identity entirely

## Composition

- REFERENCE `world.terrainAndLandform` (P1): parcels are positioned on the published relief and control network
- REFERENCE `world.soilAndAgriculturalLand` (P10): capability and contamination findings are recorded against land that this model delimits
- REFERENCE `world.buildingAndStructure` (U1) and `world.premisesAndSpatialUnit` (U2): structures and units are located on or within parcels
- REFERENCE `world.addressAndLocationReferencing` (U7): addresses resolve to parcels and premises rather than duplicating their geometry
- REFERENCE `world.metaObjectOwnershipAndStewardship` (S1): holder identity, transfer authority and delegation are resolved there, not inlined here
- REFERENCE `world.attestationCertificateAndLicense` (R5): title extracts and certificates issued from the register are attestations governed there
- REFERENCE `world.permitLicenseAndAuthorization` (A14): development consents that condition a parcel are granted and revoked in that model
- EXTEND `world.registry` (R1): this model specializes the generic register pattern with survey evidence and legal effect over spatial units
- imports: iso-19152-ladm (EXTEND): the parties, rights, spatial units and source documents backbone this model specializes
- imports: iso-19107-spatial-schema (COMPOSE): geometry primitives for boundaries and polygons
- imports: inspire (ALIGN): cadastral parcel theme for cross-register comparability

## Stewardship

A land registrar keeps the register: it decides what is recorded, in what order and with what evidence, and it publishes the resulting parcel and interest records. Ownership of the underlying meta-objects and the authority to transfer interests are expressed through S1, disclosure of holder-level detail is granted case by case through S2 access contracts, and every read of an entitled projection is logged in S4.
