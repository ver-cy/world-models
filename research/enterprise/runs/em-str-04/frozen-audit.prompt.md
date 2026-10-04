# Frozen no-tools semantic audit — EM-STR-04

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

The result is a PROFILE with WM-ACT-030 Initiative as its only root. Business Case releases, Alternative options/appraisals and Mandate assertions are contained non-roots. Investment Decision is a profile binding WM-KNW-010 rationale, WM-ACT-024 occurrence, WM-REC-010 issued record and WM-ECO-012 funding facts. No new runtime/model identifier is proposed.

Reconciled boundary:
1. WM-ACT-030 remains the sole Initiative root through revisions, gates, rejection and formalization history.
2. Formalization alone mints a separate WM-ACT-005 Project, WM-ACT-029 Program or operation identity with typed derivation, scope mapping, handover and residual obligations. Ticket, mandate, approval and funding never mint delivery identity.
3. Business Case is an immutable versioned release contained by one Initiative. Decisions bind an exact release, never `current case`; later forecasts issue a successor release or non-binding living projection.
4. Alternative has a stable Initiative-scoped option identity across releases. Appraisal values, forecasts, uncertainty, costs and risk sets remain release-local.
5. Every release includes a do-nothing comparator or explicit exception and pins one criteria set, horizon, currency, price base, valuation basis, metric revisions, method and uncertainty.
6. Assumption (WM-KNW-016), Hypothesis (WM-KNW-009), Risk/Opportunity (WM-KNW-015) and Budget (WM-ECO-012) remain external masters. Every reference pins an immutable revision or snapshot value; live-only pointers fail closed.
7. Investment Decision binds WM-KNW-010 rationale, WM-ACT-024 occurrence, WM-REC-010 issued record and WM-ECO-012 funding facts. WM-REC-010 freezes the complete join for as-of reproduction.
8. Mandate is Initiative-scoped and non-shareable. Mandate, approval, funding authorization/allocation/release/availability, formalization and realized benefit remain distinct.
9. Expected benefit is Initiative-contained appraisal content or a pinned WM-KNW-015 Opportunity reference. No Benefit root is invented. Alternative forecasts sharing one expected benefit are mutually exclusive and never summed.
10. Cost estimate, funding availability and realized spend are distinct. Realized benefit is post-delivery and never inferred from approval, activity, output or spend.
11. Rejected Initiatives retain identity, releases, alternatives, evidence and rejection records. Cascade deletion and identity reuse are forbidden.
12. Portfolio-first capital decisions without one Initiative remain WM-ACT-029-owned and outside this profile.

Scenario: Initiative I contains BC-1 with Alternatives A, B and Do-Nothing under one pin set. A and B reference the same expected-benefit fact but distinct risks and costs. Decision D-1 occurs as O-1 and is issued as REC-1, which freezes BC-1 plus exact rationale, assumption, hypothesis, risk and budget revisions. A later forecast creates BC-2 with the same option identities and new appraisal values. Reproducing D-1 returns BC-1 and its frozen join. A rejected Initiative remains addressable and creates no Project. A ticket, approval or funding fact cannot mint delivery identity.

Audit questions:
- Is there a hidden aggregate or identifier despite `newRuntimeId=false`?
- Are Initiative, release, option, appraisal, knowledge, decision, record, budget and delivery mastership unambiguous?
- Can WM-REC-010 deterministically reproduce the decision without remastering external facts?
- Are formalization, rejection, forecast supersession and portfolio-first scope safe?
- Identify any contradiction that makes even a held profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the profile.
