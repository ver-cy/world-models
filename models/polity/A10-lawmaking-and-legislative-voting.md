# A10 Lawmaking & Legislative Voting

This meta-model describes how a polity turns proposals into binding law: bills and their evolving texts, the amendments moved against them, the readings and committee stages they pass through, the votes that members cast on questions put, and the final acts of promulgation and commencement. It is its own model because the legislative record has a distinct document lifecycle and public-faith requirement, separate from the bodies that legislate (A11), the offices whose holders vote (A11), and the registers that later cite enacted law.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a10"
  csn: world.lawmaking
  version: 0.2.0
  displayName: Lawmaking & Legislative Voting
  description: Bills, readings, amendments, recorded votes and enactment of law in a polity.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.lawmaking
bundles:
  - csn: world.lawmaking.drafting
    displayName: Drafting
    layers:
      - world.lawmaking.drafting.billText
      - world.lawmaking.drafting.amendment
  - csn: world.lawmaking.deliberation
    displayName: Deliberation
    layers:
      - world.lawmaking.deliberation.readingStage
      - world.lawmaking.deliberation.committeeScrutiny
  - csn: world.lawmaking.voting
    displayName: Voting
    layers:
      - world.lawmaking.voting.rollCall
      - world.lawmaking.voting.tally
  - csn: world.lawmaking.enactment
    displayName: Enactment
    layers:
      - world.lawmaking.enactment.promulgation
      - world.lawmaking.enactment.commencement
imports:
  - source: akoma-ntoso
    version: "*"
  - source: popolo
    version: "*"
  - source: eli
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `drafting` | Bill texts and their evolution as documents | `billText`: authoritative versions of a bill Â· `amendment`: proposed changes and their disposition |
| `deliberation` | Movement of a bill through formal stages | `readingStage`: plenary readings and outcomes Â· `committeeScrutiny`: referral, hearings, committee reports |
| `voting` | Recorded decisions of members on questions put | `rollCall`: individual member positions Â· `tally`: aggregate counts, quorum and outcome |
| `enactment` | The passage from passed bill to law in force | `promulgation`: signature and official publication Â· `commencement`: entry-into-force rules and dates |

## Objects

- `bill`: a proposal for new or changed law; key attributes: billNumber, title, legislatureRef, introducedOn, status
- `billVersion`: a point-in-time authoritative text of a bill; key attributes: versionNo, text, supersedes, consolidationBasis
- `amendment`: a proposed change to a bill version; key attributes: moverRef, targetClause, proposedText, disposition
- `reading`: a formal stage of consideration; key attributes: stageType, chamberRef, heldOn, outcome
- `voteEvent`: a question put to a vote; key attributes: question, votingMethod, quorumRequired, outcome
- `castVote`: one member's recorded position in a vote event; key attributes: voterRef, position, proxyFlag
- `sponsorship`: the link of a member or body promoting a bill; key attributes: sponsorRef, role, since
- `enactment`: the act that makes a passed text law; key attributes: actIdentifier, signedByRef, promulgatedOn, commencementRule

## Relationships

- `billVersion` -> versionOf -> `bill` (N:1): each authoritative text belongs to exactly one bill
- `amendment` -> modifies -> `billVersion` (N:1): an amendment targets one specific text version
- `reading` -> considers -> `bill` (N:1): a stage advances or halts one bill
- `voteEvent` -> decides -> `reading` (1:1, optional): a reading may conclude with a formal vote
- `castVote` -> castIn -> `voteEvent` (N:1): individual positions aggregate into the tally of one vote event
- `castVote` -> castBy -> `officeholderRef` (N:1): the voter resolves to a seated officeholder in A11
- `enactment` -> enacts -> `billVersion` (1:1): promulgation freezes one final text as law

## Events

- `billIntroduced`: a bill was formally introduced into a chamber
- `readingHeld`: a reading or committee stage took place and produced an outcome
- `amendmentDisposed`: an amendment was adopted, rejected or withdrawn
- `voteRecorded`: a vote event closed and its roll call and tally became final
- `billPassed`: a bill completed all required stages in the legislature
- `billWithdrawn`: a bill was withdrawn or lapsed before passage
- `actPromulgated`: a passed text was signed and officially published
- `actCommenced`: an enacted text entered into force

## Contracts

- `openLegislativeRecord`: public read access to bills, readings, roll calls and enacted texts
- `bulkLegislativeExport`: machine-readable bulk feed of the record for publishers and researchers
- `preIntroductionDraftAccess`: restricted access to drafts before formal introduction, granted case by case by the legislature

## Projections

- `statuteBook`: enacted, in-force texts with their ELI identifiers; omits failed bills, drafts and vote detail
- `memberVotingLedger`: roll-call positions per member across vote events; omits bill text history
- `billTracker`: current stage and next step of every pending bill; omits full texts and individual votes

## Composition

- REFERENCE `world.publicOffice` (A11): chambers and committees that hold readings are branch bodies governed there
- REFERENCE `world.publicOffice` (A11): voters and sponsors resolve to seated officeholders; seats come from mandate grants
- REFERENCE `world.registryMandate` (A12): the legislative record is itself a mandated public register with a public-faith rule
- MIX-IN `world.auditTrail` (S4): tamper-evident, append-only history for every stage, amendment and recorded vote
- imports: akoma-ntoso (ALIGN): document structure for bill and act texts
- imports: popolo (ALIGN): interchange vocabulary for vote events, memberships and motions
- imports: eli (REFERENCE): durable identifier scheme for enacted legislation

## Stewardship

The legislature (a branch body of A2), acting through its clerk or secretariat as registrar, stewards this record. It is public by default under its A12 mandate; drafts and any embargoed layer are opened only by owner grant through the catalogue's S1 ownership and S2 access models.