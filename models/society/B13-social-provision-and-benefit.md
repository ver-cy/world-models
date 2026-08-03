# B13 Social Provision & Benefit

The delivery of social support to people: benefit programs and their eligibility rules, assessed entitlements, the deliveries of money and care services that fulfil them, and the review and redress machinery that keeps awards correct. It is its own meta-model because provision is a lifecycle of its own, from program design through assessment to delivery and appeal, distinct from the ledgers that move the money and the health records that may inform a care assessment.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:b13"
  csn: world.socialProvisionAndBenefit
  version: 0.2.0
  displayName: "Social Provision & Benefit"
  description: "Benefit programs, assessed entitlements, deliveries of money and care, and the review and redress around them."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.socialProvisionAndBenefit
bundles:
  - csn: world.socialProvisionAndBenefit.program
    displayName: "Program"
    layers:
      - world.socialProvisionAndBenefit.program.benefitDefinition
      - world.socialProvisionAndBenefit.program.eligibilityRules
  - csn: world.socialProvisionAndBenefit.entitlement
    displayName: "Entitlement"
    layers:
      - world.socialProvisionAndBenefit.entitlement.assessment
      - world.socialProvisionAndBenefit.entitlement.award
  - csn: world.socialProvisionAndBenefit.delivery
    displayName: "Delivery"
    layers:
      - world.socialProvisionAndBenefit.delivery.paymentDelivery
      - world.socialProvisionAndBenefit.delivery.serviceDelivery
  - csn: world.socialProvisionAndBenefit.review
    displayName: "Review"
    layers:
      - world.socialProvisionAndBenefit.review.circumstanceChange
      - world.socialProvisionAndBenefit.review.appealAndRedress
imports:
  - source: esspros
    version: "*"
  - source: ilo-convention-102
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `program` | What support exists and who is meant to get it | `benefitDefinition`: benefit kinds, amounts or service scopes, funding basis Â· `eligibilityRules`: the declared conditions of entitlement per program |
| `entitlement` | Deciding who actually qualifies | `assessment`: examining an application against the rules with stated evidence Â· `award`: the granted entitlement, its amount or scope, period and conditions |
| `delivery` | Getting support to the person | `paymentDelivery`: monetary deliveries executed over payment accounts Â· `serviceDelivery`: care and in-kind services delivered as episodes |
| `review` | Keeping awards correct and contestable | `circumstanceChange`: reported and detected changes affecting entitlement Â· `appealAndRedress`: challenges to decisions and their outcomes |

## Objects

- `benefitProgram`: one defined scheme of support; key attributes: kind, benefitShape, fundingBasis, administeringBodyRef
- `eligibilityRule`: a declared condition of entitlement; key attributes: programRef, criterion, evidenceRequired, effectivePeriod
- `application`: a person's request for support; key attributes: applicantRef, programRef, submittedAt, evidenceRefs
- `entitlement`: a granted award; key attributes: holderRef, programRef, amountOrScope, period, conditions, status
- `delivery`: one act of fulfilling an entitlement; key attributes: entitlementRef, kind, deliveredAt, channelRef, quantity
- `careService`: a defined care or in-kind service; key attributes: serviceKind, providerRef, intensity
- `circumstanceReport`: a reported or detected change of circumstances; key attributes: subjectRef, changeKind, reportedAt, source
- `appeal`: a formal challenge to an assessment or adjustment; key attributes: challengerRef, contestedDecisionRef, grounds, outcome

## Relationships

- `application` -> requests -> `benefitProgram` (many-to-one): each application targets one program
- `entitlement` -> grantedUnder -> `benefitProgram` (many-to-one): awards inherit the program's shape and rules
- `entitlement` -> heldBy -> `world.person` person (many-to-one): support attaches to an identified person or household member
- `delivery` -> fulfils -> `entitlement` (many-to-one): an award is fulfilled by a series of deliveries
- `careService` -> providedUnder -> `entitlement` (many-to-one): service episodes trace to the award authorizing them
- `circumstanceReport` -> mayAffect -> `entitlement` (many-to-many): one change can touch several awards
- `appeal` -> contests -> `entitlement` (many-to-one): decisions on an award can be challenged

## Events

- `applicationSubmitted`: a person applied for a program
- `eligibilityAssessed`: an application was examined against the rules
- `entitlementAwarded`: an award was granted with amount or scope and period
- `entitlementAdjusted`: an award was changed following a circumstance review
- `benefitDelivered`: a monetary or in-kind delivery was made
- `careEpisodeCompleted`: a care service episode concluded and was recorded
- `entitlementSuspended`: an award was paused pending review
- `appealDecided`: a challenge was resolved and the award confirmed, changed or restored

## Contracts

- `recipientSelfAccessContract`: the person's standing right to see their own applications, awards, deliveries and the reasons behind decisions
- `caseworkerAccessContract`: purpose-bound access for assigned caseworkers to the cases they handle
- `deliveryChannelContract`: terms with a payment or service channel for executing deliveries
- `statisticsExtractContract`: aggregate, disclosure-controlled extracts for program statistics

## Projections

- `recipientView`: the person's own entitlements, deliveries and decisions with reasons; omits other recipients and program internals
- `caseworkerView`: full case detail for assigned cases; omits cases not assigned
- `programPerformanceView`: uptake, expenditure and outcome aggregates; omits person-level records
- `payoutInstructionView`: delivery instructions for the payment channel; omits assessment reasoning and health-related evidence

## Composition

- REFERENCE `world.person` (H1): applicants and recipients are persons governed in their own model
- REFERENCE `world.lifeEventsAndCivilStatus` (B12): registered births, deaths and union changes trigger entitlement reviews
- REFERENCE `world.personalHealth` (B10): care-need assessment reads only extracts the person has granted for that purpose
- COMPOSE `world.ledgerAndAccount` (R2): monetary deliveries execute as postings on accounts of the ledger model
- REFERENCE `world.identityRegister` (R4): recipients and administering bodies resolve to anchored identities
- MIX-IN `world.audit` (S4): assessments, adjustments and disclosures carry the audit facet
- imports: esspros (ALIGN): benefit function classification for reporting and statistics
- imports: ilo-convention-102 (ALIGN): branch vocabulary of social security minimum standards

## Stewardship

The social provision administrator owns programs, assessments and delivery records and answers for their correctness; each person owns the view of their own case and sees every decision with its reasons. Access beyond the person's own record is granted via the S1/S2 access and consent models and audited via S4.
