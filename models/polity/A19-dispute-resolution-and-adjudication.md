# A19 Dispute Resolution & Adjudication

This meta-model describes how disagreements become decided cases: the disputes parties raise against each other, the forums (courts, tribunals, arbitration and mediation bodies) empowered to hear them, the proceedings through which claims are argued and evidence is weighed, and the decisions and remedies that close them. It is its own model because adjudication must stay independent of the models it judges: enforcement (A18) refers cases into it, contracts (O5) escalate into it, and registries record its outcomes, but the deciding forum, its procedure and its record belong here.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a19"
  csn: world.disputeResolution
  version: 0.2.0
  displayName: Dispute Resolution & Adjudication
  description: Disputes, deciding forums, proceedings, decisions and remedies.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.disputeResolution
bundles:
  - csn: world.disputeResolution.dispute
    displayName: Dispute
    layers:
      - world.disputeResolution.dispute.claimAndParties
      - world.disputeResolution.dispute.forumAssignment
  - csn: world.disputeResolution.proceeding
    displayName: Proceeding
    layers:
      - world.disputeResolution.proceeding.processSteps
      - world.disputeResolution.proceeding.evidenceRecord
  - csn: world.disputeResolution.decision
    displayName: Decision
    layers:
      - world.disputeResolution.decision.rulingAndRemedy
      - world.disputeResolution.decision.reviewAndAppeal
imports:
  - source: akoma-ntoso
    version: "*"
  - source: eli
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `dispute` | What is contested and where it will be heard | `claimAndParties`: claims, counterclaims and the parties raising them · `forumAssignment`: jurisdiction, competence and assignment to a forum |
| `proceeding` | How the case is argued | `processSteps`: filings, hearings, motions and their sequence · `evidenceRecord`: submitted evidence, its admission and custody references |
| `decision` | How the case is closed and challenged | `rulingAndRemedy`: decisions, reasons and ordered remedies · `reviewAndAppeal`: appeals, reviews and their outcomes |

## Objects

- `dispute`: a contested matter between parties; key attributes: subject reference, dispute kind, claims summary, status
- `party`: a participant in the dispute; key attributes: agent reference, procedural role (claimant, respondent, intervener), representation
- `forum`: a body empowered to decide; key attributes: name, kind (court, tribunal, arbitration, mediation), competence scope, independence basis
- `proceeding`: the managed course of one case before a forum; key attributes: case identifier, forum reference, stage, schedule
- `filing`: a procedural submission; key attributes: submitting party, kind (claim, defense, motion), date, document reference
- `evidenceItem`: material admitted for weighing; key attributes: source reference, admission status, custody reference
- `decision`: the forum's ruling; key attributes: outcome, reasons reference, deciding composition, date, finality state
- `remedy`: what the decision orders; key attributes: kind (performance, compensation, annulment, injunction), addressee, terms, compliance state

## Relationships

- `dispute` -> raisedBy -> `party` (1..n): every dispute names the parties contesting it
- `dispute` -> assignedTo -> `forum` (n..1): competence rules route each dispute to one deciding forum at a time
- `proceeding` -> hears -> `dispute` (1..1): a proceeding is the forum's handling of one dispute
- `filing` -> advances -> `proceeding` (n..1): submissions move the case through its stages
- `evidenceItem` -> weighedIn -> `proceeding` (n..1): admitted evidence belongs to the case record
- `decision` -> closes -> `proceeding` (n..1): a proceeding ends in one or more decisions
- `remedy` -> orderedBy -> `decision` (n..1): remedies exist only as orders of a decision
- `decision` -> reviewedBy -> `proceeding` (0..n): appeals open new proceedings over a prior decision

## Events

- `disputeRaised`: a party formally raised a contested matter
- `forumAssigned`: jurisdiction was resolved and the case routed to a forum
- `proceedingOpened`: the forum opened the case
- `hearingHeld`: a hearing took place
- `evidenceAdmitted`: an item of evidence was admitted to the record
- `decisionIssued`: the forum ruled, with reasons
- `appealLodged`: a party challenged a decision within the allowed window
- `remedyDischarged`: an ordered remedy was performed or enforced

## Contracts

- `partyAccess`: each party's right to the case record concerning them, including evidence they must be able to answer
- `arbitrationAgreement`: the parties' agreement to submit a class of disputes to a named private forum
- `publicationPolicy`: what of a decision is published, with party data redacted per the forum's rules

## Projections

- `publicDecisionView`: published decisions and reasons; omits or pseudonymizes party identities per policy
- `partyCaseView`: a party's complete view of their own case: filings, evidence, schedule, decisions
- `caseloadStatistics`: aggregate counts, durations and outcome distributions per forum; contains no case identities

## Composition

- REFERENCE `world.person` (H1) and `world.organization` (O1): parties, representatives and deciding members resolve to persons and organizations
- REFERENCE `world.offenseEnforcement` (A18): enforcement refers charged cases into adjudication and consumes its decisions
- REFERENCE `world.commercialContract` (O5): contract disputes escalate here under their dispute clauses
- REFERENCE `world.documentAndRecord` (N1): filings, reasons and decisions are governed documents
- REFERENCE `world.eventRegister` (R3): case events are recorded append-only on the timeline register
- imports: Akoma Ntoso (ALIGN): structured markup for judgments and procedural documents
- imports: ELI (ALIGN): identifiers for published decisions as legal resources

## Stewardship

Each forum owns its case records and decides publication under its policy; parties own their side of the record and hold access to everything they must answer. Access beyond the parties and the forum is granted only by the respective owner through S1/S2, with audit via S4.
