# X3 Incident & Emergency

This meta-model describes harm events that require response: from the first report through severity grading, alerting and response operations to resolution and after-action review. It is its own model, extending the generic occurrence (X1), because harm events carry semantics no ordinary happening has: graded severity, attributable impact, organized response and a formal closure and learning cycle.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:x3"
  csn: world.incidentEmergency
  version: 0.2.0
  displayName: "Incident & Emergency"
  description: "Harm events requiring response: report, severity, impact, alerting, response operations, resolution and review."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.incidentEmergency
bundles:
  - csn: world.incidentEmergency.incident
    displayName: "Incident"
    layers:
      - world.incidentEmergency.incident.incidentCore
      - world.incidentEmergency.incident.severity
      - world.incidentEmergency.incident.impact
  - csn: world.incidentEmergency.response
    displayName: "Response"
    layers:
      - world.incidentEmergency.response.alerting
      - world.incidentEmergency.response.operations
  - csn: world.incidentEmergency.closure
    displayName: "Closure"
    layers:
      - world.incidentEmergency.closure.resolution
      - world.incidentEmergency.closure.review
imports:
  - source: oasis-cap
    version: "*"
  - source: iso-22320
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `incident` | The harm event and how bad it is | `incidentCore`: kind, report and status of the incident · `severity`: graded judgements on declared scales · `impact`: harm attributed to people, assets and services |
| `response` | Warning and organized reaction | `alerting`: warning messages, levels and audiences · `operations`: response efforts and responder deployments |
| `closure` | How the incident ends and what is learned | `resolution`: the closure statement and residual risk · `review`: structured after-action findings |

## Objects

- `incident`: a harm-causing or harm-threatening occurrence requiring response; key attributes: incidentKind, reportedAt, status
- `severityAssessment`: a graded judgement of how bad the incident is; key attributes: scale, grade, assessedAt
- `impactRecord`: harm attributed to the incident across people, assets and services; key attributes: impactKind, quantity, verified
- `alert`: a warning message issued about the incident; key attributes: alertLevel, audience, issuedAt, expiresAt
- `responseOperation`: an organized effort to contain and resolve the incident; key attributes: operationKind, startedAt, endedAt, commandRef
- `responderAssignment`: a responder unit's deployment into an operation; key attributes: unitRef, assignedAt, releasedAt
- `resolutionRecord`: the closure statement of the incident; key attributes: resolvedAt, outcome, residualRisk
- `afterActionReview`: the structured review of the response; key attributes: reviewedAt, findings, recommendations

## Relationships

- `severityAssessment` -> grades -> `incident` (n:1): regrades accumulate as the picture clarifies
- `alert` -> warnsOf -> `incident` (n:1): one incident can drive several alerts to different audiences
- `responseOperation` -> respondsTo -> `incident` (n:1): large incidents can carry several parallel operations
- `responderAssignment` -> deploysInto -> `responseOperation` (n:1): units join and leave operations over time
- `impactRecord` -> attributesHarmTo -> `incident` (n:1): impacted objects are referenced in U1, U2, U3 and H1
- `resolutionRecord` -> closes -> `incident` (1:1): exactly one closure statement per incident
- `afterActionReview` -> examines -> `responseOperation` (n:1): reviews target operations, not victims

## Events

- `incidentReported`: a harm event was reported and entered the record
- `alertIssued`: a warning was published to a defined audience
- `severityRegraded`: the graded severity changed on new information
- `responseDispatched`: an operation was launched or a unit deployed
- `impactAssessed`: harm was attributed and quantified
- `incidentContained`: the harm stopped spreading though the incident remained open
- `incidentResolved`: the incident was closed with an outcome and residual risk
- `reviewCompleted`: the after-action review was finished and findings recorded

## Contracts

- `publicAlertFeed`: open dissemination of active alerts to any consumer
- `mutualAidExchange`: data sharing between cooperating response operators during and after incidents
- `impactDisclosureContract`: verified impact data disclosed to insurers or relief organizations under owner grant

## Projections

- `liveIncidentBoardProjection`: active incidents with alert levels and operation status; omits victim identities
- `incidentStatisticsProjection`: aggregate frequency, severity and impact; omits all case-level detail
- `afterActionSummaryProjection`: findings and recommendations; omits personal data of responders and victims

## Composition

- EXTEND `world.occurrenceEvent` (X1): an incident is an occurrence with severity, impact and response semantics added
- REFERENCE `world.buildingStructure` (U1): damaged buildings and structures in impact records
- REFERENCE `world.premisesSpatialUnit` (U2): affected premises and their occupancy context
- REFERENCE `world.physicalInfrastructureNetwork` (U3): affected network assets, mirrored there as closure events
- REFERENCE `world.situationCondition` (X4): a prolonged emergency is registered as a situation while it holds
- REFERENCE `world.person` (H1): affected parties and individual responders
- REFERENCE `world.organization` (O1): responder units and relief organizations
- imports: oasis-cap (EXTEND: alert message structure, levels and audiences)
- imports: iso-22320 (ALIGN: incident response terminology)

## Stewardship

The owner archetype is the emergency response operator, which stewards incident, alert and operation records. Victims' and responders' personal details are disclosed only under S2 grants, statistics are released in aggregate form, and the full record trail is auditable via S4.