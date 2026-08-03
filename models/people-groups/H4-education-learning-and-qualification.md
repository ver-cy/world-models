# H4 Education Learning & Qualification

This meta-model describes learning as a life path: the institutions and programs that provide education, the enrollments and assessments through which people learn, and the qualifications and issued credentials that certify what was learned. It is its own model because education has a three-sided lifecycle, provision by institutions, progression by learners, certification by registrars, whose artifacts (the credential above all) must remain verifiable long after programs and institutions change.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:h4"
  csn: world.educationQualification
  version: 0.2.0
  displayName: Education Learning & Qualification
  description: Education providers and programs, learner enrollment and assessment, qualifications and verifiable credentials.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.educationQualification
bundles:
  - csn: world.educationQualification.provision
    displayName: Provision
    layers:
      - world.educationQualification.provision.institutionProfile
      - world.educationQualification.provision.programCatalogue
  - csn: world.educationQualification.learning
    displayName: Learning
    layers:
      - world.educationQualification.learning.enrollment
      - world.educationQualification.learning.assessment
  - csn: world.educationQualification.qualification
    displayName: Qualification
    layers:
      - world.educationQualification.qualification.qualificationFramework
      - world.educationQualification.qualification.credentialRegister
imports:
  - source: europass-edc
    version: "*"
  - source: esco
    version: "*"
  - source: ceds
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `provision` | Who teaches and what is offered | `institutionProfile`: schools, universities and providers in their educational role Â· `programCatalogue`: programs, curricula and courses |
| `learning` | The learner's path through provision | `enrollment`: admission, enrollment and progression Â· `assessment`: examinations, grading and learning outcomes achieved |
| `qualification` | What learning certifies | `qualificationFramework`: qualification types, levels and frameworks Â· `credentialRegister`: issued credentials and their verification state |

## Objects

- `institutionProfile`: an education provider in its teaching role; key attributes: name, organization reference, accreditation state, level coverage
- `program`: a structured course of study; key attributes: name, level, curriculum outline, accreditation reference, duration
- `course`: a teachable unit within a program; key attributes: name, credits, outcomes taught, prerequisites
- `enrollment`: a learner's admission to a program; key attributes: learner reference, program reference, status, start, expected completion
- `assessmentResult`: a graded outcome of assessment; key attributes: enrollment reference, subject, grade, scale, date
- `qualification`: a qualification type at a framework level; key attributes: name, framework, level, skill mappings
- `credential`: an issued certification instance; key attributes: holder reference, qualification reference, issuer reference, issue date, status
- `learningOutcome`: a described capability a program teaches; key attributes: description, level, skill scheme mapping

## Relationships

- `program` -> offeredBy -> `institutionProfile` (n..1): every program has a providing institution
- `program` -> teaches -> `learningOutcome` (n..m): programs declare the outcomes they develop
- `enrollment` -> enrolls -> `person` (n..1): the learner is a natural person resolved via H1
- `assessmentResult` -> evidences -> `enrollment` (n..1): results document progression within an enrollment
- `credential` -> certifies -> `qualification` (n..1): a credential instantiates a qualification type for its holder
- `credential` -> issuedBy -> `institutionProfile` (n..1): the issuer remains accountable for the credential's validity
- `qualification` -> mappedTo -> `skill` (n..m): qualifications map to skills in the ESCO scheme, kept as scheme references

## Events

- `programAccredited`: a program received or renewed accreditation
- `learnerEnrolled`: a person was admitted and enrolled in a program
- `assessmentPassed`: an assessment was completed and graded
- `enrollmentCompleted`: a learner finished a program successfully
- `enrollmentWithdrawn`: an enrollment ended without completion
- `credentialIssued`: a credential was entered into the register
- `credentialRevoked`: an issued credential was invalidated by its issuer or registrar

## Contracts

- `credentialVerification`: third parties verify a credential's authenticity and status without receiving the transcript
- `transcriptRelease`: release of assessment detail only under the learner's consent, grounded in S1
- `educationStatisticsExtract`: aggregate enrollment and outcome data for the statistics office

## Projections

- `verifiableCredentialView`: credential, qualification, issuer and status; omits grades and enrollment history
- `learnerRecordView`: the learner's own complete record of enrollments, results and credentials
- `programProspectus`: public catalogue of institutions, programs and outcomes; omits all learner data

## Composition

- REFERENCE `world.person` (H1): learners and credential holders are natural persons referenced by identity
- REFERENCE `world.organization` (O1): institutions are organizations; the profile here carries only their educational role
- REFERENCE `world.populationGroup` (H3): learner cohorts for statistics are defined and materialized in the group model
- imports: Europass EDC (ALIGN): digital credential structure and verification semantics
- imports: ESCO (REFERENCE): skill and occupation scheme for outcome and qualification mappings, referenced never copied
- imports: CEDS (ALIGN): education data element definitions for provision and learning records

## Stewardship

The education registrar owns the qualification framework and the credential register; institutions own their profiles, programs and assessment records; the learner owns their learning record and every release of it via S1. All access is granted by the respective owner through S1/S2 and audited via S4.
