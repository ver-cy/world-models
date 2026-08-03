# N4 Software Product & System

This meta-model describes software in full context: products offered by producers, their releases and components, declared dependencies, and the deployed systems and environments where releases actually run. It is its own model because software has a double life, as a published artifact with versions and licenses and as an operated system with environments and advisories, and the two must be described together to answer questions about provenance, exposure and lifecycle.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n4"
  csn: world.softwareProduct
  version: 0.2.0
  displayName: "Software Product & System"
  description: "Software products, releases, components, dependencies and the deployed systems that run them."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.softwareProduct
bundles:
  - csn: world.softwareProduct.product
    displayName: "Product"
    layers:
      - world.softwareProduct.product.identity
      - world.softwareProduct.product.release
  - csn: world.softwareProduct.architecture
    displayName: "Architecture"
    layers:
      - world.softwareProduct.architecture.systemComposition
      - world.softwareProduct.architecture.dependencyAndSbom
  - csn: world.softwareProduct.operation
    displayName: "Operation"
    layers:
      - world.softwareProduct.operation.deploymentAndEnvironment
      - world.softwareProduct.operation.lifecycleAndSupport
imports:
  - source: aismm
    version: "*"
  - source: spdx
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `product` | The offered software artifact | `identity`: products, producers, categories Â· `release`: versions, channels, publication |
| `architecture` | What the software is made of | `systemComposition`: components and their assembly Â· `dependencyAndSbom`: declared dependencies and bill of materials |
| `operation` | Where and how it runs | `deploymentAndEnvironment`: deployed systems, environments, instances Â· `lifecycleAndSupport`: support status, advisories, end of life |

## Objects

- `softwareProduct`: a software offering with identity and producer; key attributes: productId, name, category, producerRef, lifecycleStatus.
- `release`: a published version of a product; key attributes: version, releasedAt, channel, checksum.
- `component`: a constituent part of a release; key attributes: componentId, componentType, packageRef.
- `dependency`: a declared need on another component or release; key attributes: constraintRange, scope, resolvedReleaseRef.
- `deployedSystem`: a running installation serving a purpose; key attributes: systemId, purpose, operatorRef, criticality.
- `environment`: a hosting context for systems; key attributes: environmentType, locationRef, platform.
- `advisory`: a published notice about defects or exposure; key attributes: advisoryId, severity, affectedRange, publishedAt.

## Relationships

- `softwareProduct` -> publishes -> `release` (1:N): the product's version history.
- `release` -> composedOf -> `component` (1:N): the release's bill of materials.
- `release` -> declares -> `dependency` (1:N): stated needs on other software.
- `dependency` -> resolvesTo -> `release` (N:1): the concrete release satisfying a declared need.
- `deployedSystem` -> runs -> `release` (N:N): which versions are live where.
- `deployedSystem` -> hostedIn -> `environment` (N:1): the system's hosting context.
- `advisory` -> affects -> `release` (N:N): exposure mapping from notice to versions.

## Events

- `releasePublished`: a new version became available on a channel.
- `releaseWithdrawn`: a published version was pulled from distribution.
- `systemDeployed`: a release went live in an environment.
- `systemDecommissioned`: a deployed system was retired.
- `advisoryIssued`: a defect or exposure notice was published.
- `endOfLifeAnnounced`: the producer declared the end of support for a product or release line.

## Contracts

- `softwareLicenseContract`: the usage license attached to releases.
- `supportAndMaintenanceContract`: producer or operator obligations for a product or system.
- `sbomDisclosureContract`: terms of sharing the dependency bill of materials with consumers.

## Projections

- `productCataloguePage`: public product and release information; omits deployment and operator detail.
- `sbomExport`: the component and dependency graph of a release; omits product marketing and operations.
- `operationsInventory`: systems, environments and running versions for the operator; omits producer-side release internals.

## Composition

- imports: aismm (ALIGN): whole-model binding; every bundle of this model aligns to the corresponding AISMM area so a full AISMM product model can stand behind any record here.
- REFERENCE `world.organization` (O1): producing organizations and system operators.
- REFERENCE `world.intellectualProperty` (N12): licenses and other rights over software subject matter.
- REFERENCE `world.dataset` (N3): datasets produced or consumed by deployed systems.
- REFERENCE `world.identifierNaming` (N8): package and product identifier schemes.
- imports: spdx (ALIGN): bill of materials structure and license expressions.

## Stewardship

The neutral owner archetype is the producing organization for products and releases, and the operator for deployed systems; each owns its slice of the record. Access is always granted by the respective owner through the catalogue's S1/S2 ownership and access models, with disclosure of SBOMs and inventories audited via S4.
