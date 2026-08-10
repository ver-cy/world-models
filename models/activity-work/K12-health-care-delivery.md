# K12 Health Care Delivery

This meta-model describes the system side of health care: providers and practitioners, facilities and their capacity, the care services on offer, and the flow of encounters, referrals and waiting through the system. It deliberately excludes the person side, clinical states, diagnoses and personal health episodes, which live in the personal health model (B10); this model records that care capacity existed and that encounters happened, referencing the person side without duplicating it.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k12"
  csn: world.healthCareDelivery
  version: 0.2.0
  displayName: "Health Care Delivery"
  description: "Providers, facilities, capacity and encounter flow of the care system."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.healthCareDelivery
bundles:
  - csn: world.healthCareDelivery.provision
    displayName: "Provision"
    layers:
      - world.healthCareDelivery.provision.providerRegistry
      - world.healthCareDelivery.provision.facilityProfile
      - world.healthCareDelivery.provision.serviceOffering
  - csn: world.healthCareDelivery.capacity
    displayName: "Capacity"
    layers:
      - world.healthCareDelivery.capacity.capacityStatement
      - world.healthCareDelivery.capacity.staffing
  - csn: world.healthCareDelivery.encounterFlow
    displayName: "Encounter flow"
    layers:
      - world.healthCareDelivery.encounterFlow.encounterRecord
      - world.healthCareDelivery.encounterFlow.referralAndTransfer
      - world.healthCareDelivery.encounterFlow.waitingAndQueue
imports:
  - source: hl7-fhir
    version: "*"
  - source: snomed-ct
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `provision` | Who provides care, where, and what | `providerRegistry`: provider organizations and practitioner roles · `facilityProfile`: locations, departments and equipment classes · `serviceOffering`: care services offered at facilities |
| `capacity` | The system's ability to deliver | `capacityStatement`: beds, appointment slots and equipment availability · `staffing`: practitioner coverage and on-call arrangements |
| `encounterFlow` | Care delivery as system events | `encounterRecord`: system-side facts of admissions, visits and discharges · `referralAndTransfer`: directed movement between services and facilities · `waitingAndQueue`: demand awaiting delivery |

## Objects

- `provider`: an organization delivering care; key attributes: name, kind (hospital, clinic, practice), accreditation, organization reference
- `practitionerRole`: a person acting in a care capacity; key attributes: person reference, profession, specialty, registration identifier, facilities served
- `facility`: a place where care is delivered; key attributes: name, site reference, departments, service hours
- `careService`: a defined care offering; key attributes: name, specialty, modality (inpatient, outpatient, remote), eligibility
- `capacityStatement`: quantified deliverable capacity; key attributes: facility and service reference, unit (beds, slots, procedures), quantity, period
- `encounter`: a system-side care delivery episode; key attributes: facility, service, practitioner roles involved, admission and discharge times, person-side reference
- `referral`: a directed request for care elsewhere; key attributes: source, target service or facility, urgency, status
- `waitingListEntry`: registered demand not yet served; key attributes: service reference, entry date, priority class, status

## Relationships

- `provider` -> operates -> `facility` (one-to-many): the places the organization runs
- `practitionerRole` -> practisesAt -> `facility` (many-to-many): where a practitioner works
- `careService` -> offeredAt -> `facility` (many-to-many): what care is available where
- `capacityStatement` -> quantifies -> `careService` (many-to-one): how much of a service a facility can deliver
- `encounter` -> occurredAt -> `facility` (many-to-one): where the episode took place
- `encounter` -> concerns -> `personalHealthEpisode` (one-to-one): the person-side record, referenced never inlined
- `referral` -> directsTo -> `careService` (many-to-one): the target of the referral
- `waitingListEntry` -> queuesFor -> `careService` (many-to-one): the demand a service faces

## Events

- `providerRegistered`: a care organization entered the provider registry
- `facilityCommissioned`: a care location opened or materially changed capability
- `capacityReported`: a facility declared or revised its deliverable capacity
- `encounterStarted`: a care episode began at a facility
- `encounterEnded`: a care episode concluded, with discharge disposition on the system side
- `referralMade`: a patient pathway was directed to another service or facility
- `waitingTimeRecorded`: the waiting duration for served or waiting demand was measured

## Contracts

- `directoryAccess`: consumers read providers, facilities, services and hours for finding care
- `capacityReporting`: providers disclose capacity and utilization to a public health authority per cadence
- `encounterNotification`: the system side notifies the person-side record (B10) that an encounter opened or closed, carrying references only

## Projections

- `publicDirectory`: providers, facilities, services and hours; omits capacity, staffing and all encounter data
- `capacityHeatmap`: aggregate available and occupied capacity by region and service; omits persons and individual facilities where small numbers would identify
- `referralNetworkView`: flows of referrals between services; omits individual patients

## Composition

- EXTEND `world.service` (K4): care services specialize the general service offering and delivery model
- REFERENCE `world.personalHealth` (B10): encounters reference person-side health episodes without duplicating clinical content
- REFERENCE `world.person` (H1): practitioners behind practitioner roles
- REFERENCE `world.organization` (O1): provider organizations
- REFERENCE `world.site` (P5): facilities grounded as sites
- REFERENCE `world.functionAndCapability` (K1): practitioner specialties as attributed capabilities
- REFERENCE `world.processAndWorkflow` (K3): care pathways operationalized as workflows
- imports: hl7-fhir (ALIGN): resource semantics for Organization, Location, Encounter and Schedule
- imports: snomed-ct (REFERENCE): terminology for coding services and specialties

## Stewardship

Provider organizations own their registry, capacity and encounter records, with oversight access held by a public health authority; person-side data stays with the person under B10. All access is owner-granted via the catalogue's ownership and access models (S1/S2), with audit via S4.
