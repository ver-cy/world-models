# EM-XCT-02: Enterprise Fact Authority — independent study

**Researcher stance:** I reviewed this from outside and am not approving it. All examples are made up. I ran no code and changed no files.
**Evidence labels:** **[O]** I read it this session (2026-09-21), through a summarizing fetch tool, so exact wording is not guaranteed. **[S]** The source claims it, and I did not test the claim. **[I]** My inference or proposal. **[U]** From memory or not checked this session.

---

## 0. Sources consulted

| # | Source | Version / section / date | Label |
|---|---|---|---|
| S1 | https://ver.cy/models/wm-xct-001-ownership-stewardship/spec.yaml | 0.3.0-research.1, generated 2026-08-23. Finding IDs `steward-custodian-appointment`, `delegation-mandate-scope`, `mandate-verification-revocation`, `temporal-semantics`, `control-record-lifecycle-states` (includes a *Disputed* state), `register-authority-and-competence`, `control-data-access-and-disclosure` | [O]. **Discrepancy:** the summary I got listed four bundle headings, but your brief says six. I cannot tell whether the summarizer lost detail or the brief is out of date, so this is unresolved. |
| S2 | https://ver.cy/models/wm-xct-002-access-contract-consent/spec.yaml | 0.3.0-research.1. `grantor-authority-basis` says a grant without verified authority is void. `multi-grant-conflict` names the problem but does not specify a combining algorithm. **It excludes write/modify/delete permissions.** | [O] |
| S3 | https://ver.cy/models/wm-xct-012-provenance/spec.yaml | 0.3.0-research.1. Assertion id 1..1, subject 1..n, recorded time 1..1, supersedes 0..n. Excludes access-policy definition. | [O] |
| S4 | W3C PROV-DM, https://www.w3.org/TR/prov-dm/ | Rec 2013-04-30. §5.3.2 attribution, §5.3.4 delegation, §5.1.8 invalidation, §5.4 bundles, §5.5 alternate/specialization | [O]. Several provenance descriptions of one entity may coexist. PROV does not decide truth. |
| S5 | W3C ODRL Information Model 2.2, https://www.w3.org/TR/odrl-model/ | Rec 2018-02-15. §2.10 conflict ∈ {perm, prohibit, invalid}, default **invalid**. §2.9 inheritance "MUST NOT be circular". §2.3.1 assigner/assignee | [O] |
| S6 | NIST SP 800-162, https://csrc.nist.gov/pubs/sp/800/162/upd2/final | Jan 2014, update 2019-08-02 | Abstract [O]. What it says about attribute authorities and attribute trust is [U]: I did not read the PDF. |
| S7 | Kubernetes Server-Side Apply, https://kubernetes.io/docs/reference/using-api/server-side-apply/ | Page as of 2026-09-21. GA since v1.22 [S] | [O] |
| S8 | DataHub ownership types, https://docs.datahub.com/docs/ownership/ownership-types and https://docs.datahub.com/docs/api/tutorials/owners | Current docs | [O]. Neither page covers ownership provenance or ingestion-vs-UI conflicts. |
| S9 | OpenMetadata data ownership, https://docs.open-metadata.org/latest/how-to-guides/guide-for-data-users/data-ownership, and connector YAML docs (e.g. https://docs.open-metadata.org/latest/connectors/database/redshift/yaml) | "latest" as of 2026-09-21 | [O]. Search-result summary, pages not opened. |
| S10 | Informatica Multidomain MDM trust settings, https://docs.informatica.com/master-data-management/multidomain-mdm/10-4-hotfix-1/configuration-guide/part-4--configuring-the-data-flow/mdm-hub-processes/load-process/trust-settings-and-validation-rules/trust-settings.html | 10.4 HF1 | Search-result summary only [O]. |
| S11 | Dehghani, "Data Mesh Principles", https://martinfowler.com/articles/data-mesh-principles.html | 2020-12-03 | [O] |
| S12 | XTDB key concepts, https://docs.xtdb.com/concepts/key-concepts.html | 2.x docs | [O] |
| S13 | SQL:2011 application-time and system-versioned tables | ISO/IEC 9075-2:2011 | [U]. Paywalled and not read. |

---

## 1. Boundary decision

### 1.1 Decision [I]

I agree that this should be an **application profile of WM-XCT-001**, not a new universal model. The profile has to be split along two lines the draft currently blurs:

1. **Definition authority vs. value authority.** Owning the *meaning* of a fact type ("what counts as `employment.start_date`") is different from being accountable for the *instance values* within one company scope. Group HR can own the definition while each subsidiary owns its values. A single `FactAuthority` type must carry an explicit `governs ∈ {definition, values}`, or it will merge the two.
2. **Epistemic precedence vs. write authorization.** This is the most serious flaw in the proposal. "MastershipRule" answers one question: given admitted assertions, which one does the register *select* under policy P? It does **not** answer "may system X write?" Using the word "master" invites the MDM reading, where master means "the system allowed to overwrite", and that reading is how last-writer-wins returns (see §4.1). I recommend renaming it **`PrecedenceRule`** and adding a separate **`SourceAdmission`** (which sources' assertions are *eligible for consideration* for a scope). Neither of them grants write permission.

**Critical gap:** "who may propose or change" a fact has no home. S2 excludes write/modify/delete permissions [O], and S1 excludes runtime authorization [O]. So the requirement is currently orphaned. The profile can *record* a `ChangeRight` (who may *submit a proposal*, which becomes an assertion), but enforcing it needs either a scope amendment to WM-XCT-002 or a new contour. I list this as hold H1 and do not solve it quietly inside the profile.

### 1.2 Assignments deserve independent identity [I]

Treating FactAuthority and Stewardship as properties *embedded* in a fact-type record would be a mistake. An appointment is itself a contestable, time-bound assertion. It can be transferred, revoked or disputed, and a decision record must be able to cite the exact appointment version that applied. So:

- **FactAuthority and Stewardship are independent records** with their own IDs. Each is a specialization of the S1 `steward-custodian-appointment` / `delegation-mandate-scope` patterns.
- **PrecedenceRule and SourceAdmission are policy records**, not assignments. They get their own IDs too, because the evaluator must pin them.
- The **meta-fact problem:** "Party A holds value authority over predicate P in scope S" is a fact, so who has authority over it? That regress must end at an explicit **`AuthorityAnchor`**: a bootstrap record accepted as trusted input and published through an authenticated channel. It must never end at a record that authorizes itself. ODRL's "inheritance MUST NOT be circular" (S5 §2.9) is the nearest standard analogue [O]. The anchor is my extension.

### 1.3 Definitions [I]

- **Fact predicate:** a registry-defined property type. It is referenced here and never defined here.
- **Assertion:** a WM-XCT-012 record claiming that subject *s* has value *v* for predicate *p* over valid interval *I*, attributed to a source agent. **Being authorized to assert does not make an assertion true.**
- **FactAuthority:** the accountable party for a predicate's definition or values within a scope and interval.
- **Stewardship:** a bounded operational responsibility (triage contests, run corrections, keep sources current) that an authority delegates. It confers no holding and no authority over definitions.
- **SourceAdmission:** makes a source's assertions eligible for a (predicate, scope, interval).
- **PrecedenceRule:** a partial order of admitted sources for a (predicate, scope, interval), together with fallback and staleness behavior.
- **ResolutionOutcome:** the output of the reference evaluator. It says "selected under pinned policy". It is **not** a truth claim and **not** an authorization.
- **Adjudication:** an authority's explicit, attributed decision that settles a contest by citing every contested assertion.

### 1.4 What must remain outside

Runtime authorization enforcement (WM-XCT-002 or infrastructure). Party identity and subject entity resolution. Predicate definitions and cardinality (the registry). Legal validity of appointments (S1 exclusion). Confidence and quality scoring algorithms. Lineage (WM-XCT-012). Adjudication *procedure*: only its outcome record is in scope. Cryptographic publication mechanics: referenced, not modeled.

---

## 2. Minimum viable schema

All records share an **envelope** [I]: `id` (URN, immutable), `record_version`, `profile_pin` (`efa@x.y.z`), `base_pin` (`wm-xct-001@0.3.0-research.1`), `company_dimension_id`, `recorded_at` (system time, RFC 3339), `valid_from` / `valid_to` (half-open, and `valid_to` may be open), `basis_event_at` (the S1 basis clock), `staleness_ceiling` (the S1 clock), `supersedes[]`, `evidence_refs[]` (≥1, WM-XCT-012 assertion IDs), `lifecycle`, `sensitivity`.

**Lifecycle** reuses the S1 states [O]: `pending → active → suspended → transferred | discharged`, plus `disputed`. Every transition is an appended record, never an in-place edit. **Sensitivity** is one of `public | internal | restricted | confidential`. It governs how the *record* is disclosed, **not** whether contest *status* is disclosed (see I8).

**Scope** is `{company_dimension_id, predicate_id, subject_selector, jurisdiction?, org_unit?}`. `subject_selector` must be an enumerated set or a registry-evaluable expression, with a specificity floor that reuses the S2 `scope-clause-selection` idea.

### 2.1 Exported types and the five facets

**AuthorityAnchor** (cardinality: one active per company_dimension per interval)
- *Identity/class:* `efa:AuthorityAnchor`, a root of the governance chain.
- *Direct properties:* `anchor_party_ref`, `governs_scopes[]`, `publication_ref` (digest plus signature reference).
- *Recognition:* accepted only if `publication_ref` verifies against the trusted publication channel. The evaluator treats it as trusted input and does not check it.
- *Capabilities:* may appoint FactAuthorities. Cannot assert fact values.
- *Context/evidence:* charter or board-resolution evidence reference (synthetic in fixtures).

**FactAuthority** (0..n per scope-interval, but at most one *accountable* party per `(governs, scope, instant)`; overlaps are an error)
- *Identity:* `efa:FactAuthority`, specializing `steward-custodian-appointment`.
- *Properties:* `party_ref`, `governs ∈ {definition, values}`, `scope`, `granted_by` (a FactAuthority or AuthorityAnchor id), `may_delegate: bool`.
- *Recognition:* active iff the chain to an anchor is acyclic, every link is active at the query instant, and scope and interval ⊆ the grantor's (reusing `delegation-mandate-scope`).
- *Capabilities:* appoint Stewardship, publish SourceAdmission and PrecedenceRule (values authority) or predicate-definition changes (definition authority), issue Adjudication, transfer.
- *Context:* appointment evidence and revocation-registry reference (`mandate-verification-revocation`).

**Stewardship** (0..n per scope)
- *Identity:* `efa:Stewardship`, specializing `delegation-mandate-scope`.
- *Properties:* `steward_party_ref`, `granted_by` (FactAuthority id), `duties ⊆ {triage_contest, propose_correction, maintain_admission, notify}`, `scope`, `routing_priority`.
- *Recognition:* active iff the grantor is active and the scope ⊆ grantor scope.
- *Capabilities:* receives contest routes and may *propose* an Adjudication. **May not issue an Adjudication** unless the grantor explicitly delegated `adjudicate`, and that grant is itself a recorded FactAuthority sub-grant.
- *Context:* appointment evidence and end-of-term disposition (S1).

**SourceAdmission** (0..n per scope)
- *Identity:* `efa:SourceAdmission`.
- *Properties:* `source_ref` (the source system or agent, *not* the importing pipeline), `scope`, `admitted_by` (FactAuthority), `assertion_semantics ∈ {event, snapshot}`, `authentication_requirement_ref`.
- *Recognition:* an assertion is eligible iff its *attributed source agent* (PROV `wasAttributedTo`, S4 §5.3.2) matches an active admission at the assertion's valid time **and** at the evaluation's system time.
- *Capabilities:* none. It is a filter.
- *Context:* admission rationale evidence.

**PrecedenceRule** (0..n, at most one per exact scope specificity per instant)
- *Identity:* `efa:PrecedenceRule`, not an assignment.
- *Properties:* `scope`, `tiers: [[source_ref...], ...]` (a partial order where sources in the same inner list are *equal rank*), `fallback ∈ {none, next_tier}`, `staleness_policy ∈ {ineligible, flag}`, `specificity` (derived, not declared), `published_by` (FactAuthority), `publication_ref`.
- *Recognition:* applicable iff the scope matches, the valid time ∈ interval, and publication is verified.
- *Capabilities:* none. It is input to the evaluator.
- *Context:* change-justification evidence.

**Adjudication** (0..n per contest)
- *Properties:* `resolves: [assertion ids]` (must include **all** contested assertions), `selected_assertion` or `selected_value` (an adjudicated value is itself a new assertion attributed to the authority), `issued_by`, `valid interval`.
- Recognition requires the issuer to be an active value authority for the scope at `recorded_at`.

**ResolutionOutcome** (a non-authoritative evaluator output, stored as a WM-XCT-012 activity output)
- *Properties:* `question` (subject, predicate, valid_at, as_of_system), `status ∈ {selected, corroborated, contested, adjudicated, no_admissible_source, stale, unknown_authority, rule_conflict, withheld}`, `value?`, `contributing_assertions[]` (possibly redacted to count plus opaque handles), `route_to[]` (stewardship ids), `policy_pins` (digests of every anchor, authority, admission and rule used), `evaluator_version`.
- *Capabilities:* none. It must never be consumed as a grant.

**Transfer** reuses the S1 transfer/succession bundle: `from`, `to`, `effective_at`, `evidence`, `carries_open_contests: bool` (default true). The old FactAuthority moves to `transferred` with `valid_to = effective_at`. It is not deleted.

**Kept deliberately separate:** *value* lives in the Assertion. *Write/propose permission* is the external ChangeRight (H1). *Source priority* is the PrecedenceRule. *Confidence* is an optional assertion annotation that **v1 selection never reads**.

---

## 3. Question routes, unknown behavior, invariants

### 3.1 Routes (Finding → Question → Artifact → permitted Action)

| # | Finding | Question | Artifact | Permitted action |
|---|---|---|---|---|
| R1 | efa-definition-authority | Who owns the meaning of predicate P in company C at time t? | FactAuthority(governs=definition) | Read; route definition change requests |
| R2 | efa-value-authority | Who is accountable for values of P for subjects in scope S at t? | FactAuthority(governs=values) | Read; escalate |
| R3 | steward-custodian-appointment | Whom do I notify about a contest on P/S? | Stewardship | Route; steward may propose |
| R4 | efa-precedence | What value is selected for (s, P, valid t, as-of T)? | ResolutionOutcome | Display with status; never treat as authorization |
| R5 | efa-equal-rank-contest | Why is the value contested? | Outcome plus contributing assertions | Steward triage; authority adjudicates |
| R6 | efa-source-admission | Is source X eligible for P/S at t? | SourceAdmission | Read; authority may admit or revoke (append) |
| R7 | efa-rule-overlap | Which rule applies when two scopes overlap? | Rules plus specificity computation | Evaluate; if tied, `rule_conflict` goes to authority |
| R8 | temporal-semantics | What would we have answered on date T? | Outcome with `as_of_system=T` | Replay only |
| R9 | efa-transfer-provenance | Who was accountable for P/S on a past date? | Transfer plus historical FactAuthority | Read |
| R10 | mandate-verification-revocation | Was the steward's action taken before revocation? | Stewardship lifecycle log | Validate the pre-revocation act |
| R11 | efa-unknown-authority | Nobody is recorded for P/S. Who decides? | Outcome `unknown_authority` | Route to the anchor holder. **No default grant.** |
| R12 | efa-model-maintainer | Does the registry maintainer of model P own company values? | Absence of a FactAuthority | Answer "no" unless one is explicitly recorded |
| R13 | control-data-access-and-disclosure | Can I see the value if I cannot see all sources? | Outcome `withheld` / `contested` (redacted) | Show status; request elevated view |
| R14 | efa-retroactive-rule | A rule was published today with valid_from last quarter. What changes? | New rule plus old decision pins | Re-evaluate for current knowledge; old outcomes stay attributed |
| R15 | efa-import-admission | A spreadsheet arrived with 400 rows. Do they count? | Admission check per row | Record as assertions. Eligible only if admitted. Never overwrites. |
| R16 | efa-bootstrap-anchor | Startup has no HRIS. Who is authority? | AuthorityAnchor (founder) | Anchor appoints; spreadsheet admitted as tier 1 |
| R17 | efa-adjudication | Who settled a contest and on what evidence? | Adjudication | Read; contest the adjudication (new assertion) |
| R18 | efa-stale | Is the HRIS value still current? | Outcome `stale` | Steward refresh request |

### 3.2 Unknown behavior [I]

Missing records mean "unknown". They never mean "allowed". No FactAuthority gives `unknown_authority`. No applicable rule gives `unknown_authority` for precedence (the evaluator must not invent a default order). An unrecognized source gives an ineligible assertion that is still retained and listed. A missing valid time on an assertion makes it ineligible. An unresolvable subject identity (two IDs possibly the same person) gives no contest detection across them, flagged as H4.

### 3.3 Executable invariants (≥8)

- **I1 Permutation invariance:** `eval(Q, A) == eval(Q, permute(A))` for all permutations of the assertion set.
- **I2 Equal-rank contest:** if the highest eligible tier holds ≥2 eligible assertions with distinct values for the same (s, P, overlapping valid t), then status is `contested`, all of their IDs are in `contributing_assertions`, and `route_to` is non-empty or status escalates to `unknown_authority`.
- **I3 No recency tiebreak:** `recorded_at` may only order assertions *from the same source* that are linked by `supersedes` or declared `snapshot` semantics. It never orders assertions across sources.
- **I4 Acyclic grounded authority:** every active FactAuthority has a `granted_by` chain that reaches an active AuthorityAnchor without repeating a node.
- **I5 Containment:** for every grant, `scope ⊆ grantor.scope`, `interval ⊆ grantor.interval`, and `grantor.may_delegate = true` (from S1 `delegation-mandate-scope`).
- **I6 Unknown is not a grant:** status `selected` requires an applicable PrecedenceRule and at least one eligible assertion. Otherwise the status is one of the unknown or empty statuses.
- **I7 Replay stability:** for `as_of_system = T < now`, the outcome is unchanged by any record with `recorded_at > T`.
- **I8 No silent disappearance:** if any contributing assertion is hidden from the caller, the status must not be `selected` with a value computed from the visible subset. The status becomes `withheld`, or `contested` with a redacted count.
- **I9 Maintainer ≠ owner:** a registry-maintainer role never satisfies the FactAuthority recognition test.
- **I10 Rule tie:** two applicable rules with equal computed specificity and non-identical tiers give `rule_conflict`.
- **I11 Facet separation:** no field of PrecedenceRule may reference confidence, and no field of ResolutionOutcome may be consumed as a permission. Enforce this by schema (`additionalProperties: false`) and by a lint on consumers.
- **I12 Transfer preserves history:** after a Transfer at `t`, R2 for valid time `< t` returns the prior party, including under replay.
- **I13 Adjudication completeness:** an Adjudication whose `resolves` omits any currently contested assertion is invalid.

---

## 4. Precedence, conflicts, time and attacks

### 4.1 Why practice supports "contested" and warns against "last wins"

- **Kubernetes SSA** (S7) [O] tracks field-level managers. Two managers applying the *same* value become shared owners. A *different* value from another manager is rejected as a conflict unless `force=true`, which **removes the other manager's claim**. Forcing needs only ordinary update rights, with no extra RBAC. It also has an "Update" path that skips conflict detection. Lessons [I]: (a) the corroboration concept is useful and maps to `corroborated`; (b) *force erases the loser's claim*, which violates the acceptance requirement, so Vercy's override must be an Adjudication that **cites** both claims; (c) SSA ties the right to override to write permission, which is exactly the conflation the profile must avoid; (d) SSA manages *desired state*, not claims about the world, so it is analogous but not a model to conform to.
- **Informatica MDM** (S10) [O via search summary]: if trust is not defined for a column, the column holds the value from the system that updated it most recently. Trust also decays with age. A secondary summary [O, not primary] says ties go to the most recent update. This is precisely the "late spreadsheet overwrites HRIS" failure, shipped as a **default**. Decay also mixes epistemic confidence into precedence. v1 should keep them apart (I11), and staleness should be a separate eligibility gate.
- **OpenMetadata** (S9) [O]: owners propagate top-down only when unset. Connector option `includeOwners` does not overwrite existing owners, but `overrideMetadata=true` makes the source overwrite owner, description and tags. Lesson: the behavior is a per-pipeline switch, so the *importer's configuration* decides who wins. That is policy shopping by configuration. Ownership here also means catalog ownership of assets, not value authority over facts.
- **DataHub** (S8) [O]: custom ownership types exist, and assigning owners needs an "Edit Owners" privilege. The pages I read do not document ownership provenance or ingestion-vs-UI conflicts. I infer nothing beyond that absence.
- **ODRL 2.2** (S5 §2.10) [O]: when the conflict strategy is unspecified, the default is **invalid**, meaning the whole policy is void. My profile's `rule_conflict` is *inspired by* this: refuse to pick. It is not ODRL conformance. ODRL resolves permission-versus-prohibition conflicts, not value precedence.
- **PROV-DM** (S4) [O]: multiple provenance accounts can coexist in bundles, and PROV does not adjudicate. This supports keeping both assertions, and the Outcome as a separate activity output.
- **Data mesh** (S11) [O]: domains own their data locally, and cross-domain concerns such as identifiers are standardized globally. This maps onto definition authority (global) vs. value authority (domain) [I]. Mesh gives no conflict semantics.

### 4.2 Evaluation algorithm (reference, deterministic) [I]

1. Resolve the pinned policy set at `as_of_system`. It must include only published, verified records.
2. Find the applicable PrecedenceRules for (P, s, valid_at). Compute specificity as a lexicographic tuple: enumerated subject > org_unit > jurisdiction > company-wide. If the top is tied with different tiers, return `rule_conflict`. If there is none, return `unknown_authority`.
3. Collect the assertions for (s, P) whose valid interval covers `valid_at` and whose `recorded_at ≤ as_of_system`. Collapse same-source supersession chains.
4. Partition the assertions into eligible and ineligible, by admission and staleness. Keep the ineligible ones in the output.
5. If an Adjudication covers exactly the current contest set, return `adjudicated`.
6. Walk the tiers. At the first tier with eligible assertions: one distinct value gives `selected` (or `corroborated` if ≥2 sources agree). ≥2 distinct values give `contested`. If `fallback=none` and tier 1 is empty, return `no_admissible_source`.
7. Apply the disclosure projection *after* resolution (I8).

**Multi-valued predicates:** "distinct values" presupposes cardinality 1. For registry cardinality >1 (for example several work emails), contests are about set membership. That is deferred (H5).

### 4.3 Time

The four S1 clocks [O] apply to *both* facts and policy records. Three query modes:

- **Current knowledge about valid time t:** `as_of_system = now`.
- **Replay:** `as_of_system = T`, so the result is what we knew then (I7).
- **Decision audit:** re-evaluate using the `policy_pins` stored in an old Outcome.

**Retroactive rules** (valid_from in the past) change the current-knowledge answers for past valid times but never change replay. They require the publisher to be an authority *at the recorded time of publication*, not merely at the retroactive valid_from. Otherwise a new authority could rewrite its predecessor's period without the predecessor ever having held that power. A retroactive rule over a period that was under a *different* authority must be issued by a common ancestor in the grant chain, and is `pending` until then [I].

**Future rules** are published now and applicable from valid_from. The evaluator must not apply them early. They can be revoked before they take effect, and the revocation is an appended record.

**Temporal corrections** of assertions go through `supersedes` within the same source. A correction from another source is a new competing assertion, not a correction.

XTDB (S12) [O] shows system and valid time as native columns with non-destructive updates. SQL:2011 [U] has application-time and system-versioned tables. Neither offers *authority over who may write valid-time history*. That is the part this profile adds.

**Bitemporal snapshot ≠ authenticated publication.** A bitemporal store answers "what did the register contain at T". It does not prove the policy rows were *issued by an authority* rather than inserted by a database administrator or pipeline. So PrecedenceRule, SourceAdmission and FactAuthority records need a `publication_ref`: a digest of the canonical record, signed or attested through a channel outside the store. The evaluator only *checks for presence* of verified-publication flags passed in as trusted input. It does not verify signatures, which is why it is a reference function and not a security service.

### 4.4 Attack classes

- **Policy shopping:** the caller may supply (s, P, valid_at, as_of_system) but **not** a rule id, scope or pipeline profile. Rule selection is fully determined by §4.2 step 2. Importer options such as OpenMetadata-style `overrideMetadata` have no equivalent. Import only ever *adds assertions*.
- **Confused deputy:** the ingest pipeline authenticates as itself but asserts on behalf of a source. Admission is checked against the *attributed source agent* (PROV attribution plus `actedOnBehalfOf` delegation, S4 §5.3.4), and the pipeline must itself hold an active delegation from that source. Otherwise the assertion is ineligible, however privileged the pipeline is.
- **Circular authority:** blocked by I4 and I5. An authority cannot re-grant itself a wider scope. A cycle A→B→A makes both unrecognized.
- **Output leakage:** the contest *status* is disclosed at the sensitivity of the **predicate**, not of the contributing assertions. If a caller may see predicate P at all, they see `contested` plus a count, but not the rival values or sources. If they may not see P, the whole question returns `withheld`, which is the same response as for "no data", to avoid an existence oracle. This trades against I8 as follows: I8 forbids returning a *misleading value*. It does not require revealing the contest to someone who cannot see the predicate at all.

---

## 5. Fixtures, adversarial cases, binding

### 5.1 Synthetic fixtures

**F-Startup (no HRIS or ERP).** Company `c:acme-synth`. AuthorityAnchor = founder party `p:f1`. The anchor appoints `p:f1` as values authority for `employment.*` and admits a single source `src:people-sheet` (tier 1) and `src:payroll-saas-export` (tier 1, *equal rank*). Stewardship goes to `p:ops1`. This shows that the minimum works with one spreadsheet and one person. When the sheet says start date 2026-03-01 and the payroll export says 2026-03-15, the result is `contested`, routed to `p:ops1`.

**F-Group (international).** Anchor = group board. Group HR holds `governs=definition` for `employment.*` company-wide. Each subsidiary (DE, SG, BR) holds `governs=values` with `jurisdiction` scope and its own HRIS at tier 1 and local payroll at tier 2 (`fallback=next_tier`). The group data warehouse is admitted at tier 3 for reporting only. Transfer: the SG subsidiary is merged into a regional entity effective 2026-07-01. Queries for June 2026 still return the SG authority (I12). The open SG contests carry over to the regional steward.

**F-AI/Software.** Predicate `service.owning_team`. Sources: `src:service-catalog` (tier 1), `src:codeowners-mirror` (tier 1), `src:ai-triage-agent` (admitted only for `event` proposals and never in a tier). The AI agent can create proposals that a steward reviews. It cannot be a FactAuthority because the recognition rule requires a party with a grant chain, and an agent may only act via `actedOnBehalfOf` a steward. If the catalog and the CODEOWNERS mirror disagree, the result is `contested`.

### 5.2 Adversarial scenarios (≥10)

| # | Scenario | Expected |
|---|---|---|
| A1 | Spreadsheet (tier 2) imported *after* HRIS (tier 1) with a different value | `selected` = HRIS. Spreadsheet assertion retained and ineligible for selection at this tier. |
| A2 | The same two equal-tier assertions imported in reverse order | Identical `contested` outcome (I1) |
| A3 | HRIS and payroll (equal tier) agree | `corroborated`, both IDs listed |
| A4 | Steward issues an Adjudication without delegated `adjudicate` | Adjudication invalid. Status stays `contested`. |
| A5 | New authority publishes a retroactive rule covering its predecessor's period | Rule `pending` until a common ancestor co-issues it. Replay unchanged. |
| A6 | Pipeline with admin DB rights inserts assertions attributed to itself for P | Ineligible (not admitted). Listed as ineligible. |
| A7 | Pipeline claims `actedOnBehalfOf` HRIS without a delegation record | Ineligible (confused deputy blocked) |
| A8 | Authority A grants B `may_delegate`, and B grants A a wider scope | B's grant is invalid (I5). A's original scope is unchanged. |
| A9 | Registry maintainer of the `employment` model queries as "owner" | R12 answers "not an authority" (I9) |
| A10 | Caller cleared for HRIS only, and a restricted payroll assertion contests it | `contested` with count=2, payroll values redacted. Never `selected` = HRIS (I8). |
| A11 | Two rules at equal specificity (DE jurisdiction vs. Engineering org unit) with different tiers for a DE engineer | `rule_conflict`, routed to the common authority |
| A12 | No PrecedenceRule exists for a new predicate | `unknown_authority`. No value is selected even if one source exists. |
| A13 | HRIS assertion is older than its staleness ceiling | `stale` (or ineligible with fallback, per rule). Never silently selected. |
| A14 | Adjudication settles 2 of 3 contested assertions | Invalid (I13) |
| A15 | Caller asks for `as_of_system` in the future | Clamp to `now`. Future rules are not applied early. |
| A16 | Source X is authorized, tier 1, and wrong (later superseded by X itself) | Earlier answers replay as they were. Current answer uses X's correction. The initial wrong value is never deleted. |

### 5.3 Native JSON record binding vs. mandatory companion validation [I]

**JSON Schema** (draft 2020-12) can enforce: required envelope fields, enums (`governs`, `status`, lifecycle), RFC 3339 formats, `valid_from < valid_to` (only with extension keywords, otherwise companion), `additionalProperties: false` for I11, and the non-empty `evidence_refs`.

It **cannot** enforce anything that crosses records: I1–I10 and I12–I13, grant-chain grounding, scope containment, rule overlap, pin resolution, or publication verification. So a record that passes the schema is **well-formed, not valid**. The profile must say that conformance claims require the companion validator plus the invariant test suite, and that native JSON binding alone confers nothing. The companion evaluator should ship with these fixtures as golden tests, including a property test that runs I1 over random permutations.

---

## 6. Migration, pins, holds, tradeoffs, first increment

**Migration and rollback.** Import existing catalog "owners" (DataHub-, OpenMetadata-style) as **Stewardship candidates in `pending`**, not as FactAuthorities, because catalog ownership of assets is not value authority over facts. A human anchor must confirm them. Rollback of a policy means publishing a new version that restores the prior content. It never deletes or reverts in place. Outcomes issued under the rolled-back version keep their original pins.

**Immutable pins.** Every Outcome and Adjudication records `profile_pin`, `base_pin`, `evaluator_version` and content digests of every policy record used. Floating references such as "latest" are rejected. Because `wm-xct-001` is itself at `0.3.0-research.1`, the profile must declare that it is research-grade until its base leaves research status.

**Unresolved holds:**
- **H1:** Write/propose rights have no home. S2 excludes write and S1 excludes enforcement. This is the biggest boundary gap.
- **H2:** The six-vs-four bundle discrepancy in S1 (see S1 in §0).
- **H3:** NIST SP 800-162/800-205 attribute-authority content is unread.
- **H4:** Subject identity resolution. Merging two subject IDs later can create contests retroactively. This needs a policy.
- **H5:** Contest semantics for multi-valued predicates.
- **H6:** Derived facts: which authority governs a value computed from facts with different authorities?
- **H7:** Unread paywalled ISO text (SQL:2011 and those inherited from S1) and legal alignment of appointments.
- **H8:** Whether showing a contest count leaks information in small populations. For example, "contested" on one person's compensation may itself be sensitive.
- **H9:** Whether confidence should ever affect admissibility. It is excluded in v1.

**Principal tradeoffs:**
- **Refusing to select vs. availability.** Strict `contested` and `unknown_authority` outcomes will return many non-values at first. The alternative (defaults and recency) is exactly what the acceptance criteria forbid.
- **Partial-order tiers vs. total order.** A partial order is more honest but produces more contests.
- **Predicate-level disclosure of contest status** protects integrity of answers but can leak in small populations (H8).
- **Independent assignment records** add record count and joins, but are necessary for transfer, revocation and replay.

**Recommended first increment:**
1. The profile with FactAuthority (both `governs` values), Stewardship, SourceAdmission, PrecedenceRule (tiers, `fallback`, staleness), Adjudication, AuthorityAnchor and Transfer.
2. A reference evaluator for **single-valued predicates only**, with statuses `selected`, `corroborated`, `contested`, `adjudicated`, `no_admissible_source`, `stale`, `unknown_authority`, `rule_conflict` and `withheld`.
3. Invariants I1–I13 as executable tests over the three fixtures and A1–A16.
4. JSON Schemas labeled "well-formedness only".

**Deferred, and said so openly:** enforcement and ChangeRight (H1), cryptographic publication verification (the evaluator trusts flags), multi-valued and derived predicates, confidence, identity-merge contests, and legal validity.

**Bottom line:** the attach-to-WM-XCT-001 boundary holds. The proposal as written has three conceptual flaws that need fixing before it is implemented:
- "Mastership" mixes up which source wins with who may write.
- FactAuthority merges authority over a fact type's meaning with authority over its values.
- Nothing grounds the chain of authority, so ownership claims can end up circular.
