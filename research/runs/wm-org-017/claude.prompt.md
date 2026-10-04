# Vercy meta-model deep-research protocol

You are independently researching one format-neutral Vercy meta-model. Your
output will be compared with another frontier model and will not be accepted
without automated and human-readable checks.

## Objective

Derive the fullest defensible context structure that an AI agent needs to
understand, create, inspect and operate the subject. Build:

`Bundle -> Layer -> Finding -> Question`

- A **Bundle** is a coherent top-level concern and groups layers.
- A **Layer** groups related context findings.
- A **Finding** is one atomic, answerable body of context; it is not a file type.
- A **Question** elicits one useful answer and declares the answer data needed.

Also identify candidate data elements, artifacts, functions, nested or sibling
model links and the Vercy service layers needed to govern the model.

## Research rules

1. Search broadly, then ground the structure primarily in authoritative sources:
   official standards and schemas, public or scientific authorities, normative
   registries and first-party technical documentation. Cite the exact URL and
   version/date. Use secondary sources only to discover omissions or competing
   interpretations.
2. Define scope, exclusions and boundaries before proposing the hierarchy. Do
   not duplicate a concept that belongs in a composable sibling model.
3. Make the model independent of storage format and access interface. JSON,
   YAML, Markdown, HTML, Git, MCP and MongoDB are projections, not semantics.
4. Every bundle, layer, finding, function and composition link must cite one or
   more `source_refs`. Do not invent source support.
5. Questions must cover the real decision and operating surface, not repeat
   boilerplate. Include identity, classification, composition, relationships,
   state/lifecycle, time, location where relevant, provenance, ownership,
   authority, constraints, process/events, measurement, evidence/quality,
   access/exceptions and interoperability where they genuinely apply.
6. A finding must have at least three distinct questions and candidate answer
   data. It must then choose exactly one representation: either declare one or
   more artifacts and set `inline_only_rationale` to JSON `null`, or declare an
   empty `artifacts` array and provide a substantive `inline_only_rationale`
   explaining why the context is purely inline/reference data. Never populate
   both artifacts and the rationale.
7. Identity priority is: authoritative master-system identifier; governed global
   identifier/IRI; UUID or ULID assigned by the adopting Dimension. A date is not
   an identifier. Time values use RFC 3339 with seconds and an explicit offset or
   `Z`; record event time and observation/ingestion time separately when needed.
8. Treat external standards as alignments. Record conflicts and do not claim
   conformance without evidence.
9. Include the mandatory `AGENTS.md` bootstrap contract even for MongoDB or MCP
   storage: Name, Type, Specification URL, Storage type URL, Interface URL and
   Processes URL.
10. Be exhaustive but falsifiable. Record unresolved boundaries, evidence gaps,
    region-specific assumptions and the most likely omissions. Never claim
    universal or metaphysical completeness.
11. Use at least six live sources, including at least four primary sources from
    at least three independent organizations. A structural node without primary
    support must be marked as a gap rather than presented as canonical.
12. The coverage checklist must contain these exact dimensions (plus any useful
    model-specific dimensions): `identity`, `lifecycle`, `relationships`,
    `temporal`, `provenance`, `ownership`, `validation`, `access`,
    `retention and deletion`, `interoperability`.
13. Treat the known-relation ledger as a strict composition and ownership
    contract, not as optional background. For an outgoing `REFERENCE` or
    `ALIGN`, the current model may carry the target reference, binding and
    subject-specific parameters, but must not reproduce the target model's
    lifecycle or operational functions. For an outgoing `EXTEND`, specialize
    only the current subject; do not duplicate generic identity, authority,
    lifecycle or conflict machinery that the relation rationale leaves in the
    target. Before returning, compare every bundle, layer, finding and function
    with every relation rationale. Move any target-owned concept to a
    composition link, `out_of_scope` or `boundary_notes` entry rather than
    modelling it locally. In particular, a reference to a runtime evaluator,
    enforcement engine or audit record never grants ownership of evaluation,
    execution, enforcement or audit-trail semantics.

## Provider focus

Take the conservative standards-led role. Stress-test model boundaries, distinguish normative requirements from common practice, search for counterexamples and reject attractive but unsupported structure. Keep the complete JSON under 52,000 output tokens: target 5-7 bundles, 10-16 layers and 20-28 well-bounded findings with 3-5 discriminating questions each; use concise descriptions and never pad the result with repetition.

## Registry context

```json
{
  "registry_id": "vr.wm-org-017",
  "record_plane": "world-model",
  "model_id": "WM-ORG-017",
  "name": "Performance Objective / Review",
  "alternate_names": "",
  "entry_kind": "standalone-mm",
  "origin": "claude-plus-gap-audit",
  "status": "candidate",
  "review_state": "boundary-review-required",
  "nav_path": "NAV.SOC.ORG.PERF",
  "domain_tags": "SOC.ORG.PERF",
  "legacy_alias": "",
  "existing_spec_ref": "",
  "parent_ids": "WM-ORG-016",
  "contains_ids": "",
  "aligned_model_ids": "",
  "purpose": "Objective, evidence, assessment and outcome lifecycle",
  "owner_or_maintainer": "the organization or authoritative register",
  "source_url": "",
  "namespace_uri": "",
  "source_version_or_year": "2026-08-22",
  "source_group": "",
  "source_category": "",
  "source_format": "",
  "composition_role": "",
  "default_link_type": "",
  "priority_wave": "2",
  "priority_score": "61",
  "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
  "priority_confidence": "low",
  "priority_rationale": "Objective, evidence, assessment and outcome lifecycle",
  "factor_demand": "0.62",
  "factor_data": "0.62",
  "factor_reuse": "0.52",
  "factor_interop": "0.66",
  "factor_feasibility": "0.68",
  "factor_robotics": "0.00",
  "factor_overlap": "0.10",
  "possible_duplicate_of": "",
  "shared_source_with": "",
  "relations_ref": "",
  "validation_flags": "",
  "provenance": "Claude independent review + systematic gap audit + Claude adversarial audit"
}
```

## Known relations

```json
[]
```

## Previous-version material (non-authoritative)

```text
No previous-version material is registered.
```

## Machine-gate preflight

Before returning JSON, verify all of these literal contract conditions. Do not
merely imply or paraphrase them:

- `service_layers.artifact_rules.identity_priority[0]` names the authoritative
  master-system identifier.
- `service_layers.artifact_rules.timestamp_rule` contains the literal terms
  `RFC 3339`, `seconds` and `offset`; it also distinguishes event time from
  observation or ingestion time when those differ.
- `coverage.checklist` explicitly includes `identity`, `lifecycle`,
  `relationships`, `temporal`, `provenance`, `ownership`, `validation`,
  `access`, `retention and deletion`, and `interoperability`.
- `service_layers.crud.delete` contains an explicit retention, disposition,
  tombstone or deletion rule for this model's own records and says which
  referenced model or adopting-Dimension policy owns execution when deletion
  itself is outside this model's boundary.
- Every bundle, layer, finding and function has been checked against every
  known-relation rationale; none owns a target model's lifecycle or operational
  evaluation, execution, enforcement or audit-trail semantics.
- Every local ID is unique and contains no date-like component; every
  `source_ref` resolves; every finding satisfies the exclusive artifact rule:
  non-empty `artifacts` with `inline_only_rationale: null`, or empty `artifacts`
  with a substantive rationale, never both; question texts are distinct.
- Use at least eight distinct question kinds, except that a `mixin` or
  `classifier` may use six when the narrower surface is justified.

## Output

Return only JSON that conforms to the supplied JSON Schema. Use stable
lower-kebab-case IDs within the model. Write canonical technical content in
clear English; preserve official names in source titles. Do not wrap JSON in a
Markdown code fence.


## Bounded split-pass override

This is one deliberately bounded part of a larger provider pass. The instructions below supersede the normal bundle/layer/finding quantity targets, but not the canonical JSON contract, evidence quality rules, or local validation requirements. Return only the assigned subject structure and do not duplicate adjacent split areas. The result must still be a complete schema-valid object.

# Enterprise publication research scope

The owner has requested deep research with Claude and Grok, followed by immediate publication of validated usable reviewable drafts. This pass is the independent Claude research of existing canonical candidate WM-ORG-017 Performance Objective / Review, linked to EM-PEO-06 in the Enterprise registry. Do not create an Employee duplicate or change neighboring Person, Employment, Membership, Work Assignment, Metric, Evidence, Compensation or Access identities.

Cover objectives, contextual performance evidence, observation versus contribution attribution, review/assessment, calibration, contest/appeal/correction, recognition, timeline and disclosure. A claim about a person must retain source, scope, assessment method, contested status and validity, not become an intrinsic permanent property. Grade is contextual to a role/position/assignment or qualification. Do not turn commit/ticket counts into productivity by definition. Small teams may use a minimal voluntary feedback profile, while complex organizations need distinct assessment actors and cross-employer boundaries.

Use primary sources and compare multiple schools: HR Open, ESCO/SFIA, SPACE original research, official performance-management guidance, and relevant access/provenance standards. Never claim a paid standard was read if only its landing page was available. Distinguish source support from proposed design and no certified conformance. Include concrete negative scenarios and what must remain unknown. English canonical model contract. Target 5-7 genuinely subject-specific bundles, 10-14 layers, 20-24 findings, 3-5 discriminating questions each, meaningful typed data elements and artifacts. Fill every required service layer per the exact provided schema. Do not exceed the scope merely to reach a count.

Acceptance scenario: a person has two employment relationships, receives positive and contested negative evidence in one assignment, participates in review/calibration, appeals an assessment and then changes employer. The corrected result preserves earlier assertions and evidence while enforcing purpose-bound disclosure. Closing employment does not erase justified retained evidence, and retention/disclosure is not universally identical across jurisdictions. Automated high-stakes employment decisions are outside the model's delegated actions.
