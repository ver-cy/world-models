# Frozen semantic audit: EM-ORG-04 Organizational Unit and Mandate

You are the single independent frozen auditor. Use only the material below and no tools. Audit the reconciled profile. Do not invent identifiers or external facts.

Required output:
1. Verdict ACCEPT or REVISE.
2. Confirm or reject PROFILE over WM-ORG-002 with no new identifier.
3. List every defect that could cause identity drift, parent dual-write, invalid graph cardinality/cycles, scenario leakage, team/unit collapse, mandate-placement coupling, employer inference, history rewrite or unsupported release claims.
4. Give exact remediation and fixture expectation for every defect.
5. Identify contradictions among dossier, providers, candidate and fixtures.
6. End with a closed numbered remediation checklist.

## FROZEN DOSSIER
```json
{
  "contour": {
    "id": "EM-ORG-04",
    "name": "Организационная единица и мандат",
    "domain": "ORG",
    "kind": "subject",
    "wave": "W1",
    "scope": "Подразделение как устойчивая единица ответственности. Оргсхема является отдельным ландшафтом; команда может быть самостоятельным коллективом.",
    "candidate_types": [
      "OrganizationalUnit",
      "UnitMandate",
      "UnitType",
      "StructuralPlacement"
    ],
    "specific_questions": [
      "Что делает подразделение самостоятельным объектом?",
      "Как развести административную, функциональную и юридическую принадлежность?",
      "Как согласовать OUMM и текущую WM-ORG-002 без двух владельцев unit?"
    ],
    "proposed_invariants": [
      "Родитель ограничен осью, сценарием и периодом",
      "Переименование сохраняет ID",
      "Управленческая принадлежность не определяет работодателя"
    ],
    "negative_case": "Продуктовая команда из разных департаментов принудительно получает одного административного родителя.",
    "acceptance_scenario": "Перестройка структуры as-is/to-be сохраняет старые назначения и не порождает цикл в выбранной административной оси.",
    "comparison_tracks": [
      "W3C ORG: коллективы, роли, членство и позиции",
      "GLEIF: зарегистрированная идентичность и консолидационные связи",
      "Сопоставление корпоративного управления, фактической оргструктуры и HR/ERP-представления"
    ],
    "vercy_candidates": [
      {
        "model_id": "WM-ORG-002",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "ORG-05",
        "fields": [
          {
            "name": "unit_code",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "mandate",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "unit_kind",
            "value_type": "code",
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
      "EM-ORG-01",
      "EM-ORG-06",
      "EM-PEO-02"
    ],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "queue_reservation": {
    "sequence": 31,
    "id": "EM-ORG-04",
    "status": "queued",
    "claude_status": "not-started",
    "grok_status": "not-started",
    "boundary_decision": "pending",
    "publication_urls": [],
    "remaining_scope": "Entire research brief pending",
    "target_model_ids": [
      "WM-ORG-002"
    ]
  },
  "registry_reservation": {
    "registry_id": "vr.wm-org-002",
    "record_plane": "world-model",
    "model_id": "WM-ORG-002",
    "name": "Organizational Unit",
    "alternate_names": "",
    "entry_kind": "standalone-mm",
    "origin": "grok-union-current",
    "status": "described-previous-version",
    "review_state": "migration-boundary-review",
    "nav_path": "NAV.SOC.ORG.UNT",
    "domain_tags": "SOC.ORG.UNT",
    "legacy_alias": "O2",
    "existing_spec_ref": "models/organizations/O2-organizational-unit.md",
    "parent_ids": "",
    "contains_ids": "WM-ORG-004",
    "aligned_model_ids": "",
    "purpose": "Internal structure of organizations",
    "owner_or_maintainer": "parent organization",
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
      "source_model_id": "WM-ORG-002",
      "relation_type": "CONTAINS",
      "target_model_id": "WM-ORG-004",
      "instance_semantics": "Unit instance contains or governs positions",
      "rationale": "Structural matryoshka",
      "review_state": "candidate"
    }
  ],
  "current_spec": {
    "source_file": "publications/wm-org-002-organizational-unit/spec.yaml",
    "source_bytes": 250855,
    "source_sha256": "9e3e80da4db6db6589991102b91af4af1a00080cd348848250b63f70a97b2330",
    "publication": {
      "status": "published",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "generatedAt": "2026-08-23T23:43:44Z",
      "synthesisSha256": "a991fb7774ae1b611787fe093e9d9e380499bf42c9fbe69fcb91af147be90812",
      "providerMode": "dual-provider",
      "providers": [
        "Claude",
        "Grok"
      ],
      "waivedProviders": []
    },
    "metaModel": {
      "id": "WM-ORG-002",
      "registryId": "vr.wm-org-002",
      "name": "Organizational Unit",
      "version": "0.3.0-research.1",
      "previousVersions": [],
      "entryKind": "entity",
      "family": "World Models",
      "category": "Society, people and institutions",
      "industry": [
        "Cross-industry"
      ],
      "domain": [
        "SOC.ORG.UNT"
      ],
      "tags": [
        "organizational",
        "unit",
        "soc.org.unt"
      ],
      "status": "published"
    },
    "model": {
      "registry_id": "vr.wm-org-002",
      "model_id": "WM-ORG-002",
      "name": "Organizational Unit",
      "entry_kind": "entity",
      "purpose": "Provide the format-neutral context an agent needs to understand, create, inspect and operate the internal structure of an organization: which units exist, how they nest and report, what each is mandated to do, what establishment and staffing they carry, and how that structure is changed, dated, evidenced and disclosed over time.",
      "scope_statement": "This model covers an organizational unit as a subdivision that, in the words of the W3C Organization Ontology, 'only has full recognition within the context of that Organization'. It governs unit identity, classification, containment and reporting relationships, delegated mandate and decision rights, authorized establishment and measured staffing, structural change acts and their temporal validity, plus the provenance, retention, disclosure and interoperability rules that make the structure record operable. It deliberately stops at the boundaries of legal organizational identity, of the post/position as an object in its own right, of employment relationships, of physical sites, and of statistical or financial reporting units that are derived from - but not identical to - internal structure.",
      "in_scope": [
        "Unit identity, naming, aliases and parent-scoped or ISO/IEC 6523 organization-part identification",
        "Unit kind classification against governed code lists and unit existence status",
        "Containment hierarchies, including multiple concurrent hierarchies (managerial, legal, cost, functional)",
        "Reporting and coordination lines, including non-containment and dotted-line relationships",
        "Delegated mandate, decision rights, authority limits and segregation-of-duties constraints attached to a unit",
        "Authorized establishment (post complement) seated in a unit and its occupancy state at unit granularity",
        "Dated headcount and full-time-equivalent measurement of a unit, with basis and aggregation thresholds",
        "Reorganization acts (create, rename, reparent, merge, split, transfer, disband) and unit lineage",
        "Effective dating, bitemporality and as-of reconstruction of the structure graph",
        "Record authority, approval evidence, retention/disposition and disclosure control for structure data",
        "Crosswalks to W3C ORG, CPOV, FHIR, LDAP, SCIM, schema.org and ISO/IEC 6523 projections"
      ],
      "out_of_scope": [
        "Legal personality, incorporation, registration, LEI and regulatory identity of the whole organization (WM-ORG-001)",
        "The post/position as an object with its own title, grade, job description and occupational classification (WM-ORG-004)",
        "Employment contracts, appointments, persons and their occupancy of posts",
        "Constitutive charter powers of the organization as a legal entity (charter model)",
        "Physical premises, addresses, geometry and site operations (site/location model)",
        "Statistical units such as enterprise, local unit and kind-of-activity unit used for economic observation",
        "Financial segment reporting, general ledger and cost accounting mechanics",
        "Stewardship policy machinery and access-grant issuance (S1/S2 service models)",
        "Business capability, process and value-stream modelling",
        "Identity-provider group membership and directory synchronisation state as a system of record"
      ],
      "boundary_notes": [
        {
          "neighbor": "WM-ORG-001 Organization",
          "distinction": "W3C ORG separates org:FormalOrganization (recognized in a legal jurisdiction, with rights and responsibilities) from org:OrganizationalUnit, which has full recognition only inside its parent. Legal identity, registration and LEI stay in WM-ORG-001. A branch that is separately registered is dual-classified: it is a unit here and a legal entity there, and GLEIF only issues an LEI to the legally registered entity, not to an internal division.",
          "source_refs": [
            "SRC-001",
            "SRC-013"
          ]
        },
        {
          "neighbor": "WM-ORG-004 Position",
          "distinction": "org:Post represents a position that exists independently of who fills it. This model records only the unit-side facts: how many posts are established in the unit, which posts are seated there, and the aggregate occupancy state. Post title, grade, competency profile and occupational classification belong to WM-ORG-004, which this model CONTAINS by reference rather than by copy.",
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "neighbor": "Site / Location model",
          "distinction": "FHIR states that Location records where a service occurs while Organization records who performed it; Eurostat's 'local unit' is 'an enterprise or part thereof ... situated in a geographically identified place'. A unit may be associated with one or more sites, but premises, addresses and geometry are not unit attributes and are not modelled here.",
          "source_refs": [
            "SRC-002",
            "SRC-010"
          ]
        },
        {
          "neighbor": "Statistical units model",
          "distinction": "Council Regulation (EEC) No 696/93 defines enterprise, kind-of-activity unit and local unit as observation units for economic statistics. These are derived by statistical rules from operational reality, not asserted by the organization, and their boundaries routinely differ from internal units. Treated as an ALIGN target, never as a source of internal unit identity.",
          "source_refs": [
            "SRC-010"
          ]
        },
        {
          "neighbor": "Financial segment reporting",
          "distinction": "IFRS 8 identifies operating segments through a management approach based on how the chief operating decision maker reviews internal reports, and permits aggregation of segments with similar economic characteristics. A reportable segment is therefore a derived view over internal units, not a unit; this model supplies the inputs and the change signal, not the segment determination.",
          "source_refs": [
            "SRC-009"
          ]
        },
        {
          "neighbor": "Directory and identity systems",
          "distinction": "RFC 4519 defines 'ou' as a multi-valued name attribute and RFC 7643 defines SCIM 'department', 'division' and 'organization' as free-text names. These carry no identifier, no validity period and no hierarchy semantics, so directory content is a lossy projection of this model and never its system of record.",
          "source_refs": [
            "SRC-004",
            "SRC-005"
          ]
        },
        {
          "neighbor": "Global organization registries",
          "distinction": "ROR states it 'is not focused on capturing all subdivisions of a given organization such as a university's schools or departments' because departments 'often emerge, close, combine, and change'. No general governed global identifier exists for internal units, so unit identity is parent-scoped by default.",
          "source_refs": [
            "SRC-011",
            "SRC-012"
          ]
        }
      ]
    },
    "structure_index": [
      {
        "id": "unit-identity-and-classification",
        "name": "Unit Identity and Classification",
        "description": "What a unit is, how it is unambiguously referenced, what it is called, what kind of thing it is, and whether it currently exists.",
        "layers": [
          {
            "id": "unit-identification",
            "name": "Unit Identification",
            "description": "Identifier assignment, external addressability and naming of a unit."
          },
          {
            "id": "unit-classification",
            "name": "Unit Classification and Existence",
            "description": "The kind of unit and whether it currently exists as an operating subdivision."
          }
        ]
      },
      {
        "id": "structural-composition",
        "name": "Structural Composition",
        "description": "How units nest into hierarchies and how they report to and coordinate with one another.",
        "layers": [
          {
            "id": "containment-hierarchy",
            "name": "Containment Hierarchy",
            "description": "Parent-child membership of units within the organization, including concurrent hierarchies."
          },
          {
            "id": "reporting-and-coordination",
            "name": "Reporting and Coordination",
            "description": "Directed reporting relations and non-containment relationships between units."
          }
        ]
      },
      {
        "id": "mandate-and-authority",
        "name": "Mandate and Authority",
        "description": "What a unit is empowered to do, within which limits, and who is accountable for it.",
        "layers": [
          {
            "id": "remit-and-decision-rights",
            "name": "Remit and Decision Rights",
            "description": "The scope of a unit's mandate and the decisions it may take."
          },
          {
            "id": "accountability-and-controls",
            "name": "Accountability and Controls",
            "description": "Who answers for a unit and which control constraints its structure must satisfy."
          }
        ]
      },
      {
        "id": "establishment-and-staffing",
        "name": "Establishment and Staffing",
        "description": "The posts a unit is authorized to carry and the staffing actually measured in it.",
        "layers": [
          {
            "id": "establishment-plan",
            "name": "Establishment Plan",
            "description": "The authorized complement of posts seated in a unit."
          },
          {
            "id": "staffing-measurement",
            "name": "Staffing Measurement",
            "description": "Dated, method-declared measurement of staffing attributed to a unit, and the rules for disclosing it."
          }
        ]
      },
      {
        "id": "change-and-time",
        "name": "Change and Time",
        "description": "How structure changes, what evidences the change, and how any past state can be reconstructed.",
        "layers": [
          {
            "id": "structural-change-events",
            "name": "Structural Change Events",
            "description": "The acts that create, alter, combine, move or end units, and the lineage they produce."
          },
          {
            "id": "temporal-validity",
            "name": "Temporal Validity",
            "description": "Effective dating, bitemporality and reconstruction of the structure at any past instant."
          }
        ]
      },
      {
        "id": "governance-provenance-and-disclosure",
        "name": "Governance, Provenance and Disclosure",
        "description": "Who owns the structure record, what evidences it, how long it is kept, and who may see what.",
        "layers": [
          {
            "id": "provenance-and-authority",
            "name": "Provenance and Record Authority",
            "description": "Which system and which body are authoritative for each structural assertion, and what evidences it."
          },
          {
            "id": "access-and-retention",
            "name": "Access, Disclosure and Retention",
            "description": "Controlled release of structure information and its governed disposition."
          },
          {
            "id": "external-alignment",
            "name": "External Alignment",
            "description": "Mapping to external vocabularies and controlling fidelity loss on export."
          }
        ]
      }
    ],
    "selected_findings": [
      {
        "bundle": "unit-identity-and-classification",
        "layer": "unit-identification",
        "finding": {
          "id": "unit-identifier-scheme",
          "name": "Unit Identifier Scheme and Assignment",
          "description": "A unit's authoritative identifier is normally minted by the parent organization's master system, because no general governed global registry issues identifiers for internal subdivisions. ISO/IEC 6523 provides the only widely deployed external addressing slot, combining an International Code Designator, the parent organization identifier and an optional organization part identifier; schema.org exposes this as iso6523Code in XXXX:YYYYYY:ZZZ form. Identifier stability across rename, reparenting and merge must be decided explicitly.",
          "source_refs": [
            "SRC-001",
            "SRC-007",
            "SRC-008",
            "SRC-012",
            "SRC-013"
          ],
          "questions": [
            "Which system is the authoritative assigner of this unit's identifier, and is that system the parent organization's master record rather than a downstream HR or directory system?",
            "Can this unit be addressed externally as an ISO/IEC 6523 organization part under the parent organization's ICD and organization identifier, and if so which OPI value and source indicator apply?",
            "Does the identifier survive renaming, reparenting and merger of the unit, and is it guaranteed never to be reassigned to a different unit?",
            "If no master-system identifier exists, which UUID or ULID does the adopting Dimension mint, and where is that minting act recorded?"
          ],
          "data_elements": [
            {
              "id": "de-unit-id",
              "name": "unitIdentifier",
              "description": "The authoritative identifier for the unit within its assigning scheme.",
              "value_kind": "identifier",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-unit-id-scheme",
              "name": "unitIdentifierScheme",
              "description": "Coded reference to the scheme and assigning authority for the identifier.",
              "value_kind": "code",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-unit-opi",
              "name": "organizationPartIdentifier",
              "description": "ISO/IEC 6523 organization part identifier for external addressing of the unit, with its source indicator.",
              "value_kind": "identifier",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-unit-alt-ids",
              "name": "alternateIdentifiers",
              "description": "Non-authoritative identifiers held in downstream systems (ERP cost centre code, LDAP DN, IdP group id).",
              "value_kind": "collection",
              "cardinality": "0..n",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "unit-identity-and-classification",
        "layer": "unit-identification",
        "finding": {
          "id": "unit-naming-and-designation",
          "name": "Unit Naming and Designation",
          "description": "Units carry an official name, display and short names, abbreviations, language variants and superseded historical names. FHIR provides name plus alias for 'alternate or historical names' and requires at least one name or identifier; LDAP 'ou' is explicitly multi-valued. Names are unstable and non-unique and must never be used as identity.",
          "source_refs": [
            "SRC-002",
            "SRC-004",
            "SRC-003"
          ],
          "questions": [
            "Which name is the official designation of the unit, in which language, and which instrument fixed it?",
            "Which former names remain in use downstream and over which validity periods were they current?",
            "Is the unit name required to be unique within its parent, within the whole organization, or not at all?"
          ],
          "data_elements": [
            {
              "id": "de-unit-name",
              "name": "officialName",
              "description": "The official designation of the unit, with language tag.",
              "value_kind": "text",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-unit-alias",
              "name": "alias",
              "description": "Alternate, short, acronym or historical names with type and validity period.",
              "value_kind": "collection",
              "cardinality": "0..n",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "unit-identity-and-classification",
        "layer": "unit-classification",
        "finding": {
          "id": "unit-kind-classification",
          "name": "Unit Kind and Classification Scheme",
          "description": "Units are typed against a governed code list (department, division, directorate, branch, committee, board, team, programme office, shared-service centre, cost centre). W3C ORG provides org:classification against a scheme; CPOV constrains purpose to COFOG codes for public organisations and adds a classification property; FHIR uses a CodeableConcept type. The scheme must be named, versioned and resolvable, and the same unit may carry codes from several schemes simultaneously.",
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003"
          ],
          "questions": [
            "Against which named and versioned classification scheme is the unit's kind asserted, and is that scheme resolvable to a published code list?",
            "Does the unit carry codes from more than one scheme (internal kind, public-sector function, industry activity), and which one governs behaviour?",
            "Is this subdivision also a formal organization recognized in a legal jurisdiction, requiring dual classification and a link to WM-ORG-001?",
            "What evidence is required before a unit's kind may be reclassified, and does reclassification require a reorganization act?"
          ],
          "data_elements": [
            {
              "id": "de-unit-kind",
              "name": "unitKind",
              "description": "Coded kind of unit against a governed scheme.",
              "value_kind": "code",
              "cardinality": "1..n",
              "required": true
            },
            {
              "id": "de-classification-scheme",
              "name": "classificationScheme",
              "description": "Identifier and version of the scheme from which each code is drawn.",
              "value_kind": "reference",
              "cardinality": "1..n",
              "required": true
            },
            {
              "id": "de-dual-legal-flag",
              "name": "isAlsoFormalOrganization",
              "description": "Whether this subdivision is separately recognized as a legal entity.",
              "value_kind": "boolean",
              "cardinality": "1",
              "required": true
            }
          ]
        }
      },
      {
        "bundle": "unit-identity-and-classification",
        "layer": "unit-classification",
        "finding": {
          "id": "unit-existence-status",
          "name": "Unit Existence Status",
          "description": "Whether the unit is proposed, active, dormant, suspended, disbanded or created in error. FHIR carries a boolean 'active'; ROR distinguishes active, inactive and withdrawn, where withdrawn means the record was created in error and is not a real-world cessation. That three-way distinction - operating, ceased, erroneous - is required so that error correction is not confused with reorganization.",
          "source_refs": [
            "SRC-002",
            "SRC-011"
          ],
          "questions": [
            "Which status values are permitted for a unit, and is 'created in error' modelled separately from 'ceased to operate'?",
            "Which status transitions are legal, and which of them require a reorganization act rather than a simple correction?",
            "How is a unit that exists on paper but has no establishment and no activity represented, and how long may it stay in that state?",
            "After a unit is disbanded, is its record tombstoned with its relationships retained for historical reconstruction, or removed?"
          ],
          "data_elements": [
            {
              "id": "de-unit-status",
              "name": "unitStatus",
              "description": "Current lifecycle status of the unit from the governed status vocabulary.",
              "value_kind": "code",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-status-since",
              "name": "statusEffectiveFrom",
              "description": "The instant from which the current status applies.",
              "value_kind": "timestamp",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-withdrawal-reason",
              "name": "withdrawalReason",
              "description": "Reason a record was withdrawn as erroneous, distinct from real-world disbandment.",
              "value_kind": "text",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "unit-identity-and-classification",
        "layer": "unit-classification",
        "finding": {
          "id": "collaboration-vs-unit-typing",
          "name": "Kind and scheme",
          "description": "ORG supplies org:classification with range SKOS Concept and also allows subclassing when the kind is intrinsic. CPOV uses classification codes and points to the EU Organization Types named authority list for European institutions, while other levels must use other schemes. FHIR Organization.type is an example binding. Popolo forces a single classification per organization and requires implementations to choose one scheme. There is no universal unit-kind code list; department, branch, team, committee and similar labels are local. A committee may instead be an OrganizationalCollaboration if it is not an internal subdivision.",
          "source_refs": [
            "SRC-017",
            "SRC-003",
            "SRC-018",
            "SRC-019"
          ],
          "questions": [
            "What kind is this unit, in which classification scheme, and is that kind intrinsic or merely a directory grouping?",
            "Is this body an internal unit, a committee treated as a unit, or a cross-organization collaboration?",
            "May this unit carry more than one classification at once, and if a profile forbids that, which scheme is the unique classifier?"
          ],
          "data_elements": [
            {
              "id": "collaboration-vs-unit-typing-data01",
              "name": "Unit kind code",
              "description": "Department, branch, team or other local kind",
              "value_kind": "code",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "collaboration-vs-unit-typing-data02",
              "name": "Kind scheme",
              "description": "SKOS concept scheme or FHIR value set",
              "value_kind": "identifier",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "collaboration-vs-unit-typing-data03",
              "name": "Body mode",
              "description": "unit, committee-as-unit, collaboration",
              "value_kind": "code",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "structural-composition",
        "layer": "containment-hierarchy",
        "finding": {
          "id": "parent-child-containment",
          "name": "Parent-Child Containment",
          "description": "Every unit resolves to exactly one parent organization and, except at the top, to one parent unit within a given hierarchy. W3C ORG expresses this with org:unitOf/org:hasUnit and org:subOrganizationOf; FHIR uses partOf; schema.org uses parentOrganization, which supersedes branchOf and is not distinguished from subsidiary ownership. ROR maintains reciprocal parent and child edges on active records. Cycles, orphans and multi-parent assertions within one hierarchy are integrity failures.",
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-008",
            "SRC-011"
          ],
          "questions": [
            "Which organization (WM-ORG-001 instance) does this unit ultimately belong to, and is that link mandatory and immutable for the unit's lifetime?",
            "Which unit is the immediate parent within the named hierarchy, and what is the depth and root of that path?",
            "How are cycles, orphaned units and multiple parents within a single hierarchy detected and prevented at write time?",
            "Is the parent link a containment of a non-legal subdivision or an ownership relation to a separate legal entity, and how is that difference preserved when exporting to vocabularies that conflate them?"
          ],
          "data_elements": [
            {
              "id": "de-parent-org-ref",
              "name": "parentOrganizationRef",
              "description": "Reference to the WM-ORG-001 organization instance that owns the structure.",
              "value_kind": "reference",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-parent-unit-ref",
              "name": "parentUnitRef",
              "description": "Reference to the immediate parent unit within a named hierarchy.",
              "value_kind": "reference",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-hierarchy-path",
              "name": "hierarchyPath",
              "description": "Ordered path of unit identifiers from the hierarchy root to this unit, derived not asserted.",
              "value_kind": "collection",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "structural-composition",
        "layer": "containment-hierarchy",
        "finding": {
          "id": "concurrent-hierarchies",
          "name": "Concurrent Hierarchies and Matrix Structure",
          "description": "One organization commonly maintains several simultaneous hierarchies over the same units: managerial line, legal-entity roll-up, cost/budget roll-up, functional or professional line, and the internal reporting structure that IFRS 8 makes decisive for segment identification. Each hierarchy is a separately named, separately governed edge set; collapsing them into one tree destroys the information that downstream reporting depends on.",
          "source_refs": [
            "SRC-001",
            "SRC-009",
            "SRC-005"
          ],
          "questions": [
            "Which named hierarchies exist over the unit set, who owns each, and which one is the default for display?",
            "Where does a unit's position differ between hierarchies, and is that divergence intentional or an integrity defect?",
            "Which hierarchy corresponds to the internal reports reviewed by the chief operating decision maker for the purposes of segment identification?",
            "When two hierarchies imply conflicting authority over the same unit, which precedence rule resolves the conflict?"
          ],
          "data_elements": [
            {
              "id": "de-hierarchy-id",
              "name": "hierarchyIdentifier",
              "description": "Identifier and purpose of a named hierarchy over the unit set.",
              "value_kind": "identifier",
              "cardinality": "1..n",
              "required": true
            },
            {
              "id": "de-hierarchy-edge",
              "name": "hierarchyEdge",
              "description": "A parent-child edge qualified by hierarchy identifier and validity period.",
              "value_kind": "object",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-codm-flag",
              "name": "isCodmReportingHierarchy",
              "description": "Marks the hierarchy that reflects internal management reporting for segment purposes.",
              "value_kind": "boolean",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "structural-composition",
        "layer": "reporting-and-coordination",
        "finding": {
          "id": "reporting-lines",
          "name": "Reporting Lines and Their Standards Basis",
          "description": "Reporting lines are distinct from containment: a unit may sit under one parent but report functionally elsewhere (dotted line). W3C ORG's org:reportsTo is defined between Agents or Posts, not between organizational units, so unit-to-unit reporting is an extension of the standard and must be declared as such rather than claimed as conformant. SCIM offers only a single 'manager' reference at person level, which cannot carry line type or validity.",
          "source_refs": [
            "SRC-001",
            "SRC-005"
          ],
          "questions": [
            "What type is each reporting line - administrative, functional, professional, operational or advisory - and is it solid or dotted?",
            "Does the reporting line hold between units, between posts, or between the units' heads, and which representation is authoritative?",
            "Where unit-to-unit reporting is asserted, is the departure from org:reportsTo recorded as an explicit extension with a mapping rule?",
            "Over which period is each reporting line valid, and can two lines of the same type to different targets overlap in time?"
          ],
          "data_elements": [
            {
              "id": "de-reporting-line",
              "name": "reportingLine",
              "description": "Directed reporting relation with type, subject kind, target and validity period.",
              "value_kind": "object",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-line-type",
              "name": "reportingLineType",
              "description": "Coded type of the reporting relation.",
              "value_kind": "code",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-line-extension-note",
              "name": "standardExtensionNote",
              "description": "Declaration that unit-level reporting extends beyond the domain/range of org:reportsTo.",
              "value_kind": "text",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "structural-composition",
        "layer": "reporting-and-coordination",
        "finding": {
          "id": "cross-unit-affiliations",
          "name": "Cross-Unit and External Affiliations",
          "description": "Units participate in relations that are neither containment nor reporting: shared services, joint committees, secondments of capacity, service-level relations to other units, and affiliations to bodies in other legal entities. FHIR introduces OrganizationAffiliation precisely for 'complex non-hierarchical relationships between separate legal entities without implying ownership'; ROR uses a 'related' type for 'less defined connections, such as resource sharing or participation without direct control'.",
          "source_refs": [
            "SRC-002",
            "SRC-011"
          ],
          "questions": [
            "What kind of non-hierarchical relation is this - shared service, joint body, service agreement, secondment or partnership - and does it imply any control?",
            "Does the counterparty sit inside the same parent organization or in a different legal entity, and does that change which model owns the relation?",
            "Which instrument establishes the affiliation, over what period, and what obligations does it place on the unit?"
          ],
          "data_elements": [
            {
              "id": "de-affiliation",
              "name": "unitAffiliation",
              "description": "Non-hierarchical relation between a unit and another unit or external body, with type and validity.",
              "value_kind": "object",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-affiliation-instrument",
              "name": "affiliationInstrumentRef",
              "description": "Reference to the agreement or decision that establishes the affiliation.",
              "value_kind": "reference",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "mandate-and-authority",
        "layer": "remit-and-decision-rights",
        "finding": {
          "id": "unit-mandate-scope",
          "name": "Unit Mandate and Scope",
          "description": "A unit's mandate states its reason for existence and the subject matter, geography, customer set or process it covers. W3C ORG offers org:purpose; CPOV types purpose as a code and suggests COFOG for public organisations, and adds spatial coverage of the administrative region an organisation covers. Mandate must trace to a delegating instrument, because ISO 37000 requires delegation to be formalized.",
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-014"
          ],
          "questions": [
            "What is the unit's stated remit, and is it expressed as free text, as codes from a governed scheme, or both?",
            "Which instrument delegates this mandate to the unit, and from which higher authority or charter power does it derive?",
            "Over which spatial, market, legal-entity or process scope does the mandate apply, and where does it explicitly not apply?",
            "Does this mandate overlap or conflict with the remit of another unit, and which rule resolves the overlap?"
          ],
          "data_elements": [
            {
              "id": "de-mandate-text",
              "name": "remitStatement",
              "description": "Narrative statement of what the unit is mandated to do.",
              "value_kind": "text",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-purpose-code",
              "name": "purposeCode",
              "description": "Coded purpose of the unit from a governed scheme (e.g. COFOG for public bodies).",
              "value_kind": "code",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-mandate-validity",
              "name": "mandateValidity",
              "description": "Period over which the mandate is in force.",
              "value_kind": "object",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-mandate-scope",
              "name": "mandateScope",
              "description": "Structured coverage of the mandate across spatial, market, entity and process dimensions.",
              "value_kind": "object",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "mandate-and-authority",
        "layer": "remit-and-decision-rights",
        "finding": {
          "id": "delegated-authority-limits",
          "name": "Delegated Authority Limits",
          "description": "Delegation is bounded: spend thresholds, contract-signing powers, hiring authority, approval tiers and escalation triggers. ISO 37000 holds that those who delegate remain accountable for the delegate's use of that authority, that delegation should be formalized together with appropriate assurance processes, and that no one should be accountable for matters over which they have no authority. Limits are therefore first-class data, not narrative.",
          "source_refs": [
            "SRC-014"
          ],
          "questions": [
            "Which decision types may this unit take without escalation, and what quantitative or categorical limits bound each of them?",
            "May the unit sub-delegate any part of its authority to a contained unit or post, and under what conditions?",
            "Which assurance process verifies that delegated authority is being exercised within its limits, and at what cadence?",
            "Under what circumstances is delegated authority suspended or withdrawn, and does withdrawal take effect immediately or at a stated date?"
          ],
          "data_elements": [
            {
              "id": "de-authority-limit",
              "name": "authorityLimit",
              "description": "A bounded decision right with type, quantitative limit and escalation threshold.",
              "value_kind": "object",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-limit-amount",
              "name": "limitAmount",
              "description": "Monetary or numeric ceiling attached to a decision right, with unit of measure or currency.",
              "value_kind": "quantity",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-subdelegation-rule",
              "name": "subDelegationRule",
              "description": "Whether and how authority may be further delegated downward.",
              "value_kind": "text",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "mandate-and-authority",
        "layer": "accountability-and-controls",
        "finding": {
          "id": "accountable-role",
          "name": "Accountable Role for the Unit",
          "description": "Each unit has a head or accountable role. W3C ORG models this as a Post or as a Membership linking an Agent, an Organization and a Role, which keeps the accountability slot stable while occupants change. ISO 37000 requires that decision-makers have appropriate authority, competence and resources for the responsibilities given. The person occupying the role is out of scope; the slot and its linkage are in scope.",
          "source_refs": [
            "SRC-001",
            "SRC-014"
          ],
          "questions": [
            "Which post or role is designated as head of the unit, and is that designation a property of the unit or of the post?",
            "How is an acting, interim or vacant headship represented, and who holds the accountability while the slot is unfilled?",
            "What evidence exists that the accountable role has the authority, competence and resources matching the unit's responsibilities?"
          ],
          "data_elements": [
            {
              "id": "de-head-post-ref",
              "name": "headPostRef",
              "description": "Reference to the post (WM-ORG-004) designated as head of the unit.",
              "value_kind": "reference",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-headship-state",
              "name": "headshipState",
              "description": "Whether the headship is substantively filled, acting, or vacant.",
              "value_kind": "code",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "mandate-and-authority",
        "layer": "accountability-and-controls",
        "finding": {
          "id": "segregation-of-duties",
          "name": "Segregation of Duties and Structural Controls",
          "description": "Structure itself carries control obligations: certain functions must not report into the unit they oversee, incompatible mandates must not sit in one unit, and control functions may require an independent line to a governing body. ISO 37000 frames this through accountability that cannot be discharged without matching authority and through formalized delegation with assurance. Violations are structural defects detectable at graph level.",
          "source_refs": [
            "SRC-014",
            "SRC-001"
          ],
          "questions": [
            "Which pairs or sets of mandates must never be held by the same unit, and which rule set encodes that prohibition?",
            "Which units require an independent reporting line that bypasses their operational parent, and to which body does that line run?",
            "How are segregation violations detected when a reorganization is proposed, and does detection block the change or only warn?",
            "Under what conditions may a segregation rule be waived, who may approve the waiver, and for how long?"
          ],
          "data_elements": [
            {
              "id": "de-sod-rule-ref",
              "name": "segregationRuleRef",
              "description": "Reference to a structural control rule applying to the unit.",
              "value_kind": "reference",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-independence-flag",
              "name": "requiresIndependentLine",
              "description": "Whether the unit must report independently of its operational parent.",
              "value_kind": "boolean",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-sod-waiver",
              "name": "segregationWaiver",
              "description": "An approved, time-bounded exception to a structural control rule with its compensating control.",
              "value_kind": "object",
              "cardinality": "0..n",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "change-and-time",
        "layer": "structural-change-events",
        "finding": {
          "id": "reorganization-act",
          "name": "Reorganization Act",
          "description": "A reorganization act is a decision that reshapes structure. It carries at least three distinct times - when it was decided, when it takes effect in the world, and when it was recorded - plus the deciding authority, the affected units and the change kind. W3C ORG's ChangeEvent 'resulted in a major change to an organization such as a merger or complete restructuring'; IFRS 8 then requires prior-period segment information to be restated or the change disclosed, so an act has consequences outside this model.",
          "source_refs": [
            "SRC-001",
            "SRC-009",
            "SRC-006"
          ],
          "questions": [
            "What kind of act is this - establish, rename, reclassify, reparent, merge, split, transfer between organizations, or disband - and which units does it affect in which role?",
            "What are the decision instant, the effective instant and the record instant of this act, each with an explicit offset?",
            "Which body took the decision, under which delegated power, and is the decision instrument attached as evidence?",
            "Which downstream obligations does the act trigger - segment restatement, employee information and consultation, directory reprovisioning, contract novation?",
            "May an act be recorded with an effective date in the past, and what compensating controls apply to retroactive entries?"
          ],
          "data_elements": [
            {
              "id": "de-act-kind",
              "name": "reorganizationActKind",
              "description": "Coded kind of structural change.",
              "value_kind": "code",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-act-decision-time",
              "name": "decisionTimestamp",
              "description": "When the decision was taken, in RFC 3339 form with explicit offset.",
              "value_kind": "timestamp",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-act-effective-time",
              "name": "effectiveTimestamp",
              "description": "When the change takes effect in the world.",
              "value_kind": "timestamp",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-act-recorded-time",
              "name": "recordedTimestamp",
              "description": "When the change was captured in the record, kept separate from event time.",
              "value_kind": "timestamp",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-act-affected",
              "name": "affectedUnits",
              "description": "Units affected by the act with their role as original or resulting participant.",
              "value_kind": "collection",
              "cardinality": "1..n",
              "required": true
            }
          ]
        }
      },
      {
        "bundle": "change-and-time",
        "layer": "structural-change-events",
        "finding": {
          "id": "unit-lineage",
          "name": "Unit Lineage and Succession",
          "description": "Merges and splits create many-to-many lineage that a simple parent pointer cannot express. W3C ORG uses originalOrganization and resultingOrganization on a ChangeEvent; ROR uses predecessor and successor relationships and keeps relationships on inactive or withdrawn records as historical tombstones. Lineage must survive the disappearance of its endpoints so that historical references still resolve.",
          "source_refs": [
            "SRC-001",
            "SRC-011"
          ],
          "questions": [
            "Which units are the predecessors and successors of this unit, and through which act was each lineage edge created?",
            "Does a merged or renamed unit retain its identifier as a continuation, or is a new identifier minted with a lineage edge to the old one?",
            "When a consumer dereferences the identifier of a disbanded unit, what is returned - a tombstone, a redirect to the successor, or an error?",
            "When only part of a unit moves in a split, how is the partial transfer of establishment, mandate and staffing apportioned across the lineage edge?"
          ],
          "data_elements": [
            {
              "id": "de-predecessor",
              "name": "predecessorUnitRefs",
              "description": "Units from which this unit derives through a change act.",
              "value_kind": "collection",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-successor",
              "name": "successorUnitRefs",
              "description": "Units into which this unit continues after a change act.",
              "value_kind": "collection",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-lineage-act-ref",
              "name": "lineageActRef",
              "description": "Reference to the reorganization act that created the lineage edge.",
              "value_kind": "reference",
              "cardinality": "0..n",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "change-and-time",
        "layer": "temporal-validity",
        "finding": {
          "id": "effective-dating-bitemporality",
          "name": "Effective Dating and Bitemporality",
          "description": "Every structural assertion - membership in a hierarchy, a reporting line, a mandate, an establishment line - carries a validity period in world time and a separate transaction period in record time. RFC 3339 requires a stated relationship to UTC and offers '-00:00' where the instant is known but the local offset is not, a distinction that matters for multinational effective dates. ROR's admin block separates created from last_modified, illustrating the record-time axis in practice.",
          "source_refs": [
            "SRC-006",
            "SRC-011"
          ],
          "questions": [
            "What are the validity start and end of this assertion in world time, and is an open-ended end represented explicitly or by absence?",
            "When was this assertion first recorded and when was it last modified or superseded in the record, independently of its world-time validity?",
            "Which time offset is used for effective dates in a multi-jurisdiction organization, and is a legal local midnight or a UTC instant intended?",
            "Are gaps or overlaps permitted in the validity of successive parent assignments for the same unit and hierarchy?"
          ],
          "data_elements": [
            {
              "id": "de-valid-from",
              "name": "validFrom",
              "description": "Start of world-time validity for a structural assertion, RFC 3339 with explicit offset.",
              "value_kind": "timestamp",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-valid-to",
              "name": "validTo",
              "description": "End of world-time validity, absent or explicitly open where still current.",
              "value_kind": "timestamp",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-recorded-from",
              "name": "recordedFrom",
              "description": "Start of record-time validity, i.e. when the system first held this assertion.",
              "value_kind": "timestamp",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-time-granularity",
              "name": "temporalGranularity",
              "description": "Whether the assertion is dated to an instant or to a legal calendar day in a stated jurisdiction.",
              "value_kind": "code",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "change-and-time",
        "layer": "temporal-validity",
        "finding": {
          "id": "as-of-reconstruction",
          "name": "As-Of Reconstruction and Versioning",
          "description": "Consumers need the structure as it stood at a past instant, both as it actually was (world time) and as it was believed to be at the time (record time). IFRS 8's requirement to restate prior-period segment information after an internal reorganization, or otherwise disclose the change, makes exact historical reconstruction an external obligation rather than a convenience. Reconstruction outputs must be reproducible and identified.",
          "source_refs": [
            "SRC-009",
            "SRC-006",
            "SRC-011"
          ],
          "questions": [
            "Given a world-time instant and a record-time instant, can the full unit set, hierarchy and reporting lines be reproduced deterministically?",
            "How is a structure version identified so that two consumers can prove they are looking at the same state?",
            "Does the model support producing both the pre-reorganization and post-reorganization views of a prior period for comparative reporting?",
            "How far back is full reconstruction guaranteed, and what happens to reconstruction after retention-driven deletion?"
          ],
          "data_elements": [
            {
              "id": "de-structure-version",
              "name": "structureVersionId",
              "description": "Identifier of a reproducible structure state.",
              "value_kind": "identifier",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-content-digest",
              "name": "contentDigest",
              "description": "Cryptographic digest over the canonical serialisation of the structure state.",
              "value_kind": "text",
              "cardinality": "0..1",
              "required": false
            },
            {
              "id": "de-asof-params",
              "name": "asOfParameters",
              "description": "The world-time and record-time instants that parameterise a reconstruction.",
              "value_kind": "object",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "governance-provenance-and-disclosure",
        "layer": "provenance-and-authority",
        "finding": {
          "id": "record-authority",
          "name": "Record Authority and Source of Truth",
          "description": "Unit structure has no external registrar: the parent organization is the sole authority, unlike legal identity where GLEIF and business registers verify against authoritative local sources. Different attributes may nonetheless have different masters - HR for establishment, finance for cost centres, governance secretariat for mandates - so authority is asserted per attribute group, with a declared conflict resolution order.",
          "source_refs": [
            "SRC-013",
            "SRC-011",
            "SRC-014"
          ],
          "questions": [
            "For each attribute group - identity, hierarchy, mandate, establishment, staffing - which system and which role is the master?",
            "When two systems assert different values for the same attribute, which precedence order applies and who adjudicates a persistent conflict?",
            "Is any part of the structure externally verifiable (a registered branch, a statutory committee), and against which register?",
            "For an ingested assertion, what are the source system, extraction instant and transformation applied before it reached this model?"
          ],
          "data_elements": [
            {
              "id": "de-master-system",
              "name": "masterSystemRef",
              "description": "The authoritative system for a given attribute group of the unit.",
              "value_kind": "reference",
              "cardinality": "1..n",
              "required": true
            },
            {
              "id": "de-accountable-owner",
              "name": "recordOwnerRole",
              "description": "The role accountable for the correctness of the structure record.",
              "value_kind": "reference",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-ingest-timestamp",
              "name": "ingestionTimestamp",
              "description": "When an externally sourced assertion was ingested, kept separate from its event time.",
              "value_kind": "timestamp",
              "cardinality": "0..1",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "governance-provenance-and-disclosure",
        "layer": "provenance-and-authority",
        "finding": {
          "id": "evidence-and-validation",
          "name": "Evidence and Structural Validation",
          "description": "A structural claim is only operable if it can be checked. Validation covers referential integrity against WM-ORG-001 and WM-ORG-004, acyclicity per hierarchy, temporal consistency, establishment-versus-actual variance, segregation rules and the FHIR-style minimum that an entry must have at least one name or identifier. Results are evidence, with severity and an owner, not silent failures.",
          "source_refs": [
            "SRC-002",
            "SRC-001",
            "SRC-014"
          ],
          "questions": [
            "Which validation rules apply to a unit record, at which severity, and which of them block a write?",
            "What is the minimum viable unit record that may be persisted, and does it require at least one name or identifier?",
            "Which assertions require attached documentary evidence before they are treated as authoritative rather than provisional?",
            "Which quality measures are tracked over the structure graph - orphan rate, stale-record age, unmandated units, over-establishment - and what are their thresholds?"
          ],
          "data_elements": [
            {
              "id": "de-validation-rule",
              "name": "validationRule",
              "description": "A named, expressible constraint over the structure graph with severity.",
              "value_kind": "object",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-validation-result",
              "name": "validationResult",
              "description": "Outcome of evaluating a rule against a unit or the graph, with instant and severity.",
              "value_kind": "object",
              "cardinality": "0..n",
              "required": false
            },
            {
              "id": "de-evidence-ref",
              "name": "evidenceRef",
              "description": "Reference to a document or record substantiating an assertion.",
              "value_kind": "reference",
              "cardinality": "0..n",
              "required": false
            }
          ]
        }
      },
      {
        "bundle": "governance-provenance-and-disclosure",
        "layer": "external-alignment",
        "finding": {
          "id": "projection-fidelity",
          "name": "Projection Fidelity and Lossy Export",
          "description": "Exports lose information in predictable ways: LDAP 'ou' and SCIM 'department' carry only names, so identifier, kind, validity period, mandate and reporting type vanish; org charts drop mandate and staffing; segment reports aggregate units away. A projection must declare what it drops and must never be re-imported as authoritative, or the lossy copy will silently overwrite the governed record.",
          "source_refs": [
            "SRC-004",
            "SRC-005",
            "SRC-009",
            "SRC-001"
          ],
          "questions": [
            "For each defined projection, which elements are omitted, flattened or aggregated, and is that loss declared to consumers?",
            "May any projection be re-imported as a source of truth, and what guard prevents an accidental round-trip overwrite?",
            "How stale may a projection be before consumers must be warned, and how is its generation instant and source version published with it?"
          ],
          "data_elements": [
            {
              "id": "de-projection-name",
              "name": "projectionName",
              "description": "Identifier of a defined outward view over the structure.",
              "value_kind": "identifier",
              "cardinality": "1",
              "required": true
            },
            {
              "id": "de-loss-manifest",
              "name": "lossManifest",
              "description": "Declared list of elements omitted, flattened or aggregated by a projection.",
              "value_kind": "collection",
              "cardinality": "1..n",
              "required": true
            },
            {
              "id": "de-projection-source-version",
              "name": "sourceStructureVersion",
              "description": "The structure version a projection was generated from.",
              "value_kind": "reference",
              "cardinality": "1",
              "required": true
            }
          ]
        }
      }
    ],
    "functions": [
      {
        "id": "resolve-unit-identity",
        "name": "Resolve Unit Identity",
        "description": "Resolve any inbound reference - master-system identifier, ISO/IEC 6523 organization part identifier, alias, former name, LDAP distinguished name or IdP group id - to the single current unit record or to a tombstone with a successor pointer."
      },
      {
        "id": "validate-structure-graph",
        "name": "Validate Structure Graph",
        "description": "Evaluate integrity rules over a structure version: acyclicity within each named hierarchy, single parent per hierarchy per validity interval, no orphans, referential integrity to WM-ORG-001 and WM-ORG-004, temporal gap and overlap rules, and segregation-of-duties constraints."
      },
      {
        "id": "reconstruct-structure-as-of",
        "name": "Reconstruct Structure As Of",
        "description": "Return the unit set, hierarchies, reporting lines and mandates valid at a given world-time instant as recorded at a given record-time instant, producing a deterministic, digest-identified view."
      },
      {
        "id": "apply-reorganization-act",
        "name": "Apply Reorganization Act",
        "description": "Apply an evidenced structural change - establish, rename, reclassify, reparent, merge, split, transfer or disband - creating lineage edges, closing and opening validity intervals, and registering downstream obligations."
      },
      {
        "id": "derive-org-chart",
        "name": "Derive Org Chart Projection",
        "description": "Generate a hierarchy view for a named hierarchy at an as-of instant, containing unit names and kinds only, with mandate detail and staffing deliberately excluded."
      },
      {
        "id": "evaluate-mandate-conflict",
        "name": "Evaluate Mandate Conflict",
        "description": "Detect overlapping or incompatible remits across units and breaches of authority limits or independence requirements, before or after a proposed structural change."
      },
      {
        "id": "compute-headcount-rollup",
        "name": "Compute Headcount Rollup",
        "description": "Aggregate staffing measurements up a named hierarchy under a declared counting basis and period convention, applying suppression where a cell falls below the minimum size."
      },
      {
        "id": "reconcile-external-directory",
        "name": "Reconcile External Directory",
        "description": "Compare LDAP or SCIM representations of units against the governed structure, report drift, and push corrections outward without ever accepting the directory as a source of truth."
      },
      {
        "id": "emit-standards-mapping",
        "name": "Emit Standards Mapping",
        "description": "Serialise the structure into a target vocabulary - W3C ORG, CPOV, FHIR Organization, schema.org, or an ISO/IEC 6523 party identifier - using the versioned crosswalk and attaching a fidelity declaration."
      },
      {
        "id": "apply-disposition",
        "name": "Apply Disposition",
        "description": "Execute the approved retention schedule over structure records: destroy, transfer to archive or flag for review, while preserving the tombstones and lineage edges required for historical reference resolution."
      },
      {
        "id": "assign-unit-mandate",
        "name": "Assign mandate",
        "description": "Attach or withdraw a remit, purpose code and delegation source on a unit for a validity interval."
      },
      {
        "id": "seat-post-in-unit",
        "name": "Seat post in unit",
        "description": "Create or attach an established post in a unit independently of any holder. Occupancy is not performed here."
      },
      {
        "id": "assert-reporting-line",
        "name": "Assert reporting line",
        "description": "Record a supervisory or dotted-line reporting edge between units or posts with validity."
      },
      {
        "id": "record-staffing-snapshot",
        "name": "Record staffing snapshot",
        "description": "Store a dated established and filled count for a unit with basis and observation time. Treat as an extension until a primary unit-level metric standard is cited."
      }
    ],
    "composition": [
      {
        "target": "WM-ORG-001 Organization",
        "relation": "REFERENCE",
        "purpose": "Every unit resolves to exactly one parent organization, which holds legal identity, registration and external identifiers. W3C ORG grounds the dependency: a unit 'only has full recognition within the context of that Organization'.",
        "required": true,
        "source_refs": [
          "SRC-001",
          "SRC-013"
        ]
      },
      {
        "target": "WM-ORG-004 Position",
        "relation": "CHILD",
        "purpose": "Units contain or govern established posts. This model holds the establishment count, seating and unit-level occupancy; the post as an object that 'exists independently of who fills it' is defined in WM-ORG-004.",
        "required": false,
        "source_refs": [
          "SRC-001"
        ]
      },
      {
        "target": "Employment / role assignment model",
        "relation": "REFERENCE",
        "purpose": "Employment records fill the posts seated in a unit and are the derivation source for unit-level occupancy counts; persons and contracts never enter this model.",
        "required": false,
        "source_refs": [
          "SRC-001",
          "SRC-005"
        ]
      },
      {
        "target": "Charter / constitutive powers model",
        "relation": "REFERENCE",
        "purpose": "Unit mandates trace upward to powers held by the organization; ISO 37000 requires delegation to be formalized and delegators to remain accountable, so the upstream power must be resolvable.",
        "required": false,
        "source_refs": [
          "SRC-014"
        ]
      },
      {
        "target": "Site / Location model",
        "relation": "REFERENCE",
        "purpose": "A unit may be associated with one or more premises, but FHIR keeps Location distinct from Organization and Eurostat's local unit is a geographic statistical construct, so premises are referenced rather than embedded.",
        "required": false,
        "source_refs": [
          "SRC-002",
          "SRC-010"
        ]
      },
      {
        "target": "Stewardship model (S1)",
        "relation": "MIX-IN",
        "purpose": "The parent organization owns the structure record and units have no independent standing; ownership, custodianship and accountability facets come from the stewardship model.",
        "required": true,
        "source_refs": [
          "SRC-014",
          "SRC-013"
        ]
      },
      {
        "target": "Access grant model (S2)",
        "relation": "REFERENCE",
        "purpose": "Disclosure classes defined here are enforced by grants issued in the access model; this model supplies the scoped projections and suppression parameters, not the grant machinery.",
        "required": true,
        "source_refs": [
          "SRC-015",
          "SRC-003"
        ]
      },
      {
        "target": "Audit trail model (S4)",
        "relation": "MIX-IN",
        "purpose": "Reorganization acts, mandate changes, waivers and disposition actions require immutable audit facets with separate event and record timestamps.",
        "required": true,
        "source_refs": [
          "SRC-006",
          "SRC-016"
        ]
      },
      {
        "target": "W3C Organization Ontology (org:)",
        "relation": "ALIGN",
        "purpose": "Primary structural alignment for OrganizationalUnit, hasUnit/unitOf, subOrganizationOf, purpose, classification, Post, Site and ChangeEvent. Unit-to-unit reportsTo is declared an extension, since org:reportsTo binds Agents and Posts.",
        "required": false,
        "source_refs": [
          "SRC-001"
        ]
      },
      {
        "target": "Core Public Organisation Vocabulary (CPOV) v2.1.2",
        "relation": "ALIGN",
        "purpose": "Public-sector profile alignment for hasUnit, code-valued purpose (COFOG), classification and spatial coverage; applicable only where the parent organization is a public body.",
        "required": false,
        "source_refs": [
          "SRC-003"
        ]
      },
      {
        "target": "HL7 FHIR Organization / OrganizationAffiliation (R5)",
        "relation": "ALIGN",
        "purpose": "Healthcare-sector projection where departments are Organization instances chained by partOf and non-hierarchical relations use OrganizationAffiliation; a known structural conflict with the distinct-unit-class model.",
        "required": false,
        "source_refs": [
          "SRC-002"
        ]
      },
      {
        "target": "ISO/IEC 6523 organization part identification (via Peppol ICD registry)",
        "relation": "ALIGN",
        "purpose": "External addressing of a unit as an organization part under the parent's ICD and organization identifier, used for e-business party and delivery-location identification.",
        "required": false,
        "source_refs": [
          "SRC-007",
          "SRC-008"
        ]
      },
      {
        "target": "LDAP (RFC 4519) and SCIM (RFC 7643) directory schemas",
        "relation": "ALIGN",
        "purpose": "Outbound-only projection targets. Both carry unit information as names without identifiers, validity or typed edges, so alignment is declared lossy and re-import is prohibited.",
        "required": false,
        "source_refs": [
          "SRC-004",
          "SRC-005"
        ]
      },
      {
        "target": "Statistical units framework (Council Regulation (EEC) No 696/93)",
        "relation": "ALIGN",
        "purpose": "Mapping of internal units to enterprise, kind-of-activity unit and local unit for statistical reporting, recorded as a derivation with explicit boundary mismatch rather than as equivalence.",
        "required": false,
        "source_refs": [
          "SRC-010"
        ]
      },
      {
        "target": "IFRS 8 operating segment determination",
        "relation": "ALIGN",
        "purpose": "The internal reporting hierarchy is an input to segment identification under the management approach, and reorganization acts trigger the restate-or-disclose obligation; segment determination itself stays outside this model.",
        "required": false,
        "source_refs": [
          "SRC-009"
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
        "rationale": "Both providers independently classify WM-ORG-002 as an entity, and the base draws the boundary on every side with source-referenced neighbour distinctions: legal personality to WM-ORG-001 (W3C ORG FormalOrganization vs OrganizationalUnit; GLEIF issues LEIs only to legal entities), the post as an object to WM-ORG-004 (org:Post exists independently of its holder), premises to a site model (FHIR Location vs Organization), statistical observation units to a statistics model (Reg. 696/93), and derived segments to financial reporting (IFRS 8 management approach with permitted aggregation). Directory content (RFC 4519 ou, RFC 7643 department) is fixed as a lossy projection and never a system of record. The one live boundary disagreement is the unit-to-site association, which the secondary provider places in scope; the base exclusion is retained for this pass and the association is deferred rather than forced into a layer that does not fit it."
      },
      "decisions": [
        {
          "concept": "Base provider selection",
          "disposition": "accepted claude as base",
          "rationale": "Not chosen for size. The base states in_scope, out_of_scope and seven source-referenced neighbour distinctions that close the boundary on every side, and its adversarial checks show the boundary was tested rather than asserted. The secondary provider leaves the site boundary open and treats multi-hierarchy structure as an omission."
        },
        {
          "concept": "Entry kind",
          "disposition": "accepted as entity",
          "rationale": "Both providers converge on entity independently, and the node behaves as a persistent identified thing with lifecycle, relationships and versioned state rather than as an event, a policy or a service."
        },
        {
          "concept": "W3C ORG OrganizationalCollaboration typing",
          "disposition": "accepted into unit-classification",
          "rationale": "Fills a gap the base itself declares unresolved, is anchored in the base's own tier-1 source, and supplies the test that keeps cross-organization bodies out of the unit set instead of silently absorbing them."
        },
        {
          "concept": "ChangeEvent conformance threshold",
          "disposition": "accepted into structural-change-events",
          "rationale": "Prevents the base from over-claiming ORG semantics by treating every rename or reparent as a ChangeEvent, and adds CPOV hasFormalFramework as the link from the act to its authorizing instrument."
        },
        {
          "concept": "Unit-to-site and contact-point linkage",
          "disposition": "deferred",
          "rationale": "Genuinely evidence-backed in W3C ORG via org:Site, hasSite, hasPrimarySite and hasRegisteredSite, and therefore not rejected on evidence. But the base excludes premises by explicit adversarial decision and no existing base layer hosts a placement finding, so importing it would require inventing structure. Held open as a boundary question."
        },
        {
          "concept": "Grok master-and-global-identifiers finding",
          "disposition": "rejected as duplicative",
          "rationale": "The base already covers master-system assignment, ISO/IEC 6523 organization-part addressing, identifier stability across rename and reparent, and the UUID/ULID fallback. Only the point that an LDAP distinguished name is a naming address rather than a persistent identifier is additive, and it belongs as a crosswalk note on projection fidelity, not a new finding."
        },
        {
          "concept": "Grok lexical-names finding",
          "disposition": "rejected as duplicative",
          "rationale": "The base's naming finding already carries official name, aliases, former names and the rule that names are never identity. The SKOS prefLabel/altLabel/notation binding and CPOV's at-most-one-preferred-label-per-language cardinality are refinements to that finding, to be folded into the crosswalk rather than added as separate structure."
        },
        {
          "concept": "Grok head-of-unit finding",
          "disposition": "rejected as duplicative",
          "rationale": "The base's accountable-role finding already models the head as a post or Membership slot with acting, interim and vacant states and keeps person occupancy out of scope. org:headOf as a specialization of memberOf is a mapping detail for the crosswalk."
        },
        {
          "concept": "Grok unit-purpose finding",
          "disposition": "rejected as duplicative",
          "rationale": "The base's mandate-scope finding covers remit statement, delegating instrument, spatial and functional limits, and the CPOV COFOG recommendation with its public-sector restriction already recorded as a conflict."
        },
        {
          "concept": "Grok posts-in-unit finding",
          "disposition": "rejected as a finding, escalated to a hold",
          "rationale": "Duplicates the base's authorized-post-complement, but carries a caveat the base lacks: neither W3C ORG nor the ISO material consulted defines establishment counts, grades or pay bands, so those are local controls rather than standard properties. That evidentiary limit is recorded as a publication hold instead of new structure."
        },
        {
          "concept": "Grok predecessor-successor finding",
          "disposition": "rejected as duplicative",
          "rationale": "The base's unit-lineage finding covers predecessor and successor edges, identifier continuity, tombstone dereferencing and partial transfer in a split. CPOV prev/next and the dual-running overlap window are deferred as crosswalk and validation detail."
        },
        {
          "concept": "Grok atomic mutation functions",
          "disposition": "rejected as subsumed",
          "rationale": "establish-unit, reparent-unit, merge-or-split-units and disband-unit are decompositions of the base's apply-reorganization-act, which already opens and closes validity intervals, creates lineage edges and registers downstream obligations. Importing them would fork the write path."
        },
        {
          "concept": "Grok disclose-org-chart function",
          "disposition": "rejected as duplicative",
          "rationale": "The base already separates derive-org-chart, which deliberately omits mandate and staffing, from the structure-disclosure package and its scoping rules; a second disclosure entry point would blur that separation."
        },
        {
          "concept": "Unit-to-unit reporting stance",
          "disposition": "accepted base framing",
          "rationale": "Both providers agree org:reportsTo is defined between Agents and Posts. The base's stricter treatment of unit-level edges as a declared non-conformant extension with a mapping rule governs, and the imported assert-reporting-line function must write that declaration."
        },
        {
          "concept": "Measurement coverage status",
          "disposition": "reclassified to extension-grade",
          "rationale": "The base marks measurement covered on ESRS S1-6, which is an undertaking-level disclosure standard, while the secondary provider marks it a gap because no primary source defines a unit-grain metric. The honest position is that unit-level headcount and FTE are operationally necessary but standards-thin."
        },
        {
          "concept": "Concurrent named hierarchies",
          "disposition": "retained from base",
          "rationale": "The base models managerial, legal, cost and functional hierarchies as separately governed edge sets with per-hierarchy single-parent constraints and ties the choice to IFRS 8's management approach; the secondary provider lists typed multi-hierarchy collections as an omission, so the base is strictly stronger here."
        }
      ],
      "publicationHolds": [
        "Source and live-version verification is outstanding for all sixteen base sources and for the two imported W3C ORG and CPOV anchors. Resolve the dated W3C ORG REC URI against the latest-version URI, confirm CPOV 2.1.2, schema.org v30.0 and the Peppol ICD list are still current, and pin FHIR deliberately, since the base cites R5 and the secondary provider cites R4.",
        "ISO-derived structure is guidance-grade, not requirement-grade. ISO 37000:2021, ISO 30414:2018, ISO 15489-1:2016 and ISO/IEC 6523-1:2023 are paywalled and were reviewed only through committee decks, catalogue metadata and deployment profiles, so the delegated-authority, assurance and segregation findings must not be published as normatively sourced until clause text is verified.",
        "ESRS S1-6 clause text was not machine-parsed; headcount, FTE, breakdown and the fifty-employee country threshold are stated at summary level and must be checked against Annex I of Commission Delegated Regulation (EU) 2023/2772 before any compliance-adjacent claim.",
        "Unit-grain staffing measurement has no primary standard. Established-versus-filled counts, budgeted FTE and establishment complement are local controls; publish the measurement layer and record-staffing-snapshot as extension-grade with that limitation visible.",
        "Multi-profile validation is incomplete. The model was tested chiefly against public-sector (CPOV/COFOG), healthcare (FHIR), EU reporting (IFRS 8, ESRS S1), directory (LDAP/SCIM) and e-invoicing (ISO/IEC 6523) profiles. Private-sector matrix organizations, military, academic-collegiate, ecclesiastical and cooperative unit forms are not validated and must not be presented as covered.",
        "Council Regulation (EEC) No 696/93 was not retrieved from EUR-Lex; the statistical-unit boundary currently rests on a Eurostat glossary entry that cites it, and must be confirmed against the regulation text.",
        "Regional scope must be stated on the face of any draft: CPOV, ESRS and the statistical-unit framework are EU instruments, NARA General Records Schedules bind US federal agencies only, financial alignment assumes IFRS rather than ASC 280, and employee consultation duties before a reorganization are jurisdiction-conditioned."
      ],
      "deferredResearch": [
        "Unit-to-site association: decide whether org:hasSite, hasPrimarySite and hasRegisteredSite belong here as a bounded reference or entirely in the site model. The base excludes premises after an explicit adversarial test; the secondary provider places the link in scope on W3C ORG evidence. Resolve before the next boundary pass, and add a placement layer only if the reference is accepted.",
        "CPOV range and lineage detail: CPOV ranges unitOf at Public Organisation and states a unit cannot exist on its own, which is narrower than W3C ORG's units-of-units, and CPOV prev/next cover rename and split sequences that may retain identity. Fold both into the crosswalk with explicit range, cardinality and fidelity notes.",
        "Popolo Organization and Post as an additional crosswalk target, including its single-classification restriction, its rejection of org:holds in favour of Membership, and its distinct former-name property, which few vocabularies provide.",
        "Cost-centre, profit-centre and funds-centre ERP hierarchies: confirm whether these are admitted as named concurrent hierarchies inside this model or remain finance masters referenced from it, since both providers flag them and neither resolves the boundary.",
        "Works councils, union structures and co-determination bodies: both providers record these as an unmodelled gap that nonetheless gates reorganization effectiveness. Determine whether they become a sibling model or remain a jurisdiction-conditioned precondition on the act.",
        "Establishment-count standardization: search for a primary, unit-grain source defining authorized post complement, grade and budgeted FTE. Absent one, keep the establishment findings marked as local control rather than standard property.",
        "LDAP distinguished-name instability under reparenting, and the name-reuse-after-disbandment collision case with x500UniqueIdentifier-style disambiguators, as validation rules on the identity and projection-fidelity findings.",
        "Informal and shadow structure, temporary project organizations and de facto reporting: both providers record these as gaps with no authoritative source. Confirm the gap stands rather than inventing structure to close it."
      ]
    },
    "statistics": {
      "sources": 23,
      "bundles": 6,
      "layers": 13,
      "findings": 28,
      "questions": 106,
      "artifacts": 17,
      "functions": 14
    }
  },
  "evidence_limits": [
    "The current publication is reviewable-draft and publishableCanonical false.",
    "Complete spec parsed and pinned by digest; selected findings form the compact reviewer projection.",
    "Enterprise v1 fields and registry relations are non-normative."
  ]
}

```

## CLAUDE STUDY
## Verdict

**PROFILE.** EM-ORG-04 does not prove an independent identity or lifecycle for `OrganizationalUnit` separate from the reserved WM-ORG-002: the reserved model already owns unit identity, kind classification, containment, mandate, establishment, reorganization acts and bitemporality, and EM-ORG-04's four candidate types map onto it without residue at entity grain. A new model candidate is not justified; nor is the reserved model incomplete in the "COMPLETE RESERVED MODEL" sense, since its layers exist and are populated. What is missing is one qualifier dimension (scenario/branch) and a set of enforcement rules that the reserved model states as questions rather than constraints. That is the shape of a narrow Enterprise profile over WM-ORG-002, not a second owner of `unit`. No canonical status, approved relation or installability is claimed here.

## Evidence state

The spec is pinned by digest (`9e3e80da…`, 250,855 bytes) and parsed; the reviewer projection is a selected subset of 28 findings. Publication metadata is self-limiting: `status: published` but `adjudicationStatus: reviewable-draft` and `publishableCanonical: false`, version `0.3.0-research.1`. The registry reservation carries `status: described-previous-version`, `review_state: migration-boundary-review`, and a source date (2026-08-22) earlier than the spec's `generatedAt` (2026-08-23) — a reconciliation item, not a defect finding. The EM-ORG-04 → WM-ORG-002 link is `conceptual-candidate` at `index-and-publication-metadata` depth; both ledger relations are `review_state: candidate`. Seven publication holds are open, including unverified live source versions and paywalled ISO clause text underlying the delegation and segregation findings. Enterprise v1 fields are non-normative. Nothing below should be read as clearing those holds.

## Identity and aggregate boundary

Unit identity passes the separation test in the reserved model: `unitIdentifier` + `unitIdentifierScheme` are mandatory and parent-scoped (ROR explicitly declines to identify subdivisions), names are declared non-identity with aliases and historical names, and `unitStatus` separates "ceased" from "created in error". Identity is therefore independent of name, of mandate and of any placement — the profile only needs to make the identifier-stability question ("does the identifier survive rename, reparent, merger?") a fixed answer rather than an open question.

`UnitType` is not an entity: the reserved model already renders it as `unitKind` against a versioned `classificationScheme`, multi-valued. Do not mint it.

`UnitMandate` is **a temporal assignment, not intrinsic and not an independent aggregate**. Evidence: `mandateValidity` as a period, `assign-unit-mandate` as attach/withdraw over an interval, delegation traced to an instrument, and ISO 37000's requirement that delegation be formalized. It has no identity apart from the (unit, instrument, interval) triple and no lifecycle independent of the unit, so it stays a reified assignment inside WM-ORG-002.

## Placement/axis/scenario contract

`StructuralPlacement` is likewise not a new model: `hierarchyEdge` is already "a parent-child edge qualified by hierarchy identifier and validity period", with `hierarchyIdentifier` required `1..n` and managerial, legal, cost and functional hierarchies kept as separately governed edge sets. Axis coexistence without overwriting is therefore supported today.

Two defects remain. First, `parentUnitRef` (`0..1`) sits on the unit record alongside the edge collection, creating a second, unqualified write path that silently privileges one axis; `hierarchyPath` is derived from it. Second, there is no scenario qualifier anywhere. Asserted-current and historical-as-of are handled by valid-time plus record-time; approved-future is handled by a future `effectiveTimestamp`; **hypothetical scenario is unsupported** — a to-be structure can only be expressed by asserting it, which contaminates `validate-structure-graph`, `reconstruct-structure-as-of` and `derive-org-chart`.

## Mandate and authority

Keep the reserved model's framing: remit statement plus coded purpose, bounded `authorityLimit` objects as first-class data, `headPostRef` to WM-ORG-004 with `headshipState` for acting/vacant, and segregation rules with time-bounded waivers. The profile should add nothing structural here, but must not publish the delegation/segregation material as normatively sourced while the ISO hold stands. Mandate must be placement-independent: a unit's remit is not derived from, and does not change with, its administrative parent.

## Temporal/reorganization rules

`apply-reorganization-act` carries decision, effective and record instants with `affectedUnits`, closes and opens validity intervals and writes lineage; `predecessorUnitRefs`/`successorUnitRefs` plus `lineageActRef` express many-to-many merge and split; tombstones are retained through `apply-disposition`. Rename and reparent therefore preserve identity by construction, and merge/split/disband produce explicit lineage. The gaps are narrow: the open question on gaps/overlaps between successive parent assignments must be closed as a rule, and the ChangeEvent conformance threshold (accepted in adjudication) must prevent every rename being over-claimed as `org:ChangeEvent`.

## Invariants

Proposed as profile-level, testable constraints (labels illustrative, not assigned identifiers):

1. A placement is valid only as an axis-, scenario- and interval-qualified edge; no parent may be asserted on the unit record itself.
2. Per (axis, scenario, instant): at most one parent, and the edge set is acyclic. Acyclicity is evaluated per scenario branch, never across merged branches.
3. Rename and reparent preserve `unitIdentifier`; merge, split and disband require a lineage edge and an act reference.
4. Placement on any management axis never determines employer or legal entity; the employer derives only from `parentOrganizationRef` / `isAlsoFormalOrganization` and the out-of-scope employment model.
5. A body typed as collaboration may not hold an administrative-axis parent placement.
6. Scenario-qualified placements are excluded from asserted-current reads unless the scenario is the asserted branch.

## Scenario walkthrough

**Negative case.** A cross-department product team is given one administrative parent. The reserved model can represent it correctly — `Body mode: collaboration`, plus `unitAffiliation` edges to contributing units — but nothing prevents the wrong representation: `parentUnitRef` accepts a single value, and `derive-org-chart` needs a tree in the default hierarchy, which pressures an operator to invent a parent. Result: the team is mistaken for a unit, its members' home-unit posts are double-counted by `compute-headcount-rollup`, and the misplacement propagates into the IFRS 8 reporting hierarchy. Invariants 1 and 5 close this; without them the case fails.

**Acceptance case.** As-is/to-be reorganization on the administrative axis. If "to-be" is an *approved* future act, the reserved model passes: the act opens new intervals without deleting old assignments, `reconstruct-structure-as-of` replays the as-is state, and `validate-structure-graph` proves acyclicity on the selected axis. If "to-be" is a *hypothetical* option under evaluation, it fails: there is no branch on which to run validation, and asserting it corrupts the current view. The acceptance scenario is therefore met only under the approved-future reading.

## Profile shape

A narrow Enterprise profile over WM-ORG-002 — no new model, no second owner of `unit`, identifier unassigned and not requested. Content: (a) reify placement and forbid the unit-level parent attribute; (b) add the scenario/branch qualifier to placements, mandates, reporting lines and to the parameters of `validate-structure-graph`, `reconstruct-structure-as-of` and `derive-org-chart`; (c) convert the open questions on identifier stability, single-parent-per-axis, gap/overlap and employer independence into the invariants above; (d) tighten collaboration typing from a code value to an enforced exclusion. EM-ORG-04's questions 1–3 resolve as: identity is what makes a unit standalone; axes separate the three belongings; and the two-owner risk disappears because the profile constrains rather than redefines.

## Gaps and publication holds

Unsupported scenario semantics: hypothetical/branch structures, scenario comparison and per-branch validation — the single material capability gap. Also unresolved and blocking any readiness claim: the unit-to-site placement question (deferred in adjudication, and it would host any future site-axis placement); cost/profit/funds-centre hierarchies unresolved as in-model axes versus finance masters; unit-grain staffing measurement with no primary standard (extension-grade); ISO clause text, EUR-Lex 696/93, ESRS S1-6 Annex I and all source live-version checks outstanding; FHIR R4/R5 unpinned; private-sector matrix, military, academic, ecclesiastical and cooperative forms unvalidated — directly relevant to the matrix case above. The crosswalk depth required by EM-ORG-04's blocking decisions is not yet evidenced, so the profile recommendation is a boundary finding only.


## GROK STUDY
**Verdict.** PROFILE over WM-ORG-002. No new catalogue or runtime ID. OrganizationalUnit, UnitType, UnitMandate and StructuralPlacement are named 002 constructs, not a second unit master. The org chart remains the EM-LND-01 projection. Team collectives remain WM-ORG-003 / EM-ORG-05. OUMM-style fields are reconciled by constraining 002, not by minting a parallel owner. This is standards alignment, not a W3C ORG or ISO 37000 conformance claim.

**Identity test.** Source facts: 002 already treats names as unstable and non-unique; the identifier is minted by the containing WM-ORG-001 organization and survives rename, reparenting and merger unless a continuity decision mints a new id with a lineage edge. Card invariant: renaming preserves the ID. Every unit resolves to exactly one parent *organization* for its lifetime.

The unit key is that 002 identifier. Rename updates name forms and keeps historical names. Reparent closes one StructuralPlacement interval and opens another. Reclassification changes UnitType only. Fail-to-new-ID if current name, current mandate text or current parent is treated as the key.

Merge, split, disband and transfer between 001 organizations require a reorganization *act* plus lineage edges. Continuity is an explicit decision (retain id XOR new id + predecessor/successor). Partial transfers apportion mandate and establishment across the lineage. The 001 owner link is not an axis parent.

**Mandate boundary.** UnitMandate is a temporal assignment on the unit, not the unit’s identity and not a placement edge. It owns remit and coverage (subject, geography, customer, process), delegating instrument and body, bounds (spend, signing, hiring), validity interval and sub-delegation conditions. 002 already traces mandate to a formal instrument (ISO 37000 alignment).

Mandate is placement-independent: a unit can keep the same remit across a reparent; a reparent does not rewrite remit. Changing remit is a mandate-version event. Fail if remit is stored only as the parent’s purpose, or if moving a unit silently edits mandate.

UnitType is classification against a governed scheme (department, division, cost centre, …). Repeatable and dated. Not identity. Listing “team” as a 002 type code must not collapse a 003 collective into a unit.

**Placement key / cardinality.** StructuralPlacement is a reified 002 edge. Key:

`(childUnit, parentUnit, axis, scenario, validInterval)`

Record-time and act-ref are provenance, not identity.

Tree-like axes (administrative containment, legal-entity roll-up, cost roll-up when declared as a tree): at most one parent per `(child, axis, scenario)` at any overlapping valid-time instant. Overlap of two open intervals on that key is refused. Graph-like axes (functional / professional, some reporting): multiple declared parents only if the axis profile allows them; still acyclic per `(axis, scenario, interval)`. Child ≠ parent. Self-loops refused.

The **unqualified unit-level parent field is the second write path this PROFILE forbids.** If 002 still exposes `parentUnit` without axis + scenario + interval, that field becomes a derived projection of one designated default (typically administrative + authoritative current) or is removed. Writes go only through StructuralPlacement. Dual-write of “the parent” and an axis edge is a publication blocker.

**Scenario model.** Four assertion kinds, not interchangeable.

1. **Asserted current** — authoritative as-of now; default read.
2. **Historical** — closed valid-intervals; immutable except record-time correction.
3. **Approved future** — valid-from in the future, backed by an approved reorganization act; visible in planning reads, not in current structure unless as-of ≥ effective instant.
4. **Hypothetical** — requires an explicit scenario-branch identifier. Excluded from authoritative reads. Must not leak into current or approved-future graphs.

EM-LND-01 left scenario unsupported on the landscape. This PROFILE is the unit-placement extension: hypotheticals are first-class 002 facts only when `scenario ≠ authoritative`. Landscape snapshots pin scenario + as-of; they do not own placements. An authoritative read that cannot reconstruct the requested horizon is refused.

**Team / unit distinction.** A 003 collaboration or cross-department product team cannot receive an administrative StructuralPlacement. Administrative placement is unit-to-unit containment on the administrative axis. Team members remain in their home units; the team is linked by 003 membership and optionally a functional or project edge. If the product body is *also* a standing 002 unit, dual-typing must be explicit — then it is a unit, not a 003 collaboration. W3C ORG alignment: `org:OrganizationalUnit` ≠ `org:OrganizationalCollaboration`.

Management parent never determines employer or legal entity (card invariant). Employer is a WM-ORG-005 fact bound to a 001 legal subject. Administrative, functional, legal, cost and reporting parents are independent graphs. None is inferred from another.

**Temporal and lineage rules.** Every placement and mandate carries world-time validity and record time. Axes coexist and are not unioned before evaluation. A cycle across the union of two axes is allowed; a cycle inside one `(axis, scenario, interval)` is refused. Reorganization acts carry decision, effective and record instants. Old intervals are closed, not rewritten.

**Scenario results.**

*Negative — product team forced under one administrative parent.* Team T has members from units A and B. Writing T as administrative child of A falsifies A/B containment and invents a single tree parent. Correct: T is a 003 team; members keep placements in A and B; optional project-axis coordination; no administrative parent for T.

*Acceptance — as-is / to-be reorganization.* As-is = authoritative placements valid at \(t_0\). To-be = approved-future (or named branch) placements valid at \(t_1\), produced by a reorganization act with lineage. Cycle check runs inside the selected `(administrative, scenario, interval)` only, not across as-is ∪ to-be. Authoritative current read at \(t < t_1\) returns as-is. Old mandates, staffing and 003 membership persist via closed intervals. Contaminating current state with to-be edges fails the card.

**Required profile constraints.** Unit ID survives rename and reparent. Merge / split / disband require act + lineage. UnitType ≠ identity. Mandate ⊥ placement. Placement key includes axis + scenario + interval. No unqualified parent write path. Single parent only within tree-like axis/scenario/time. Acyclicity per axis/scenario/interval. Hypothetical needs an explicit branch and is excluded from authoritative reads. 003 teams cannot take administrative placement. Management parent ≠ employer / legal entity. EM-LND-01 remains the projection; 002 remains the unit master.

**Publication blockers.** 002 is a non-canonical reviewable draft; source and live-version pins remain open. 002 still describes “one parent unit within a given hierarchy” without a first-class StructuralPlacement key or a named scenario field — PROFILE text must land before dual-write of an unqualified `parentUnit` can be closed. “Team” remains a 002 type-code leak against 003. No executable fixtures for: rename/reparent identity stability; mandate unchanged across reparent; refused admin placement of a 003 team; as-is/to-be cycle check that does not contaminate current state; acyclicity per axis with a legal cycle across the union. Alignments to W3C ORG and ISO 37000 are alignments only. Do not invent OrganizationalUnit, UnitMandate, UnitType or StructuralPlacement runtime identifiers.


## PROVIDER COMPARISON
# EM-ORG-04 provider comparison

Claude and Grok independently converge on **PROFILE** over `WM-ORG-002`, with no new catalogue or runtime identifier. Unit identity remains stable across rename, reparent and reclassification. UnitType is a dated classification, UnitMandate is a placement-independent temporal assignment, and StructuralPlacement is a reified edge qualified by child, parent, axis, scenario and interval.

Both providers reject an unqualified parent as a second write path, keep administrative, functional, legal, cost and reporting axes separate, distinguish current, historical, approved-future and hypothetical assertions, prevent hypothetical leakage into authoritative reads, and keep cross-department teams in WM-ORG-003 rather than forcing administrative placement.

Grok sharpens the boundary with explicit tree-like versus graph-like axis cardinality, per-axis/scenario/interval acyclicity, a scenario branch requirement, an explicit dual-typing rule for bodies that are both standing units and collaborations, and a rule that employer/legal entity cannot be inferred from management placement. These refinements preserve the PROFILE decision.


## CANDIDATE
```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-ORG-04",
  "name": "Enterprise Organizational Unit and Mandate",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ORG-002"
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-pre-audit-publication-held",
  "publishableCanonical": false,
  "fixturesExecuted": false,
  "basePins": [
    {
      "modelId": "WM-ORG-002",
      "registryId": "vr.wm-org-002",
      "modelVersion": "0.3.0-research.1",
      "sourceFile": "publications/wm-org-002-organizational-unit/spec.yaml",
      "sourceBytes": 250855,
      "sourceSha256": "9e3e80da4db6db6589991102b91af4af1a00080cd348848250b63f70a97b2330",
      "synthesisSha256": "a991fb7774ae1b611787fe093e9d9e380499bf42c9fbe69fcb91af147be90812",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "providerMode": "dual-provider",
      "registryStatus": "described-previous-version",
      "registryReviewState": "migration-boundary-review",
      "invalidationRule": "Any source, synthesis or reservation drift invalidates this candidate."
    }
  ],
  "constraints": [
    "OrganizationalUnit uses the stable WM-ORG-002 identity and never keys identity by name, mandate, type or current parent.",
    "Rename, reparent and reclassification preserve identity; merge, split, disband and cross-organization transfer require a reorganization act, explicit continuity decision and lineage edges.",
    "UnitType is a repeatable dated classification assignment under a governed scheme and is never identity.",
    "UnitMandate is a temporal assignment with remit, coverage, delegating instrument/body, authority bounds, validity, evidence and sub-delegation conditions; it is independent of placement.",
    "StructuralPlacement is the only authored parent path and is keyed by child, parent, axis, scenario and valid interval; record time and act reference are provenance.",
    "Any unqualified parentUnit field is removed or becomes a derived read projection of the designated default axis/scenario/as-of query.",
    "Tree-like axes permit at most one overlapping parent per child, axis and scenario at an instant; graph-like axes may allow multiple parents only under their axis profile.",
    "Self-loops are forbidden and acyclicity is evaluated independently for each axis, scenario and interval; a cycle across the union of different axes is not itself an error.",
    "Asserted-current, historical, approved-future and hypothetical assertions are distinct; hypothetical assertions require an explicit branch and are excluded from authoritative reads.",
    "Approved-future placements require an approved reorganization act and affect current reads only when the effective instant is reached.",
    "WM-ORG-003 teams and collaborations cannot receive administrative StructuralPlacement; explicit dual-typing is required before a body is also treated as a standing WM-ORG-002 unit.",
    "Management, reporting, functional, legal and cost parents never determine employing legal entity; employment remains externally mastered.",
    "Every placement and mandate is bitemporal and corrections append superseding assertions rather than rewrite closed history.",
    "EM-LND-01 remains a scenario-and-as-of-pinned projection and never masters unit placement.",
    "No W3C ORG, ISO 37000, canonical, installable or conformance claim is made; alignments remain informative while source and base holds are open.",
    "Publication is refused while WM-ORG-002 is noncanonical, StructuralPlacement/scenario fields and parent-write migration are unapplied, team type leakage remains, or fixtures are unexecuted."
  ],
  "profileTypes": {
    "OrganizationalUnit": "WM-ORG-002 identity master",
    "UnitType": "dated classification assignment",
    "UnitMandate": "temporal assignment inside profile",
    "StructuralPlacement": "reified relationship inside profile"
  },
  "placementContract": {
    "key": [
      "childUnit",
      "parentUnit",
      "axis",
      "scenario",
      "validInterval"
    ],
    "provenance": [
      "recordTime",
      "reorganizationActRef",
      "evidence"
    ],
    "axes": [
      "administrative",
      "functional",
      "legal",
      "cost",
      "reporting",
      "project"
    ],
    "writePath": "StructuralPlacement only",
    "defaultParent": "derived projection only"
  },
  "scenarioContract": {
    "kinds": [
      "asserted-current",
      "historical",
      "approved-future",
      "hypothetical"
    ],
    "hypotheticalBranchRequired": true,
    "authoritativeLeakageForbidden": true
  },
  "teamBoundary": {
    "WM-ORG-003": "collaboration/team master",
    "administrativePlacement": "forbidden unless explicit standing-unit dual type",
    "membership": "remains WM-ORG-003"
  },
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
    "Source and live-version verification is outstanding for all sixteen base sources and for the two imported W3C ORG and CPOV anchors. Resolve the dated W3C ORG REC URI against the latest-version URI, confirm CPOV 2.1.2, schema.org v30.0 and the Peppol ICD list are still current, and pin FHIR deliberately, since the base cites R5 and the secondary provider cites R4.",
    "ISO-derived structure is guidance-grade, not requirement-grade. ISO 37000:2021, ISO 30414:2018, ISO 15489-1:2016 and ISO/IEC 6523-1:2023 are paywalled and were reviewed only through committee decks, catalogue metadata and deployment profiles, so the delegated-authority, assurance and segregation findings must not be published as normatively sourced until clause text is verified.",
    "ESRS S1-6 clause text was not machine-parsed; headcount, FTE, breakdown and the fifty-employee country threshold are stated at summary level and must be checked against Annex I of Commission Delegated Regulation (EU) 2023/2772 before any compliance-adjacent claim.",
    "Unit-grain staffing measurement has no primary standard. Established-versus-filled counts, budgeted FTE and establishment complement are local controls; publish the measurement layer and record-staffing-snapshot as extension-grade with that limitation visible.",
    "Multi-profile validation is incomplete. The model was tested chiefly against public-sector (CPOV/COFOG), healthcare (FHIR), EU reporting (IFRS 8, ESRS S1), directory (LDAP/SCIM) and e-invoicing (ISO/IEC 6523) profiles. Private-sector matrix organizations, military, academic-collegiate, ecclesiastical and cooperative unit forms are not validated and must not be presented as covered.",
    "Council Regulation (EEC) No 696/93 was not retrieved from EUR-Lex; the statistical-unit boundary currently rests on a Eurostat glossary entry that cites it, and must be confirmed against the regulation text.",
    "Regional scope must be stated on the face of any draft: CPOV, ESRS and the statistical-unit framework are EU instruments, NARA General Records Schedules bind US federal agencies only, financial alignment assumes IFRS rather than ASC 280, and employee consultation duties before a reorganization are jurisdiction-conditioned."
  ],
  "publicationGate": {
    "publishableCanonical": false,
    "fixturesExecuted": false,
    "statusCeiling": "reviewable research checkpoint",
    "openHolds": [
      "WM-ORG-002 publishableCanonical=false",
      "first-class StructuralPlacement and scenario fields absent",
      "unqualified parent dual-write unresolved",
      "team type-code leak against WM-ORG-003",
      "source/live-version pins open",
      "no executed fixtures"
    ],
    "rule": "Any open hold, pin drift or unexecuted fixture refuses publication."
  }
}
```

## FIXTURES
```json
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Organizational Unit and Mandate",
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
      "id": "rename",
      "kind": "positive",
      "input": "Unit renamed",
      "expect": "same unit ID; dated name changes",
      "sha256": "42a6c0166601f4c7139e89ee42692ba463472907c8216a4be0b57e873d9d6aee"
    },
    {
      "id": "reparent",
      "kind": "positive",
      "input": "Unit moves between parents in one axis",
      "expect": "close old interval, open new; same ID",
      "sha256": "91225676adef41aa867100b37aa8b24baf01659aeb4ce58bd8dfc3bafbbd8177"
    },
    {
      "id": "mandate-reparent",
      "kind": "positive",
      "input": "Unit reparented without remit change",
      "expect": "mandate version unchanged",
      "sha256": "82225501221200c7597a9a9b97a303712dadeabcbf70afaceb8e770f70e999aa"
    },
    {
      "id": "mandate-change",
      "kind": "positive",
      "input": "Remit changes",
      "expect": "new mandate version; same unit ID",
      "sha256": "390cf235dff3c3b88278d5b8cfcea2a476b1e545f6c71601d020c007f0413afb"
    },
    {
      "id": "matrix-axes",
      "kind": "positive",
      "input": "Administrative and functional parents coexist",
      "expect": "both accepted in separate axes",
      "sha256": "84a45692fb63294aba4ba11318fd291541b9ea5f8d8b644545013a2c9a20fa9d"
    },
    {
      "id": "tree-overlap",
      "kind": "negative",
      "input": "Two administrative parents overlap in same scenario",
      "expect": "reject",
      "sha256": "0b0a13c0961c252c3ee66172ffb7ab920af7cbe652277ad8eab72592dbb3af9e"
    },
    {
      "id": "graph-multiple",
      "kind": "positive",
      "input": "Functional axis profile allows two parents",
      "expect": "accept if acyclic",
      "sha256": "f4e17d0cb92da099c6d7a5cff3076763f4c11608b2bf5f9b09b84b0d73a4e706"
    },
    {
      "id": "axis-cycle",
      "kind": "negative",
      "input": "Cycle within one axis/scenario/interval",
      "expect": "reject",
      "sha256": "e0c5c01922e78bff83ec1530375a28e0f927396cdcb7600ef3332f30ff76dcb6"
    },
    {
      "id": "union-cycle",
      "kind": "positive",
      "input": "Union of two axes forms a cycle but each axis is acyclic",
      "expect": "accept",
      "sha256": "f3ca3bd96040a4b0a41b95ba73b5fbbaed814862608ecaad306bed3bbd83e418"
    },
    {
      "id": "self-loop",
      "kind": "negative",
      "input": "Unit is its own parent",
      "expect": "reject",
      "sha256": "a99f20d3aacb94c9997023ad6618461fa357959918c268884e3b8ef09b16c536"
    },
    {
      "id": "parent-dual-write",
      "kind": "negative",
      "input": "Unqualified parent conflicts with StructuralPlacement",
      "expect": "reject publication/write",
      "sha256": "426a38cb5d4b4575c0605b5e5271f85685af5f01695d5a3044cedae75427f953"
    },
    {
      "id": "approved-future",
      "kind": "positive",
      "input": "Future placement backed by act",
      "expect": "exclude before effective time; include after",
      "sha256": "0b8d34e4770856f4d516a9ef5edfeac4a99fbfa701bf2f9a4193985562603677"
    },
    {
      "id": "hypothetical-branch",
      "kind": "positive",
      "input": "To-be branch has explicit scenario",
      "expect": "planning read only",
      "sha256": "1c605008108e9b597fd87b6c8b663d25497d81e33bf73ba10e81b30f3c956e8e"
    },
    {
      "id": "hypothetical-current",
      "kind": "negative",
      "input": "Hypothetical edge appears in current read",
      "expect": "reject",
      "sha256": "150daac95e1f35bf0e59c35eecb8dbe0de4eccdc5cf6343aa3798113d3516ab9"
    },
    {
      "id": "team-as-unit",
      "kind": "negative",
      "input": "Product team forced under administrative parent",
      "expect": "reject; keep WM-ORG-003 affiliations",
      "sha256": "af4d657ea1d98634a2c61aa454a8612dd1bed3dd61ae8f2852d3fcbb987e72c7"
    },
    {
      "id": "explicit-dual-type",
      "kind": "positive",
      "input": "Standing body is explicitly both unit and team",
      "expect": "unit placement and team membership remain distinct",
      "sha256": "7883a4cf8fd670b51ab3d0542d7ee5a9041fd393b547340de3b5706f8910d1b5"
    },
    {
      "id": "management-employer",
      "kind": "negative",
      "input": "Administrative parent used as employer",
      "expect": "reject",
      "sha256": "6b4d230657010385a5aab23c8e15ee93fddd33f4a73e8c4167284a7194101cda"
    },
    {
      "id": "merge-lineage",
      "kind": "positive",
      "input": "Two units merge under approved act",
      "expect": "new or retained ID follows explicit continuity decision and lineage",
      "sha256": "989f15781cb393c3f360992c9069986924eeabca851fd6d5e2d9315acdbd41d8"
    },
    {
      "id": "split-lineage",
      "kind": "positive",
      "input": "Unit splits",
      "expect": "successor edges and apportioned mandates required",
      "sha256": "302c1fff57bad7f3ba70b40ea60246657706bdf6ca2ad4cf798659a5f240bd45"
    },
    {
      "id": "as-is-to-be",
      "kind": "positive",
      "input": "Current and approved-future graphs queried independently",
      "expect": "current remains uncontaminated and each graph validates separately",
      "sha256": "26804318c8c6348c540a760d5000d3079e29b1253b874e4709c06b9a0e59f9d0"
    }
  ]
}
```
