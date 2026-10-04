# FROZEN SEMANTIC AUDIT — EM-ORG-01 (Company and Enterprise Group)

Single independent frozen auditor. No tools used. Material limited to the frozen dossier, the two provider studies, the comparison, the PROFILE and the FIXTURES.

---

## 1. Verdict

**REVISE.**

The boundary decision is sound. The profile artifact is not releasable: it under-specifies exactly the places where this contour's stated negative case and invariants are enforced — perimeter kind governance, graph constraints, bitemporal replay determinism, append-only history, mastership enforcement at the WM-ORG-001/WM-ORG-012 seam, and the inheritance of base publication holds. Thirty-one semantic defects are listed in §3, of which eleven are blocking.

---

## 2. Disposition of PROFILE over WM-ORG-001 and WM-ORG-012

**CONFIRMED.** `decision: PROFILE`, `newRuntimeId: false`, `bases: [WM-ORG-001, WM-ORG-012]` is the correct disposition on this evidence.

Confirmed because:

- Every v1 candidate field lands inside an existing base structure (business_name/purpose/industry/operating_scope inside WM-ORG-001's naming, declared-purpose, activity-classification and presence/statistical layers; group_name/boundary_basis/consolidation_basis/effective_period inside WM-ORG-012's `relation-identity.kind`, `relation-identity.scope`, `control-interest.controlBasis` and `relationship-time.validTime`).
- "Company" exhibits no independent identity, formation act, standing, obligation cycle or succession distinct from the WM-ORG-001 subject; it is that subject narrowed by `entity-category` and `legal-personality-flag`, which are applicability switches, not a second lifecycle.
- A named perimeter has no formation act, no registration standing, no filing obligation and no succession of its own; it is a versioned specification plus a reproducible projection over WM-ORG-012 membership facts.
- No reserved model exists for this contour, and both providers independently reached PROFILE.

**No identifier is allocated by this audit.** The audit does not create, reserve or imply `Company`, `EnterpriseGroup`, `GroupMembership`, `BusinessBoundary`, `BrandAssociation` or any perimeter identifier as a catalogue or runtime id. The split trigger remains unallocated and, per §3 D-A3, is currently mis-armed.

**CONFIRMED-WITH-CORRECTION** on one sub-disposition: the PROFILE's treatment of legal personality (see D-B8, C-07) is wrong as written and must be corrected without changing the PROFILE verdict.

---

## 3. Semantic defects

Blocking defects marked **[B]**.

### Class A — Duplicate organization identity

**D-A1 — Company profile states only what is not a key.** **[B]**
The constraints forbid dates, names, addresses, brands, sites and affiliations as keys but never state the positive key rule, and never carry WM-ORG-001's unregistered case (identity resting on an adopting-Dimension UUID/ULID) or the multilingual case where several co-equal language-tagged legal names exist.
*Fix:* add a constraint naming the key as (a) a scheme-qualified identifier with issuing scheme and register code, or (b) an adopting-Dimension canonical key where no authoritative identifier exists; add that two distinct organizations may legitimately carry the same legal-name string, and that co-equal legal names in multilingual jurisdictions never reduce to one.
*Fixture:* two organizations with identical legal-name strings in different register codes → two identities retained; an unregistered collective with no scheme identifier → identity accepted on canonical key alone, registration findings marked inapplicable, never treated as a data gap; a subject with two co-equal legal names → both retained as legal-kind, neither demoted to alternate.

**D-A2 — No entity-resolution gate and no identifier non-reassignment rule.** **[B]**
Nothing requires a merge, split or non-match to carry comparison evidence, method, confidence, a coded resolution decision, a resolvable tombstone and reversibility; nothing forbids reassigning a retired identifier or ignoring an upstream DUPLICATE/annulled registration status.
*Fix:* require every resolution act to emit a resolution record (compared attributes, sources, method, confidence with named scale, coded decision including explicit non-match, deciding agent, timestamp, reversibility) and a resolvable tombstone for any retired record; state that an identifier retired by dissolution or merge remains a historical key and is never reassigned.
*Fixture:* silent merge without a resolution record → reject; explicit non-match must persist so the same comparison is not re-decided; merged record must remain resolvable as a tombstone; reuse of a dissolved subject's identifier → reject; upstream DUPLICATE status on a candidate must be surfaced, not overwritten.

**D-A3 — Split trigger is mis-armed against the known nearest miss.** **[B]**
Both studies identify the register-issued statistical enterprise-group number as the nearest miss that must stay alignment-only, yet no fixture refuses a partial trigger. `true-group-actor-trigger` is the only trigger fixture and it is positive, so the only tested path is the one that creates a subject.
*Fix:* state explicitly that a register-issued group number alone satisfies none of the three conditions; require all three to be independently evidenced and recorded before any subject is created; state that a created group actor is a WM-ORG-001 instance with `legal-personality-flag` and `entity-category` explicitly asserted, is never a member of its own perimeter, and never becomes master of any member fact.
*Fixture:* statistical enterprise-group number alone → refuse subject creation, retain alignment only; any two of three conditions → refuse; created group actor without asserted entity-category/personality → reject; group actor appearing as a member of its own perimeter → reject.

**D-A4 — `BusinessBoundary` is bound ambiguously and collapses two different perimeters.** **[B]**
The PROFILE treats "EnterpriseGroup / BusinessBoundary" as one thing over WM-ORG-012, but the dossier lists `BusinessBoundary` beside `Company`, where it also reads as the single-subject business perimeter — which legal units, sites and activities constitute "the business." That is the statistical-enterprise-spanning-legal-units problem, not a group problem, and the conflation is the exact route by which several legal units get merged into one "company."
*Fix:* split the term into two disjoint profile objects: `GroupPerimeter` (multi-organization, over WM-ORG-012 membership facts) and `BusinessPerimeter` (single-subject operating/statistical alignment on WM-ORG-001, alignment-only, never an identity, never a merge key, never an input to a consolidation perimeter).
*Fixture:* a statistical enterprise spanning two legal units → two organization identities retained, one business-perimeter alignment recorded, no merge; a business perimeter submitted as a group perimeter → reject; a business perimeter used as a consolidation input → reject.

**D-A5 — Unit, team and branch endpoints are unguarded.**
Management perimeters sourced from internal structure will present WM-ORG-002 units and WM-ORG-003 teams as members; WM-ORG-012 endpoints are organization references only, so either units leak into endpoints or a unit is silently promoted to an organization. The branch case is the inverse trap: a branch holding its own LEI is a categorised organization record, not an internal unit.
*Fix:* constrain perimeter endpoints to WM-ORG-001 subjects; require units and teams to be routed through containment, never membership; state the discrimination test (independent registry entry or scheme-issued identifier → organization, else unit) and that a branch is recorded once, as an organization with BRANCH category, not twice.
*Fixture:* unit or team as a perimeter member → reject with a containment redirect; branch with its own LEI modelled as an internal unit → reject; the same branch present as both an organization record and a unit → reject as duplicate identity.

### Class B — False control and consolidation

**D-B1 — `perimeterKinds` is an ungoverned string list.** **[B]**
WM-ORG-012's `relation-identity.kind` requires scheme, version, code and exclusions. The PROFILE supplies six bare strings with no scheme identifier, no version, no per-kind definition, no required basis type per kind, and no mutual-exclusion matrix. A bare string list is re-interpretable at will, and without exclusions a brand-licence edge can be read as control by a downstream consumer.
*Fix:* define the kinds as a versioned code list with, per kind: code, definition, admissible basis types, required basis fields, admissible evidence classes, and an exclusion set naming the near-neighbour kinds it is not equivalent to; declare the list closed for a specification version, with extension only by a new version and a named governing owner; require the list version to be pinned on every membership fact and every materialization.
*Fixture:* membership with a kind outside the pinned list → reject; membership with a kind but no list version → reject; one relationship asserted as both brand-licence and consolidation on the same evidence → reject; consolidation kind with a basis type admissible only for franchise → reject.

**D-B2 — No graph rules.** **[B]**
WM-ORG-012 carries `graphRules` (profile, cardinality, cyclePolicy, selfLinkPolicy) and asks the kind-specific question. The PROFILE states none, so two ultimate parents can coexist at one instant, consolidation cycles are untyped, and self-links are unforbidden.
*Fix:* declare per-kind cardinality (at most one ultimate-consolidation parent per valid-time slice; at most one direct-consolidation parent per slice; management may be multi-parent; brand-licence and alliance many-to-many), acyclicity for consolidation within a slice, self-link prohibited for consolidation and control, and that no universal organization tree is imposed across kinds.
*Fixture:* two ultimate parents with overlapping valid time → reject or surface as a typed conflict, never silently pick one; consolidation cycle → refuse materialization with a typed error rather than breaking the cycle; self-consolidation → reject; multiple management parents → accept.

**D-B3 — No bar on transitivity, collapsed chains, or derived-to-asserted contamination.** **[B]**
WM-ORG-012 puts universal transitivity out of scope and carries `chain.prohibitedInferences`; BODS requires indirect interests through component records. The PROFILE forbids none of this, and nothing prevents a materialized perimeter from being re-ingested as asserted evidence.
*Fix:* forbid inferring control from edge composition without a named, versioned derivation rule; require indirect interests to retain component records and never be collapsed into a single edge; state that a derived edge or materialized perimeter is never admissible as an asserted fact or as evidence for another derivation.
*Fixture:* transitive control inferred from two direct edges with no derivation rule → reject; indirect interest without component records → reject; derived perimeter re-ingested as an asserted membership → reject; derived edge cited as recognition evidence → reject.

**D-B4 — Only one period type survives; accounting and filing periods are lost.** **[B]**
RR-CDF carries three distinct period types and BODS separates statement date from interest start; the PROFILE reduces everything to valid time, knowledge time and inclusion date. A consolidation perimeter for a reporting year therefore has no period to evaluate against, and a relationship valid in one year can be used for another year's consolidation.
*Fix:* require typed periods with the period type declared (relationship validity, accounting period, document filing period) and require a consolidation perimeter materialization to name which period type it evaluates; require interest quantifiers to carry measurement method, unit, denominator, class, as-of and uncertainty.
*Fixture:* consolidation membership with no accounting period → reject; perimeter materialized for an accounting period using relationship validity only → reject; min/max range interest compared to a threshold as if exact → reject; quantifier without denominator or class → reject.

**D-B5 — Control thresholds are unpinned and not jurisdiction-qualified.**
BODS asks under which jurisdiction's threshold a beneficial-ownership or control determination is made; no constraint requires any threshold used by a perimeter rule to be a pinned, jurisdiction-qualified rule parameter.
*Fix:* require every threshold test to be a declared parameter of the pinned rule version, qualified by jurisdiction and standard, and recorded in the materialization manifest.
*Fixture:* an unqualified majority-threshold rule → reject; the same fact set under two jurisdiction-qualified rule versions → two distinct, separately labelled results, never one merged answer.

**D-B6 — Statistical perimeter conflates a Dimension derivation with an authority's delineation.** **[B]**
The PROFILE lists `statistical` as a perimeter kind but never says whether such a perimeter is authority-asserted or Dimension-derived from control links. WM-ORG-001 holds statistical-unit alignment as ALIGN-only with an explicit merge/split prohibition; the statistical authority is master of its own enterprise-group delineation.
*Fix:* split the case: an authority-asserted statistical perimeter records the statistical register, unit identifier and authority as master with the Dimension as non-master replica; a Dimension-derived statistical perimeter is labelled derived, non-authoritative and non-comparable to the official delineation, is never written back to `statistical-unit-type`, and never drives merge or split.
*Fixture:* derived statistical perimeter published as the official enterprise group → reject; derived result written into the statistical-unit alignment fields → reject; authority delineation disagreeing with the derived result → retain both as a recorded divergence, never resolve silently.

**D-B7 — HR/ERP structure can reach the consolidation perimeter.**
The dossier names HRIS as a candidate master system and its third comparison track separates corporate governance, actual org structure and the HR/ERP representation. Nothing stops an HRIS reporting line from being recorded as a control or consolidation basis.
*Fix:* constrain HR/ERP-sourced facts to the management kind with the source system recorded as master, and forbid them as admissible basis or evidence for consolidation, ownership-control or statistical kinds.
*Fixture:* HRIS reporting line submitted as a consolidation basis → reject; the same line as a management-kind membership → accept with source master recorded; a management perimeter used as a consolidation input → reject.

**D-B8 — The constraint barring legal personality from the Company profile removes the applicability switch.** **[B]**
"Legal personality and registration facts remain external sibling aspects and are never copied into the Company profile" conflates *not researched in this contour* with *not referenced by this profile*. WM-ORG-001 holds entity category, legal-personality flag, formed-by-statute, formation act, registry entries and standing as in-scope, and those are precisely what stop a branch or sole proprietorship from being treated as a separate consolidating legal person.
*Fix:* restate as a mastership rule, not a reference ban: the Company profile does not master and does not duplicate legal-personality or registration facts, and must reference them from WM-ORG-001 as mandatory applicability switches, with the master named per field group. Answer the contour's own question here: business and legal person coincide only where the subject carries separate legal personality with a registration standing; otherwise they are two aspects of one subject and the bearing legal person is referenced, never inlined.
*Fixture:* Company profile instance without a referenced entity-category and personality flag → reject; branch without separate personality treated as a consolidating parent or as an independent legal person → reject; sole proprietor whose legal person is a natural person → business-facing record plus a person reference, never a merged subject; resident government entity formed by statute → registration findings inapplicable, not missing.

**D-B9 — Reporting-exception mastership is orphaned.**
The constraint grants WM-ORG-001 only identity, names, succession, statistical alignment and derived endpoint indexes, which excludes `reporting-exception-reason`; yet the `absence-status` fixture requires a typed no-parent exception to be preserved. No side masters it.
*Fix:* assign organization-side reporting exceptions to WM-ORG-001 explicitly (they are obligations about the organization, not relationship facts) and distinguish them from WM-ORG-012's `absence.reason`, stating how a perimeter result reports each.
*Fixture:* organization-side reporting exception written as a relationship absence → reject; perimeter materialized over a subject with an open reporting exception → result carries the typed exception and never a synthesized parent; exception with no review date → reject.

### Class C — Mutable historical perimeter meaning

**D-C1 — No append-only rule.** **[B]**
Both bases are append-only in substance (WM-ORG-012's functions append revisions and claims; WM-ORG-001 mixes in the audit-trail model under append-only artifact rules). The PROFILE never states it, so an in-place edit of a membership fact silently rewrites every past perimeter.
*Fix:* state that membership facts, evidence, closures and perimeter specifications are append-only; any change is a new superseding revision carrying `supersedes`, with the superseded revision retained and retrievable.
*Fixture:* in-place edit of a membership fact → reject, must supersede; revision without `supersedes` → reject; superseded revision unretrievable → reject; past as-of view recomputed after a supersede at an earlier knowledge time → unchanged.

**D-C2 — Perimeter specification versions are not immutable and have no lineage.** **[B]**
Specification version is part of the perimeter identity tuple, but nothing declares a published version immutable, and nothing links versions, so amending the kind filter, role scope, basis requirement or as-of policy in place changes the meaning of every historical materialization while the identity tuple stays constant.
*Fix:* declare a published specification version immutable across all of its semantic content (admitted kinds and kind-list version, endpoint roles, required basis, as-of and knowledge-time policy, dispute and absence policy, threshold parameters, rule version); require a lineage link between successive versions; require every materialization to cite the version it evaluated.
*Fixture:* edit to a published specification version → reject, must mint a new version; new version without lineage to its predecessor → reject; replay of a past materialization under an amended specification → refuse, or return under the original pinned version with an explicit version-divergence notice; results from two specification versions presented as comparable → reject.

**D-C3 — Closure meaning is untested; record retirement can shrink past perimeters.** **[B]**
WM-ORG-012's `closure.meaning` separates real-world termination, publisher record retirement and correction of erroneous data. No fixture exercises the distinction, and it is the central mutable-history test for this contour.
*Fix:* require closure meaning, reason and evidence on every membership close, and state the replay consequence of each: real-world termination shortens valid time and changes past views only after its effective date; record retirement changes no valid-time view; correction changes valid-time views only at knowledge times after the correction, with the pre-correction view retained.
*Fixture:* membership closed as record retirement → all past as-of views unchanged; closed as real-world termination → views after the effective date change, earlier ones do not; closed as correction → two retrievable views across the correction's knowledge times; closure with no meaning code → reject.

**D-C4 — Retention and erasure versus pinned materialization inputs.** **[B]**
WM-ORG-001 carries an erasure/minimisation action, and materializations pin input fact ids and digests. When an input is archived, deleted or minimised to a tombstone, replay either breaks or silently returns a different set.
*Fix:* require a materialization to be replay-safe under retention: retain a self-contained evidence manifest with digests, and define tombstone-tolerant replay that returns the pinned result digest plus a typed `inputs-redacted` status naming which inputs are unavailable. A replay may never silently produce a different member set.
*Fixture:* replay after an input is minimised to a tombstone → pinned digest plus `inputs-redacted`, never a recomputed different set; replay returning a different set without a typed status → reject; materialization with no evidence manifest → reject.

### Class D — Non-reproducible bitemporal views

**D-D1 — "Knowledge time" is singular against three stamps in each base.** **[B]**
WM-ORG-012 carries observedAt, recordedAt, publishedAt and supersedes; WM-ORG-001 separates effective date, authority-recording date and observation timestamp. The PROFILE offers one "knowledge time" and never nominates the replay axis, so two implementations replay against different clocks and both claim conformance.
*Fix:* nominate one replay axis (the adopting Dimension's recorded-at) as normative for every as-of query, retain the other stamps as attributes, publish the crosswalk between the WM-ORG-001 triple, the WM-ORG-012 quartet and the profile's two axes, and require all timestamps to be RFC 3339 with explicit offset.
*Fixture:* as-of query with no declared axis → reject; a fact whose observed-at precedes its recorded-at across a correction → replay follows recorded-at only; timestamp without offset → reject; the same query replayed on two implementations → identical member set and digest.

**D-D2 — Materialization manifest is incomplete, so results are not deterministic.** **[B]**
The manifest pins valid time, knowledge time, specification version, input fact ids and digests, rule version and result digest. It omits the kind and basis code-list versions, the dispute and absence policy version, the threshold parameter set, the member ordering and tie-break rule, and the interval precision, uncertainty and open-endedness policy — while both bases explicitly carry precision, uncertainty and open ends.
*Fix:* extend the manifest to pin all of the above, and declare a total, deterministic member ordering plus an explicit policy for estimated, unknown and open interval endpoints (whether an open or unknown endpoint includes, excludes or flags the member).
*Fixture:* materialization missing any pinned element → reject; a member whose interval endpoint is estimated, unknown or open → resolved by the pinned policy, flagged in the result, never silently included or dropped; two runs of the same manifest → byte-identical result digest and identical member order.

**D-D3 — Dispute and absence handling is undefined.** **[B]**
The `disputed-fact` fixture expects the result to be "qualified" and `absence-status` expects an exception preserved, but neither the PROFILE nor the fixtures define what qualification does to membership, so a disputed control fact may be counted, excluded or flagged at each implementation's discretion.
*Fix:* define a versioned dispute-and-absence policy stating, per kind, whether a disputed fact is included, excluded or included-with-qualification; require the result to carry a per-member status and a result-level qualification; require absence reasons to distinguish unknown, withheld, not-reported, expired and evidenced non-existence within a declared coverage scope and search time.
*Fixture:* disputed consolidation fact → per-member status plus result-level qualification, never a bare boolean membership; two competing claims → both retained, resolution only by the named authority; absence with no reason code or no coverage scope → reject; withheld data presented as absent → reject.

### Class E — Member-mastership leakage

**D-E1 — `perimeter-owns-member` covers only editing.** **[B]**
Leakage has at least five further routes, none tested: a group projection applying perimeter-level disclosure or licence terms to member facts and over-publishing them; a member's retention action leaving a dangling membership; the perimeter result inheriting the strongest rather than the weakest member corroboration; a perimeter steward acting as an authorised change agent on member identity fields; and member attributes (activity code, jurisdiction, standing) being inferred from membership.
*Fix:* add constraints for each: member disclosure class and licence always dominate a perimeter projection; a member retention action must leave the membership resolvable as a tombstone, never dangling and never deleted; a perimeter result carries the weakest corroboration level among its inputs; perimeter stewardship confers no change authority over any member or relationship field; and no member attribute may be inferred from membership.
*Fixture:* perimeter projection publishing a member fact above its disclosure class → reject; member erased leaving a dangling membership → reject; perimeter result claiming corroboration above its weakest input → reject; perimeter steward editing a member identity field → reject; member jurisdiction or activity code inferred from its group → reject.

**D-E2 — Mastership at the seam is asserted, not enforced, and the required base amendment is missing.** **[B]**
The PROFILE names WM-ORG-012 master of relationship facts while WM-ORG-001 is published with a `record-control-relationship` function that creates and updates relationship records, with consolidation, group and ownership findings, and with an adjudication that *accepted* the endpoint-retaining reading and deferred the seam. `proposedRegistryAmendments` covers only the PARENT→REFERENCE demotion. The profile therefore re-adjudicates a base unilaterally, and the second write path stays open.
*Fix:* add a second held amendment against WM-ORG-001 (demote the control/ownership endpoint fields and the `record-control-relationship` write function to derived, read-only, regenerable projections of WM-ORG-012 edges, with a stated regeneration rule and no independent write path) and record it as reopening WM-ORG-001's accepted boundary decision. Until both amendments are approved, the profile must declare the seam blocked rather than name a master.
*Fixture:* profile naming WM-ORG-012 master while the WM-ORG-001 seam item is open → publication refused; the same consolidating-parent fact authored on both sides → reject; a WM-ORG-001 endpoint index edited directly rather than regenerated → reject; an endpoint index presented as authoritative → reject.

**D-E3 — No stewardship declaration and no profile owner.**
Three distinct stewardship levels exist — member record (WM-ORG-001), relationship record (WM-ORG-012), perimeter specification (this profile) — and the PROFILE names none, while both registry entries assign maintainership to "the organization" or a register, which cannot own an adopter's perimeter construct. Unassigned stewardship means the perimeter author de facto claims authority over members.
*Fix:* declare the three levels with master, steward, authority basis and review-due per level, name the profile owner and the perimeter-specification steward, and state that each level's authority stops at its own record.
*Fixture:* perimeter specification with no steward or review-due → reject; a single steward asserted across all three levels → reject; authority basis absent on any level → reject.

### Class F — Unsupported release claims

**D-F1 — The release gate is unenforceable because the fixtures are declarative.** **[B]**
`declarativeOnly: true` with no harness, no schema, no pass/fail predicate and no expected artifact digests, yet `release-gate` is itself expressed as a fixture expecting a refusal to be enforced. Both bases also lack executable fixtures, WM-ORG-012 explicitly so.
*Fix:* rename the set to fixture intents, add `executable: false`, and add an execution-requirements block (harness identifier, case schema version, deterministic pins, expected result digest per case, recorded outcome per case). `fixturesExecuted` may flip to true only when every case has a recorded executed outcome and digest.
*Fixture:* `fixturesExecuted: true` with any case lacking a recorded outcome or digest → reject; a case with no machine-checkable predicate → reject as non-executable; publication attempt while the harness is undeclared → refused.

**D-F2 — Base publication holds are not inherited, and no rule caps the profile at its bases' status.** **[B]**
WM-ORG-001 carries seven open holds and WM-ORG-012 six; the PROFILE's gate lists five of its own. Material omissions for this contour: multi-profile domain validation not performed (six profiles); FATF 24/25 unreachable, so the ownership layer is not authority-backed although this profile leans on control and ownership; source and live-version verification incomplete with divergent GLEIF URL paths; the naming layer still asks for a single legal name; ISO 17442, ISO 20275 and ISO 5009 cited from catalogue pages or unfetched; EUID provisional; WM-ORG-012 lacking source pins, nested schema, resolver and graph-rule engine.
*Fix:* enumerate inherited holds with base id and hold text, and add a constraint that a profile's gate is the union of its own holds and all open holds of its bases, and that a profile can never hold an evidential status above the weakest of its bases.
*Fixture:* profile asserting canonical status while any base is `publishableCanonical: false` → refused; gate omitting any open base hold → reject; profile relying on the ownership layer while the FATF grounding hold is open → the reliance is marked provisional.

**D-F4 — Conformance loophole.**
"External GLEIF, IFRS, Eurostat and W3C sources are alignment evidence only unless exact conformance evidence exists" leaves "exact conformance evidence" undefined, which is precisely the loophole WM-ORG-001's holds close by requiring alignment-only until normative text is obtained.
*Fix:* replace the loophole with a gate: conformance may be claimed only with a pinned normative-text reference, a retrieval record, a version pin and a per-clause conformance statement; everything else is alignment-only, with no exception path.
*Fixture:* conformance claimed from a catalogue landing page or an indexed extract → reject; conformance claimed with no per-clause statement → reject; alignment restated as conformance in a projection → reject.

**D-F5 — IFRS is named as a source that neither base cites.** **[B]**
No IFRS source exists in either base's source set, yet the PROFILE names IFRS among its external sources and Grok's study derives a substantive control conclusion from IFRS 10 about franchise rights. That is an external fact introduced at profile level.
*Fix:* remove IFRS from the source enumeration or record it as an uncited, adopter-owned profile dependency with no source reference in either base; state that accounting-consolidation basis is carried as an adopter-supplied standard identifier and version in `controlBasis.accountingStandard`, and that the profile states no substantive accounting rule; withdraw the IFRS 10 franchise-rights conclusion as unevidenced on this material.
*Fixture:* perimeter asserting a consolidation basis with no standard identifier and version → reject; profile text stating a substantive accounting-control rule → reject; franchise excluded from consolidation on brand grounds alone rather than on an absent control basis → reject.

**D-F6 — No base pins and undeclared crosswalk depth.** **[B]**
The dossier's own blocking decisions require immutable refs and a confirmed semantic crosswalk; the registry records both mappings as `conceptual-candidate` with evidence depth `boundary-reviewed` and `index-and-publication-metadata`. The PROFILE names bases by id only, with no version, no byte count, no digest, and no statement that the crosswalk was performed against a keyword projection rather than the pinned full specifications.
*Fix:* add base references pinning model id, version, source file, source bytes, source SHA-256, synthesis SHA-256 and adjudication status; declare `crosswalkDepth` as selected-findings projection; surface both registry mapping statuses and evidence depths; state that any change to a base digest invalidates the profile revision.
*Fixture:* profile revision whose base digest no longer matches → invalid, must be re-audited; crosswalk claimed as confirmed while depth is a projection → reject; missing digest or version on any base → reject.

**D-F7 — None of the six required domain profiles is exercised.** **[B]**
WM-ORG-001's hold requires end-to-end walks of a registered company with an LEI, an unregistered informal collective, an international branch with its own LEI, a fund with umbrella and management relationships, a resident government entity formed by statute, and a sole proprietor. A profile named "Company" cannot claim coverage while the cases that decide whether a Company is a legal person are unwalked. The fund case additionally has management-and-umbrella control semantics with no matching perimeter kind, and WM-ORG-012's supply/exchange layer is unexercised although franchise and alliance kinds are declared over it.
*Fix:* add the six profiles as mandatory coverage cases with a recorded end-to-end walk each, and state that coverage claims are provisional until each is walked; either add a fund umbrella/management kind with its own basis or record the fund case as an explicit uncovered gap.
*Fixture:* one walk per profile, each asserting which findings are mandatory, optional and inapplicable for it; any coverage claim with an unwalked profile → reject; fund umbrella or management relationship forced into the consolidation kind → reject.

**D-F8 — Candidate types are not fully dispositioned.**
`GroupMembership` appears only inside prose constraints and `BrandAssociation` only as a prohibition; no artifact records a disposition for each of the five dossier candidate types, and no field-level binding exists for the eight v1 candidate fields. Unbound names get re-minted later as new attributes or types.
*Fix:* add an explicit disposition per candidate type (bound-to-base-structure, profile object, or refused, with reason) and a normative field-binding table mapping each v1 field to base model, bundle, layer, finding and data element with a status of bound, bound-with-constraint or deferred-unbound — including `boundary_basis` → kind code plus basis type, `consolidation_basis` → basis definition plus accounting standard, `effective_period` → typed valid time with precision, `group_name` → non-identifying label.
*Fixture:* an unbound v1 field introduced as a new attribute → reject; `group_name` used as a perimeter or organization key → reject; a candidate type used with no recorded disposition → reject.

---

## 4. Contradictions among dossier, providers, profile and fixtures

**C-01 — Registry versus publication state, both models.** Registry `vr.wm-org-001` records status `described-previous-version`, review state `migration-boundary-review` and spec ref `models/organizations/O1-organization.md`, while `current_specs` points at `publications/wm-org-001-organization/spec.yaml` with `status: published`. Registry `vr.wm-org-012` records status `candidate`, review state `boundary-review-required` and an empty spec ref, while `current_specs` shows a published spec file. Both mappings remain `conceptual-candidate`. The profile builds on the publication view and never reconciles the registry view. Resolve before any amendment is filed.

**C-02 — Queue reservation contradicts the delivered material.** `queue_reservation` records `status: queued`, `claude_status: not-started`, `grok_status: not-started`, `boundary_decision: pending`, `remaining_scope: "Entire research brief pending"`, yet two provider studies, a comparison and a revision-2 profile exist. The reservation record is stale relative to the work.

**C-03 — Entry-kind vocabularies disagree.** Registry says `standalone-mm` for both; the specs say `entity` for WM-ORG-001 and `relationship` for WM-ORG-012. Two vocabularies are in use with no crosswalk.

**C-04 — Registry parentage contradicts the model's own boundary.** `parent_ids: WM-ORG-001` on `vr.wm-org-012` versus WM-ORG-012's boundary note "a relationship is not either organization" and its `REFERENCE` composition edge. Both studies flag it; the PROFILE holds the amendment. As long as parentage stands, a perimeter is structurally owned by one member, contradicting the third dossier invariant.

**C-05 — Relation vocabulary mismatch.** The relationship ledger records `CONTAINS` for WM-ORG-001 → WM-ORG-002/003, while WM-ORG-001's composition records the same edges as `CHILD`. One vocabulary must govern.

**C-06 — Dangling sibling references.** WM-ORG-012's boundary notes and composition reference WM-ORG-014 and WM-ORG-015, which appear nowhere in the frozen registry reservations. The profile inherits unresolvable delegations for customer/account and supplier qualification.

**C-07 — Legal-personality delegation is a contour statement applied as a model statement.** The dossier scope parks legal personality and shares on neighbouring *research contours*; Grok's study routes them to EM-ORG-02 and EM-ORG-03; the PROFILE converts this into a ban on those facts inside the Company profile. WM-ORG-001 holds them as in-scope and mastered. Further, EM-ORG-03 is cited by Grok although the dossier's related contours are EM-ORG-02, 04, 05 and 06 — EM-ORG-03 is not listed and is unsupported on this material. Correct per D-B8.

**C-08 — IFRS appears as a source in the profile and as a substantive authority in Grok's study, with no IFRS source in either base.** See D-F5.

**C-09 — Franchise kind: providers disagree, the profile sides silently.** Claude treats franchise as expressible over WM-ORG-012's kind vocabulary; Grok states flatly that WM-ORG-012 has no franchise kind and no perimeter-profile object. The PROFILE declares `franchise` as a governed perimeter kind with no amendment and no vocabulary. Unreconciled.

**C-10 — Split trigger: disjunctive versus conjunctive, and two different outcomes.** Claude's trigger is any-of three, one of which ("must occupy an endpoint in WM-ORG-012") is the inverse of the PROFILE's third all-required condition ("external models must master the group without traversing WM-ORG-012"); Claude's outcome is a reserved new model candidate, Grok's is a WM-ORG-001 instance and never a catalogue type. The PROFILE adopts Grok wholesale without recording the divergence or the evidence that decided it.

**C-11 — The seam is simultaneously declared resolved and held open.** Claude declares the WM-ORG-001 seam trigger fired because WM-ORG-012 is registered and mastership must be assigned now; WM-ORG-001's deferred research says re-test at sibling registration; WM-ORG-012's registry status is `candidate` with `boundary-review-required`, so whether it counts as registered is itself unsettled. The PROFILE asserts mastership in its constraints while listing "dual-write seam unresolved" as an open hold. Internally contradictory.

**C-12 — Fixture set contradicts its own gate.** `declarativeOnly: true` versus the `release-gate` case expecting an enforced publication refusal, and `candidateStatus: provider-reconciled-awaiting-single-frozen-audit` alongside `fixturesExecuted: false`. Nothing in the set can be executed, so the gate it asserts cannot bind.

**C-13 — A base's unfixed framing is inherited silently.** WM-ORG-001 holds publication pending a naming-layer reframe to multiple co-equal legal names, yet its selected finding still asks which single name form is the legal name. The Company profile depends on name forms and carries the unfixed framing forward without noting it.

**C-14 — Basis value type contradicts the required structure.** The dossier's v1 candidate `consolidation_basis` is `text` while `boundary_basis` is `code`; WM-ORG-012 requires a structured basis (type, definition, accounting standard). A free-text consolidation basis cannot satisfy the coded, versioned basis the perimeter contract needs.

**C-15 — Profile constraint contradicts its own fixture on WM-ORG-001's retained scope.** The constraint limits WM-ORG-001 to identity, names, succession, statistical alignment and derived endpoint indexes; the `absence-status` fixture requires organization-side reporting exceptions to be preserved. See D-B9.

---

## 5. Closed remediation checklist

Sixteen items. The list is closed: no further item may be added to satisfy this audit, and no item may be closed by weakening a semantic rule, deleting a fixture, relabelling a defect as deferred research, or narrowing the profile's scope. Items 1–12 are blocking; 13–16 must be complete before the gate in 16 is evaluated.

1. Reconcile record state: registry versus publication status and spec refs for both models, entry-kind vocabularies, ledger `CONTAINS` versus composition `CHILD`, the stale queue reservation, and the dangling WM-ORG-014/WM-ORG-015 references. (C-01, C-02, C-03, C-05, C-06)
2. Pin the bases: model id, version, source file, bytes, source SHA-256, synthesis SHA-256, adjudication status, registry mapping status and evidence depth; declare `crosswalkDepth` as a selected-findings projection; invalidate the revision on any digest change. (D-F6)
3. State the positive identity key rule and the entity-resolution gate: canonical key or scheme-qualified identifier, resolution records with evidence, method, confidence, coded decision and reversibility, resolvable tombstones, identifier non-reassignment, same-string and co-equal-name cases. (D-A1, D-A2, C-13)
4. Correct the legal-personality constraint to a mastership rule and make entity category and legal-personality flag mandatory referenced applicability switches; answer the business-versus-legal-person question in those terms. (D-B8, C-07)
5. Split `BusinessBoundary` into `GroupPerimeter` and `BusinessPerimeter`, and constrain perimeter endpoints to WM-ORG-001 subjects with unit, team and branch routing rules. (D-A4, D-A5)
6. Replace `perimeterKinds` with a versioned, closed code list carrying per-kind definitions, admissible and required basis, admissible evidence and an exclusion matrix; pin its version on every fact and materialization; resolve the franchise-kind divergence and the free-text consolidation basis. (D-B1, C-09, C-14)
7. Declare graph rules, chain rules and inference prohibitions: per-kind cardinality, acyclicity, self-link policy, no transitivity without a versioned derivation rule, component records for indirect interests, and no derived-to-asserted contamination. (D-B2, D-B3)
8. Restore typed periods and quantifier semantics (relationship, accounting, filing; method, unit, denominator, class, as-of, uncertainty) and require pinned jurisdiction-qualified thresholds. (D-B4, D-B5)
9. Separate authority-asserted from Dimension-derived statistical perimeters; bar HR/ERP-sourced facts from consolidation, ownership-control and statistical kinds; assign organization-side reporting exceptions to WM-ORG-001. (D-B6, D-B7, D-B9, C-15)
10. Make history immutable: append-only with `supersedes`, immutable published specification versions with lineage, closure-meaning semantics with stated replay consequences, and retention-safe replay with an evidence manifest and a typed `inputs-redacted` status. (D-C1, D-C2, D-C3, D-C4)
11. Make replay deterministic: nominate the single knowledge-time replay axis with a crosswalk to both bases' time vocabularies, complete the materialization manifest (code-list versions, dispute and absence policy version, threshold set, total member ordering, precision, uncertainty and open-endedness policy), and define a versioned dispute-and-absence policy with per-member status. (D-D1, D-D2, D-D3)
12. Close member-mastership leakage on all routes and enforce the seam: disclosure and licence dominance, retention tombstones over dangling memberships, weakest-corroboration propagation, no perimeter change authority, no inferred member attributes; file the second held amendment demoting WM-ORG-001's control endpoints and `record-control-relationship` write path to regenerable projections, and declare the seam blocked until both amendments are approved. (D-E1, D-E2, C-04, C-11)
13. Declare three-level stewardship (member, relationship, perimeter specification) with master, steward, authority basis and review-due, plus the profile owner. (D-E3)
14. Add the candidate-type dispositions for all five dossier types and the normative field-binding table for all eight v1 fields. (D-F8)
15. Correct the release surface: remove or reclassify IFRS and withdraw the IFRS 10 conclusion; replace the conformance loophole with a pinned-normative-text gate; enumerate all inherited base holds and add the rule that a profile's status can never exceed the weakest of its bases; record the unadjudicated split-trigger divergence. (D-F5, D-F4, D-F2, C-08, C-10)
16. Make the gate real, then evaluate it: convert the fixture set to declared intents with an execution-requirements block and per-case digests, add every fixture named in §3 including the six mandatory domain-profile walks, execute them, and only then evaluate publication — which remains refused while `fixturesExecuted` is false, while either base is non-canonical, or while any base, seam or amendment hold is open. (D-F1, D-F7, C-12)
