## Verdict

Not fit to freeze as-is — remediable without redesign. The core dispositions are sound and mutually consistent across the four artifacts: view/projection identity is correctly separated from subject identity, `decision: PROFILE` with `newRuntimeId: false` is supported by both providers and by the local synthesis, control-facet independence and single-measure projections are stated normatively, and the Control pending-master hold is honestly carried. The material defects are concentrated in (a) time pinning and currency clock, (b) the vocabulary for "undetermined", (c) what the projection record is required to publish, and (d) local-evidence invariants that did not survive into the binding profile candidate. Fixture coverage is broad on the classic bad inferences and thin on everything the defects below touch.

## Material defects

**1. Snapshot pins a single as-of time, but the evidence declares three time axes.**
Local evidence keeps event, observation/as-of and record times distinct; constraint 3 binds only "as-of time and scenario". A snapshot pinned by as-of alone is not reproducible once backdated evidence or late-arriving findings land, because the same as-of yields a different body later.
*Remediation:* require the snapshot to pin a record/ingest cut-off in addition to the as-of (valid-time) instant, and state that records arriving after the ingest cut-off never enter a frozen snapshot.

**2. Currency evaluation clock is unpinned and unrecorded.**
Local evidence says currency "is recomputed against caller-supplied cut-off"; the view definition also "pins … cut-off"; constraint 3 says current status is "derived at read time" without naming the clock. Two reads of one snapshot ID can therefore return different currency verdicts with nothing on the record to distinguish them.
*Remediation:* have the currency rule name its clock explicitly, and require every read/projection result to record the evaluation instant used alongside the snapshot ID.

**3. "Undetermined" is overloaded across two unrelated states.**
Missing applicability is first-class undetermined and sits *outside* the denominator (constraint 5). The acceptance scenario's C-1 — applicable, designed, implemented, no required execution in period — is called "unsupported" in the local evidence but "undetermined" in fixture `implemented-not-operated`. Under the profile's own vocabulary that wording pushes an in-scope control out of the coverage denominator.
*Remediation:* give the facet state a distinct name (e.g. `not-exercised-in-period`) and state that it remains inside the coverage denominator while being excluded from the effectiveness denominator under a declared exclusion.

**4. "Disputed" is lost between artifacts.**
The local evidence keeps indeterminate and disputed as separate outcomes and invariant 6 requires both countable. The profile candidate's constraints carry only `undetermined`; disputed has no defined denominator placement and no fixture, so it will collapse into applicable or into undetermined at implementation time.
*Remediation:* add a constraint naming disputed applicability as a distinct retained, countable outcome with its denominator placement stated.

**5. Projections may publish a quantity without publishing what was excluded.**
Local-evidence invariant 2 requires every quantity to declare denominator *and exclusions*; constraint 6 requires only measure type, denominator and numerator rule, and the Assurance Coverage Projection shape records no gap/undetermined counts. A 100% coverage figure over a heavily undetermined population is therefore well-formed under the profile as written.
*Remediation:* make undetermined, disputed and excluded counts with their exclusion reasons mandatory fields of the projection record, and declare a quantity ill-formed without them.

**6. The comparability verdict has no recorded home on the projection.**
Constraint 11 and invariant 10 require an explicit comparability verdict for aggregation and trend claims; only the parent landscape shape carries "comparability/caveats", while aggregates are produced by the projection.
*Remediation:* add the comparability verdict (and the axes it covers) as a required field of any aggregating projection record.

**7. View and projection outputs are not on the non-evidence list.**
Constraint 8 excludes completed cards, mappings, documents, incident-free periods and unexpired exceptions from proving later facets, but says nothing about the landscape's own snapshots or coverage projections. An "assessment-present 100%" projection can be cited back as effectiveness or compliance evidence — the exact inference the profile exists to block.
*Remediation:* extend constraint 8 so snapshot bodies and projection outputs are explicitly non-evidence for any control facet, compliance or assurance conclusion.

**8. Four local invariants did not reach the binding artifact.** The profile candidate is the artifact that binds; these are present in the local evidence and absent from its constraints:
- requirement / obligation / control / evidence distinctness;
- findings remain engagement-owned and observations never promote to findings automatically (leaving bases WM-ACT-033 and WM-MAT-008 wholly unconstrained);
- effectiveness conclusions must name method, vocabulary, validity and invalidation triggers;
- assurance conclusions must carry scope, method, exclusions and assurance level.
*Remediation:* restate each as a constraint in the profile candidate; no wording change is needed beyond what the local evidence already contains.

**9. Exception expiry does not propagate in the binding artifact.**
The local evidence and acceptance scenario require expiry to flag dependent conclusions revalidation-pending and suspend reliance. Constraint 10 stops at "readable but cannot authorize"; nothing requires the dependent conclusions to change state, and no fixture exercises propagation.
*Remediation:* add to constraint 10 that expiry or supersession sets dependent conclusions to revalidation-pending.

**10. `WM-ACT-034`'s candidate status is held in the prose and dropped from `holds`.**
The local evidence holds record that WM-ACT-034 remains a candidate with empty relationship contracts; the profile candidate lists it in `bases` with holds naming only Control and WM-XCT-027. The machine-readable artifact therefore understates how much of the base set is unratified.
*Remediation:* add a hold naming WM-ACT-034's candidate status, and mark provisional bases as such in the profile candidate.

**11. Term drift on the second artifact's kind.**
It is "Assurance Coverage View" in the name, comparison and constraint 1, "Assurance Coverage Projection" in the minimal shape. Since constraint 4 assigns definition-level rules to "the view definition", the drift leaves it ambiguous whether the coverage artifact owns its own selectors and snapshots or is purely a projection run of the landscape snapshot.
*Remediation:* pick one term — Assurance Coverage Projection, given constraint 1's "cite-only projection" — and use it in the name, constraints and shape.

## Additional fixtures required

```json
[
{"id":"late-record-after-ingest-cutoff","kind":"positive","input":"Backdated evidence for an in-scope control arrives after a snapshot's record cut-off but with an event time before its as-of.","expect":"The frozen snapshot body and digest are unchanged; the record appears only in a later snapshot."},
{"id":"currency-clock-recorded","kind":"positive","input":"One snapshot is read at two different caller cut-offs.","expect":"Body, included references, exclusions, caveats and digest are identical; currency verdicts may differ and each result records the evaluation instant and snapshot ID used."},
{"id":"digest-mismatch","kind":"negative","input":"A snapshot body is served whose content digest does not match the recorded digest.","expect":"The read is rejected and the snapshot is not citable."},
{"id":"not-exercised-in-period","kind":"positive","input":"Applicable control C1 is designed and implemented with no required execution in the period.","expect":"C1 stays in the coverage denominator, is excluded from the effectiveness denominator under a declared exclusion, and its operating and effectiveness facets are not-exercised-in-period rather than applicability-undetermined."},
{"id":"disputed-applicability","kind":"positive","input":"Requirement R9 has a disputed applicability conclusion for unit U at the requested time and scenario.","expect":"Disputed is retained as a distinct countable outcome, is not merged into undetermined or applicable, and its denominator placement is stated on the projection."},
{"id":"exclusions-not-published","kind":"negative","input":"A coverage percentage is emitted with an explicit denominator but no undetermined, disputed or excluded counts and no exclusion reasons.","expect":"The projection is ill-formed."},
{"id":"comparability-verdict-recorded","kind":"positive","input":"Cells from two criteria are aggregated with an explicit comparability verdict.","expect":"The aggregating projection record stores the verdict and the axes it covers, and the caveats survive export."},
{"id":"projection-as-effectiveness-evidence","kind":"negative","input":"An assessment-present coverage projection is cited as evidence that a control is effective, or a snapshot body is cited as compliance evidence.","expect":"The citation is rejected; view and projection outputs are non-evidence for control facets, compliance and assurance."},
{"id":"observation-promoted-to-finding","kind":"negative","input":"A WM-MAT-008 observation is recorded as an audit finding without an owning WM-ACT-033 engagement.","expect":"The promotion is rejected; findings remain engagement-owned."},
{"id":"effectiveness-conclusion-metadata","kind":"negative","input":"An effectiveness conclusion omits method, vocabulary, validity or invalidation triggers.","expect":"The conclusion is ill-formed and cannot ground risk-reduction credit."},
{"id":"assurance-conclusion-metadata","kind":"negative","input":"An assurance conclusion omits scope, method, exclusions or assurance level.","expect":"The conclusion is ill-formed and cannot be aggregated."},
{"id":"requirement-obligation-collapse","kind":"negative","input":"A requirement expression is counted as a fulfilled obligation, or an obligation is counted as a control.","expect":"The collapse is rejected; requirement, obligation, control and evidence remain distinct."},
{"id":"expired-exception-dependents","kind":"positive","input":"Exception X3 expires before cut-off and prior conclusions relied on it.","expect":"Dependent conclusions are set to revalidation-pending, reliance is suspended, and the cited requirement is unchanged."},
{"id":"provisional-base-marked","kind":"positive","input":"The profile rests on candidate base WM-ACT-034 and on unreconciled WM-XCT-027.","expect":"Both are marked provisional in bases and named in holds, and any dependent quantity is labelled provisional."},
{"id":"pending-master-provisional-coverage","kind":"positive","input":"A coverage projection reports over control facets while Control is identifier-unassigned.","expect":"Pending-master markers are present, the result is labelled provisional, and Control is never presented as resolved."},
{"id":"cross-scenario-effectiveness-reuse","kind":"negative","input":"An effectiveness determination current for scenario S is used to credit risk reduction in scenario S2.","expect":"The credit is rejected; risk reduction requires a same-scenario, in-scope, current determination."}
]
```
