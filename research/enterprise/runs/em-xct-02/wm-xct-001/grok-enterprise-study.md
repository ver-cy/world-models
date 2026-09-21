# EM-XCT-02 — Independent study: Fact ownership and accountability

**Contour:** Fact ownership and accountability  
**Date of study:** 2026-09-21  
**Stance:** External researcher. Not an approver. Synthetic examples only. No inference about actual organizations.  
**Evidence labels used below:** **[observed]** = present in the cited source; **[source-asserted]** = claim the source itself makes; **[inference/proposal]** = this study’s recommendation; **[unverified]** = not independently confirmed against normative text.

Sources were read on 2026-09-21. Vocabulary similarity is never treated as conformance.

| Source | Version / section | URL |
|---|---|---|
| WM-XCT-001 Ownership/Stewardship | 0.3.0-research.1, published 2026-08-23 | https://ver.cy/models/wm-xct-001-ownership-stewardship/spec.yaml |
| WM-XCT-002 Access/Contract/Consent | 0.3.0-research.1 | https://ver.cy/models/wm-xct-002-access-contract-consent/spec.yaml |
| WM-XCT-012 Provenance | 0.3.0-research.1 / 1.0-draft | https://ver.cy/models/wm-xct-012-provenance/spec.yaml |
| W3C PROV-DM | REC 30 April 2013 | https://www.w3.org/TR/prov-dm/ |
| W3C ODRL Information Model 2.2 | REC 15 February 2018 | https://www.w3.org/TR/odrl-model/ |
| NIST SP 800-162 | Jan 2014, updates 2019-02-25 / 2019-08-02; §§2.2, 2.4.2–2.4.3, 3.1.3.3 | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-162.pdf |
| Kubernetes Server-Side Apply | docs last modified 2026-03-15 | https://kubernetes.io/docs/reference/using-api/server-side-apply/ |
| OpenMetadata data ownership | v2.0.x | https://docs.open-metadata.org/v2.0.x/how-to-guides/guide-for-data-users/data-ownership |
| DataHub OwnershipType + typed owners | current public metamodel / 2026-05-11 blog | https://docs.datahub.com/docs/generated/metamodel/entities/ownershiptype |
| Wikidata Help:Ranking | current help page | https://www.wikidata.org/wiki/Help:Ranking |
| HL7 FHIR R5 Provenance | hl7.fhir.core#5.0.0 (generated 2023-03-26) | https://hl7.org/fhir/R5/provenance.html |
| SQL:2011 temporal (application time / system time / bitemporal) | standard feature description via public secondary expositions | https://wiki.postgresql.org/wiki/SQL2011Temporal |
| CRDT multi-value register vs LWW | public literature (Shapiro lineage; ACM CSUR 2024 survey) | https://doi.org/10.1145/3695249 |

---

## 1. Boundary, reuse, extend, and what MUST remain outside

### Decision (inference/proposal)

**Do not attach an “Enterprise Fact Authority” application profile to WM-XCT-001 as if fact authority were a control modality of a meta-object.** Reuse selected *patterns* from 001, 002 and 012. Introduce three *independently identified* types. Treat the companion evaluator as a reference decision function over trusted policy input, not as a production PEP.

This is a rejection of the provisional attach-point, not of the three-type vocabulary.

### Why the attach-point is a category error

WM-XCT-001 **[observed]** records *assertions of control over a referenced meta-object* in named modalities (legal title, beneficial interest, custody, administrative controllership, de-facto technical control). Its own finding `controllable-object-anchor` states that objects that are pure abstractions, aggregates without a canonical instance, or copies without a single authoritative instance are not controllable and must be flagged rather than silently given an owner.

A fact type — “the meaning of `employee.costCenter` for Company Nord in 2026” — is exactly such an abstraction. Packing FactAuthority into 001 as administrative control invites a modality code to stand in for three different questions 001 does not distinguish:

1. who owns the *meaning* of a predicate (glossary / fact-type governance);
2. which *system* is admissible and how it ranks for *values* of that predicate on a subject-class, in a company/scope, during an interval;
3. who is operationally accountable when two admitted sources disagree.

001 already **[observed]** excludes runtime authorization, general content lineage, party identity, and determination of legal validity. Adding mastership inside 001 either violates those exclusions or silently widens the mixin. Alignment is not conformance: 001’s own `interoperability-and-alignment` finding says so.

PROV-DM **[observed]** models Entity / Activity / Agent and the relations wasAttributedTo, wasAssociatedWith, actedOnBehalfOf. Attribution ascribes responsibility for an entity’s existence; delegation assigns authority to carry out an *activity* while the responsible agent retains some responsibility. PROV does not model ownership of meaning, source-of-truth precedence, or access control.

ODRL 2.2 **[observed]** models Policy, Permission, Prohibition, Duty, assigner, assignee, and a conflict term (`perm` / `prohibit` / `invalid`; default `invalid`). It does not decide whether the assigner owns the asset, whether the assigner may issue the policy, or what the asset’s fact-value is.

NIST SP 800-162 **[observed]** defines ABAC as evaluation of subject, object, operation and environment attributes against policy. It separates PAP (administration), PDP (decision), PEP (enforcement) and PIP (attribute retrieval). Attribute authorities are typically authoritative for *attribute type* (the example given is HR for Name attributes). That is closer to mastership of an *attribute source* than to object ownership, and it is still authorization machinery, not a fact store.

Product practice confirms the split. OpenMetadata **[source-asserted]** binds owner to “all operations on a data asset,” including bulk import. That owner→write collapse is the anti-pattern this contour must forbid. DataHub **[observed]** keeps typed owners (TECHNICAL_OWNER, BUSINESS_OWNER, DATA_STEWARD, custom OwnershipType entity) as a versioned *aspect* separate from policies and from system-of-record. Kubernetes SSA **[observed]** tracks field *managers*, not meaning-owners; force is a concurrency override, not authorization; Update (PUT) silently transfers management. Wikidata **[observed]** keeps rank distinct from references: a source can support a value that is still deprecated. FHIR R5 Provenance **[observed]** records who produced a resource version; `meta.lastUpdated` is not a source-of-truth declaration.

### What to reuse from the existing packages

From **001**, reuse as *referenced patterns*, not as subclass:

- four clocks (event / effective / observation-ingestion / record-write);
- stewardship does not imply beneficial holding (`steward-custodian-appointment`);
- delegation cannot exceed grantor powers (`delegation-mandate-scope`);
- mandate verification and split revocation/publication times;
- contestation retains competing claims (`competing-claims-and-dispute-status`);
- register competence is bounded (`register-authority-and-competence`);
- assignment identity is not the effective date (`control-record-identity-versioning`);
- lifecycle states that keep superseded records addressable;
- tombstoning rather than erasure of links.

From **002**, reuse grantor-authority-basis (unverified grant is void), fail-closed coverage, and the rule that a business role alone does not authorize runtime access. The authority record is an *object that 002 may grant read over*; 002 does not decide fact values.

From **012**, reuse assertion identity distinct from target, recorded time, supersession by new assertion rather than in-place edit, activity/agent/attribution, and the explicit stance that provenance is not truth and is not access permission.

### Definitions (inference/proposal; grounded in the above)

**Fact type / predicate.** A governed identifier for a meaning (“legal name of a natural person in employment context”), not a cell value and not a database column. Identity is independent of any system that stores instances.

**FactAuthority.** An identified, time-bounded governance record: for this company (or explicit scope), this fact-type family, this interval, *this party is accountable for the meaning and for the mastership policy*. It is not title to a meta-object, not write permission, not a source ranking.

**StewardshipAssignment.** An identified, time-bounded operational appointment: this party stewards *this* FactAuthority (or a stated sub-scope) under instruction limits, with a duty to receive contested routes. Stewardship is not beneficial holding and is not mastership.

**MastershipRule.** An identified, time-bounded, published rule: for this predicate, this subject-class, this company/scope, this effective interval, this source is admissible at this rank, with this effect on conflict (select / retain-loser / contest). Mastership is source *admissibility and precedence*, not authorization, not truth, not confidence.

**Fact assertion.** A 012-shaped record: assertion id ≠ subject id; value; source; effective interval; recorded-at; provenance refs. A source can be authorized to assert and still be wrong.

**Evaluator outcome.** One of `{selected, contested, unevaluable}`. Contested retains *both* provenance refs and routes to the live steward. Unevaluable is the closed default when authority, assignment or rule is missing, expired, unpublished, or out of competence.

### MUST remain outside

- Runtime authorization, PEP/PDP enforcement, tokens, session (002 + NIST ABAC).
- Party identity and legal-person determination (person/org models).
- Determination of legal validity of a claimed right (001 exclusion).
- Content lineage of the payload as a substitute for mastership (012).
- Epistemic confidence as a substitute for contestation or rank.
- Write permission derived from owner, steward, field-manager, or source rank.
- Model-maintainer / schema-author identity as instance FactAuthority.
- Physical custody, key management, replication (001 exclusion).
- Adjudication procedure; only dispute status and ingested outcome.
- A universal “fact owner” singleton per predicate for the whole world.

**Critical flaw, stated once:** an assignment deserves independent identity; source precedence is being confused with authorization if MastershipRule is coded as a 001 control modality or as an ODRL Permission. Those are different objects with different failure modes.

---

## 2. Minimum viable object / relationship schema

Three exported types. None is an aggregate part of another. Relations are references, not containment. Cardinality below is for the *operative* slice at one instant; history is append-only.

### FactAuthority

| Facet | Content |
|---|---|
| Identity / class | `factAuthorityId` (stable, not equal to effective-from). Class: governance record. Scope key: `(companyId, factTypeFamilyId, optional geographic/legal-unit qualifier)`. **[inference]** Do not require uniqueness of accountable party globally; two parties may *claim* authority — that claim is itself contestable. |
| Direct properties | `accountablePartyRef`, `basisRef` (instrument or register act), `competenceNote` (object-class / jurisdiction / modality bounds, from 001 register-authority), `validInterval`, `status` ∈ {proposed, effective, suspended, disputed, superseded, terminated}. |
| Recognition / observation | Recognised when a register with competence records it. Observed via `recordedAt` / `ingestedAt`. Absence of a record is not a negative fact. |
| Capabilities / actions | propose, activate, suspend, dispute, supersede, terminate, transfer-accountability. Cannot: grant runtime access, write instance facts, raise a source rank by existing. |
| Context / evidence | four clocks; evidence pack for basis; prior-belief snapshot on retroactive correction; sensitivity class on the *authority record* (ownership data is not inherently public — 001 `control-data-access-and-disclosure`). |

**Lifecycle.** Proposed → (pending conditions) → effective → {suspended | disputed} → {effective | superseded | terminated}. Superseded remains addressable. Transfer mints a *new* `factAuthorityId` (or a new version in an explicit lineage) and leaves the old one queryable as-of.

**Mastership relation.** A FactAuthority *governs* zero or more MastershipRules. It does not contain them.

**Sensitivity.** Authority and steward identity are personal or organizational data. Default deny on disclosure; 002 projection only.

### StewardshipAssignment

| Facet | Content |
|---|---|
| Identity / class | `assignmentId` independent of both party and authority. Class: bounded operational appointment. This naming is deliberate: products that collapse “stewardship” into a role label lose the assignment record (DataHub ownership *aspect*; Collibra resource-role-on-asset). |
| Direct properties | `authorityRef` (1), `stewardPartyRef` (1), `instructionLimits`, `dutySet`, `validInterval`, `status`, `routeAddress` (logical, not a mailbox that leaks). |
| Recognition / observation | Live only if `now ∈ validInterval`, parent FactAuthority is effective, and revocation publication time has not passed the reliance rule (001 `mandate-verification-revocation`). |
| Capabilities / actions | receive contest route, propose value change, propose rule change, request transfer. Cannot: exceed instructionLimits; appoint a successor beyond grantor powers; change rank of a source; become beneficial holder. |
| Context / evidence | appointment instrument; four clocks; delegation chain if the steward is itself a delegate (actedOnBehalfOf *shape*, not PROV conformance claim). |

**Cardinality.** 0..n assignments per FactAuthority; at most one *operative* assignment per `(authority, sub-scope)` at an instant unless the authority explicitly allows co-stewards. Co-stewards do not merge identities.

### MastershipRule

| Facet | Content |
|---|---|
| Identity / class | `ruleId` independent of authority. Class: source-admissibility / precedence rule. |
| Direct properties | `authorityRef`, `predicateId`, `subjectClass`, `companyScope`, `sourceId`, `rank` (total order *within this rule-set version*), `conflictEffect` ∈ {select-highest, contest-if-equal, retain-loser}, `validInterval` (fact-effective time), `publicationTime` (policy clock), `status`. |
| Recognition / observation | A rule is visible to the evaluator only if `policyAsOf ≥ publicationTime` and the rule is effective. Unpublished or future-published rules are invisible. |
| Capabilities / actions | admit or exclude an assertion source for selection. Cannot: authorize a write; assert a value; hide a contested loser; bind by request-time shopped scope. |
| Context / evidence | publishing party must be the live FactAuthority or a steward acting inside instructionLimits; publication proof; rule-set version pin. |

**Cardinality.** 0..n rules per `(authority, predicate, scope)`. Overlap is allowed and is the conflict surface of §4.

### Relationships (inference)

- FactAuthority 1 — *governs* → 0..n MastershipRule  
- FactAuthority 1 — *is-stewarded-by* → 0..n StewardshipAssignment  
- StewardshipAssignment *cannot exist* without `authorityRef` resolving to an identified FactAuthority (unknown authority is not a grant).  
- Fact assertion (012) *is-admitted-by* 0..1 selected MastershipRule at evaluation time; admission ≠ correctness.  
- TransferEvent references prior assignment/authority ids and does not rewrite them.

### What the schema refuses to encode as implication

`sourceRank ⇏ writePermission ⇏ factValue ⇏ confidence ⇏ disclosureGrant`. Four (plus disclosure) distinct fields. A late spreadsheet never becomes true by arriving last.

---

## 3. Question routes, unknown behavior, invariants

Routes are Finding → Question → Artifact → permitted Action. Unknown / missing artifact yields the stated closed behavior.

1. **Finding** `controllable-object-anchor` → **Q** Is a fact type a controllable meta-object? → **Artifact** FactAuthority (not a 001 holding) → **Action** mint FactAuthority; do *not* mint a control-record on the predicate. **Unknown:** treat as not-controllable; do not invent an owner.
2. **Finding** `steward-custodian-appointment` → **Q** Who operates this fact-type under instruction? → **StewardshipAssignment** → appoint / revoke. **Unknown:** no steward; contests are unevaluable-unroutable (queue on register, do not auto-approve).
3. **Finding** `delegation-mandate-scope` → **Q** May this steward sub-delegate contest handling? → mandate clause on the assignment → allow only if explicit and ≤ grantor powers. **Unknown:** no sub-delegation.
4. **Finding** `mandate-verification-revocation` → **Q** Is this assignment live at reliance instant T? → assignment + revocation publication time + reliance rule → rely or refuse. **Unknown revocation publication:** refuse reliance.
5. **Finding** `grantor-authority-basis` (002) → **Q** May party P publish a MastershipRule? → FactAuthority live at P + basis verification → publish or void-ab-initio. **Unknown basis:** void.
6. **Finding** `register-authority-and-competence` → **Q** Is this register competent for company C / fact-type F / jurisdiction J? → competence note → record as authoritative or evidentiary-only. **Unknown competence:** evidentiary-only; evaluator cannot select.
7. **Finding** `provenance-assertion-record-identity` (012) → **Q** What is the identity of this value claim? → assertion id + subject ref + recordedAt → retain; never key by import order. **Unknown assertion id:** reject admission.
8. **Finding** `temporal-semantics` (001 four clocks) → **Q** What was selected at fact-effective T, given policy published by T′? → bitemporal evaluation (§4) → return snapshot. **Unknown clocks:** unevaluable.
9. **Finding** `competing-claims-and-dispute-status` → **Q** Two equal-rank sources, different values, same subject/predicate/effective time? → both assertions + contest record → status=contested, route to live steward. **Unknown steward:** contested-unrouted; values still retained.
10. **Finding** `multi-grant-conflict` (002) → **Q** May a reader see the loser value? → 002 projection on the contest record → project status and/or values per grant. **Unknown grant:** default deny on values; do not drop the contest record.
11. **Finding** `control-record-lifecycle-states` → **Q** Is this authority operative? → status field → only `effective` participates in selection. **Unknown status:** treat as not operative.
12. **Finding** `interoperability-and-alignment` → **Q** Does using `prov:wasAttributedTo` make us PROV-conformant? → none → record alignment-with-loss; no conformance badge.
13. **Finding** model-maintainer-is-not-owner (acceptance) → **Q** May the Dimension author appoint themselves FactAuthority by editing the model? → role binding → reject. **Unknown role separation:** reject.
14. **Finding** `scope-clause-selection` (002) → **Q** Which company-scope binds the rule? → scope on the *fact*, not on the request → bind or fail-closed. **Unknown scope:** unevaluable (blocks policy shopping).
15. **Finding** transfer-preserves-history (acceptance + 001 `chain-of-title-reconstruction`) → **Q** Who was steward on 2025-03-01 after a 2026 transfer? → prior assignment id as-of → return historical steward and historical selected/contested set. **Unknown prior id:** admit a hole; do not interpolate.
16. **Finding** (product, DataHub MCP) late UPSERT → **Q** May ingestion without a mastership gate overwrite? → admission layer → reject if source rank < current selected, or contest if equal. **Unknown rank:** unevaluable, do not write selected value.

### Unknown behavior (closed)

Missing FactAuthority, expired assignment, unpublished rule, missing assertion id, missing clocks, out-of-competence register, unverified grantor → `unevaluable`. Never “Approved by default.” OpenMetadata’s **[source-asserted]** behavior that a glossary with no reviewers auto-approves new terms is a documented counterexample and is forbidden here.

### Executable invariants (≥8)

**INV-1 Equal-rank contest.** If two admitted sources have equal rank for `(subject, predicate, effectiveTime)` and unequal values, evaluator emits `contested`, retains both 012 assertion ids, routes to the assignment live at contest-time. Import order, `recordedAt`, filename, and transport timestamp are not in the selection key.

**INV-2 No last-write.** A later assertion from a lower or equal rank MUST NOT replace a higher-rank selected value. Spreadsheet after HRIS cannot win by arrival.

**INV-3 Facet separation.** FactValue, WritePermission, SourcePriority, EpistemicConfidence, DisclosureGrant are independent. Authorized-to-assert ⇏ true.

**INV-4 Unknown ≠ grant.** Missing / expired / unpublished / out-of-competence ⇒ no selection, no write of selected value, status=`unevaluable`.

**INV-5 Transfer retains answers.** Transfer at T mints new assignment/authority ids. Queries with as-of < T return prior steward and prior selected-or-contested set. Historical rows are not rewritten.

**INV-6 Maintainer ≠ instance owner.** Identity of the model/Dimension maintainer is not a FactAuthority basis.

**INV-7 Policy clock ≠ fact clock.** A MastershipRule participates in an evaluation only if `policyAsOf ≥ publicationTime`. Backdated `validInterval` without a prior publication does not rewrite past authenticated evaluations.

**INV-8 Delegation ceiling.** Assignment powers ⊆ live parent FactAuthority powers. Parent transfer, suspension or termination shrinks or extinguishes the assignment automatically.

**INV-9 Contested values survive filtering.** Access projection may hide a value from a reader; it MUST NOT delete the contest record or the loser assertion.

**INV-10 Apply-style admission.** Writes that change selected value or contest status require companion validation. A raw JSON PUT analog of Kubernetes Update is not a conforming write.

---

## 4. Precedence, conflict, time, and abuse surfaces

### Source precedence

A MastershipRule-set, pinned by version, defines a total order of sources *inside that pin* for a `(predicate, subjectClass, companyScope)` at a fact-effective instant. The evaluator:

1. collects assertions whose effective interval covers T;
2. drops sources the rule-set excludes;
3. if one unique highest rank remains with one value → `selected` (loser retained only if `retain-loser`);
4. if two or more highest-rank sources disagree → `contested`;
5. if no live rule-set or no FactAuthority → `unevaluable`.

This is closer to a Wikidata multi-statement store (retain, annotate) than to Kubernetes SSA (one live value, force takes the field) or to an LWW CRDT (timestamp discards). SSA **[observed]** is a conflict *detector* for field managers; co-ownership exists only when values already match; force discards the other manager. LWW **[observed]** keeps one value. A multi-value register **[observed]** keeps concurrent writes. The acceptance criterion is MV-register + explicit steward route, not LWW and not SSA-force.

ODRL conflict terms **[observed]** resolve Permission vs Prohibition on actions, defaulting to `invalid`. They are the right shape for “do not invent a winner,” the wrong object for fact values. Do not encode MastershipRule as an ODRL Permission.

### Equal-rank and overlapping rules

Equal rank + unequal value → contested (INV-1).  
Overlapping rules with *unequal* rank and *partial* scope intersection: **[unverified / deferred]** whether composition is most-specific-wins or fail-to-contested. Increment 1 must fail-to-contested (or unevaluable) on partial overlap rather than invent a lattice. That is the honest default; most-specific composition is a later profile.

Overlapping *authorities* (two FactAuthority records for the same company × fact-type) is itself a contest at the governance layer. Do not pick the one that arrived last.

### Temporal corrections, future and retroactive rules, replay, import

Four fact clocks from 001 plus a fifth *policy-publication* clock:

| Clock | Who sets it | Role |
|---|---|---|
| eventTime | world / source | when the underlying event happened |
| effectiveTime | source / steward | when the fact is claimed to hold |
| ingestedAt | register | when the assertion was observed |
| recordedAt | register | when the row was written |
| publicationTime | policy register | when the MastershipRule / appointment became citable |

SQL:2011 **[observed]** already separates application time (valid time) from system time (transaction time); both together are bitemporal. That pair is necessary and *insufficient*. A bitemporal snapshot answers “what did the store believe at system-time S about valid-time V?” It does not answer “which *authenticated policy pin* was in force at S?” Policy shopping and retroactive rule insertion attack the missing fifth clock.

**Corrections.** A wrong value is superseded by a new 012 assertion with `supersedesRef`. The old assertion remains. A wrong *rule* is superseded by a new rule with a new `publicationTime`. Replay of imports must re-evaluate against the *policy pin of the original evaluation*, not against today’s rules, unless the caller explicitly requests policy-as-of-now (and that request is authorized and audited).

**Future rules / appointments.** Valid-from in the future does not handle today’s contest (route to the assignment live *now*).

**Retroactive rules.** A rule published today with `validInterval` starting last year may affect evaluations whose `policyAsOf` is today. It must not silently mutate the authenticated result stored for last year’s close. Distinguish:

- *bitemporal snapshot* = store history;
- *authenticated policy publication* = signed/pinned rule-set version that an evaluation cites.

**Import admission.** Admission is a function of MastershipRule + assertion identity + clocks. Order in a file, worksheet tab, or Kafka offset is not a rank.

### Abuse surfaces

**Policy shopping.** An actor switches request-scope to a subsidiary whose rule-set ranks CSV equal to HRIS. Defence: bind scope from the *fact’s* company/scope, not from the caller’s chosen header. Ambiguous scope → unevaluable.

**Confused deputy.** An ingestion service may *assert* extracts from HRIS and still must not appoint stewards or raise ranks. Defence: separate capabilities on the three types (schema §2). The deputy’s identity appears on the 012 assertion as activity-agent, not as FactAuthority.

**Circular owner authority.** “I am FactAuthority because I published the MastershipRule that names me” or “I am FactAuthority because I maintain the Dimension.” Defence: FactAuthority basis must resolve to a register act *outside* the rule being published (bootstrap competence of the control/governance register — 001 `register-authority-and-competence`). Model maintainer identity is excluded by INV-6.

**Output information leakage.** A reader asks “is it contested?” Defence: 002 projection may return status without loser value, winner value, or steward personal identifiers. INV-9 forbids *deletion* of the contest; it does not grant *disclosure* of the contest payload.

PROV bundles **[observed]** can wrap the evaluation record so the decision itself has provenance. That wrap is evidence, not a permission. FHIR’s split of `occurred` vs `recorded` **[observed]** is the same clock discipline at resource level.

---

## 5. Synthetic fixtures, adversarial scenarios, binding vs companion

No HRIS/ERP is required for startup. Parties are named persons or named synthetic orgs. Sources are files with assertion ids.

### Startup fixture (minimum)

- Company: **Nord Studio** (single legal unit).  
- Parties: Ana (accountable), Ben (steward).  
- Fact type: `person.preferredName`.  
- Sources: `sheet-onboarding-v1` (rank 10), `manual-correction` (rank 10).  
- Objects: one FactAuthority (Ana, 2026-01-01..∞, published 2026-01-01), one StewardshipAssignment (Ben, same interval), two equal-rank MastershipRules.  
- Seed assertions: two rows for subject `emp-1`, predicate `person.preferredName`, effective 2026-09-01, values “Alex” vs “Alexandra”, distinct assertion ids.  
**Expected:** contested; both provenance refs retained; routed to Ben. Importing the sheet second does not win.

### International group fixture

- Group **HoldCo**, subsidiaries **Nord** and **Sud**, different registers, different publication times.  
- Predicate `employee.costCenter`.  
- Group rule-set pin `grp-2026.03`: HRIS rank 20, local-CSV rank 10.  
- Sud local pin `sud-2026.06`: HRIS rank 10, local-CSV rank 10 (equal).  
- Fact for employee of Nord, cost center effective 2026-04-15.  
**Expected:** group pin binds because fact.company = Nord; Sud pin is invisible. Switching the request header to Sud is policy shopping → fail closed if fact.company is Nord.

### AI / software organization fixture

- Synthetic org **Toolwright**.  
- Predicates: `service.slo.target`, `model.trainingCutoff`, `repo.defaultOwner`.  
- Sources: Git default CODEOWNERS file (rank 10), service catalog (rank 20), model card YAML (rank 20 for `model.*` only).  
- FactAuthority for `model.*` is the model-governance cell, not the Git org owners file, not the platform team that maintains the Vercy Dimension.  
**Expected:** a late CODEOWNERS change does not overwrite `model.trainingCutoff`. A platform engineer who can edit the schema cannot appoint themselves FactAuthority for training-cutoff.

### Adversarial scenarios (≥10) and expected results

| ID | Attack | Expected |
|---|---|---|
| A1 | Late CSV vs HRIS, same subject/predicate/effective time | If rank(HRIS)>rank(CSV): selected=HRIS, CSV retained if retain-loser, never silent overwrite. If equal: contested + route. |
| A2 | Raw JSON PUT bypasses evaluator (K8s Update analog) | Admission layer rejects. Native binding alone cannot change selected/contested. |
| A3 | Dimension maintainer self-appoints FactAuthority | Reject. Maintainer ≠ instance owner. |
| A4 | Request shops subsidiary pin | Bind by fact scope; shopped header ignored; ambiguous → unevaluable. |
| A5 | Ingestion service raises its own source rank | Reject. Deputy may assert, not govern. |
| A6 | Rule backdated one year, published today | Affects evaluations with policyAsOf ≥ publicationTime only. Prior authenticated closes unchanged. |
| A7 | Reader without disclosure grant receives loser value + steward email | Status may project; values and personal identifiers must not. Contest record remains stored. |
| A8 | Future-dated steward; contest today | Route to assignment live *now*; if none, contested-unrouted. |
| A9 | Two FactAuthority claims for same company × fact-type | Governance-layer contest; evaluator unevaluable for instance selection until resolved or explicitly dual-routed. |
| A10 | Equal-rank pair; access filter drops loser | Forbidden. Filter may hide; store keeps both assertion ids. |
| A11 | Delegation wider than parent | Reject at write of assignment (INV-8). |
| A12 | Replay last year’s import under today’s equal-rank CSV rule | Replay cites last year’s policy pin; does not flip last year’s selected value. |

### Native JSON-record binding vs companion validation

**Minimum native binding** is a projection: JSON objects with the identifiers and fields in §2, plus 012 assertion envelopes. It is suitable for interchange and for *reading* a pinned snapshot.

**Companion validation is mandatory** for any write that could change selected value, contest status, authority, assignment, or rule. Reasons, all observed analogically:

- DataHub MCP default write is UPSERT; optimistic concurrency is opt-in — late jobs without a header are LWW.  
- Kubernetes Update does not fail on managed-field conflict; Apply does.  
- 002 treats unverified grants as void *only if* verification runs.  
- 012 treats provenance as evidence, not as an enforcement engine.

The evaluator is a deterministic function:

`evaluate(assertions, rulePin, authoritySlice, assignmentSlice, factEffectiveT, policyAsOf) → {status, selected?, contested[], routeTo?, unevaluableReason?}`

It is not an authenticated PEP. Production enforcement, if any, lives behind 002 and an identity layer this contour does not define.

---

## 6. Migration, pins, holds, tradeoffs, first increment

### Migration / rollback

- New types are additive. Do not migrate 001 holdings into FactAuthority.  
- Existing catalog “owners” (OpenMetadata-style or DataHub-typed) import as *StewardshipAssignment candidates* or as *typed party annotations*, never as MastershipRule and never as write grants.  
- Rollback = pin the previous rule-set version and previous assignment ids; do not delete rows. Tombstone terminated authorities.  
- Evaluations already emitted keep their cited `rulePin` and assertion ids so rollback does not rewrite history.

### Immutable version pins

Every evaluation cites `ruleSetVersion`, `authorityLineageVersion`, `evaluatorSemver`. Pins are immutable. A “fix” is a new pin. This is the authenticated policy publication object that bitemporal tables do not give you for free.

### Unresolved research holds

- Unread paywalled ISO text already held on 001 (ISO 19152-1:2024, ISO/IEC 27002:2022, ISO 19115-1) plus unread ISO 8000 / 22745 master-data quality text. No claim about those clauses.  
- Legal-source alignment of “accountable party” with any jurisdiction’s controller / information-owner statutes: out of scope (001 already excludes legal validity).  
- Predicate identity: SKOS concept vs Vercy fact-type id vs glossary term URN — not decided. Increment 1 uses an opaque `predicateId`.  
- Composition of overlapping MastershipRules with unequal rank and partial scope intersection.  
- Untested broad domain profiles (the 001 hold stands).  
- Whether contested *authority* (A9) should block instance evaluation or dual-route: increment 1 blocks.  
- Multi-register competence graphs across HoldCo / Nord / Sud.  
- Automated agents as FactAuthority or steward (001 excludes automated agents as holders; keep that hold).

### Principal design tradeoffs

| Choice | Cost of the other pole |
|---|---|
| Independent assignment identity vs aggregate parts | Aggregates cannot transfer with provenance or support two live stewards. |
| Sibling contour referencing 001 vs application profile of 001 | Profile silently widens 001 and treats a predicate as a controllable object, against `controllable-object-anchor`. |
| MV-contest vs LWW / SSA-force | LWW and force destroy the acceptance criterion (equal-authority retain). |
| Fail-to-contested on overlap vs most-specific lattice | Lattice is implementable later; inventing it now is hidden policy. |
| Mandatory companion vs “JSON is enough” | JSON-enough reproduces DataHub UPSERT and K8s Update last-write. |
| Fifth policy clock vs pure bitemporal | Pure bitemporal cannot stop retroactive rule insertion from rewriting authenticated closes. |

### Bounded first implementable increment

Ship only:

1. Three identified types with the fields in §2.  
2. Evaluator function implementing INV-1, INV-2, INV-3, INV-4, INV-7, INV-10 on a single-company scope.  
3. Startup fixture + A1, A2, A3, A10 as executable tests.  
4. Native JSON projection + mandatory companion on writes that change selected/contested.  
5. Version pins on rule-sets.

Candid deferrals: international competence graph, most-specific overlap lattice, 002-backed disclosure projections beyond a single sensitivity flag, transfer UI, legal-effect, SKOS binding, any PEP, any claim of PROV/ODRL/ABAC/SSA conformance, any HRIS connector.

That increment already answers the acceptance bar: two equally authoritative sources, different values, same subject/predicate/effective time → contested, both provenance refs retained, routed to the live steward; import order is not truth; a late spreadsheet cannot overwrite a higher-rank source; the model maintainer is not the fact owner; rules act in time; unknown authority is not a grant; value, write permission, rank and confidence stay distinct; authorized-to-assert can still be wrong; disputed values do not vanish because a reader lacks a grant.

The provisional idea that these three types “might be aggregate parts rather than three global models” should be rejected for increment 1. If a later profile wants a document-composition view, it can *project* the three identified records into one envelope. It must not make the envelope the identity.
