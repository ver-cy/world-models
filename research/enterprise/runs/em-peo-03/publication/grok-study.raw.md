**Verdict.** Accept with conditions. Decide: complete reserved **WM-PER-009** as definition-only scheme-scoped Skill and Competency (A, B); keep **Proficiency Scale** and **Person Capability Assertion** as identifier-unassigned roots (C, D); profile Competency Assessment on **WM-ACT-034** (E, conditional); reuse **WM-PER-008**, **WM-XCT-017**, and the **WM-PER-013** licence profile (F, conditional); allocate no identifier (G). Not publication-ready. No new identifier is assigned.

**Strongest evidence.** The reserved root already exists and the neighbouring drafts already cover qualification, licence, assessment act, attestation/credential, position, person, and AI-agent instruction. Completing 009 as definitions, and only definitions, closes the stated spec gap without colliding with those drafts. Identifier-unassigned Scale and Assertion roots preserve the required separations without consuming reserved space.

**Strongest counterexample.** A single “skill record” that stores ESCO code, SFIA level, course completion, licence expiry, and “current expert” on one object. That record would infer expert proficiency from a course, treat an expired certificate as current competence, and collapse ESCO/SFIA/local by identity rather than by versioned lossy mapping. The proposal fails if drafting recreates that object on 009 or on the reused artefacts.

**Identity / mastership.** Definition identity is `(scheme, scheme-local-code, definition-version)`. Label, occupation, role, and person are not identity. Scheme owner remains master of imported ESCO/SFIA definitions; the enterprise masters only local-scheme definitions and enterprise mapping records. Import copies a reference; it does not transfer mastership. Relabelling an ESCO skill as a local competency is a mapping, not an identity merge.

**Skill / competency.** Complete WM-PER-009 as two classes under one reserved root. *Skill*: scheme-scoped ability to perform a class of tasks; may be atomic; need not carry behavioural criteria. *Competency*: scheme-scoped applied capability in context, typically combining knowledge, skills, behaviours, and performance criteria. Same label across types or schemes is not the same definition. Intra-scheme composition (`includes-skill`, `related-to`, `supersedes`) is definition structure, not a holding and not a proficiency claim. Neither class embeds a default level, expiry, evidence, role expectation, or course. Spec must explicitly exclude scale levels, person, assessment, qualification, licence, credential, course, and role. Cross-scheme “equivalence” is not part of 009.

**Scales / mappings.** Proficiency Scale is an unassigned root. Scale identity is `(scale-scheme, scale-id, scale-version)`; levels belong to a version. A definition may name admissible scales; it does not own levels. ESCO, SFIA, and local scales are unlike constructs (SFIA mixes autonomy, complexity, influence, and depth; ESCO is a vocabulary with unlike annotations; local 1–5 collapses those axes). Compare only through versioned **lossy** mappings: source `(scale-version, level)` → target `(scale-version, level)`, with loss notes, authority, effective window, and a non-reversibility flag. Mapping is not identity, not equivalence, and not a person holding. Forbidden: mapping people; treating maps as reversible; transitive person inference; using a map to mint a target-scale holding.

**Person assertions.** Person Capability Assertion is an unassigned root: a dated claim that a Person stands in a stated relation to one 009 definition, optionally against one scale-version and level. Kinds are disjoint: self-assessed | assessed (points at a WM-ACT-034 profile instance) | evidence-backed | third-party-attested. Forbidden as current competence: inferred-from-role, inferred-from-course, inferred-from-expired-artefact. One person + one definition may have many assertions. Latest is not current.

**Assessment / evidence.** Competency Assessment is an act profile of WM-ACT-034, not a definition and not a holding. Payload: subject, target definition identity, method, scale-version used, result level, assessor, when, evidence refs, act validity. Same competency assessed by different methods and scales yields distinct acts. An act may justify an assertion; it is not the assertion. Self-assessment does not inherit verified status. Verified evidence is an artefact/attestation, not the act and not the holding. Condition on E: the profile must keep method, scale-used, result, assessor-type, and evidence-refs first-class and must not store a single current score per competency.

**Qualification / credential / licence.** Reuse only 008 / XCT-017 / 013. Do not mint skill-licence or competency-qualification types. These artefacts are evidence sources that may support an assertion; they are not holdings and not scale levels. Title overlap with a competency label is not claim coverage. Licence-in-force is not demonstrated proficiency on an enterprise scale. Condition on F: assertion.current requires a supporting artefact in-force at as-of whose claim covers that definition and scale-version.

**Role / course.** Role expectation is a position requirement (`definition + scale-version + level`), not a holding. Occupying the role writes nothing. Course completion may support a Qualification or Credential; it must not write proficiency, especially “expert”. “Course covers K” is a versioned lossy curriculum map, insufficient for level inference.

**Time / privacy.** Assertion, assessment, qualification, credential, and licence carry as-of, valid-from, valid-to, recorded-at. Current is a time-indexed query, not an eternal flag. Expired artefacts remain history and drop out of current-competence queries. Scores and self-assessments are personal data, purpose-limited. Do not copy proficiency into AI-agent instruction without a current verified assertion and a privacy basis.

**Governance.** Scheme owners master imported definitions. Enterprise masters local definitions, published scale versions, mapping records, assertion lifecycle, and assessment-method catalogue. Issuers master artefact validity; the enterprise must not extend expiry. Mapping stewards cannot mint identity or current holdings. Definition versioning ≠ scale versioning ≠ mapping versioning ≠ assertion supersession.

**Scenario.** Competency K, local scheme, 009. T1: self-assessment on local scale Ls v1 → assertion A1 `claimed`, not verified. T2: proctored WM-ACT-034 act on SFIA v8 → A2 `assessed` at SFIA 4; versioned lossy map Ls v1 → SFIA v8 records residual; A1 is not upgraded to expert; no merged score. T3: XCT-017 credential C cites K / SFIA v8 / 4, expires T4. T5>T4: C remains historically true; current flags on assertions supported only by C drop; role “needs K at 4” stays unsatisfied; a T0 course certificate restores neither current competence nor a higher mapped level. Reverse map Local “Proficient” → SFIA 4 is not licensed and writes no holding.

**Invariants.**
1. Skill-def ≠ Competency-def when labels match.
2. Definition identity is `(scheme, code, version)`; label is display.
3. A definition carries no person, level, expiry, or evidence.
4. Completing 009 allocates no new identifier.
5. Imported definitions remain mastered by the scheme owner.
6. Scale identity is `(scale-scheme, scale-id, scale-version)`.
7. Cross-scheme comparison exists only as a versioned lossy mapping.
8. A mapping must not create or translate a Person Capability Assertion.
9. Assessment act ≠ holding.
10. Self-assessment does not imply verified evidence.
11. One competency + two methods + two scales = two acts and up to two assertions, never one merged score.
12. Course completion must not write proficiency.
13. An expired credential/licence/qualification cannot support current competence.
14. Occupying a role never writes an assertion.
15. Current competence is time-indexed and evidence-bound.
16. Artefact title similarity is not claim coverage.

**Minimum model set.** WM-PER-009 SkillDefinition + CompetencyDefinition + Scheme; identifier-unassigned ProficiencyScale (version, levels) + ScaleMapping (lossy, versioned, non-reversible); identifier-unassigned PersonCapabilityAssertion; WM-ACT-034 Competency Assessment profile; reused WM-PER-008, WM-XCT-017, WM-PER-013; Position role-expectation link; Course-completion as activity/result only; Person. No further allocated root.

**Blockers.** 009 still has no spec — completion must stay definition-only or the reserved root will absorb holdings. WM-ACT-034 cannot be used until the profile distinguishes self vs verified vs evidence and refuses a single current score. 008/017/013 must expose issue/expiry/status and claim-to-definition binding or the expired-credential rule is unenforceable. Versioned lossy mappings have no home yet; without an unassigned mapping object they will be jammed into 009. Role and course drafts must be barred from writing `assertion.current`. Assigning an identifier to Scale or Assertion violates G and preempts reserved-space governance.