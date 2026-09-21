# Migration and rollback

Version 0.1.0 introduces a new optional reference profile. It does not mutate an existing Dimension or revise the underlying 011/036 semantic basis. The published parent 0.3.1-enterprise.1 adds discovery and review metadata around unchanged legacy synthesis; the profile explicitly pins 0.3.0-research.1 semantic files.

Adopt in a new synthetic Dimension first. Obtain the published WM-XCT-040 0.1.1 composer and the trusted Vercy skill, verify their tool-pins.json hashes, then run:

```text
python acceptance.py --composer /trusted/wm-xct-040 --skill /trusted/vercy --report local-acceptance.json
```

The harness uses its own temporary directories and leaves existing Dimensions alone. It is a fixed 2026 acceptance fixture, not an indefinitely valid production policy. Expired fixture windows fail closed; do not silently backdate a production clock to make it pass.

Existing bare-ID tables, matcher scores and previously merged records require manual semantic mapping. Retain source strings, qualification, occurrence identity, referent reference, evidence, reception history and uncertainty. A lossy table cannot be upgraded by inventing missing timestamps or source assignment IDs. Live import admits receipt-stamped transitions; historic bulk restoration needs a separately reviewed provenance workflow.

Unsupported schema versions are rejected. No automatic downgrade is offered. Rollback means ceasing use of the optional profile and preserving its complete evidence package; it does not erase a history or reverse changes in a source system. Correct a wrong claim with an authorized retraction and a new assertion where fixed content changes.

One frozen policy includes both read and write declarations. Policy rotation invalidates the pins. Continued use after expiry requires a reviewed replacement policy/claim set and is not implemented as an automatic migration here.
