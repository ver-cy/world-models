# Frozen semantic audit: EM-ORG-02 Legal Identity, Registration and Presence

You are the single independent frozen auditor. Use only the material below and no tools. Audit the reconciled profile after Claude/Grok comparison. Do not invent identifiers, standards claims or external facts.

Required output:
1. Verdict: ACCEPT or REVISE.
2. Confirm or reject PROFILE over WM-ORG-001, WM-ORG-010 and WM-ORG-011 with no new identifier.
3. List every semantic defect that could cause duplicate subject identity, identifier collision, status-plane leakage, false personality, branch/obligor confusion, historical-party rewrite, non-reproducible as-of answers, mastership leakage or unsupported release claims.
4. Give exact remediation and fixture expectation for every defect.
5. Identify contradictions among dossier, providers, profile and fixtures.
6. End with a closed numbered remediation checklist.

Do not restate the whole model. Holds are not permission to weaken semantics.

## FROZEN DOSSIER
```json
{
  "contour": {
    "id": "EM-ORG-02",
    "name": "Юридическая идентичность и регистрация",
    "domain": "ORG",
    "kind": "subject",
    "wave": "W1",
    "scope": "Правовой субъект, регистрационные записи, филиалы и правопреемство. Реестровая запись имеет собственную идентичность и подтверждаемое основание.",
    "candidate_types": [
      "LegalEntity",
      "Registration",
      "Branch",
      "LegalStanding",
      "SuccessionRelation"
    ],
    "specific_questions": [
      "Какие признаки отделяют самостоятельное лицо от филиала?",
      "Как связать LEI, налоговый и регистрационный номера без ложного тождества?",
      "Какие изменения продолжают идентичность, а какие создают правопреемника?"
    ],
    "proposed_invariants": [
      "Номер уникален в схеме и юрисдикции",
      "Статус регистрации не подменяет статус субъекта",
      "Правопреемство не перезаписывает стороны старых договоров"
    ],
    "negative_case": "Новая выписка из другого реестра создаёт вторую компанию.",
    "acceptance_scenario": "Один субъект с тремя регистрациями, филиал без отдельной правосубъектности и слияние должны давать корректные ответы на историческую дату.",
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
        "model_id": "WM-ORG-010",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "boundary-reviewed",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-ORG-011",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "ORG-02",
        "fields": [
          {
            "name": "legal_name",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "legal_form",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "jurisdiction",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "formation_date",
            "value_type": "date",
            "status": "candidate-not-normative"
          }
        ]
      },
      {
        "predecessor": "ORG-03",
        "fields": [
          {
            "name": "register_uri",
            "value_type": "uri",
            "status": "candidate-not-normative"
          },
          {
            "name": "register_number",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "registered_at",
            "value_type": "date",
            "status": "candidate-not-normative"
          },
          {
            "name": "registration_status",
            "value_type": "code",
            "status": "candidate-not-normative"
          }
        ]
      },
      {
        "predecessor": "ORG-08",
        "fields": [
          {
            "name": "branch_kind",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "host_jurisdiction",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "authority_scope",
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
      "EM-COM-01",
      "EM-FIN-01",
      "EM-LEG-01",
      "EM-ORG-01",
      "EM-ORG-03",
      "EM-PEO-02"
    ],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "queue_reservation": {
    "sequence": 30,
    "id": "EM-ORG-02",
    "status": "queued",
    "claude_status": "not-started",
    "grok_status": "not-started",
    "boundary_decision": "pending",
    "publication_urls": [],
    "remaining_scope": "Entire research brief pending",
    "target_model_ids": [
      "WM-ORG-001",
      "WM-ORG-010",
      "WM-ORG-011"
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
      "registry_id": "vr.wm-org-010",
      "record_plane": "world-model",
      "model_id": "WM-ORG-010",
      "name": "Legal Entity Registration",
      "alternate_names": "",
      "entry_kind": "standalone-mm",
      "origin": "claude-plus-gap-audit",
      "status": "candidate",
      "review_state": "boundary-review-required",
      "nav_path": "NAV.SOC.ORG.REG",
      "domain_tags": "SOC.ORG.REG",
      "legacy_alias": "",
      "existing_spec_ref": "",
      "parent_ids": "WM-ORG-001",
      "contains_ids": "",
      "aligned_model_ids": "",
      "purpose": "Legal identity, jurisdiction, registers and lifecycle",
      "owner_or_maintainer": "the organization or authoritative register",
      "source_url": "",
      "namespace_uri": "",
      "source_version_or_year": "2026-08-22",
      "source_group": "",
      "source_category": "",
      "source_format": "",
      "composition_role": "",
      "default_link_type": "",
      "priority_wave": "0",
      "priority_score": "86",
      "priority_method": "cohort-proxy with model-specific robotics check; use TOP-50 sequence",
      "priority_confidence": "low",
      "priority_rationale": "Legal identity, jurisdiction, registers and lifecycle",
      "factor_demand": "0.92",
      "factor_data": "0.84",
      "factor_reuse": "0.88",
      "factor_interop": "0.82",
      "factor_feasibility": "0.88",
      "factor_robotics": "0.00",
      "factor_overlap": "0.06",
      "possible_duplicate_of": "",
      "shared_source_with": "",
      "relations_ref": "",
      "validation_flags": "",
      "provenance": "Claude independent review + systematic gap audit + Claude adversarial audit"
    },
    {
      "registry_id": "vr.wm-org-011",
      "record_plane": "world-model",
      "model_id": "WM-ORG-011",
      "name": "Business Establishment / Branch",
      "alternate_names": "",
      "entry_kind": "standalone-mm",
      "origin": "claude-plus-gap-audit",
      "status": "candidate",
      "review_state": "boundary-review-required",
      "nav_path": "NAV.SOC.ORG.EST",
      "domain_tags": "SOC.ORG.EST",
      "legacy_alias": "",
      "existing_spec_ref": "",
      "parent_ids": "WM-ORG-001",
      "contains_ids": "",
      "aligned_model_ids": "",
      "purpose": "Operational location distinct from legal entity and unit",
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
      "priority_rationale": "Operational location distinct from legal entity and unit",
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
      "selected_findings": [
        {
          "bundle": "identity-and-designation",
          "layer": "identifier-schemes-and-keys",
          "finding": {
            "id": "qualified-identifiers",
            "name": "Scheme-qualified external identifiers",
            "description": "An organization identifier is meaningless without its scheme. ISO 6523 ICD codes pair a numeric scheme designator with a value (0199 for LEI, 0060 for D-U-N-S, 0208 for the Belgian enterprise number); LEI-CDF pairs RegistrationAuthorityID with RegistrationAuthorityEntityID; BODS requires id plus scheme/schemeName or uri; and the EU EUID must itself be ISO 6523 compliant.",
            "source_refs": [
              "SRC-012",
              "SRC-002",
              "SRC-011",
              "SRC-016",
              "SRC-005",
              "SRC-010"
            ],
            "questions": [
              "Under which governed scheme was each identifier issued, and what is the registered scheme designator for that scheme?",
              "Which authority issued the identifier, and is that authority listed in a governed registration-authority registry?",
              "Can the identifier be reassigned, retired or superseded, and what happens to references when it is?",
              "How was the identifier verified against its issuing source, and when was that verification last performed?"
            ],
            "data_elements": [
              {
                "id": "identifier-scheme-code",
                "name": "Identifier scheme code",
                "description": "Governed designator of the issuing scheme, such as an ISO 6523 ICD code or a GLEIF registration-authority code.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "identifier-value",
                "name": "Identifier value",
                "description": "The identifier string exactly as issued, preserving case and any check characters.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "identifier-uri",
                "name": "Identifier resolvable URI",
                "description": "Dereferenceable URI for the identifier where the scheme publishes one.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "identifier-verified-at",
                "name": "Identifier verification timestamp",
                "description": "RFC 3339 timestamp with explicit offset recording when the identifier was last checked against the issuing source.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "identity-and-designation",
          "layer": "identifier-schemes-and-keys",
          "finding": {
            "id": "canonical-key-selection",
            "name": "Canonical key selection and internal identity",
            "description": "Because many organizations hold several external identifiers and many hold none, the model must state a deterministic priority for choosing the canonical key: authoritative master-system identifier first, then a governed global identifier or IRI, then a UUID or ULID assigned by the adopting Dimension. Dates, names and addresses are never keys.",
            "source_refs": [
              "SRC-002",
              "SRC-011",
              "SRC-005",
              "SRC-016"
            ],
            "questions": [
              "Which identifier is the canonical key for this organization record, and which rule in the identity priority selected it?",
              "Under which events may the canonical key change, and how are prior keys kept resolvable?",
              "If the organization has no external identifier at all, what dimension-assigned identifier is used and who assigned it?",
              "Within which namespace is the canonical key unique, and is that namespace globally resolvable?"
            ],
            "data_elements": [
              {
                "id": "canonical-key",
                "name": "Canonical key",
                "description": "The single selected identifier used as the record key, carrying its scheme and priority tier.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "key-priority-tier",
                "name": "Key priority tier",
                "description": "Coded tier recording whether the key is an authoritative master-system identifier, a governed global identifier/IRI, or a dimension-assigned UUID/ULID.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "alias-identifier",
                "name": "Alias identifier",
                "description": "Any non-canonical identifier retained so that historical references continue to resolve to this record.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "identity-and-designation",
          "layer": "identifier-schemes-and-keys",
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
          "bundle": "classification-form-and-purpose",
          "layer": "legal-form-and-category",
          "finding": {
            "id": "entity-legal-form",
            "name": "Entity legal form assignment",
            "description": "Legal form is a four-character ELF code valid only in combination with a jurisdiction, drawn from a list of more than 3,600 forms across more than 200 jurisdictions. The reserved codes 8888 (form not yet listed) and 9999 (no separate legal form) make the absence of a form explicitly representable rather than null.",
            "source_refs": [
              "SRC-004",
              "SRC-002",
              "SRC-006"
            ],
            "questions": [
              "Which ELF code and jurisdiction pair describes the organization's legal form, and which code-list version was used?",
              "If no listed legal form applies, is the correct representation 8888 (pending listing) or 9999 (no separate legal form), and why?",
              "Has the legal form changed through conversion, and what is the effective date of each form assignment?",
              "Is the legal form valid only at a sub-national level requiring an ISO 3166-2 jurisdiction code?"
            ],
            "data_elements": [
              {
                "id": "elf-code",
                "name": "ELF code",
                "description": "Four-character ISO 20275 entity legal form code.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "formation-jurisdiction",
                "name": "Jurisdiction of legal formation",
                "description": "ISO 3166-1 alpha-2 code, or ISO 3166-2 subdivision code where the legal form exists only at subdivision level.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "other-legal-form-text",
                "name": "Other legal form text",
                "description": "Free-text legal form as stated locally, used when no listed ELF code applies.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "classification-form-and-purpose",
          "layer": "legal-form-and-category",
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
          "bundle": "registration-standing-and-lifecycle",
          "layer": "formation-and-registry-entries",
          "finding": {
            "id": "formation-act-and-creation-date",
            "name": "Formation act and creation date",
            "description": "LEI-CDF records EntityCreationDate as the legal establishment date, schema.org records foundingDate and foundingLocation, BODS records foundingDate and formedByStatute, and Companies House records date_of_creation. Formation date and first registration date are frequently different and must not be conflated.",
            "source_refs": [
              "SRC-002",
              "SRC-010",
              "SRC-011",
              "SRC-013"
            ],
            "questions": [
              "On what date did the organization legally come into existence, and is that the same as its first registration date?",
              "Which instrument created the organization — articles, deed, statute, treaty or a founding resolution — and where is it held?",
              "In which jurisdiction and at which location was the organization founded, and does that differ from its current jurisdiction?",
              "If no formation date is known or the organization predates its register, how is that recorded without fabricating a date?"
            ],
            "data_elements": [
              {
                "id": "entity-creation-date",
                "name": "Entity creation date",
                "description": "Date on which the organization was legally established, with precision declared.",
                "value_kind": "date",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "constitutive-instrument-ref",
                "name": "Constitutive instrument reference",
                "description": "Reference to the founding instrument held in the charter model or by a custodian.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "founding-jurisdiction",
                "name": "Founding jurisdiction",
                "description": "Jurisdiction under whose law the organization was constituted.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "registration-standing-and-lifecycle",
          "layer": "formation-and-registry-entries",
          "finding": {
            "id": "registry-entry-and-authority",
            "name": "Registry entry and registration authority",
            "description": "An entry links the organization to an authoritative source through a register code plus a local entity number, as in LEI-CDF's RegistrationAuthorityID and RegistrationAuthorityEntityID, drawing on a governed list of more than 1,050 registers across 232 jurisdictions. The EU adds the EUID, which must be ISO 6523 compliant and unequivocally identify companies and branches across interconnected registers.",
            "source_refs": [
              "SRC-005",
              "SRC-002",
              "SRC-016",
              "SRC-013",
              "SRC-012"
            ],
            "questions": [
              "Which register holds an entry for this organization, and what is its governed register code?",
              "What entry or registration number does that register assign, and what is its syntax and check rule?",
              "How many registers hold entries for this organization, and which is authoritative for which fact?",
              "Does the entry describe a branch or a foreign company rather than a domestically constituted organization?"
            ],
            "data_elements": [
              {
                "id": "register-code",
                "name": "Register code",
                "description": "Governed code identifying the registration or validation authority.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "register-entity-number",
                "name": "Register entity number",
                "description": "The entity's identification number as maintained by that register.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "register-entry-date",
                "name": "Register entry date",
                "description": "Date on which the register accepted the entry.",
                "value_kind": "date",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "cross-register-identifier",
                "name": "Cross-register identifier",
                "description": "Interconnection identifier such as the EU EUID used to address the organization across interconnected registers.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "registration-standing-and-lifecycle",
          "layer": "standing-status-and-obligations",
          "finding": {
            "id": "entity-status-vs-registration-status",
            "name": "Entity status distinguished from record registration status",
            "description": "LEI-CDF keeps EntityStatus (ACTIVE, INACTIVE, NULL — whether the entity is legally registered and operating) strictly separate from RegistrationStatus (PENDING_VALIDATION, ISSUED, DUPLICATE, LAPSED, RETIRED, ANNULLED, CANCELLED, TRANSFERRED, PENDING_TRANSFER, PENDING_ARCHIVAL — the standing of the record). Companies House adds a twelve-value national enumeration plus company_status_detail. Collapsing these into one status field destroys answerability.",
            "source_refs": [
              "SRC-002",
              "SRC-013"
            ],
            "questions": [
              "Is the organization itself currently in existence and operating, and on what date was that last established?",
              "What is the standing of each record about the organization, separately from the organization's own status?",
              "Where a status is qualified (for example administration, liquidation or struck-off pending), what is the qualifying detail and the governing procedure?",
              "How does a national status value map onto the model's normalised status, and what is lost in the mapping?"
            ],
            "data_elements": [
              {
                "id": "entity-status",
                "name": "Entity status",
                "description": "Whether the organization is legally in existence and operating, coded under a named enumeration.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "record-registration-status",
                "name": "Record registration status",
                "description": "Standing of a specific record or registration about the organization, coded under that scheme's enumeration.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "status-detail",
                "name": "Status detail",
                "description": "Qualifying detail for a status, such as the insolvency or dissolution procedure in progress.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "status-observed-at",
                "name": "Status observation timestamp",
                "description": "RFC 3339 timestamp with explicit offset recording when the status was observed, held separately from the status effective date.",
                "value_kind": "timestamp",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "registration-standing-and-lifecycle",
          "layer": "lifecycle-events-and-succession",
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
          "bundle": "registration-standing-and-lifecycle",
          "layer": "lifecycle-events-and-succession",
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
          "bundle": "registration-standing-and-lifecycle",
          "layer": "lifecycle-events-and-succession",
          "finding": {
            "id": "dissolution-and-expiry",
            "name": "Dissolution and expiry",
            "description": "An organization ceases as a subject by dissolution, completion of winding-up, or replacement through corporate action. schema.org dissolutionDate is a secondary discovery field. LEI RETIRED means the entity ceased without merger; INACTIVE covers closure, acquisition or illegitimacy. Identifier records are not reused. History remains queryable after cessation. Deletion of the subject record is a retention decision, not an automatic consequence of dissolution.",
            "source_refs": [
              "SRC-018",
              "SRC-021",
              "SRC-010"
            ],
            "questions": [
              "Has the organization ceased, on what effective datetime, under which reason, and is winding-up still in progress?",
              "Which identifiers remain the correct historical keys after cessation, and which must not be reassigned or reused for a new entity?",
              "How long must the dissolved organization's identity and lineage remain available for resolution and audit, and who is the residual steward?"
            ],
            "data_elements": [
              {
                "id": "dissolution-and-expiry-data01",
                "name": "Dissolution datetime",
                "description": "Effective cessation datetime in RFC 3339, with precision if the source is date-only.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "dissolution-and-expiry-data02",
                "name": "Cessation reason",
                "description": "dissolved, merged, illegitimate, or other, aligned to LEI expiration reasons where applicable.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "dissolution-and-expiry-data03",
                "name": "Retain until",
                "description": "Earliest datetime at which deletion of the subject record may be considered, if ever.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "presence-and-reachability",
          "layer": "locations-sites-and-channels",
          "finding": {
            "id": "operating-sites-and-branches",
            "name": "Operating sites, branches and service areas",
            "description": "W3C ORG models Site as a place where an organization operates and separates hasSite from hasRegisteredSite. Operating presence is distinct from legal seat: a branch may be separately registered and separately identified, while a site may be purely operational with no registry footprint at all.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-013",
              "SRC-010"
            ],
            "questions": [
              "What kind of presence is this — registered branch, operating site, local unit or service point — and is it separately registered?",
              "Over which period was the site active, and what evidences its opening and closing?",
              "Which geographic areas does the organization serve from this site, and at what granularity is that recorded?",
              "Which place or facility record does this site resolve to, and who maintains that record?"
            ],
            "data_elements": [
              {
                "id": "site-kind",
                "name": "Site kind",
                "description": "Coded kind of operating presence.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "site-place-ref",
                "name": "Site place reference",
                "description": "Reference into the place or facility model where the site's spatial detail is held.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "served-area",
                "name": "Served area",
                "description": "Coded geographic area served, at a declared granularity.",
                "value_kind": "code",
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
    "WM-ORG-010": {
      "source_file": "publications/wm-org-010-legal-entity-registration/spec.yaml",
      "source_bytes": 279735,
      "source_sha256": "4bae598815feb67b552c9f3463f45f4368da077609b7451743a470d1a9dab615",
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-08-23T22:48:15Z",
        "synthesisSha256": "8e6a9b3302f0ca4f0b1c3f826bd5bd38361ed8f4b026cb02859f58d5dac99589",
        "providerMode": "dual-provider",
        "providers": [
          "Claude",
          "Grok"
        ],
        "waivedProviders": []
      },
      "metaModel": {
        "id": "WM-ORG-010",
        "registryId": "vr.wm-org-010",
        "name": "Legal Entity Registration",
        "version": "0.3.0-research.1",
        "previousVersions": [],
        "entryKind": "entity",
        "family": "World Models",
        "category": "Society, people and institutions",
        "industry": [
          "Cross-industry"
        ],
        "domain": [
          "SOC.ORG.REG"
        ],
        "tags": [
          "legal",
          "entity",
          "registration",
          "soc.org.reg"
        ],
        "status": "published"
      },
      "model": {
        "registry_id": "vr.wm-org-010",
        "model_id": "WM-ORG-010",
        "name": "Legal Entity Registration",
        "entry_kind": "entity",
        "purpose": "Model the legal identity of an organization as constituted and recorded by an authoritative register or registration authority in a jurisdiction, so that an agent can identify, verify, monitor and operate on registered legal persons without conflating them with the organizations, groups or statistical units they relate to.",
        "scope_statement": "In scope is the registration record of a legal person (and of branches that carry their own register entries): the authoritative register and its assigned identifier, legal name and name history, legal form and jurisdiction of formation, registered addresses, registration and entity status, dated legal entity events including succession and dissolution, structural relationships as reported to registers, evidence and validation of those facts, cross-scheme identifier alignment, and the governance of the record (provenance, access tiers, retention, interoperability). Out of scope is anything that is a fact about the organization's operation, ownership content, finances or authorizations rather than about its registered legal existence.",
        "in_scope": [
          "Authoritative register identity: registration authority, register-assigned entity identifier, and qualified alternate identifiers such as LEI, EUID and ISO/IEC 6523-scoped scheme identifiers",
          "Legal name, transliterations, trading and previous names with dated validity",
          "Entity legal form (ISO 20275 ELF) and jurisdiction of formation at country and subdivision level",
          "Registered/legal address, headquarters address and other addresses recorded by the register",
          "Registration status, entity status, status detail and compliance standing signals such as strike-off proposals and overdue filings",
          "Dated legal entity events: name change, legal form conversion, merger, division, spin-off, seat transfer, dissolution, liquidation, restoration, with effective and recorded dates",
          "Branch and establishment registration records and their head-office linkage",
          "Structural relationships as reported to registers: consolidating parents, branch/head-office, fund and feeder relationships, with validation level and reporting exceptions",
          "Evidence artifacts: certificates, dated register extracts, gazette notices, filings and their authentication",
          "Validation sources, corroboration levels, discrepancy detection and register correction processes",
          "Access tiers, licence conditions, personal-data handling, retention and deletion constraints on register records",
          "Interoperability mappings to external organization vocabularies and register-to-register exchange"
        ],
        "out_of_scope": [
          "Internal organizational structure, units, posts, headcount and reporting lines (parent organization model)",
          "Beneficial ownership and control content, including natural-person particulars; only the linkage and access classification are in scope",
          "Financial statement content, accounting figures and audit opinions, even when filed with a register",
          "Sector authorizations, licences, permits and regulatory registrations that do not constitute legal existence",
          "Tax assessment, returns and fiscal compliance; only the fiscal identifier as an alternate identifier is in scope",
          "Statistical units (enterprise, enterprise group, local unit, kind-of-activity unit) and business demography",
          "Trademarks, brands and domain names",
          "Contracts, credit ratings, sanctions listings and adverse media",
          "Natural-person identity records and employment relationships",
          "Physical premises management, geocoding and facility operations"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-001 Organization (parent model)",
            "distinction": "The parent models any organization, including informal, unregistered and purely internal ones. WM-ORG-010 models only the subset that has acquired or claims registered legal status, and only the facts that the register constitutes or records. W3C ORG makes the same cut with org:FormalOrganization, which RegOrg further narrows to rov:RegisteredOrganization for entities that gained legal entity status through formal registration.",
            "source_refs": [
              "SRC-006",
              "SRC-007"
            ]
          },
          {
            "neighbor": "Statistical business register unit model (enterprise, legal unit, enterprise group)",
            "distinction": "A legal unit is not an enterprise. Statistical frameworks define the enterprise as the smallest set of legal units with autonomy in financial and investment decisions, so a single enterprise may span several registered legal persons and a registered legal person may be only part of an enterprise. WM-ORG-010 stops at the registered legal unit and delegates statistical unit construction, demography and continuity rules elsewhere.",
            "source_refs": [
              "SRC-016"
            ]
          },
          {
            "neighbor": "Beneficial ownership register model",
            "distinction": "Beneficial ownership is held in a separate mechanism with a different legal basis and a materially different access regime; unrestricted public access to beneficial ownership data was struck down in the EU, whereas core company particulars remain publicly disclosable. Only the pointer, holding mechanism and access tier belong here.",
            "source_refs": [
              "SRC-015",
              "SRC-018"
            ]
          },
          {
            "neighbor": "Global LEI System (GLEIF/LEI issuers)",
            "distinction": "An LEI is a governed global identifier layered on top of a register record; GLEIF and its issuers are not registers of formation. LEI reference data explicitly cross-references the local business register through a registration-authority code and a local entity identifier, which confirms that the register, not the LEI, is the master identity source.",
            "source_refs": [
              "SRC-002",
              "SRC-003"
            ]
          },
          {
            "neighbor": "Tax registration and fiscal identifier model",
            "distinction": "Tax numbers, VAT numbers and employer identification numbers are usually assigned by a different authority under a different act; being on a business register does not imply tax registration and vice versa. They are carried here only as qualified alternate identifiers, scheme-tagged so they cannot be mistaken for the register identity.",
            "source_refs": [
              "SRC-013",
              "SRC-012"
            ]
          },
          {
            "neighbor": "Branch / establishment as an organization site",
            "distinction": "A branch is not a separate legal person, but in many jurisdictions it holds its own register entry, identifier and disclosure duties, and LEI relationship data recognises IS_INTERNATIONAL_BRANCH_OF as a distinct relationship. Branch registration records are therefore in scope, while branch premises and operations are not.",
            "source_refs": [
              "SRC-005",
              "SRC-008"
            ]
          },
          {
            "neighbor": "Regulatory licence and authorization model",
            "distinction": "Authorization to carry on a regulated activity is granted by a supervisor and can be withdrawn without ending legal existence. Registration constitutes or records existence; licensing conditions conduct. Conflating them makes an entity appear dissolved when it has merely lost a permission.",
            "source_refs": [
              "SRC-009",
              "SRC-008"
            ]
          },
          {
            "neighbor": "Document and evidence model",
            "distinction": "Certificates, extracts and filings are modelled here only as evidence bound to registration facts, with issuer, as-of date and authentication. Generic document lifecycle, storage and rendering belong to a composable document model.",
            "source_refs": [
              "SRC-010",
              "SRC-002"
            ]
          }
        ]
      },
      "structure_index": [
        {
          "id": "legal-identity-and-designation",
          "name": "Legal identity and designation",
          "description": "What the registered legal person is called, how it is identified across schemes, and how it is classified by legal form and activity.",
          "layers": [
            {
              "id": "identity-and-identifiers",
              "name": "Identity and identifiers",
              "description": "The authoritative register-assigned identity and the qualified alternate identifiers that denote the same legal person."
            },
            {
              "id": "names-and-designations",
              "name": "Names and designations",
              "description": "The registered legal name, its variants across scripts and uses, and its dated history."
            },
            {
              "id": "legal-form-and-classification",
              "name": "Legal form and classification",
              "description": "The constitutive legal form and jurisdiction, and the categorical and activity classifications applied to the record."
            }
          ]
        },
        {
          "id": "register-and-registration-authority",
          "name": "Register and registration authority",
          "description": "The authority that keeps the register, what the register legally accomplishes, and the dated act of registration with its ongoing filing obligations.",
          "layers": [
            {
              "id": "registration-authority-and-register-scope",
              "name": "Registration authority and register scope",
              "description": "Identification of the authority and register instance, and the legal effect of entry."
            },
            {
              "id": "registration-act-and-filings",
              "name": "Registration act and filings",
              "description": "The dated act of registration, the currency of the record, and the recurring disclosure obligations that maintain it."
            }
          ]
        },
        {
          "id": "lifecycle-status-and-events",
          "name": "Lifecycle, status and events",
          "description": "The state of the entity and of its record, the dated events that change them, and the end and possible restoration of registered existence.",
          "layers": [
            {
              "id": "status-and-standing",
              "name": "Status and standing",
              "description": "The two independent status axes and the softer signals of standing that precede a formal status change."
            },
            {
              "id": "legal-entity-events-and-succession",
              "name": "Legal entity events and succession",
              "description": "Dated typed events that change registered facts, including those that create, absorb, transform or end legal persons."
            }
          ]
        },
        {
          "id": "jurisdiction-place-and-cross-border-presence",
          "name": "Jurisdiction, place and cross-border presence",
          "description": "Addresses recorded by the register, and the entity's registered footprint beyond its jurisdiction of formation.",
          "layers": [
            {
              "id": "registered-addresses",
              "name": "Registered addresses",
              "description": "Addresses of record and their legal roles."
            },
            {
              "id": "cross-border-presence",
              "name": "Cross-border presence",
              "description": "Branch registration, seat transfer and authorization to operate outside the jurisdiction of formation."
            }
          ]
        },
        {
          "id": "relationships-control-and-representation",
          "name": "Relationships, control and representation",
          "description": "Structural links between registered entities, the linkage to control and ownership mechanisms, and who may bind the entity.",
          "layers": [
            {
              "id": "group-and-parent-relationships",
              "name": "Group and parent relationships",
              "description": "Reported structural links between registered entities, with periods, evidence and exceptions."
            },
            {
              "id": "control-representation-and-ownership-linkage",
              "name": "Control, representation and ownership linkage",
              "description": "The pointer to control information and the registration facts about who may act for the entity."
            }
          ]
        },
        {
          "id": "evidence-verification-and-quality",
          "name": "Evidence, verification and quality",
          "description": "What proves each registration fact, how strongly it was corroborated, and how discrepancies are detected and resolved.",
          "layers": [
            {
              "id": "evidence-and-validation",
              "name": "Evidence and validation",
              "description": "Documentary evidence for registration facts and the strength of their corroboration."
            },
            {
              "id": "quality-and-conflict-management",
              "name": "Quality and conflict management",
              "description": "Detecting, reporting and resolving divergence between the register record and other sources."
            }
          ]
        },
        {
          "id": "governance-access-provenance-and-retention",
          "name": "Governance, access, provenance and retention",
          "description": "Who may see what, how personal data in register records is handled, how every assertion is attributed, and how long records must survive.",
          "layers": [
            {
              "id": "access-publicity-and-privacy",
              "name": "Access, publicity and privacy",
              "description": "Disclosure tiers and the handling of personal data within registration records."
            },
            {
              "id": "provenance-retention-and-interoperability",
              "name": "Provenance, retention and interoperability",
              "description": "Attribution of every fact to its source and time, survival of the record over time, and alignment to external vocabularies and exchange protocols."
            }
          ]
        }
      ],
      "selected_findings": [
        {
          "bundle": "legal-identity-and-designation",
          "layer": "identity-and-identifiers",
          "finding": {
            "id": "register-anchored-legal-entity-identity",
            "name": "Register-anchored legal entity identity",
            "description": "The master identity of the registered legal person is the pair (registration authority, identifier assigned by that authority). Locally assigned surrogate keys are subordinate and must be flagged as such. LEI reference data models this explicitly as RegistrationAuthorityID plus RegistrationAuthorityEntityID, and the governed authority list exists precisely because a bare registration number is ambiguous across 232 jurisdictions.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-007",
              "SRC-009"
            ],
            "questions": [
              "Which register or registration authority holds the authoritative record for this entity, and what identifier does it assign?",
              "Is the register-assigned identifier stable, reused after dissolution, or changed on conversion or migration?",
              "When no register-assigned identifier exists, which fallback identity is used and how is it qualified?",
              "How is the identifier syntactically validated before acceptance?"
            ],
            "data_elements": [
              {
                "id": "registration-authority-code",
                "name": "Registration authority code",
                "description": "Governed code identifying the register or registration authority that holds the authoritative record.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "register-entity-identifier",
                "name": "Register entity identifier",
                "description": "Identifier assigned to the entity by the registration authority, stored exactly as recorded.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "locally-assigned-identifier",
                "name": "Locally assigned identifier",
                "description": "UUID or ULID minted by the adopting Dimension when no authoritative identifier is available; always flagged as non-authoritative.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "identifier-validity-interval",
                "name": "Identifier validity interval",
                "description": "Start and end of the period during which a given identifier denoted this entity.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "legal-identity-and-designation",
          "layer": "identity-and-identifiers",
          "finding": {
            "id": "cross-scheme-identifier-alignment",
            "name": "Cross-scheme identifier alignment",
            "description": "Additional identifier schemes attached to the same legal person (LEI, EUID, VAT or tax number, D-U-N-S, GLN, national scheme numbers) together with the scheme qualification that keeps them unambiguous, and the precedence rules when they disagree. ISO/IEC 6523 exists because an organization identifier without its issuing scheme cannot be interpreted.",
            "source_refs": [
              "SRC-013",
              "SRC-012",
              "SRC-003",
              "SRC-001"
            ],
            "questions": [
              "Which additional identifier schemes are recorded for this entity and which authority issues each?",
              "Does each alternate identifier denote the same legal person, or a different unit such as an establishment, VAT group or branch?",
              "What is the precedence order when alternate identifiers disagree with the authoritative register record?",
              "How is a global identifier's own registration status reconciled with the underlying register record?"
            ],
            "data_elements": [
              {
                "id": "identifier-scheme-code",
                "name": "Identifier scheme code",
                "description": "Code qualifying which scheme an alternate identifier belongs to.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "alternate-identifier-value",
                "name": "Alternate identifier value",
                "description": "Value of an identifier issued under a scheme other than the authoritative register.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "identifier-equivalence-assertion",
                "name": "Identifier equivalence assertion",
                "description": "Typed assertion that an alternate identifier denotes the same legal person, with strength and evidence.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "global-identifier-record-status",
                "name": "Global identifier record status",
                "description": "Lifecycle status of the alternate global identifier record itself, distinct from the entity's legal status.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "legal-identity-and-designation",
          "layer": "names-and-designations",
          "finding": {
            "id": "legal-name-variants-and-name-history",
            "name": "Legal name, variants and name history",
            "description": "The legal name exactly as recorded by the authoritative register, plus typed variants (transliterations, trading names, abbreviations, previous legal names) each with dated validity and an evidencing filing. Reference-data formats keep other names and transliterated names in separate typed containers because collapsing them destroys the distinction between the legally operative name and a convenience label.",
            "source_refs": [
              "SRC-002",
              "SRC-007",
              "SRC-008",
              "SRC-011"
            ],
            "questions": [
              "What is the legal name exactly as recorded by the authoritative register, including script, diacritics and legal-form suffix?",
              "Which other names are recorded and how is each typed?",
              "When did each name become effective, when did it cease, and what filing evidences the change?",
              "Does the register enforce name uniqueness, and is the name reserved or in dispute?"
            ],
            "data_elements": [
              {
                "id": "legal-name",
                "name": "Legal name",
                "description": "The official name of the legal entity as recorded in the official register or its constituting documents.",
                "value_kind": "text",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "name-variant",
                "name": "Name variant",
                "description": "A typed alternative name with language, script and validity interval.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "name-change-effective-date",
                "name": "Name change effective date",
                "description": "Date on which a recorded name became or ceased to be operative.",
                "value_kind": "date",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "legal-identity-and-designation",
          "layer": "legal-form-and-classification",
          "finding": {
            "id": "entity-legal-form-and-jurisdiction-of-formation",
            "name": "Entity legal form and jurisdiction of formation",
            "description": "The legal form under which the entity exists and the jurisdiction whose law constitutes it. These are interdependent: a legal form has meaning only under local legislation, which is why the governed code list carries local-language names and why a Dutch BV must not be normalised into a German GmbH. Sub-national formation jurisdictions are the norm in federal states.",
            "source_refs": [
              "SRC-004",
              "SRC-002",
              "SRC-008"
            ],
            "questions": [
              "Under which jurisdiction's law was the entity formed, at what sub-national level, and how is that coded?",
              "What is the entity's legal form, expressed both as a local-language name and as a governed code?",
              "Has the legal form changed over time, and what conversion event caused the change?",
              "If no governed code exists for the form, which placeholder and free-text value are used?"
            ],
            "data_elements": [
              {
                "id": "legal-jurisdiction-code",
                "name": "Legal jurisdiction code",
                "description": "Coded jurisdiction whose law constitutes the entity, at country and where relevant subdivision level.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "entity-legal-form-code",
                "name": "Entity legal form code",
                "description": "Governed four-character code for the entity's legal form under the applicable jurisdiction.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "other-legal-form-text",
                "name": "Other legal form text",
                "description": "Local-language legal form name used when no governed code applies.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "legal-identity-and-designation",
          "layer": "legal-form-and-classification",
          "finding": {
            "id": "legal-personality-and-capacity",
            "name": "Legal personality and capacity",
            "description": "A registered legal person is a juristic person distinct from its members, able to acquire rights and assume obligations in its own name. UNCITRAL treats this as affirmative asset partitioning and recommends that members are not personally liable solely by reason of membership. UNCITRAL insolvency guidance adds that a corporation obtains personality by a legal process and enjoys perpetuity independent of changing members. ISO 17442 requires the party to have the legal right in its jurisdiction to enter independently into legal contracts.",
            "source_refs": [
              "SRC-024",
              "SRC-026",
              "SRC-020"
            ],
            "questions": [
              "Does this subject have legal personality distinct from its members or controllers under the law of the formation jurisdiction?",
              "Which capacities does the law confer on this legal person, and are any of them restricted by statute, objects or duration?",
              "Are members or shareholders shielded from the entity's debts solely by reason of membership, and under which legal form rule?",
              "At what event time did legal personality attach, and is registration constitutive or merely declaratory in this jurisdiction?"
            ],
            "data_elements": [
              {
                "id": "legal-personality-and-capacity-data01",
                "name": "Has legal personality",
                "description": "Whether the subject is a juristic person distinct from natural-person members.",
                "value_kind": "boolean",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "legal-personality-and-capacity-data02",
                "name": "Personality effective at",
                "description": "Event time at which legal personality attached under the formation law, recorded separately from observation or ingestion time.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "legal-personality-and-capacity-data03",
                "name": "Formation theory",
                "description": "Whether registration creates the person (UNCITRAL LLE Recommendation 8: formed once registered) or records a person already constituted.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "legal-personality-and-capacity-data04",
                "name": "Member liability regime",
                "description": "Limited, unlimited or mixed liability of members solely by reason of membership.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "register-and-registration-authority",
          "layer": "registration-authority-and-register-scope",
          "finding": {
            "id": "registration-authority-identification",
            "name": "Registration authority identification",
            "description": "Identification of the organization operating the register, the specific register instance, its statutory mandate and its territorial or sectoral coverage, distinguishing a constitutive registration authority from a validation-only source. The existence of a governed list of more than a thousand registers across 232 jurisdictions shows that 'the register' is never inferable from the country alone.",
            "source_refs": [
              "SRC-003",
              "SRC-009",
              "SRC-002",
              "SRC-010"
            ],
            "questions": [
              "Which organization operates the register, and under what statutory mandate?",
              "Which coded entry from a governed registration-authority list applies, and at what list version?",
              "Does the register cover the whole jurisdiction, or only a sub-national or sectoral segment?",
              "Is this source constitutive for registration, or is it consulted only to validate?"
            ],
            "data_elements": [
              {
                "id": "registration-authority-name",
                "name": "Registration authority name",
                "description": "Legal name of the organization operating the register.",
                "value_kind": "text",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "authority-mandate-reference",
                "name": "Authority mandate reference",
                "description": "Citation of the legislation or instrument conferring the register's mandate.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "register-coverage-statement",
                "name": "Register coverage statement",
                "description": "Declared territorial and sectoral scope of the register, with exclusions.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "register-and-registration-authority",
          "layer": "registration-authority-and-register-scope",
          "finding": {
            "id": "register-legal-effect",
            "name": "Register legal effect: constitutive versus declaratory",
            "description": "What entry on the register legally accomplishes: whether legal personality arises from registration or is merely recorded, from when disclosed particulars are opposable to third parties, what liability or warranty the register accepts, and whether parallel registers can conflict. This distinction determines whether absence from a register is evidence of non-existence or merely of non-disclosure.",
            "source_refs": [
              "SRC-009",
              "SRC-010",
              "SRC-007"
            ],
            "questions": [
              "Does registration create legal personality, or record an entity that already exists?",
              "Which particulars are opposable to third parties once disclosed, and from when?",
              "What is the register's liability regime for inaccurate entries, and is the data warranted?",
              "Are there parallel registers in the same jurisdiction whose entries could conflict?"
            ],
            "data_elements": [
              {
                "id": "register-legal-effect-code",
                "name": "Register legal effect code",
                "description": "Whether entry is constitutive of legal personality or declaratory only.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "opposability-start-date",
                "name": "Opposability start date",
                "description": "Date from which a disclosed particular may be relied on against third parties.",
                "value_kind": "date",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "register-warranty-statement",
                "name": "Register warranty or disclaimer statement",
                "description": "The register's published position on accuracy, verification and liability.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "register-and-registration-authority",
          "layer": "registration-act-and-filings",
          "finding": {
            "id": "registration-act-dates-and-record-currency",
            "name": "Registration act dates and record currency",
            "description": "The dated act of registration and how current the record is: entity creation date, the register's own initial registration date, last update, next renewal or confirmation date, and — critically — the separation of event time, register-recorded time and our observation time. Reference-data formats keep creation date and initial registration date as distinct fields precisely because they routinely differ.",
            "source_refs": [
              "SRC-002",
              "SRC-008",
              "SRC-001"
            ],
            "questions": [
              "What is the entity creation date, and how does it differ from the register's initial registration date?",
              "When was the register record last updated, and when did we last observe or retrieve it?",
              "What periodic confirmation or renewal obligation applies, and when is it next due?",
              "How are date-only register values reconciled with timestamped ingestion records?"
            ],
            "data_elements": [
              {
                "id": "entity-creation-date",
                "name": "Entity creation date",
                "description": "Date the entity was first established or came into legal existence.",
                "value_kind": "date",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "initial-registration-date",
                "name": "Initial registration date",
                "description": "Date the record was first created in the register or identifier system.",
                "value_kind": "date",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "last-update-timestamp",
                "name": "Last update timestamp",
                "description": "Time the source record was last modified, in RFC 3339.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "observation-timestamp",
                "name": "Observation timestamp",
                "description": "Time at which the adopting Dimension retrieved or observed the record, in RFC 3339.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "next-renewal-date",
                "name": "Next renewal or confirmation date",
                "description": "Next date on which the record must be confirmed or renewed.",
                "value_kind": "date",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "lifecycle-status-and-events",
          "layer": "status-and-standing",
          "finding": {
            "id": "registration-status-and-entity-status",
            "name": "Registration status and entity status",
            "description": "Two distinct axes that must not be conflated: the legal state of the entity in the register (active, dissolved, in liquidation, converted), and the state of the registration record as a data object (published, pending, lapsed, retired, duplicate). An entity can be perfectly alive while its identifier record has lapsed, and a record can remain published after the entity is dissolved.",
            "source_refs": [
              "SRC-002",
              "SRC-008",
              "SRC-001"
            ],
            "questions": [
              "What is the entity's status in the authoritative register and which code list defines it?",
              "What is the status of the registration record as a data object, independent of the entity's legal state?",
              "Which status transitions are legally possible, and which are terminal?",
              "What supplementary status detail qualifies the headline status?"
            ],
            "data_elements": [
              {
                "id": "entity-status-code",
                "name": "Entity status code",
                "description": "Legal status of the entity as recorded by the register.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "registration-record-status-code",
                "name": "Registration record status code",
                "description": "Status of the registration record as a data object, independent of the entity's legal state.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "status-detail-code",
                "name": "Status detail code",
                "description": "Qualifier refining the headline status.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "status-effective-date",
                "name": "Status effective date",
                "description": "Date from which the current status applies.",
                "value_kind": "date",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "lifecycle-status-and-events",
          "layer": "legal-entity-events-and-succession",
          "finding": {
            "id": "legal-entity-event-record-and-effective-dating",
            "name": "Legal entity event record and effective dating",
            "description": "Discrete typed events recorded with an effective date in the legal jurisdiction, a date recorded by the register, a completion status and supporting validation documents. Public-authority policy explicitly separates events that alter reference data from those that retire or create identifiers, and prioritises frequent events such as name changes and mergers over rare ones such as reverse takeovers.",
            "source_refs": [
              "SRC-011",
              "SRC-002"
            ],
            "questions": [
              "What type of legal entity event occurred, per a governed event type list?",
              "What is the event's effective date in the jurisdiction, the date the register recorded it, and the time we ingested it?",
              "What is the event's completion status?",
              "Which documents validate the event and which fields does it change?"
            ],
            "data_elements": [
              {
                "id": "legal-entity-event-type",
                "name": "Legal entity event type",
                "description": "Governed code for the kind of event that altered the registered facts.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "event-effective-date",
                "name": "Event effective date",
                "description": "Date on which the event took legal effect in the jurisdiction.",
                "value_kind": "date",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "event-recorded-date",
                "name": "Event recorded date",
                "description": "Date on which the register or identifier system recorded the event.",
                "value_kind": "date",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "event-status-code",
                "name": "Event status code",
                "description": "Completion state of the event.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "lifecycle-status-and-events",
          "layer": "legal-entity-events-and-succession",
          "finding": {
            "id": "succession-merger-division-and-conversion",
            "name": "Succession: merger, division and conversion",
            "description": "Events that create, absorb or transform legal persons and the predecessor/successor links they generate, including cross-border operations where two registers must notify each other. Organization vocabularies model this as change events with original and resulting organizations rather than as an in-place update, which is the only representation that survives later audit.",
            "source_refs": [
              "SRC-010",
              "SRC-006",
              "SRC-002",
              "SRC-011",
              "SRC-014"
            ],
            "questions": [
              "Which predecessor and successor entities are linked by this event, and by which identifiers?",
              "Is the operation a merger by absorption, a merger by formation, a division, a spin-off or a conversion?",
              "Does the operation cross jurisdictions, and which registers must notify each other?",
              "Does the entity's identifier survive the operation, or is a new one assigned and the old one retired?"
            ],
            "data_elements": [
              {
                "id": "successor-entity-reference",
                "name": "Successor entity reference",
                "description": "Reference to an entity that succeeds this one following the operation.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "predecessor-entity-reference",
                "name": "Predecessor entity reference",
                "description": "Reference to an entity this one succeeds.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "operation-type-code",
                "name": "Operation type code",
                "description": "Coded kind of merger, division, spin-off or conversion.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "lifecycle-status-and-events",
          "layer": "legal-entity-events-and-succession",
          "finding": {
            "id": "dissolution-liquidation-and-restoration",
            "name": "Dissolution, liquidation and restoration",
            "description": "The end and possible reinstatement of registered existence: voluntary and compulsory dissolution, liquidation and insolvency proceedings with appointed office-holders, deregistration, and restoration to the register. Restoration is a genuine counterexample to naive terminal-state modelling: a dissolved entity can be brought back, so 'dissolved' is not always absorbing.",
            "source_refs": [
              "SRC-002",
              "SRC-008",
              "SRC-009",
              "SRC-011"
            ],
            "questions": [
              "On what date and on what ground did registered existence end?",
              "Which insolvency or liquidation proceeding is open, who is the appointed office-holder, and what are its dates?",
              "Can the entity be restored or reinstated, under what conditions and within what period?",
              "What happens to the record and its identifiers after dissolution?"
            ],
            "data_elements": [
              {
                "id": "entity-expiration-date",
                "name": "Entity expiration date",
                "description": "Date on which registered legal existence ended.",
                "value_kind": "date",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "entity-expiration-reason",
                "name": "Entity expiration reason",
                "description": "Coded ground on which registered existence ended.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "data-insolvency-proceeding",
                "name": "Insolvency or liquidation proceeding",
                "description": "An open or closed proceeding with type, dates and appointed office-holder.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "restoration-event",
                "name": "Restoration event",
                "description": "An event reinstating the entity to the register, with authority, date and effect.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "jurisdiction-place-and-cross-border-presence",
          "layer": "cross-border-presence",
          "finding": {
            "id": "branch-and-establishment-registration",
            "name": "Branch and establishment registration",
            "description": "Registration records for branches and establishments that are not separate legal persons but carry their own register entries, identifiers and disclosure duties in a host jurisdiction. Relationship data recognises an international branch relationship as a distinct type, and national registers hold explicit branch and foreign-company sub-structures pointing back to the home register.",
            "source_refs": [
              "SRC-008",
              "SRC-005",
              "SRC-010",
              "SRC-011"
            ],
            "questions": [
              "Is this record a branch or establishment rather than an autonomous legal person, and which head office does it belong to?",
              "Which host-jurisdiction register holds the branch record and what identifier does it assign?",
              "Which particulars must the branch disclose locally versus rely on from the head office register?",
              "How is closure or dissolution of the head office propagated to the branch record?"
            ],
            "data_elements": [
              {
                "id": "branch-indicator",
                "name": "Branch indicator",
                "description": "Whether the record describes a branch or establishment rather than an autonomous legal person.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "head-office-reference",
                "name": "Head office reference",
                "description": "Reference to the legal person of which this record is a branch.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "branch-registration-identifier",
                "name": "Branch registration identifier",
                "description": "Identifier assigned to the branch by the host register.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "jurisdiction-place-and-cross-border-presence",
          "layer": "cross-border-presence",
          "finding": {
            "id": "redomiciliation-and-foreign-qualification",
            "name": "Redomiciliation and foreign qualification",
            "description": "Transfer of the registered seat between jurisdictions, and authorization to do business in jurisdictions other than that of formation, with or without continuity of legal personality. Register status vocabularies carry values for transfer out of the jurisdiction, confirming that jurisdiction of formation is a dated fact rather than a constant.",
            "source_refs": [
              "SRC-008",
              "SRC-010",
              "SRC-002",
              "SRC-017"
            ],
            "questions": [
              "Has the entity transferred its registered seat, from which jurisdiction to which, and on what date?",
              "Is legal personality continuous across the transfer, or was the entity re-formed?",
              "In which additional jurisdictions is the entity qualified or authorized to do business, and under what identifier?",
              "Which identifiers are retired, retained or newly assigned as a result?"
            ],
            "data_elements": [
              {
                "id": "seat-transfer-event",
                "name": "Seat transfer event",
                "description": "A transfer of registered seat between jurisdictions with dates and continuity assertion.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "foreign-qualification-record",
                "name": "Foreign qualification record",
                "description": "Authorization to do business in a jurisdiction other than that of formation.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "jurisdiction-of-formation-history",
                "name": "Jurisdiction of formation history",
                "description": "Ordered history of jurisdictions under whose law the entity has been constituted.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "evidence-verification-and-quality",
          "layer": "evidence-and-validation",
          "finding": {
            "id": "registration-evidence-documents-and-extracts",
            "name": "Registration evidence documents and extracts",
            "description": "Documents that evidence registration facts — certificates of incorporation or good standing, dated register extracts, gazette publications and cross-border company certificates — each speaking as of a point in time and each requiring authentication before reliance. Extracts age: an extract is a dated snapshot, not a standing truth, which is why an as-of timestamp and a freshness window are mandatory.",
            "source_refs": [
              "SRC-010",
              "SRC-008",
              "SRC-002",
              "SRC-009"
            ],
            "questions": [
              "Which document evidences each registration fact, and who issued it?",
              "As of what date do the extract's contents speak, and how long is it treated as current?",
              "Is the document authenticated, and how is authenticity checked?",
              "Is a translation or legalization required for cross-border use?"
            ],
            "data_elements": [
              {
                "id": "evidence-document-reference",
                "name": "Evidence document reference",
                "description": "Reference to a document evidencing one or more registration facts.",
                "value_kind": "reference",
                "cardinality": "1..n",
                "required": true
              },
              {
                "id": "extract-as-of-date",
                "name": "Extract as-of timestamp",
                "description": "Point in time as of which an extract's contents are stated to be accurate.",
                "value_kind": "timestamp",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "authentication-method-code",
                "name": "Authentication method code",
                "description": "How the document's authenticity is established.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "evidence-verification-and-quality",
          "layer": "quality-and-conflict-management",
          "finding": {
            "id": "data-quality-discrepancies-and-challenge-process",
            "name": "Data quality, discrepancies and challenge process",
            "description": "Detection, reporting and resolution of divergence between the register record and other authoritative or self-reported sources, including statutory discrepancy-reporting duties on obliged entities and the register's own correction or challenge procedure. Unresolved conflicts must be represented explicitly rather than silently resolved by picking a value.",
            "source_refs": [
              "SRC-009",
              "SRC-018",
              "SRC-008",
              "SRC-002"
            ],
            "questions": [
              "Which discrepancies exist between the register record and other sources?",
              "Is there a duty to report the discrepancy, to whom, and within what deadline?",
              "What process corrects an erroneous register entry, and who may initiate it?",
              "Which quality checks run automatically and at what thresholds?",
              "How is an unresolved conflict represented so downstream consumers are not misled?"
            ],
            "data_elements": [
              {
                "id": "discrepancy-record",
                "name": "Discrepancy record",
                "description": "A recorded divergence between sources with values, detection metadata and status.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "quality-check-result",
                "name": "Quality check result",
                "description": "Outcome of an automated validation rule against the record.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              },
              {
                "id": "correction-request",
                "name": "Correction or challenge request",
                "description": "A submitted request to correct the register entry, with initiator, date and outcome.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false
              }
            ]
          }
        },
        {
          "bundle": "governance-access-provenance-and-retention",
          "layer": "provenance-retention-and-interoperability",
          "finding": {
            "id": "provenance-source-attribution-and-observation-time",
            "name": "Provenance, source attribution and observation time",
            "description": "Full attribution of every recorded fact to its source, retrieval method, retrieving agent and time, keeping three clocks separate: when the event took legal effect, when the register recorded it, and when we observed it. Collapsing these makes it impossible to reconstruct what was knowable at a past decision point.",
            "source_refs": [
              "SRC-002",
              "SRC-006",
              "SRC-001"
            ],
            "questions": [
              "From which source system, endpoint or file was each fact obtained, and at which version?",
              "What are the event time, the register's recorded time and our observation time for each fact?",
              "Which agent performed the retrieval and under what authorization?",
              "How is the retrieved payload preserved so the assertion can be re-checked later?"
            ],
            "data_elements": [
              {
                "id": "source-system-identifier",
                "name": "Source system identifier",
                "description": "Identifier of the system, endpoint or publication from which a fact was obtained.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "provenance-observation-timestamp",
                "name": "Provenance observation timestamp",
                "description": "RFC 3339 timestamp at which the fact was observed or ingested.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "payload-content-hash",
                "name": "Payload content hash",
                "description": "Hash of the retrieved payload with its algorithm, used for integrity only.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false
              },
              {
                "id": "retrieval-agent-reference",
                "name": "Retrieval agent reference",
                "description": "Reference to the agent or job that performed the retrieval.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false
              }
            ]
          }
        }
      ],
      "functions": [
        {
          "id": "resolve-registration-identity",
          "name": "Resolve registration identity",
          "description": "Resolve a candidate organization description to a single authoritative register record, or report that no confident resolution exists."
        },
        {
          "id": "validate-identifier-syntax",
          "name": "Validate identifier syntax and scheme",
          "description": "Check that an identifier conforms to the format and any checksum defined by its scheme, and that the scheme code itself is known."
        },
        {
          "id": "ingest-register-record",
          "name": "Ingest register record with provenance",
          "description": "Retrieve a register record or bulk export and store it as timestamped assertions with full source attribution."
        },
        {
          "id": "apply-legal-entity-event",
          "name": "Apply legal entity event",
          "description": "Record a typed legal entity event and derive the field changes, identifier retirements and successor links it implies."
        },
        {
          "id": "compute-current-status",
          "name": "Compute current status as of a time",
          "description": "Return the entity status, record status and standing signals that were true as of a given instant, using the stored assertion history."
        },
        {
          "id": "request-and-verify-evidence",
          "name": "Request and verify registration evidence",
          "description": "Obtain a dated extract or certificate and verify its authenticity and freshness before it is relied on."
        },
        {
          "id": "link-alternate-identifier",
          "name": "Link alternate identifier",
          "description": "Attach an identifier from another scheme to the registration record with an explicit equivalence assertion and evidence."
        },
        {
          "id": "detect-and-report-discrepancy",
          "name": "Detect and report discrepancy",
          "description": "Compare the register record with other held sources, classify divergence and discharge any statutory reporting duty."
        },
        {
          "id": "evaluate-access-request",
          "name": "Evaluate access request against tier",
          "description": "Decide whether a requester may read specified fields, documents or artifacts, and produce the audit record."
        },
        {
          "id": "project-to-exchange-format",
          "name": "Project record to an exchange format",
          "description": "Render the format-neutral record into a named external vocabulary or exchange message, declaring what is lost."
        },
        {
          "id": "close-or-supersede-record",
          "name": "Close or supersede a registration record",
          "description": "Close a record on dissolution, transfer out or supersession, retaining a tombstone and honouring retention duties."
        },
        {
          "id": "submit-register-filing",
          "name": "Update register particulars",
          "description": "File and publish changes to name, registered office, representatives, capital, objects, legal form or other disclosed particulars, with event-effective time distinct from filing time."
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-001 Organization (registered parent model)",
          "relation": "CHILD",
          "purpose": "WM-ORG-010 specialises the parent organization concept to the subset that has registered legal status, mirroring the org:Organization to org:FormalOrganization to rov:RegisteredOrganization narrowing. The parent owns organization identity in general; this model owns the registration facts.",
          "required": true,
          "source_refs": [
            "SRC-006",
            "SRC-007"
          ]
        },
        {
          "target": "Beneficial ownership and control model (sibling)",
          "relation": "REFERENCE",
          "purpose": "Hold ownership and control content, including natural-person particulars, under its own access regime. This model carries only the pointer, holding-mechanism type and access tier.",
          "required": true,
          "source_refs": [
            "SRC-018",
            "SRC-015"
          ]
        },
        {
          "target": "Postal address and location model (sibling)",
          "relation": "COMPOSE",
          "purpose": "Supply the structured address type used for legal, headquarters and other recorded addresses, and own geocoding and premises identity, which are outside registration scope.",
          "required": true,
          "source_refs": [
            "SRC-002",
            "SRC-006"
          ]
        },
        {
          "target": "Jurisdiction and geopolitical unit model (sibling)",
          "relation": "REFERENCE",
          "purpose": "Resolve country and subdivision codes, jurisdictional hierarchy and the legal systems that give legal forms their meaning; legal form and jurisdiction are interdependent and must resolve against a governed jurisdiction set.",
          "required": true,
          "source_refs": [
            "SRC-004",
            "SRC-002"
          ]
        },
        {
          "target": "Document and evidence model (sibling)",
          "relation": "COMPOSE",
          "purpose": "Own generic document lifecycle, storage, rendering and signature verification, so that certificates, extracts, filings and gazette notices are typed evidence here rather than duplicated document machinery.",
          "required": true,
          "source_refs": [
            "SRC-010",
            "SRC-008"
          ]
        },
        {
          "target": "Natural person and party identity model (sibling)",
          "relation": "REFERENCE",
          "purpose": "Resolve officers, representatives and registered agents to person records without importing person identity or employment semantics into the registration record.",
          "required": false,
          "source_refs": [
            "SRC-006",
            "SRC-008"
          ]
        },
        {
          "target": "Provenance and observation mixin",
          "relation": "MIX-IN",
          "purpose": "Apply uniform source attribution, retrieving-agent identity, and the separation of event time, source-recorded time and observation time to every assertion in this model.",
          "required": true,
          "source_refs": [
            "SRC-002",
            "SRC-006"
          ]
        },
        {
          "target": "Bitemporal versioning and history mixin",
          "relation": "MIX-IN",
          "purpose": "Provide append-only assertion history with validity and transaction intervals, which the legal entity events and data history requirement depends on.",
          "required": true,
          "source_refs": [
            "SRC-011",
            "SRC-002"
          ]
        },
        {
          "target": "Tax registration and fiscal identifier model (sibling)",
          "relation": "REFERENCE",
          "purpose": "Own fiscal registration, assessment and compliance. This model carries tax and VAT numbers only as scheme-qualified alternate identifiers and makes no inference about tax status from business-register presence.",
          "required": false,
          "source_refs": [
            "SRC-013",
            "SRC-012"
          ]
        },
        {
          "target": "Regulatory licence and authorization model (sibling)",
          "relation": "REFERENCE",
          "purpose": "Own sector authorizations that condition conduct rather than constitute existence, preventing licence withdrawal from being read as loss of legal personality.",
          "required": false,
          "source_refs": [
            "SRC-009",
            "SRC-008"
          ]
        },
        {
          "target": "Statistical business register unit model (sibling)",
          "relation": "ALIGN",
          "purpose": "Declared boundary alignment: the enterprise, enterprise group, local unit and kind-of-activity unit are constructed from legal units but are not legal units. Mapping is one-to-many in both directions and must be recorded, not assumed.",
          "required": false,
          "source_refs": [
            "SRC-016"
          ]
        },
        {
          "target": "ISO 20275 Entity Legal Forms code list",
          "relation": "ALIGN",
          "purpose": "External governed classifier for legal form, referenced with an explicit version because codes and jurisdictions are added between releases.",
          "required": true,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "W3C Registered Organization Vocabulary and Organization Ontology",
          "relation": "ALIGN",
          "purpose": "Declared alignment for export and linked-data projection. Mapping is partial: RegOrg lacks the register-authority qualification and event history this model requires, and its status remains a Working Group Note.",
          "required": false,
          "source_refs": [
            "SRC-007",
            "SRC-006"
          ]
        },
        {
          "target": "GLEIF LEI-CDF and RR-CDF reference data formats",
          "relation": "ALIGN",
          "purpose": "Declared alignment for entity and relationship reference data exchange, version-pinned to LEI-CDF 3.1 and RR-CDF 2.1; alignment is not a conformance claim and holds only for entities within the identifier system's eligibility scope.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-005"
          ]
        },
        {
          "target": "ISO/IEC 6523 identifier scheme registry",
          "relation": "REFERENCE",
          "purpose": "Supply the scheme codes that qualify alternate organization identifiers, without which an identifier value cannot be interpreted or compared.",
          "required": true,
          "source_refs": [
            "SRC-013",
            "SRC-012"
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
          "rationale": "Both providers independently returned entry_kind 'entity' and the same registry_id and name, and both draw the same primary cut against WM-ORG-001: the subject is a legal person whose identity is anchored in an authoritative register, not the social/operational organisation. The subject has a stable identity anchor (registration authority + register-assigned identifier), a lifecycle with typed events, and states that persist independently of any single observation, which is the entity test rather than an event, relation or process test. The base scope is accepted as drawn by Claude: registration facts only, with ownership content, capital and share structure, statistical units, tax assessment and sector licensing delegated to siblings."
        },
        "decisions": [
          {
            "concept": "Base provider selection",
            "disposition": "Claude as base",
            "rationale": "Claude's boundaries are the clearest and most complete: eight boundary notes with distinct neighbours, a ten-item out-of-scope list, and inline_only_rationale on nine findings that explicitly refuse to duplicate sibling models. It makes three cuts Grok does not make at all — legal unit versus statistical enterprise, registration versus sector licensing, and evidence versus a generic document model. Size is corroborating, not decisive."
          },
          {
            "concept": "Grok legal personality and capacity",
            "disposition": "Accepted into legal-form-and-classification",
            "rationale": "The one axis where Grok is materially stronger than the base. Personality, capacity, asset partitioning and the member liability shield are the substance of what registration confers, and the base models only the register's act, not the legal status it produces."
          },
          {
            "concept": "Grok eligible-party-types",
            "disposition": "Rejected as duplicative",
            "rationale": "Its category content (general entity, fund, sole proprietor, branch, international organisation) is already the base's entity-category-and-economic-activity-classification finding, and its admission-gate question is carried by the accepted legal-personality finding. Adding it would create two competing category findings in the same layer."
          },
          {
            "concept": "Grok authoritative-and-global-identifiers",
            "disposition": "Rejected as duplicative",
            "rationale": "The base already splits this across register-anchored-legal-entity-identity and cross-scheme-identifier-alignment, including syntactic validation, precedence on disagreement and global-identifier status reconciliation. LEI check-digit structure, one-LEI-per-entity uniqueness and LOU portability are question-level detail, not a third identifier finding."
          },
          {
            "concept": "Grok authoritative-register-binding",
            "disposition": "Rejected as duplicative",
            "rationale": "Fully covered by registration-authority-identification, which already carries the governed RA list, coverage scope and the constitutive-versus-validation-source distinction. The reserved RA codes for entities with no ordinary register are subsumed by the base's fallback-identity-strategy question."
          },
          {
            "concept": "Grok euid-and-bris-interconnection",
            "disposition": "Deferred as an EU regional profile",
            "rationale": "Evidence-backed but region-specific. The base deliberately generalises register-to-register exchange into interoperability-mappings-and-exchange-projections and states in its regional assumptions that EU interconnection is one realisation, not the universal pattern. Promoting it to a core finding would structurally privilege one jurisdiction and undermine multi-profile validation."
          },
          {
            "concept": "Grok constituting-instruments",
            "disposition": "Rejected, with parts deferred",
            "rationale": "The instrument-and-particulars content duplicates mandatory-disclosure-particulars-and-filing-obligations, and the disclosed-representatives content duplicates officers-and-authority-to-represent. Its remaining content — authorised and subscribed capital, stated objects, entity duration and the location of the shareholder or member register — sits outside the base boundary, which delegates capital and share structure to a capital and securities sibling."
          },
          {
            "concept": "Bearer shares and nominee arrangements",
            "disposition": "Rejected, routed to siblings",
            "rationale": "Grok's FATF-grounded transparency-obstacle content is real but is a share-structure and beneficial-ownership fact, both of which the base explicitly delegates. Recording it here would replicate restricted ownership content outside its access regime, which is the specific failure the base's beneficial-ownership-register-linkage finding was written to prevent."
          },
          {
            "concept": "Judicial declaration of nullity",
            "disposition": "Folded into existing vocabularies, grounding deferred",
            "rationale": "Grok is right that EU law requires disclosure of judicially declared nullity and the base names only dissolution, liquidation, strike-off and restoration. Nullity is a value in the governed event-type list and a ground under end-date-and-ground, not a new finding; its retroactive effect on third-party reliance needs primary-text grounding first."
          },
          {
            "concept": "Authoritative identity priority",
            "disposition": "Retain base ordering unchanged",
            "rationale": "Both providers independently land on the same priority — register authority plus register-assigned identifier first, governed global identifier (LEI, EUID) second, locally minted surrogate last and flagged as such. No adjudication needed; the agreement raises confidence in the base wording rather than requiring a merge."
          },
          {
            "concept": "Legal unit versus statistical enterprise boundary",
            "disposition": "Retain from base; absent in Grok",
            "rationale": "Claude's UNECE-grounded boundary note that one registration record is neither one enterprise nor one business, in either direction, is a load-bearing cut that Grok does not make anywhere. It is preserved verbatim as a boundary note and as the relationship-versus-statistical-group question."
          },
          {
            "concept": "Registrar-side formation function",
            "disposition": "Rejected",
            "rationale": "Grok's form-and-register-legal-entity brings a legal person into existence, which presumes the operator is the registration authority. The base is an observer-and-operator model over an external authoritative register; accepting it would silently change the model's role rather than fill a gap."
          },
          {
            "concept": "Grok corroborate-reference-data function",
            "disposition": "Rejected as duplicative",
            "rationale": "The base's request-and-verify-evidence and detect-and-report-discrepancy jointly produce and update the corroboration grade held by validation-sources-and-corroboration-level. A third overlapping verification function would blur the boundary between fetching evidence, comparing sources and grading corroboration."
          },
          {
            "concept": "Service-layer merge",
            "disposition": "Merge",
            "rationale": "Both providers place validation, access, retention and interoperability concerns in cross-cutting layers with substantially the same content; keeping them separate would fragment provenance and access enforcement across two vocabularies. Base layer identifiers govern."
          }
        ],
        "publicationHolds": [
          "Source retrieval is not verified. Claude's own adversarial checks record that EUR-Lex full texts, the FATF guidance page, the ISO catalogue and the UNECE publication all refused automated retrieval, so those citations rest on titles and published summaries rather than confirmed full text. Every accepted source must be re-fetched and its contribution re-confirmed before publication.",
          "SRC-019 (GDPRhub, authority tier 3, non-primary) carries the load-bearing claim that no general right to erasure exists against a companies register. Replace it with the primary CJEU judgment in C-398/15 (Manni) or downgrade every finding that depends on it, including personal-data-in-registration-records and record-history-retention-and-deletion-constraints.",
          "Version pins must be reconciled and re-verified as-of a single date: ELF list v1.6 (Feb 2026), GLEIF RA list v1.8.1 (Nov 2024), LEI-CDF 3.1, Peppol ICD (May 2026), schema.org 30.0, and the FATF Recommendations edition (Claude cites March 2023 guidance, Grok cites an update dated June 2026).",
          "The two providers cite different EU implementing regulations for the system of interconnection of registers — Commission Implementing Regulation (EU) 2021/1042 (Claude) and (EU) 2020/2244 (Grok). Determine which is in force, whether one repeals the other, and pin the surviving instrument before publishing any interconnection or exchange-protocol structure.",
          "Claude cites Directive (EU) 2025/25 as in force from 30 January 2025 via a Commission overview page rather than the Official Journal text. Confirm against EUR-Lex before any disclosure or interconnection claim relies on it.",
          "Domain-profile validation is incomplete. The model has been reasoned against EU, UK and global identifier-system profiles only. Before publication it must be exercised against at least: US state-level formation with no national register, a non-EU civil-law register (for example Japan or Brazil), a national identifier scheme outside the RA-list framing (China USCC, India CIN), and a jurisdiction where a legal form arises without registration, which is the case the fallback identity path exists to serve.",
          "Legal-effect characterisations — constitutive versus declaratory registration, opposability of disclosed particulars to third parties, register liability or warranty for inaccurate entries, and third-party reliance on translated versions — are stated as general rules but grounded partly in secondary summaries. Hold until each is confirmed against primary statutory text for at least two contrasting jurisdictions."
        ],
        "deferredResearch": [
          "EUID and BRIS as an explicit EU regional profile overlay (Grok SRC-003, SRC-010): EUID composition, the no-centralised-database constraint on the central platform, and the branch-disclosure and cross-border-merger notification message types — to be modelled as a jurisdiction profile bound to the base's interoperability layer, not as core structure.",
          "Registered capital, subscribed versus authorised capital, share classes, bearer shares and nominee shareholder or director arrangements: confirm the split between the capital and securities sibling model and the beneficial-ownership sibling, and decide where the FATF transparency-obstacle mitigations attach.",
          "Stated objects, entity duration and the notified location of the shareholder or member register: these are register-disclosed in many jurisdictions and are currently unowned by any model in the set; decide whether they belong here as registration facts or to the capital and governance siblings.",
          "Administrative strike-off, restoration, reinstatement and dormancy: both providers record that global instruments do not specify these and that they are nationally common. Needs national-profile research (UK, US states, Australia) to ground the base's claim that dissolution is non-absorbing within a jurisdiction-specific window.",
          "Judicial declaration of nullity of a company: primary-text grounding for its disclosure requirement, its retroactive effect on acts already performed, and whether it belongs in the event-type vocabulary as a distinct type or as a ground under termination of registered existence.",
          "FATF 'sufficient links' test for foreign-created legal persons, and how it interacts with the base's foreign-qualification and redomiciliation structure — currently only partially extracted by Grok and absent from the base.",
          "Register fee schedules and cost-of-access economics, declared a gap by the base: determine whether any primary source enumerates them across jurisdictions or whether the gap must remain declared.",
          "Whether Vercy models the registrar role at all: the rejected formation and disclosure functions imply a second actor perspective. Decide explicitly, because accepting it later would change the model's purpose statement rather than extend it."
        ]
      },
      "statistics": {
        "sources": 28,
        "bundles": 7,
        "layers": 15,
        "findings": 29,
        "questions": 118,
        "artifacts": 21,
        "functions": 12
      }
    },
    "WM-ORG-011": {
      "source_file": "publications/wm-org-011-business-establishment-branch/spec.yaml",
      "source_bytes": 98436,
      "source_sha256": "3f9170a43804efa776b942b76d7c6ac5b836f23c7bf5f7de0f5285a48088fa2f",
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-09-09T20:04:30Z",
        "synthesisSha256": "d27bb1dfc0581d8c597b3cc463476d07ab2431732e54776f02338edb4ba3f1d4",
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
        "id": "WM-ORG-011",
        "registryId": "vr.wm-org-011",
        "name": "Business Establishment / Branch",
        "version": "0.3.0-research.1",
        "previousVersions": [],
        "entryKind": "aggregate",
        "family": "World Models",
        "category": "Society, people and institutions",
        "industry": [
          "Cross-industry"
        ],
        "domain": [
          "SOC.ORG.EST"
        ],
        "tags": [
          "business",
          "establishment",
          "branch",
          "soc.org.est"
        ],
        "status": "published"
      },
      "model": {
        "registry_id": "vr.wm-org-011",
        "model_id": "WM-ORG-011",
        "name": "Business Establishment / Branch",
        "entry_kind": "aggregate",
        "purpose": "Describe an organization operating presence with explicit source-defined kind, operator, sites, local activity and evidence.",
        "scope_statement": "One record represents an establishment, branch or outlet under a declared definition and jurisdiction. These kinds are not interchangeable. Organizational identity, physical premises, statutory authority and service execution retain their own masters.",
        "in_scope": [
          "Issuer-qualified presence identity and organizational attachment",
          "Time-bound sites, local activity, recognition and availability",
          "Scoped mandate, register evidence, continuity, reporting grain and governed exchange"
        ],
        "out_of_scope": [
          "Treating every branch as one premises or a separate legal person",
          "Automatic registration, permit determination or service execution",
          "Remastering building geometry, organization accounts or private personnel records"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-001 Organization",
            "distinction": "Proposed REFERENCE: operating presence is not the entire parent or legal entity.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-004"
            ]
          },
          {
            "neighbor": "Physical premises and organizational unit",
            "distinction": "A site can host several units; an organizational unit is not its address.",
            "source_refs": [
              "SRC-004",
              "SRC-005"
            ]
          },
          {
            "neighbor": "Statistical establishment versus international branch",
            "distinction": "Source-qualified kind is mandatory; GLEIF branch scope may encompass several offices.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-006"
            ]
          },
          {
            "neighbor": "Service, permit and reporting masters",
            "distinction": "Keep scoped references; public listing is not service permission or proof of legal standing.",
            "source_refs": [
              "SRC-006",
              "SRC-007",
              "SRC-008"
            ]
          }
        ]
      },
      "structure_index": [
        {
          "id": "presence-operating-identity-and-organizational-attachment",
          "name": "Operating identity and organizational attachment",
          "description": "Organizational operating-presence concerns: operating identity and organizational attachment.",
          "layers": [
            {
              "id": "establishment-kind",
              "name": "Kind, issuer and identity boundary",
              "description": "Source-qualified organizational presence record for kind, issuer and identity boundary. No universal equivalence of branch, legal entity and premises is implied."
            },
            {
              "id": "operator-attachment",
              "name": "Operator, parent and legal accountability",
              "description": "Source-qualified organizational presence record for operator, parent and legal accountability. No universal equivalence of branch, legal entity and premises is implied."
            }
          ]
        },
        {
          "id": "presence-sites-and-recognizable-presence",
          "name": "Sites and recognizable presence",
          "description": "Organizational operating-presence concerns: sites and recognizable presence.",
          "layers": [
            {
              "id": "site-binding",
              "name": "Site bindings and address roles",
              "description": "Source-qualified organizational presence record for site bindings and address roles. No universal equivalence of branch, legal entity and premises is implied."
            },
            {
              "id": "presence-recognition",
              "name": "Public identity and recognition evidence",
              "description": "Source-qualified organizational presence record for public identity and recognition evidence. No universal equivalence of branch, legal entity and premises is implied."
            }
          ]
        },
        {
          "id": "presence-local-activity-and-usable-services",
          "name": "Local activity and usable services",
          "description": "Organizational operating-presence concerns: local activity and usable services.",
          "layers": [
            {
              "id": "local-activity",
              "name": "Activity classification and scope",
              "description": "Source-qualified organizational presence record for activity classification and scope. No universal equivalence of branch, legal entity and premises is implied."
            },
            {
              "id": "service-availability",
              "name": "Opening, availability and access conditions",
              "description": "Source-qualified organizational presence record for opening, availability and access conditions. No universal equivalence of branch, legal entity and premises is implied."
            }
          ]
        },
        {
          "id": "presence-local-authority-and-registration-evidence",
          "name": "Local authority and registration evidence",
          "description": "Organizational operating-presence concerns: local authority and registration evidence.",
          "layers": [
            {
              "id": "local-mandate",
              "name": "Mandate, roles and contact responsibility",
              "description": "Source-qualified organizational presence record for mandate, roles and contact responsibility. No universal equivalence of branch, legal entity and premises is implied."
            },
            {
              "id": "registration-evidence",
              "name": "Registration and scoped operating authorization",
              "description": "Source-qualified organizational presence record for registration and scoped operating authorization. No universal equivalence of branch, legal entity and premises is implied."
            }
          ]
        },
        {
          "id": "presence-continuity-and-reporting-grain",
          "name": "Continuity and reporting grain",
          "description": "Organizational operating-presence concerns: continuity and reporting grain.",
          "layers": [
            {
              "id": "presence-continuity",
              "name": "Opening, relocation and succession",
              "description": "Source-qualified organizational presence record for opening, relocation and succession. No universal equivalence of branch, legal entity and premises is implied."
            },
            {
              "id": "reporting-scope",
              "name": "Statistical scope and local measures",
              "description": "Source-qualified organizational presence record for statistical scope and local measures. No universal equivalence of branch, legal entity and premises is implied."
            }
          ]
        },
        {
          "id": "presence-governed-establishment-knowledge",
          "name": "Governed establishment knowledge",
          "description": "Organizational operating-presence concerns: governed establishment knowledge.",
          "layers": [
            {
              "id": "presence-governance",
              "name": "Mastership, freshness and disclosure",
              "description": "Source-qualified organizational presence record for mastership, freshness and disclosure. No universal equivalence of branch, legal entity and premises is implied."
            },
            {
              "id": "presence-exchange",
              "name": "Interoperability and semantic acceptance",
              "description": "Source-qualified organizational presence record for interoperability and semantic acceptance. No universal equivalence of branch, legal entity and premises is implied."
            }
          ]
        }
      ],
      "selected_findings": [
        {
          "bundle": "presence-operating-identity-and-organizational-attachment",
          "layer": "establishment-kind",
          "finding": {
            "id": "establishment-kind-record",
            "name": "Kind, issuer and identity boundary record",
            "description": "Source-qualified organizational presence record for kind, issuer and identity boundary. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003",
              "SRC-006"
            ],
            "questions": [
              "Which operating-presence kind and source definition identify this record rather than a legal entity or building?",
              "Which issuer-qualified identifiers and aliases refer to this exact unit, and which identify only its parent or premises?",
              "Which evidence distinguishes co-located establishments or a multi-site branch without merging them by name or address?"
            ],
            "data_elements": [
              {
                "id": "establishment-kind-subject-kind",
                "name": "subject-kind",
                "description": "Proposed structured answer group: kind code; definition URI; jurisdiction; applicability. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "establishment-kind-identity-set",
                "name": "identity-set",
                "description": "Proposed structured answer group: issuer; identifier; alias kind; effective interval. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "establishment-kind-distinction-evidence",
                "name": "distinction-evidence",
                "description": "Proposed structured answer group: neighbor refs; matching criteria; evidence refs; uncertainty. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-operating-identity-and-organizational-attachment",
          "layer": "operator-attachment",
          "finding": {
            "id": "operator-attachment-record",
            "name": "Operator, parent and legal accountability record",
            "description": "Source-qualified organizational presence record for operator, parent and legal accountability. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-002",
              "SRC-004",
              "SRC-006"
            ],
            "questions": [
              "Which organization operates this presence and which legal entity is accountable under the recorded profile?",
              "Is the relationship a branch, unit, ownership, franchise or brand association, and what evidence supports that exact relation?",
              "Which changes of operator or parent preserve this identity and which require an evidenced successor under the issuer's rules?"
            ],
            "data_elements": [
              {
                "id": "operator-attachment-accountable-parties",
                "name": "accountable-parties",
                "description": "Proposed structured answer group: operator ref; legal entity ref; role; profile. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "operator-attachment-organizational-links",
                "name": "organizational-links",
                "description": "Proposed structured answer group: target ref; relation kind; authority; valid interval. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "operator-attachment-continuity-rule",
                "name": "continuity-rule",
                "description": "Proposed structured answer group: issuer rule; change ref; predecessor; successor; decision. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-sites-and-recognizable-presence",
          "layer": "site-binding",
          "finding": {
            "id": "site-binding-record",
            "name": "Site bindings and address roles record",
            "description": "Source-qualified organizational presence record for site bindings and address roles. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-004",
              "SRC-005",
              "SRC-006"
            ],
            "questions": [
              "Which physical or digital sites are bound to this unit during each period, and which are merely correspondence addresses?",
              "Which site is registered, primary, headquarters or customer-facing without assuming these roles coincide?",
              "Which premises, entrance and geospatial master references locate the presence without making the organization itself a building?"
            ],
            "data_elements": [
              {
                "id": "site-binding-site-bindings",
                "name": "site-bindings",
                "description": "Proposed structured answer group: site ref; site kind; relationship period; address role. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "site-binding-site-roles",
                "name": "site-roles",
                "description": "Proposed structured answer group: role code; site ref; authority; validity. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "site-binding-premises-location",
                "name": "premises-location",
                "description": "Proposed structured answer group: premises ref; entrance ref; coordinate ref; evidence. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-sites-and-recognizable-presence",
          "layer": "presence-recognition",
          "finding": {
            "id": "presence-recognition-record",
            "name": "Public identity and recognition evidence record",
            "description": "Source-qualified organizational presence record for public identity and recognition evidence. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-003",
              "SRC-005",
              "SRC-007",
              "SRC-008"
            ],
            "questions": [
              "Which trading names, signs, contact channels and official pages identify this particular outlet rather than its entire chain?",
              "What observed evidence confirms presence at the claimed site, and how recent and reliable is it?",
              "Which misleading names, shared phone numbers or stale listings create ambiguity requiring a separate candidate match?"
            ],
            "data_elements": [
              {
                "id": "presence-recognition-public-identity",
                "name": "public-identity",
                "description": "Proposed structured answer group: trading name; sign evidence; channel refs; official page. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "presence-recognition-presence-observation",
                "name": "presence-observation",
                "description": "Proposed structured answer group: method; observation time; source; confidence. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "presence-recognition-matching-ambiguity",
                "name": "matching-ambiguity",
                "description": "Proposed structured answer group: candidate refs; conflicting signals; disposition; reviewer ref. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-local-authority-and-registration-evidence",
          "layer": "local-mandate",
          "finding": {
            "id": "local-mandate-record",
            "name": "Mandate, roles and contact responsibility record",
            "description": "Source-qualified organizational presence record for mandate, roles and contact responsibility. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-004",
              "SRC-006",
              "SRC-008"
            ],
            "questions": [
              "Who holds local responsibility and what source-defined role or delegation applies?",
              "Which actions may that role authorize, with what financial, territorial or temporal limits?",
              "How can an agent reach an authorized contact without exposing private staff details or mistaking a contact listing for a mandate?"
            ],
            "data_elements": [
              {
                "id": "local-mandate-local-roles",
                "name": "local-roles",
                "description": "Proposed structured answer group: role ref; holder ref; authority evidence; period. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "local-mandate-mandate-scope",
                "name": "mandate-scope",
                "description": "Proposed structured answer group: action kinds; limits; delegation ref; expiry. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "local-mandate-contact-routing",
                "name": "contact-routing",
                "description": "Proposed structured answer group: official channel; purpose; disclosure rule; verification time. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-local-authority-and-registration-evidence",
          "layer": "registration-evidence",
          "finding": {
            "id": "registration-evidence-record",
            "name": "Registration and scoped operating authorization record",
            "description": "Source-qualified organizational presence record for registration and scoped operating authorization. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-006",
              "SRC-008"
            ],
            "questions": [
              "Which register records recognize this kind of unit, with which jurisdiction, identifier and current status?",
              "Which referenced permits or authorizations cover which local activities and sites, and when do they apply?",
              "Which missing, expired or conflicting evidence requires an unresolved status rather than a claim that operation is legally permitted?"
            ],
            "data_elements": [
              {
                "id": "registration-evidence-register-evidence",
                "name": "register-evidence",
                "description": "Proposed structured answer group: register URI; record ID; unit kind; status; checked at. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "registration-evidence-authorization-bindings",
                "name": "authorization-bindings",
                "description": "Proposed structured answer group: permit ref; scope; jurisdiction; validity. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "registration-evidence-standing-uncertainty",
                "name": "standing-uncertainty",
                "description": "Proposed structured answer group: gap; conflict refs; consequence; responsible reviewer. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-continuity-and-reporting-grain",
          "layer": "presence-continuity",
          "finding": {
            "id": "presence-continuity-record",
            "name": "Opening, relocation and succession record",
            "description": "Source-qualified organizational presence record for opening, relocation and succession. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-002",
              "SRC-004",
              "SRC-005",
              "SRC-009"
            ],
            "questions": [
              "Which events establish opening, suspension, resumption, relocation or closure, and which dates are effective versus recorded?",
              "Did the event change the operating unit, premises, parent or only a public label?",
              "Which successor and predecessor links preserve history without reusing retired identifiers contrary to their issuer's rules?"
            ],
            "data_elements": [
              {
                "id": "presence-continuity-lifecycle-events",
                "name": "lifecycle-events",
                "description": "Proposed structured answer group: event ref; type; effective time; recorded time; source. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "presence-continuity-change-subject",
                "name": "change-subject",
                "description": "Proposed structured answer group: affected entity ref; changed attributes; unchanged identity rationale. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "presence-continuity-succession-links",
                "name": "succession-links",
                "description": "Proposed structured answer group: predecessor; successor; issuer policy; evidence. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-continuity-and-reporting-grain",
          "layer": "reporting-scope",
          "finding": {
            "id": "reporting-scope-record",
            "name": "Statistical scope and local measures record",
            "description": "Source-qualified organizational presence record for statistical scope and local measures. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-006",
              "SRC-008"
            ],
            "questions": [
              "Which observation or reporting-unit definition applies to local employment, output or other reported measures?",
              "Which period, unit, coverage and source qualify each value, and is it measured, estimated, suppressed or unavailable?",
              "Which parent or co-located unit totals already include these measures, preventing duplicate aggregation?"
            ],
            "data_elements": [
              {
                "id": "reporting-scope-reporting-grain",
                "name": "reporting-grain",
                "description": "Proposed structured answer group: statistical unit kind; definition ref; covered activities; locations. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "reporting-scope-reported-measures",
                "name": "reported-measures",
                "description": "Proposed structured answer group: measure code; value state; unit; period; source. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "reporting-scope-aggregation-boundary",
                "name": "aggregation-boundary",
                "description": "Proposed structured answer group: included unit refs; overlap rule; parent totals; exclusions. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              }
            ]
          }
        },
        {
          "bundle": "presence-governed-establishment-knowledge",
          "layer": "presence-governance",
          "finding": {
            "id": "presence-governance-record",
            "name": "Mastership, freshness and disclosure record",
            "description": "Source-qualified organizational presence record for mastership, freshness and disclosure. No universal equivalence of branch, legal entity and premises is implied.",
            "source_refs": [
              "SRC-001",
              "SRC-004",
              "SRC-008"
            ],
            "questions": [
              "Which organization or register owns each assertion and which local copies are derived projections?",
              "How are contradictory operator, address, activity or status claims retained and reviewed without silently selecting a convenient source?",
              "Which roles may read or export establishment, contact and statistical details, under what retention and correction rules?"
            ],
            "data_elements": [
              {
                "id": "presence-governance-assertion-mastership",
                "name": "assertion-mastership",
                "description": "Proposed structured answer group: field scope; master ref; cache ref; refresh rule. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "presence-governance-contested-assertions",
                "name": "contested-assertions",
                "description": "Proposed structured answer group: claim refs; authority comparison; review status; valid times. Preserve explicit unknowns and master references; executable nested schema is deferred.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true
              },
              {
                "id": "presence-governance-information-policy",
                "name": "information-policy",
                "description": "Proposed structured answer group: role scope; export limits; retention ref; correction receipt. Preserve explicit unknowns and master references; executable nested schema is deferred.",
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
          "id": "resolve-presence",
          "name": "Resolve operating presence",
          "description": "Disambiguate a presence using source-qualified identity."
        },
        {
          "id": "locate-presence",
          "name": "Locate current sites",
          "description": "Resolve time-bound site roles and evidence."
        },
        {
          "id": "describe-local-service",
          "name": "Describe usable local services",
          "description": "Combine service references with qualified availability."
        },
        {
          "id": "check-mandate-evidence",
          "name": "Check authority evidence completeness",
          "description": "Inspect scoped mandate and registration evidence, not legal validity."
        },
        {
          "id": "record-continuity",
          "name": "Record organizational presence change",
          "description": "Preserve relocation, closure and succession decisions."
        },
        {
          "id": "exchange-presence",
          "name": "Exchange with unit-grain losses",
          "description": "Map presence into a target vocabulary without erasing distinctions."
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-001",
          "relation": "REFERENCE",
          "purpose": "Resolve operator and parent organization while preserving distinct presence identity; proposed typed relation.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-004"
          ]
        },
        {
          "target": "https://www.w3.org/TR/vocab-org/",
          "relation": "ALIGN",
          "purpose": "Candidate organization, unit and site mapping; not complete mandate conformance.",
          "required": false,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "https://www.gs1.org/standards/id-keys/gln",
          "relation": "ALIGN",
          "purpose": "Qualify party/function/location identifiers without identity conflation.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "https://schema.org/LocalBusiness",
          "relation": "ALIGN",
          "purpose": "Optional public discovery projection of local services and contacts.",
          "required": false,
          "source_refs": [
            "SRC-007"
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
          "rationale": "One source-defined organizational presence with explicit kind, sites and operator attachment; establishment, branch, outlet, organization and premises remain distinct. REFERENCE WM-ORG-001 is an explicit proposed boundary relation."
        },
        "decisions": [
          {
            "concept": "Unit kind and identity",
            "disposition": "accepted with limitations",
            "rationale": "Require source and jurisdiction discriminator; retain statistical local-unit versus multi-office branch differences."
          },
          {
            "concept": "Organization and premises",
            "disposition": "accepted",
            "rationale": "Operator, legal entity, unit and site have separate identities and time-bound relations."
          },
          {
            "concept": "Identifiers and continuity",
            "disposition": "accepted with limitations",
            "rationale": "Common names, addresses or codes do not imply equivalence; continuity follows evidenced issuer rules."
          },
          {
            "concept": "Local service and mandate",
            "disposition": "accepted with limitations",
            "rationale": "Schedules, public contacts and registry records do not establish capacity, operating permission or delegation."
          },
          {
            "concept": "Evidence and conformance",
            "disposition": "deferred",
            "rationale": "Selected source passages and proposed fixtures support a design, not exhaustive statutory or executable adapter assurance."
          },
          {
            "concept": "Provider attribution",
            "disposition": "accepted with mandatory hold",
            "rationale": "Both external providers timed out once. Separate frozen Codex self-audit is not independent review."
          }
        ],
        "publicationHolds": [
          "No independent external research or reviewer: Claude and Grok each timed out once. Codex-only research and self-review remain reviewable-draft, never canonical.",
          "Source-defined establishment, branch and outlet kinds are not synonyms; profile review and any future model split require governed migration.",
          "GS1 overview evidence is indexed text with direct HTTP 403. Allocation rules and mutable source release pins are not fully inspected.",
          "GLEIF 2.8.5 selected clauses are historical reference evidence; replacement releases and full applicability remain unverified.",
          "No complete statutory inventory, executable nested instance schema, registry resolver, legal-standing verifier or real multi-registry fixture is delivered.",
          "Actual local delegation, service availability, premises accessibility, confidentiality and retention must be established by adopters.",
          "Independent external review was explicitly waived by the repository owner; this codex-only result remains a reviewable draft."
        ],
        "deferredResearch": [
          "Independent external review and exact source release pins.",
          "Profile-specific establishment, registered branch and outlet boundaries with governed split options.",
          "Complete GLN allocation and current GLEIF rules with loss-aware adapters.",
          "Executable negative fixtures for co-location, multi-site branches, relocation and suppressed reporting measures."
        ]
      },
      "statistics": {
        "sources": 9,
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
    "All three current publications are reviewable drafts with publishableCanonical false.",
    "WM-ORG-011 used a single-provider waiver and lacks independent external review.",
    "The complete specs were parsed and pinned by byte count and SHA-256; selected findings form the compact reviewer projection.",
    "Registry relations and Enterprise v1 properties remain non-normative."
  ]
}

```

## CLAUDE STUDY

# Boundary review — EM-ORG-02 Legal Identity and Registration

*Independent reviewer opinion on frozen dossier only. No canonical status, legal effect, approved relation or installability is claimed or implied.*

## Verdict per model

**WM-ORG-001 Organization — PROFILE.** Retain as the single master of organization / legal-subject identity (the party that can be a contract counterparty, carry a canonical key, bear entity status, succession and continuity). Profile it by demoting its `formation-and-registry-entries` and `standing-status-and-obligations` layers from owned structure to typed references into registration records. It keeps `entity-status`, `canonical-key-selection`, `entity-resolution-and-duplicates`, `lifecycle-event-records`, `succession-and-continuity`, `dissolution-and-expiry`. It surrenders `register-code`, `register-entity-number`, `register-entry-date`, `cross-register-identifier` and `record-registration-status` as owned elements.

**WM-ORG-010 Legal Entity Registration — PROFILE (re-subjected), not merge/retire.** Independent identity and lifecycle are proven for the *registration record*: it has its own key (authority + assigned number), its own status enumeration (published/pending/lapsed/retired/duplicate), its own evidence, currency and renewal clocks, and it can lapse while the subject lives. That is not the lifecycle of WM-ORG-001. But its declared subject is wrong: `register-anchored-legal-entity-identity` makes "(registration authority, register identifier)" the *master identity of the legal person*. That is the direct generator of duplicate `LegalEntity` and must be re-subjected to master the *record*, not the person.

**WM-ORG-011 Business Establishment / Branch — PROFILE, narrowed, with a standing publication hold.** Keep as master for operating presence (site bindings, local activity, availability, presence recognition, reporting grain). Strip any mastership claim over `registration-evidence-record` as a source of legal standing; it may cache a reference to a WM-ORG-010 registration record but must not assert registered existence. Evidence depth is the weakest in the set (single-provider waiver, no independent external review, 9 sources, templated "proposed structured answer group" data elements), so it is not eligible to master anything a legal or compliance answer depends on.

No identifier-unassigned candidate is proposed. The three needed subjects — legal subject, registration record, operating presence — are covered by the three existing identifiers once re-subjected.

## Evidence state

All three publications are `reviewable-draft`, `publishableCanonical: false`. WM-ORG-001 and WM-ORG-010 are dual-provider adjudicated and boundary-reviewed; WM-ORG-011 is Codex-only under an owner waiver, self-audited, which is not independent review. WM-ORG-011's dossier depth is `index-and-publication-metadata`, below the other two. Selected findings are a reviewer projection of specs pinned at 301830 / 279735 / 98436 bytes with stated SHA-256; full semantic crosswalk was not performed here and is not asserted. Registry relations and Enterprise v1 candidate properties are non-normative.

## Identity / mastership reconciliation

One subject master: **WM-ORG-001**. One master per registration record: **WM-ORG-010**, with *one record per (registration authority, register instance, assigned entry)* — never one record per legal person. Cardinality is subject 1 → 0..n registration records. Zero is a first-class case (informal collectives, statute-formed bodies), which WM-ORG-001 already admits and WM-ORG-010's `CHILD`/`required: true` composition does not; that composition must be re-read as an upward reference from record to subject, not a subtype narrowing that forces every registered subject to exist twice.

The duplicate-LegalEntity guard is a mastership rule, not a matching heuristic: **ingesting a registration record never mints a subject.** Subject creation and subject merge are separate, evidenced decisions owned by WM-ORG-001's `reconcile-duplicate-records`, carrying method, compared attributes, confidence, decider, reversibility and an explicit *non-match* outcome, with tombstones that keep retired keys resolvable.

## Registration and identifier contract

Five separable things, none substituting for another:

1. **Subject status** — is the organization in existence and operating (WM-ORG-001 `entity-status`).
2. **Registration-record status** — standing of one record/identifier as a data object (WM-ORG-010), n per subject, independently dated.
3. **LEI** — a governed global identifier layered over a register entry, with its own record status; never the subject key by default, never evidence of personality.
4. **Tax / VAT identifier** — different authority, different act, and frequently a *different unit* (VAT group, establishment). Carried scheme-qualified; never a merge key.
5. **National register number** — meaningful only inside its authority's namespace.
6. **Evidence extract** — a dated, authenticated artifact speaking as of a point in time with a freshness window; it is provenance, never a status and never an identity.

**Equality test.** Two identifier values denote the same thing only if *scheme code* matches, *issuing authority/jurisdiction* matches, and the *validity intervals* overlap at the queried time. Equal strings across schemes, across authorities, or across disjoint validity windows are non-matches. Cross-scheme sameness is only ever an explicit, evidenced `identifier-equivalence-assertion` with strength — not an inferred join.

## Branch / establishment boundary

Three discriminators, applied in order, each independent of the others:

- **Legal personality** — can the subject independently bear rights and enter contracts? Yes → independent legal entity, its own WM-ORG-001 subject.
- **Register entry** — does an authority hold an entry for it? A branch typically has one (and may hold its own LEI under category BRANCH) *without* personality. Registration therefore never implies personality.
- **Operating locus** — a place of activity with neither personality nor register entry is an establishment/premises only.

Resulting placement: a registered non-person branch is a WM-ORG-001 subject record with `legal-personality-flag = false` and an attribution edge to the head-office legal person; its host-register entry is a WM-ORG-010 record; its physical operation is a WM-ORG-011 presence. Obligations and contracts attribute to the head office. A presence may span several sites, and a branch registration may span several presences — the mapping is many-to-many and must be recorded, never assumed.

## Succession and temporal rules

Three clocks kept separate on every assertion: event-effective time, authority-recorded time, observation time. Changes are classified by WM-ORG-001's `continuity-decision`: name change, seat transfer, legal-form conversion and restoration normally *preserve* identity; merger by formation, division and (jurisdiction-dependent) discontinuous redomiciliation *create* a successor subject with predecessor/successor edges. Succession writes new edges only — it never rewrites the party of an executed contract, never back-dates the predecessor's identifiers, and never reassigns a retired key. Predecessors remain resolvable after dissolution; deletion is a retention decision, not a consequence of cessation.

## Invariants

1. A registration record references exactly one subject; a subject has 0..n registration records.
2. No registration ingestion creates, merges or splits a subject.
3. Register number uniqueness holds only within (scheme, authority/jurisdiction, validity); never globally.
4. Registration-record status never substitutes for subject status, in either direction.
5. Register entry ≠ legal personality; personality is asserted separately and evidenced.
6. LEI, tax/VAT and register number are distinct scheme-qualified facts; no silent cross-scheme join.
7. An extract is a dated snapshot with an as-of time; it never sets status by itself.
8. Succession adds edges; historical parties, names and identifiers are immutable.
9. Retired identifiers are never reassigned and remain resolvable.
10. Every as-of query answers from assertion history, not from current state.
11. Operating presence asserts no legal standing.

## Scenario walkthrough

**Negative case.** A new extract arrives from register RA2 for a company already held under RA1. Under WM-ORG-010's current wording, the (RA2, number) pair is itself the master identity, so ingestion mints a second legal person; the company now appears twice, with split statuses and split contract history. Under the profiled contract, ingestion creates registration record R2 only, in `unlinked` state. Linking R2 to subject S is a separate resolution decision: compared attributes, evidence, confidence, decider, and a recorded outcome that may be *non-match* (two genuinely different companies) or *link* (one subject, two registers). Either outcome is auditable and reversible; neither is reachable by ingest alone.

**Acceptance case.** Subject S holds R1 (home register), R2 (LEI, own record status), R3 (VAT, different authority). Branch B is a subject with `legal-personality-flag = false`, head-office edge to S, host-register record R4, and presence P1. S is absorbed into T by merger effective E. Query "who was the party, and was the entity active, on date T0 < E": return S, entity status from the assertion true at T0, name valid at T0, and the subset of R1–R3 whose validity covers T0 — R2 may be `LAPSED` at T0 while S is active, and that is reported, not reconciled. B resolves to S, not to itself, as obligor. Query at T1 > E returns T as current subject with a predecessor edge to S, while the pre-E contract still names S.

## Migration / profile shape

Move from WM-ORG-001 to WM-ORG-010 as references: register code, register entity number, entry date, cross-register identifier, record registration status, registration evidence. Retain in WM-ORG-001: canonical key and tier, aliases, entity status, entity category and personality flag, formation act, lifecycle events, succession and continuity, dissolution, entity resolution. Re-subject WM-ORG-010's `register-anchored-legal-entity-identity` to a registration-record key, add a mandatory subject reference, and relax the `required: true` CHILD composition to an upward reference. Narrow WM-ORG-011 to presence; convert its `registration-evidence-record` to a read-only reference. Add a non-owned registration-record status vocabulary mapping per authority with declared mapping loss.

## Gaps and publication holds

All inherited holds stand and none are discharged here: unverified source retrieval and version pins in both dual-provider models (GLEIF URL variants, ISO catalogue pages rather than normative text, unreachable FATF, contested EU implementing regulation, GDPRhub as a load-bearing tier-3 source), incomplete multi-profile validation (US state formation, non-EU civil-law registers, China USCC / India CIN, forms arising without registration), unreframed multilingual co-equal legal names in WM-ORG-001, and WM-ORG-011's absence-of-independent-review hold. New holds from this review: the WM-ORG-010 subject re-designation is unvalidated against fixtures; the branch triple-placement (subject + registration + presence) has no worked fixture; no semantic crosswalk between WM-ORG-001 and WM-ORG-010 status vocabularies exists; identifier-equality and non-match cases have no negative fixtures. Until these are closed, this is a boundary opinion on a frozen draft — not an approved relation set, not canonical, not installable.


## GROK STUDY

**Verdict.** PROFILE all three. No new catalogue or runtime ID. WM-ORG-001 is the single organization / legal-subject master. WM-ORG-010 is re-subjected to registration *records*, each referencing exactly one 001 subject. WM-ORG-011 is narrowed to operating presence and only references registration evidence. This is standards alignment, not a GLEIF, ISO 17442 or companies-register conformance claim.

**Subject / record mastership.** Source facts: the card says a registry record has its own identity and a verifiable basis; registration status does not substitute for subject status. 010 today treats the pair (registration authority, assigned identifier) as legal-person identity — that is the defect this PROFILE corrects. 001 already holds legal personality, subject lifecycle and succession. 011 already states there is no universal equivalence of branch, legal entity and premises.

- **001** owns subject identity, `legalPersonality`, subject status with its own validity, name forms, and succession continuity. It does not own the register line. A subject may have `legalPersonality=false` (registered branch) and remain a 001 subject attributed to a head-office subject.

- **010** owns the register/authority, scheme, number, record status, evidence extract, issue/lapse dates, and `subjectRef` cardinality 1. The pair (authority, number) identifies a *record*, not a person. One subject may have many 010 records (national number, LEI, VAT, foreign-branch entry). LEI, tax/VAT, national number and EUID are records under different schemes, not extra subjects.

- **011** owns presence kind, operator / head-office attribution, site / premises reference, local activity and opening/closing. It references a 001 subject and, when present, 010 evidence. It does not mint a subject and does not assert personality.

**Identifier equality.** A number is unique within scheme and jurisdiction (card invariant). Two identifier tokens are the same registration identifier only if `(scheme, authority-or-jurisdiction, number, overlapping validity)` match. A bare number with no scheme is uninterpretable. Cross-scheme links (LEI ↔ company number ↔ VAT) are explicit, evidenced equivalence assertions with source, confidence and validity — never string equality. Importing a record cannot create or merge a subject.

**Status distinctions.** Six independently dated planes. None substitutes for another. Missing on one plane is `unknown`, not copied.

1. **Subject status** (001) — active, in liquidation, dissolved, converted, informal. A lapsed LEI does not dissolve the company.
2. **Registration-record status** (010) — pending, issued/published, lapsed, retired, duplicate, annulled, transferred.
3. **LEI status** — a 010 record under the GLEIF scheme. Issued / Lapsed / Retired is record status. LEI EntityStatus is a *claim about the subject*, stored as evidence pointing at 001. GLEIF itself separates EntityStatus from RegistrationStatus.
4. **Tax / VAT registration status** — a separate 010 record. VAT deregistration ≠ dissolved subject.
5. **National register-number status** — 010 under that authority. A strike-off proposal is a record/procedure flag until 001 is updated from an authoritative event.
6. **Evidence extract** — an observation of a 010 record at a knowledge-time. Extract currency ≠ current record status ≠ subject status.

As-of queries apply one `(valid-time, knowledge-time)` pair to subject, each record and each extract separately.

**Branch / presence boundary.** Registration, personality and premises are separate tests. A registered branch with no separate legal personality:

1. Personality on 001: head-office subject `legalPersonality=true`. If a branch-as-organization row is kept, it has `legalPersonality=false` and `bearingLegalPerson →` head office. Never mint personality from a branch number. GLEIF alignment: an international branch is the same legal person as its head office; it may hold its own LEI as a *record*.
2. Head-office attribution on 011 (or a 012 relationship).
3. 010 branch or LEI-BRANCH record keyed by (authority, number), `subjectRef` to the non-person subject.
4. 011 presence for premises/activity, referencing that 010 evidence.

Passing registration does not pass personality. Passing premises does not pass registration. An unregistered domestic site is 011 only.

**Succession.** 001 owns predecessor/successor edges with transition kind (merger, split, absorption, conversion), effective time, continuity decision and carried/lapsed identifiers. 010 may record register-side events (struck off, converted, successor number in *that* register) pointing at the same 001 edge. Historical contract parties stay the 001 identifiers current at formation. Succession adds edges; it never rewrites those party identifiers (card invariant).

**Scenario results.**

*Negative — new extract creates a duplicate company.* Extract from register B arrives with a different (scheme, authority) pair. Correct path: create or update a 010 record; bind to an existing 001 subject only by evidenced equivalence; otherwise remain `unresolved`. Same scheme+authority+number+overlap as an existing 010 → same record (or record-status DUPLICATE). Minting Company-2 fails the card.

*Acceptance — one subject, three records, non-person branch, merger.* Subject S has 010-R1 (national register ISSUED), 010-R2 (LEI, possibly lapsed independently), 010-R3 (VAT). Branch B: 001 with `legalPersonality=false`, attributed to S; 010 branch record; 011 presence. Merger at \(t_m\) adds S → S′. Contracts dated before \(t_m\) still cite S. As-of \(t < t_m\): S is current; three record statuses independently dated; B visible if valid at \(t\). As-of \(t \ge t_m\): S′ is current; S remains resolvable via the edge; B attribution changes only by an explicit act.

**Migration field moves.**

- 001 → 010: register-authority + number used as subject identity; register-record status living only on the organization; extract-as-identity; alternate scheme numbers stored as if they were the 001 key. 001 keeps subject id, `legalPersonality`, subject status, succession edges, name forms, and a derived index of bound 010 records.
- 010 → 001: drop “authority+number *is* the legal person.” Each record gains mandatory `subjectRef`. Legal form / personality copied from an extract become claims on the record, accepted onto 001 only by an evidenced subject update. 010 entity-status axis becomes a projection, not a second write path.
- 011: drop any field that asserts personality or treats a branch number as a new 001 id. Keep kind, operatorRef, site, activity, evidenceRef → 010.

**Required constraints.** One 010 record → exactly one 001 subject. Import creates records, not subjects. Identifier equality = scheme + authority/jurisdiction + overlapping validity. Cross-scheme equivalence is explicit and evidenced. Six status planes never substitute. 011 references; it does not master subjects. Succession adds edges; contracts keep historical party ids.

**Publication blockers.** All three bases are non-canonical reviewable drafts; 011 has no independent external review. 010’s published identity rule still equates authority+number with the legal person until the PROFILE text lands. Dual-write of subject status versus 010 entity-status is unresolved. No executable fixtures for: extract-does-not-mint-subject; three independently dated records; four-test non-person branch; merger that preserves historical contract parties; as-of queries with mixed record statuses. Source-pin holds on 010 (RA list, ELF, BRIS instrument) remain. Alignments to GLEIF LEI-CDF, ISO 6523 and ISO 17442 are alignments only. Do not invent LegalEntity, Registration or Branch runtime identifiers.


## PROVIDER COMPARISON

# EM-ORG-02 provider comparison

Claude and Grok independently converge on **PROFILE** across `WM-ORG-001`, `WM-ORG-010` and `WM-ORG-011`, with no new catalogue or runtime identifier. `WM-ORG-001` remains the sole organization/legal-subject identity and continuity master. `WM-ORG-010` is narrowed to registration records, each linked to exactly one subject after explicit evidence-backed resolution. `WM-ORG-011` is narrowed to operating presence and never establishes personality or mints a subject.

Both reject identity merge from a new extract, equal unqualified number or premises; separate legal personality, registration and presence; and preserve predecessor identity on historical contracts through succession. Grok sharpens the contract with a four-part identifier key (scheme, authority or jurisdiction, number, overlapping validity), six independently dated status planes, four separate branch tests, explicit field moves from WM-ORG-001/011 into WM-ORG-010, and a ban on dual writes of subject status. These refinements preserve the PROFILE decision and make the migration boundary testable.

Both providers keep publication held because every base is noncanonical, WM-ORG-010 requires a breaking re-subjecting migration and status crosswalk, WM-ORG-011 lacks independent review, source pins remain unresolved, and no executable fixtures exist.


## RECONCILED CANDIDATE
```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-ORG-02",
  "name": "Enterprise Legal Identity, Registration and Presence",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ORG-001",
    "WM-ORG-010",
    "WM-ORG-011"
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-pre-audit-publication-held",
  "publishableCanonical": false,
  "fixturesExecuted": false,
  "basePins": [
    {
      "modelId": "WM-ORG-001",
      "registryId": "vr.wm-org-001",
      "modelVersion": "0.3.0-research.1",
      "sourceFile": "publications/wm-org-001-organization/spec.yaml",
      "sourceBytes": 301830,
      "sourceSha256": "ce27fcf5453fb390d7aea631ab91748404ca25968a8b3af67311bf4c65a76cf1",
      "synthesisSha256": "028d2a633bcd0786942ca19af92a232a01b997a6ee26cf5484617922452043ac",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "providerMode": "dual-provider",
      "registryStatus": "described-previous-version",
      "registryReviewState": "migration-boundary-review",
      "invalidationRule": "Any source, synthesis or reservation drift invalidates this candidate and its derived materializations."
    },
    {
      "modelId": "WM-ORG-010",
      "registryId": "vr.wm-org-010",
      "modelVersion": "0.3.0-research.1",
      "sourceFile": "publications/wm-org-010-legal-entity-registration/spec.yaml",
      "sourceBytes": 279735,
      "sourceSha256": "4bae598815feb67b552c9f3463f45f4368da077609b7451743a470d1a9dab615",
      "synthesisSha256": "8e6a9b3302f0ca4f0b1c3f826bd5bd38361ed8f4b026cb02859f58d5dac99589",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "providerMode": "dual-provider",
      "registryStatus": "candidate",
      "registryReviewState": "boundary-review-required",
      "invalidationRule": "Any source, synthesis or reservation drift invalidates this candidate and its derived materializations."
    },
    {
      "modelId": "WM-ORG-011",
      "registryId": "vr.wm-org-011",
      "modelVersion": "0.3.0-research.1",
      "sourceFile": "publications/wm-org-011-business-establishment-branch/spec.yaml",
      "sourceBytes": 98436,
      "sourceSha256": "3f9170a43804efa776b942b76d7c6ac5b836f23c7bf5f7de0f5285a48088fa2f",
      "synthesisSha256": "d27bb1dfc0581d8c597b3cc463476d07ab2431732e54776f02338edb4ba3f1d4",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "providerMode": "single-provider-waiver",
      "registryStatus": "candidate",
      "registryReviewState": "boundary-review-required",
      "invalidationRule": "Any source, synthesis or reservation drift invalidates this candidate and its derived materializations."
    }
  ],
  "constraints": [
    "WM-ORG-001 is the sole master of organization or legal-subject identity, canonical identifiers, legal personality, continuity, subject status and succession.",
    "WM-ORG-010 masters registration records; each record references exactly one WM-ORG-001 subject after an explicit evidence-backed resolution and cannot create, merge, split or reassign a subject during ingestion.",
    "WM-ORG-011 masters operating-presence facts and references its operator subject and registration evidence; it never asserts legal personality or mints a subject.",
    "Identifier equality requires the same scheme, authority or jurisdiction, assigned number and overlapping validity; equal strings across schemes or authorities are never identity evidence.",
    "Cross-scheme equivalence is an explicit, dated, evidenced assertion and cannot be inferred by import, name, address, premises, extract or number similarity.",
    "Subject status, registration-record status, LEI status, tax or VAT status, national register-number status and evidence-extract currency are six independent dated planes.",
    "Registration, legal personality, premises and head-office attribution are four separate tests; no one test implies another.",
    "A registered branch without separate personality may be a WM-ORG-001 subject with legalPersonality=false, an explicit head-office relation, WM-ORG-010 records and WM-ORG-011 presences; the head office remains obligor unless authority says otherwise.",
    "A registration record and an operating presence are not one-to-one and neither is a substitute for the subject.",
    "Effective time, authority-recorded time and observed time are separate on every assertion; evidence extracts are dated observations, not current state.",
    "Name change, seat transfer, restoration or form conversion preserves identity only under an explicit continuity decision; mergers, divisions and discontinuous redomiciliations append predecessor and successor edges.",
    "Succession never rewrites historical contract-party identifiers, registration records, evidence or predecessor identity; retired identities remain resolvable as-of time.",
    "WM-ORG-001 and WM-ORG-010 cannot both author subject status or personality; registration-derived subject claims require evidence and an authorized update to WM-ORG-001.",
    "WM-ORG-010 registration authority, number, record status, evidence and scheme identifiers replace duplicate registration fields in WM-ORG-001; migration preserves provenance and source values.",
    "WM-ORG-011 removes personality and branch-number-as-subject fields; it retains presence kind, operatorRef, site, activity and a read-only evidenceRef to WM-ORG-010.",
    "No standard, legal-effect, approved-relation, canonical, installable or conformance claim is made from alignment evidence.",
    "Publication is refused while fixturesExecuted is false, any base is noncanonical, inherited holds remain, WM-ORG-010 re-subjecting and field/status crosswalks are unapproved, or WM-ORG-011 independent review is absent."
  ],
  "mastership": {
    "subjectIdentity": "WM-ORG-001",
    "registrationRecord": "WM-ORG-010",
    "operatingPresence": "WM-ORG-011",
    "forbiddenDualWrites": [
      "subject status",
      "legal personality",
      "canonical subject identity",
      "succession"
    ],
    "registrationResolution": "explicit evidenced reversible decision; never import side effect"
  },
  "identifierContract": {
    "equalityTuple": [
      "scheme",
      "authorityOrJurisdiction",
      "number",
      "overlappingValidity"
    ],
    "crossSchemeEquivalence": "explicit evidenced dated assertion",
    "forbiddenSoleKeys": [
      "unqualified number",
      "name",
      "address",
      "site",
      "extract"
    ]
  },
  "statusPlanes": [
    "subject status",
    "registration-record status",
    "LEI status",
    "tax/VAT status",
    "national register-number status",
    "evidence-extract currency"
  ],
  "branchContract": {
    "tests": [
      "registration",
      "legal personality",
      "premises or operating presence",
      "head-office attribution"
    ],
    "nonPersonBranch": "WM-ORG-001 subject with legalPersonality=false, explicit head-office relation, zero or more WM-ORG-010 records and zero or more WM-ORG-011 presences",
    "obligorRule": "head office remains obligor unless separate authority is evidenced"
  },
  "temporalContract": {
    "assertionTimes": [
      "effective",
      "authority-recorded",
      "observed"
    ],
    "history": "append-only supersession",
    "asOf": "replay from assertion history"
  },
  "successionContract": {
    "edges": "append-only predecessor/successor",
    "historicalParties": "never rewritten",
    "retiredIdentities": "resolvable"
  },
  "migrationPlan": [
    {
      "from": "WM-ORG-001",
      "to": "WM-ORG-010",
      "fields": [
        "register authority and number",
        "registration-record status",
        "extract evidence",
        "alternate scheme numbers"
      ]
    },
    {
      "from": "WM-ORG-010",
      "to": "WM-ORG-001",
      "fields": [
        "subject identity reference only"
      ],
      "rule": "subjectRef mandatory; personality/form/status claims require evidence and authorized WM-ORG-001 update"
    },
    {
      "from": "WM-ORG-011",
      "to": "removed",
      "fields": [
        "personality",
        "branch number as subject identity"
      ]
    },
    {
      "from": "WM-ORG-011",
      "to": "retained",
      "fields": [
        "presence kind",
        "operatorRef",
        "site",
        "activity",
        "evidenceRef to WM-ORG-010"
      ]
    }
  ],
  "executionRequirements": {
    "carrier": "none selected; declarative semantics only",
    "requiredBeforeExecution": [
      "approved carrier",
      "validator",
      "fixture runner",
      "digest-verified results"
    ],
    "fixtureDigestRequired": true,
    "publicationBehavior": "refuse while fixturesExecuted=false"
  },
  "inheritedBaseHolds": [
    {
      "base": "WM-ORG-001",
      "hold": "Source and live-version verification is incomplete and must be run before publication: every accepted source URL must be re-fetched and its version pin confirmed. The two providers cite different GLEIF URL paths for the same two documents (LEI-CDF 3.1 under /common-data-file-format/current-versions/ versus /common-data-file-format/, and the ELF list under /code-lists/ versus the bare path), so at least one variant in each pair is stale or a redirect and the canonical form must be established."
    },
    {
      "base": "WM-ORG-001",
      "hold": "Multi-profile domain validation has not been performed. The structure must be exercised against at least six distinct profiles before publication: a registered company with an LEI, an unregistered informal collective with no scheme identifier, an international branch holding its own LEI without separate legal personality, a fund with an umbrella and management relationship, a resident government entity formed by statute, and a sole proprietor whose legal person is a natural person. Coverage claims are provisional until each profile is walked end to end."
    },
    {
      "base": "WM-ORG-001",
      "hold": "The EUID and BRIS provisions carried by Commission Implementing Regulation (EU) 2021/1042 were surfaced from indexed EUR-Lex text rather than a full-text read, by the base provider's own admission. The EUID-specific data element must be treated as provisional and verified against the Official Journal before any normative reliance."
    },
    {
      "base": "WM-ORG-001",
      "hold": "FATF Recommendations 24 and 25 were unreachable (HTTP 403), so the beneficial-ownership structure rests on BODS at authority tier 2 rather than on the intergovernmental requirement it implements. The ownership layer must be re-grounded before it is published as an authority-backed structure."
    },
    {
      "base": "WM-ORG-001",
      "hold": "The base naming finding asks which single name form is the legal name, which is wrong for multilingual jurisdictions where RegOrg and SEMIC CBV make legalName a repeatable language-tagged literal with several co-equal legal names. The naming layer must be reframed to admit multiple co-equal legal names, with the RegOrg prohibition on storing translations in alternative-name fields, before that layer is published as normative."
    },
    {
      "base": "WM-ORG-001",
      "hold": "ISO 17442-1:2020 and ISO 20275 were cited from standards-catalogue landing pages, not normative text. Any statement in the synthesized model that reads as a conformance or eligibility rule derived from those standards must be marked alignment-only until the normative text is obtained."
    },
    {
      "base": "WM-ORG-001",
      "hold": "ISO 5009 is carried by the base as a tier-1 primary source for official organizational roles while the other provider records it as discovered but not fetched. The official-roles finding's specific claims (role counts, jurisdiction coverage, tie to ELF, exclusion of internal functional titles) must be confirmed against the fetched code list before publication."
    },
    {
      "base": "WM-ORG-010",
      "hold": "Source retrieval is not verified. Claude's own adversarial checks record that EUR-Lex full texts, the FATF guidance page, the ISO catalogue and the UNECE publication all refused automated retrieval, so those citations rest on titles and published summaries rather than confirmed full text. Every accepted source must be re-fetched and its contribution re-confirmed before publication."
    },
    {
      "base": "WM-ORG-010",
      "hold": "SRC-019 (GDPRhub, authority tier 3, non-primary) carries the load-bearing claim that no general right to erasure exists against a companies register. Replace it with the primary CJEU judgment in C-398/15 (Manni) or downgrade every finding that depends on it, including personal-data-in-registration-records and record-history-retention-and-deletion-constraints."
    },
    {
      "base": "WM-ORG-010",
      "hold": "Version pins must be reconciled and re-verified as-of a single date: ELF list v1.6 (Feb 2026), GLEIF RA list v1.8.1 (Nov 2024), LEI-CDF 3.1, Peppol ICD (May 2026), schema.org 30.0, and the FATF Recommendations edition (Claude cites March 2023 guidance, Grok cites an update dated June 2026)."
    },
    {
      "base": "WM-ORG-010",
      "hold": "The two providers cite different EU implementing regulations for the system of interconnection of registers — Commission Implementing Regulation (EU) 2021/1042 (Claude) and (EU) 2020/2244 (Grok). Determine which is in force, whether one repeals the other, and pin the surviving instrument before publishing any interconnection or exchange-protocol structure."
    },
    {
      "base": "WM-ORG-010",
      "hold": "Claude cites Directive (EU) 2025/25 as in force from 30 January 2025 via a Commission overview page rather than the Official Journal text. Confirm against EUR-Lex before any disclosure or interconnection claim relies on it."
    },
    {
      "base": "WM-ORG-010",
      "hold": "Domain-profile validation is incomplete. The model has been reasoned against EU, UK and global identifier-system profiles only. Before publication it must be exercised against at least: US state-level formation with no national register, a non-EU civil-law register (for example Japan or Brazil), a national identifier scheme outside the RA-list framing (China USCC, India CIN), and a jurisdiction where a legal form arises without registration, which is the case the fallback identity path exists to serve."
    },
    {
      "base": "WM-ORG-010",
      "hold": "Legal-effect characterisations — constitutive versus declaratory registration, opposability of disclosed particulars to third parties, register liability or warranty for inaccurate entries, and third-party reliance on translated versions — are stated as general rules but grounded partly in secondary summaries. Hold until each is confirmed against primary statutory text for at least two contrasting jurisdictions."
    },
    {
      "base": "WM-ORG-011",
      "hold": "No independent external research or reviewer: Claude and Grok each timed out once. Codex-only research and self-review remain reviewable-draft, never canonical."
    },
    {
      "base": "WM-ORG-011",
      "hold": "Source-defined establishment, branch and outlet kinds are not synonyms; profile review and any future model split require governed migration."
    },
    {
      "base": "WM-ORG-011",
      "hold": "GS1 overview evidence is indexed text with direct HTTP 403. Allocation rules and mutable source release pins are not fully inspected."
    },
    {
      "base": "WM-ORG-011",
      "hold": "GLEIF 2.8.5 selected clauses are historical reference evidence; replacement releases and full applicability remain unverified."
    },
    {
      "base": "WM-ORG-011",
      "hold": "No complete statutory inventory, executable nested instance schema, registry resolver, legal-standing verifier or real multi-registry fixture is delivered."
    },
    {
      "base": "WM-ORG-011",
      "hold": "Actual local delegation, service availability, premises accessibility, confidentiality and retention must be established by adopters."
    },
    {
      "base": "WM-ORG-011",
      "hold": "Independent external review was explicitly waived by the repository owner; this codex-only result remains a reviewable draft."
    }
  ],
  "publicationGate": {
    "publishableCanonical": false,
    "fixturesExecuted": false,
    "statusCeiling": "reviewable research checkpoint",
    "openHolds": [
      "all bases publishableCanonical=false",
      "WM-ORG-010 re-subjecting and field/status crosswalk unapproved",
      "WM-ORG-010 source pins and legal-effect claims unresolved",
      "WM-ORG-011 independent review absent",
      "no executable carrier or executed fixture evidence"
    ],
    "rule": "Any open hold, pin drift, missing digest or unexecuted fixture refuses publication."
  }
}
```

## DECLARATIVE FIXTURES
```json
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Legal Identity, Registration and Presence",
  "candidateRevision": 2,
  "declarativeOnly": true,
  "fixturesExecuted": false,
  "executionRequirements": {
    "carrier": "none selected; declarative semantics only",
    "requiredBeforeExecution": [
      "approved carrier",
      "validator",
      "fixture runner",
      "digest-verified results"
    ],
    "fixtureDigestRequired": true,
    "publicationBehavior": "refuse while fixturesExecuted=false"
  },
  "cases": [
    {
      "id": "ORG02-SECOND-EXTRACT",
      "title": "Second extract for a possible subject",
      "mode": "accept",
      "expectation": "create an unlinked registration record; never mint or merge a subject",
      "sha256": "412ba026a25a47616f86a1fe9525fd59a94fcff331002ccb3cec87a061cb5981"
    },
    {
      "id": "ORG02-EQUAL-NUMBER-CROSS-SCHEME",
      "title": "Equal number strings across schemes",
      "mode": "reject",
      "expectation": "reject identity equality",
      "sha256": "0cf30160a725f79ad9b2af78d9cc9407d870a52e27f701e0616d91c4fd9d17f8"
    },
    {
      "id": "ORG02-EQUAL-NUMBER-CROSS-AUTHORITY",
      "title": "Equal scheme and number under different authorities",
      "mode": "reject",
      "expectation": "reject identity equality",
      "sha256": "1b63bffbca3ea7b22a87fea3e5f17832657d5a2dc34ff579bd87a97e54b5ef35"
    },
    {
      "id": "ORG02-NONOVERLAP",
      "title": "Same qualified identifier in non-overlapping validity",
      "mode": "reject",
      "expectation": "retain separate dated assertions without automatic merge",
      "sha256": "0590bc0135494ece0956f488209a373ee97119807688c6f61b1ec2060c8044be"
    },
    {
      "id": "ORG02-THREE-RECORDS",
      "title": "One subject with home register, LEI and VAT records",
      "mode": "accept",
      "expectation": "accept three independently statused records",
      "sha256": "c4df2333b53e04b9cee73e515cc4b9619e52a928e94913a12f2368e2f65c10bb"
    },
    {
      "id": "ORG02-STATUS-LEAK",
      "title": "Registration status overwrites subject status",
      "mode": "reject",
      "expectation": "reject dual write",
      "sha256": "dcb3202157f881b096301a7c4d492476f6eb7fa2580f8092ee07563c0b51570d"
    },
    {
      "id": "ORG02-EXTRACT-CURRENT",
      "title": "Old extract treated as current subject state",
      "mode": "reject",
      "expectation": "reject observation-to-state inference",
      "sha256": "1b446b69388fd7450e2e1e2fb5668e403c25ccd03e1326674528819954cf142b"
    },
    {
      "id": "ORG02-PRESENCE-PERSONALITY",
      "title": "Premises imply legal personality",
      "mode": "reject",
      "expectation": "reject",
      "sha256": "e0ab10d7d9366cde07b0e822fca541a5110a51f8f1c351685c6528a09e349061"
    },
    {
      "id": "ORG02-NONPERSON-BRANCH",
      "title": "Registered branch without personality",
      "mode": "accept",
      "expectation": "accept subject, head-office link, registration and presence as separate records",
      "sha256": "f39be96c674abcfc618facbefb44123a58c37f10b02df783082c7e97fd10d14f"
    },
    {
      "id": "ORG02-BRANCH-OBLIGOR",
      "title": "Non-person branch becomes obligor without authority",
      "mode": "reject",
      "expectation": "reject",
      "sha256": "d27fd0ef62aaf17120e5c628ba0ec09bb3fb5f3ff99ff73f03aef8e2ca7fe654"
    },
    {
      "id": "ORG02-REGISTRATION-PRESENCE-ONE-TO-ONE",
      "title": "Registration forced one-to-one with presence",
      "mode": "reject",
      "expectation": "reject",
      "sha256": "1b349407faec42dcbfbea3f513419a4548c897eaaf87472b0bbb4da0a500076b"
    },
    {
      "id": "ORG02-MERGER-HISTORY",
      "title": "Merger with historical contracts",
      "mode": "accept",
      "expectation": "append succession edges and preserve predecessor party identifiers",
      "sha256": "f98c08278260ef260908195b4b6315725361662d6435f2ef3f1c94956ef940c2"
    },
    {
      "id": "ORG02-CONVERSION-CONTINUITY",
      "title": "Form conversion claims continuity",
      "mode": "accept",
      "expectation": "accept only with explicit authority-backed continuity decision",
      "sha256": "ace213f2dadebd177a74acb488f4f4085398af96ab8226533a2e0e0e2eefa2d1"
    },
    {
      "id": "ORG02-IMPORT-MINT",
      "title": "Registry import creates a subject",
      "mode": "reject",
      "expectation": "reject",
      "sha256": "21d262f5b87e0b41bc9a85906ac1f1621ae4e23a95867275245e04e05575346a"
    },
    {
      "id": "ORG02-CROSS-SCHEME-EQUIVALENCE",
      "title": "LEI and national number linked",
      "mode": "accept",
      "expectation": "accept only with explicit dated evidence",
      "sha256": "48eddb9e1c26af0101314e945b0e5787e8ddd65e1fe66013c0ea22031b7a26c5"
    },
    {
      "id": "ORG02-WM011-PERSONALITY",
      "title": "Presence record authors personality",
      "mode": "reject",
      "expectation": "reject",
      "sha256": "29408fc27952dd43166547449493fd951f461b5e62d52bfb23e5e28915b6fb4f"
    },
    {
      "id": "ORG02-BASE-PIN-DRIFT",
      "title": "Any pinned base digest changes",
      "mode": "reject",
      "expectation": "invalidate candidate and derived views",
      "sha256": "307d1ad2db098aa509d184806e48030f5a4615b5a638587e3d4d15c93ef095dd"
    },
    {
      "id": "ORG02-PUBLICATION-GATE",
      "title": "fixturesExecuted=false",
      "mode": "reject",
      "expectation": "refuse publication",
      "sha256": "140fc491dc86e22b3c8b89dfacfc8bc63294c95e3cdbd37711a237e969704db3"
    }
  ]
}
```
