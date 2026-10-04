# Verdict

Split the contour across three dispositions rather than one.

1. **Objective, Key Result, Target — profile of WM-KNW-011.** No new identity is justified: the goal record already carries identity independent of attribute values, a declared lifecycle with supersession, one accountable party, `de-record-role-code` with `de-naming-regime`, and `fd-target-value-and-baseline`. A Key Result is that record with role `key-result`, naming regime `OKR`, and measure binding made mandatory; a Target is the quantified commitment already modelled there. Splitting would duplicate identity, lifecycle and provenance machinery — the same reasoning WM-KNW-011's own boundary decision used.
2. **Observation — reuse WM-XCT-025 as a mixin, on a host this contour must name.** It supplies value, unit with version pin, method reference, GUM uncertainty, censoring, and the three time anchors. It owns no record: its adjudication states the host owns identity and lifecycle. EM-STR-02 therefore needs an outcome-observation host; the mixin alone cannot close the contour.
3. **Outcome, Benefit (expected/realised/disbenefit) and its attribution — identifier-unassigned candidates.** Nothing in the reservations masters them.
4. **Value Assessment — complete-reserved WM-ACT-034** (subject, criteria, evidence, score, conclusion), profiled so the valuation method is a declared reference, never a built-in formula.
5. **Metric Definition — out of scope**, EM-DAT-05, identifier unassigned. WM-KNW-011 explicitly disclaims indicator definitions.
6. **Deliverable and work contribution — out of scope**, EM-WRK-03; referenced only.

# Evidence

Both candidate links are `conceptual-candidate` at `index-and-publication-metadata` depth; both specs are parsed and pinned (WM-KNW-011 sha256 c89f858…, WM-XCT-025 sha256 1309429…), both `published` but `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, single-provider waiver with Grok waived, `status: candidate`, `review_state: boundary-review-required`. Both carry empty relationship contracts, so every exclusion below is declared and not yet enforceable. No semantic crosswalk has been verified; this review reads the two specs as supplied and asserts no canonical completeness and no installability.

# Identity/mastership

| Thing | Master | Independent identity |
|---|---|---|
| Objective / KR / Target | OKR and strategic-decision system | Yes — WM-KNW-011 |
| Metric Definition | Metric registry (EM-DAT-05) | Yes, elsewhere |
| Observation | Producing measurement/reporting system | Host record + WM-XCT-025 fields |
| Outcome | Outcome owner in the benefits function | Yes — new |
| Benefit (expected, realised, disbenefit) | Benefits register / portfolio | Yes — new |
| Attribution claim | Asserted by the work; adjudicated by the benefit owner | No — owned part of Benefit |
| Value Assessment | Assessment authority | Yes — WM-ACT-034 |

Outcome earns its own identity on two grounds the dossier makes testable: an outcome can exist with no objective (the negative side effect), and one outcome can serve several objectives. It is therefore neither a status on the Objective nor a field on the Observation.

Attribution deliberately gets **no** independent entry. The anti-double-counting rule (shares over one benefit and period must not exceed unity) is a consistency constraint that needs a closed transactional boundary; that boundary is the Benefit aggregate. Attribution is an owned part identified by benefit identity plus a register-issued discriminator — the pattern WM-KNW-011 already applies to restatement notes.

# Objective/KR/target

Objective states the end; it is not a metric — WM-KNW-011's measure binding is by reference only. Target = `de-target-value` + `de-comparison-operator` + `de-measure-unit` + `de-base-period` + `de-target-period`. **Gap:** `fd-measure-binding` has no version pin, so a target cannot currently pin the metric version it was set against. The profile must add a mandatory metric-definition version pin (mirroring `code-system-version-pin`) and refuse a target whose metric version is unresolvable. A metric redefinition is a methodology restatement (`de-change-class` = methodological) with `de-prior-value` retained, not a silent re-baseline.

# Outcome/observation

Outcome is the asserted change in a subject's state, distinct from the deliverable that enabled it and from the Observation that evidences it. Its lifecycle: `hypothesised → observed → contested → withdrawn`. It holds references to enabling deliverables (EM-WRK-03), to objectives it serves, and to one or more observations. Observations attach WM-XCT-025: `phenomenon-time` / `phenomenon-period` for when the change applies, `result-time` for when it was produced, `ingestion-time` for capture, plus uncertainty, censoring and `data-absent-reason`. A deliverable yields an outcome only when an observation with `result_status` ∈ {final, amended} and phenomenon time inside the outcome's window supports the change; delivery alone never does.

# Benefit attribution

Benefit is one entity with a **polarity** code (benefit / disbenefit) — a disbenefit has the same identity, lifecycle and mastership as a benefit, so it is a code, not a model. Claim state is separate: `expected → forecast → partially-realised → realised → reversed`. Each attribution part carries contributor reference, declared share with its own uncertainty interval, `attribution_method` (WRK-11 candidate), evidence references, and adjudication status. No double counting because: shares are asserted against the single benefit record; the sum of adjudicated shares per benefit per measurement period must not exceed 1; and a programme claim and its constituent project claims may not both be adjudicated for the same period — the programme either holds the benefit with project shares beneath it, or holds none.

# Value/anti-value comparison

No universal formula. Comparison runs only inside a declared Value Assessment (WM-ACT-034) naming criteria, scale and commensuration method. Benefit and disbenefit on incompatible scales are reported as a labelled pair with both scales intact; netting to a scalar requires a cited method and is itself an assessment with its own identity and uncertainty. WM-XCT-025's `assess-comparability` is advisory only, and its unresolved canonicalisation-refusal condition applies directly: ordinal, nominal and offset scales must refuse conversion rather than convert silently.

# Invariants

1. An Objective is not a metric; measures are referenced.
2. A Target pins the metric definition version; unresolvable pin ⇒ reject.
3. Realisation requires ≥1 final observation whose phenomenon time falls in the realisation window; otherwise the claim stays `expected` or `forecast`.
4. `expected` and `realised` are distinct claims; neither overwrites the other.
5. Adjudicated shares per benefit per period sum ≤ 1; programme and constituent project claims are mutually exclusive for a period.
6. Disbenefit is polarity, not a separate model; it is never netted without a declared method.
7. Absent measurement is coded (`data-absent-reason`), never zero.
8. Uncertainty travels with value and with share; aggregation must not drop it.
9. An outcome may exist with no objective and may serve several.
10. Value/anti-value carry no universal formula without a cited methodology.

# Scenario

Benefit B, +8% retention, expected 2027-Q2. Projects P1 and P2 each assert contribution: P1 claims 0.6 ± 0.15, P2 claims 0.5 ± 0.2; sum 1.1 > 1 ⇒ both stay `asserted`, benefit stays `forecast`, and the benefit owner adjudicates to 0.55 and 0.45 with intervals preserved. Measurement slips: the metric source arrives 2027-Q4 with `phenomenon-period` Q2 and `result-time` Q4. Until then B is `forecast` with `data-absent-reason = measurement-pending`, and neither project may report realisation. On arrival, +5.2% with expanded uncertainty ±1.8 (k=2): B becomes `partially-realised`, the objective's target is unmet, and status `missed` needs the observation reference, not the plan. A disbenefit D — support contacts +12% — is attributed to P1 at 1.0. D is not subtracted from B: no commensuration method links retention percentage and contact volume, so a Value Assessment records both with a stated conclusion and an explicit non-netting note. Attribution, delay and uncertainty all survive.

# Minimal profile/candidate shape

- **Profile of WM-KNW-011**: roles `objective | key-result | target`; naming regime `OKR`; mandatory measure reference **plus version pin**; attainment reference constrained to observations or assessments; restatement mandatory on metric change.
- **Host record for observations** (identifier unassigned) embedding WM-XCT-025 under a named binding profile; mandatory set = value, unit + pin, measurand, `result-time`, `result-status`, uncertainty or a restricted-uncertainty marker.
- **Outcome** (identifier unassigned): identity, subject, change statement, window, enabling-deliverable refs, objective refs, observation refs, status, provenance.
- **Benefit** (identifier unassigned): identity, polarity, kind, baseline, realisation horizon, claim state, outcome refs, owned attribution parts (contributor, share + interval, method, evidence, adjudication), restatement log.
- **Profile of WM-ACT-034** for Value Assessment: subject refs, criteria, declared method and scale, evidence, conclusion, non-netting declaration.

# Holds

Single-provider waiver on both bases; empty relationship contracts make all exclusions unenforceable; both records remain `candidate` / `boundary-review-required`; WM-KNW-011's parent link to WM-ACT-008 is contested as containment; WM-XCT-025's field-group identity is deferred; EM-DAT-05 metric mastership and benefit/value mastership are unallocated; the crosswalk is unverified. Nothing here claims canonical completeness or installability. New identifiers must be issued by the registry — none are invented above.
