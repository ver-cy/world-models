# Frozen semantic audit: EM-PEO-01 Enterprise Person and Contextual Identity

You are the single independent frozen auditor. Use only the material below and no tools. Do not invent identifiers or external facts.

Required output:
1. Verdict ACCEPT or REVISE.
2. Confirm or reject restricted PROFILE over WM-PER-001 and no new identifier.
3. List every defect that could cause person/record/account collapse, mastership inversion, unsafe deterministic linkage, namesake merge, name-history loss, pseudonym correlation, contact-as-identity, privacy over-disclosure, history rewrite or unsupported release claims.
4. Give exact remediation and fixture expectation for every defect.
5. Identify contradictions.
6. End with a closed numbered remediation checklist.

## FROZEN DOSSIER
```json
{
  "contour": {
    "id": "EM-PEO-01",
    "name": "Человек и контекстная идентичность",
    "domain": "PEO",
    "kind": "subject",
    "wave": "W1",
    "scope": "Минимальная идентичность физического лица и допустимые контакты. Кадровые, клиентские и технические роли ссылаются на человека по договору раскрытия.",
    "candidate_types": [
      "Person",
      "NameForm",
      "ContactPoint",
      "IdentityEvidence"
    ],
    "specific_questions": [
      "Как отличить однофамильцев и не объединить людей по email?",
      "Когда псевдоним или локальный идентификатор достаточен?",
      "Как поддержать изменение имени без потери истории и избыточного раскрытия?"
    ],
    "proposed_invariants": [
      "Тождество требует доказательства",
      "Личные сведения раскрываются по цели",
      "Работодатель не становится владельцем всех сведений о человеке"
    ],
    "negative_case": "Два пользователя с одинаковым display name объединены автоматически.",
    "acceptance_scenario": "Три системы, два однофамильца и смена имени дают корректные bindings; неуверенное совпадение остаётся предложением.",
    "comparison_tracks": [
      "HR Open: обмен кадровыми данными",
      "W3C ORG и ESCO/SFIA: отношения, навыки и уровни ответственности",
      "Практика HRIS/ATS/LMS и независимая проверка измерения результатов через SPACE"
    ],
    "vercy_candidates": [
      {
        "model_id": "WM-PER-001",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "PEO-01",
        "fields": [
          {
            "name": "display_name",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "name_forms",
            "value_type": "localized_text",
            "status": "candidate-not-normative"
          },
          {
            "name": "identity_evidence",
            "value_type": "reference",
            "status": "candidate-not-normative"
          },
          {
            "name": "preferred_language",
            "value_type": "code",
            "status": "candidate-not-normative"
          }
        ]
      }
    ],
    "suggested_owner": "Руководитель HR / ответственный за персонал",
    "candidate_master_systems": "HRIS, кадровый реестр, ATS, LMS",
    "related_research_contours": [
      "EM-COM-01",
      "EM-LEG-01",
      "EM-ORG-03",
      "EM-ORG-05",
      "EM-PEO-02",
      "EM-PEO-03"
    ],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "queue": {
    "sequence": 34,
    "id": "EM-PEO-01",
    "status": "queued",
    "claude_status": "not-started",
    "grok_status": "not-started",
    "boundary_decision": "pending",
    "publication_urls": [],
    "remaining_scope": "Entire research brief pending",
    "target_model_ids": [
      "WM-PER-001"
    ]
  },
  "reservation": {
    "registry_id": "vr.wm-per-001",
    "record_plane": "world-model",
    "model_id": "WM-PER-001",
    "name": "Person",
    "alternate_names": "",
    "entry_kind": "standalone-mm",
    "origin": "grok-union-current",
    "status": "described-previous-version",
    "review_state": "migration-boundary-review",
    "nav_path": "NAV.SOC.PER.NAT",
    "domain_tags": "SOC.PER.NAT",
    "legacy_alias": "H1",
    "existing_spec_ref": "models/people-groups/H1-person.md",
    "parent_ids": "",
    "contains_ids": "",
    "aligned_model_ids": "",
    "purpose": "Natural person as a civil identity and life-course subject",
    "owner_or_maintainer": "civil registrar for the registered identity; the person as owner of personal data via S1",
    "source_url": "",
    "namespace_uri": "",
    "source_version_or_year": "2026-08-22",
    "source_group": "",
    "source_category": "",
    "source_format": "",
    "composition_role": "",
    "default_link_type": "",
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
    "relations_ref": "",
    "validation_flags": "гражданская идентичность, не организм",
    "provenance": "current-112 + Grok review + Claude adversarial audit"
  },
  "spec": {
    "bytes": 252757,
    "sha256": "7a4a71ddd69fdc31b37806958442d1cfca4ec0bf861e54578adb312e0d7a4df3",
    "publication": {
      "status": "published",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "generatedAt": "2026-08-23T20:43:15Z",
      "synthesisSha256": "ffefc6ce9cf9d7c6b9661c80834009180840f8da0a23e7409434e4c49c9472b2",
      "providerMode": "dual-provider",
      "providers": [
        "Claude",
        "Grok"
      ],
      "waivedProviders": []
    },
    "model": {
      "registry_id": "vr.wm-per-001",
      "model_id": "WM-PER-001",
      "name": "Person",
      "entry_kind": "entity",
      "purpose": "Model the natural person as a civil-identity anchor and life-course subject: a stable, referenceable identity that carries registered core attributes, scheme-qualified identifiers, evidence of identity, legal standing, life-event anchors and person-controlled personal-sphere data, so every other model can reference persons without copying them.",
      "scope_statement": "Format-neutral context structure for the natural person as a legally registered identity and data subject. Covers what an agent must know to establish, resolve, evidence, update, disclose, close and audit a person identity. Excludes the human as a biological organism, and excludes any concept that resolves in a composable sibling model (household, organization, address, vital-event record, qualification, authenticator).",
      "in_scope": [
        "Person identity anchor, reference identifier and domain of applicability",
        "Registered core attributes: legal names over time, birth facts, administratively recorded sex and legal gender recognition",
        "Scheme-qualified identifier assignments, their validity, revocation and correlation properties",
        "Identity evidence: issued documents and electronic attestations, their status and holder binding",
        "Identity proofing outcome and assurance level, including biometric reference pointers",
        "Civil status, nationality and statelessness determination",
        "Legal capacity state and representation or support arrangements",
        "Anchors to vital and registered life events, with event time separated from registration and ingestion time",
        "Vital status and identity-record lifecycle states",
        "Person-controlled contact points, declared residence pointer and self-declared attributes",
        "Lawful basis, consent grants, subject rights, minimal disclosure, retention, erasure and disclosure audit",
        "Attribute accuracy, duplicate detection, record merge/split and external schema alignment"
      ],
      "out_of_scope": [
        "The human biological organism: anatomy, physiology, genome, clinical findings and cause of death",
        "Household, family and kinship composition, including filiation ties as first-class objects",
        "Population, community and demographic group membership",
        "Educational, professional and occupational credentials as objects",
        "Organizations acting as issuers, employers or corporate guardians",
        "Address and place as spatial objects, geocoding and address validation",
        "The vital-event registration record itself and its statistical processing",
        "Party roles, employment, customer and account relationships",
        "Authenticators, sessions, keys and login security",
        "Cross-border private-international-law rules for recognising foreign status",
        "Behavioural profiling, scoring and inference about persons"
      ],
      "boundary_notes": [
        {
          "neighbor": "Human biological organism / health subject model",
          "distinction": "This model treats the person as a civil identity, not an organism. HL7 FHIR Patient covers care-context demographics and explicitly permits several Patient records for one human; the anchor here is one per natural person and reconciles to Patient records by link, not by absorbing them.",
          "source_refs": [
            "SRC-009",
            "SRC-002"
          ]
        },
        {
          "neighbor": "Household and family model (legacy alias H2)",
          "distinction": "Kinship, filiation and household membership are separate registered acts and separate statistical units in UN civil-registration guidance. Person holds only typed pointers to them, never the tie itself.",
          "source_refs": [
            "SRC-001",
            "SRC-017"
          ]
        },
        {
          "neighbor": "Vital-event / civil-registration act model",
          "distinction": "The registration act, its informant, its statistical coding and its certificate are the event model's content. Person holds the anchor, the person's role in the event and the resulting status change only.",
          "source_refs": [
            "SRC-001",
            "SRC-017"
          ]
        },
        {
          "neighbor": "Address and place model",
          "distinction": "Residence is a pointer with a kind and a validity period. Address value shapes come from OASIS xAL and place resolution from the place model; usual residence as a statistical construct belongs to the census/statistics model.",
          "source_refs": [
            "SRC-016",
            "SRC-004",
            "SRC-001"
          ]
        },
        {
          "neighbor": "Organization model (legacy alias O1)",
          "distinction": "Registrars, issuing authorities, credential issuers and corporate guardians are organizations. Person references them; it does not define them.",
          "source_refs": [
            "SRC-003",
            "SRC-004"
          ]
        },
        {
          "neighbor": "Credential and authenticator security model",
          "distinction": "NIST separates identity proofing and enrollment from authenticator management. This model carries the proofing outcome and assurance level; authenticator binding, lifecycle and session security are out of scope.",
          "source_refs": [
            "SRC-008"
          ]
        },
        {
          "neighbor": "Consent and authorization service (legacy alias S1) and audit service (S4)",
          "distinction": "Person declares which data is subject-owned and what must be logged; the grant store, policy decision point and audit trail are service-layer components composed in, not duplicated here.",
          "source_refs": [
            "SRC-011",
            "SRC-017"
          ]
        },
        {
          "neighbor": "Publication vocabularies (schema.org Person)",
          "distinction": "schema.org Person is an open publication vocabulary with no validity periods, no issuing authority and no assurance semantics. It is a projection target only and must never be treated as an identity-assurance signal.",
          "source_refs": [
            "SRC-010",
            "SRC-003"
          ]
        }
      ]
    },
    "findings": [
      {
        "id": "person-identity-anchor",
        "name": "Person identity anchor",
        "description": "The natural person as a persistent entity distinct from any record, identifier, document or credential about them, carrying the reference identifier every other model points to.",
        "questions": [
          "Which identifier is the reference identifier for this person, and which authority guarantees its persistence and non-reuse?",
          "Does this record denote the natural person, or a registration record about the person?",
          "Within which domain of applicability is this identity asserted unique and resolvable?",
          "If no authoritative master-system identifier exists for this person, which fallback identifier is assigned, by whom, and why was the authoritative one unavailable?"
        ],
        "data_elements": [
          {
            "id": "de-person-reference-identifier",
            "name": "Person reference identifier",
            "description": "The single identifier that persistently references this person within the declared domain of applicability.",
            "value_kind": "identifier",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-domain-of-applicability",
            "name": "Domain of applicability",
            "description": "The named domain within which the reference identifier is unique and the identity is meaningful.",
            "value_kind": "text",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-identifier-origin-class",
            "name": "Identifier origin class",
            "description": "Whether the reference identifier is an authoritative master-system identifier, a governed global identifier or a locally assigned surrogate.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "duplicate-detection-and-merge",
        "name": "Duplicate detection, merge and split",
        "description": "Several records may describe one person across systems; the model must express same-as links, merge, supersession and split without destroying history or silently unifying distinct people.",
        "questions": [
          "Which other person records are asserted to denote the same natural person, and with what link type and direction?",
          "What evidence and matching threshold justified this merge, and which role authorised it?",
          "How is an incorrect merge reversed, and what happens to identifiers and credentials issued under the superseded record?"
        ],
        "data_elements": [
          {
            "id": "de-record-link",
            "name": "Person record link",
            "description": "A typed assertion that another person record denotes the same natural person, with direction and asserting system.",
            "value_kind": "reference",
            "cardinality": "0..n",
            "required": false
          },
          {
            "id": "de-match-confidence",
            "name": "Match confidence",
            "description": "Quantified confidence that two records denote the same person, with the algorithm or rule set version.",
            "value_kind": "number",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-surviving-record-ref",
            "name": "Surviving master record reference",
            "description": "The record that remains authoritative after a merge; the superseded record remains resolvable as a tombstone.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "alternative-registration-routes",
        "name": "Exceptional identity paths",
        "description": "UN LIA explicitly covers persons whose birth was not registered and refugees whose proof of legal identity may be issued by the host State or an internationally mandated authority. Statelessness is a named UN LIA concern. National CRVS practice also includes foundlings, unknown parentage, incomplete dates, delayed registration and, in some jurisdictions, presumed death and later identity restoration. Those last national cases are recorded here as operating needs with incomplete global normative detail.",
        "questions": [
          "Is proof of legal identity issued by a host State or by an internationally mandated authority for a refugee or similar status, and how does it link to this person?",
          "Was this identity opened for a foundling or person of unknown parentage, and which placeholder name and birth facts were assigned?",
          "Has legal identity been retired by presumed death or later restored, and what is the current vital status?"
        ],
        "data_elements": [
          {
            "id": "alternative-registration-routes-data01",
            "name": "Proof of identity issuer kind",
            "description": "Host State versus internationally mandated authority for refugees.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "alternative-registration-routes-data02",
            "name": "Foundling or unknown parentage flag",
            "description": "Marks identities opened without ordinary parental birth facts.",
            "value_kind": "boolean",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "alternative-registration-routes-data03",
            "name": "Presumed-death order",
            "description": "National court or registrar instrument; global UN LIA text does not specify this path.",
            "value_kind": "identifier",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "legal-name-versioning",
        "name": "Legal name as a versioned structured fact",
        "description": "Legal name is a time-bounded, structured, script-bearing fact with an ordering convention, not a fixed string attribute of the person.",
        "questions": [
          "What are the structured parts of this name and which cultural convention orders and formats them?",
          "Over which validity period was this the person's legal name, and which instrument changed it?",
          "Is this a birth name, current legal name, former name or alias, and who may assert each?",
          "In which script and encoding is the name recorded, and which transliteration is authoritative for machine-readable use?"
        ],
        "data_elements": [
          {
            "id": "de-name-part",
            "name": "Name part",
            "description": "One structured component of a name with its role, value and sequence position under the declared ordering convention.",
            "value_kind": "object",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-name-role",
            "name": "Name role",
            "description": "Classifies the name as birth name, current legal name, former legal name or alias.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-name-validity-period",
            "name": "Name validity period",
            "description": "The period during which this name form was the person's legal name.",
            "value_kind": "object",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-name-script-code",
            "name": "Name script code",
            "description": "Writing system in which the name is recorded, distinguishing native-script and transliterated forms.",
            "value_kind": "code",
            "cardinality": "1..n",
            "required": false
          }
        ]
      },
      {
        "id": "birth-facts-record",
        "name": "Registered birth facts",
        "description": "Date, precision, place and, where recorded, time of birth as registered, plus multiple-birth order, distinguished from the place and date of registration.",
        "questions": [
          "What is the registered date of birth and at what precision is it known?",
          "What is the registered place of birth, at which administrative granularity, and does it differ from the place of registration?",
          "Was this birth part of a multiple birth, and what birth order was registered?",
          "Which registration act established these facts, and how must a correction to them be evidenced?"
        ],
        "data_elements": [
          {
            "id": "de-birth-date",
            "name": "Date of birth",
            "description": "Registered day, month and year of birth, held as a date rather than a timestamp.",
            "value_kind": "date",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-birth-date-precision",
            "name": "Birth date precision",
            "description": "Declared precision or estimation status of the birth date, required where full dates are unknown.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-birth-place-ref",
            "name": "Place of birth reference",
            "description": "Pointer to the place of birth resolved in the place model, with the recorded administrative granularity.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-multiple-birth-order",
            "name": "Multiple birth order",
            "description": "Birth order within a multiple delivery, where registered.",
            "value_kind": "number",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "sex-and-gender-recording",
        "name": "Sex and gender recording",
        "description": "Administratively recorded sex, legal gender recognition and self-identified gender are three distinct values with different code lists, owners and disclosure rules.",
        "questions": [
          "Which code list and version encodes the administratively recorded sex, and what does each value mean in that list?",
          "Is a self-identified gender recorded separately from administrative sex, and who controls that value?",
          "Has a legal gender recognition changed the registered value, and from which date does the change take effect?",
          "Which of these values may be disclosed to which relying-party class, given the sensitivity of gender data?"
        ],
        "data_elements": [
          {
            "id": "de-administrative-sex-code",
            "name": "Administrative sex code",
            "description": "Coded sex as recorded by the register, always accompanied by the code list reference and version.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-self-identified-gender",
            "name": "Self-identified gender",
            "description": "Gender as declared by the person, held in the personal sphere and carrying no registrar warranty.",
            "value_kind": "text",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-gender-recognition-effective-date",
            "name": "Gender recognition effective date",
            "description": "Date from which a legally recognised change of registered sex or gender takes effect.",
            "value_kind": "date",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "identifier-assignment",
        "name": "Scheme-qualified identifier assignment",
        "description": "An identifier attaches to the person under a named scheme with an assigning authority, validity period, format rule and reuse policy, without becoming the person.",
        "questions": [
          "Under which named scheme was this identifier assigned, and by which authority?",
          "What is the identifier's validity period, and may it be revoked, reissued or reused for a different person?",
          "Is this identifier a reference identifier for the person or a scoped, derived or sector-limited identifier?",
          "Which format, checksum or registry lookup validates this identifier value?"
        ],
        "data_elements": [
          {
            "id": "de-identifier-scheme",
            "name": "Identifier scheme name",
            "description": "The named scheme under which the identifier was issued, qualified by its governing authority.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-identifier-value-pointer",
            "name": "Identifier value pointer",
            "description": "Pointer to the identifier value, held so it can be withheld from projections that do not need it.",
            "value_kind": "identifier",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-identifier-reuse-policy",
            "name": "Identifier reuse policy",
            "description": "Whether the scheme permits reassignment of a retired identifier value to another person.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "identifier-correlation",
        "name": "Identifier correlation and pseudonymity",
        "description": "Cross-domain identifiers make a person correlatable across contexts; the model must record correlatability class and any pairwise or sector-specific pseudonym derivation.",
        "questions": [
          "Which of this person's identifiers are correlatable across domains, and what harm follows from that linkage?",
          "Where a pairwise or sector-specific pseudonym is required, how is it derived, scoped and rotated?",
          "Which identifiers may be omitted entirely from a given presentation without breaking verification?"
        ],
        "data_elements": [
          {
            "id": "de-correlatability-class",
            "name": "Identifier correlatability class",
            "description": "Classifies an identifier as globally correlatable, sector-scoped, pairwise or single-use.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-pseudonym-derivation",
            "name": "Pseudonym derivation method",
            "description": "Reference to the documented derivation and rotation method for scoped pseudonymous identifiers.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "issued-identity-evidence",
        "name": "Issued identity evidence",
        "description": "Physical documents and electronic attestations evidence a registered identity and assert a subset of attributes; they never constitute the person and their revocation does not revoke the person.",
        "questions": [
          "What type of evidence is this, who issued it, and over which validity period?",
          "What is its current status: valid, expired, suspended, revoked, lost or stolen, and where is that status published?",
          "Which person attributes does this evidence assert, and which of those are authoritative rather than copied from another source?",
          "How is the evidence bound to the holder, cryptographically or physically?"
        ],
        "data_elements": [
          {
            "id": "de-evidence-type",
            "name": "Evidence type",
            "description": "Kind of identity evidence, such as travel document, national identity card, civil extract or electronic attestation.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-evidence-status",
            "name": "Evidence status",
            "description": "Current lifecycle status of the evidence with its effective time and reason.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-asserted-attribute-set",
            "name": "Asserted attribute set",
            "description": "The person attributes this evidence carries, each flagged as authoritative or copied.",
            "value_kind": "collection",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-holder-binding-method",
            "name": "Holder binding method",
            "description": "How the evidence is bound to the person presenting it, for example portrait, biometric match or key-bound proof.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "identity-proofing-assurance",
        "name": "Identity proofing and assurance",
        "description": "The recorded outcome of resolving, validating and verifying a claimed identity against evidence, expressed as an assurance level with an expiry and an optional biometric reference.",
        "questions": [
          "At which identity assurance level was this person proofed, and against which published criteria and version?",
          "Which resolution, validation and verification steps were performed, and with what outcome for each?",
          "Which biometric reference, if any, was captured, in which encoding, and where is it stored?",
          "When does this proofing outcome expire or require re-proofing, and what event forces early re-proofing?"
        ],
        "data_elements": [
          {
            "id": "de-assurance-level",
            "name": "Identity assurance level",
            "description": "Assurance level attained by the proofing process, qualified by the criteria set that defines it.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-proofing-step-outcome",
            "name": "Proofing step outcome",
            "description": "Per-step record of resolution, validation and verification with evidence used and result.",
            "value_kind": "collection",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-biometric-reference-ref",
            "name": "Biometric reference pointer",
            "description": "Pointer to a stored biometric reference and its encoding standard; the biometric data itself is never inlined.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "civil-status-registration",
        "name": "Registered civil status",
        "description": "One current registered civil status per person with an effective date and governing jurisdiction; history is carried by the acts that changed it, not by overwriting the value.",
        "questions": [
          "What is the currently registered civil status, from which effective date, and under which jurisdiction's law?",
          "Which registered act caused the most recent change of civil status?",
          "How is a civil status established under foreign law recognised here, and what evidence is required?"
        ],
        "data_elements": [
          {
            "id": "de-civil-status-code",
            "name": "Civil status code",
            "description": "Registered civil or marital status value, qualified by the national code list it comes from.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-civil-status-effective-date",
            "name": "Civil status effective date",
            "description": "Date from which the current civil status took legal effect, distinct from its registration date.",
            "value_kind": "date",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-civil-status-jurisdiction",
            "name": "Governing jurisdiction",
            "description": "Jurisdiction whose law governs the meaning and effects of the recorded status.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "nationality-holding",
        "name": "Nationality holding",
        "description": "Zero, one or several nationalities held by the person, each with a coding, acquisition basis, dates and conferring authority.",
        "questions": [
          "Which nationalities does the person hold, in which coding scheme, and from which dates?",
          "Which authority conferred or withdrew each nationality, and on what legal basis?",
          "Where several nationalities are held, which one governs a given official interaction?"
        ],
        "data_elements": [
          {
            "id": "de-nationality-code",
            "name": "Nationality code",
            "description": "Country code identifying a nationality held, with the coding scheme and version stated.",
            "value_kind": "code",
            "cardinality": "0..n",
            "required": false
          },
          {
            "id": "de-nationality-basis",
            "name": "Nationality acquisition basis",
            "description": "Legal ground on which the nationality was acquired or withdrawn.",
            "value_kind": "code",
            "cardinality": "0..n",
            "required": false
          }
        ]
      },
      {
        "id": "statelessness-determination",
        "name": "Statelessness and undetermined nationality",
        "description": "Determined statelessness, undetermined nationality and simply unrecorded nationality are three different states with different consequences for document issuance.",
        "questions": [
          "Is the person determined stateless, of undetermined nationality, or is nationality merely unrecorded?",
          "Which authority made the determination, when, and under which procedure?",
          "Which substitute documents or registration routes establish legal identity where no nationality-based document exists?"
        ],
        "data_elements": [
          {
            "id": "de-nationality-determination-status",
            "name": "Nationality determination status",
            "description": "Explicit status distinguishing determined statelessness, undetermined nationality and unrecorded nationality.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-substitute-document-ref",
            "name": "Substitute identity document reference",
            "description": "Pointer to a document issued in place of a nationality-based identity document.",
            "value_kind": "reference",
            "cardinality": "0..n",
            "required": false
          }
        ]
      },
      {
        "id": "legal-capacity-state",
        "name": "Legal capacity state",
        "description": "Capacity is a time-bounded, domain-scoped legal state established by a legal act, with equal recognition before the law as the default and restriction as the evidenced exception.",
        "questions": [
          "What is the person's legal capacity state, over which effective period, and for which domains of action?",
          "Which legal act or judgment established, restricted or restored capacity?",
          "Is any restriction general or limited to specified matters, and when is it reviewed?"
        ],
        "data_elements": [
          {
            "id": "de-capacity-class",
            "name": "Capacity class",
            "description": "Coded legal capacity state, defaulting to full capacity where no restricting act exists.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-capacity-scope",
            "name": "Capacity restriction scope",
            "description": "Enumerated domains of action to which a restriction applies; empty means unrestricted.",
            "value_kind": "collection",
            "cardinality": "0..n",
            "required": false
          },
          {
            "id": "de-capacity-effective-period",
            "name": "Capacity effective period",
            "description": "Period during which the recorded capacity state applies, with review date where required.",
            "value_kind": "object",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "representation-arrangement",
        "name": "Representation and support arrangement",
        "description": "An arrangement by which a person or organization supports or acts for the person, distinguishing supported from substituted decision-making and recording the person's own will and preferences.",
        "questions": [
          "Who acts for or supports the person, in which capacity, and with what scope of authority?",
          "Is the arrangement supported decision-making or substituted decision-making, and how is that recorded?",
          "When does the arrangement start, end or require renewal, and who may terminate it?",
          "How are the person's own expressed will and preferences recorded alongside the representative's acts?"
        ],
        "data_elements": [
          {
            "id": "de-representative-ref",
            "name": "Representative reference",
            "description": "Pointer to the representing or supporting party, resolved in the person or organization model.",
            "value_kind": "reference",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-representation-type",
            "name": "Representation type",
            "description": "Whether the arrangement is supported or substituted decision-making.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-authority-scope",
            "name": "Scope of representative authority",
            "description": "Enumerated matters over which the representative may act.",
            "value_kind": "collection",
            "cardinality": "1..n",
            "required": true
          }
        ]
      },
      {
        "id": "life-event-anchor",
        "name": "Vital and registered life event anchor",
        "description": "The person carries typed anchors to life events resolved in the vital-event model, together with the role the person played in each event.",
        "questions": [
          "Which vital or registered life events anchor to this person, and in which model does each event resolve?",
          "What role does the person play in each anchored event: subject, parent, spouse, informant or declarant?",
          "Which anchors are mandatory for a complete civil identity in this jurisdiction, and which are optional?"
        ],
        "data_elements": [
          {
            "id": "de-event-anchor-ref",
            "name": "Life event anchor reference",
            "description": "Typed pointer to a registered event record held in the vital-event model.",
            "value_kind": "reference",
            "cardinality": "0..n",
            "required": false
          },
          {
            "id": "de-person-role-in-event",
            "name": "Person role in event",
            "description": "The capacity in which the person participates in the anchored event.",
            "value_kind": "code",
            "cardinality": "0..n",
            "required": false
          }
        ]
      },
      {
        "id": "event-time-versus-record-time",
        "name": "Occurrence time versus record time",
        "description": "Every person fact carries a time of occurrence, a time of registration and a time of ingestion; conflating them corrupts history and prevents lawful correction.",
        "questions": [
          "What are the occurrence time, the registration time and the ingestion time for this fact, and are they stored separately?",
          "Which values carry an explicit UTC offset or Z, and which are deliberately dates without a time zone?",
          "How are late, retroactive or back-dated registrations represented without rewriting existing history?",
          "Which time value governs when two sources disagree about when a fact took effect?"
        ],
        "data_elements": [
          {
            "id": "de-occurrence-time",
            "name": "Occurrence time",
            "description": "When the fact actually happened, as a date or an RFC 3339 timestamp with explicit offset, with precision stated.",
            "value_kind": "timestamp",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-registration-time",
            "name": "Registration time",
            "description": "When the authority registered the fact, as an RFC 3339 timestamp with explicit offset.",
            "value_kind": "timestamp",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-ingestion-time",
            "name": "Observation or ingestion time",
            "description": "When this system observed or ingested the assertion, recorded separately from occurrence and registration.",
            "value_kind": "timestamp",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-effective-period",
            "name": "Assertion effective period",
            "description": "The period during which the asserted value is held to be true, enabling supersession without deletion.",
            "value_kind": "object",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "vital-status-and-death",
        "name": "Vital status and death registration",
        "description": "Vital status is an evidenced state; registered death, judicially declared death and presumed death are distinct and must not be collapsed.",
        "questions": [
          "What is the person's current vital status and what evidence supports it?",
          "For a registered death, what are the date, time and place of death, and how do they differ from the date and place of registration?",
          "How is a presumed or judicially declared death represented differently from a registered death?",
          "Which downstream references, identifiers and credentials must be notified or closed when death is registered?"
        ],
        "data_elements": [
          {
            "id": "de-vital-status-code",
            "name": "Vital status code",
            "description": "Living, deceased, presumed deceased or unknown, with the evidence basis recorded.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-death-date",
            "name": "Date of death",
            "description": "Registered date of death, held separately from the date of death registration.",
            "value_kind": "date",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-death-determination-basis",
            "name": "Death determination basis",
            "description": "Whether death was medically certified, judicially declared or presumed, with the deciding authority.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "identity-record-lifecycle",
        "name": "Identity record lifecycle state",
        "description": "The identity record moves through governed states such as established, active, suspended and archived; transitions carry an authority, a reason and a timestamp.",
        "questions": [
          "Which lifecycle state is the identity record in, and which published state vocabulary defines it?",
          "Who may suspend, reactivate or archive an identity record, and on which grounds?",
          "After archiving, what remains resolvable and what is destroyed?"
        ],
        "data_elements": [
          {
            "id": "de-record-lifecycle-state",
            "name": "Identity record lifecycle state",
            "description": "Current governed state of the identity record, bound to the adopting Dimension's published state vocabulary.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-state-transition-authority",
            "name": "State transition authority",
            "description": "Role or authority that executed the most recent lifecycle transition, with the recorded reason.",
            "value_kind": "reference",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "person-controlled-contact-point",
        "name": "Person-controlled contact point",
        "description": "A channel through which the person can be reached, owned and revocable by the person, with a verification state and per-purpose usage limits.",
        "questions": [
          "What channel type and value does this contact point use, and has the value been verified?",
          "Who controls this contact point and for which purposes may it be used?",
          "What visibility or disclosure setting applies, and can it differ per relying party?"
        ],
        "data_elements": [
          {
            "id": "de-channel-type",
            "name": "Contact channel type",
            "description": "The kind of channel, such as email, telephone, postal or messaging endpoint.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-contact-verification-state",
            "name": "Contact verification state",
            "description": "Whether the contact value has been proven reachable and controlled by the person.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-contact-purpose-limitation",
            "name": "Contact purpose limitation",
            "description": "Enumerated purposes for which this contact point may be used.",
            "value_kind": "collection",
            "cardinality": "0..n",
            "required": false
          }
        ]
      },
      {
        "id": "declared-residence-pointer",
        "name": "Declared residence pointer",
        "description": "A typed pointer to an address resolved in the place model, distinguishing legal domicile, registered residence and self-declared mailing address from statistical usual residence.",
        "questions": [
          "Which address does the person declare or stand registered at, and in which model does that address resolve?",
          "Is this a legal domicile, a registered residence or a self-declared mailing address?",
          "Over which period was it valid and who may change it?"
        ],
        "data_elements": [
          {
            "id": "de-residence-address-ref",
            "name": "Residence address reference",
            "description": "Pointer to an address object held in the place or address model; address components are not duplicated here.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-residence-kind",
            "name": "Residence kind",
            "description": "Legal domicile, registered residence or self-declared mailing address.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "self-declared-attributes",
        "name": "Self-declared attributes and preferences",
        "description": "Values supplied solely by the person, including communication and accessibility preferences, carrying no registrar warranty and always distinguishable from verified values in any projection.",
        "questions": [
          "Which attributes are declared solely by the person and carry no authority warranty?",
          "Which language and communication preferences apply, including accessible formats the person requires?",
          "How is a self-declared value distinguished from an authority-verified value in every projection that carries it?",
          "Which self-declared values may the person unilaterally change, hide or delete?"
        ],
        "data_elements": [
          {
            "id": "de-self-declared-attribute",
            "name": "Self-declared attribute",
            "description": "A person-supplied name-value assertion with declaration time and no registrar warranty.",
            "value_kind": "object",
            "cardinality": "0..n",
            "required": false
          },
          {
            "id": "de-attribute-assurance-flag",
            "name": "Attribute assurance flag",
            "description": "Marks each attribute as self-declared, third-party asserted or authority-verified.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-preferred-language-code",
            "name": "Preferred language code",
            "description": "Language the person prefers for communication, with preference ranking.",
            "value_kind": "code",
            "cardinality": "0..n",
            "required": false
          },
          {
            "id": "de-accessible-format-need",
            "name": "Accessible format need",
            "description": "Format or assistance the person requires to receive and act on communications.",
            "value_kind": "code",
            "cardinality": "0..n",
            "required": false
          }
        ]
      },
      {
        "id": "lawful-basis-and-consent",
        "name": "Lawful basis and consent grant",
        "description": "Each processing purpose is bound to a lawful basis; consent-based purposes carry a scoped, withdrawable grant, while statutory registration processing is not consent-dependent.",
        "questions": [
          "What is the lawful basis for each declared processing purpose over this person's data?",
          "Where consent is the basis, what is its exact scope, and how are withdrawal and its propagation recorded?",
          "Which processing is mandated by registration law and therefore cannot be refused by withdrawing consent?"
        ],
        "data_elements": [
          {
            "id": "de-processing-purpose",
            "name": "Processing purpose",
            "description": "A declared, specific purpose for which person data is processed.",
            "value_kind": "text",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-lawful-basis-code",
            "name": "Lawful basis code",
            "description": "The legal ground permitting processing for a given purpose.",
            "value_kind": "code",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-consent-grant-ref",
            "name": "Consent grant reference",
            "description": "Pointer to a scoped grant held by the consent service, with validity and withdrawal state.",
            "value_kind": "reference",
            "cardinality": "0..n",
            "required": false
          }
        ]
      },
      {
        "id": "subject-rights-execution",
        "name": "Subject right execution",
        "description": "How access, rectification, erasure, restriction, portability and objection requests are received, decided, executed and evidenced, including lawful refusal.",
        "questions": [
          "Which right was exercised, when, by whom, and with what outcome?",
          "Which data can the person rectify directly and which requires a registrar act?",
          "Which records are exportable in a portable form and which are excluded, and why?",
          "What lawful grounds justify refusing, restricting or deferring a request?"
        ],
        "data_elements": [
          {
            "id": "de-right-request-type",
            "name": "Subject right request type",
            "description": "Which right is being exercised over the person's data.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-right-decision-outcome",
            "name": "Request decision outcome",
            "description": "Granted, partially granted, refused or deferred, with the ground recorded.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true
          },
          {
            "id": "de-requester-verification",
            "name": "Requester verification evidence",
            "description": "How the requesting party's entitlement to act was verified, including representative mandates.",
            "value_kind": "reference",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "minimal-disclosure-projection",
        "name": "Minimal disclosure projection",
        "description": "Each relying party receives the narrowest projection satisfying its stated need, preferring a derived predicate over the underlying attribute, with special-category data excluded by default.",
        "questions": [
          "What is the minimum attribute set that satisfies this relying party's stated need?",
          "Can the need be met by a derived predicate instead of the underlying attribute?",
          "Which requested attributes fall into a special category requiring a stricter condition before release?",
          "Which projection is released for statutory public-record requests, and what does it deliberately omit?"
        ],
        "data_elements": [
          {
            "id": "de-released-attribute-set",
            "name": "Released attribute set",
            "description": "The attributes actually released in a disclosure, recorded per disclosure event.",
            "value_kind": "collection",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-predicate-assertion",
            "name": "Predicate assertion",
            "description": "A derived boolean claim released instead of an underlying attribute, such as an age threshold.",
            "value_kind": "boolean",
            "cardinality": "0..n",
            "required": false
          },
          {
            "id": "de-special-category-flag",
            "name": "Special category flag",
            "description": "Marks an attribute as belonging to a legally defined special category of personal data.",
            "value_kind": "boolean",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "retention-erasure-and-audit",
        "name": "Retention, erasure and disclosure audit",
        "description": "Retention classes and periods, the tension between permanent vital records and erasure rights, the method by which deletion is demonstrated, and what every disclosure must log.",
        "questions": [
          "How long must each class of person data be retained, and under whose mandate?",
          "Which data is subject to erasure on request and which is exempt because a legal obligation requires permanent retention?",
          "What is logged for every disclosure, and for how long is the log itself retained?",
          "How is deletion demonstrated: physical destruction, cryptographic erasure or de-identification?"
        ],
        "data_elements": [
          {
            "id": "de-retention-class",
            "name": "Retention class",
            "description": "Grouping of person data elements that share a retention rule and mandate.",
            "value_kind": "code",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-retention-period",
            "name": "Retention period",
            "description": "Duration for which a retention class must be kept, with the trigger that starts it.",
            "value_kind": "duration",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-deletion-method",
            "name": "Deletion method",
            "description": "How data was removed: destruction, cryptographic erasure or de-identification.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false
          }
        ]
      },
      {
        "id": "attribute-accuracy-and-correction",
        "name": "Attribute accuracy and correction",
        "description": "Every core attribute carries a source and last-verified time; corrections supersede rather than overwrite, and population-level quality is measured.",
        "questions": [
          "What is the source and last-verified time of each core attribute?",
          "What triggers a correction, and which authority may make it in the register of record?",
          "How are erroneous historical values retained for audit while no longer being presented as current?",
          "Which quality indicators are measured over the person population and against what target?"
        ],
        "data_elements": [
          {
            "id": "de-attribute-source-ref",
            "name": "Attribute source reference",
            "description": "Pointer to the system or act that is the source of record for an attribute value.",
            "value_kind": "reference",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-last-verified-time",
            "name": "Last verified time",
            "description": "RFC 3339 timestamp of the most recent verification of the attribute against its source.",
            "value_kind": "timestamp",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-quality-indicator",
            "name": "Population quality indicator",
            "description": "Measured indicator such as completeness, timeliness of registration or duplication rate.",
            "value_kind": "number",
            "cardinality": "0..n",
            "required": false
          }
        ]
      },
      {
        "id": "external-schema-alignment",
        "name": "External schema alignment",
        "description": "Alignments to external vocabularies are versioned, explicitly lossy where relevant, and are mappings until conformance evidence exists.",
        "questions": [
          "Which external vocabulary or credential schema is this projection aligned to, at which version?",
          "Which parts of the alignment are lossy, and which fields have no counterpart in the target?",
          "Where two aligned standards conflict on the same concept, which one governs here and why?",
          "Is this alignment a claim of conformance or only a mapping, and what evidence supports the claim?"
        ],
        "data_elements": [
          {
            "id": "de-alignment-target-ref",
            "name": "Alignment target reference",
            "description": "Identifies the external vocabulary, schema or code list this model is mapped to.",
            "value_kind": "reference",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-alignment-version",
            "name": "Alignment target version",
            "description": "Exact version or release date of the target that the mapping was made against.",
            "value_kind": "text",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-conformance-claim-flag",
            "name": "Conformance claim flag",
            "description": "False by default; true only where retrievable conformance evidence exists.",
            "value_kind": "boolean",
            "cardinality": "1",
            "required": true
          }
        ]
      },
      {
        "id": "script-and-transliteration",
        "name": "Script, encoding and transliteration",
        "description": "Names exist in native script, transliterated and machine-readable truncated forms; each form must be identified, rule-bound and reconcilable to the registered name.",
        "questions": [
          "In which script and character encoding is each name form recorded, and which form is the registered original?",
          "Which transliteration rule set produced the machine-readable form, and is the transformation reversible?",
          "How are truncated machine-readable forms reconciled with the full registered name?"
        ],
        "data_elements": [
          {
            "id": "de-name-form-script",
            "name": "Name form script and encoding",
            "description": "Script and character encoding of a specific recorded name form.",
            "value_kind": "code",
            "cardinality": "1..n",
            "required": true
          },
          {
            "id": "de-transliteration-rule-ref",
            "name": "Transliteration rule set reference",
            "description": "The published rule set used to derive a transliterated or machine-readable name form.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false
          },
          {
            "id": "de-truncation-flag",
            "name": "Truncation flag",
            "description": "Indicates that a machine-readable name form was truncated to fit a fixed-length field.",
            "value_kind": "boolean",
            "cardinality": "0..1",
            "required": false
          }
        ]
      }
    ],
    "functions": [
      {
        "id": "resolve-person-reference",
        "name": "Resolve person reference",
        "description": "Resolve a set of candidate identifiers and attributes to a single person reference identifier within a declared domain of applicability, or report non-resolution."
      },
      {
        "id": "register-person-identity",
        "name": "Register person identity",
        "description": "Establish a new person anchor from a civil registration act, or from a recorded exception route where no registration act exists."
      },
      {
        "id": "record-name-change",
        "name": "Record name change",
        "description": "Add a new time-bounded legal name assertion and close the validity of the prior one without deleting it."
      },
      {
        "id": "assign-scheme-identifier",
        "name": "Assign scheme-qualified identifier",
        "description": "Record an identifier issued to the person under a named scheme with authority, validity, reuse policy and correlatability class."
      },
      {
        "id": "record-identity-evidence",
        "name": "Record identity evidence",
        "description": "Register an issued document or electronic attestation as evidence about the person, with issuer, validity, asserted attributes, holder binding and status source."
      },
      {
        "id": "assess-identity-assurance",
        "name": "Assess identity assurance",
        "description": "Run and record resolution, validation and verification against collected evidence and emit an assurance level with an expiry."
      },
      {
        "id": "anchor-life-event",
        "name": "Anchor life event",
        "description": "Attach a typed anchor to a registered life event resolved in the vital-event model, recording the person's role and the three time values."
      },
      {
        "id": "record-legal-standing-change",
        "name": "Record legal standing change",
        "description": "Record a change of civil status, nationality, statelessness determination, legal capacity or representation arrangement with its authority and effective period."
      },
      {
        "id": "close-identity-on-death",
        "name": "Close identity on death",
        "description": "Record registered, judicially declared or presumed death, transition the identity record lifecycle state and drive downstream closure."
      },
      {
        "id": "merge-or-split-person-records",
        "name": "Merge or split person records",
        "description": "Apply a same-as, merge or split decision across person records, preserving both records' histories and keeping superseded identifiers resolvable."
      },
      {
        "id": "emit-minimal-disclosure",
        "name": "Emit minimal disclosure projection",
        "description": "Produce the narrowest attribute projection or derived predicate that satisfies a relying party's stated need, and log the disclosure."
      },
      {
        "id": "execute-subject-right-request",
        "name": "Execute subject right request",
        "description": "Intake, verify, decide and execute an access, rectification, erasure, restriction, portability or objection request, including lawful refusal."
      },
      {
        "id": "apply-retention-decision",
        "name": "Apply retention or erasure decision",
        "description": "Evaluate a retention class against its schedule and legal obligations, then retain, suppress, de-identify or destroy, and evidence the outcome."
      },
      {
        "id": "record-evidence-status-change",
        "name": "Revoke identity document",
        "description": "Invalidate a document before expiry and record revocation time, authority and reason."
      }
    ],
    "composition": [
      {
        "target": "Household and family membership model (sibling; legacy alias H2)",
        "relation": "REFERENCE",
        "purpose": "Household membership, filiation and kinship ties are separate registered acts and separate statistical units; Person holds only typed pointers to them.",
        "required": false,
        "source_refs": [
          "SRC-001",
          "SRC-017"
        ]
      },
      {
        "target": "Population and community group model (sibling; legacy alias H3)",
        "relation": "REFERENCE",
        "purpose": "Group and community membership resolves against the person reference identifier and is never stored as a person attribute, particularly where it would reveal special-category data.",
        "required": false,
        "source_refs": [
          "SRC-011",
          "SRC-012"
        ]
      },
      {
        "target": "Education and qualification model (sibling; legacy alias H4)",
        "relation": "REFERENCE",
        "purpose": "Earned credentials anchor to the person as holder; credential content and awarding rules live in the qualification model.",
        "required": false,
        "source_refs": [
          "SRC-010",
          "SRC-006"
        ]
      },
      {
        "target": "Organization model (sibling; legacy alias O1)",
        "relation": "REFERENCE",
        "purpose": "Registrars, issuing authorities, credential issuers, verifiers and corporate guardians must resolve as organizations rather than being described inside Person.",
        "required": true,
        "source_refs": [
          "SRC-003",
          "SRC-004",
          "SRC-006"
        ]
      },
      {
        "target": "Address and place model (sibling)",
        "relation": "REFERENCE",
        "purpose": "Places of birth, death and residence resolve as place or address objects; Person stores pointers plus a residence kind and validity period.",
        "required": true,
        "source_refs": [
          "SRC-004",
          "SRC-001"
        ]
      },
      {
        "target": "Vital event and civil registration act model (sibling)",
        "relation": "REFERENCE",
        "purpose": "The registration act, informant details, certificate issuance and statistical coding belong to the event model; Person keeps anchors, roles and resulting status changes.",
        "required": true,
        "source_refs": [
          "SRC-001",
          "SRC-017"
        ]
      },
      {
        "target": "Human biological organism and health subject model (sibling)",
        "relation": "REFERENCE",
        "purpose": "Explicit boundary: physiology, clinical findings, cause of death and genomic data are excluded here and must be reached only through a governed reference.",
        "required": false,
        "source_refs": [
          "SRC-009",
          "SRC-011"
        ]
      },
      {
        "target": "Consent and authorization service (legacy alias S1)",
        "relation": "COMPOSE",
        "purpose": "Grants, scopes, withdrawal and policy decisions over person data are executed by the consent service; Person declares what is subject-owned and which purposes exist.",
        "required": true,
        "source_refs": [
          "SRC-011",
          "SRC-017"
        ]
      },
      {
        "target": "Audit and evidence service (legacy alias S4)",
        "relation": "COMPOSE",
        "purpose": "Disclosure logs, lifecycle transition logs and correction records are written to the audit service so the person and oversight authorities can read them.",
        "required": true,
        "source_refs": [
          "SRC-017",
          "SRC-011"
        ]
      },
      {
        "target": "ISO/IEC 24760-1:2025 identity management framework",
        "relation": "ALIGN",
        "purpose": "Adopt the entity/identity/identifier/reference-identifier distinction and identity-register and relying-party roles as the model's conceptual vocabulary; the exact lifecycle state list must be bound to a published Dimension vocabulary.",
        "required": false,
        "source_refs": [
          "SRC-003"
        ]
      },
      {
        "target": "Core Person Vocabulary 2.00 (SEMIC)",
        "relation": "ALIGN",
        "purpose": "Map name components, birth and death facts, citizenship, domicile and the Identifier class with scheme, issuing authority and issue date.",
        "required": false,
        "source_refs": [
          "SRC-004"
        ]
      },
      {
        "target": "EUDI Wallet PID Rulebook (ARF Annex 3.01)",
        "relation": "ALIGN",
        "purpose": "Map the person identification data attribute set for wallet-based presentation, including predicate attributes such as age_over_18 and the issuer-defined personal administrative number policy.",
        "required": false,
        "source_refs": [
          "SRC-005"
        ]
      },
      {
        "target": "W3C Verifiable Credentials Data Model v2.0",
        "relation": "ALIGN",
        "purpose": "Express identity evidence as credentials with issuer, subject, validity window, status and proof, and use presentations for selective disclosure.",
        "required": false,
        "source_refs": [
          "SRC-006"
        ]
      },
      {
        "target": "W3C Decentralized Identifiers v1.0",
        "relation": "ALIGN",
        "purpose": "Provide the governed global identifier option at identity-priority level two, with documented correlation risk and controller-versus-subject separation.",
        "required": false,
        "source_refs": [
          "SRC-007"
        ]
      },
      {
        "target": "NIST SP 800-63A-4 identity proofing and enrollment",
        "relation": "ALIGN",
        "purpose": "Adopt resolution, validation and verification as recorded proofing steps producing an assurance level, while keeping authenticator management outside this model.",
        "required": false,
        "source_refs": [
          "SRC-008"
        ]
      },
      {
        "target": "HL7 FHIR R5 Patient",
        "relation": "ALIGN",
        "purpose": "Map to care-context demographics and reconcile the one-anchor-per-person rule with FHIR's multiple Patient records via link semantics rather than merge.",
        "required": false,
        "source_refs": [
          "SRC-009"
        ]
      },
      {
        "target": "schema.org Person",
        "relation": "ALIGN",
        "purpose": "Provide a lossy public publication projection only; no validity periods, authority or assurance semantics may be inferred from it.",
        "required": false,
        "source_refs": [
          "SRC-010"
        ]
      },
      {
        "target": "OASIS CIQ v3.0 xNL and xAL value shapes",
        "relation": "MIX-IN",
        "purpose": "Reuse structured, culture-aware name and address value shapes instead of re-inventing name part roles and ordering conventions.",
        "required": false,
        "source_refs": [
          "SRC-016"
        ]
      },
      {
        "target": "ISO/IEC 5218:2022 codes for the representation of human sexes",
        "relation": "ALIGN",
        "purpose": "Bind the administrative sex code list, noting the standard's explicit exclusion of gender identity, which forces separate modelling of self-identified gender.",
        "required": false,
        "source_refs": [
          "SRC-013",
          "SRC-005"
        ]
      },
      {
        "target": "ICAO Doc 9303 Part 3 (Eighth Edition, 2021)",
        "relation": "ALIGN",
        "purpose": "Bind machine-readable-zone name transliteration, truncation behaviour and biometric image encoding used by travel-document evidence.",
        "required": false,
        "source_refs": [
          "SRC-014"
        ]
      },
      {
        "target": "Regulation (EU) 2016/679 (GDPR)",
        "relation": "ALIGN",
        "purpose": "Regional legal alignment for lawful basis, special categories, accuracy, storage limitation and subject rights; other jurisdictions require their own binding.",
        "required": false,
        "source_refs": [
          "SRC-011",
          "SRC-012"
        ]
      }
    ],
    "adjudication": {
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
        "rationale": "Both providers independently resolved WM-PER-001 as an entity and both drew the same outer line: the natural person as a civil-identity subject, with the biological organism, household/filiation, organisational roles and location master data resolved in sibling models, and documents/identifiers treated as evidence rather than as the person. Claude's boundary is adopted because it names each neighbour with a stated distinction and source refs (FHIR Patient, household, vital-event act, address/place, organization, authenticator security, consent/audit services, schema.org projection) and separates the record plane from the entity plane. Grok's explicit exclusions of legal persons, devices and fictional/undead characters are folded into the base boundary prose as clarifying text, not as new structure."
      },
      "decisions": [
        {
          "concept": "Base provider selection",
          "disposition": "Claude as base",
          "rationale": "Chosen on boundary clarity, not size: eight neighbour-by-neighbour boundary notes with source refs, complete in/out-of-scope lists, an explicit record-plane versus entity-plane split, and adversarial checks that individually tested household absorption, document-as-identity, national-identifier-as-primary-key and schema.org-as-canonical. Grok's boundary is compatible but coarser and leaves quality, interoperability and disclosure concerns folded into a single governance bundle."
        },
        {
          "concept": "Entry kind",
          "disposition": "Accepted as entity",
          "rationale": "Both providers independently returned entity with matching subject framing (a referenceable civil-identity subject other models point at), so no reclassification, split or merge of the registry entry is warranted before nodes are accepted."
        },
        {
          "concept": "Alternative registration routes (refugee, host-State, mandated authority, delayed conferral)",
          "disposition": "Accepted into identity-anchor",
          "rationale": "The only grok finding that is materially absent from the base, evidence-backed in UN LIA and the UN CRVS-IdM handbook, and separable without restating an existing base finding. The base explicitly listed this as a likely missing finding."
        },
        {
          "concept": "Evidence status change / document revocation operation",
          "disposition": "Accepted as a renamed function",
          "rationale": "Fills a real operational gap: the base models evidence status as a question but never transitions it. Renamed to keep issuance and revocation attributed to the issuing authority, consistent with the base's organization boundary note."
        },
        {
          "concept": "Citizenship as a jurisdiction tie versus nationality as document encoding",
          "disposition": "Rejected as an addition, deferred as research",
          "rationale": "Grok's citizenship-ties would sit beside nationality-holding and statelessness-determination in the same layer while restating holding, conferring authority, dates and stateless/refugee status. The genuine delta is terminological (CPV citizenship as a Jurisdiction relationship versus ICAO nationality encoding), which belongs in the existing finding's text once primary wording is verified, not in a third overlapping node."
        },
        {
          "concept": "Contact, domicile and residency as one finding",
          "disposition": "Rejected as an addition, residency delta deferred",
          "rationale": "Two thirds of grok's contact-domicile-residency duplicates the base findings person-controlled-contact-point and declared-residence-pointer. The only new content is residency as a tie to a jurisdiction (habitual residence) rather than a pointer to an address, which should extend the existing residence finding rather than create a duplicate node."
        },
        {
          "concept": "Minority, age of majority and child consent",
          "disposition": "Rejected as an import, deferred as a dedicated finding",
          "rationale": "Grok carries GDPR Article 8 child consent and age-of-majority rules only inside a combined capacity-and-representation finding that duplicates the base's legal-capacity-state and representation-arrangement. The base separately flags child-specific protections as a likely addition, so this is queued as its own research task instead of imported as overlapping structure."
        },
        {
          "concept": "Identity conferral and retirement as a distinct finding",
          "disposition": "Rejected as duplicative",
          "rationale": "Grok's identity-create-and-retire is covered by the base's birth-facts-record, vital-status-and-death, identity-record-lifecycle and the register-person-identity and close-identity-on-death functions. Its unique value is normative grounding (CRC Article 7, ICCPR Article 24(2), SDG 16.9), which is a citation improvement to existing nodes, not new structure."
        },
        {
          "concept": "Document sex field versus civil-register marker",
          "disposition": "Rejected as duplicative",
          "rationale": "The base already governs three distinct values (administrative sex, legal gender recognition, self-identified gender) and handles document divergence generically through q-evid-attributes, which asks which evidence-asserted attributes are authoritative rather than copied. The ICAO M/F/X value set is a code-list binding for the existing finding."
        },
        {
          "concept": "eIDAS pairwise identifier matching constraint",
          "disposition": "Rejected as an addition, retained as a constraint",
          "rationale": "The base's identifier-correlation covers pairwise and sector-specific pseudonym derivation and omission, and duplicate-detection-and-merge covers matching evidence and thresholds. Grok's rule that an eIDAS unique identifier must not be assumed equal to a national personal number tightens those existing nodes rather than justifying a new finding."
        },
        {
          "concept": "Vital-statistics extract function",
          "disposition": "Rejected on boundary grounds",
          "rationale": "The base explicitly places the vital-event registration record and its statistical processing outside this model, and delegates usual residence as a statistical construct to the census/statistics model. Accepting produce-vital-statistics-extract would reopen a boundary the base closed deliberately; statutory public-record release stays covered by emit-minimal-disclosure and q-disc-public."
        },
        {
          "concept": "Issue identity document function",
          "disposition": "Rejected as boundary-crossing and duplicative",
          "rationale": "Issuance is an act of the issuing authority, an organization the base references but does not define; the base already records the resulting artefact through record-identity-evidence with issuer, validity, asserted attributes and holder binding."
        },
        {
          "concept": "Verify-identity and match-person-records functions",
          "disposition": "Rejected as duplicative",
          "rationale": "Covered by assess-identity-assurance (proofing outcome and assurance level), emit-minimal-disclosure (confirm only what was asked, with logging), resolve-person-reference and merge-or-split-person-records. Importing them would create two operations with the same trigger and outcome."
        },
        {
          "concept": "Service-layer composition (consent, audit, disclosure ledgers)",
          "disposition": "Merged as composed service references",
          "rationale": "Both providers agree that grant stores, policy decision points and audit ledgers are sibling service components referenced from the person model, so the base's lawful-basis, disclosure and retention findings stay as declarations of what must be governed and logged, without duplicating the service structure."
        },
        {
          "concept": "schema.org Person",
          "disposition": "Retained as a lossy publication projection only",
          "rationale": "Both providers reached the same conclusion from different angles (no validity periods, issuing authority or assurance semantics; admits fictional and undead characters), so it stays a projection target with a conformance-claim flag defaulting to false and is barred from being read as an assurance signal."
        }
      ],
      "publicationHolds": [
        "Reconcile and re-pin the Core Person Vocabulary version before publication: base cites CPV 2.00 (2022-04-01), grok cites CPV 2.1.2 (2026-05-12). Properties grok relies on (Contact Point on Person, residency as Jurisdiction, the gender/sex split, GenericDate) must be confirmed against the live release actually pinned.",
        "Reconcile the ISO/IEC 24760-1 edition: base cites the 2025 edition, grok cites 2019. Both retrievals were catalogue-level only, so no definition, identifier taxonomy or identity-record state vocabulary may be published as canonical from this standard.",
        "Re-verify GDPR Article 9 special-category wording against the EUR-Lex OJ text; the base verified it from an unofficial reproduction (tier 3) after repeated EUR-Lex retrieval failure.",
        "Re-verify CRPD Article 12 and General Comment No. 1 wording against an official UN-hosted text; one provider recorded an HTTP 403 at OHCHR and quoted secondary sources.",
        "Verify every accepted source URL as live and version-pinned, including the two OASIS CIQ v3.0 URL variants, both ICAO Doc 9303 landing pages, and the UN Principles and Recommendations Rev.3 PDF whose body could not be text-extracted (paragraph-level citations are currently absent).",
        "Run domain-profile validation on at least one non-EU profile before publication: the model is EU/UN-weighted (GDPR, eIDAS/EUDI PID, CPV, NIST levels), and a common-law vital-records plus ID-card regime and a Nordic population-register architecture must be mapped into the frame rather than assumed equivalent.",
        "Correct the base coverage-claim counts: it states 7 bundles, 15 layers and 28 findings, but the base structure contains 14 layers; after the accepted addition the merged model is 7 bundles, 14 layers, 29 findings and 14 functions.",
        "Scope the imported alternative-registration-routes finding on publication: only the UN LIA and CRVS-IdM backed portion (host-State or internationally mandated issuance, conferral by an identification authority linked to civil registration, delayed registration) may be presented as sourced; foundling, unknown-parentage and presumed-death-restoration sub-cases must be marked as unsourced operating cases, and the overlap with q-stateless-substitute must be resolved."
      ],
      "deferredResearch": [
        "Dedicated minority finding: age of majority and its jurisdictional variation, emancipation, and GDPR Article 8 child-consent thresholds, plus child-specific identity protections (preservation of identity, adoption record sealing and later access) that the base flagged as a likely addition.",
        "Citizenship as a legal tie to a jurisdiction versus nationality as encoded on travel documents: verify CPV and ICAO wording and decide whether the base nationality-holding finding is retitled or split, rather than adding a third overlapping node.",
        "Residency and habitual residence as a jurisdiction tie distinct from the address-typed domicile pointer, including which one governs applicable law; extend declared-residence-pointer rather than duplicating the contact layer.",
        "Foundlings, unknown parentage, confidential birth (including accouchement sous X), intersex civil markers, and identity restoration after a presumed or judicially declared death: no primary UN paragraph was located by either provider.",
        "Cross-border recognition of foreign civil status, foreign gender recognition and foreign capacity decisions, including the Hague Convention on the international protection of adults and apostille legalisation of civil documents, which neither provider fetched.",
        "Digital-identity assurance beyond the sources used: World Bank ID4D practice, and reconciliation of NIST SP 800-63A-4 assurance levels with eIDAS levels of assurance, which are not one-to-one mappable.",
        "Biometric modality profiles (ISO/IEC 19794 and 39794) and the template-protection, retention and matching-threshold rules that follow; both providers reference biometrics only as pointers and neither found an authoritative matching threshold for cross-script name matching.",
        "Deceased-person data handling after death and posthumous personality or digital remains, where most data-protection regimes stop applying while permanent registry obligations continue."
      ]
    },
    "statistics": {
      "sources": 26,
      "bundles": 7,
      "layers": 14,
      "findings": 29,
      "questions": 103,
      "artifacts": 31,
      "functions": 14
    }
  },
  "limits": [
    "Non-canonical reviewable draft; complete spec parsed and pinned; registry/v1 mappings non-normative."
  ]
}
```

## CLAUDE STUDY
```md
## Verdict

**PROFILE over WM-PER-001**, with one dependency: the *account binding* concept EM-PEO-01 names is deliberately out of WM-PER-001's scope and cannot be profiled from it — it must resolve in a sibling contour or, if none holds it, as an **identifier-unassigned candidate**. I do not assign an ID.

Not REUSE ONLY: WM-PER-001's required elements assume a civil-registration master (registration time, civil status, nationality determination, vital status are `required: true`), which no enterprise adopter can satisfy; unrestricted reuse would force fabricated values. Not COMPLETE RESERVED MODEL: the four candidate types (Person, NameForm, ContactPoint, IdentityEvidence) already resolve onto existing findings — `person-identity-anchor`, `legal-name-versioning` + `script-and-transliteration`, `person-controlled-contact-point`, `issued-identity-evidence` — so the enterprise contour adds restriction and context, not missing substance.

## Evidence

Structurally sufficient for a profiling decision; insufficient for any alignment or conformance statement. The spec is parsed and hash-pinned (252 757 B, sha256 7a4a71…), dual-provider, with an adjudication record that shows reasoned rejection of duplicates. Against that: `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, eleven open publication holds, registry `review_state: migration-boundary-review` and `status: described-previous-version`. The EM→WM link itself is `conceptual-candidate` at `index-and-publication-metadata` depth — the semantic crosswalk is asserted, not demonstrated. Registry `priority_confidence: low`. Two holds bear directly on this contour's core: the CPV version conflict (2.00 vs 2.1.2) governs whether ContactPoint attaches to Person at all in the alignment target, and the ISO/IEC 24760-1 edition conflict (2025 vs 2019) governs the entity/identity/reference-identifier vocabulary the whole matching contract leans on. Neither may be cited as settled.

## Boundary / mastership

The dossier's own fields conflict and the conflict must be resolved against the spec, not the queue row. `suggested_owner` "HR lead" and `candidate_master_systems` "HRIS, ATS, LMS" contradict the reservation's `owner_or_maintainer`: civil registrar for registered identity, the person for personal data. The profile should hold the spec's position:

- **Person anchor** — not HR-mastered. HRIS holds a *local record* linked to the anchor by `de-record-link`, never the anchor itself.
- **Legal name, birth facts, civil status, nationality, capacity, vital status** — registrar-mastered; enterprise-side these are *evidence-copied* values carrying `de-attribute-assurance-flag` and `de-attribute-source-ref`, correctable only upstream.
- **Contact points, preferred language, accessible-format need, usage name** — person-controlled and revocable (`person-controlled-contact-point`, `self-declared-attributes`).
- **Employment-context assertions, roles, accounts** — mastered by the employing organization but attached *to the relationship*, not to the person. ATS data is self-declared candidate claim, unverified by construction; LMS masters nothing identity-bearing.

Four things EM-PEO-01 asks to distinguish map as: *identity assertion* = a name/attribute claim with assurance flag and effective period; *evidence artifact* = `issued-identity-evidence` (issuer, status, asserted attribute set, holder binding); *contact point* = reachability channel with verification state and purpose limitation; *account binding* = a tie between a local system principal and the anchor — excluded here by the authenticator boundary note (`SRC-008`) and by the out-of-scope line on party/account relationships.

## Matching / linking contract

1. No attribute is a matching key on its own. `display_name` is `candidate-not-normative` in v1 and must never reach key status. Email is a `ContactPoint`: a verified contact proves *reachability and control of a channel*, never identity, and is shared, reassigned and delegated in practice.
2. Deterministic merge permitted only on a scheme-qualified identifier where `de-identifier-scheme` authority matches, `de-identifier-reuse-policy` forbids reassignment, and both records declare the same `de-domain-of-applicability`. Reuse-permitting schemes are disqualified as keys outright.
3. Everything else produces a **proposal**: `de-record-link` + `de-match-confidence` + rule-set version, resolved by a human role. The base carries confidence and link direction but has **no data element for link state (proposed/confirmed/rejected) and none for the authorising role**, though `duplicate-detection-and-merge` asks for the latter. The profile must add both; otherwise "uncertain match remains a proposal" is unenforceable.
4. Merge never destroys: superseded record survives as a resolvable tombstone via `de-surviving-record-ref`; reversal is a first-class path.
5. Evidence-based confirmation runs through `assess-identity-assurance`, producing `de-assurance-level` with expiry — not through attribute similarity.

## Names / contacts / pseudonyms

Names are time-bounded structured facts: `de-name-part`, `de-name-role`, `de-name-validity-period`, `de-name-script-code`. `record-name-change` opens a new assertion and closes the prior one; history is preserved by supersession, never overwrite. Display name is a derived presentation form, never stored as the authoritative value and never indexed for matching. The base's four name roles (birth / current legal / former legal / alias) are too coarse for enterprise usage names and pseudonyms — the profile should sub-type `alias` (usage name, professional pseudonym, system-local label) and route unverified ones through `self-declared-attributes` with `de-attribute-assurance-flag`.

A pseudonym or local identifier suffices when the purpose needs only *continuity of the same subject inside one domain* — training completion, internal directory presence, forum participation. Then `de-identifier-origin-class` = locally assigned surrogate, `de-correlatability-class` = pairwise or sector-scoped, derivation documented in `de-pseudonym-derivation`. It is never sufficient where a legal act, payroll, or evidence-bound assurance is required, and a pseudonymous identifier must never seed a merge.

## Privacy / disclosure

Purpose-bound by default: `emit-minimal-disclosure` releases the narrowest set, preferring `de-predicate-assertion` over the underlying attribute, with `de-special-category-flag` gating. Former names are the sharp case — disclosing them can reveal gender recognition, so the profile should suppress `former legal name` by default and release it only under a stated legal obligation, logged per disclosure. Consent and audit compose in as services (S1, S4); the employer declares purposes, it does not hold the grant store. Statutory HR processing runs on legal obligation, not consent, and must be labelled as such so withdrawal semantics stay honest.

## Invariants

Adopt all three, made testable: (i) *identity requires evidence* — no merge or elevation without `de-proofing-step-outcome` or a no-reuse scheme identifier; (ii) *purpose-bound disclosure* — every release logs `de-released-attribute-set` against a declared purpose; (iii) *employer is not universal owner* — subject-owned classes are person-revocable and survive employment termination independently of retention classes. Add: (iv) reference identifier is opaque and carries no attributes; (v) occurrence / registration / ingestion times stay separate (`event-time-versus-record-time`); (vi) `de-conformance-claim-flag` stays false.

## Scenarios

**Negative — auto-merge on display name.** Two records, `display_name` "Anna Ivanova", same domain. Rules 1–3 reject: no scheme identifier, display name non-normative. A confidence value may be written; no merge occurs, no surviving-record reference is set. If a shared verified email is also present, still refused — control of a channel is not identity. Blocked absent a link-state element, which is why the profile adds one.

**Acceptance — three systems, two namesakes, name change.** HRIS, directory, LMS. Namesake A changes legal name: `record-name-change` closes the old validity period and opens the new; the anchor and reference identifier are untouched; downstream systems re-resolve by identifier, not by name, so nothing breaks and the former name remains queryable but disclosure-suppressed. Namesake B is unaffected — no attribute-similarity path exists to link them. LMS holds only a local surrogate for B with pairwise correlatability; its tie to the anchor is a proposal at low confidence and stays a proposal until an authorised role confirms it against evidence. Result: three correct bindings, two distinct anchors, one open proposal.

## Profile shape

Restriction-only, no new semantics beyond the two link fields. Include: identity anchor, duplicate detection, legal-name versioning, script/transliteration, identifier assignment, identifier correlation, issued evidence, proofing assurance, contact point, self-declared attributes, lawful basis, subject rights, minimal disclosure, retention/audit, attribute accuracy, occurrence-vs-record time, record lifecycle, external alignment. Exclude at finding level (not element level, to avoid inheriting their required elements): birth facts, administrative sex, civil status, nationality, statelessness, legal capacity, representation, life-event anchors, alternative registration routes, vital status — each reachable only as a governed reference. Tighten: `de-identifier-origin-class` and `de-correlatability-class` required on every identifier; `de-contact-purpose-limitation` raised to `1..n`; `de-attribute-assurance-flag` mandatory on every projected attribute.

## Holds

Carry forward, unresolved: CPV version and whether ContactPoint attaches to Person; ISO/IEC 24760-1 edition for the identifier taxonomy and lifecycle vocabulary; GDPR Article 9 wording re-verification; source-URL liveness. Profile-specific: verify the EM→WM crosswalk beyond index metadata before treating the four candidate types as satisfied; resolve the owner/master-system contradiction in the queue row; locate or open the account-binding home; specify link state and authorising role; validate against a non-EU regime, since the base is EU/UN-weighted. No conformance or installability claim is made here.

```

## GROK STUDY
```md
**Verdict.** Conditional fail for publication. A restricted Enterprise usage profile over WM-PER-001 is the correct shape: reuse the person-anchor, do not mint a new catalogue ID, and do not treat the published Person model as an installed enterprise person master. EM-PEO-01 remains queued (Claude/Grok not-started; boundary decision pending). Mapping status is conceptual-candidate only. The card is fit only if the restrictions, matching contract and fixtures below are bound before any publication claim.

**Mastership.** Person-anchor mastership stays on the WM-PER-001 natural-person entity and its domain-scoped reference identifier, whose issuing authority warrants persistence and non-reuse. The person is distinct from any record, identifier, document or credential about them. Registered-identity facts belong to the registrar of record; personal-sphere contacts and self-declarations belong to the person. HRIS, ATS and LMS are source systems of local bindings and purpose-limited projections, never universal person masters. An employee number is employer-scoped; changing employer does not change Person. AccountBinding is outside WM-PER-001 — party roles, customer and account relationships, authenticators, sessions and login are out of scope — and may remain an identifier-unassigned sibling candidate. Do not infer Person from Account. Do not treat a source row key, display name or email as the person.

**Matching contract.** Deterministic same-person linking is allowed only when both records carry a non-reassigned scheme-qualified identifier that matches on exact scheme, schemeVersion, issuer, scope and value inside the same authority/domain, with a no-reuse policy and declared referent kind Person. Compare qualified keys only; do not infer issuer, tenant or namespace; do not normalise. Display name, preferred name, email, phone and match-score cannot activate an asserted claim or auto-merge. Failing that test, create a proposed link only: state proposed; rule version; purpose; interval; authorising role; evidence references; and confidence if the host policy encodes it — otherwise record explicit absence of a numeric score so absence is not read as zero. A probable-entity-match cannot enter asserted state. Merge or split requires a durable record-linkage decision (inputs, threshold, authorising role, reversal path). Name plus date of birth is not an identifier.

**Name, contact and pseudonym rules.** Legal name is a time-bounded structured NameForm (parts; role birth/current/former/alias; script; ordering; validity; name-change instrument). A name change closes the prior validity interval and retains the former name; in-place overwrite is forbidden. Self-declared and display names never replace a legal name. Display name is a rendering, not an identity key; the brief field `display_name` is candidate-not-normative. ContactPoints are person-controlled, purpose-limited, visibility-scoped and separately verified; reference WM-PER-010, do not absorb it. Email and phone are contact values, not person identifiers. Pseudonyms and local IDs are scheme-qualified derived identifiers with correlatability class, relying-party or sector scope, and rotation; they are sufficient only inside that declared scope and are never deterministic merge keys.

**Privacy.** Disclosure is purpose-bound and deny-by-default. Every read names purpose, lawful basis and relying-party class and returns the narrowest projection. HR, customer and technical roles reference the person under a disclosure agreement; the employer does not own all person data. Special-category data and former-name fields are withheld from default projections. A same-as or proposed link is its own sensitivity class because linkage can defeat a pseudonym. Consent is scoped and withdrawable; statutory HR processing cannot be refused by withdrawal but remains purpose-limited.

**Scenario.** Three systems — HRIS, ATS, LMS — hold records for two namesakes who share a display name and a similar email local-part; one later records a legal-name change with a change instrument. Expected: two Person anchors remain distinct; each local record stays a source binding, identifier-unassigned where no scheme-qualified key exists; the name change versions NameForm, closes the prior legal-name interval and retains history; no system auto-merges on display name or email; the uncertain ATS–HRIS–LMS correspondence remains a proposal with rule version, state and authorising role. The card’s negative case — two users with the same display name merged automatically — must fail closed. An AccountBinding without a person identifier stays a sibling candidate, not a Person.

**Profile restrictions.** This is a restricted Enterprise usage profile over WM-PER-001 0.3.0-research.1, not a new subject model and not whole-parent conformance. In-profile: Person anchor reference; time-bounded NameForm with history; purpose-bound ContactPoint (reference, not absorb); IdentityEvidence references; scheme-qualified identifiers with reuse policy; proposed or asserted linkage records. Out-of-profile: replacing the civil registrar; biological or health data; household or kinship as objects; employment, customer or account facts as person attributes; authenticators and sessions; behavioural scoring; universal EMPI; biometrics as merge keys. Civil-status, nationality, legal-capacity and vital-event layers stay optional for enterprise. The contact-point ownership conflict between WM-PER-010 and WM-XCT-024 remains open.

**Blockers.** (1) EM-PEO-01 research is queued; reuse/extend/new is undecided; no published restricted-profile package exists over WM-PER-001. (2) `brief.json` lists HRIS, ATS and LMS as `candidate_master_systems`. That listing is a candidate list, not confirmed mastership, and it contradicts person-anchor mastership; rewrite as local bindings only. (3) Semantic crosswalk, mastership-and-rights matrix, and namesake-plus-name-change fixtures are absent. (4) WM-PER-001 is reviewable-draft, not a canonical Vercy release; source and coverage holds remain open. (5) AccountBinding is not an EM-PEO-01 candidate type (Person, NameForm, ContactPoint, IdentityEvidence) and must stay an identifier-unassigned sibling. (6) Do not invent a catalogue ID.
```

## PROVIDER COMPARISON
```md
# EM-PEO-01 provider comparison

Claude and Grok converge on a restricted **PROFILE** over `WM-PER-001`, with no new identifier. Both preserve one durable Person anchor across local HRIS, ATS, directory and LMS records; forbid automatic merge from display name, email or similarity; require scheme, issuer, scope and non-reuse guarantees for deterministic linking; preserve effective-dated name history; and keep AccountBinding outside the Person model as an identifier-unassigned sibling candidate.

Claude sharpened the conflict between enterprise adoption and civil-registration-required fields, the missing link-state and authorising-role carriers, and the finding-level exclusion needed to avoid inheriting unsuitable required elements. Grok sharpened the exact qualified-key tuple, explicit absence of confidence, purpose-bound disclosure and separation of local source bindings from person mastership. Grok's version and neighboring-model references are treated as explanatory only unless they are present in the frozen dossier.

```

## CANDIDATE REVISION 2
```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-PEO-01",
  "contourName": "Человек и контекстная идентичность",
  "name": "Enterprise Person and Contextual Identity",
  "decision": "PROFILE",
  "decisionByBase": {
    "WM-PER-001": "RESTRICTED PROFILE",
    "newIdentifier": false
  },
  "newRuntimeId": false,
  "bases": [
    "WM-PER-001"
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-frozen-audit",
  "publishableCanonical": false,
  "fixturesExecuted": false,
  "basePins": [
    {
      "modelId": "WM-PER-001",
      "registryId": "vr.wm-per-001",
      "sourceFile": "publications/wm-per-001-person/spec.yaml",
      "sourceBytes": 252757,
      "sourceSha256": "7a4a71ddd69fdc31b37806958442d1cfca4ec0bf861e54578adb312e0d7a4df3",
      "synthesisSha256": "ffefc6ce9cf9d7c6b9661c80834009180840f8da0a23e7409434e4c49c9472b2",
      "publicationStatus": "published",
      "publicationStatusMeaning": "pipeline emission, not canonical adjudication",
      "adjudicationStatus": "reviewable-draft",
      "publishableCanonical": false,
      "providerMode": "dual-provider",
      "registryStatus": "described-previous-version",
      "registryReviewState": "migration-boundary-review",
      "registryEntryKind": "standalone-mm",
      "specEntryKind": "entity",
      "entryKindDivergence": true,
      "registrySnapshotSha256": "64b97cffa92f4db5c7888273828184abcfb3155e3c0e8f94fa798d1b1c458fe3",
      "registryDigestMeaning": "SHA-256 of UTF-8 canonical JSON for full frozen reservation, sorted keys and compact separators"
    }
  ],
  "requiredDependencies": [
    {
      "name": "Identifier and identity-resolution support",
      "modelId": null,
      "pinned": false
    },
    {
      "name": "Temporal validity and provenance support",
      "modelId": null,
      "pinned": false
    },
    {
      "name": "Disclosure and lawful-basis services",
      "modelId": null,
      "pinned": false
    }
  ],
  "deferredCandidates": [
    {
      "name": "AccountBinding",
      "identifier": null,
      "status": "unassigned",
      "reason": "Independent local-principal binding lifecycle outside Person."
    }
  ],
  "mastership": {
    "PersonAnchor": "WM-PER-001 authority, never universal HRIS/ATS/LMS ownership",
    "registeredIdentityFacts": "registrar or issuer of record",
    "personControlled": "contact, usage name, preferences, self-declarations",
    "employmentContext": "employment relationship",
    "localBindings": "each source system"
  },
  "constraints": [
    "WM-PER-001 remains the only Person anchor in this contour; the profile creates no second person identity.",
    "HRIS, ATS, directory and LMS records are local bindings and purpose-limited projections and never become universal Person masters.",
    "Civil registrar facts remain registrar-sourced; person-controlled contacts, usage names and preferences remain distinct from employer-controlled relationship assertions.",
    "A source row key, account, authenticator, session, display name, email, phone, name plus date of birth or similarity score never denotes a Person by itself.",
    "Deterministic same-person linkage requires an exact tuple of scheme, scheme version, issuer, authority/domain scope, value, Person referent kind and a documented non-reassignment policy.",
    "Qualified identifiers are compared as opaque values; issuer, namespace, tenant, normalization or scope are never inferred.",
    "Any linkage that fails the deterministic contract remains a proposed link carrying rule version, purpose, validity, authorising role, evidence references and confidence or an explicit confidence-absent marker.",
    "Probable matches never enter asserted state automatically; merge and split require an addressable linkage decision with inputs, threshold, authorising role and reversal path.",
    "Merge preserves resolvable tombstones and history and never destroys source records.",
    "Names are structured, script-aware, effective-dated assertions; name change closes the prior interval and opens a new one without changing the Person anchor.",
    "Display names are renderings and not authoritative values or matching keys.",
    "Usage names and pseudonyms are typed aliases with assurance, purpose, correlatability class, relying-party or sector scope and rotation policy.",
    "A pairwise or sector pseudonym provides continuity only inside its declared scope and never seeds cross-domain merge.",
    "Contact verification proves control or reachability of a channel and never Person identity.",
    "Contact disclosure is purpose-limited and visibility-scoped; former names and special-category attributes are suppressed by default.",
    "Every disclosure declares purpose, lawful basis, relying-party class and released attribute set and returns the narrowest projection.",
    "Consent withdrawal affects consent-based processing only; statutory processing remains separately purpose-limited and evidenced.",
    "Identity evidence is referenced with issuer, status, asserted attributes, holder binding and assurance expiry and is not copied into Person.",
    "Employment, customer, party-role and account facts remain owned by their relationship records and are not Person attributes.",
    "AccountBinding remains an identifier-unassigned sibling candidate and cannot create, own or merge a Person.",
    "Reference identifiers are opaque and carry no embedded attributes.",
    "Occurrence, registration and knowledge time remain separate where supported; corrections append superseding assertions.",
    "Enterprise adoption excludes unsuitable civil-registration-required findings at finding level rather than fabricating values.",
    "All standards references are alignment-only; no conformance, canonical release or installability claim is permitted.",
    "Publication is refused while base holds, mastership conflicts, link carriers, dependency pins, registry drift or fixtures remain unresolved."
  ],
  "matchingContract": {
    "deterministicTuple": [
      "scheme",
      "schemeVersion",
      "issuer",
      "authorityDomainScope",
      "value",
      "referentKind=Person",
      "nonReassignmentPolicy"
    ],
    "fallback": "proposed link only",
    "proposalFields": [
      "state",
      "ruleVersion",
      "purpose",
      "validFrom",
      "validUntil",
      "authorisingRole",
      "evidenceRefs",
      "confidenceOrExplicitAbsent"
    ],
    "mergeDecisionFields": [
      "inputs",
      "threshold",
      "authorisingRole",
      "reversalPath"
    ]
  },
  "findingSelection": {
    "excludeAsGovernedReferences": [
      "birth facts",
      "administrative sex",
      "civil status",
      "nationality",
      "statelessness",
      "legal capacity",
      "representation",
      "life-event anchors",
      "alternative registration routes",
      "vital status"
    ]
  },
  "profileTypes": {
    "Person": {
      "baseModelId": "WM-PER-001",
      "disposition": "reuse anchor under restriction"
    },
    "NameForm": {
      "baseModelId": "WM-PER-001",
      "disposition": "profile existing findings"
    },
    "ContactPoint": {
      "baseModelId": "WM-PER-001",
      "disposition": "restricted projection; ownership conflict held"
    },
    "IdentityEvidence": {
      "baseModelId": "WM-PER-001",
      "disposition": "reference evidence only"
    },
    "AccountBinding": {
      "baseModelId": null,
      "registryId": null,
      "runtimeId": null,
      "disposition": "identifier-unassigned sibling candidate"
    }
  },
  "inheritedHolds": [
    {
      "baseModelId": "WM-PER-001",
      "index": 1,
      "text": "Reconcile and re-pin the Core Person Vocabulary version before publication: base cites CPV 2.00 (2022-04-01), grok cites CPV 2.1.2 (2026-05-12). Properties grok relies on (Contact Point on Person, residency as Jurisdiction, the gender/sex split, GenericDate) must be confirmed against the live release actually pinned."
    },
    {
      "baseModelId": "WM-PER-001",
      "index": 2,
      "text": "Reconcile the ISO/IEC 24760-1 edition: base cites the 2025 edition, grok cites 2019. Both retrievals were catalogue-level only, so no definition, identifier taxonomy or identity-record state vocabulary may be published as canonical from this standard."
    },
    {
      "baseModelId": "WM-PER-001",
      "index": 3,
      "text": "Re-verify GDPR Article 9 special-category wording against the EUR-Lex OJ text; the base verified it from an unofficial reproduction (tier 3) after repeated EUR-Lex retrieval failure."
    },
    {
      "baseModelId": "WM-PER-001",
      "index": 4,
      "text": "Re-verify CRPD Article 12 and General Comment No. 1 wording against an official UN-hosted text; one provider recorded an HTTP 403 at OHCHR and quoted secondary sources."
    },
    {
      "baseModelId": "WM-PER-001",
      "index": 5,
      "text": "Verify every accepted source URL as live and version-pinned, including the two OASIS CIQ v3.0 URL variants, both ICAO Doc 9303 landing pages, and the UN Principles and Recommendations Rev.3 PDF whose body could not be text-extracted (paragraph-level citations are currently absent)."
    },
    {
      "baseModelId": "WM-PER-001",
      "index": 6,
      "text": "Run domain-profile validation on at least one non-EU profile before publication: the model is EU/UN-weighted (GDPR, eIDAS/EUDI PID, CPV, NIST levels), and a common-law vital-records plus ID-card regime and a Nordic population-register architecture must be mapped into the frame rather than assumed equivalent."
    },
    {
      "baseModelId": "WM-PER-001",
      "index": 7,
      "text": "Correct the base coverage-claim counts: it states 7 bundles, 15 layers and 28 findings, but the base structure contains 14 layers; after the accepted addition the merged model is 7 bundles, 14 layers, 29 findings and 14 functions."
    },
    {
      "baseModelId": "WM-PER-001",
      "index": 8,
      "text": "Scope the imported alternative-registration-routes finding on publication: only the UN LIA and CRVS-IdM backed portion (host-State or internationally mandated issuance, conferral by an identification authority linked to civil registration, delayed registration) may be presented as sourced; foundling, unknown-parentage and presumed-death-restoration sub-cases must be marked as unsourced operating cases, and the overlap with q-stateless-substitute must be resolved."
    }
  ],
  "inheritedHoldRule": "Inherited holds remain verbatim and cannot be discharged by this contour.",
  "publicationHolds": [
    "WM-PER-001 is non-canonical reviewable draft.",
    "Queue master-system wording conflicts with base mastership.",
    "Link-state and authorising-role carriers lack allocated base elements.",
    "AccountBinding has no allocated home.",
    "Fixtures are declarative and unexecuted."
  ],
  "provenance": {
    "claudeStudy": "claude-study.raw.md",
    "grokStudy": "grok-study.raw.md",
    "comparison": "provider-comparison.md",
    "audit": "pending"
  }
}
```

## FIXTURES REVISION 2
```json
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "contourId": "EM-PEO-01",
  "profileName": "Enterprise Person and Contextual Identity",
  "fixtureRevision": 2,
  "fixturesExecuted": false,
  "baseSourcePins": {
    "WM-PER-001": "7a4a71ddd69fdc31b37806958442d1cfca4ec0bf861e54578adb312e0d7a4df3"
  },
  "cases": [
    {
      "id": "namesakes-three-systems",
      "kind": "positive",
      "input": "Two namesakes have similar display names and email local parts across HRIS, ATS and LMS, with no qualified key.",
      "expect": "keep two anchors; create proposals only",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "097b32310819a012b199683481d8009d19f984952266a50859bcbacb3bb6a8c2"
    },
    {
      "id": "qualified-no-reuse-link",
      "kind": "positive",
      "input": "Both records have exact scheme/version/issuer/scope/value Person identifiers and a no-reuse policy.",
      "expect": "permit deterministic link",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "b26d0740c0037704b0fa51db88133e54ce506b269821992feee497f2b448019a"
    },
    {
      "id": "issuer-missing",
      "kind": "negative",
      "input": "Identifier values match but issuer is absent on one record.",
      "expect": "refuse deterministic link; proposal only",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "37c68506dd362102da880656d4031e543cb8aca2066a4fef507b818ffb18f611"
    },
    {
      "id": "email-auto-merge",
      "kind": "negative",
      "input": "Two records share a verified email.",
      "expect": "refuse merge",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "ead0c63a031e28eea87d8969d063fe2d758764cb26d48701460cd4801bc89fc8"
    },
    {
      "id": "name-dob-auto-merge",
      "kind": "negative",
      "input": "Name and date of birth match.",
      "expect": "refuse deterministic link",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "4f5a83c4400351bdf21bbfc2316d514757d924cbebc2b64f7ced3a04ecb5027a"
    },
    {
      "id": "legal-name-change",
      "kind": "positive",
      "input": "Name-change instrument closes former legal name and opens current name.",
      "expect": "preserve anchor and history",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "c5911ccc21835c71228e7b8035ebbbc815de4f784e0302bef8223e546f3ebcee"
    },
    {
      "id": "overwrite-former-name",
      "kind": "negative",
      "input": "Current legal name overwrites prior assertion.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "852969d6c15af8f43f19253ae7f4cc9fe00605c7d0cddce87fb24af291ec78c8"
    },
    {
      "id": "pseudonym-cross-domain",
      "kind": "negative",
      "input": "Pairwise pseudonym is reused across unrelated purposes.",
      "expect": "refuse correlation",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "5bdccdaad9b723972a0a98a1bf232574c0830f659d348562a8b349a7df27043c"
    },
    {
      "id": "contact-as-identity",
      "kind": "negative",
      "input": "Verified phone is treated as identity proof.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "52599665eb78f1194d124b13b75c3d20fe51bf3e0c477930347d164a9245864b"
    },
    {
      "id": "proposal-without-authoriser",
      "kind": "negative",
      "input": "Uncertain match lacks authorising role.",
      "expect": "refuse assertion",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "98402b4cd92f35e5228e85b751d04f5f24ec99364bae6571296c605d6f1a2516"
    },
    {
      "id": "probable-to-asserted",
      "kind": "negative",
      "input": "High confidence directly activates asserted link.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "da0fc3c9b4117a162c4b36976aee282b925c743b41b8a2f4aa6946c24874b02d"
    },
    {
      "id": "merge-destroys-source",
      "kind": "negative",
      "input": "Merge deletes losing source record.",
      "expect": "refuse; tombstone and reversal required",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "e1b0e1e24974db688065706f678d6fc81a361ad0682e956f85487e44225282e1"
    },
    {
      "id": "former-name-default-disclosure",
      "kind": "negative",
      "input": "Default directory projection releases former legal name.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "46f29166a9643234563bf39f49294d0e2b6f1ecb5b1c3f86cb68ea34aa8a04c6"
    },
    {
      "id": "purpose-bound-minimal",
      "kind": "positive",
      "input": "Disclosure declares purpose, basis, relying party and minimal attributes.",
      "expect": "accept",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "cc5803530f5253b880996cd58aa1d4fe804d42385f5235037220adede92c61bd"
    },
    {
      "id": "hris-universal-master",
      "kind": "negative",
      "input": "HRIS claims universal ownership of person and registrar facts.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "c5e6d7a6c76fbd4dc0c2100f082b0714fcd6f8cc185225835dcf253f49878b4c"
    },
    {
      "id": "account-creates-person",
      "kind": "negative",
      "input": "Local login account creates Person anchor.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "ab59e43014490b353d4de215a05fbb1877b81452b1c47d916968be07e363fbfb"
    },
    {
      "id": "employment-as-person-attribute",
      "kind": "negative",
      "input": "Employment status is intrinsic Person attribute.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "d590dfabbc104c22b2073701fe3d77e7196f049b58b2ebc4e17dcd8b8780c8aa"
    },
    {
      "id": "civil-fields-fabricated",
      "kind": "negative",
      "input": "Enterprise adopter fabricates required civil facts.",
      "expect": "refuse; exclude governed findings",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "088cb3d9e11ac34008479ec186a10dbfea43d61b5a07558864ff6d88f6d397d1"
    },
    {
      "id": "standards-conformance",
      "kind": "negative",
      "input": "Profile claims parent or standards conformance.",
      "expect": "refuse",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "59f0846569784f5778bbb3e18eca05fbf252d2068ec80935388cda4672a550aa"
    },
    {
      "id": "two-namesakes-one-change",
      "kind": "positive",
      "input": "Two anchors exist; one changes legal name; LMS correspondence is uncertain.",
      "expect": "preserve both anchors and leave LMS proposal open",
      "digestMeaning": "SHA-256 of canonical JSON case definition only; no execution meaning",
      "sha256": "4d66bd69b6d687f3ee42d0a4deee1a9fae539f5cc263c865bdbd0236d9f54ac2"
    }
  ]
}
```
