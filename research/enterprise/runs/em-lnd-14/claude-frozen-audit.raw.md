## Verdict
**ACCEPT WITH LIMITS**

## Critical findings

1. **Participation/impact conflation (most serious).** Clause 5 establishes *proven participation* from recorded consume/derive/basis edges, but the scenario reports R1/R2 and A1/A2 as *proven impacted*. Participation is a lineage fact; impact is a judgement about effect. The profile applies the two-step test (binding + effect) only to Sys/P in clause 7, while silently collapsing it for runs and artifacts. This is not an unsafe contradiction — the resulting class is over-inclusive, not falsely exculpatory — but it must be renamed and derived explicitly.
2. **Latent aggregate in the impact-result set.** The declaration key (version + tenant + source revisions + as-of + perimeter + crosswalk + policy version) and the emitted proven/potential/unknown set are durable, citable and membership-defining. Neither is a runtime or model identifier, but a persisted, re-citable impact set becomes a de facto master if it is stored rather than re-derived.
3. **Dual-candidate ownership ambiguity.** Landscape (projection) and Usage Network (viewpoint) read on the same declaration and edges. Nothing in the packet forbids the viewpoint asserting independent membership or a derived edge being promoted to authoritative.
4. **Rights leakage by traversal.** Clause 4 sets intersection-of-rights at the edge, but mixed-input A3 can expose a restricted parent's existence through traversal even where that parent is individually filtered. Inference-level exposure is unaddressed.
5. **Applicability overlay vs immutable record.** Clauses 6 and 9 correctly retain E1/S records, but "loses applicability" must not be written into those records.
6. **Potential ≠ silence.** P and Sys resting at *potential* with D merely "flagged" leaves no bounded obligation to resolve binding and effect.

## Required holds

- **H1** Rename artifact/run results to *proven participation → proven applicability impact*; operational or harm impact requires separately established binding and effect, as for Sys/P.
- **H2** Impact results are re-derivable projection output only: receipt-addressed by declaration key, never master-identified, never written back onto run, artifact, evaluation, safety, system or deployment masters.
- **H3** Single declaration owner; Usage Network asserts no membership and creates no edges. Derived edges carry provenance to a WM-XCT-037-owned edge and can never be promoted to authoritative.
- **H4** Rights filter applied per hop *and* at result-set assembly; suppress traversal disclosures that reveal a filtered parent through a mixed-input child. Tenant isolation is non-overridable.
- **H5** No "unaffected" class may be emitted. Absence of edges yields *unknown*, never negative clearance.
- **H6** Applicability loss and review flags are overlays with their own effective time; evidence is never deleted, decisions never auto-revoked.
- **H7** *Potential* carries a bounded resolution obligation for D's review.
- **H8** Dependency roots in clause 12 (Dataset Revision, Deployment Decision/Endpoint, Compute, Commercial Product, Rights/Licence Grant) remain reuse-or-block holds. Base-model publication blockers retained as holds — none contradict this profile.

## Scenario result

D2 withdrawn: R1/R2, A1/A2 proven participation with proven applicability impact. A3 same, sole-cause **false**. E1/S records immutable, applicability invalidated by overlay. Sys/P potential operational impact pending binding and effect. D valid, flagged, not revoked. Unofficial fine-tunes **unknown**, not unaffected. Compute C stands with no product, registry, deployment or agent identity. All evidence and rights restrictions survive.

## Identifier decision

`newRuntimeId=false` **upheld**. No new runtime, model or master identifier. Declaration key is a scoping tuple; impact sets are projection receipts. Registration confers no rights, deployment, disclosure or publication authority.
