# S7 Access Enforcement & Breach

This meta-model describes what happens when the cluster's promises are broken: reads outside scope, onward sharing, retention past the deadline, grants ignored after revocation. It records signals, cases, established breaches, the sanctions imposed and the remedies delivered to the harmed party, plus each grantee's resulting standing. It is its own model because enforcement has a lifecycle and evidence discipline of its own, distinct from the contracts it protects and from the courts that decide contested cases.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s7"
  csn: world.accessEnforcement
  version: 0.2.0
  displayName: "Access Enforcement & Breach"
  description: "Violations of access contracts as cases: signals, established breaches, sanctions, remedies and grantee standing."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.accessEnforcement
bundles:
  - csn: world.accessEnforcement.violation
    displayName: "Violation"
    layers:
      - world.accessEnforcement.violation.signals
      - world.accessEnforcement.violation.cases
  - csn: world.accessEnforcement.resolution
    displayName: "Resolution"
    layers:
      - world.accessEnforcement.resolution.sanctions
      - world.accessEnforcement.resolution.remedies
  - csn: world.accessEnforcement.standing
    displayName: "Standing"
    layers:
      - world.accessEnforcement.standing.complianceStatus
      - world.accessEnforcement.standing.reinstatement
imports:
  - source: odrl
    version: "*"
  - source: iso-29100
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `violation` | Noticing and investigating | `signals`: anomalies from the audit log and reports from owners Â· `cases`: opened proceedings, gathered evidence, referral state |
| `resolution` | Consequences and redress | `sanctions`: consequences imposed on the violator Â· `remedies`: what the harmed party receives, from notification to erasure and restitution |
| `standing` | The violator's ongoing status | `complianceStatus`: a grantee's current standing across all cases Â· `reinstatement`: the path back to good standing after remedies are fulfilled |

## Objects

- `violationSignal`: a raw indication of possible violation; key attributes: source (audit anomaly, owner report, self-report), time, referenced entries.
- `enforcementCase`: an opened proceeding; key attributes: parties, evidence references, state, referral state.
- `breach`: an established violation of an access contract or of catalogue rules; key attributes: contract reference, kind (out-of-scope read, onward sharing, retention breach, post-revocation use), severity, established by.
- `sanction`: an imposed consequence; key attributes: kind (contract suspension, grant ineligibility, penalty under applicable law), duration, imposing body.
- `remedy`: redress delivered to the harmed party; key attributes: kind (notification, erasure confirmation, correction, restitution), delivered time, evidence.
- `complianceStanding`: a grantee's current status; key attributes: standing class, active sanctions, since.
- `reinstatementRecord`: the restoration of standing; key attributes: conditions met, verified by, effective time.

## Relationships

- `violationSignal` -> triggers -> `enforcementCase` (0..1): signals may be dismissed on triage or may open a case.
- `enforcementCase` -> establishes -> `breach` (0..1): a case ends in an established breach or a dismissal, never both.
- `breach` -> violates -> `accessContract` (1..1): every breach names the S2 instrument, or the catalogue rule, it broke.
- `sanction` -> imposedFor -> `breach` (*..1): consequences attach to established breaches, not to accusations.
- `remedy` -> redresses -> `breach` (*..1): the harmed owner's redress is tracked to completion per breach.
- `complianceStanding` -> summarizes -> `sanction` (0..*): standing is the live rollup of a grantee's active sanctions.
- `reinstatementRecord` -> restores -> `complianceStanding` (1..1): reinstatement is itself an evidenced act, not a decay.

## Events

- `signalRaised`: an anomaly or report suggested a violation.
- `caseOpened`: triage found the signal credible and a proceeding began.
- `caseReferred`: a contested or grave case was handed to the courts with its evidence package.
- `breachEstablished`: a violation was found proven, by the enforcing body or by a court.
- `sanctionImposed`: a consequence took effect against the violator.
- `remedyDelivered`: the harmed party received their redress and it was evidenced.
- `caseDismissed`: a case closed without an established breach.
- `standingReinstated`: a violator returned to good standing after fulfilling conditions.

## Contracts

- `breachNotification`: the harmed owner is informed of an established breach touching their objects, with the case evidence they are entitled to.
- `courtReferral`: the evidence package and case record are transmitted to the adjudication model under chain-of-custody terms.
- `standingCheck`: a prospective grantor queries a grantee's current standing before entering a new grant; detail beyond the standing class is not returned.

## Projections

- `ownerCaseView`: all signals, cases and outcomes touching my objects; omits every other owner's matters.
- `standingBadge`: a grantee's current standing class only; omits case detail and history.
- `enforcementStatistics`: cohort-grain counts of breaches, sanctions and remedies via the S5 machinery; omits all parties.

## Composition

- REFERENCE `world.accessContract` (S2): the violated instrument, its scope and its obligations define what counts as a breach.
- REFERENCE `world.accessAudit` (S4): the append-only log is the primary evidence source; signals cite entries and proofs of inclusion.
- REFERENCE `world.ownership` (S1): the harmed party is resolved through ownership records, including guardians acting for wards.
- REFERENCE `world.privacyAggregation` (S5): public enforcement statistics are released only at cohort grain under its floors.
- REFERENCE `world.disputeResolution` (A19): contested cases are decided by the courts model; this model records referrals and receives outcomes.
- imports: odrl (ALIGN): duty, prohibition and remedy vocabulary mapped onto obligations, sanctions and redress.
- imports: iso-29100 (ALIGN): privacy principles, including redress, that remedy kinds trace to.

## Stewardship

An enforcement registrar archetype keeps cases, sanctions and standing, acting alongside the courts (A19) that decide contested matters. It owns process records only: evidence stays anchored in S4, the harmed owner's rights stay theirs, and reads of enforcement data follow S1/S2 like everything else.
