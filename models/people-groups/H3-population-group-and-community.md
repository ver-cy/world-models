# H3 Population Group & Community

This meta-model describes groups, cohorts and communities as addressable collectives: named groups with memberships and roles, rule-based statistical cohorts with their materialized snapshots, and the representation and channels that make a collective addressable as one party. It is its own model because collectives have identity, membership dynamics and spokesmanship of their own, distinct from the persons inside them and from any formal organization they may or may not become.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:h3"
  csn: world.populationGroup
  version: 0.2.0
  displayName: Population Group & Community
  description: Groups, cohorts and communities as addressable collectives with membership, representation and statistical materialization.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.populationGroup
bundles:
  - csn: world.populationGroup.collective
    displayName: Collective
    layers:
      - world.populationGroup.collective.groupIdentity
      - world.populationGroup.collective.membership
  - csn: world.populationGroup.cohort
    displayName: Cohort
    layers:
      - world.populationGroup.cohort.cohortDefinition
      - world.populationGroup.cohort.cohortMaterialization
  - csn: world.populationGroup.addressability
    displayName: Addressability
    layers:
      - world.populationGroup.addressability.representation
      - world.populationGroup.addressability.collectiveChannel
imports:
  - source: w3c-org
    version: "*"
  - source: skos
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `collective` | Named groups and their belonging | `groupIdentity`: groups and communities as named collectives · `membership`: member ties, roles, joining and leaving |
| `cohort` | Rule-based statistical collectives | `cohortDefinition`: criteria, time frames and population base of a cohort · `cohortMaterialization`: computed snapshots, counts and distributions |
| `addressability` | The collective as one addressable party | `representation`: stewards, spokespersons and their mandates · `collectiveChannel`: how the collective as a whole is reached |

## Objects

- `group`: a named collective of persons; key attributes: name, kind (community, cohort base, interest group), formation basis, status
- `community`: a group with shared life, practice or identity; key attributes: locality or bond, self-description, steward reference
- `membership`: a person's tie to a group; key attributes: person reference, role, visibility setting, start, end
- `memberRole`: a role within a group; key attributes: role type, mandate scope, appointment basis
- `cohortDefinition`: a rule-based population slice; key attributes: criteria expression, base population, time frame, defining authority reference
- `cohortSnapshot`: a materialized cohort at a point in time; key attributes: definition reference, timestamp, count, distribution summary
- `representationMandate`: an authorization to speak or act for the group; key attributes: holder reference, scope, grant basis, validity
- `collectiveChannel`: an address for the collective as one party; key attributes: channel type, endpoint pointer, steward reference

## Relationships

- `membership` -> ties -> `person` (n..1): each membership joins one natural person, resolved via H1, to one group
- `group` -> subgroupOf -> `group` (n..1): collectives nest into larger collectives
- `cohortDefinition` -> drawsOn -> `person` (n..m): cohort criteria evaluate person and household attributes without ever listing members publicly
- `cohortSnapshot` -> materializes -> `cohortDefinition` (n..1): snapshots are dated computations of a definition
- `representationMandate` -> authorizes -> `person` (n..1): a mandate names its holder and its scope
- `group` -> constitutedAs -> `organization` (0..1): a group that formalizes becomes an organization in O1 while keeping its collective history here
- `community` -> holds -> `norm` (n..m): communities are the holders of norms described in D9

## Events

- `groupFormed`: a collective came into existence with a name and basis
- `memberJoined`: a person joined a group at a chosen visibility
- `memberLeft`: a membership ended
- `mandateGranted`: the group granted a representation mandate
- `mandateRevoked`: a mandate was withdrawn or expired
- `cohortDefined`: a statistical cohort definition was fixed by its defining authority
- `snapshotTaken`: a cohort was materialized into counts and distributions
- `groupDissolved`: a collective ceased to exist

## Contracts

- `membershipDisclosureConsent`: each member's control over whether and where their membership is visible
- `cohortStatisticsContract`: the statistics office computes cohorts against protected data; only aggregates leave the boundary
- `collectiveAddressContract`: the rules under which third parties may address the collective through its channel

## Projections

- `publicGroupDirectory`: groups, self-descriptions and channels; omits member lists entirely
- `statisticalCohortView`: cohort counts and distributions; contains no individual records
- `stewardRoster`: current representation mandates and their scopes; omits ordinary membership

## Composition

- REFERENCE `world.person` (H1): members, stewards and mandate holders are natural persons referenced by identity
- REFERENCE `world.household` (H2): cohort criteria may evaluate household attributes as counting units
- REFERENCE `world.organization` (O1): formalized groups continue as organizations; the reference preserves continuity of the collective
- REFERENCE `world.socialNorm` (D9): communities are the norm-holders that D9 describes
- imports: W3C ORG (ALIGN): membership, role and organizational-structure semantics
- imports: SKOS (REFERENCE): classification schemes for group kinds and cohort domains

## Stewardship

A group steward owns each community's record and its addressability; the statistics office owns cohort definitions and snapshots and guarantees that only aggregates leave the protected layer. Membership visibility belongs to each member, and every access is granted by the respective owner through S1/S2 with audit via S4.
