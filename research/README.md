# Vercy model research

This directory turns the unified Vercy registry into evidence-backed model
specifications. Dual-provider research by Claude and Grok is the default. The
repository-wide `provider-policy.json` may record an explicit owner-authorized
single-provider waiver when a provider is unavailable or unreliable.

Scope is 401 world-model records plus two separately queued Vercy assemblies
(AISMM and PLMM). The 1,180 external registry entries are standards, schemas,
classifiers and protocols: they receive an alignment/verification pass and are
not forced into an artificial Bundle/Layer hierarchy.

The single queue was paused at sequence 90 (`WM-XCT-037`) and checkpointed in
[`PAUSE-CHECKPOINT-2026-09-04.md`](./PAUSE-CHECKPOINT-2026-09-04.md). The owner
subsequently replaced that execution mode with six isolated manual workstreams.
Their authoritative ownership and coordination contract is
[`../workstreams/README.md`](../workstreams/README.md).

## Quality gate

A model moves through these states:

1. `queued` — ordered by `planning/VERCY-TOP-50-DELIVERY-SEQUENCE.csv`, then by
   wave and priority score in the unified registry.
2. `provider_complete` — every active provider in `provider-policy.json`
   completed independent structured research; waived providers remain visible.
3. `synthesized` — agreements, conflicts and omissions are explicitly resolved.
   Single-provider mode additionally requires a separate no-tools adversarial
   audit that cannot add facts or silently substitute the waived provider.
4. `validated` — schema and semantic completeness checks pass.
5. `reviewable_draft` - a structurally valid synthesis without critical
   conflicts may have publication lifecycle `published`, provided its distinct
   research-review state, provider waiver and every hold remain visible. It must
   not be described as canonical or complete.
6. `publishable_draft` - all critical conflicts and publication holds are closed;
   the result may be promoted toward a canonical release. Research output is
   never published directly.

Single-provider results are always `reviewable_draft`: the provider waiver and
independent-review hold must appear in the synthesis evidence, publication
manifest, AI specification and human-facing page. A published distribution is
not a canonicality claim. They cannot become canonical or `publishable_draft`
until an independent second-provider review is restored.

The minimum subject structure is:

`Bundle -> Layer -> Finding -> Question`

Each finding also carries candidate data elements and artifacts. Model-level
functions, composition links and all Vercy service layers are mandatory. Empty
placeholder structures do not pass validation.

## Files

- `model-research.schema.json` — strict provider output contract.
- `MODEL-RESEARCH-PROMPT.md` — shared research protocol with provider-specific
  omission-hunting roles.
- `PAUSE-CHECKPOINT-2026-09-04.md` — current aggregate achievement snapshot,
  exact resume point and remaining execution plan.
- `queue.csv` — all world models in deterministic delivery order.
- `status.csv` — regenerated checkpoint projection from per-provider manifests.
- `assembly-queue.csv` — AISMM and PLMM migration/research track.
- `runs/<model-id>/` — prompts, provider responses and validation reports.

## Running one provider

```powershell
python tools/run_model_research.py --provider claude --model-id WM-XCT-011
python tools/run_model_research.py --provider grok --model-id WM-XCT-011
```

With the current repository policy, `run_research_batch.py` invokes only the
declared active providers unless `--providers` is explicitly supplied.

Use `--prompt-only` to materialize the exact input without calling a provider.
The runner uses a temporary empty working directory, denies local write tools and
provides only the selected registry record, relations and legacy source excerpt.
AISMM and PLMM use the separate assembly track because they compose many subject
models and require migration analysis rather than a false standalone boundary.

Validate a normalized provider result:

```powershell
python tools/validate_model_research.py research/runs/wm-xct-011/claude.result.json
```

After synthesis, generate the resumable source gate:

```powershell
python tools/build_source_verification_queue.py --model-id WM-XCT-011
```

## Evidence rule

Prefer primary standards, official schemas, public authorities, normative
registries and first-party technical documentation. Secondary literature can
identify gaps but cannot be the only support for a bundle, layer or finding.
Every structural node cites source IDs, and the validator requires a diverse
primary-source base. A model can be broad without pretending that evidence or
coverage is complete: unresolved boundaries and omissions are recorded.
