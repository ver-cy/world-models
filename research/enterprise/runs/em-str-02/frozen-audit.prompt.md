You are the single frozen no-tools semantic auditor for EM-STR-02. Use only the frozen material below. Audit revision 2 for objective/metric/target, observation/outcome, Outcome/Benefit root separation, attribution, delayed measurement, uncertainty, disbenefit and Value Assessment boundaries. Confirm that the boundary register honestly rejects the combined root, allocates no identifier and claims no publication readiness. Check stable rule IDs and concrete fixtures. Return PASS or REVISE first, then one closed numbered defect checklist. Do not invent identifiers or another provider study.

===== provider-comparison.md =====
# EM-STR-02 provider comparison

Claude and Grok agree that WM-KNW-011 remains the Objective/Key Result/Target master, quantitative targets pin exact Metric Definition revisions, WM-XCT-025 has no standalone identity and is restricted to qualified observation hosts, and WM-ACT-034 is the Value Assessment activity. Both reject delivery, planned effects and KR attainment as proof of realised Outcome or Benefit.

Both providers reject the original combined Outcome and Benefit aggregate. Claude describes Outcome and Benefit as distinct identifier-unassigned candidates; Grok defers their allocation until the WM-ACT-029 and EM-WRK-03 ownership crosswalk. The reconciled artifact therefore becomes a non-allocating boundary register: it records two separate potential roots, allocates neither, and forbids a combined write boundary.

Attribution Claim remains a Benefit-owned revisable assertion. Adjudicated shares cannot exceed one; they need not total one and residual unattributed value is explicit. Benefit and Disbenefit use the same candidate record shape with polarity but remain separately identifiable records. Counterfactual-only Benefit and intended-versus-realised record identity remain holds. No ID or publication readiness is claimed.


===== claude-study.raw.md =====
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


===== grok-study.raw.md =====
# Grok independent study — EM-STR-02

## Verdict
Conditional accept of the proposed profiles; reject one identifier-unassigned Outcome and Benefit Realization aggregate. Profile WM-KNW-011 for Objective, Key Result and Target with mandatory Metric Definition revision pins. Restrict WM-XCT-025 to WM-MAT-008 observation hosts as an EM-STR-02 usage rule, not a settled catalogue fact. Profile WM-ACT-034 for Value Assessment. Reference EM-DAT-05 for metric definitions and EM-WRK-03 for work/deliverables. Outcome and Benefit should not remain one aggregate. Identity for those classes is deferred. No identifiers are minted.

## Identity / mastership
WM-KNW-011 owns the desired-end-state record but not metrics, observations, evaluation verdicts, actions, benefits or realized outcomes. Metric master is EM-DAT-05. WM-XCT-025 is a mixin with no standalone identity and its CHILD link to WM-MAT-008 is unfrozen. Value Assessment is a WM-ACT-034 profile. Outcome and Benefit have no assigned identity here. WM-ACT-029 and EM-WRK-03 are possible benefit-owner homes, so a third unassigned bag would create a third home.

## Objective / KR / target
Profile WM-KNW-011. A Key Result is a measurable-progress role under an Objective with mandatory quantitative binding. Target uses baseline, base period, value, unit, operator, horizon and milestones. Every quantitative field pins an EM-DAT-05 MetricDefinition revision. Metric change creates a successor binding and comparability note. KR hit is an external evaluation and never proves Outcome or Benefit.

## Outcome / observation
Observation is a measurement fact. Outcome is an asserted subject state-change and horizon, evidenced by observations over time. One observation or deliverable acceptance is not an Outcome. Intended end-state stays on WM-KNW-011. Realized, claimed, disputed or superseded Outcome is a separate identity whose allocation is deferred pending crosswalk to WM-ACT-029 and EM-DAT-05. Outcome cites observations; it does not embed WM-XCT-025.

## Benefit attribution
Reject packing Benefit, Disbenefit and Attribution Claim into the Outcome write boundary. Outcome and Benefit differ in identity, lifecycle, mastership and N:M multiplicity. Claims are revisable without rewriting Outcome or Observation. One Benefit is named once; Attribution Claims are benefit-owned parts with contributor, method, as-of, confidence/interval, optional share and causal limit. Shares need not total one; residual unattributed is required. Program and project must not mint duplicate realised Benefits. Disbenefit is a first-class value record, not a negative field on an intended Benefit. A Benefit may cite Outcomes or a counterfactual assumption; do not mint a fake Outcome.

## Value / anti-value
No universal formula. WM-ACT-034 Value Assessment names a version-pinned valuation profile, cites observations, and may conclude valued, anti-valued, insufficient evidence or incomparable scales. Abstention is first-class. Netting is an assessment conclusion under a declared method. Collision with WM-ACT-029 benefit-owner semantics remains a hold.

## Invariants
A goal is not a metric. Target pins metric version. Deliverable done, planned effect or KR hit does not prove realized Benefit. The same Benefit is not separately realised by program and project. Attribution revision does not rewrite Outcome or Observation. Uncertainty is mandatory on claims and assessments; residual unattributed is allowed. Net value loads related Disbenefits or declares them out of scope. WM-XCT-025 is not adopted on intent, assessment or unassigned Outcome/Benefit records.

## Scenario
Objective/KR/Target pins MetricDefinition R. Projects A and B accept deliverables, but Benefit B remains unrealised. Delayed observations show handling time down and error rate up, producing Outcome O1 and O2. B receives two uncertain claims with residual open. Program points to B rather than minting B-prime. Disbenefit D is recorded for O2. WM-ACT-034 assessment under profile P@version concludes net value with uncertainty or incomparable; delivery acceptance is not evidence.

## Blockers
Outcome and Benefit identity remain deferred until WM-ACT-029/EM-WRK-03 crosswalk. WM-KNW-011 relationships are empty; TargetValue is dual-homed; WM-XCT-025 to WM-MAT-008 CHILD is unfrozen; WM-ACT-034 lacks a published Value Assessment profile; intended versus realized Benefit and counterfactual-only Benefit remain open. Review is structural and not canonical or installable.


===== candidate-allocation-offline\allocation-candidate.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-STR-02",
  "proposedName": "Outcome and Benefit Boundary Register",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "allocationBoundaryState": "deferred-two-roots-combined-root-rejected",
  "decision": "BOUNDARY REGISTER; NO MODEL ALLOCATION",
  "canonicalPublishable": false,
  "candidateRevision": 2,
  "clusterIdentityTest": {
    "scope": "Research register only; no aggregate root is asserted.",
    "perObject": {
      "Outcome": {
        "candidateIdentity": [
          "outcomeId"
        ],
        "mastership": "outcome owner / measurement interpretation authority; unresolved",
        "lifecycle": [
          "hypothesised",
          "claimed",
          "observed",
          "contested",
          "withdrawn",
          "superseded"
        ]
      },
      "Benefit": {
        "candidateIdentity": [
          "benefitId"
        ],
        "mastership": "benefits register or value office; unresolved against WM-ACT-029 and EM-WRK-03",
        "lifecycle": [
          "expected",
          "forecast",
          "measurement-pending",
          "partially-realised",
          "realised",
          "reversed",
          "closed",
          "superseded"
        ]
      }
    }
  },
  "boundary": {
    "owns": [
      "research boundary decisions only"
    ],
    "references": [
      {
        "target": "WM-KNW-011",
        "purpose": "Objective, Key Result and Target"
      },
      {
        "target": "EM-DAT-05",
        "purpose": "Metric Definition revision"
      },
      {
        "target": "WM-MAT-008",
        "purpose": "qualified Observation host"
      },
      {
        "target": "WM-XCT-025",
        "purpose": "observation mixin usage rule only"
      },
      {
        "target": "WM-ACT-034",
        "purpose": "Value Assessment activity"
      },
      {
        "target": "WM-ACT-029",
        "purpose": "results-chain and benefit-owner crosswalk"
      },
      {
        "target": "EM-WRK-03",
        "purpose": "program, work and deliverable contribution"
      }
    ],
    "excludes": [
      "combined Outcome and Benefit aggregate",
      "metric or observation mastership",
      "work or deliverable identity",
      "automatic realization or scalar netting"
    ]
  },
  "potentialRoots": {
    "Outcome": {
      "allocation": "deferred",
      "identity": "subject plus state-of-interest plus horizon",
      "owns": [
        "state-change assertion",
        "status and assertion history",
        "observation citations"
      ]
    },
    "Benefit": {
      "allocation": "deferred",
      "identity": "beneficiary plus value-kind plus valuation profile plus period",
      "owns": [
        "expected and realized claim history",
        "polarity",
        "Benefit-owned Attribution Claims",
        "residual unattributed contribution"
      ]
    }
  },
  "invariantRules": [
    {
      "id": "EM-STR-02.BR-01",
      "text": "Objective, Metric Definition, Target, Observation, Outcome, Benefit and Deliverable remain distinct identities or referenced subjects."
    },
    {
      "id": "EM-STR-02.BR-02",
      "text": "WM-KNW-011 remains the Objective, Key Result and Target master; a Key Result is a measurable-progress role and not a new root."
    },
    {
      "id": "EM-STR-02.BR-03",
      "text": "Every quantitative target pins an exact Metric Definition revision, unit, operator, baseline period and target period; latest or bare-name references are invalid."
    },
    {
      "id": "EM-STR-02.BR-04",
      "text": "Metric redefinition never silently rewrites a target; it creates a successor binding with retained prior value and comparability note."
    },
    {
      "id": "EM-STR-02.BR-05",
      "text": "WM-XCT-025 is used only on qualified WM-MAT-008 observation hosts under an explicit usage rule and is never embedded in goals, assessments, Outcomes or Benefits."
    },
    {
      "id": "EM-STR-02.BR-06",
      "text": "Observation, deliverable acceptance, planned effect and KR attainment never by themselves prove an Outcome or realised Benefit."
    },
    {
      "id": "EM-STR-02.BR-07",
      "text": "Outcome and Benefit are separate potential roots with different identity, lifecycle and mastership; this boundary register allocates neither."
    },
    {
      "id": "EM-STR-02.BR-08",
      "text": "An Outcome asserts a subject state-change and horizon and cites qualified observations without owning measurement facts."
    },
    {
      "id": "EM-STR-02.BR-09",
      "text": "A Benefit identifies beneficiary, value kind, valuation profile and Outcome or counterfactual basis and is never owned by an Outcome write boundary."
    },
    {
      "id": "EM-STR-02.BR-10",
      "text": "Attribution Claim is a Benefit-owned revisable assertion and never rewrites Outcome, Observation or contributing work."
    },
    {
      "id": "EM-STR-02.BR-11",
      "text": "Adjudicated attribution shares for one Benefit and period cannot exceed one; residual unattributed contribution is explicit and permitted."
    },
    {
      "id": "EM-STR-02.BR-12",
      "text": "Program and constituent projects reference one Benefit identity and never create duplicate realised-Benefit records for the same value and period."
    },
    {
      "id": "EM-STR-02.BR-13",
      "text": "Benefit and Disbenefit are separately identifiable value records using a polarity code; neither is silently netted into the other."
    },
    {
      "id": "EM-STR-02.BR-14",
      "text": "Missing or delayed measurement carries an explicit absent reason and remains forecast or measurement-pending; it is never represented as zero or realised."
    },
    {
      "id": "EM-STR-02.BR-15",
      "text": "Value Assessment pins criteria, valuation profile, method, scale, evidence and uncertainty and may conclude valued, anti-valued, insufficient-evidence or incomparable."
    },
    {
      "id": "EM-STR-02.BR-16",
      "text": "Net value requires a declared commensuration method and loads related Disbenefits or explicitly declares them out of scope."
    },
    {
      "id": "EM-STR-02.BR-17",
      "text": "Uncertainty travels with observations, attribution claims and assessment conclusions and is never stripped by aggregation or comparison."
    },
    {
      "id": "EM-STR-02.BR-18",
      "text": "Superseded Objective bindings, Outcome assertions, Benefit claims and assessment conclusions remain resolvable and are never overwritten or recycled."
    }
  ],
  "holds": [
    "No model or registry identifier is allocated or guessed.",
    "Outcome and Benefit allocation is deferred pending WM-ACT-029 and EM-WRK-03 ownership crosswalk.",
    "The original combined aggregate is rejected.",
    "TargetValue ownership and WM-XCT-025 to WM-MAT-008 relation are unfrozen.",
    "WM-ACT-034 lacks an approved Value Assessment profile.",
    "Counterfactual-only Benefit and intended-versus-realised identity remain unresolved.",
    "Package conversion and live conformance are pending."
  ],
  "publicationStatement": "Research boundary register only; not canonically publishable, installable, allocated or verified."
}


===== candidate-allocation-offline\profile-candidate.json =====
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-STR-02",
  "name": "Enterprise Objectives, Targets and Value Assessment",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "candidateRevision": 2,
  "canonicalPublishable": false,
  "bases": [
    "WM-KNW-011",
    "WM-ACT-034"
  ],
  "references": [
    "EM-DAT-05",
    "WM-MAT-008",
    "WM-XCT-025",
    "WM-ACT-029",
    "EM-WRK-03"
  ],
  "constraintRules": [
    {
      "id": "EM-STR-02.EP-01",
      "text": "WM-KNW-011 is profiled for objective, key-result and target roles without creating another root."
    },
    {
      "id": "EM-STR-02.EP-02",
      "text": "Key Result requires an exact Metric Definition revision pin and quantitative target parameters."
    },
    {
      "id": "EM-STR-02.EP-03",
      "text": "Metric change creates a traceable successor binding and never silently rebases history."
    },
    {
      "id": "EM-STR-02.EP-04",
      "text": "WM-XCT-025 is a usage reference restricted to WM-MAT-008 observation hosts, not a profile base or standalone record."
    },
    {
      "id": "EM-STR-02.EP-05",
      "text": "WM-ACT-034 Value Assessment cites Benefits, Disbenefits, Outcomes and observations by reference and pins valuation profile and method."
    },
    {
      "id": "EM-STR-02.EP-06",
      "text": "Assessment may abstain for insufficient evidence or incomparable scales and never treats delivery acceptance as evidence."
    }
  ],
  "holds": [
    "No model or registry identifier is allocated or guessed.",
    "Outcome and Benefit allocation is deferred pending WM-ACT-029 and EM-WRK-03 ownership crosswalk.",
    "The original combined aggregate is rejected.",
    "TargetValue ownership and WM-XCT-025 to WM-MAT-008 relation are unfrozen.",
    "WM-ACT-034 lacks an approved Value Assessment profile.",
    "Counterfactual-only Benefit and intended-versus-realised identity remain unresolved.",
    "Package conversion and live conformance are pending."
  ],
  "publicationStatement": "Research boundary register only; not canonically publishable, installable, allocated or verified."
}


===== candidate-allocation-offline\fixtures.json =====
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "contourId": "EM-STR-02",
  "candidateName": "Outcome and Benefit Boundary Register",
  "candidateRevision": 2,
  "canonicalPublishable": false,
  "executable": false,
  "publicationStatement": "Research boundary register only; not canonically publishable, installable, allocated or verified.",
  "cases": [
    {
      "id": "EM-STR-02.FX-001",
      "kind": "negative",
      "input": "A record violates this boundary: Objective, Metric Definition, Target, Observation, Outcome, Benefit and Deliverable remain distinct identities or referenced subjects.",
      "expect": "Reject under EM-STR-02.BR-01.",
      "rules": [
        "EM-STR-02.BR-01"
      ]
    },
    {
      "id": "EM-STR-02.FX-002",
      "kind": "negative",
      "input": "A record violates this boundary: WM-KNW-011 remains the Objective, Key Result and Target master; a Key Result is a measurable-progress role and not a new root.",
      "expect": "Reject under EM-STR-02.BR-02.",
      "rules": [
        "EM-STR-02.BR-02"
      ]
    },
    {
      "id": "EM-STR-02.FX-003",
      "kind": "negative",
      "input": "Target T cites metric name Retention without revision, unit or periods.",
      "expect": "Reject under EM-STR-02.BR-03.",
      "rules": [
        "EM-STR-02.BR-03"
      ]
    },
    {
      "id": "EM-STR-02.FX-004",
      "kind": "negative",
      "input": "A record violates this boundary: Metric redefinition never silently rewrites a target; it creates a successor binding with retained prior value and comparability note.",
      "expect": "Reject under EM-STR-02.BR-04.",
      "rules": [
        "EM-STR-02.BR-04"
      ]
    },
    {
      "id": "EM-STR-02.FX-005",
      "kind": "negative",
      "input": "Outcome O embeds WM-XCT-025 fields directly.",
      "expect": "Reject under EM-STR-02.BR-05.",
      "rules": [
        "EM-STR-02.BR-05"
      ]
    },
    {
      "id": "EM-STR-02.FX-006",
      "kind": "negative",
      "input": "Project delivery D is accepted and Benefit B is marked realised with no observation.",
      "expect": "Reject under EM-STR-02.BR-06.",
      "rules": [
        "EM-STR-02.BR-06"
      ]
    },
    {
      "id": "EM-STR-02.FX-007",
      "kind": "negative",
      "input": "One transaction creates a combined OutcomeBenefit root.",
      "expect": "Reject under EM-STR-02.BR-07.",
      "rules": [
        "EM-STR-02.BR-07"
      ]
    },
    {
      "id": "EM-STR-02.FX-008",
      "kind": "negative",
      "input": "A record violates this boundary: An Outcome asserts a subject state-change and horizon and cites qualified observations without owning measurement facts.",
      "expect": "Reject under EM-STR-02.BR-08.",
      "rules": [
        "EM-STR-02.BR-08"
      ]
    },
    {
      "id": "EM-STR-02.FX-009",
      "kind": "negative",
      "input": "A record violates this boundary: A Benefit identifies beneficiary, value kind, valuation profile and Outcome or counterfactual basis and is never owned by an Outcome write boundary.",
      "expect": "Reject under EM-STR-02.BR-09.",
      "rules": [
        "EM-STR-02.BR-09"
      ]
    },
    {
      "id": "EM-STR-02.FX-010",
      "kind": "negative",
      "input": "Attribution revision mutates the cited Outcome.",
      "expect": "Reject under EM-STR-02.BR-10.",
      "rules": [
        "EM-STR-02.BR-10"
      ]
    },
    {
      "id": "EM-STR-02.FX-011",
      "kind": "negative",
      "input": "Two adjudicated project shares are 0.6 and 0.5 with residual hidden.",
      "expect": "Reject under EM-STR-02.BR-11.",
      "rules": [
        "EM-STR-02.BR-11"
      ]
    },
    {
      "id": "EM-STR-02.FX-012",
      "kind": "negative",
      "input": "Program and project each mint a realised copy of Benefit B.",
      "expect": "Reject under EM-STR-02.BR-12.",
      "rules": [
        "EM-STR-02.BR-12"
      ]
    },
    {
      "id": "EM-STR-02.FX-013",
      "kind": "negative",
      "input": "Support-contact Disbenefit is silently subtracted from retention Benefit.",
      "expect": "Reject under EM-STR-02.BR-13.",
      "rules": [
        "EM-STR-02.BR-13"
      ]
    },
    {
      "id": "EM-STR-02.FX-014",
      "kind": "negative",
      "input": "Measurement is delayed and realised value is stored as zero.",
      "expect": "Reject under EM-STR-02.BR-14.",
      "rules": [
        "EM-STR-02.BR-14"
      ]
    },
    {
      "id": "EM-STR-02.FX-015",
      "kind": "negative",
      "input": "A record violates this boundary: Value Assessment pins criteria, valuation profile, method, scale, evidence and uncertainty and may conclude valued, anti-valued, insufficient-evidence or incomparable.",
      "expect": "Reject under EM-STR-02.BR-15.",
      "rules": [
        "EM-STR-02.BR-15"
      ]
    },
    {
      "id": "EM-STR-02.FX-016",
      "kind": "negative",
      "input": "Net value excludes a known Disbenefit without declaration.",
      "expect": "Reject under EM-STR-02.BR-16.",
      "rules": [
        "EM-STR-02.BR-16"
      ]
    },
    {
      "id": "EM-STR-02.FX-017",
      "kind": "negative",
      "input": "Aggregation drops all uncertainty intervals.",
      "expect": "Reject under EM-STR-02.BR-17.",
      "rules": [
        "EM-STR-02.BR-17"
      ]
    },
    {
      "id": "EM-STR-02.FX-018",
      "kind": "negative",
      "input": "Superseded Benefit identifier is recycled.",
      "expect": "Reject under EM-STR-02.BR-18.",
      "rules": [
        "EM-STR-02.BR-18"
      ]
    },
    {
      "id": "EM-STR-02.FX-019",
      "kind": "positive",
      "input": "Projects A and B reference one Benefit B with adjudicated shares 0.45 and 0.35 and residual 0.20; delayed observations retain phenomenon and result times plus uncertainty.",
      "expect": "Accept one Benefit, two claims, explicit residual and preserved timing/uncertainty.",
      "rules": [
        "EM-STR-02.BR-11",
        "EM-STR-02.BR-12",
        "EM-STR-02.BR-14",
        "EM-STR-02.BR-17"
      ]
    },
    {
      "id": "EM-STR-02.FX-020",
      "kind": "positive",
      "input": "Value Assessment P@3 reports retention Benefit and support-contact Disbenefit as incomparable labelled dimensions.",
      "expect": "Accept abstention/non-netting with pinned methodology and both records retained.",
      "rules": [
        "EM-STR-02.BR-13",
        "EM-STR-02.BR-15",
        "EM-STR-02.BR-16"
      ]
    }
  ]
}
