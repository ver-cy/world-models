# Independent enterprise metamodel study — EM-XCT-06

Study date: 21 September 2026 UTC. Produce an independent, substantive English research memo for Vercy. The owner wants composable metamodels usable by a small startup and a large international, software, hardware or AI company. This is not a description of any real company's internals. Another provider receives this identical brief independently; you are not given its answer. This is a research/design study, not an audit of implemented code and not authorization to publish. Do not use private files, organizational extracts, actual personnel or credentials.

Use primary official sources if your tools permit browsing. Identify exactly what you actually opened, the edition/section and access limitations. If browsing fails or you rely on memory, mark it unverified rather than fabricate fresh source verification. Do not run code or use MCP/local filesystem. Cite usable official URLs, not search-result links. Paid standards you cannot read establish only their published scope, not full conformance. Do not copy proprietary schemas, tables or currency/unit databases. Separate normative observation, source assertion, inference and your proposal.

## Problem and object boundary to challenge

EM-XCT-06 is a research contour, not automatically one model or one database table. Its proposed vocabulary is Quantity, Money, UnitReference, CalendarReference and LocalizedText, plus reusable magnitude/range/date conventions. We must preserve precision, units, currency effective time and rate provenance, calendar and timezone context, and distinguish a translation/label from a new entity. Eight hours in different working calendars must not silently mean identical available capacity.

Choose reuse, exact profile, separate shared contracts, new independently identified records, adapters or explicit deferral. Do not create a giant universal value bag or manufacture model identities to fit the research list. Do not demand every primitive have an independent lifecycle if it is an embedded value. Conversely, preserve independently governed rate observations, unit-definition revisions, calendar revisions, conversion decisions/receipts or designation assertions where their identity, authority or correction behavior requires it. A computed value does not become its source's master fact.

Distinguish quantity kind, physical dimension, unit and scalar; a numerical monetary amount, a currency definition and an exchange-rate observation; instant, local civil date/time, wall-clock duration, elapsed duration, working-calendar availability; language tag, locale/formatting policy, designation assertion and object identity. Consider temperature point versus delta, dimensionless ratios/percentages, nonlinear/logarithmic units, unknown/approximate/ranged/censored values, currency changes and non-ISO assets without assuming all are immediately implementable.

## Current Vercy candidates — metadata only, not asserted compatibility

Exact current spec bytes have been retrieved and hash-compared by Codex; full semantic comparison is a separate ongoing step. All following candidate versions are published 0.3.0-research.1 and marked installable in the runtime catalogue; that does not establish production, source or standards assurance. Optional URLs below may be opened for actual semantic reading. Do not claim to have read them if you have not.

| Candidate | Official Vercy spec | SHA-256 |
|---|---|---|
| WM-XCT-008 Quantity / Unit | https://ver.cy/models/wm-xct-008-quantity-unit/spec.yaml | b315e808411d0a4f4009f057707454164ccbe5ac8bf99b5ad2864b9d1e334dde |
| WM-XCT-009 Time / Calendar | https://ver.cy/models/wm-xct-009-time-calendar/spec.yaml | inspect actual runtime/publication metadata; no unverified hash supplied here |
| WM-XCT-010 Location Referencing / Address | https://ver.cy/models/wm-xct-010-location-referencing-address/spec.yaml | 2db36973c77f288e2f9d6e977fc694fda067a65271d2911c3504a9b4d749e9a4 |
| WM-XCT-031 Localization / Language | https://ver.cy/models/wm-xct-031-localization-language/spec.yaml | 8d9903a28c0385c790abbe1965eb5c716ba58ae1084474641cf16671466935f9 |
| WM-XCT-032 Currency / Monetary Value | https://ver.cy/models/wm-xct-032-currency-monetary-value/spec.yaml | b102b6cba7cca2717d71791736633397ffe92377039817395bdab9bf1be3a7c0 |

The initial assignment mistakenly associated 010 with this calendar-oriented contour. It is a location/address model, not a replacement for 009. Local place may help select a calendar/timezone, but an address must not silently determine either. Preserve inherited publication holds. No runtime subtype or dependency is implied by this table.

Vercy metamodels expose Bundles → Layers → Findings → Questions → evidence Artifacts → proposed Actions, plus stable identities, fields/relations, lifecycle, provenance and mastership. One projection describes one canonical object. Instance relationships, specification dependencies and delivery packages are distinct graphs. Reference validators must be distinguished from host policy and actual source resolution. Unknown is not zero, an unavailable rate is not one, a formatted string is not the canonical value, and a successful calculation is not permission to execute a payment or staffing decision.

## Research tracks

Compare at least three substantive schools using primary sources: standards/ontologies (e.g. BIPM SI, QUDT, UCUM, W3C Time, BCP 47); actual open-system practice (e.g. exact decimal arithmetic, unit-aware libraries, IANA tzdb/Temporal, financial value APIs); and a competing domain/modelling school (e.g. quantity calculus versus lexical codes, money amount versus posted accounting, local civil scheduling versus elapsed time). Unicode CLDR is a formatting/localization data source, not an identity oracle. ISO 4217 scope/maintenance and a real provider's explicitly non-transactional reference-rate policy may be useful; do not claim unlicensed full ISO contents.

## Required output

1. Recommend a practical minimal first publication and what should remain separate or deferred. For every proposed canonical type: definition, identity and correction/split rules, neighbor distinction, owner, source, independent applicability, lifecycle and chosen form. Avoid over-building a production engine to justify a schema, but identify hidden unsafe assumptions.
2. Compare the Vercy candidates only to the extent actually read. Give exact/narrower/broader/overlap/unrelated plus reuse/profile/new/defer and losses. Preserve disagreements and uncertainty; do not equate a hash with semantic compatibility.
3. Propose concrete fields (type, precision/scale/unit, required/nullability/cardinality, computed versus asserted, sensitivity), qualified relations and lifecycle transitions with actor/guard/evidence. Distinguish schema versions, definition versions, object revisions and state.
4. Propose at least 15 useful question routes with bundle/layer placement, expected facts/artifacts and permitted proposed action. Include missing-context behavior and one minimal startup example.
5. Cover all five facets separately for each independent type: identity/class, direct properties, recognition/observation, capabilities/actions and context/evidence. Delegate only to an exact actually known contract or label the dependency unresolved.
6. Give an authority matrix: semantic owner, authoritative system, allowed writer/read purpose, effective/recorded/as-of time, conflicts, disclosure and retention. Do not assume HRIS/ERP is mandatory or authoritative everywhere. Imported reference data is evidence, not a new right to serve it.
7. Specify at least 12 meaningful invariants and at least 12 negative cases. Classify what schema can check, what semantic code can check, what requires a trusted host and what needs expert judgment. Include immutable correction, replay, conflict, reference drift, rights, same-version roundtrip and cross-version refusal/migration.
8. Explain exact arithmetic and rounding, rational or decimal factors and FX direction/source/date, timezone/calendar versions and DST ambiguity, and qualified designation identity. Recommend bounded executable behavior only where a small independent implementation is defensible. Do not endorse ambient locale, floats or stale data as implicit context.
9. Give a source table with official URL, version/date/section, claim, boundary implication, adopted/rejected/unknown and actual verification depth. State licensing and unread-source limits. No standards-conformance claim without actual clause-level evidence.
10. Finish with concrete acceptance criteria, highest-risk design alternatives, proposed publication limits and a step-by-step implementation/research assignment. No fabricated execution or file hash verification.

## Same synthetic acceptance cases for both providers

A. Startup: an invoice line has an exact fractional quantity, unit price and currency; calculation declares multiplication and rounding. A translated product label leaves product identity unchanged. No hidden ERP, FX feed or locale may be assumed. Rounding per line versus after summation must remain distinct.

B. International matrix: a monetary estimate uses an attributed FX quote with base/quote direction, observation/effective time and intended purpose; a rate correction must not rewrite the earlier published result. Mixed EUR/USD cannot be added without a specific policy/context. Eight nominal working hours in two dated calendars do not establish equal availability; leave, location and DST are separately governed inputs. Preserve a local time falling in a DST gap or overlap without silently choosing an instant.

C. Hardware/AI: a temperature point is not a temperature difference; equal physical dimension is insufficient to establish quantity-kind substitutability. Decimal/rational unit conversion must declare its definition revision and rounding. A model-release label in two languages remains one release; a locale-specific decimal separator never changes the stored magnitude. Nonlinear units, uncertainty propagation and real financial/workforce actions can be deferred explicitly rather than falsely implemented.

D. Historical/drift negatives: an unchanged short unit/currency code whose issuer/version changed; a reversed FX pair; a stale as-of quote; an ambiguous local time; an unknown currency with assumed two decimal places; incompatible quantity kinds; self-certified calibration; unknown treated as zero; duplicate/missing designation language; silently changed rounding context; mismatched definition pin; lost provenance after import.

Provide one complete English memo. If a source or candidate is inaccessible, continue the independent conceptual study and name the exact unverified area. Do not contact others, publish, or modify any external state.
