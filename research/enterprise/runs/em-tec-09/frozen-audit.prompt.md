# EM-TEC-09 frozen semantic audit prompt

You are the sole final Claude Opus high no-tools auditor. This is exactly one frozen audit after an independent Claude study, local synthesis, and the exact visible Grok response. Do not browse, use tools, invent identifiers, claim publication readiness, reconstruct truncated text, or request another study.

Admitted evidence is limited to the initial Claude study, local synthesis, the exact visible Grok response, and the candidate artifacts appended below. Grok attempted browsing in hidden reasoning contrary to the prompt; all hidden reasoning and sources are excluded. The visible response is provider-truncated after this exact text: `Blockers. Technology, Technology Adoption, and Architecture Exception are still identifier-unassigned. Rule-to-standard reference cardinality is not`. Do not infer or reconstruct anything after it.

Audit the settled boundary and artifacts:

- Technology, Technology Adoption, and Architecture Exception are independent identifier-unassigned roots.
- Architecture Exception is the waiver master. Renewal creates a new grant.
- Architecture Standard profiles WM-KNW-012 and references WM-KNW-013 rules.
- Conformance Assessment profiles WM-ACT-034.
- ADR reuses WM-KNW-010 / WM-ACT-024 / WM-REC-010.
- Technology remains distinct from product, release, package, deployment, lifecycle, support, and local adoption.
- Adoption and conformance remain independent.
- Exception remains distinct from assessment, nonconformity, and risk acceptance.
- No runtime or model identifier is allocated.

Return:

1. Verdict on decision and artifacts.
2. Numbered material defects, each with exact deterministic remediation.
3. A single exact JSON array of additional fixtures. Every fixture must contain `id`, `target`, `kind`, `input`, `expect`, `violates`, `closesDefect`; every negative must also contain `expectedCode`.
4. Exact final counts for prior, additional, and total fixtures, split into positive and negative.
5. Freeze decision. Do not ask for or perform a rerun.


## Initial Claude study

# EM-TEC-09 — Technologies and Architecture Standards

## Verdict

Reuse/profile for three candidates, new identity for two.

| Candidate | Disposition | Basis |
|---|---|---|
| **Technology** | **New model candidate, identifier unassigned** | Independent identity and lifecycle; not a product, release or instance |
| **TechnologyAdoption** | **New model candidate, identifier unassigned** | Organization-scoped standing state with its own effective interval |
| **ArchitectureStandard** | **Profile over WM-KNW-012** (+ WM-KNW-013 by reference) | No independent identity beyond a governed normative statement |
| **ConformanceAssessment** | **Profile over WM-ACT-034** | Subject/criteria/evidence/outcome aggregate already owned |
| **ArchitectureException** | **New model candidate, identifier unassigned** | Subject, owner, expiry and revocation differ from the standard's |

WM-REC-005 is rejected as the standard master: its only spec is legacy `N6-model-and-ontology.md`, a registry of models and ontologies, not a normative standards artifact. Its registry name is misleading. WM-SFT-002 is referenced for deployed systems on the strength of prior Enterprise research only.

## Evidence

WM-KNW-012 already owns work/expression/manifestation identity, issuing authority and mandate, applicability scope, rule-slot inventory, declared precedence, **registered derogations**, lifecycle with separate in-force/efficacy/applicability intervals, and supersession — the entire surface an architecture standard needs. WM-KNW-013 owns the expression grammar, modality, severity, and an outcome vocabulary including *indeterminate* and *not-applicable*. WM-ACT-034 owns criteria binding at a pinned version, tailoring with not-applicable justification, evidence-to-criterion linkage, criterion outcomes, aggregation, conclusion with validity window, and supersession. WM-KNW-010 / WM-ACT-024 / WM-REC-010 own decision rationale, the authorized occurrence, and the fixed issued record. Nothing in the dossier owns an abstract technology or an organization's stance toward one.

## Identity/mastership

| Layer | Master |
|---|---|
| Abstract technology | Technology (unassigned) — technology radar / architecture catalogue |
| Vendor product, release lineage | WM-SFT-001 — producer catalogue |
| Component / package coordinate | WM-SFT-007 — registry of record |
| Deployed system / application | WM-SFT-002 (prior Enterprise research) — operator catalogue/CMDB |
| Standard work and expressions | WM-KNW-012 — architecture authority |
| Individual normative rules | WM-KNW-013 |
| Conformance assessment | WM-ACT-034 — assessing body |
| Adoption stance | TechnologyAdoption (unassigned) — CTO/CIO |
| Exception | ArchitectureException (unassigned) — subject system owner |
| ADR | WM-KNW-010 + WM-ACT-024 + WM-REC-010 |

Every record is source-qualified; a technology name, standard title or version string is never a key.

## Technology/product/version

Four separate identities. **Technology** is an abstract capability class (a language, protocol, database engine, runtime style) with no producer, no digest and no support contract. **Software Product** (WM-SFT-001) has a producer of record and a licence. **Release** is a version within that product's lineage, ordered under a declared version scheme. **Deployed instance** is an operator-side occurrence in an environment. One technology maps many-to-many to products; one product to many releases; one release to many instances. A product name never mints a technology, and a technology never inherits a digest.

## Adoption/lifecycle

Three orthogonal axes, three masters, never collapsed:

1. **Technology lifecycle** — upstream state (active, maintenance, end-of-life) asserted by the technology's own community; on the Technology record with asserting party and observation time.
2. **Vendor support status** — WM-SFT-001 support window and end-of-support for a *release*, vendor-asserted, jurisdictionally constrained.
3. **Local adoption** — TechnologyAdoption: organization reference, technology reference, **stage** drawn from a named stage scheme **at a declared scheme version**, effective interval with explicit start and open-or-bounded end, scope (unit, domain, platform), and a reference to the authorizing decision. No radar stage vocabulary is evidenced in this dossier; the scheme must be declared, never assumed.

A product reaching end-of-support does not change adoption stage; a hold stage does not change upstream lifecycle. Stage transitions are append-only events; prior stages stay resolvable for as-of queries.

## Standard/rules

**ArchitectureStandard** profiles WM-KNW-012: the standard work carries stable identity across dated expressions; each expression carries a **version** and an **applicability scope** (parties, target resources, governed actions, contextual conditions). Normative content sits in rule slots that bind WM-KNW-013 expressions **by reference only** — no operator or operand vocabulary is copied. Modality is explicit: an obligation, a prohibition and a *recommendation* have different enforcement levels. Supersession creates a new expression; the prior expression remains resolvable so a past assessment stays reproducible.

## Conformance assessment

Profiles WM-ACT-034. Each assessment fixes: subject reference plus pinned subject state; **criteria binding to one standard expression at one version**, with selected rules, not-applicable justifications and retained binding snapshot; declared method and coverage; **evidence** items linked to specific rules with sufficiency judgement; criterion outcomes from the bound vocabulary; aggregation model; conclusion with validity window and named decision authority. **Partial** conformance is the composite of per-rule outcomes under a declared completeness rule. **Indeterminate**, *untested* and *not-applicable* are first-class and are never coerced to satisfied or to zero. Where only a sample was assessed, any whole-system claim is an explicit extrapolation.

## Exception/waiver

Independent identity because subject, owner and lifecycle all differ from the standard's. Required: **subject** (system/application/deployment, not the standard); **derogated rules** (specific WM-KNW-013 slots under named standard expressions — possibly spanning several standards); **scope** (which instances, environments, interfaces); **granting authority**, distinct from the assessing party and from the requesting owner; **accountable owner**; bounded **expiry**; **conditions** and compensating obligations; **renewal** as a new dated grant, never an edited expiry; **revocation** as a dated event with ground. An exception authorizes continued non-conformity; it does not change the assessment outcome, does not delete the nonconformity, and is not a risk acceptance — residual risk is a separate referenced decision.

## Decision/ADR

An ADR is rationale (WM-KNW-010) + occurrence (WM-ACT-024) + issued record (WM-REC-010). It may *cause* an adoption transition, a standard expression or an exception grant, and is referenced by each; it is none of them. A technology record is a catalogue entity with no authority, no alternatives and no approver.

## Time/version/scenario

All instants RFC 3339 with seconds and explicit offset; event, observation and ingestion times separate. Milestone dates stay dates. Point-in-time resolution: given an instant, return the applicable standard expression, the assessment effective then, the adoption stage then, and any exception in force then. Scenario and as-of projections carry a scenario identifier, are read-only against baseline, and may never be cited as actual conformance.

## Acceptance scenario

Standard S, expressions v1.0 and v2.0 (v2.0 adds rule R7). Application A, assessed once against v1.0 → **conformant**. Re-bound to v2.0 → **partially conformant**, R7 violated, evidence cited. Exception X granted for R7, scoped to A, owner named, expiry set, compensating control attached → A's **effective** status is *non-conformant with exception in force*; the v2.0 assessment outcome is unchanged. At expiry, X lapses; A reverts to partially conformant with no re-assessment and no new standard version. Adoption of the underlying technology remains *adopted* throughout — three statuses moving independently.

## Invariants

1. Standard expression has a version and a declared applicability scope.
2. Assessment records evidence per criterion, or an explicit basis for judgement alone.
3. Exception has a bounded expiry and a named accountable owner.
4. Granting authority ≠ assessing party ≠ subject owner.
5. Adoption never implies conformance; conformance never implies adoption.
6. One criterion satisfied never yields a composite conclusion.
7. Indeterminate, untested and not-applicable are never coerced to satisfied.
8. Technology lifecycle, vendor support status and adoption stage are separately mastered.
9. Renewal is a new grant; expiry and revocation are dated events on the exception.
10. Superseded standard expressions and assessments stay resolvable.
11. Scenario records never mutate baseline conformance.
12. Unassigned referents are never silently promoted.

## Holds

All cited drafts are `publishableCanonical: false`; WM-KNW-012, WM-KNW-013, WM-ACT-034 and WM-KNW-010 are single-provider with visible waivers. **Contradictions:** the relations table contains no row for any of the five candidates, so every edge asserted here is unratified; WM-KNW-013 carries a *waived* outcome value and its own exception finding while WM-KNW-012 owns derogations — three models touch waiver and mastership must be fixed before implementation; WM-KNW-012's WM-KNW-013 edge is typed REFERENCE against prose saying "composition"; WM-KNW-013's parent WM-REC-006 is unregistered here. **Gaps:** access `scopes` are stated in the record plane in all four normative drafts and need a subject-plane mapping; WM-ACT-034 has no assessor competence/impartiality function and an overclaimed access dimension; WM-KNW-012 has no revocation or renewal function; no stage scheme, and no Technology/TechnologyAdoption/ArchitectureException reservation, exists in this dossier. No canonical completeness, installability or publication readiness is claimed.


## Local synthesis

# EM-TEC-09 local synthesis

## Disposition

- Propose identifier-unassigned **Technology**, **Technology Adoption** and **Architecture Exception** roots.
- Profile WM-KNW-012 as **Architecture Standard**, with individual requirements/rules referenced from WM-KNW-013.
- Profile WM-ACT-034 as **Conformance Assessment**.
- Reuse WM-KNW-010, WM-ACT-024 and WM-REC-010 for ADR rationale, occurrence and issued record.
- Reject legacy WM-REC-005 as the Architecture Standard master because its document models models/ontologies rather than normative standards.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Technology is an abstract capability class such as a language, protocol, database engine or runtime style. It is distinct from producer-owned Software Product, versioned Release, Component/Package and operator-owned deployed instance.

Technology Adoption is an organization-scoped standing state linking organization, technology, declared stage scheme/version, scope, effective interval and authorizing decision. Architecture Exception has its own subject, derogated rules, authority, accountable owner, expiry, renewal and revocation lifecycle.

WM-KNW-012 owns the standard work and versioned expressions. WM-KNW-013 owns individual normative rule expressions. WM-ACT-034 owns conformance assessment identity and evidence. ADR records remain in the decision triad.

## Technology and adoption

Technology, product, release and deployed instance retain different identities. One technology maps many-to-many to products. Product releases use their producer's version scheme. Deployments use operator-side identity. Technology never inherits producer, license, digest or deployment state.

Upstream technology lifecycle, vendor release support status and local adoption stage are separate assertions with separate authorities and schedules. Adoption stage cites a named stage scheme at a pinned version, organizational scope, effective interval and decision. A vendor end-of-support event does not silently change adoption stage.

## Standard and rules

Architecture Standard profiles WM-KNW-012. The work has stable identity; each expression has version, issuing authority, effective/applicability intervals and scope. Rule slots reference WM-KNW-013 expressions and preserve modality. Recommendation, obligation and prohibition never share enforcement meaning.

Supersession creates a successor expression and preserves the previous version for as-of assessment. The standard never owns the technology, product or assessed system.

## Conformance assessment

Conformance Assessment profiles WM-ACT-034 and pins subject state, one standard expression/version, selected rules, tailoring and not-applicable justifications. Evidence links to individual rules with sufficiency judgement. Outcome vocabulary keeps satisfied, violated, indeterminate, untested and not-applicable distinct. Aggregation and completeness rules are declared before a composite conclusion.

Adoption never proves conformance. A recommended technology may be implemented incorrectly or only partially. Sampling a component never supports whole-system conformance without explicit extrapolation and scope.

## Exception and ADR

Architecture Exception identifies the subject, exact standard expression and derogated rule set, environments/interfaces/instances in scope, granting authority, accountable owner, conditions, compensating obligations and bounded expiry. Renewal creates a new grant. Revocation is a dated event. An exception authorizes temporary nonconformity but never changes the assessment result or deletes the nonconformity. Residual-risk acceptance remains a separate decision.

ADR is a binding of WM-KNW-010 rationale, WM-ACT-024 occurrence and WM-REC-010 fixed record. It may authorize a technology adoption transition, standard expression or exception grant, but is none of those objects.

## Acceptance result

Standard S has v1.0 and v2.0; v2.0 adds rule R7. Application A conforms to v1.0. Assessment against v2.0 records R7 violated and a partially conformant result. Exception X grants a temporary derogation for R7 with owner, scope, expiry and compensating condition. The assessment remains partially conformant while the effective operational view says nonconformant with exception in force. After expiry, that exception state disappears without changing the assessment or standard. The underlying technology remains adopted throughout.

## Required invariants

1. Technology, product, release and deployment remain distinct.
2. Technology lifecycle, vendor support and adoption stage have separate authorities.
3. Adoption stage pins its scheme and version.
4. Standard expression has version and applicability scope.
5. Conformance assessment pins exact criteria and subject state.
6. Evidence is linked per criterion or absence is explicit.
7. Indeterminate, untested and not-applicable are never coerced to satisfied.
8. Adoption never implies conformance and conformance never implies adoption.
9. Exception identifies subject, exact rules, owner, authority and bounded expiry.
10. Renewal is a new grant; revocation is a dated event.
11. Exception never rewrites the assessment result.
12. Superseded standards, assessments and grants remain resolvable.
13. Scenario records never mutate baseline status.

## Holds

Technology, Technology Adoption and Architecture Exception lack registry allocations. All reused bases are non-canonical drafts or legacy boundaries. Derogation/waiver ownership overlaps WM-KNW-012 and WM-KNW-013. Relation types conflict with composition prose and no Enterprise edges are approved. No adoption-stage scheme exists. Assessment impartiality, exception renewal/revocation operations, access mappings, crosswalks and fixtures are incomplete. No installability or publication-readiness claim is made.


## Exact visible Grok response

Verdict: Conditionally sound. Technology Adoption and Architecture Exception both require independent roots; waiver mastership is resolved to Architecture Exception as the grant record. Identifiers remain unassigned. This review does not claim publication readiness.

Strongest evidence. The required separations are load-bearing. Abstract technology is not a product, release, or deployment. Upstream lifecycle is not vendor support and is not local adoption. Adoption is not conformance. A standard expression is not a rule. An exception is not an assessment result, a nonconformity, or a risk acceptance. Architecture Standard can profile WM-KNW-012 and reference WM-KNW-013 rules. Conformance Assessment can profile WM-ACT-034. ADR can reuse the WM-KNW-010 / WM-ACT-024 / WM-REC-010 triad. The exception fields named in the proposal — subject, exact rules, authority, owner, conditions, bounded expiry, renewal as a new grant — are the minimum needed to keep a waiver auditable. WM-REC-005 is legacy-only and does not model a normative standard.

Strongest counterexample. An application uses a language recommended by the standard and is claimed conformant. The claim fails. Language use is evidence for at most one rule. The same application is assessed against standard v1 and standard v2 and fails other rules in both. A temporary R7 exception covers only the named rule, the named subject, and a bounded period. After expiry the nonconformity stands unless a new grant exists. An approved R7 can exist before reassessment and remain valid after a failed retest until expiry, so it is not an assessment outcome.

Identity and mastership. Technology, Technology Adoption, and Architecture Exception need independent identity. They stay identifier-unassigned. Architecture Standard is a profile of WM-KNW-012, not a new rule root; it references WM-KNW-013 rule identities and does not own them. Conformance Assessment is a profile of WM-ACT-034. ADR is not a fourth root; it reuses the decision triad. Waiver mastership sits with Architecture Exception. Assessment records the evaluation and the nonconformity evidence and may cite the exception. Risk acceptance is a decision outcome and may authorize a grant. Neither assessment nor risk acceptance owns the waiver. Rule drafts that treat exceptions as external masters are consistent with this.

Technology, product, and version. Technology is the abstract capability or class. Product, release, and deployment instance are separate identities. A technology identity does not change because a vendor ships a release or an organization deploys an instance. Version applies to the standard and to the product release, not to the abstract technology root.

Adoption and lifecycle. Technology Adoption is an independent root. It records local selection, scope, effective period, and the split between upstream lifecycle, vendor support, and local support. The decision triad may authorize an adoption, but the adoption state persists after the decision and can change without a new decision, for example when a support window ends. Adoption does not imply conformance. Conformance does not imply adoption.

Standard and rules. The standard is the expression: scope, version, status, and the set of referenced rules. Rules keep their own identity under WM-KNW-013. A recommendation inside a standard is not a mandatory rule and is not a conformance result. Replacing a rule requires a new rule identity or a new version, not a silent edit of the standard text.

Conformance assessment. Each assessment is version-scoped and subject-scoped. One application can hold concurrent assessments against standard v1 and standard v2. A result cites the rules evaluated, the evidence, and the outcome. It does not create, extend, or revoke an exception. Partial evidence, including use of a recommended language, never aggregates to whole-system conformance.

Exception and waiver. Architecture Exception is the independent root and the waiver master. A valid grant identifies the subject, the exact rules waived, the authority, the owner, the conditions, and a bounded expiry. Renewal is a new grant with a new identity. An exception does not erase the nonconformity; it bounds permission to operate despite it. It is not an assessment, not a risk-acceptance record, and not a change to the rule.

ADR. An architecture decision record reuses the decision triad: knowledge, act, and record. It may authorize an adoption or an exception. It does not replace either root. The decision ends; the adoption state and the exception grant continue under their own identities.

Time, version, and scenario. Standard v1 and standard v2 coexist. Assessments are pinned to the version evaluated. R7 is time-bounded. Expiry restores the prior nonconformity unless a new grant is recorded. No back-dating. No extension of the same exception identity.

Scenario. Application A is assessed against standard v1 and fails rule R7 plus two other rules. It is assessed against standard v2 and fails the successor of R7 plus one other rule. A temporary exception is granted for R7 only, with named authority, owner, conditions, and an expiry date. A claims whole-system conformance because it uses the recommended language. The claim is rejected. After expiry, A remains nonconformant on R7 unless a new grant exists. The v2 assessment is unaffected by the v1 exception.

Invariants.

1. Technology identity is independent of product, release, and deployment.
2. Technology Adoption is an independent root, not a role on Technology and not only a decision.
3. Architecture Exception is an independent root and the waiver master.
4. Assessment profiles WM-ACT-034 and does not own exceptions.
5. Standard profiles WM-KNW-012 and references, but does not own, WM-KNW-013 rules.
6. ADR reuses the decision triad and does not replace adoption or exception.
7. Adoption does not imply conformance; conformance does not imply adoption.
8. One subject may have concurrent assessments against different standard versions.
9. Recommended-language use is evidence for at most one rule.
10. An exception names subject, exact rules, authority, owner, conditions, and bounded expiry.
11. Renewal is a new grant, not an extension of the same identity.
12. Expiry ends the grant; the nonconformity stands unless a new grant exists.
13. An exception may precede or outlast the assessment that cited it.
14. WM-REC-005 is not used as a normative standard.

Minimum model set. Technology; Technology Adoption; Architecture Standard as a profile of WM-KNW-012 referencing WM-KNW-013; Conformance Assessment as a profile of WM-ACT-034; Architecture Exception; ADR as a reuse of the decision triad. Product, release, and deployment remain outside the technology root. Risk acceptance remains a decision outcome, not the waiver master.

Blockers. Technology, Technology Adoption, and Architecture Exception are still identifier-unassigned. Rule-to-standard reference cardinality is not


## Technology allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-TEC-09","proposedName":"Technology","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An abstract technical capability class remains identifiable independently of vendor products, releases, packages and deployments.","versionIdentity":"Changes to canonical capability definition or classification append a successor definition version.","independentLifecycle":["proposed","recognized","active","deprecated","obsolete","superseded","retired"],"mastership":"enterprise technology taxonomy authority"},"boundary":{"owns":["technology identity","abstract capability definition","technology classification","upstream lifecycle assertions","successor and equivalence assertions","taxonomy history"],"references":[{"target":"WM-SFT-001","purpose":"Software product boundary"},{"target":"WM-SFT-009","purpose":"Release boundary"},{"target":"WM-SFT-010","purpose":"Runtime and deployment boundary"},{"target":"WM-KNW-012","purpose":"Architecture standard"}],"excludes":["vendor product","producer release","component or package","deployed instance","license","local adoption state"]},"objects":{"Technology":{"identity":["technologyId"],"required":["name","definition","ownerRef","status"],"optional":["classificationRefs","successorRef"]}},"invariants":["Technology and product remain distinct.","Technology and release remain distinct.","Technology and deployment remain distinct.","One technology may map many-to-many to products.","Vendor versions never become technology identity.","Technology never inherits producer or license.","Technology never inherits artifact digest.","Upstream lifecycle is separately sourced.","Local adoption does not mutate upstream status.","Equivalence requires governed assertion.","Retirement preserves historical mappings.","Missing lifecycle evidence remains unknown."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## Technology profile candidate

{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-TEC-09","name":"Enterprise Technology Standards and Exceptions","decision":"PROFILE","newRuntimeId":false,"bases":["WM-KNW-012","WM-KNW-013","WM-ACT-034","WM-KNW-010","WM-ACT-024","WM-REC-010"],"constraints":["Architecture Standard profiles WM-KNW-012 and references WM-KNW-013 rules.","Conformance Assessment profiles WM-ACT-034 and pins exact criteria and subject state.","ADR reuses the rationale, occurrence and issued-record triad.","Adoption never proves conformance and conformance never proves adoption.","Exceptions never rewrite assessments or standards."]}


## Technology fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Technology","cases":[{"id":"multi-product","kind":"positive","input":"One protocol is implemented by several products.","expect":"The technology remains one abstract capability with external product mappings."},{"id":"upstream-deprecation","kind":"positive","input":"A technology is deprecated upstream.","expect":"The sourced lifecycle changes without mutating local adoption."},{"id":"successor","kind":"positive","input":"A successor protocol is recognized.","expect":"Both identities and the successor assertion remain resolvable."},{"id":"product-collapse","kind":"negative","input":"A vendor product is used as technology identity.","expect":"The conflation is rejected."},{"id":"deployment-state","kind":"negative","input":"A deployment outage marks the technology obsolete.","expect":"The inference is rejected."},{"id":"license-inheritance","kind":"negative","input":"The technology inherits one product license.","expect":"The inheritance is rejected."}]}


## Technology validation policy

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## Technology Adoption allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-TEC-09","proposedName":"Technology Adoption","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An organization-scoped standing adoption state remains identifiable independently of the technology, products and authorizing decisions.","versionIdentity":"Stage, scope, effective interval or authority changes append successor adoption episodes.","independentLifecycle":["proposed","trial","approved","preferred","restricted","deprecated","prohibited","retired"],"mastership":"enterprise technology governance authority"},"boundary":{"owns":["technology-adoption identity","organization and scope binding","stage scheme and version binding","effective intervals","decision and authority binding","successor history"],"references":[{"target":"WM-ORG-001","purpose":"Organization scope"},{"target":"WM-REC-010","purpose":"Authorizing decision"},{"target":"WM-KNW-012","purpose":"Architecture standard"},{"target":"WM-ACT-034","purpose":"Conformance assessment"}],"excludes":["technology definition","vendor support status","product or release","deployment instance","conformance result","standard definition"]},"objects":{"TechnologyAdoption":{"identity":["technologyAdoptionId"],"required":["organizationRef","technologyRef","stageSchemeVersionRef","stage","scope","validFrom","decisionRef"],"optional":["validTo","supersedesRef"]}},"invariants":["Every adoption pins one organization and technology.","Stage pins a named scheme and version.","Scope and effective interval are explicit.","Each transition requires authority and decision.","Upstream lifecycle and local stage remain separate.","Vendor support and local stage remain separate.","Adoption never implies conformance.","Conformance never implies adoption.","Product use does not silently create adoption.","Transitions append successor episodes.","Historical stages remain resolvable.","Missing stage evidence remains unknown."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## Technology Adoption fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Technology Adoption","cases":[{"id":"trial","kind":"positive","input":"One business unit trials a technology.","expect":"The scoped stage is recorded independently."},{"id":"preferred","kind":"positive","input":"A decision promotes adoption to preferred.","expect":"A successor episode records authority and effective time."},{"id":"vendor-eos","kind":"positive","input":"Vendor support ends while local use continues.","expect":"Support and adoption states remain separate."},{"id":"implicit-conformance","kind":"negative","input":"Preferred status is treated as proof of conformance.","expect":"The inference is rejected."},{"id":"floating-scheme","kind":"negative","input":"A stage lacks its scheme version.","expect":"The adoption is rejected."},{"id":"silent-transition","kind":"negative","input":"Vendor status silently changes local stage.","expect":"The transition is rejected."}]}


## Technology Adoption validation policy

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## Architecture Exception allocation candidate

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-TEC-09","proposedName":"Architecture Exception","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A bounded authorization to derogate exact architecture rules remains identifiable independently of standards, assessments and risk decisions.","versionIdentity":"Renewal is a new grant; scope, condition or authority changes never overwrite an effective grant.","independentLifecycle":["requested","reviewed","granted","effective","expired","revoked","renewed","closed"],"mastership":"authorized architecture governance authority"},"boundary":{"owns":["architecture-exception identity","subject and exact derogated rules","scope and environments","granting authority and accountable owner","conditions and compensating obligations","bounded validity","renewal and revocation history"],"references":[{"target":"WM-KNW-012","purpose":"Standard expression"},{"target":"WM-KNW-013","purpose":"Derogated rules"},{"target":"WM-ACT-034","purpose":"Conformance assessment"},{"target":"WM-REC-010","purpose":"Grant decision"},{"target":"WM-KNW-015","purpose":"Residual-risk boundary"}],"excludes":["standard definition","rule expression","conformance result","risk acceptance","ADR rationale","permanent standard amendment"]},"objects":{"ArchitectureException":{"identity":["architectureExceptionId"],"required":["subjectRef","standardVersionRef","ruleRefs","scope","ownerRef","authorityRef","validFrom","validUntil","status"],"optional":["conditions","compensatingObligations","renewalOfRef","revokedAt"]}},"invariants":["Each exception pins one exact standard expression.","Derogated rules are enumerated.","Subject and scope are explicit.","Granting authority and owner are distinct roles.","Validity is bounded.","Renewal creates a new grant.","Revocation is a dated event.","Expiry never deletes history.","An exception never rewrites assessment outcome.","An exception never amends the standard.","Residual-risk acceptance requires a separate decision.","Missing exception evidence never implies authorization."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## Architecture Exception fixtures

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Architecture Exception","cases":[{"id":"bounded-grant","kind":"positive","input":"A rule derogation is granted for one application and environment until a fixed date.","expect":"Subject, rule, scope, owner, authority and expiry are retained."},{"id":"renewal","kind":"positive","input":"A valid grant is renewed with new conditions.","expect":"A new linked grant is created."},{"id":"expiry","kind":"positive","input":"The grant expires.","expect":"Operational exception state ends while history remains."},{"id":"assessment-rewrite","kind":"negative","input":"The grant changes violated to satisfied.","expect":"The rewrite is rejected."},{"id":"unbounded","kind":"negative","input":"A grant has no expiry or accountable owner.","expect":"The grant is rejected."},{"id":"risk-collapse","kind":"negative","input":"The grant is treated as residual-risk acceptance.","expect":"The conflation is rejected."}]}


## Architecture Exception validation policy

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}

