# Business Establishment / Branch: authored design

Six bundles with two layers each. Each question maps to one explicit candidate
answer group. Proposed contracts are not executable instance schemas.
Require a source-qualified kind; statistical establishment, registered branch
and operational outlet are not universally equivalent.

## Operating identity and organizational attachment

### Kind, issuer and identity boundary
- Which operating-presence kind and source definition identify this record rather than a legal entity or building?
- Which issuer-qualified identifiers and aliases refer to this exact unit, and which identify only its parent or premises?
- Which evidence distinguishes co-located establishments or a multi-site branch without merging them by name or address?
Candidate fields: subject-kind {kind code; definition URI; jurisdiction; applicability}; identity-set {issuer; identifier; alias kind; effective interval}; distinction-evidence {neighbor refs; matching criteria; evidence refs; uncertainty}.
Sources: SRC-001, SRC-002, SRC-003, SRC-006.

### Operator, parent and legal accountability
- Which organization operates this presence and which legal entity is accountable under the recorded profile?
- Is the relationship a branch, unit, ownership, franchise or brand association, and what evidence supports that exact relation?
- Which changes of operator or parent preserve this identity and which require an evidenced successor under the issuer's rules?
Candidate fields: accountable-parties {operator ref; legal entity ref; role; profile}; organizational-links {target ref; relation kind; authority; valid interval}; continuity-rule {issuer rule; change ref; predecessor; successor; decision}.
Sources: SRC-002, SRC-004, SRC-006.

## Sites and recognizable presence

### Site bindings and address roles
- Which physical or digital sites are bound to this unit during each period, and which are merely correspondence addresses?
- Which site is registered, primary, headquarters or customer-facing without assuming these roles coincide?
- Which premises, entrance and geospatial master references locate the presence without making the organization itself a building?
Candidate fields: site-bindings {site ref; site kind; relationship period; address role}; site-roles {role code; site ref; authority; validity}; premises-location {premises ref; entrance ref; coordinate ref; evidence}.
Sources: SRC-004, SRC-005, SRC-006.

### Public identity and recognition evidence
- Which trading names, signs, contact channels and official pages identify this particular outlet rather than its entire chain?
- What observed evidence confirms presence at the claimed site, and how recent and reliable is it?
- Which misleading names, shared phone numbers or stale listings create ambiguity requiring a separate candidate match?
Candidate fields: public-identity {trading name; sign evidence; channel refs; official page}; presence-observation {method; observation time; source; confidence}; matching-ambiguity {candidate refs; conflicting signals; disposition; reviewer ref}.
Sources: SRC-003, SRC-005, SRC-007, SRC-008.

## Local activity and usable services

### Activity classification and scope
- Which principal and secondary activities actually occur here and which belong only to the parent organization?
- Which classifier, edition, code and allocation method describe this reporting scope?
- Which locally offered goods or services and delivery channels are referenced without copying their full specifications?
Candidate fields: local-activities {activity refs; principal flag; effective period; evidence}; activity-codes {scheme URI; edition; code; assignment method}; service-bindings {service ref; channel; local scope; availability evidence}.
Sources: SRC-001, SRC-002, SRC-007.

### Opening, availability and access conditions
- When is each local service available, under which timezone, exception calendar and last confirmation?
- Which appointment, eligibility, accessibility or entry conditions qualify use without assuming an open door means every service is offered?
- Which temporary disruptions, capacity limits or closure notices override the normal schedule?
Candidate fields: service-schedule {service ref; local timezone; weekly intervals; exceptions; confirmed at}; use-conditions {condition kind; service scope; premises evidence ref; policy}; availability-override {disruption ref; interval; affected service; status; evidence}.
Sources: SRC-007, SRC-008, SRC-009.

## Local authority and registration evidence

### Mandate, roles and contact responsibility
- Who holds local responsibility and what source-defined role or delegation applies?
- Which actions may that role authorize, with what financial, territorial or temporal limits?
- How can an agent reach an authorized contact without exposing private staff details or mistaking a contact listing for a mandate?
Candidate fields: local-roles {role ref; holder ref; authority evidence; period}; mandate-scope {action kinds; limits; delegation ref; expiry}; contact-routing {official channel; purpose; disclosure rule; verification time}.
Sources: SRC-004, SRC-006, SRC-008.

### Registration and scoped operating authorization
- Which register records recognize this kind of unit, with which jurisdiction, identifier and current status?
- Which referenced permits or authorizations cover which local activities and sites, and when do they apply?
- Which missing, expired or conflicting evidence requires an unresolved status rather than a claim that operation is legally permitted?
Candidate fields: register-evidence {register URI; record ID; unit kind; status; checked at}; authorization-bindings {permit ref; scope; jurisdiction; validity}; standing-uncertainty {gap; conflict refs; consequence; responsible reviewer}.
Sources: SRC-002, SRC-003, SRC-006, SRC-008.

## Continuity and reporting grain

### Opening, relocation and succession
- Which events establish opening, suspension, resumption, relocation or closure, and which dates are effective versus recorded?
- Did the event change the operating unit, premises, parent or only a public label?
- Which successor and predecessor links preserve history without reusing retired identifiers contrary to their issuer's rules?
Candidate fields: lifecycle-events {event ref; type; effective time; recorded time; source}; change-subject {affected entity ref; changed attributes; unchanged identity rationale}; succession-links {predecessor; successor; issuer policy; evidence}.
Sources: SRC-002, SRC-004, SRC-005, SRC-009.

### Statistical scope and local measures
- Which observation or reporting-unit definition applies to local employment, output or other reported measures?
- Which period, unit, coverage and source qualify each value, and is it measured, estimated, suppressed or unavailable?
- Which parent or co-located unit totals already include these measures, preventing duplicate aggregation?
Candidate fields: reporting-grain {statistical unit kind; definition ref; covered activities; locations}; reported-measures {measure code; value state; unit; period; source}; aggregation-boundary {included unit refs; overlap rule; parent totals; exclusions}.
Sources: SRC-001, SRC-002, SRC-006, SRC-008.

## Governed establishment knowledge

### Mastership, freshness and disclosure
- Which organization or register owns each assertion and which local copies are derived projections?
- How are contradictory operator, address, activity or status claims retained and reviewed without silently selecting a convenient source?
- Which roles may read or export establishment, contact and statistical details, under what retention and correction rules?
Candidate fields: assertion-mastership {field scope; master ref; cache ref; refresh rule}; contested-assertions {claim refs; authority comparison; review status; valid times}; information-policy {role scope; export limits; retention ref; correction receipt}.
Sources: SRC-001, SRC-004, SRC-008.

### Interoperability and semantic acceptance
- Which mappings preserve or lose distinctions among establishment, branch, site, legal entity and organizational unit?
- Is a shared identifier a qualified mapping rather than proof that all source-defined subjects are identical?
- Which fixtures demonstrate co-location, multi-site branches, relocation, temporary closure and withheld measures before an adapter is trusted?
Candidate fields: concept-mapping {source profile; target profile; relation; loss register}; identifier-mapping {source ID; target ID; scope; confidence; evidence}; adapter-evidence {fixture refs; expected result; observed result; unresolved mismatch}.
Sources: SRC-001, SRC-003, SRC-004, SRC-005, SRC-006, SRC-007.
