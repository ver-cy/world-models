# N3 Dataset & Data Register

This meta-model describes datasets as catalogued assets: identifiable collections of data with distributions, declared schemas, measured quality and a listing in a data register. It is its own model because cataloguing semantics (what a dataset is, how it is served, how good it is, where it is listed) apply uniformly to open data portals, research repositories and internal registers, independently of what the data itself is about.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n3"
  csn: world.dataset
  version: 0.2.0
  displayName: "Dataset & Data Register"
  description: "Datasets as catalogued assets with distributions, schemas, quality and register listings."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.dataset
bundles:
  - csn: world.dataset.catalogue
    displayName: "Catalogue"
    layers:
      - world.dataset.catalogue.description
      - world.dataset.catalogue.distribution
  - csn: world.dataset.structure
    displayName: "Structure"
    layers:
      - world.dataset.structure.schemaReference
      - world.dataset.structure.lineage
  - csn: world.dataset.quality
    displayName: "Quality"
    layers:
      - world.dataset.quality.qualityMeasurement
      - world.dataset.quality.fitnessForUse
imports:
  - source: dcat
    version: "*"
  - source: w3c-dqv
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `catalogue` | Describing and serving the asset | `description`: titles, themes, holders, cadence · `distribution`: files, endpoints, formats, services |
| `structure` | What shape the data has and where it came from | `schemaReference`: declared schemas resolved against the model registry · `lineage`: sources and derivation chains |
| `quality` | How good the data is | `qualityMeasurement`: measured dimensions and scores · `fitnessForUse`: assessments and certifications for purposes |

## Objects

- `dataset`: an identifiable collection of data managed as one asset; key attributes: datasetId, title, themes, updateFrequency, holderRef.
- `datasetSeries`: a grouping of related datasets released over time; key attributes: seriesId, title, cadence.
- `distribution`: a concrete serving of a dataset; key attributes: format, byteSize, checksum, accessUrlRef, licenseRef.
- `accessService`: an endpoint that serves distributions; key attributes: endpointRef, protocol, authRequirement.
- `dataSchema`: the declared structure of the data; key attributes: schemaRef, version, fieldCount.
- `qualityMeasurement`: a measured quality result; key attributes: dimension, score, measuredAt, method.
- `registerEntry`: the listing of a dataset in a catalogue or register; key attributes: catalogueRef, listedAt, status.

## Relationships

- `datasetSeries` -> aggregates -> `dataset` (1:N): editions or slices of one continuing asset.
- `dataset` -> distributedAs -> `distribution` (1:N): one asset, many formats and channels.
- `distribution` -> servedBy -> `accessService` (N:N): services expose distributions.
- `dataset` -> describedBy -> `dataSchema` (N:1): the schema fixes the data's shape.
- `dataset` -> derivedFrom -> `dataset` (N:N): lineage across processing steps.
- `qualityMeasurement` -> evaluates -> `dataset` (N:1): measured quality attaches to the asset.
- `registerEntry` -> catalogues -> `dataset` (1:1): the register anchors discoverability.

## Events

- `datasetPublished`: a dataset became available through at least one distribution.
- `distributionAdded`: a new format or channel was opened for an existing dataset.
- `schemaVersionAdopted`: the dataset switched to a new declared schema version.
- `qualityAssessed`: a quality measurement or fitness assessment was completed.
- `datasetDeprecated`: the holder marked the dataset as superseded or discouraged.
- `datasetWithdrawn`: the dataset was removed from service.

## Contracts

- `openDataLicenseContract`: standard public license terms attached to distributions.
- `dataSharingAgreement`: bilateral terms for controlled sharing of non-public datasets.
- `apiAccessContract`: service terms for programmatic access through an access service.

## Projections

- `openCataloguePage`: public descriptive metadata and open distributions; omits internal lineage and holder-only quality detail.
- `harvestFeed`: a DCAT-shaped serialization for catalogue aggregators; omits non-catalogue attributes.
- `stewardQualityDashboard`: quality scores, lineage and schema drift for the holder; omits public presentation fields.

## Composition

- REFERENCE `world.organization` (O1): data holders, publishers and service operators.
- REFERENCE `world.modelOntology` (N6): schemaReference resolves to schemas and models registered there.
- REFERENCE `world.identifierNaming` (N8): dataset and distribution identifiers come from registered schemes.
- REFERENCE `world.officialStatistics` (N10): statistical releases appear here as catalogued datasets while their statistical semantics stay in N10.
- imports: dcat (EXTEND): the catalogue backbone of dataset, distribution and data service is specialized by this model.
- imports: w3c-dqv (MIX-IN): the quality measurement facet applied to datasets and distributions.

## Stewardship

The neutral owner archetype is the data holder, the party accountable for the asset's content and service levels; catalogue operators list but do not own. Access is always granted by the holder through the catalogue's S1/S2 ownership and access models, with grants and harvests audited via S4.
