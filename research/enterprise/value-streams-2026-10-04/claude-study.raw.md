# Frozen Independent Study — Enterprise Value-Stream Coverage and Minimum Meta-Model Set

Scope note: this review uses only the frozen register and inventory supplied in the prompt. No identifiers are allocated, no publication is claimed, and every candidate below remains identifier-unassigned.

---

## A. Coverage frame

Completeness is argued over a **finite cross-product of three closed dimensions**, not over an open list of business labels.

**Dimension 1 — Beneficiary locus (4 values, exhaustive by boundary logic).**
External counterparty (customer, consumer, applicant, member, citizen); external supply-side counterparty (supplier, partner, labour market, funder/investor); external authority/society (regulator, auditor, standards body, donor/public); internal enterprise beneficiary (governing body, organizational unit, position holder, internal service consumer).

**Dimension 2 — Value mode (11 values, fixed by the objective).**
Acquisition, creation, delivery, realization, capture, renewal/retirement, change, enablement, governance, assurance, recovery.

**Dimension 3 — Beneficiary value-state lattice (closed transition set).**
`unaware → aware/eligible → committed/entitled → in possession or in service → outcome achieved → benefit realized → renewed or exited`, plus two orthogonal segments: `degraded → restored` (recovery) and `unauthorized/unevidenced → authorized/evidenced` (governance, assurance, enablement-by-permission).

**Closure argument.** A value stream is admissible only if it traverses one or more contiguous segments of the lattice for one named beneficiary locus. The lattice has a finite segment set; the locus dimension is finite; therefore the set of admissible archetype cells is finite. Coverage is demonstrated when (i) every segment × locus cell is either filled by at least one archetype or declared empty-by-construction with a reason, and (ii) no archetype spans two loci without an explicit cross-boundary hand-off.

**Cells declared empty-by-construction.**
- *External value capture.* Economic capture accrues to the enterprise; the counterparty-side state change is only `obligation discharged`, already mastered by WM-XCT-029 and WM-ECO-009. Capture is therefore an internal stream (I9). This is why order-to-cash fails (G1).
- *Internal acquisition of market demand.* Demand originates outside; internal analogues are funding (I8) and capacity (I6).
- *External assurance-of-self.* The enterprise cannot be the assurer and the assured beneficiary in one stream; internal assurance is I12, external issuance is E12.

**Explicit exclusions.** Department and function lists; generic Porter-style value chains; application workflows and SDLC chains; project and programme plans; touchpoint-only journeys; product, asset, employment and case lifecycles lacking beneficiary value progression; document or ledger state chains; organizational capability inventories. Each is adjudicated in D and G.

---

## B. External value streams

Masters column cites frozen inventory IDs reusable as profile bases. "Gap" means no master carries the stream identity itself.

| # | Canonical archetype | Beneficiary / counterparty | Trigger | Terminal value outcome | Typical variants | Current masters (profile bases) | Gaps |
|---|---|---|---|---|---|---|---|
| E1 | Latent Need to Committed Agreement | Prospective customer/member | Expressed or detected need | Counterparty holds an enforceable, priced commitment | Self-serve, assisted, tender-led, channel, renewal-upsell | WM-ECO-026, WM-ECO-021, WM-ECO-020, WM-ECO-006, WM-XCT-029, WM-ORG-014 (EM-COM-02/03, EM-LEG-01) | Stream identity; beneficiary value-state sequence |
| E2 | Claimed Eligibility to Conferred Entitlement | Applicant, citizen, member, grantee | Application or eligibility event | Beneficiary holds a conferred right or benefit | Public benefit, licence, membership, grant award | WM-REC-009, WM-POL-012, WM-POL-018, WM-POL-017, WM-ECO-030, WM-POL-004 (EM-LEG-04) | Stream identity; separation of conferral from case closure |
| E3 | Request to Rendered Service | Customer/service consumer | Service request or scheduled obligation | Beneficiary's need served at agreed level | Scheduled, on-demand, field, digital self-service, care | WM-ACT-004, WM-ACT-021, WM-ACT-026, WM-ACT-007, WM-SFT-016 (EM-PRD-02, EM-COM-04) | Stream identity; stage-level value states |
| E4 | Order to Beneficiary Possession and Use | Customer, consignee | Confirmed order or entitlement | Beneficiary possesses and can use the item/entitlement | Goods, digital licence, subscription activation, installation | WM-ECO-024, WM-FLW-011, WM-FLW-004, WM-ECO-022, WM-SFT-009 (EM-COM-03) | Stream identity; consumption entitlement (EM-COM-03 candidate) |
| E5 | Unmet Market Need to Available Offering | Market segment / addressed beneficiary class | Validated unmet need or mandate | Offering is available and obtainable by the beneficiary class | Product, service, data product, AI-enabled, regulated launch | WM-OBJ-002, WM-ACT-004, WM-DAT-008, WM-REC-006, WM-ACT-022 (EM-PRD-01/03/04) | Stream identity; market-availability outcome distinct from release |
| E6 | Adoption to Realized Beneficiary Outcome | Customer, member, donor, public | Onboarding completion or first use | Beneficiary's stated outcome achieved and evidenced | Customer success, clinical outcome, mission/donor effect, policy effect | WM-KNW-011, WM-ACT-034, WM-MAT-008, WM-ACT-049 (EM-STR-02) | Stream identity; outcome and benefit boundary unresolved (EM-STR-02) |
| E7 | Failure or Grievance to Remedied Position | Affected customer/counterparty | Detected failure, complaint, claim, breach | Beneficiary's value position restored or compensated | Service restoration, refund/return, warranty, insurance claim, dispute/redress | WM-ACT-021, WM-ECO-025, WM-ECO-036, WM-POL-009, WM-ACT-043 (EM-LEG-05, EM-RSK-04) | Stream identity; remedy outcome distinct from case closure |
| E8 | Expiring Entitlement to Renewed or Exited Relationship | Existing customer/member | Term end, usage decay, withdrawal notice | Relationship renewed, migrated, or orderly exited with obligations settled | Renewal, migration, offering withdrawal, membership lapse, divestment | WM-ECO-022, WM-ECO-006, WM-ORG-014, WM-XCT-029 (EM-COM-03, EM-LND-07) | Stream identity; renewal is only a version link today |
| E9 | Supply Need to Assured Supply | Enterprise as beneficiary; supplier counterparty | Qualified internal need | Enterprise holds assured, compliant supply capacity | Strategic sourcing, tender, catalogue buy, partner sourcing | WM-ECO-007, WM-ECO-019, WM-ORG-015, WM-ECO-006 (EM-OPS-02) | Stream identity; requests/sourcing events unassigned (EM-OPS-02) |
| E10 | Capital Need to Funded Capacity | Enterprise as beneficiary; investor/funder/lender | Approved capital or funding need | Funds committed and available under accepted terms | Equity, debt, grant, public funding, internal capital call | WM-ECO-037, WM-ECO-038, WM-ECO-030, WM-ECO-005 (EM-FIN-06, EM-ORG-03) | Stream identity; instrument/investment roots unassigned |
| E11 | Counterparty Intent to Operating Integration | New supplier, partner, channel, large client | Signed intent or award | Counterparty is operationally integrated and transacting | Supplier onboarding, partner enablement, client migration, API consumer onboarding | WM-ORG-015, WM-SFT-003, WM-XCT-002, WM-ACT-040 (EM-TEC-03) | Stream identity; integration root unassigned (EM-TEC-03) |
| E12 | External Obligation to Accepted Disclosure or Assurance | Regulator, auditor, owner, public | Reporting period, mandate, assurance demand | Authority accepts the disclosure or issues assurance | Statutory filing, tax filing, ESG disclosure, certification, external audit | WM-ECO-033, WM-ECO-032, WM-ECO-034, WM-ECO-035, WM-ACT-051 (EM-FAC-02, EM-RSK-02) | Stream identity; acceptance outcome distinct from filing submission |
| E13 | Counterparty Capability Gap to Enabled Counterparty | Customer, developer, partner, citizen | Identified capability or literacy gap | Counterparty independently capable of obtaining value | Customer education, certification, developer enablement, public capability building | WM-ACT-038, WM-KNW-004, WM-ACT-041, WM-PER-008 (EM-PEO-05) | Stream identity; learning roots unassigned (EM-PEO-05) |

---

## C. Internal value streams

| # | Canonical archetype | Beneficiary (internal) | Trigger | Terminal value outcome | Typical variants | Current masters (profile bases) | Gaps |
|---|---|---|---|---|---|---|---|
| I1 | Strategic Intent to Governed Commitment | Governing body / executive mandate holder | Strategic signal, cycle, scenario shift | Enterprise holds an authorized, funded, owned commitment set | Annual planning, scenario-driven re-plan, M&A, mandate change | WM-ACT-030, WM-KNW-010, WM-KNW-011, WM-ORG-018, WM-REC-010 (EM-STR-01/04, EM-WRK-04) | Stream identity; Strategy/Business Model/Scenario roots unassigned |
| I2 | Authorized Commitment to Delivered Change | Receiving organizational unit | Approved initiative or change mandate | Changed capability exists and is accepted by the receiver | Project, programme, agile product change, operational change, platform build | WM-ACT-005, WM-ACT-029, WM-ACT-006, WM-ACT-032, WM-SFT-008, WM-SFT-009 (EM-WRK-01/02/03, EM-TEC-10) | Stream identity; acceptance distinct from delivery |
| I3 | Delivered Change to Adopted Capability-in-Use | Operating unit / internal service consumer | Acceptance or go-live | Capability in routine productive use with evidenced effect | Rollout, adoption, hypercare, decommission-of-predecessor | WM-ACT-040, WM-ACT-034, WM-MAT-008, WM-KNW-011 (EM-STR-02, EM-WRK-03) | Stream identity; benefit realization unowned |
| I4 | Role Need to Deployed Capable Worker | Receiving unit / position owner | Authorized workforce demand | Position productively occupied by a capable worker | External hire, internal mobility, contingent, succession fill | WM-ORG-008, WM-ACT-039, WM-ORG-005, WM-ORG-016, WM-ACT-040 (EM-PEO-02/04) | Stream identity; requisition/candidacy/employee-profile unassigned |
| I5 | Competence Gap to Applied Competence | Worker, team, receiving unit | Assessed gap, new standard, role change | Competence demonstrably applied in work context | Training, certification, on-the-job, regulatory requalification | WM-PER-009, WM-ACT-038, WM-PER-008, WM-ACT-034 (EM-PEO-03/05) | Stream identity; learning and capability-assertion roots unassigned |
| I6 | Resource Need to Allocated Capacity | Demanding unit / initiative | Unmet resource demand | Capacity committed and consumable by the demander | People, compute, budgetary, facility, equipment | WM-ORG-016, WM-FLW-015, WM-ACT-008 (EM-WRK-05, EM-FAC-01) | Stream identity; Resource Demand/Pool unassigned |
| I7 | Asset Need to Serviceable Asset-in-Use | Operating unit / asset user | Asset need, condition breach, calibration due | Asset available, compliant and fit for use | Acquisition, maintenance, calibration, replacement, disposal | WM-OBJ-022, WM-ACT-013, WM-OBJ-023, WM-ACT-007, WM-BLT-002 (EM-OPS-03, EM-FAC-01) | Stream identity; maintenance/calibration roots unassigned |
| I8 | Funding Need to Authorized and Released Funds | Responsibility centre / budget holder | Budget cycle, reforecast, unfunded commitment | Funds authorized, released and spendable within mandate | Annual budget, reforecast, capital release, grant drawdown | WM-ECO-012, WM-REC-010, WM-ECO-016 (EM-FIN-01/05) | Stream identity; Responsibility Centre unassigned |
| I9 | Delivered Value to Captured Economic Benefit | Enterprise / owners | Recognized delivery or realization event | Economic benefit recognized, collected and reportable | Revenue recognition, cost avoidance, cost recovery, consolidation | WM-ECO-016, WM-ECO-017, WM-ECO-018, WM-ECO-009, WM-ECO-002 (EM-FIN-02/03/04) | Stream identity; must stay distinct from E1–E8 outcomes |
| I10 | Decision Need to Acted-Upon Decision | Decision owner / accountable role | Decision need, trigger threshold, mandate | Decision taken, recorded and acted upon with traceable rationale | Investment, architecture, risk acceptance, pricing, policy | WM-KNW-010, WM-REC-010, WM-ACT-024, WM-ACT-036, WM-KNW-007, WM-KNW-008 (EM-KNW-02, EM-DAT-07) | Stream identity; Evidence Artifact and Analysis Method unassigned |
| I11 | Exposure to Accepted Residual Risk State | Risk owner / governing body | Identified exposure, threshold breach | Residual risk within appetite and formally accepted | Enterprise risk, cyber, compliance, continuity, project risk | WM-KNW-015, WM-XCT-027, WM-ACT-034, WM-REC-010 (EM-RSK-01) | Stream identity; Control unassigned, treatment unowned |
| I12 | Control Obligation to Evidenced Assurance | Governing body / accountable executive | Assurance plan, finding, mandate | Control effectiveness evidenced and accepted | Internal audit, control testing, policy attestation, data-quality assurance | WM-ACT-033, WM-ECO-035, WM-DAT-007, WM-XCT-038 (EM-RSK-02, EM-DAT-04) | Stream identity; Procedure Definition unassigned |
| I13 | Disruption to Restored Operating Capability | Affected operating unit / internal consumer | Detected disruption or loss of capability | Operating capability restored and verified within tolerance | IT continuity, site continuity, supply disruption, data restore | WM-ACT-043, WM-ACT-042, WM-ACT-019, WM-ACT-020 (EM-RSK-04, EM-TEC-05) | Stream identity; restoration outcome distinct from incident closure |
| I14 | End-of-Need to Safely Retired Capability | Enterprise / successor owner | Obsolescence, policy, exit decision | Capability retired with obligations, data and risk discharged | Application decommission, product sunset, site exit, entity wind-down | WM-XCT-035, WM-SFT-002, WM-ECO-006, WM-ORG-010 (EM-TEC-02, EM-LEG-03) | Stream identity; retirement outcome unmastered |
| I15 | Access Need to Authorized Least-Privilege Access | Worker, agent, internal consumer | Role change, joiner/mover/leaver, grant request | Appropriate access authorized, in force and periodically re-justified | Joiner/mover/leaver, privileged access, agent authority, consent | WM-PER-002, WM-XCT-002, WM-XCT-004, WM-AI-002 (EM-RSK-03, EM-XCT-07 pending) | Stream identity; Authorization Domain / Access Grant allocation unresolved |

**Coverage check.** Modes are covered as: acquisition E1, E2, E9, E10, I4, I7; creation E5, I2; delivery E3, E4; realization E6, I3; capture I9; renewal/retirement E8, I14; change E11, I2; enablement E13, I5, I6, I8, I15; governance E12, I1, I11; assurance E12, I12; recovery E7, I13. Every non-empty cell of A's cross-product is occupied; empty cells are justified in A.

---

## D. Composition rules

1. **Nesting.** A stream may contain a sub-stream only if the sub-stream's beneficiary class is identical and its terminal outcome is exactly one stage value-state of the parent. Otherwise the relation is a hand-off, not nesting. Depth is bounded at two levels of nesting; deeper structures are process decomposition.
2. **Decomposition.** Stage is the only decomposition unit of a stream. A stage must assert a named change in beneficiary value state. Internal work steps, approvals, system calls and hand-offs between teams decompose into WM-ACT-003 / WM-ACT-002 / WM-ACT-015 and never become stages.
3. **Variants.** Same beneficiary class, trigger class and terminal outcome with a different stage path or channel ⇒ **variant** inside the same stream identity. Any change of beneficiary, trigger, state sequence or terminal outcome ⇒ **new version** if the identity triple is preserved, **new stream** if it is not.
4. **Cross-boundary hand-off.** The terminal outcome of one stream may be the trigger of another (e.g. E1 → E4, E4 → E6, I2 → I3, E7 ↔ I13). Hand-offs are explicit, directed, version-pinned edges; they do not merge streams and never make an internal stream external. External/internal is a **role of the same stream definition under a stated governing boundary** (integrity constraint), expressed as a boundary-scoped classification, not as a second root.
5. **Many-to-many realization.** A stage may be realized by many capabilities, processes, services, systems or suppliers, and any realizer may serve many stages. Realization is an evidenced, time-bounded assertion with pinned versions; no exclusivity and no containment of realizers by streams.
6. **Distinctions.**
   - *Process/Workflow* (WM-ACT-003, EM-OPS-01): ordered activity and control flow; identity survives beneficiary change. A stream survives process redesign; a process does not survive flow redefinition.
   - *Journey*: observed or designed touchpoint sequence from the beneficiary's experiential perspective; may traverse several streams; carries no terminal value outcome obligation.
   - *Lifecycle* (WM-XCT-021, WM-OBJ-022): status progression of a subject (asset, employment, case, product); beneficiary need not change value state at all.
   - *Business Capability* (EM-STR-03): a standing ability — `(outcome class, acted-upon object)` — with no trigger, no sequence and no terminal event.
   - *Value chain*: an industry-level abstraction of activity categories; neither beneficiary-specific nor triggered; not representable as a stream and excluded.
7. **Views never mint identity.** Maps, landscapes, portfolios and heat overlays are projections over streams, stages and realizations; they may be governed declarations but carry no business identity of their own.

---

## E. Meta-model decision register

| Semantic element | Decision | Owner contour | Dependency boundary |
|---|---|---|---|
| Value Stream | **NEW** (passes F) | EM-STR-01 | References beneficiary role, trigger class, outcome class, capability/process realizers by pinned version; owns no realizer |
| Value Stream Stage | **CONTAINED** in Value Stream | EM-STR-01 | Addressable inside the aggregate only; no independent mastership, no cross-aggregate reuse |
| Value Stream Variant | **CONTAINED** in Value Stream | EM-STR-01 | Uses WM-XCT-022 version/change semantics; no separate root |
| Value Stream Map / View | **PROFILE / PROJECTION**, no identity | EM-LND (value-stream landscape profile, reusing the EM-LND-18 declaration pattern) | Read-only over stream, stage, realization and metric facts |
| Value Stream Portfolio / Landscape | **PROFILE / PROJECTION**, no identity | same as above | Governance scope + filter only; may not assert stream content |
| Value Exchange | **CONTAINED** in Business Model (declared reciprocal structure); realized exchanges are **PROJECTION** | EM-STR-01 for declaration; WM-XCT-029, WM-ECO-006, WM-ECO-021, WM-ECO-024, WM-ECO-009 for realized legs | No root: every leg already has a master; a root would duplicate mastership |
| Outcome | **REUSE + DEFER.** Outcome *class* = governed vocabulary on WM-KNW-018 + WM-KNW-006; achieved outcome = PROFILE over WM-KNW-007 + WM-MAT-008 | EM-STR-02 | Root candidate stays deferred per EM-STR-02; value streams need only the class reference |
| Benefit Realization | **PROFILE** over WM-ACT-034 + WM-KNW-011 + WM-MAT-008, mastered by Program assertions | EM-WRK-03 with EM-STR-02 boundary | Must not be asserted by the stream; stream supplies the outcome link only |
| Business Capability | **NEW** (passes, but outside the value-stream critical path) | EM-STR-03 | Referenced by stage realization; independent of stream existence |
| Capability Realization | **NEW** (passes; ownership differs from capability) | EM-STR-03 | Binds one capability to one realizer; streams reference, never own |
| Metric Definition | **NEW** (passes) | EM-DAT-05 | Streams and stages reference definitions by pinned version; observations stay on WM-MAT-008 |
| Value Proposition | **CONTAINED** in Business Model / Offering | EM-STR-01, EM-PRD-01 | Honours the frozen EM-STR-01 contained-proposition decision; no root |
| Journey | **PROJECTION**, non-normative; candidate parked | EM-TEC-06 (User Journey, unassigned) | Projection over WM-ACT-027, WM-ACT-021, WM-ACT-026, bound to a pinned stream version |
| Process Execution | **REUSE** WM-ACT-003 (definition) + WM-ACT-002 / WM-ACT-015 (occurrence) | EM-OPS-01 (complete reserved) | No new root; streams reference executions as realization evidence |
| Beneficiary binding | **PROFILE** over WM-XCT-023 + WM-ORG-013 (+ WM-ORG-014, WM-PER-001, WM-ORG-001) | EM-ORG-07 | Role binding only; no new party root |
| Trigger | **CONTAINED** trigger class in stream; occurrences via WM-ACT-015 | EM-STR-01 | Occurrence facts stay externally mastered |
| Stream-to-stream hand-off | **PROFILE** over WM-XCT-037 | EM-WRK-06 | Narrowed edge semantics; no new root |
| Boundary role (external/internal) | **CONTAINED** boundary-scoped classification via WM-XCT-020 | EM-XCT-09 (pending) | Forbids duplicate roots for visibility differences |
| Stage Realization (stage ↔ process/service/system) | **CONTAINED** now; optional later root only on evidence of independent governance | EM-STR-01 | Deliberately not a root in this iteration |

---

## F. Minimum new roots

### F1. Value Stream — **must-have, single required root**

- **Stable identity.** The governed triple `(beneficiary class, trigger class, terminal outcome class)` under a stated governing boundary. Identity survives process redesign, automation, outsourcing, system replacement, organizational restructuring, channel change and renaming. This matches and is narrower than the frozen EM-STR-01 identity statement.
- **Independent lifecycle.** Proposed → accepted → in force → superseded → retired, independent of any initiative, process, capability, system or organizational unit lifecycle. A stream can be in force while all its realizers are replaced, and can be retired while its realizers persist.
- **Mastership.** The enterprise architecture / business-architecture authority of the governing boundary masters the stream declaration. No other master asserts it today: WM-ACT-003 masters flow, WM-ACT-001 masters function, WM-ACT-029/WM-ACT-005 master change vehicles, WM-ECO-* master transactions. No duplication.
- **Version driver.** A version changes if and only if beneficiary class, trigger class, stage value-state sequence, or terminal outcome class changes. Realizer substitution, channel addition, metric change and owner change are non-versioning.
- **Transfer test.** A stream transfers between organizational units, legal entities (EM-ORG-01/02) and even enterprises on divestment while retaining identity and history; its realizers transfer separately. Transferability is independent of any realizer — the decisive proof that it cannot be contained.
- **Aggregate objects (contained, no independent mastership).** Stage (ordered, value-state-changing), Variant, Trigger specification, Beneficiary binding, Terminal outcome binding, Stage realization assertion, Hand-off edge, Boundary-role classification.
- **Invariants.**
  1. ≥1 named beneficiary binding; exactly one beneficiary class per stream version.
  2. ≥2 stages; each stage asserts a distinct beneficiary value state; stages are totally ordered within a variant.
  3. Terminal outcome ≠ any output, deliverable, document, payment or completion event.
  4. No stage may be defined by an organizational unit, system, application or document state.
  5. Realization assertions are many-to-many, evidenced, time-bounded and version-pinned.
  6. Missing realization, metric or outcome evidence is `unknown` — never zero, success or completion.
  7. Boundary role is derived from the beneficiary binding plus governing boundary; it may not create a second stream identity.
  8. A sub-stream link requires identical beneficiary class and a parent stage match; otherwise it is a hand-off.

### F2. Roots that pass the test but are **not required** for value-stream representation
Kept separate from F1 because ownership and identity differ; recommended only in the later sequence steps (I).

| Candidate | Identity | Why separate | Status recommendation |
|---|---|---|---|
| Business Capability (EM-STR-03) | `(outcomeClassRef, actedUponObjectRef)` | Standing ability, no trigger or sequence; owned by capability authority | Allocate after F1; enables stage realization |
| Capability Realization (EM-STR-03) | Temporal evidenced capability↔realizer binding | Ownership follows the realizer, not the capability | Allocate with Business Capability |
| Metric Definition (EM-DAT-05) | Metric exists independently of observation, target, report | Measurement authority, not stream authority | Allocate after F1 |

### F3. Candidates explicitly **not** created
Value Stream Stage, Value Stream Map/View, Value Stream Portfolio/Landscape, Value Exchange, Value Proposition, Journey, Process Execution, Outcome, Benefit Realization, Stage Realization. Each fails at least one of independent identity, independent lifecycle or non-duplicated mastership — see E and H.

---

## G. Negative cases

| # | Label | Verdict | Reason | Correct master(s) |
|---|---|---|---|---|
| G1 | Order-to-cash | **Reject** | Beneficiary is enterprise cash; stages are document/ledger states; payment never proves outcome | WM-ECO-020, WM-ECO-024, WM-ECO-008, WM-ECO-009, WM-ECO-016; capture = I9 |
| G2 | Procure-to-pay | **Reject** | Transactional document chain; no beneficiary value-state progression | WM-ECO-019, WM-ECO-008, WM-ECO-009; stream = E9 |
| G3 | Hire-to-retire | **Reject** | Employment/person lifecycle, not beneficiary value progression; no terminal value outcome | WM-ORG-005, WM-ACT-040, EM-PEO-02; streams = I4, I5 |
| G4 | Incident-to-recovery | **Reject as labelled** | Case/ticket lifecycle; terminal state is closure, not restored beneficiary value | WM-ACT-019, WM-ACT-042, WM-ACT-021; conforming reformulations = E7 (external), I13 (internal) |
| G5 | Strategy-to-outcome | **Reject** | No single beneficiary, no recognizable trigger, unbounded causal chain; conflates governance, change and realization | Split into I1, I2, I3, plus deferred EM-STR-02 outcome/benefit boundary |
| G6 | Data-to-insight | **Reject** | Insight is an output; no beneficiary value state changes on delivery | WM-DAT-005, WM-ACT-053, WM-DAT-006, WM-ACT-036; stream = I10 |
| G7 | Record-to-report | **Reject** | Accounting close process over ledger states | WM-ECO-016, WM-ECO-018, EM-FIN-04 |
| G8 | Plan-to-produce | **Reject** | Manufacturing process and material lifecycle; beneficiary absent | WM-ACT-010, WM-OBJ-020, EM-OPS-04/05; delivery stream = E4 |
| G9 | Concept-to-code / idea-to-deploy | **Reject** | Application and engineering workflow; release is an output | WM-SFT-013, WM-SFT-008, WM-SFT-009; stream = E5 or I2 |
| G10 | Campaign-to-lead | **Reject** | Touchpoint and output chain; lead is not a beneficiary value state | WM-ECO-027, WM-ECO-026, EM-COM-02; stream = E1 |
| G11 | Acquire-to-retire (asset) | **Reject** | Asset lifecycle without beneficiary value progression | WM-OBJ-022, EM-OPS-03; stream = I7 |
| G12 | Defect-to-fix | **Reject** | Defect lifecycle; fix is an output | WM-SFT-014, WM-SFT-015, EM-TEC-08 |
| G13 | Requisition-to-onboard | **Reject** | Proper subset of I4 and a process chain; no distinct terminal outcome | EM-PEO-04 candidates; stream = I4 |
| G14 | "Finance value stream" / any department-named stream | **Reject** | Department list; no beneficiary, trigger or terminal outcome | WM-ORG-002, EM-LND-01 |
| G15 | "Digital transformation value stream" | **Reject** | Programme with a finite plan, not a repeatable triggered stream | WM-ACT-029, EM-WRK-03 |
| G16 | Quote-to-contract | **Reject** | Document state chain and a proper subset of E1 | WM-ECO-021, WM-ECO-006; stream = E1 |

---

## H. Adjudication

1. **Value Stream — NEW ROOT (must-have).** Only element passing identity, lifecycle, mastership, version-driver and transfer tests without duplicating an existing master. Owner EM-STR-01.
2. **Value Stream Stage — CONTAINED.** No identity outside its stream version; renumbering or merging stages is a stream version change. Reuse across streams would require a beneficiary-free identity, which contradicts the value-stream test.
3. **Value Stream Map / View — PROJECTION, NO ROOT.** Views do not mint business identity. May be expressed as a governed declaration profile reusing the EM-LND-18 pattern, but asserts no stream content.
4. **Value Stream Portfolio / Landscape — PROJECTION + GOVERNANCE SCOPE PROFILE, NO ROOT.** Same reasoning; scope selection and perimeter only, consistent with EM-LND-07 and EM-LND-18 precedent.
5. **Value Exchange — CONTAINED (declaration) + PROJECTION (realization), NO ROOT.** Declared reciprocal exchange belongs to Business Model; realized legs are already mastered by WM-XCT-029, WM-ECO-006, WM-ECO-021, WM-ECO-024, WM-ECO-009. A root would violate single-mastership.
6. **Outcome — DEFER (no root now).** Honours EM-STR-02's rejection of a combined root and deferral of two separate identities. Value streams require only an outcome *class* reference, satisfied by a governed WM-KNW-018 scheme with WM-KNW-006 terms; achieved outcomes profile WM-KNW-007 and WM-MAT-008. Note: EM-STR-03's `outcomeClassRef` has the same dependency, so one shared class vocabulary serves both and prevents a duplicate root.
7. **Benefit Realization — PROFILE, NO ROOT.** Mastered as programme-owned assertions (EM-WRK-03) over WM-ACT-034, WM-KNW-011, WM-MAT-008. Delivery, completion and payment never prove benefit.
8. **Business Capability — NEW ROOT, but optional for value streams.** Passes on the EM-STR-03 pair identity; required for stage realization quality, not for stream existence.
9. **Capability Realization — NEW ROOT, optional for value streams.** Separate from Business Capability because ownership follows the realizer and the binding must survive transfer and correction independently.
10. **Metric Definition — NEW ROOT, optional for value streams.** Passes on EM-DAT-05 identity. Streams must not embed formulas; they reference pinned definitions.
11. **Value Proposition — CONTAINED, NO ROOT.** Frozen EM-STR-01 decision stands; a proposition has no lifecycle independent of the business model or offering that asserts it.
12. **Journey — NO ROOT NOW; non-normative projection; candidate parked.** Consistent with EM-TEC-06. WM-FLW-009 Journey/Trip must **not** be reused — physical trip semantics would be a category error.
13. **Process Execution — REUSE, NO ROOT.** WM-ACT-003 for definition, WM-ACT-002/WM-ACT-015 for occurrence, EM-OPS-01 already complete-reserved. Streams cite executions as realization evidence only.

---

## I. Implementation sequence

**Step 0 — Prerequisites (no allocation).** Publish the coverage frame (A), the exclusion list, and the adjudication register (H) as a frozen reviewer artefact. Resolve the pending cross-cutting contours that Value Stream depends on for correctness: EM-XCT-02 (fact ownership), EM-XCT-03 (provenance/assertions), EM-XCT-04 (time, states, versions), EM-XCT-09 (classifications/profiles, needed for the boundary-role classification), EM-XCT-10 (registration/acceptance). *Blocking risk:* allocating Value Stream before EM-XCT-04 and EM-XCT-09 would hard-code version-pinning and boundary-role semantics locally and create later migration debt. This is the one dependency I would not bypass.

**Step 1 — Outcome class vocabulary (no new root).** Publish a governed outcome-state-class scheme as a WM-KNW-018 / WM-KNW-006 instance, shared by Value Stream terminal outcomes, stage value states and EM-STR-03's `outcomeClassRef`. This removes the only semantic blocker that would otherwise push Outcome toward premature root status.

**Step 2 — Value Stream root (must-have, first and only required allocation).** Allocate under EM-STR-01 with the F1 identity, lifecycle, aggregate objects and invariants. Reuse without modification: WM-XCT-023 + WM-ORG-013 (beneficiary role), WM-ACT-015 (trigger occurrence), WM-XCT-021 (lifecycle), WM-XCT-022 (version), WM-XCT-020 (boundary-role classification), WM-XCT-037 (hand-off edges), WM-KNW-011 (goal linkage), WM-ACT-034 + WM-MAT-008 (evidence).

**Step 3 — Seed the frozen archetype set.** Register B (13 external) and C (15 internal) as stream definitions at the enterprise governing boundary, each with stages, trigger class, terminal outcome class and the gap annotations from B/C. Do **not** create variants for external/internal visibility.

**Step 4 — EM-STR-01 binding reconciliation.** Restate EM-STR-01's four candidate roots so that Value Stream is allocated, Business Model, Strategy and Strategic Scenario remain unassigned, and Value Proposition and Value Exchange are confirmed contained. No second stream-like root.

**Step 5 — Business Capability + Capability Realization (EM-STR-03).** Allocate together; then convert stage realization assertions from free references to capability-anchored references. Safe only after Step 1 (shared outcome classes).

**Step 6 — Metric Definition (EM-DAT-05).** Allocate; attach stream and stage measures by pinned definition reference. Observations remain on WM-MAT-008.

**Step 7 — Benefit realization profiles.** Activate EM-WRK-03 programme-owned benefit assertions against stream terminal outcomes; keep the EM-STR-02 outcome/benefit boundary register as the adjudication record. Revisit the two deferred EM-STR-02 identities only if programme-owned assertions prove insufficient.

**Optional later roots (do not allocate now).** Value Stream Landscape declaration (only as an EM-LND profile), User Journey (EM-TEC-06, still deferred), Stage Realization (only on demonstrated independent governance), and any Value Exchange root (only if realized-exchange mastership is ever shown to be unassignable to existing WM-ECO/WM-XCT masters — not the case today).

**Must-have vs optional summary.** Must-have: one root, Value Stream. Optional-later and already owned elsewhere: Business Capability, Capability Realization, Metric Definition. Never: Stage, Map, Portfolio, Exchange, Proposition, Journey, Process Execution, and — for now — Outcome and Benefit Realization as roots.
