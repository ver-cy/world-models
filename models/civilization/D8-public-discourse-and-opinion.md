# D8 Public Discourse & Opinion

This meta-model describes what publics talk about and what they think: discourse topics and the arenas where they circulate, the measurement of opinion through polls with open methodology, and organized information campaigns with their messages and reach. It is its own model because opinion is a measured, methodology-dependent quantity, not a raw fact, and the model must carry instrument, sampling and disclosure alongside every published number to keep the measurement honest and comparable.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:d8"
  csn: world.publicDiscourse
  version: 0.2.0
  displayName: Public Discourse & Opinion
  description: Discourse topics and arenas, opinion polling with open methodology, published measures and information campaigns.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.publicDiscourse
bundles:
  - csn: world.publicDiscourse.topic
    displayName: Topic
    layers:
      - world.publicDiscourse.topic.discourseTopic
      - world.publicDiscourse.topic.arena
  - csn: world.publicDiscourse.measurement
    displayName: Measurement
    layers:
      - world.publicDiscourse.measurement.pollDesign
      - world.publicDiscourse.measurement.fieldwork
      - world.publicDiscourse.measurement.opinionMeasure
  - csn: world.publicDiscourse.campaign
    displayName: Campaign
    layers:
      - world.publicDiscourse.campaign.campaignProfile
      - world.publicDiscourse.campaign.messageTrace
imports:
  - source: aapor-practice
    version: "*"
  - source: ddi
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `topic` | What is being discussed and where | `discourseTopic`: topics, framings and agendas over time · `arena`: media arenas and channels where discourse circulates |
| `measurement` | How opinion is measured and published | `pollDesign`: instruments, sampling frames, declared methodology · `fieldwork`: collection waves and response aggregates · `opinionMeasure`: published measures and their time series |
| `campaign` | Organized attempts to shape discourse | `campaignProfile`: information campaigns, sponsors and declared aims · `messageTrace`: message variants and their distribution traces |

## Objects

- `discourseTopic`: a subject of public discussion; key attributes: name, framing variants, lifecycle stage, related claims
- `arena`: a channel or venue of discourse; key attributes: type, reach class, operator reference
- `poll`: a designed opinion measurement exercise; key attributes: conductor reference, instrument, frame, waves, disclosure status
- `samplingFrame`: the population definition a poll draws from; key attributes: cohort reference, coverage, exclusions
- `questionInstrument`: the questions as fielded; key attributes: wording, order, scales, language versions
- `opinionMeasure`: a published measured quantity; key attributes: topic, value, margin, wave, method summary
- `campaign`: an organized information campaign; key attributes: sponsor reference, aims, period, budget class
- `message`: a campaign message variant; key attributes: content summary, format, arenas used, reach estimate

## Relationships

- `poll` -> measures -> `discourseTopic` (n..m): polls attach to the topics they quantify
- `poll` -> fieldedWith -> `questionInstrument` (1..n): the instrument as fielded is part of the poll's identity
- `poll` -> drawsFrom -> `samplingFrame` (n..1): every poll declares its frame
- `opinionMeasure` -> derivedFrom -> `poll` (n..1): no measure exists without its producing poll
- `campaign` -> targets -> `discourseTopic` (n..m): campaigns aim at topics and framings
- `message` -> belongsTo -> `campaign` (n..1): messages are variants within a campaign
- `poll` -> conductedBy -> `organization` (n..1): the polling organization is an O1 entity accountable for methodology
- `opinionMeasure` -> concerns -> `claim` (n..m): measures tie to claims in the document and record model (N1), separating what people think from what is established

## Events

- `topicEmerged`: a topic entered measurable public discussion
- `pollFielded`: fieldwork for a poll began
- `waveClosed`: a collection wave completed and its aggregates were fixed
- `measurePublished`: an opinion measure was released with its method summary
- `methodologyDisclosed`: full methodology for a poll was made open
- `campaignLaunched`: an information campaign began distribution
- `campaignConcluded`: a campaign ended and its reach record was closed

## Contracts

- `methodologyDisclosure`: the standing obligation of polling organizations to keep design, frame and instrument open for every published measure
- `microdataResearchAccess`: de-identified respondent-level data released to researchers under contract, never publicly
- `measureSyndication`: redistribution of published measures with mandatory method summary attached

## Projections

- `publishedMeasureBoard`: topline measures with margins and method summaries; omits all respondent microdata
- `campaignTransparencyRegister`: campaigns with sponsor, period, budget class and reach; omits targeting internals and creative work product
- `topicTimeline`: topic lifecycles with attached measures and campaigns; omits fieldwork operations

## Composition

- REFERENCE `world.organization` (O1): polling organizations, arena operators and campaign sponsors are organizations
- REFERENCE `world.populationGroup` (H3): sampling frames and reported breakdowns are defined over statistical cohorts, never over identifiable members
- REFERENCE `world.documentAndRecord` (N1): opinion measures link to the claims they concern, keeping measured belief distinct from evidenced knowledge
- REFERENCE `world.socialNorm` (D9): discourse about norms and customs cross-links to their descriptive records
- imports: AAPOR practice (ALIGN): disclosure elements and transparency practice for every published measure
- imports: DDI (ALIGN): instrument, dataset and wave description for polls and their archives

## Stewardship

Polling organizations steward polls and measures under an open-methodology obligation; campaign records are stewarded by a neutral transparency registrar. Respondent-level data never leaves the protected layer except under research contract, and all access is granted by the respective owner through the catalogue's S1/S2 models with audit via S4.
