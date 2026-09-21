# Research comparisons

**S01 — 2022-11-15 Candidate Recommendation Draft; Principles and vocabulary; temporal reference systems.** Temporal topology and reference systems need explicit interpretation. Half-open storage and receipt history are our additional choices, not an OWL-Time conformance claim. [Primary source](https://www.w3.org/TR/2022/CRD-owl-time-20221115/).

**S02 — 2015-09-01 Recommendation; 3.10 History; 3.11 Legal state configurations.** A history pseudostate restores a prior active configuration. It is not an archival audit ledger. Parallel configurations cannot always be represented by one status code. [Primary source](https://www.w3.org/TR/scxml/).

**S03 — Living documentation read 2026-09-21; System time; Valid time; Behind the scenes.** Distinct system and valid axes support late corrections and earlier recorded views. The application contract chooses full snapshots, not XTDB SQL portion updates. [Primary source](https://docs.xtdb.com/about/time-in-xtdb.html).

**S04 — Living documentation read 2026-09-21; Temporal columns and bitemporality; transaction processing.** Database temporal columns and half-open periods inform the narrow reference. Engine imports can have different clock controls; no automatic adapter or SQL conformance is claimed. [Primary source](https://docs.xtdb.com/concepts/key-concepts.html).

**S05 — Living vendor documentation read 2026-09-21; How does temporal work?; How do I query temporal data?.** Columns named ValidFrom/ValidTo in this system-time example use transaction begin time. Import must not mistake them for domain effective time. Equal transaction instants motivate a separate sequence. [Primary source](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal/overview?view=sql-server-ver17).

**S06 — Living architecture guidance read 2026-09-21; Solution; Pattern advantages; concurrency example.** Append-only domain-event replay is an alternative. Optimistic expected-version checks inform our guarded writes; this companion records assertion snapshots rather than pretending to execute domain events. [Primary source](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing).

**S07 — 2.0.0; Items 1–3, 9–11.** API compatibility promises require a defined surface. The companion uses only the normal numeric triplet as a binding grammar and infers no compatibility from a label. [Primary source](https://semver.org/spec/v2.0.0.html).

Full snapshots were chosen as an inspectable single-scope reference; deltas, multi-master adjudication, general calendar arithmetic and statechart execution remain outside it. These are design proposals supported by synthetic cases, not universal claims. See boundary-decision.md for provider reconciliation and exact limits.
