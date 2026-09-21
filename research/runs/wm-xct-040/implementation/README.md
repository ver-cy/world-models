# Compose models for a new company Dimension

WM-XCT-040 Model Composition Resolution, 0.1.1. A shared contract and reference implementation.

This model records which exact model releases a Dimension uses, who authorized them, which dependencies are mandatory, which bytes were verified, and which data is ready to be written. It provides one composition contract. It does not replace the Vercy kernel or the Organization, Legal Entity, Organizational Unit and Employee models.

The publication is available for use and further review. Research assurance remains `reviewable-draft`; complete enterprise architecture and universal compatibility are not claimed. The research dossier records the independent reviews and remaining limitations. Version 0.1.1 publishes English documentation with unchanged executable code and schemas. Technical review evidence refers to the 0.1.0 implementation, not to a new review of this translation.

## Package contents

- `model-spec.md`: boundaries, types, relationships, states, authority, time, data mastership and migration.
- `field-catalog.json`: fields, types, requiredness, sources and owners.
- `whole-object-coverage.json`: five descriptive facets for each of the nine contract types.
- `composition-plan.schema.json`, `policy.schema.json`: executable JSON Schema 2020-12 schemas.
- `composition.py`: validation of the exact model selection and staging of verified files.
- `bootstrap_dimension.py`: creation of a new Dimension using a trusted local Vercy skill.
- `crosswalk.json`, `kernel-boundary-decision.json`: mappings to existing models and the boundary decision.
- `examples/`: synthetic scenarios, policies, exact version pins and copies of published packages.
- `test-results.json`, `acceptance-results.json`: recorded test results.

## A reproducible example

Extract the complete package. Use Python 3.12+ and `jsonschema[format-nongpl] >=4,<5`. Supply the Vercy skill path explicitly, pointing to a trusted local copy from the official Vercy distribution. The composer does not download or execute package code automatically.

```text
python -m pip install "jsonschema[format-nongpl]>=4,<5"
python test_composition.py
python acceptance.py --skill /trusted/vercy/skills/vercy --report acceptance-local.json
```

`acceptance.py` creates temporary test Dimensions and removes only its own temporary data after verification. It explicitly runs the verified example validator for nested data. The ordinary composer does not run that code automatically.

To retain a separate tutorial Dimension:

```text
python composition.py validate examples/startup/plan.json --assets examples/assets --policy examples/startup/policy.json --lock examples/startup/current.lock
python composition.py stage examples/startup/plan.json --assets examples/assets --policy examples/startup/policy.json --lock examples/startup/current.lock --target /existing-parent/startup-stage
python bootstrap_dimension.py --stage /existing-parent/startup-stage --policy examples/startup/policy.json --lock examples/startup/current.lock --skill /trusted/vercy/skills/vercy --target /existing-parent/startup-dimension --name "Synthetic startup" --namespace urn:dimension:synthetic:startup
```

Replace the paths with yours. The parent directory must exist; the target directories must be new. `--namespace` must exactly match `dimensionId` in the plan and the independently supplied policy. Bootstrap creates the structure and registries; organization data is added separately. `acceptance.py` demonstrates that next step.

## Use with your company

The synthetic example policies do not authorize operations on your company. The Dimension owner independently defines its identifier, actors, purpose, allowed models, sources and policy validity period. The plan references the SHA-256 digests of that policy and the starting lock file. Changes to those documents require recalculating their corresponding digests.

For each selected model, specify its exact version and the SHA-256 digest and size of its specification and AGENTS.md. Separate mandatory dependencies (`requires`) from optional links (`references`). The closure contains every mandatory dependency declared in the plan and excludes packages outside that graph. Dependencies are not extracted automatically from specification prose. Cycles, ambiguous versions and namespace conflicts are rejected.

`semantic-only` stores a semantic specification without claiming that its fact schema is ready. For `native-binding`, explicitly supply a runtime schema bound to the exact specification bytes. A nested snapshot additionally requires a closed data schema and a separate domain validator. Successful V3 validation does not replace validation of the nested object's contents.

The tutorial plans expire at the end of 2026. After expiry, `validate --at` can check their historical composition at a date when they were valid. New creation requires a new valid policy and plan; a historical validation date does not authorize writes.

## What the scenarios demonstrate

| Scenario | Verified behavior | Boundary |
|---|---|---|
| Startup | New Dimension, Organization, one object and name fact, V3 validation | The name only, not a complete organization schema |
| Group | Organization data and Organizational Unit as a semantic package | No runtime schema is invented for the unit |
| AI team | Organization and a published Performance Case example, V3 and separate nested validation | Synthetic example, not a real personnel evaluation system |

Every scenario rejects repeated creation over an existing Dimension while preserving its data.

## Migration and recovery

This implementation creates new Dimensions only. An existing Dimension requires a separate migration plan covering backup, loss analysis and data conversion. Automatic upgrades and downgrades are not supported.

An ordinary failure cleans up only the operation's temporary directory and lease. After a process crash, inspect the remaining lease owner, confirm that its process is no longer active, and inspect the receipt before recovery. Do not remove leases blindly. Directory rename is the activation point on the tested local filesystem; distributed transactions and power-loss durability are not claimed.

The contract does not implement enterprise IAM, publisher signature verification, ELMM minimum-version selection, execution of every domain rule, or changes to existing Dimensions. The `published` lifecycle status does not remove these limits.

Specifications must be JSON or JSON preceded by one leading `#` line: Vercy's JSON-compatible YAML form. General YAML is rejected. The three example packages were compared byte for byte with their published ver.cy versions. This adapter supports the `commercial-company` preset.

The examples are reproducible with their current plans through December 31, 2026; later runs need a new policy and plan. Copied semantic specifications and AGENTS.md files retain their source provenance. The minimal Organization name binding was authored for the initial release; the Performance example uses an existing published reference binding. A nested schema and validator must be present, but running them is a separate step and does not happen automatically during Dimension creation. Activation evidence covers Windows and cooperating processes that honor the lease.

Run tests with ordinary Python, without `-O`; optimized mode is explicitly rejected. The acceptance test loads the nested validator from the installed copy and records its SHA-256 digest in the report.
