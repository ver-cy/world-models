# D9 Social Norm & Custom

This meta-model describes the informal rules of social life: norms, customs, traditions and etiquette that bind communities without being law, together with the informal sanctions that uphold them and the observations that evidence them. It is its own model because these rules are observed rather than decreed, they have holders (communities) rather than issuers, and their lifecycle (emergence, drift, contestation, lapse) follows social dynamics that no legal or organizational model represents.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:d9"
  csn: world.socialNorm
  version: 0.2.0
  displayName: Social Norm & Custom
  description: Informal rules, customs, traditions and etiquette held by communities, with informal sanctions and observed practice.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.socialNorm
bundles:
  - csn: world.socialNorm.norm
    displayName: Norm
    layers:
      - world.socialNorm.norm.normStatement
      - world.socialNorm.norm.applicabilityScope
  - csn: world.socialNorm.custom
    displayName: Custom
    layers:
      - world.socialNorm.custom.tradition
      - world.socialNorm.custom.transmission
  - csn: world.socialNorm.enforcement
    displayName: Enforcement
    layers:
      - world.socialNorm.enforcement.informalSanction
      - world.socialNorm.enforcement.complianceObservation
imports:
  - source: social-science
    version: "*"
  - source: skos
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `norm` | Informal rules as described statements | `normStatement`: the rule as observed and articulated Â· `applicabilityScope`: which community, setting and situation the rule binds |
| `custom` | Practiced traditions and etiquette | `tradition`: customs, traditions and etiquette forms Â· `transmission`: how customs pass on, drift and lapse |
| `enforcement` | How communities uphold their rules | `informalSanction`: disapproval, exclusion and reputation responses Â· `complianceObservation`: documented adherence, deviation and contestation |

## Objects

- `norm`: an informal rule held by a community; key attributes: statement, strength, holder reference, codification status
- `custom`: a practiced tradition; key attributes: name, occasion, form, transmission mode
- `etiquetteRule`: a situational conduct expectation; key attributes: setting, expected behavior, breach severity
- `applicabilityScope`: where and to whom a rule applies; key attributes: community reference, setting, situation, exceptions
- `informalSanction`: a typical community response to breach; key attributes: form, severity, typical duration
- `practiceObservation`: a documented instance of practice or breach; key attributes: date, setting, method, observer class
- `contestation`: a documented challenge to a norm; key attributes: challenger community segment, grounds, period

## Relationships

- `norm` -> heldBy -> `community` (n..m): norms belong to the communities that live them, resolved via H3
- `custom` -> practicedIn -> `community` (n..m): customs are located in practicing communities
- `norm` -> scopedBy -> `applicabilityScope` (1..n): every norm declares where it binds
- `informalSanction` -> respondsTo -> `norm` (n..1): sanctions are typed responses to specific norms
- `practiceObservation` -> evidences -> `custom` (n..1): observations are the evidential base of every description
- `contestation` -> challenges -> `norm` (n..1): contestation records a live challenge without judging it
- `norm` -> codifiedInto -> `legalRule` (0..1): when a custom becomes law, the successor lives in the law model (R) and this record marks the boundary

## Events

- `normObserved`: a norm was first documented from observed practice
- `customPerformed`: a documented performance of a custom took place
- `sanctionApplied`: a community applied an informal sanction to a recorded breach
- `contestationRaised`: a segment of the community openly challenged a norm
- `normShifted`: accumulated observations established that the rule's content or strength changed
- `customLapsed`: observation ceased to find the custom in practice

## Contracts

- `ethnographicResearchAccess`: community-granted access for systematic study of its norms and customs
- `communityReviewContract`: the holder community reviews and validates descriptions of its own norms before publication
- `descriptiveCatalogueAccess`: public access to validated, aggregated norm and custom descriptions

## Projections

- `etiquetteGuide`: practical conduct expectations for visitors and newcomers by setting; omits sanction records and observations
- `normAtlas`: norms and customs by community and scope with strength indicators; built on aggregated observations only
- `changeTimeline`: how norms shifted, were contested or lapsed over time; omits individual observation details

## Composition

- REFERENCE `world.populationGroup` (H3): the holders of every norm and custom are communities and groups; this model never defines communities itself
- REFERENCE `world.religionBelief` (D6): religiously grounded observances cross-link to their tradition's practice records
- REFERENCE `world.lawAndRegulation` (R): the codification boundary; a norm that becomes law is thereafter the law model's fact
- REFERENCE `world.publicDiscourse` (D8): contested norms surface as discourse topics; contestation records link across
- imports: social science practice (ALIGN): descriptive and observational method vocabulary
- imports: SKOS (REFERENCE): classification schemes for norm domains, settings and custom types

## Stewardship

The holder communities steward descriptions of their own norms and customs; the model records what is observed, never what anyone decrees. Publication requires community validation, and access is granted by the community steward through the catalogue's S1/S2 ownership and access models with audit via S4.
