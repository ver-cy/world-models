# WM-ACT-054 bounded provider focus

Research the governed participation aggregate connecting one research subject
to one study. Cover subject profile and study-specific identity, recruitment and
screening, eligibility, consent, assent and representative permission,
enrolment, allocation and blinding, participation periods and activities,
intervention and observation references, adherence, safety and incident links,
withdrawal, discontinuation, lost-to-follow-up and completion, compensation,
privacy, pseudonymisation, de-identification, data use, retention and audit while
keeping external masters distinct.

Use current official primary sources. Inspect ICH E6(R3) Good Clinical Practice,
ICH E8(R1), the 2024 Declaration of Helsinki, United States 45 CFR 46 and the
Belmont Report, EU Clinical Trials Regulation 536/2014, WHO trial-registration
requirements, HL7 FHIR R5 ResearchSubject, ResearchStudy and Consent, CDISC ODM
2.0 and current CDASH or SDTM guidance, ISO 14155:2020 catalogue metadata, HHS
HIPAA de-identification guidance, W3C PROV-O, GDPR and RFC 3339. Record species,
subject kind, jurisdiction, research type, protocol and standard versions rather
than claiming universal human-clinical-research semantics.

Stress-test these semantics:

- participant, human subject, animal subject, biospecimen, household, cluster,
  organization and other unit-of-analysis profiles are not interchangeable;
- person, animal, organization, specimen, study, protocol, consent artifact,
  eligibility criterion, intervention, observation, adverse event, payment and
  identity-linkage records remain external masters; this aggregate owns the
  study-specific participation relationship and typed references;
- public study subject ID, local screening or enrolment ID, randomization ID,
  pseudonym and restricted identity-linkage key have different scopes;
- recruitment contact, prescreening, screening, eligibility determination,
  informed consent, enrolment, allocation and start of participation are separate
  events and none alone proves the others;
- consent, assent, representative permission, re-consent, refusal and withdrawal
  are independently sourced and scoped; withdrawal from an intervention,
  participation, future contact and future data use are not equivalent;
- planned arm, assigned arm, actual exposure and observed adherence remain
  distinct, and blinding restricts views without erasing authoritative truth;
- completion, discontinuation, withdrawal, loss to follow-up and death are
  different participation outcomes; death itself remains an external event;
- successful enrolment does not prove eligibility, valid consent, protocol
  compliance, safety, benefit, data completeness or retention permission;
- pseudonymisation and de-identification do not prove anonymity or eliminate
  re-identification risk; linkage and re-identification authority are protected;
- already collected data, biospecimens and legal records after withdrawal follow
  consent, protocol, law, ethics and records policy rather than automatic delete.

The only registered relation is candidate incoming `WM-ACT-036 CONTAINS
WM-ACT-054`. Treat it as a boundary hold: this model may reference its parent
Research Study and record participation membership, but must not own or mutate
study protocol, governance or results. Keep the result reviewable-draft until
relation approval, research-type and jurisdiction profiles, ethics and privacy
review, release-pinned mappings and independent external review.
