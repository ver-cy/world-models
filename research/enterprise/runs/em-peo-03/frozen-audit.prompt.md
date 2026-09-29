# Frozen semantic audit: EM-PEO-03 Competencies and Qualifications

You are the single independent frozen auditor. Use only the JSON below and no tools. Do not invent identifiers or external facts.

Return:
1. Verdict ACCEPT or REVISE.
2. Confirm or reject the complete minimum model set and the decision to allocate no new identifier now.
3. List every defect that could collapse definition, scale, mapping, person assertion, assessment, evidence, qualification, credential, licence, role or course; lose history; infer current competence; breach privacy; or overclaim validation/publication.
4. Give exact remediation and one fixture expectation for every defect.
5. Identify contradictions.
6. End with a closed numbered remediation checklist.

## FROZEN RECONCILED DOSSIER
```json
{
  "reservedCompletion": {
    "format": "vercy-world-model-candidate/v1",
    "contourId": "EM-PEO-03",
    "modelId": "WM-PER-009",
    "registryId": "vr.wm-per-009",
    "name": "Skill / Competency Definition",
    "version": "0.1.0-candidate.2",
    "entryKind": "concept-scheme-aggregate",
    "status": "research-candidate",
    "canonicalPublishable": false,
    "purpose": "Represent scheme-scoped Skill and Competency definitions, immutable scheme releases, composition and explicitly lossy mappings without owning person capability assertions, assessments, qualifications, credentials or role assignments.",
    "boundary": {
      "owns": [
        "scheme and immutable release identity",
        "scheme-scoped SkillDefinition and CompetencyDefinition identity",
        "language-tagged labels, definition text, definition type and applicability",
        "intra-scheme definition structure and deprecation/successor lineage",
        "version-pinned directional concept mappings with purpose, authority and declared semantic loss"
      ],
      "delegates": [
        "proficiency scale identity and level semantics to an identifier-unassigned Proficiency Scale candidate",
        "person capability holdings to an identifier-unassigned Person Capability Assertion candidate",
        "competency assessments to WM-ACT-034",
        "qualification definitions and awards to WM-PER-008",
        "issued credential identity and validity to WM-XCT-017",
        "professional licence specialization to WM-PER-013",
        "position expectations and requirements to WM-ORG-004"
      ],
      "excludes": [
        "a person current capability state",
        "assessment event result or evidence",
        "qualification award or credential lifecycle",
        "role occupant assignment",
        "course completion inference",
        "AI-agent instruction package identity",
        "proficiency scale level ownership or level mappings",
        "cross-scheme identity equivalence",
        "current competence flag or merged current score"
      ]
    },
    "objects": {
      "CompetencyScheme": {
        "identity": [
          "schemeId",
          "releaseId"
        ],
        "required": [
          "name",
          "authorityRef",
          "version",
          "issuedAt",
          "contentDigest",
          "status"
        ],
        "optional": [
          "supersedesReleaseId"
        ],
        "lifecycle": [
          "draft",
          "issued",
          "superseded",
          "withdrawn"
        ]
      },
      "SkillCompetencyConcept": {
        "identity": [
          "schemeId",
          "releaseId",
          "conceptId"
        ],
        "required": [
          "conceptType",
          "preferredLabels",
          "definition",
          "status"
        ],
        "optional": [
          "alternativeLabels",
          "broaderConceptRefs",
          "narrowerConceptRefs",
          "context",
          "applicability",
          "deprecatedAt",
          "successorConceptRef"
        ],
        "lifecycle": [
          "draft",
          "active",
          "deprecated",
          "retired"
        ]
      },
      "CompetencyComposition": {
        "identity": [
          "compositionId"
        ],
        "required": [
          "competencyConceptRef",
          "componentRefs",
          "context",
          "authorityRef",
          "validFrom",
          "status"
        ],
        "optional": [
          "validTo",
          "compositionRule",
          "evidenceRefs"
        ]
      },
      "ConceptMapping": {
        "identity": [
          "mappingId"
        ],
        "required": [
          "sourceConceptRef",
          "targetConceptRef",
          "sourceSchemeReleaseRef",
          "targetSchemeReleaseRef",
          "direction",
          "purpose",
          "strength",
          "semanticLoss",
          "authorityRef",
          "issuedAt",
          "status"
        ],
        "optional": [
          "validTo",
          "evidenceRefs",
          "successorMappingId"
        ],
        "lifecycle": [
          "draft",
          "issued",
          "superseded",
          "withdrawn"
        ]
      }
    },
    "conceptTypes": [
      "skill",
      "competency"
    ],
    "mappingStrengths": [
      "narrower-than",
      "broader-than",
      "overlaps",
      "related",
      "purpose-qualified-equivalent"
    ],
    "relations": [
      {
        "target": "WM-ACT-034",
        "relation": "REFERENCE",
        "required": false,
        "purpose": "Allow assessment criteria and results to pin immutable skill or competency definitions."
      },
      {
        "target": "WM-ORG-004",
        "relation": "REFERENCE",
        "required": false,
        "purpose": "Allow position requirements to pin immutable concept and scale versions without becoming person assertions."
      },
      {
        "target": "WM-XCT-017",
        "relation": "REFERENCE",
        "required": false,
        "purpose": "Allow credential evidence to cite concepts while issuance and validity remain credential-owned."
      }
    ],
    "operations": [
      {
        "id": "issue-scheme-release",
        "effect": "Issue an immutable content-addressed concept-scheme release.",
        "authority": "scheme authority"
      },
      {
        "id": "deprecate-concept",
        "effect": "Deprecate a concept with successor guidance without rewriting prior references.",
        "authority": "scheme authority"
      },
      {
        "id": "compose-competency",
        "effect": "Issue a context-qualified composition of knowledge skill and behaviour references.",
        "authority": "scheme authority"
      },
      {
        "id": "issue-mapping",
        "effect": "Issue a directional purpose-limited mapping with declared loss.",
        "authority": "mapping authority"
      },
      {
        "id": "supersede-mapping",
        "effect": "Issue a successor mapping while preserving the predecessor.",
        "authority": "mapping authority"
      }
    ],
    "invariants": [
      "SkillDefinition and CompetencyDefinition remain distinct even when labels match.",
      "Definition identity is scheme, scheme-local code and immutable definition version; labels are display only.",
      "A definition carries no person, proficiency level, expiry, evidence, assessment, qualification, credential, licence, role or course state.",
      "Imported definitions remain mastered by their scheme owner; an enterprise copy never transfers authority.",
      "Relabelling across schemes creates a mapping and never an identity merge.",
      "Competency composition is definition structure, never a holding or proficiency claim.",
      "Concept mappings pin both releases, are directional, purpose-limited and declare semantic loss.",
      "Concept mapping is not level mapping, identity, equivalence or a Person Capability Assertion.",
      "Definition deprecation never rewrites historical references.",
      "Assessment results and evidence never mutate a definition.",
      "Course completion and role occupancy never write proficiency.",
      "Credential or licence status never becomes current competence.",
      "Human definitions never share identity with AI-agent instruction packages.",
      "Completing reserved WM-PER-009 allocates no additional identifier."
    ],
    "holds": [
      "WM-PER-009 completion remains a research candidate and definition-only.",
      "Base and neighboring models remain non-canonical reviewable drafts or carry inherited holds.",
      "No approved competency relation rows are available; all proposed links remain held.",
      "External ESCO, SFIA, CTDL, CLR, Open Badges and VC mappings require pinned source verification.",
      "Proficiency Scale and Person Capability Assertion remain identifier-unassigned.",
      "Declarative fixtures are not executable tests and package conversion/live verification remain pending."
    ],
    "candidateRevision": 2
  },
  "scaleCandidate": {
    "format": "vercy-model-allocation-candidate/v1",
    "contourId": "EM-PEO-03",
    "proposedName": "Proficiency Scale",
    "modelId": null,
    "registryId": null,
    "allocationState": "unassigned",
    "decision": "NEW MODEL",
    "canonicalPublishable": false,
    "identityTest": {
      "stableIdentity": "A governed proficiency scale remains identifiable across competency concepts, assessments and organizations while its ordered levels and descriptors evolve through released versions.",
      "versionIdentity": "Changes to level order, descriptors, measurement level, interpretation or applicability create immutable scale versions; a different measurement construct creates a separate scale.",
      "independentLifecycle": [
        "draft",
        "reviewed",
        "approved",
        "effective",
        "superseded",
        "retired"
      ],
      "mastership": "competency-scheme or assessment-method authority"
    },
    "boundary": {
      "owns": [
        "persistent proficiency-scale identity",
        "ordered level set",
        "level identifiers and descriptors",
        "measurement-level semantics",
        "interpretation and applicability rules",
        "version validity and successor lineage",
        "cross-scale mapping references",
        "approval and retirement history"
      ],
      "references": [
        {
          "target": "WM-PER-009",
          "purpose": "Skill or competency definition master"
        },
        {
          "target": "WM-ACT-034",
          "purpose": "Competency assessment"
        },
        {
          "target": "WM-PER-008",
          "purpose": "Qualification definition and award"
        },
        {
          "target": "WM-XCT-017",
          "purpose": "Issued credential"
        },
        {
          "target": "WM-ORG-004",
          "purpose": "Position competency requirement"
        }
      ],
      "excludes": [
        "skill or competency concept identity",
        "person capability assertion",
        "assessment event, result or evidence",
        "qualification, licence or credential identity",
        "role expectation or course completion",
        "person or position mastership"
      ]
    },
    "objects": {
      "ProficiencyScale": {
        "identity": [
          "proficiencyScaleId"
        ],
        "required": [
          "name",
          "ownerRef",
          "measurementLevel",
          "status"
        ],
        "optional": [
          "successorRef",
          "retiredAt"
        ],
        "lifecycle": [
          "draft",
          "reviewed",
          "approved",
          "effective",
          "superseded",
          "retired"
        ]
      },
      "ScaleVersion": {
        "identity": [
          "proficiencyScaleId",
          "version"
        ],
        "required": [
          "orderedLevels",
          "validFrom",
          "contentDigest",
          "status"
        ],
        "optional": [
          "interpretation",
          "applicability",
          "validTo",
          "supersedesVersion"
        ],
        "lifecycle": [
          "draft",
          "approved",
          "effective",
          "superseded",
          "withdrawn"
        ]
      },
      "ScaleMapping": {
        "identity": [
          "scaleMappingId"
        ],
        "required": [
          "sourceScaleVersionRef",
          "sourceLevelRef",
          "targetScaleVersionRef",
          "targetLevelRef",
          "direction",
          "purpose",
          "authorityRef",
          "semanticLoss",
          "nonReversible",
          "validFrom",
          "status"
        ],
        "optional": [
          "validTo",
          "evidenceRefs",
          "successorMappingRef",
          "residualDescription"
        ],
        "lifecycle": [
          "draft",
          "issued",
          "superseded",
          "withdrawn"
        ]
      }
    },
    "invariants": [
      "Scale identity is scale scheme, scale id and immutable scale version.",
      "Level identity and interpretation exist only inside one scale version.",
      "Ordering or descriptor changes create a successor version and never rewrite finalized results.",
      "Cross-scale comparison exists only through an addressable version-pinned mapping.",
      "Every mapping is directional, purpose-limited, loss-declaring and non-reversible unless an independent reverse mapping exists.",
      "A mapping never maps a person or creates, translates or upgrades a Person Capability Assertion.",
      "Mapping transitivity is never inferred.",
      "Matching labels or numbers never imply equivalence.",
      "Missing, indeterminate and not-applicable never collapse to level zero.",
      "A scale never owns assessment evidence, qualification, credential, licence, role expectation or course completion.",
      "Retired and superseded scale versions remain resolvable.",
      "No identifier is allocated until registry reservation is approved."
    ],
    "holds": [
      "Registry allocation is pending and identifiers remain null.",
      "Scale mapping source crosswalks and authorities require pinned verification.",
      "Base-model and relation approvals remain external.",
      "Fixtures are declarative and unexecuted; package conversion and live verification remain pending."
    ],
    "candidateRevision": 2
  },
  "assertionCandidate": {
    "format": "vercy-model-allocation-candidate/v1",
    "contourId": "EM-PEO-03",
    "proposedName": "Person Capability Assertion",
    "modelId": null,
    "registryId": null,
    "allocationState": "unassigned",
    "decision": "NEW MODEL",
    "canonicalPublishable": false,
    "identityTest": {
      "stableIdentity": "An attributable assertion that one person holds one competency at a stated level remains identifiable independently of person, competency, scale, assessment and credential records.",
      "versionIdentity": "A new asserter, basis, level, scale version, validity interval, assurance or evidence conclusion creates a new assertion or explicit successor.",
      "independentLifecycle": [
        "proposed",
        "active",
        "revalidated",
        "superseded",
        "expired",
        "withdrawn",
        "revoked"
      ],
      "mastership": "authorized capability-assertion issuer or HR evidence authority"
    },
    "boundary": {
      "owns": [
        "persistent person-capability assertion identity",
        "person and competency-version references",
        "proficiency level and scale-version reference",
        "asserter, basis and assertion mode",
        "validity interval and observation time",
        "evidence, assurance and confidence",
        "revalidation and decay rules",
        "supersession, withdrawal and revocation history"
      ],
      "references": [
        {
          "target": "WM-PER-009",
          "purpose": "Competency definition"
        },
        {
          "target": "WM-ACT-034",
          "purpose": "Assessment and result evidence"
        },
        {
          "target": "WM-PER-008",
          "purpose": "Qualification award"
        },
        {
          "target": "WM-XCT-017",
          "purpose": "Credential evidence"
        },
        {
          "target": "WM-PER-013",
          "purpose": "Professional licence profile"
        },
        {
          "target": "WM-ORG-004",
          "purpose": "Position competency requirement"
        }
      ],
      "excludes": [
        "person, competency or scale identity",
        "assessment event or result identity",
        "qualification, credential or licence identity",
        "role requirement or position assignment",
        "course participation or completion",
        "external scheme-definition mastership"
      ]
    },
    "objects": {
      "PersonCapabilityAssertion": {
        "identity": [
          "personCapabilityAssertionId"
        ],
        "required": [
          "personRef",
          "definitionVersionRef",
          "assertionKind",
          "asserterRef",
          "validFrom",
          "recordedAt",
          "status"
        ],
        "optional": [
          "scaleVersionRef",
          "levelRef",
          "validTo",
          "assessmentRef",
          "evidenceRefs",
          "assurance",
          "confidence",
          "revalidationRule",
          "decayRule",
          "supersedesRef"
        ],
        "assertionKindVocabulary": [
          "self-assessed",
          "assessed",
          "evidence-backed",
          "third-party-attested"
        ],
        "lifecycle": [
          "proposed",
          "active",
          "revalidated",
          "superseded",
          "expired",
          "withdrawn",
          "revoked"
        ]
      }
    },
    "invariants": [
      "Every assertion identifies one person, one definition version, one kind, one asserter and a validity interval.",
      "Scale and level are both present or both absent; a level is meaningless without exact scale version.",
      "One person and definition may have multiple concurrent assertions; latest is never synonymous with current.",
      "Self-assessed, assessed, evidence-backed and third-party-attested kinds remain disjoint and visible.",
      "An assessment act may justify an assertion but is never the assertion.",
      "Self-assessment never inherits verification or third-party assurance.",
      "A mapping never creates or translates a person assertion.",
      "Course completion and role occupancy never create an assertion.",
      "Credential, qualification or licence title similarity never proves claim coverage.",
      "Expired or revoked supporting artifacts cannot support a current-evidence query but remain historical evidence.",
      "Current is derived at an as-of instant from assertion validity, evidence coverage and artifact status; it is never a stored eternal flag.",
      "Changing person, definition, scale, level, kind, asserter, basis or assurance creates a successor and never rewrites history.",
      "Disclosure is purpose-bound, least-privilege and preserves self-declared status.",
      "No identifier is allocated until registry reservation is approved."
    ],
    "holds": [
      "Registry allocation is pending and identifiers remain null.",
      "Privacy, assurance, artifact-coverage and revalidation policy require canonical governance.",
      "Assessment and artifact bindings inherit base-model publication holds.",
      "Fixtures are declarative and unexecuted; package conversion and live verification remain pending."
    ],
    "candidateRevision": 2
  },
  "fixtures": {
    "wmPer009": [
      [
        "same-label-different-type",
        "negative",
        "One scheme uses the same label for a SkillDefinition and CompetencyDefinition.",
        "The two definitions remain distinct by type and stable code."
      ],
      [
        "cross-scheme-label-match",
        "negative",
        "ESCO and a local scheme share a preferred label.",
        "No identity merge occurs; only a governed directional mapping may relate them."
      ],
      [
        "definition-holding-collapse",
        "negative",
        "A definition record receives personRef and currentLevel.",
        "The record is invalid because holdings remain external."
      ],
      [
        "deprecated-successor",
        "positive",
        "A definition is deprecated and replaced by two narrower successors.",
        "Historical references resolve unchanged and successor links are explicit."
      ],
      [
        "course-completion",
        "negative",
        "A learner completes a course mapped to a competency.",
        "No proficiency or capability assertion is created."
      ],
      [
        "role-occupancy",
        "negative",
        "A person occupies a role requiring a competency.",
        "No capability assertion is created."
      ],
      [
        "assessment-pins-old-release",
        "positive",
        "A finalized assessment pins definition release v2 after v3 is issued.",
        "The result remains bound to v2 and is never silently recomputed."
      ],
      [
        "mapping-not-equivalence",
        "negative",
        "A purpose-qualified mapping is used as cross-scheme identity equivalence.",
        "The inference is rejected and declared loss remains visible."
      ]
    ],
    "scale": [
      [
        "same-number-different-scale",
        "negative",
        "Local v2 level 4 and SFIA v8 level 4 share a numeral.",
        "No equivalence is inferred."
      ],
      [
        "lossy-directional-map",
        "positive",
        "Local Proficient maps toward SFIA 4 for development planning with residual loss.",
        "The mapping pins both versions, direction, purpose, authority, loss and non-reversibility."
      ],
      [
        "reverse-not-implied",
        "negative",
        "A consumer reverses a one-way local-to-SFIA mapping.",
        "No reverse mapping or assertion is produced."
      ],
      [
        "transitive-not-implied",
        "negative",
        "A→B and B→C mappings exist.",
        "No A→C mapping or person inference is produced."
      ],
      [
        "scale-version-change",
        "positive",
        "Descriptors change from scale v1 to v2.",
        "A successor version is created and finalized v1 results remain on v1."
      ],
      [
        "mapping-person",
        "negative",
        "A service applies a level mapping directly to a person's assertion.",
        "The operation is rejected; mappings compare scale values only."
      ],
      [
        "missing-not-zero",
        "negative",
        "An assessment has indeterminate result.",
        "No zero level is created."
      ],
      [
        "retired-history",
        "positive",
        "A scale version is retired.",
        "Historical assertions and assessments remain resolvable against it."
      ]
    ],
    "assertion": [
      [
        "multiple-methods-scales",
        "positive",
        "One competency is assessed by manager review on local v2 and work sample on SFIA v8.",
        "Two acts and up to two assertions remain separate; no merged score exists."
      ],
      [
        "self-not-verified",
        "negative",
        "A self-assessment is projected as verified.",
        "The projection is rejected."
      ],
      [
        "course-not-competence",
        "negative",
        "Course completion attempts to create expert proficiency.",
        "No assertion is created."
      ],
      [
        "expired-credential",
        "negative",
        "A supporting credential expired before the as-of query.",
        "Issuance history remains, but it cannot support current competence."
      ],
      [
        "role-not-holding",
        "negative",
        "Role occupancy is treated as evidence of competence.",
        "No assertion follows."
      ],
      [
        "mapping-no-translation",
        "negative",
        "A local-scale assertion is translated to SFIA via a scale map.",
        "No target assertion is minted."
      ],
      [
        "latest-not-current",
        "negative",
        "The newest assertion is expired while an older independent assertion remains valid.",
        "Current is computed per assertion at the as-of instant; newest is not automatically current."
      ],
      [
        "title-not-coverage",
        "negative",
        "A certificate title matches a competency label without claim binding.",
        "Coverage is not inferred."
      ],
      [
        "successor-history",
        "positive",
        "A new assessment changes the supported level.",
        "A successor assertion is created and prior assertion remains resolvable."
      ],
      [
        "privacy-projection",
        "positive",
        "A consumer requests only verified claims for staffing purpose.",
        "The response minimizes fields and excludes self-assessed details without authority."
      ]
    ]
  },
  "sourceFacts": {
    "WM-PER-009": "Reserved ID exists but current spec is missing; completion must remain definition-only.",
    "bases": "All relevant supplied bases are reviewable drafts and carry inherited holds.",
    "relations": "No approved competency relation rows are available.",
    "runtime": "No executable semantics are proposed; fixtures are declarative and unexecuted."
  },
  "providerComparison": "# EM-PEO-03 provider comparison\n\nClaude and Grok converge on a definition-only completion of reserved `WM-PER-009`, identifier-unassigned `Proficiency Scale` and `Person Capability Assertion` candidates, a Competency Assessment profile over `WM-ACT-034`, and reuse of `WM-PER-008`, `WM-XCT-017`, and the `WM-PER-013` licence profile. Both prohibit course or role inference, current competence from expired artifacts, identity merging from equal labels, and exact or reversible cross-scale equivalence.\n\nClaude sharpened the definition-versus-holding identity split, bitemporal evidence and assessment boundaries, and the difference between concept and level mappings. Grok sharpened the exact definition/scale identities, disjoint assertion kinds, current-as-query rule, non-transitive person inference and the minimum model set. External standard details and neighboring ownership remain held unless pinned in the frozen dossier.\n"
}
```
