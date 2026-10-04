# Frozen semantic audit — EM-WRK-03

## Verdict

**Decision preserved; artifacts not freezable as submitted.**

The supplied evidence does not disprove the intended disposition. Reuse of WM-ACT-029 under a mandatory Program discriminator, Portfolio as disjoint sibling, ProgramComponent / Tranche / BenefitDependency as program-owned assertions, Transition Plan profiled on WM-ACT-008, the Outcome / Benefit Realization dependency external and identifier-unassigned, and no runtime/model ID allocation — all stand, and all three provider texts converge on them.

What fails is the encoding. The profile candidate and fixture set do not carry the reconciliation the provider comparison claims was reached, omit the package's second hard blocker from its own holds list, contain one containment-leaking fixture string, and leave nine of the thirteen local invariants with no enforcing constraint and no fixture. Fourteen material defects follow. Defects 1–5 are blocking; the remainder are deterministic editorial corrections.

---

## Material defects

### 1. The unallocated benefit master is absent from the candidate's holds, and constraint 5 asserts reuse of it

`PROFILE CANDIDATE.holds` lists three items; the unallocated Outcome / Benefit Realization master is not among them — despite Claude scoring it blocking hold (a) and Grok scoring it hard blocker 2. Worse, `constraints[4]` ends "…Outcome / Benefit Realization **reuses the existing EM-STR-02 candidate**," which asserts a satisfied binding to an identifier-unassigned, unapproved cross-contour referent. That contradicts the provider comparison ("must treat it as an external unresolved dependency and must not allocate or master it") and the audit instruction to keep it identifier-unassigned.

**Remediation.** Replace `constraints[4]` with exactly:
`"Output, capability, outcome, benefit, disbenefit and attribution remain distinct; the Outcome / Benefit Realization master is external, identifier-unassigned, referenced only, and is neither allocated nor mastered by this contour."`
Insert into `holds` exactly:
`"Blocking: the external Outcome / Benefit Realization master is identifier-unassigned; benefit and attribution logic terminates in an unresolved reference. The EM-STR-02 candidate is a named unallocated referent, not a reusable base."`

### 2. The mandatory intended-target requirement is unsatisfiable as stated

The provider comparison records the reconciled profile as requiring "at least one intended outcome or benefit target" (Grok invariant 5: "absent that target it is not a Program"). Under defect 1 that reference has no allocated master, so every conforming Program instance would carry a required dangling field. The two requirements cannot both hold.

**Remediation.** Bind the mandatory field to the allocated base and keep realization optional. Add to `constraints` exactly:
`"A Program must reference at least one intended aim mastered by WM-KNW-011; absent that reference the Program profile is rejected. A reference to the external Outcome / Benefit Realization master is optional, is recorded with absent-identifier reason `identifier-unassigned`, and never satisfies the mandatory intended-aim reference."`

### 3. The containment contradiction has a hold but no invariant, no constraint and no fixture

All three texts treat `parent_ids = WM-ACT-005` **and** `contains_ids = WM-ACT-005` as the package's hard canonical blocker. Grok states the rule ("WM-ACT-029 does not contain WM-ACT-005 as child identity", invariant 4). Neither the local synthesis's thirteen invariants, nor the candidate's eight constraints, nor any of the seven fixtures encode it. The blocker is recorded but not detectable.

**Remediation.** Add to `constraints` exactly:
`"The only lawful WM-ACT-029 to WM-ACT-005 edge is a ProgramComponent membership assertion referencing an external master; child-identity containment, nesting, minting and exclusive-membership defaults are rejected, and a profile never cancels an inherited containment edge."`
Add fixture `containment-edge-asserted` (below).

### 4. `bases` is role-flat and leaks mastership

`bases` lists seven models with no role distinction. Two are profiled (WM-ACT-029, WM-ACT-008), four are referenced external masters (WM-ACT-005, WM-ACT-034, WM-KNW-011, WM-ORG-016), and one is derivation-only (WM-ACT-030 — Claude: "derivation only"; Grok: "as origin only"). A flat list reads as this contour profiling or mastering all seven, which contradicts the mastership section of every supplied text.

**Remediation.** Replace the `bases` field with exactly:
`"profiledBases": ["WM-ACT-029","WM-ACT-008"], "referencedMasters": ["WM-ACT-005","WM-ACT-034","WM-KNW-011","WM-ORG-016"], "derivationOnly": ["WM-ACT-030"], "unallocatedExternalReferents": ["Outcome / Benefit Realization"]`

### 5. Non-project component masters and the sustainment owner are named but bound to nothing

Invariant 2 ("program components are not limited to projects") admits operations, products and campaigns; the acceptance scenario turns on `OPS-1` accepting a transition and on sustainment "remaining operationally mastered." No operations, product, campaign or sustainment master appears in `bases` or anywhere in the package. Invariant 2, fixture `two-project-transition` and fixture `post-program-benefit` are therefore not decidable, and "operationally mastered" is an unverifiable claim.

**Remediation.** Add to `constraints` exactly:
`"A non-project component is admitted only by reference to an external master identified outside this contour; it acquires no WM-ACT-005 baseline, phase, gate or authorization semantics by membership."`
Add to `holds` exactly:
`"Blocking for non-project cases: operation, product, campaign and sustainment masters are named in the disposition but bound to no model in this package; admissibility of non-project components and of post-closure sustainment ownership is held pending their allocation."`

### 6. Membership termination is inferred from component closure

The local synthesis acceptance result says P-A "closes first; its membership ends," and fixture `project-closes-first` expects membership to end "**as appropriate**" — an undefined trigger and non-deterministic expectation. Grok states the opposite direction explicitly: "Closing the component does not erase the historical assertion," and nothing in the package authorizes a component-side event to terminate a program-owned assertion. This is a reverse cascade, the mirror of invariant 4.

**Remediation.** Add to `constraints` exactly:
`"Membership termination is an explicit, effective-dated, program-authored event; it is never inferred from component closure, and component closure neither ends nor deletes any ProgramComponent, Tranche or BenefitDependency row."`
Replace `project-closes-first.expect` with exactly:
`"Project closure is recorded on the project master only; it emits no membership-end event, no outcome assertion and no realization assertion, and the joint benefit stays forecast with absent-reason measurement-pending."`

### 7. Discriminator non-nullability, immutability and supersession are not encoded

All three texts require the discriminator to be mandatory, non-nullable, unambiguous and changeable only by supersession with new identity ("not an in-place conversion"; "not silently flipped"). `constraints[0]` says only "a mandatory discriminator." Invariant 1 has no fixture.

**Remediation.** Replace `constraints[0]` with exactly:
`"Program profiles WM-ACT-029 with exactly one non-null discriminator; ambiguity or absence fails validation, the value is immutable in place, and a change of profile is supersession with new identity, never an update."`
Add fixtures `discriminator-absent`, `discriminator-ambiguous`, `discriminator-flipped-in-place`.

### 8. The falsifiable benefit hypothesis has no assigned master, and the provider comparison suppresses the divergence

Invariant 7 requires every joint benefit to carry an explicit falsifiable hypothesis. The local synthesis and Claude place it in the program-owned results chain; Grok explicitly excludes it from BenefitDependency and states "causal claims sit **at most** with WM-KNW-011 as target statements," while separately arguing the Program cannot master realization. The hypothesis therefore has three candidate homes and no assigned one. The provider comparison reports the two reviews as agreeing on the benefit axis and names only two Grok sharpenings; this divergence is omitted, which overstates reconciliation.

**Remediation.** Add to `constraints` exactly:
`"The falsifiable benefit hypothesis is a program-owned, versioned results-chain assertion distinct from both the WM-KNW-011 intended aim it references and the external realization master; it survives program closure as a historical assertion and asserts no realization."`
Add to the provider comparison, as a third sharpening, exactly:
`"Third, the reviews diverge on the home of the causal hypothesis: the local synthesis and Claude place it in the program results chain, Grok places causal claims at most with WM-KNW-011 and excludes BenefitDependency. The reconciled profile assigns the hypothesis to the program results chain and the intended aim to WM-KNW-011."`

### 9. Attribution has no adjudicating authority and no period key, so the ≤ 1.0 rule is undecidable

Invariant 8 bounds "adjudicated shares … per benefit and period," and fixture `double-count-benefit` tests it. The package never says who adjudicates (Grok: an after-the-fact WM-ACT-034 judgment; local synthesis and Claude leave it unattributed), which time axis defines "period," or how unadjudicated shares are treated — the local synthesis's "attribution remains unadjudicated until shares reconcile" implies self-adjudication on reconciliation, which is unsafe inference. BenefitDependency endpoint kinds are likewise unenumerated, so a dependency may silently terminate on the unallocated realization master.

**Remediation.** Add to `constraints` exactly:
`"Attribution is an adjudicated WM-ACT-034 judgment stating method, uncertainty and causal limits; it is never inferred from membership, dependency or share reconciliation. Adjudicated shares are summed per benefit identifier per observation-time period and must not exceed 1.0; unadjudicated shares are excluded from all totals and are never reported as realized."`
And exactly:
`"A BenefitDependency endpoint is one of: a program-owned results-chain node, a ProgramComponent, a Tranche, or a reference to the external realization master carried with absent-identifier reason identifier-unassigned."`
Replace `double-count-benefit.expect` with exactly:
`"The duplicate attribution is rejected; only WM-ACT-034-adjudicated shares are summed, per benefit identifier and observation period, to at most 1.0."`

### 10. "Addressable" has no identity form, leaving a latent identifier allocation

Grok's soft blocker 3 is precise: if addressability is later read as requiring codes, the no-new-ID decision is violated. Claude supplies the exact form — `{program-id}--{artifact-kind}--{assertion-id}` — but neither the local synthesis nor the candidate carries it, and `newRuntimeId: false` constrains only this contour's own allocation.

**Remediation.** Replace `constraints[1]` with exactly:
`"ProgramComponent, Tranche and BenefitDependency are effective-dated program-owned assertions addressed as {program-id}--{artifact-kind}--{assertion-id}, valid only inside one aggregate; they are never independent roots and are never assigned a WM-* code."`
Add fixtures `assertion-allocated-root-id` and `assertion-composite-identity`.

### 11. Time-axis bindings and the absent-reason vocabulary are unspecified

Seven axes are enumerated (planned, decision, event, effective, observation, ingestion, knowledge); Claude's scenario then introduces an eighth pair, phenomenon time versus result time, unreconciled with the list. No axis is bound to any assertion: "effective-dated" membership, "validity-bounded" dependency, the attribution "period" and realization observations all float. `measurement-pending` and `identifier-unassigned` are used as absent-reasons with no declared vocabulary, so `project-closes-first` cannot be evaluated.

**Remediation.** Add to `constraints` exactly:
`"ProgramComponent and Tranche are bounded on effective time; BenefitDependency validity is bounded on effective time; realization and disbenefit records are bounded on observation time and carry decision time separately; ingestion and knowledge time are recorded and never substituted for effective or observation time."`
And exactly:
`"Absent values are recorded with one of the reasons measurement-pending or identifier-unassigned; no other absent-reason is admitted and no absent value is read as a negative or realized result."`

### 12. Reconciled requirements stated in the provider comparison are missing from the candidate

The comparison states the reconciled profile "requires … historical assertion retention, independent versioning of program assertions and transition plans, and explicit references rather than duplicated plan or component facts." None of the three appears in `constraints`. Grok's soft blocker 4 turns on the last of them.

**Remediation.** Add to `constraints` exactly:
`"Historical ProgramComponent, Tranche and BenefitDependency rows are retained through member closure and program closure; the Program profile, each assertion kind and each Transition Plan are versioned independently; readiness and handover bindings on WM-ACT-029 are references to the pinned WM-ACT-008 plan release and never duplicate plan or component facts."`

### 13. The holds list is under-populated and one hold is stale

`holds` carries three generic entries against seven further holds evidenced in Claude's text (`publishableCanonical` false throughout, ISO support abstract-level only, unsourced retention/access house policy, unnormalized programme/program token, single-provider-waiver drafts for WM-ACT-029 and WM-ACT-030, the **deferred Program/Portfolio split** — on which the whole sibling-profile disposition is contingent). Separately, `holds[2]` says the Grok review and the frozen audit are "pending," which is stale at freeze. And Claude's load-bearing evidence — WM-ACT-029's `out_of_scope`, `policies`, `adversarial_checks` and the `vr.wm-act-029` registry row — is not supplied in this package and is single-sourced; it is not disproved here, but it is not verifiable here either.

**Remediation.** Replace `holds` with exactly:
```
["Blocking: WM-ACT-029 is recorded with WM-ACT-005 as both parent and contained model; canonical resolution required.",
 "Blocking: the external Outcome / Benefit Realization master is identifier-unassigned; benefit and attribution logic terminates in an unresolved reference. The EM-STR-02 candidate is a named unallocated referent, not a reusable base.",
 "Blocking for non-project cases: operation, product, campaign and sustainment masters are named in the disposition but bound to no model in this package.",
 "The Program/Portfolio split is recorded as deferred in the base; the sibling-profile disposition is contingent on that base decision.",
 "Relevant relation rows remain unapproved.",
 "WM-ACT-029 and WM-ACT-030 are single-provider-waiver drafts without independent review; reused bases remain non-canonical with source and provider holds.",
 "publishableCanonical is false throughout; ISO support is abstract-level only; retention and access rules are unsourced house policy; the programme/program token is unnormalized.",
 "WM-ACT-029 out_of_scope, policies and adversarial_checks and the vr.wm-act-029 registry row are cited from material not supplied in this package; single-source and unverified at audit.",
 "Independent provider review and the single frozen semantic audit are complete; no further provider run is admissible.",
 "No installability or publication-readiness claim is made."]
```

### 14. The fixture set leaks containment, half-covers one invariant, and leaves nine invariants untested

`two-project-transition.input` reads "A program **contains** two projects" — the exact verb the package's hard blocker forbids, inside the artifact meant to enforce the ban. `arbitrary-folder` expects only Program rejection, covering half of invariant 13 ("neither a Program nor a Portfolio"). `post-program-benefit` is a positive case asserting an external master that is unallocated, so it cannot pass. Across the seven cases there is no coverage for invariants 1, 2, 7, 8 (partly), 10 (partly), 11, 12, 13 (partly), nor for the containment edge, dual membership, portfolio/program membership crossover or plan duplication.

**Remediation.** Replace `two-project-transition.input` with exactly:
`"A program holds ProgramComponent membership assertions referencing two externally mastered projects and one transition to an externally mastered operation, against one joint benefit."`
Replace `arbitrary-folder.expect` with exactly:
`"Both the Program and the Portfolio profiles are rejected and the container is routed out of WM-ACT-029."`
Replace `post-program-benefit.expect` with exactly:
`"Program closure records handover, benefit owner and residual obligations; realization observations continue against the external benefit master, referenced with absent-identifier reason identifier-unassigned, and no realization claim is made inside this contour."`
Append the fixtures below to `cases`.

---

## Exact additional fixtures

```json
[
  {"id":"containment-edge-asserted","kind":"negative","input":"The registry asserts WM-ACT-029 contains WM-ACT-005 as child identity while the profile claims external component mastership.","expect":"The containment edge is rejected; only a ProgramComponent membership assertion referencing an external master is lawful, and the profile does not cancel the inherited edge."},
  {"id":"discriminator-absent","kind":"negative","input":"A WM-ACT-029 instance is created with no profile discriminator.","expect":"Validation fails; the discriminator is non-null and mandatory."},
  {"id":"discriminator-ambiguous","kind":"negative","input":"A WM-ACT-029 instance carries both the Program and the Portfolio discriminator.","expect":"Validation fails; exactly one discriminator is permitted and the profiles are disjoint."},
  {"id":"discriminator-flipped-in-place","kind":"negative","input":"An existing Program instance is updated to the Portfolio discriminator, retaining its identity.","expect":"The in-place conversion is rejected; a profile change is supersession with new identity."},
  {"id":"assertion-allocated-root-id","kind":"negative","input":"BenefitDependency is given its own WM-* root code so that it can be addressed.","expect":"The allocation is rejected; addressability is satisfied by the composite assertion identity and no new root is minted."},
  {"id":"assertion-composite-identity","kind":"positive","input":"A ProgramComponent, a Tranche and a BenefitDependency are addressed within one program aggregate.","expect":"Each resolves as {program-id}--{artifact-kind}--{assertion-id}, is valid only inside that aggregate, and carries no independent root identity."},
  {"id":"non-project-component","kind":"positive","input":"An externally mastered operation is admitted as a program component alongside two projects.","expect":"Membership is recorded by reference to the external master; no WM-ACT-005 baseline, phase, gate or authorization semantics are inferred for the operation."},
  {"id":"membership-end-inferred-from-closure","kind":"negative","input":"Closing a component project automatically terminates its ProgramComponent assertion.","expect":"The inferred termination is rejected; membership ends only by an explicit, effective-dated, program-authored event."},
  {"id":"membership-row-deleted-on-closure","kind":"negative","input":"Program closure deletes the historical ProgramComponent, Tranche and BenefitDependency rows.","expect":"The deletion is rejected; historical assertions are retained through member closure and program closure."},
  {"id":"program-closure-cascades-component-closure","kind":"negative","input":"Closing the program sets the remaining components to closed.","expect":"The cascade is rejected; program closure neither closes, cancels nor deletes any member."},
  {"id":"component-closure-asserts-realization","kind":"negative","input":"Project closure emits a realized state for the joint benefit it contributes to.","expect":"The realization assertion is rejected; closure proves neither outcome nor benefit and the benefit remains forecast with absent-reason measurement-pending."},
  {"id":"joint-benefit-without-hypothesis","kind":"negative","input":"A joint benefit is declared with owner, baseline, target and indicator but no falsifiable hypothesis.","expect":"The benefit is rejected; an explicit falsifiable results-chain hypothesis is required."},
  {"id":"attribution-shares-exceed-one","kind":"negative","input":"Adjudicated contribution shares for one benefit and one observation period sum to 1.3.","expect":"The adjudication is rejected; adjudicated shares sum to at most 1.0 per benefit identifier and observation period."},
  {"id":"unadjudicated-shares-reported-as-realized","kind":"negative","input":"Unadjudicated contribution shares are reconciled and reported as realized attribution without a WM-ACT-034 judgment.","expect":"The report is rejected; attribution is adjudicated only by a WM-ACT-034 judgment and is never inferred from reconciliation or membership."},
  {"id":"dual-membership-implies-attribution","kind":"negative","input":"A project appears as a component of two programs and attribution shares are derived from the dual membership.","expect":"Both memberships are valid; the derived attribution is rejected because membership implies neither mastership nor attribution."},
  {"id":"portfolio-membership-creates-program-membership","kind":"negative","input":"Adding a project to a Portfolio creates a ProgramComponent assertion on a sibling Program, or the reverse.","expect":"The propagation is rejected; Portfolio membership and Program membership are disjoint assertions."},
  {"id":"transition-plan-existence-as-acceptance","kind":"negative","input":"A released transition plan is treated as operational acceptance and the capability is reported as handed over.","expect":"The inference is rejected; operational acceptance is a separate authorized WM-ACT-034 decision by the receiving operational owner."},
  {"id":"transition-plan-duplicated-on-029","kind":"negative","input":"Readiness and handover bindings on WM-ACT-029 carry a second copy of the WM-ACT-008 plan content.","expect":"The duplication is rejected; bindings are references to a pinned plan release."},
  {"id":"sustainment-closed-with-program","kind":"negative","input":"Program closure terminates the sustainment obligations recorded for the accepted capability.","expect":"The termination is rejected; sustainment obligations survive program closure and remain externally mastered."},
  {"id":"released-assertion-mutated","kind":"negative","input":"A released membership, allocation, decision or observation is edited in place to correct an error.","expect":"The mutation is rejected; released assertions are immutable and corrected only by an explicit successor."},
  {"id":"benefit-dependency-endpoint-unallocated","kind":"positive","input":"A BenefitDependency terminates on the external Outcome / Benefit Realization master, which has no allocated identifier.","expect":"The endpoint is recorded with absent-identifier reason identifier-unassigned; no identifier is minted and no realization claim is made."},
  {"id":"independent-versioning","kind":"positive","input":"A transition plan release is pinned while program membership and results-chain assertions are revised.","expect":"The Program profile, each assertion kind and the transition plan version independently, and the pinned plan release is unaffected."}
]
```

---

## Freeze decision

**FREEZE — audit spent, decision frozen, publication blocked.**

The EM-WRK-03 boundary is frozen as submitted at the disposition level: `decision: PROFILE`, `newRuntimeId: false`, WM-ACT-029 Program profile with Portfolio sibling, three program-owned assertions, Transition Plan on WM-ACT-008, Outcome / Benefit Realization external and identifier-unassigned. No provider run is requested and none is admissible; this audit does not recur.

The artifacts are **not** frozen. All fourteen remediations above are exact, deterministic edits derivable from the supplied text alone and require no further adjudication; apply them to the profile candidate, the fixture set and the provider comparison before checkpoint. Defects 1–5 remain blocking after the edits, because each records an unresolved external fact — the registry containment contradiction, the unallocated benefit master, and the unbound non-project and sustainment masters — that no editorial action inside this contour can close.

No installability, canonical completeness or publication-readiness is claimed, and none is reachable while holds 1–3 stand.
