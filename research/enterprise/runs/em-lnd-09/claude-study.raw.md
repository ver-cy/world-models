# Verdict

EM-LND-09 is a **governed profile**, not a new identity. Define **ContractLandscape** as a read-only projection over WM-ECO-006 agreement records and WM-XCT-029 obligation records; define **ObligationNetwork** as its dependency/deadline view — the same profile rendered as a directed graph rather than a flat register. Neither candidate has independent business identity: every contract fact is mastered by WM-ECO-006, every duty fact by WM-XCT-029, and the landscape adds only perimeter, as-of parameters and graph derivation. Allocate no new runtime or model identifier. Served output is an immutable digest-identified projection.

# Evidence

Both dossier parents are `status: published` with `adjudicationStatus: reviewable-draft` and `publishableCanonical: false`, and the contour records `mapping_status: conceptual-candidate` with `evidence_depth: index-and-publication-metadata` for each. The registry marks WM-XCT-029 `candidate` / `boundary-review-required` and WM-ECO-006 `described-previous-version` / `migration-boundary-review`. `related_research_contours` is empty; the frozen relations list contains no edge between WM-ECO-006 and WM-XCT-029, so the composition relied on below is read from each spec's own `composition` array, not from a ratified ledger. That is sufficient for a boundary decision and insufficient for a crosswalk claim.

# Identity/mastership

WM-ECO-006 masters the agreement instrument: agreement identity and instance boundary, party positions, formation and execution, the clause tree with work and expression identifiers, constituent-document precedence, amendment, assignment, notice, termination and survival, and record governance. Its identity priority puts the jointly designated register number first, then a governed IRI, then a Dimension-minted UUID/ULID; a date is never an identifier.

WM-XCT-029 masters each duty: modality and violability, obligor/obligee/beneficiary, obligated action, antecedent and detachment, due basis, recurrence, lifecycle state, fulfilment and evidence, non-performance, excuse, cure and consequence obligations. Occurrence identity is composite — standing obligation identifier plus occurrence key from the recorded recurrence rule version.

The contract derives obligations from stable clause **work** identifiers and never writes obligation state. The obligation cites its source clause and never becomes a second store for normative clause text. WM-ECO-006's `derive-obligation-set` marks derived rules as derived; its `apply-amendment` invalidates and re-derives affected rules.

# Scope

In scope for the profile: perimeter of agreements (party positions, subject-matter class, governing-law declaration), the obligation set derived from those agreements, dependency and precedence edges, deadline derivation inputs, evidence-of-fulfilment pointers, dispute and non-performance markers, and the as-of/knowledge-time parameters. Out of scope: clause authoring, signature validation, adjudication proceedings (WM-ECO-006 boundary note to world.disputeResolution), risk treatment, accounting recognition, and any legal interpretation of which term prevails.

# Parties and versions

Party identity resolves to WM-ORG-001 (or the person model); WM-ECO-006 stores only the party **position**, its role, the governed identifier link and verification evidence with observation time. WM-ORG-001's registry flag "контракт не «организация»" is upheld — the landscape never treats an agreement as an organization.

Parties are historic in three distinct senses, and the profile must keep them apart: (a) the party position pinned at execution, with its identity verification evidence and observation time; (b) organizational lifecycle of the occupying entity, mastered by WM-ORG-001 (name change, merger, succession, dissolution) — WM-ORG-001 warns that a lapsed identifier is not cessation; (c) contractual-plane change of who occupies the position, via WM-ECO-006 `assign-or-novate`, which changes party positions "on the contractual plane only" and does not move in rem title. A later organizational change never overwrites the pinned execution-time position.

Contract-version identity is FRBR-style: the work identifier persists; each amendment produces a new expression under `apply-amendment`, retaining and keeping addressable the superseded expression. WM-ECO-006 records the expression-versus-work conflict explicitly — consumers keying on expression identifiers break across renumbering, so both must be stored. Obligation identity is separately versioned: WM-XCT-029 versions by supersession when modality, obligor, action, due basis or governing law changes, and patches in place otherwise; a release-and-substitute novation creates a successor obligation, while delegation of performance preserves identity.

# Obligation dependencies

Three dependency kinds, all mastered by WM-XCT-029's `finding-composition-and-dependency`:

1. **Antecedent condition** — the duty exists but detaches only when its constraint set is satisfied; detachment is an evidenced, timestamped event.
2. **Order of performance / reciprocal dependency** — each party's duty conditional on the counterparty's. WM-XCT-029 names withholding of performance in reciprocal obligations as deferred research (UNIDROIT 7.1.3), so the profile can represent the dependency but cannot assert the withholding state.
3. **Parent/child decomposition** — a parent discharged only when children are discharged, distinct from mere reporting grouping.

Dependency on another party's performance is therefore a typed edge with a named counterparty duty, not an inference from a missed date. WM-XCT-029 requires cycle detection on dependencies as a declared validation dimension, and adversarially notes that reciprocal dependency "is a common source of deadlock."

# Survival and deadlines

Contract term and obligation term are separate clocks. WM-ECO-006's `termination-expiry-and-survival` holds which provisions survive and what wind-down remains; `avoid-or-terminate` releases open primary obligations subject to damages and restitution while preserving dispute and winding-up clauses. WM-XCT-029's `limitation-and-survival` makes survival after termination of the instrument a question distinct from limitation, and models an obligation that is substantively owed yet time-barred — a state a simple open/closed model cannot express.

Deadlines: WM-XCT-029's `due-time-and-window` distinguishes fixed time, obligor-chosen period, reasonable time and event-derived deadlines as a first-class field, not implied by presence or absence of a date. `compute-due-schedule` derives nominal and adjusted instants from due basis, recurrence rule, time zone, business-day convention and trigger-event instants, via WM-XCT-009 for calendar and business-day arithmetic. Conditional deadlines run from the detachment or trigger instant, and the recorded inputs must make the computation reproducible. WM-XCT-009 warns that converting a legally stated local civil time to a UTC instant at capture destroys legally relevant information, so both representations are retained.

Evidence of fulfilment: WM-XCT-029 `record-fulfilment-evidence` binds evidence to the specific occurrence and quantity it discharges, with issuer, validity interval, integrity proof and revocation status. Fulfilment is never asserted on elapsed time alone; evidence revocation appends a reopening transition and never edits a prior acceptance. WM-ECO-006 holds the counterparty acceptance decision separately, applying deemed acceptance only where an agreed rule exists.

# Dispute/non-performance

Four states stay visibly distinct. **Overdue** is a computed state from due schedule plus grace expiry with no discharge. **Declared non-performance** requires WM-XCT-029 `declare-non-performance` — grace expired, no accepted excuse, declaring party authorised — and covers defect and lateness, not only a missed date. **Excused** is a coded ground (impediment, hardship, interference), never inferred from silence. **Disputed** is a separate contestation status on the determination itself; WM-ECO-006 puts the record into a disputed state that blocks disposition, and a breach declaration is a party event, not a judgment.

The landscape therefore renders overdue and dispute as independent facets of the same obligation. An obligation may be overdue and undisputed, disputed and not overdue, or both. A cure or additional period (`offer-cure-or-additional-period`) suspends inconsistent remedies without discharging the duty and without making the obligation not-overdue.

# Conflicting agreements

Conflict is recorded, never resolved. Within one agreement, WM-ECO-006 owns constituent-document precedence ranks and authentic language via `document-set-precedence-and-language`, plus incorporation of competing standard terms. Across agreements, no cited source supplies a resolution rule, so the profile emits a typed conflict observation: the two obligations, their source clause references, the conflict kind (contradictory duty, incompatible deadline, overlapping exclusivity, incompatible governing law), and the precedence assertion each agreement itself declares — with no computed winner.

Precedence assertions are carried as declarations with their basis and are explicitly not interpreted. WM-ECO-006 records that a force-majeure certificate is not automatic exemption, that agreed penalties may be unenforceable in some systems, and that CISG Article 28 lets a court refuse specific performance under its own law — each a reason the landscape must not compute a legal outcome. Automated legal interpretation is out of scope; the profile surfaces the conflict to the legal reviewer WM-XCT-029 requires for jurisdiction-bearing fields.

# Time/access

Four time axes stay separate: world/event time (when the contractual fact took effect), observation/ingestion time (when the register learned it), as-of/knowledge time (the state of knowledge the view reconstructs), and measurement period. Both parents mandate RFC 3339 with seconds and an explicit offset, WM-ECO-006 preserving the local offset of execution, dispatch and delivery rather than normalising to Z, and using `-00:00` where UTC is known but the offset is not. Historical reads at a past instant must return what the register asserted then.

Access is deny-by-default to non-party positions. Each party position reads the full joint record; non-parties read only through a declared, versioned projection under WM-XCT-003 with a published omission list, authorised by WM-XCT-002. Enumerated exceptions cover adjudication, regulatory basis, due-diligence grants and mandatory disclosure. Disclosure scope is a parameter of the view, and an aggregate or existence-only shape is the default where clause text or prices would otherwise leak.

# Scenario

Agreement A expires at its stated term. Termination is recorded as an event, not a deletion. Primary delivery obligations are released. The confidentiality obligation, carrying survival period P beyond termination, remains in an active state with its own clock; it is not overdue and not discharged. The evidence-retention obligation likewise survives, and its links to previously recorded fulfilment evidence remain resolvable because WM-ECO-006 forbids hard-deleting executed text, signature and performance evidence while any limitation period or hold runs, and WM-XCT-029 blocks deletion inside the enforceability window and tombstones rather than dangles references. A confidentiality breach declared after expiry is a valid non-performance against a surviving duty, with the expired agreement expression still addressable as its source. The negative case — expiry deleting the confidentiality obligation — is rejected: contract term is not obligation term, and expiry of the instrument is a lifecycle event on the agreement, never a disposition of its surviving duties or their evidence.

# Invariants

1. Contract term is not the term of each obligation.
2. Party positions are historic; execution-time positions are never overwritten by later organizational change.
3. Dispute is visible separately from overdue and from non-performance.
4. Work identity persists across amendment; superseded expressions remain addressable.
5. Obligation identity is preserved on delegation and replaced on release-and-substitute novation.
6. Derived obligations are marked derived and never acquire normative status over executed text.
7. Due basis is explicit; a deadline is never inferred from the presence or absence of a date.
8. Conditional deadlines cite their trigger or detachment instant and are reproducible from recorded inputs.
9. Fulfilment requires an evidenced test or a recorded discharge mode; elapsed time alone never discharges.
10. Evidence revocation reopens by appending; it never edits prior findings.
11. Dependency on another party's performance is a typed edge naming the counterparty duty.
12. Dependency cycles are detected and reported, never silently ordered.
13. Conflicting agreements produce a recorded conflict with no computed winner.
14. Every view declares perimeter, as-of/knowledge time, disclosure scope and input pins.
15. Views are immutable, digest-identified and not re-importable as sources.

# Minimal profile shape

Scope and version; agreement perimeter (party positions, subject-matter class, governing-law declaration); obligation derivation pins (clause work identifiers, expression versions, derivation rule version); world and knowledge as-of; measurement period; dependency edge set with kind and counterparty-duty reference; unresolved-dependency and cycle register; deadline derivation inputs (due basis, trigger instants, calendar/business-day convention version, local-offset retention); survival register (surviving duty, survival period, source clause); state facets per obligation (lifecycle, overdue, excused, disputed, cure window) held independently; evidence pointers with issuer, integrity proof and revocation status; conflict register with precedence assertions carried uninterpreted; disclosure scope and projection version; input revision pins; output digest; gap and hold register.

# Holds

Both parents are `publishableCanonical: false` reviewable drafts. WM-XCT-029 carries a boundary-review requirement on its edges to the agreement, right, policy and compliance-register models, declared gaps for service-level objectives (ISO/IEC 19086-1 unreachable) and obligations-register operations (ISO 37301 paywalled), and unasserted commitment operations. WM-ECO-006 carries a source-verification hold on all 21 URLs, a multi-profile validation hold, a writing-rule hold, a regional-labelling hold and a no-conformance hold, plus a deferred question on whether an obligation's source may be a legal norm rather than a clause — directly relevant to statutory duties in this landscape. Withholding of performance in reciprocal obligations and insolvency effects on enforceability are deferred in WM-XCT-029. No semantic crosswalk between the two parents has been verified, no relation between them exists in the frozen ledger, and no fixtures were run. Nothing here is legal advice, a claim of canonical completeness, or an installable release.
