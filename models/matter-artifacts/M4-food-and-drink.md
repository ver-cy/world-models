# M4 Food & Drink

This meta-model describes nutrition goods and their safety: what a food or drink product contains, what it delivers nutritionally, how long it keeps, and whether it is currently safe to consume. It is its own model because ingredient declarations, nutrient profiles, allergens and recall status form a tightly coupled semantic block with its own authorities and its own tempo (reformulations, alerts, expiry), distinct from generic goods cataloguing which it extends.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m4"
  csn: world.foodDrink
  version: 0.2.0
  displayName: "Food & Drink"
  description: Food and drink products with ingredients, allergens, nutrient profiles, shelf life and safety status.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.foodDrink
bundles:
  - csn: world.foodDrink.product
    displayName: Product
    layers:
      - world.foodDrink.product.foodIdentity
      - world.foodDrink.product.ingredientDeclaration
      - world.foodDrink.product.allergenDeclaration
  - csn: world.foodDrink.nutrition
    displayName: Nutrition
    layers:
      - world.foodDrink.nutrition.nutrientProfile
      - world.foodDrink.nutrition.servingAndPortion
  - csn: world.foodDrink.safety
    displayName: Safety
    layers:
      - world.foodDrink.safety.shelfLifeAndStorage
      - world.foodDrink.safety.safetyStatus
imports:
  - source: foodon
    version: "*"
  - source: fao-infoods
    version: "*"
  - source: codex-alimentarius
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `product` | What the food is and what it is made of | `foodIdentity`: product name, food category, form (fresh, processed, beverage), producer reference · `ingredientDeclaration`: ordered ingredient list with proportions and processing roles · `allergenDeclaration`: declared allergens, contains and may-contain statements |
| `nutrition` | What consuming it delivers | `nutrientProfile`: nutrient values per reference basis with tagname coding · `servingAndPortion`: serving sizes, portions per pack, reference intake basis |
| `safety` | Whether and how long it is safe | `shelfLifeAndStorage`: durability dates, storage instructions, after-opening rules · `safetyStatus`: alerts, withdrawals and recalls with scope and resolution |

## Objects

- `foodItem`: a food or drink product class; key attributes: name, category, form, producer reference.
- `ingredientEntry`: one line of the ingredient declaration; key attributes: rank, ingredient reference, proportion, role.
- `allergenDeclaration`: a declared allergen relationship; key attributes: allergen code, statement type (contains, may contain), basis.
- `nutrientValue`: one nutrient measurement or declaration; key attributes: nutrient tagname, value, unit, basis (per 100 g, per serving).
- `servingSpec`: a declared serving; key attributes: serving size, unit, servings per pack.
- `shelfLifeSpec`: durability of the product; key attributes: date type (best before, use by), duration, storage conditions.
- `safetyStatus`: the current or historical safety standing; key attributes: status, reason, scope, effective period.
- `foodBatch`: a production batch of the product; key attributes: batch code, production date, durability date, quantity.

## Relationships

- `foodItem` -> declares -> `ingredientEntry` (1..*): the ordered ingredient list defines the recipe as declared.
- `foodItem` -> carries -> `allergenDeclaration` (0..*): allergen statements attach at product level.
- `foodItem` -> profiledBy -> `nutrientValue` (0..*): nutrient values accumulate per basis and method.
- `foodItem` -> servedAs -> `servingSpec` (0..*): one product may declare several serving bases.
- `foodItem` -> keptUnder -> `shelfLifeSpec` (1..*): every food has at least one durability rule.
- `foodBatch` -> ofFoodItem -> `foodItem` (many-to-one): batches bound production populations of the product.
- `safetyStatus` -> appliesTo -> `foodBatch` (0..*): safety standing can target specific batches or the whole product.

## Events

- `recipeRevised`: the ingredient declaration of the product changed.
- `nutritionDeclared`: a nutrient profile was published or superseded.
- `allergenAdvisoryChanged`: allergen statements were added, removed or reworded.
- `batchProduced`: a production batch came into existence with its durability dates.
- `safetyAlertRaised`: an alert was issued for the product or specific batches.
- `batchWithdrawn`: a batch was withdrawn from distribution or recalled from consumers.
- `shelfLifeExpired`: a batch passed its durability date and left saleable status.

## Contracts

- `labelDataAccess`: supply of label-equivalent data (ingredients, allergens, nutrition, dates) to retailers, apps and carriers of the product.
- `allergenNotification`: subscription for parties who must learn immediately when allergen declarations change.
- `recallBroadcast`: wide, priority distribution of safety alerts and withdrawal notices to holders of affected batches.

## Projections

- `consumerLabelView`: exactly what a label shows (ingredients, allergens, nutrition per basis, dates); omits batch and supply data.
- `dietPlanningView`: nutrient values and servings only, for meal and diet computation; omits safety and production facts.
- `safetyAuthorityView`: batches, durability, safety status and producer references; omits marketing content.

## Composition

- EXTEND `world.tradableGood` (M3): a food item is a good; identifiers, packaging and batch mechanics are inherited, nutrition and safety semantics are added.
- REFERENCE `world.materialSubstance` (M1): ingredient entries and additives resolve to substance classes (additive codes, compounds).
- REFERENCE `world.physicalItem` (M2): an individually tracked pack (a serialized case, a returned unit) is an item.
- imports: foodon (ALIGN): ontology alignment for food categories and ingredient kinds.
- imports: fao-infoods (REFERENCE): nutrient tagname scheme for the nutrient profile layer.
- imports: codex-alimentarius (ALIGN): labelling and food safety concept alignment.

## Stewardship

Each food product record is stewarded by its producer or current holder per the catalogue's S1 ownership model; label data and safety notices flow to other parties only under S1/S2 grants, with recall broadcasts audited via S4.
