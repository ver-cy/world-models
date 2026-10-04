# Enterprise Classification Review

An original offline companion for company classification sets, narrowing profiles and explicit correspondence review. Public documentation is English. Research assurance remains reviewable-draft; see review.json for actual study/audit dispositions.

Extract the complete package. Use Python3.12+ with jsonschema[format-nongpl]>=4,<5. The examples use invented Project/Document categories and independently supplied synthetic host contexts.

```text
python test_classification.py
python fixtures.py
python acceptance.py --composer /trusted/wm-xct-040/versions/0.1.1 --skill /trusted/vercy/skills/vercy --report acceptance-local.json
```

Use classification_review.review(packet, host_context, authenticated_actor, purpose, current_UTC_seconds) from a trusted host. Supply host context independently; do not approve a packet merely because it includes an approval claim. The command-line form reads separate files and emits an assessment:

```text
python classification_review.py --packet packet.json --host host-context.json --actor urn:company:reviewer --purpose classification-review
```

The host establishes source rights, completeness, current identity and approval competence. Before actual adoption, read AGENTS.md, model-spec.md, model-fields.md, adoption-limits.md, migration.md and bindings/native-v3.md. No live business object is changed; effects is empty. A candidate-only result needs a separate authorized host workflow.
