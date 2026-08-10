# B10 Personal Health

The health status and care of one person: conditions, observations, encounters with care providers, medications, treatments and care plans, gathered as a record that belongs to the person it describes. It is its own meta-model because person-grain health facts have the strictest custody requirements in the catalogue and a clinical structure of their own, distinct both from population-level health (B14) and from any register that merely certifies a health fact.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:b10"
  csn: world.personalHealth
  version: 0.2.0
  displayName: "Personal Health"
  description: "The health status, care history and care plans of one person, held under the person's own custody."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.personalHealth
bundles:
  - csn: world.personalHealth.healthState
    displayName: "Health state"
    layers:
      - world.personalHealth.healthState.condition
      - world.personalHealth.healthState.observationAndResult
      - world.personalHealth.healthState.allergyAndRisk
  - csn: world.personalHealth.care
    displayName: "Care"
    layers:
      - world.personalHealth.care.encounter
      - world.personalHealth.care.medicationAndTreatment
      - world.personalHealth.care.carePlan
  - csn: world.personalHealth.custody
    displayName: "Custody"
    layers:
      - world.personalHealth.custody.recordCustody
      - world.personalHealth.custody.disclosureControls
imports:
  - source: hl7-fhir
    version: "*"
  - source: snomed-ct
    version: "*"
  - source: who-icd
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `healthState` | What is currently and historically true of the person's health | `condition`: diagnosed and self-reported conditions with course and resolution · `observationAndResult`: measurements, test results and findings · `allergyAndRisk`: allergies, intolerances and standing risk factors |
| `care` | What is done about the person's health | `encounter`: contacts with care providers, from visit to admission · `medicationAndTreatment`: prescriptions, administrations and procedures · `carePlan`: agreed goals and coordinated activities across providers |
| `custody` | The person's control over the record | `recordCustody`: the record as the person's property, provider contributions as entries into it · `disclosureControls`: scoped grants, emergency access and donation of de-identified data |

## Objects

- `healthRecord`: the person's whole health folder; key attributes: subjectRef, custodyStatus, coverageSpan
- `condition`: a state of ill or noteworthy health; key attributes: code, onsetAt, course, resolvedAt, severity
- `observation`: a single measured or noted finding; key attributes: code, value, unit, observedAt, method
- `allergyIntolerance`: a standing adverse-reaction risk; key attributes: agent, reactionKind, criticality, verifiedAt
- `encounter`: one contact between the person and a care provider; key attributes: providerRef, kind, startedAt, endedAt, reason
- `medication`: a medicine prescribed or taken; key attributes: code, dosage, startedAt, endedAt, prescriberRef
- `treatment`: a procedure or therapy performed or planned; key attributes: code, performedAt, outcome, performerRef
- `carePlan`: an agreed program of care; key attributes: goals, activities, period, participants

## Relationships

- `healthRecord` -> aggregates -> `encounter` (one-to-many): the record collects all encounters of its subject
- `observation` -> madeDuring -> `encounter` (many-to-one): findings arise in a care contact
- `condition` -> evidencedBy -> `observation` (many-to-many): diagnoses rest on findings, findings can support several conditions
- `treatment` -> addresses -> `condition` (many-to-many): therapy targets one or more conditions
- `medication` -> prescribedDuring -> `encounter` (many-to-one): prescriptions trace to the contact that produced them
- `carePlan` -> coordinates -> `treatment` (one-to-many): a plan sequences treatments and activities

## Events

- `conditionDiagnosed`: a condition was identified and entered into the record
- `observationRecorded`: a measurement or finding was added
- `encounterClosed`: a care contact concluded and its content was filed
- `medicationPrescribed`: a medicine was ordered for the person
- `treatmentAdministered`: a procedure or therapy was carried out
- `carePlanAgreed`: the person and providers settled a plan of care
- `allergyIdentified`: a standing adverse-reaction risk was established
- `conditionResolved`: a condition was recorded as ended

## Contracts

- `careProviderAccessContract`: a scoped, time-limited grant by the person letting a provider read and contribute to defined parts of the record
- `emergencyAccessContract`: break-glass access to the emergency subset, always fully audited and notified to the person afterwards
- `researchContributionContract`: the person's voluntary donation of de-identified extracts under stated purposes and revocability

## Projections

- `patientSummaryView`: current conditions, medications, allergies and recent encounters; omits deep history and provider notes
- `emergencyView`: blood-relevant facts, critical allergies and active medications only; omits everything else
- `researchView`: de-identified, cohort-ready extracts; omits identifiers, free text and rare-trait combinations that could re-identify
- `selfView`: the complete record with its full access history, visible only to the person

## Composition

- REFERENCE `world.person` (H1): the subject of the record is the person entity governed in its own model
- REFERENCE `world.identityRegister` (R4): record custody and provider access bind to anchored identities and keys
- COMPOSE `world.publicHealthAndEpidemiology` (B14): consented or legally mandated notifiable facts flow upward de-identified and at cohort grain, never as the person's record
- REFERENCE `world.attestationCertificateAndLicense` (R5): immunization and fitness certificates are issued as attestations grounded in record entries
- REFERENCE `world.socialProvisionAndBenefit` (B13): care-need assessments may read granted extracts when the person applies for care services
- MIX-IN `world.audit` (S4): every read, contribution and disclosure carries the audit facet
- imports: hl7-fhir (ALIGN): condition, observation, encounter, medication and care-plan resource semantics
- imports: snomed-ct (REFERENCE): clinical terms as an externally governed code scheme
- imports: who-icd (REFERENCE): diagnosis classification as an externally governed code scheme

## Stewardship

The person owns the record outright, with the strictest default settings in the catalogue: nothing is visible to anyone until the person grants it. All access, including provider contributions and emergency use, is granted through the S1/S2 access and consent models and is fully auditable by the person via S4.
