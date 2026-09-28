# Frozen semantic audit: EM-ORG-01 Company and Enterprise Group

You are the single independent frozen auditor. Use only the material below and no tools. Audit the reconciled profile after Claude/Grok comparison. Do not invent identifiers or external facts.

Required output:
1. Verdict: ACCEPT or REVISE.
2. Confirm or reject PROFILE over WM-ORG-001 and WM-ORG-012 with no new identifier.
3. List every semantic defect that could cause duplicate organization identity, false control/consolidation, mutable historical perimeter meaning, non-reproducible bitemporal views, member-mastership leakage or unsupported release claims.
4. Give exact remediation and fixture expectation for every defect.
5. Identify contradictions among dossier, providers, profile and fixtures.
6. End with a closed numbered remediation checklist.

Do not restate the whole model. Holds are not permission to weaken semantics.

## FROZEN DOSSIER

```
{
  "contour": {
    "id": "EM-ORG-01",
    "name": "Компания и группа компаний",
    "domain": "ORG",
    "kind": "subject",
    "wave": "W1",
    "scope": "Бизнес-идентичность организации и явно обоснованный периметр группы. Правосубъектность и доли принадлежат соседним моделям.",
    "candidate_types": [
      "Company",
      "EnterpriseGroup",
      "GroupMembership",
      "BusinessBoundary",
      "BrandAssociation"
    ],
    "specific_questions": [
      "Когда бизнес и правовое лицо являются одним объектом?",
      "Какие независимые периметры группы нужны управлению, консолидации и рынку?",
      "Как сохранить идентичность при ребрендинге, продаже и разделении бизнеса?"
    ],
    "proposed_invariants": [
      "Основание и дата включения обязательны",
      "Бренд не доказывает контроль",
      "Периметр группы не назначает владельца всех фактов участников"
    ],
    "negative_case": "Три компании с одинаковым брендом автоматически объединены в одно юрлицо.",
    "acceptance_scenario": "На синтетическом примере франшизы и холдинга показать разные графы бренда, управления и контроля; ребрендинг не создаёт новую личность.",
    "comparison_tracks": [
      "W3C ORG: коллективы, роли, членство и позиции",
      "GLEIF: зарегистрированная идентичность и консолидационные связи",
      "Сопоставление корпоративного управления, фактической оргструктуры и HR/ERP-представления"
    ],
    "vercy_candidates": [
      {
        "model_id": "WM-ORG-001",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "boundary-reviewed",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-ORG-012",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "ORG-01",
        "fields": [
          {
            "name": "business_name",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "purpose",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "industry",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "operating_scope",
            "value_type": "text",
            "status": "candidate-not-normative"
          }
        ]
      },
      {
        "predecessor": "ORG-04",
        "fields": [
          {
            "name": "group_name",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "boundary_basis",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "consolidation_basis",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "effective_period",
            "value_type": "interval",
            "status": "candidate-not-normative"
          }
        ]
      }
    ],
    "suggested_owner": "Корпоративный секретарь / владелец организационной модели",
    "candidate_master_systems": "Корпоративный реестр, HRIS, реестры юрлиц",
    "related_research_contours": [
      "EM-ORG-02",
      "EM-ORG-04",
      "EM-ORG-05",
      "EM-ORG-06"
    ],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "queue_reservation": {
    "sequence": 29,
    "id": "EM-ORG-01",
    "status": "queued",
    "claude_status": "not-started",
    "grok_status": "not-started",
    "boundary_decision": "pending",
    "publication_urls": [],
    "remaining_scope": "Entire research brief pending",
    "target_model_ids": [
      "WM-ORG-001",
      "WM-ORG-012"
    ]
  },
  "registry_reservations": [
    {
      "registry_id": "vr.wm-org-001",
      "record_plane": "world-model",
      "model_id": "WM-ORG-001",
      "name": "Organization",
      "alternate_names": "",
      "entry_kind": "standalone-mm",
      "origin": "grok-union-current",
      "status": "described-previous-version",
      "review_state": "migration-boundary-review",
      "nav_path": "NAV.SOC.ORG.ORG",
      "domain_tags": "SOC.ORG.ORG",
      "legacy_alias": "O1",
      "existing_spec_ref": "models/organizations/O1-organization.md",
      "parent_ids": "",
      "contains_ids": "WM-ORG-002;WM-ORG-003",
      "aligned_model_ids": "",
      "purpose": "Any organization: company, NGO, community, institution",
      "owner_or_maintainer": "the organization (via officers)",
      "source_url": "",
      "namespace_uri": "",
      "source_version_or_year": "2026-08-22",
      "source_group": "",
      "source_category": "",
      "source_format": "",
      "composition_role": "CONTAINS",
      "default_link_type": "TYPED-EDGES",
      "priority_wave": "0",
      "priority_score": "88",
      "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
      "priority_confidence": "low",
      "priority_rationale": "AI foundation: high reuse across agents and domains",
      "factor_demand": "0.92",
      "factor_data": "0.85",
      "factor_reuse": "0.92",
      "factor_interop": "0.85",
      "factor_feasibility": "0.90",
      "factor_robotics": "0.00",
      "factor_overlap": "0.05",
      "possible_duplicate_of": "",
      "shared_source_with": "",
      "relations_ref": "planning/VERCY-MODEL-RELATIONS.csv",
      "validation_flags": "",
      "provenance": "current-112 + Grok review + Claude adversarial audit"
    },
    {
      "registry_id": "vr.wm-org-012",
      "record_plane": "world-model",
      "model_id": "WM-ORG-012",
      "name": "Inter-organizational Relationship",
      "alternate_names": "",
      "entry_kind": "standalone-mm",
      "origin": "claude-plus-gap-audit",
      "status": "candidate",
      "review_state": "boundary-review-required",
      "nav_path": "NAV.SOC.ORG.REL",
      "domain_tags": "SOC.ORG.REL",
      "legacy_alias": "",
      "existing_spec_ref": "",
      "parent_ids": "WM-ORG-001",
      "contains_ids": "",
      "aligned_model_ids": "",
      "purpose": "Partnership, control, affiliation and supply relationships",
      "owner_or_maintainer": "the organization or authoritative register",
      "source_url": "",
      "namespace_uri": "",
      "source_version_or_year": "2026-08-22",
      "source_group": "",
      "source_category": "",
      "source_format": "",
      "composition_role": "",
      "default_link_type": "",
      "priority_wave": "1",
      "priority_score": "74",
      "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
      "priority_confidence": "low",
      "priority_rationale": "Partnership, control, affiliation and supply relationships",
      "factor_demand": "0.82",
      "factor_data": "0.72",
      "factor_reuse": "0.64",
      "factor_interop": "0.74",
      "factor_feasibility": "0.79",
      "factor_robotics": "0.00",
      "factor_overlap": "0.08",
      "possible_duplicate_of": "",
      "shared_source_with": "",
      "relations_ref": "",
      "validation_flags": "",
      "provenance": "Claude independent review + systematic gap audit + Claude adversarial audit"
    }
  ],
  "relationship_ledger": [
    {
      "source_model_id": "WM-ORG-001",
      "relation_type": "CONTAINS",
      "target_model_id": "WM-ORG-002",
      "instance_semantics": "Organization instance contains organizational-unit instances",
      "rationale": "Structural matryoshka",
      "review_state": "candidate"
    },
    {
      "source_model_id": "WM-ORG-001",
      "relation_type": "CONTAINS",
      "target_model_id": "WM-ORG-003",
      "instance_semantics": "Organization instance contains team instances",
      "rationale": "Operational matryoshka",
      "review_state": "candidate"
    }
  ],
  "current_specs": {
    "WM-ORG-001": {
      "source_file": "publications/wm-org-001-organization/spec.yaml",
      "source_bytes": 301830,
      "source_sha256": "ce27fcf5453fb390d7aea631ab91748404ca25968a8b3af67311bf4c65a76cf1",
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-08-23T21:50:25Z",
        "synthesisSha256": "028d2a633bcd0786942ca19af92a232a01b997a6ee26cf5484617922452043ac",
        "providerMode": "dual-provider",
        "providers": [
          "Claude",
          "Grok"
        ],
        "waivedProviders": []
      },
      "metaModel": {
        "id": "WM-ORG-001",
        "registryId": "vr.wm-org-001",
        "name": "Organization",
        "version": "0.3.0-research.1",
        "previousVersions": [],
        "entryKind": "entity",
        "family": "World Models",
        "category": "Society, people and institutions",
        "industry": [
          "Cross-industry"
        ],
        "domain": [
          "SOC.ORG.ORG"
        ],
        "tags": [
          "organization",
          "soc.org.org"
        ],
        "status": "published"
      },
      "model": {
        "registry_id": "vr.wm-org-001",
        "model_id": "WM-ORG-001",
        "name": "Organization",
        "entry_kind": "entity",
        "purpose": "Provide the format-neutral context an agent needs to identify, classify, register, operate on and reason about any organization — company, NGO, cooperative, institution, public body, community or informal collective — independently of any storage or interface projection.",
        "scope_statement": "WM-ORG-001 models the organization as an externally addressable actor: its designations, scheme-qualified identifiers, legal form and activity classification, declared purpose and scale, formation and registry standing, lifecycle and succession, external control/ownership and official representation, physical and electronic presence, and the provenance, quality, access and interoperability governance of the organization record itself. Internal composition (units, teams), person-level records, employment relations and constitutive rule detail are delegated to sibling models. Storage in JSON, YAML, Markdown, Git, MongoDB or exposure over MCP or HTTP are projections of this semantics, never part of it.",
        "in_scope": [
          "Names and designations over time, including language, script and transliteration variants",
          "Scheme-qualified identifiers (LEI, national registration number, EUID, VAT/tax IDs, DUNS, GLN) and internal canonical keys",
          "Entity legal form, entity category/subcategory and legal personality",
          "Activity and sector classification (NACE, ISIC, national schemes) and statistical-unit alignment",
          "Declared purpose, object clause, non-profit status and scale indicators",
          "Formation act, registry entries, registration authority and registered standing",
          "Entity status vs registration status, recurring filing and renewal obligations",
          "Lifecycle events, succession, continuity and lineage across mergers, divisions and conversions",
          "External group, ownership, beneficial-ownership and control relationships as endpoints",
          "Official organizational roles and authorised representation at organization level",
          "Registered office, operating sites, branches and electronic addresses/channels",
          "Record provenance, corroboration level, data quality, disclosure classification, retention and standard crosswalks"
        ],
        "out_of_scope": [
          "Internal organizational units, divisions and departments (WM-ORG-002)",
          "Teams and operational groupings (WM-ORG-003)",
          "Natural persons as subjects, including officer and beneficial-owner person records",
          "Employment, appointment and contractor relations as person-to-organization records",
          "Full constitutive rule text, bylaws, powers and decision procedures (charter model)",
          "The public register as an institution, its governance and its own lifecycle",
          "Financial statements, tax positions, products, services and contracts",
          "Physical facility, property and premises detail beyond the presence pointer",
          "Trademark and brand rights over names",
          "Access-grant issuance and stewardship mechanics (service models)"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-002 Organizational Unit",
            "distinction": "W3C ORG separates FormalOrganization (legally recognised, can hold external identifiers and be a party) from OrganizationalUnit, which exists only within a larger organization. Test: if the subject can independently hold a registry entry or a scheme-issued identifier, it belongs here; otherwise it is a unit. Branches are the hard case — a branch may hold its own LEI (EntityCategory BRANCH) yet is not a separate legal person, so it is modelled here as a categorised organization record linked by IS_INTERNATIONAL_BRANCH_OF rather than as an internal unit.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003"
            ]
          },
          {
            "neighbor": "WM-ORG-003 Team",
            "distinction": "A team is an operational grouping with no external legal or registry standing and no scheme-qualified identifier. Teams are contained instances, never subjects of registration, standing or succession findings in this model.",
            "source_refs": [
              "SRC-001"
            ]
          },
          {
            "neighbor": "Statistical enterprise / enterprise group",
            "distinction": "Eurostat's business-register recommendations treat the legal unit and the statistical enterprise as different units: an enterprise may combine several legal units, and enterprise-group boundaries follow control, not legal personality. This model's subject is the organization-as-actor; statistical-unit membership is recorded as a classification alignment, never as identity, and must not be used to merge or split organization records.",
            "source_refs": [
              "SRC-015",
              "SRC-008"
            ]
          },
          {
            "neighbor": "Person / sole proprietor",
            "distinction": "GLEIF EntityCategory SOLE_PROPRIETOR recognises a business subject whose legal person is a natural person. The natural person remains a separate subject in the person model; this model holds only the business-facing record and the link.",
            "source_refs": [
              "SRC-002"
            ]
          },
          {
            "neighbor": "Public register (register-as-institution)",
            "distinction": "Registration authorities are themselves organizations and are enumerated in a governed registry (GLEIF RA list, 1,050+ registers, 232 jurisdictions). This model stores a reference to the authority code and the entry, not the register's own model content.",
            "source_refs": [
              "SRC-005"
            ]
          },
          {
            "neighbor": "Beneficial owner (person) records",
            "distinction": "BODS separates entity records, person records and relationship records. Only entity records and the organization-side endpoints of relationship records are in scope; person records and their personal data are delegated, because they carry different privacy, access and retention obligations.",
            "source_refs": [
              "SRC-011"
            ]
          },
          {
            "neighbor": "Site / place / address model",
            "distinction": "W3C ORG hasSite/hasRegisteredSite point at Site, which is itself a locatable thing. This model holds the presence assertion (kind, validity, role of the location) and references the place model for geometry, building and postal-normalisation detail.",
            "source_refs": [
              "SRC-001",
              "SRC-002"
            ]
          },
          {
            "neighbor": "Fund / sub-fund structures",
            "distinction": "GLEIF EntityCategory FUND with IS_SUBFUND_OF, IS_FEEDER_TO and IS_FUND-MANAGED_BY shows that fund vehicles are organization-like subjects whose 'control' semantics are management and umbrella membership rather than ownership. They are in scope as categorised organizations but their investment semantics are not modelled here.",
            "source_refs": [
              "SRC-002",
              "SRC-003"
            ]
          },
          {
            "neighbor": "Unregistered and informal organizations",
            "distinction": "A large share of organizations (community groups, clubs, unincorporated associations, informal collectives) have no registry entry and no scheme identifier. The registration and standing bundle must therefore be optional, and identity must be able to rest on an adopting-Dimension UUID/ULID. Claiming registry-backed identity for such subjects is a modelling error, not a data gap.",
            "source_refs": [
              "SRC-001",
              "SRC-011"
            ]
          }
        ]
      },
      "structure_index": [
        {
          "id": "identity-and-designation",
          "name": "Identity and designation",
          "description": "Everything needed to say which organization is being referred to: its names across time, language and script; its identifiers under external schemes; the canonical key the adopting Dimension uses; and the evidence needed to resolve or reject a candidate match.",
          "layers": [
            {
              "id": "naming-and-designations",
              "name": "Naming and designations",
              "description": "Legal, trading, former, abbreviated and transliterated names of the organization, each with language, script, kind and validity in time."
            },
            {
              "id": "identifier-schemes-and-keys",
              "name": "Identifier schemes and canonical keys",
              "description": "Externally issued, scheme-qualified identifiers for the organization, and the internal canonical key used when no authoritative identifier exists."
            }
          ]
        },
        {
          "id": "classification-form-and-purpose",
          "name": "Classification, legal form and declared purpose",
          "description": "How the organization is typed by governed code lists (legal form, entity category, activity, statistical unit) and what it declares about its own purpose, non-profit character and scale.",
          "layers": [
            {
              "id": "legal-form-and-category",
              "name": "Legal form and entity category",
              "description": "The organization's legal form under its jurisdiction of formation, its entity category and subcategory, and whether it has separate legal personality at all."
            },
            {
              "id": "activity-and-statistical-classification",
              "name": "Activity and statistical classification",
              "description": "Coded economic-activity assignments under versioned schemes, and the organization's relationship to statistical units used by official registers."
            },
            {
              "id": "declared-purpose-and-scale",
              "name": "Declared purpose and scale",
              "description": "What the organization states about its own mission, non-profit character and size, and how those self-declarations are dated and evidenced."
            }
          ]
        },
        {
          "id": "registration-standing-and-lifecycle",
          "name": "Formation, registration standing and lifecycle",
          "description": "How the organization came into existence, where it is recorded, what its current standing is, what recurring obligations keep that standing alive, and how it changes or ends.",
          "layers": [
            {
              "id": "formation-and-registry-entries",
              "name": "Formation and registry entries",
              "description": "The constitutive act that created the organization and the entries that public and private registers hold about it."
            },
            {
              "id": "standing-status-and-obligations",
              "name": "Standing, status and recurring obligations",
              "description": "The organization's current legal standing, the separate standing of each record about it, and the periodic acts required to keep both current."
            },
            {
              "id": "lifecycle-events-and-succession",
              "name": "Lifecycle events and succession",
              "description": "Discrete events that change the organization or its record, and the lineage links that connect predecessor and successor organizations."
            }
          ]
        },
        {
          "id": "control-ownership-and-representation",
          "name": "Control, ownership and representation",
          "description": "External relationships that determine who controls the organization, who owns or benefits from it, and who may act for it.",
          "layers": [
            {
              "id": "group-structure-and-ownership",
              "name": "Group structure and ownership",
              "description": "Consolidation and group membership links, and ownership or control interests including beneficial ownership."
            },
            {
              "id": "official-roles-and-affiliation",
              "name": "Official roles, representation and affiliation",
              "description": "Who is empowered to act for the organization under law, and which external bodies the organization is affiliated with or accredited by."
            }
          ]
        },
        {
          "id": "presence-and-reachability",
          "name": "Presence and reachability",
          "description": "Where the organization is legally seated, where it actually operates, and through which electronic addresses and channels it can be reached.",
          "layers": [
            {
              "id": "locations-sites-and-channels",
              "name": "Locations, sites and channels",
              "description": "Registered and operating locations of the organization together with its electronic addresses and public channels, each with a role, validity and reachability status."
            }
          ]
        },
        {
          "id": "record-governance-and-interoperability",
          "name": "Record governance and interoperability",
          "description": "Governance of the organization record itself: where each assertion came from, how well corroborated it is, who may see it, how long it is kept, and how it maps onto external standards.",
          "layers": [
            {
              "id": "provenance-quality-and-access",
              "name": "Provenance, quality, access and retention",
              "description": "Per-assertion provenance and corroboration, data-quality assessment, disclosure classification and retention rules for the organization record."
            },
            {
              "id": "interoperability-and-mapping",
              "name": "Interoperability and mapping",
              "description": "Declared alignments to external standards and the recorded divergences between sources that assert different values for the same organization."
            }
          ]
        }
      ],
      "selected_complete_findings": [
        {
          "bundle": {
            "id": "identity-and-designation",
            "name": "Identity and designation",
            "description": "Everything needed to say which organization is being referred to: its names across time, language and script; its identifiers under external schemes; the canonical key the adopting Dimension uses; and the evidence needed to resolve or reject a candidate match."
          },
          "layer": {
            "id": "naming-and-designations",
            "name": "Naming and designations",
            "description": "Legal, trading, former, abbreviated and transliterated names of the organization, each with language, script, kind and validity in time."
          },
          "finding": {
            "id": "name-forms-and-validity",
            "name": "Name forms, kinds and validity periods",
            "description": "An organization carries several simultaneous name forms with different legal weight. LEI-CDF distinguishes LegalName from OtherEntityNames, schema.org separates legalName from name and alternateName, and BODS separates name from alternateNames. Each form needs a kind, a language tag, and an explicit validity interval because names change without changing identity.",
            "source_refs": [
              "SRC-002",
              "SRC-010",
              "SRC-011",
              "SRC-001"
            ],
            "questions": [
              "Which single name form is the legal name in the jurisdiction of formation, and which register or constitutive document evidences it?",
              "In which languages and scripts is each name form authoritative, and is any Latin transliteration normative or merely convenience?",
              "Over which interval was each name form valid, and is the interval closed, open-ended or unknown?",
              "Is the name form unique within its register, and may two distinct organizations legitimately carry the same string?"
            ],
            "data_elements": [
              {
                "id": "name-value",
                "name": "Name value",
                "description": "The literal name string exactly as recorded by the asserting source, without normalisation.",
                "value_kind": "text",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "name-kind",
                "name": "Name kind",
                "description": "Coded role of the name form: legal, trading/doing-business-as, former, abbreviation, transliteration or alternate.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "name-language-tag",
                "name": "Name language tag",
                "description": "BCP 47 language (and where needed script) tag governing the name string.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "name-validity-interval",
                "name": "Name validity interval",
                "description": "Interval during which the name form applied, with open ends permitted and precision declared.",
                "value_kind": "duration",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "identity-and-designation",
            "name": "Identity and designation",
            "description": "Everything needed to say which organization is being referred to: its names across time, language and script; its identifiers under external schemes; the canonical key the adopting Dimension uses; and the evidence needed to resolve or reject a candidate match."
          },
          "layer": {
            "id": "naming-and-designations",
            "name": "Naming and designations",
            "description": "Legal, trading, former, abbreviated and transliterated names of the organization, each with language, script, kind and validity in time."
          },
          "finding": {
            "id": "name-history-and-change",
            "name": "Name history and change tracking",
            "description": "Former names must remain retrievable and ordered, because lookups, sanctions screening and lineage tracing rely on historical strings. Companies House exposes previous_company_names as a first-class array and LEI-CDF carries name changes inside LegalEntityEvents; a purely current-state name model loses answerable history.",
            "source_refs": [
              "SRC-013",
              "SRC-002",
              "SRC-001"
            ],
            "questions": [
              "What is the ordered sequence of legal names, and which change event caused each transition?",
              "Did any recorded name change coincide with a change of legal identity rather than a mere renaming?",
              "When was each historical name observed or ingested, as distinct from when it became legally effective?"
            ],
            "data_elements": [
              {
                "id": "former-name-entry",
                "name": "Former name entry",
                "description": "A retired name with its effective-from and effective-to dates and the change event that retired it.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "name-change-event-ref",
                "name": "Name change event reference",
                "description": "Reference to the lifecycle event record that caused the name transition.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "identity-and-designation",
            "name": "Identity and designation",
            "description": "Everything needed to say which organization is being referred to: its names across time, language and script; its identifiers under external schemes; the canonical key the adopting Dimension uses; and the evidence needed to resolve or reject a candidate match."
          },
          "layer": {
            "id": "identifier-schemes-and-keys",
            "name": "Identifier schemes and canonical keys",
            "description": "Externally issued, scheme-qualified identifiers for the organization, and the internal canonical key used when no authoritative identifier exists."
          },
          "finding": {
            "id": "entity-resolution-and-duplicates",
            "name": "Entity resolution, matching evidence and duplicates",
            "description": "Governed registries themselves record duplicates — LEI RegistrationStatus includes DUPLICATE, and Companies House exposes partial_data_available and etag for concurrency. A defensible model therefore records the evidence, method and confidence behind every merge or split rather than asserting a silent match.",
            "source_refs": [
              "SRC-002",
              "SRC-013",
              "SRC-011",
              "SRC-005"
            ],
            "questions": [
              "Which attributes and sources were compared to conclude that two candidate records denote the same organization?",
              "Who decided the merge or split, when, and is the decision reversible?",
              "Does an upstream register already flag one of the records as a duplicate or annulled registration?",
              "Which candidate pairs were explicitly rejected as non-matches, so the same comparison is not repeated?"
            ],
            "data_elements": [
              {
                "id": "match-confidence",
                "name": "Match confidence",
                "description": "Declared confidence in a resolution decision, expressed on a stated scale with the scale identified.",
                "value_kind": "number",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "resolution-decision",
                "name": "Resolution decision",
                "description": "Coded outcome of an entity-resolution comparison, including explicit non-match.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "superseded-record-ref",
                "name": "Superseded record reference",
                "description": "Reference to a record retired by a merge, kept resolvable as a tombstone.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "classification-form-and-purpose",
            "name": "Classification, legal form and declared purpose",
            "description": "How the organization is typed by governed code lists (legal form, entity category, activity, statistical unit) and what it declares about its own purpose, non-profit character and scale."
          },
          "layer": {
            "id": "legal-form-and-category",
            "name": "Legal form and entity category",
            "description": "The organization's legal form under its jurisdiction of formation, its entity category and subcategory, and whether it has separate legal personality at all."
          },
          "finding": {
            "id": "entity-category-and-personality",
            "name": "Entity category, subcategory and legal personality",
            "description": "LEI-CDF categorises entities as BRANCH, GENERAL, FUND, SOLE_PROPRIETOR, RESIDENT_GOVERNMENT_ENTITY or INTERNATIONAL_ORGANIZATION, with government subcategories. Category determines which other findings are even applicable and whether the subject has separate legal personality — a branch and a sole proprietorship do not.",
            "source_refs": [
              "SRC-002",
              "SRC-001",
              "SRC-013",
              "SRC-011"
            ],
            "questions": [
              "Which entity category and subcategory apply, and which facts of the record does that category make mandatory or inapplicable?",
              "Does the organization have separate legal personality, and if not, which legal person bears its rights and obligations?",
              "Is the organization unregistered or informal, such that registration, standing and succession findings do not apply?",
              "Is this a government or international-organization subject whose formation rests on statute or treaty rather than registration?"
            ],
            "data_elements": [
              {
                "id": "entity-category",
                "name": "Entity category",
                "description": "Coded category of the organization subject, controlling applicability of other findings.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "legal-personality-flag",
                "name": "Separate legal personality flag",
                "description": "Whether the organization is itself a legal person distinct from its members or parent.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "formed-by-statute",
                "name": "Formed by statute indicator",
                "description": "Whether the organization was created by statute or treaty rather than by registration.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "classification-form-and-purpose",
            "name": "Classification, legal form and declared purpose",
            "description": "How the organization is typed by governed code lists (legal form, entity category, activity, statistical unit) and what it declares about its own purpose, non-profit character and scale."
          },
          "layer": {
            "id": "activity-and-statistical-classification",
            "name": "Activity and statistical classification",
            "description": "Coded economic-activity assignments under versioned schemes, and the organization's relationship to statistical units used by official registers."
          },
          "finding": {
            "id": "statistical-unit-alignment",
            "name": "Statistical unit alignment",
            "description": "Official registers hold enterprise group, enterprise and local unit as mandatory statistical units alongside legal units and their links, because an enterprise may span several legal units and group boundaries follow control rather than legal personality. Recording this alignment prevents an agent from silently merging legal units into one organization or splitting an organization to match a statistical unit.",
            "source_refs": [
              "SRC-015",
              "SRC-008"
            ],
            "questions": [
              "Which statistical unit types is this organization mapped to, and by which statistical authority?",
              "Does the mapped enterprise span legal units other than this organization, and which ones?",
              "Where is the group's global decision centre, and does it differ from this organization's jurisdiction?",
              "Where the statistical view and the legal view disagree, which is authoritative for a given consumer?"
            ],
            "data_elements": [
              {
                "id": "statistical-unit-type",
                "name": "Statistical unit type",
                "description": "Coded statistical unit to which this organization is mapped in an official business register.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "statistical-register-ref",
                "name": "Statistical register reference",
                "description": "Identifier of the statistical business register and the unit identifier it assigns.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "registration-standing-and-lifecycle",
            "name": "Formation, registration standing and lifecycle",
            "description": "How the organization came into existence, where it is recorded, what its current standing is, what recurring obligations keep that standing alive, and how it changes or ends."
          },
          "layer": {
            "id": "lifecycle-events-and-succession",
            "name": "Lifecycle events and succession",
            "description": "Discrete events that change the organization or its record, and the lineage links that connect predecessor and successor organizations."
          },
          "finding": {
            "id": "lifecycle-event-records",
            "name": "Lifecycle event records",
            "description": "LEI-CDF v3.1 introduced LegalEntityEvents as a container carrying event type, dates, validation documents and the fields affected. W3C ORG models ChangeEvent linked by changedBy and resultedFrom. An event record must separate the date the event legally took effect from the date it was recorded and the date it was observed.",
            "source_refs": [
              "SRC-002",
              "SRC-001",
              "SRC-014",
              "SRC-013"
            ],
            "questions": [
              "What type of lifecycle event occurred, and which fields of the organization record does it affect?",
              "What are the event's effective date, its recorded date at the authority, and the observation time in this system?",
              "Which validation documents evidence the event, and who validated them?",
              "Is the event completed, in progress or withdrawn, and can it be superseded by a later correction?"
            ],
            "data_elements": [
              {
                "id": "event-type-code",
                "name": "Lifecycle event type code",
                "description": "Coded event type such as name change, legal form conversion, seat transfer, merger, division, dissolution or status change.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "event-effective-date",
                "name": "Event effective date",
                "description": "Date on which the event took legal effect, distinct from its recording and observation times.",
                "value_kind": "date",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "event-observed-at",
                "name": "Event observation timestamp",
                "description": "RFC 3339 timestamp with explicit offset recording when this system learned of the event.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "event-affected-fields",
                "name": "Affected fields",
                "description": "List of record fields whose values the event changes.",
                "value_kind": "collection",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "registration-standing-and-lifecycle",
            "name": "Formation, registration standing and lifecycle",
            "description": "How the organization came into existence, where it is recorded, what its current standing is, what recurring obligations keep that standing alive, and how it changes or ends."
          },
          "layer": {
            "id": "lifecycle-events-and-succession",
            "name": "Lifecycle events and succession",
            "description": "Discrete events that change the organization or its record, and the lineage links that connect predecessor and successor organizations."
          },
          "finding": {
            "id": "succession-and-continuity",
            "name": "Succession, continuity and lineage",
            "description": "W3C ORG treats an organization resulting from a change event as sufficiently distinct to have its own identity, linked to originalOrganization; LEI-CDF carries SuccessorEntity with SuccessorLEI or SuccessorEntityName; Eurostat register practice defines continuity rules for unit births and deaths. The hard question is when a change preserves identity and when it creates a new subject.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-015",
              "SRC-013"
            ],
            "questions": [
              "Did this change preserve the organization's identity, or did it terminate one subject and create another?",
              "Which organizations are predecessors and which are successors, and what is the cardinality of the transition?",
              "If a successor exists but has no identifier, how is it recorded without inventing one?",
              "Which identifiers, registrations, obligations and relationships transfer to the successor and which lapse?"
            ],
            "data_elements": [
              {
                "id": "successor-reference",
                "name": "Successor reference",
                "description": "Identifier of a successor organization, or its name where no identifier exists.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "predecessor-reference",
                "name": "Predecessor reference",
                "description": "Identifier of a predecessor organization from which this subject resulted.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "continuity-decision",
                "name": "Continuity decision",
                "description": "Coded determination of whether identity was preserved across the transition, with the rule applied.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "control-ownership-and-representation",
            "name": "Control, ownership and representation",
            "description": "External relationships that determine who controls the organization, who owns or benefits from it, and who may act for it."
          },
          "layer": {
            "id": "group-structure-and-ownership",
            "name": "Group structure and ownership",
            "description": "Consolidation and group membership links, and ownership or control interests including beneficial ownership."
          },
          "finding": {
            "id": "consolidation-and-group-links",
            "name": "Consolidation, branch and fund relationship links",
            "description": "RR-CDF records IS_DIRECTLY_CONSOLIDATED_BY, IS_ULTIMATELY_CONSOLIDATED_BY, IS_INTERNATIONAL_BRANCH_OF, IS_FUND-MANAGED_BY, IS_SUBFUND_OF and IS_FEEDER_TO, each with up to three distinct period types, a status, quantifiers with a measurement method, and eight exception reasons for when a parent cannot be reported.",
            "source_refs": [
              "SRC-003",
              "SRC-002",
              "SRC-015"
            ],
            "questions": [
              "Which relationship type connects this organization to the other party, and in which direction?",
              "Which distinct periods apply — relationship validity, accounting period and document filing period — and do they differ?",
              "What quantified measure describes the relationship, and by which measurement method and unit?",
              "If no parent can be reported, which exception reason applies and when will it be reviewed?"
            ],
            "data_elements": [
              {
                "id": "relationship-type-code",
                "name": "Relationship type code",
                "description": "Coded organization-to-organization relationship such as direct or ultimate consolidation, branch, fund management, sub-fund or feeder.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "relationship-period",
                "name": "Relationship period",
                "description": "A typed interval qualifying the relationship, with the period type declared.",
                "value_kind": "duration",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "relationship-quantifier",
                "name": "Relationship quantifier",
                "description": "Quantified measure of the relationship with its measurement method and unit.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "reporting-exception-reason",
                "name": "Reporting exception reason",
                "description": "Coded reason a required parent relationship is not reported.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "control-ownership-and-representation",
            "name": "Control, ownership and representation",
            "description": "External relationships that determine who controls the organization, who owns or benefits from it, and who may act for it."
          },
          "layer": {
            "id": "group-structure-and-ownership",
            "name": "Group structure and ownership",
            "description": "Consolidation and group membership links, and ownership or control interests including beneficial ownership."
          },
          "finding": {
            "id": "ownership-and-beneficial-ownership",
            "name": "Ownership and beneficial-ownership interests",
            "description": "BODS models ownership and control as relationship records with a subject entity, an interested party, and an array of interests each carrying type, directOrIndirect, a beneficialOwnershipOrControl flag valid only for natural persons, share values expressible as exact figures or as minimum/maximum ranges, and start and end dates. Indirect chains are represented through component records rather than collapsed edges.",
            "source_refs": [
              "SRC-011",
              "SRC-010",
              "SRC-003"
            ],
            "questions": [
              "What type of interest does the interested party hold, in what amount or range, and is it held directly or indirectly?",
              "Is this interest asserted as beneficial ownership or control by a natural person, and under which jurisdiction's threshold?",
              "Where the interested party is unknown or unspecified, what reason is recorded and what is the follow-up?",
              "For an indirect interest, which component records describe each step of the ownership chain?",
              "Who asserted this ownership statement, on what date, from which source type, and under what licence is it published?"
            ],
            "data_elements": [
              {
                "id": "interest-type",
                "name": "Interest type",
                "description": "Coded kind of ownership or control interest, such as shareholding, voting rights or right to appoint directors.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "interest-share",
                "name": "Interest share",
                "description": "Share of the interest expressed as an exact percentage or as a bounded range with inclusive or exclusive limits.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "interested-party-ref",
                "name": "Interested party reference",
                "description": "Reference to the person or organization holding the interest, or an explicit unspecified-party marker.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "statement-date",
                "name": "Statement date",
                "description": "Date or RFC 3339 date-time at which the ownership statement was made, distinct from the interest start date.",
                "value_kind": "timestamp",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "control-ownership-and-representation",
            "name": "Control, ownership and representation",
            "description": "External relationships that determine who controls the organization, who owns or benefits from it, and who may act for it."
          },
          "layer": {
            "id": "official-roles-and-affiliation",
            "name": "Official roles, representation and affiliation",
            "description": "Who is empowered to act for the organization under law, and which external bodies the organization is affiliated with or accredited by."
          },
          "finding": {
            "id": "external-affiliation-and-accreditation",
            "name": "External affiliation, membership and accreditation",
            "description": "Organizations belong to federations, chambers, standards bodies and networks, and hold accreditations or certifications granted by external bodies. W3C ORG models Membership as an n-ary relation between agent, organization and role; schema.org exposes memberOf and hasCredential. These links are neither ownership nor control and must not be conflated with them.",
            "source_refs": [
              "SRC-001",
              "SRC-010",
              "SRC-013"
            ],
            "questions": [
              "Which external body is the organization affiliated with or accredited by, and what is that body's own identifier?",
              "What rights, obligations or claims does the affiliation confer, and is it publicly verifiable?",
              "Over which period is the affiliation or accreditation valid, and what triggers its lapse or withdrawal?",
              "Is this link genuinely non-controlling, or does it in substance confer control that belongs in the ownership layer?"
            ],
            "data_elements": [
              {
                "id": "affiliation-type",
                "name": "Affiliation type",
                "description": "Coded kind of external link such as association membership, accreditation, certification or network participation.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "affiliating-body-ref",
                "name": "Affiliating body reference",
                "description": "Scheme-qualified identifier of the external body conferring the affiliation.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "affiliation-validity",
                "name": "Affiliation validity interval",
                "description": "Period over which the affiliation or accreditation is valid.",
                "value_kind": "duration",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "record-governance-and-interoperability",
            "name": "Record governance and interoperability",
            "description": "Governance of the organization record itself: where each assertion came from, how well corroborated it is, who may see it, how long it is kept, and how it maps onto external standards."
          },
          "layer": {
            "id": "provenance-quality-and-access",
            "name": "Provenance, quality, access and retention",
            "description": "Per-assertion provenance and corroboration, data-quality assessment, disclosure classification and retention rules for the organization record."
          },
          "finding": {
            "id": "record-stewardship-and-change-authority",
            "name": "Record stewards",
            "description": "The organization itself, acting through officers, is the steward of its own subject record. Registers hold registrar-stewarded copies. GLEIF ManagingLOU administers the LEI record. CBV legal representatives (via schema.org and related discovery) are not the same as employment posts. This layer records stewardship of data, not corporate governance of people.",
            "source_refs": [
              "SRC-018",
              "SRC-020",
              "SRC-010"
            ],
            "questions": [
              "Who is the steward of this Dimension's organization record, in which role, and through which officer or system account?",
              "Which registrars steward authoritative copies, and which copy is master for which field group?",
              "Who is authorized to create, update or request deletion of identity fields, and under what evidence standard?"
            ],
            "data_elements": [
              {
                "id": "record-stewardship-and-change-authority-data01",
                "name": "Steward identifier",
                "description": "Organization, officer or system that stewards the record.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "record-stewardship-and-change-authority-data02",
                "name": "Master copy system",
                "description": "Which system is master for a named field group.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "record-stewardship-and-change-authority-data03",
                "name": "Authority basis",
                "description": "Legal or policy basis on which the steward acts.",
                "value_kind": "text",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        }
      ],
      "functions": [
        {
          "id": "resolve-organization-identifier",
          "name": "Resolve organization identifier",
          "description": "Resolve a scheme-qualified identifier to the canonical organization record, returning a minimal profile and the corroboration level of the answer."
        },
        {
          "id": "ingest-registry-extract",
          "name": "Ingest registry extract",
          "description": "Ingest a point-in-time extract from a named register, storing it as an immutable artifact and deriving field-level assertions with provenance."
        },
        {
          "id": "assert-lifecycle-event",
          "name": "Assert lifecycle event",
          "description": "Record a lifecycle event affecting the organization, with separate effective, authority-recording and observation times, affected fields and validation documents."
        },
        {
          "id": "evaluate-succession-continuity",
          "name": "Evaluate succession continuity",
          "description": "Decide whether a transition preserved organizational identity or created a new subject, and write the resulting lineage edges."
        },
        {
          "id": "reconcile-duplicate-records",
          "name": "Reconcile duplicate organization records",
          "description": "Compare candidate records, record the comparison evidence and confidence, and execute a merge, split or explicit non-match decision with a reversible tombstone."
        },
        {
          "id": "classify-activity",
          "name": "Assign or migrate activity classification",
          "description": "Assign an activity code under a named scheme revision, or migrate an existing assignment to a newer revision using a published correspondence table."
        },
        {
          "id": "record-control-relationship",
          "name": "Record control or ownership relationship",
          "description": "Create or update a relationship record between the organization and another party, with typed periods, quantifiers, interests and, where applicable, a reporting exception."
        },
        {
          "id": "evaluate-record-standing",
          "name": "Evaluate record standing and obligations",
          "description": "Recompute entity status, record registration status and the obligation schedule from held observations, flagging staleness and imminent lapse."
        },
        {
          "id": "publish-projection",
          "name": "Publish governed projection",
          "description": "Emit a scoped projection of the organization record — public directory card, compliance profile, lineage view or ownership disclosure — applying disclosure classification, minimisation and licence constraints."
        },
        {
          "id": "apply-retention-action",
          "name": "Apply retention or erasure action",
          "description": "Execute the retention decision for a field group or record: archive, delete, or minimise to a tombstone, with evidence of the action."
        },
        {
          "id": "map-to-external-standard",
          "name": "Map record to external standard",
          "description": "Produce an aligned representation of the organization record against a named external standard and version, declaring mapping relation types and semantic loss."
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-002 Organizational Unit",
          "relation": "CHILD",
          "purpose": "Internal divisions and departments of the organization are modelled as contained unit instances that resolve back to this organization's canonical key. W3C ORG's OrganizationalUnit exists only within a larger organization and cannot independently hold registry standing, so the split follows a normative distinction rather than convenience.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "WM-ORG-003 Team",
          "relation": "CHILD",
          "purpose": "Operational groupings without external legal identity are contained instances. They inherit organizational context from this model but carry no registration, standing or succession findings.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "W3C Organization Ontology (org:)",
          "relation": "ALIGN",
          "purpose": "Alignment target for Organization, FormalOrganization, OrganizationalUnit, OrganizationalCollaboration, Site, Role, Post, Membership and ChangeEvent, and for classification, purpose, identifier, subOrganizationOf, hasSite, hasRegisteredSite, resultedFrom and originalOrganization. Alignment only; no conformance is claimed.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "ISO 17442 Legal Entity Identifier and the LEI-CDF reference data model",
          "relation": "REFERENCE",
          "purpose": "Supplies the governed global identifier and the normative separation of entity status from record registration status, validation sources, legal entity events and successor references. Referenced, not embedded, because the Global LEI Index remains the authoritative source.",
          "required": false,
          "source_refs": [
            "SRC-002"
          ]
        },
        {
          "target": "GLEIF Relationship Record (RR-CDF) control relationships",
          "relation": "REFERENCE",
          "purpose": "Provides the typed, period-bounded, quantified control relationship vocabulary and the exception reasons used when a parent cannot be reported.",
          "required": false,
          "source_refs": [
            "SRC-003"
          ]
        },
        {
          "target": "ISO 20275 Entity Legal Forms code list",
          "relation": "REFERENCE",
          "purpose": "Governs the legal form value space, including the reserved codes for forms not yet listed and for entities with no separate legal form. Codes are referenced by list version and are only valid with a jurisdiction.",
          "required": false,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "ISO 5009 Official Organizational Roles code list",
          "relation": "REFERENCE",
          "purpose": "Governs the official-role value space for representation, tied to the entity legal form, and provides the normative basis for excluding internal functional titles from statutory representation claims.",
          "required": false,
          "source_refs": [
            "SRC-007"
          ]
        },
        {
          "target": "GLEIF Registration Authorities List",
          "relation": "REFERENCE",
          "purpose": "Supplies the governed register code space used to qualify every registry entry and validation source across 232 jurisdictions.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "ISO 3166 country and subdivision codes via the GLEIF accepted legal jurisdictions list",
          "relation": "REFERENCE",
          "purpose": "Constrains jurisdiction values to ISO 3166-1 alpha-2 with ISO 3166-2 subdivisions where legal forms exist only sub-nationally.",
          "required": false,
          "source_refs": [
            "SRC-006"
          ]
        },
        {
          "target": "NACE Rev. 2.1 and ISIC Rev. 5 activity classifications",
          "relation": "REFERENCE",
          "purpose": "Provide the versioned activity code spaces and the correspondence tables required for revision migration and cross-scheme comparison.",
          "required": false,
          "source_refs": [
            "SRC-008",
            "SRC-009"
          ]
        },
        {
          "target": "ISO 6523 International Code Designator register (as operated in business networks)",
          "relation": "REFERENCE",
          "purpose": "Defines the scheme-designator plus value pattern used for both qualified identifiers and electronic business addresses, and is the structural basis required for the EU European Unique Identifier.",
          "required": false,
          "source_refs": [
            "SRC-012",
            "SRC-016"
          ]
        },
        {
          "target": "Beneficial Ownership Data Standard (BODS)",
          "relation": "COMPOSE",
          "purpose": "Ownership and control statements compose with this model: entity records align to the organization record while person records and their privacy obligations are delegated. Interests, share ranges, component records and per-statement source metadata are adopted rather than re-invented.",
          "required": false,
          "source_refs": [
            "SRC-011"
          ]
        },
        {
          "target": "schema.org Organization",
          "relation": "ALIGN",
          "purpose": "Publication-side alignment for directory and web projections, confirming the identifier surface and profile fields. It is a projection vocabulary and is never treated as the semantic authority for registration or standing.",
          "required": false,
          "source_refs": [
            "SRC-010"
          ]
        },
        {
          "target": "W3C PROV-O provenance vocabulary",
          "relation": "MIX-IN",
          "purpose": "Mixed in across all findings to attribute assertions to agents, derive record versions from sources and separate event time from observation time using qualified provenance where circumstances matter.",
          "required": false,
          "source_refs": [
            "SRC-014"
          ]
        },
        {
          "target": "Public register model (register-as-institution)",
          "relation": "REFERENCE",
          "purpose": "Registration authorities are themselves organizations with their own governance, coverage and update cadence; this model references their codes and entries without absorbing their institutional model.",
          "required": false,
          "source_refs": [
            "SRC-005",
            "SRC-016"
          ]
        },
        {
          "target": "Person model",
          "relation": "REFERENCE",
          "purpose": "Officers, authorised representatives and beneficial owners are person subjects held elsewhere; this model stores only references so that personal-data access and retention rules stay in one place.",
          "required": false,
          "source_refs": [
            "SRC-011",
            "SRC-007"
          ]
        },
        {
          "target": "Charter and constitutive rules model",
          "relation": "REFERENCE",
          "purpose": "Object clauses, powers, decision procedures and amendment rules are referenced from the purpose and representation findings rather than duplicated, keeping a single authoritative text.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-011"
          ]
        },
        {
          "target": "Employment and appointment model",
          "relation": "REFERENCE",
          "purpose": "Person-to-organization working relations resolve against the identity kept here; membership and role occupancy semantics are delegated to that model.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "Place, address and facility model",
          "relation": "REFERENCE",
          "purpose": "Presence points reference place records for geometry, building identity and postal normalisation; this model keeps only the presence assertion, its role and its validity.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-002"
          ]
        },
        {
          "target": "Statistical business register units (legal unit, enterprise, enterprise group, local unit)",
          "relation": "ALIGN",
          "purpose": "Alignment only: statistical units follow control and economic activity rather than legal personality, so the mapping is recorded as a classification and must never drive merging or splitting of organization records.",
          "required": false,
          "source_refs": [
            "SRC-015",
            "SRC-008"
          ]
        },
        {
          "target": "Stewardship and access-grant service models",
          "relation": "MIX-IN",
          "purpose": "Ownership of the record and issuance of access grants over it are governed by the catalogue's service models; this model supplies the disclosure classes and scopes those services enforce.",
          "required": false,
          "source_refs": [
            "SRC-011",
            "SRC-013"
          ]
        },
        {
          "target": "Audit trail service model",
          "relation": "MIX-IN",
          "purpose": "Every lifecycle event, resolution decision, disclosure and retention action emits an audit facet, satisfying the append-only requirements stated in the artifact rules.",
          "required": false,
          "source_refs": [
            "SRC-014",
            "SRC-002"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "dual-provider",
        "activeProviders": [
          "claude",
          "grok"
        ],
        "waivedProviders": [],
        "providerPolicy": {},
        "boundaryDecision": {
          "entry_kind": "entity",
          "status": "accepted",
          "rationale": "Both providers independently returned entry_kind 'entity' and the subject behaves as one: a persistent, externally addressable subject bearing identity, classification, standing and a lifecycle, not an event, relation or service. The one live boundary divergence is control and ownership: the base retains organization-side endpoints of consolidation, group and beneficial-ownership relationship records while Grok delegates them entirely to a sibling. Adjudicated in favour of the base, because BODS itself separates entity records, person records and relationship records, so keeping only the entity-side endpoint is evidenced rather than invented, and the base already delegates person records with their distinct privacy, access and retention obligations. The ownership layer is nonetheless marked as the seam to re-test when the sibling relationship model is registered, so this acceptance is of the base's endpoint-only reading, not of a full relationship model living inside WM-ORG-001."
        },
        "decisions": [
          {
            "concept": "Base provider selection",
            "disposition": "Claude adopted as base",
            "rationale": "Nine evidenced neighbor notes, each carrying an operational discrimination test for the hard cases (branch holding its own LEI, statistical enterprise spanning legal units, sole proprietor, register-as-institution, fund and sub-fund, informal collectives, BODS person records, site and place), plus explicit prohibition rules. Grok's boundary is cleaner only where it delegates ownership wholesale, and it leaves umbrella, branch and successor relations half-inside. Size was not the deciding factor."
          },
          {
            "concept": "Control and ownership inside the organization model",
            "disposition": "Base reading retained; endpoint-only scope confirmed",
            "rationale": "Grok places beneficial ownership, shareholding and GLEIF Level 2 records entirely out of scope. The base keeps only the organization-side endpoints, which BODS supports by separating entity, person and relationship records. Retaining the endpoint preserves group and consolidation answerability without importing person-level privacy, access and retention obligations."
          },
          {
            "concept": "Home legal jurisdiction as a first-class finding",
            "disposition": "Accepted from Grok",
            "rationale": "The base makes legal form jurisdiction-dependent and cites the accepted-jurisdictions code list, yet never establishes the jurisdiction of formation as its own fact, leaving a dangling dependency and no answer for multi-register countries."
          },
          {
            "concept": "Organization formality spectrum",
            "disposition": "Accepted from Grok",
            "rationale": "The base declares a broad W3C ORG reading that admits informal collectives but implements it only as an exception question under a GLEIF category vocabulary. The W3C ORG, RegOrg and CBV three-step spectrum gives that reading real structure."
          },
          {
            "concept": "National legal form vocabulary alongside ELF",
            "disposition": "Accepted from Grok",
            "rationale": "ELF is a cross-border alignment and does not replace the home register's own form code when that register is master; the cross-border false-equivalence guard for SA, LLC and GmbH is absent from the base."
          },
          {
            "concept": "Dissolution as a terminal state distinct from succession",
            "disposition": "Accepted from Grok",
            "rationale": "The base models termination only as a transition to a successor and cannot represent cessation without one, winding-up in progress, or the rule that identifiers remain historical keys and are never reassigned."
          },
          {
            "concept": "Record stewardship and change authority",
            "disposition": "Accepted from Grok",
            "rationale": "The base's checklist claims steward coverage that no finding implements; per-field-group master assignment and authorised change agents are distinct from provenance attribution."
          },
          {
            "concept": "LEI and global identifier scheme specifics (grok lei-and-global-schemes)",
            "disposition": "Deferred, not added",
            "rationale": "The ISO 17442 eligibility test and LEI exclusivity rule are genuinely unanswerable from the base's generic scheme-qualified identifier finding, but Grok's evidence is an ISO catalogue landing page, not the normative text, and a scheme-specific finding would cut against the base's deliberate format-neutral generalisation. Re-open once ISO 17442-1:2020 normative text is readable."
          },
          {
            "concept": "National standing codes (grok national-standing-codes)",
            "disposition": "Rejected as duplicative",
            "rationale": "The base's entity-status-vs-registration-status finding already asks for qualifying status detail and the governing procedure for administration, liquidation and struck-off-pending, and already requires the source value plus a mapping loss note. Only the restoration and redomiciliation gap is genuinely new, and both providers agree no primary cross-jurisdictional schema exists for it, so it moves to deferred research rather than into structure."
          },
          {
            "concept": "Primary versus secondary activity (grok primary-versus-secondary-activity)",
            "disposition": "Rejected as duplicative",
            "rationale": "The base's activity-code-assignments finding already asks which activity is principal and by what criterion principality was determined, and separately asks whether the code was assigned by the organization, a register or a statistical authority."
          },
          {
            "concept": "Contact channels (grok contact-channels)",
            "disposition": "Rejected as duplicative",
            "rationale": "The base's electronic-addresses-and-channels finding already covers channel purpose including legal service, per-channel verification, and retirement with redirect or tombstone, on a stronger scheme-qualified footing than the schema.org-backed alternative."
          },
          {
            "concept": "Non-activity classifications (grok non-activity-classifications)",
            "disposition": "Rejected as weakly supported and overlapping",
            "rationale": "Charity and nonprofit status is already carried by the base's purpose-and-nonprofit-status finding with a granting authority and instrument. The remaining taxonomic-scheme content rests on W3C ORG plus a tier-3 schema.org reference, and Grok itself records the absence of any cross-border nonprofit classification as a gap."
          },
          {
            "concept": "Multiple co-equal legal names in multilingual jurisdictions",
            "disposition": "Accepted as a required correction to the base naming finding, not as a new finding",
            "rationale": "RegOrg and SEMIC CBV make legalName a repeatable language-tagged literal precisely because bilingual jurisdictions grant several legal names of equal standing, which contradicts the base question asking which single name form is the legal name. Adding Grok's finding would duplicate name-forms-and-validity, so this is recorded as a framing correction and carried as a publication hold instead."
          },
          {
            "concept": "Alternative-name integrity rule",
            "disposition": "Accepted as a constraint on the base naming layer, not as a new finding",
            "rationale": "RegOrg and CBV forbid storing a translation of the legal name in an alternative or trading name field. The base already separates name kinds and language tags but states no such prohibition, and a prohibition is a rule on an existing finding rather than a finding of its own."
          },
          {
            "concept": "Grok functions",
            "disposition": "All six rejected as duplicative",
            "rationale": "resolve-identifier, record-legal-entity-event and validate-current-standing map one-to-one onto the base's resolve-organization-identifier, assert-lifecycle-event and evaluate-record-standing; syndicate-directory-card and disclose-registry-extract are scoped emissions already covered by publish-projection; construct-succession-lineage is the read side of evaluate-succession-continuity and the lineage view publish-projection already names. No function addition would add capability."
          },
          {
            "concept": "Statistical unit alignment",
            "disposition": "Retained from base; no Grok equivalent",
            "rationale": "Grok has no counterpart to the Eurostat business-register distinction between legal unit, enterprise and enterprise group, nor to the prohibition on using statistical units to merge or split organization records. This is a base-only strength that the synthesis must preserve intact."
          },
          {
            "concept": "schema.org source classification disagreement",
            "disposition": "Normalised to non-primary discovery tier",
            "rationale": "The base records schema.org as a primary source at authority tier 2 while Grok records it as non-primary at tier 3. Grok's classification is the defensible one for a community vocabulary used as a discovery mapping, and both models already treat it as alignment rather than conformance."
          },
          {
            "concept": "Security dimension",
            "disposition": "Retained as a declared gap",
            "rationale": "The base marks transport security, authentication, key management and integrity signing as deliberately unmodelled because no cited primary source governs them at the semantic layer. Grok asserts no structure there either, so the honest declared gap is carried forward rather than papered over."
          }
        ],
        "publicationHolds": [
          "Source and live-version verification is incomplete and must be run before publication: every accepted source URL must be re-fetched and its version pin confirmed. The two providers cite different GLEIF URL paths for the same two documents (LEI-CDF 3.1 under /common-data-file-format/current-versions/ versus /common-data-file-format/, and the ELF list under /code-lists/ versus the bare path), so at least one variant in each pair is stale or a redirect and the canonical form must be established.",
          "Multi-profile domain validation has not been performed. The structure must be exercised against at least six distinct profiles before publication: a registered company with an LEI, an unregistered informal collective with no scheme identifier, an international branch holding its own LEI without separate legal personality, a fund with an umbrella and management relationship, a resident government entity formed by statute, and a sole proprietor whose legal person is a natural person. Coverage claims are provisional until each profile is walked end to end.",
          "The EUID and BRIS provisions carried by Commission Implementing Regulation (EU) 2021/1042 were surfaced from indexed EUR-Lex text rather than a full-text read, by the base provider's own admission. The EUID-specific data element must be treated as provisional and verified against the Official Journal before any normative reliance.",
          "FATF Recommendations 24 and 25 were unreachable (HTTP 403), so the beneficial-ownership structure rests on BODS at authority tier 2 rather than on the intergovernmental requirement it implements. The ownership layer must be re-grounded before it is published as an authority-backed structure.",
          "The base naming finding asks which single name form is the legal name, which is wrong for multilingual jurisdictions where RegOrg and SEMIC CBV make legalName a repeatable language-tagged literal with several co-equal legal names. The naming layer must be reframed to admit multiple co-equal legal names, with the RegOrg prohibition on storing translations in alternative-name fields, before that layer is published as normative.",
          "ISO 17442-1:2020 and ISO 20275 were cited from standards-catalogue landing pages, not normative text. Any statement in the synthesized model that reads as a conformance or eligibility rule derived from those standards must be marked alignment-only until the normative text is obtained.",
          "ISO 5009 is carried by the base as a tier-1 primary source for official organizational roles while the other provider records it as discovered but not fetched. The official-roles finding's specific claims (role counts, jurisdiction coverage, tie to ELF, exclusion of internal functional titles) must be confirmed against the fetched code list before publication."
        ],
        "deferredResearch": [
          "ISO 17442-1:2020 normative text, to ground LEI eligibility (whether the subject can enter contracts or is legally or financially responsible) and LEI exclusivity and non-reassignment as evidenced constraints. If confirmed, re-open the deferred grok finding lei-and-global-schemes for placement in the identifier-schemes-and-keys layer.",
          "Cross-border redomiciliation and continuation, and restoration after administrative strike-off, as event types. Both providers independently record that no primary cross-jurisdictional schema exists, so these currently sit as event hooks with no code list; find whether any regional instrument (EU mobility directive, US continuance statutes) supplies a citable vocabulary.",
          "NAICS from a first-party Bureau source, and the NAICS-to-ISIC correspondence. North American activity classification is a known regional omission and the activity layer is currently European-weighted through NACE.",
          "Core Public Organisation Vocabulary as the specialised public-body profile, to test whether the government and international-organization subjects currently handled through the GLEIF entity category and subcategory need their own evidenced structure.",
          "Organizational digital-identity credentials (verifiable credentials, organizational wallets, vLEI role credentials). Not verifiable from either retrieval pass and would need its own evidenced layer rather than being folded into identifier schemes.",
          "Series LLCs, protected-cell companies and comparable internal liability partitions, and DAOs or smart-contract collectives without a register or contract capacity. These stress the formality spectrum and the legal-personality flag and are currently recorded as gaps by both providers.",
          "Whether the ownership and control layer should remain in WM-ORG-001 as organization-side endpoints or move to a dedicated relationship sibling once that model is registered. Re-test the seam at sibling registration time rather than pre-emptively splitting now."
        ]
      },
      "statistics": {
        "sources": 22,
        "bundles": 6,
        "layers": 13,
        "findings": 33,
        "questions": 128,
        "artifacts": 24,
        "functions": 11
      }
    },
    "WM-ORG-012": {
      "source_file": "publications/wm-org-012-inter-organizational-relationship/spec.yaml",
      "source_bytes": 95392,
      "source_sha256": "6f30b72271fa4b9d6bef532f2eb217cd8c3c8a6a106d46d63cc37b4229b2c0f7",
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-09-09T20:36:09Z",
        "synthesisSha256": "5c5bac1bfd9549d932182afad4c9810489bb4489e8aa96aba4cbd4d5814921f8",
        "providerMode": "single-provider-waiver",
        "providers": [
          "Codex"
        ],
        "waivedProviders": [
          "Claude",
          "Grok"
        ]
      },
      "metaModel": {
        "id": "WM-ORG-012",
        "registryId": "vr.wm-org-012",
        "name": "Inter-organizational Relationship",
        "version": "0.3.0-research.1",
        "previousVersions": [],
        "entryKind": "relationship",
        "family": "World Models",
        "category": "Society, people and institutions",
        "industry": [
          "Cross-industry"
        ],
        "domain": [
          "SOC.ORG.REL"
        ],
        "tags": [
          "inter",
          "organizational",
          "relationship",
          "soc.org.rel"
        ],
        "status": "published"
      },
      "model": {
        "registry_id": "vr.wm-org-012",
        "model_id": "WM-ORG-012",
        "name": "Inter-organizational Relationship",
        "entry_kind": "relationship",
        "purpose": "Describe attributed, time-qualified organizational relationships without confusing affiliation, supply, consolidation and ownership.",
        "scope_statement": "A source-qualified relationship aggregate with explicit participants, kind, direction, scope and evidence. Real-world relation state, publisher record state and observer claims remain separate. Multi-party arrangements require retained membership context.",
        "in_scope": [
          "Relationship identity, endpoint roles and qualified kind",
          "Control-basis references, collaboration and exchange scope",
          "Temporal assertions, graph constraints, disputes and permitted mappings"
        ],
        "out_of_scope": [
          "Organization identity, contract execution and ownership-register mastership",
          "Customer/account and supplier-qualification lifecycles",
          "Inferring legal authority, beneficial ownership or universal transitivity from a generic link"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-001 Organization",
            "distinction": "Reference organization identities; a relationship is not either organization.",
            "source_refs": [
              "SRC-001",
              "SRC-005"
            ]
          },
          {
            "neighbor": "WM-ORG-014 and WM-ORG-015",
            "distinction": "Customer/account and supplier/partner qualification remain separate lifecycle masters; relationships provide scoped links.",
            "source_refs": [
              "SRC-005"
            ]
          },
          {
            "neighbor": "Ownership and accounting consolidation",
            "distinction": "Qualified relation kinds are not universally equivalent; person beneficial owners are out of endpoint scope.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-004"
            ]
          },
          {
            "neighbor": "Activity and contract",
            "distinction": "PROV Association qualifies activity-agent provenance, not inter-organizational partnership; contract execution stays delegated.",
            "source_refs": [
              "SRC-005",
              "SRC-006"
            ]
          }
        ]
      },
      "structure_index": [
        {
          "id": "relation-relationship-identity-and-endpoint-semantics",
          "name": "Relationship identity and endpoint semantics",
          "description": "Inter-organizational relationship identity and endpoint semantics.",
          "layers": [
            {
              "id": "relation-identity",
              "name": "Source-qualified relationship identity",
              "description": "Qualified relationship assertion for source-qualified relationship identity. Retain source scope and do not infer legal or commercial authority from its mere existence."
            },
            {
              "id": "participant-roles",
              "name": "Participants, direction and multiplicity",
              "description": "Qualified relationship assertion for participants, direction and multiplicity. Retain source scope and do not infer legal or commercial authority from its mere existence."
            }
          ]
        },
        {
          "id": "relation-relationship-basis-and-domain-extent",
          "name": "Relationship basis and domain extent",
          "description": "Inter-organizational relationship basis and domain extent.",
          "layers": [
            {
              "id": "recognition-basis",
              "name": "Basis, recognition and authority",
              "description": "Qualified relationship assertion for basis, recognition and authority. Retain source scope and do not infer legal or commercial authority from its mere existence."
            },
            {
              "id": "control-interest",
              "name": "Control and ownership interpretation",
              "description": "Qualified relationship assertion for control and ownership interpretation. Retain source scope and do not infer legal or commercial authority from its mere existence."
            }
          ]
        },
        {
          "id": "relation-collaboration-and-exchange-boundaries",
          "name": "Collaboration and exchange boundaries",
          "description": "Inter-organizational collaboration and exchange boundaries.",
          "layers": [
            {
              "id": "collaboration-scope",
              "name": "Partnership purpose and responsibilities",
              "description": "Qualified relationship assertion for partnership purpose and responsibilities. Retain source scope and do not infer legal or commercial authority from its mere existence."
            },
            {
              "id": "exchange-link",
              "name": "Supply and service linkage",
              "description": "Qualified relationship assertion for supply and service linkage. Retain source scope and do not infer legal or commercial authority from its mere existence."
            }
          ]
        },
        {
          "id": "relation-time-lifecycle-and-graph-interpretation",
          "name": "Time, lifecycle and graph interpretation",
          "description": "Inter-organizational time, lifecycle and graph interpretation.",
          "layers": [
            {
              "id": "relationship-time",
              "name": "Effective interval and record history",
              "description": "Qualified relationship assertion for effective interval and record history. Retain source scope and do not infer legal or commercial authority from its mere existence."
            },
            {
              "id": "graph-interpretation",
              "name": "Graph derivation and structural constraints",
              "description": "Qualified relationship assertion for graph derivation and structural constraints. Retain source scope and do not infer legal or commercial authority from its mere existence."
            }
          ]
        },
        {
          "id": "relation-evidence-dispute-and-stewardship",
          "name": "Evidence, dispute and stewardship",
          "description": "Inter-organizational evidence, dispute and stewardship.",
          "layers": [
            {
              "id": "assertion-evidence",
              "name": "Evidence quality and counterclaims",
              "description": "Qualified relationship assertion for evidence quality and counterclaims. Retain source scope and do not infer legal or commercial authority from its mere existence."
            },
            {
              "id": "relationship-stewardship",
              "name": "Mastership, freshness and permitted disclosure",
              "description": "Qualified relationship assertion for mastership, freshness and permitted disclosure. Retain source scope and do not infer legal or commercial authority from its mere existence."
            }
          ]
        },
        {
          "id": "relation-exchange-and-operational-acceptance",
          "name": "Exchange and operational acceptance",
          "description": "Inter-organizational exchange and operational acceptance.",
          "layers": [
            {
              "id": "external-mapping",
              "name": "Versioned external mappings",
              "description": "Qualified relationship assertion for versioned external mappings. Retain source scope and do not infer legal or commercial authority from its mere existence."
            },
            {
              "id": "maintenance-acceptance",
              "name": "Safe relationship maintenance operations",
              "description": "Qualified relationship assertion for safe relationship maintenance operations. Retain source scope and do not infer legal or commercial authority from its mere existence."
            }
          ]
        }
      ],
      "selected_complete_findings": [
        {
          "bundle": {
            "id": "relation-relationship-identity-and-endpoint-semantics",
            "name": "Relationship identity and endpoint semantics",
            "description": "Inter-organizational relationship identity and endpoint semantics."
          },
          "layer": {
            "id": "relation-identity",
            "name": "Source-qualified relationship identity",
            "description": "Qualified relationship assertion for source-qualified relationship identity. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "relation-identity-record",
            "name": "Source-qualified relationship identity record",
            "description": "Qualified relationship assertion for source-qualified relationship identity. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-004"
            ],
            "questions": [
              "Which master namespace and identifier distinguish this relationship from another relationship between the same organizations?",
              "Which versioned kind definition makes it partnership, affiliation, supply, control or another relation, and which near-neighbour kinds are excluded?",
              "Which scope qualifier distinguishes parallel relationships by service, geography, business unit or agreement without overwriting one another?"
            ],
            "data_elements": [
              {
                "id": "relation-identity-identity",
                "name": "identity",
                "description": "Proposed structured answer group: namespace,id,master. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "relation-identity-kind",
                "name": "kind",
                "description": "Proposed structured answer group: scheme,version,code,exclusions. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "relation-identity-scope",
                "name": "scope",
                "description": "Proposed structured answer group: dimensions,values,parallelRelationshipRefs. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-relationship-identity-and-endpoint-semantics",
            "name": "Relationship identity and endpoint semantics",
            "description": "Inter-organizational relationship identity and endpoint semantics."
          },
          "layer": {
            "id": "participant-roles",
            "name": "Participants, direction and multiplicity",
            "description": "Qualified relationship assertion for participants, direction and multiplicity. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "participant-roles-record",
            "name": "Participants, direction and multiplicity record",
            "description": "Qualified relationship assertion for participants, direction and multiplicity. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-001",
              "SRC-004",
              "SRC-005"
            ],
            "questions": [
              "Which organization references occupy each endpoint role and which identity resolution remains unknown or disputed?",
              "Is the relation directional, reciprocal or symmetric under its kind, and what inverse label preserves rather than changes its meaning?",
              "Is this a bilateral relation or a multi-party arrangement, and what is lost if its membership is exported as pairwise edges?"
            ],
            "data_elements": [
              {
                "id": "participant-roles-participants",
                "name": "participants",
                "description": "Proposed structured answer group: orgRefs,roles,resolution. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "participant-roles-direction",
                "name": "direction",
                "description": "Proposed structured answer group: kind,inverse. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "participant-roles-arity",
                "name": "arity",
                "description": "Proposed structured answer group: arrangementRef,participantSet,pairwiseLoss. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-relationship-basis-and-domain-extent",
            "name": "Relationship basis and domain extent",
            "description": "Inter-organizational relationship basis and domain extent."
          },
          "layer": {
            "id": "recognition-basis",
            "name": "Basis, recognition and authority",
            "description": "Qualified relationship assertion for basis, recognition and authority. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "recognition-basis-record",
            "name": "Basis, recognition and authority record",
            "description": "Qualified relationship assertion for basis, recognition and authority. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-001",
              "SRC-004",
              "SRC-006"
            ],
            "questions": [
              "What evidence establishes the claimed relation rather than merely common branding, a shared address or an unverified marketing statement?",
              "Who asserts or recognizes it, in which capacity, and does the other party confirm, contest or have no recorded position?",
              "Which governing instrument and jurisdiction qualify the assertion without transferring contract ownership or legal adjudication to this record?"
            ],
            "data_elements": [
              {
                "id": "recognition-basis-recognition",
                "name": "recognition",
                "description": "Proposed structured answer group: signals,counterexamples,evidenceRefs. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "recognition-basis-positions",
                "name": "positions",
                "description": "Proposed structured answer group: claimant,capacity,counterpartyPosition. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "recognition-basis-basis",
                "name": "basis",
                "description": "Proposed structured answer group: instrumentRefs,jurisdiction. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-relationship-basis-and-domain-extent",
            "name": "Relationship basis and domain extent",
            "description": "Inter-organizational relationship basis and domain extent."
          },
          "layer": {
            "id": "control-interest",
            "name": "Control and ownership interpretation",
            "description": "Qualified relationship assertion for control and ownership interpretation. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "control-interest-record",
            "name": "Control and ownership interpretation record",
            "description": "Qualified relationship assertion for control and ownership interpretation. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-004"
            ],
            "questions": [
              "Does the relation concern accounting consolidation, equity, votes, other control or beneficial interest, and which definition applies?",
              "What share, range, denominator, class, date and uncertainty qualify a quantitative interest instead of an unqualified percentage?",
              "Is direct or indirect control explicitly evidenced, which intermediate records support it, and which inference rules are prohibited?"
            ],
            "data_elements": [
              {
                "id": "control-interest-controlbasis",
                "name": "controlBasis",
                "description": "Proposed structured answer group: type,definition,accountingStandard. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "control-interest-interest",
                "name": "interest",
                "description": "Proposed structured answer group: value,min,max,denominator,class,asOf,uncertainty. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "control-interest-chain",
                "name": "chain",
                "description": "Proposed structured answer group: directness,components, derivationRule,prohibitedInferences. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-collaboration-and-exchange-boundaries",
            "name": "Collaboration and exchange boundaries",
            "description": "Inter-organizational collaboration and exchange boundaries."
          },
          "layer": {
            "id": "collaboration-scope",
            "name": "Partnership purpose and responsibilities",
            "description": "Qualified relationship assertion for partnership purpose and responsibilities. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "collaboration-scope-record",
            "name": "Partnership purpose and responsibilities record",
            "description": "Qualified relationship assertion for partnership purpose and responsibilities. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-001",
              "SRC-006"
            ],
            "questions": [
              "What jointly stated purpose and activity scope belong to this collaboration?",
              "Which responsibilities are attributed to each party and where are their governing mandates mastered?",
              "What limits distinguish the collaboration from a newly formed legal entity or permission for an agent to bind either party?"
            ],
            "data_elements": [
              {
                "id": "collaboration-scope-purpose",
                "name": "purpose",
                "description": "Proposed structured answer group: statement,scope,evidence. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "collaboration-scope-responsibilities",
                "name": "responsibilities",
                "description": "Proposed structured answer group: party,role, mandateRef. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "collaboration-scope-boundary",
                "name": "boundary",
                "description": "Proposed structured answer group: entityFormationRef,excludedAuthorities. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-time-lifecycle-and-graph-interpretation",
            "name": "Time, lifecycle and graph interpretation",
            "description": "Inter-organizational time, lifecycle and graph interpretation."
          },
          "layer": {
            "id": "relationship-time",
            "name": "Effective interval and record history",
            "description": "Qualified relationship assertion for effective interval and record history. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "relationship-time-record",
            "name": "Effective interval and record history record",
            "description": "Qualified relationship assertion for effective interval and record history. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-004",
              "SRC-006",
              "SRC-007"
            ],
            "questions": [
              "When did the relationship take effect and cease, at what precision, and are interval endpoints known, estimated or open?",
              "When was the assertion observed, recorded and published, distinct from its effective interval, and which revision supersedes it?",
              "Does closure mean real-world termination, publisher record retirement or correction of erroneous data, and how is that distinction retained?"
            ],
            "data_elements": [
              {
                "id": "relationship-time-validtime",
                "name": "validTime",
                "description": "Proposed structured answer group: start,end,precision,uncertainty. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "relationship-time-knowledgetime",
                "name": "knowledgeTime",
                "description": "Proposed structured answer group: observedAt,recordedAt,publishedAt,supersedes. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "relationship-time-closure",
                "name": "closure",
                "description": "Proposed structured answer group: meaning,reason,evidence. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-time-lifecycle-and-graph-interpretation",
            "name": "Time, lifecycle and graph interpretation",
            "description": "Inter-organizational time, lifecycle and graph interpretation."
          },
          "layer": {
            "id": "graph-interpretation",
            "name": "Graph derivation and structural constraints",
            "description": "Qualified relationship assertion for graph derivation and structural constraints. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "graph-interpretation-record",
            "name": "Graph derivation and structural constraints record",
            "description": "Qualified relationship assertion for graph derivation and structural constraints. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-004"
            ],
            "questions": [
              "Which kind-specific constraints permit or forbid self-links, cycles and multiple parents without imposing one universal organization tree?",
              "Which direct records, time slice and rule generated an indirect relation, and can the derived edge be reproduced separately from asserted data?",
              "What ambiguity or information loss arises from merging conflicting, incomplete or differently scoped relationship graphs?"
            ],
            "data_elements": [
              {
                "id": "graph-interpretation-graphrules",
                "name": "graphRules",
                "description": "Proposed structured answer group: profile,cardinality,cyclePolicy,selfLinkPolicy. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "graph-interpretation-derivation",
                "name": "derivation",
                "description": "Proposed structured answer group: inputRefs,asOf,ruleVersion,outputKind. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "graph-interpretation-graphloss",
                "name": "graphLoss",
                "description": "Proposed structured answer group: gaps,conflicts,scope. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-evidence-dispute-and-stewardship",
            "name": "Evidence, dispute and stewardship",
            "description": "Inter-organizational evidence, dispute and stewardship."
          },
          "layer": {
            "id": "assertion-evidence",
            "name": "Evidence quality and counterclaims",
            "description": "Qualified relationship assertion for evidence quality and counterclaims. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "assertion-evidence-record",
            "name": "Evidence quality and counterclaims record",
            "description": "Qualified relationship assertion for evidence quality and counterclaims. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-004",
              "SRC-006"
            ],
            "questions": [
              "Which attributable source, exact record and retrieval context support each relationship assertion, and what validation has actually occurred?",
              "Which contradictory assertions coexist and who may resolve their conflict under the Dimension policy rather than overwrite inconvenient evidence?",
              "Does missing data mean unknown, withheld, not reported, expired or explicit non-existence within a defined search scope?"
            ],
            "data_elements": [
              {
                "id": "assertion-evidence-evidence",
                "name": "evidence",
                "description": "Proposed structured answer group: source,recordRef,retrievedAt,validation. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "assertion-evidence-dispute",
                "name": "dispute",
                "description": "Proposed structured answer group: claims,resolutionAuthority,status. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "assertion-evidence-absence",
                "name": "absence",
                "description": "Proposed structured answer group: reason,coverageScope,searchTime. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": {
            "id": "relation-evidence-dispute-and-stewardship",
            "name": "Evidence, dispute and stewardship",
            "description": "Inter-organizational evidence, dispute and stewardship."
          },
          "layer": {
            "id": "relationship-stewardship",
            "name": "Mastership, freshness and permitted disclosure",
            "description": "Qualified relationship assertion for mastership, freshness and permitted disclosure. Retain source scope and do not infer legal or commercial authority from its mere existence."
          },
          "finding": {
            "id": "relationship-stewardship-record",
            "name": "Mastership, freshness and permitted disclosure record",
            "description": "Qualified relationship assertion for mastership, freshness and permitted disclosure. Retain source scope and do not infer legal or commercial authority from its mere existence.",
            "source_refs": [
              "SRC-004",
              "SRC-005",
              "SRC-006"
            ],
            "questions": [
              "Which system and role master this relationship record and when is review due?",
              "Which fields or endpoints are confidential, redacted or publicly reusable under a stated access policy and source license?",
              "How does a redacted projection preserve the distinction between withheld and absent information while retaining an authorized evidence trail?"
            ],
            "data_elements": [
              {
                "id": "relationship-stewardship-stewardship",
                "name": "stewardship",
                "description": "Proposed structured answer group: master,steward,reviewDue. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "relationship-stewardship-disclosure",
                "name": "disclosure",
                "description": "Proposed structured answer group: fieldClasses, policyRef,licenseRef. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "relationship-stewardship-projection",
                "name": "projection",
                "description": "Proposed structured answer group: redactions,reasonCodes,auditRef. Preserve attributed unknowns; nested executable schema and profile constraints remain a hold.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        }
      ],
      "functions": [
        {
          "id": "resolve-relationship",
          "name": "Resolve qualified relationship",
          "description": "Compare identities and scopes without merging parallel relations."
        },
        {
          "id": "inspect-relationship-graph",
          "name": "Inspect qualified graph",
          "description": "Traverse asserted or explicitly derived relationships at a declared time."
        },
        {
          "id": "record-relationship-assertion",
          "name": "Record attributed assertion",
          "description": "Append evidence-backed claim without creating a real-world agreement."
        },
        {
          "id": "revise-relationship-lifecycle",
          "name": "Append lifecycle revision",
          "description": "Separate effective termination, correction and record retirement."
        },
        {
          "id": "record-relationship-dispute",
          "name": "Register counterclaim",
          "description": "Preserve incompatible positions for authorized review."
        },
        {
          "id": "project-relationship",
          "name": "Export permitted projection",
          "description": "Apply versioned vocabulary mapping with declared losses."
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-001",
          "relation": "REFERENCE",
          "purpose": "Proposed endpoint-identity reference, not a frozen approved ledger edge.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-005"
          ]
        },
        {
          "target": "WM-ORG-014",
          "relation": "REFERENCE",
          "purpose": "Proposed customer/account lifecycle delegation where relevant.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "WM-ORG-015",
          "relation": "REFERENCE",
          "purpose": "Proposed supplier qualification delegation where relevant.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "https://www.w3.org/TR/vocab-org/",
          "relation": "ALIGN",
          "purpose": "Candidate generic links; relationship kind semantics require a profile.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "https://standard.openownership.org/en/latest/standard/reference.html",
          "relation": "ALIGN",
          "purpose": "Candidate organization-interest subset only, with explicit endpoint and component loss.",
          "required": false,
          "source_refs": [
            "SRC-004"
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
          "entry_kind": "relationship",
          "status": "accepted",
          "rationale": "One source-qualified relationship with explicit participants, direction, scope, time and assertions. Endpoint identities, ownership and commercial lifecycles remain referenced."
        },
        "decisions": [
          {
            "concept": "Relationship identity and graph",
            "disposition": "accepted with limitations",
            "rationale": "Parallel scopes, direct versus derived edges and kind-specific constraints prevent universal hierarchy assumptions."
          },
          {
            "concept": "Control, interest and partnership",
            "disposition": "accepted with limitations",
            "rationale": "Consolidation, ownership, supply and affiliation retain source definitions and cannot be inferred as equivalent."
          },
          {
            "concept": "Time and evidence",
            "disposition": "accepted",
            "rationale": "Publisher record closure differs from real-world termination; counterclaims and missing/withheld values are explicit."
          },
          {
            "concept": "Operations and composition",
            "disposition": "accepted with limitations",
            "rationale": "Record-level operations confer no commercial authority; model references remain proposed and loss-aware."
          },
          {
            "concept": "Source and executable conformance",
            "disposition": "deferred",
            "rationale": "Selected primary-source clauses inform design; exact pins, nested schemas and round-trip fixtures remain open."
          },
          {
            "concept": "Independent review",
            "disposition": "accepted with mandatory hold",
            "rationale": "Both external attempts timed out; frozen Codex self-audit is not independent review."
          }
        ],
        "publicationHolds": [
          "Claude and Grok each timed out once. Codex-only result and self-review remain reviewable-draft, never canonical.",
          "Source release pins, licenses, full RR-CDF XSD and BODS/OCDS normative constraints are not completely verified.",
          "No executable nested answer schema, identity resolver, graph-rule engine or real round-trip fixtures delivered.",
          "Jurisdiction-specific partnership, control and disclosure law remain adopter-owned profile work; no legal conclusions.",
          "Composition edges are proposed; multi-party/cyclic graph fixtures and independent review remain pending.",
          "Independent external review was explicitly waived by the repository owner; this codex-only result remains a reviewable draft."
        ],
        "deferredResearch": [
          "Independent external review and precise source/version/license pins.",
          "Executable loss-aware mapping and graph fixtures.",
          "Jurisdiction-specific relationship-kind profiles and approved typed composition."
        ]
      },
      "statistics": {
        "sources": 7,
        "bundles": 6,
        "layers": 12,
        "findings": 12,
        "questions": 36,
        "artifacts": 12,
        "functions": 6
      }
    }
  },
  "evidence_limits": [
    "Both current publications are reviewable drafts with publishableCanonical false.",
    "WM-ORG-012 used a single-provider waiver and has no independent external review.",
    "Selected findings are a keyword projection; source byte count and SHA-256 pin the complete parsed specifications.",
    "Candidate Enterprise v1 fields and registry relations are non-normative until independently accepted."
  ]
}

```

## CLAUDE STUDY

```
# Verdict

**PROFILE**, for both halves, with no identifier allocated.

- **Company** → profile over **WM-ORG-001** (constrained Organization view). No independent identity.
- **EnterpriseGroup / GroupMembership / BusinessBoundary / BrandAssociation** → profile over **WM-ORG-012**, with an alignment pointer in WM-ORG-001. A reusable group-boundary profile is expressible over WM-ORG-012 without a new model; a split trigger is stated below and is not currently met.

Not REUSE ONLY: the profile must add a kind vocabulary, perimeter-scope constraints and prohibition rules that neither spec states. Not COMPLETE RESERVED MODEL: no reserved model exists here. NEW MODEL CANDIDATE is held in reserve behind the split trigger, unallocated.

# Evidence state

Both targets are `reviewable-draft`, `publishableCanonical: false`. WM-ORG-001 is dual-provider with seven publication holds and a seam deferral; WM-ORG-012 is a single-provider Codex waiver with no independent external review and no executable schema, fixtures or source pins. Registry `mapping_status` for both is `conceptual-candidate`; WM-ORG-012's `evidence_depth` is index-and-publication-metadata only. Selected findings are a keyword projection; the SHA-256 and byte counts pin the full specs, which I have not read. This verdict is therefore a boundary disposition, not a crosswalk confirmation.

# Identity and boundary

Company fails the independent-identity test. Its v1 candidate fields land entirely inside WM-ORG-001: `business_name` → name-kind trading/DBA in `name-forms-and-validity`; `purpose` → `declared-purpose-and-scale`; `industry` → `activity-and-statistical-classification`; `operating_scope` → `locations-sites-and-channels` plus `statistical-unit-alignment`. WM-ORG-001 already admits companies, NGOs, branches, funds, sole proprietors and informal collectives under one subject with `entity-category` and `legal-personality-flag` as applicability switches. "Company" is that subject filtered to commercial legal forms — a constrained view, not a new lifecycle. The business/legal-person question ("when are they one object?") is answered by the existing category plus personality flag, not by a second identity.

Separation the profile must keep explicit, each already carried by one of the two specs: legal entity (`entity-category`, formation, standing); business organization (declared purpose, activity, presence); brand (name-kind, and WM-ORG-001 excludes trademark rights); franchise network (WM-ORG-012 collaboration scope); management perimeter (WM-ORG-012 scope dimensions); accounting consolidation perimeter (`controlBasis.accountingStandard`); ownership/control graph (`control-interest`, BODS interests); statistical enterprise group (`statistical-unit-type` + `statistical-register-ref`, alignment only). Eight distinct perimeters, no shared key.

EnterpriseGroup likewise fails independent identity today. It has no formation act, no registration standing, no filing obligations and no succession of its own — only a name, a basis, a purpose and an interval over a member set. That is a purpose-qualified projection, and WM-ORG-012 already models exactly that shape: `participant-roles.arity` carries `arrangementRef`, `participantSet` and `pairwiseLoss`, and the scope statement requires retained membership context for multi-party arrangements.

# Group membership and perimeter contract

The required five elements map onto WM-ORG-012 without gaps:

- **basis** → `recognition-basis.basis` (instrumentRefs, jurisdiction) + `control-interest.controlBasis` (type, definition, accountingStandard)
- **purpose** → `relation-identity.kind` (scheme, version, code, exclusions) + `relation-identity.scope` (dimensions, values, parallelRelationshipRefs)
- **effective interval** → `relationship-time.validTime`, with `knowledgeTime` and `closure.meaning` separating real-world end from record retirement and from correction
- **evidence** → `assertion-evidence` (source, recordRef, retrievedAt, validation; plus `dispute` and `absence` reason codes)
- **authority** → `recognition-basis.positions` (claimant, capacity, counterpartyPosition) + `relationship-stewardship` (master, steward, reviewDue)

`boundary_basis` and `consolidation_basis` become constrained values of `kind` and `controlBasis`; `effective_period` is `validTime`; `group_name` is a label on the arrangement, non-identifying and non-resolving. The perimeter is a derived set: membership records are the facts, the boundary is a query at a declared `asOf` using `graph-interpretation.derivation` (inputRefs, ruleVersion, outputKind), reproducible separately from asserted data.

# Brand/rebranding/succession

WM-ORG-012's recognition finding already asks for evidence "rather than merely common branding, a shared address or an unverified marketing statement" — the negative case is anticipated in the source spec. The profile hardens this into a prohibition: a brand edge carries `controlBasis.type = not-asserted` and may never appear in a consolidation or control derivation input set. WM-ORG-001's `external-affiliation-and-accreditation` supplies the parallel organization-side rule that affiliation is neither ownership nor control.

Rebranding: a name change is a `lifecycle-event-records` entry with a `former-name-entry` and `continuity-decision = identity preserved`. No new organization record, no identifier reassignment, no membership change unless the basis itself changed. Merger, split and sale route through `succession-and-continuity` (predecessor/successor refs, transition cardinality, rule applied). Memberships do not auto-transfer across a split: each successor's membership must be re-asserted with its own basis, interval and evidence.

# Mastership reconciliation

WM-ORG-001's adjudication retained organization-side control endpoints only, and its deferred item explicitly says to re-test the seam "at sibling registration time." WM-ORG-012 is now registered. The trigger has fired, so the profile must assign mastership rather than leave both sides asserting.

Proposed split: WM-ORG-012 masters the relationship fact — `relationship-type-code`, `relationship-period`, `relationship-quantifier` and BODS interest quantum are duplicates of `control-interest` and `relationship-time` and must be demoted in WM-ORG-001 to a non-authoritative, derived endpoint index. WM-ORG-001 retains `reporting-exception-reason`, which is an organization-side reporting obligation about the organization, not a relationship fact. WM-ORG-001's `record-stewardship-and-change-authority` already carries "Master copy system" per field group, so this declaration needs no new structure.

Registry inconsistency to resolve first: `vr.wm-org-012` records `parent_ids: WM-ORG-001` while the spec's own boundary note says "a relationship is not either organization" and its composition edge is REFERENCE. Structural parentage would make a perimeter owned by one member, contradicting the third proposed invariant.

# Invariants

1. Basis, purpose, effective interval, evidence and authority are all required on every membership; any missing one is recorded as a typed `absence` reason, never as an empty value.
2. A brand association or shared name is never admissible evidence of control, legal identity or consolidation, and is excluded from derivation inputs.
3. A perimeter assigns no mastership over any member fact; membership confers no authority to bind a member.
4. Statistical or consolidation units never drive merging or splitting of organization records (carried forward from WM-ORG-001 verbatim).
5. Rebranding preserves organization identity; only an explicit `continuity-decision` may create or terminate a subject.
6. Parallel memberships under different bases coexist via scope dimensions and never overwrite one another.
7. Derived perimeter edges are labelled, time-stamped and reproducible; asserted and derived are never merged.

# Scenario walkthrough

**Negative.** Three organizations share one brand. Collapse is blocked at four independent points: `entity-resolution-and-duplicates` requires comparison evidence, method, confidence and an explicit `resolution-decision`, and a brand string is not a scheme-qualified identifier; `name-kind` separates trading from legal name across three registry entries; the statistical-alignment prohibition forbids merge; and WM-ORG-012 rejects common branding as recognition evidence. Existing structure blocks the case — no new model is needed to prevent it.

**Acceptance.** Franchise network: star graph of brand-licence edges, `controlBasis` not asserted, no accounting standard, `boundary.excludedAuthorities` recording that franchisees cannot bind the franchisor. Holding group: DAG of consolidation edges with accounting standard, interest value with denominator, class and `asOf`, and distinct relationship/accounting/filing periods. A franchisee that is also a subsidiary appears in both graphs as parallel relationships, distinguished by scope. Rebranding the network changes name forms and brand-edge scope; it creates no organization and moves no member between perimeters.

# Profile or candidate shape

Profile artifacts, none normative: a governed `boundary_basis` code list (legal-control, accounting-consolidation, management, brand-licence/franchise, statistical, contractual-alliance) with mutual exclusions; a required-element constraint over the five membership fields; the seven invariants as machine-checkable rules; a per-field-group mastership declaration for the WM-ORG-001/WM-ORG-012 seam; and the two scenario fixtures above as acceptance tests.

**Split trigger** — promote to a new model candidate only when a perimeter (a) holds a registry-issued identifier with its own standing and filing obligations as a party in the adopting Dimension, not merely an alignment pointer; or (b) bears facts attaching to no membership and no member, such as group-level statements, obligations or succession; or (c) must occupy an endpoint in WM-ORG-012, whose endpoints are organization references today. The statistical enterprise group's register-assigned unit identifier is the nearest miss and stays alignment-only under WM-ORG-001.

# Gaps and publication holds

No legal effect, canonical status, approved relation or installability is claimed here; this is a reviewable boundary opinion over draft inputs. Blocking holds: WM-ORG-012 has no independent external review, no source pins and no fixtures, so the profile cannot be published as evidenced; the seam reconciliation changes WM-ORG-001 and reopens its adjudication; the registry `parent_ids` conflict must be resolved; trademark and brand rights are out of scope of both specs and point to an unidentified brand/IP model; franchise-specific and jurisdictional control definitions remain adopter-owned; and the full crosswalk against the pinned 301,830-byte and 95,392-byte specs has not been performed.

```

## GROK STUDY

```
**Verdict.** PROFILE over WM-ORG-001 and WM-ORG-012. No new catalogue or runtime ID. Company is a constrained 001 view. EnterpriseGroup / BusinessBoundary is a purpose-qualified 012 profile whose members reference 001. BrandAssociation is a relationship or name-form fact, not an identity. Legal personality stays on the EM-ORG-02 neighbor; ownership shares stay on EM-ORG-03. This is standards alignment, not a GLEIF, IFRS 10 or Eurostat conformance claim.

**Company identity test.** Source facts: 001 already masters externally addressable organization identity, name forms (legal, trading, former), legal-form / personality flags, statistical-unit alignment and succession. Card parks legal personality and ownership shares on neighbors. Dates, names and addresses are never keys. Many organizations are not legal entities; some umbrellas contain several.

Company does not mint a second identifier. The PROFILE constrains a 001 subject as a commercial actor: trading-name set in force, optional statistical-enterprise alignment, legal-personality flag referenced from EM-ORG-02 rather than copied. Business and legal entity coincide as *one object* only when that 001 subject also has an EM-ORG-02 registration with separate legal personality; they remain two aspects. Informal collectives stay 001 without being companies-as-legal-persons.

Fail-to-new-ID if Company copies registry attributes, treats a trading name as the key, or collapses three same-brand actors into one legal entity.

**Group identity / lifecycle.** EnterpriseGroup / BusinessBoundary is a named perimeter specification plus a generated as-of view, not a third organization. Identity: `(perimeter-id, boundaryKind, purpose, spec-version)` over the 012 membership-fact set it evaluates. Lifecycle versions the specification (which kinds count, which roles, which control basis, as-of policy). It does not mint 001 identities for “the group as actor” unless an independent constitutive organization already exists — a listed holding is already a 001 subject; the consolidation graph *around* it is the perimeter.

A materialized perimeter is a reproducible query at one `(valid-time, knowledge-time)` pair. Same pins produce the same member set. It is not a stored second master of the members and does not become owner of member facts (card invariant).

**Membership / perimeter contract.** GroupMembership is a 012 relationship under a named purpose. Every fact must carry:

1. `boundaryKind` + `purpose` ∈ {management, consolidation, ownership-control, statistical, franchise, alliance} (extensible; not a merge key).
2. Endpoint roles scoped to that kind.
3. `validTime` and `knowledgeTime`; inclusion date mandatory.
4. Recognition or control *basis* — accounting standard + consolidation class; equity / votes / contract / de facto; statistical-authority mapping; franchise instrument; alliance instrument. Basis is not inferred from brand or from another kind.
5. Evidence and claimant authority.
6. Master / steward of *this relationship* (012), distinct from endpoint mastership (001) and from 02 / 03.
7. Dispute / absence / reporting-exception status (GLEIF-style “no parent / opt-out / unknown” remains first-class).

One organization may sit in many perimeters. Graphs are not unioned before evaluation. A materialized “the group” without a declared kind is refused.

**Mastership seam.** 012 masters relationship kind, period, direction, quantifier, control / interest facts, evidence, claimant and dispute. 001 retains identity, names, succession, statistical alignment, derived endpoint *indexes* and organization-side reporting exceptions.

Challenge the registry parent 012 → 001. A relationship is not a subtype of an organization. W3C ORG membership / `org:linkedTo` relate Organizations; they are not child types. GLEIF RR-CDF is a separate record from Level 1 identity. Demote PARENT to REFERENCE (composition of endpoints only). 012 cites two or more 001 identities; it does not inherit names or legal personality. 001’s current consolidation endpoint fields become derived projections of 012 edges, not a second write path. Dual-write of the same consolidating-parent fact is a blocker until 012 is named master of that fact. Ownership *shares* remain EM-ORG-03.

**Brand / rebranding / succession.** BrandAssociation is `{orgRef, mark, role, validity, source}`. It does not prove control (card invariant; IFRS 10 alignment: typical franchise rights protect the brand, they do not confer power over returns). Rebranding updates 001 name forms with identity-continuity true; former names stay citable. Sale or split uses 001 succession plus 012 membership close / open with inclusion dates. Brand edges may persist across a sale if the mark transfers; that does not merge successor with predecessor. Statistical-enterprise alignment on 001 blocks silently merging legal units into “the company.”

**Scenario results.**

1. *Three organizations share one brand.* Three 001 identities remain. BrandAssociation edges connect each to the mark. No control or consolidation edge is inferred. Auto-merge into one legal entity fails the negative case.

2. *Franchise network versus holding / consolidation group.* Franchise graph: kind = franchise / affiliation; basis = licence; purpose = brand-system; control = false unless separately evidenced. Holding graph: kind = control / consolidation; basis = accounting standard + interest; purpose = consolidation; GLEIF L2 analogue. Management graph: kind = direction; basis = mandate; purpose = management. Three queries over the same store yield three graphs. A brand-only member does not appear in the consolidation perimeter.

3. *Rebranding of one franchisee.* 001 identity unchanged; former name retained; BrandAssociation may update. Holding perimeter unchanged unless a control fact also changed.

**Split trigger for a true group subject.** Mint a group-as-actor only if all hold: (1) an identifier that is not any member’s 001 id and not a query digest (register-issued enterprise-group number that outlives particular edges); (2) obligations or legal capacity that are not those of any member and not EM-ORG-02; (3) other models must master the group without going through 012. Today none are proven. That actor would still be a **001 instance**, not a new catalogue type; membership graphs stay 012. Eurostat “enterprise group” can be the *result* of a purpose = statistical query over control links.

**Required constraints.** Company = 001 profile, not a second identity. Every membership carries kind, purpose, roles, bitemporal interval, basis, evidence, claimant, steward, dispute / absence. Do not infer control from brand. Do not union perimeters. 012 REFERENCE 001, not PARENT. Perimeter does not own member facts.

**Publication blockers.** Both bases are non-canonical reviewable drafts; 012 lacks independent review and executable fixtures. 012 has no franchise kind and no named perimeter-profile object — PROFILE fields, not new IDs. 001 still writes ownership / control endpoints pending the sibling-seam retest it already declared. Dual-write of consolidating-parent facts is unresolved. No fixtures for three-org brand non-merge, franchise ≠ holding, rebranding continuity, or as-of reproducibility with reporting exceptions. Alignments to GLEIF L2, IFRS 10, W3C ORG and Reg. 696/93 are alignments only. Do not invent Company, EnterpriseGroup or BrandAssociation runtime identifiers.

```

## PROVIDER COMPARISON

```
# EM-ORG-01 provider comparison

+Claude and Grok independently converge on **PROFILE** over `WM-ORG-001` and `WM-ORG-012`, with no new catalogue or runtime identifier. Company remains a constrained organization view. EnterpriseGroup / BusinessBoundary remains a purpose-qualified relationship perimeter and reproducible bitemporal projection.

+Both providers reject identity inference from a shared brand, name, site or affiliation; preserve rebranding continuity; separate management, consolidation, ownership/control, statistical, franchise and alliance graphs; and require explicit membership basis, evidence, authority, stewardship and dispute/absence semantics.

+Grok sharpens the boundary by naming a perimeter-specification identity, requiring inclusion dates, refusing an unqualified union graph, demoting the registry parent relation from WM-ORG-012 to WM-ORG-001 into a reference, and keeping legal personality and ownership shares with sibling models. It also states a strict split trigger: any true group actor would still be a WM-ORG-001 instance after independent identity, obligations/capacity and external mastership are proven. These refinements do not change the PROFILE decision.
+
```

## PROFILE

```
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-ORG-01",
  "name": "Company and Enterprise Group Boundary",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ORG-001",
    "WM-ORG-012"
  ],
  "constraints": [
    "Company is a constrained WM-ORG-001 view and never a parallel organization identity.",
    "Dates, names, addresses, brands, sites and affiliations are never organization identity keys.",
    "Legal personality and registration facts remain external sibling aspects and are never copied into the Company profile.",
    "EnterpriseGroup / BusinessBoundary is a versioned perimeter specification and reproducible view over WM-ORG-012 facts, not a third organization.",
    "A perimeter specification is identified by perimeter id, boundary kind, purpose and specification version.",
    "Every membership carries kind, purpose, endpoint roles, valid time, knowledge time, inclusion date, basis, evidence, claimant authority, relationship steward and dispute/absence status.",
    "Management, consolidation, ownership-control, statistical, franchise and alliance perimeters are evaluated independently and never implicitly unioned.",
    "Recognition, control or consolidation is never inferred from brand or from a different boundary kind.",
    "WM-ORG-012 masters relationship facts; WM-ORG-001 retains identity, names, succession, statistical alignment and derived endpoint indexes only.",
    "The WM-ORG-012 to WM-ORG-001 registry parent claim is proposed for demotion to a non-owning reference; dual writing is forbidden.",
    "A materialized perimeter pins valid time, knowledge time, specification version, input fact ids and digests, rule version and result digest.",
    "A perimeter does not own member facts, grant authority over a member, or bind a member.",
    "Rebranding changes dated name and brand facts while preserving organization identity.",
    "Sale, merger, split and succession close and open explicit membership facts and never silently transfer them.",
    "A true group actor is represented only as a WM-ORG-001 instance after independent identity, capacity or obligations and external mastership are proven.",
    "BrandAssociation is a relationship or name-form fact and never a runtime identifier.",
    "External GLEIF, IFRS, Eurostat and W3C sources are alignment evidence only unless exact conformance evidence exists.",
    "Publication is refused while fixturesExecuted is false, publishableCanonical is false or any base/mastership hold remains open."
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-single-frozen-audit",
  "publishableCanonical": false,
  "fixturesExecuted": false,
  "perimeterKinds": [
    "management",
    "consolidation",
    "ownership-control",
    "statistical",
    "franchise",
    "alliance"
  ],
  "splitTrigger": {
    "allRequired": [
      "independent identifier not equal to a member id or query digest",
      "independent obligations or legal capacity",
      "external models must master the group without traversing WM-ORG-012"
    ],
    "result": "represent as WM-ORG-001 instance; do not mint a catalogue type"
  },
  "proposedRegistryAmendments": [
    {
      "source": "WM-ORG-012",
      "current": "PARENT -> WM-ORG-001",
      "proposed": "REFERENCE -> WM-ORG-001",
      "status": "held-pending-registry-review"
    }
  ],
  "publicationGate": {
    "publishableCanonical": false,
    "fixturesExecuted": false,
    "openHolds": [
      "both bases non-canonical",
      "WM-ORG-012 independent review and executable fixtures absent",
      "dual-write seam unresolved",
      "registry parent amendment unapproved",
      "sibling legal-personality and ownership-share boundaries must remain external"
    ]
  }
}

```

## FIXTURES

```
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Company and Enterprise Group Boundary",
  "declarativeOnly": true,
  "cases": [
    {
      "id": "shared-brand",
      "kind": "positive",
      "input": "Three organizations trade under one brand.",
      "expect": "Three identities remain; brand association creates no ownership or consolidation inference."
    },
    {
      "id": "parallel-perimeters",
      "kind": "positive",
      "input": "One organization belongs to a franchise network and an accounting group.",
      "expect": "Two independently governed memberships coexist and produce separate graphs."
    },
    {
      "id": "rebrand",
      "kind": "positive",
      "input": "A company changes its trading name.",
      "expect": "Organization identity persists; former name and dated brand association remain citable."
    },
    {
      "id": "brand-implies-control",
      "kind": "negative",
      "input": "A shared brand is used as proof of corporate control.",
      "expect": "Reject without qualified relationship evidence."
    },
    {
      "id": "silent-transfer",
      "kind": "negative",
      "input": "A sale silently transfers all memberships to a successor.",
      "expect": "Reject; close and open explicit effective assertions."
    },
    {
      "id": "unqualified-group-query",
      "kind": "negative",
      "input": "A query requests the group without boundary kind or purpose.",
      "expect": "Refuse the materialization."
    },
    {
      "id": "same-org-many-perimeters",
      "kind": "positive",
      "input": "One organization belongs to management, statistical and alliance perimeters.",
      "expect": "Keep three scoped facts and views without union inference."
    },
    {
      "id": "brand-only-excluded-from-consolidation",
      "kind": "positive",
      "input": "A franchisee shares the brand but has no control fact.",
      "expect": "Exclude it from the consolidation perimeter."
    },
    {
      "id": "bitemporal-replay",
      "kind": "positive",
      "input": "The same valid time is queried at two knowledge times after a correction.",
      "expect": "Produce two digest-pinned reproducible views."
    },
    {
      "id": "missing-inclusion-date",
      "kind": "negative",
      "input": "A membership lacks its inclusion date.",
      "expect": "Reject as incomplete membership evidence."
    },
    {
      "id": "missing-basis",
      "kind": "negative",
      "input": "A consolidation membership lacks recognition/control basis.",
      "expect": "Reject."
    },
    {
      "id": "disputed-fact",
      "kind": "positive",
      "input": "A control relationship is disputed.",
      "expect": "Keep it first-class and qualify the perimeter result."
    },
    {
      "id": "absence-status",
      "kind": "positive",
      "input": "No parent is reported under a typed exception.",
      "expect": "Preserve the absence/reporting exception without inventing a parent."
    },
    {
      "id": "relationship-as-organization",
      "kind": "negative",
      "input": "WM-ORG-012 record inherits organization names or legal personality.",
      "expect": "Reject; relationship references endpoints only."
    },
    {
      "id": "dual-write-parent",
      "kind": "negative",
      "input": "The same consolidating parent is authored in WM-ORG-001 and WM-ORG-012.",
      "expect": "Reject until one authoritative relationship master remains."
    },
    {
      "id": "perimeter-owns-member",
      "kind": "negative",
      "input": "A perimeter attempts to edit a member organization.",
      "expect": "Reject; member mastership remains WM-ORG-001."
    },
    {
      "id": "group-label-as-identity",
      "kind": "negative",
      "input": "A descriptive group label is used as the organization key.",
      "expect": "Reject."
    },
    {
      "id": "true-group-actor-trigger",
      "kind": "positive",
      "input": "A register-issued group id has independent obligations and external mastership.",
      "expect": "Create or reuse a WM-ORG-001 subject; keep membership edges in WM-ORG-012."
    },
    {
      "id": "statistical-unit-no-merge",
      "kind": "negative",
      "input": "A statistical enterprise mapping merges legal-unit identities.",
      "expect": "Reject; retain organization masters and map the statistical view."
    },
    {
      "id": "succession-with-brand-continuity",
      "kind": "positive",
      "input": "A predecessor is sold and the brand persists.",
      "expect": "Preserve succession and brand facts without identity merge."
    },
    {
      "id": "registry-parent-held",
      "kind": "negative",
      "input": "Candidate claims the parent relation is already approved.",
      "expect": "Reject; record only a proposed amendment."
    },
    {
      "id": "alignment-not-conformance",
      "kind": "negative",
      "input": "Profile claims IFRS/GLEIF/W3C conformance from alignment evidence.",
      "expect": "Reject unsupported conformance claim."
    },
    {
      "id": "release-gate",
      "kind": "negative",
      "input": "Profile is promoted while fixturesExecuted=false.",
      "expect": "Publication refused."
    }
  ]
}

```
