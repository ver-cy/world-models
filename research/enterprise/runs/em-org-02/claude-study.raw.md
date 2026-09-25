# Boundary review — EM-ORG-02 Legal Identity and Registration

*Independent reviewer opinion on frozen dossier only. No canonical status, legal effect, approved relation or installability is claimed or implied.*

## Verdict per model

**WM-ORG-001 Organization — PROFILE.** Retain as the single master of organization / legal-subject identity (the party that can be a contract counterparty, carry a canonical key, bear entity status, succession and continuity). Profile it by demoting its `formation-and-registry-entries` and `standing-status-and-obligations` layers from owned structure to typed references into registration records. It keeps `entity-status`, `canonical-key-selection`, `entity-resolution-and-duplicates`, `lifecycle-event-records`, `succession-and-continuity`, `dissolution-and-expiry`. It surrenders `register-code`, `register-entity-number`, `register-entry-date`, `cross-register-identifier` and `record-registration-status` as owned elements.

**WM-ORG-010 Legal Entity Registration — PROFILE (re-subjected), not merge/retire.** Independent identity and lifecycle are proven for the *registration record*: it has its own key (authority + assigned number), its own status enumeration (published/pending/lapsed/retired/duplicate), its own evidence, currency and renewal clocks, and it can lapse while the subject lives. That is not the lifecycle of WM-ORG-001. But its declared subject is wrong: `register-anchored-legal-entity-identity` makes "(registration authority, register identifier)" the *master identity of the legal person*. That is the direct generator of duplicate `LegalEntity` and must be re-subjected to master the *record*, not the person.

**WM-ORG-011 Business Establishment / Branch — PROFILE, narrowed, with a standing publication hold.** Keep as master for operating presence (site bindings, local activity, availability, presence recognition, reporting grain). Strip any mastership claim over `registration-evidence-record` as a source of legal standing; it may cache a reference to a WM-ORG-010 registration record but must not assert registered existence. Evidence depth is the weakest in the set (single-provider waiver, no independent external review, 9 sources, templated "proposed structured answer group" data elements), so it is not eligible to master anything a legal or compliance answer depends on.

No identifier-unassigned candidate is proposed. The three needed subjects — legal subject, registration record, operating presence — are covered by the three existing identifiers once re-subjected.

## Evidence state

All three publications are `reviewable-draft`, `publishableCanonical: false`. WM-ORG-001 and WM-ORG-010 are dual-provider adjudicated and boundary-reviewed; WM-ORG-011 is Codex-only under an owner waiver, self-audited, which is not independent review. WM-ORG-011's dossier depth is `index-and-publication-metadata`, below the other two. Selected findings are a reviewer projection of specs pinned at 301830 / 279735 / 98436 bytes with stated SHA-256; full semantic crosswalk was not performed here and is not asserted. Registry relations and Enterprise v1 candidate properties are non-normative.

## Identity / mastership reconciliation

One subject master: **WM-ORG-001**. One master per registration record: **WM-ORG-010**, with *one record per (registration authority, register instance, assigned entry)* — never one record per legal person. Cardinality is subject 1 → 0..n registration records. Zero is a first-class case (informal collectives, statute-formed bodies), which WM-ORG-001 already admits and WM-ORG-010's `CHILD`/`required: true` composition does not; that composition must be re-read as an upward reference from record to subject, not a subtype narrowing that forces every registered subject to exist twice.

The duplicate-LegalEntity guard is a mastership rule, not a matching heuristic: **ingesting a registration record never mints a subject.** Subject creation and subject merge are separate, evidenced decisions owned by WM-ORG-001's `reconcile-duplicate-records`, carrying method, compared attributes, confidence, decider, reversibility and an explicit *non-match* outcome, with tombstones that keep retired keys resolvable.

## Registration and identifier contract

Five separable things, none substituting for another:

1. **Subject status** — is the organization in existence and operating (WM-ORG-001 `entity-status`).
2. **Registration-record status** — standing of one record/identifier as a data object (WM-ORG-010), n per subject, independently dated.
3. **LEI** — a governed global identifier layered over a register entry, with its own record status; never the subject key by default, never evidence of personality.
4. **Tax / VAT identifier** — different authority, different act, and frequently a *different unit* (VAT group, establishment). Carried scheme-qualified; never a merge key.
5. **National register number** — meaningful only inside its authority's namespace.
6. **Evidence extract** — a dated, authenticated artifact speaking as of a point in time with a freshness window; it is provenance, never a status and never an identity.

**Equality test.** Two identifier values denote the same thing only if *scheme code* matches, *issuing authority/jurisdiction* matches, and the *validity intervals* overlap at the queried time. Equal strings across schemes, across authorities, or across disjoint validity windows are non-matches. Cross-scheme sameness is only ever an explicit, evidenced `identifier-equivalence-assertion` with strength — not an inferred join.

## Branch / establishment boundary

Three discriminators, applied in order, each independent of the others:

- **Legal personality** — can the subject independently bear rights and enter contracts? Yes → independent legal entity, its own WM-ORG-001 subject.
- **Register entry** — does an authority hold an entry for it? A branch typically has one (and may hold its own LEI under category BRANCH) *without* personality. Registration therefore never implies personality.
- **Operating locus** — a place of activity with neither personality nor register entry is an establishment/premises only.

Resulting placement: a registered non-person branch is a WM-ORG-001 subject record with `legal-personality-flag = false` and an attribution edge to the head-office legal person; its host-register entry is a WM-ORG-010 record; its physical operation is a WM-ORG-011 presence. Obligations and contracts attribute to the head office. A presence may span several sites, and a branch registration may span several presences — the mapping is many-to-many and must be recorded, never assumed.

## Succession and temporal rules

Three clocks kept separate on every assertion: event-effective time, authority-recorded time, observation time. Changes are classified by WM-ORG-001's `continuity-decision`: name change, seat transfer, legal-form conversion and restoration normally *preserve* identity; merger by formation, division and (jurisdiction-dependent) discontinuous redomiciliation *create* a successor subject with predecessor/successor edges. Succession writes new edges only — it never rewrites the party of an executed contract, never back-dates the predecessor's identifiers, and never reassigns a retired key. Predecessors remain resolvable after dissolution; deletion is a retention decision, not a consequence of cessation.

## Invariants

1. A registration record references exactly one subject; a subject has 0..n registration records.
2. No registration ingestion creates, merges or splits a subject.
3. Register number uniqueness holds only within (scheme, authority/jurisdiction, validity); never globally.
4. Registration-record status never substitutes for subject status, in either direction.
5. Register entry ≠ legal personality; personality is asserted separately and evidenced.
6. LEI, tax/VAT and register number are distinct scheme-qualified facts; no silent cross-scheme join.
7. An extract is a dated snapshot with an as-of time; it never sets status by itself.
8. Succession adds edges; historical parties, names and identifiers are immutable.
9. Retired identifiers are never reassigned and remain resolvable.
10. Every as-of query answers from assertion history, not from current state.
11. Operating presence asserts no legal standing.

## Scenario walkthrough

**Negative case.** A new extract arrives from register RA2 for a company already held under RA1. Under WM-ORG-010's current wording, the (RA2, number) pair is itself the master identity, so ingestion mints a second legal person; the company now appears twice, with split statuses and split contract history. Under the profiled contract, ingestion creates registration record R2 only, in `unlinked` state. Linking R2 to subject S is a separate resolution decision: compared attributes, evidence, confidence, decider, and a recorded outcome that may be *non-match* (two genuinely different companies) or *link* (one subject, two registers). Either outcome is auditable and reversible; neither is reachable by ingest alone.

**Acceptance case.** Subject S holds R1 (home register), R2 (LEI, own record status), R3 (VAT, different authority). Branch B is a subject with `legal-personality-flag = false`, head-office edge to S, host-register record R4, and presence P1. S is absorbed into T by merger effective E. Query "who was the party, and was the entity active, on date T0 < E": return S, entity status from the assertion true at T0, name valid at T0, and the subset of R1–R3 whose validity covers T0 — R2 may be `LAPSED` at T0 while S is active, and that is reported, not reconciled. B resolves to S, not to itself, as obligor. Query at T1 > E returns T as current subject with a predecessor edge to S, while the pre-E contract still names S.

## Migration / profile shape

Move from WM-ORG-001 to WM-ORG-010 as references: register code, register entity number, entry date, cross-register identifier, record registration status, registration evidence. Retain in WM-ORG-001: canonical key and tier, aliases, entity status, entity category and personality flag, formation act, lifecycle events, succession and continuity, dissolution, entity resolution. Re-subject WM-ORG-010's `register-anchored-legal-entity-identity` to a registration-record key, add a mandatory subject reference, and relax the `required: true` CHILD composition to an upward reference. Narrow WM-ORG-011 to presence; convert its `registration-evidence-record` to a read-only reference. Add a non-owned registration-record status vocabulary mapping per authority with declared mapping loss.

## Gaps and publication holds

All inherited holds stand and none are discharged here: unverified source retrieval and version pins in both dual-provider models (GLEIF URL variants, ISO catalogue pages rather than normative text, unreachable FATF, contested EU implementing regulation, GDPRhub as a load-bearing tier-3 source), incomplete multi-profile validation (US state formation, non-EU civil-law registers, China USCC / India CIN, forms arising without registration), unreframed multilingual co-equal legal names in WM-ORG-001, and WM-ORG-011's absence-of-independent-review hold. New holds from this review: the WM-ORG-010 subject re-designation is unvalidated against fixtures; the branch triple-placement (subject + registration + presence) has no worked fixture; no semantic crosswalk between WM-ORG-001 and WM-ORG-010 status vocabularies exists; identifier-equality and non-match cases have no negative fixtures. Until these are closed, this is a boundary opinion on a frozen draft — not an approved relation set, not canonical, not installable.
