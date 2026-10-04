Continuation of the same frozen R2 no-tools audit. ACK only; do not audit yet.
FRAGMENT 15/15
PAYLOAD BEGIN
BEGIN FILE crosswalk.json sha256:682ce21aaaca1ead153910f96ef857f24c40aa16aa46a9cab732494695ba0f9d
Complete JSON values, minified for review; spec.model.scope uses the explicitly identified identical earlier text. SHA identifies original formatted bytes.
{"mappings":[{"from":"WM-XCT-001","version":"0.3.1-enterprise.1","digest":"sha256:fa942556a3f460729db2e94b24d1efd4d33ee2e5fb0b1deed3ce040756acf474","relation":"overlap","decision":"semantic-reference-only","limits":"Governance comparison; no inherited mandate schema"},{"from":"WM-XCT-012","version":"0.3.0-research.1","digest":"sha256:aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5","relation":"overlap","decision":"semantic-reference-only","limits":"Attribution/history comparison; no fetching or checkpoint engine"},{"from":"Enterprise Identity","version":"0.1.0","digest":"sha256:2cf9808893dfbf33e36d960e04fbc1ff0b1308b27d27f49187b1851fad875163","artifact":"model-spec.md","decision":"separate aboutness profile","limits":"Published four-kind Identity schema cannot represent board ABOUT Project or dataset-record ABOUT Dataset. No same-as or exactMatch inferred."},{"from":"Enterprise Fact Authority","version":"0.1.0","digest":"sha256:cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582","decision":"external fact selection","limits":"Its full-register one-receipt-per-second contract supplies neither durable connector progress nor destination atomicity. Adapter deferred."},{"from":"Enterprise Assertion Provenance","version":"0.1.0","digest":"sha256:a8f41fb65aa5892c884731c9c4d06402637bf26bc55ab53a6ad9c7fbc34a44f0","decision":"external provenance alignment","limits":"Source capture and evidence assessment remain separately governed. This implementation does not emit its records automatically."}]}
END FILE crosswalk.json

BEGIN FILE invariants.md sha256:6c45ef57843db005db48470b7183d5ccf4b5e197a72ba964109bc46790ecfac8
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
# Invariants

1. A source record is not a business subject; aboutness never creates or merges one.
2. Qualified lineage preserves exact source/resource/scheme/key/generation; unknown generation is non-joinable.
3. Source-instance generation, record generation and SyncEpoch are independent.
4. Every mapping activation enforces one active claim per complete lineage/purpose.
5. Changed anchors need a new mapping ID; historical occurrence pins never change.
6. Current authentication/authorization precedes receipt lookup; full archives stay privileged.
7. Batch identity is scope/epoch-wide, not actor-scoped; exact own retry requires current intake rights.
8. Content identity excludes attempt/head/fence/computed pins; ordered input descriptors remain exact.
9. One local transaction retains receipt, occurrences, quarantine and head; conservation always holds.
10. Closed epochs refuse every COMMIT; authorized historical READ is separate.
11. Source tokens are opaque; only local committed progress orders heads.
12. Source event, acquisition and host receipt times remain distinct; missing source time stays null.
13. Complete accounting alone proves neither source consistency nor visibility.
14. Absence comparison needs explicit comparable ordered rounds and emits proposals only.
15. Archives are historical-only and cannot restore writable acquisition authority.
16. Native outer validity never substitutes for installed nested replay and exact predecessor preservation.
17. Hashes do not establish source authenticity, secret safety or latest-owned-store continuity.
18. Provider studies and static audits are distinct from executed tests and production readiness.

END FILE invariants.md

BEGIN FILE migration.md sha256:a22cc436f19c27715422667a52ce8b136960292e3b1702e32953ffcb79684101
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
# Migration and recovery

This release introduces an original companion, not a subtype or replacement of a World Model. Existing source keys need explicit qualification and continuity evidence; unmatched kinds/unknown generations cannot be silently coerced. Export source descriptions and review mappings before acquisition.

There is no writable archive migration. inspect_import accepts an exact supported archive only as historical evidence and emits a structured LossReport on unsupported/inconsistent input. No lossy conversion, token resume or origin-host takeover is attempted. A new host needs a new local register/epoch and verified fresh baseline. A normal process restart can reopen the current locally owned database after host continuity verification. Old/cloned databases cannot be detected internally.

Future schema/algorithm changes require new pinned versions and separately reviewed migrations preserving lexical keys, generations, purpose, mapping revisions/pins, accepted and quarantine ordinals, grants/catalogue chronology and receipt/head history. Removing a native projection does not undo a commit. Database rollback is not a semantic correction; retain evidence and reconcile externally.

END FILE migration.md

BEGIN FILE lifecycle/transitions.md sha256:0f6689d428735d7860f27d97ab194a8b966302cc0210f10d97a63230bea8afaa
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
# Guarded lifecycle

Mapping: proposed -> active/disputed/retracted; active -> disputed/retracted; disputed -> active/retracted; retracted terminal. Activation checks catalogue/pair, uniqueness and corrected-predecessor retirement. Changed immutable anchors need a new ID.

Epoch: new -> open -> closed; one open per scope. Open starts fence 1/head null/progress 0. Admin advances fence; admitted first batches advance progress/head atomically. All rounds must be sealed before close. Closed epoch permits no commit even for an old key; current authorized read is separate.

Round: opened -> pages in contiguous order -> sealed once. Terminal stops later pages. Incomplete/errored rounds can be sealed without completeness. Snapshot assessment never changes mappings or subjects.

Batch: new admitted key -> immutable committed receipt; exact own retry returns prior acknowledgement without an event. Changed content, principal collision and stale new-admission preconditions retain a restricted diagnostic. Unauthorized/invalid calls and exact-retry telemetry are external. Quarantine stays open; resolution is deferred.

END FILE lifecycle/transitions.md

BEGIN FILE README.md sha256:d3726ed330cf447285fa9f5a055201d4ecfb0ab8ff8e03a8dc9a53b17242cf3b
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
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

END FILE README.md

BEGIN FILE requirements.txt sha256:756cc9e506ae4ee1a6f6c0507088b5cfc0dc8ba350fb2d2d46f1ffa72033adb6
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
jsonschema==4.26.0

END FILE requirements.txt

PAYLOAD END — FRAGMENT 15/15
