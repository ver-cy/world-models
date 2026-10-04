**Verdict.** Accept EM-LEG-02. Reuse WM-POL-001; treat ExternalRequirement and NormVersion as constrained profiles inside it, not peer roots. Profile WM-ACT-034 for applicability assessments. Reference jurisdiction externally. Allocate no new model ID.

ApplicabilityAssessment needs a new aggregate? **No.** It is a typed profile of the existing WM-ACT-034 assessment aggregate. Legal pins are mandatory associations. If ACT-034 mutates or auto-merges issued instances, fix ACT-034 to append-only peers; do not split identity out of ACT-034.

Jurisdiction needs an independently allocated model? **No.** External reference only. Not a POL-001 work, expression, or norm, and not an EM-LEG-02 master.

Accept is conditional: POL-001 must expose six distinct temporal axes, not one valid-from/to; ACT-034 must allow concurrent issued peers and forbid silent merge.

**Strongest evidence.** WM-POL-001 already masters work, expression, manifestation, source, provision, and norm identity, plus temporal applicability. WM-ACT-034 already masters assessment identity and lifecycle. WM-KNW-012 already holds internal interpretations. WM-XCT-029 already masters instantiated duties. New IDs would duplicate those masters. Market-specific readings belong on assessments, not on legal identity.

**Strongest counterexample.** Future-effective amendment with partial commencement and a transitional period. If NormVersion is a monolithic snapshot with one commencement or in-force interval, successor expression V1 cannot commence provision P1 at Tc1 and P2 at Tc2, and cannot keep prior expression V0 efficacious for product class C until Td. Second failure: ACT-034 implicit latest-wins would drop one of two market assessments.

**Identity / mastership.** POL-001 is sole master of the legal stack. ExternalRequirement is a constrained profile of an externally originated *norm identity*, bound to at least one provision of exactly one expression, and cites source/manifestation. It is not a Work and does not mint a second work id. NormVersion is a constrained profile of a POL-001 *expression* only — not a temporal slice, not a market reading, not a knowledge-time snapshot. Work identity is stable across amendment; expression changes with authentic formulation; manifestation/source with publication embodiment; provision is expression-relative. Because ExternalRequirement sits at norm layer and NormVersion at expression layer, neither may be minted per market or per assessment.

**Temporal axes.** Keep pairwise distinct, no shared field: publication/promulgation; commencement (provision-scoped); efficacy/applicability; transitional or compliance deadline; repeal/supersession; knowledge time. Also distinct from assessment facts-as-of and ACT-034 performed-at. Citability after publication does not entail efficacy. Knowledge time never writes efficacy.

**Exceptions / transitions.** Model separately, not one Exception type: source exceptions; authority-backed derogations; beneficiary-scoped exemptions; transitional periods. A transitional period binds prior expression, successor expression, scope (subject/activity/product), interval, and ending event. Interval end does not repeal the successor or erase prior identity. Derogation and exemption change scoped efficacy; they do not mint a NormVersion.

**Assessment boundary.** ACT-034 owns identity, status, assessor, performed-at, review/expiry, and explicit supersession. The profile adds immutable pins: norm expression and provisions; subject/activity/product/market state; jurisdiction ref; facts-as-of; reasoning/evidence; conclusion; confidence/limitations. KNW-012 may be cited as evidence; it must not conclude applicability or carry market or jurisdiction findings. Review/expiry is assessment lifecycle time, not norm commencement.

**Conflict handling.** No uniqueness on (expression, subject, jurisdiction, facts-as-of). Silent merge, overwrite, latest-wins, and implicit supersession are forbidden. Explicit named supersession only; prior remains queryable. Different markets are different pins, not a conflict. True conflict is overlapping pins with different conclusions; both persist.

**Jurisdiction.** Qualifier on applicability. Assessment and any POL-001 temporal record point at an external jurisdiction identifier as used at facts-as-of. Nested competence is a reference list on the assessment. Do not profile Jurisdiction through POL-001. Do not invent an external owner ID.

**Obligations / compliance.** Four separate claims: citation (POL-001) is not applicability (ACT-034 profile), obligation, or compliance. Instantiated duties only via WM-XCT-029. Assessment must not create XCT-029 instances. XCT-029 must not store applicability reasoning. Compliance is a claim against an instantiated duty, not an assessment conclusion. Obligation-claim owner is unnamed; do not fill that gap with a new EM-LEG-02 model.

**Scenario.** Same work. Amendment at Tp publishes new expression V1 (new manifestation). P1 commences Tc1; P2 commences Tc2. Transitional R: class C keeps V0 efficacious for P1-subject matter until Td. Before Tc1, V1 is citable but not efficacious. Between Tc1 and Td, P1 has commenced, R applies to C, and P2 remains uncommenced. Assessments A1 and A2 pin the same V1 and P1 for different markets, with their own reasoning and conclusions. Both live. Neither forks ExternalRequirement nor NormVersion. Pre-amendment assessments remain peers; the new expression does not auto-expire them.

**Invariants.**
1. POL-001 is the only master of work/expression/manifestation/source/provision/norm identity.
2. ExternalRequirement binds one POL-001 norm identity and at least one provision of exactly one expression; it does not mint work identity.
3. NormVersion has no identity independent of a POL-001 expression.
4. Publication, commencement, efficacy, transitional/compliance deadline, repeal/supersession, and knowledge time are pairwise distinct.
5. Commencement is provision-scoped; NormVersion shall not imply uniform commencement.
6. Citability does not entail efficacy; uncommenced provisions generate no XCT-029 duties.
7. Source exception, authority derogation, beneficiary exemption, and transitional period are distinct identities.
8. ApplicabilityAssessment identity equals WM-ACT-034 assessment identity.
9. Issued assessment pins are immutable.
10. facts-as-of, performed-at, knowledge time and every POL-001 legal time axis remain distinct.
11. Conflicting issued assessments coexist; replacement only via explicit named supersession.
12. Assessment may cite KNW-012 and must not be KNW-012; KNW-012 must not conclude applicability.
13. Citation, applicability, obligation and compliance are distinct; assessment does not instantiate XCT-029.
14. Jurisdiction is an external reference; EM-LEG-02 allocates no Jurisdiction model.
15. Market state is a pin; two markets produce two assessments.
16. Repeal/supersession does not delete assessments pinned to a prior expression.
17. Transitional interval end does not repeal the successor or erase the prior expression.

**Minimum completion shape.** ExternalRequirement profiles POL-001 norm identity and cites source/manifestation; publication/promulgation and repeal/supersession live there. NormVersion profiles POL-001 expression only, with a provision list, no commencement field and no market dimension. Provision-level commencement and repeal live on POL-001. Four exception/transition records reference POL-001 expression/provision ids. ApplicabilityAssessment profiles ACT-034 with a full immutable pin set, concurrent peers and explicit supersession only. Jurisdiction is an external ref slot with a documented key-as-of contract and no newly allocated model. Duties arise only through XCT-029 after scoped efficacy is true. Optional KNW-012 interpretation is linked from the assessment and never replaces it. Obligation and compliance remain uninstantiated here.

**Blockers.** POL-001 temporal applicability may be a single valid-from/to; profiling then cannot carry the scenario until POL-001 exposes the six legal axes and provision-scoped commencement — a completion condition, not a new model ID. ACT-034 must allow concurrent issued peers and forbid implicit merge; payload must accept structured pins, not an opaque blob. NormVersion must stay locked to expression. External jurisdiction key contract (stability, as-of) is unspecified; do not invent an owner ID. No owner for obligation-as-claim or compliance-as-claim; do not grow them on assessment or POL-001. KNW-012 versus ACT-034 dual-write rule is required or interpretations fork.
