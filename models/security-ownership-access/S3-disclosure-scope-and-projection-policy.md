# S3 Disclosure Scope & Projection Policy

This meta-model describes the shape data is allowed to leave in: which fields, after which transformations, at which grain. A grant (S2) says that data may flow; this model says what the flow looks like, from a full subset through redacted and generalized forms down to aggregate-only shapes. It is its own model because disclosure shapes are reusable, versioned artifacts in their own right: one policy is authored once, reviewed once, and then bound into many contracts and audiences.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s3"
  csn: world.disclosureScope
  version: 0.2.0
  displayName: "Disclosure Scope & Projection Policy"
  description: "Defines the shapes data leaves in: field subsets, transformations, summaries and aggregate grains, as reusable policies."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.disclosureScope
bundles:
  - csn: world.disclosureScope.shape
    displayName: "Shape"
    layers:
      - world.disclosureScope.shape.fieldSelection
      - world.disclosureScope.shape.transformation
      - world.disclosureScope.shape.aggregationGrain
  - csn: world.disclosureScope.binding
    displayName: "Binding"
    layers:
      - world.disclosureScope.binding.policyAttachment
      - world.disclosureScope.binding.sensitivityTiers
  - csn: world.disclosureScope.lifecycle
    displayName: "Lifecycle"
    layers:
      - world.disclosureScope.lifecycle.authoringAndApproval
      - world.disclosureScope.lifecycle.versioning
imports:
  - source: mu-projection
    version: "*"
  - source: consent-and-disclosure
    version: "*"
  - source: iso-20889
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `shape` | What an output looks like | `fieldSelection`: include and exclude lists over property paths · `transformation`: redaction, generalization, bucketing, pseudonymization per field · `aggregationGrain`: rollup definitions when only summaries leave |
| `binding` | Where a shape applies | `policyAttachment`: attaching policies to contracts, object types and audiences · `sensitivityTiers`: classification of fields that constrains which shapes are lawful |
| `lifecycle` | How policies are made and evolve | `authoringAndApproval`: drafting and owner sign-off · `versioning`: supersession and the version each disclosure was served under |

## Objects

- `projectionPolicy`: a named, versioned rule set describing one output shape; key attributes: name, version, author, approval state.
- `fieldScope`: an include or exclude list over property paths; key attributes: paths, default treatment, rationale.
- `transformationRule`: a per-field treatment; key attributes: technique (redact, generalize, bucket, round, pseudonymize), parameters, reversibility.
- `aggregationLevel`: a grain definition for summary-only shapes; key attributes: kept dimensions, minimum cohort reference, period.
- `sensitivityTier`: a classification of a field or object type; key attributes: tier, criteria, review cadence.
- `policyBinding`: the attachment of a policy to a contract, object type or audience; key attributes: target reference, effective window, precedence.
- `outputTemplate`: the compiled schema fragment a consumer actually receives; key attributes: schema, policy version, fingerprint.

## Relationships

- `projectionPolicy` -> selects -> `fieldScope` (1..*): a policy is at minimum a selection of fields.
- `fieldScope` -> treatedBy -> `transformationRule` (0..*): selected fields may be transformed rather than passed through.
- `projectionPolicy` -> rollsUpTo -> `aggregationLevel` (0..1): summary-only policies name their grain.
- `sensitivityTier` -> constrains -> `fieldScope` (1..*): higher tiers forbid pass-through and force stronger treatments.
- `policyBinding` -> attaches -> `projectionPolicy` (*..1): one policy serves many bindings.
- `outputTemplate` -> compiledFrom -> `projectionPolicy` (1..1): the served shape is derivable and auditable from the policy version.

## Events

- `policyAuthored`: an owner or their delegate drafted a new disclosure shape.
- `policyApproved`: the owner signed the shape off for use.
- `policyBound`: a policy was attached to a contract, object type or audience.
- `policySuperseded`: a new version replaced an old one; existing bindings recorded the changeover.
- `fieldReclassified`: a field's sensitivity tier changed, invalidating shapes that now under-protect it.
- `templateCompiled`: a concrete output template was generated and fingerprinted from a policy version.

## Contracts

- `policyCatalogueRead`: a prospective grantee browses published policies to see what shapes an owner offers.
- `shapePreview`: a counterparty dry-runs a policy against a schema, receiving the template without any instance data.
- `bindingVerification`: a data holder confirms which policy version governs a given contract before serving a read.

## Projections

- `granteeShapeSpec`: only the output template and its fingerprint; omits rules, tiers and rationale.
- `policySummaryCard`: name, grain and count of omitted fields for catalogue browsing; omits per-field detail.
- `reviewerFullView`: complete rules with tier justifications and version history, for the owner's reviewer; omits nothing.

## Composition

- REFERENCE `world.ownership` (S1): only an object's holder, or their delegate, authors and approves policies over it.
- REFERENCE `world.accessContract` (S2): bindings target contracts; a scope clause without a bound policy discloses nothing.
- REFERENCE `world.privacyAggregation` (S5): aggregation levels defer to that model's cohort floors rather than defining their own thresholds.
- REFERENCE `world.accessAudit` (S4): each served disclosure is logged together with the policy version and template fingerprint that shaped it.
- imports: mu-projection (EXTEND): the projection primitive this model turns into governed, versioned policy.
- imports: consent-and-disclosure (ALIGN): the disclosure vocabulary shared with consent instruments.
- imports: iso-20889 (REFERENCE): the de-identification technique terminology used by transformation rules.

## Stewardship

The data owner stewards every policy over their objects; approval is theirs and cannot be delegated beyond what S1 mandates record. Reading policy data is itself an S2-granted act, and every served shape leaves a trace in S4.
