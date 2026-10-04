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
