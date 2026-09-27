# Frozen no-tools semantic audit — EM-AI-01

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, infer missing catalogue text, invent identifiers, or grant publication authority.

The proposed result is a PROFILE over WM-AI-001, WM-AI-002, WM-AI-005 and WM-AI-004 with no new runtime/model identifier. WM-SFT-004 remains the referenced model-artifact master.

Reconciled boundary:

1. WM-AI-001 masters the governed AI System accountability and use-context boundary. WM-AI-002 masters durable Agent identity. WM-AI-005 masters immutable configuration revisions. WM-AI-004 masters one bounded run.
2. Agent identity is assigned and distinct from configuration digest, model version, endpoint URL, grant and run. Model/tool/endpoint changes and runtime grant attenuation preserve Agent identity. Accountable-authority, purpose or trust-domain change creates a new Agent by default; identity-preserving transfer requires an explicit governed transfer record.
3. WM-SFT-004 remains the model-artifact master. WM-AI-005 pins its immutable model-version reference and serving contract; WM-AI-004 records the requested and resolved model version, endpoint and serving digest.
4. ToolBinding remains a relation only when a first-class external grant has independent identity, exact scope and audience, approval lineage and revocation lifecycle. WM-AI-005 declares tool/grant pins and approval class, WM-AI-002 records vetting, and WM-AI-004 observes grant id, exercised scope, call audience, allow/deny result and vetted-set membership.
5. InferenceEndpoint remains a relation only when an external runtime/network master identifies the destination, WM-AI-005 pins model/parser/context/tool-protocol/safety/rate-class serving semantics and WM-AI-004 records the resolved destination and serving digest. URL equality is not serving identity.
6. Accountable authority is a referenced human, organization or operator copied onto each run. `role=agent` grants nothing. Delegation is explicit, attenuated, audience-bound, revocable and terminates at the accountable authority.
7. Effective authorization at each action is principal rights ∩ agent-held grant ∩ declared tool scope ∩ audience ∩ unrevoked approval ∩ delegated scope ∩ effective configuration. Missing any term denies the action. Grant revocation blocks later calls without rewriting earlier observations or changing Agent identity.
8. Every run pins a base digest over canonical approved configuration bytes and an effective digest over resolved authorization decisions, overlays, disabled tools and serving identity. Hash algorithm and domain separation are explicit. Dynamic grant/approval state is excluded from the immutable base digest and included by reference and decision result in the effective digest.
9. One run keeps one immutable configuration revision. It records the stable agent, authority, revision, both digests, requested/resolved model, tool snapshot, observed invocations, endpoint resolution, approvals and outputs.

Scenario: one System and Agent A with accountable operator H. C1 pins M1 and T1/T2. R1 records allow and deny decisions and cannot invoke T3. C2 pins M2 and T1/T2/T3. R2 keeps Agent A, uses a distinct base digest, invokes T3 only with its exact grant, audience and approval, and records M2 even if the URL is unchanged. Runtime attenuation makes effective digest differ from base without changing A. Changing authority and trust domain without governed transfer must fail Agent reuse.

Negative cases reject config hash as agent id, new Agent per model version, agent-role delegation, missing H, opaque grant text, missing audience, silent same-URL serving drift, retrospective rewrite after revocation and T3 under C1.

Provider comparison: Claude supported reuse and relation decomposition. Grok conditionally accepted it and supplied the missing external-grant, serving-contract, identity-transition, dual-digest and action-time clock conditions. The reconciled profile incorporates those conditions and keeps their absence as publication holds.

Audit questions:

- Does this profile introduce an independent aggregate identity despite `newRuntimeId=false`?
- Are System, Agent, model, configuration, run, grant and endpoint mastership unambiguous?
- Do the external-grant and endpoint conditions safely preserve the no-new-master decision?
- Does the C1/R1/C2/R2 scenario preserve identity, authority and reproducibility?
- Identify any critical contradiction that makes even a held reviewable profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat unresolved external-master evidence and base-model edits as holds unless they contradict the profile itself.
