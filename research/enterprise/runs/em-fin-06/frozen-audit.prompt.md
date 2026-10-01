# Frozen semantic audit prompt — EM-FIN-06

You are the sole frozen semantic auditor for this contour. This audit runs exactly once. Use only supplied text. Do not browse, call tools, invent identifiers, claim standards conformance or propose publication of blockers.

Audit the reconciled EM-FIN-06 boundary and allocation/profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence/rights semantics, non-deterministic fixtures and missing publishability holds. Preserve the intended decision unless evidence disproves it: keep Financial Instrument and Investment as independent identifier-unassigned candidates; WM-ECO-038 is position master only; WM-ECO-002 is a Valuation profile with mandatory subject-kind; InvestmentTransaction is event plus WM-ECO-016 posting; Share Class is subordinate classification; allocate no catalogue, model or runtime ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect exact deterministic remediation; Exact additional fixtures as a JSON array; final freeze decision. Be sceptical and concise. Never request another provider run.
## local-evidence.md

`	ext
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

`

## claude-study.raw.md

`	ext
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

`

## grok-study.raw.md

`	ext
Verdict: Conditionally accept. Reuse WM-ECO-038 only as the security/equity position master; profile WM-ECO-002 for Valuation with mandatory subject-kind; bound InvestmentTransaction to an economic event plus the WM-ECO-016 posting boundary. Create identifier-unassigned roots for Financial Instrument and Investment only. Allocate no identifier. Do not treat this as publication-ready.

Strongest evidence: The proposal already splits position mastership from valuation and from posting. That split is what keeps a price observation from becoming a rights fact, and a journal line from becoming the economic event.

Strongest counterexample: A convertible note in two lots, one observation date, a discounted-cash-flow valuation in USD and a market-multiple valuation in EUR, plus an unexercised conversion right. If WM-ECO-038 is treated as the instrument, if either valuation overwrites the other, or if the latest investee valuation or the contingent right is read as votes or control, lineage and governance are both wrong. Conversion that mutates the same position identity erases predecessor cost and restrictions.

Identity/mastership: Financial Instrument needs an independent unassigned root: the abstract contractual object with immutable term versions. WM-ECO-037 Debt Instrument does not conflict if it specializes or constrains that root; it must not be a rival master. The unassigned Share Class candidate does not need an independent root; it is a classification of equity terms, not the instrument and not the holding. Investment needs an independent unassigned root for the participation or commitment. Portfolio membership is a grouping, not identity. Holding does not need a new root.

Instrument/investment/holding: Separate investee or underlying asset, instrument, investment participation, and holding. Issuer capacity and holder capacity are distinct role facts. Terms stay on the instrument version. Quantity, lots, restrictions, and cost lineage stay on the WM-ECO-038 position. An investment may exist before a settled lot and may span several lots or instruments.

Transactions/postings: Acquisition, disposal, settlement, and conversion are events. Settlement is not the event and not the posting. Postings remain inside the WM-ECO-016 boundary and reference the event and the affected lots. No new transaction root.

Valuation: No new root. Profile WM-ECO-002 with mandatory subject-kind: instrument, holding, investee, or participation. Method, basis, currency, assumptions, inputs, model version, evidence, uncertainty, review, and supersession are required. Two same-date valuations under different methods or currencies both remain. Supersession is an explicit review act and does not delete the prior observation.

Conversion: A conversion right is a contingent term on an instrument version, not a current capacity. It confers no current votes and no current ownership. A conversion event must create predecessor position, successor position, and posting lineage. It must not overwrite the predecessor or the prior term version.

Ownership/voting/control: These are not roots here. They are derived only from effective ownership and governance facts, using Organization, Inter-organizational Relationship, and Governance Body. Reject the latest company valuation, any price, and any unexercised conversion right as a source of votes, ownership, control, or consolidation.

Time/currency/provenance: Effective time, observation time, and knowledge time are distinct. Currency is a property of the valuation, not of the instrument identity. Provenance travels with each observation and each posting link.

Governance: Control and consolidation read recognized governance facts only. A valuation review may supersede a value; it may not confer rights.

Scenario: One convertible instrument, term version fixed. Investment participation by the holder. Two lots under WM-ECO-038. On the same observation date, cost-basis USD and fair-value EUR valuations both persist with method, inputs, model version, evidence, uncertainty, and knowledge time. Neither updates votes. The investee enterprise valuation is rejected for control. Later conversion closes the debt lots, opens successor equity lots, and posts closing and opening lines with explicit lineage.

Invariants:
1. Instrument terms are immutable; change creates a new version with an effective interval; prior versions remain addressable.
2. Positions reference a specific term version.
3. Issuer and holder capacities are separate role facts.
4. Lots carry quantity, restrictions, and cost lineage independently of term text.
5. Contingent conversion rights confer zero current votes and zero current ownership.
6. Conversion emits predecessor position, successor position, and posting lineage, and does not overwrite the predecessor.
7. Two valuations may share subject and observation date and still differ in method, basis, currency, and result.
8. Supersession is an explicit review; it preserves the superseded observation and its provenance.
9. Valuation never sources voting, ownership, control, or consolidation.
10. Latest investee valuation is not evidence of voting power or control.
11. Effective, observation, and knowledge times are recorded separately.
12. Settlement, economic event, and journal posting are distinct objects.
13. Portfolio membership does not identify an Investment.
14. Share Class does not master the instrument or the holding.
15. Consolidation reads governance facts only.

Minimum model set: unassigned Financial Instrument root; unassigned Investment participation root; WM-ECO-038 as position master with lots; WM-ECO-002 profiled as Valuation with subject-kind; event plus WM-ECO-016 posting boundary; conversion right as term; conversion as specialized event with lineage; ownership, voting, control, and consolidation only via existing organization, relationship, and governance-body facts. Debt Instrument specializes or constrains the instrument root. Share Class stays subordinate.

Blockers: No identifier may be allocated. Specialization of WM-ECO-037 under the instrument root is undecided in the adjacent draft and must be fixed before any shared term model. Subject-kind on the valuation profile is mandatory and currently only proposed. Dual same-date valuations are unsafe until supersession cannot imply deletion. Contingent rights are unsafe until a hard exclusion from current votes is enforced. Do not claim publication readiness.

`

## candidate-allocation-offline-financial-instrument/allocation-candidate.json

`	ext
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FIN-06","proposedName":"Financial Instrument","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"A financial instrument exists before any holder and survives transfers and position closure while retaining governed issuer terms.","versionIdentity":"Issuance terms, conversion provisions, maturity, rights or governing conditions change through immutable instrument versions.","independentLifecycle":["draft","issued","effective","matured","converted","cancelled","retired"],"mastership":"instrument issuer or authoritative instrument registry"},
"boundary":{"owns":["stable instrument identity","issuer capacity and immutable terms","issuance and term versions","conversion, maturity and contingent-right provisions","governing law and successor lineage"],"references":[{"target":"WM-ECO-038","purpose":"Positions and holdings against an instrument version"},{"target":"WM-ECO-002","purpose":"Valuation assertions about an instrument"},{"target":"WM-ECO-016","purpose":"Accounting postings from instrument events"},{"target":"WM-ORG-001","purpose":"Issuer and investee identity"},{"target":"WM-ORG-012","purpose":"Control and relationship context"}],"excludes":["investee identity","investment participation identity","holder position and custody account","transaction and settlement occurrence","valuation and posting identity"]},
"objects":{"FinancialInstrument":{"identity":["financialInstrumentId"],"required":["instrumentKind","issuerRef","status","currentVersionRef"],"optional":["registryRef","successorRef"],"lifecycle":["draft","issued","effective","matured","converted","cancelled","retired"]},"InstrumentVersion":{"identity":["financialInstrumentId","version"],"required":["terms","rights","effectiveFrom","contentDigest"],"optional":["effectiveTo","maturity","conversionTerms","supersedesVersion"]}},
"invariants":["Investee, instrument, investment, position, transaction, posting and valuation remain distinct identities.","Instrument terms are immutable and versioned.","Issuer, holder, beneficial owner, nominee and custodian capacities remain distinct.","An instrument survives holder transfer and position closure.","Quantity, ownership percentage, voting power, cost, carrying amount and value remain separate assertions.","Contingent conversion rights are excluded from current voting and ownership denominators.","Conversion is an explicit event, not a term mutation.","Conversion preserves predecessor and successor position lineage.","Value never establishes ownership, voting, control or consolidation.","Instrument identity never derives from a mutable ticker or alias alone.","Corporate-action corrections append history.","Governing terms and evidence remain version-qualified.","Retired versions remain resolvable.","Instrument identifiers are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Overlap with WM-ECO-037 Debt Instrument and the Share Class candidate requires adjudication.","Independent Grok review is pending.","Trade, settlement, corporate-action and frozen crosswalk authorities remain incomplete."]}

`

## candidate-allocation-offline-financial-instrument/fixtures.json

`	ext
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Financial Instrument","cases":[{"id":"transfer-survival","kind":"positive","input":"A note transfers from holder A to holder B.","expect":"Instrument identity and terms persist while positions and holder capacities change."},{"id":"convertible-note","kind":"positive","input":"A note converts under versioned cap, discount and ratio terms.","expect":"An explicit event retires the predecessor position and creates successor positions against the resulting instrument version."},{"id":"instrument-valuation","kind":"positive","input":"Two same-date valuations use different methods and currencies.","expect":"Both remain separate assertions with original inputs and uncertainty."},{"id":"ticker-identity","kind":"negative","input":"A mutable ticker is used as sole instrument identity.","expect":"The identity is rejected without a governed identifier."},{"id":"future-votes","kind":"negative","input":"Contingent conversion rights are counted as current votes.","expect":"The denominator calculation is rejected."},{"id":"value-proves-control","kind":"negative","input":"A high valuation is used to establish control.","expect":"The inference is rejected."},{"id":"term-overwrite","kind":"negative","input":"Conversion terms are edited in an issued version.","expect":"The mutation is rejected; a successor version is required."}]}

`

## candidate-allocation-offline-financial-instrument/profile-candidate.json

`	ext
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-FIN-06","name":"Enterprise Investment Holding, Transaction and Valuation Binding","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ECO-038","WM-ECO-002","WM-ECO-016","WM-ORG-001","WM-ORG-012","WM-ORG-018"],"constraints":["WM-ECO-038 owns security-backed positions, quantities, lots, rights, restrictions and successor history.","WM-ECO-002 owns valuation assertions and must state subject-kind, basis, method, assumptions, currency, time, evidence and uncertainty.","Economic events own acquisition, disposal, subscription, transfer and conversion occurrences while WM-ECO-016 owns their accounting postings.","Trade, settlement, availability, position change and posting remain distinct states or events.","Contingent rights are excluded from current voting and ownership denominators.","Value never establishes voting power, control or consolidation treatment."],"holds":["Financial Instrument and Investment remain unassigned.","WM-ECO-038 relation and contingency conflicts require reconciliation.","Independent Grok review and frozen audit remain pending."]}

`

## candidate-allocation-offline-investment/allocation-candidate.json

`	ext
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FIN-06","proposedName":"Investment","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"A governed participation or exposure can persist through instrument replacement, temporary zero holdings, undrawn commitments and exited-but-retained history.","versionIdentity":"Mandate, commitment, stage, strategy or exit-context changes create effective-dated revisions while the participation identity persists.","independentLifecycle":["proposed","approved","committed","active","partially-exited","exited","retained","closed"],"mastership":"investment governance or portfolio authority"},
"boundary":{"owns":["stable governed participation identity","mandate and investment thesis","commitment and stage","instrument and position participation lineage","exit context and retained history"],"references":[{"target":"WM-ECO-038","purpose":"Positions and holdings realizing the investment"},{"target":"WM-ECO-002","purpose":"Investee, instrument and holding valuations"},{"target":"WM-ECO-016","purpose":"Accounting postings from investment events"},{"target":"WM-ORG-001","purpose":"Investee and investor identities"},{"target":"WM-ORG-018","purpose":"Investment governance and decision authority"}],"excludes":["plain portfolio membership","instrument terms","position quantity and custody","transaction or corporate-action occurrence","valuation and posting identity"]},
"objects":{"Investment":{"identity":["investmentId"],"required":["investorRef","investeeOrExposureRef","mandateRef","stage","status"],"optional":["commitment","exitContext","successorRef"],"lifecycle":["proposed","approved","committed","active","partially-exited","exited","retained","closed"]},"InvestmentParticipationRevision":{"identity":["investmentId","revision"],"required":["instrumentOrAssetRefs","positionRefs","effectiveFrom","contentDigest"],"optional":["effectiveTo","supersedesRevision","commitmentTerms"]}},
"invariants":["Investment identity requires governed participation beyond plain portfolio membership.","Investment can persist through temporary zero holding and instrument replacement.","Investment, instrument, position, transaction, posting and valuation remain distinct.","Mandate, commitment, stage and exit context are explicit.","Instrument and position lineage remain externally mastered.","An undrawn commitment does not imply a current position.","Exit does not erase retained governance or provenance history.","Acquisition, disposal, transfer and conversion remain explicit events.","Postings remain accounting representations and never become investments.","Value never establishes ownership, voting power, control or consolidation.","Different subject-kind valuations remain non-interchangeable.","Currency conversions preserve original amounts and rate provenance.","Corrections append history and preserve originals.","Investment identifiers are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","Portfolio, mandate, transaction and corporate-action references remain unallocated.","Frozen audit, crosswalks and registry relations remain pending."]}

`

## candidate-allocation-offline-investment/fixtures.json

`	ext
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Investment","cases":[{"id":"instrument-replacement","kind":"positive","input":"Convertible note N becomes preferred shares after conversion.","expect":"Investment identity persists while predecessor and successor positions retain lineage."},{"id":"undrawn-commitment","kind":"positive","input":"An approved investment has a commitment but no funded position.","expect":"The investment remains identifiable without inventing a holding."},{"id":"exited-retained","kind":"positive","input":"All positions are sold but governance retains an exited record.","expect":"The investment enters exited or retained state with immutable history."},{"id":"portfolio-row-mints-investment","kind":"negative","input":"Every listed position automatically creates an Investment root.","expect":"Creation is rejected without independent mandate and lifecycle."},{"id":"commitment-is-position","kind":"negative","input":"An undrawn commitment is counted as current owned quantity.","expect":"The assertion is rejected."},{"id":"valuation-is-holding","kind":"negative","input":"A valuation amount overwrites position quantity and cost.","expect":"The substitution is rejected."},{"id":"exit-deletes-history","kind":"negative","input":"Closing the final position deletes the investment record.","expect":"Deletion is rejected; exited lineage remains resolvable."}]}

`

