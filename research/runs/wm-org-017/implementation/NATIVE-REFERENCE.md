# Optional native Dimension reference binding 0.1.0

This supplementary binding is separate from the published semantic specification. Codex prepared it after the provider reviews. It is a bounded demonstrator, not a universal installer fix or production HR adapter.

The generic installer currently downloads and pins semantic packages, but omits the `agents`, `specification`, `specificationDigest` and `runtimeSchema` fields required by the newer V1-V3 validator. The first four-package installation therefore failed V3 validation. Keep that failure visible; do not report every published package as runtime-ready.

For WM-ORG-017 alone, a reference binding stores one entire, semantically validated case snapshot as an immutable fact at `performance.case.snapshot`, on the single canonical case object. It preserves the case's external master references and internal identities. It does not turn Person or Employment into locally mastered copies. Native object state describes whether the record is active; case.value.state describes the review workflow.

To reproduce in an authorized synthetic company Dimension:

1. Create a fresh Dimension with Vercy Skill using the commercial-company preset. Install the published `vr.wm-org-017` semantic package with `reconcile_models.py` and verify the specification digest.
2. Copy `runtime-model.reference.json` alongside the pinned AGENTS.md and spec.yaml. In this model's `registries/meta-models.yaml` entry, set `agents` and `specification` to those relative file paths, `specificationDigest` to the exact `vercy.lock` digest, and `runtimeSchema` to the relative path of the copied runtime-model.reference.json. Keep id/version identical to the pin. This is explicit reference-profile adoption; do not overwrite other model entries or change the immutable spec.
3. Run `vercy.py validate <dimension>` before writing data. Validate the value from `native-fact.reference.json` with `validate_examples.errors(value)` as well as instance.schema.json. The supplied `validate_examples.py` demonstrates that semantic gate and its negative fixtures; Python requires `jsonschema`.
4. Append `native-object.reference.json`, then `native-fact.reference.json` through the Vercy Skill `write_record.py <dimension> object|fact <file>`. The writer provides an atomic lease, immutable record IDs, validation and rollback. Do not copy runtime records directly into a live Dimension.
5. Run `vercy.py validate <dimension>` again and preserve both the native report and the nested-case validation result. Future corrections need new immutable fact IDs and explicit supersedes links; object changes require the expected current head.

Only use the supplied synthetic examples for this demonstrator. Real cases require a reviewed owner, authority, master-system resolution, access/retention policy and import adapter. `V3` verifies native record structure and cross-record semantics; it does not validate the nested review workflow. The companion semantic validator is a separate required check. Bypassing it is not a conforming use of this reference profile.

Production multi-record transactions, rollback across the object-plus-fact pair, cross-case calibration and full profile migration remain outside this demonstrator. The public evidence folder records the successful one-object/one-fact test and the generic installation failure separately.
