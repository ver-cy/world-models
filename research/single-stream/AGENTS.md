# Vercy canonical research stream

- Repository: `R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models`
- Branch: `feat/mega-model-registry`
- Queue: `research/status.csv`
- State: `research/single-stream/STATE.json`
- Log: `research/single-stream/LOG.md`
- Consolidation record: `research/single-stream/CONSOLIDATION-2026-09-06.md`
- Publication target: `https://ver.cy/models/`

This is the only active subject-model research stream. Never resume or write to
`research/stream-01` through `research/stream-06` or their worktrees. Their
branches, dirty working copies and untracked files are preserved as read-only
evidence and prepared inputs.

## Processing order

1. Work only in the canonical repository and verify the exact branch and a
   clean tree before starting a model.
2. Regenerate `research/status.csv`; choose the lowest-sequence row whose
   `validation_status` is not `valid`. A ready salvaged result may be integrated
   out of order only once, then normal lowest-sequence order resumes.
3. Reuse the matching former-workstream dossier only as untrusted preparation.
   Do not copy its claims or provider attribution without verification.
4. Freeze one model boundary. Make one bounded Claude attempt and one bounded
   Grok attempt through the safe runners unless a terminal manifest already
   exists. A timeout, authentication failure, invalid JSON or missing provider
   is recorded and never retried for the same model in later heartbeats.
5. Validate every admitted external result. When neither external result is
   usable, Codex produces a source-grounded `codex.result.json` under the active
   provider waiver. Compare admitted results, run a separate no-tools
   adversarial adjudication, synthesize and validate. A valid result with no
   critical conflict may publish as `reviewable-draft`; visible provider and
   source-verification holds are mandatory and must not be hidden.
6. Generate `AGENTS.md`, `spec.yaml`, the human card and publication manifest.
   Update shared status, the site runtime catalogue, Bitrix import and all
   generated indexes. Deploy, migrate, run HTTP and SEO/AEO/GEO checks, then
   make one model commit and push it.
7. Continue with the next queue row without asking the owner for routine
   approval. Stop only for unsafe secret handling, an unresolved critical
   semantic conflict, corrupt canonical state or a production failure that
   would make the public catalogue inconsistent.

## Throughput rule

Provider perfection is not a completion gate. Claude and Grok are bounded
best-effort external passes. A provider failure does not authorize fabricated
evidence or invalid structure; the transparent Codex fallback and no-tools
audit preserve forward progress. Prefer a smaller valid reviewable draft with
explicit holds over an indefinitely blocked ideal draft.

Catalogue scale is tiered. Deep Vercy specifications remain individually
validated. External standards and classifiers are indexed as external entries,
and high-cardinality domain profiles are generated deterministically from
licensed/open classifiers and materialized on demand. Never manufacture a
million near-duplicate deep specifications merely to increase a counter.

## Publication authority

The repository owner explicitly authorized autonomous publication of valid
reviewable drafts to the Vercy catalogue. This does not authorize secret
disclosure, arbitrary external writes, deletion of evidence or representing a
reviewable draft as canonical.
