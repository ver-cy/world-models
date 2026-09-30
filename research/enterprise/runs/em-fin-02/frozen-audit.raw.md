# Frozen audit — EM-FIN-02

**Verdict: REJECT FOR ALLOCATION; candidate revision 3 required.** The reuse split (015 external accounts / 016 entries+postings / 017 derived balances / new candidate for Chart, Ledger Account, policy, adoption) is sound and the Grok correction — Ledger Account cannot profile WM-ECO-015 — is correctly absorbed. The correspondence-only profile is correctly non-mastering in intent. But the declarative package does not yet enforce its own prose: several boundary rules exist only in narrative, the Ledger Account key destroys the stable identity the candidate claims, period/close state has no master, and fixture traceability is positional and partly mis-mapped. `publishable: false` and the registry hold are correctly retained.

## Material defects

### Anti-dual-mastership

**D01 — Divergence and cross-ledger mapping are owned twice.** Candidate `boundary.owns` claims "cross-ledger mapping definitions and divergence semantics"; the profile records "cross-ledger mapping evidence" and divergence reasons. No text separates definition from instance.
*Remediation:* candidate owns the divergence-reason vocabulary and mapping-rule definitions only; profile instances must cite a candidate-defined reason code and may define none.

**D02 — Accounting period and close state have no master.** Every hard-close rule and the phrase "earliest permitted later period" depend on a period calendar and a per-ledger open/hard-closed state. The candidate owns `closeRules` (policy), 016 owns entries, 017 owns balances, the profile owns nothing. The governing state is unassigned.
*Remediation:* add an owned object `LedgerPeriod` — identity `[ledgerRef, periodId]`, required `state` (open | soft-closed | hard-closed), `authorityRef` — and an invariant that close state is read only from it.

**D03 — Correction links have no master or vocabulary.** Fixtures expect "a linked reversal or adjustment" and "restatement"; no object, invariant or constraint defines the link or assigns it.
*Remediation:* assign the entry-to-entry correction link to WM-ECO-016 as an intra-ledger relation with closed kinds (reverse | adjust | restate); state the profile never carries it.

### Ledger Account vs Financial Account identity

**D04 — `LedgerAccount.identity` includes `chartRevisionRef`, so every chart revision mints a new account identity.** This contradicts `identityTest.stableIdentity` ("remain identifiable across hierarchy revisions"), the `chart-successor` fixture, and 017 balance continuity across a revision boundary.
*Remediation:* stable ledger-scoped `ledgerAccountId`; versioned key `[ledgerAccountId, effectiveFrom]`; `chartRevisionRef` becomes a required attribute, `predecessorRef` required on continuation.

**D05 — No interval or code-uniqueness constraints.** Nothing forbids two simultaneously effective Ledger Accounts for the same node, or two effective accounts sharing `accountCode` inside one ledger. I04 only denies cross-ledger/cross-revision code identity.
*Remediation:* add invariants — intervals per `(ledgerRef, nodeId)` never overlap; `accountCode` is unique within `(ledgerRef, effective instant)`.

**D06 — The posting-target rule exists only in prose.** "A posting target is always a Ledger Account, never a raw WM-ECO-015 Financial Account" is absent from `invariants`; fixture `raw-financial-account-posting` therefore traces to I01/I02, which do not state it.
*Remediation:* add invariant "every Posting targets exactly one Ledger Account; a WM-ECO-015 Financial Account is never a posting target."

**D07 — Backing schema cannot express its own invariant.** I06 and the `optional-financial-backing` fixture require "per declared context and interval" and "declared entity"; the object has a single scalar `financialAccountBackingRef` with no context or interval fields.
*Remediation:* replace with `backings[]` of `{financialAccountRef, contextRef, effectiveFrom, effectiveTo}` and constrain at most one effective per context.

### Chart and policy lifecycle

**D08 — Lifecycle is declared once and enforced nowhere.** `AccountingPolicy.status` has no enum and no transition rules; `ChartRevision` has no approval state; "suspended" and "retired" have no defined effect on already-pinned revisions or on active adoptions. I16 preserves resolvability but permits retiring a chart a ledger still adopts.
*Remediation:* give `AccountingPolicy` the same explicit lifecycle enum; add invariants — lifecycle transitions never alter pinned revisions; suspension blocks new adoption and new postings from an effective-dated instant only; retirement requires no effective adoption or an effective-dated successor adoption.

### Ledger adoption cardinality

**D09 — Concurrent multi-chart adoption is permitted.** `LedgerAdoption.identity = [ledgerRef, chartOfAccountsId, effectiveFrom]` lets one ledger hold effective adoptions of two different charts simultaneously, contradicting I03. `revocationRef` is undefined and could retroactively invalidate pinned revisions. The hold correctly flags cardinality as unadjudicated, but no fixture forces the decision.
*Remediation:* identity `[ledgerRef, effectiveFrom]`; invariant "at most one adoption is effective per ledger at any instant, across all charts"; revocation is effective-dated closure only, never retroactive past a posted entry.

**D10 — Two policy-pinning paths with no precedence.** `LedgerAdoption.policyRevisionRef` and `LedgerAccount.policyRevisionRef` can disagree, and I05 does not say which wins. `policyKind` implies a set of policies per ledger while both fields are singular.
*Remediation:* adoption carries `policyRevisionRefs[]`, at most one effective per `policyKind`; `LedgerAccount.policyRevisionRef` becomes an optional narrowing that must lie in the same policy lineage; adoption governs on conflict.

### Effective revision pinning

**D11 — Only one time dimension exists.** I05 pins "on its accounting date", which is undefined and not carried on any object; without a record time, a late correction with an accounting date inside a hard-closed period cannot be distinguished from an edit, which is exactly the `hard-close` fixture pair.
*Remediation:* require `accountingDate` and `recordedAt` on every entry and posting; pin revisions by `accountingDate`; evaluate close permission against period state at `recordedAt`.

### Currency roles

**D12 — Roles are enumerated but unbound.** No invariant fixes exactly one balancing currency role per ledger; the translation-residual rule appears only in the synthesis prose; 017 balances are qualified by "currency" with no role, so an EUR balance is ambiguous between transaction, functional and presentation.
*Remediation:* closed role vocabulary; invariant "each ledger declares exactly one balancing currency role"; invariant "translation residuals post inside the same ledger under its pinned policy"; add `currencyRole` to the 017 qualification key.

**D14 — FX rate mastership and pinning are unstated.** WM-XCT-014 is referenced for "rate context where applicable" with no invariant, so a restated rate could silently change a posted amount — a direct breach of I10 by a path I10 does not cover.
*Remediation:* invariant "every translated posting pins rate identity and revision from WM-XCT-014; a rate correction never mutates a posted amount and requires a linked same-ledger correction entry."

### Balancing scope and tolerance

**D13 — Tolerance permits an unrecorded residual.** `tolerance` is required with no unit or dimension and no rule about what happens to a residual inside it. As written, an entry may be accepted while its postings do not sum to zero, which breaks 017 derivation from 016.
*Remediation:* tolerance is a detection threshold only; any nonzero residual must post to a designated residual Ledger Account in the same ledger, so postings sum to exactly zero in the balancing currency role.

**D15 — "Scope" is undefined and used as a key.** `balancingScope` in policy and "scope" in the 017 qualification are never defined or related; the hold acknowledges this but nothing forces one definition.
*Remediation:* policy revision declares an explicit scope dimension vector; require the same declared vector to qualify both balancing evaluation and balance assertions.

### External-event correlation and sibling divergence

**D16 — Sibling-group cardinality is undefined.** The rules assume one entry per ledger per event. Neither an entry citing several events nor a ledger booking two entries for one event is addressed, yet both are ordinary. Divergence reason is free text and pins neither sibling's policy revision.
*Remediation:* state event↔entry correlation is many-to-many; define the sibling group as `(eventRef, ledgerRef) → set of entries`; attach the divergence reason to the ledger's correlation set, drawn from the candidate's closed vocabulary, pinning both sides' policy revisions.

### Append-only correction, hard close, WM-ECO-017 immutability

**D17 — Hard-close wording and effect are inconsistent.** I11 says "next-period correction"; the synthesis and the `hard-close-restricted-cash-correction` fixture say "earliest permitted later period" — these differ whenever the next period is also closed. Separately, "explicitly authorised exception" has no defined effect and is not distinguished from amendment.
*Remediation:* adopt "earliest open permitted later period" in all three places; define the exception as authorising an appended, linked correction entry with an accounting date inside the closed period, carrying `authorityRef`, and never an amendment of an existing entry or closed balance.

**D18 — 017 immutability is scoped only to closed balances.** I13 leaves open-period assertions overwritable in place, so a stated as-of assertion is not reproducible.
*Remediation:* "every emitted balance assertion is immutable regardless of period state; recomputation emits a successor assertion with its own as-of and basis."

### Correspondence-only profile and fixture traceability

**D19 — The profile's decisive base is not in `bases`.** The profile constrains Ledger Account ownership to the candidate, which is absent from `bases`, so its dependency chain is unresolvable and invisible.
*Remediation:* add the candidate as a declared base placeholder with `allocationState: unassigned`, and make the profile non-instantiable while any base is unallocated.

**D20 — Correspondence-only vs required supersession.** "Every binding … is append-only with supersession" and `cascade-delete` both require the binding record to be referenceable, while `newRuntimeId: false` and "mints no … identity" forbid any key.
*Remediation:* permit a profile-local binding key explicitly typed as non-subject and non-resolvable outside the profile; state it is never a subject identity.

**D21 — Fixture traceability is positional and partly wrong.** The `invariants` array has no `id` fields, so `I01`–`I16` are inferred from order and any insertion silently renumbers every fixture. Profile constraints have no ids at all, so `profile-mints-ledger-account` and `cascade-delete` — both profile rules — are mapped to I01/I02 and I16, which do not state them.
*Remediation:* convert `invariants` to objects with stable `id`, never renumbered; assign ids to profile constraints; re-point those two fixtures at the profile ids.

## Additional fixtures required

Exactly these, in addition to the existing seventeen:

1. `ledger-adoption-exclusivity` — negative. One ledger holds effective adoptions of two different charts over overlapping intervals. Rejected; at most one adoption is effective per ledger at any instant.
2. `adoption-revocation-retroactive` — negative. An adoption is revoked with effect before an already-posted entry. Rejected; revocation is effective-dated closure only.
3. `policy-pinning-conflict` — negative. `LedgerAccount.policyRevisionRef` names a different lineage than the ledger's effective adoption. Rejected; the account-level pin must narrow within the adopted lineage.
4. `ledger-account-identity-continuity` — positive. A node is unchanged across a successor chart revision. One stable Ledger Account identity persists; its balance series is continuous across the revision boundary; `predecessorRef` resolves.
5. `overlapping-account-intervals` — negative. Two effective Ledger Accounts exist for the same `(ledgerRef, nodeId)` at one instant. Rejected.
6. `duplicate-account-code-in-ledger` — negative. Two Ledger Accounts share `accountCode` effective simultaneously in one ledger. Rejected.
7. `second-concurrent-backing` — negative. A Ledger Account declares a second WM-ECO-015 backing for the same context and interval. Rejected; at most one per declared context.
8. `suspended-policy-posting` — negative, with positive tail. A posting is made against a suspended policy revision; and an entry pinned before suspension is re-read. New posting rejected; the pre-suspension pinned entry remains valid and unchanged.
9. `retire-adopted-chart` — negative. A chart is retired while a ledger adoption remains effective. Rejected; requires no effective adoption or an effective-dated successor adoption.
10. `tolerance-residual-unposted` — negative. An entry is accepted with a within-tolerance residual that is not posted. Rejected; residual posts to the designated same-ledger residual account and postings sum to exactly zero.
11. `balancing-scope-undeclared` — negative. Balancing is evaluated on a scope dimension not declared in the pinned policy revision. Rejected.
12. `fx-rate-restatement` — negative. A WM-XCT-014 rate revision changes and prior translated postings are recomputed in place. Rejected; posted amounts are immutable; a linked same-ledger correction is required.
13. `balance-currency-role-missing` — negative. A 017 assertion is keyed by currency without a currency role. Rejected; role is part of the qualification key.
14. `open-period-balance-overwrite` — negative. An open-period balance assertion is overwritten in place on recomputation. Rejected; a successor assertion with its own as-of and basis is emitted.
15. `late-entry-into-closed-period` — paired. (a) negative: an entry with an accounting date inside a hard-closed period is recorded without an authorised exception; rejected. (b) positive: the same entry under an explicit exception with `authorityRef` is appended, linked, and leaves the original entry and closed balance immutable.
16. `hard-close-exception-amends-original` — negative. An authorised exception is used to amend the original closed-period entry. Rejected; the exception authorises appending only.
17. `sibling-divergence-unstated` — negative. Siblings differ in recognition date and account with no divergence reason recorded. Rejected; a reason from the closed vocabulary, pinning both policy revisions, is required.
18. `multi-entry-single-event` — positive. One external event correlates to two entries inside the same ledger and one in another. Grouping is `(eventRef, ledgerRef)`; each entry balances alone; divergence is recorded at set level.
19. `close-state-single-source` — negative. Close state is asserted by an object other than the owning `LedgerPeriod`. Rejected; close state is read only from the period master.
20. `binding-supersession` — positive, profile-scoped. A correspondence binding is superseded. The prior binding is retained and resolvable, the local binding key is not a subject identity, and no upstream master is mutated.

Every new and re-pointed fixture must cite stable invariant or profile-constraint ids per D21; fixtures remain non-executable while the registry allocation and base contradictions stand.