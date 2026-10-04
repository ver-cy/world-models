# EM-COM-04 Independent Review

## VERDICT

**PROFILE.** No new aggregate. EM-COM-04 binds to WM-ACT-021 *Service Case / Ticket* as a profile-bound case type, which is exactly the extension mechanism WM-ACT-021 declares for itself ("request, inquiry, issue and complaint are represented as profile-bound case classifications"). Three of the four contour invariants are already owned by the frozen WM-ACT-021 contract; one requires a genuine profile-level addition (requester-presence mode). Creating a second inquiry/service-request aggregate would duplicate identity, merge, state and closure semantics that WM-ACT-021 already holds.

## COVERAGE

**Invariant 2 (merge/relationship without chronology loss) — fully owned.** `link-or-merge-case` states the effect "predecessor identities and history remain resolvable"; the `duplicates-merge-and-originating-subject` finding carries merge continuity; the *safe mutation and federation* decision mandates append-only revisions and alias retention. Reuse, no profile needed.

**Invariant 3 (many cases → one incident/problem/root-cause fix) — semantically owned, structurally unpinned.** The *case versus underlying subject* decision and the "Incident or problem" boundary note establish that the underlying condition keeps independent identity; `remedy-root-cause-and-corrective-action-bindings` carries the link. The many-to-one direction is implied but never stated as a cardinality contract, and the relation ledger holds no approved edge.

**Invariant 4 (resolution vs closure vs acceptance) — fully owned.** The *resolution, acceptance and closure* decision names them separate assertions with independent authority and evidence; `resolve-close-or-cancel-case` produces outcome revision and closure decision as distinct outputs; the `closure-cancellation-and-acceptance` finding carries acceptance and unresolved obligations. Nothing to add at Enterprise level; only *which* prerequisites gate closure and whether deemed acceptance applies is local policy.

**Invariant 1 (explicit anonymous requester mode) — partially owned.** WM-ACT-021 separates requester, submitter and represented party, and `register-case` yields "an attributable case with explicit unknowns". An unknown requester is not the same assertion as a declared anonymous mode: unknown is a data gap, anonymous is an intake decision with downstream consequences for contactability, acceptance and projection.

## GAPS

**G1 — Requester-presence mode (justifies PROFILE).** Missing semantics: a closed vocabulary distinguishing *identified*, *pseudonymous*, *withheld-by-requester*, *anonymous-by-policy*, plus the derived assertion "acceptance is unobtainable by design". This changes `register-case` preconditions, `record-case-communication` audience resolution and closure prerequisites, so it is profile-level, not a note.

**G2 — Merged-case chronology ordering (adoption/mapping note only).** WM-ACT-021 preserves history but does not state how two merged chronologies interleave. WM-ACT-027 supplies the RFC 3339 temporal profile and correlation keys. Mapping note, not new semantics.

**G3 — Case↔issue cardinality and direction (registry reconciliation, not modelling).** Needs an approved edge asserting many WM-ACT-021 cases → one WM-KNW-014 issue.

**G4 — Acceptance solicitation policy (local policy).** Deemed acceptance, silence windows and reopen windows are jurisdiction- and sector-bound; the frozen contract deliberately leaves these to profiles.

## SIBLING REFERENCES

- **WM-KNW-014 Issue / Problem** — carries root cause, known error, workaround and disposition. It declares `CHILD` of WM-ACT-021 while describing that parent as "change request / work item". WM-ACT-021 is a service case, not a change model. This is a contradiction inside the frozen dossier and must be resolved before EM-COM-04 cites either edge.
- **WM-ACT-027 Communication Interaction** — owns turns, delivery evidence and the permission-decision reference. Note a requiredness mismatch: WM-ACT-027 makes the permission/consent reference `required: true`; WM-ACT-021's communication composition is `required: false`.
- **WM-ACT-007 Work Order** — remedy execution authority; referenced, never absorbed.

## MINIMUM PUBLISHABLE ARTIFACT

A single EM-COM-04 profile binding document containing: (1) profile identity plus pinned `WM-ACT-021 v0.3.0-research.1` and its `synthesisSha256`; (2) the requester-presence mode vocabulary and its effect on register/communicate/close preconditions; (3) an invariant-to-element conformance table for all four invariants; (4) declared sibling edges with direction and cardinality, marked provisional; (5) the mismatch register (WM-KNW-014 parent direction; permission requiredness); (6) an inherited-status statement. No schema, no runtime rules, no new aggregate.

## BLOCKERS

1. Both WM-ACT-021 and WM-KNW-014 are `reviewable-draft` with `publishableCanonical: false`; EM-COM-04 cannot publish above the status of what it profiles.
2. WM-ACT-021's relation ledger has no approved outgoing edges — every sibling reference here is provisional.
3. The WM-KNW-014 → WM-ACT-021 `CHILD` declaration conflicts with WM-ACT-021's own scope.
4. Single-provider waiver on both models: no independent external review exists upstream. This review does not cure that.
5. Sector/jurisdiction profiles for privacy, retention and closure are explicitly deferred upstream, and G1 sits inside that deferred surface.

## FIVE ADVERSARIAL FIXTURES

1. **Anonymous report, later self-identification.** Anonymous-mode inquiry resolved with no contactable requester; three months later a party claims authorship and demands the chronology. Does the case gain a requester retroactively, or gain a new attested claim over an immutable anonymous intake?
2. **Merge with divergent commitments.** Two cases merge; each pinned a different SLA policy version and one ID already exists in an exported external ticket. Which commitment instance survives, and does the losing alias still resolve from the external system?
3. **Rolled-back root-cause fix.** Four hundred cases reference one problem; the fix is reverted after three hundred closed as resolved. Do prior resolution assertions remain true-as-asserted while acceptance and closure are separately invalidated?
4. **Deemed acceptance across a calendar boundary.** Closure recorded, acceptance timer expires during a holiday the business calendar excludes, then the customer rejects. Closure stands, acceptance disputed — three distinct assertions must remain independently readable.
5. **Agent-submitted anonymous caller withdrawing consent.** Submitter is an agent, represented party is anonymous, permission is later withdrawn. Tests the requiredness mismatch between WM-ACT-021 and WM-ACT-027.

*This review is a documentary assessment of the frozen dossier. No model was executed and no standards conformance is claimed.* (~790 words)
