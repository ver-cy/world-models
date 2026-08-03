# O6 Labor Market & Vacancy

This meta-model describes the meeting of labor demand and supply: vacancies posted by organizations, applications and dossiers submitted by persons, the matching and screening between them, and the offers and placements that conclude the process. It is its own model because the market interaction precedes and is distinct from the employment relation it may produce, and because the two sides own their data separately until they meet.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:o6"
  csn: world.laborMarket
  version: 0.2.0
  displayName: "Labor Market & Vacancy"
  description: "Vacancies, applications, matching, offers and placements between organizations and persons."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.laborMarket
bundles:
  - csn: world.laborMarket.vacancy
    displayName: "Vacancy"
    layers:
      - world.laborMarket.vacancy.posting
      - world.laborMarket.vacancy.requirements
  - csn: world.laborMarket.candidacy
    displayName: "Candidacy"
    layers:
      - world.laborMarket.candidacy.application
      - world.laborMarket.candidacy.screening
  - csn: world.laborMarket.matching
    displayName: "Matching"
    layers:
      - world.laborMarket.matching.proposal
      - world.laborMarket.matching.offer
  - csn: world.laborMarket.placement
    displayName: "Placement"
    layers:
      - world.laborMarket.placement.outcome
imports:
  - source: esco
    version: "*"
  - source: hr-open
    version: "*"
  - source: schema-org
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `vacancy` | The demand side | `posting`: the announcement, channels and validity Â· `requirements`: skills, qualifications and conditions offered |
| `candidacy` | The supply side | `application`: submissions and attached dossiers Â· `screening`: assessments and shortlists |
| `matching` | Bringing the sides together | `proposal`: mediated or computed matches Â· `offer`: offers and their responses |
| `placement` | The conclusion | `outcome`: confirmed placements, starts and early outcomes |

## Objects

- `vacancy`: an open position announced to the market; key attributes: title, posting organization reference, validity window, status.
- `requirementProfile`: what the vacancy asks for; key attributes: occupation code, skill codes, qualifications, conditions offered.
- `application`: a candidate's response to a vacancy; key attributes: submission date, status, withdrawal flag.
- `candidateDossier`: the candidate-owned dossier attached to applications; key attributes: experience summary, skill codes, availability, disclosure scope.
- `screeningResult`: an assessment during selection; key attributes: stage, outcome, assessed date.
- `matchProposal`: a suggested pairing of vacancy and candidate; key attributes: proposer kind (intermediary, algorithmic service), score or rationale, status.
- `offer`: a concrete offer to a candidate; key attributes: role offered, conditions summary, response deadline, response.
- `placement`: the confirmed conclusion; key attributes: start date, probation terms, early outcome.

## Relationships

- `vacancy` -> postedBy -> `world.organization` (n:1): the demand side resolves to an organization (O1).
- `requirementProfile` -> specifies -> `vacancy` (1:1): the requirements of one posting.
- `application` -> respondsTo -> `vacancy` (n:1): a candidacy aimed at one posting.
- `application` -> submittedBy -> `world.person` (n:1): the supply side resolves to a person (H1).
- `matchProposal` -> pairs -> `vacancy` (n:m): proposals connect vacancies with candidate dossiers.
- `offer` -> extends -> `application` (1:1): the offer that grew out of a candidacy or match.
- `placement` -> concludes -> `offer` (1:1): the accepted offer that became a placement.
- `placement` -> initiates -> `world.employment` (1:1): the employment relation (O3) the placement composes.

## Events

- `vacancyPosted`: a vacancy was announced to the market.
- `vacancyClosed`: a vacancy was filled, withdrawn or expired.
- `applicationSubmitted`: a candidate applied.
- `applicationWithdrawn`: a candidate withdrew.
- `candidateShortlisted`: screening advanced a candidate.
- `offerExtended`: an offer was made.
- `offerAccepted`: the candidate accepted; a declined offer is recorded on the same object.
- `placementConfirmed`: the placement was confirmed and a start date fixed.

## Contracts

- `postingSyndication`: boards and aggregators republish open vacancies under source attribution terms.
- `candidateConsent`: per-process consent for a posting organization or intermediary to read a candidate dossier.
- `placementStatistics`: aggregate anonymized matching and placement reporting for market observers.

## Projections

- `jobBoard`: open vacancies with requirements; omits applications and screening.
- `recruiterPipeline`: the organization's funnel from application to placement; omits candidates' activity elsewhere.
- `candidateJourney`: the person's own applications, matches and offers; omits internal screening notes unless disclosed.

## Composition

- REFERENCE `world.organization` (O1): posting organizations and intermediaries.
- REFERENCE `world.person` (H1): candidates as self-owned subjects.
- REFERENCE `world.organizationalUnit` (O2): vacancies may target established positions.
- COMPOSE `world.employment` (O3): a confirmed placement composes the initial employment record there.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): side-specific ownership and consent-based access.
- MIX-IN `world.auditTrail` (S4): audit facets on posting, screening and placement events.
- imports: esco (REFERENCE): occupation and skill codes in requirements and dossiers.
- imports: hr-open (ALIGN): recruiting interchange shapes for applications and offers.
- imports: schema-org (ALIGN): public job posting vocabulary for syndicated vacancies.

## Stewardship

The posting organization owns the vacancy side; the person owns the candidate side; applications, matches and offers are bilateral records. Access on each side is granted by its owner under the S1/S2 models of this catalogue.
