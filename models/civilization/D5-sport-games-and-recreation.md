# D5 Sport Games & Recreation

This meta-model describes the world of organized sport and informal recreation: the disciplines people play and the rules that codify them, the leagues and competitions that structure play into seasons, fixtures, results and records, and the participation of teams, athletes and casual players. It is its own model because competitive sport has a distinctive lifecycle (sanctioning, seasons, fixtures, results, standings, records) that no generic event or organization model captures, while recreation adds a non-competitive participation dimension of its own.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:d5"
  csn: world.sportRecreation
  version: 0.2.0
  displayName: Sport Games & Recreation
  description: Sports and disciplines, leagues and competitions, results and records, teams and recreational activity.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.sportRecreation
bundles:
  - csn: world.sportRecreation.discipline
    displayName: Discipline
    layers:
      - world.sportRecreation.discipline.sportTaxonomy
      - world.sportRecreation.discipline.ruleset
  - csn: world.sportRecreation.competition
    displayName: Competition
    layers:
      - world.sportRecreation.competition.league
      - world.sportRecreation.competition.fixture
      - world.sportRecreation.competition.result
  - csn: world.sportRecreation.participation
    displayName: Participation
    layers:
      - world.sportRecreation.participation.athleteAndTeam
      - world.sportRecreation.participation.recreationalActivity
imports:
  - source: sportsml
    version: "*"
  - source: schema-org
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `discipline` | What sports exist and how play is codified | `sportTaxonomy`: sports, disciplines and their family tree Â· `ruleset`: codified rules of play, formats, scoring systems |
| `competition` | Organized competitive play and its outcomes | `league`: leagues, divisions, seasons and sanctioning Â· `fixture`: scheduled competitions, matches and staging Â· `result`: results, standings, records and rankings |
| `participation` | Who plays, competitively or for leisure | `athleteAndTeam`: teams, rosters and competitor roles Â· `recreationalActivity`: casual, amateur and club-level activity |

## Objects

- `sport`: a recognized sport or discipline; key attributes: name, family, discipline codes, governing federation reference
- `ruleset`: a codified body of rules for a sport; key attributes: version, format, scoring system, sanctioning body reference
- `league`: a standing competitive structure; key attributes: name, sport, tier, divisions, organizer reference
- `season`: a bounded competitive cycle of a league; key attributes: start, end, format, promotion and relegation rules
- `competition`: a sanctioned competitive event, from a tournament down to a single race; key attributes: type, stage structure, sanctioning status
- `fixture`: a scheduled contest between competitors; key attributes: date, venue reference, competitors, officials
- `result`: the recorded outcome of a fixture or competition; key attributes: score, placements, records touched, verification status
- `team`: a competing collective with a roster; key attributes: name, club or organization reference, roster window
- `recreationalActivity`: a non-competitive practiced activity; key attributes: activity type, setting, regularity, facility reference

## Relationships

- `sport` -> codifiedBy -> `ruleset` (1..n): each sport is governed by one or more versioned rulesets
- `league` -> runsSeason -> `season` (1..n): a league is realized as a sequence of seasons
- `competition` -> partOf -> `season` (n..1): competitions and rounds sit inside a season's calendar
- `fixture` -> producedResult -> `result` (1..0..1): a played fixture yields at most one verified result
- `team` -> competedIn -> `fixture` (n..m): teams and individual competitors meet in fixtures
- `team` -> rosters -> `person` (n..m): roster slots resolve to natural persons in H1; only the role linkage lives here
- `fixture` -> stagedAt -> `facility` (n..1): staging resolves to a sports facility governed by the built-environment model (U)
- `recreationalActivity` -> practicedBy -> `person` (n..m): leisure participation, held at the participant's discretion

## Events

- `competitionSanctioned`: an organizing body approved a competition under a ruleset
- `seasonOpened`: a league season began and its fixture calendar became binding
- `fixturePlayed`: a scheduled contest took place
- `resultRecorded`: an outcome was verified and entered into standings
- `recordSet`: a performance surpassed a recognized record for the discipline
- `teamRegistered`: a team entered a league or competition with a declared roster
- `seasonClosed`: final standings were fixed and promotions or relegations applied

## Contracts

- `resultsFeedContract`: licensed distribution of live and final results to media and data consumers
- `historicalStatisticsAccess`: research and almanac access to standings, records and season archives
- `fixtureSyndication`: redistribution of fixture calendars with staging and ticketing pointers

## Projections

- `publicStandingsBoard`: current standings and results per league; omits roster personal data and officials' details
- `fixtureCalendar`: upcoming fixtures with venues; omits results processing and verification state
- `sportAlmanac`: historical records and season archives; omits in-progress seasons and unverified results

## Composition

- REFERENCE `world.organization` (O1): federations, leagues, clubs and organizing bodies are organizations; this model holds only their sporting roles
- REFERENCE `world.person` (H1): athletes, officials and recreational participants resolve to natural persons; no personal attributes are copied
- REFERENCE `world.buildingAndFacility` (U): stadiums, halls and grounds are facilities of the built environment; fixtures hold facility references only
- REFERENCE `world.tourismHospitality` (D7): major competitions appear as visitor experiences in the tourism model
- imports: SportsML (ALIGN): event, fixture and result vocabulary for sports data exchange
- imports: schema.org (ALIGN): SportsEvent, SportsTeam and SportsActivityLocation typing for public projections

## Stewardship

Organizing bodies (federations, leagues, clubs) steward the layers they sanction: rulesets, seasons, fixtures and verified results. Roster and participation data concerning a person is disclosed only under that person's grant, with access always issued by the respective owner through the catalogue's S1/S2 ownership and access models and audited via S4.
