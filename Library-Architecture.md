# Library architecture: the world-model catalogue

> **Status:** DRAFT v0.2 (2026-08-03). Companion register: [`world-models.csv`](world-models.csv). Model cards: [`models/`](models/).
> Published by the [Vercy](https://ver.cy) project as a vendor-neutral, standalone library. It is bound to no product, no platform and no government program; any Dimension may adopt any subset of it.

## 1. Purpose and stance

This catalogue answers one question: **which meta-models are sufficient to describe, at instance level, the world of people and what happens on planet Earth**, in a form any Vercy-conformant Universe can adopt. Land and rivers, buildings and grain, machines and software, people and households, organizations and contracts, actions and accidents, registries and flows.

Three commitments shape it:

1. **Breadth first.** 112 meta-models across 15 clusters, each scoped in one line in the register and described in its own card. It is far cheaper to split or deepen a model later than to discover a missing continent of reality.
2. **Assembly, not authorship.** Nearly every model binds existing external standards (LADM, GS1, IFC, FHIR, CIM, DCAT, W3C ORG, schema.org, ISO suites and others) through the composition mechanisms of the standard (EXTEND, REFERENCE, COMPOSE, MIX-IN, ALIGN per Meta-Model-Composition). The catalogue models the connective tissue: identity, ownership hooks, events, contracts and projections.
3. **Ownership and access are architecture, not policy.** Every meta-object has an owner, and nothing is readable without the owner's permission. Security, ownership and access form a first-class cluster (S) whose models are referenced by every other cluster.

## 2. How each model is described

Every model is one card in `models/<cluster>/<ID>-<slug>.md`, described per the Vercy standard (MMAS) with **its own set of bundles and layers**:

- a **Manifest** block (MUIF): identity (`vercy:world:<id>`), canonical semantic name (`world.<name>`), version, declared conformance (MMAS level A1, Structured), namespaces, bundles with layers, external imports;
- **Bundles and layers**: the model's own composition hierarchy, designed from its subject matter, never a copied template;
- the five semantic primitives: **Objects**, **Relationships**, **Events**, **Contracts**, **Projections**;
- **Composition**: how the model references, extends or composes sibling models and external standards;
- **Stewardship**: the neutral owner archetype (registrar, steward, operator, the person) whose permission gates every read.

Cards are at maturity **A1 (Structured)**: identity, structure and primitives are declared; full packaging (per-model repositories, schemas, validation assets) is a later maturity step, model by model, on demand.

## 3. The cluster map

| Cluster | Prefix | Models | Scope |
|---|---|---|---|
| Planet & Nature | P | 11 | Terrain, land, water, atmosphere, subsurface, flora, fauna, ecosystems, hazards, soil, space |
| Matter & Artifacts | M | 9 | Materials, physical items, goods, food, medicines, machinery, vehicles, devices, heritage |
| Built Environment | U | 7 | Buildings, premises, infrastructure networks, settlements, utility points, construction, addressing |
| Activity & Work | K | 12 | Capabilities, acts, processes, services, projects, methods, plans, production, agriculture, extraction, maintenance, care |
| Knowledge & Information | N | 12 | Documents, reports, datasets, software, media, models, messages, identifiers, language, statistics, time, IP |
| Organizations | O | 7 | Organizations, units, employment, mandates, commercial contracts, labor market, procurement |
| Registries & Ledgers | R | 6 | The registry pattern, ledgers, event registers, identity registers, attestations, registry federation |
| Flows & Resources | F | 9 | Energy, money, logistics, water and food supply, waste, emissions, mobility, credit, communications |
| Events & Phenomena | X | 5 | Occurrences, observations, incidents, situations, encounters |
| Security Ownership & Access | S | 8 | Ownership and stewardship, access contracts and consent, disclosure policy, audit, privacy floors, verification, enforcement, cyber integrity |
| Polity | A | 10 | Lawmaking, offices, registry mandates, elections, permits, treaties, borders, defense, offense and enforcement, adjudication |
| Society | B | 5 | Personal health, personal property, life events, social provision, public health |
| Economy | C | 2 | Price and valuation, insurance and risk pooling |
| Civilization | D | 5 | Sport, religion, tourism, public discourse, norms and customs |
| People & Groups | H | 4 | Person, household and family, groups and communities, education and qualifications |

The machine register [`world-models.csv`](world-models.csv) is the authoritative row set; a card exists for every row.

## 4. Conventions

- **IDs** are stable (`P2`, `K8`, `H1`, ...) and never reused.
- **CSNs** follow `world.<lowerCamelName>` with bundle and layer segments beneath (`world.landParcelAndCadastre.tenure.rightsAndRestrictions`).
- **Statuses** in the register: `described` (card exists at A1), `deepened` (a richer specification or package exists somewhere, referenced from the card), `retired`.
- **Owner archetypes** are generic roles, not institutions of any particular polity.
- Cross-model references use CSN plus ID; ownership and access always route through S1/S2, audit through S4.

## 5. Adopting the catalogue

Take one model, one cluster or the whole library: vendor the repository at a pinned ref into your Dimension's `imports/`, keep the IDs and CSNs for federation compatibility, bind your own doctrine and policy where the cards leave stewardship generic, and register your adoption in your own Universe. Two Dimensions that both speak these CSNs can map their worlds to each other through them.
