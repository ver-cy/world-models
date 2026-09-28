# Frozen semantic audit: EM-LND-06 Software Product Landscape

You are the single independent frozen auditor. Use only the material below and no tools. Audit the reconciled candidate after Claude/Grok boundary comparison. Do not invent identifiers or external facts.

Required output:
1. Verdict: ACCEPT or REVISE.
2. Confirm or reject COMPLETE RESERVED MODEL on existing vr.vercy.plmm, with 0.1.0-legacy immutable and no new identifier.
3. List every semantic defect that could cause duplicate identity, mutable historical meaning, false completeness, non-reproducible traversal, access leakage, or unsupported release claims.
4. For each defect, give a concise exact remediation and a fixture expectation.
5. Identify any contradictions among dossier, providers, candidate and fixtures.
6. End with a closed numbered remediation checklist. If none, say none.

Do not restate the whole model. Treat publication holds as holds, not permission to weaken semantics.

## FROZEN PROVIDER DOSSIER

```
{
  "contour": {
    "id": "EM-LND-06",
    "name": "Ландшафт программных продуктов",
    "domain": "LND",
    "kind": "landscape",
    "wave": "W1",
    "scope": "Состав, взаимодействия, ownership, критичность и эволюция ПО между продуктами. PLMM  -  кандидат, статус и версия требуют отдельного решения.",
    "candidate_types": [
      "SoftwareLandscape",
      "LandscapeMembership",
      "LandscapeDependency"
    ],
    "specific_questions": [
      "Что PLMM вправе описывать самостоятельно?",
      "Как согласовать AISMM 3.1 runtime и 3.2 README с PLMM legacy?",
      "Как строить impact по неполным сведениям?"
    ],
    "proposed_invariants": [
      "Внутренности продукта не копируются",
      "Версии зависимостей закреплены",
      "Неполнота графа видима"
    ],
    "negative_case": "Установка PLMM legacy объявлена готовым каноническим ландшафтом.",
    "acceptance_scenario": "Три продукта и общая платформа дают impact graph и вопросы о пробелах, без создания второго SoftwareProduct.",
    "comparison_tracks": [
      "Vercy composition и whole-object: отдельный объект ландшафта и делегирование",
      "ArchiMate/ISO 42010: виды, вопросы и правила представления",
      "Сравнить предметные модели участников и практическую сборку разрешённого контекста"
    ],
    "vercy_candidates": [
      {
        "model_id": "PLMM",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "boundary-reviewed",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-XCT-039",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "boundary-reviewed",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "LND-06",
        "fields": [
          {
            "name": "scope",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "architecture_state",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "as_of",
            "value_type": "datetime",
            "status": "candidate-not-normative"
          },
          {
            "name": "composition_version",
            "value_type": "text",
            "status": "candidate-not-normative"
          }
        ]
      }
    ],
    "suggested_owner": "Куратор мета-моделей Vercy",
    "candidate_master_systems": "Реестр моделей, sources.yaml, vercy.lock, политики",
    "related_research_contours": [],
    "blocking_decisions": [
      "Согласовать runtime и repository версии AISMM/PLMM и роль ELMM; совместимость сейчас не доказана.",
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "runtime_index": {
    "AISMM": {
      "id": "vr.vercy.aismm",
      "modelId": "AISMM",
      "aliases": [],
      "slug": "vercy-aismm",
      "name": "AI Software Meta-Model",
      "version": "3.1.0",
      "status": "published",
      "installable": true,
      "specUrl": "https://ver.cy/models/vercy-aismm/spec.yaml",
      "agentsUrl": "https://ver.cy/models/vercy-aismm/AGENTS.md",
      "pageUrl": "https://ver.cy/models/vercy-aismm/",
      "digest": "sha256:a60376c71032d617ef743a54307dabf477fb38b9f14b8dbe63a79b208ea0cbe5",
      "family": "Vercy examples",
      "category": "Core",
      "domain": [
        "software-engineering"
      ],
      "industry": [
        "Cross-industry"
      ],
      "tags": [
        "ai",
        "software",
        "architecture"
      ],
      "purpose": "Connected software context for AI agents and software delivery.",
      "requires": [],
      "unresolvedRequires": [],
      "relations": []
    },
    "PLMM": {
      "id": "vr.vercy.plmm",
      "modelId": "PLMM",
      "aliases": [],
      "slug": "vercy-plmm",
      "name": "Product Landscape Meta-Model",
      "version": "0.1.0-legacy",
      "status": "legacy",
      "installable": false,
      "specUrl": "https://ver.cy/models/vercy-plmm/spec.yaml",
      "agentsUrl": "https://ver.cy/models/vercy-plmm/AGENTS.md",
      "pageUrl": "https://ver.cy/models/vercy-plmm/",
      "digest": "sha256:71003d1d674f20f73732a38c3311823a19f9ad20df442a94a7a6f0a0ef4054ce",
      "family": "Vercy examples",
      "category": "Landscape",
      "domain": [
        "product-management"
      ],
      "industry": [
        "Cross-industry"
      ],
      "tags": [
        "product",
        "portfolio",
        "capability"
      ],
      "purpose": "Product landscape, portfolio and capability context.",
      "requires": [],
      "unresolvedRequires": [],
      "relations": []
    }
  },
  "plmm_runtime_spec": {
    "vercy": "1.0-draft",
    "metaModel": {
      "id": "vercy.plmm",
      "name": "Product Landscape Meta-Model",
      "version": "0.1.0-legacy",
      "family": "Vercy examples",
      "category": "Landscape",
      "industry": [
        "Cross-industry"
      ],
      "domain": [
        "product-management"
      ],
      "tags": [
        "product",
        "portfolio",
        "capability"
      ],
      "status": "legacy assembly"
    },
    "canonicalUrl": "https://ver.cy/models/vercy-plmm/",
    "structure": {
      "bundles": []
    },
    "serviceLayers": {
      "artifactFormats": [],
      "policies": [],
      "crud": {},
      "roles": []
    },
    "legacySource": "https://github.com/ver-cy/plmm",
    "migrationNotes": [
      "Findings, questions, artifacts, CRUD rules and access roles are not explicit in this legacy version."
    ]
  },
  "aismm_runtime_spec_summary": {
    "metaModel": {
      "id": "vercy.aismm",
      "name": "AI Software Meta-Model",
      "version": "3.1.0",
      "previousVersions": [
        {
          "version": "3.0.0",
          "source": "https://github.com/ver-cy/software-meta-model/blob/main/RELEASE_NOTES_v3.0.0.md"
        },
        {
          "version": "2.x",
          "source": "https://github.com/ver-cy/software-meta-model/blob/main/MIGRATION-v2-to-v3.md"
        }
      ],
      "family": "Vercy examples",
      "category": "Core",
      "industry": [
        "Cross-industry"
      ],
      "domain": [
        "software-engineering",
        "AI systems"
      ],
      "tags": [
        "ai",
        "software",
        "architecture",
        "operations",
        "governance"
      ],
      "status": "canonical legacy assembly projection"
    },
    "statistics": {
      "bundles": 13,
      "layers": 86,
      "findings": 380,
      "questions": 1537
    },
    "source": "https://github.com/ver-cy/software-meta-model"
  },
  "repository_pins": {
    "plmm": {
      "commit": "a8e388c21901540b71cc8479d4d6ef119c2ea276",
      "describe": "a8e388c",
      "last_commit": "2026-06-22T20:59:59+03:00 README: enrich from detailed PLMM spec",
      "readme": "# Product Landscape Meta-Model (PLMM)\n\n<p align=\"center\">\n  <a href=\"./LICENSE\"><img alt=\"License: Apache-2.0\" src=\"https://img.shields.io/badge/License-Apache_2.0-blue.svg\"></a>\n  <img alt=\"PLMM version 0.1.0\" src=\"https://img.shields.io/badge/PLMM-v0.1.0-1f6feb.svg\">\n  <img alt=\"Spec status: draft\" src=\"https://img.shields.io/badge/status-draft-orange.svg\">\n  <a href=\"https://github.com/orkestron-ai/software-meta-model\"><img alt=\"Federates AISMM\" src=\"https://img.shields.io/badge/federates-AISMM-7c5cff.svg\"></a>\n</p>\n\n<p align=\"center\">\n  <em>A structured, Git-native, AI-ready model of the whole product landscape — the federation layer above AISMM.</em>\n</p>\n\n## Contents\n\n- [What is PLMM?](#what-is-plmm)\n- [PLMM and AISMM](#plmm-and-aismm)\n- [Why PLMM is needed](#why-plmm-is-needed)\n- [What PLMM gives you](#what-plmm-gives-you)\n- [How PLMM is structured](#how-plmm-is-structured) · [The eleven layers](#the-eleven-layers)\n- [Layer document model](#layer-document-model)\n- [Repository-native by design](#repository-native-by-design)\n- [PLMM and AI agents](#plmm-and-ai-agents)\n- [What PLMM is not](#what-plmm-is-not)\n- [Status & roadmap](#status--roadmap)\n- [License](#license)\n\n## What is PLMM?\n\n**PLMM (Product Landscape Meta-Model)** is a structured, machine-readable and\nhuman-readable way to describe an entire **portfolio of products** as one\nconnected system.\n\nWhere [AISMM](https://github.com/orkestron-ai/software-meta-model) models a\n*single* software product in full context, PLMM models the **landscape between\nproducts**: the registry, the dependency and integration graph, shared\ncapabilities, cross-product processes, ownership and governance, and how each\nproduct's AISMM is federated into one navigable whole.\n\nIn simple terms:\n\n```text\nAISMM = full structured context of ONE product\nPLMM  = full structured context of the PRODUCT LANDSCAPE (many products + how they relate)\n```\n\nIt is designed to be stored in Git, reviewed like code, used by humans, and\ntraversed by AI agents that need to know *which* products and *which* AISMM\nmodels a task touches.\n\n---\n\n## Core model\n\nPLMM frames the enterprise as a single chain of context, from the whole\nlandscape down to a single product's full-context model:\n\n```text\nEnterprise Landscape  →  PLMM  →  Product  →  AISMM\n```\n\nEverything in PLMM is expressed with five core entities:\n\n| Entity | What it represents |\n|--------|--------------------|\n| **Product** | A business/technical asset in the landscape (identity, lifecycle, ownership). |\n| **Product Relationship** | A typed edge between products — dependency, integration, event or data flow. |\n| **Capability** | A business capability, mapped to the product(s) that own or share it. |\n| **Cross-Product Process** | A process that spans several products and the models it needs. |\n| **AISMM Reference** | A federation link from a product into its own AISMM model. |\n\n---\n\n## PLMM and AISMM\n\nPLMM does not replace AISMM — it **federates** it.\n\n```text\n            ┌──────────────────────────── PLMM ────────────────────────────┐\n            │  Product registry · graph · capabilities · processes ·        │\n            │  operations · governance · semantic routing · portfolio       │\n            └───────┬───────────────────┬───────────────────┬───────────────┘\n                    │ federates         │ federates         │ federates\n                ┌───▼───┐           ┌───▼───┐           ┌───▼───┐\n                │ AISMM │           │ AISMM │           │ AISMM │   ← one per product\n                │ prod A│           │ prod B│           │ prod C│\n                └───────┘           └───────┘           └───────┘\n```\n\n- Each product keeps its own **AISMM** (b0–b12) as the source of truth for that product.\n- PLMM holds only **landscape-level** facts and **references** into each AISMM\n  (see the [AISMM Federation layer](./07-federation/aismm-federation.layer.md)) — never a copy.\n- An agent enters at PLMM, resolves *which products and contexts* a task spans\n  (see [Semantic Routing](./10-semantic-routing/semantic-routing.layer.md)),\n  then loads the relevant AISMM models.\n\n---\n\n## Why PLMM is needed\n\nA single product is well described by AISMM. But an organization rarely has one\nproduct — it has a **landscape**:\n\n- many products and services, owned by different teams\n- dependencies, integrations, events and data flows between them\n- capabilities that are shared, duplicated or missing\n- business processes that span several products at once\n- one product replacing, extending or deprecating another over time\n- a need to know, for any change, *what else it touches*\n\nWithout a landscape model this knowledge lives in people's heads, slide decks\nand stale diagrams. PLMM makes it **explicit, versioned and queryable** — the\nsame way AISMM does for a single product.\n\n---\n\n## What PLMM gives you\n\n- **Product Registry** — every product as a first-class, identified asset.\n- **Product Graph** — dependencies, integrations, events and data exchange.\n- **Capability Landscape** — who owns what, what's shared, where the gaps are.\n- **Cross-Product Processes** — flows that span multiple products and the models they need.\n- **AISMM Federation** — a contract binding each product's AISMM into the landscape.\n- **Semantic Routing** — a deterministic answer to \"which contexts must I load?\"\n- **Landscape Governance** — ownership, accountability, risk and compliance across the portfolio.\n\n---\n\n## How PLMM is structured\n\nPLMM is organized as **eleven layers**, each answering a distinct set of\nquestions about the landscape. Layers are folders; each holds one or more\n`*.layer.md` documents.\n\n### The eleven layers\n\n| # | Layer | Answers |\n|---|-------|---------|\n| 01 | [Product Profile](./01-products/product-profile.layer.md) | What is each product, why does it exist, who owns it? |\n| 02 | [Product Relationships](./02-relationships/product-relationships.layer.md) | How do products depend on, integrate with and feed each other? |\n| 03 | [Capability Landscape](./03-capabilities/capability-landscape.layer.md) | Which product owns which capability; what is shared? |\n| 04 | [Cross-Product Processes](./04-processes/cross-product-processes.layer.md) | Which products and AISMM models does a process span? |\n| 05 | [Operations](./05-operations/operations.layer.md) | Where each product runs (hosting, FQDN, VLAN), how it's monitored, backed up, and its SLA? |\n| 06 | [Governance](./06-governance/governance.layer.md) | Who is accountable (Product / Business / Engineering Owner); what risk and compliance applies? |\n| 07 | [AISMM Federation](./07-federation/aismm-federation.layer.md) | Which AISMM belongs to a product; what is exposed? |\n| 08 | [Change & Evolution](./08-change/change-evolution.layer.md) | What changed across the landscape; what replaced what? |\n| 09 | [Consistency & Trust](./09-consistency/consistency-trust.layer.md) | Is information verified; what is its source and coverage? |\n| 10 | [Semantic Routing](./10-semantic-routing/semantic-routing.layer.md) | Which contexts and AISMM models must a task load? |\n| 11 | [Portfolio Landscape](./11-portfolio/portfolio-landscape.layer.md) | How do products roll up into groups and business units? |\n\nThe portfolio hierarchy PLMM describes:\n\n```text\nBusiness Unit\n └─ Product Group\n     └─ Product\n         └─ AISMM   (the product's own full-context model)\n```\n\n---\n\n## Layer document model\n\nEvery layer document is plain Markdown and follows the same shape, so humans\nand parsers read it the same way:\n\n```markdown\n# <Layer name>\n\n## Purpose\n<what this layer captures, in one or two sentences>\n\n## Questions\n<the concrete questions this layer answers>\n\n## Blocks / Structure\n<the named blocks or fields the layer is composed of>\n```\n\nKeep landscape *facts and references* here; keep product *internals* in that\nproduct's AISMM. When a layer is intentionally not filled yet, say so explicitly\nrather than leaving it blank.\n\n---\n\n## Repository-native by design\n\nPLMM is a **specification**, not a package to install. A landscape model lives\nin a Git repository:\n\n- folders are layers, documents are Markdown — diff and review like code\n- references into product AISMM repos are links, not copies\n- history is the landscape's evolution; pull requests are how it changes\n\nThis makes the landscape model versioned, auditable and mergeable — the same\nproperties AISMM gives a single product.\n\n---\n\n## PLMM and AI agents\n\nAn AI agent working across products needs to know the blast radius of a task\n*before* it starts. PLMM gives it a deterministic entry point:\n\n1. Enter at the **Product Graph** and **Semantic Routing** layers.\n2. Resolve which products, capabilities and processes the task spans.\n3. Follow the **AISMM Federation** references to load exactly the product\n   models needed — no more, no less.\n\nThis keeps agent context **scoped and explainable**: the model decides what to\nload, and you can trace why.\n\n---\n\n## What PLMM is not\n\n- It is **not** a replacement for AISMM — it sits above it and references it.\n- It is **not** a copy of product internals — only landscape facts and links.\n- It is **not** a CMDB lock-in or a diagramming tool — it is a Git-native,\n  AI-readable knowledge model.\n- It is **not** a runtime — execution lives in the products themselves.\n\n---\n\n## Status & roadmap\n\nPLMM is an early **draft (v0.1.0)**: the eleven layers and their questions are\ndefined; field-level schemas, a landscape registry format, consistency rules and\nvalidation tooling are the next steps — mirroring how AISMM matured. Feedback and\nproposals are welcome via issues and pull requests.\n\n---\n\n## License\n\nLicensed under the [Apache License 2.0](./LICENSE). See [NOTICE](./NOTICE).\n\nPart of the [Orkestron](https://github.com/orkestron-ai) ecosystem: PLMM is the\nlandscape-level model that complements\n[AISMM](https://github.com/orkestron-ai/software-meta-model) (per product) and\nfeeds [Full-Context Development (FCD)](https://github.com/orkestron-ai/full-context-development).\n· [orkestron.ai](https://orkestron.ai/)\n",
      "layers": {
        "01-products/product-profile.layer.md": "# Product Profile Layer\n\n## Purpose\nDescribes a product as a business and technical asset.\n\n## Questions\n- What is this product?\n- Why does it exist?\n- What business domain does it support?\n\n## Structure\n- Identity\n- Classification\n- Lifecycle\n- Ownership\n- Environment\n\n## Main Fields\nid\nname\ndescription\npurpose\ntype\ngroup\nstatus\ncriticality\n",
        "02-relationships/product-relationships.layer.md": "# Product Relationships Layer\n\n## Purpose\nDescribes dependencies and interactions between products.\n\n## Questions\n- What products depend on each other?\n- What integrations exist?\n- What data flows exist?\n\n## Blocks\n- Dependency Graph\n- Integration Graph\n- Event Graph\n- Data Exchange Graph\n\n## Relationship Types\ndepends_on\nconsumes_from\nprovides_to\nextends\nreplaces\nfederates_with\n",
        "03-capabilities/capability-landscape.layer.md": "# Capability Landscape Layer\n\n## Purpose\nMaps business capabilities to products.\n\n## Questions\n- Which product owns capability?\n- Which capabilities are shared?\n- What capability dependencies exist?\n\n## Blocks\n- Capability Catalog\n- Ownership\n- Dependency Graph\n",
        "04-processes/cross-product-processes.layer.md": "# Cross Product Process Layer\n\n## Purpose\nDescribes business processes spanning multiple products.\n\n## Questions\n- Which products participate in a process?\n- Which AISMM models are required?\n\n## Blocks\n- Process Catalog\n- Process Routing\n- Process Criticality\n",
        "05-operations/operations.layer.md": "# Operations Layer\n\n## Purpose\nOperational characteristics of products.\n\n## Questions\n- Where is it hosted?\n- How is it monitored?\n- How is it backed up?\n\n## Blocks\n- Infrastructure Profile\n- Monitoring Profile\n- Incident Profile\n- Backup Profile\n- SLA Profile\n",
        "06-governance/governance.layer.md": "# Governance Layer\n\n## Purpose\nOwnership, accountability and compliance.\n\n## Blocks\n- Team Assignment\n- Responsibility Matrix\n- Risk Registry\n- Compliance Registry\n\n## Questions\n- Who owns the product?\n- Who supports it?\n- What compliance requirements apply?\n",
        "07-federation/aismm-federation.layer.md": "# AISMM Federation Layer\n\n## Purpose\nConnects PLMM with product AISMM repositories.\n\n## Blocks\n- AISMM Registry\n- Exported Projections\n- Federation Contract\n- Federation Coverage\n\n## Questions\n- Which AISMM belongs to the product?\n- What is exposed outside?\n",
        "08-change/change-evolution.layer.md": "# Change & Evolution Layer\n\n## Purpose\nTracks product and landscape evolution.\n\n## Blocks\n- Product History\n- Product Migration\n- Landscape Migration\n- Deprecation Registry\n\n## Questions\n- What changed?\n- What replaced the system?\n",
        "09-consistency/consistency-trust.layer.md": "# Consistency & Trust Layer\n\n## Purpose\nMeasures confidence and coverage.\n\n## Blocks\n- Coverage\n- Confidence\n- Provenance\n- Validation State\n\n## Questions\n- Is information verified?\n- What is the source?\n",
        "10-semantic-routing/semantic-routing.layer.md": "# Semantic Routing Layer\n\n## Purpose\nDetermines which AISMM models must be loaded.\n\n## Blocks\n- Context Entry Points\n- Expansion Rules\n- Traversal Policies\n\n## Questions\n- Which products participate in analysis?\n- Which contexts should be loaded?\n",
        "11-portfolio/portfolio-landscape.layer.md": "# Portfolio Landscape Layer\n\n## Purpose\nGroups products into business portfolios.\n\n## Hierarchy\nBusiness Unit\n -> Product Group\n   -> Product\n     -> AISMM\n\n## Questions\n- Which portfolio owns the product?\n- Which product groups exist?\n"
      }
    },
    "aismm": {
      "commit": "fe40e613287fa91c563da42aa22b5ee8f630562b",
      "describe": "v3.1.0-4-gfe40e61",
      "last_commit": "2026-08-03T21:12:07+03:00 FCD standard link: point to its own repository ver-cy/fcd",
      "readme_head": "# AI-driven Software Meta-Model (AISMM)\n\n<p align=\"center\">\n  <a href=\"./LICENSE\"><img alt=\"License: Apache-2.0\" src=\"https://img.shields.io/badge/License-Apache_2.0-blue.svg\"></a>\n  <img alt=\"AISMM version 3.1.0\" src=\"https://img.shields.io/badge/AISMM-v3.1.0-1f6feb.svg\">\n  <img alt=\"Spec status: stable\" src=\"https://img.shields.io/badge/status-stable-brightgreen.svg\">\n  <a href=\"./CONTRIBUTING.md\"><img alt=\"PRs welcome\" src=\"https://img.shields.io/badge/PRs-welcome-brightgreen.svg\"></a>\n  <a href=\"./CODE_OF_CONDUCT.md\"><img alt=\"Contributor Covenant 2.1\" src=\"https://img.shields.io/badge/Contributor%20Covenant-2.1-blueviolet.svg\"></a>\n</p>\n\n<p align=\"center\">\n  <em>A structured, Git-native, AI-ready product knowledge model for full-context software development.</em>\n</p>\n\n## Contents\n\n- [What is AISMM?](#what-is-aismm)\n- [Quick start](#quick-start)\n- [Why AISMM is needed](#why-aismm-is-needed)\n- [Core idea](#core-idea) · [What AISMM gives you](#what-aismm-gives-you)\n- [How AISMM is structured](#how-aismm-is-structured) · [Bundles (b0–b12)](#bundles)\n- [Canonical product model layout](#canonical-product-model-layout) · [Document model](#document-model)\n- [Repository-native by design](#repository-native-by-design) · [Machine-readable schemas](#machine-readable-schemas)\n- [AISMM and AI agents](#aismm-and-ai-agents) · [AISMM and RAG](#aismm-and-rag)\n- [What's new in v3.1](#aismm-v31-additions) · [v3 additions](#aismm-v3-additions) · [v2 additions](#aismm-v2-additions)\n- [How AISMM relates to other approaches](#how-aismm-relates-to-other-approaches)\n- [What AISMM is not](#what-aismm-is-not) · [Versioning and conformance](#versioning-and-conformance)\n- [FAQ](#faq)\n- [Contributing & community](#contributing--community) · [License](#license)\n\n## What is AISMM?\n\n**AISMM (AI-driven Software Meta-Model)** is a structured, machine-readable and human-readable way to describe a software product as a complete system.\n\nIt is not just documentation.\n\nAISMM is a **product knowledge model** that connects:\n\n- why the product exists\n- what business value it creates\n- how the system is designed\n- how behavior is specified\n- how the code is implemented\n- how the system runs in production\n- how quality, risk and compliance are controlled\n- how changes are planned and released\n- how knowledge is indexed, traced and trusted\n\nIn simple terms:\n\n```text\nAISMM = full structured context of a software product\n```\n\nIt is designed to be stored in Git, reviewed like code, used by humans, and processed by AI agents.\n\n---\n\n## AISMM at a glance\n\n<p align=\"center\">\n  <img src=\"./assets/aismm-diagram-v3.png\" alt=\"AISMM Structure v3\" width=\"100%\">\n</p>\n\n<p align=\"center\">\n  <em>AISMM connects value, system design, execution and knowledge into a unified model for AI-driven software engineering.</em>\n</p>\n\n---\n\n## Quick start\n\nAISMM is a **specification**, not a package to install. \"Getting started\" means\nputting a product's knowledge under the model. The fastest path:\n\n1. **Vendor the meta-model into your product repo.** Add this canon as\n   `00-meta/software-meta-model-main/` (and the template tree alongside it) so\n   your repo carries the rules it conforms to. See\n   [Canonical product model layout](#canonical-product-model-layout).\n\n2. **Create the registry.** Copy\n   [`examples/aismm.registry.example.json`](./examples/aismm.registry.example.json)\n   to `aismm.registry.json` at your repo root and fill in your `product_id` and\n   sources. Parsers and agents start from this file — see\n   [`aismm-model-registry.md`](./aismm-model-registry.md).\n\n3. **Stand up the bundle/layer folders** under `aismm/` (b0–b12). For any layer\n   you'll need but haven't filled yet, drop an **explicit empty-layer block**\n   instead of leaving it missing — copy\n   [`examples/empty-layer.example.md`](./examples/empty-layer.example.md). See\n   [Empty layers vs missing layers](#empty-layers-vs-missing-layers).\n\n4. **Write your first real layer** — a good start is `b0.001` (product\n   definition) or `b4.401` (requirements). Add the AISMM block header (see\n   [Document model](#document-model)) and link it to related entities.\n\n5. **Validate and declare a level.** Run the consistency and health checks\n   ([`aismm-consistency-checks.md`](./aismm-consistency-checks.md),\n   [`aismm-health.md`](./aismm-health.md)) and declare a\n   [conformance level](#versioning-and-conformance) — start at L1.\n\n> New to the concepts? Read [What is AISMM?](#what-is-aismm) and\n> [Core idea](#core-idea) first, then come back here.\n\n---\n\n## Why AISMM is needed\n\nModern software products are not just code.\n\nA real product includes:\n\n- business goals\n- value streams\n- stakeholders\n- requirements\n- architecture\n- data models\n- APIs\n- integrations\n- processes\n- UX scenarios\n- runtime infrastructure\n- monitoring\n- incidents\n- tests\n- risks\n- security controls\n- release history\n- decisions\n- hidden context in tasks and discussions\n\nMost companies keep this knowledge scattered across many systems:\n\n```text\nJira + Git + Confluence + Figma + BPMN + Grafana + CI/CD + Slack + people's heads\n```\n\nThis creates several problems:\n\n- AI agents cannot understand the full product context.\n- New developers need too much time to understand the system.\n- Architecture decisions lose their original reasoning.\n- Requirements drift away from implementation.\n- Tests are not clearly linked to behavior.\n- Incidents are not clearly linked to releases and changes.\n- Product value is disconnected from technical work.\n- Knowledge becomes too large, noisy and hard to retrieve.\n\nAISMM solves this by turning scattered product knowledge into a **connected semantic model**.\n\n---\n\n## Core idea\n\nAISMM treats a software system as:\n\n```text\nValue + Structure + Behavior + Execution + Change + Knowledge\n```\n\nOr more explicitly:\n\n```text\nSoftware System =\n  Business Value\n  + Product Behavior\n  + System Design\n  + Implementation\n  + Runtime Reality\n  + Quality / Risk / Compliance\n  + SDLC History\n  + Traceable Knowledge\n```\n\nThis allows both humans and AI agents to reason about the product as a whole.\n\n---\n\n## What AISMM gives you"
    }
  },
  "managed_it_service_graph": {
    "publication": {
      "status": "published",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "generatedAt": "2026-09-20T19:02:23Z",
      "synthesisSha256": "dcda6e0b3750b6d70b888d298f966e732d86bca9813c6a27255ffb4d6314f0f2",
      "providerMode": "single-provider-waiver",
      "providers": [
        "Codex"
      ],
      "waivedProviders": [
        "Claude",
        "Grok"
      ]
    },
    "model": {
      "registry_id": "vr.wm-xct-039",
      "model_id": "WM-XCT-039",
      "name": "Managed IT Service Graph",
      "entry_kind": "aggregate",
      "purpose": "Compose client-isolated infrastructure and service references with explicit authoritative data routing.",
      "scope_statement": "A bounded service-provider/client graph profile. It records tenant boundary, service/asset references, dependencies, desired versus observed state, per-fact mastership, routed change outcomes, and authorized projections. It does not become a competing CMDB or authorization engine.",
      "in_scope": [
        "Client and provider relationship references",
        "Typed service-to-asset dependencies",
        "Per-fact owning Dimension and master-system mapping",
        "Source-qualified observations and change outcomes",
        "Purpose-bound projections and handover evidence"
      ],
      "out_of_scope": [
        "Full asset, party, ownership, task or contract lifecycles",
        "Implemented IAM, CMDB, discovery, Jira connector or distributed transaction engine",
        "Automatic legal ownership transfer or proof of client acceptance",
        "Universal infrastructure schema or full Redfish conformance"
      ],
      "boundary_notes": [
        {
          "neighbor": "Ownership / Stewardship",
          "distinction": "Reference control assertions; administration does not imply title or client acceptance.",
          "source_refs": [
            "SRC-001",
            "SRC-004"
          ]
        },
        {
          "neighbor": "Dependency / Impact",
          "distinction": "Reference typed dependency semantics; domain profile supplies tenant/master boundaries, not universal impact calculus.",
          "source_refs": [
            "SRC-002",
            "SRC-003"
          ]
        },
        {
          "neighbor": "Redfish and CMDB",
          "distinction": "Reference infrastructure identities and observations; adapters and their schema versions are separately validated.",
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "neighbor": "Task and service case",
          "distinction": "Link work IDs; do not copy task state as an independently editable authority.",
          "source_refs": [
            "SRC-001",
            "SRC-006"
          ]
        }
      ]
    },
    "selected_findings": [
      {
        "bundle": {
          "id": "boundary-bundle",
          "name": "Tenant and service boundary",
          "description": "Bounded graph concerns: tenant and service boundary"
        },
        "layer": {
          "id": "tenant-layer",
          "name": "Client and provider identities",
          "description": "Authored composition-profile design for client and provider identities. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "tenant-finding",
          "name": "Client and provider identities",
          "description": "Authored composition-profile design for client and provider identities. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-004"
          ],
          "questions": [
            {
              "id": "tenant-q1",
              "text": "Which client Dimension and provider organization does this graph describe?",
              "kind": "identity",
              "answer_data": [
                "tenant-identity-data"
              ]
            },
            {
              "id": "tenant-q2",
              "text": "Who is the current graph steward and what evidence authorizes administration?",
              "kind": "ownership",
              "answer_data": [
                "tenant-stewardship-data"
              ]
            },
            {
              "id": "tenant-q3",
              "text": "Which shared resources are referenced without transferring their ownership to this client?",
              "kind": "constraint",
              "answer_data": [
                "tenant-shared-resources-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "tenant-identity-data",
              "name": "identity",
              "description": "Proposed members: clientDimensionId, providerPartyRef, graphId, namespace. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-004"
              ]
            },
            {
              "id": "tenant-stewardship-data",
              "name": "stewardship",
              "description": "Proposed members: stewardRef, authorityEvidenceRef, effectiveFrom, effectiveTo. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-004"
              ]
            },
            {
              "id": "tenant-shared-resources-data",
              "name": "shared-resources",
              "description": "Proposed members: resourceRefs, owningDimensionRefs, permittedReferenceScope. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-004"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "tenant-artifact",
              "name": "Client and provider identities record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-004"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "boundary-bundle",
          "name": "Tenant and service boundary",
          "description": "Bounded graph concerns: tenant and service boundary"
        },
        "layer": {
          "id": "service-layer",
          "name": "Service responsibility",
          "description": "Authored composition-profile design for service responsibility. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "service-finding",
          "name": "Service responsibility",
          "description": "Authored composition-profile design for service responsibility. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-003"
          ],
          "questions": [
            {
              "id": "service-q1",
              "text": "What bounded service outcome is represented by this graph?",
              "kind": "definition",
              "answer_data": [
                "service-service-data"
              ]
            },
            {
              "id": "service-q2",
              "text": "Which provider roles perform work and which party remains accountable?",
              "kind": "relationship",
              "answer_data": [
                "service-responsibility-data"
              ]
            },
            {
              "id": "service-q3",
              "text": "Which services or subcontractor obligations are explicitly outside this graph?",
              "kind": "exception",
              "answer_data": [
                "service-exclusions-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "service-service-data",
              "name": "service",
              "description": "Proposed members: serviceRef, outcomeDescription, boundary, lifecycleState. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003"
              ]
            },
            {
              "id": "service-responsibility-data",
              "name": "responsibility",
              "description": "Proposed members: responsibleRoleRefs, accountablePartyRef, agreementRef. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003"
              ]
            },
            {
              "id": "service-exclusions-data",
              "name": "exclusions",
              "description": "Proposed members: excludedServiceRefs, reason, evidenceRef. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "service-artifact",
              "name": "Service responsibility record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-003"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "boundary-bundle",
          "name": "Tenant and service boundary",
          "description": "Bounded graph concerns: tenant and service boundary"
        },
        "layer": {
          "id": "identity-map-layer",
          "name": "Asset identity and recognition",
          "description": "Authored composition-profile design for asset identity and recognition. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "identity-map-finding",
          "name": "Asset identity and recognition",
          "description": "Authored composition-profile design for asset identity and recognition. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-002",
            "SRC-005"
          ],
          "questions": [
            {
              "id": "identity-map-q1",
              "text": "Which authoritative identifier distinguishes this asset from similarly named resources?",
              "kind": "identity",
              "answer_data": [
                "identity-map-anchor-data"
              ]
            },
            {
              "id": "identity-map-q2",
              "text": "Is the referenced item physical equipment, a virtual resource or a service endpoint?",
              "kind": "classification",
              "answer_data": [
                "identity-map-classification-data"
              ]
            },
            {
              "id": "identity-map-q3",
              "text": "How was the identity match observed and how are ambiguous matches quarantined?",
              "kind": "evidence",
              "answer_data": [
                "identity-map-recognition-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "identity-map-anchor-data",
              "name": "anchor",
              "description": "Proposed members: assetRef, masterSystemId, masterRecordId, aliasEvidence. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-005"
              ]
            },
            {
              "id": "identity-map-classification-data",
              "name": "classification",
              "description": "Proposed members: assetClassRef, resourceKind, classificationEvidence. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-005"
              ]
            },
            {
              "id": "identity-map-recognition-data",
              "name": "recognition",
              "description": "Proposed members: observationRef, observedAt, matchEvidence, ambiguityState. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-005"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "identity-map-artifact",
              "name": "Asset identity and recognition record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-002",
                "SRC-005"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "graph-bundle",
          "name": "Dependencies and observations",
          "description": "Bounded graph concerns: dependencies and observations"
        },
        "layer": {
          "id": "dependency-layer",
          "name": "Service-to-asset dependencies",
          "description": "Authored composition-profile design for service-to-asset dependencies. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "dependency-finding",
          "name": "Service-to-asset dependencies",
          "description": "Authored composition-profile design for service-to-asset dependencies. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-005"
          ],
          "questions": [
            {
              "id": "dependency-q1",
              "text": "Which service depends on which asset and in what direction?",
              "kind": "relationship",
              "answer_data": [
                "dependency-edge-data"
              ]
            },
            {
              "id": "dependency-q2",
              "text": "Under which condition and time interval is this dependency valid?",
              "kind": "constraint",
              "answer_data": [
                "dependency-validity-data"
              ]
            },
            {
              "id": "dependency-q3",
              "text": "Is the dependency declared, observed or inferred and what uncertainty remains?",
              "kind": "quality",
              "answer_data": [
                "dependency-assurance-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "dependency-edge-data",
              "name": "edge",
              "description": "Proposed members: sourceRef, targetRef, relationType, owningDimensionId. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-005"
              ]
            },
            {
              "id": "dependency-validity-data",
              "name": "validity",
              "description": "Proposed members: condition, validFrom, validTo, evidenceRef. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-005"
              ]
            },
            {
              "id": "dependency-assurance-data",
              "name": "assurance",
              "description": "Proposed members: assertionKind, confidence, sourceRef, unresolvedAssumptions. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-005"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "dependency-artifact",
              "name": "Service-to-asset dependencies record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-005"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "graph-bundle",
          "name": "Dependencies and observations",
          "description": "Bounded graph concerns: dependencies and observations"
        },
        "layer": {
          "id": "state-layer",
          "name": "Declared and observed state",
          "description": "Authored composition-profile design for declared and observed state. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "state-finding",
          "name": "Declared and observed state",
          "description": "Authored composition-profile design for declared and observed state. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-002",
            "SRC-003",
            "SRC-005"
          ],
          "questions": [
            {
              "id": "state-q1",
              "text": "What desired state is declared by the configuration authority?",
              "kind": "state",
              "answer_data": [
                "state-desired-data"
              ]
            },
            {
              "id": "state-q2",
              "text": "What actual state was observed and by which method?",
              "kind": "measurement",
              "answer_data": [
                "state-observed-data"
              ]
            },
            {
              "id": "state-q3",
              "text": "How is a discrepancy retained without overwriting desired or observed state?",
              "kind": "validation",
              "answer_data": [
                "state-difference-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "state-desired-data",
              "name": "desired",
              "description": "Proposed members: configurationRef, revision, validFrom, declaringAuthority. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-003",
                "SRC-005"
              ]
            },
            {
              "id": "state-observed-data",
              "name": "observed",
              "description": "Proposed members: observationRef, value, unit, method, observedAt, tolerance. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-003",
                "SRC-005"
              ]
            },
            {
              "id": "state-difference-data",
              "name": "difference",
              "description": "Proposed members: desiredRef, observedRef, discrepancyId, assessmentState. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-003",
                "SRC-005"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "state-artifact",
              "name": "Declared and observed state record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-002",
                "SRC-003",
                "SRC-005"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "graph-bundle",
          "name": "Dependencies and observations",
          "description": "Bounded graph concerns: dependencies and observations"
        },
        "layer": {
          "id": "impact-layer",
          "name": "Bounded impact assessment",
          "description": "Authored composition-profile design for bounded impact assessment. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "impact-finding",
          "name": "Bounded impact assessment",
          "description": "Authored composition-profile design for bounded impact assessment. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-002",
            "SRC-003"
          ],
          "questions": [
            {
              "id": "impact-q1",
              "text": "Which directed dependency paths are traversed for this impact question?",
              "kind": "process",
              "answer_data": [
                "impact-traversal-data"
              ]
            },
            {
              "id": "impact-q2",
              "text": "Which missing or stale edges limit the confidence of the impact result?",
              "kind": "quality",
              "answer_data": [
                "impact-limits-data"
              ]
            },
            {
              "id": "impact-q3",
              "text": "Who reviews an inferred impact before it authorizes an operational action?",
              "kind": "decision",
              "answer_data": [
                "impact-review-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "impact-traversal-data",
              "name": "traversal",
              "description": "Proposed members: startRefs, relationFilter, depthLimit, cyclePolicy. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "impact-limits-data",
              "name": "limits",
              "description": "Proposed members: missingEdgeRefs, staleSourceRefs, confidence, completenessBoundary. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "impact-review-data",
              "name": "review",
              "description": "Proposed members: reviewerRef, evidenceRef, decisionRef, actionAuthorizationRef. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "impact-artifact",
              "name": "Bounded impact assessment record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "mastership-bundle",
          "name": "Authoritative data and changes",
          "description": "Bounded graph concerns: authoritative data and changes"
        },
        "layer": {
          "id": "master-layer",
          "name": "Per-fact mastership",
          "description": "Authored composition-profile design for per-fact mastership. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "master-finding",
          "name": "Per-fact mastership",
          "description": "Authored composition-profile design for per-fact mastership. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003"
          ],
          "questions": [
            {
              "id": "master-q1",
              "text": "Which one owning Dimension and master system govern this fact path at this time?",
              "kind": "ownership",
              "answer_data": [
                "master-mapping-data"
              ]
            },
            {
              "id": "master-q2",
              "text": "What approved evidence defines that master assignment and its precedence?",
              "kind": "authority",
              "answer_data": [
                "master-authority-data"
              ]
            },
            {
              "id": "master-q3",
              "text": "What happens when mastership is unknown or equally authoritative sources disagree?",
              "kind": "exception",
              "answer_data": [
                "master-conflict-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "master-mapping-data",
              "name": "mapping",
              "description": "Proposed members: subjectRef, factPath, owningDimensionId, masterSystemId, validFrom, validTo. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "master-authority-data",
              "name": "authority",
              "description": "Proposed members: policyRef, approvingRoleRef, approvalEvidenceRef, precedenceScope. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "master-conflict-data",
              "name": "conflict",
              "description": "Proposed members: pendingState, conflictingAssertionRefs, resolutionOwnerRef, resolutionEvidence. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "master-artifact",
              "name": "Per-fact mastership record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "mastership-bundle",
          "name": "Authoritative data and changes",
          "description": "Bounded graph concerns: authoritative data and changes"
        },
        "layer": {
          "id": "write-layer",
          "name": "Routed change lifecycle",
          "description": "Authored composition-profile design for routed change lifecycle. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "write-finding",
          "name": "Routed change lifecycle",
          "description": "Authored composition-profile design for routed change lifecycle. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-006"
          ],
          "questions": [
            {
              "id": "write-q1",
              "text": "To which master endpoint is the proposed change routed under the current grant?",
              "kind": "process",
              "answer_data": [
                "write-route-data"
              ]
            },
            {
              "id": "write-q2",
              "text": "Which version precondition and retry key protect the change from stale writes or duplication?",
              "kind": "constraint",
              "answer_data": [
                "write-preconditions-data"
              ]
            },
            {
              "id": "write-q3",
              "text": "What authoritative acknowledgement or readback proves that the change took effect?",
              "kind": "event",
              "answer_data": [
                "write-outcome-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "write-route-data",
              "name": "route",
              "description": "Proposed members: changeId, targetSystemRef, operation, scope, authorizationRef. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-006"
              ]
            },
            {
              "id": "write-preconditions-data",
              "name": "preconditions",
              "description": "Proposed members: expectedRevision, conditionalRequestBinding, operationKey, retryPolicy. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-006"
              ]
            },
            {
              "id": "write-outcome-data",
              "name": "outcome",
              "description": "Proposed members: requestRef, responseRef, masterRevision, state, failureReason, readbackEvidence. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-006"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "write-artifact",
              "name": "Routed change lifecycle record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-006"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "exchange-bundle",
          "name": "Projection and provider lifecycle",
          "description": "Bounded graph concerns: projection and provider lifecycle"
        },
        "layer": {
          "id": "projection-layer",
          "name": "Authorized cross-Dimension view",
          "description": "Authored composition-profile design for authorized cross-dimension view. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "projection-finding",
          "name": "Authorized cross-Dimension view",
          "description": "Authored composition-profile design for authorized cross-dimension view. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-004"
          ],
          "questions": [
            {
              "id": "projection-q1",
              "text": "Which recipient, purpose, objects and fields are permitted in this projection?",
              "kind": "access",
              "answer_data": [
                "projection-grant-data"
              ]
            },
            {
              "id": "projection-q2",
              "text": "How fresh is the projected view and when must it expire or be rechecked?",
              "kind": "temporal",
              "answer_data": [
                "projection-freshness-data"
              ]
            },
            {
              "id": "projection-q3",
              "text": "How are revocation, deletion and derived sensitive relationships handled by this view?",
              "kind": "privacy",
              "answer_data": [
                "projection-withdrawal-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "projection-grant-data",
              "name": "grant",
              "description": "Proposed members: sourceDimensionId, targetDimensionId, recipientRef, purpose, objectFilter, fieldAllowlist, policyRef. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-004"
              ]
            },
            {
              "id": "projection-freshness-data",
              "name": "freshness",
              "description": "Proposed members: sourceRevision, observedAt, refreshedAt, maxAge, expiresAt. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-004"
              ]
            },
            {
              "id": "projection-withdrawal-data",
              "name": "withdrawal",
              "description": "Proposed members: revocationState, tombstoneRef, cacheInvalidationBinding, retentionException, derivedEdgeFilter. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-004"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "projection-artifact",
              "name": "Authorized cross-Dimension view record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-003",
                "SRC-004"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "exchange-bundle",
          "name": "Projection and provider lifecycle",
          "description": "Bounded graph concerns: projection and provider lifecycle"
        },
        "layer": {
          "id": "handover-layer",
          "name": "Provider change and handover",
          "description": "Authored composition-profile design for provider change and handover. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "handover-finding",
          "name": "Provider change and handover",
          "description": "Authored composition-profile design for provider change and handover. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003"
          ],
          "questions": [
            {
              "id": "handover-q1",
              "text": "Which authority acceptance and cutover evidence allow a new provider to take over?",
              "kind": "lifecycle",
              "answer_data": [
                "handover-cutover-data"
              ]
            },
            {
              "id": "handover-q2",
              "text": "Which object identifiers and historical master references must survive handover?",
              "kind": "identity",
              "answer_data": [
                "handover-continuity-data"
              ]
            },
            {
              "id": "handover-q3",
              "text": "Which previous grants and connector credentials must be revoked and verified?",
              "kind": "security",
              "answer_data": [
                "handover-revocation-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "handover-cutover-data",
              "name": "cutover",
              "description": "Proposed members: outgoingProviderRef, incomingProviderRef, clientAcceptanceRef, cutoverAt, verificationState. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "handover-continuity-data",
              "name": "continuity",
              "description": "Proposed members: preservedIds, mappingRefs, historicalMasterRefs, exportManifestRef. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "handover-revocation-data",
              "name": "revocation",
              "description": "Proposed members: grantRefs, credentialReferencesOnly, revocationEvidence, residualAccessReview. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "handover-artifact",
              "name": "Provider change and handover record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      },
      {
        "bundle": {
          "id": "exchange-bundle",
          "name": "Projection and provider lifecycle",
          "description": "Bounded graph concerns: projection and provider lifecycle"
        },
        "layer": {
          "id": "assurance-layer",
          "name": "Graph completeness and audit",
          "description": "Authored composition-profile design for graph completeness and audit. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources."
        },
        "finding": {
          "id": "assurance-finding",
          "name": "Graph completeness and audit",
          "description": "Authored composition-profile design for graph completeness and audit. Cited sources motivate distinctions; these field groups are not asserted to be mandated verbatim by those sources.",
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003"
          ],
          "questions": [
            {
              "id": "assurance-q1",
              "text": "Which graph invariants have been checked and which checks remain unimplemented?",
              "kind": "validation",
              "answer_data": [
                "assurance-checks-data"
              ]
            },
            {
              "id": "assurance-q2",
              "text": "Which source revisions and approvals explain each material graph change?",
              "kind": "provenance",
              "answer_data": [
                "assurance-audit-data"
              ]
            },
            {
              "id": "assurance-q3",
              "text": "Which exported fields are preserved, transformed or lost by a destination adapter?",
              "kind": "interoperability",
              "answer_data": [
                "assurance-mapping-data"
              ]
            }
          ],
          "data_elements": [
            {
              "id": "assurance-checks-data",
              "name": "checks",
              "description": "Proposed members: validationRunRef, ruleIds, failures, unimplementedChecks. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "assurance-audit-data",
              "name": "audit",
              "description": "Proposed members: eventRefs, actorRefs, sourceRevisions, approvalRefs, recordingTime. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            },
            {
              "id": "assurance-mapping-data",
              "name": "mapping",
              "description": "Proposed members: adapterVersion, fieldMap, lossReport, reconciliationEvidence. This draft declares a semantic record group; nested executable schemas are not yet supplied. Unknown and not-applicable require explicit reasons.",
              "value_kind": "object",
              "cardinality": "1",
              "required": true,
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "artifacts": [
            {
              "id": "assurance-artifact",
              "name": "Graph completeness and audit record",
              "description": "Attributed minimal record or protected master-system reference; preserves unknowns and excludes secrets.",
              "media_or_form": [
                "structured record",
                "source reference"
              ],
              "serial": true,
              "identity_strategy": "Use authoritative master-system identifier; otherwise namespace-scoped immutable identifier with explicit mapping.",
              "source_refs": [
                "SRC-001",
                "SRC-002",
                "SRC-003"
              ]
            }
          ],
          "inline_only_rationale": null
        }
      }
    ],
    "functions": [
      {
        "id": "register-graph",
        "name": "Register graph",
        "description": "Register graph within the declared Dimension policy.",
        "inputs": [
          "approved tenant boundary and authority"
        ],
        "outputs": [
          "stable graph identity and referenced endpoints"
        ],
        "preconditions": [
          "Owner authority and client scope are established"
        ],
        "effects": [
          "Create an attributed graph revision; do not create client acceptance"
        ],
        "source_refs": [
          "SRC-001",
          "SRC-002"
        ]
      },
      {
        "id": "route-change",
        "name": "Route proposed change",
        "description": "Route proposed change within the declared Dimension policy.",
        "inputs": [
          "fact path, proposed value and expected master revision"
        ],
        "outputs": [
          "acknowledged, pending or failed operation evidence"
        ],
        "preconditions": [
          "Exactly one master and current operation grant resolve"
        ],
        "effects": [
          "Submit through the authorized adapter; only authoritative confirmation updates the observed projection"
        ],
        "source_refs": [
          "SRC-001",
          "SRC-006"
        ]
      },
      {
        "id": "project-graph",
        "name": "Build permitted projection",
        "description": "Build permitted projection within the declared Dimension policy.",
        "inputs": [
          "graph revision, recipient, purpose and field policy"
        ],
        "outputs": [
          "filtered view with origin and freshness"
        ],
        "preconditions": [
          "Source and target policies and role/task scope permit every disclosed field and inferred edge"
        ],
        "effects": [
          "Materialize a revocable derived view; do not grant independent write authority"
        ],
        "source_refs": [
          "SRC-001",
          "SRC-003",
          "SRC-004"
        ]
      },
      {
        "id": "handover-graph",
        "name": "Record provider handover",
        "description": "Record provider handover within the declared Dimension policy.",
        "inputs": [
          "accepted transfer plan and access inventory"
        ],
        "outputs": [
          "continuity manifest and revocation evidence"
        ],
        "preconditions": [
          "Incoming authority acceptance and retention obligations are verified"
        ],
        "effects": [
          "Record cutover with stable IDs; external credential changes require separate authorized execution"
        ],
        "source_refs": [
          "SRC-001",
          "SRC-002",
          "SRC-003"
        ]
      }
    ],
    "composition": [
      {
        "target": "vr.wm-xct-001",
        "relation": "COMPOSE",
        "purpose": "Control and stewardship assertions for referenced Dimension and resources",
        "required": true,
        "source_refs": [
          "SRC-001",
          "SRC-002"
        ]
      },
      {
        "target": "vr.wm-xct-003",
        "relation": "COMPOSE",
        "purpose": "Projection and disclosure constraints",
        "required": true,
        "source_refs": [
          "SRC-001",
          "SRC-002"
        ]
      },
      {
        "target": "vr.wm-xct-037",
        "relation": "COMPOSE",
        "purpose": "Typed dependency and bounded impact semantics",
        "required": true,
        "source_refs": [
          "SRC-001",
          "SRC-002"
        ]
      }
    ],
    "researchAdjudication": {
      "providerMode": "single-provider-waiver",
      "activeProviders": [
        "codex"
      ],
      "waivedProviders": [
        "claude",
        "grok"
      ],
      "providerPolicy": {
        "contract_version": "1.0.0",
        "mode": "single-provider-waiver",
        "effective_at": "2026-09-06T00:00:00Z",
        "scope": "Canonical single-stream subject-model research after the six-workstream consolidation",
        "active_providers": [
          "codex"
        ],
        "waived_providers": [
          {
            "provider": "claude",
            "authorized_by": "repository owner",
            "authorized_at": "2026-09-06T00:00:00Z",
            "reason": "Claude produced no result on prior 1800-second and 900-second attempts and again timed out on bounded 600-second Sonnet and 300-second Haiku passes. The owner prioritized completion over provider availability."
          },
          {
            "provider": "grok",
            "authorized_by": "repository owner",
            "authorized_at": "2026-09-06T00:00:00Z",
            "reason": "The repository owner authorized completion without Grok when Grok is unavailable, slow or schema-invalid. Grok may still be attempted as a bounded supplemental reviewer, but its failure never blocks a valid Claude plus no-tools result."
          }
        ],
        "review_rule": "Codex may complete source-grounded fallback research after bounded Claude and Grok attempts fail. It requires a separate no-tools adversarial audit and remains reviewable-draft with a visible absence-of-external-review hold.",
        "supplemental_provider_attempts": [
          {
            "provider": "claude",
            "required": false,
            "maximum_attempts": 1,
            "failure_policy": "record-and-continue",
            "admission_rule": "Use only a locally schema-valid result whose sources and boundaries survive adjudication."
          },
          {
            "provider": "grok",
            "required": false,
            "maximum_attempts": 1,
            "failure_policy": "record-and-continue",
            "admission_rule": "Use only a locally schema-valid result whose sources and boundaries survive adjudication."
          }
        ]
      },
      "boundaryDecision": {
        "entry_kind": "aggregate",
        "status": "accepted",
        "rationale": "A bounded service-provider/client graph profile. It records tenant boundary, service/asset references, dependencies, desired versus observed state, per-fact mastership, routed change outcomes, and authorized projections. It does not become a competing CMDB or authorization engine."
      },
      "decisions": [
        {
          "concept": "Cross-client composition",
          "disposition": "accepted",
          "rationale": "Own only graph relationships and master mappings; preserve referenced model boundaries."
        },
        {
          "concept": "Operational enforcement",
          "disposition": "deferred",
          "rationale": "Publication does not implement adapters, IAM or nested runtime schemas."
        }
      ],
      "publicationHolds": [
        "Nested data-group schemas and executable graph/IAM enforcement are not supplied.",
        "Redfish source is the standards overview; concrete DSP schema mapping is not claimed.",
        "No production Jira, discovery, CMDB or revocable-cache adapter is implemented.",
        "External independent research results are admitted only if available and validated; assurance remains reviewable-draft.",
        "Claude timed out after one 60-second attempt; Grok returned provider-error after one bounded attempt. A separate Codex no-tools audit reviewed the supplied design summary, not source truth or executable behavior.",
        "Independent external review was explicitly waived by the repository owner; this codex-only result remains a reviewable draft."
      ],
      "deferredResearch": [
        "Executable nested schemas and tenant-isolation negative fixtures",
        "Versioned CMDB/Redfish/Jira adapters and operational readback tests"
      ]
    }
  },
  "registry_policy": {
    "reserved_candidates": [
      "PLMM",
      "WM-XCT-039"
    ],
    "rule": "PLMM already has reserved runtime id vr.vercy.plmm. Do not invent a replacement ID; decide whether to complete, profile or retire it."
  }
}

```

## CLAUDE INDEPENDENT STUDY

```
## Verdict

**COMPLETE RESERVED MODEL** — in place, under the existing reserved id `vr.vercy.plmm`, as a new version line; keep `0.1.0-legacy` frozen as a historical artifact.

Rejected alternatives, on dossier evidence:

- **REUSE ONLY** is impossible. The runtime spec has `structure.bundles: []`, `serviceLayers.crud: {}`, `roles: []`, `policies: []`, `artifactFormats: []`, and `installable: false`. There is nothing instantiable to reuse.
- **PROFILE** has no valid base. AISMM is explicitly per-product ("full structured context of ONE product"); profiling it would relocate landscape facts into product scope. WM-XCT-039 is narrower (tenant-scoped service→asset graph, `entry_kind: aggregate`) and is itself `publishableCanonical: false`.
- **RETIRE** is unjustified: the repository pin `a8e388c` carries eleven substantive layers covering exactly the contour's scope, and no other dossier model masters product-to-product landscape membership.

## Evidence state/version reconciliation

**AISMM 3.2 mismatch: not present in this dossier.** Runtime `version: 3.1.0`; repository README badge `AISMM v3.1.0`; `previousVersions` lists only 3.0.0 and 2.x. No 3.2 string appears anywhere. The contour's `specific_questions` entry about "AISMM 3.1 runtime and 3.2 README" is stale against these bytes and should be closed as a numbering question.

It is replaced by a different, narrower discrepancy: `describe: v3.1.0-4-gfe40e61` — the pinned tree is **four commits past the v3.1.0 tag** (last commit 2026-08-03, an FCD link change). So the *label* reconciles while the *bytes* do not equal the tag. Additionally `aismm_runtime_spec_summary.metaModel.status` reads "canonical legacy assembly projection" while the registry says `status: published, installable: true`; the dossier contains no fixture or digest cross-check linking the runtime digest `sha256:a603…` to commit `fe40e61`. I therefore assert no compatibility and no installability for either model.

**PLMM.** Runtime `0.1.0-legacy`, `status: legacy`, digest `sha256:7100…`, empty projection, `legacySource: https://github.com/ver-cy/plmm`. Repository pin `a8e388c` (2026-06-22) declares **v0.1.0 draft** and links to `orkestron-ai/software-meta-model` and the Orkestron org. Two unreconciled facts: (a) the runtime `-legacy` suffix versus the repository's plain `0.1.0` draft label; (b) org provenance `ver-cy` versus `orkestron-ai`. Neither is resolvable from the dossier; both are publication holds.

**Declared federation is prose only.** Both models have `requires: []` and `relations: []`. The PLMM→AISMM federation exists in README text and in layer `07-federation`, not in the registry graph.

## Boundary

PLMM masters the landscape *between* products and nothing inside one:

| PLMM masters | PLMM references only |
|---|---|
| `SoftwareLandscape` identity, scope, `architecture_state`, `as_of`, `composition_version` | Product internals (requirements, architecture, code, runtime) — AISMM |
| `LandscapeMembership` (which product is in which landscape, since when, with what confidence) | `SoftwareProduct` identity itself — held by the product's own master/AISMM registry |
| `LandscapeDependency` (typed, directed, version-pinned product-to-product edges) | Asset-level and tenant-isolated service graphs — WM-XCT-039 |
| Completeness/coverage of the graph and impact-routing results | Projection/IAM enforcement, CMDB/discovery adapters — out of scope per WM-XCT-039's own `out_of_scope` |

**No second `SoftwareProduct`.** Membership carries `productRef` (external authoritative id) plus `aismmRef`; the product record is never re-mastered. Relation vocabulary can be adopted from repo layer 02: `depends_on, consumes_from, provides_to, extends, replaces, federates_with`.

**Tenant/service specialization.** WM-XCT-039 is not a parent and not a dependency. For managed-service landscapes, `LandscapeMembership` may carry an optional `tenantScopeRef`; isolation, projection grants and per-fact mastership stay delegated. Any `COMPOSE` edge to `vr.wm-xct-039` would inherit its single-provider waiver and its "nested schemas not supplied" hold — so do not declare one now.

## Membership/dependency/completeness contract

- **Membership identity:** namespace-scoped immutable surrogate, natural key `(landscapeId, productRef, validFrom)`. Lifecycle `proposed → asserted → withdrawn`; withdrawal tombstones, never deletes, so historical impact answers stay explainable. Each membership carries `assertionKind (declared|observed|inferred)`, `confidence`, `sourceRef`.
- **Dependency identity:** `(landscapeId, sourceMembershipRef, targetMembershipRef, relationType, validFrom)`, plus mandatory `sourceVersionPin` and `targetVersionPin` (tag **and** commit **and** digest). An edge lacking either pin is state `unpinned` and is excluded from any answer labelled canonical; it still appears in the result as a gap. Edges reference memberships, not raw products, so an edge cannot outlive its membership.
- **Completeness:** every impact answer emits `traversal { startRefs, relationFilter, depthLimit, cyclePolicy }` and `limits { missingEdgeRefs, staleSourceRefs, unknownMembershipRefs, unpinnedEdgeRefs, confidence, completenessBoundary }`. An empty graph must return "unknown, zero coverage", never "no impact".

## Migration path

1. Freeze `0.1.0-legacy` with digest `sha256:7100…` as a non-installable historical record; do not edit it.
2. Open `0.2.0-draft` on the same id `vr.vercy.plmm`, sourced from immutable ref `a8e388c21901540b71cc8479d4d6ef119c2ea276`, recorded as commit + describe + content digest.
3. Project the eleven repo layers into `structure.bundles` (today `[]`), preserving layer numbering as stable ids.
4. Close the three gaps the legacy spec itself names: findings, questions, artifacts — plus `crud` and `roles`.
5. Add `requires: [AISMM @ pinned ref]` so federation is registry-visible rather than prose.
6. Resolve `ver-cy` vs `orkestron-ai` provenance with the owner before any canonical label.
7. Flip `installable` only after fixtures execute. Nothing in this dossier supports that flip.

## Invariants

1. **No product internals.** Membership/dependency records may hold refs, typed edges, ownership and criticality; any field that duplicates an AISMM bundle is a violation.
2. **Pinned versions.** Every dependency edge pins both endpoints to immutable refs; unpinned edges are visible and non-canonical.
3. **Visible incompleteness.** Absence is represented explicitly (unknown/not-applicable with reason); no silent empty result.
4. **Single product master.** One authoritative `productRef` per membership; duplicate product identities are rejected.
5. **Non-destructive lifecycle.** Withdrawals tombstone; recorded impact answers keep their `as_of` and coverage.

## Scenario walkthrough

**Negative — "legacy install is the canonical landscape."** Rejected. `installable: false`; `bundles: []` means `LandscapeMembership` and `LandscapeDependency` have no definitions to instantiate; `crud: {}` and `roles: []` mean no write authority or lifecycle exists; `migrationNotes` states findings, questions, artifacts, CRUD and roles are absent. The digest makes that emptiness reproducible, not correct. Calling it canonical would return empty impact graphs indistinguishable from "no impact" — violating invariant 3.

**Acceptance — three products + shared platform.** Four memberships (P1, P2, P3, Platform), each `productRef` + `aismmRef`, no new `SoftwareProduct`. Edges: P1 `depends_on` Platform (both pinned), P2 `consumes_from` Platform (both pinned), P3 `depends_on` Platform (`declared`, target pin missing). Query "change Platform": returns P1, P2 as pinned-confirmed; P3 as affected-but-unpinned; `limits` lists the missing pin, any stale source, and open questions ("which Platform revision does P3 consume?"). Impact graph plus visible gaps, product internals untouched.

## Gaps and publication holds

- No fixtures run; **no installability or compatibility claim** for PLMM or AISMM.
- AISMM pinned tree is 4 commits past v3.1.0; immutable-ref choice (tag vs `fe40e61`) undecided.
- No evidence linking runtime digests to repository commits.
- `requires: []` on both models: federation unproven in the registry.
- `ver-cy` vs `orkestron-ai` provenance unresolved.
- WM-XCT-039: `publishableCanonical: false`, single-provider waiver with Claude and Grok waived, nested schemas and adapters absent — unusable as a normative base; its composition targets `vr.wm-xct-001/003/037` are not in this dossier.
- `candidate_properties_from_v1` are `candidate-not-normative`.
- **ELMM appears nowhere in the dossier** despite being named in a blocking decision — its role cannot be decided here.
- Semantic crosswalk PLMM↔AISMM unverified; `published` ≠ independently reviewed.

```

## GROK INDEPENDENT STUDY

```
**Verdict.** COMPLETE RESERVED MODEL on existing runtime `vr.vercy.plmm`. Preserve `0.1.0-legacy` byte-identical and non-installable. Open a new draft version on the same identifier. No second model ID. No second SoftwareProduct. Product internals remain AISMM-owned. WM-XCT-039 is not a base dependency while held. This is standards alignment, not a new product register.

**Identity / lifecycle test.** Frozen evidence: the reserved runtime is structurally empty (no bundles, CRUD, roles or policies). The catalogue page retains it as a reference while a catalogue-native specification is completed. The pinned PLMM draft at `a8e388c21901540b71cc8479d4d6ef119c2ea276` has eleven landscape layers and states that internals stay in AISMM. EM-TEC-01 already forbids a second product and requires a single owner of internal facts. ISO 42010 / ArchiMate alignment: a landscape view is not a second architecture of the product.

- **SoftwareLandscape.** Identity: landscape-id + spec version + perimeter + architecture-state + `asOf`. Lifecycle versions the spec and generated impact results. It does not mint products. Fail if it stores AISMM internals or if a membership row is treated as a product master.

- **LandscapeMembership.** A reference record. Key: `(landscape-id, productRef, aismmRef)` plus validity interval. `productRef` is one authoritative external product identity (WM-SFT-001 and/or the product’s AISMM passport). One membership per product per landscape per interval. Two `aismmRef`s for one `productRef` at overlapping validity → `unresolved`, not two products. Fail if membership mints a local SoftwareProduct or copies components, SBOMs, APIs or owners.

- **LandscapeDependency.** Typed directed edge between memberships, not between raw product ids. Key: `(fromMembership, toMembership, dependencyType, fromPin, toPin)`. Endpoint pins are immutable. Changing a pin is a new edge. An unpinned target is a first-class state, not a missing row.

Regional deploy, runtime instance and AISMM repository are not products.

**Ownership boundary.** PLMM owns landscape identity, membership references, typed inter-product edges, completeness status and reproducible impact-query results. AISMM owns per-product internals. WM-SFT-001 remains the catalogue product aggregate. The eleven draft layers are internal structure of the new `vr.vercy.plmm` version, not eleven new catalogue IDs. Layers beyond the three types (capabilities, operations, governance, change, trust) are projections of memberships and dependencies plus external references. WM-XCT-039 may later inform a managed-service projection; it is tenant-scoped, `publishableCanonical: false`, and lacks nested schemas/adapters, so it is REFERENCE-optional at most.

**Membership and dependency keys.** Membership requires `productRef`, `aismmRef` (version **and** content digest; commit if used), validity, assertion kind (`observed` | `declared` | `inferred`), confidence and source. Unpinned `aismmRef` is an explicit gap, never silent “latest.” Dependency requires type (`uses-platform`, `integrates`, `data-flow`, `event`, `runtime-shared`), membership endpoints and immutable pins `{membership-id, productRef, aismmRef, recorded-at}`. Internal package dependencies stay in AISMM. Pin states: `pinned-current`, `pinned-stale`, `target-unpinned` / `source-unpinned`, `missing`. Unpinned ≠ absent ≠ no impact.

**Temporal / version semantics.** Landscape `asOf` is the query instant. Membership validity is the assertion interval. Pins are write-time facts. A later AISMM revision does not rewrite an edge; the old pin becomes stale relative to `asOf`. Do not float to latest AISMM. Runtime 3.1.0, the tree four commits past tag `v3.1.0`, and any 3.2 README label are not proven digest-compatible; that is why pins carry digest, not a version label alone.

**Completeness contract.** Every impact result is reproducible from `(landscape-id, asOf, pinned membership+dependency set, query seed)` and returns three parts: confirmed paths; qualified paths (unpinned, stale, missing); gap questions. Coverage class ∈ {`unknown` | `zero` | `partial` | `complete`}. Empty graph means unknown or zero coverage, not “no impact.” An empty `0.1.0-legacy` install must not be read as “nothing depends on this platform.”

**Scenario walkthrough.** Products P1, P2, P3 and platform F. Edges P1→F and P2→F fully pinned. Edge P3→F lacks target version. Platform-change query at `asOf` *t*: return P1 and P2 as confirmed paths with pins; keep P3 visible as affected-but-unpinned; do not invent a version and do not drop the edge; emit gap questions (which F version/digest does P3 bind? is P3’s `aismmRef` stale? what is landscape coverage at *t*?). No second SoftwareProduct is created for F or any Pi. If the landscape had no memberships, the result is unknown coverage, not “no dependents.” Declaring the empty reserved runtime a finished canonical landscape fails this test and the card negative case.

**Required fields / relations** (named on the completed reserved model, not new IDs): landscape `{id, scope, architecture-state, asOf, composition-version, coverage-status}`; membership `{productRef, aismmRef{version,digest}, validity, assertionKind, confidence, source}`; dependency `{type, from, to, fromPin, toPin, pinState}`; impact result `{confirmed[], qualified[], gap-questions[], coverage-status}`.

**Migration from legacy.** Keep `0.1.0-legacy` unchanged and non-installable. No instance data migrates (there is none). Consumers receive a documented successor pointer, not an implicit upgrade. The repo “v0.2.0” label at commit `a8e388c…` is evidence, not an automatic runtime version. Assign the new runtime version only after bundles, CRUD, roles, policies and completeness fixtures exist, with that commit’s digest pinned.

**Publication blockers.**
- Runtime-digest-to-commit compatibility for AISMM 3.1.0 versus the post-tag tree is unproven; membership pins cannot claim a single AISMM coordinate until that hold is explicit.
- `0.1.0-legacy` must not be marked installable or canonical.
- WM-XCT-039 remains held; do not make it a required composition edge.
- WM-SFT-001 ↔ AISMM “no second product” resolution lives on EM-TEC-01 and is still queued.
- No fixtures yet for unpinned-edge retention, empty-graph = unknown coverage, or stale-pin non-retargeting.
- Alignments to ISO 42010, ArchiMate and SBOM/PURL practice are alignments only.
- Do not invent a second PLMM identifier or a landscape-local SoftwareProduct.
```

## PROVIDER COMPARISON

```
# EM-LND-06 provider comparison

Both independent studies converge on **COMPLETE RESERVED MODEL** for the existing `vr.vercy.plmm` identifier. Both preserve `0.1.0-legacy` byte-identical and non-installable, reject a second PLMM identifier and a second `SoftwareProduct`, keep product internals in AISMM, and treat WM-XCT-039 as optional reference evidence while it is held.

Claude contributed the frozen eleven-layer boundary, non-destructive lifecycle, explicit query parameters, evidence access ceiling, source-provenance holds and the per-membership exact AISMM content pin that replaces any universal version assumption. Grok sharpened the membership/dependency natural keys, overlapping-context conflict, pin-state vocabulary, stale-pin non-retargeting, closed coverage classes, three-part impact result, product-kind exclusions and explicit successor migration.

The reconciled candidate revision 2 adopts both sets. It creates no new identifier and makes no installability or compatibility claim.

```

## RECONCILED CANDIDATE

```
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-LND-06",
  "modelId": "PLMM",
  "runtimeId": "vr.vercy.plmm",
  "slug": "vercy-plmm",
  "name": "Software Product Landscape",
  "version": "0.2.0-candidate.2",
  "entryKind": "landscape-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "legacyRelease": {
    "version": "0.1.0-legacy",
    "digest": "sha256:71003d1d674f20f73732a38c3311823a19f9ad20df442a94a7a6f0a0ef4054ce",
    "immutable": true,
    "installable": false
  },
  "sourcePin": {
    "commit": "a8e388c21901540b71cc8479d4d6ef119c2ea276",
    "describe": "a8e388c",
    "contentDigest": "sha256:050e7848b81700839264dfbca657015bcfded509195440067c36da7f057f9343",
    "snapshotRule": "Digest is over the canonical JSON serialization of the eleven frozen layer documents."
  },
  "purpose": "Represent a governed time-aware software product landscape, typed cross-product dependencies, explicit completeness and reproducible impact results without copying product identity or internals.",
  "boundary": {
    "owns": [
      "landscape identity and immutable scope versions",
      "temporal landscape-membership assertions",
      "typed dependency assertions between memberships",
      "withdrawal tombstones and assertion provenance",
      "coverage and completeness statements",
      "impact-query request identity and reproducible result evidence"
    ],
    "delegates": [
      "software-product identity and lifecycle to the referenced product master",
      "product internals to pinned AISMM product contexts",
      "deployment and runtime facts to their domain masters",
      "capability, process, organization, risk and portfolio identity to external masters",
      "tenant-scoped managed-service semantics to WM-XCT-039 when explicitly referenced"
    ],
    "excludes": [
      "a second SoftwareProduct identity",
      "copies of requirements architecture code deployment or runtime facts",
      "unqualified enterprise-wide completeness claims",
      "automatic promotion of inferred or scenario edges",
      "compatibility claims based only on equal version labels"
    ]
  },
  "bundles": [
    {
      "id": "plmm.01",
      "name": "Product membership",
      "semantics": "Landscape identity, scope, temporal membership and authoritative product references."
    },
    {
      "id": "plmm.02",
      "name": "Product relationships",
      "semantics": "Typed dependency, integration, event and data-flow edges between memberships."
    },
    {
      "id": "plmm.03",
      "name": "Capability projection",
      "semantics": "Read-only capability-to-product mappings whose capability master stays external."
    },
    {
      "id": "plmm.04",
      "name": "Cross-product process projection",
      "semantics": "Read-only process participation and routing references."
    },
    {
      "id": "plmm.05",
      "name": "Operations projection",
      "semantics": "References to external deployment, runtime, observation, incident and SLA masters."
    },
    {
      "id": "plmm.06",
      "name": "Governance projection",
      "semantics": "References to external owner, mandate, risk and compliance masters."
    },
    {
      "id": "plmm.07",
      "name": "AISMM federation",
      "semantics": "Pinned product-to-AISMM references and exposed-projection declarations."
    },
    {
      "id": "plmm.08",
      "name": "Change and evolution",
      "semantics": "Non-destructive replacement, deprecation and migration assertions."
    },
    {
      "id": "plmm.09",
      "name": "Consistency and trust",
      "semantics": "Coverage, staleness, provenance, validation state and unknown-boundary declarations."
    },
    {
      "id": "plmm.10",
      "name": "Semantic routing",
      "semantics": "Reproducible traversal request and result semantics."
    },
    {
      "id": "plmm.11",
      "name": "Portfolio projection",
      "semantics": "Read-only business-unit and product-group classifications."
    }
  ],
  "entities": {
    "Landscape": {
      "identity": [
        "landscapeId"
      ],
      "required": [
        "name",
        "perimeter",
        "scopeVersionId",
        "architectureState",
        "asOf",
        "compositionVersion",
        "coverageStatus",
        "validFrom",
        "status"
      ],
      "lifecycle": [
        "draft",
        "active",
        "superseded",
        "withdrawn"
      ]
    },
    "LandscapeMembership": {
      "identity": [
        "membershipId"
      ],
      "required": [
        "landscapeId",
        "productRef",
        "productVersionPin",
        "aismmRef",
        "validFrom",
        "recordedAt",
        "assertionKind",
        "confidence",
        "sourceRef",
        "status"
      ],
      "optional": [
        "validTo",
        "withdrawalReason"
      ],
      "lifecycle": [
        "proposed",
        "asserted",
        "withdrawn"
      ],
      "naturalKey": [
        "landscapeId",
        "productRef",
        "aismmRef.contentDigest",
        "validFrom"
      ],
      "aismmRef": {
        "required": [
          "version",
          "contentDigest"
        ],
        "optional": [
          "commit",
          "tag"
        ],
        "rule": "The content digest is authoritative. A version label or tag alone never proves compatibility."
      }
    },
    "LandscapeDependency": {
      "identity": [
        "dependencyId"
      ],
      "required": [
        "landscapeId",
        "sourceMembershipId",
        "targetMembershipId",
        "relationType",
        "sourceVersionPin",
        "targetVersionPin",
        "pinState",
        "validFrom",
        "recordedAt",
        "evidenceRefs",
        "authorityRef",
        "status"
      ],
      "optional": [
        "validTo",
        "confidence",
        "scenarioRef",
        "withdrawalReason"
      ],
      "lifecycle": [
        "proposed",
        "asserted",
        "withdrawn"
      ],
      "naturalKey": [
        "landscapeId",
        "sourceMembershipId",
        "targetMembershipId",
        "relationType",
        "sourceVersionPin.contentDigest",
        "targetVersionPin.contentDigest",
        "validFrom"
      ],
      "pinStates": [
        "pinned-current",
        "pinned-stale",
        "source-unpinned",
        "target-unpinned",
        "missing"
      ]
    },
    "CompletenessStatement": {
      "identity": [
        "statementId"
      ],
      "required": [
        "landscapeId",
        "scopeVersionId",
        "asOf",
        "coverageClass",
        "coveredSources",
        "knownMissingSources",
        "staleSources",
        "unknownBoundary",
        "evidenceRefs"
      ],
      "coverageClasses": [
        "unknown",
        "zero",
        "partial",
        "complete"
      ]
    },
    "ImpactQueryResult": {
      "identity": [
        "resultId"
      ],
      "required": [
        "landscapeId",
        "scopeVersionId",
        "query",
        "querySeed",
        "asOf",
        "confirmedPaths",
        "qualifiedPaths",
        "gapQuestions",
        "visitedMemberships",
        "traversedDependencies",
        "excludedEdges",
        "coverageStatementId",
        "evidenceDigest"
      ]
    }
  },
  "pinPolicy": {
    "canonicalEdge": "Both endpoint product versions and every referenced AISMM context must provide immutable identifier, commit or version, and content digest.",
    "aismm": "No universal AISMM tag is imposed. Each membership pins the exact product-context commit and digest it actually uses; a tag may be recorded as descriptive evidence.",
    "unresolved": "Unpinned or stale references remain visible but are excluded from canonical impact answers."
  },
  "relations": [
    {
      "target": "vr.vercy.aismm",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve pinned product-internal context without copying it or claiming global compatibility."
    },
    {
      "target": "WM-XCT-039",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve an optional tenant-scoped managed-service projection without importing service or asset mastership."
    }
  ],
  "operations": [
    {
      "id": "issue-landscape-scope",
      "effect": "Issue an immutable scope version for one landscape.",
      "authority": "landscape steward"
    },
    {
      "id": "assert-membership",
      "effect": "Assert temporal participation of one authoritative product version.",
      "authority": "landscape steward or delegated product owner"
    },
    {
      "id": "withdraw-membership",
      "effect": "End membership validity through a tombstone while retaining history.",
      "authority": "landscape steward"
    },
    {
      "id": "assert-dependency",
      "effect": "Assert one typed evidenced edge between pinned memberships.",
      "authority": "declared relationship owner"
    },
    {
      "id": "withdraw-dependency",
      "effect": "End edge validity without deletion.",
      "authority": "declared relationship owner"
    },
    {
      "id": "query-impact",
      "effect": "Produce a reproducible result with traversal parameters, exclusions and coverage limits.",
      "authority": "authorized reader"
    }
  ],
  "invariants": [
    "The existing vr.vercy.plmm identifier is reused; 0.1.0-legacy remains byte-identical, immutable and non-installable.",
    "A membership references exactly one authoritative product identity and never creates a second SoftwareProduct.",
    "Regional deployments, runtime instances and AISMM repositories are not SoftwareProducts.",
    "Product internals are referenced through immutable pins and are never copied into PLMM.",
    "One productRef cannot have overlapping active memberships with different AISMM content digests in the same landscape; the conflict resolves to unresolved.",
    "A dependency connects memberships in one landscape scope version rather than unversioned raw product names.",
    "Every canonical dependency pins both endpoint product versions and AISMM content digests and records evidence plus authority.",
    "Changing an endpoint content digest creates a new dependency assertion; an existing edge is never silently retargeted.",
    "Unpinned, stale, missing, inferred or scenario edges remain visible but are excluded from confirmed canonical paths.",
    "Unpinned, missing and no-impact are distinct states.",
    "Membership and dependency withdrawal is non-destructive and preserves predecessor evidence.",
    "Dependency successor lineage is acyclic.",
    "A query result pins landscape scope, as-of time, query seed, start nodes, relation filter, depth and cycle policy.",
    "Every result reports confirmed paths, qualified paths, gap questions and a coverage class.",
    "An empty graph means unknown or zero observed coverage and never proves zero impact.",
    "Traversal over the same pinned scope, graph and parameters yields the same evidence digest.",
    "Capability, process, organization, risk, deployment, service and portfolio identities remain external masters.",
    "An AISMM version label alone never proves content compatibility; the exact content digest is authoritative.",
    "WM-XCT-039 is optional reference evidence and never a required base while publishableCanonical is false.",
    "Access to a landscape result cannot exceed access to its contributing evidence; hidden evidence produces a qualified redacted gap.",
    "Retired products and withdrawn edges remain resolvable for historical as-of queries.",
    "The eleven PLMM layers are internal bundles of one runtime version and never create catalogue identifiers.",
    "The repository v0.2.0 label does not assign a runtime version without registry-controlled release evidence."
  ],
  "holds": [
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "The PLMM repository organization and historical runtime legacySource provenance must be reconciled before release.",
    "AISMM runtime-digest-to-repository-commit compatibility remains unproven and must stay explicit in every membership pin.",
    "WM-SFT-001 and AISMM product identity crosswalk remains dependent on EM-TEC-01.",
    "WM-XCT-039 remains optional and held; no required composition edge may be declared.",
    "Installability requires package conversion and runtime, search, resolve, package and live verification."
  ],
  "candidateRevision": 2,
  "providerReconciliation": {
    "claudeVerdict": "COMPLETE RESERVED MODEL",
    "grokVerdict": "COMPLETE RESERVED MODEL",
    "resolvedDecision": "Complete the existing reserved vr.vercy.plmm model; preserve 0.1.0-legacy byte-identical and non-installable; create no new model or runtime identifier and no second SoftwareProduct."
  },
  "temporalPolicy": {
    "queryTime": "asOf is the world-time instant evaluated by an impact query.",
    "assertionTime": "recordedAt is the record-time instant at which a membership or dependency assertion entered the landscape.",
    "interval": "Validity intervals are half-open [validFrom, validTo); absent validTo means open-ended.",
    "pinEvolution": "A changed endpoint content digest creates a successor dependency assertion. Prior assertions are never retargeted or overwritten.",
    "staleness": "A pin may be classified stale relative to asOf, but remains the historical write-time fact. Queries never float it to latest."
  },
  "relationVocabulary": [
    "uses-platform",
    "integrates",
    "data-flow",
    "event",
    "runtime-shared"
  ],
  "completenessContract": {
    "resultParts": [
      "confirmedPaths",
      "qualifiedPaths",
      "gapQuestions"
    ],
    "coverageClasses": [
      "unknown",
      "zero",
      "partial",
      "complete"
    ],
    "emptyGraphRule": "An empty graph means unknown coverage or zero observed coverage. It never proves zero impact or no dependants.",
    "canonicalRule": "Only paths whose memberships, endpoint pins, sources, authority and evidence are complete and current may be labelled confirmed.",
    "qualifiedRule": "Unpinned, stale, missing, inferred and scenario assertions remain visible as qualified paths with machine-readable reasons."
  },
  "migration": {
    "from": "0.1.0-legacy",
    "rule": "Preserve the legacy release byte-identical and non-installable. No instance migration exists because the legacy structure is empty.",
    "successor": "Consumers receive an explicit successor pointer and opt in to a separately versioned draft after bundles, CRUD, roles, policies and fixtures are complete.",
    "versionGuard": "The repository v0.2.0 label is evidence, not an automatic runtime version assignment."
  }
}

```

## RECONCILED FIXTURES

```
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "PLMM",
  "version": "0.2.0-candidate.2",
  "cases": [
    {
      "id": "confirmed-impact-path",
      "kind": "positive",
      "input": "Four pinned memberships and two evidenced dependencies.",
      "expect": "Canonical query returns confirmed paths and a bounded coverage statement."
    },
    {
      "id": "shared-platform-qualified-edge",
      "kind": "positive",
      "input": "P1 and P2 use platform F through current pins; P3 has a dependency whose target version is unpinned.",
      "expect": "P1 and P2 are confirmed, P3 remains affected-but-unpinned, and a gap question requests F version and digest."
    },
    {
      "id": "unpinned-target-retained",
      "kind": "negative",
      "input": "A target pin has no content digest.",
      "expect": "The edge remains visible as target-unpinned and cannot support a confirmed canonical path."
    },
    {
      "id": "stale-pin-no-retarget",
      "kind": "negative",
      "input": "A newer AISMM context exists after the dependency was recorded.",
      "expect": "The old pin is classified stale and stays unchanged; the system does not float it to latest."
    },
    {
      "id": "pin-change-successor",
      "kind": "positive",
      "input": "A dependency moves to a new target content digest.",
      "expect": "A new dependency assertion is created and the prior edge remains reconstructible."
    },
    {
      "id": "overlapping-aismm-contexts",
      "kind": "negative",
      "input": "One productRef has two active overlapping memberships with different AISMM content digests.",
      "expect": "The membership state is unresolved and does not create two products."
    },
    {
      "id": "empty-observation",
      "kind": "negative",
      "input": "No dependencies were observed for an incompletely covered source set.",
      "expect": "Result reports zero observed edges and unknown impact beyond the coverage boundary."
    },
    {
      "id": "legacy-empty-runtime",
      "kind": "negative",
      "input": "The empty 0.1.0-legacy runtime is interpreted as proof that nothing depends on a platform.",
      "expect": "The conclusion is rejected; the legacy runtime remains non-installable and coverage is unknown."
    },
    {
      "id": "withdrawn-history",
      "kind": "positive",
      "input": "A dependency is withdrawn after replacement.",
      "expect": "Current query excludes it while a historical as-of query still resolves it."
    },
    {
      "id": "cycle-bounded",
      "kind": "positive",
      "input": "An A-B-C-A dependency cycle exists.",
      "expect": "Traversal honors the declared cycle policy and terminates reproducibly."
    },
    {
      "id": "scenario-edge",
      "kind": "negative",
      "input": "A proposed future dependency exists only in a scenario.",
      "expect": "It stays qualified and is excluded from authoritative current-state results unless scenario mode is explicit."
    },
    {
      "id": "inferred-edge",
      "kind": "negative",
      "input": "An inferred dependency has confidence below the confirmation threshold.",
      "expect": "It appears in qualified paths with confidence and source, not in confirmed paths."
    },
    {
      "id": "restricted-evidence",
      "kind": "negative",
      "input": "One traversed edge cites evidence unavailable to the requester.",
      "expect": "The result preserves the stricter access ceiling and discloses a redacted qualified gap."
    },
    {
      "id": "repo-label-not-runtime-version",
      "kind": "negative",
      "input": "A repository v0.2.0 label is used as the runtime version without registry release evidence.",
      "expect": "Version assignment is rejected."
    },
    {
      "id": "copy-product-internals",
      "kind": "negative",
      "input": "The landscape copies components, SBOMs, APIs or owners from AISMM.",
      "expect": "The duplicated product internals are rejected."
    },
    {
      "id": "runtime-instance-as-product",
      "kind": "negative",
      "input": "A regional runtime instance is registered as a second SoftwareProduct.",
      "expect": "The identity split is rejected and the runtime stays an external reference."
    },
    {
      "id": "held-service-graph-required",
      "kind": "negative",
      "input": "WM-XCT-039 is declared a required base dependency while held.",
      "expect": "The composition is rejected; only optional reference use is allowed."
    }
  ],
  "candidateRevision": 2
}

```
