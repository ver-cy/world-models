Benjamin’s standards map is in. I’ll wait once more for Harper’s bundle draft and Lucas’s negative-case notes, then write the memo.# Research Memo

**Subject:** Vercy WM-ORG-017 Performance Objective / Review — independent adversarial design review  
**Catalogue:** WM-ORG-017 · `vr.wm-org-017`  
**Tagline (verified):** “Objective, evidence, assessment and outcome lifecycle”  
**Parent listed (verified):** WM-ORG-016 Work Assignment  
**Classifier (verified):** NAV.SOC.ORG.PERF  
**Status of the catalogue object (verified):** planned stub. The Bundle → Layer → Finding → Question / Artifact specification has not been written. No placeholder YAML is published as if complete.  
**Assurance this memo may claim:** visibly reviewable draft of a *proposed* specification. Not a canonical Vercy release. Not a compliance attestation.

Method. Catalogue pages and neighbor models were read as live objects. Primary instruments were read for what they actually specify. Design structure below is **inferred**: it is a proposal constrained by those sources and by the brief, not a found specification. Where a source is gated, mirrored, or only abstracted, that limit is named. No clause of GDPR, the AI Act, SHRM, HR Open, SFIA, ESCO, or ISO is invented, and none is treated as satisfied by the existence of a field.

---

## 1. Identity and lifecycle boundaries; alternative splits

### 1.1 What the object is

WM-ORG-017 is a **governed cycle object**: one identifiable plan-and-assessment lifecycle that binds *intended outcomes*, *attributed evidence*, *period assessment*, *optional calibration*, *contest/correction*, *recognition candidates*, and *purpose-limited disclosure*.

It is not a person, not an employment, not a membership, not a position, and not a work assignment. Those are separate referenced identities. The catalogue parent is Work Assignment (WM-ORG-016), which models the time-bounded binding of an agent to a role, post, or body of work. Employment (WM-ORG-005) is the jurisdiction-qualified worker–employer relationship and already owns assignment *realization links*, skill *references*, and dispute routes for *employment status*, not period ratings. Person (WM-PER-001) is the civil-identity anchor other models point at. Position (WM-ORG-004) holds competency *requirements*, not demonstrated period delivery. Organization (WM-ORG-001) is the entity. Membership (WM-ORG-006) is a required separate boundary: the Employment publication hold states that a previous card fused Employment and Membership and that the registry now splits them.

**Inferred identity rule.** One WM-ORG-017 instance is identified by its own durable identifier in a declared master system. Dates, person names, and “FY2025 review” labels are never keys. Two reviews of the same person in different periods, or under different employments, are different instances.

### 1.2 What it must not own

| Neighbor | Owns | 017 may only |
|---|---|---|
| WM-PER-001 Person | civil identity | `person_ref` |
| WM-ORG-001 Organization | entity identity | `org_context_ref` / governing-entity ref |
| WM-ORG-004 Position | durable post and required capabilities | `position_ref` |
| WM-ORG-005 Employment | legal relationship, status disputes | `employment_ref` (0..n, one governing per review) |
| WM-ORG-006 Membership | affiliation without employment | `membership_ref` only if work is membership-based |
| WM-ORG-016 Assignment | occupancy of work | `assignment_ref[]` |
| WM-PER-008 Education / Qualification | credentialed learning outcomes | reference, do not absorb |
| External vocabularies (ESCO URI, SFIA skill+level) | concept identity | reference as context or capability *claim*, never as the cycle grade |

The five-facet gate applies. This is an abstract object: physical properties are `not-applicable`. Identity/class and context/evidence are `required`. Recognition/observation is `required` for evidence items. Capabilities/behaviour/actions are `required` for lifecycle transitions (open, submit, calibrate, contest, close, project, archive). Direct properties are `required` only for native cycle fields (period, purpose, scale version, decision mode). Facets may be `delegated` to a pinned neighbor, not copied.

### 1.3 Lifecycle this model covers

**In scope (inferred, matching the brief and the catalogue tagline):**

1. Draft objective → agreed objective  
2. In-period evidence capture and attribution  
3. Review period open; reviewer assignment  
4. Assessment acts against a *versioned contextual scale*  
5. Optional calibration act (visible adjustment, not a fog)  
6. Cycle outcome recorded as period-scoped, non-portable  
7. Recognition events as candidates, not rating writes  
8. Appeal / contest / correction with supersession  
9. Purpose-specific disclosure and portability projection  
10. Temporal validity, archive, minimisation hook (duration is a policy hook, not a number this model may invent)

**Out of scope:** hiring or firing execution; payroll execution; visa/immigration determination; skill-ontology maintenance; position classification; attendance/roster master data; always-on monitoring collection systems; a global intrinsic employee score; any automatic employment decision from commits, keystrokes, presence, webcam, or emotion inference.

### 1.4 Alternative model splits

The catalogue currently chooses **S0**: one aggregate covering objective + evidence + review + calibration + appeal + recognition + disclosure.

| Split | What it does | Cost |
|---|---|---|
| **S0 Catalogue current** | One WM-ORG-017 aggregate | Matches the stub. Risk of fusing plan, grade, badge, and pay input. |
| **S1 HR-XML-faithful** | 017a ObjectivesPlan/Result + 017b EPMResult/RaterPanel | Strongest existing interchange precedent. Risk of orphaned plans. |
| **S2 Cycle vs instance** | Program/Period instrument vs ReviewInstance vs ObjectiveItem | Best for multinational calibration. More objects. |
| **S3 Recognition-out** | Recognition as neighbor | Recommended. Recognition often exists with no review. |
| **S4 Scale-out** | RatingScaleVersion as its own catalog object | Recommended. Scales must version independently of people. |
| **S5 Calibration-out** | CalibrationSession sibling | Later, if many-reviews-to-one-session cardinality explodes. |

**Recommended hybrid (inferred, not approved):** keep WM-ORG-017 as the aggregate for ObjectiveItem + EvidenceItem + ReviewInstance + AppealCase; *reference* a versioned RatingScale; *reference* Recognition if a neighbor exists, otherwise hold recognition as a disjoint event type inside 017; keep CalibrationSession as an internal bundle now. Parent remains WM-ORG-016 for work context, but **Employment WM-ORG-005 is required-when-the-subject-is-an-employee**. Assignment-only parent under-specifies contractor, dual employment, host/agency, and employer change. The 005 COMPOSE 016 ledger edge is still *candidate*, not approved; 017 cannot pretend otherwise.

HR Open already splits ObjectivesPlan, ObjectivesResult, EPMResult, EPMRaterPanel, EPMParticipant, DevelopmentPlan. That is integration vocabulary, not a fairness code. SFIA splits knowledge / skill / competency evidential claims and, separately, treats competency assessment (LEDA) as distinct from performance appraisals. ESCO splits occupation vs skill concepts and is a dictionary, not a grade. ANSI/SHRM-09001-2012 limits itself to goal setting, performance review, and individual improvement plans, and explicitly does not address competencies or compensation.

---

## 2. Proposed structure: 7 bundles, 14 layers, 24 findings

All slugs and findings below are **inferred design**. They are written in the house style of published ORG neighbors so a later YAML author can implement them without inventing a second grammar.

### Bundle 1 — `identity-class-and-neighbor-bindings`  
*Facet: identity-class (required).*

**Layer 1.1** `instance-identity-and-lineage`  
- **F01 Authoritative instance identifier and master system.** Stable ID, issuer, namespace, master system, status, typed aliases for one objective-and-review instance. Dates and person names are not keys.  
  *Questions:* Which system masters this instance ID? How are two reviews of the same person in different periods kept distinct?  
  *Artifact:* Instance identity record (ID, scheme, master, status, aliases).  
  *Invariant:* Correction of a clerical ID is a new version, not a reuse of the old ID on a different person.

- **F02 Duplicate, merge, split, supersession and successor lineage.**  
  *Questions:* When is a record a correction of the same world-fact versus a new cycle? What successor pointer is written on close-and-replace?  
  *Artifact:* Lineage edge set (predecessor, successor, reason: correction | split | period-successor | void).

**Layer 1.2** `neighbor-bindings-and-class-boundary`  
- **F03 Neighbor bindings without identity copy.** Typed refs: `person_ref` (1), `employment_ref[]` (0..n), `assignment_ref[]` (1..n), `org_context_ref` (1), `position_ref` (0..1), `membership_ref` (0..1).  
  *Questions:* Which employment governs *this* review if two are concurrent? Which assignments were actually in scope?  
  *Artifact:* Binding set with valid time, asserted time, knowledge time.  
  *Invariant:* No embedded copy of legal name, contract terms, salary, or civil identifiers.

- **F04 Class boundary: what this object is not.** Explicit rejection codes for “this is a person scorecard”, “this is a competency ontology”, “this is a DORA dashboard”, “this is a pay instruction”.  
  *Artifact:* Boundary note + rejected-fusion log.

### Bundle 2 — `objective-plan-and-period`  
*Facet: direct-properties (required for period/purpose/objective fields).*

**Layer 2.1** `review-period-and-program-instrument`  
- **F05 Review period, program and cycle instrument.** Interval `[start,end)`, timezone, schedule code (continuous | quarterly | midyear | annual | probation | project | ad-hoc — HR-XML schedule words are *alignment candidates*, not adopted enumerations until the XSD is pinned).  
  *Questions:* What period is being assessed? Which program instrument (legal entity, language, scale version, collective-instrument ref) governs the cycle?  
  *Artifact:* Period + program instrument record.

- **F06 Purpose code.** Declared purpose at creation: `development | administrative | statutory | recognition-only | compensation-input | promotion-input | contested | research-aggregate`. Cross-purpose reuse is a governed event, not a default join.  
  *Invariant:* Purpose limitation is a hook. The model does not adjudicate lawful basis.  
  *Artifact:* Purpose declaration with owner and knowledge time.

**Layer 2.2** `objective-items-and-success-criteria`  
- **F07 Objective item.** Intended outcome, owner, metric or qualitative test, evidence plan, difficulty/specificity notes, valid interval, governing employment + assignment. Locke and Latham support specific, difficult goals *with feedback* for relatively straightforward tasks; CIPD’s evidence review warns that the same pattern can harm complex knowledge work. The model stores the goal object; it does not mandate SMART theater.  
  *Questions:* What would count as met, unmet, or not-evaluable? Which constraints (staffing, dependency, incident load) are declared up front?  
  *Artifact:* Objective item record + evidence-plan list.

- **F08 Alignment and unit of objective.** Individual, shared-team, or cascaded-from-org-objective, with explicit unit of analysis.  
  *Invariant:* A team objective may be *linked* to several review instances; it is not copied as each person’s private achievement.

### Bundle 3 — `evidence-attribution-and-quality`  
*Facet: recognition-observation (required).*

**Layer 3.1** `evidence-items-and-unit-of-analysis`  
- **F09 Evidence item.** Source party, method, URI/artifact pointer, observed interval, freshness, confidence, quality class (`owner-statement | attested-third-party | system-log | work-product | contested`).  
  *Questions:* What was observed, by whom, by what method, at what time, at what unit of analysis?  
  *Artifact:* Evidence item with RFC 3339 timestamp, provenance, quality tags.

- **F10 Prohibited-proxy handling.** Evidence typed as keystroke, always-on presence, webcam attention, emotion inference, or raw commit-count **may be linked as a work-product or system log** but cannot be the sole or automatic basis of an assessment outcome. SPACE treats Activity as one of five dimensions and the most commonly misused; productivity “cannot be measured by a single metric or dimension.” DORA four keys are software-delivery *team/system* measures.  
  *Invariant:* `unit_of_analysis ∈ {person, assignment, team, system, artifact}`. Team/system metrics used as a person rating without an attribution rule are incomplete records, not silent scores.  
  *Artifact:* Proxy-class flag + exclusion reason on the assessment act.

**Layer 3.2** `attribution-and-credit`  
- **F11 Multi-subject attribution.** N:N rows: artifact → parties, share or role (author | co-author | reviewer | incident-commander | unknown), confidence, `employment_ref` on each row.  
  *Invariant:* Dual employment requires an employment foreign key on every attribution row. Email domain is not identity.

- **F12 Credit dispute and conflicting evidence coexistence.** Dispute state on the attribution row. Conflicting evidence is retained, not collapsed.  
  *Artifact:* Attribution row set + dispute case pointer.

### Bundle 4 — `assessment-raters-and-scales`  
*Facet: capabilities-behaviour-actions (required for assessment acts).*

**Layer 4.1** `reviewer-assignment-and-decision-mode`  
- **F13 Rater assignment, panel, recusal.** Who may rate, on what authority, for which items, with conflict/recusal. Aligns with the *existence* of HR-XML EPMRaterPanel / EPMParticipant as interchange objects, not with an unfetched field list.  
  *Questions:* Is the rater the assignment supervisor, a host-org manager, a matrix lead, a peer, or a calibration-only rater? Which employment owns the rater’s authority?

- **F14 Decision mode.** `human | human-with-AI-assist | solely-automated`, plus `significant_effect_flag`. EU AI Act Annex III.4(b) names systems used to decide terms, promotion or termination, allocate tasks from behaviour/traits, or monitor and evaluate performance and behaviour. GDPR Art. 22 addresses *solely* automated decisions with legal or similarly significant effects.  
  *Invariant:* The model records mode. It does not implement a scorer and does not declare a use lawful.

**Layer 4.2** `rating-scale-version-and-application`  
- **F15 Versioned contextual rating scale.** `scale_id`, `version`, locale, context (job family, jurisdiction, cycle), anchors (label + definition), whether forced distribution is *declared*, `valid_from/valid_to`, `successor_scale_id`.  
  *Invariant:* No field `overall_employee_score` with unbounded validity. “Exceeds” on v3 is not “Exceeds” on v4.

- **F16 Rating application.** A rating is `(scale_id, scale_version, item_id, value, rater_role, valid_time, knowledge_time)`. Item may be an objective, a declared behavior, or a cycle-scoped overall *in this instrument*. SFIA level, if present, is a referenced capability claim with its own purpose, not this grade. ESCO URI may classify occupation context, never the grade.  
  *Artifact:* Rating application row. Closed reviews keep the scale version they used.

### Bundle 5 — `calibration-outcome-and-recognition`

**Layer 5.1** `calibration-act`  
- **F17 Calibration as a visible adjustment act.** Input rating, output rating, panel ref, criterion ref, quorum/notes, subject visibility of *own* outcome, appealability. Bol (2025) documents that calibration committees are strategic information environments, not neutral truth machines — which is why the act must be inspectable.  
  *Invariant:* Calibration that changes a rating without a before/after record is not representable as “the same rating.” Hidden forced ranking is a profile declaration, not an invisible rewrite.

**Layer 5.2** `outcome-and-recognition`  
- **F18 Cycle outcome.** Period-scoped result, optional in-cycle overall against the instrument’s scale version, links to development-plan *reference* (HR-XML DevelopmentPlan is a neighbor projection). RemunerationRecommendation, if aligned at all, is a **reference out**, not an executable pay object. HR-XML embeds it inside EPMResult; copying that shape would put a pay decision inside a model that must not auto-decide employment.

- **F19 Recognition event disjoint from rating.** Thanks, award, spot bonus, peer kudos reference the person and optionally an objective. They do not write F16.  
  *Artifact:* Recognition event (optional neighbor later; disjoint type now).

### Bundle 6 — `appeal-correction-and-disclosure`  
*Facet: context-evidence (required).*

**Layer 6.1** `appeal-and-correction`  
- **F20 Contest types.** Distinguish `FactCorrection` | `AttributionCorrection` | `OpinionContest` | `ProcessContest` | `ProxyExclusion`. GDPR Art. 16 is the right to rectification of inaccurate data and completion by supplementary statement. Manager *opinion* is not automatically “inaccurate” because the subject disagrees; the model must still attach the supplementary statement.  
  *Artifact:* Appeal case + subject supplementary statement.

- **F21 Correction supersession.** Prior assertion remains at knowledge-time T0; new assertion at T1 with actor, reason, and recipient-notification hook (Art. 19 *shape*, not a compliance claim). Silent rewrite is forbidden.

**Layer 6.2** `purpose-disclosure-and-portability`  
- **F22 Purpose-specific disclosure projection.** A projection is a derived artifact: which fields, which purpose, which audience, which legal-basis *declaration* (hook), expiry.  
  *Invariant:* Default join across purposes is refused.

- **F23 Employer-change portability versus originating-controller confidentiality.** On employment end, originating employer remains source of truth for that cycle’s master record. Destination employer receives only an authorised projection. No silent merge of grades into a portable talent score.

### Bundle 7 — `governance-profiles-and-agent-operations`

**Layer 7.1** `profile-jurisdiction-and-policy-hooks`  
- **F24 Adopting profile and hooks.** Profile ∈ {startup, international-enterprise, public-service-unreviewed, platform-work-unreviewed}. Retention, works-council notice, language, collective instrument: **hooks with declared basis**, never invented periods or rights.  
  *Artifact:* Profile declaration + open-hold list. Agent operations may draft and validate; they may not mark the instance canonical while holds remain.

**Layer 7.2** is reserved for interoperability projections (HR-XML EPM as *optional projection*, ISO 30414 as *org-level reporting neighbor*, not an individual score). No extra finding until those XSDs/texts are pinned.

**Five-facet coverage (inferred applicability):**

| Facet | Applicability |
|---|---|
| Identity and class | required (B1) |
| Direct properties | required for period, purpose, scale-version, decision-mode; physical fields n/a |
| Recognition and observation | required (B3) |
| Capabilities, behaviour, actions | required for lifecycle acts (B4–B6) |
| Context and evidence | required (B6–B7); provenance and time on every assertion |

---

## 3. Relations, cardinalities, time, source of truth, permissions

### 3.1 Cardinalities (inferred)

| From | To | Card. | Note |
|---|---|---|---|
| ReviewInstance | Person | 1 | subject; never owned |
| ReviewInstance | Employment | 0..n stored, **1 governing** | concurrent employments allowed |
| ReviewInstance | Assignment | 1..n | work actually assessed |
| ReviewInstance | Organization (governing entity) | 1 | may differ from payroll or host |
| ReviewInstance | Position | 0..1 | context only |
| ReviewInstance | RatingScaleVersion | 1 | frozen at close |
| ReviewInstance | ObjectiveItem | 0..n | plan may be empty only if profile allows continuous feedback-only |
| ObjectiveItem | EvidenceItem | 0..n | |
| EvidenceItem | AttributionRow | 1..n | multi-subject |
| AttributionRow | Employment | 0..1 | required when dual employment exists |
| ReviewInstance | AssessmentAct | 1..n | draft, submitted, calibrated, final |
| AssessmentAct | Rater (Person + PartyRole) | 1..n | |
| ReviewInstance | CalibrationAct | 0..1 | many reviews : one session possible |
| ReviewInstance | AppealCase | 0..n | |
| ReviewInstance | RecognitionEvent | 0..n | disjoint |
| ReviewInstance | DisclosureProjection | 0..n | purpose-tagged |
| CalibrationAct | ReviewInstance | 1..n | |

### 3.2 Time

Follow the neighbor pattern already used on Employment and Assignment: **valid time**, **asserted/effective time**, **knowledge time**. RFC 3339 with seconds and timezone.

- Valid time: the period the objective or rating claims to describe.  
- Knowledge time: when the assertion entered the record.  
- Correction does not move knowledge time of the prior row.  
- Scale version validity is independent of review validity.  
- Closed reviews are immutable except via supersession.

### 3.3 Source of truth

| Fact | Master | 017 stores |
|---|---|---|
| Who the person is | WM-PER-001 | ref |
| Whether they are employed, by whom | WM-ORG-005 | governing ref |
| What work they were bound to | WM-ORG-016 | refs |
| What the post requires | WM-ORG-004 | ref |
| Occupation/skill concept | ESCO / SFIA / local | URI + version |
| Rating instrument | RatingScaleVersion catalog | pinned version id |
| What was agreed as an objective | **017** | object |
| What evidence was offered and who claimed credit | **017** | objects |
| What rating was applied in this cycle | **017** | object |
| What calibration changed | **017** | act |
| What the subject contested | **017** | case |
| What may be shown to a later employer | **017 projection**, not the master | |

Adopting Dimension declares the operational master (HRIS, files, spreadsheet). The logical model stays format-independent.

### 3.4 Permission rules (inferred hooks, not a privacy code)

- Subject: read own objectives, evidence offered, own ratings, own calibration *outcome*, own appeal file, own supplementary statement. Not other employees’ ratings.  
- Assigned rater: read in-scope items for the assigned period; write draft ratings; no write to another rater’s signed act.  
- Calibration panel: read items in the session; write CalibrationAct; still cannot silently replace F16.  
- Appeal officer: read contested packet; write superseding assertion.  
- Receiving employer: only a projection with purpose `hiring-reference` or equivalent declared basis.  
- Analytics / ISO 30414 productivity reporting: aggregates with unit_of_analysis ≠ person, or anonymised. Individual cycle records are not HCRD metrics.  
- Agents: draft and validate; cannot mark canonical; cannot invent lawful bases; cannot auto-close a solely-automated significant-effect act without human-intervention pointer.

Every read, export, or purpose-change is an auditable event. Neighbors already treat access audit as a cross-cutting model; 017 should reference that pattern rather than invent a second audit log identity.

---

## 4. Startup versus international enterprise profiles

Same model. Different required bundles. Not two ontologies.

**Startup profile (inferred).**  
Required: one ReviewPeriod (often continuous or quarterly); lightweight objectives; evidence notes; single manager rater; subject comment; one 3–4 point contextual scale version; appeal to a named human (founder or HR-of-one); dual-employment *representability* even if unused; prohibition on commit/keystroke→grade automation.  
Optional / absent: calibration committee, 360 panel, works-council notice, multi-jurisdiction retention matrix, union observer, language variants. Recognition may be a disjoint note. Source of truth may be the operating tool; person and employment must still be referenced, even if those masters are spreadsheets.

**International enterprise profile (inferred).**  
Required: program instrument with legal entity, jurisdiction, language, and collective-instrument *reference*; reviewer assignment with recusal; multi-source evidence with quality class; versioned scales per job family/country; calibration act with quorum and notes; appeal route with an officer who is not the original rater; purpose-specific disclosure; retention-by-purpose as a hook; manager-change and employer-change (successor / TUPE-like) continuity of *pointers*, not of confidential free text. Governing entity, payroll entity, and host entity may differ (secondment, agency). Special-category data is not copied into the review. Works-council and employee-rep duties are references, not invented rights.

Neither profile may claim GDPR, AI Act, or labour-law compliance by having the fields.

---

## 5. Worked synthetic case

Generic public fiction. No real employee data.

**Identities.**  
Person **P** (WM-PER-001).  
Org **Northwind Labs** (WM-ORG-001) — Employment **E1** (WM-ORG-005), Assignment **A1** “Staff engineer, payments platform” (WM-ORG-016).  
Org **Cedar Analytics** (WM-ORG-001) — concurrent 0.2 FTE advisory Employment **E2**, Assignment **A2** “Advisor, open-source telemetry”.  
Shared work-product **W**: a public pull request plus design note used in both products.  
Manager **M1** (Northwind), Manager **M2** (Cedar), Peer **R** (Northwind), Calibration panel **C**, Appeal officer **Q**.

**Sequence.**

1. 2025-01-15 E1 active. 2025-03-01 E2 starts; dual employment declared; conflict note on A2.  
2. Objective **O1** under E1/A1: “Ship payments retry budget v2 by 2025-06-30.” Evidence plan: design doc, *system-level* incident count, customer-impact note. Commit volume is not in the plan.  
3. Objective **O2** under E2/A2: “Publish telemetry schema guidance.” Shares artifact W.  
4. 2025-07-10 M1 opens ReviewInstance **R1** (governing employment E1). Draft rates O1 “below target”, citing “low commit count in Q2” (F10 invalid as sole basis) and “W was Cedar’s work” (F11/F12 attribution conflict).  
5. Peer R files Recognition **K1** for P’s Northwind sev-1 response. K1 must not write the rating (F19).  
6. P files Appeal **C1**: (a) ProxyExclusion of commit count; (b) AttributionCorrection on W; attaches supplementary statement and a Cedar letter that W was co-authored.  
7. Conflicting evidence rows all remain: M1 commit-count log (unit=person, proxy-class=activity-count), P incident timeline (unit=system, quality=work-product), Cedar joint-authorship attestation (unit=artifact).  
8. Calibration **CAL1** changes draft “below” → “meets”, criterion “team activity metric is not an individual grade.” Before/after recorded. P may see own outcome, not others.  
9. Q accepts AttributionCorrection: W marked joint, 50/50, each row carrying E1 or E2. R1 superseded by **R1b**. Knowledge time of R1 preserved. Recipients of R1 notified via the Art. 19-shaped hook.  
10. 2025-10-01 E1 ends (resignation). Northwind retains R1/R1b master. P requests projection **PRJ1**: objective titles, final in-cycle ratings, P’s statement, joint-attribution flag. Excludes M1 free text about Cedar clients and raw telemetry.  
11. 2025-10-15 new Employment **E3** at Org **Harbor**. Harbor must not ingest Northwind free text. Harbor may accept PRJ1 only under purpose `hiring-reference` and a declared basis. Harbor starts new cycle objects. Northwind scale version does not continue.

If any of those rows cannot be instantiated, the draft specification is incomplete.

---

## 6. Strongest negative cases and unresolved issues

**N1 Object fusion.** One record that is the person, the employment, the assignment, the objective, the grade, the badge, and a lifelong talent score. Produces undeletable stigma and breaks neighbor identity.

**N2 Activity-as-worth.** Commits, lines, keystrokes, badge time, camera-on minutes used as EPMResult. Contradicts SPACE, the brief, and — if automated — sits inside AI Act Annex III.4(b) “monitor and evaluate performance and behaviour.”

**N3 Hidden calibration.** Committee changes the number; subject sees only the last number; no criterion. That is a second, unaccountable rater.

**N4 Purpose laundering.** Development review reused for layoff, visa, acquisition diligence, or next-employer reference with no new purpose tag.

**N5 Dual-employment leakage.** A’s packet contains B’s clients; the same PR is counted as delivery for both employers; git identity is treated as employment identity.

**N6 Credit collision without a contest object.** Joint artifact; one manager writes “sole owner”; the other author has nowhere to put a supplementary statement that survives.

**N7 Employer change as portable credit score.** Closed ratings travel with the person like a Schufa file. That is the Art. 22 risk surface. The opposite failure — destroying all history the worker is entitled to port — is also a failure.

**N8 Scale drift presented as trend.** “Improved from 3 to 4” across two incompatible instruments.

**N9 Solely automated significant effect.** Scoring function writes `final` and a downstream “recommend terminate” with no rater identity and no contest route.

**N10 Correction that erases history.** Art. 16 accuracy versus the forensic need to know what was asserted at T0. Neighbors already use bitemporal time; 017 must not regress.

**N11 Recognition write-through.** Kudos auto-mutates the period grade.

**N12 Team SPACE / DORA pasted onto one assignee.** Missing unit of analysis.

**N13 Host / agency / payroll split.** Rater in host; employment in agency; assignment has host. If the review does not declare which legal employer owns the record, disclosure and retention become undefined.

**N14 ISO 30414 back-propagation.** Organization-level productivity HCA used as individual stack-rank.

**N15 Competency collapse.** SFIA level or ESCO URI stored as the cycle grade. SFIA Foundation text distinguishes competency assessment from performance appraisals; PEMT is the skill of *managing* performance, levels 4–6, not a grade given to the worker.

### Unresolved issues that block canonical assurance

1. Catalogue body does not exist. This memo is a first specification proposal against a TODO card.  
2. Neighbor composition is not approved. WM-ORG-005 COMPOSE WM-ORG-016 is candidate. Parent=016 is a catalogue assertion, not an approved ledger edge.  
3. Official HR-XML EPM 3.3 XSD was not retrieved (member/community download). Field-level mapping is unverified. Third-party schema viewers are not the standard.  
4. ANSI/SHRM-09001-2012 was read from a third-party PDF host, not the ANSI store.  
5. ISO 30400:2022 term entries were not retrieved (paywalled). Do not invent ISO definitions of performance, competence, or objective.  
6. ISO 30414:2025 full metric formulae were not retrieved. Abstract/TOC only.  
7. No primary source defines a universal dual-employment credit protocol or a cross-employer portability schema.  
8. Retention cannot be published as a number. Assignment already records this as a policy hook; 017 must do the same.  
9. No jurisdiction-specific appeal statute is encoded — and must not be. At least one EU and one non-EU labour/privacy specialist pass is absent.  
10. No deterministic fixtures yet for dual employment, disputed artifact, invalid proxy, calibration, appeal, employer change.  
11. No second-provider review of this draft. Published ORG neighbors at `0.3.0-research.1` are themselves reviewable-drafts with open holds.  
12. AI Act Annex III high-risk *application timing* is politically mobile. Do not freeze a date in the model.  
13. Public-service, military, seafarer, domestic, child, platform, and collective-bargaining profiles are unreviewed — same hold family as Employment.

---

## 7. Primary source URLs and actual applicability

Verified links first. Inferred design is not a source.

1. **https://ver.cy/models/wm-org-017-performance-objective-review/** — Catalogue target. Confirms ID, parent WM-ORG-016, classifier, planned/TODO status, no YAML. Does not specify bundles.  
2. **https://ver.cy/models/wm-org-016-work-assignment/** — Listed parent. Time-bounded work binding. Assignment ≠ review. Privacy/retention already treated as hooks.  
3. **https://ver.cy/models/wm-org-005-employment/** — Neighbor. Dual employment, assignment realization links, status dispute — not period ratings. Holds: Membership split, COMPOSE 016 candidate, no certified HR-schema crosswalk.  
4. **https://ver.cy/model-agent-protocol.md** and **https://ver.cy/object-description-profile.yaml** — Whole-object five-facet gate, no invented physical fields, no claiming canonical on a draft.  
5. **https://www.hropenstandards.org/standards** — Names DevelopmentPlan, EPMParticipant, EPMRaterPanel, EPMResult, ObjectivesPlan, ObjectivesResult. Integration schema family. Not a fairness, evidence-quality, or appeal standard. XSDs not independently fetched.  
6. **https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/two-pillar-structure-esco** — Occupations pillar on ISCO-08; skills/competences pillar; URI concepts. Dictionary for matching and training, not a performance scale.  
7. **https://sfia-online.org/en/about-sfia/about-sfia-appendices/knowledge-skill-and-competency** — Knowledge ≠ skill ≠ competency. Competency requires live accountability and consistent outcomes. Time served is not competence.  
8. **https://sfia-online.org/en/sfia-9/skills/competency-assessment** — LEDA: competency assessment is distinct from performance appraisals.  
9. **https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/** and **https://dl.acm.org/doi/10.1145/3454122.3454124** — Forsgren, Storey, Maddila, Zimmermann, Houck, Butler, ACM Queue 19(1) 2021. Productivity is multi-dimensional; not only individual; not one metric. Does not define an HR review object.  
10. **https://www.iso.org/standard/86106.html** — ISO 30414:2025 HCRD. Organization-level reporting areas include productivity and skills/capabilities. Not an individual appraisal process. Full text paywalled.  
11. **https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679** — GDPR. Art. 5 purpose limitation, minimisation, accuracy, storage limitation. Art. 16 rectification and supplementary statement. Art. 22 solely automated decisions with legal or similarly significant effects. Jurisdiction-conditional. Recital 71 names performance-at-work as a profiling example.  
12. **https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689** — Regulation (EU) 2024/1689, Annex III point 4(a)(b). Employment/worker-management high-risk class includes monitoring and evaluating performance and behaviour, and decisions on terms, promotion, or termination. Art. 5 prohibits workplace emotion inference except medical/safety. The meta-model is not itself an AI system; an adopting Dimension that uses AI to draft or rank may be in scope.

**Secondary, use with caution.** CIPD factsheet and “Could do better?” evidence review (goal-setting and appraisal research; not a schema). ANSI/SHRM-09001-2012 via third-party PDF host (minimum elements for goals/review/PIP; competencies and compensation out of scope). DORA four keys (https://dora.dev/guides/dora-metrics-four-keys/) as team/system delivery metrics only. Locke and Latham 2002 (DOI 10.1037/0003-066X.57.9.705) for goal specificity, not for cascading annual theater. UK ICO employment-records guidance is UK practice, not EU law and not a data model.

---

## Conclusion

**Usable as a visibly reviewable draft: yes**, on four conditions that this memo already tries to meet:

- every structural choice is marked inferred;  
- neighbor identities are references, not copies;  
- rating scales are versioned and contextual, with no global intrinsic employee score;  
- commits, keystrokes, and other surveillance proxies cannot close an assessment, and employment decisions are not executable objects inside this model.

**What specifically blocks canonical assurance:**

the catalogue specification does not yet exist; official HR-XML field lists and ISO term/metric texts are unpinned; neighbor relation ledger edges are not approved; retention and appeal rights cannot be published as universal numbers or clauses; dual-employment / disputed-credit / employer-change fixtures do not exist as executable tests; no second-provider review and no specialist labour/privacy pass have been done; compliance with GDPR, the AI Act, SHRM, HR Open, SFIA, ESCO, or ISO would be a false claim if asserted from this text.

The honest next artifacts are: (i) a Dimension-scoped YAML that implements the seven bundles without pretending the XSDs were read, (ii) a fixture pack for the synthetic case in §5, (iii) a RatingScaleVersion mini-object split (S4), and (iv) a source-refetch hold list that names the gated files. Until those close, WM-ORG-017 should carry the same banner its neighbors already use: **research assurance, reviewable-draft, not canonical.**