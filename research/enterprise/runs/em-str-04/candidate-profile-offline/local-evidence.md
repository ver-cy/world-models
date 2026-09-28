# EM-STR-04 local synthesis

## Disposition

- Reuse WM-ACT-030 as the Initiative root and define an Enterprise investment-rationale profile.
- Keep **Business Case** as an immutable versioned release inside Initiative.
- Keep **Alternative** as an addressable contained record in the appraisal release.
- Reference WM-KNW-016 for Assumption and WM-KNW-009 for Hypothesis.
- Define **Investment Decision** as a profile binding WM-KNW-010 rationale, WM-ACT-024 decision occurrence, WM-REC-010 issued record and WM-ECO-012 funding facts.
- Keep Mandate as an Initiative-scoped authority assertion citing its external instrument. Mandate, approval, funding and realized benefit remain distinct.
- Allocate no new catalogue or runtime identifier.

## Identity and transition

Initiative identity is source-qualified and survives business-case revisions, gates and rejection. Idea, request or ticket becomes an Initiative only through explicit registration with a case for change, mandate and accountable sponsor.

Initiative never changes type in place into Project, Program, Portfolio or operation. Formalization mints a new master identity, records typed derivation and scope mapping, hands over responsibility and preserves residual obligations. A ticket, approval or budget line never creates a delivery object.

## Business case and alternatives

A Business Case release binds problem/opportunity evidence, baseline, mandate, option set, criteria, assumptions, hypotheses, expected-result logic, risk, cost, funding references and uncertainty. Released versions are immutable; changed inputs create successors.

Every comparison uses one pinned criteria set, horizon, currency, price base, valuation basis and metric revisions. It includes a do-nothing or business-as-usual comparator unless the absence is explicitly justified. Mandatory criteria remain separate from compensatory criteria. Ordinal bands and incomparable value/harm dimensions are never arithmetically netted without a declared method.

An Alternative has an Initiative-scoped stable option identity across releases. Each Business Case release holds its own appraisal estimates, uncertainty and risk set. Decision rationale references alternatives and records why one was selected and others rejected. Alternative identity and rationale identity never collapse.

## Assumption, hypothesis and forecast

Assumption is a bounded accepted premise with owner, validity window and defeat condition. Hypothesis is a provisional claim framed for evaluation with predictions and criteria. Forecast is a dated projection with method and confidence. Acceptance never means truth and none converts into another by relabelling.

Defeated assumptions, material forecast divergence, baseline changes, criteria or metric revisions, cost/funding changes, risk breaches, authority changes, gates and horizon expiry trigger review.

## Decision, mandate, funding and benefits

WM-KNW-010 owns rationale content. WM-ACT-024 owns the authorized occurrence. WM-REC-010 owns the fixed issued expression and freezes the complete join to the chosen Business Case release and pinned external revisions. Mandate authorizes exploration within guardrails. WM-ECO-012 owns authorization, allocation, release and availability of funds as separate facts; Initiative holds references only.

Expected benefit references the unallocated Outcome and Benefit Realization candidate. Two alternatives may reference one benefit identity while carrying mutually exclusive forecast values. Those forecasts are never summed. Approval or funding does not prove outcome, causation or benefit realization.

## Grok reconciliation

Grok Heavy returned `Accept with conditions` and agreed that neither Business Case nor Investment Decision needs independent root identity. It sharpened the profile by requiring stable Initiative-scoped option identity across releases, immutable release-local appraisal values, revision-pinned Assumption/Hypothesis/Risk/Budget references and a WM-REC-010 record that freezes the complete decision join. Expected benefit shared across Alternatives is a pinned Opportunity reference; contained expected-benefit content is confined to one Alternative's release-local appraisal. Portfolio-first capital decisions without one Initiative stay outside the profile under WM-ACT-029.

## Frozen-audit reconciliation

The single frozen audit returned `ACCEPT WITH LIMITS`. Its eight holds were incorporated without another audit: REC-1 is the durable decision address and O-1 the temporal anchor; option keys are allocated by Initiative scope; criteria/pin sets are release-local copies or pinned external revisions; funding state kind is frozen with its budget revision; rejection uses WM-REC-010 join discipline; realized benefit stays outside the profile under the delivery identity; supersession is directed and never followed by an as-of decision; and portfolio decisions are never retro-mapped to mandates.

## Acceptance result

Options A and B reference one expected benefit B1 but use different risk sets. BC-1 pins criteria C-v2, the do-nothing baseline, horizon and price base. Decision D-1 is taken at occurrence O-1 and issued as REC-1, selecting A and recording B's rejection basis. A later B1 forecast change creates BC-2 and may trigger review; it does not rewrite BC-1, D-1 or REC-1. The as-of view reproduces the original fixed input package. A rejected Initiative is cancelled and retained. No Project is created without a separate authorizing instrument and typed derivation.

## Required invariants

1. Initiative identity is never reused across formalization.
2. Ticket, approval and budget line never mint delivery identity.
3. Business Case releases are immutable and superseded explicitly.
4. Business Case never substitutes for Initiative identity.
5. Option sets include a do-nothing comparator or explicit exception.
6. Comparison pins criteria, horizon, price base and metric revisions.
7. Estimates include method, unit/scale and uncertainty.
8. Rejected initiatives and alternatives retain evidence and rationale.
9. Mandate, approval, funding availability and benefit realization remain distinct.
10. Assumption, hypothesis and forecast remain distinct.
11. Alternative forecasts sharing one benefit are never summed.
12. Investment decisions are reproducible as-of date from fixed inputs.
13. Decision, event, effective, observation and knowledge times remain distinct.
14. Unallocated and blocked referents are never promoted silently.
15. WM-REC-010 freezes the complete decision join and never points only to live current state.
16. Alternative identity is stable across releases while appraisal values are release-local.
17. Budget mastership remains external to Initiative.
18. Rejected Initiative history cannot be cascade-deleted or reused.
19. Decision labels are narrative aliases; WM-REC-010 is the durable address.
20. Rejection uses the same frozen-join discipline as approval.
21. Decisions never resolve through Business Case supersession chains.
22. Realized benefit remains outside the Initiative profile after formalization.

## Holds

WM-ACT-030 and several adjacent drafts are non-canonical single-provider results. Its registry parent WM-ACT-005 conflicts with the Initiative-is-not-Project boundary. Approved relation rows for Initiative, case, option, decision, budget and formalization are absent. Outcome/Benefit and Metric Definition remain unallocated. Composition/interoperability coverage, source pins, crosswalks, source-master confirmation and fixtures remain incomplete. No installability or publication-readiness claim is made.
