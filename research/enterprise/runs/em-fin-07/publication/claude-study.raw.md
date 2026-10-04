# EM-FIN-07 — Tax Profile, Obligation and Filing: independent adjudication

## Verdict

- **TaxObligation → reuse WM-POL-011.** Obligation identity, legal basis, period, scope, assessment, notice, due components and balance snapshots are already owned there. No new root.
- **TaxProfile → split.** Obligation-scoped tax classification (tax type, obligation class, jurisdiction, administration profile) is already WM-POL-011's. A persistent **taxpayer tax registration / tax account** with its own lifecycle (registration, group membership, filing frequency, deregistration) and its **basis assertions** (residence, source, place of supply, nexus) is owned by none of the three drafts and needs independent identity. Recorded as an identifier-unassigned candidate; **no identifier allocated here.**
- **TaxCalculation → profile, not new.** A calculation is an owned, addressable, source-qualified assertion inside its asserting aggregate (obligation or return revision). The dossier shows no identity or lifecycle independent of that chain. The genuinely reusable object is the *rule/rate/formula/form-schema version*, which is a pinned reference, not a calculation run.
- **TaxReturn and TaxFiling → reuse WM-ECO-032.** It already carries return-revision and filing-attempt as separate member identities, plus acknowledgement. Both candidates resolve inside one master; no new root.
- **WM-ACT-052 → duplicate root; demote.** As specified it re-owns return composition, calculation, validation, declaration, submission, acknowledgement, self-assessment, authority assessment, notice, liability, allocation and dispute — the union of the two subject masters. Useful only if reduced to a thin case profile owning case identity, scope tuple, orchestration state, deadlines and typed cross-links, with every subject-owning claim stripped.
- **No catalogue or runtime identifier is allocated by this review.**

## Evidence

All three drafts are `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, single-provider (Codex) with Claude and Grok waived. WM-POL-011 `in_scope` lists return links, tax-base and calculation assertions, assessments, notices, balances. WM-ECO-032 `scope_statement` lists return and revision identities, filing attempts, acknowledgements, and declares WM-POL-011 "a provisional parent signal only… no settled containment edge." WM-ACT-052 `scope_statement` lists return composition, calculations, validations, declaration, submission, acknowledgement, self-assessed and authority-determined positions, notice, liability, settlement and dispute. The frozen `relations` ledger contains no tax rows; registry `parent_ids` assert WM-POL-011 for both WM-ECO-032 and WM-ACT-052.

## Identity/mastership

Nineteen facts must stay separately identified: taxpayer subject (WM-ORG-001); legal registration (WM-ORG-010); tax registration/account (gap); residence, source/place, nexus bases (gap, basis-scoped); jurisdiction (WM-POL-015); versioned legal rule (WM-POL-001); obligation (WM-POL-011); taxable event (external reference); period (obligation attribute); calculation assertion (owned record, two homes); return revision and filing attempt (WM-ECO-032); acknowledgement (WM-ECO-032); authority assessment, notice, balance (WM-POL-011); payment/allocation (WM-ECO-009 + prior EM-FIN-03 allocation profile); dispute (external case); process case (demoted WM-ACT-052). None of these may be canonicalised by taxpayer name, tax type, period, date, amount or digest.

## Tax profile/registration/nexus

Registration ≠ residence ≠ nexus. Registration is an administrative act by a named authority creating an account identity, filing frequency and validity interval. Residence is a legal status assertion under a pinned rule. Source/place-of-supply and nexus are per-transaction or per-activity connecting factors. Each is a separately evidenced, time-qualified assertion with its own authority, rule version and confidence. Multiple bases coexist without ranking. **Negative case rejected:** an office address is at most one evidence item supporting one basis, for one tax type, in one jurisdiction, for one period. It never enumerates obligations.

## Obligation/rules/period

One obligation = (authority, jurisdiction, tax profile, liable party, period), authority-qualified. Legal basis binds provision anchors with effective interval and interpretation status via WM-POL-001. Period, chargeability, threshold, exemption and relief are obligation-scoped assertions. Potential, declared, assessed, payable, disputed, collectible and collected amounts stay distinct components — already WM-POL-011 policy and preserved.

## Calculation

Two legitimate homes, never merged: **declared** values inside a return revision (WM-ECO-032 `derive-declared-values`) and **liability** assertions inside the obligation (WM-POL-011 `assemble-tax-base-calculation`, with origin self-assessed / authority / estimate / reassessment). A calculation assertion records inputs, rule and rate versions, formula version, rounding, currency, origin, actor, assumptions, uncertainty, superseded predecessor and derivation graph. Cross-home links are **correlation only**; equal totals never prove equal assertions. Recomputation appends a successor version; it never edits a predecessor.

## Return/filing

Return, revision, filing attempt and acknowledgement are four identities. One revision may have many attempts (retry, duplicate, replacement); each attempt has its own payload digest, channel, endpoint, idempotency key and postmark; each acknowledgement correlates to one attempt. Submitted revisions and executed attempts are immutable facts. Amendment, correction, supersession and withdrawal append linked successors with change set, reason and authority. Return class (original, amended, corrected, superseding, supplemental, final, nil, information) is explicit, never inferred from sequence.

## Assessment/payment/dispute

Receipt, technical/schema validity, acceptance-for-processing, authority assessment, notice, legal effect, due date, payable balance, payment, collectibility and finality remain independent assertions. None proves another. Declared tax is not assessed liability; assessment is not payment; payment allocation is not discharge of every obligation; notice is not finality. Payments and allocations stay in the payment master with typed references; disputes stay external with typed links and quantified suspension effects.

## Multi-jurisdiction

Concurrent bases are preserved side by side with asserting authority, rule version and evidence. Relief or allocation (credit, exemption, treaty route) is a recorded assertion with its own basis, never an automatic netting. No basis is suppressed because another exists; overlap is classified, not resolved.

## Time/version/provenance

Distinct axes: taxable event, period boundary, rule effective interval, due, preparation, signature, submission, postmark, receipt, rejection, acceptance, assessment issue, legal effect, notice service, payment value date, observation, ingestion and knowledge time. Applicable law, rule, rate, form, schema, taxonomy and code-set versions are pinned to effective period **and** knowledge time, so a recomputation is reproducible as-of any past instant.

## Governance/privacy

Tax data is restricted by default; purpose-bound, attributable, logged access. Only the competent authority or an authorised filer may establish official assessment or filing assertions. Agents may propose calculations and perform reversible clerical operations; legal interpretation, adverse assessment, disclosure, enforcement and destruction of cited history require accountable authority. Retention honours statutory minima and legal hold; closure and tombstone replace deletion.

## Acceptance scenario

Taxpayer T holds a residence basis in J1 and both a source basis and a nexus basis in J2 — three assertions, three authorities, three rule versions, no ranking. Obligation O1 (J1, period P) and O2 (J2, period P) are separate aggregates; neither is inferred from T's office address. For O2, return revision R1 is signed, attempt A1 is rejected on schema, attempt A2 is accepted with acknowledgement K2. Amended revision R2 supersedes R1 immutably and is filed as attempt A3 with acknowledgement K3. Declared calculation C1 (R1) and C2 (R2) coexist; authority calculation C3 produces assessment S1 with notice N1 for O2. O1 is unaffected. Grounds, calculation versions, receipts and authority responses remain four distinct, separately resolvable sets.

## Invariants

1. Obligation, return revision, filing attempt, acknowledgement, assessment, notice, balance, payment and dispute identities never merge.
2. Registration, residence, source/place and nexus are separate evidenced bases.
3. An address never derives an obligation.
4. Concurrent bases coexist unranked; suppression is a defect.
5. Every rule, rate, form, schema and taxonomy reference is version-pinned to effective period and knowledge time.
6. Submitted revisions and executed attempts are immutable; corrections append successors.
7. One revision may have many attempts; each attempt has at most one correlated authority response.
8. Declared, assessed, payable, disputed, collectible and collected amounts stay separate components.
9. Receipt ≠ validity ≠ acceptance ≠ assessment ≠ payment ≠ finality.
10. A calculation assertion carries origin, actor, rule versions and predecessor; recomputation appends.
11. Cross-home calculation links are correlation, never equality.
12. A return class is declared, never inferred.
13. Amounts carry type, currency, unit, precision, period, source and provenance.
14. Event, authority-recording, observation and knowledge times remain distinct.
15. No aggregate asserts an official act without competent authority.

## Minimal model set

WM-POL-011 (obligation/assessment master) · WM-ECO-032 (return/filing master) · WM-POL-001 (rule versions) · WM-POL-015 (jurisdiction) · WM-ORG-001 (taxpayer subject) · WM-ORG-010 (legal registration, distinct from tax registration) · WM-ECO-009 with the EM-FIN-03 allocation profile (payment) · one identifier-unassigned **Tax Registration / Account + basis assertion** candidate · one thin EM-FIN-07 enterprise binding profile · WM-ACT-052 demoted to a case-correlation profile.

## Holds

Three-way duplicate root across WM-POL-011 / WM-ECO-032 / WM-ACT-052 blocks boundary sign-off. Registry `parent_ids` assert containment that the frozen relation ledger does not record — contradiction unresolved. Registry `entry_kind: standalone-mm` and document `entryKind: aggregate` are separate axes and must not be conflated. All three drafts are single-provider with independent external review waived. Tax registration/account ownership, rate-schedule catalogue ownership, jurisdiction and tax-type profiles, source pins, crosswalks and fixtures remain open. This review states no current law and no tax rates, and claims no canonical completeness, installability or publication readiness.
