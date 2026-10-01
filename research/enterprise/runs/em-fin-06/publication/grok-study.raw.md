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
