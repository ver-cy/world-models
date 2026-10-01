# Verdict

Complete reserved **WM-SFT-016** as one aggregate — *Service Level Objective and Reliability Commitment* — owning four surfaces: **SLI specification**, **SLO policy**, **SLO evaluation**, **error-budget policy**. **ObservabilityBinding** stays inside as an effective-dated binding record but owns no telemetry. Two surfaces are delegated, not absorbed: **raw observations** → WM-MAT-008; **contractual SLA** → WM-ECO-006 plus the obligation model per EM-LEG-01. The SLI formula is **reused** from the EM-DAT-05 Metric Definition candidate, not reminted. Availability, latency, freshness/correctness and journey variants are EXTEND **profiles**, not independent models. Five separate models would fracture one decision (what we promise, measured how, over what window, with what budget) across five lifecycles; one model that also swallowed telemetry and contract would make an unknown indistinguishable from a breach claim.

# Evidence

WM-MAT-008 already owns a single determination act: result, unit binding with versioned code system, `dataAbsentReason`, censoring, quality flags recorded but never evaluated, phenomenon/result/valid/ingestion time separated, and an explicit prohibition on encoding absence as zero. That prohibition *is* "no data ≠ met", one layer down; duplicating it here would create a second absence vocabulary. WM-ECO-006 owns deontic obligations with bearer, violation, penalty and reparation, plus the rule that derived content never acquires normative status over executed text — so a service credit cannot originate in an SLO record. EM-DAT-05 already established that formula, population boundary, unit, dimensions and null semantics belong to an immutable metric definition version, and that changing any of them mints a successor. EM-PRD-02 narrowed WM-ACT-004 to Service Definition (outcome, consumer scope, accountable provider) with commitments held outside it. EM-LEG-01 already ruled that WM-SFT-016 may own targets, observations and error budgets but never obligees, enforceability or remedies.

# Identity/mastership

Stable **SLO identity** = subject reference + SLI specification reference + purpose. Immutable **SLO policy version** = that identity plus target, window definition, eligibility predicate, exclusion set and error-budget policy. Any change to formula, good/valid-event predicate, eligibility, exclusions, target or window mints a successor version; labels and rationale may be corrected editorially with explicit classification. **Evaluation identity** = policy version + window instance; evaluations are append-only and restatements are additive.

Mastership splits: SLO policy versions are mastered as code in Git (reviewable, signed, versioned); the SLI's formula and population are mastered by the Metric Definition registry; observations are mastered by the telemetry store via WM-MAT-008; evaluations are mastered by the evaluator that computed them, recorded with its identity and version. The observability platform is a **source system**, never the master of a commitment. CMDB and the software catalogue master the subject referents only.

# SLI/SLO/evaluation/error budget

**SLI specification**: pins a Metric Definition version and adds what a metric definition cannot carry — the unit of user work (attempt, request, session, job), the *good-event* predicate, the *valid-event* predicate, the observation point (which boundary the events are counted at), and the ObservabilityBinding. Two SLIs over the same formula but different observation points are different SLIs.

**SLO policy**: target, window definition (length, rolling or calendar-aligned, alignment timezone), eligibility predicate, declared exclusions with authority and cap, minimum coverage threshold, and the verdict vocabulary. A target without an SLI reference and a window definition cannot be activated.

**SLO evaluation**: immutable record carrying policy version, window instance bounds with explicit offsets, valid-event count, good-event count, ineligible count by reason, expected-versus-observed coverage fraction, attained value, and a verdict from `met | breached | unknown-insufficient-coverage | no-eligible-traffic | partial-window`. It cites observations; it never stores telemetry.

**Error-budget policy**: budget derived from target and window, consumption ledger per evaluation, and reaction rules as *policy statements* — they trigger obligations elsewhere (change freeze, escalation) and never mutate the evaluation.

# Subject placement

Subject is a typed reference with a declared **subject kind**:

- **Service** (WM-ACT-004 Service Definition) — primary commitment subject; the promise attaches to outcome and consumer scope, so a changed implementation does not restate the SLO.
- **User journey** — a distinct composite subject: an ordered, named set of service-mediated steps with its own outcome criterion. A journey is not a service and not a process; it needs its own subject record, referencing the services it traverses.
- **System/application** (EM-TEC-02) — permitted, and correct for platform-owned reliability, but it is a commitment about a system, never a substitute for the journey SLO.
- **Instance** (EM-TEC-04 runtime) — **diagnostic only**. Instance indicators may not be the subject of a commitment; they roll up only where the SLI declares additivity across the instance dimension.

Rule: commitments live at service and journey; rollup from instance or component to service or journey requires a declared aggregation rule and fails closed where none exists. **Useful user outcome** = an attempt at the journey's or service's declared expected outcome, observed at the boundary closest to the user, satisfying the outcome criterion within the stated latency budget — with the unit of user work, the eligibility predicate and the observation point all named. "99.9%" on a product card, with no window, no unit of work and no observation point, names no SLI and no window instance: it is an unevaluable marketing claim, not evidence of reliability.

# Missing data and windows

Every evaluation carries expected valid events (or expected coverage) against observed, and a declared minimum coverage threshold. Below threshold → `unknown-insufficient-coverage`. Zero eligible traffic → `no-eligible-traffic`, never `met`. Unclassifiable attempts are counted as `indeterminate` and are never folded into good events — the single rule that prevents telemetry loss from reading as success. Gap reasons reuse WM-MAT-008 absence and censoring codes rather than a local vocabulary.

Window definition is part of the policy version. Changing length, alignment, calendar basis or timezone mints a successor, closes open windows on the predecessor, and requires a budget-transition record: the error budget is re-based, never silently recomputed across the change. The first window under a new definition is `partial-window` unless it is fully covered. Cross-version comparison is rejected unless an explicit reconciliation yields `comparable-with-restatement`; absence of a verdict means non-comparable.

# Eligibility/exclusions

Exclusions are declared **ex ante** in the policy version, each with a predicate, an authorising role and a cap on excluded volume or duration. Exclusion reclassifies events to ineligible with a reason code and reports the count; it never deletes events and never reduces the denominator invisibly. Retroactive exclusion is an amendment producing a restated evaluation, with the original retained and both linked. Uncapped or undeclared exclusion is a defect.

# Scenario

Journey J (checkout) traverses S1 auth, S2 pricing, S3 payment; SLI = per-attempt end-to-end success within 3 s, observed at the edge. Mid-month the window changes from 30-day rolling to calendar-month aligned to Europe/Nicosia.

Policy v3 windows close at cutover; v4 opens, and its first month is `partial-window`. The budget is re-based with a transition record; v3 and v4 attainment are not comparable. Separately, S2's collector loses 14 hours of spans: 41,900 of 1,080,000 attempts lack an S2 outcome and cannot be classified, so they are `indeterminate`, not successes. Coverage is 96.1% against a declared 99.0% minimum, so the v4 partial-window evaluation returns **`unknown-insufficient-coverage`**, with counts, gap interval, gap reason and evaluator identity recorded. Had the missing spans been read as "no error observed", the journey would have reported 99.97% and consumed almost no budget — the false success this design blocks. The evaluation is verifiable; it is simply not a pass.

# Invariants

1. An SLO names an SLI specification version, a target and a window definition; none may be defaulted.
2. No data is not met: absence, indeterminate and zero-traffic are distinct verdicts.
3. Missing telemetry never becomes a good event.
4. SLI formula, population and unit are reused from Metric Definition, never restated.
5. Observations are cited, never copied; the model records verdicts and never evaluates telemetry rules.
6. Changing formula, predicate, eligibility, exclusions, target or window mints a policy version; activated versions are immutable.
7. Error budget never carries silently across a window-definition change.
8. Exclusions are declared ex ante, capped, authorised, counted and reported; retroactive exclusion is a restatement.
9. Instance and component indicators are diagnostic; commitments attach to service or journey, and rollup requires declared additivity.
10. SLO and SLA have different bases: no SLO becomes enforceable without an executed clause, a named obligee and a remedy owned by the contract model.
11. Every evaluation is attributable: evaluator identity, version, coverage accounting, window bounds with explicit offsets.
12. Superseded policy versions and restated evaluations remain resolvable.

# Minimal completion shape

SLI specification (metric definition ref, unit of user work, good-event predicate, valid-event predicate, observation point, observability binding). SLO policy (subject ref + subject kind, SLI ref, target, window definition, eligibility, exclusions with caps and authority, minimum coverage, verdict vocabulary). ObservabilityBinding (telemetry source ref, query or stream identity, effective interval, expected-volume basis, known gap ledger). SLO evaluation (policy version, window instance, counts, coverage, attained value, verdict, evaluator, restatement links). Error-budget policy plus consumption ledger and reaction rules as policy statements only.

# Holds

WM-SFT-016 has **no specification file**; evidence is index and publication metadata only. Its registry row sets `parent_ids: WM-ECO-006`, which structurally subordinates SLO to Commercial Contract and contradicts the invariant it must uphold — a registry defect for the registrar to correct before completion, not something to model around. `relations_ref`, `aligned_model_ids` and `contains_ids` are empty, so every boundary here is narrative and unenforced. WM-MAT-008 is a single-provider reviewable draft with an unresolved cardinality hold, an empty relationship contract and three flagged artifact-identity defects; any reliance on its absence and censoring vocabulary inherits those. WM-ACT-004 is a previous-version migration reservation with wildcard imports, and the journey subject it must anchor does not yet exist. The Metric Definition aggregate has no assigned identifier. The `INF.SFT.SLO` placement understates non-software service levels. No semantic crosswalk, immutable refs, fixtures or profile tests have been run. Nothing here is a claim of canonical completeness, conformance or installability.
