You are the single frozen independent semantic auditor for EM-PEO-09. Use only the material below. Do not use tools or browse. Audit the revision-2 candidate for identity, lifecycle, mastership, boundary completeness, temporal/currency/FTE semantics, benefit/payroll/payment separation, privacy reconstruction resistance, stable rule IDs and fixture binding. Verify that no identifier is allocated and no publication readiness is claimed. Return PASS or REVISE first, then a closed numbered checklist of defects. Do not propose a fifth root unless an independent identity and lifecycle is strictly necessary.



===== provider-comparison.md =====
# EM-PEO-09 provider comparison

Claude and Grok agree on exactly four identifier-unassigned roots: Compensation Band, Compensation Assignment, Benefit Plan and Benefit Enrollment. Both reject Compensation Review as a root, retain authoritative review outcomes on WM-REC-010, limit WM-ECO-031 to payroll calculation and payslip facts, and preserve WM-ECO-009 payment and settlement authority. No identifier is allocated.

The reconciled candidate adopts Grok's sharper rule that an assignment may be off-band and that position-in-range and compa-ratio are observations. It adopts Claude's explicit amount tuple, jurisdiction separation and employee-versus-public-benefit boundary. Eligibility remains plan-owned; election and coverage remain enrollment-owned; claim, remittance and privacy-floor algorithms remain unowned. Aggregate privacy rules are declarative because WM-XCT-005 has no current specification and no numeric threshold is invented.


===== claude-study.raw.md =====
# Verdict

Four new roots, one rejection, no identifiers allocated.

- **CompensationBand** — NEW root. Pay structure/range scheme: versioned band definitions with ordered or overlapping ranges, keyed to a grade-scheme version. Not WM-ORG-004, which explicitly excludes "compensation plan and pay-structure master data (grade ladders and steps are referenced by key)".
- **CompensationAssignment** — NEW root. Person/engagement-scoped compensation terms with effective-dated components. Neither WM-ORG-005 (holds *references* to remuneration masters) nor WM-ECO-031 (holds run-scoped term *bindings* as calculation inputs) owns the term master.
- **BenefitPlan** — NEW root, with versioned eligibility rule as an owned component, not a separate root (parity with EM-FIN-05 Allocation Rule).
- **BenefitEnrollment** — NEW root, owning election and coverage periods as components.
- **CompensationReview** — REJECTED as a root. The authoritative outcome profiles WM-REC-010; the periodic cycle (population, budget, guidelines, calibration) is a process/case contour, deferred. This follows EM-PEO-08, which created no calibration root.

Profile WM-ECO-031 for calculation and payslip. Reuse WM-ECO-009 for payment, WM-ECO-004 for currency and FX, WM-ECO-002 for in-kind valuation, WM-XCT-003 for aggregate disclosure shape.

# Evidence

WM-ECO-031's own boundary decision resolves it as a "payroll execution and compensation-result aggregate," and its publication holds state that "compensation plans, agreements, equity administration and non-payroll rewards may require separate canonical models." Its deferred research asks to "evaluate separate canonical compensation-plan… models." Its out-of-scope forbids owning Benefit Plan masters and forbids "treating compensation term as earned pay."

WM-ORG-005 lists "remuneration, benefit, training and expense references" as *bindings* with effective time and disclosure class, and excludes payroll/compensation lifecycles. WM-ORG-004 owns "pay range and transparency obligations" at seat level while excluding the ladder itself. Both bases therefore point outward for the term master; neither claims it.

WM-POL-012 and WM-XCT-005 are reservations with no current spec, so they cannot be profiled — only referenced.

# Identity/mastership

Distinct identities: band scheme → band version → range; position pay range (seat attribute, WM-ORG-004); compensation assignment → component version; employment relationship (WM-ORG-005); review decision (WM-REC-010); payroll run → payee result → revision (WM-ECO-031); earning component; statutory base; deduction; employer contribution; pay statement; payment instruction → execution → settlement (WM-ECO-009); statutory contribution remittance and filing; benefit plan version → eligibility rule version; enrollment → election → coverage period; claim; valuation assertion (WM-ECO-002); aggregate disclosure (WM-XCT-003).

Mastership: compensation authority masters bands and assignments; benefits authority masters plans and enrollments; payroll steward masters runs and results; finance masters payments and settlement; tax authority masters filing acceptance. No downstream record proves an upstream authority.

# Band/range

A band is a reusable structure: minimum, midpoint/reference, maximum, currency, unit, period, effective window, geography/market differential, authority. It is not an entitlement and not an individual assignment. A position range is a seat-scoped reference to a band version (WM-ORG-004) plus any seat-specific override. Band membership never implies an occupant's pay; an occupant may sit outside range with a recorded exception. Bands are keyed to a grade-scheme version (EM-PEO-08 Grade Scheme candidate) but are a distinct axis from grade, proficiency and performance rating.

# Assignment/components

CompensationAssignment binds one worker in one engagement/position context and owns typed, independently effective-dated components: base salary/wage, allowance, variable/target incentive, commission plan participation, equity grant reference, in-kind benefit. Each component pins amount or rate, currency (WM-ECO-004), unit/basis (hour, month, annum, unit of output), period, frequency, FTE and working-time normalization basis (WM-ORG-004 capacity, WM-ORG-005 working-time pattern), source authority and authorizing decision (WM-REC-010). Components carry band reference and compa-ratio basis where applicable. An assignment authorizes possible remuneration; it never asserts earned pay.

# Review/decision

A review is an occasion; the decision is the record. Each authorized outcome is a WM-REC-010 decision citing authority, delegation limit, rationale, evidence and effective date, producing a successor assignment component version. Effective date is distinct from decision date and from communication date. Reviews may produce no change; nil outcomes are recorded, not omitted. A decision alone changes no payroll result: WM-ECO-031 must ingest the amended component under its own effective-dating and proration rules.

# Benefit plan/enrollment

BenefitPlan owns plan identity, versions, sponsor, jurisdiction profile, coverage categories, cost-sharing structure, carrier/provider reference, and versioned eligibility rules (service, hours, class, dependent definitions). BenefitEnrollment independently owns the worker's election, election window and reason (open enrollment, life event), dependent coverage, coverage start/end, waiver, and suspension during unpaid leave. Enrollment lifecycle is independent of payroll: enrollment can exist with no deduction, and coverage can continue while payroll produces no result. Claims/use are a separate insurance-claim subject with no owner in this dossier.

**Employee benefit vs WM-POL-012.** Employer-sponsored benefit: sponsor is the employer, eligibility derives from employment/assignment, funding is employer/worker contribution, and remedy is contractual. WM-POL-012 public benefit: state or social authority, statutory eligibility (residency, need, status), public funding, administrative decision and appeal (WM-POL-017). They are never substituted; a statutory scheme administered through payroll remains a public program with a contribution obligation, not an employee plan.

# Payroll/payment

Profile WM-ECO-031 for run and payee-result calculation, earning components, taxable/pensionable/insurable bases, deductions, employer contributions, net pay, employer cost, pay statement issuance and statutory filing projection. Payslip issuance does not prove receipt. Net pay does not prove payment; payment instruction, execution, rejection, return and settlement are WM-ECO-009 facts, and settlement finality discharges the obligation. Statutory contribution remittance is filed under WM-ECO-031 and settled under WM-ECO-009; submission never proves authority acceptance. In-kind and equity valuation is a WM-ECO-002 value assertion referenced by the payroll input, not computed in payroll.

# Currency/time

Every amount pins currency code with code-system version; assignments are held in their original currency. Conversion is a derived assertion recording rate, rate type, quotation direction, determination time, source authority and rounding, per WM-ECO-004's prohibition on derived inverse rates and its publisher fitness caveat. Silent conversion is rejected. Distinct times: effective, decided, communicated, earning, pay period, cutoff, calculation, payday, settlement, observation, knowledge. Mid-period changes are effective-dated component successors; payroll prorates by declared working-time basis and records the proration input.

# Aggregation/privacy

Aggregate publishing uses a WM-XCT-003 aggregate-only shape: declared grain, measures, period, and a mandatory cohort-floor reference. Floor computation, re-identification risk and repeated-query budget accounting belong to WM-XCT-005, which has no current spec — so differencing and composition resistance are asserted, not enforced. Required controls: minimum cohort size, complementary suppression against differencing across overlapping cohorts, release-set linkability declaration, join-key withholding, uniform response across empty/refused/suppressed, and governed suppression with recorded authority. Every served projection emits the provenance tuple to the access-audit model (not in dossier). Pay-gap indicators may profile WM-MAT-008 as measured observations, with its registry-placement hold noted.

# Acceptance scenario

Part-time worker, 0.6 FTE, monthly base in EUR plus a USD allowance. Mid-period, a review decision raises base effective the 16th. Result: two effective-dated base component versions; payroll produces one payee result with two prorated earning components, each pinning currency, period and FTE basis; the USD allowance converts with recorded rate and time. Benefit enrollment is unchanged and its coverage continues though the deduction differs. A requested department average over a two-person cohort is refused by the floor; the same measure requested for a five-person cohort and then a four-person subset is suppressed by complementary suppression, since differencing would isolate one person. Refusal and suppression are logged identically.

# Invariants

1. Every amount pins currency, unit/basis, period, frequency, FTE/working-time normalization and source authority.
2. A band or range is never an individual assignment.
3. Payment facts originate from financial sources; net pay, payslip and filing prove nothing about settlement or acceptance.
4. Terms, inputs, calculations, decisions, payments and disclosures are separate assertions.
5. Multi-currency amounts are never silently converted; FX records source, direction and time.
6. Mid-period changes append effective-dated successors; originals remain resolvable.
7. Benefit enrollment and coverage are independent of payroll production.
8. Employee benefit plans are never WM-POL-012 public programs.
9. Aggregates require a cohort floor plus differencing and repeated-query controls, with governed suppression and audit.
10. Absence of pay data is unknown, never zero.

# Minimal model set

New roots (unallocated): CompensationBand, CompensationAssignment, BenefitPlan (with eligibility-rule component), BenefitEnrollment (with coverage-period component). Profiles: WM-ECO-031 (calculation, payslip, statutory projection), WM-REC-010 (compensation decision), WM-XCT-003 (aggregate-only shape), WM-MAT-008 (indicator observations, cautioned). Reuse: WM-ORG-005, WM-ORG-004, WM-ECO-004, WM-ECO-009, WM-ECO-002. Reference-only: WM-XCT-005, WM-POL-012.

# Holds

Every base is a reviewable draft with `publishableCanonical: false`; WM-ECO-031, WM-ORG-005 and WM-ECO-002 carry single-provider waivers and absence-of-external-review holds. The frozen relation ledger contains no WM-ECO-031 edges, so the parent signal to WM-ORG-005 and all proposed edges remain unsettled. Relation/spec gaps: WM-XCT-005 and WM-POL-012 have no specs; access-audit (WM-XCT-004), ownership (WM-XCT-001), consent (WM-XCT-002) and sensitivity classification (WM-XCT-020) are referenced by WM-XCT-003 but absent from the dossier; no owner exists for benefit claims, insurance carrier contracts, equity-plan administration, market survey data, or the grade-scheme candidate from EM-PEO-08. WM-ECO-031's scope statement claims ownership of compensation terms while its boundary notes and out-of-scope treat them as external — an unresolved overlap that must be narrowed to run-scoped bindings before the assignment root is registered. Jurisdictional payroll, tax, benefit and pay-transparency profiles, crosswalks, immutable pins and fixtures are unverified. No canonical completeness, installability or publication readiness is claimed.


===== grok-study.raw.md =====
# Grok independent study — EM-PEO-09

## Verdict
Conditional accept of the proposal. Accept identifier-unassigned roots CompensationBand, CompensationAssignment, BenefitPlan, BenefitEnrollment. Keep plan eligibility and enrollment coverage as owned components. Reject CompensationReview as a root; profile authoritative outcomes on WM-REC-010. Profile WM-ECO-031 for payroll calculation and payslip as distinct faces. Reuse WM-ECO-009, WM-ECO-004, WM-ECO-002 and WM-XCT-003 without re-rooting. Allocate no identifier. Do not claim publication readiness. Employee benefits are not Public Benefit/Program. Privacy Aggregation Floor remains a reservation.

## Strongest evidence
The mandated separations already have homes: band is policy range; assignment is individual terms; employment and position are existing drafts; review is a decision; payroll calculation/payslip is WM-ECO-031; payment and remittance are settlement; eligibility, enrollment, coverage, claim and valuation are different facts; aggregates are projections. Collapsing any pair fails amount pinning, mid-period versioning, or coverage-without-pay.

## Strongest counterexample
A model that treats band min/max as the worker's terms, lets a review overwrite assignment history, equates payslip with payment, binds medical coverage to the payroll calendar, or publishes two overlapping department-band aggregates that differ by one person. That model cannot survive the combined test below.

## Identity/mastership
Band: compensation-policy master, organization-scoped, versioned; not person-owned. Assignment: HR/comp-admin master; one identity per concurrent Employment/Position binding; mid-period change versions that identity; dual employment yields distinct identities. Plan: sponsor/benefits-admin master. Enrollment: benefits-admin master, person+plan+period+election. Review outcome mastership stays on WM-REC-010. Payroll-engine masters calc/payslip; payment master stays on Payment/WM-XCT-003. Assignment does not own worker, employment, payroll result or payment.

## Band/range
Range is not an assignment and not a payable. Range points are Money amounts. Assignment may omit a band (off-band allowed) or reference one band per effective interval and still sit outside min/max. Occupancy, compa-ratio and position-in-range are Observation/Measurement, not band attributes. Mid-period band change versions the band only. Band statistics are not assignment facts.

## Assignment/components
Owned components only: base, allowance, differential, target variable. Incentive vehicles stay components unless they have an independent eligibility population (then Plan pattern; no fifth root here). References Employment and/or Position; optional Band; optional authorized-by WM-REC-010. Not employment, position, band, calc, payslip, payment or remittance.

## Review/decision
Reject CompensationReview as root. WM-REC-010 authorizes, rejects or amends a proposal for an assignment (and optionally a band structure). Proposed terms live on the decision; authorized terms live on a successor assignment version. Unapplied recommendation stays on the decision. Calibration paths are decision typology, not PEO roots.

## Benefit plan/enrollment
Accept both roots. Eligibility is owned on Plan, not a root and not an enrollment. Coverage is owned on Enrollment, not a root and not a claim. Enrollment requires Plan; may reference Employment and may outlive it (leave, continuation, retiree medical). Plan version is not the enrollment snapshot. Dependents, tier, waiver and default-enroll are enrollment/coverage states. Claim is out of this EM. Valuation is Price/Valuation, not Plan or Enrollment. Employee BenefitPlan is not a Public Benefit/Program reservation.

## Payroll/payment
WM-ECO-031: calculation is determination; payslip is worker-facing statement of that determination. Payslip is not Payment and not aggregate Projection/Disclosure Policy. Payroll result is not payment. Payment settles an obligation; it does not create terms, coverage or the obligation. Statutory remittance differs from net-pay settlement and from claim. Off-cycle correction: revised calc is not a payment reversal. Deduction on a payslip is not proof of coverage.

## Currency/time
Every amount pins currency, basis, period, frequency, FTE normalization and source. Assignment effective interval differs from payroll period, payment value-date, enrollment/coverage interval, review timestamp and remittance due date. Mid-period change needs versioned terms plus explicit proration. Frequency conversion and FX conversion are Price/Valuation plus Observation/Measurement, not identity rewrites. Assignment, calc, settlement and remittance currencies may all differ. FTE applies to pay comparison; coverage FTE is independent.

## Aggregation/privacy
Aggregates are projections under Projection/Disclosure Policy, not attributes of Band, Assignment, Plan or Enrollment. Releases must resist singleton, differencing, repeated-query and join attacks. Privacy Aggregation Floor has no spec: invariants can be stated; k, suppression and noise cannot.

## Scenario
Worker W, 0.6 FTE. Band B: USD 100,000–140,000 FTE-annual. Assignment A1: USD 72,000 actual annual. Mid-period WM-REC-010 decision D authorizes A2: EUR 5,500 per month actual, FTE 0.8. Payroll period P spans A1 and A2. Payslip prorates USD and EUR days with explicit FX; net is not settlement. Payment settles later in GBP. Remittance uses another basis and due date. Medical Plan remains elected; coverage stays 1.0 family through an unpaid gap in P; no claim. Employer-cost valuation is a separate observation. Aggregates G1 (department by band) and G2 (department by band by FTE) differ by exactly W; disclosure must refuse G2 or both.

## Invariants
1. Band range is never an assignment and never payable.
2. Assignment is individual terms, not employment, position, band or payroll result.
3. Review is not a root; WM-REC-010 authorizes; it is not the assignment.
4. Payroll calc/payslip is not payment and not remittance.
5. Payment extinguishes a payable; it does not create terms or coverage.
6. BenefitPlan is not a Public Benefit/Program.
7. Eligibility is owned on Plan; it is not enrollment.
8. Enrollment is election; coverage is owned; neither is a claim.
9. Coverage may be active when pay is zero and when no payroll period exists.
10. Every amount pins currency, basis, period, frequency, FTE normalization and source.
11. FX and frequency conversions are derived observations, not identity rewrites.
12. Mid-period change versions terms; it does not overwrite history.
13. Aggregates are disclosure projections, not root attributes.
14. A singleton aggregate, or one that isolates a person by difference, join or repeated query, must not be released.
15. Off-band assignment is valid.
16. Enrollment may outlive active employment.

## Minimum model set
Unassigned roots: CompensationBand, CompensationAssignment, BenefitPlan, BenefitEnrollment. Owned: range points; assignment components; plan eligibility; enrollment election/coverage. Profile: WM-REC-010; WM-ECO-031 (calc and payslip faces). Reuse: WM-ECO-009, WM-ECO-004, WM-ECO-002, WM-XCT-003; Employment; Position; Money/Instrument; Price/Valuation; Payment; Projection/Disclosure Policy; Observation/Measurement. Not in set: CompensationReview; claim root; remittance root; Public Benefit/Program; Privacy Aggregation Floor.

## Blockers
Privacy Aggregation Floor is reserved with no spec. Public Benefit/Program is reserved with no spec. Reuse-target texts were not in the response packet; amount-pin and settlement fitness are assumed, not verified. Claim is unspecified; do not mint it. No target IDs are allocated. WM-ECO-031 dual-face versus Projection/Disclosure Policy must be profiled, not assumed closed.

## Decisions on every candidate and gap
Accept Band, Assignment, Plan and Enrollment as unassigned roots. Reject Review, claim-root, remittance-root, eligibility-root, coverage-root, payslip-root and aggregate-on-root. Relations to close: Assignment to Employment/Position as reference; Assignment to Band optional and at most one per interval; WM-REC-010 authorizes Assignment/Band version; Enrollment to Plan required; Enrollment to Employment optional and may outlive it; calculation reads Assignment versions plus Enrollment plus time; Payment settles obligation and is not payslip identity; valuation goes to Price/Valuation; position-in-range goes to Observation/Measurement; aggregate goes to Disclosure Policy only. Gaps left open: public-program boundary; privacy-floor controls; claim event; unverified reuse-target fitness.


===== candidate\benefit-enrollment.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-PEO-09",
  "proposedName": "Benefit Enrollment",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "candidateRevision": 2,
  "identityTest": {
    "stableIdentity": "A benefit enrollment remains identifiable by person, plan version, election and coverage interval independently of payroll.",
    "versionIdentity": "Changing election, dependent set, tier, waiver, suspension or coverage interval appends a successor state and preserves history.",
    "independentLifecycle": [
      "offered",
      "elected",
      "waived",
      "pending",
      "active",
      "suspended",
      "continued",
      "ended",
      "superseded"
    ],
    "mastership": "benefits enrollment administration authority"
  },
  "boundary": {
    "owns": [
      "enrollment identity and immutable states",
      "election and waiver",
      "dependent set and tier",
      "coverage periods and continuation state"
    ],
    "references": [
      {
        "target": "Benefit Plan",
        "purpose": "required plan version"
      },
      {
        "target": "WM-ORG-005",
        "purpose": "optional Employment context"
      },
      {
        "target": "WM-ECO-031",
        "purpose": "optional payroll deduction input only"
      },
      {
        "target": "WM-REC-010",
        "purpose": "authorized exception or decision"
      }
    ],
    "excludes": [
      "eligibility-rule authority",
      "claim adjudication",
      "valuation",
      "payroll result",
      "payment"
    ]
  },
  "invariantRules": [
    {
      "id": "BE-01",
      "text": "A benefit enrollment remains identifiable by person, plan version, election and coverage interval independently of payroll."
    },
    {
      "id": "BE-02",
      "text": "Changing election, dependent set, tier, waiver, suspension or coverage interval appends a successor state and preserves history."
    },
    {
      "id": "BE-03",
      "text": "Enrollment requires a plan version and may reference Employment, but may outlive active employment under continuation rules."
    },
    {
      "id": "BE-04",
      "text": "Election and coverage are enrollment-owned components; neither is eligibility nor a claim."
    },
    {
      "id": "BE-05",
      "text": "Coverage may remain active when pay is zero, no deduction exists or no payroll period exists."
    },
    {
      "id": "BE-06",
      "text": "A deduction on a payslip is not evidence of coverage."
    },
    {
      "id": "BE-07",
      "text": "Enrollment interval, coverage interval, payroll period and payment date are distinct."
    },
    {
      "id": "BE-08",
      "text": "Dependent coverage and tier are explicit states with source authority and effective time."
    },
    {
      "id": "BE-09",
      "text": "Valuation, claim adjudication and payment remain external masters."
    },
    {
      "id": "BE-10",
      "text": "Ending Employment does not silently end enrollment; an authorized rule or successor state is required."
    },
    {
      "id": "BE-11",
      "text": "Missing enrollment or coverage data is unknown, never waived or inactive by inference."
    },
    {
      "id": "BE-12",
      "text": "Historic enrollment remains resolvable after plan succession or retirement."
    }
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "All proposed relations are provisional until registry approval.",
    "Every cited base remains a non-canonical draft or reservation.",
    "Jurisdiction crosswalks, immutable source pins, package conversion and live conformance are pending.",
    "Privacy Aggregation Floor and Public Benefit / Program have no current specification."
  ],
  "publicationStatement": "Research candidate only; not canonically publishable, installable or verified."
}


===== candidate\benefit-plan.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-PEO-09",
  "proposedName": "Benefit Plan",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "candidateRevision": 2,
  "identityTest": {
    "stableIdentity": "A benefit plan remains identifiable independently of any person, enrollment, payroll deduction, claim or payment.",
    "versionIdentity": "Changing sponsor, jurisdiction, eligibility, coverage categories or cost-sharing creates an immutable successor plan version.",
    "independentLifecycle": [
      "draft",
      "reviewed",
      "approved",
      "offered",
      "effective",
      "closed",
      "superseded",
      "retired"
    ],
    "mastership": "benefits administration authority"
  },
  "boundary": {
    "owns": [
      "plan identity and immutable versions",
      "sponsor and jurisdiction context",
      "coverage categories and cost sharing",
      "versioned eligibility rules"
    ],
    "references": [
      {
        "target": "WM-ORG-005",
        "purpose": "employment-derived eligibility context"
      },
      {
        "target": "WM-ECO-002",
        "purpose": "valuation boundary"
      },
      {
        "target": "WM-REC-010",
        "purpose": "authorizing decision"
      },
      {
        "target": "WM-POL-012",
        "purpose": "explicit public-program exclusion"
      }
    ],
    "excludes": [
      "person enrollment",
      "coverage election",
      "claim or use",
      "payroll deduction",
      "payment",
      "public benefit program"
    ]
  },
  "invariantRules": [
    {
      "id": "BP-01",
      "text": "A benefit plan remains identifiable independently of any person, enrollment, payroll deduction, claim or payment."
    },
    {
      "id": "BP-02",
      "text": "Changing sponsor, jurisdiction, eligibility, coverage categories or cost-sharing creates an immutable successor plan version."
    },
    {
      "id": "BP-03",
      "text": "Eligibility is a versioned plan-owned rule and is neither enrollment nor coverage."
    },
    {
      "id": "BP-04",
      "text": "An employee benefit plan is not a WM-POL-012 Public Benefit / Program."
    },
    {
      "id": "BP-05",
      "text": "Plan eligibility does not prove enrollment, coverage, claim acceptance or payment."
    },
    {
      "id": "BP-06",
      "text": "Valuation is owned by WM-ECO-002 and is not a plan fact."
    },
    {
      "id": "BP-07",
      "text": "Payroll deduction configuration is not plan identity and does not prove coverage."
    },
    {
      "id": "BP-08",
      "text": "Plan retirement preserves active and historic enrollment references under explicit continuation rules."
    },
    {
      "id": "BP-09",
      "text": "Plan versions pin sponsor, jurisdiction, effective interval and source authority."
    },
    {
      "id": "BP-10",
      "text": "Missing eligibility evidence is unknown and cannot be coerced to ineligible."
    },
    {
      "id": "BP-11",
      "text": "Public-program and employee-plan boundaries remain explicit even when payroll administers statutory contributions."
    },
    {
      "id": "BP-12",
      "text": "A claim or use event is outside this candidate and no claim root is minted here."
    }
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "All proposed relations are provisional until registry approval.",
    "Every cited base remains a non-canonical draft or reservation.",
    "Jurisdiction crosswalks, immutable source pins, package conversion and live conformance are pending.",
    "Privacy Aggregation Floor and Public Benefit / Program have no current specification."
  ],
  "publicationStatement": "Research candidate only; not canonically publishable, installable or verified."
}


===== candidate\compensation-assignment.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-PEO-09",
  "proposedName": "Compensation Assignment",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "candidateRevision": 2,
  "identityTest": {
    "stableIdentity": "A compensation assignment remains identifiable per worker and concurrent Employment or Position context independently of band, payroll and payment.",
    "versionIdentity": "A change to authorized terms or effective interval appends a successor assignment version and never overwrites history.",
    "independentLifecycle": [
      "proposed",
      "reviewed",
      "authorized",
      "effective",
      "amended",
      "suspended",
      "ended",
      "superseded"
    ],
    "mastership": "HR compensation administration authority"
  },
  "boundary": {
    "owns": [
      "assignment identity and immutable versions",
      "base, allowance, differential and target-variable components",
      "effective terms and proration inputs"
    ],
    "references": [
      {
        "target": "WM-ORG-005",
        "purpose": "Employment context"
      },
      {
        "target": "WM-ORG-004",
        "purpose": "Position context"
      },
      {
        "target": "Compensation Band",
        "purpose": "optional range context"
      },
      {
        "target": "WM-REC-010",
        "purpose": "authorizing decision"
      },
      {
        "target": "WM-ECO-004",
        "purpose": "Money and currency"
      }
    ],
    "excludes": [
      "employment identity",
      "position identity",
      "band identity",
      "earned pay",
      "payslip",
      "payment",
      "remittance"
    ]
  },
  "invariantRules": [
    {
      "id": "CA-01",
      "text": "A compensation assignment remains identifiable per worker and concurrent Employment or Position context independently of band, payroll and payment."
    },
    {
      "id": "CA-02",
      "text": "A change to authorized terms or effective interval appends a successor assignment version and never overwrites history."
    },
    {
      "id": "CA-03",
      "text": "An assignment owns only base, allowance, differential and target-variable components; reusable incentive eligibility may require a separate plan boundary."
    },
    {
      "id": "CA-04",
      "text": "Every component pins currency, basis, period, frequency, FTE or working-time normalization, effective interval and source authority."
    },
    {
      "id": "CA-05",
      "text": "An assignment references Employment and/or Position, may cite at most one band per effective interval, and may cite an authorizing WM-REC-010 decision."
    },
    {
      "id": "CA-06",
      "text": "Concurrent employments or positions have distinct assignment identities."
    },
    {
      "id": "CA-07",
      "text": "A WM-REC-010 decision may authorize, reject or amend proposed terms; only a successor assignment carries authorized terms."
    },
    {
      "id": "CA-08",
      "text": "An unapplied recommendation remains on the decision and does not alter an assignment."
    },
    {
      "id": "CA-09",
      "text": "Assignment effective time, decision time, payroll period, payment value date and remittance due date are distinct."
    },
    {
      "id": "CA-10",
      "text": "A mid-period change requires versioned terms and explicit proration inputs."
    },
    {
      "id": "CA-11",
      "text": "An assignment authorizes possible remuneration and never asserts earned pay, payslip issuance, payment or settlement."
    },
    {
      "id": "CA-12",
      "text": "Original-currency terms are preserved; conversions are explicit derived observations."
    },
    {
      "id": "CA-13",
      "text": "Absence of assignment data is unknown, never zero."
    }
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "All proposed relations are provisional until registry approval.",
    "Every cited base remains a non-canonical draft or reservation.",
    "Jurisdiction crosswalks, immutable source pins, package conversion and live conformance are pending.",
    "Privacy Aggregation Floor and Public Benefit / Program have no current specification."
  ],
  "publicationStatement": "Research candidate only; not canonically publishable, installable or verified."
}


===== candidate\compensation-band.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-PEO-09",
  "proposedName": "Compensation Band",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "candidateRevision": 2,
  "identityTest": {
    "stableIdentity": "A compensation band remains identifiable independently of a worker, position, assignment, payroll result and payment.",
    "versionIdentity": "Changing range points, currency, basis, period, geography, authority or applicability creates an immutable successor version.",
    "independentLifecycle": [
      "draft",
      "reviewed",
      "approved",
      "published",
      "effective",
      "deprecated",
      "superseded",
      "retired"
    ],
    "mastership": "enterprise compensation architecture authority"
  },
  "boundary": {
    "owns": [
      "band identity",
      "immutable band versions",
      "Money-valued range points",
      "applicability and differential rules"
    ],
    "references": [
      {
        "target": "WM-ORG-004",
        "purpose": "Position range context"
      },
      {
        "target": "WM-ECO-004",
        "purpose": "Money and currency"
      },
      {
        "target": "WM-ECO-002",
        "purpose": "valuation and conversion boundary"
      },
      {
        "target": "WM-REC-010",
        "purpose": "authorizing decision"
      }
    ],
    "excludes": [
      "individual compensation terms",
      "grade scheme",
      "earned pay",
      "payroll result",
      "payment or settlement"
    ]
  },
  "invariantRules": [
    {
      "id": "CB-01",
      "text": "A compensation band remains identifiable independently of a worker, position, assignment, payroll result and payment."
    },
    {
      "id": "CB-02",
      "text": "Changing range points, currency, basis, period, geography, authority or applicability creates an immutable successor version."
    },
    {
      "id": "CB-03",
      "text": "A band range is neither an individual assignment nor a payable."
    },
    {
      "id": "CB-04",
      "text": "Minimum, reference and maximum are Money amounts and each pins currency, unit or basis, period, frequency, FTE normalization and source authority."
    },
    {
      "id": "CB-05",
      "text": "An assignment may omit a band or be outside a cited range; off-band status is explicit and valid."
    },
    {
      "id": "CB-06",
      "text": "A Position may cite one band version for an effective interval, but that citation does not state occupant pay."
    },
    {
      "id": "CB-07",
      "text": "Grade, proficiency, performance and compensation band remain separate axes."
    },
    {
      "id": "CB-08",
      "text": "Compa-ratio, occupancy and position-in-range are observations and never band attributes."
    },
    {
      "id": "CB-09",
      "text": "A band change does not mutate assignment, payroll or payment history."
    },
    {
      "id": "CB-10",
      "text": "Original-currency values remain original; FX and frequency conversions are derived observations with source, direction, time and rounding."
    },
    {
      "id": "CB-11",
      "text": "Retirement preserves historical resolution and citations."
    },
    {
      "id": "CB-12",
      "text": "Missing range values are unknown, never zero."
    }
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "All proposed relations are provisional until registry approval.",
    "Every cited base remains a non-canonical draft or reservation.",
    "Jurisdiction crosswalks, immutable source pins, package conversion and live conformance are pending.",
    "Privacy Aggregation Floor and Public Benefit / Program have no current specification."
  ],
  "publicationStatement": "Research candidate only; not canonically publishable, installable or verified."
}


===== candidate\enterprise-compensation-benefits-profile.json =====
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-PEO-09",
  "name": "Enterprise Compensation, Benefits and Payroll",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "candidateRevision": 2,
  "bases": [
    "WM-ECO-031",
    "WM-ORG-005",
    "WM-ORG-004",
    "WM-ECO-004",
    "WM-ECO-002",
    "WM-REC-010",
    "WM-ECO-009",
    "WM-XCT-003",
    "WM-MAT-008"
  ],
  "candidateRoots": [
    "Compensation Band",
    "Compensation Assignment",
    "Benefit Plan",
    "Benefit Enrollment"
  ],
  "constraints": [
    "Compensation Review is not a root; WM-REC-010 owns authoritative review outcomes.",
    "WM-ECO-031 owns payroll calculation and payslip faces, not source term authority.",
    "WM-ECO-009 owns payment instruction, execution and settlement; payslip and net pay do not prove settlement.",
    "Statutory remittance, net-pay settlement and benefit claim remain distinct.",
    "Aggregates are WM-XCT-003 projections and never root attributes.",
    "A singleton or a release isolating a person through differencing, join or repeated query is refused.",
    "Privacy controls are declarative because WM-XCT-005 has no current specification; no k, noise or budget value is invented.",
    "Every amount pins currency, basis, period, frequency, FTE normalization and source authority."
  ],
  "holds": [
    "Registry allocation is pending; no identifier is guessed.",
    "All proposed relations are provisional until registry approval.",
    "Every cited base remains a non-canonical draft or reservation.",
    "Jurisdiction crosswalks, immutable source pins, package conversion and live conformance are pending.",
    "Privacy Aggregation Floor and Public Benefit / Program have no current specification."
  ],
  "unownedScopeRegister": [
    "benefit claim or use",
    "statutory remittance root",
    "privacy floor algorithm",
    "equity-plan administration",
    "insurance-carrier contract"
  ],
  "canonicalPublishable": false,
  "publicationStatement": "Research candidate only; not canonically publishable, installable or verified."
}


===== candidate\fixtures.json =====
{
  "format": "vercy-enterprise-combined-fixtures/v1",
  "contour": "EM-PEO-09",
  "executable": false,
  "cases": [
    {
      "id": "band-01",
      "kind": "semantic",
      "input": "A compensation band remains identifiable independently of a worker, position, assignment, payroll result and payment.",
      "expect": "Rule CB-01 is normatively asserted.",
      "rules": [
        "CB-01"
      ]
    },
    {
      "id": "band-02",
      "kind": "semantic",
      "input": "Changing range points, currency, basis, period, geography, authority or applicability creates an immutable successor version.",
      "expect": "Rule CB-02 is normatively asserted.",
      "rules": [
        "CB-02"
      ]
    },
    {
      "id": "band-03",
      "kind": "semantic",
      "input": "A band range is neither an individual assignment nor a payable.",
      "expect": "Rule CB-03 is normatively asserted.",
      "rules": [
        "CB-03"
      ]
    },
    {
      "id": "band-04",
      "kind": "semantic",
      "input": "Minimum, reference and maximum are Money amounts and each pins currency, unit or basis, period, frequency, FTE normalization and source authority.",
      "expect": "Rule CB-04 is normatively asserted.",
      "rules": [
        "CB-04"
      ]
    },
    {
      "id": "band-05",
      "kind": "semantic",
      "input": "An assignment may omit a band or be outside a cited range; off-band status is explicit and valid.",
      "expect": "Rule CB-05 is normatively asserted.",
      "rules": [
        "CB-05"
      ]
    },
    {
      "id": "band-06",
      "kind": "semantic",
      "input": "A Position may cite one band version for an effective interval, but that citation does not state occupant pay.",
      "expect": "Rule CB-06 is normatively asserted.",
      "rules": [
        "CB-06"
      ]
    },
    {
      "id": "band-07",
      "kind": "semantic",
      "input": "Grade, proficiency, performance and compensation band remain separate axes.",
      "expect": "Rule CB-07 is normatively asserted.",
      "rules": [
        "CB-07"
      ]
    },
    {
      "id": "band-08",
      "kind": "semantic",
      "input": "Compa-ratio, occupancy and position-in-range are observations and never band attributes.",
      "expect": "Rule CB-08 is normatively asserted.",
      "rules": [
        "CB-08"
      ]
    },
    {
      "id": "band-09",
      "kind": "semantic",
      "input": "A band change does not mutate assignment, payroll or payment history.",
      "expect": "Rule CB-09 is normatively asserted.",
      "rules": [
        "CB-09"
      ]
    },
    {
      "id": "band-10",
      "kind": "semantic",
      "input": "Original-currency values remain original; FX and frequency conversions are derived observations with source, direction, time and rounding.",
      "expect": "Rule CB-10 is normatively asserted.",
      "rules": [
        "CB-10"
      ]
    },
    {
      "id": "band-11",
      "kind": "semantic",
      "input": "Retirement preserves historical resolution and citations.",
      "expect": "Rule CB-11 is normatively asserted.",
      "rules": [
        "CB-11"
      ]
    },
    {
      "id": "band-12",
      "kind": "semantic",
      "input": "Missing range values are unknown, never zero.",
      "expect": "Rule CB-12 is normatively asserted.",
      "rules": [
        "CB-12"
      ]
    },
    {
      "id": "assignment-01",
      "kind": "semantic",
      "input": "A compensation assignment remains identifiable per worker and concurrent Employment or Position context independently of band, payroll and payment.",
      "expect": "Rule CA-01 is normatively asserted.",
      "rules": [
        "CA-01"
      ]
    },
    {
      "id": "assignment-02",
      "kind": "semantic",
      "input": "A change to authorized terms or effective interval appends a successor assignment version and never overwrites history.",
      "expect": "Rule CA-02 is normatively asserted.",
      "rules": [
        "CA-02"
      ]
    },
    {
      "id": "assignment-03",
      "kind": "semantic",
      "input": "An assignment owns only base, allowance, differential and target-variable components; reusable incentive eligibility may require a separate plan boundary.",
      "expect": "Rule CA-03 is normatively asserted.",
      "rules": [
        "CA-03"
      ]
    },
    {
      "id": "assignment-04",
      "kind": "semantic",
      "input": "Every component pins currency, basis, period, frequency, FTE or working-time normalization, effective interval and source authority.",
      "expect": "Rule CA-04 is normatively asserted.",
      "rules": [
        "CA-04"
      ]
    },
    {
      "id": "assignment-05",
      "kind": "semantic",
      "input": "An assignment references Employment and/or Position, may cite at most one band per effective interval, and may cite an authorizing WM-REC-010 decision.",
      "expect": "Rule CA-05 is normatively asserted.",
      "rules": [
        "CA-05"
      ]
    },
    {
      "id": "assignment-06",
      "kind": "semantic",
      "input": "Concurrent employments or positions have distinct assignment identities.",
      "expect": "Rule CA-06 is normatively asserted.",
      "rules": [
        "CA-06"
      ]
    },
    {
      "id": "assignment-07",
      "kind": "semantic",
      "input": "A WM-REC-010 decision may authorize, reject or amend proposed terms; only a successor assignment carries authorized terms.",
      "expect": "Rule CA-07 is normatively asserted.",
      "rules": [
        "CA-07"
      ]
    },
    {
      "id": "assignment-08",
      "kind": "semantic",
      "input": "An unapplied recommendation remains on the decision and does not alter an assignment.",
      "expect": "Rule CA-08 is normatively asserted.",
      "rules": [
        "CA-08"
      ]
    },
    {
      "id": "assignment-09",
      "kind": "semantic",
      "input": "Assignment effective time, decision time, payroll period, payment value date and remittance due date are distinct.",
      "expect": "Rule CA-09 is normatively asserted.",
      "rules": [
        "CA-09"
      ]
    },
    {
      "id": "assignment-10",
      "kind": "semantic",
      "input": "A mid-period change requires versioned terms and explicit proration inputs.",
      "expect": "Rule CA-10 is normatively asserted.",
      "rules": [
        "CA-10"
      ]
    },
    {
      "id": "assignment-11",
      "kind": "semantic",
      "input": "An assignment authorizes possible remuneration and never asserts earned pay, payslip issuance, payment or settlement.",
      "expect": "Rule CA-11 is normatively asserted.",
      "rules": [
        "CA-11"
      ]
    },
    {
      "id": "assignment-12",
      "kind": "semantic",
      "input": "Original-currency terms are preserved; conversions are explicit derived observations.",
      "expect": "Rule CA-12 is normatively asserted.",
      "rules": [
        "CA-12"
      ]
    },
    {
      "id": "assignment-13",
      "kind": "semantic",
      "input": "Absence of assignment data is unknown, never zero.",
      "expect": "Rule CA-13 is normatively asserted.",
      "rules": [
        "CA-13"
      ]
    },
    {
      "id": "plan-01",
      "kind": "semantic",
      "input": "A benefit plan remains identifiable independently of any person, enrollment, payroll deduction, claim or payment.",
      "expect": "Rule BP-01 is normatively asserted.",
      "rules": [
        "BP-01"
      ]
    },
    {
      "id": "plan-02",
      "kind": "semantic",
      "input": "Changing sponsor, jurisdiction, eligibility, coverage categories or cost-sharing creates an immutable successor plan version.",
      "expect": "Rule BP-02 is normatively asserted.",
      "rules": [
        "BP-02"
      ]
    },
    {
      "id": "plan-03",
      "kind": "semantic",
      "input": "Eligibility is a versioned plan-owned rule and is neither enrollment nor coverage.",
      "expect": "Rule BP-03 is normatively asserted.",
      "rules": [
        "BP-03"
      ]
    },
    {
      "id": "plan-04",
      "kind": "semantic",
      "input": "An employee benefit plan is not a WM-POL-012 Public Benefit / Program.",
      "expect": "Rule BP-04 is normatively asserted.",
      "rules": [
        "BP-04"
      ]
    },
    {
      "id": "plan-05",
      "kind": "semantic",
      "input": "Plan eligibility does not prove enrollment, coverage, claim acceptance or payment.",
      "expect": "Rule BP-05 is normatively asserted.",
      "rules": [
        "BP-05"
      ]
    },
    {
      "id": "plan-06",
      "kind": "semantic",
      "input": "Valuation is owned by WM-ECO-002 and is not a plan fact.",
      "expect": "Rule BP-06 is normatively asserted.",
      "rules": [
        "BP-06"
      ]
    },
    {
      "id": "plan-07",
      "kind": "semantic",
      "input": "Payroll deduction configuration is not plan identity and does not prove coverage.",
      "expect": "Rule BP-07 is normatively asserted.",
      "rules": [
        "BP-07"
      ]
    },
    {
      "id": "plan-08",
      "kind": "semantic",
      "input": "Plan retirement preserves active and historic enrollment references under explicit continuation rules.",
      "expect": "Rule BP-08 is normatively asserted.",
      "rules": [
        "BP-08"
      ]
    },
    {
      "id": "plan-09",
      "kind": "semantic",
      "input": "Plan versions pin sponsor, jurisdiction, effective interval and source authority.",
      "expect": "Rule BP-09 is normatively asserted.",
      "rules": [
        "BP-09"
      ]
    },
    {
      "id": "plan-10",
      "kind": "semantic",
      "input": "Missing eligibility evidence is unknown and cannot be coerced to ineligible.",
      "expect": "Rule BP-10 is normatively asserted.",
      "rules": [
        "BP-10"
      ]
    },
    {
      "id": "plan-11",
      "kind": "semantic",
      "input": "Public-program and employee-plan boundaries remain explicit even when payroll administers statutory contributions.",
      "expect": "Rule BP-11 is normatively asserted.",
      "rules": [
        "BP-11"
      ]
    },
    {
      "id": "plan-12",
      "kind": "semantic",
      "input": "A claim or use event is outside this candidate and no claim root is minted here.",
      "expect": "Rule BP-12 is normatively asserted.",
      "rules": [
        "BP-12"
      ]
    },
    {
      "id": "enrollment-01",
      "kind": "semantic",
      "input": "A benefit enrollment remains identifiable by person, plan version, election and coverage interval independently of payroll.",
      "expect": "Rule BE-01 is normatively asserted.",
      "rules": [
        "BE-01"
      ]
    },
    {
      "id": "enrollment-02",
      "kind": "semantic",
      "input": "Changing election, dependent set, tier, waiver, suspension or coverage interval appends a successor state and preserves history.",
      "expect": "Rule BE-02 is normatively asserted.",
      "rules": [
        "BE-02"
      ]
    },
    {
      "id": "enrollment-03",
      "kind": "semantic",
      "input": "Enrollment requires a plan version and may reference Employment, but may outlive active employment under continuation rules.",
      "expect": "Rule BE-03 is normatively asserted.",
      "rules": [
        "BE-03"
      ]
    },
    {
      "id": "enrollment-04",
      "kind": "semantic",
      "input": "Election and coverage are enrollment-owned components; neither is eligibility nor a claim.",
      "expect": "Rule BE-04 is normatively asserted.",
      "rules": [
        "BE-04"
      ]
    },
    {
      "id": "enrollment-05",
      "kind": "semantic",
      "input": "Coverage may remain active when pay is zero, no deduction exists or no payroll period exists.",
      "expect": "Rule BE-05 is normatively asserted.",
      "rules": [
        "BE-05"
      ]
    },
    {
      "id": "enrollment-06",
      "kind": "semantic",
      "input": "A deduction on a payslip is not evidence of coverage.",
      "expect": "Rule BE-06 is normatively asserted.",
      "rules": [
        "BE-06"
      ]
    },
    {
      "id": "enrollment-07",
      "kind": "semantic",
      "input": "Enrollment interval, coverage interval, payroll period and payment date are distinct.",
      "expect": "Rule BE-07 is normatively asserted.",
      "rules": [
        "BE-07"
      ]
    },
    {
      "id": "enrollment-08",
      "kind": "semantic",
      "input": "Dependent coverage and tier are explicit states with source authority and effective time.",
      "expect": "Rule BE-08 is normatively asserted.",
      "rules": [
        "BE-08"
      ]
    },
    {
      "id": "enrollment-09",
      "kind": "semantic",
      "input": "Valuation, claim adjudication and payment remain external masters.",
      "expect": "Rule BE-09 is normatively asserted.",
      "rules": [
        "BE-09"
      ]
    },
    {
      "id": "enrollment-10",
      "kind": "semantic",
      "input": "Ending Employment does not silently end enrollment; an authorized rule or successor state is required.",
      "expect": "Rule BE-10 is normatively asserted.",
      "rules": [
        "BE-10"
      ]
    },
    {
      "id": "enrollment-11",
      "kind": "semantic",
      "input": "Missing enrollment or coverage data is unknown, never waived or inactive by inference.",
      "expect": "Rule BE-11 is normatively asserted.",
      "rules": [
        "BE-11"
      ]
    },
    {
      "id": "enrollment-12",
      "kind": "semantic",
      "input": "Historic enrollment remains resolvable after plan succession or retirement.",
      "expect": "Rule BE-12 is normatively asserted.",
      "rules": [
        "BE-12"
      ]
    },
    {
      "id": "mid-period-multi-currency",
      "kind": "acceptance",
      "input": "0.6 FTE worker changes USD annual terms to EUR monthly terms mid-period; payment later settles in GBP.",
      "expect": "Two assignment versions, explicit proration and FX observations; payroll and settlement remain distinct.",
      "rules": [
        "CA-02",
        "CA-04",
        "CA-09",
        "CA-10",
        "CA-12"
      ]
    },
    {
      "id": "coverage-without-pay",
      "kind": "acceptance",
      "input": "Family medical coverage continues through an unpaid payroll gap.",
      "expect": "Coverage remains active independently of payroll.",
      "rules": [
        "BE-03",
        "BE-05",
        "BE-06",
        "BE-07"
      ]
    },
    {
      "id": "off-band",
      "kind": "positive",
      "input": "An assignment is outside its optional cited band.",
      "expect": "The assignment is valid and off-band state is explicit.",
      "rules": [
        "CB-05",
        "CA-05"
      ]
    },
    {
      "id": "review-no-change",
      "kind": "positive",
      "input": "A review decision recommends no change.",
      "expect": "Decision remains authoritative; no successor assignment is invented.",
      "rules": [
        "CA-07",
        "CA-08"
      ]
    },
    {
      "id": "unsafe-difference",
      "kind": "negative",
      "input": "Two department-band aggregates differ by exactly one worker.",
      "expect": "Disclosure is refused under the profile privacy constraint.",
      "rules": []
    },
    {
      "id": "payslip-payment",
      "kind": "negative",
      "input": "A payslip is used as proof of settlement.",
      "expect": "Inference is rejected; WM-ECO-009 remains authoritative.",
      "rules": []
    },
    {
      "id": "deduction-coverage",
      "kind": "negative",
      "input": "A deduction is used as proof of benefit coverage.",
      "expect": "Inference is rejected.",
      "rules": [
        "BP-07",
        "BE-06"
      ]
    },
    {
      "id": "employee-public",
      "kind": "negative",
      "input": "An employer medical plan is classified as a public benefit.",
      "expect": "Classification is rejected.",
      "rules": [
        "BP-04",
        "BP-11"
      ]
    }
  ]
}
