## Verdict

**Not publishable — conditional pass on decisions, fail on contract completeness.**

The two decisions are sound and I concur with them on the frozen material: `Procedure Definition` (definition + immutable version) is the only construct here that survives an independent-identity test, and the Enterprise Audit and Assurance seam is correctly a correspondence-only profile with no minted subject identity and no runtime ID. The exclusive-composition resolution of the WM-ECO-035 / WM-ACT-033 dual root is the right shape.

It is blocked by 24 material defects below: the exclusive split is incomplete (criteria binding, sampling record and issued report have no owner), AssuranceOpinion is required to be both sealed-without-identity and explicitly supersedable, closure authority is unassigned, procedure-version authorization is claimed but unexpressed, and five declared invariants (I04, I09, I11, P04, P11) plus synthesis invariants 11 and 15 are unenforced and unfixtured. No standards conformance is assessed or claimed; no identifier is allocated or implied.

## Material defects

**Independent identity**

- **D1 — Ambiguous master.** `identityTest.mastership` reads "audit methodology *or* assurance procedure authority", i.e. two candidate masters. *Fix:* name exactly one mastering authority role.
- **D2 — Unadjudicated seam with WM-KNW-012.** ProcedureVersion owns "ordered method steps" while WM-KNW-012 is referenced for "pinned criteria **or governing method expression**". *Fix:* add a rule — WM-KNW-012 masters criteria statements only; procedure steps are never criteria and criteria never carry steps.
- **D3 — Two-level approval.** `ProcedureDefinition.lifecycle` carries draft/reviewed/approved/effective/superseded alongside a version lifecycle that also carries approved/effective/superseded, so approval has no single locus. *Fix:* restrict definition status to {draft, active, suspended, retired}; approval and effectivity exist only on ProcedureVersion.

**Procedure authorization / version pins**

- **D4 — Ambiguous effective version.** `validFrom`/`validTo` have no non-overlap constraint and `supersedesVersion` is optional. *Fix:* at most one version effective per definition per instant; `supersedesVersion` required whenever a predecessor exists.
- **D5 — Authorization claimed but unexpressed.** `owns` includes "procedure-version authorization bindings", yet no ProcedureVersion field records approver or approval time, and no rule restricts a pin to a version authorized as of the execution time. *Fix:* require an authorization record (approver + timestamp) on approved/effective versions, and add an invariant that a new pin requires authorized, non-withdrawn, non-suspended status at execution time; withdrawal blocks new pins and never retro-invalidates completed tests.

**Exclusive dual-root mastership**

- **D6 — Criteria binding unowned.** P01/P02 allocate nothing for criteria; the synthesis says "an engagement holds a pinned binding" while I02 pins criteria on the performed test. Residual dual mastership. *Fix:* WM-ECO-035 masters the engagement criteria binding (set + version); performed tests reference it read-only and may not pin a divergent version. Also adopt "before evaluation" uniformly — required invariant 2 says "before a finding is issued", which is weaker than I02.
- **D7 — Sampling record and issued report unowned.** Sampling is called execution-local but appears in no owned set; required invariant 14 protects "issued reports" that P11 does not name and no base masters. *Fix:* assign the sampling record to the WM-ACT-033 performed test, and either make the report a WM-ECO-035 issuance artifact or state that no report object exists apart from AssuranceOpinion.

**Commission composition**

- **D8 — "Cannot outlive" collides with immutability.** P03 forbids an Execution outliving its Engagement while P11 requires issued work to stay immutable and resolvable. *Fix:* restate P03 as an authorized-activity window — no execution activity outside the engagement's authorized period; records are retained immutably and remain resolvable after closure.

**Opinion scope / limitations**

- **D9 — Sealed but supersedable.** "Create no model for AssuranceOpinion… sealed statement" cannot satisfy invariant 14 and P11, which require explicit supersession and withdrawal; an artifact with no identity cannot be referenced or superseded. *Fix:* give it an engagement-scoped issuance identity (engagement + issuance sequence) mastered by WM-ECO-035, with no new registry model.
- **D10 — Incomplete mandatory limitation set.** P06 mandates only exclusions and frame gaps; the synthesis also binds period, assurance level, evidence limitations, modification and use restrictions. *Fix:* add those four to P06's mandatory enumeration.

**Closure authority / retest**

- **D11 — Closure authority unassigned.** The closure sequence names a "finding closure decision" with no holder and no incompatibility rule. *Fix:* the closure decision is recorded by the engagement's issuance authority, citing the stated closure criteria and the retest reference; the corrective-action actor, audited management and the retest executor cannot decide closure.
- **D12 — Unbounded successor-cell escape.** P09 permits closure against an "explicitly declared successor cell" with no declarer, authority or equivalence test. *Fix:* a successor cell requires closure-authority authorization with recorded equivalence rationale; otherwise closure is rejected.

**Corrective-action separation**

- **D13 — Management response unmastered.** It is required to be separate from WM-ACT-006 but is assigned to no base and no shape. *Fix:* master it in WM-ACT-033 as an engagement-scoped assertion shaped by WM-KNW-007, attached to the finding, never instantiated in WM-ACT-006.
- **D14 — Root cause unenforced.** Required invariant 11 appears in no I- or P-rule and no fixture. *Fix:* add a rule — root cause is an evidenced claim carrying a conclusion status whose vocabulary includes `undetermined`, distinct from finding, issue and action identity.

**Evidence and finding identity**

- **D15 — Evidence terminology and cardinality unreconciled.** "evidence item" (synthesis), "evidence package" (P02) and "evidenceRequirements" (version) are undifferentiated, and I06's single-test binding forbids legitimate reuse of one evidence item. *Fix:* define the item as the identified unit carrying provenance and integrity, the package as a named collection of item references, and bind test + cell on each *reference*, allowing one item to be referenced by several performed tests.
- **D16 — Finding identity unscoped.** Nothing states whether finding identity is engagement-scoped or global, nor forbids minting a new identity at retest or supersession. *Fix:* finding identity is an engagement-scoped key, unique within the engagement and unchanged by retest, response or closure.

**Sampling frame / method / sample / cell**

- **D17 — I05 weaker than the stated requirement.** It omits sample size, selection-method version, deviations and the projection claim that the synthesis requires. *Fix:* extend I05 to population, frame, gaps, method **and method version**, sample units **and size**, deviations, and an explicit projection claim for which `none` is a valid value.
- **D18 — Closed vocabularies claimed but undefined.** "closed sampling-method vocabulary", "result vocabulary" and "frame-gap representation" are owned while `samplingMethod` is optional and no member is enumerated. *Fix:* enumerate the closed lists, or downgrade the ownership claim to a referenced vocabulary under an explicit hold.

**Immutability**

- **D19 — Incomplete append-only coverage.** P11 names performed tests, evidence, findings and opinions but not observations, management responses, retest records or issued reports, and withdrawal carries no reason or authority requirement. *Fix:* extend P11 to all recorded engagement artifacts; a withdrawal requires a stated reason and authority and never edits its predecessor.
- **D20 — Time distinctions unenforced.** Required invariant 15 appears in no I- or P-rule and no fixture. *Fix:* add a rule requiring event, execution, observation, issuance, response, completion, retest and ingestion times to be separately recorded fields.

**Correspondence-only profile and fixture traceability**

- **D21 — Missing reference base.** WM-KNW-012 carries the criteria pin central to I02 and P09 but is absent from profile `bases`. *Fix:* add WM-KNW-012 as a reference-only base.
- **D22 — Acceptance scenario untraceable.** Fixtures use Site X/Y while the acceptance result uses Site 3, F-1, I-7, CA-1, R-1; no fixture traces that scenario end to end; and `version-pinned-execution` reuses "v2.1" — the acceptance *criteria* version — as a *procedure* version, conflating two distinct pins. *Fix:* give procedure and criteria distinct version tokens, and add one end-to-end acceptance fixture using the acceptance-result tokens.
- **D23 — Non-falsifiable fixture.** `criteria-changed-on-retest` expects "Rejected unless successor cell/criteria creates a new adjudicated path", which no implementation can fail. *Fix:* amend its expectation to — closure of the original finding is rejected, and the changed criteria produce a new finding on a new adjudicated path.
- **D24 — Unfixtured rules.** I04, I09, I11, P04 and P11 have no covering case. *Fix:* the fixtures below.

## Additional fixtures required (exact)

Amend `criteria-changed-on-retest` per D23, then add these 29:

| id | kind | covers |
|---|---|---|
| `single-criteria-binding` — execution pins a criteria version differing from the engagement binding → rejected | negative | D6 |
| `criteria-pin-before-evaluation` — criteria pinned prior to evaluation, not merely prior to issuance → accepted | positive | D6 |
| `procedure-step-asserts-criterion` — ProcedureVersion step states a criterion (or WM-KNW-012 criteria carry steps) → rejected | negative | D2 |
| `definition-level-approval-only` — definition marked approved with no approved version → rejected | negative | D3 |
| `overlapping-effective-versions` — two versions of one definition effective at the same instant → rejected | negative | D4 |
| `missing-version-authorization` — version reaches effective without approver and approval time → rejected | negative | D5 |
| `withdrawn-version-new-pin` — new performed test pins a withdrawn or suspended version → rejected; previously completed pins unaffected | negative | D5 |
| `superseded-version-resolvable` — superseded version stays immutable and resolvable for an issued finding | positive | I11, D4 |
| `procedure-holds-engagement-fact` — ProcedureDefinition record carries engagement scope, opinion or closure state → rejected | negative | I04 |
| `sampling-record-incomplete` — performed test omits sample size, selection-method version or deviations → rejected | negative | D17 |
| `projection-claim-none` — sample supporting no projection records projection claim `none` → accepted | positive | D17 |
| `sampling-method-outside-vocabulary` — sampling method value outside the closed vocabulary → rejected | negative | D18 |
| `evidence-item-multi-test-reuse` — one evidence item referenced by two performed tests, each reference carrying its own test and cell binding → accepted | positive | D15 |
| `finding-identity-stable-across-retest` — retest or supersession mints a new finding identity → rejected | negative | D16 |
| `duplicate-finding-key-in-engagement` — same finding key reused within one engagement → rejected | negative | D16 |
| `opinion-supersession-identity` — superseding opinion issued as a new engagement-scoped issuance referencing the withdrawn one; original unaltered | positive | D9 |
| `opinion-missing-period-or-level` — opinion omits period, assurance level, modification type or use restriction → rejected | negative | D10 |
| `closure-by-unauthorized-party` — corrective-action actor, audited management or the retest executor records the closure decision → rejected | negative | D11 |
| `successor-cell-unauthorized` — closure against a successor cell lacking closure-authority authorization and equivalence rationale → rejected | negative | D12 |
| `management-response-mastership` — management response stored as a WM-ACT-006 action or as a finding attribute → rejected | negative | D13 |
| `root-cause-undetermined` — evidenced root cause with conclusion status `undetermined` → accepted, finding unaffected in identity | positive | D14 |
| `timestamp-collapse` — observation time reused as issuance or ingestion time → rejected | negative | D20 |
| `issued-artifact-in-place-edit` — in-place edit of an issued observation, finding, response, retest record or opinion → rejected; successor appended | negative | P11, D19 |
| `withdrawal-without-reason` — withdrawal recorded without stated reason and authority → rejected | negative | D19 |
| `merged-audit-root` — a merged Audit root or third master claims both engagement and execution facts → rejected | negative | P04 |
| `independence-competence-separate-records` — one combined attestation offered for both → rejected; separate engagement- and execution-scoped records accepted | negative | I09 |
| `engagement-closed-execution-resolvable` — engagement closes; its execution records stay immutable and resolvable while no new execution activity is permitted | positive | D8 |
| `issued-report-master` — report deliverable mastered outside WM-ECO-035 or duplicating opinion identity → rejected | negative | D7 |
| `acceptance-end-to-end` — criteria v2.1, distinct procedure version, Process A frame 412 of 430, Site 3 excluded, F-1 → I-7 → CA-1 complete → R-1 independent retest → closure by issuance authority; opinion lists exclusion and frame gap | positive | D22 |