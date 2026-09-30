# EM-AI-02 local synthesis — reconciled and frozen

## Disposition

- Reuse WM-AI-007 for registry identity, WM-SFT-004 for immutable artifacts, WM-AI-006 for runs and run-contained effective configuration, WM-DAT-001 for datasets, WM-AI-001 for the AI system, WM-FLW-015 for observed consumption, and EM-WRK-05 demand/capacity/reservation for requested and granted compute.
- WM-AI-005 is a generic configuration type only; it is never the effective training record or a second run identity.
- Family and architecture remain classifications. Reusable Training Recipe has no present independent identity and remains a conditional identifier-unassigned candidate. No catalogue, model or runtime identifier is allocated.

## Identity and mastership

Registry entry, artifact, run, evaluation, deployment, endpoint and system are distinct. Digest pins bytes without replacing governed artifact identity; names, aliases, family, endpoint and timestamps never establish identity. Protected weights, data and confidential dossiers stay outside the public catalogue.

Requested compute is an EM-WRK-05 demand assertion referencing a run; granted compute is an EM-WRK-05 reservation or quota; observed compute is WM-FLW-015 consumption. WM-AI-006 owns none of them and holds only typed references.

## Run, configuration and provenance

Every run pins one resolved effective-configuration digest covering base artifact, tokenizer, dataset snapshots/splits/transforms, code, dependencies, parameters, seeds, environment, rights, licences and reproducibility limits. WM-AI-006 singly masters reproducibility. WM-SFT-004 may retain only a non-authoritative (runRef, runRevision) reference and restates no reproducibility status.

A derived artifact carries the union of restrictions from every version-qualified input of its producing run, including seed checkpoint and base artifact, plus output restrictions. Derivation never relaxes restrictions. Sibling-run, family, architecture, alias, registry-entry and endpoint edges never propagate them.

## Checkpoint promotion

A checkpoint remains run-contained while referenced only within its producing run. Cross-run input or retention beyond the producing run window requires prior promotion to a WM-SFT-004 checkpoint-role artifact with digest and derivation to producing run and step. No derivation edge terminates on a run-contained checkpoint.

## Deployment and serving

No EM-AI-02 base masters endpoints or deployments. WM-AI-001, WM-SFT-004 and WM-AI-007 hold only authority-qualified external deployment observations. Endpoint is an unowned typed reference here. Co-serving divergent restrictions is asserted but unenforced and therefore HELD until a frozen bind-time rights authority exists. Endpoint creation, repointing or region change creates neither run nor artifact.

## Time and evidence

Every instant uses RFC 3339 seconds precision with explicit UTC offset. Ordering and duration comparisons are valid only within one clock kind; cross-clock arithmetic is rejected. When a referenced digest changes, evidence becomes stale and supports no lifecycle, rights, reproducibility or publication decision until re-asserted. Prior evidence remains resolvable.

## Acceptance result

R0 checkpoint CK is promoted to a WM-SFT-004 checkpoint-role artifact before seeding R1 and R2. R1 uses D1 and produces A1; R2 uses restricted D2 and produces A2. Each run has distinct configuration, demand/reservation references and WM-FLW-015 actuals. Endpoint E may point to both digests, but co-serving compliance is HELD because bind-time rights evaluation is unowned. Family and endpoint merge no identity, lineage or restrictions.

## Required invariants

1. Digest verifies bytes but does not replace governed identity.
2. Equal names or aliases do not prove equal weights.
3. Every run pins one immutable effective configuration digest.
4. Training pins base model, tokenizer, data, code, dependencies, seeds and environment.
5. Requested, granted and observed compute remain distinct externally mastered assertions.
6. A grant implies no employment, identity, deployment or use.
7. Cross-run checkpoint use requires promotion to an identified artifact.
8. Endpoint changes create no run or artifact revision.
9. Derived restrictions are the union along derivation; shared serving merges nothing.
10. Weight transformations create successor artifacts with lineage.
11. Registry entry, artifact, run, evaluation and deployment remain separate.
12. Protected weights and data stay outside the public catalogue.
13. Reproducibility is bounded, pinned and WM-AI-006-mastered.
14. Different compute quantity kinds are never summed.
15. Family and architecture classify and identify nothing.
16. Reusable Training Recipe has no assigned identifier and may not be referenced as an identified object.

## Holds

The two required base relations are unratified and overridden to conditional. Endpoint, deployment and evaluation authority and bind-time rights enforcement are unassigned. WM-SFT-004 has a source-ledger inconsistency and an artifact-level reproducibility assertion requiring base correction. WM-AI-006 and WM-AI-007 are single-provider drafts under waiver. Source, crosswalk and fixture holds remain. The recipe candidate is unallocated. canonicalPublishable and installable remain false; no publication-readiness claim is made.
