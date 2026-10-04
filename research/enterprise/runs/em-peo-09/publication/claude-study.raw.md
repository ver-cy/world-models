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
