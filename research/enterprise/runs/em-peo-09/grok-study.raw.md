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
