The team is aligned on reuse and identity. One residual (Balance) is resolved as a separate asserted position, not a minted root. Final review follows.

Verdict. Conditional accept. Reuse WM-POL-011 for obligation and authority assessment. Reuse WM-ECO-032 for return revisions, filing attempts, and acknowledgements. Treat Tax Calculation as an owned assertion. Keep one identifier-unassigned Tax Registration/Account candidate with separate residence, source/place, and nexus assertions. Demote WM-ACT-052 to a thin case-correlation profile. Allocate no identifier. Do not treat this pack as publication-ready.

Strongest evidence. An amended return across two jurisdictions splits grounds, calculations, attempts, receipts, and authority responses without a shared calculation root and without office-address nexus. Legal Registration and Tax Registration/Account already diverge in lifecycle: personality can exist with zero, one, or many tax accounts; an account can be suspended while legal personality continues.

Strongest counterexample. Source-only withholding or payee-withheld remittance: taxable event, obligation, and payment exist with no taxpayer-facing account and no return revision. Forcing Tax Registration/Account there creates a phantom root. Authority assessment without a taxpayer-owned return is still an Assessment owning a calculation, not a floating Calculation root.

Identity/mastership. Independent roots (no identifiers allocated): Taxpayer (party role); Legal Registration; Tax Registration/Account (unassigned; instantiate only on an authority handle or explicit account-opening event); Legal Rule; Obligation; Taxable Event; Period; Return Revision; Filing Attempt; Acknowledgement; Assessment; Notice; Payment/Allocation; Dispute; Process Case (thin). Not roots: TaxProfile (non-owning view); TaxCalculation (owned assertion); TaxReturn/TaxFiling (profiles over WM-ECO-032); TaxObligation (profile over WM-POL-011); jurisdictional bases (assertions); declared/assessed/payable/paid/final (states). Balance is a separate asserted position on Registration/Account or Obligation, knowledge-timed; not a minted identity and not a second master of Assessment or Payment. Duplicate boundaries: EM-FIN-07 must not remaster WM-POL-011 or WM-ECO-032; WM-ACT-052 must not own amounts, revisions, or legal outcomes; Legal Registration ≠ Tax Registration/Account; Obligation ≠ Assessment ≠ Notice ≠ Balance; Filing Attempt ≠ Acknowledgement ≠ Return Revision.

Registration/nexus. Tax Registration/Account is a jurisdictional relationship artifact, not a party. Identity, when present, is authority-assigned; the model does not mint a surrogate. Residence, source/place, and nexus are concurrent, independent basis assertions. Office address does not create a basis, a registration, or an obligation. Basis does not entail registration; registration does not entail obligation.

Obligation/rules. Obligation is mastered in WM-POL-011. It requires a pinned Legal Rule version and at least one jurisdictional ground. Taxable Event and Period remain separate roots. Assessment is a distinct authority act over an obligation, not the obligation itself.

Calculation. Owned assertion, not a root. Each assertion binds to exactly one of Obligation, Return Revision, or Assessment, plus period, ground set, and pinned rule/rate/form/schema/taxonomy/code-set versions. Two grounds in one period imply two calculation assertions. Declared, assessed, amended, and disputed calculations may coexist.

Return/filing. Return Revision, Filing Attempt, and Acknowledgement are mastered in WM-ECO-032. Submitted revisions and attempts are immutable. Amendments and corrections are append-only successors. Acknowledgement of a filing is not an assessment.

Assessment/payment/dispute. Assessment and its authority semantics stay in WM-POL-011. Notice is a distinct authority communication. Payment/Allocation references Obligation, Assessment, or an asserted Balance; it does not overwrite declared or assessed calculations. Dispute is its own root. Process Case correlates work; it does not own the economic or policy objects.

Multi-jurisdiction. One Taxpayer may hold concurrent grounds and zero-to-many accounts across authorities in one period. Each ground carries its own obligation, calculation set, attempts, and authority responses. No shared calculation across grounds.

Time/version/provenance. Every Legal Rule, rate, form, schema, taxonomy, and code-set version is pinned to an effective period and a knowledge time. Revisions, attempts, acknowledgements, assessments, notices, and payments are append-only provenance. Knowledge time and effective time are not aliases.

Privacy/governance. TaxProfile is a convening view, not a master store of registrations or amounts. Access and retention attach to Taxpayer, Registration/Account, Return Revision, and Dispute, not to a collapsed profile. No model-allocated tax identifier.

Scenario. Party P has Legal Registration L. Residence basis in J1; source/place and nexus bases in J2 from activity, not from office address. Candidate accounts A1 (J1) and A2 (J2), identifiers unassigned. Period T. Events E1 (J1) and E2 (J2). Obligations O1 under rule-set R1 and O2 under R2, each pinned by effective period and knowledge time. J1 revision V1 owns declared calculation C1; attempt F1; acknowledgement K1. J2 revision V2 owns C2-declared; attempt F2; acknowledgement K2. Amendment creates V1′ (V1 preserved) owning C1-amended, attempt F1′, acknowledgement K1′. J2 assessment S2 owns C2-assessed ≠ C2-declared; notice N2; balance position B2; payment allocated to B2/O2; dispute D2. Process case PC2 only correlates F2, S2, N2, D2.

Invariants.

1. Tax Registration/Account is neither Taxpayer nor Legal Registration.
2. No model-allocated identifier for Tax Registration/Account or Calculation.
3. Residence, source/place, and nexus are separate; office address implies none of them.
4. Obligation requires a pinned Legal Rule and at least one ground; address is not a ground.
5. A calculation has exactly one owner in {Obligation, Return Revision, Assessment}.
6. Submitted revisions and attempts are immutable; corrections append.
7. Acknowledgement ≠ Assessment ≠ Notice.
8. Declared, assessed, payable, paid, and final are distinct and may disagree.
9. Payment/Allocation does not mutate an assessment or a declared calculation.
10. One Taxpayer may have multiple grounds and accounts in one period.
11. Process Case correlates and does not own policy or economic roots.
12. Rule/rate/form/schema/taxonomy/code-set versions carry effective period and knowledge time.
13. TaxProfile cannot master registrations, obligations, calculations, or filings.
14. Legal Registration does not entail Tax Registration/Account or any obligation.
15. Two grounds in one period imply two obligations and two calculation assertions.
16. Obligation plus event plus payment may exist with no Tax Registration/Account.

Minimum model set. Taxpayer; Legal Registration; Tax Registration/Account (unassigned); BasisAssertion (residence | source/place | nexus); Jurisdiction; LegalRule (versioned); TaxableEvent; Period; Obligation (WM-POL-011); Calculation (owned); ReturnRevision; FilingAttempt; Acknowledgement (WM-ECO-032); Assessment (WM-POL-011); Notice; Balance (asserted position); PaymentAllocation; Dispute; ProcessCase (thin WM-ACT-052); TaxProfile as view only.

Blockers. Allocating an identifier to Tax Registration/Account or Calculation. WM-ACT-052 retaining ownership of obligation, return, assessment, balance, or payment. TaxProfile or office address treated as obligation generators. Collapsing declared/assessed/payable/paid/final into one amount. Missing dual pin of effective period and knowledge time. Requiring a phantom account on withholding-only paths. Treating Balance as a second master of Assessment and Payment, or erasing it into those roots. Any publication-readiness claim.
