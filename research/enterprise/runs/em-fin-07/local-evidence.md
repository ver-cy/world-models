# EM-FIN-07 local synthesis

## Disposition

- Reuse WM-POL-011 as the Tax Obligation and authority-assessment master.
- Reuse WM-ECO-032 as the Tax Return master, with separate contained identities for revisions, filing attempts and acknowledgements.
- Profile Tax Calculation as an addressable assertion owned by either a return revision or an obligation assessment; do not create a calculation root.
- Propose an identifier-unassigned **Tax Registration / Account** root with time-qualified residence, source/place and nexus basis assertions.
- Demote WM-ACT-052 to a thin filing-and-assessment case correlation profile; its present aggregate duplicates WM-POL-011 and WM-ECO-032.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

WM-POL-011 owns obligation identity, legal basis, period and scope, tax-base and calculation assertions, assessments, notices, due components and balance snapshots. WM-ECO-032 owns return and revision identities, filing attempts, payloads and acknowledgements. Taxpayer, legal registration, jurisdiction, legal rule, payment and dispute remain external masters.

A Tax Registration / Account has an independent authority-created lifecycle: registration, identifiers, filing frequency, account state, group membership and deregistration. Legal-entity registration does not own it. Residence, source/place-of-supply and nexus are distinct, evidenced basis assertions attached to the relevant taxpayer, tax type, jurisdiction and interval.

WM-ACT-052 currently re-owns the union of return composition, calculation, submission, assessment, notice, liability, settlement and dispute. A useful case profile may own only a case identifier, scope tuple, orchestration state, deadlines and typed links.

## Registration, nexus and obligation

Registration, residence, source/place and nexus never collapse. An office address is only possible evidence for one basis under one rule; it never enumerates all obligations. Multiple jurisdictional bases coexist with separate authorities, rule versions, evidence, intervals and confidence.

One obligation is authority-qualified for a liable party, jurisdiction, tax profile and period. It pins legal provisions and versions, taxable events, chargeability, thresholds, exemptions, exclusions and reliefs. Potential, declared, assessed, payable, disputed, collectible and collected amounts remain distinct.

## Calculation

Declared calculations live with a return revision. Self-assessed, estimated, authority-calculated and reassessed liability assertions live with an obligation. Each assertion records inputs, rule/rate/formula versions, rounding, currency, origin, actor, assumptions, uncertainty, derivation and predecessor.

Equal totals do not merge calculations across homes. Recomputation appends a successor and preserves the original. Reusable rule, rate and formula definitions remain pinned external references.

## Return, filing and acknowledgement

Return, revision, filing attempt and acknowledgement have separate identities. One revision may have several attempts. Each attempt records payload digest, channel, endpoint, idempotency key and postmark; each acknowledgement correlates to an attempt.

Signed or submitted revisions and executed attempts are immutable facts. Amendments, corrections, supersessions and withdrawals append successors with an explicit class, reason, authority and change set.

## Assessment, payment and dispute

Receipt, technical validity, acceptance for processing, assessment, notice, legal effect, due balance, payment allocation, collectibility and finality are distinct assertions. Declared tax is not assessed liability, assessment is not payment, and one payment allocation does not discharge every obligation.

Payments remain WM-ECO-009 transactions with the EM-FIN-03 allocation profile. Disputes and appeals remain external proceedings with quantified links and suspension effects.

## Time, versions and provenance

Taxable-event time, period, rule effective interval, due date, preparation, signature, submission, postmark, receipt, acceptance, assessment, notice service, payment value date, observation, ingestion and knowledge time remain distinct.

Law, rule, rate, form, schema, taxonomy and code-set versions are pinned to effective period and knowledge time. This preserves reproducibility without asserting current law or rates.

## Acceptance result

Taxpayer T has a residence basis in J1 and source plus nexus bases in J2. Each basis has its own authority, evidence, rule version and interval. Obligations O1 and O2 are separate; neither follows automatically from an office address. For O2, return R1 has rejected attempt A1 and accepted attempt A2 with acknowledgement K2. Amended R2 supersedes R1 and is filed as A3 with K3. Declared calculations C1 and C2 coexist, while authority calculation C3 supports assessment S1 and notice N1. O1 remains unaffected.

## Required invariants

1. Obligation, return revision, filing attempt, acknowledgement, assessment, notice, balance, payment and dispute never merge.
2. Legal registration and tax registration remain distinct.
3. Residence, source/place and nexus are separately evidenced bases.
4. An address never derives an obligation.
5. Concurrent jurisdictional bases coexist without implicit ranking or netting.
6. Rules, rates, forms, schemas and taxonomies are version-pinned to effective and knowledge time.
7. Submitted revisions and executed attempts are immutable.
8. Corrections and amendments append successors.
9. One revision may have multiple attempts, each separately correlated.
10. Declared, assessed, payable, disputed, collectible and collected amounts remain distinct.
11. Receipt, validity, acceptance, assessment, payment and finality never imply each other.
12. Calculation assertions state origin, actor, versions, currency, rounding and lineage.
13. Cross-home calculations correlate but do not become identical.
14. Amounts preserve type, currency, unit, precision, period and provenance.
15. Official acts require competent authority.

## Holds

WM-POL-011, WM-ECO-032 and WM-ACT-052 overlap as three aggregate roots. Registry parent signals have no approved relation-ledger edges and conflict with WM-ECO-032's provisional-reference boundary. Tax Registration / Account, rate-schedule ownership and source masters remain unallocated. Jurisdiction and tax-type profiles, source pins, crosswalks, privacy controls and acceptance fixtures remain incomplete. Base drafts are non-canonical and single-provider, so no installability or publication-readiness claim is made.
