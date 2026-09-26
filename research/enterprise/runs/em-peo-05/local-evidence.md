# EM-PEO-05 local synthesis

## Disposition

- Propose identifier-unassigned **Learning Program**, **Enrollment**, **Career Path** and **Succession Plan** roots.
- Reuse and narrow WM-ACT-038 for scheduled Learning Activity / Course Delivery; keep definition, enrollment and assessed results external.
- Profile Learning Result on WM-PER-008 as an outcome-achievement assertion; do not create a separate root.
- Profile Development Plan on WM-ACT-008 with subject, purpose and disclosure constraints.
- Profile readiness assessment on WM-ACT-034, nomination and appointment decisions on WM-REC-010, and assignments on WM-ORG-016.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Learning definition and version, delivery/cohort, session, enrollment, attendance, assessment result, delivery completion, learning result, competency assertion, qualification award, credential, development plan, development objective, career-path definition, worker aspiration, succession plan, nomination, readiness assessment, appointment decision and assignment remain distinct.

Curriculum stewards master program definitions. Providers master deliveries. Registrars master enrollment and admission. Assessors master results. Awarding bodies and credential issuers retain their respective authority. The worker and manager co-govern a development plan while the worker owns aspiration. Talent-governance authorities master succession plans and readiness assertions. Appointing authorities issue decisions; WM-ORG-016 remains the assignment master.

## Learning definition, delivery and enrollment

WM-ACT-038 already places program/course definition, enrollment, assessment, result, qualification and credential outside its aggregate. It should own a scheduled delivery/cohort, released roster projections, delivery sessions, participation assertions, attendance and completion disposition. Its parent relation to WM-PER-008 is rejected: delivery and learner record reference one another without a containment relation.

Learning Program is a reusable, versioned curriculum definition that exists independently of a delivery. Enrollment is an independent lifecycle root because admission, prerequisites, capacity, waitlist, transfer, withdrawal and learner rights may exist before a delivery and survive its cancellation or replacement. WM-ACT-038 binds source-qualified participation to an enrollment; login or access never proves attendance.

## Results, qualifications and credentials

Attendance, assessment result, delivery completion, learning result, competency assertion, qualification award and credential are non-equivalent assertions.

Learning Result profiles WM-PER-008 and pins the learning-objective identifier and version, criteria version, scale version and WM-ACT-034 result. Completion never implies outcome achievement. Outcome achievement never implies qualification. Qualification never implies issued credential, and credential validity never proves current competence.

## Development plan and career path

Development Plan profiles WM-ACT-008 with non-authorizing intent. It owns versioned development objectives, success criteria, planned activities, target dates, baseline and progress. Enrollment, delivery, learning result and credential references are many-to-many realization links, allowing one course to serve multiple objectives without duplicating results. No element grants promotion, pay, entitlement or authority.

Career Path is a reusable versioned graph or ordered ladder referencing job families, positions or grade levels. It defines typical transitions and expectations and exists without an incumbent. A worker aspiration is a dated worker-declared assertion carried by the development plan profile; it is neither a promise nor a nomination.

## Succession, readiness and appointment

Succession Plan independently owns critical-position scope, review cycle, pool membership, bench depth, coverage state and referenced readiness assessments. Each revision creates a successor and leaves prior readiness facts and current assignments unchanged.

Readiness profiles WM-ACT-034 with pinned criteria, method, evidence, scale, assessor competence, impartiality and validity. Nomination and appointment are distinct WM-REC-010 decisions. Appointment requires an authorized decision followed by a WM-ORG-016 assignment. Readiness, pool membership and nomination confer neither assignment nor access.

## Privacy and retention

Potential and readiness ratings are deny-by-default, purpose-bound and minimum-disclosure data. Each records lawful basis, authorized audience, review interval and challenge/correction route. Correction creates an attributable successor. Retention triggers remain specific to enrollment, result, award, credential, plan, rating and decision. Legal hold suspends disposition, and disposal never cascades to person, position, employment or assignment masters.

## Required invariants

1. Definition, delivery and enrollment are distinct.
2. Enrollment identity is external to a delivery.
3. Attendance is not learning achievement.
4. Completion is not qualification.
5. Learning Result pins objective version and assessment basis.
6. One score is not durable competency.
7. One result may realize several development objectives without duplication.
8. A development plan is not a personnel decision.
9. Worker aspiration is not management nomination.
10. Career path is not entitlement or promotion.
11. Readiness is not appointment or access.
12. Succession-plan revision leaves assignments unchanged.
13. Ratings expire and remain contestable.
14. Final results and released delivery history change only through successors.

## Acceptance result

One program version and delivery serve two development objectives through one enrollment and one outcome-achievement assertion. A learner who attends but fails assessment retains attendance while receiving no learning result, competency assertion, award or credential. A revised succession plan changes pool/readiness assertions without mutating current assignments. A later appointment occurs only through a new authorized decision and assignment, from which access may then be derived.

## Holds

No approved relation rows cover WM-ACT-038, WM-PER-008, WM-XCT-017 or WM-PER-009. WM-ACT-038, WM-PER-008 and WM-XCT-017 remain single-provider waived drafts; WM-ACT-034 retains access and retention holds; WM-PER-009 lacks a current specification. Learning Program, Enrollment, Career Path, Succession Plan and the previously proposed Person Capability Assertion lack registry allocations and independent evidence. Source pins, interoperability crosswalks and fixtures remain unverified. This checkpoint is not an installable release.
