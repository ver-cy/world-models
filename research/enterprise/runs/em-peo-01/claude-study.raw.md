## Verdict

**PROFILE over WM-PER-001**, with one dependency: the *account binding* concept EM-PEO-01 names is deliberately out of WM-PER-001's scope and cannot be profiled from it — it must resolve in a sibling contour or, if none holds it, as an **identifier-unassigned candidate**. I do not assign an ID.

Not REUSE ONLY: WM-PER-001's required elements assume a civil-registration master (registration time, civil status, nationality determination, vital status are `required: true`), which no enterprise adopter can satisfy; unrestricted reuse would force fabricated values. Not COMPLETE RESERVED MODEL: the four candidate types (Person, NameForm, ContactPoint, IdentityEvidence) already resolve onto existing findings — `person-identity-anchor`, `legal-name-versioning` + `script-and-transliteration`, `person-controlled-contact-point`, `issued-identity-evidence` — so the enterprise contour adds restriction and context, not missing substance.

## Evidence

Structurally sufficient for a profiling decision; insufficient for any alignment or conformance statement. The spec is parsed and hash-pinned (252 757 B, sha256 7a4a71…), dual-provider, with an adjudication record that shows reasoned rejection of duplicates. Against that: `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, eleven open publication holds, registry `review_state: migration-boundary-review` and `status: described-previous-version`. The EM→WM link itself is `conceptual-candidate` at `index-and-publication-metadata` depth — the semantic crosswalk is asserted, not demonstrated. Registry `priority_confidence: low`. Two holds bear directly on this contour's core: the CPV version conflict (2.00 vs 2.1.2) governs whether ContactPoint attaches to Person at all in the alignment target, and the ISO/IEC 24760-1 edition conflict (2025 vs 2019) governs the entity/identity/reference-identifier vocabulary the whole matching contract leans on. Neither may be cited as settled.

## Boundary / mastership

The dossier's own fields conflict and the conflict must be resolved against the spec, not the queue row. `suggested_owner` "HR lead" and `candidate_master_systems` "HRIS, ATS, LMS" contradict the reservation's `owner_or_maintainer`: civil registrar for registered identity, the person for personal data. The profile should hold the spec's position:

- **Person anchor** — not HR-mastered. HRIS holds a *local record* linked to the anchor by `de-record-link`, never the anchor itself.
- **Legal name, birth facts, civil status, nationality, capacity, vital status** — registrar-mastered; enterprise-side these are *evidence-copied* values carrying `de-attribute-assurance-flag` and `de-attribute-source-ref`, correctable only upstream.
- **Contact points, preferred language, accessible-format need, usage name** — person-controlled and revocable (`person-controlled-contact-point`, `self-declared-attributes`).
- **Employment-context assertions, roles, accounts** — mastered by the employing organization but attached *to the relationship*, not to the person. ATS data is self-declared candidate claim, unverified by construction; LMS masters nothing identity-bearing.

Four things EM-PEO-01 asks to distinguish map as: *identity assertion* = a name/attribute claim with assurance flag and effective period; *evidence artifact* = `issued-identity-evidence` (issuer, status, asserted attribute set, holder binding); *contact point* = reachability channel with verification state and purpose limitation; *account binding* = a tie between a local system principal and the anchor — excluded here by the authenticator boundary note (`SRC-008`) and by the out-of-scope line on party/account relationships.

## Matching / linking contract

1. No attribute is a matching key on its own. `display_name` is `candidate-not-normative` in v1 and must never reach key status. Email is a `ContactPoint`: a verified contact proves *reachability and control of a channel*, never identity, and is shared, reassigned and delegated in practice.
2. Deterministic merge permitted only on a scheme-qualified identifier where `de-identifier-scheme` authority matches, `de-identifier-reuse-policy` forbids reassignment, and both records declare the same `de-domain-of-applicability`. Reuse-permitting schemes are disqualified as keys outright.
3. Everything else produces a **proposal**: `de-record-link` + `de-match-confidence` + rule-set version, resolved by a human role. The base carries confidence and link direction but has **no data element for link state (proposed/confirmed/rejected) and none for the authorising role**, though `duplicate-detection-and-merge` asks for the latter. The profile must add both; otherwise "uncertain match remains a proposal" is unenforceable.
4. Merge never destroys: superseded record survives as a resolvable tombstone via `de-surviving-record-ref`; reversal is a first-class path.
5. Evidence-based confirmation runs through `assess-identity-assurance`, producing `de-assurance-level` with expiry — not through attribute similarity.

## Names / contacts / pseudonyms

Names are time-bounded structured facts: `de-name-part`, `de-name-role`, `de-name-validity-period`, `de-name-script-code`. `record-name-change` opens a new assertion and closes the prior one; history is preserved by supersession, never overwrite. Display name is a derived presentation form, never stored as the authoritative value and never indexed for matching. The base's four name roles (birth / current legal / former legal / alias) are too coarse for enterprise usage names and pseudonyms — the profile should sub-type `alias` (usage name, professional pseudonym, system-local label) and route unverified ones through `self-declared-attributes` with `de-attribute-assurance-flag`.

A pseudonym or local identifier suffices when the purpose needs only *continuity of the same subject inside one domain* — training completion, internal directory presence, forum participation. Then `de-identifier-origin-class` = locally assigned surrogate, `de-correlatability-class` = pairwise or sector-scoped, derivation documented in `de-pseudonym-derivation`. It is never sufficient where a legal act, payroll, or evidence-bound assurance is required, and a pseudonymous identifier must never seed a merge.

## Privacy / disclosure

Purpose-bound by default: `emit-minimal-disclosure` releases the narrowest set, preferring `de-predicate-assertion` over the underlying attribute, with `de-special-category-flag` gating. Former names are the sharp case — disclosing them can reveal gender recognition, so the profile should suppress `former legal name` by default and release it only under a stated legal obligation, logged per disclosure. Consent and audit compose in as services (S1, S4); the employer declares purposes, it does not hold the grant store. Statutory HR processing runs on legal obligation, not consent, and must be labelled as such so withdrawal semantics stay honest.

## Invariants

Adopt all three, made testable: (i) *identity requires evidence* — no merge or elevation without `de-proofing-step-outcome` or a no-reuse scheme identifier; (ii) *purpose-bound disclosure* — every release logs `de-released-attribute-set` against a declared purpose; (iii) *employer is not universal owner* — subject-owned classes are person-revocable and survive employment termination independently of retention classes. Add: (iv) reference identifier is opaque and carries no attributes; (v) occurrence / registration / ingestion times stay separate (`event-time-versus-record-time`); (vi) `de-conformance-claim-flag` stays false.

## Scenarios

**Negative — auto-merge on display name.** Two records, `display_name` "Anna Ivanova", same domain. Rules 1–3 reject: no scheme identifier, display name non-normative. A confidence value may be written; no merge occurs, no surviving-record reference is set. If a shared verified email is also present, still refused — control of a channel is not identity. Blocked absent a link-state element, which is why the profile adds one.

**Acceptance — three systems, two namesakes, name change.** HRIS, directory, LMS. Namesake A changes legal name: `record-name-change` closes the old validity period and opens the new; the anchor and reference identifier are untouched; downstream systems re-resolve by identifier, not by name, so nothing breaks and the former name remains queryable but disclosure-suppressed. Namesake B is unaffected — no attribute-similarity path exists to link them. LMS holds only a local surrogate for B with pairwise correlatability; its tie to the anchor is a proposal at low confidence and stays a proposal until an authorised role confirms it against evidence. Result: three correct bindings, two distinct anchors, one open proposal.

## Profile shape

Restriction-only, no new semantics beyond the two link fields. Include: identity anchor, duplicate detection, legal-name versioning, script/transliteration, identifier assignment, identifier correlation, issued evidence, proofing assurance, contact point, self-declared attributes, lawful basis, subject rights, minimal disclosure, retention/audit, attribute accuracy, occurrence-vs-record time, record lifecycle, external alignment. Exclude at finding level (not element level, to avoid inheriting their required elements): birth facts, administrative sex, civil status, nationality, statelessness, legal capacity, representation, life-event anchors, alternative registration routes, vital status — each reachable only as a governed reference. Tighten: `de-identifier-origin-class` and `de-correlatability-class` required on every identifier; `de-contact-purpose-limitation` raised to `1..n`; `de-attribute-assurance-flag` mandatory on every projected attribute.

## Holds

Carry forward, unresolved: CPV version and whether ContactPoint attaches to Person; ISO/IEC 24760-1 edition for the identifier taxonomy and lifecycle vocabulary; GDPR Article 9 wording re-verification; source-URL liveness. Profile-specific: verify the EM→WM crosswalk beyond index metadata before treating the four candidate types as satisfied; resolve the owner/master-system contradiction in the queue row; locate or open the account-binding home; specify link state and authorising role; validate against a non-EU regime, since the base is EU/UN-weighted. No conformance or installability claim is made here.
