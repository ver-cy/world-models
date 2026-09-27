# EM-PEO-09 local synthesis

## Disposition

- Propose identifier-unassigned **Compensation Band**, **Compensation Assignment**, **Benefit Plan** and **Benefit Enrollment** roots.
- Keep eligibility rules inside versioned Benefit Plan and elections/coverage periods inside Benefit Enrollment.
- Reject Compensation Review as a root: authoritative outcomes profile WM-REC-010; the periodic review cycle remains an unresolved process/case boundary.
- Profile WM-ECO-031 for payroll calculation, payee result and payslip; reuse WM-ECO-009 for payment, WM-ECO-004 for money/FX, WM-ECO-002 for valuation and WM-XCT-003 for aggregate disclosure shape.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Band scheme and version, range, position range, compensation assignment and component, employment, review decision, payroll run/result/revision, earning, statutory base, deduction, employer contribution, payslip, payment instruction/execution/settlement, statutory remittance, benefit-plan version, eligibility rule, enrollment, election, coverage period, claim, valuation assertion and aggregate disclosure remain distinct.

Compensation authorities master bands and assignments. Benefits authorities master plans and enrollments. Payroll stewards master calculation runs and results. Finance masters payment and settlement. Tax and benefit authorities retain acceptance and statutory authority. No downstream result proves its upstream authorization.

## Bands and assignments

Compensation Band is a reusable versioned pay structure with minimum, reference and maximum values, currency, unit, period, geography or differential, authority and validity. It may reference the Grade Scheme candidate but remains a distinct axis. A position range references a band version and may carry a governed exception; it is never an entitlement or individual assignment.

Compensation Assignment binds one worker in one engagement/position context. It owns independently effective-dated components such as base wage, allowance, variable target, commission participation, equity reference and in-kind benefit. Each pins amount/rate, currency, unit/basis, period, frequency, FTE and working-time normalization, source authority and authorizing WM-REC-010 decision. It authorizes possible remuneration and never asserts earned pay.

## Review and decision

The review occasion is not a root in this contour. Each authorized outcome is a WM-REC-010 decision producing successor component versions with effective, decision and communication times kept separate. Nil outcomes remain recorded. Payroll must independently ingest a valid successor under declared proration rules.

## Benefit plan and enrollment

Benefit Plan owns sponsor, jurisdiction profile, plan versions, coverage categories, cost-sharing structure, carrier/provider reference and versioned eligibility rules. Benefit Enrollment owns worker election, window/reason, dependent coverage, coverage interval, waiver and suspension. Enrollment and coverage are independent of payroll and may continue without a payroll result or deduction.

Employer-sponsored benefits remain distinct from WM-POL-012 public programs. Employer plans derive eligibility from employment/assignment and contractual terms. Public programs derive authority and eligibility from statute and public administration, even if contributions pass through payroll.

## Payroll, payment and valuation

WM-ECO-031 owns run/payee calculation, earning components, statutory bases, deductions, contributions, net pay, payslip and filing projection. Payslip and net pay do not prove receipt. WM-ECO-009 owns instruction, execution, rejection, return and settlement. WM-ECO-002 owns in-kind or equity valuation assertions referenced as inputs.

Every monetary amount pins currency-system version, unit/basis, period, frequency, FTE normalization and source authority. Original-currency terms remain original. Derived conversion records rate, type, direction, source, determination time and rounding. Mid-period changes append component successors and payroll records the declared proration basis.

## Aggregation and privacy

Aggregate pay disclosure profiles WM-XCT-003 with declared grain, measures, period and mandatory cohort-floor reference. WM-XCT-005 lacks a current spec, so suppression enforcement remains a hold. Required controls include minimum cohort size, complementary suppression against differencing, repeated-query accounting, join-key withholding, uniform refused/suppressed behavior and logged authority. Indicators may profile WM-MAT-008; aggregates never expose individual compensation.

## Required invariants

1. Every amount pins currency, unit/basis, period, frequency, normalization and authority.
2. A band/range is never an individual assignment.
3. Assignment terms are not earned-pay facts.
4. Review decision, payroll result, payslip and payment settlement are distinct.
5. Payment facts come from financial sources.
6. Multi-currency terms are never silently converted.
7. Mid-period changes append effective-dated successors.
8. Benefit enrollment and coverage are independent of payroll production.
9. Employee benefit plans are not public-benefit programs.
10. Aggregates require cohort floors, differencing controls, query controls and audit.
11. Suppression is governed and does not leak whether a cohort is empty or unsafe.
12. Missing compensation data is unknown, never zero.

## Acceptance result

A 0.6-FTE worker has monthly EUR base and a USD allowance. A decision changes base effective mid-period, producing two immutable component versions and two prorated earning components. The allowance uses an explicit FX assertion. Benefit coverage continues independently while its deduction changes. A two-person average is refused, and overlapping five-person/four-person requests trigger complementary suppression because their difference would reveal one person.

## Holds

Four proposed roots lack allocations. All bases remain non-canonical drafts; WM-ECO-031, WM-ORG-005 and WM-ECO-002 retain single-provider holds. WM-ECO-031 ambiguously claims term ownership while also treating terms as external; it must be narrowed to run-scoped bindings. No approved WM-ECO-031 relation exists. WM-XCT-005 and WM-POL-012 lack current specs. Benefit claims, carrier contracts, equity administration, market surveys and the Grade Scheme candidate have no settled owner. Jurisdiction profiles, source pins, crosswalks and fixtures remain unverified. This checkpoint is not an installable release.
