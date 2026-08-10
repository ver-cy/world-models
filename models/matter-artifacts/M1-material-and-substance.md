# M1 Material & Substance

This meta-model describes chemical substances and engineered materials as classes of matter: what they are made of, how they behave, how hazardous they are, and where physical stocks of them exist as lots. It is its own model because substance-level facts (identity, composition, hazard) are class knowledge maintained once for the whole world, while every other model in the catalogue that touches matter (items, foods, medicines, artifacts) only points at these classes instead of restating chemistry.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m1"
  csn: world.materialSubstance
  version: 0.2.0
  displayName: "Material & Substance"
  description: Chemical substances and engineered materials, their composition, properties, hazard classification and physical lots.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.materialSubstance
bundles:
  - csn: world.materialSubstance.identity
    displayName: Identity
    layers:
      - world.materialSubstance.identity.substanceIdentity
      - world.materialSubstance.identity.nomenclature
      - world.materialSubstance.identity.composition
  - csn: world.materialSubstance.behavior
    displayName: Behavior
    layers:
      - world.materialSubstance.behavior.physicalChemical
      - world.materialSubstance.behavior.stabilityReactivity
  - csn: world.materialSubstance.hazard
    displayName: Hazard
    layers:
      - world.materialSubstance.hazard.hazardClassification
      - world.materialSubstance.hazard.handlingPrecaution
  - csn: world.materialSubstance.occurrence
    displayName: Occurrence
    layers:
      - world.materialSubstance.occurrence.lotAndStock
imports:
  - source: cas
    version: "*"
  - source: chebi
    version: "*"
  - source: un-ghs
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `identity` | What a substance or material is and what it consists of | `substanceIdentity`: registry identifiers, structure references, form (pure substance, mixture, alloy, polymer) · `nomenclature`: systematic, trade and common names with language and context · `composition`: constituent entries with proportions, purity grades and impurity ranges |
| `behavior` | Measured and declared behavior of the class | `physicalChemical`: state, density, melting and boiling points, solubility and comparable determinations · `stabilityReactivity`: stability conditions, incompatibilities, decomposition products |
| `hazard` | Danger the class poses and how to handle it | `hazardClassification`: hazard classes, categories and signal words per classification scheme · `handlingPrecaution`: precautionary and first-aid statements, storage class requirements |
| `occurrence` | Where quantities of the class physically exist | `lotAndStock`: produced lots, quantities on hand, storage conditions and custody references |

## Objects

- `substance`: a single chemical entity; key attributes: registry identifiers, molecular formula, structure reference, form.
- `material`: an engineered or natural material defined by composition rather than a single molecule (steel grade, timber, fabric); key attributes: material family, grade, specification reference.
- `compositionEntry`: one constituent line of a material or mixture; key attributes: constituent reference, proportion range, role (base, additive, impurity).
- `identifierRecord`: an assignment of an external registry identifier to a substance or material; key attributes: scheme, code, assignment date.
- `propertyValue`: one determined or declared property of the class; key attributes: property kind, value, unit, method, conditions.
- `hazardClassification`: a hazard class and category assigned to a substance or material; key attributes: scheme, class, category, signal word.
- `materialLot`: a produced, bounded quantity of a material or substance; key attributes: lot code, quantity, unit, production date, holder reference.
- `storageCondition`: conditions a lot is kept under; key attributes: temperature range, humidity, containment type, segregation rules.

## Relationships

- `material` -> composedOf -> `compositionEntry` (1..*): a material is defined by its ordered constituent entries.
- `compositionEntry` -> resolvesTo -> `substance` (many-to-one): each entry points at the substance it consists of.
- `substance` -> registeredUnder -> `identifierRecord` (0..*): external registry identifiers attach without replacing native identity.
- `substance` -> classifiedAs -> `hazardClassification` (0..*): a substance may carry several hazard classes at once.
- `substance` -> characterizedBy -> `propertyValue` (0..*): determinations accumulate over time and methods.
- `materialLot` -> instanceOf -> `material` (many-to-one): every lot is a quantity of exactly one class.
- `materialLot` -> keptUnder -> `storageCondition` (0..*): current and required storage conditions for the lot.

## Events

- `substanceRegistered`: a new substance or material class entered the model with its initial identity.
- `compositionRevised`: the declared composition of a material changed (reformulation, purity change).
- `propertyDetermined`: a measurement or authoritative declaration added a property value.
- `hazardReclassified`: the hazard classification of a class changed under a scheme revision or new evidence.
- `lotProduced`: a bounded quantity of a class came into existence with a lot code.
- `lotTransferred`: custody of a lot moved to another holder.
- `lotDepleted`: a lot was consumed, disposed of or otherwise ceased to exist as stock.

## Contracts

- `safetyDataAccess`: read access to hazard and precaution layers for anyone handling or transporting the class; typically broad, since safety data is meant to travel with the matter.
- `stockDisclosure`: holder-granted visibility of lot quantities and locations to a named counterparty (auditor, insurer, buyer).
- `classificationFeed`: subscription to reclassification and composition-revision events for downstream models that embed references to this one.

## Projections

- `safetyDataSheetView`: identity, hazard, handling and stability for one class; omits stock, holders and commercial context.
- `transportView`: hazard class, packing and segregation facts needed by carriers; omits composition detail and property history.
- `catalogueChemistryView`: identity, nomenclature and key properties for catalogue builders; omits lots and precaution text.

## Composition

- REFERENCE `world.physicalItem` (M2): a lot stored in a drum or container is containerized as an identifiable item; item-level material declarations point back at classes here.
- REFERENCE `world.place` (P1): production and storage sites of lots resolve to place identities rather than local address fields.
- REFERENCE (inbound) from `world.foodDrink` (M4) and `world.medicine` (M5): ingredient and active-substance links resolve into this model; `world.culturalArtifact` (M9) resolves materials and techniques here.
- imports: cas (REFERENCE): registry numbers as the primary external identifier scheme for substances.
- imports: chebi (ALIGN): ontology alignment for biologically relevant substances and roles.
- imports: un-ghs (REFERENCE): hazard classes, categories and precautionary statement codes.

## Stewardship

Class-level substance and material records are stewarded by a standards registrar archetype that curates identity, composition and hazard facts; each lot record is stewarded by its holder. Access to any record is granted by its owner through the catalogue's S1/S2 ownership and access models, with changes traceable via S4 audit.
