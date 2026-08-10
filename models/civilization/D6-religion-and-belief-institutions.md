# D6 Religion & Belief Institutions

This meta-model describes confessions and belief traditions, the congregations and communities organized around them, and their practices: rites, observances, calendars and sites. It is its own model because religious life combines a doctrinal taxonomy, community institutions and a practice calendar in a way no generic organization or event model covers, and because the data it touches (personal affiliation above all) carries the strongest subject-protection defaults in the catalogue.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:d6"
  csn: world.religionBelief
  version: 0.2.0
  displayName: Religion & Belief Institutions
  description: Confessions and belief traditions, congregations, practices, observance calendars and sacred sites.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.religionBelief
bundles:
  - csn: world.religionBelief.confession
    displayName: Confession
    layers:
      - world.religionBelief.confession.traditionTaxonomy
      - world.religionBelief.confession.doctrineAndText
  - csn: world.religionBelief.congregation
    displayName: Congregation
    layers:
      - world.religionBelief.congregation.communityBody
      - world.religionBelief.congregation.ministryRole
  - csn: world.religionBelief.practice
    displayName: Practice
    layers:
      - world.religionBelief.practice.riteAndObservance
      - world.religionBelief.practice.observanceCalendar
imports:
  - source: cidoc-crm
    version: "*"
  - source: skos
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `confession` | Belief traditions as described bodies of doctrine | `traditionTaxonomy`: religions, denominations, schools and their lineage · `doctrineAndText`: creeds and canonical texts as documented heritage artifacts |
| `congregation` | Organized communities of belief | `communityBody`: congregations, orders and associations as living communities · `ministryRole`: clergy, ministers and lay service roles |
| `practice` | Observance in time and place | `riteAndObservance`: rites, services and observances as practiced · `observanceCalendar`: liturgical calendars and recurring observance dates |

## Objects

- `confession`: a religion, denomination or school of belief; key attributes: name, lineage position, doctrinal summary, classification codes
- `doctrineText`: a creed or canonical text described as a heritage artifact; key attributes: title, tradition, language, documentation reference
- `congregation`: a local community of a confession; key attributes: name, confession reference, organization reference, locality
- `ministryRole`: a service role within a congregation; key attributes: role type, ordination requirements, holder reference
- `rite`: a defined ritual or service form; key attributes: name, confession, occasion, participants pattern
- `observanceDay`: a recurring holy day or observance; key attributes: name, calendar rule, confession, obligation character
- `sacredSite`: a place of worship or veneration; key attributes: name, site reference, consecration status, custodian reference
- `affiliation`: a person's declared tie to a confession or congregation; key attributes: declaration date, visibility setting, standing

## Relationships

- `confession` -> branchOf -> `confession` (n..1): denominational lineage within a tradition
- `congregation` -> professes -> `confession` (n..1): each congregation belongs to a confession
- `congregation` -> gathersAt -> `sacredSite` (n..m): communities use one or more sites for worship
- `rite` -> observedBy -> `congregation` (n..m): which communities practice which rites
- `observanceDay` -> definedBy -> `confession` (n..1): observances belong to a tradition's calendar
- `affiliation` -> declares -> `person` (n..1): the affiliation subject is a natural person in H1, and the record stays under that person's control
- `ministryRole` -> heldBy -> `person` (n..0..1): a role may be vacant or held by one person at a time

## Events

- `congregationFounded`: a community was established under a confession
- `congregationDissolved`: a community ceased to exist or merged
- `siteConsecrated`: a site was dedicated for worship by its tradition
- `observanceHeld`: a calendar observance took place in a community
- `riteCelebrated`: a rite was performed on a recordable occasion
- `affiliationDeclared`: a person declared an affiliation, at a visibility they chose
- `affiliationWithdrawn`: a person withdrew a previously declared affiliation

## Contracts

- `communityDirectoryAccess`: publication of a congregation's public listing, granted by the community itself
- `affiliationDisclosureConsent`: per-person consent governing any visibility of affiliation data, grounded in S1
- `heritageResearchAccess`: scholarly access to doctrine, texts and site documentation granted by the tradition's custodians

## Projections

- `publicCongregationDirectory`: congregations, sites and service times; omits membership and affiliation entirely
- `observanceCalendarView`: holy days and observance dates per confession; omits community-internal scheduling
- `heritageCatalogue`: doctrine texts, lineage and sites as documented heritage; omits all living-person data

## Composition

- REFERENCE `world.organization` (O1): a congregation's legal and administrative body is an organization; this model holds the community and practice semantics on top of that reference
- REFERENCE `world.person` (H1): affiliation subjects and role holders are natural persons; affiliation is among the most protected personal facts
- REFERENCE `world.buildingAndFacility` (U): sacred sites resolve to places and structures of the built environment
- REFERENCE `world.socialNorm` (D9): customs and observances entwined with religious practice are cross-linked to the norm and custom model
- imports: CIDOC CRM (ALIGN): heritage documentation semantics for texts, rites and sites
- imports: SKOS (REFERENCE): confession and tradition taxonomies as concept schemes

## Stewardship

The communities themselves steward their confession, congregation and practice data, with strong subject-protection defaults throughout. Personal affiliation belongs to the person and is visible only under that person's own grant; all access flows through the catalogue's S1/S2 ownership and access models and is audited via S4.
