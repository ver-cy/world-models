# EM-FIN-06 — Investments, Instruments and Valuation: independent adjudication

## Verdict

Boundary decision: **partial reuse with two new independent identities**. Reuse WM-ECO-038 for security-backed **positions only**; reuse/profile WM-ECO-002 for **Valuation**; reuse transaction and posting masters for **InvestmentTransaction**; raise **FinancialInstrument** and **Investment** as separate identifier-unassigned candidates. The negative case is rejected. Reviewable-draft assurance only; no canonical completeness, installability or publication readiness is claimed, and no identifiers are allocated.

## Evidence

Basis is the frozen dossier: WM-ECO-038 (aggregate, `boundary-review-required`), WM-ECO-002, WM-ECO-016, WM-ORG-001, WM-ORG-012, WM-ORG-018, the six reservation rows and six relation rows, plus prior checkpoints EM-FIN-02, EM-FIN-04, EM-FIN-05, EM-ORG-03, EM-LEG-04. All five specs are single-provider or dual-provider **reviewable drafts** with `publishableCanonical: false`; WM-ECO-038 and WM-ECO-002 carry explicit absence-of-external-review holds. The v1 candidate properties (`security_class`, `quantity`, `valuation: money`, `as_of`) are non-normative and are rejected below.

## Identity/mastership

Independent identity is granted where a thing survives the destruction of its neighbours and carries its own lifecycle:

- **FinancialInstrument — independent identity required.** Issuance terms exist with zero holders, survive every holding, and must be immutably versioned by the issuer. WM-ECO-038 itself declares the instrument an external, `required: true` reference.
- **Investment — independent identity required (participation profile).** An investment participation survives instrument replacement (note → preferred shares), survives zero current holdings (undrawn commitment, exited-but-tracked), and carries commitment, stage, mandate and exit attributes no holding owns.
- **InvestmentTransaction — no independent identity.** Profile over the economic acquisition/disposal event master plus WM-ECO-016 postings plus a WM-ECO-038 position-change assertion. Consistent with EM-FIN-02 ("do not create another transaction root").
- **Valuation — no independent identity.** Profile WM-ECO-002.
- **Conversion right** is a dependent component of the instrument and a scoped holding assertion; **conversion event** is an event of the instrument/corporate-action master, not a new root.

## Instrument/investment/holding

WM-ECO-038 **cannot** own generic investment semantics. Its canonicalization requires a security plus an account or register context, and its known omissions demand separate profiles per position class. Direct private stakes with no issued security, LP/JV interests, undrawn commitments and real-asset investments have no security and no account-servicer context; forcing them in would either fabricate a security or collapse investee, instrument and position. Decision: WM-ECO-038 = **security/equity position master**, profiled for investment use; Investment references investee (WM-ORG-001) or underlying asset, references instrument versions, and references — never absorbs — holdings. For plain listed portfolios, Investment is not minted: portfolio membership is a grouping relationship over holdings, distinct from participation.

Gap: the dossier names WM-ECO-037 Debt Instrument and EM-ORG-03's unallocated **Share Class** candidate. A single FinancialInstrument root with debt/equity/hybrid class components is preferable to three competing roots; this overlap must go to registry adjudication before allocation.

## Transactions/postings

Acquisition, disposal, transfer, subscription and conversion are economic events with their own identity, direction, quantity, price, fees and settlement state. Journal posting is the accounting artifact: reuse WM-ECO-016 unchanged, including its balancing invariant within one ledger, currency, scope and tolerance, its immutability after posting, and correction by linked reversal. A trade is not settlement; settled is not available; a posting is not a position change. **Gap:** WM-ECO-038 treats Order/Trade/Settlement and Corporate Action as authoritative external masters, but no such model is allocated in this dossier, so InvestmentTransaction cannot yet be profiled onto a named master.

## Valuation

Reuse/profile WM-ECO-002; do not mint a Valuation root. It already owns assertion identity and family typing, basis and premise, approaches, inputs and comparables, assumptions and special assumptions, model and software version, uncertainty and sensitivity, review and sign-off, correction/supersession/withdrawal, and currency conversion that preserves the original amount with rate source, direction and rounding. The required profile addition is a **mandatory subject-kind discriminator**: valuing the investee entity, the instrument, the holding, and the accounting carrying amount of the investment are four different assertions that frequently coexist and must never be substituted. Reject `valuation: money` as a scalar field.

## Convertible rights and conversion

Conversion terms (ratio, cap, discount, trigger, maturity, anti-dilution) are **immutable instrument-version terms**. The holder's conversion right is a **contingent future right**, typed with its trigger and effect-time, and must never aggregate into current voting or equity rights: pre-conversion the note holder has zero votes and zero ownership percentage. **Contradiction to fix:** WM-ECO-038 places conversion and subscription rights in the same finding as voting and dividend rights, which invites aggregation; the profile must carry a contingency flag and exclude contingent rights from any voting or percentage denominator. Conversion is an **explicit event**: it derecognises the predecessor holding, creates successor holdings bound to the new instrument version, produces WM-ECO-016 postings, and preserves the Investment identity across the change with full lineage.

## Ownership/voting/control/consolidation

Reject the negative case. A company valuation does not create voting or control rights. Economic interest, capital rights, voting power, contractual control, de facto control and consolidation treatment are separate assertions with separate bases, evidence and denominators (EM-ORG-03). Voting derives from class vote ratios, effective denominator rules and treasury/suspension treatment; control basis and scope belong to WM-ORG-012, which correctly refuses to infer consolidation from ownership; governance authority belongs to WM-ORG-018 and its mandate. Consolidation scope remains with EM-FIN-04's unallocated Consolidation Scope/Run candidates, not here.

## Time/currency/provenance

Separate effective, trade, settlement, record, observation, ingestion and knowledge times; preserve date-only precision. Valuations carry basis date, observation time and knowledge time independently. Quantities carry units; prices, costs, carrying amounts and valuations carry currency with rate source, type, date and authority, and conversions never replace originals. Every assertion carries source, actor, evidence digest, confidence, conflict state and supersession lineage. Same-date divergence is preserved, never reconciled by recency.

## Governance/assurance

Owners: financial leadership for investment records; issuer or registrar for instrument terms; custodian/registrar for positions; valuer for valuation conclusions; accounting for postings and carrying amounts. Master systems: ERP, accounting, bank, billing, FinOps, plus registrar and custodian. Agents may not trade, settle, convert, vote, determine beneficial ownership or issue valuation conclusions without delegated authority.

## Acceptance scenario

Convertible note N (instrument version v1, cap C, discount d) held by investor I in investee X, recorded as Investment INV-1 and holding H-1 with a contingent conversion right and zero votes. On 2026-06-30 two valuations of X are recorded: V-A (income approach, EUR) and V-B (market approach, USD). Both persist with distinct identity, method, basis, inputs, model version, uncertainty and provenance; neither supersedes the other and neither sets I's voting power. Conversion event E-1 later retires H-1 and creates H-2 in preferred class P (instrument version v2), with linked postings; INV-1 continues unchanged; V-A and V-B remain resolvable at their original knowledge times.

## Invariants

1. Investee, instrument, holding, transaction, posting and valuation have distinct identities.
2. Instrument terms are immutable and versioned; issuer and holder capacities stay separate.
3. Quantity, unit, percentage, voting power, cost, carrying amount and market value are separately typed, sourced and timed.
4. Every valuation states subject-kind, effective date, method, basis, currency, assumptions, inputs, model version, evidence and uncertainty.
5. Two same-date valuations coexist; divergence and provenance are preserved.
6. Valuation is an opinion, never a fact and never a rights allocation.
7. Value never establishes voting power, control or consolidation.
8. Contingent conversion rights are excluded from current voting and percentage denominators.
9. Conversion is an explicit event creating successor holdings, postings and lineage.
10. Postings balance within one ledger, currency, scope and tolerance; posted entries are immutable.
11. Positions preserve lots, balance buckets, rights and restrictions without collapsing them.
12. Trade, settlement, effective ownership and record date remain distinct events.
13. Corrections append successors; originals stay resolvable.
14. No aggregate view erases source positions, capacities or conflicts.

## Minimal model set

WM-ECO-038 (security position profile) · WM-ECO-002 (valuation profile with subject-kind) · WM-ECO-016 (postings) · WM-ORG-001 (investee, issuer, holder) · WM-ORG-012 (control/affiliation) · WM-ORG-018 (governance authority) · **FinancialInstrument** (new, identifier-unassigned) · **Investment** (new aggregate, identifier-unassigned) · referenced-but-unallocated: trade/settlement event, corporate action, portfolio/mandate, consolidation scope.

## Holds

Registry/spec conflict: WM-ECO-038's row asserts `EXTEND WM-ECO-005` while its spec downgrades this to REFERENCE and holds it. WM-ECO-002 has no approved outgoing relations, so every binding proposed here is a draft. FinancialInstrument overlaps WM-ECO-037 and the EM-ORG-03 Share Class candidate. Trade/settlement, corporate action, portfolio and consolidation masters are unallocated. WM-ECO-038 marks 26 of 27 dimensions covered while carrying fourteen publication holds — self-assessment exceeds evidence. Crosswalks (FIBO, ISO 20022, IFRS 9/13, IAS 32, XBRL), release pins, licensing and acceptance fixtures are unverified. This is a local no-tools adjudication, not independent external review.
