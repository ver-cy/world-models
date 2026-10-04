# Frozen Semantic Audit — EM-PEO-01 Enterprise Person and Contextual Identity

## 1. Verdict

**REVISE.** The decision is right; the artifact is not yet safe to freeze or publish. Candidate revision 2 states correct rules in prose but leaves several of them without carriers, without dispositions, and without executable fixtures — so the contour's own negative case is not yet provably closed, and three required base compositions are silently dropped.

## 2. Decision confirmation

**Confirmed: restricted PROFILE over WM-PER-001, no new identifier.**

- All four contour candidate types resolve onto existing base findings — Person → `person-identity-anchor`; NameForm → `legal-name-versioning` + `script-and-transliteration`; ContactPoint → `person-controlled-contact-point`; IdentityEvidence → `issued-identity-evidence`. No missing substance justifies a new model.
- Unrestricted reuse is correctly refused: `de-registration-time`, `de-civil-status-code`, `de-nationality-determination-status`, `de-vital-status-code` are `required: true` and presuppose a civil-registration master no enterprise adopter has. Restriction, not reuse.
- No identifier is minted anywhere in candidate rev 2 (`newIdentifier: false`, `newRuntimeId: false`, AccountBinding `identifier: null`). Correct.

**Qualification that must be fixed:** the label "RESTRICTED PROFILE" is inaccurate as drafted. The matching contract requires `schemeVersion`, `issuer`, `authorityDomainScope`, link state, authorising role and asserting system — six carriers with no base data elements. That is restriction **plus local extension**. Declare it as such with a closed extension register, and raise the missing carriers upstream as a base change request against WM-PER-001; do not let an unlabelled extension ride inside a document that claims restriction only.

## 3. Defects

### A. Person / record / account collapse

**A1 — No record-plane vs entity-plane constraint.** The base asks it directly ("Does this record denote the natural person, or a registration record about the person?"); the reservation carries `record_plane: world-model`. Candidate rev 2 has no such constraint, so a local HRIS row can be asserted as the person.
*Fix:* constraint — every local record is a record *about* a person; only the anchor denotes the person; no source row, projection or binding may be asserted as the Person.
*Fixture:* `hris-row-as-person`, negative — HRIS row asserted as Person referent → refuse, residual state: anchor unchanged, row remains a binding.

**A2 — Anchor origin class unstated; constraint 1 ambiguous.** "WM-PER-001 remains the only Person anchor" is either false or unusable: an enterprise onboarding a person with no authoritative identifier must assign a locally assigned surrogate under its own `de-domain-of-applicability`. As written it reads either as claiming the enterprise anchor *is* the civil anchor (collapse + mastership inversion) or as forbidding a local anchor (profile unusable). The base's fourth anchor question — which fallback, by whom, why the authoritative one was unavailable — is unanswered.
*Fix:* restate as one anchor per person **per declared domain**; `de-identifier-origin-class` required on the anchor, defaulting to locally-assigned-surrogate; cross-domain equivalence is a link, never identity; record why no authoritative identifier was available.
*Fixture:* `local-surrogate-anchor`, positive — no authoritative identifier → anchor created with origin class locally-assigned-surrogate, domain declared, fallback reason recorded. `surrogate-as-authoritative`, negative — local surrogate presented as an authoritative identifier or as civil identity → refuse.

**A3 — AccountBinding sits inside `profileTypes`.** It is not one of the contour's four candidate types, is declared an identifier-unassigned sibling, and is simultaneously listed as a profile type with `baseModelId: null`. That is a de-facto in-profile type with no base and no identifier.
*Fix:* remove from `profileTypes`; keep only in `deferredCandidates` with an explicit non-member marker.
*Fixture:* `accountbinding-in-profile`, negative — profile package declaring AccountBinding as an in-profile type → refuse validation.

**A4 — Account deprovisioning path untested.** `account-creates-person` covers one direction only.
*Fixture:* `account-removal-destroys-anchor`, negative — account deprovisioning archives or destroys the anchor → refuse; anchor and tombstones survive independently of accounts.

### B. Mastership inversion

**B1 — `mastership.PersonAnchor: "WM-PER-001 authority"` names a model, not an authority.** The reservation names the civil registrar for registered identity and the person for personal data via S1. A model cannot master anything.
*Fix:* three-way restatement — (i) anchor authority per declared domain (registrar where an authoritative identifier exists, otherwise the enterprise as surrogate assignor, explicitly labelled); (ii) registrar/issuer of record for registered facts; (iii) the person for the personal sphere. Name the enterprise **profile steward** as a fourth, distinct role.

**B2 — `suggested_owner` inversion unaddressed; enumeration incomplete.** Publication hold 2 covers only `candidate_master_systems`. `suggested_owner` "Руководитель HR" is the sharper inversion, and "кадровый реестр" is absent from the profile's local-bindings enumeration (HRIS, ATS, directory, LMS), so a system omitted from the list can claim mastership by silence.
*Fix:* extend the hold to `suggested_owner`; make the local-bindings clause open-ended ("any personnel, recruitment, learning, directory or registry system") rather than an enumeration.
*Fixture:* `unlisted-system-claims-master`, negative — a personnel register not named in the profile claims person mastership → refuse.

**B3 — No bar on local correction of evidence-copied registrar facts.** "Civil registrar facts remain registrar-sourced" does not forbid HRIS editing a copied legal name in place.
*Fix:* copied facts are correctable only at source and re-ingested with `de-attribute-source-ref` and `de-last-verified-time`; local edits of copied facts are refused.
*Fixture:* `local-edit-of-copied-fact`, negative — HRIS overwrites copied legal name without an upstream instrument → refuse; correction routed to source.

**B4 — Assurance and source carriers not required profile-wide.** `de-attribute-assurance-flag` is scoped to `self-declared-attributes` in the base; Claude's study required it on every projected attribute but the candidate dropped it. Without it, copied, self-declared and verified values are indistinguishable in projections.
*Fix:* require `de-attribute-assurance-flag` and `de-attribute-source-ref` on every in-profile attribute and on every disclosure.
*Fixture:* `projection-without-assurance-flag`, negative → refuse.

**B5 — Required base compositions unreconciled.** The base marks five compositions `required: true`: Organization, Address/place, Vital-event, Consent service S1, Audit service S4. `requiredDependencies` lists three unnamed, unpinned items instead, and two of the required compositions (Address/place, Vital-event) correspond to findings the profile excludes. A profile cannot silently drop a required composition.
*Fix:* add a per-composition disposition table — retained-required (Organization for issuer/relying-party/authorising role; S1; S4) or not-required-in-profile with the excluded finding named as the reason (Address/place, Vital-event).
*Fixture:* `missing-required-composition`, negative — profile omits the Organization or Audit composition → refuse.

**B6 — Work-issued channels misclassified.** `mastership.personControlled` claims all contact points. Employer-issued email and telephony are employer-controlled and reclaimed on termination; the "person-controlled and revocable" claim is false for them.
*Fix:* split contact points by controller; only person-controlled channels are subject-revocable; employer channels attach to the employment relationship, not the person.
*Fixture:* `work-email-as-person-controlled`, negative → refuse; `work-email-reclaimed`, positive — termination detaches the channel without touching the anchor or person-controlled channels.

### C. Unsafe deterministic linkage

**C1 — The deterministic tuple has no carriers.** `identifier-assignment` holds exactly three elements: `de-identifier-scheme`, `de-identifier-value-pointer`, `de-identifier-reuse-policy`. The base has **no** element for issuing authority, scheme version, per-identifier scope or identifier validity — though the finding asks about all of them. Four of the seven tuple components are unallocated, and the candidate's holds name only link state and authorising role. Absent carriers, an implementation falls back to scheme name + value — exactly the unsafe linkage the contour forbids.
*Fix:* allocate all four as profile extensions and as a base change request; state that no deterministic link may be asserted while any tuple component lacks a carrier.
*Fixture:* `tuple-carrier-absent`, negative — deterministic link asserted in a package where a tuple carrier is unallocated → refuse at schema level, not at data level.

**C2 — No validity, status or interval-overlap requirement.** The tuple accepts a revoked, expired, suspended or non-overlapping identifier on either side. Non-reassignment alone does not make a retired value a safe key.
*Fix:* both identifiers must be active, or their validity intervals must overlap, and neither may be revoked, suspended, lost or stolen.
*Fixture:* `revoked-identifier-key`, negative; `non-overlapping-validity`, negative → both refuse, proposal only.

**C3 — Pointer equality is not value equality.** The base deliberately holds values behind `de-identifier-value-pointer` so they can be withheld. Matching on pointers yields false negatives across systems and, where two records reference one shared vault entry, a false positive collapse.
*Fix:* comparison is on the resolved value under its authority; pointer identity is never sufficient and never necessary.
*Fixture:* `pointer-equality-merge`, negative → refuse.

**C4 — Biometrics not barred as a key.** Grok excluded "biometrics as merge keys"; the candidate lost it, while `identity-proofing-assurance` and `de-biometric-reference-ref` are in-profile.
*Fix:* add to constraints and to `findingSelection` out-of-profile uses.
*Fixture:* `biometric-as-merge-key`, negative → refuse.

**C5 — Proposals lack direction and asserting system.** The base `de-record-link` carries both; `proposalFields` omits them, making proposals unattributable and unreversible.
*Fix:* add `direction` and `assertingSystem` to `proposalFields`.
*Fixture:* `proposal-without-asserting-system`, negative → refuse (parallel to the existing `proposal-without-authoriser`).

**C6 — Split and reversal underspecified.** Nothing states which record retains the reference identifier after a reversed merge, or bars reissuing the superseded identifier to one of the separated persons. Reversal that reuses the key re-collapses the namesakes.
*Fix:* on split, each person receives a distinct anchor; the superseded identifier stays a resolvable tombstone and is never reassigned regardless of scheme reuse policy.
*Fixture:* `split-reuses-identifier`, negative → refuse; `merge-reversal`, positive — two anchors restored, both histories intact, tombstone resolvable, reversal decision addressable.

**C7 — Fabricated assurance can authorise elevation.** `de-assurance-level` (1, required) and `de-proofing-step-outcome` (1..n, required) are in-profile, but most enterprise persons are never proofed. Forcing a value invites a fabricated level, and a fabricated level can then authorise evidence-based confirmation.
*Fix:* make the finding conditional on an actual proofing event; define an explicit not-proofed value that can never authorise linkage, elevation or merge.
*Fixture:* `fabricated-assurance-authorises-merge`, negative → refuse; `not-proofed-value`, positive — recorded without fabrication, cannot authorise elevation.

**C8 — Script, transliteration and truncation not barred as keys.** `script-and-transliteration` is in-profile; the base's own deferred research records that no authoritative cross-script name-matching threshold was found.
*Fix:* native-script, transliterated and truncated name forms are never keys, and no threshold may be asserted.
*Fixture:* `cross-script-name-match`, negative; `truncated-mrz-name-match`, negative → both refuse.

### D. Namesake merge

**D1 — The acceptance scenario is not tested.** The contour requires "три системы, два однофамильца и смена имени дают корректные bindings; неуверенное совпадение остаётся предложением." No fixture exercises correct bindings and refusal in one case: `namesakes-three-systems` and `two-namesakes-one-change` both assert only what must *not* happen.
*Fixture:* `acceptance-three-systems`, positive — three systems, two namesakes, one legal-name change; expect exactly two anchors, at least one deterministic binding accepted on a full qualified tuple, one uncertain correspondence remaining a proposal with all `proposalFields` populated, and closed/open name intervals on the changed name.

**D2 — `name-dob-auto-merge` uses a field the profile excludes.** `birth-facts-record` is excluded at finding level, so the fixture's date of birth has no declared home.
*Fix:* declare the DOB's source in the fixture — self-declared attribute or evidence-asserted copied attribute — and confirm the refusal holds in both cases.

**D3 — Intra-system duplication untested.** Auto-merge most often occurs inside one system, not across three.
*Fixture:* `intra-system-namesake-dedup`, negative — two rows in one HRIS, same display name, no qualified key → refuse merge, proposal only.

### E. Name-history loss and history rewrite

**E1 — "where supported" is an escape hatch.** Constraint 22 permits collapsing occurrence, registration and knowledge time. Simultaneously `de-registration-time` is `required: true` with no registrar in the enterprise context — the same fabrication trap the profile correctly avoided for civil fields.
*Fix:* delete "where supported"; remap the triple for enterprise as occurrence time / asserting-system assertion time / ingestion time, and state explicitly that registrar registration time is populated only where a registrar act exists.
*Fixture:* `collapsed-time-triple`, negative → refuse; `fabricated-registration-time`, negative → refuse.

**E2 — Correction and change are not distinguished.** A typo correction recorded as a name change fabricates a former legal name; a real change recorded as a correction destroys history.
*Fix:* corrections supersede the erroneous assertion within the same interval and are never presented as former names; changes close an interval and open a new one, with the instrument required.
*Fixture:* `typo-recorded-as-name-change`, negative → refuse; `correction-supersedes`, positive — erroneous value retained for audit, not presented as current or as a former name.

**E3 — Suppression has no lawful-release path.** `former-name-default-disclosure` refuses default release, but nothing defines authorised release, so suppression is implementable as deletion.
*Fixture:* `former-name-lawful-release`, positive — stated legal obligation, named relying-party class, logged disclosure → release permitted, history intact.

**E4 — Lifecycle archiving can destroy history, and its vocabulary is unpinned.** `de-record-lifecycle-state` is required and bound to "the adopting Dimension's published state vocabulary", while inherited hold 2 forbids publishing any identity-record state vocabulary as canonical from ISO/IEC 24760-1. An in-profile required element depends on a held vocabulary.
*Fix:* declare a profile-local provisional state set marked non-canonical and bound to hold 2; state what survives archiving (anchor, name intervals, tombstones, disclosure log).
*Fixture:* `offboarding-archives-history`, negative → refuse.

**E5 — Retention versus erasure unstated.** No constraint that person-controlled data and registrar-copied data follow different retention classes, that erasure never destroys linkage tombstones or the disclosure log, and that subject-owned classes survive employment termination independently.
*Fixture:* `erasure-destroys-tombstone`, negative → refuse; `termination-retention-split`, positive — person-controlled data handled under its own class, copied facts under theirs, audit log retained.

### F. Pseudonym correlation

**F1 — Link records are not a sensitivity class.** Grok's point was lost in reconciliation: disclosing a same-as or proposed link defeats a pseudonym even when no attribute is released.
*Fix:* classify link and proposal records as a sensitivity class, excluded from default projections.
*Fixture:* `link-record-in-default-projection`, negative → refuse.

**F2 — Pseudonym-as-key untested.** `pseudonym-cross-domain` tests reuse across purposes, not use as a deterministic key.
*Fixture:* `pseudonym-as-merge-key`, negative → refuse.

**F3 — Correlatability carriers not tightened.** Rotation policy and scope are asserted in prose only; `de-correlatability-class` and `de-pseudonym-derivation` are not required per identifier in the profile.
*Fix:* require `de-identifier-origin-class` and `de-correlatability-class` on every identifier; require `de-pseudonym-derivation` wherever the class is pairwise or single-use; allocate a rotation-policy carrier or drop the claim.

### G. Contact-as-identity

**G1 — Shared and delegated channels unhandled.** A functional mailbox attached as a person-controlled contact point binds several people to one anchor.
*Fix:* shared, functional and delegated channels may never be person-controlled contact points and never contribute to linkage.
*Fixture:* `shared-mailbox-as-person-contact`, negative → refuse.

**G2 — Purpose limitation unenforceable.** `de-contact-purpose-limitation` is `0..n`; Claude's tightening to `1..n` was dropped.
*Fix:* raise to `1..n` in the profile.
*Fixture:* `contact-without-purpose`, negative → refuse.

**G3 — No staleness or reassignment rule on verification.** A recycled telephone number retains a stale verified state.
*Fix:* verification state carries a time and is invalidated on channel reassignment or failure.
*Fixture:* `stale-verified-channel`, negative → refuse use under an unexpired verification claim.

### H. Privacy over-disclosure

**H1 — Predicate preference absent.** `de-predicate-assertion` exists in the base; the profile says only "narrowest projection".
*Fix:* a derived predicate is preferred wherever it satisfies the stated need.
*Fixture:* `attribute-where-predicate-suffices`, negative → refuse.

**H2 — Disclosure logging not mandated.** Constraint 16 requires disclosures to *declare* purpose and basis but never to be logged, though the Audit service composition is `required: true` in the base.
*Fix:* every disclosure writes `de-released-attribute-set`, purpose, basis and relying-party class to the audit service; the log is readable by the person.
*Fixture:* `unlogged-disclosure`, negative → refuse.

**H3 — `sex-and-gender-recording` disposition is ambiguous.** The exclusion list says "administrative sex", which is one of three values in the finding; `de-self-identified-gender` and `de-gender-recognition-effective-date` are unallocated. Left in, they are special-category data with no code-list governance; left out silently, the profile loses the stated reason former names are sensitive.
*Fix:* per-element disposition — administrative sex and gender-recognition date out-of-profile as governed references; self-identified gender in-profile only as a person-controlled self-declared attribute under `de-special-category-flag`; keep the former-name suppression rationale explicit.
*Fixture:* `gender-recognition-date-in-hr`, negative → refuse.

**H4 — `declared-residence-pointer` is unallocated** in both studies and in the candidate. Silently in-profile, home address flows into HR projections; silently dropped, the exclusion is undocumented.
*Fix:* explicit disposition with `de-residence-kind` restricted and default-suppressed if retained.
*Fixture:* `residence-in-default-projection`, negative → refuse.

**H5 — Biometric reference pointer in-profile without handling.** See C4; also requires a special-category disclosure rule.
*Fixture:* `biometric-pointer-disclosed`, negative → refuse.

**H6 — Named projections undefined.** Fixtures refer to a "default directory projection" that the profile never defines; relying-party classes are asserted without an enumeration.
*Fix:* define the profile's projections and relying-party classes as a closed list, each with its minimum attribute set.

### I. Unsupported release claims and profile integrity

**I1 — `basePins.sourceFile` is not supported by the frozen dossier.** It asserts `publications/wm-per-001-person/spec.yaml`; the reservation's only spec reference is `models/people-groups/H1-person.md`. Two different spec locations, no reconciliation.
*Fix:* pin by digest only, or record both paths with their relationship stated; the digest is authoritative.

**I2 — Registry drift is not an enumerated hold.** `entryKindDivergence: true` (`standalone-mm` vs `entity`), `status: described-previous-version` and `review_state: migration-boundary-review` appear only inside a generic constraint clause.
*Fix:* add an explicit publication hold naming all three.

**I3 — Unpinned required dependencies are not an enumerated hold.** Three `requiredDependencies` with `modelId: null, pinned: false`, against the contour's blocking decision "выбрать immutable refs".
*Fix:* add the hold; name each dependency or delete it.

**I4 — The ContactPoint "ownership conflict held" has no in-dossier provenance.** It is residue of Grok's `WM-PER-010` / `WM-XCT-024`, neither of which exists in the frozen material — and in the frozen dossier contact points resolve **inside** WM-PER-001.
*Fix:* restate as "no contact-point sibling is pinned in this dossier; `person-controlled-contact-point` is base-held," and record the external conflict as unverified, out-of-dossier.

**I5 — `de-conformance-claim-flag` not asserted.** The base defaults it false; the profile relies on prose alone.
*Fix:* assert the flag false as a profile invariant.
*Fixture:* `conformance-flag-true-without-evidence`, negative → refuse (extends the existing `standards-conformance` case to the element).

**I6 — Fixtures are not executable and not bound to the candidate.** `expect: "refuse"` is not an assertion: no violated-invariant id, no refusal reason code, no required residual state. Constraints are an unnumbered prose array, so no constraint↔fixture traceability exists. `baseSourcePins` pins the base spec but nothing binds the fixture set to candidate revision 2.
*Fix:* number the constraints as addressable invariant ids; give each fixture `invariantIds`, `preconditions`, `expectedRefusalReason` and `residualState`; add a candidate digest to the fixture file; add a coverage matrix showing every invariant has at least one fixture and every fixture cites an invariant.

**I7 — v1 predecessor mappings not declared non-normative.** The base `limits` state "registry/v1 mappings non-normative"; PEO-01's `display_name`, `name_forms`, `identity_evidence`, `preferred_language` are all `candidate-not-normative`. The candidate handles `display_name` only.
*Fix:* one clause declaring all v1 predecessor field mappings non-normative and non-key.

**I8 — No digest in the candidate or fixture set has been verified here.** Four asserted digests (spec, synthesis, registry snapshot, twenty fixture case digests) are unverifiable from the frozen material.
*Fix:* record that the frozen audit accepted digests as declared and verified none; independent recomputation remains open.

## 4. Contradictions

1. **Restriction versus extension.** `decisionByBase: "RESTRICTED PROFILE"` against a matching contract requiring six carriers with no base elements, and a hold conceding exactly that. Restriction-only and extension cannot both hold. → Declare restriction + closed local extension register; raise a base change request.
2. **Ownership inside the frozen dossier.** Contour `suggested_owner` "Руководитель HR" and `candidate_master_systems` "HRIS, кадровый реестр, ATS, LMS" against reservation `owner_or_maintainer` "civil registrar … the person as owner of personal data via S1". → Resolve to the reservation; the contour fields are candidate lists, and `suggested_owner` denotes the profile steward only.
3. **Entry kind.** Registry `standalone-mm` versus spec `entity`. Recorded as divergence, never resolved, never held. → Hold it; adopt `entity` for profiling and mark the registry row as drifted.
4. **Publication state.** Spec `publication.status: published` versus registry `described-previous-version` / `migration-boundary-review` and `publishableCanonical: false`. Partly mitigated by `publicationStatusMeaning`; still an unreconciled pair.
5. **Contact-point home.** Grok: "reference WM-PER-010, do not absorb it." Frozen dossier: `person-controlled-contact-point` is a WM-PER-001 finding. Direct contradiction, preserved unresolved as "ownership conflict held". → Frozen dossier governs.
6. **Optional versus excluded.** Grok: civil-status, nationality, capacity and vital-event layers "stay optional for enterprise." Claude and the candidate: excluded at finding level. Optional permits registrar facts without a registrar — i.e. fabrication. → Exclusion is correct; record the rejection of "optional" explicitly so it does not re-enter.
7. **AccountBinding provenance.** Claude's study asserts EM-PEO-01 "names" account binding. The frozen contour does not: its candidate types are four, and "технические роли" are roles, not account bindings. AccountBinding is auditor-introduced. → Record it as such; it is not contour-derived and must not be treated as in-scope work.
8. **Out-of-dossier identifiers in the Grok study.** `WM-PER-010`, `WM-XCT-024` and version `0.3.0-research.1` appear nowhere in the frozen material, which carries only `source_version_or_year: 2026-08-22` and `generatedAt: 2026-08-23`. Candidate rev 2 correctly omits them; the comparison document's "explanatory only" clause must be applied to the residual "ownership conflict" too.
9. **DOB in a fixture for an excluded finding.** `name-dob-auto-merge` exercises a date of birth while `birth-facts-record` is excluded. → Declare the field's in-profile source.
10. **Hold 7 is not a contour blocker.** Inherited hold 7 concerns base prose counts; the frozen `statistics` block already matches the corrected figures (7 bundles, 14 layers, 29 findings, 14 functions — confirmed against the delivered arrays). Carrying all eight holds at equal weight obscures the three that actually bite this contour (1 CPV/ContactPoint, 2 ISO 24760 taxonomy and lifecycle vocabulary, 6 non-EU validation). → Keep all eight verbatim and undischarged, but mark blocking relevance per hold.
11. **Verdict flattening.** Grok returned "conditional fail for publication"; the comparison document reports only convergence on PROFILE. The convergence is real, the fail is about publication readiness — and this audit agrees with it. → Record both.
12. **Unnamed identity-resolution dependency.** `requiredDependencies[0]` posits external identifier and identity-resolution support while constraint 1 makes WM-PER-001 the sole anchor and the base already owns `resolve-person-reference`. → Name it or delete it.

## 5. Closed remediation checklist

1. Relabel the decision as restricted profile **plus** a closed local extension register; open a base change request against WM-PER-001 for `issuer`, `schemeVersion`, per-identifier scope, identifier validity/status, link state, authorising role, asserting system. (C1, C5, contradiction 1)
2. Number all constraints as addressable invariant ids. (I6)
3. Add the record-plane/entity-plane constraint and its fixture. (A1)
4. Restate the anchor rule as one anchor per declared domain; require `de-identifier-origin-class`; answer the base's fallback question. (A2)
5. Remove AccountBinding from `profileTypes`; mark it a non-member deferred candidate and auditor-introduced. (A3, contradiction 7)
6. Add the account-deprovisioning fixture. (A4)
7. Rewrite the mastership block as four distinct roles; extend the mastership hold to `suggested_owner`; make the local-bindings clause open-ended. (B1, B2, contradiction 2)
8. Forbid local correction of copied registrar facts; route corrections to source. (B3)
9. Require `de-attribute-assurance-flag` and `de-attribute-source-ref` on every in-profile attribute and disclosure. (B4)
10. Add a per-composition disposition table covering all five `required: true` base compositions. (B5, contradiction 12)
11. Split contact points by controller; separate employer channels from person-controlled channels. (B6)
12. Bar deterministic linkage while any tuple component lacks a carrier; add active-status and validity-overlap to the tuple; forbid pointer-equality matching; bar biometrics, pseudonyms, and native/transliterated/truncated name forms as keys. (C1–C4, C8, F2)
13. Add `direction` and `assertingSystem` to `proposalFields`. (C5)
14. Specify split and reversal: distinct anchors, non-reassignable superseded identifier, resolvable tombstone. (C6)
15. Make `identity-proofing-assurance` conditional and define a not-proofed value that cannot authorise elevation. (C7)
16. Add the combined acceptance fixture (three systems, two namesakes, one name change, one deterministic accept, one open proposal); declare the DOB source in `name-dob-auto-merge`; add intra-system dedup. (D1–D3, contradiction 9)
17. Delete "where supported" from the time-triple constraint; remap the triple for enterprise; forbid fabricated registration time. (E1)
18. Distinguish correction from change; forbid fabricated former names. (E2)
19. Define the lawful-release path for suppressed former names. (E3)
20. Declare a provisional, non-canonical lifecycle state set bound to inherited hold 2; state what survives archiving. (E4, contradiction 10)
21. Specify retention and erasure classes; protect tombstones and the disclosure log from erasure. (E5)
22. Classify link and proposal records as a sensitivity class excluded from default projections. (F1)
23. Require `de-correlatability-class` per identifier and `de-pseudonym-derivation` for pairwise/single-use; allocate or drop the rotation-policy claim. (F3)
24. Bar shared, functional and delegated channels; raise `de-contact-purpose-limitation` to `1..n`; time-bound verification state. (G1–G3)
25. Mandate predicate preference and audited disclosure logging. (H1, H2)
26. Give per-element dispositions for `sex-and-gender-recording` and `declared-residence-pointer`; handle the biometric pointer as special-category. (H3–H5)
27. Define named projections and relying-party classes as a closed list. (H6)
28. Pin the base by digest and reconcile the two spec paths. (I1)
29. Add explicit publication holds for registry drift and unpinned dependencies. (I2, I3, contradictions 3–4)
30. Restate the ContactPoint conflict as out-of-dossier and unverified; confirm `person-controlled-contact-point` is base-held. (I4, contradiction 5)
31. Assert `de-conformance-claim-flag` false as a profile invariant with a fixture. (I5)
32. Record the rejection of "optional" civil layers in favour of finding-level exclusion. (Contradiction 6)
33. Purge out-of-dossier identifiers and version strings from all downstream artifacts. (Contradiction 8)
34. Record both provider verdicts, including Grok's conditional publication fail. (Contradiction 11)
35. Declare all v1 predecessor field mappings non-normative and non-key. (I7)
36. Make fixtures executable — `invariantIds`, `preconditions`, `expectedRefusalReason`, `residualState` — bind the fixture set to the candidate by digest, and add the invariant↔fixture coverage matrix. (I6)
37. Record that no digest was recomputed in this frozen audit and that verification remains open. (I8)
38. Keep all eight inherited holds verbatim and undischarged, annotated with blocking relevance to this contour. (Contradiction 10)
39. Re-issue as candidate revision 3 with `fixturesExecuted: false` until items 1–38 are closed and the fixture set is actually executed; no publication or installability claim before then.

End of checklist.