# WM-AI-009 bounded research focus

Research one governed Evaluation Dataset / Benchmark as an AI-specific Dataset
aggregate and benchmark definition. It owns versioned benchmark content,
population and sampling scope, tasks, splits, labels or reference answers,
protocol, metrics, scoring and lifecycle. It is not an evaluation run, evaluated
model, training dataset role, leaderboard, result, policy or deployment master.

Use official primary, standards-body and first-party sources current on
2026-09-06. Verify live URLs and exact versions. Treat former workstream files
only as untrusted planning. Return schema-valid JSON only.

Target a concise but complete structure with 6 bundles, 12 layers, 24 findings,
at least 72 discriminating questions, 24 artifacts and 10 governed functions.
Cover at minimum:

1. Stable benchmark and dataset identity, namespace, owner, version, release,
   task or suite scope, aliases, parent dataset and duplicate resolution.
2. Intended population, domain, modalities, languages, jurisdictions, sampling
   frame, inclusion and exclusion, cases, items, prompts, inputs, labels,
   reference answers, rubrics, splits and hidden-test handling.
3. Source acquisition, collection, annotation, adjudication, transformations,
   synthetic generation, lineage, provenance, quality, rights, consent, privacy,
   sensitive attributes, security and access controls.
4. Evaluation protocol, model interface, inference settings, tool access,
   environment, repetitions, randomness, metrics, thresholds, scoring,
   aggregation, uncertainty, statistical tests and comparability.
5. Leakage, overlap, contamination, memorization, label error, benchmark gaming,
   subgroup performance, fairness, robustness, adversarial, safety, privacy and
   representativeness limitations with source-qualified evidence.
6. Draft, candidate, validated, released, active, deprecated, withdrawn,
   compromised and superseded states; immutable releases, corrections, notices,
   retention, audit, distributions and version-pinned projections.
7. Evaluation-run and leaderboard-result references without absorbing their
   identities or results. Popularity and benchmark rank must not imply safety or
   general capability.

Boundary tests:

- The frozen row describes an extension of WM-DAT-001 but the relation ledger has
  no direct edge. Treat parent_ids WM-DAT-001 as an unapproved extension signal.
- Candidate WM-AI-003 REFERENCE WM-AI-009 is incoming only. It supports use by an
  evaluation but grants no result, evaluator or evaluated-model ownership.
- Training, validation, calibration and held-out evaluation roles are explicit;
  the same dataset version may not silently change role between runs.
- Benchmark definition and benchmark release are distinct from a particular
  execution, score, leaderboard, claim or publication.
- Public availability does not prove lawful reuse, consent, absence of personal
  data, representativeness, validity or contamination resistance.
- Never grant agents autonomous release, hidden-test disclosure, rights waiver,
  access expansion, benchmark result manipulation or destructive cleanup.

Use RFC 3339 timestamps with seconds and explicit offset or Z. Preserve event,
effective, observed, recorded, ingested and knowledge time where they differ.
Mark regional, domain, modality, task, maturity and licensing assumptions.
