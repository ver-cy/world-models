# Frozen semantic audit prompt — EM-FIN-04

You are the sole frozen semantic auditor for this contour. This audit runs exactly once. Use only supplied text. Do not browse, call tools, invent identifiers, claim standards conformance or propose publication of blockers.

Audit the reconciled EM-FIN-04 boundary and allocation/profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence/rights semantics, non-deterministic fixtures and missing publishability holds. Preserve the intended decision unless the supplied evidence disproves it: profile WM-ECO-018 for consolidated statements; keep Consolidation Scope and Consolidation Run as independent identifier-unassigned candidates; profile Elimination Entry on WM-ECO-016 within one consolidation book and run; keep source ledgers, organizations, control, holdings and policy externally mastered; allocate no catalogue, model or runtime ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect exact deterministic remediation; Exact additional fixtures as a JSON array; final freeze decision. Be sceptical and concise. Never request another provider run.
## local-evidence.md

`	ext
# EM-FIN-04 local synthesis

## Disposition

- Reuse WM-ECO-018 as Financial Statement under a consolidated-statement profile.
- Propose identifier-unassigned **Consolidation Scope** and **Consolidation Run** roots because both have lifecycles independent of a statement issue.
- Profile Elimination Entry on WM-ECO-016 and constrain it to a consolidation book and one run, with mandatory pair and residual evidence.
- Reuse accounts, journals, positions, organizations, control relationships, holdings and policy/rule masters.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Consolidation Scope persists across periods, runs, statements, management reports and disclosures. Its lifecycle follows control and perimeter changes. Consolidation Run is an immutable execution that pins scope, method, ledgers, mappings, rates and cutoff and remains reproducible after the statement that cites it changes.

WM-ECO-018 already owns report and issue identity. Elimination Entry remains a balanced WM-ECO-016 posting document with additional consolidation constraints. Source ledgers, accounts, positions, organizations, holdings and control assertions retain their own mastership.

## Statement, scope and run

Statement issue, perimeter, transformation, run, elimination and source ledger are distinct. WM-ECO-018 binds and presents consolidation outputs but does not execute consolidation or own its transformations.

The existing WM-ECO-018 service role claiming ownership of perimeter, eliminations and transformations conflicts with its out-of-scope declaration and must be narrowed to binding and citation.

## Perimeter and control

Every scope version is purpose-qualified: statutory reporting, management, ownership/control and statistical perimeters may differ and are never silently shared.

Membership declares consolidation approach, control basis, governing instrument, evidence, claimant capacity, valid time and knowledge time. Economic ownership, voting power, control and consolidation treatment remain separate assertions. Common owners alone create no membership because they establish neither control basis nor reporting authority.

Management perimeter may follow operational responsibility while statutory perimeter follows an accounting control test. One entity may validly appear in only one of them.

## Source ledgers and transformation

Source postings remain immutable in their own books. Each run enumerates contributing books and revisions, pinned trial-balance or position sets, group-account mapping, currency translation, reclassification and alignment rules.

Transformation steps record inputs, outputs and rule versions. Consolidation adjustments live only in consolidation books and never rewrite source entries.

## Elimination entry

An Elimination Entry balances within one consolidation book, currency and tolerance. It records class, both counterparty legs, book/entry/line references, matching key, matched and unmatched amounts, residual reason and authorization.

An unmatched leg becomes a visible break and never a silent one-sided posting. Intercompany revenue/cost, receivable/payable, investment/equity, unrealized profit and dividend eliminations remain distinguished.

## Currency, time and knowledge

Transaction, functional and presentation currencies remain explicit. Rate, rate type, rate date, source and rate-set version are pinned.

Reporting period, cutoff, posting, event, run, issue, filing, ingestion and knowledge times remain distinct. Reproduction at prior knowledge time resolves the run, scope, rates, mappings and ledger revisions valid at that knowledge cut rather than current configuration.

## Restatement and publication

Completed runs and issued statements are immutable. Corrections create successor runs and successor statement versions with restatement class, reason and lineage. Original and recalculated editions remain resolvable.

Approval, assurance, issue, filing and publication are independent states. None validates a figure by itself, and publication never erases a prior or recalculated edition.

## Governance and assurance

Run execution, elimination posting, scope change, post-cutoff adjustment, issue and restatement require authority. Initiator and authorizer are separated or a compensating control is recorded.

Assurance engagements remain external and pin exact run and statement versions. Method, accounting framework, taxonomy, disclosure and recalculation policies are pinned WM-KNW-012 revisions.

## Acceptance result

Group P consolidates subsidiary S from statutory EUR book L-STAT and management USD book L-MGMT. Run R1 pins scope v2, rate set FX-2026Q2, mapping M1 and cutoff T1. Elimination E1 removes a 100,000 intercompany sale and 70,000 cost, cites both legs and matching key IC-8841, and explains a 120 FX residual. Statement A1 cites R1. Scope v3 later removes a disposed subsidiary; R2 and a recalculated comparative retain a bridge for scope, method, rate and activity changes. A late adjustment enters R2 and never backdates R1. A1 remains reproducible at its original knowledge time.

## Required invariants

1. Statement, scope, run, elimination, posting and position have distinct identifiers.
2. Every statement pins scope, method/framework, taxonomy, rate set, run and ledger revisions.
3. Inclusion requires control basis, authority, evidence and interval.
4. Common ownership alone never establishes inclusion.
5. Management and statutory perimeters remain parallel and non-substitutable.
6. Eliminations post only to consolidation books.
7. Every elimination cites paired evidence and explains residuals.
8. Entries balance within one book, currency, scope and tolerance.
9. Ownership assertions state right type, class, denominator and time.
10. Event, cutoff, run, issue and knowledge times remain distinct.
11. Runs are immutable and corrected by successors.
12. Restatements append versions and preserve originals.
13. Post-cutoff adjustments are dated and authorized.
14. Scope changes produce comparability bridges.

## Holds

Consolidation Scope and Consolidation Run have no registry allocations. Chart of Accounts/Mapping, FX Rate Set, Intercompany Match and Trial Balance also lack allocated masters. WM-ECO-018 contradicts its own out-of-scope boundary, and WM-ECO-018/017 composition direction conflicts with the referenced-master boundary. WM-ORG-012 parentage and WM-ECO-038 extension semantics remain unsettled. Relations, source pins and fixtures are absent or unapproved, and bases remain non-canonical drafts. No installability or publication-readiness claim is made.

`

## claude-study.raw.md

`	ext
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

`

## grok-study.raw.md

`	ext
Verdict: Conditional accept of the allocation, not publication-ready. Independent roots are required only for Consolidation Scope and Consolidation Run, both identifier-unassigned. Consolidated Financial Statement is a profile of WM-ECO-018. Elimination Entry is a constrained profile of WM-ECO-016, not a new root. Source ledgers, organizations, control, holdings and accounting policy stay externally mastered. No other identifier is allocated.

Strongest evidence: The proposal separates the issued statement from the scope decision, the run, and the adjustments, and it refuses to derive membership from holdings. That is what lets two source ledgers, a later scope change, and an intercompany elimination coexist without a second chart, a second organization master, or a rewrite of the original knowledge-time result.

Strongest counterexample: An unrealized intercompany inventory profit on a sale between two ledgers, followed by a mid-period method change from full to equity, then a later restatement of control evidence. If scope is a statement attribute, or the run is not version-pinned, the post-change portion cannot be isolated and the original issue cannot be reproduced. A 60% holding with protective rights only, or de facto control below 50%, is wrongly included if membership is inferred from common owners.

Identity and mastership: Candidates that need independent roots are Consolidation Scope and Consolidation Run only. Financial Statement does not: the issued report is a specialization of the WM-ECO-018 statement master and must reference scope and run rather than absorb them. Elimination Entry does not: it is an adjustment class on WM-ECO-016, bound to one consolidation book and one run. External masters remain the source of ledger identity, organization identity, control assessments, equity holdings and policy. The consolidation model stores versioned references, not copies.

Statement, scope and run: The statement is the publication artifact. Scope is the governed membership and method decision. Run is the execution binding that consumes one scope version and emits one reproducible result. A statement may cite both; it is not their container. A scope change is a new scope version, not an edit of a statement.

Perimeter and control: Statutory and management perimeters are separate scope instances even when membership overlaps. Legal or accounting control is evidenced and dated; common ownership and equity percentage are inputs to that evidence, never inclusion rules. Automatic inclusion from common owners is rejected.

Ledgers and transformation: Source postings remain in their source ledgers. Consolidation transformations — mapping, currency translation, method application, cutoff — are run-scoped and pinned. They do not rewrite source journals. Each run names the source books, periods and cutoffs it consumed.

Elimination: An elimination is a consolidation adjustment, not a source posting. It exists only inside one consolidation book and one run, and it carries pair identity, match status, cutoff and authorization. Unmatched intercompany amounts are not silently cleared. The profile is acceptable only if WM-ECO-016 can carry a run-scoped adjustment discriminator without sharing source-journal identity. If it cannot, the profile fails; a further identifier is still not allocated.

Currency, time and knowledge: Event time of the sale is distinct from knowledge time of the elimination and of the statement issue. The run pins currency, rate version, policy, mapping, framework and taxonomy versions. A result at knowledge time T is recoverable only from pins known at T.

Restatement and publication: Original issue and restatement are distinct. Restatement is a new run, and if re-issued a new statement issue, that references the original run and does not overwrite it. Publication does not change ledger facts, scope history or elimination identity.

Governance and assurance: Scope membership, method, control evidence, cutoff and run authorization are explicit governed facts. Holdings, policy and organizations are cited, not re-decided inside the consolidation model. Assurance relies on immutability at knowledge time and on pair evidence, not on recomputation against later masters.

Scenario: Ledger A sells inventory to Ledger B. At knowledge time T1, statutory scope S1 includes both under full consolidation; run R1 pins books, period, rates, policy, mapping, control evidence and cutoff, and posts one elimination of the unrealized margin with pair evidence. At T2 a scope change moves B to equity from a mid-period effective date; run R2 pins S2 and eliminates only the post-change portion. At T3 control evidence is restated; run R3 references R1 and R2 and does not replace them. A common owner of an out-of-scope entity C creates no membership.

Invariants:
1. No entity enters a perimeter solely because a common owner or equity holding exists.
2. Inclusion requires explicit membership, perimeter type, method and control evidence valid at the run’s knowledge time.
3. Statutory and management perimeters are distinct scopes even if membership overlaps.
4. A run binds exactly one scope version.
5. A run pins source books, periods, cutoffs, mapping, policy, framework, taxonomy, currency and rate versions, transformations and authorization.
6. A run is immutable at its knowledge time; later change creates a new run.
7. Source postings are never mutated by consolidation.
8. Eliminations exist only in one consolidation book and one run.
9. Elimination requires pair and match evidence; unmatched amounts are not auto-cleared.
10. Event time, knowledge time and publication time are distinct.
11. Original issue and restatement are distinct; restatement references and does not overwrite.
12. Statement identity does not contain scope, run, transformation or ledger facts.
13. Holdings, organizations, control and policy remain externally mastered.
14. The statement known at T is reproducible from pins known at T.

Minimum model set: WM-ECO-018 profile for the consolidated statement issue; identifier-unassigned Consolidation Scope root; identifier-unassigned Consolidation Run root; WM-ECO-016 constrained profile for Elimination Entry; versioned external references for ledgers, organizations, control evidence, holdings, policy, mapping, framework, taxonomy, currency and rates.

Blockers: The elimination profile has no demonstrated adjustment discriminator, so source and consolidation identity may collapse. Scope does not yet pin control-evidence version, perimeter type and effective date as consumable facts. External references must be version-addressable or the run cannot reproduce. Restatement as a new run that cites the original, without a new identifier, is unspecified. Management and statutory perimeters must not share one membership list. Until those pins exist, the two-ledger, scope-change and intercompany-sale test cannot be assured.

`

## candidate-allocation-offline-consolidation-scope/allocation-candidate.json

`	ext
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FIN-04","proposedName":"Consolidation Scope","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"A governed consolidation scope persists across reporting periods, runs, statements and management views.","versionIdentity":"Perimeter, purpose, control basis, consolidation approach or governing authority changes create immutable effective-dated revisions.","independentLifecycle":["draft","approved","effective","superseded","retired"],"mastership":"group finance consolidation-governance authority"},
"boundary":{"owns":["stable scope identity","purpose-qualified perimeter","membership and consolidation treatment","control basis, authority and evidence","effective periods and comparability lineage"],"references":[{"target":"WM-ORG-001","purpose":"Included organization identity"},{"target":"WM-ORG-012","purpose":"Enterprise group context"},{"target":"WM-ECO-038","purpose":"Ownership and control assertions"},{"target":"WM-KNW-012","purpose":"Pinned accounting and consolidation policy"},{"target":"WM-ECO-018","purpose":"Statements citing a scope revision"}],"excludes":["statement issue identity","consolidation execution","journal entry and elimination posting","source ledger and account identity","position and holding identity"]},
"objects":{"ConsolidationScope":{"identity":["consolidationScopeId"],"required":["name","purpose","ownerRef","status","currentRevisionRef"],"optional":["successorRef"],"lifecycle":["draft","approved","effective","superseded","retired"]},"ScopeRevision":{"identity":["consolidationScopeId","revision"],"required":["membership","consolidationApproach","controlBasis","authorityRef","evidenceRefs","effectiveFrom","contentDigest"],"optional":["effectiveTo","supersedesRevision","comparabilityBridgeRef"]}},
"invariants":["Statement, scope, run, elimination, posting and position have distinct identities.","Every membership states purpose, consolidation approach, control basis, authority, evidence and interval.","Common ownership alone never establishes membership.","Economic ownership, voting power, control and consolidation treatment remain separate assertions.","Management and statutory perimeters remain parallel and non-substitutable.","Every run pins one immutable scope revision.","Scope changes never rewrite source ledger facts.","Structural changes create successor revisions and comparability bridges.","Valid time and knowledge time remain distinct.","Original and recalculated perimeters remain resolvable.","A statement cites but never owns scope history.","Access and confidentiality inherit from referenced masters.","Retired identifiers and revisions remain resolvable.","Scope identifiers are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","WM-ECO-018 boundary contradiction and relation direction require reconciliation.","Frozen audit, policy pins and fixtures remain pending."]}

`

## candidate-allocation-offline-consolidation-scope/fixtures.json

`	ext
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Consolidation Scope","cases":[{"id":"parallel-perimeters","kind":"positive","input":"An entity is in the management perimeter but outside the statutory perimeter.","expect":"Separate purpose-qualified scope revisions preserve both valid treatments."},{"id":"disposed-subsidiary","kind":"positive","input":"A disposed subsidiary leaves the scope next period.","expect":"A successor scope revision and comparability bridge preserve the prior perimeter."},{"id":"control-evidence","kind":"positive","input":"A subsidiary is included based on an effective control instrument.","expect":"Membership records control basis, evidence, authority and interval."},{"id":"common-owner-only","kind":"negative","input":"Two entities are consolidated solely because they share an owner.","expect":"Inclusion is rejected without control basis and reporting authority."},{"id":"silent-purpose-reuse","kind":"negative","input":"A management perimeter is silently used for statutory reporting.","expect":"The substitution is rejected."},{"id":"overwrite-scope","kind":"negative","input":"A disposal edits the prior scope revision in place.","expect":"The mutation is rejected; a successor revision is required."},{"id":"scope-owns-ledger","kind":"negative","input":"Scope membership replaces source ledger and organization identities.","expect":"The identity merge is rejected."}]}

`

## candidate-allocation-offline-consolidation-scope/profile-candidate.json

`	ext
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-FIN-04","name":"Enterprise Consolidated Financial Statement and Elimination Binding","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ECO-018","WM-ECO-015","WM-ECO-016","WM-ECO-017","WM-ORG-001","WM-ORG-012","WM-ECO-038","WM-KNW-012"],"constraints":["WM-ECO-018 owns report and issue identity and cites consolidation outputs without executing consolidation.","WM-ECO-016 owns balanced journal entries; elimination entries are constrained to one consolidation book and run.","Source ledgers, accounts, positions, organizations, holdings and control assertions retain their mastership.","Every elimination cites both counterparty legs, matching key, matched and unmatched amounts, residual reason and authorization.","Consolidation adjustments never rewrite source entries.","Approval, assurance, issue, filing and publication remain independent states."],"holds":["Consolidation Scope and Run remain unassigned.","WM-ECO-018 boundary and composition direction require correction.","Independent Grok review and frozen audit remain pending."]}

`

## candidate-allocation-offline-consolidation-run/allocation-candidate.json

`	ext
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-FIN-04","proposedName":"Consolidation Run","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"Each consolidation execution remains identifiable independently of the statement that cites it.","versionIdentity":"Changed scope, ledgers, mappings, rates, cutoff or corrections create successor runs rather than mutating a completed run.","independentLifecycle":["planned","running","completed","failed","superseded","retired"],"mastership":"group finance consolidation execution authority"},
"boundary":{"owns":["immutable run identity","pinned scope, framework, ledgers, mappings, rates and cutoff","ordered transformation and reconciliation evidence","contained run outputs and comparability bridge","successor-run lineage"],"references":[{"target":"WM-ECO-018","purpose":"Statements citing selected run outputs"},{"target":"WM-ECO-016","purpose":"Source and consolidation-book journal entries"},{"target":"WM-ECO-017","purpose":"Pinned positions and trial-balance sets"},{"target":"WM-ECO-015","purpose":"Ledger and account identity"},{"target":"WM-KNW-012","purpose":"Accounting, mapping and transformation policy revisions"}],"excludes":["statement issue lifecycle","scope identity","source posting identity","account and position identity","assurance engagement"]},
"objects":{"ConsolidationRun":{"identity":["consolidationRunId"],"required":["scopeRevisionRef","frameworkRef","sourceBookRefs","sourceRevisionRefs","mappingRefs","rateSetRef","cutoff","executedAt","status"],"optional":["successorRunRef","executorRef"],"lifecycle":["planned","running","completed","failed","superseded","retired"]},"TransformationStep":{"identity":["consolidationRunId","stepId"],"required":["ruleRevisionRef","inputRefs","outputRefs","sequence"],"optional":["authorizationRef","residualExplanation"]}},
"invariants":["Every run pins scope, framework, taxonomy, rates, mappings, cutoff and source revisions.","Source postings remain immutable in their books.","Transformations record input, output and rule versions.","Adjustments post only to consolidation books.","Every elimination cites paired evidence and explains residuals.","Entries balance within one book, currency, scope and tolerance.","Unmatched legs remain visible breaks.","Transaction, functional and presentation currencies remain explicit.","Rate value, type, date, source and set version are pinned.","Event, cutoff, run, issue and knowledge times remain distinct.","Completed runs are immutable and corrected by successors.","Restatements preserve original runs and statement editions.","Post-cutoff adjustments are dated and authorized.","Run identifiers and contained steps are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","Scope, chart/mapping, FX rate-set, match and trial-balance masters remain unallocated.","Frozen audit, relation approvals and fixtures remain pending."]}

`

## candidate-allocation-offline-consolidation-run/fixtures.json

`	ext
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Consolidation Run","cases":[{"id":"two-ledger-run","kind":"positive","input":"A run pins statutory EUR and management USD books, mapping M1, rate set FX1 and cutoff T1.","expect":"Each source revision remains immutable and the run records transformations into the consolidation book."},{"id":"paired-elimination","kind":"positive","input":"An intercompany sale and cost are eliminated with a documented FX residual.","expect":"The balanced elimination cites both legs, match key and residual explanation."},{"id":"late-adjustment","kind":"positive","input":"A late adjustment is discovered after statement A1.","expect":"A successor run and statement version preserve A1 and prior knowledge-time reproduction."},{"id":"source-rewrite","kind":"negative","input":"A consolidation adjustment edits a source-ledger posting.","expect":"The mutation is rejected."},{"id":"one-sided-elimination","kind":"negative","input":"An unmatched receivable is silently eliminated on one side.","expect":"The entry is rejected and exposed as a break."},{"id":"current-rate-replay","kind":"negative","input":"A historical run is reproduced using today's FX rate set.","expect":"The reproduction is rejected because the pinned historical rate set is required."},{"id":"overwrite-run","kind":"negative","input":"A correction rewrites a completed run.","expect":"The mutation is rejected; a successor run is required."}]}

`

