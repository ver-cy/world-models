# WM-ACT-014 Health Care Delivery: Codex pre-research

Status: preparatory analysis by Codex. This is not Claude research, provider evidence, adjudication, synthesis, validation or a publication artifact.

## Frozen boundary

- Registry plane: `standalone-mm`; research-plane candidate: `aggregate` because the subject is a delivery-system aggregate spanning provision, capacity, access and care-flow records.
- Root subject: the system-side capability and delivery of health services by provider organizations through authorized roles and physical or virtual locations.
- Included: provider-service-location directory bindings, role availability, operating capacity, scheduling and queue state, referrals and transfers as delivery coordination, and the system-side shell of actual encounters.
- Excluded: personal clinical state, diagnoses, observations, treatment content, medications, procedures, patient-owned longitudinal health episodes, professional qualification lifecycle, organization lifecycle, facility construction, billing and insurance adjudication.
- Strict relation: `WM-ACT-014 CONTAINS WM-ACT-018`. The encounter model owns encounter lifecycle and detailed event semantics. This model may aggregate and reference encounters for flow, utilization and capacity questions, but must not reproduce the encounter model.
- The legacy K12 card is useful only as non-authoritative migration evidence. Its provider, facility, capacity and encounter-flow separation is retained as a hypothesis, while ownership boundaries require tightening.

## Primary evidence set

| ID | Organization | Source | Intended support | Verification hold |
| --- | --- | --- | --- | --- |
| CXS-001 | WHO | Integrated people-centred care | continuum, coordination, equity, quality and responsiveness | verify resolution and page version |
| CXS-002 | WHO | Services organization and integration | delivery across levels and sites, comprehensive service continuum | verify current page date |
| CXS-003 | WHO | Service Availability and Readiness Assessment | facility availability, readiness, inputs and service-delivery monitoring | verify guide version 2.2 document |
| CXS-004 | WHO | Quality health services: a planning guide | national, district and facility quality-action levels | verify ISBN document text |
| CXS-005 | HL7 International | FHIR R5 HealthcareService | offered service, organization, physical or virtual location, availability linkage | R5 is trial-use in relevant areas |
| CXS-006 | HL7 International | FHIR R5 PractitionerRole | authorized role-period, organization, location, specialty and offered service | R5 is trial-use in relevant areas |
| CXS-007 | HL7 International | FHIR R5 Encounter | actual encounter versus planned appointment; service provider, participants and locations | detailed lifecycle belongs to WM-ACT-018 |
| CXS-008 | HL7 International | FHIR R5 Organization and Location | separates who performed a service from where it occurred | confirm permanent R5 pages |
| CXS-009 | ISO | ISO 7101:2023 | documented delivery processes, people-centred quality, risk, safety and performance improvement | full normative clauses not reviewed |
| CXS-010 | OECD | Health at a Glance 2025 | access, unmet need, waiting time and system-performance indicator dimensions | cross-country comparability limits |

Source URLs:

- https://www.who.int/health-topics/integrated-people-centered-care
- https://www.who.int/teams/integrated-health-services/clinical-services-and-systems/service-organizations-and-integration
- https://www.who.int/data/data-collection-tools/service-availability-and-readiness-assessment-%28sara%29
- https://www.who.int/publications/i/item/9789240011632/
- https://hl7.org/fhir/healthcareservice.html
- https://hl7.org/fhir/practitionerrole.html
- https://hl7.org/fhir/encounter.html
- https://hl7.org/fhir/organization.html
- https://hl7.org/fhir/location.html
- https://www.iso.org/standard/81647.html
- https://www.oecd.org/en/publications/health-at-a-glance-2025_8f9e3f98-en/full-report.html

## Candidate subject structure

### Bundle 1: Delivery network

1. Provider-service topology
   - provider organization reference and accountable delivery unit
   - service offering identity, category, modality and eligibility summary
   - physical, mobile, home and virtual delivery-location bindings
2. Authorized delivery roles
   - practitioner-role reference and authorization period
   - role, specialty, organization, location and service binding
   - coverage gaps and temporary or unfilled roles

Boundary note: organization and person identity, employment, qualifications and licensing remain externally owned. Local records describe only their participation in delivery.

### Bundle 2: Availability and operational capacity

1. Published availability
   - service hours, planned closures, access channels and availability exceptions
   - distinction between directory availability and bookable operational supply
2. Capacity statements
   - capacity type, quantity, unit, period, location and service
   - staffed versus physical capacity and surge capacity
   - source, confidence and observation time
3. Readiness and constraints
   - workforce, equipment, infrastructure and essential-input readiness references
   - service limitations, outage state and restoration estimate

Boundary note: inventories, workforce contracts, devices and facilities are references. This model owns only their effect on deliverable service capacity.

### Bundle 3: Demand, access and allocation

1. Access pathway
   - entry channel, eligibility rule reference, referral requirement and geographic reach
   - accessibility, language, remote-care and reasonable-adjustment attributes
2. Queue and waiting state
   - demand registration, priority class, clock start and pause rules
   - offered, deferred, declined, removed and fulfilled states with reasons
   - distinction among prospective wait, completed wait and censored wait
3. Scheduling and allocation
   - requested service and resource class
   - allocated slot, role, location and capacity reservation references
   - cancellation, rescheduling, no-show and reallocation events

Boundary note: appointment semantics should compose with a scheduling model if one exists. Patient-specific eligibility evidence and personal preference stay in their owning models.

### Bundle 4: Care-flow coordination

1. Referral routing
   - source, target service, urgency, reason-code reference and acceptance state
   - redirection, rejection, expiry and closure reasons
2. Transfer and handoff
   - sending and receiving provider-service-location references
   - requested, accepted, departed, arrived and failed handoff milestones
   - responsibility-transfer point and continuity exception
3. Encounter-flow projection
   - encounter reference, class, service, responsible provider and location
   - system-side admission/start and discharge/end timestamps
   - aggregation by pathway, queue, capacity and utilization

Boundary note: encounter clinical content and detailed lifecycle remain in `WM-ACT-018`; this bundle owns only cross-encounter system flow and references.

### Bundle 5: Quality, safety and performance

1. Delivery quality commitments
   - applicable quality-policy and service-level references
   - safe, effective, timely, equitable, integrated and people-centred dimensions
2. Operational measures
   - denominator, numerator, population, period, stratifier and calculation provenance
   - availability, readiness, utilization, cancellation, waiting and continuity measures
3. Delivery disruptions and exceptions
   - outage, diversion, capacity breach, unsafe condition and access failure
   - impact scope, mitigation, escalation and resolution references

Boundary note: incident investigation, clinical outcome interpretation and audit trail semantics belong to their dedicated models. This model may reference their determinations.

### Bundle 6: Governance, provenance and disclosure

1. Stewardship and authority
   - owner of each directory, capacity, queue and flow record
   - asserted authority, jurisdiction/profile and effective period
2. Provenance and versioning
   - source system, recorder, event time, observation time, ingestion time and supersession
   - authoritative identifier first, governed global identifier second, Dimension UUID/ULID third
3. Access, consent and disclosure
   - public directory versus operational versus person-linked projections
   - purpose, recipient class, minimum necessary disclosure and emergency exception reference
4. Retention and disposition
   - record-class-specific retention policy reference
   - legal hold, de-identification, tombstone and verified disposition outcome
   - execution delegated to the adopting Dimension or the dedicated retention/disposition model

## Candidate functions

- register and version a service offering
- bind a service to provider, authorized role and delivery location
- publish directory-safe availability
- record time-bounded capacity and readiness statements
- register demand and manage queue-state transitions
- allocate delivery capacity and record scheduling exceptions
- route referrals and coordinate transfers
- ingest encounter references without duplicating encounter semantics
- calculate provenance-bearing access, wait, utilization and continuity projections
- declare outages, diversions and capacity breaches
- enforce owner-gated projections and purpose restrictions
- apply retention, legal-hold and disposition instructions through the owning policy model

## Adversarial checks for the later no-tools audit

1. Does an `aggregate` root improperly absorb the encounter lifecycle despite the `CONTAINS WM-ACT-018` relation?
2. Are provider directories being confused with actual operational availability or bookable capacity?
3. Are professional qualifications or employment facts duplicated instead of referenced?
4. Are person-linked queue, referral and encounter fields separated from public service-directory data?
5. Are physical beds/equipment distinguished from staffed and usable capacity?
6. Do waiting-time measures define clock start, pauses, censoring, removal and completion consistently?
7. Are virtual, home, mobile, emergency and cross-organization delivery settings represented without assuming a hospital-only model?
8. Are event time, observation time and ingestion time distinct and RFC 3339 values required to contain seconds and an explicit offset or `Z`?
9. Is deletion execution delegated to the owning retention policy while this model preserves tombstone and provenance requirements?
10. Are regional accreditation, licensing, eligibility and reporting rules marked as profile-specific rather than universal?

## Preliminary holds

- Claude independent research has not run.
- The no-tools Claude adversarial audit has not run.
- Source URLs and document-level versions require live verification during the provider pass.
- ISO 7101 normative clause text was not available in this pre-research pass.
- The sole model relation is still marked `candidate`.
- The boundary between the aggregate care-delivery shell and `WM-ACT-018` needs explicit adjudication.
- Cross-jurisdiction validation and domain-profile testing remain outstanding.
- Retention periods, licensing rules, access exceptions and quality thresholds must be supplied by adopting-jurisdiction policy.

## Agent-native five-facet assessment

Roadmap basis: `VERCY-AGENT-NATIVE-REALITY-2026-09-05.md`. This assessment is mandatory input to Claude research and later adjudication.

| Facet | Applicability | Reason or delegation |
| --- | --- | --- |
| identity/class | required | Every `Health Care Delivery` instance needs authoritative identity, class membership criteria, distinguishing attributes, versioned taxonomy and whole-part boundaries. |
| direct properties | required | The subject is abstract, informational, organizational, event-like or observational at this boundary. Record its direct legal, logical, computational or semantic properties and do not invent physical fields. |
| recognition/observation | required | Agents need logical, textual, registry or evidence-based recognition criteria, confidence and rules for distinguishing adjacent classes. |
| capabilities/behaviour/possible actions | required | Agents must distinguish what the subject can do, how it behaves, its states and transitions, and what authorized actors may do with it. |
| context/evidence | required | Ownership, provenance, place, time, history, governing rules, access, confidence and master-system evidence are necessary for safe agent memory and action. |

### Behaviour and action distinctions

Claude must separately assess:

- `capability`: what the subject can do or undergo;
- `behavior`: how it responds under stated conditions;
- `state`: its current operational, legal, informational or physical condition;
- `transition`: an evidenced change from one valid state to another;
- `affordance`: what an agent, person or related object may do with it;
- `operation`: required permission, preconditions, tools, inputs, effects, output and reversibility;
- `constraint`: limits, compatibility, prohibitions and applicable policy;
- `hazard`: a condition with potential harm and its exposure context;
- `failure mode`: how capability or integrity fails, how failure is detected and what recovery or safe-state response applies.

### Measurement rule

Do not add geometry, mass, material, colour or other physical measurements unless the model references a genuinely physical subject owned elsewhere. Direct properties here are domain-native nonphysical attributes. Observations must still record method, time, confidence and evidence.

### Future publication AGENTS.md gate

The generated model `AGENTS.md` must route an agent through population, extension, patching, editing, validation and retirement. It must explain the Bundle to Layer to Finding to Question to Artifact traversal, the five facets, fact versus hypothesis versus unknown, delegated child models and master systems, autonomous versus confirmation-required operations, and pre-write plus post-write checks. After the public protocol exists, it must link to `https://ver.cy/model-agent-protocol.md`; until then this URL remains an explicit publication dependency and verification hold.
