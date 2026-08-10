# A14 Permit License & Authorization

This meta-model describes the application-to-grant process for regulated activity: submissions and the evidence offered with them, review against criteria, the decision to grant or refuse, and the lifecycle of conditions, renewals and revocations that follows a grant. The granted right itself is recorded in the rights register (R5); this model owns the process around it. It is its own model because permitting is a repeatable administrative procedure whose shape (criterion, evidence, decision, condition) is identical across domains that otherwise share nothing.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a14"
  csn: world.authorization
  version: 0.2.0
  displayName: Permit License & Authorization
  description: Application-to-grant processes for regulated activity, from submission to revocation.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.authorization
bundles:
  - csn: world.authorization.application
    displayName: Application
    layers:
      - world.authorization.application.submission
      - world.authorization.application.evidence
  - csn: world.authorization.review
    displayName: Review
    layers:
      - world.authorization.review.assessment
      - world.authorization.review.decision
  - csn: world.authorization.grantLifecycle
    displayName: Grant lifecycle
    layers:
      - world.authorization.grantLifecycle.condition
      - world.authorization.grantLifecycle.monitoring
      - world.authorization.grantLifecycle.revocation
imports:
  - source: cpsv
    version: "*"
  - source: cccev
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `application` | What the applicant brings | `submission`: applications, applicants, requested scope · `evidence`: documents and facts offered against criteria |
| `review` | How the authority decides | `assessment`: evaluation of criteria and consultations · `decision`: grant, refusal and stated reasons |
| `grantLifecycle` | What happens after grant | `condition`: obligations attached to a grant · `monitoring`: compliance checks and renewals · `revocation`: suspension and withdrawal |

## Objects

- `application`: a request to be authorized for a regulated activity; key attributes: applicantRef, activityType, requestedScope, submittedOn, status
- `evidenceItem`: a document or fact offered to satisfy a criterion; key attributes: criterionRef, sourceRef, validity, verifiedFlag
- `criterion`: a requirement the applicant must meet; key attributes: description, legalBasisRef, evidenceTypesAccepted
- `reviewStep`: one assessment or consultation act in the review; key attributes: reviewerRef, criterionSet, finding, completedOn
- `decision`: the concluding act on an application; key attributes: outcome, reasons, deciderRef, decidedOn, appealPath
- `grantReference`: the pointer to the issued right recorded in R5; key attributes: rightRef, scope, validity
- `condition`: an obligation attached to a grant; key attributes: text, monitoringRule, breachConsequence
- `revocation`: the suspension or withdrawal of a grant; key attributes: grantRef, ground, effectiveOn, appealPath

## Relationships

- `application` -> submittedBy -> `partyRef` (N:1): the applicant resolves to a person in P1 or an organization in O1
- `evidenceItem` -> supports -> `application` (N:1): evidence is filed against one application
- `reviewStep` -> evaluates -> `application` (N:1): assessments accumulate on one case
- `decision` -> concludes -> `application` (1:1): every application ends in exactly one decision or lapse
- `decision` -> issues -> `grantReference` (1:0..1): a positive decision creates the right recorded in R5
- `condition` -> attachedTo -> `grantReference` (N:1): obligations follow the grant, not the application
- `revocation` -> terminates -> `grantReference` (N:1): withdrawal acts on the granted right

## Events

- `applicationSubmitted`: an applicant filed a request for authorization
- `evidenceProvided`: evidence was added to an open application
- `assessmentCompleted`: a review step recorded its finding
- `decisionIssued`: the authority granted or refused the application with reasons
- `grantRecorded`: the issued right was entered in the rights register
- `conditionImposed`: an obligation was attached to a grant
- `renewalGranted`: a grant's validity was extended after monitoring
- `grantRevoked`: a grant was suspended or withdrawn

## Contracts

- `applicantFileAccess`: an applicant's guaranteed access to their own case file, findings and reasons
- `publicPermitVerification`: third-party check that a permit exists and is valid, with its public conditions
- `regulatorExchange`: scoped exchange of case data between authorizing authorities with overlapping competence

## Projections

- `caseFile`: the full process view for the deciding authority; omits nothing within the case
- `permitCheck`: validity plus public conditions of a grant; omits application materials and internal findings
- `pipelineStatistics`: volumes, durations and outcome rates by activity type; omits all party identities

## Composition

- REFERENCE `world.grantedRight` (R5): the issued right lives there; this model holds only the process and the pointer
- REFERENCE `world.person` (P1): natural-person applicants and their evidence sources
- REFERENCE `world.organization` (O1): organizational applicants and consulted bodies
- REFERENCE `world.publicOffice` (A11): reviewers and deciders act under office powers
- REFERENCE `world.offenseEnforcement` (A18): enforcement outcomes may ground revocation
- MIX-IN `world.auditTrail` (S4): every submission, finding and decision is append-only
- imports: cpsv (ALIGN): public service description of the permitting procedure
- imports: cccev (EXTEND): criterion and evidenceItem specialize the core criterion and evidence structure

## Stewardship

The authorizing authority for each regulated domain (a mandated registrar or operator under A12) stewards its processes. Applicants always see their own file; all other access, including regulator exchange, is granted by the owner via S1 and S2.