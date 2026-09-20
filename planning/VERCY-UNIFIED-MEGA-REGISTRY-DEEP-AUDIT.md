# Vercy unified mega-registry: deep audit

Status: candidate baseline, 2026-08-22. “Complete” here means broad, benchmarked and continuously testable—not a claim that a finite registry can exhaust every possible concept.

## Audited result

The unified registry contains **1,581 entries**:

- **401 subject/world-model entries**: 347 standalone candidates, 33 mixins, 12 patterns, 5 views, 1 extension, 1 subtype profile and 2 categories awaiting completed splits;
- **1,180 interoperability entries**: external semantic models, metamodels, standards, classifications, identifiers, profiles, formats and protocols.

The previous 112 cards remain traceable through clean `legacy_alias` codes and `existing_spec_ref`. The 192-model Grok synthesis is retained; 209 additional candidates come from Claude's reviews and the domain-by-domain gap audit.

Artifacts:

- `VERCY-UNIFIED-MEGA-REGISTRY.csv` — canonical machine candidate registry;
- `VERCY-MODEL-TAXONOMY.yaml` — planes, navigation, facets and relation vocabulary;
- `VERCY-MODEL-RELATIONS.csv` — first 108 typed composition/matryoshka relations;
- `VERCY-BENCHMARK-COVERAGE.csv` — cross-check against 41 authoritative model/classifier families;
- `VERCY-WORLD-MODEL-SIMILARITY-REVIEW.csv` — lexical boundary-review queue;
- `VERCY-UNIFIED-MEGA-REGISTRY-AUDIT.json` — reproducible machine audit;
- `VERCY-TOP-50-DELIVERY-SEQUENCE.csv` — dependency-aware first implementation sequence.

## Nine audit passes

### 1. Source reconciliation

Inputs were separated by provenance instead of overwritten:

- current 112-model library;
- Grok's 192-candidate top-down registry;
- Claude's independent 144-model proposal and gaps;
- the current 1,180-row external catalogue;
- a systematic pass over daily AI workflows and domain benchmarks.

Result: all old model IDs are represented. Twenty-four old entries legitimately map to multiple new candidates because the old card combined lifecycles—for example Weather/Climate, Software Product/System, Employment/Membership, Money/Payment and Cyber Integrity/Vulnerability/Incident Response.

### 2. Ontological coverage

Coverage was checked for continuant-like entities, agents, information objects, events, processes, states, relationships, roles, contracts/rules, measurements and collections/views. Major gaps found and added include:

- observation/measurement, type-level engineering BOM and inventory position;
- interpersonal and inter-organizational relationships, roles and assignments;
- claim, evidence, decision, goal, policy, risk, issue, assumption and dependency;
- form, application, decision record, minutes, log and configuration record;
- lifecycle, version, quality, obligation, proof, retention and same-as mixins.

### 3. Physical-world coverage

Physical coverage now descends through matter → product type/design/configuration → item/assembly/handling unit → site/facility/premises → infrastructure/network/flows. Nature descends through taxonomy/organism/population/ecosystem and genome/sequence/gene/protein/phenotype, plus Earth, ocean, climate and space.

The registry intentionally does not create separate core models for every species, commodity, vehicle type or manufactured class. Those belong in taxonomies or extension profiles aligned through CPC, HS, UNSPSC, IEC CDD and domain classifications.

### 4. Social/institutional coverage

New coverage includes legal registration, establishment/branch, stakeholder, customer/supplier relationship, work assignment, governance body, jurisdiction, administrative case, filings, evidence, judgment, sanction, enforcement, immigration, customs, property right, financial account/transaction/position/statement, orders, fulfilment, returns, CRM opportunity, advertising, grants, payroll, tax filing, ESG disclosure and insurance claims.

Court Case is no longer a single opaque record: it can contain filings and evidence, produce judgments, and reference sanctions/enforcement without forcing all jurisdictions into one storage schema.

### 5. Information/software/AI coverage

The information plane now covers records and forms; data contracts, pipelines, lineage and quality; semantic claims and decisions; media renditions; packages, builds, deployments, SBOMs, changes, defects, tests and telemetry; and a separate AI lifecycle:

`AI System → AI Agent / Model Artifact → Prompt/Configuration → Training or Agent Run → Evaluation → Governance Assessment`.

This corrects the prior conflation of a conceptual Model/Ontology, trained model artifact and deployed AI system.

### 6. Activity/lifecycle coverage

Operational additions include meeting, communication, program/portfolio, initiative, milestone, change request, review/audit, assessment, research study, recruitment, onboarding, incident response, recovery, publication, clinical observation, procedure, medication administration, care plan, compliance, tax processing and pipeline runs.

The audit deliberately keeps subject and process separate where owner/lifecycle differ: Insurance Claim vs Claim Handling; Cyber Incident vs Incident Response; Court Case vs Judgment; Dataset vs Pipeline Run; AI Model Artifact vs Training Run.

### 7. External interoperability audit

The external plane is normalized into nine initial kinds:

- 82 external metamodels;
- 134 semantic/information models;
- 124 vocabularies/classifications;
- 48 identifier schemes;
- 46 application profiles;
- 113 frameworks/methods;
- 145 protocols/interfaces;
- 332 formats/schema mechanisms;
- 156 other standards pending finer typing.

Status normalization yields 975 active/published, 60 draft/proposed, 45 legacy/superseded and 100 unverified entries.

Important correction: 42 rows share an authoritative landing URL with another row. This does **not** prove duplication; several publishers expose a family of distinct standards on one page. These are marked `shared_source_with`, never auto-merged. No exact Name+Maintainer duplicate currently exists.

Only ten external groups have detailed model-ID alignments in this pass; all 37 groups have domain-level alignment. The remaining per-entry alignment is a large follow-up job and must not be presented as finished.

### 8. Boundary and duplicate audit

The current lexical pass produced 16 review pairs. Most are valid different lifecycles despite similar names: Employment/Deployment, Situation/Simulation, Insurance Claim/Claim Handling, Decision Record/Decision Activity.

Two real corrections were already made:

- duplicate Party Role candidates were collapsed into cross-cutting `WM-XCT-023`;
- Measurement was split and renamed into subject record `WM-MAT-008 Observation / Measurement Record` and reusable fields `WM-XCT-025 Observable Result Fields`.

Remaining high-risk boundary areas:

- Act / Event / Encounter / Interaction / Situation;
- generic Case/Ticket vs Administrative Case vs Court Case vs Investigation;
- Document/Record vs specialized forms, evidence, filings and decisions;
- Creative Work vs Media Asset vs Publication/Edition;
- Product Type vs Configuration vs Offer vs Item;
- Money/Payment/Transaction/Account/Position;
- Dataset/Data Product/Catalog Entry/Knowledge Graph;
- Software Product/System/Component/Deployment;
- AI System/Agent/Model Artifact/Run;
- Disease/Condition vs Diagnosis/Observation vs Encounter/Episode.

Every one of the 347 standalone candidates must pass the six-part gate before specification work: independent identity, lifecycle, owner, master system, access boundary and non-subset questions. Failure changes its kind to subtype, view, extension, mixin or bundle; it is not silently deleted.

### 9. Priority audit

Priority is based on AI demand, digital data availability, reuse, interoperability and feasibility, penalized for essential robotics and likely overlap. Physical models are not penalized when useful digital records already exist.

The numeric score is still cohort-derived, not a per-model measurement. Every row now declares `priority_method` and `priority_confidence=low`; it must be recalibrated using model-specific expert judgment, catalogue searches, agent queries, template downloads, implementations and user feedback. `VERCY-TOP-50-DELIVERY-SEQUENCE.csv` is therefore the reviewed delivery order and is more actionable than sorting the provisional score.

## Corrections accepted from the adversarial Claude audit

- restored `described-previous-version` plus `existing_spec_ref` for rows derived from the 112 existing cards;
- cleaned `legacy_alias` down to real legacy codes;
- expanded flat `NAV.XCT` into 38 stable subpaths;
- populated `contains_ids`, relation roles and `relations_ref` from the typed relation register;
- explicitly marked cohort-based priority as low-confidence instead of presenting it as measured analysis;
- collapsed duplicate Dependency candidates into `WM-XCT-037`;
- separated the former Credit/Security and Border/Customs/Migration categories into explicit child candidates;
- added Clinical Specimen, Biobank, Archival Fonds, AI Incident Report, Content Provenance Credential, Research Subject and Satellite Mission gaps;
- resolved API and Online Account as deliberate KEEP-BOTH boundaries, and retyped unresolved category/view/subtype candidates.

## Machine validation

The build currently verifies:

- 1,581 unique registry IDs;
- 401 unique world-model IDs;
- 137 current rows trace to 112 already described previous-version cards through `existing_spec_ref`;
- no missing required world names or navigation paths;
- no unresolved declared parent IDs;
- no flat `NAV.XCT` paths remain;
- 108 relation rows with no unresolved source/target model IDs;
- all external entries have source URLs;
- all 37 external groups map to at least one domain;
- all 50 delivery-sequence IDs exist and are unique.

## Known limitations and mandatory next audits

1. **Candidate inflation:** 347 standalone candidates are intentionally over-inclusive. Boundary interviews will reduce this number.
2. **Facets not populated row-by-row:** the facet vocabulary is defined, but realm/kind/identity/governance/granularity/mastership/sensitivity values still need assigning to every world model.
3. **External typing is heuristic:** the first kind is inferred mainly from the source `Category`; 156 generic standards and 100 unverified statuses require manual verification.
4. **External alignment is shallow:** domain coverage is complete, entry-to-model alignment is not.
5. **Relations are illustrative, not exhaustive:** 108 high-value edges establish semantics but do not yet describe all matryoshkas.
6. **No question inventory yet:** model existence has been reviewed, but the Questions → Findings → Functions test must still determine final boundaries.
7. **Version truth changes:** active standards and classifications require scheduled source checks; registry completeness is always relative to an `as_of` timestamp.
8. **Language:** canonical names are currently English; multilingual labels/definitions should be added without changing stable IDs.

## Acceptance rule

This baseline may be called the “most complete Vercy candidate registry so far.” It should not yet be marketed as a complete set of finished specifications. A model moves from `candidate` only after questions, findings, functions, owner/mastership, access policy, composition, external alignment and canonical YAML have been reviewed.

The next work item is the first model in the sequence, `WM-XCT-011 Identifier Scheme`, followed by Provenance and Time. The first subject model is `WM-PER-001 Person`.
