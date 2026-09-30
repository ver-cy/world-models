# Frozen semantic audit prompt — EM-FIN-07

You are the sole frozen semantic auditor for this contour. This audit is run exactly once. Use only the supplied text. Do not browse, call tools, state current law or rates, invent identifiers, claim standards conformance or propose publication of blockers.

Audit the reconciled EM-FIN-07 boundary and allocation/profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence/privacy semantics, non-deterministic fixtures and missing publishability holds. Preserve the intended decision unless supplied evidence disproves it: reuse WM-POL-011 for obligation/assessment; reuse WM-ECO-032 for return revisions/filing attempts/acknowledgements; keep Tax Calculation as an owned assertion; keep Tax Registration / Account independently identified but identifier-unassigned and optional (never a mandatory bridge); demote WM-ACT-052 to thin case correlation; allocate no catalogue, model or runtime ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect give exact deterministic remediation; Exact additional fixtures as a JSON array; and final freeze decision. Be sceptical and concise. If there are no material defects, say so explicitly. Never request another provider run.

## LOCAL SYNTHESIS

```text
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

```

## CLAUDE FROZEN STUDY

```text
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

```

## EXACT GROK RESPONSE

```text
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

```

## PROVIDER COMPARISON

```text
# EM-FIN-07 provider comparison

Claude and Grok agree on the primary boundary: reuse WM-POL-011 for obligation and authority assessment; reuse WM-ECO-032 for return revisions, filing attempts and acknowledgements; keep Tax Calculation as an owned assertion; retain one independently identified but identifier-unassigned Tax Registration / Account candidate; demote WM-ACT-052 to a thin case-correlation profile; allocate no catalogue, model or runtime identifier.

Both reviews separate taxpayer, Legal Registration, Tax Registration / Account, jurisdictional grounds, legal rules, obligation, taxable event, period, calculation, return revision, filing attempt, acknowledgement, assessment, notice, balance, payment/allocation, dispute and process case. They preserve append-only submitted revisions and attempts, dual effective/knowledge-time pins and distinct declared, assessed, payable, paid and final states.

Grok sharpens optionality: an authority-assigned account is instantiated only on an authority handle or explicit account-opening event. A withholding-only path may have event, obligation and payment without a taxpayer-facing account or return, so Registration / Account is never a mandatory bridge. Residence, source/place and nexus grounds are concurrent assertions; office address implies none. Legal Registration does not entail a tax account or obligation.

Grok also makes Calculation ownership exclusive across Obligation, Return Revision or Assessment; Balance is a knowledge-timed asserted position rather than an independent root; and Process Case may correlate work but own no amount, revision, legal outcome, assessment or payment. These sharpen the Claude boundary without changing the decision.

Publication remains held by the unallocated Tax Registration / Account candidate, three-way draft overlap, unapproved parent/relation signals, unresolved rate-schedule and jurisdiction/tax-type ownership, incomplete privacy/source/crosswalk fixtures and single-provider non-canonical bases. The result is reviewable research with no installability or publication-readiness claim.

```

## ALLOCATION CANDIDATE

```json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FIN-07","proposedName":"Tax Registration / Account","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"An authority-created tax registration or account persists across periods, returns, assessments and payments independently of legal-entity registration.","versionIdentity":"Tax type, filing frequency, group membership, account state or jurisdictional basis changes append effective-dated revisions and assertions.","independentLifecycle":["pending","registered","active","suspended","deregistered","closed"],"mastership":"competent tax authority or authoritative tax-registration system"},
"boundary":{"owns":["stable tax registration or account identity","authority-issued identifiers","tax type and filing frequency","account state and group membership","deregistration and successor lineage","time-qualified residence, source/place and nexus basis assertions"],"references":[{"target":"WM-POL-011","purpose":"Tax obligations and authority assessments"},{"target":"WM-ECO-032","purpose":"Return revisions, filing attempts and acknowledgements"},{"target":"WM-ORG-001","purpose":"Taxpayer identity"},{"target":"WM-ORG-010","purpose":"Legal registration kept distinct from tax registration"},{"target":"WM-POL-001","purpose":"Versioned legal rules supporting jurisdictional bases"},{"target":"WM-ECO-009","purpose":"Payments and allocation to obligations"}],"excludes":["legal-entity registration","tax obligation and balance","return or filing attempt","assessment and notice","payment and dispute lifecycle"]},
"objects":{"TaxRegistrationAccount":{"identity":["taxRegistrationAccountId"],"required":["taxpayerRef","authorityRef","jurisdictionRef","taxTypeRef","status","currentRevisionRef"],"optional":["authorityIdentifier","successorRef"],"lifecycle":["pending","registered","active","suspended","deregistered","closed"]},"RegistrationRevision":{"identity":["taxRegistrationAccountId","revision"],"required":["filingFrequency","effectiveFrom","contentDigest"],"optional":["effectiveTo","groupMembership","supersedesRevision"]},"JurisdictionalBasisAssertion":{"identity":["basisAssertionId"],"required":["basisKind","subjectRef","taxTypeRef","jurisdictionRef","ruleVersionRef","evidenceRefs","validFrom"],"optional":["validTo","confidence","supersedesRef"]}},
"invariants":["Legal registration and tax registration remain distinct.","Registration, residence, source/place and nexus never collapse.","Residence, source/place and nexus are separately evidenced assertions.","An address never derives an obligation or registration by itself.","Concurrent jurisdictional bases coexist without implicit ranking or netting.","Every basis states authority, rule version, evidence and interval.","Registration never replaces obligation, return, assessment or payment identity.","Taxpayer identity remains externally mastered.","Authority-issued identifiers are scoped to authority, jurisdiction and tax type.","State changes are effective-dated and preserve history.","Deregistration never erases prior returns or obligations.","Official acts require competent authority.","Privacy and access controls follow taxpayer and authority policy.","Retired identifiers and revisions remain resolvable and are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","WM-POL-011, WM-ECO-032 and WM-ACT-052 aggregate overlap requires adjudication.","Rate-schedule ownership, jurisdiction profiles, frozen audit and crosswalks remain incomplete."]}

```

## PROFILE CANDIDATE

```json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-FIN-07","name":"Enterprise Tax Obligation, Return and Filing Binding","decision":"PROFILE","newRuntimeId":false,"bases":["WM-POL-011","WM-ECO-032","WM-ACT-052","WM-POL-001","WM-POL-015","WM-ORG-001","WM-ORG-010","WM-ECO-009"],"constraints":["WM-POL-011 owns obligation identity, legal basis, period, tax base, assessments, notices, due components and balances.","WM-ECO-032 owns return and revision identity, filing attempts, payloads and acknowledgements.","Tax calculations are addressable assertions owned by a return revision or obligation assessment and never form another root.","WM-ACT-052 is limited to case correlation, scope tuple, orchestration state, deadlines and typed links.","Return revision, filing attempt and acknowledgement have separate identities and one revision may have several attempts.","Declared, assessed, payable, disputed, collectible and collected amounts remain distinct."],"holds":["Tax Registration / Account remains unassigned.","Three-way aggregate overlap and parent signals require reconciliation.","Independent Grok review and frozen audit remain pending."]}

```

## FIXTURES

```json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Tax Registration / Account","cases":[{"id":"two-jurisdictions","kind":"positive","input":"Taxpayer T has residence in J1 and source plus nexus bases in J2.","expect":"Separate basis assertions retain authority, rule version, evidence and interval without implicit netting."},{"id":"multiple-filing-attempts","kind":"positive","input":"Return revision R1 has rejected attempt A1 and accepted A2.","expect":"The registration stays stable while attempts and acknowledgements remain separately identified."},{"id":"deregistration-history","kind":"positive","input":"An account is deregistered after the final period.","expect":"Prior obligations, returns and authority identifiers remain resolvable."},{"id":"address-creates-obligation","kind":"negative","input":"An office address automatically creates all tax obligations.","expect":"The inference is rejected without a rule-qualified basis and authority."},{"id":"legal-registration-merge","kind":"negative","input":"A company registration number is used as the tax-account identity in every jurisdiction.","expect":"The identity merge is rejected."},{"id":"basis-collapse","kind":"negative","input":"Residence, source and nexus are stored as one undifferentiated flag.","expect":"The assertion is rejected."},{"id":"deregister-delete","kind":"negative","input":"Deregistration deletes prior filings and assessments.","expect":"Deletion is rejected; history must remain resolvable."}]}

```
