# Verdict

Reuse **WM-ECO-018** for `FinancialStatement` as a constrained consolidated-statement profile: no new root. Raise **`ConsolidationScope`** and **`ConsolidationRun`** as identifier-unassigned new roots — both have identity and lifecycle independent of any statement. Treat **`EliminationEntry`** as a profile of **WM-ECO-016** constrained to a consolidation book and contained in a run: no new root, but a mandatory pair-evidence extension. No identifiers allocated; no catalogue or runtime entry created.

# Evidence

The dossier supplies WM-ECO-018 (statement, `aggregate`), WM-ECO-015 (account/ledger), WM-ECO-016 (journal entry/posting, dual-provider), WM-ECO-017 (position/balance), WM-ORG-001 (organization), WM-ORG-012 (inter-organizational relationship), WM-ECO-038 (equity holding), WM-KNW-012 (policy/rule). All are `published` with `publishableCanonical: false` and `reviewable-draft`; four carry single-provider waivers. Prior boundary work is directly reusable: EM-FIN-02 fixes ledger/entry/posting mastership and the no-cross-ledger-balancing rule; EM-ORG-01 and EM-ORG-03 fix perimeter-as-membership and the separation of economic, voting, control and consolidation assertions; EM-FAC-02 establishes the boundary-version / registry / immutable-run trio this contour needs; EM-DAT-06 supplies the report-definition versus report-issue split.

# Identity/mastership

`ConsolidationScope` needs independent identity: one perimeter version serves many periods, runs, statements, management reports and disclosures, and its lifecycle follows control changes and recalculation policy, not a statement issue cycle. `ConsolidationRun` needs independent identity: it is an immutable execution pinning scope version, method edition, ledger revisions, mappings, rates and cutoff, and it survives the statement that cites it. `FinancialStatement` does not need a new root — WM-ECO-018 already owns report identity, versions, facts and issue lifecycle. `EliminationEntry` does not need a new root: it is a balanced posting document, which WM-ECO-016 already masters as an aggregate with header, lines and a balancing invariant; only its book, pairing and provenance constraints are new. Source ledgers, accounts, positions, entities, control relations, holdings and policy versions stay externally mastered.

# Statement/scope/run

Report issue ≠ execution ≠ perimeter ≠ transformation ≠ elimination ≠ source ledger. WM-ECO-018 binds and cites; it does not execute. WM-ECO-018's own `out_of_scope` excludes owning a Consolidation Run, yet its `serviceLayers.roles` assigns a "Consolidation and data steward" ownership of "entity perimeter, ledger and position bindings, eliminations, transformations, lineage." **That is a contradiction** and must be corrected to binding-and-citation language before publication. Its `scope_statement` phrase "consolidation and elimination bindings" is acceptable only as reference.

# Perimeter/control

Scope versions are purpose-qualified per EM-ORG-01: statutory-reporting, management, ownership/control and statistical perimeters coexist as parallel scoped graphs and are never implicitly shared. Each member assertion records consolidation approach (control, joint control, significant influence, equity share), control basis, governing instrument, evidence, claimant capacity, valid time and knowledge time, resolved against WM-ORG-012 with WM-ORG-001 endpoints. Ownership percentages come from WM-ECO-038 holdings plus EM-ORG-03's class/denominator/right-type discipline; economic share, voting power, control and consolidation remain non-substitutable. **The negative case is rejected structurally:** common owners produce no membership, because no basis, instrument or evidence is present; shared ownership is a sibling relation, not a control edge. Management and statutory perimeters differ legitimately when management follows operating responsibility or segment stewardship while the statutory perimeter follows the control test — the same entity may sit in one and not the other, with no reconciliation implied.

# Source ledgers/transformation

Source postings stay immutable in their own books (EM-FIN-02). A run enumerates each contributing ledger/book by identifier and revision, pins its trial balance or position set at cutoff, and records the chart-to-group-account mapping version, currency translation rule, reclassification rule and alignment adjustments as transformation steps with declared inputs and outputs. Ledger facts and consolidation adjustments never share a field: adjustments live only in consolidation books. Each ledger corrects independently; no adjustment rewrites a source entry.

# Elimination entry

An elimination is a WM-ECO-016 entry in a consolidation book, contained in one run, balancing within that book, currency and declared tolerance. It additionally requires: elimination class (intercompany revenue/cost, receivable/payable, investment/equity, unrealised profit, dividend), both counterparty legs with their book, entry and line references, the intercompany matching key, matched and unmatched amounts, residual difference with reason (timing, FX, in-transit, cutoff), and authorisation. An unmatched leg yields a recorded break, never a silent one-sided posting. WM-ECO-016 already declares this as an omission ("intercompany elimination and multi-entity matching postings … not modelled as their own structure") and defers the top-side hand-off, so this profile closes a self-declared gap rather than inventing one.

# Currency/time/knowledge

Transaction, functional and presentation currency roles stay explicit with rate, rate type, rate date, source and rate-set version. Reporting period, instant/duration, cutoff, posting date, run time, statement issue time, filing time, observation, ingestion and knowledge time remain distinct RFC 3339 instants with explicit offsets. Reproducing a report at a prior knowledge time resolves the run whose knowledge cut matches, with its pinned scope version, rate set and ledger revisions — not current configuration.

# Restatement/publication

Issued statement versions and completed runs are immutable. Corrections create successor runs and successor statement versions with restatement class and reason; predecessors remain resolvable. Publication, filing acceptance, approval and assurance are separate states and none of them validates a figure. A published edition never erases a recalculated edition, and a recalculated edition never overwrites the original.

# Governance/assurance

Authorisation is required for run execution, elimination posting, post-cutoff adjustment, scope change, issue and restatement; initiator and authoriser are separated or a compensating control is recorded. Assurance engagements pin specific run and statement versions and remain external. Method, framework, taxonomy, disclosure and recalculation policies are pinned WM-KNW-012 versions.

# Acceptance scenario

Group P consolidates S. Books L-STAT (statutory, EUR) and L-MGMT (management, USD) each hold S's sale to P of 100,000 with cost 70,000, recognised on different rules. Run R1 pins scope v2 (control basis, evidence), rate set FX-2026Q2, mappings M1 and cutoff T1; elimination E1 removes intercompany revenue and cost with both legs cited, matching key IC-8841, and a 120 FX residual explained. Statement issue A1 cites R1. Scope v3 removes a disposed subsidiary; R2 and a recalculated comparative are produced, with a bridge decomposing scope, method, rate and activity differences and a non-comparability marker. A late adjustment after T1 is recorded as a dated post-cutoff adjustment in R2, not backdated into R1. A1 remains fully reproducible at its own knowledge time.

# Invariants

1. Statement, scope version, run, elimination entry, source posting, position and filing hold disjoint identifiers. 2. Every issued statement pins one scope version, one method/framework/taxonomy edition, one rate set, one run and enumerated ledger revisions. 3. Inclusion requires recorded control basis, authority, evidence and interval; common ownership alone never suffices. 4. Management and statutory perimeters are parallel and non-substitutable. 5. Eliminations post only to consolidation books; source ledgers stay immutable. 6. Every elimination carries matched pair evidence with residual and reason. 7. Each entry balances within one book, currency, scope and tolerance; no cross-book netting. 8. Percentage assertions declare right type, class scope, denominator, valid and knowledge time and rule version. 9. Event, cutoff, as-of, run, issue and knowledge times are never collapsed. 10. Runs are immutable; correction appends a successor. 11. Restatement appends a version; publication erases neither edition. 12. Post-cutoff adjustments are dated and authorised, never backdated. 13. Scope change forces a successor version plus a comparability bridge; results across scope versions are not additive. 14. Derived figures are labelled and reproducible from pinned inputs.

# Minimal model set

WM-ECO-018 (consolidated statement profile), WM-ECO-016 (source postings and elimination profile), WM-ECO-015 (ledger/account), WM-ECO-017 (positions, trial balance), WM-ORG-001, WM-ORG-012 (control relations), WM-ECO-038 (holdings), WM-KNW-012 (policy/method/framework versions), plus identifier-unassigned candidates: ConsolidationScope, ConsolidationRun, Chart-of-Accounts/Mapping, FX Rate Set, Intercompany Match, Trial Balance.

# Holds

All bases are non-canonical reviewable drafts; WM-ECO-018, WM-ECO-017, WM-ECO-038 and WM-ORG-012 had both external providers time out. Contradictions: WM-ECO-018's consolidation-steward role versus its own out-of-scope; WM-ECO-018 COMPOSE WM-ECO-017 versus WM-ECO-017's REFERENCE to WM-ECO-018; WM-ORG-012's registry `parent_ids: WM-ORG-001` versus its reference boundary; WM-ECO-038 EXTEND against a category marked for split; WM-ECO-018 marking every checklist dimension covered while admitting no external review. Gaps: no allocated home for chart of accounts/accounting policy, consolidation method set, FX rate set, intercompany matching, trial balance, or assurance-engagement identity; WM-REC-002 parent unfrozen. Relations, immutable source pins and fixtures are absent. No claim of canonical completeness, installability or publication readiness.
