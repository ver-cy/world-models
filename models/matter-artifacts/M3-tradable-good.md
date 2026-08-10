# M3 Tradable Good

This meta-model describes items in their market aspect: the good as a saleable class with its classification codes, identifiers, units of measure, packaging hierarchy and batch structure. It is its own model because market-facing description evolves on catalogue time (assortments, codes, pack changes) independently of both the chemistry of matter (M1) and the life of individual instances (M2), and because exchange models across the catalogue need a stable good identity to transact against.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m3"
  csn: world.tradableGood
  version: 0.2.0
  displayName: Tradable Good
  description: Goods as market classes with classification, identifiers, units, packaging hierarchy and batches.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.tradableGood
bundles:
  - csn: world.tradableGood.catalogue
    displayName: Catalogue
    layers:
      - world.tradableGood.catalogue.goodDefinition
      - world.tradableGood.catalogue.variantStructure
  - csn: world.tradableGood.identification
    displayName: Identification
    layers:
      - world.tradableGood.identification.identifierAssignment
      - world.tradableGood.identification.classificationCoding
  - csn: world.tradableGood.packaging
    displayName: Packaging
    layers:
      - world.tradableGood.packaging.packagingHierarchy
      - world.tradableGood.packaging.unitOfMeasure
  - csn: world.tradableGood.flow
    displayName: Flow
    layers:
      - world.tradableGood.flow.batchLot
imports:
  - source: gs1-gpc
    version: "*"
  - source: gs1-gtin
    version: "*"
  - source: unspsc
    version: "*"
  - source: unece-rec20
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `catalogue` | The good as a described market class | `goodDefinition`: name, description, brand reference, origin declaration, lifecycle status · `variantStructure`: variants (size, colour, flavour) and their relation to the base good |
| `identification` | How the market names and codes the good | `identifierAssignment`: identifier scheme assignments at each packaging level · `classificationCoding`: classification codes from one or more schemes with validity periods |
| `packaging` | How the good is quantified and packed | `packagingHierarchy`: each, inner pack, case, pallet levels and their containment · `unitOfMeasure`: net content, sale units and measure codes |
| `flow` | Bounded production populations of the good | `batchLot`: batches with production references, date ranges and recall status |

## Objects

- `good`: a saleable class of item; key attributes: name, description, brand reference, origin, status.
- `goodVariant`: a variant of a base good; key attributes: varying dimension, variant value, own identifiers.
- `classificationCode`: a classification assignment; key attributes: scheme, code, validity period.
- `identifierAssignment`: an identifier issued for the good at a packaging level; key attributes: scheme, value, level, issue date.
- `packagingLevel`: one level of the pack hierarchy; key attributes: level type, contained quantity, dimensions, weight.
- `unitOfMeasure`: the measure a good is quantified in; key attributes: measure code, net content, basis.
- `batch`: a bounded production population; key attributes: batch code, production window, quantity, recall status.

## Relationships

- `goodVariant` -> variantOf -> `good` (many-to-one): variants share the base good's definition and differ on declared dimensions.
- `good` -> classifiedBy -> `classificationCode` (1..*): at least one scheme places the good in a market taxonomy.
- `good` -> packagedAs -> `packagingLevel` (1..*): every good has at least a base unit level.
- `packagingLevel` -> contains -> `packagingLevel` (0..*): higher levels aggregate lower levels with fixed quantities.
- `identifierAssignment` -> assignedAt -> `packagingLevel` (many-to-one): identifiers are level-specific (an each and a case differ).
- `good` -> measuredIn -> `unitOfMeasure` (1..*): net content and sale measures for the good.
- `batch` -> ofGood -> `good` (many-to-one): each batch belongs to exactly one good or variant.

## Events

- `goodDefined`: a new good entered the catalogue with its initial definition.
- `variantIntroduced`: a variant of an existing good was declared.
- `identifierAssigned`: an identifier was issued for the good at a packaging level.
- `classificationRevised`: the good moved within a classification scheme or a scheme revision re-coded it.
- `packagingChanged`: the pack hierarchy or net content of the good changed.
- `batchReleased`: a production batch was released into circulation.
- `batchRecalled`: a batch was recalled from circulation.
- `goodDiscontinued`: the good ceased to be offered as a market class.

## Contracts

- `catalogueSyndication`: ongoing supply of good definitions, identifiers and pack data to trading partners and marketplaces.
- `identifierVerification`: query contract answering whether an identifier is genuine, what good and level it names, and its status.
- `traceabilityDisclosure`: batch-level disclosure to a named party (buyer, authority) for a stated purpose and period.

## Projections

- `retailListingView`: name, brand, variant, net content and consumer-level identifier; omits batches and case-level logistics data.
- `customsClassificationView`: classification codes, origin and measures needed at borders; omits commercial description and variants.
- `traceabilityView`: batches, their windows and recall status; omits catalogue marketing content.

## Composition

- REFERENCE `world.physicalItem` (M2): serialized instances of a good are items; the item's kind reference resolves here.
- REFERENCE `world.materialSubstance` (M1): composition and hazard disclosures attached to a good resolve to substance classes.
- EXTEND (inbound): `world.foodDrink` (M4) and `world.medicine` (M5) specialize the good with nutrition and medicinal semantics.
- REFERENCE (inbound) from the exchange cluster (X): offers, sales and settlements refer to good identities defined here; this model holds no transaction facts itself.
- imports: gs1-gpc (REFERENCE): brick-level product classification scheme.
- imports: gs1-gtin (REFERENCE): identifier scheme for goods at each packaging level.
- imports: unspsc (REFERENCE): procurement-oriented classification alternative.
- imports: unece-rec20 (REFERENCE): code list for units of measure.

## Stewardship

Each good record is stewarded by its seller or holder as established in the catalogue's S1 ownership model; syndication and lookup by other parties happen only under grants issued through S1/S2, with S4 providing the audit trail.
