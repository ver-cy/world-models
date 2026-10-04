**Verdict: REVISE.** The proposal’s separations are directionally right. It is not implementable as stated: ShareClass has no assigned identifier; WM-ORG-012 is overloaded by both OwnershipInterest and ControlRelation; legacy WM-ORG-007 reuse is unproven for the required splits; procedure evidence is not forced on Resolution. Do not treat the proposal as a pass, a profile pack ready to load, or a claim of external-standard conformance.

**Strongest evidence:** Rights schedules live on ShareClass (votes-per-unit, economic entitlement, capital rights). Every figure is a calculation that must name right type, class, denominator, time, scenario, rule and inputs. Cross-holdings add a declared cycle convention as an input. Those three rules make “51% economic interest means 51% votes or signing power” an invalid inference by construction.

**Strongest counterexample:** Issuer X has Class A (1 vote/unit) and Class B (10 votes/unit). Holder H has 51% of X’s economic units, all in Class A; Class B sits elsewhere — H is a voting minority. X holds 40% of Y Class A economic units; Y holds 30% of X Class A. Without a declared cycle convention the indirect percentages are undefined, not nettable into one holding. P is appointed to X’s board at t1 and membership ends at t2; attendance at meeting M between t1 and t2 remains true and is not membership at t2. Meeting M records Resolution R without quorum: decision content and authentic expression exist; procedure evidence records the defect. R creates no Mandate and no power to sign.

**Identity / mastership:** Masters stay with cited models except ShareClass. WM-ECO-038 masters holding quantity. WM-ORG-012 masters the inter-organizational link facet only. WM-ORG-018 masters GovernanceBody. WM-ORG-007 is the claimed Mandate master, reuse conditional. WM-KNW-010, WM-REC-010 and WM-ACT-025 remain separate masters under Resolution. ShareClass is the only identifier-unassigned new-model candidate and the only new master this review permits. Independent identity:

- ShareClass — YES. Required. Rights bundle and vote ratio are class-level.
- OwnershipInterest — NO. Profile of WM-ECO-038 and WM-ORG-012.
- ControlRelation — YES as a typed-profile identity on WM-ORG-012. No new WM code. Bare 012 reuse is rejected because OwnershipInterest already profiles 012.
- GovernanceBody — NO. Reuse WM-ORG-018.
- Mandate — NO. Reuse WM-ORG-007 only if 007 already keeps mandate, eligibility, quorum and authority distinct; otherwise the reuse is blocked, not replaced by an invented identifier.
- Resolution — NO. Composition only.

**Ownership / share class:** An OwnershipInterest is one holder, one issuer, one ShareClass, a quantity, a time and a scenario. ShareClass carries the rights schedule. Two classes of one issuer may differ on economic entitlement, capital rights and votes-per-unit. WM-ECO-038 does not master the class; WM-ORG-012 does not master the class. Percentages are calculated, not stored as a second master. Reciprocal holdings do not merge classes or issuers.

**Control / consolidation:** Control is not one 012 edge. Keep contractual control, de-facto control, voting control, consolidation perimeter and signing authority apart. OwnershipInterest must not store `controls=true`. Consolidation cites a named rule, time and scenario; it is not a rollup of economic % or vote %. Signing authority is Mandate-scoped, not a control flag.

**Indirect calculations:** A result that omits right type, class, denominator, time, scenario, rule or inputs is non-authoritative. Walk by class, apply vote ratio at the class, apply eligibility at the body or meeting, apply the cycle convention before aggregation. Reciprocal holdings remain two holdings plus a cycle policy (treasury-elimination, proportional look-through, graph-cut / SCC collapse, or ignore-cycles — named as convention families, not as new identifiers). Convention must be identical inside one scenario or results are incomparable. Time and scenario are part of the identity of a calculated claim.

**Body / membership:** GovernanceBody identity is WM-ORG-018. Meetings do not re-identify the body. Membership is interval-valued. Appointment, attendance, membership, voting eligibility, quorum contribution and authority stay distinct. A membership change does not rewrite historical attendance or past records.

**Mandate / quorum / voting:** Mandate is a grant: grantor, grantee, scope, instrument, effective interval, revocation. Quorum and voting eligibility are body/meeting properties, not Mandate properties. Vote weight is ShareClass ratio × eligible holding, not economic %. Quorum names its denominator (members, votes, or capital). Quorum failure does not delete the meeting record; it blocks valid adoption.

**Resolution / authority:** Resolution composes WM-KNW-010 (decision content), WM-REC-010 (authentic expression) and WM-ACT-025 (procedure evidence). Procedure evidence is mandatory. A no-quorum record can exist as content + expression + failed procedure. It does not confer Mandate or power to sign any contract. Authority to bind is a live Mandate whose scope covers the act.

**Scenario:** Two classes with unequal vote ratios; reciprocal holdings with no implicit netting; board membership change that leaves prior attendance intact; resolution adopted on the record without quorum. Reject every inference from 51% economic interest to 51% votes, consolidation, or signing authority.

**Invariants:**

1. Economic interest ≠ capital rights ≠ voting rights.
2. Voting rights ≠ contractual or de-facto control ≠ consolidation ≠ signing authority.
3. ShareClass is independently identified; never an attribute of a holding, an 012 link, or an organization.
4. Each OwnershipInterest names one class, one holder, one issuer, one time, one scenario.
5. A percentage is undefined unless right type, class, denominator, time, scenario, rule and inputs are declared.
6. A cross-holding calculation without a declared cycle convention is invalid.
7. Reciprocal holdings are two holdings plus a cycle policy, not one net holding.
8. OwnershipInterest does not infer ControlRelation; ControlRelation does not infer Mandate.
9. Consolidation cites a named rule; it is not a rollup of holdings or votes.
10. Appointment ≠ membership ≠ attendance ≠ voting eligibility ≠ quorum ≠ authority.
11. Quorum failure is procedure evidence; it neither erases the record nor creates authority.
12. Time and scenario belong to the identity of any calculated claim.

**Minimum model set:** WM-ECO-038; WM-ORG-012; WM-ORG-018; WM-ORG-007; WM-KNW-010; WM-REC-010; WM-ACT-025; ShareClass (unassigned). Organization, membership, meeting, decision and fixed-record remain boundary types. No further identifiers.
