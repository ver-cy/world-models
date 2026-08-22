# Vercy mega-registry: architecture and delivery order

Status: working baseline, 2026-08-22. This defines the target registry; the existing 112 cards remain examples of the previous assembly.

## Decision

Vercy will maintain one federated registry, but not one inheritance tree. It has two connected planes:

1. **World models** describe things, actors, information, activities and situations. These become Vercy meta-model specifications.
2. **Interoperability entries** describe external ontologies, schemas, classifications, formats, protocols and industry bundles. They align to or implement world models; they are not automatically meta-models themselves.

Every entry declares `entry_kind`: `standalone-mm`, `mixin`, `pattern`, `view-candidate`, `external-metamodel`, `vocabulary`, `classification`, `format`, `protocol`, `extension` or `industry-bundle`. This prevents JSON, an industry vocabulary and a Court Case model from being presented as equivalent catalogue objects.

The first desired-model register contains **192 candidates**: 169 standalone models, 14 cross-cutting mixins, 6 patterns and 3 candidate views. Candidate status means boundaries may still be split or collapsed before drafting.

Machine register: [VERCY-DESIRED-MODELS-MEGA-REGISTRY.csv](VERCY-DESIRED-MODELS-MEGA-REGISTRY.csv).

## Navigation hierarchy

The catalogue descends from areas to categories and only then to models:

- `PHY` — physical world: matter, objects/products, living systems, places, built environment, Earth systems, space and flows.
- `SOC` — social world: people, organizations, polity/law, economy and civil society.
- `INF` — information and virtual world: records, data, knowledge, media, software and virtual environments.
- `ACT` — activity and situations: capabilities, actions, processes, services, projects, tasks, work orders, plans, methods, production, agreements, exchange, maintenance, healthcare, events, encounters, incidents, cyber incidents, cases and experience.
- `XCT` — cross-cutting composition: identity, ownership, access, audit, privacy, quantity, time, location, provenance, registries, security and classification.

This hierarchy is for discovery, not inheritance. Models also receive orthogonal facets: realm, ontological kind, industry, scale, identity mode, governance layer, origin, granularity and composition role. Thus Court Case can live under legal activity and still be found through government, organization, document and event searches without duplication.

## Composition and “matryoshka” rules

- `CONTAINS` — a parent instance owns child instances, for example Project contains Tasks.
- `COMPOSE` — peer models form a usable aggregate, for example Organization + Team + Position.
- `REFERENCE` — points to an independently mastered object.
- `MIX-IN` — adds reusable context without becoming the subject, for example ownership or provenance.
- `EXTEND` — a compatible specialization adds bundles, layers, findings or artifacts.
- `ALIGN` — maps a Vercy concept to an external standard or classification.
- `VIEW` — a use-case projection that does not create a second source of truth.

A candidate remains standalone only when it has its own identity and lifecycle, plausible owner/master system, independent access policy, and questions not merely a subset of its parent. Otherwise it becomes a subtype, mixin, view or bundle.

## Priority model

Priority uses seven explicit 0–1 factors:

`score = 100 × (0.30 demand + 0.20 data + 0.15 reuse + 0.15 interoperability + 0.20 feasibility) × (1 − 0.55 robotics) × (1 − 0.25 overlap)`

- `demand`: frequency/value of current AI-agent tasks.
- `data`: likelihood useful records already exist digitally.
- `reuse`: applicability across domains and other models.
- `interoperability`: value of stable IDs and external alignment.
- `feasibility`: ability to specify and populate now.
- `robotics`: dependence on physical sensing/actuation; currently penalized.
- `overlap`: risk the entry should be a subtype, view or mixin.

Initial scores are provisional portfolio estimates, not false precision. Recalibrate them later from searches, template downloads, agent requests, adopted specs and feedback.

### Delivery waves

- **Wave 0 — foundation (27):** Person, Organization, Organizational Unit, Position, Document/Record, Dataset, Event, Physical Item Instance, Product Type, Contract, Project, Task, Plan, Software Product, Message, Place/Address, Money, Payment and foundational identity/governance/time/provenance mixins.
- **Wave 1 — high current demand (33):** Team, Work Order/Ticket, Court Case, Cyber Incident, Vulnerability, Legal Instrument, Tax Obligation, Invoice, Facility, Vehicle, Health, Education, Employment, Non-human Agent, Agent Skill, ML Model Artifact and related high-value records.
- **Wave 2 — useful expansion (105):** digitally represented domain models and physical contexts useful without robotics.
- **Wave 3 — breadth (27):** deep nature, Earth, space and civilizational coverage with lower near-term agent demand or weaker digital availability.

Within a wave, complete shared dependencies first, then choose the highest-scoring model whose owner, use cases and source systems are known.

## External classifier and standard alignment

The later merge preserves authoritative identifiers/versioning while Vercy stays format- and interface-neutral:

- UN/CEFACT Core Component Library for reusable business information components.
- UN Statistics classifications for products (CPC), industries (ISIC), government functions (COFOG) and related classifiers.
- NIEM for reusable core/domain components, extensions and multiple representations.
- FIBO for finance ontology families and formal alignments.
- The existing Vercy external catalogue: 1,180 entries to normalize, classify and link.

External rows are deduplicated by stable source identity, not name. Each receives kind, publisher, authoritative URL, version, namespace, covered Vercy models, relation, format/interface bindings and review status. It becomes a Vercy spec only through explicit adoption.

## Workflow for every model

1. **Boundary:** identity, lifecycle, owner, master system, parent/children, mixins and exclusions.
2. **Questions:** what an AI agent or human needs answered, grouped by task and access role.
3. **Findings/properties:** atomic semantics, provenance, temporality, cardinality and sensitivity—not JSON/YAML/MongoDB fields.
4. **Functions:** reading, creation, amendment, deletion/retention, validation, comparison, derivation and events.
5. **Structure:** bundles, layers, findings, artifacts and serial artifacts.
6. **Alignment:** classifications and standards through typed `ALIGN`/`REFERENCE` relations.
7. **Packaging:** `Agents.md`, canonical YAML instruction, version links, patch rules and selectable format/interface templates.
8. **Verification:** representative questions, permissions, round-trip packaging, migrations and bootstrap from `Agents.md` alone.

Ready means: owner archetype, three real AI use cases, master sources, parent/child decision and external shortlist. Done means: reviewed questions/findings/functions, full bundle/layer hierarchy, access/provenance policy, valid canonical YAML, templates, version links, catalogue card and tests.

## Next queue

Build a connected backbone rather than 27 isolated specs:

1. Identifier + Provenance + Time + Ownership/Access mixins.
2. Person + Organization + Organizational Unit + Position + Team.
3. Document/Record + Message + Dataset.
4. Project + Task + Plan + Event.
5. Product Type + Physical Item Instance + Place/Address.
6. Contract + Money + Payment + Invoice.
7. Court Case, Cyber Incident and Software Product as demanding end-to-end validation models.

The first detailed pass should be **Person**: it exercises identity, privacy, consent, roles, records and events without robotics. The second should be **Organization**, establishing ownership structure needed by most models.

## Research provenance

The candidates derive from the current 112-model catalogue, the 1,180-row external catalogue and an independent Grok review. A parallel Claude review was attempted on 2026-08-22 but returned no usable output before the local process was stopped; rerun it when access is available. The prompt, Grok output and deterministic build script are retained under the Vercy project research directory.
