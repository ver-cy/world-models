# N6 Model & Ontology

This meta-model describes models and ontologies as first-class objects of the world: meta-models, schemas, vocabularies and ontologies with registered identity, versions, semantic fingerprints, alignments to other models, and assessed conformance. It is its own model because the ecosystem's semantic assets need the same registry discipline as any other asset, and because datasets, software and standards all point into this registry rather than describing their schemas ad hoc.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n6"
  csn: world.modelOntology
  version: 0.2.0
  displayName: "Model & Ontology"
  description: "Models, schemas and ontologies as registered assets with versions, fingerprints, mappings and conformance."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.modelOntology
bundles:
  - csn: world.modelOntology.registry
    displayName: "Registry"
    layers:
      - world.modelOntology.registry.modelIdentity
      - world.modelOntology.registry.versionAndFingerprint
  - csn: world.modelOntology.semantics
    displayName: "Semantics"
    layers:
      - world.modelOntology.semantics.structureDescription
      - world.modelOntology.semantics.mappingAndAlignment
  - csn: world.modelOntology.conformance
    displayName: "Conformance"
    layers:
      - world.modelOntology.conformance.conformanceProfile
      - world.modelOntology.conformance.validationEvidence
imports:
  - source: meta-universe-mmas
    version: "*"
  - source: w3c-owl
    version: "*"
  - source: w3c-skos
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `registry` | Who the model is and which state it is in | `modelIdentity`: models, kinds, stewards, namespaces · `versionAndFingerprint`: released versions and their semantic fingerprints |
| `semantics` | What the model says and how it relates | `structureDescription`: described bundles, classes, terms · `mappingAndAlignment`: declared alignments between model versions |
| `conformance` | Whether the model meets its claims | `conformanceProfile`: profiles, levels, claims · `validationEvidence`: validation runs and reports |

## Objects

- `model`: a registered model, schema, vocabulary or ontology; key attributes: modelId, namespaceRef, modelKind, stewardRef.
- `modelVersion`: a released state of a model; key attributes: version, releasedAt, changeClass, status.
- `namespace`: the naming scope a model is declared in; key attributes: namespaceUri, prefix, authorityRef.
- `fingerprint`: the semantic fingerprint of a version; key attributes: algorithm, digest, computedAt.
- `mapping`: a declared alignment between two model versions; key attributes: mappingType, coverage, direction.
- `conformanceClaim`: a claimed level against a profile; key attributes: profileRef, level, claimedBy, claimedAt.
- `validationReport`: evidence from a validation run; key attributes: validatorRef, outcome, findingsCount, runAt.

## Relationships

- `model` -> hasVersion -> `modelVersion` (1:N): the release history of the model.
- `modelVersion` -> identifiedBy -> `fingerprint` (1:1): the fingerprint fixes the version's semantics.
- `model` -> declaredIn -> `namespace` (N:1): naming sovereignty over the model.
- `mapping` -> aligns -> `modelVersion` (N:N): field-level equivalences between sovereign models.
- `modelVersion` -> extends -> `modelVersion` (N:N): specialization of an imported model version.
- `conformanceClaim` -> claims -> `modelVersion` (N:1): the claim is about one released state.
- `validationReport` -> verifies -> `conformanceClaim` (N:1): evidence behind the claim.

## Events

- `modelRegistered`: a model entered the registry with identity and steward.
- `versionReleased`: a new version of a model was published.
- `fingerprintComputed`: the semantic fingerprint of a version was fixed.
- `mappingPublished`: an alignment between two models was declared.
- `conformanceAssessed`: a validation run assessed a conformance claim.
- `modelDeprecated`: the steward marked a model or version as superseded.

## Contracts

- `modelUsageLicenseContract`: license terms for reuse of a registered model.
- `registryListingContract`: terms between steward and registry operator for listing and updating entries.
- `conformanceAssessmentContract`: engagement with an assessor for validation and certification.

## Projections

- `publicRegistryView`: identity, current version, fingerprint and conformance level; omits validation findings detail.
- `dependencyGraphView`: the extends and mapping graph between versions; omits descriptive prose.
- `versionDiffView`: what changed between two versions of one model; omits unrelated registry entries.

## Composition

- REFERENCE `world.dataset` (N3): datasets resolve their schema references against this registry.
- REFERENCE `world.softwareProduct` (N4): implementations and validators of registered models are software products.
- REFERENCE `world.identifierNaming` (N8): namespace URIs and model identifiers come from registered schemes.
- REFERENCE `world.documentRecord` (N1): specification texts behind a version are governed documents.
- imports: meta-universe-mmas (ALIGN): registered meta-models are described using the MMAS composition hierarchy.
- imports: w3c-owl (REFERENCE): formalism referenced for ontology-kind entries.
- imports: w3c-skos (REFERENCE): formalism referenced for vocabulary and concept-scheme entries.

## Stewardship

The neutral owner archetype is the model steward, the party accountable for a model's evolution and claims; the registry operator lists entries without owning them. Access to non-public drafts and evidence is always granted by the steward through the catalogue's S1/S2 ownership and access models, with assessment activity audited via S4.
