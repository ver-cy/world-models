# Enterprise Source Synchronization

Model records can describe a company's sources and explain how external records refer to existing business subjects. The bounded Python/SQLite reference demonstrates protected metadata intake, immutable mapping outcomes, retry receipts, quarantine accounting and scope-qualified coverage. It never creates or retires a Project, Person or Dataset.

Version 0.1.0 is currently an unpublished implementation candidate. Research studies and S1/S2 clarification are complete; native installation acceptance and frozen implementation audits are recorded separately in acceptance-results.json and the release review files. Candidate status is not evidence of audit acceptance. Public research: https://ver.cy/enterprise/research/em-xct-08/ .

Read model-spec.md for the exact behavior and limits. build_schema.py generates sync.schema.json. sync_register.py contains the local reducer/storage and privileged archive analysis. fixtures.py creates synthetic startup, international and AI examples. acceptance.py composes and validates three new synthetic native Dimensions with the pinned toolchain. run_tests.py writes an exact-input report. test_sync.py includes actual process-crash and concurrent-writer checks; fault_worker.py is used only by tests.

Install Python 3.12 or newer and the pinned jsonschema dependency from requirements.txt in your own environment. From this package directory run:

```text
python test_sync.py
python fixtures.py ./new-synthetic-examples
```

The example output directory must not already contain the named databases. These commands only create local synthetic files; there are no live connectors. Treat a real operational register and all its exported identifiers, counts, references and digests as restricted. No current-policy disclosure mechanism is carried with copied exports.

Minimum descriptive adoption needs a SourceInstance, a qualified acquisition scope, a separately governed target catalogue and steward-reviewed mapping purpose. Executable adoption additionally needs authenticated host actors, current grants, trusted time, protected evidence storage and an owned current local database. Source and target systems need not include HRIS or ERP. Unknown continuity stays visible rather than being guessed.

Limitations affecting use include a full-history 8 MiB/2,000-event reference budget, no production IAM, no fetching or verification of external evidence, no distributed exactly-once, no writable archive import, no cross-register adapter, no automated quarantine resolution and no universal standards/legal conformance. The startup, international and AI fixtures do not describe any real company.
