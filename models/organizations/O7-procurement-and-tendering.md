# O7 Procurement & Tendering

This meta-model describes how organizations buy through competition: tenders and their lots, clarifications, sealed bids, evaluation against published criteria, awards and their challenges, and the securities that back performance. It covers both private tendering and public procurement with its added transparency duties. It is its own model because the competitive process has strict sequencing and confidentiality rules that no general agreement model provides, and it ends where the contract model begins.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:o7"
  csn: world.procurement
  version: 0.2.0
  displayName: "Procurement & Tendering"
  description: "Tenders, clarifications, sealed bids, evaluation, awards, challenges and performance securities."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.procurement
bundles:
  - csn: world.procurement.solicitation
    displayName: "Solicitation"
    layers:
      - world.procurement.solicitation.notice
      - world.procurement.solicitation.clarification
  - csn: world.procurement.bidding
    displayName: "Bidding"
    layers:
      - world.procurement.bidding.submission
      - world.procurement.bidding.evaluation
  - csn: world.procurement.award
    displayName: "Award"
    layers:
      - world.procurement.award.decision
      - world.procurement.award.challenge
  - csn: world.procurement.assurance
    displayName: "Assurance"
    layers:
      - world.procurement.assurance.security
imports:
  - source: ocds
    version: "*"
  - source: uncitral
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `solicitation` | Announcing the competition | `notice`: tender publication, lots and criteria Â· `clarification`: questions, answers and addenda |
| `bidding` | Competing | `submission`: sealed bids and attachments Â· `evaluation`: compliance checks and scoring |
| `award` | Deciding | `decision`: award, standstill and notification Â· `challenge`: protests and their outcomes |
| `assurance` | Securing performance | `security`: bid and performance bonds and guarantees |

## Objects

- `tender`: the competition as a whole; key attributes: procedure kind, publication date, deadlines, public flag, status.
- `lot`: a separately awardable part of a tender; key attributes: scope, estimated size, award status.
- `evaluationCriterion`: a published basis of judgment; key attributes: criterion kind (price, quality), weight, scoring rule.
- `clarification`: a question, answer or addendum; key attributes: question hash, answer text, issue date, tender effect.
- `bid`: a sealed competitive submission; key attributes: bidder reference, submission time, seal state, validity period.
- `evaluationRecord`: the assessment of bids; key attributes: criterion scores, compliance findings, evaluator references.
- `award`: the decision; key attributes: winning bid reference, decision date, standstill window, status.
- `performanceBond`: a security backing performance; key attributes: kind, amount, issuer reference, validity.

## Relationships

- `tender` -> issuedBy -> `world.organization` (n:1): the procuring organization (O1).
- `tender` -> dividedInto -> `lot` (1:n): separately awardable parts.
- `bid` -> respondsTo -> `lot` (n:1): each bid targets a lot, or the whole tender when undivided.
- `bid` -> submittedBy -> `world.organization` (n:1): the bidder, an organization (O1) or a person (H1) where individuals may bid.
- `evaluationRecord` -> scores -> `bid` (n:m): assessments of bids against the published criteria.
- `award` -> selects -> `bid` (1:1): the winning submission.
- `award` -> concludesIn -> `world.commercialContract` (1:1): the agreement (O5) the award composes.
- `performanceBond` -> secures -> `award` (n:1): the security behind an award.

## Events

- `tenderPublished`: the competition was announced with criteria and deadlines.
- `clarificationIssued`: a question was answered or an addendum published to all bidders.
- `bidSubmitted`: a sealed bid entered custody.
- `bidsOpened`: seals were broken after the deadline, in the recorded order.
- `evaluationCompleted`: scoring and compliance findings were finalized.
- `awardAnnounced`: the decision was notified and the standstill window opened.
- `awardChallenged`: a protest was lodged against the decision.
- `bondPosted`: a bid or performance security was put in place.

## Contracts

- `sealedBidCustody`: bids are held unreadable by everyone, including the procurer, until the opening event.
- `publicNoticeFeed`: open publication of notices, criteria and awards for public tenders.
- `bidderWorkroomAccess`: each bidder reads the tender file and its own bid only.
- `auditorAccess`: full-file access for auditors and challenge forums.

## Projections

- `openContractingView`: notices, criteria, awards and winning values for public tenders; omits losing bids' commercial content.
- `bidderView`: the tender file, own bid and own scores after debrief; omits competitors' bids.
- `evaluationMinute`: the complete internal evaluation record; omits nothing, access tightly restricted.

## Composition

- REFERENCE `world.organization` (O1): procurers and bidders; individual bidders via `world.person` (H1).
- COMPOSE `world.commercialContract` (O5): the award concludes in an agreement modelled there.
- REFERENCE `world.priceValuation` (C7): estimates and benchmark prices inform criteria and evaluation.
- REFERENCE `world.publicRegister` (A12): public tenders are registered and their notices published there.
- REFERENCE `world.disputeResolution` (A19): challenges are heard there.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): ownership and access grants over the tender file and bids.
- MIX-IN `world.auditTrail` (S4): audit facets on submission, opening, evaluation and award events.
- imports: ocds (ALIGN): open contracting data model for the public view of tenders and awards.
- imports: uncitral (ALIGN): procurement law vocabulary for procedures and standstill.

## Stewardship

The procuring organization owns the tender file; each bidder owns its bid until opening under the sealed custody contract; public tenders additionally carry registration and publication duties via the public register. Access is granted by the respective owners under the S1/S2 models of this catalogue.
