# N5 Media & Creative Work

This meta-model describes works of media, art and entertainment along the ladder from abstract work to expression to published manifestation, together with who contributed, who holds rights, and how the work reaches audiences through releases and performances. It is its own model because creative works have identity above any file or edition (the same novel across translations, the same song across recordings), and this layered identity drives rights, distribution and cataloguing everywhere in the cultural economy.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n5"
  csn: world.creativeWork
  version: 0.2.0
  displayName: "Media & Creative Work"
  description: "Creative works, their expressions and manifestations, contributions, rights and distribution."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.creativeWork
bundles:
  - csn: world.creativeWork.work
    displayName: "Work"
    layers:
      - world.creativeWork.work.workIdentity
      - world.creativeWork.work.expressionAndEdition
      - world.creativeWork.work.manifestationAndItem
  - csn: world.creativeWork.rights
    displayName: "Rights"
    layers:
      - world.creativeWork.rights.authorshipAndContribution
      - world.creativeWork.rights.rightsAndLicensing
  - csn: world.creativeWork.distribution
    displayName: "Distribution"
    layers:
      - world.creativeWork.distribution.publicationAndRelease
      - world.creativeWork.distribution.performanceAndExhibition
imports:
  - source: schema-org
    version: "*"
  - source: ifla-lrm
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `work` | The layered identity of the creation | `workIdentity`: abstract works, types, genres · `expressionAndEdition`: translations, arrangements, cuts, editions · `manifestationAndItem`: formats, carriers, published objects |
| `rights` | Who made it and who controls it | `authorshipAndContribution`: creators and their roles · `rightsAndLicensing`: rights statements, territories, terms |
| `distribution` | How it reaches audiences | `publicationAndRelease`: releases, channels, territories · `performanceAndExhibition`: performances, screenings, exhibitions |

## Objects

- `creativeWork`: the abstract work above all versions; key attributes: workId, workType, genre, createdYear.
- `expression`: a realized version of the work; key attributes: expressionType, languageRef, completedAt.
- `manifestation`: a published embodiment of an expression; key attributes: format, carrier, publisherRef, releaseDate.
- `contribution`: a creator's role in the work; key attributes: contributorRef, role, share.
- `rightsStatement`: a claim of rights over the work; key attributes: rightType, holderRef, territory, term.
- `publicationRelease`: a release of manifestations to a channel; key attributes: channel, releasedAt, territory.
- `performance`: a live or broadcast rendering of an expression; key attributes: venueRef, performedAt, performerRefs.

## Relationships

- `creativeWork` -> realizedBy -> `expression` (1:N): translations, arrangements and cuts of one work.
- `expression` -> embodiedIn -> `manifestation` (1:N): editions and formats of one expression.
- `contribution` -> contributesTo -> `creativeWork` (N:1): authorship and other creative roles.
- `rightsStatement` -> covers -> `creativeWork` (N:N): rights claims scoped by territory and term.
- `creativeWork` -> derivedFrom -> `creativeWork` (N:N): adaptations, remixes, sequels.
- `publicationRelease` -> releases -> `manifestation` (1:N): what a release put into a channel.
- `performance` -> performs -> `expression` (N:1): the version actually rendered live.

## Events

- `workCreated`: a new abstract work came into existence.
- `expressionCompleted`: a translation, arrangement or edition was finished.
- `manifestationPublished`: a publishable embodiment entered circulation.
- `workPerformed`: the work was performed, screened or exhibited.
- `adaptationReleased`: a derived work reached the public.
- `rightsTransferred`: a rights statement changed holder.
- `workWithdrawn`: the work was withdrawn from circulation by its rights holder.

## Contracts

- `distributionLicenseContract`: terms for releasing manifestations through a channel or territory.
- `performanceRightsContract`: terms for public performance or exhibition of expressions.
- `archivalDepositContract`: deposit of manifestations with an archive or library, with preservation permissions.

## Projections

- `publicCatalogueEntry`: work, main expressions and available manifestations; omits rights shares and contract detail.
- `rightsClearanceView`: rights statements, holders, territories and terms for licensing work; omits distribution history.
- `releaseHistoryView`: the chronology of releases and performances; omits rights and contribution shares.

## Composition

- REFERENCE `world.person` (H1): creators, performers and individual rights holders.
- REFERENCE `world.organization` (O1): publishers, studios, labels and collecting bodies.
- REFERENCE `world.intellectualProperty` (N12): rights statements are formalized as registered rights and licenses there.
- REFERENCE `world.languageTerminology` (N9): languages of expressions and translation relationships.
- COMPOSE `world.documentRecord` (N1): textual manifestations may be held as governed documents.
- imports: schema-org (ALIGN): CreativeWork vocabulary for public description and discovery.
- imports: ifla-lrm (ALIGN): the work, expression, manifestation ladder and its identity rules.

## Stewardship

The neutral owner archetype is the author or current rights holder; libraries, archives and platforms hold copies and listings without owning the work. Access to non-public detail is always granted by the owner through the catalogue's S1/S2 ownership and access models, with licensing activity audited via S4.
