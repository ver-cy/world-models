## Verdict

`ACCEPT WITH LIMITS`

## Critical findings

1. **No independent aggregate identity is introduced.** Every identifying term stays with an existing master: System → WM-AI-001, Agent → WM-AI-002, configuration revision → WM-AI-005, run → WM-AI-004, model artifact → WM-SFT-004. The base and effective digests are derived attributes of an already-identified revision and run; clause 8 assigns them no keying role and clause 9 records them as run content. `newRuntimeId=false` holds — provided the derived, non-identifying status of the effective digest is stated explicitly rather than left implied.

2. **Grant and endpoint mastership is asserted but not evidenced.** Clauses 4 and 5 make ToolBinding and InferenceEndpoint relations *conditional* on an external first-class grant master and an external runtime/network master. The packet names neither. The no-new-master decision is therefore conditional, not established: if no such external master exists, the conditions force these into entities and break the decision. This is unresolved external-master evidence, so it holds rather than revises.

3. **Run-level authority is not bound to Agent-level authority.** Clause 6 copies accountable authority onto each run; clause 2 makes authority change an Agent-identity change absent a governed transfer record. No clause requires the run-recorded authority to equal the Agent's governed authority or to cite a transfer record when it differs. The "changing authority without governed transfer must fail Agent reuse" negative case is enforceable at the Agent boundary but silently bypassable at run level.

4. **The action-time clock is narrated, not reconciled.** The provider-comparison paragraph states the profile incorporates Grok's action-time clock condition, but clauses 1–9 contain no time anchor. Clause 7 requires "unrevoked approval" and clause 8 excludes dynamic grant state from the base digest, so "revocation blocks later calls" (clause 7) has no defined ordering relation. Replay reproducibility of allow/deny is under-specified.

5. **No contradiction internal to the profile makes a held reviewable version unsafe.** Clauses 2, 3, 5, 7 and 8 are mutually consistent; the identified defects are omissions.

## Required holds

- External grant master identity, scope/audience model, approval lineage and revocation lifecycle — evidence required.
- External runtime/network master for endpoint destination — evidence required.
- Action-time clock and ordering semantics for revocation versus invocation.
- Run-authority equality invariant, with governed-transfer citation on divergence.
- Base-model edits to WM-AI-002 (vetting record), WM-AI-005 (tool/grant pins, approval class, serving contract) and WM-AI-004 (grant id, exercised scope, audience, result, vetted-set membership, serving digest).
- Explicit declaration that both digests are derived and non-identifying.
- Hash algorithm and domain-separation strings.

## Scenario result

C1/R1 and C2/R2 pass. Agent A survives M1→M2 and T-set widening (clause 2); T3 is denied under C1 by clause 7's declared-tool-scope term; R2's distinct base digest follows from changed canonical approved bytes; M2 is recorded despite unchanged URL (clauses 3, 5); attenuation separates effective from base without touching A. Authority-plus-trust-domain change without a transfer record correctly fails Agent reuse at the Agent boundary — but see finding 3 for the run-level gap. Revocation replay is unverifiable pending the clock hold.

## Identifier decision

No new runtime or model identifier. `newRuntimeId=false` confirmed. WM-SFT-004 retained as model-artifact master. Publication withheld pending the holds above; the profile is reviewable as held.
