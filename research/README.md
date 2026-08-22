# Vercy dual-provider model research

This directory turns the unified Vercy registry into evidence-backed model
specifications. Every world-model record is researched independently by Claude
and Grok before a synthesis can be promoted to the website catalogue.

Scope is 401 world-model records plus two separately queued Vercy assemblies
(AISMM and PLMM). The 1,180 external registry entries are standards, schemas,
classifiers and protocols: they receive an alignment/verification pass and are
not forced into an artificial Bundle/Layer hierarchy.

## Quality gate

A model moves through these states:

1. `queued` — ordered by `planning/VERCY-TOP-50-DELIVERY-SEQUENCE.csv`, then by
   wave and priority score in the unified registry.
2. `claude_complete` and `grok_complete` — independent structured research.
3. `synthesized` — agreements, conflicts and omissions are explicitly resolved.
4. `validated` — schema and semantic completeness checks pass.
5. `reviewable_draft` - a structurally valid synthesis may be projected into the
   public catalogue only with an explicit research-draft badge and every hold
   visible. It must not be described as canonical or complete.
6. `publishable_draft` - all critical conflicts and publication holds are closed;
   the result may be promoted toward a canonical release. Research output is
   never published directly.

The minimum subject structure is:

`Bundle -> Layer -> Finding -> Question`

Each finding also carries candidate data elements and artifacts. Model-level
functions, composition links and all Vercy service layers are mandatory. Empty
placeholder structures do not pass validation.

## Files

- `model-research.schema.json` — strict provider output contract.
- `MODEL-RESEARCH-PROMPT.md` — shared research protocol with provider-specific
  omission-hunting roles.
- `queue.csv` — all world models in deterministic delivery order.
- `status.csv` — regenerated checkpoint projection from per-provider manifests.
- `assembly-queue.csv` — AISMM and PLMM migration/research track.
- `runs/<model-id>/` — prompts, provider responses and validation reports.

## Running one provider

```powershell
python tools/run_model_research.py --provider claude --model-id WM-XCT-011
python tools/run_model_research.py --provider grok --model-id WM-XCT-011
```

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
