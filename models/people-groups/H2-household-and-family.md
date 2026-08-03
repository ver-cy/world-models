# H2 Household & Family

This meta-model describes households as dwelling-sharing units and families as webs of registered and lived relations: membership, kinship, dependency and care, and the residence linkage that ties a household to a dwelling. It is its own model because the household is simultaneously a social unit (who lives together), an administrative unit (registered relations, dependency) and a statistical unit (the census household), and these three readings must be kept coherent on one shared structure.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:h2"
  csn: world.household
  version: 0.2.0
  displayName: Household & Family
  description: Households and family relations as social, administrative and statistical units.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.household
bundles:
  - csn: world.household.composition
    displayName: Composition
    layers:
      - world.household.composition.householdUnit
      - world.household.composition.membership
  - csn: world.household.kinship
    displayName: Kinship
    layers:
      - world.household.kinship.familyRelation
      - world.household.kinship.dependencyAndCare
  - csn: world.household.residence
    displayName: Residence
    layers:
      - world.household.residence.domicile
imports:
  - source: schema-org
    version: "*"
  - source: un-census-recommendations
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `composition` | Who forms the unit | `householdUnit`: the dwelling-sharing unit itself Â· `membership`: member ties, roles and tenure of belonging |
| `kinship` | How members are related | `familyRelation`: registered and lived kinship ties Â· `dependencyAndCare`: dependants, caregiving and maintenance arrangements |
| `residence` | Where the unit lives | `domicile`: declared and registered residence linkage to dwellings |

## Objects

- `household`: a dwelling-sharing unit; key attributes: identifier, formation date, type (single, family, collective), status
- `householdMembership`: a person's belonging to a household; key attributes: person reference, role, start, end
- `householdRole`: a role within the unit; key attributes: role type (head or reference member, dependant, other), basis
- `familyRelation`: a typed kinship tie between persons; key attributes: relation type, registration status, effective period
- `dependency`: a recognized dependency of one person on another or on the unit; key attributes: dependant reference, basis, degree, period
- `careArrangement`: a caregiving arrangement; key attributes: caregiver reference, cared-for reference, scope, formality
- `residenceRecord`: the household's residence at a dwelling; key attributes: dwelling reference, kind (registered, actual), period

## Relationships

- `householdMembership` -> joins -> `person` (n..1): each membership ties one person, resolved via H1, into one household
- `household` -> comprises -> `householdMembership` (1..n): the unit exists through its memberships
- `familyRelation` -> relates -> `person` (n..m): kinship ties connect persons pairwise, inside or across households
- `dependency` -> supports -> `person` (n..1): a dependency names its dependant and its supporting party
- `residenceRecord` -> locates -> `household` (n..1): residence records place the unit at a dwelling in the built-environment model (U)
- `household` -> countedIn -> `cohortDefinition` (n..m): households enter statistical cohorts defined in H3 without exposing members

## Events

- `householdFormed`: a new household unit came into existence
- `memberJoined`: a person entered a household
- `memberLeft`: a person left a household
- `relationRegistered`: a family relation (marriage, partnership, adoption, parentage) was registered
- `relationDissolved`: a registered relation was dissolved or annulled
- `residenceChanged`: the household's registered or actual residence changed
- `householdDissolved`: the unit ceased to exist

## Contracts

- `householdSelfManagement`: the members' joint mandate to maintain their own unit record
- `registeredRelationExtract`: registrar-certified extracts of registered relations for administrative use
- `censusAggregation`: release of household data to the statistics office in anonymized, aggregated form only

## Projections

- `administrativeHouseholdView`: registered relations, roles and residence for administrative consumers; omits informal care detail
- `censusUnitView`: household size, type and composition shape for statistics; contains no identities
- `memberSelfView`: a member's own view of the unit and every relation concerning them

## Composition

- REFERENCE `world.person` (H1): every member, relative, dependant and caregiver is a natural person referenced by identity, never copied
- REFERENCE `world.buildingAndFacility` (U): residence records point to dwellings governed by the built-environment model
- REFERENCE `world.populationGroup` (H3): households feed statistical cohorts as counting units
- imports: schema.org (ALIGN): public typing for household and family concepts
- imports: UN census recommendations (ALIGN): household and family definitions used for the statistical reading of the unit

## Stewardship

The household members jointly own the unit's record; the civil registrar owns registered relations within it. Access to any household or kinship data is granted by the respective owner through the catalogue's S1/S2 ownership and access models, with audit via S4.
