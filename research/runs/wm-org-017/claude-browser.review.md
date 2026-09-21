# Vercy WM-ORG-017 Performance Objective / Review: independent design-review memo

**Scope note.** This review covers a generic public enterprise model and uses synthetic cases only. Every claim is labelled with one of three tags:

- **[O] Observed.** The source says this, and I read it in this pass.
- **[I] Inference.** This is my design reasoning.
- **[U] Unverified.** This is a mapping or fact I did not confirm from a primary source in this pass.

Nothing here asserts compliance with any standard or law.

---

## 0. Headline decisions

1. **Keep the governed case, but narrow what it is.** The aggregate root should be a *Performance Review Case*: one subject, one governing context, one period, one program. It should not be a general "performance record" for a person.
2. **Split out three things that the proposed boundary currently absorbs.**
   - A **Calibration Session** spans many cases. It becomes its own object, and each case holds only a case-local calibration outcome.
   - **Team or shared objectives** are referenced, not owned, by the case.
   - **Recognition** is a reference to a decision mastered elsewhere, such as pay or awards. Only the *recommendation* lives in the case.
3. **Assessment is optional and modal.** "Narrative-only" is a first-class assessment mode, not a degraded rating. A case with zero assessments is valid until it reaches the issue gate.
4. **There is no person-level score object anywhere in WM-ORG-017.** Any cross-period or cross-employer aggregate is out of scope and is treated as a negative case.
5. **Attribution is a claim, not a share.** Unknown or contested shares are represented explicitly. The model never defaults to an equal split.

---

## 1. Identity, lifecycle, cardinalities, ownership

### Identity

**[I]** The case has an opaque, system-issued identifier that never encodes a Person or Employment ID.

Its natural-key uniqueness constraint is: *(subject agent ref, governing context ref, program/template ref, period)*. Only one non-cancelled case may exist per tuple.

The governing context is exactly one of:

- Employment
- Engagement/Contract (for contractors)
- Membership
- Work Assignment

This resolves the concurrent-employment problem. A person with two employments gets two cases, never one case with two contexts.

**Precedent for independent position identity.** The W3C ORG ontology models people's relations to organizations through Membership, Role and Post. A Post represents some position within an organization that exists independently of the person or persons filling it [O]. This supports keeping context identity separate from person identity. Treating a Vercy "governing context" as an ORG Membership or Post is a design mapping [U], not a stated equivalence.

### Lifecycle

**[I]** The case moves through these states:

**Draft → Planned → Monitoring → Input Collection → Assessed-Draft → (Calibration Pending → Calibrated)? → Issued → Acknowledged → (Under Appeal → Revised | Upheld)* → Closed → Retention-Restricted → Disposed**

Side exits:

- **Cancelled (insufficient period).** OPM's public-sector example requires that a program establish a minimum period of performance that must be completed before a performance rating may be prepared [O]. Vercy should generalize this into a configurable minimum-period guard [I], not a legal claim.
- **Superseded.** Used when a case is re-scoped, for example after a context change.

**Monitoring is not optional.** A "Planned" case with objectives but no check-ins may proceed. However, the issue gate must record whether progress reviews occurred. OPM defines a progress review as communicating with the employee about performance compared to the performance standards of critical and non-critical elements [O].

### Cardinalities

| From case to… | Cardinality | Owner / master |
|---|---|---|
| Subject agent | 1 | Person master (reference only) |
| Governing context | exactly 1 | Employment / Engagement / Membership / Work Assignment masters |
| Period | 1 (bounded interval; may be extended) | Case |
| Program/template | 1 | Performance program config |
| Individual objectives | 0..n (versioned) | Case |
| Shared/team objectives | 0..n references | Team/org objective master |
| Evidence references | 0..n | Source systems (raw evidence never copied) |
| Attribution claims | 0..n | Case |
| Reviewer assignments | 1..n (≥1 accountable owner) | Case |
| Assessment versions | 0..n; ≤1 "issued current" | Case |
| Calibration outcomes | 0..n (one per session participation) | Case; session is external |
| Appeals / correction requests | 0..n | Case |
| Recognition recommendations | 0..n | Case (recommendation); downstream decision mastered elsewhere |
| Disclosure grants | 0..n | Case |

---

## 2. Domain bundles → facets → findings / questions / artifacts

The facets used below are Vercy's five whole-object facets:

- **ID**: identity/class
- **DP**: direct properties
- **RO**: recognition/observation
- **CBA**: capabilities/behaviour/actions
- **CE**: context/evidence

### B1. Case identity and governing context (ID, CE)

- **Finding [O].** OPM's rules require programs to establish criteria and procedures to address employee performance for employees who are on detail, who are transferred, and for other special circumstances. A departmental order shows one implementation of this: when an employee is detailed or temporarily promoted for 90 days or more, the temporary supervisor must complete an advisory rating and forward it to the supervisor of record.
- **Design consequence [I].** Secondary contexts contribute *advisory inputs* into the one governing case rather than creating a second authority. The 90-day figure is a single agency's choice and must not become a Vercy default.
- **Question.** When a contractor converts to employee mid-period, do we close one case and open another, or supersede? My recommendation is **close and open**, with an advisory link, because the governing contracts differ.
- **Artifact.** Governing-context resolution rule plus a uniqueness constraint.

### B2. Objectives, standards and capability vocabulary (DP, CBA)

- **Finding [O].** OPM defines a performance standard as the management-approved expression of the performance threshold(s), requirement(s), or expectation(s) that must be met to be appraised at a particular level of performance. It also states that performance plans shall be provided to employees at the beginning of each appraisal period (normally within 30 days).
- **Finding [O].** SFIA describes itself through seven levels of responsibility, ranging from Level 1 (the lowest) to Level 7 (the highest). SFIA's own material lists performance management frameworks – describe achievement of organisational/personal objectives as a *different* kind of framework from itself.
- **Finding [O].** ESCO provides descriptions of 3,039 occupations and 13,939 skills linked to these occupations, translated into 28 languages, and those concepts and the relations between them are published as Linked Open Data.
- **Decision [I].** SFIA and ESCO terms may tag objectives and competency expectations by URI, pinned to a version. A SFIA level is never used as a rating scale value. Keeping skill level and performance level apart is essential.
- **Question.** Can an objective change mid-period? Yes, but only as a new version, with the prior version retained and the assessment bound to a named version.

### B3. Evidence and attribution (CE, RO)

- **Finding [O].** PROV-O provides qualified attribution: if this Entity prov:wasAttributedTo Agent :ag, then it can qualify how it was influenced using prov:qualifiedAttribution.
- **Gap [O].** A 2015 public comment observed that prov:hadRole is not listed among the properties describing prov:Attribution, and the example uses a (fake) property ex:hadRole. PROV therefore gives no ready-made role-on-attribution property and no notion of credit shares. Vercy must add its own terms, such as `contributionRole`, `shareStatus`, `shareValue?` and `disputeRef?` [I].
- **Finding [O].** SPACE notes that software is often the sum of many developers' contributions, exacerbating the difficulty in evaluating the performance of any individual developer.
- **Decision [I].** An attribution claim has:
  - a claimant
  - a contributor
  - an evidence reference
  - a role
  - a `shareStatus` of *unknown*, *asserted*, *agreed* or *disputed*

  A `shareValue` is allowed only when the status is *agreed*. Contested credit stays contested. The assessment must cite the claims it relied on, and the issue gate warns if any cited claim is *disputed*.

### B4. Reviewer assignment and assessment (RO, CBA)

- **Finding [O].** HR-XML's EPMResult is described as a result where an appraisal typically consists of a number of sections, including an overall rating or score, competency ratings, objective ratings, and other ratings. A 2007 draft of the schema includes a RaterPanelInfo component.
- **Finding [O].** Separately, HR-XML has an EPMParticipant noun that contains a collection of data relevant to enrolling a participant within an employee performance management program. The participant/result split supports separating case enrolment from assessment output [I].
- **Caveat [U].** These are third-party mirrors of legacy HR-XML 3.x schemas. I did not locate or read the current HR Open Standards overview in this pass, and I am not asserting any field-level mapping.
- **Finding [O].** OPM requires that a rating of record shall be based only on the evaluation of actual job performance for the designated appraisal period. Agencies shall not carry over a rating of record prepared for a previous appraisal period as the rating of record for a subsequent appraisal period(s) without an actual evaluation.
- **Decision [I].** Assessment mode is one of *narrative*, *scaled* or *mixed*. The scale reference is required only for *scaled* and *mixed*.

  The contractor case uses governing context = Engagement and mode = narrative, with no scale. It is fully valid.

  Reviewer roles are:
  - accountable reviewer (exactly 1 at issue)
  - contributor/advisory reviewer (0..n)
  - self-input (0..1)
  - second-level approver (0..1, per program)

### B5. Calibration (RO, CBA)

- **Finding.** No primary source in this pass defines calibration.
- **Relevant finding [O].** SPACE warns that any measurement paradigm should check for biases and norms. It gives the example that looking at metrics over a year would bias against those taking parental leave.
- **Decision [I].** A Calibration Session is a separate object with its own:
  - participants
  - population scope
  - rules (for example, distribution guidance being advisory or forbidden)
  - minutes reference

  The case records a Calibration Outcome for each session: pre-value, post-value, rationale and session reference.

  Repeated calibration is allowed. Each outcome is append-only, and the "current" assessment version points to the latest outcome. A calibration outcome cannot change narrative text written by the accountable reviewer. It can only produce a new assessment version authored by an identified person.

### B6. Appeal, correction and retroactivity (CBA, CE)

- **Finding [O].** OPM restricts retroactive change. After deadlines pass, an agency shall not produce or change retroactively a rating of record that covers that earlier appraisal period, except in defined cases. The rulemaking explains that the exception is meant to provide for corrective action when ordered by a third party or as part of a bona fide settlement of a grievance, complaint, or other formal proceeding permitted by law.
- **Finding [O].** For automated decisions under GDPR Art. 22, commentary citing the Article 29 Working Party guidance says controllers should provide a way for the data subject to obtain human intervention, express their point of view and contest the decision.
- **Decision [I].** Two distinct request types handle correction versus opinion:
  - A **Correction Request** covers factual or data errors, such as the wrong period, a misattributed evidence item or a wrong objective version. It produces a *Correction* that amends the record and propagates a notice to consumers who received the old version.
  - An **Appeal** covers disagreement with judgment. It produces a *Decision* of *upheld*, *revised* or *partially revised*. If upheld, it attaches the subject's *Statement of Disagreement* to the case, and any disclosure of the assessment must carry that statement.

  Mapping this to GDPR rectification (Art. 16) is plausible but was not re-read in this pass [U]. Opinions are generally treated differently from factual inaccuracies, and that is exactly why the two types stay separate.
- **Repeated appeals.** Each appeal references the assessment version it challenges. A second appeal on the same version needs a new ground or an escalation level. The program configures a maximum escalation depth.

### B7. Recognition and the downstream-decision firewall (CBA, CE)

- **Finding [O].** The U.S. federal HR business standard lists service outcomes that include initiate employee reward and/or remediation based on employee performance rating. This is a public-sector process linkage, not a universal requirement.
- **Finding [O].** The EU AI Act Annex III employment category covers systems used for decisions affecting terms of work-related relationships, the promotion or termination of work-related contractual relationships, to allocate tasks based on individual behaviour or personal traits or characteristics or to monitor and evaluate the performance and behaviour of persons. The Act also says an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.
- **Timing [U].** Application dates may be moving. One compliance vendor reports a political agreement under which Annex III high-risk obligations would shift to 2 December 2027 (from 2 August 2026), conditional on formal adoption. I have not confirmed adoption status.
- **Decision [I].** The case emits *Recognition Recommendations* and *Consumption Events*. Pay, promotion, dismissal and hiring systems pull these under their own governance. No state transition in WM-ORG-017 can itself execute a downstream decision.

### B8. Disclosure, portability and retention (DP, CE)

- **Finding [O].** SPACE advises that teams and organizations should be cognizant of developer privacy and report only anonymized, aggregate results at the team or group level. It also notes that in some countries, reporting on individual productivity isn't legal.
- **Decision [I].** Every read outside the reviewer chain requires a *Disclosure Grant*, which records:
  - purpose
  - recipient
  - scope (the whole case, the narrative only, the outcome only, or the fact of existence)
  - legal-basis reference
  - expiry

  On an employer change, nothing is copied. At most, the subject can export their own copy, or the prior controller can issue a purpose-limited *attestation* such as "a review was completed for period X" under a grant. The dossier never moves.

---

## 3. Boundary challenge and alternative

The proposed boundary is broadly right about the separate masters: Person, Employment, Membership, Work Assignment, Organization, raw evidence, and pay/hiring/dismissal decisions. It over-reaches in three places.

1. **Calibration is cross-case by nature.** Modelling it inside the case hides the population-level decision, which is where bias and forced-distribution risk live. It needs to be a peer object (B5).
2. **Objectives have mixed ownership.** Team and OKR objectives cascade and outlive any single review. The case should own *individual commitments* and *reference* shared objectives. Otherwise, closing one case appears to close a team goal.
3. **"Recognition" is ambiguous.** In Vercy's facet vocabulary, "recognition/observation" means how the object is recognised. In HR, "recognition" means rewards. Rename the business concept to **Acknowledgement & Reward Recommendation** to avoid a semantic collision in the facet layer.

The resulting alternative is **WM-ORG-017 = Performance Review Case (root)**. It has these children:

- Objective Commitments
- Attribution Claims
- Reviewer Assignments
- Assessment Versions
- Calibration Outcomes
- Appeals/Corrections
- Reward Recommendations
- Disclosure Grants

It also has three peer objects: Calibration Session, Shared Objective and Performance Program. A proposed sibling, **WM-ORG-017a Performance Program**, holds period rules, scales, minimum period, reviewer rules and calibration policy.

---

## 4. Minimal profiles

**Startup profile.** This is the minimum a publishable draft case needs:

- One program with an annual or half-year period
- Assessment mode *narrative* by default
- One accountable reviewer, plus optional self-input
- Objectives as free text with an optional ESCO/SFIA tag
- Evidence as links only
- Attribution claims optional
- No calibration
- One appeal level, to a founder or a designated alternate who is not the reviewer
- Disclosure limited to the subject and reviewer, with an HR role when one exists
- Retention period declared

Contractors use the same profile with governing context = Engagement.

**International enterprise profile.** Everything in the startup profile, plus:

- Programs per legal entity or country, with a jurisdiction reference on every disclosure grant
- Scaled or mixed modes
- Second-level approval
- Calibration sessions with recorded rules
- Advisory inputs from secondary contexts
- Multi-level appeals, with an employee-representative or works-council consultation flag where configured [I; the specific obligations vary by country and are not verified here]
- An AI-assist register: any model-generated draft text or suggestion is flagged, its provenance recorded, and a human author is required for the issued version
- Translation of narrative with the original language preserved
- A data-residency tag
- Legal-hold override on disposal

---

## 5. Invariants and negative cases

1. **One governing context per case.**
   *Negative:* a case referencing both Employment A and Employment B is rejected. The fix is two cases plus advisory links.
2. **The natural key is unique among non-cancelled cases.**
   *Negative:* a second "FY26 engineering review" for the same subject, context and program is rejected.
3. **Draft validity without assessment.** A case may exist in Draft, Planned or Monitoring with zero assessment versions.
   *Negative:* the Issued state with zero assessment versions is rejected.
4. **Scale is conditional on mode.** Mode *narrative* forbids a scale value, and *scaled* requires one.
   *Negative:* a contractor case with a numeric rating but no declared scale is rejected. So is a system that imputes a default "meets" value.
5. **No assumed or carried-over assessment.** Each issued assessment cites evidence or observation from its own period. This generalizes OPM 430.208(a)(2) and (h).
   *Negative:* copying last year's rating forward is rejected.
6. **Attribution shares are never inferred.** `shareValue` exists only when `shareStatus` = agreed.
   *Negative:* auto-splitting a three-person project's credit 33/33/33 is rejected. So is deriving shares from commit counts.
7. **Proxy-signal prohibition.** Commit counts, keystrokes, screen time, badge swipes, emotion or biometric signals, and other surveillance telemetry may not be an evidence type for individual assessment. They may appear only as subject-supplied context. SPACE supports this directly: activity metrics should never be used in isolation either to reward or to penalize developers [O]. The stricter Vercy rule of exclusion rather than "not in isolation" is a design choice [I].
   *Negative:* a connector that pushes per-person commit totals into Evidence is rejected at schema level.
8. **No automated downstream execution.** No case transition invokes pay, promotion, termination or hiring actions. Downstream systems must record a named human decision-maker.
   *Negative:* the rule "rating ≤ 2 → auto-open termination workflow" is rejected.
9. **No portable person score.** No attribute or derived view aggregates assessments across cases into a person-level score, and nothing crosses a controller boundary.
   *Negative:* a "lifetime performance index" field is rejected. So is an export API returning ratings to a new employer.
10. **Calibration is append-only and attributed.** Every post-calibration change produces a new assessment version with a session reference and a named author.
    *Negative:* a silent in-place edit of a rating after a calibration meeting is rejected.
11. **Correction and appeal are distinct.**
    *Negative:* closing a factual correction request as "appeal upheld" is rejected. So is rewriting a manager's narrative to settle a disagreement without the reviewer's authorship.
12. **Disagreement travels with disclosure.** If a Statement of Disagreement exists, every disclosure grant covering the assessment includes it.
    *Negative:* a grant that discloses the outcome only while suppressing an attached statement is rejected.
13. **Retroactive change needs a basis.** After Closed, changes require a Correction or an Appeal decision reference.
    *Negative:* an HR admin edit on a closed case with no linked request is rejected.
14. **The reviewer is independent from the appeal decider.**
    *Negative:* an appeal decided by the same accountable reviewer is rejected, unless the startup profile explicitly records that no alternative exists and flags it.
15. **The raw evidence master is untouched.** The case stores references plus the excerpt hash the reviewer relied on, not copies.
    *Negative:* attaching full exported email mailboxes as evidence is rejected.

---

## 6. Serious omissions and publication gates

### Omissions in the current boundary

- **No Performance Program object.** Without one, rules have to be duplicated per case.
- **No AI-assist provenance.** Generative drafting of reviews is now common. Given the AI Act Annex III scope above, the model needs to record where text came from.
- **No leave and accommodation handling.** There is no pro-ration or exclusion for leave periods, although the parental-leave bias is explicitly flagged by SPACE [O].
- **No reviewer conflict-of-interest declaration.**
- **No explicit retention/disposal schedule or legal hold.**
- **No works-council or collective-agreement hook.**
- **No "performance improvement plan" boundary decision.** My recommendation is to keep PIPs out, as a separate object that may *reference* a case. PIPs carry dismissal-adjacent risk.
- **No multilingual narrative handling.**

### Publishable draft gate

A draft can be published when:

- Identity and the natural key are defined
- The governing-context rule is settled
- The lifecycle is modelled with side exits
- The cardinality table is agreed
- Bundles are mapped to facets
- Invariants 1–9 are expressible as schema or rule constraints
- Negative-case fixtures exist for the contractor, concurrent-employment and shared-credit scenarios
- All source claims are tagged O/I/U

### Canonical gate

A canonical model additionally requires:

- All 15 invariants tested against synthetic fixtures, including repeated calibration and a double appeal
- The Program and Calibration Session objects ratified
- The disclosure-grant purpose vocabulary reviewed by privacy counsel for at least one EU and one non-EU jurisdiction
- Any HR Open mapping verified against current published HR Open artifacts, **not** legacy HR-XML mirrors
- AI Act timing confirmed from EUR-Lex
- A decision on whether narrative text is ever machine-scored. My recommendation is no.

---

## 7. Primary references and what each supports

- **W3C ORG** (https://www.w3.org/TR/vocab-org/). This is a core ontology for organizational structures designed to allow domain-specific extensions to add classification of organizations and roles. It supports the separation of the context and position masters. It does *not* model performance.
- **ORG Post definition** (https://dvcs.w3.org/hg/gld/rev/1f4271e58fd5, editor's repository). This supports "position exists independently of holder." It is a working-group revision, so the final Recommendation wording is [U].
- **PROV-O qualified attribution** (https://dvcs.w3.org/hg/prov/rev/379513c95ed8) and the **hadRole-on-Attribution question** (https://lists.w3.org/Archives/Public/public-prov-comments/2015Apr/0001.html). Together these support the attribution pattern and the need for Vercy-specific role and share terms.
- **SPACE, ACM Queue 2021** (https://queue.acm.org/detail.cfm?id=3454124). This supports multidimensionality, no activity metrics in isolation, team attribution difficulty, aggregate-only reporting and bias checks. It is research guidance, not a standard.
- **5 CFR 430.206 / 430.208** (https://www.law.cornell.edu/cfr/text/5/430.206, https://www.law.cornell.edu/cfr/text/5/430.208). These are a U.S. federal example of period-bound ratings, no assumed ratings, no carry-over, a minimum period and limits on retroactive change. They are not universal law.
- **1998 Federal Register rulemaking** (https://www.govinfo.gov/content/pkg/FR-1998-10-05/html/98-26623.htm). This supports the rationale for correction exceptions.
- **GSA FIBF HR EPM** (https://ussm.gsa.gov/business-standards-api/hr/epm/business-lifecycle/). This supports the public-sector rating→reward/remediation linkage.
- **HR-XML 3.x EPMResult / EPMParticipant** (https://schemas.liquid-technologies.com/HR-XML/3.1/epmresult_xsd.html, https://schemas.liquid-technologies.com/HR-XML/3.0/processepmparticipant_xsd.html). These third-party mirrors support only the participant/result split and appraisal sectioning. No field mapping is asserted, and the HR Open overview was not verified.
- **SFIA** (https://sfia-online.org/en/about-sfia/how-sfia-works, https://sfia-online.org/en/forum/sfia-fundamentals-how-sfia-works). These support SFIA as a capability-level vocabulary distinct from performance management.
- **ESCO** (https://esco.ec.europa.eu/uk/node/8, https://interoperable-europe.ec.europa.eu/…esco). These support linked-data capability URIs and multilingual labels.
- **EU AI Act Art. 6 / Annex III** (https://euaiact.com/article/6 as a text mirror). This supports the profiling rule and the employment-use scope. The primary EUR-Lex text and current application dates are [U].
- **GDPR Art. 22 commentary** (https://gdpr-text.com/hr/read/article-22). This supports human intervention and contestation for automated decisions. The Art. 16 rectification mapping is [U].

I can turn this into a shareable doc if you'd like to iterate on it with others.