# S8 Cyber Integrity & System Security

This meta-model describes the technical health of the systems the catalogue depends on: known vulnerabilities, which live systems are exposed and how far patched, the threats and indicators observed against them, the incidents that actually occurred, and the control baselines and posture assessments that say how well defended each system is. It is its own model because system security has its own registries, actors and cadence (disclosure, patching, incident response) that are orthogonal to who owns data and who may read it, yet every access guarantee in this cluster silently assumes it.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s8"
  csn: world.cyberIntegrity
  version: 0.2.0
  displayName: "Cyber Integrity & System Security"
  description: "Vulnerabilities, exposures, threats, incidents, controls and posture of the catalogue's registered systems and networks."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.cyberIntegrity
bundles:
  - csn: world.cyberIntegrity.weakness
    displayName: "Weakness"
    layers:
      - world.cyberIntegrity.weakness.vulnerabilities
      - world.cyberIntegrity.weakness.exposures
  - csn: world.cyberIntegrity.threat
    displayName: "Threat"
    layers:
      - world.cyberIntegrity.threat.actorsAndCampaigns
      - world.cyberIntegrity.threat.indicators
  - csn: world.cyberIntegrity.incident
    displayName: "Incident"
    layers:
      - world.cyberIntegrity.incident.detection
      - world.cyberIntegrity.incident.response
  - csn: world.cyberIntegrity.assurance
    displayName: "Assurance"
    layers:
      - world.cyberIntegrity.assurance.controls
      - world.cyberIntegrity.assurance.posture
imports:
  - source: cve
    version: "*"
  - source: cwe
    version: "*"
  - source: cvss
    version: "*"
  - source: iso-27001
    version: "*"
  - source: oasis-stix
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `weakness` | What could be exploited | `vulnerabilities`: known weaknesses in software and components Â· `exposures`: which concrete systems carry them and their patch state |
| `threat` | Who and what attacks | `actorsAndCampaigns`: actors, campaigns and techniques posing risk Â· `indicators`: observable signs of compromise and their attribution |
| `incident` | What actually happened | `detection`: declared incidents, triage and impact scoping Â· `response`: containment, recovery and closure |
| `assurance` | How well defended | `controls`: each owner's declared control baseline Â· `posture`: periodic assessments against that baseline |

## Objects

- `vulnerability`: a known weakness in software or a component; key attributes: CVE reference, CWE class, CVSS severity, affected versions.
- `exposure`: the presence of a vulnerability in one concrete system; key attributes: system reference, discovery time, mitigations in place.
- `patchState`: the remediation status of an exposure; key attributes: state (open, mitigated, patched, accepted), target date, verified time.
- `threat`: an actor, campaign or technique posing risk; key attributes: capability, intent, technique references.
- `indicator`: an observable sign of compromise; key attributes: observable, confidence, first and last seen.
- `cyberIncident`: a realized security event; key attributes: systems struck, impact, timeline, data-exposure flag.
- `controlBaseline`: the control set a system owner declares; key attributes: control catalogue reference, scope, declared time.
- `postureAssessment`: one evaluation of a system against its baseline; key attributes: method, findings, score, assessed time.

## Relationships

- `exposure` -> instantiates -> `vulnerability` (*..1): one published weakness fans out into many concrete exposures.
- `exposure` -> affects -> `registeredSystem` (*..1): exposures attach to systems and network nodes registered in M8 and N4.
- `patchState` -> remediates -> `exposure` (1..1): every exposure carries exactly one live remediation status.
- `indicator` -> signals -> `threat` (*..1): indicators are attributed, with stated confidence, to threats.
- `cyberIncident` -> exploited -> `vulnerability` (0..*): incidents cite the weaknesses used when known.
- `cyberIncident` -> struck -> `registeredSystem` (1..*): every incident names the systems affected.
- `postureAssessment` -> evaluates -> `controlBaseline` (1..1): assessments measure a system against its own declared baseline.

## Events

- `vulnerabilityDisclosed`: a weakness became known, with or without a coordinated embargo.
- `exposureIdentified`: a concrete system was found to carry a known vulnerability.
- `patchApplied`: a remediation was applied and its verification recorded.
- `threatObserved`: a threat actor, campaign or technique was observed in scope.
- `incidentDeclared`: a security event was declared an incident and triage began.
- `incidentContained`: the spread of an incident was stopped; recovery began.
- `incidentClosed`: recovery finished and lessons were recorded.
- `assessmentCompleted`: a posture assessment concluded with findings.

## Contracts

- `coordinatedDisclosure`: a finder, the system owner and the CERT steward agree on an embargo and publication timeline for a new vulnerability.
- `threatSharing`: system owners exchange indicators and threat context under attribution and confidentiality terms.
- `incidentNotification`: the CERT steward, and the owners of data held on a struck system, are notified within agreed timeframes when an incident has a data-exposure flag.

## Projections

- `publicAdvisory`: vulnerability, affected versions and fixed versions; omits which live systems remain unpatched.
- `ownerRiskDashboard`: exposures, patch states and posture for one owner's systems only; omits everyone else's estate.
- `certSituationBoard`: cross-system aggregate of exposures, threats and incidents at cohort grain; omits identifiable unpatched systems.

## Composition

- REFERENCE `world.informationSystem` (M8): the software systems whose weaknesses, incidents and baselines this model tracks.
- REFERENCE `world.network` (N4): network infrastructure appears as the other class of protected, registered asset.
- REFERENCE `world.ownership` (S1): system ownership determines who patches, who declares baselines and who is notified.
- REFERENCE `world.accessAudit` (S4): access-log anomalies feed detection, and incident timelines cite log entries as evidence.
- REFERENCE `world.accessEnforcement` (S7): an incident that is also a violation of access contracts escalates into that model's cases.
- imports: cve (REFERENCE): the public identifier scheme for vulnerabilities.
- imports: cwe (REFERENCE): the weakness classification scheme behind vulnerability classes.
- imports: cvss (REFERENCE): the severity scoring vocabulary carried on vulnerabilities.
- imports: iso-27001 (ALIGN): the control catalogue that declared baselines map to.
- imports: oasis-stix (ALIGN): the exchange shape for threats and indicators under threat-sharing contracts.

## Stewardship

Each system owner stewards the records of their own systems: exposures, patch states, baselines and assessments. A CERT steward archetype coordinates across owners, runs disclosure embargoes and keeps the situation board; access to any owner's detail remains a grant from that owner under S1/S2, logged in S4.
