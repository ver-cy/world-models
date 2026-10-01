# EM-FIN-06 local synthesis

## Disposition

- Reuse WM-ECO-038 as the security or equity position master and profile it for investment holdings.
- Reuse/profile WM-ECO-002 for Valuation, with mandatory subject-kind and full method, assumption, currency, time and provenance semantics.
- Reuse economic-event and WM-ECO-016 posting boundaries for InvestmentTransaction; do not create another transaction root.
- Propose identifier-unassigned **Financial Instrument** and **Investment** roots because their identities and lifecycles are independent of holdings, transactions and valuations.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

A Financial Instrument exists before any holder, survives transfers and position closure, and owns immutable issuer terms and version lineage. It must remain distinct from the investee, a share class, a holding and a transaction.

An Investment is a governed participation or exposure that can survive replacement of one instrument by another, a temporary zero holding, an undrawn commitment and an exited-but-retained lifecycle. It owns mandate, commitment, stage and exit context. Plain portfolio membership over listed positions does not automatically mint Investment identity.

WM-ECO-038 owns security-backed positions, quantities, lots, capacities, rights, restrictions and successor history. It cannot be the generic investment master because non-security participations and real-asset investments need no security, register or custody account.

## Instrument, holding and transaction

Instrument terms, issuance version, issuer capacity, holder capacity, position and account/register context remain separate. Quantity, unit, ownership percentage, voting power, cost, carrying amount and market value are separately typed and timed.

Acquisition, disposal, subscription, transfer and conversion are economic events. A posting is their accounting representation in WM-ECO-016. Trade, settlement, availability and position change are distinct states or events. Posted entries remain immutable and corrections use linked reversals.

The dossier lacks an allocated general trade/settlement event master, so the InvestmentTransaction profile cannot yet bind to a named canonical root.

## Valuation

WM-ECO-002 already owns valuation assertion identity, subject, basis and premise, methods, inputs, assumptions, model version, uncertainty, review, supersession and currency conversion. A profile must require subject-kind: investee, instrument, holding or accounting carrying amount. These assertions can coexist and are never interchangeable.

Valuation is never a scalar field on a holding. Two same-date valuations under different methods or currencies remain distinct assertions with their original inputs, evidence and uncertainty. Recency alone never reconciles them.

## Convertible instruments

Conversion ratio, cap, discount, triggers, maturity and anti-dilution terms belong to an immutable instrument version. A holder's conversion right is contingent and excluded from current voting and ownership denominators.

Conversion is an explicit event. It derecognizes a predecessor position, creates successor positions bound to the resulting instrument version, produces accounting effects and preserves the Investment identity and lineage.

WM-ECO-038 currently groups conversion/subscription rights with voting and dividend rights. The profile must add contingency and denominator-exclusion semantics so future rights cannot be aggregated as present rights.

## Ownership, control and consolidation

Value never establishes ownership, voting power, control or consolidation treatment. Economic interest, capital rights, voting power, contractual control, de facto control and consolidation inclusion remain separate assertions with distinct bases, evidence, denominators and effective times.

WM-ORG-012 owns organizational relationship and control assertions. WM-ORG-018 owns governance authority. Consolidation scope and run remain the unassigned EM-FIN-04 candidates.

## Time, currency and provenance

Effective, trade, settlement, record, observation, ingestion and knowledge times remain distinct. Date-only precision is preserved. Every monetary assertion retains currency, rate source, rate type, rate date, direction and rounding; conversion never replaces the original amount.

Every instrument, holding, event and valuation assertion preserves source, actor, evidence digest, confidence, conflict state, version and supersession lineage.

## Acceptance result

Convertible note N v1 is held by investor I in investee X as Investment INV-1 and position H-1. H-1 has a contingent conversion right and zero current votes. On one date, V-A values X by an income method in EUR and V-B by a market method in USD. Both remain independently resolvable and neither sets voting power. Conversion event E-1 retires H-1, creates preferred position H-2 against instrument v2 and links its postings; INV-1 continues and both valuations retain their original knowledge-time provenance.

## Required invariants

1. Investee, instrument, investment, position, transaction, posting and valuation have distinct identities.
2. Instrument terms are immutable and versioned.
3. Issuer, holder, beneficial owner, nominee and custodian capacities remain distinct.
4. Quantity, percentage, voting power, cost, carrying amount and value are separately typed.
5. Every valuation identifies subject-kind, date, method, basis, currency, inputs, assumptions, model version, evidence and uncertainty.
6. Same-date valuations may diverge and preserve provenance.
7. Value never establishes voting, control or consolidation.
8. Contingent rights are excluded from current voting and ownership denominators.
9. Conversion is an explicit event with predecessor/successor position lineage.
10. Transactions, settlements, position changes and postings remain distinct.
11. Posted entries balance and are corrected by successors or reversals.
12. Currency conversions preserve original amounts and rate provenance.
13. Corrections append history; originals remain resolvable.
14. Aggregate views never erase source capacity, conflict or evidence.

## Holds

Financial Instrument overlaps reserved WM-ECO-037 Debt Instrument and the unassigned Share Class candidate from EM-ORG-03; registry adjudication is required before allocation. Investment, trade/settlement event, corporate action, portfolio/mandate and consolidation masters are unallocated. WM-ECO-038's registry extension claim conflicts with its spec's reference-only treatment, while WM-ECO-002 has no approved outgoing relations. WM-ECO-038's conversion-right grouping needs a contingency constraint. Crosswalks, release pins, licences and fixtures remain unverified. Base drafts are non-canonical, so no installability or publication-readiness claim is made.


## Provider reconciliation and frozen audit

Grok independently upheld two identifier-unassigned roots: Financial Instrument and Investment. WM-ECO-038 remains the position master, WM-ECO-002 is profiled with a closed subject-kind discriminator, WM-ECO-016 remains the posting master, and the transaction event leg stays explicitly unbound. Share Class is subordinate to instrument-version equity terms. The sole frozen Claude audit upheld this decision and identified 22 mechanical artifact defects; all 22 are remediated without rerun. Its exact 57-case fixture array is retained alongside the original cases. No catalogue, model, registry or runtime identifier is allocated, and no canonical publishability or standards-conformance claim is made.
