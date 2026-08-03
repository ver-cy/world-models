# N2 Report & Statement

This meta-model describes structured reporting: financial statements, statistical returns and compliance filings understood as sets of figures and assertions about a defined period, prepared against a template, filed with a receiver, validated and attested. It is its own model because the report lifecycle (prepare, file, validate, restate, attest) and the fact-in-context semantics of figures are shared across finance, regulation and statistics, distinct from the general document semantics of N1.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n2"
  csn: world.reportStatement
  version: 0.2.0
  displayName: "Report & Statement"
  description: "Structured financial, statistical and compliance reporting as figures and assertions over periods."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.reportStatement
bundles:
  - csn: world.reportStatement.reporting
    displayName: "Reporting"
    layers:
      - world.reportStatement.reporting.reportDefinition
      - world.reportStatement.reporting.submission
  - csn: world.reportStatement.content
    displayName: "Content"
    layers:
      - world.reportStatement.content.figures
      - world.reportStatement.content.assertions
  - csn: world.reportStatement.assurance
    displayName: "Assurance"
    layers:
      - world.reportStatement.assurance.validationChecks
      - world.reportStatement.assurance.attestationAndOpinion
imports:
  - source: xbrl
    version: "*"
  - source: sdmx
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `reporting` | What must be reported and the act of filing | `reportDefinition`: templates, taxonomies, mandates Â· `submission`: filed reports, periods, receivers |
| `content` | What the report says | `figures`: quantitative facts with units and contexts Â· `assertions`: declarative statements and disclosures |
| `assurance` | Why the report can be relied on | `validationChecks`: rule checks against templates Â· `attestationAndOpinion`: responsibility statements and external opinions |

## Objects

- `report`: a structured account for a period; key attributes: reportId, reportType, status, preparedByRef.
- `reportTemplate`: the mandated structure and taxonomy for a report type; key attributes: templateId, taxonomyRef, version, mandatingAuthorityRef.
- `reportingPeriod`: the interval a report covers; key attributes: periodStart, periodEnd, frequency, fiscalContext.
- `figure`: a reported quantitative fact; key attributes: conceptRef, value, unit, decimals, contextRef.
- `assertion`: a declarative statement or disclosure made in a report; key attributes: statementText, assertionType, madeByRef.
- `attestation`: a signed responsibility statement or external opinion; key attributes: attestorRef, opinionType, signedAt.
- `filing`: the submission act and receipt; key attributes: filedAt, receiverRef, receiptNumber, channel.
- `validationResult`: the outcome of a rule check; key attributes: ruleRef, severity, outcome, checkedAt.

## Relationships

- `report` -> conformsTo -> `reportTemplate` (N:1): the template mandates structure and taxonomy.
- `report` -> covers -> `reportingPeriod` (N:1): every report is about a period.
- `report` -> contains -> `figure` (1:N): the quantitative substance of the report.
- `assertion` -> assertedIn -> `report` (N:1): disclosures live inside a specific report.
- `figure` -> restates -> `figure` (N:1): a corrected figure supersedes a previously reported one.
- `attestation` -> attests -> `report` (N:1): responsibility and opinion attach to the whole report.
- `filing` -> submits -> `report` (1:1): the act that makes a report official.

## Events

- `reportPrepared`: a report reached a complete draft state.
- `reportFiled`: the report was submitted to its receiver.
- `filingAccepted`: the receiver accepted the filing.
- `filingRejected`: the receiver rejected the filing with findings.
- `figureRestated`: a previously reported figure was corrected.
- `reportAmended`: an amended report replaced an earlier filing.
- `attestationSigned`: a responsibility statement or opinion was signed.

## Contracts

- `regulatoryFilingContract`: the obligation and channel terms between reporter and receiving authority.
- `publicDisclosureContract`: terms of publication of filed reports for general consumption.
- `assuranceEngagementContract`: engagement between reporter and external attestor over scope and opinion.

## Projections

- `publicFilingView`: the accepted report as disclosed; omits validation traces and working notes.
- `supervisorView`: full content plus validation results and restatement history for the receiving authority.
- `seriesExtract`: figures only, keyed by concept and period, prepared for statistical reuse; omits assertions and attestations.

## Composition

- REFERENCE `world.organization` (O1): reporting organizations and receiving authorities.
- COMPOSE `world.documentRecord` (N1): a filing materializes as a governed document with signatures and retention.
- REFERENCE `world.officialStatistics` (N10): accepted figures feed statistical series production.
- REFERENCE `world.timeCalendar` (N11): reporting periods, deadlines and fiscal calendars.
- REFERENCE `world.identifierNaming` (N8): filer, report and concept identifier schemes.
- imports: xbrl (ALIGN): fact, context, unit and taxonomy semantics for financial figures.
- imports: sdmx (ALIGN): exchange semantics for statistical returns.

## Stewardship

The neutral owner archetype is the reporting organization, which owns its reports and figures even after filing; receivers hold copies under their own mandates. Access is always granted by the owner through the catalogue's S1/S2 ownership and access models, with disclosure and reuse audited via S4.
