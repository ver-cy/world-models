# A13 Election & Electoral Process

This meta-model describes how a polity chooses its officeholders: the franchise and voter rolls, candidacies and campaign finance, ballot design and casting channels, and the counting that turns ballots into declared results and mandate grants. It is its own model because an election is a time-boxed, high-integrity process with secrecy constraints found nowhere else in the catalogue: cast ballots must aggregate into tallies without ever becoming linkable back to voters, while every counting step must still be auditable.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a13"
  csn: world.election
  version: 0.2.0
  displayName: Election & Electoral Process
  description: Franchise, candidacies, ballots, counts and mandate grants of an electoral process.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.election
bundles:
  - csn: world.election.franchise
    displayName: Franchise
    layers:
      - world.election.franchise.voterRoll
      - world.election.franchise.eligibility
  - csn: world.election.campaign
    displayName: Campaign
    layers:
      - world.election.campaign.nomination
      - world.election.campaign.campaignFinance
  - csn: world.election.ballot
    displayName: Ballot
    layers:
      - world.election.ballot.ballotDesign
      - world.election.ballot.castingChannel
  - csn: world.election.count
    displayName: Count
    layers:
      - world.election.count.tally
      - world.election.count.resultAndMandate
imports:
  - source: oasis-eml
    version: "*"
  - source: popolo
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `franchise` | Who may vote and who may stand | `voterRoll`: registration of eligible voters per roll · `eligibility`: qualification and disqualification rules |
| `campaign` | The contest before voting day | `nomination`: candidacies and their validation · `campaignFinance`: declared funding and spending |
| `ballot` | The act of voting | `ballotDesign`: questions, lists, candidate ordering · `castingChannel`: polling place, postal, assisted and other channels |
| `count` | From ballots to mandates | `tally`: counting, recounts, invalid ballots · `resultAndMandate`: declared results and mandate grants |

## Objects

- `election`: one called electoral event; key attributes: electionType, calledOn, pollingDates, legalBasisRef
- `constituency`: a territorial or corporate unit returning seats; key attributes: name, magnitude, boundaryRef
- `voterRegistration`: one person's entry on a voter roll; key attributes: personRef, rollRef, status, basis
- `candidacy`: a validated bid for a mandate; key attributes: candidateRef, nominatorRef, listPosition, status
- `ballot`: the designed ballot instrument, not a marked paper; key attributes: constituencyRef, contests, layout, languageSet
- `tally`: the counted totals for one ballot in one constituency; key attributes: countsPerOption, invalidCount, turnout, recountFlag
- `result`: the legally declared outcome; key attributes: constituencyRef, allocation, declaredOn, challengeWindow
- `mandateGrant`: the award that seats a winner into an office; key attributes: candidacyRef, officeRef, term, certifiedOn

## Relationships

- `election` -> contestedIn -> `constituency` (1:N): an election is decided constituency by constituency
- `voterRegistration` -> enfranchises -> `personRef` (N:1): a roll entry resolves to a person in P1, one active entry per roll
- `candidacy` -> contests -> `election` (N:1): each candidacy belongs to one election
- `tally` -> counts -> `ballot` (N:1): totals are produced per ballot design per constituency
- `result` -> declaredFrom -> `tally` (1:N): a declared result consolidates one or more tallies, including recounts
- `mandateGrant` -> awardedTo -> `candidacy` (1:1): each seat awarded traces to exactly one winning candidacy
- `mandateGrant` -> seats -> `officeRef` (N:1): the grant fills an office defined in A11

## Events

- `electionCalled`: an election was formally called with its dates and legal basis
- `candidacyValidated`: a nomination was checked and admitted to the ballot
- `votingOpened`: casting began through the authorized channels
- `votingClosed`: casting ended and counting became permissible
- `tallyCompleted`: a count for one ballot and constituency was finalized
- `recountOrdered`: a tally was reopened under the correction procedure
- `resultDeclared`: the outcome of a constituency was legally declared
- `mandateGranted`: a winner was certified and the corresponding office seat filled

## Contracts

- `openResults`: public access to declared results, tallies and turnout, permanently retained
- `accreditedObserverAccess`: process access for accredited observers to counting and casting-channel records
- `voterRollExtract`: restricted, purpose-bound extracts of the roll, granted by the electoral registrar under the access regime

## Projections

- `resultsBoard`: declared results and allocations per constituency; omits roll data and individual ballots, which are never stored linkably
- `turnoutStatistics`: participation aggregates by area and channel; omits all person-level data
- `mandateLedger`: who received which mandate for which office and term; omits count detail

## Composition

- REFERENCE `world.person` (P1): voters and candidates resolve to persons
- REFERENCE `world.publicOffice` (A11): mandate grants seat elected offices defined there
- REFERENCE `world.publicOffice` (A11): the bodies whose composition the election determines
- REFERENCE `world.registryMandate` (A12): the electoral register operates under its own independent mandate
- MIX-IN `world.auditTrail` (S4): every roll change and count step is append-only and independently checkable
- imports: oasis-eml (ALIGN): election process and results interchange structure
- imports: popolo (ALIGN): candidacies, posts and memberships for civic data consumers

## Stewardship

An independent electoral registrar, holding its own A12 mandate, stewards this model. Results and statistics are public; voter rolls and channel records are graded, and any access beyond a person's view of their own registration is granted only by the registrar via S1 and S2.