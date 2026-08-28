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
6. A finding must have at least three distinct questions, candidate answer data
   and at least one artifact or an explicit explanation of why it is purely
   inline/reference data.
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

{{PROVIDER_FOCUS}}

## Registry context

```json
{{REGISTRY_RECORD}}
```

## Known relations

```json
{{RELATIONS}}
```

## Previous-version material (non-authoritative)

```text
{{LEGACY_EXCERPT}}
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
  `source_ref` resolves; every finding has an artifact or a substantive
  inline-only rationale; question texts are distinct.
- Use at least eight distinct question kinds, except that a `mixin` or
  `classifier` may use six when the narrower surface is justified.

## Output

Return only JSON that conforms to the supplied JSON Schema. Use stable
lower-kebab-case IDs within the model. Write canonical technical content in
clear English; preserve official names in source titles. Do not wrap JSON in a
Markdown code fence.
