# Independent enterprise metamodel study — EM-XCT-06

**To:** Vercy  
**From:** Independent research desk (dual-provider assignment; this memo is one of two independently produced answers)  
**Study date named in the brief:** 21 September 2026 UTC  
**Memo date:** 22 September 2026  
**Object:** Composable metamodels usable by a small startup and by a large international software, hardware or AI company  
**Status:** Research / design study. Not an audit of implemented code. Not authorization to publish. Not a description of any real company’s internals.

**Classification of statements used below.**  
- *Observation:* what a page we opened actually said, at the depth we reached.  
- *Source assertion:* a claim the source makes about its own authority or scope.  
- *Inference:* our reading of implications.  
- *Proposal:* what this study recommends Vercy publish, keep separate, or defer.

---

## How this study was done

Tools permitted browsing of public URLs. They returned **summarizer extracts**, not raw file bytes. We did **not** run code, compute hashes, use a local filesystem as an evidence store, contact third parties, or modify external state. The SHA-256 values in the assignment table are **not independently verified** and are **not** treated as semantic compatibility.

**Vercy candidate specs actually opened**

| URL opened | What was visible | Access limit |
|---|---|---|
| `https://ver.cy/models/wm-xct-008-quantity-unit/spec.yaml` | YAML/JSON hybrid; `vercy: 1.0-draft`; version `0.3.0-research.1`; `publishableCanonical: false`; `adjudicationStatus: reviewable-draft`; generated `2026-08-23T03:58:21Z`; dual-provider Claude + Grok | Summarizer-truncated; not raw bytes |
| `https://ver.cy/models/wm-xct-009-time-calendar/spec.yaml` | Same publication envelope; generated `2026-08-22T21:28:49Z`; no SHA-256 was supplied in the brief | Same |
| `https://ver.cy/models/wm-xct-010-location-referencing-address/spec.yaml` | Location / address model | Same |
| `https://ver.cy/models/wm-xct-031-localization-language/spec.yaml` | Generated `2026-09-03T14:02:45Z`; **single-provider-waiver** (Claude; Grok waived) | Same |
| `https://ver.cy/models/wm-xct-032-currency-monetary-value/spec.yaml` | Generated `2026-09-03T21:52:36Z`; `publishableCanonical: false`; provider-mode **unverified in one extract, reported as single-provider-waiver in another** — treat provider-mode of 032 as **uncertain** | Same |

**Primary official sources actually opened** (full table in §9): BIPM SI Brochure landing and selected passages of the 9th-edition English PDF; VIM JCGM 200:2012 selected definitions; UCUM spec page; QUDT overview and GitHub releases; W3C OWL-Time TR; RFC 5646; RFC 3339; IANA tz-link; TC39 Temporal docs and timezone page; Unicode CLDR landing; SIX ISO 4217 Maintenance Agency landing; ECB euro reference-rate page; Federal Reserve H.10 about page.

**Unread / unverified on purpose:** full SI Brochure clause audit; ISO 80000 series (paywalled); full ISO 4217:2015 text and code tables (not copied); IEEE 754-2019 full text; ISO 8601-1/2; ISO 20022 schemas; GUM full text; CLDR/LDML full data; ECB framework PDF at one tried path that 404’d; candidate YAML raw bytes and the brief’s SHA-256 column.

---

## 1. Practical minimal first publication

**Proposal.** Publish **five small shared contracts**, not one universal value bag and not five production engines. A startup must be able to issue an invoice line without standing up a unit-conversion service, an FX feed, a tz compiler or a CLDR snapshot. A large company must be able to pin registries, attribute rates and refuse unsafe arithmetic without being forced through an ERP or HRIS.

### 1.1 Publish now (minimal contracts)

| Contract | Form | Why first |
|---|---|---|
| **QuantityValue** | Embedded value object | Case A quantity and Case C temperature/unit conversion rest on it |
| **UnitReference** | Pinned pointer (not the magnitude) | Short codes drift; the pin is the reusable fact |
| **MonetaryAmount** + **CurrencyReference** | Embedded amount + pinned catalogue pointer | Case A invoice; Case B mixed-currency refusal |
| **ExchangeRateObservation** | Independently identified record | Case B attributed FX; correction must not rewrite a published result |
| **Temporal value shapes** + **CalendarReference** / **TzdbReleasePin** | Embedded Instant / CivilDateTime / ExactDuration / NominalDuration + pinned reference data | Case B DST and “eight hours ≠ eight hours” |
| **LocalizedText** | Embedded designation | Cases A and C: translation does not mint a new entity |

### 1.2 Keep separate (independently identified when governance requires it)

- **QuantityKind** record (governed id + vocabulary version).  
- **UnitDefinitionRevision** (expression, factor/offset, edition).  
- **CurrencyDefinition snapshot** (catalogue + edition + digest + status; published minor unit only if the pinned edition states one).  
- **ConversionReceipt / CalculationReceipt** (inputs, operation, rounding context, result). A computed value is not the source’s master fact.  
- **DesignationAssertion** when a label is governed (effective interval, supersession, asserter). Otherwise LocalizedText stays embedded.  
- **WorkingAvailability** as a *derived projection*, never as a stored “8 hours” master.

### 1.3 Explicit deferrals (name them so they are not falsely implemented)

- Uncertainty-budget / GUM propagation.  
- Nonlinear and logarithmic unit *execution* (declare “not linear”; do not pretend to convert).  
- Holiday / recurrence / leap-smear engines.  
- Payment, settlement, ledger posting, staffing permission.  
- Crypto / community / non-ISO assets as first-class ISO-like currencies.  
- Ambient locale, binary floating point, “unknown = 0”, “missing rate = 1”.  
- Treating an address (WM-XCT-010) as a timezone or working calendar.

### 1.4 For every proposed canonical type

#### QuantityValue

- **Definition.** A number bound to a quantity kind and a unit reference, with an explicit value form (point, range, censored, unknown/absent).  
- **Identity.** None independent. Host record owns it.  
- **Correction / split.** Never mutate magnitude independently of unit. Correction is a new host revision or a CalculationReceipt. Split a range into endpoints only as derived views that cite the source.  
- **Neighbor distinction.** Not MonetaryAmount (currency has no ISQ dimension). Not Instant. Not a measurement act. Not a nominal property (VIM 1.30: no magnitude).  
- **Owner / source.** Host product. Source category: asserted | measured | computed | converted.  
- **Independent applicability.** Any measured or computed magnitude slot.  
- **Lifecycle / form.** Host lifecycle. Embedded value.  
- **Hidden unsafe assumption.** That the host has pinned a unit vocabulary. Without the pin, `kg` versus a later homograph is silent drift.

#### UnitReference

- **Definition.** A pointer to a unit in a named code system at a named edition (`code` + `codeSystem` + `systemVersion`, optional alternate codes).  
- **Identity.** The triple above. A glyph or short symbol is not identity.  
- **Correction.** New pin. Stored values keep the pin they were written under.  
- **Neighbor.** Not QuantityKind. Not the display name. Not a currency code.  
- **Owner.** Unit-system steward (BIPM for SI meaning; UCUM / QUDT / UN/CEFACT for chosen encodings). Imported tables are evidence.  
- **Form.** Reference object.

#### QuantityKind

- **Definition.** The aspect common to mutually comparable quantities (VIM 1.2, as read in JCGM 200:2012).  
- **Identity.** Governed identifier + vocabulary version.  
- **Correction.** Vocabulary revision; instances pin the version used.  
- **Neighbor.** Dimension vector is a commensurability fingerprint, **not** the kind. Same dimension does not make kinds substitutable (thermodynamic temperature versus temperature difference; energy versus torque).  
- **Form.** Independently identified record if the adopter governs kinds; otherwise a pinned external id.

#### MonetaryAmount

- **Definition.** An exact decimal amount inseparably bound to a CurrencyReference, with declared scale and optional rounding intent.  
- **Identity.** None independent.  
- **Correction.** New declaration. An FX correction **must not** rewrite an earlier published amount.  
- **Neighbor.** Not QuantityValue. Not ExchangeRateObservation. Not a journal posting. Not a price list.  
- **Owner.** Host (invoice line, estimate, budget cell).  
- **Form.** Embedded value.  
- **Hidden unsafe assumption.** That ISO minor-unit digits may be inferred when the currency is unknown. Case D forbids that.

#### CurrencyReference / CurrencyDefinition

- **Definition.** Catalogue identity of a currency, fund or metal at a pinned edition.  
- **Identity.** `(catalogue, edition, alphabetic code)` and/or numeric code. Short letters without edition are insufficient.  
- **Correction.** Succession pointer (redenomination, historic move). Do not restated historical amounts automatically.  
- **Owner.** ISO 4217 Maintenance Agency (SIX, on the page we opened) or a declared alternate catalogue. Importing a list does not create a right to re-serve it as if we were the MA.  
- **Form.** Pinned reference + optional snapshot record.

#### ExchangeRateObservation

- **Definition.** An attributed quote: base, quote, direction as published, rate decimal, unit count, source, series, observation / publication / retrieval / effective times, purpose, quality, usage restriction.  
- **Identity.** Independent. Reversed pair is a different observation.  
- **Correction.** Superseding observation. Prior published *results* stay.  
- **Neighbor.** Not the converted MonetaryAmount. Not a tradable benchmark unless the publisher says so.  
- **Owner.** Rate publisher (example: ECB reference rates) or a named internal treasury source.  
- **Lifecycle.** `recorded → published → superseded | withdrawn`. Published observations are immutable.

#### Instant

- **Definition.** Zero-extent position on a named time scale, typically carried as RFC 3339 with an explicit offset or `Z`. `-00:00` only when the offset is genuinely unknown (RFC 3339).
- **Identity.** Embedded.  
- **Neighbor.** Not CivilDateTime. Not Duration.

#### CivilDateTime

- **Definition.** Local civil date and time plus optional zone id, calendar key, tzdb release pin, binding mode and disambiguation policy.  
- **Identity.** Embedded. A civil time that falls in a DST gap or overlap is **preserved**; an instant is derived only under an explicit policy.  
- **Neighbor.** Not Instant. Not WorkingAvailability. Not an address.

#### ExactDuration vs NominalDuration

- **Definition.** ExactDuration is elapsed time on a time scale (SI-second count). NominalDuration is calendar-clock quantity (days, months, “eight hours” as a schedule token). They do not share a field.  
- **Neighbor.** WorkingAvailability is a derived function of a dated calendar revision, leave, location and DST inputs — not a duration.

#### CalendarReference / TzdbReleasePin

- **Definition.** Pointer to a calendar system and/or IANA tzid plus the tzdb release used.  
- **Identity.** Independent for the reference-data release; embedded when only citing.  
- **Source assertion we adopt:** IANA’s tz-link page states the database is **not authoritative**; governments control the rules.

#### LocalizedText / DesignationAssertion

- **Definition.** Text in a BCP 47 language tag bound to a designated object. A tag identifies language of content, not object identity (RFC 5646).
- **Identity of the text.** Embedded.  
- **Identity of a governed assertion.** `(objectRef, fieldPath, languageTag, version)`.  
- **Correction.** Supersede the assertion; do not mint a new product or release.  
- **Neighbor.** Locale / formatting policy (CLDR) is a rendering context and **must not** change stored magnitude. CLDR is not an identity oracle.

---

## 2. Comparison with Vercy candidates (only what was actually read)

All five candidates are published `0.3.0-research.1`, `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`. That is a **catalogue status**, not production, source or standards assurance. Hash in the brief ≠ semantics.

| Candidate | Relation to this contour | Reuse decision | Losses if adopted whole | Disagreements / uncertainty |
|---|---|---|---|---|
| **WM-XCT-008 Quantity / Unit** | **Overlap / broader** than the first publication. Explicitly **out of scope for money**, calendar instants as first-class entities, and the measurement act. Distinguishes kind, dimension, unit, scalar; point vs difference; exact decimal lexical form; registry pins. | **Profile** QuantityValue + UnitReference. Do not swallow GUM/traceability/plausibility machinery. | Over-built uncertainty and calibration fields; startup would appear to need a metrology engine. | Aligns QUDT and UCUM at once; those systems disagree on some dimensional treatments (e.g. plane angle). Do not collapse. |
| **WM-XCT-009 Time / Calendar** | **Overlap / broader.** Mixin + governed reference data. Instant vs civil vs exact/nominal duration; working-day calendar as composed/derived; gap/overlap functions; tzdb as mirror not legal oracle. | **Profile** the value shapes and CalendarReference. **Defer** holiday engine, recurrence expansion, leap tables as executable services. | Recurrence / observance / business-centre engine is a product, not a first schema. | Brief supplied **no hash** for 009. We invent none. OWL-Time is a class split, not a staffing calendar. |
| **WM-XCT-010 Location / Address** | **Unrelated** to this contour. Purpose on the opened spec is addresses, locators, gazetteers. No statement that an address determines timezone or calendar. | **Do not reuse.** Place **may** be an input to *select* a calendar; it **must not** silently determine one. Preserve inherited publication holds. | — | Initial assignment error confirmed. |
| **WM-XCT-031 Localization / Language** | **Overlap / narrower-or-different.** Mixin for locale *binding*; explicitly does **not** hold localized content. BCP 47 well-formed vs valid; declared vs detected; translation does not change host identity; CLDR is pinned convention data. Single-provider-waiver. | **Profile** tag/locale machinery. **New** small LocalizedText value for the label itself. **Defer** TMS / XLIFF. | Binding-lifecycle field explosion; lower assurance because Grok was waived. | 031 is a binding, not the text. Contour needs both. |
| **WM-XCT-032 Currency / Monetary Value** | **Overlap / broader.** Exact decimal (sign, coefficient, scale); currency pinned to catalogue edition; absence ≠ zero; FX as referenced observation with direction, purpose, times; mixin is never a ledger or payment. | **Profile** MonetaryAmount + CurrencyReference. **New** independent ExchangeRateObservation (032 already treats the publisher as owner of the series — agree). **Defer** cash increments, cross-rate engine, payment permission. | Field explosion; ISO 4217 list contents unread here; provider-mode uncertain. | 008 routes currency *entirely* out; 032 still shares numeric-fidelity rules with 008. **Do not merge into one type.** |

**Proposal.** Treat 008 and 032 as neighboring profiles that share *numeric fidelity* and *nothing else*. Treat 009 as the temporal profile. Treat 031 as the language-tag profile. Treat 010 as out of contour.

---

## 3. Concrete fields, relations and lifecycle

Notation: `req` = required, `0..1` optional, `0..n` repeatable. “Computed” means derived and never the master fact.

### 3.1 QuantityValue (embedded)

| Field | Type | Precision / unit | Card. | Computed? | Sensitivity |
|---|---|---|---|---|---|
| `numericLexical` | string (decimal or rational `p/q`) | Exact lexical; trailing zeros significant when exactness says so | 1 if valueForm ∈ {point, range endpoints}; else 0 | asserted | inherits host |
| `valueForm` | enum `point \| range \| censored \| unknown \| absent` | — | 1 req | asserted | — |
| `absentReason` | enum / code | — | 0..1 req if absent | asserted | — |
| `quantityKindId` | string | pinned vocab id | 1 req | asserted | — |
| `kindVocabVersion` | string | — | 0..1 (req before compare/convert) | asserted | — |
| `unitRef` | UnitReference | — | 0..1 | asserted | — |
| `unitAbsenceReason` | enum | — | 0..1; XOR with unitRef | asserted | — |
| `pointOrDifference` | enum `point \| difference` | mandatory when kind is interval-scale | 0..1 | asserted | — |
| `exactness` | enum `exact \| approximate \| unknown` | — | 0..1 | asserted | — |
| `bounds` | pair of QuantityValue-like endpoints | same kind/unit | 0..1 | asserted | — |
| `originCategory` | enum `asserted \| measured \| computed \| converted` | — | 0..1 | asserted | — |

**Invariant at this layer:** `unitRef` XOR `unitAbsenceReason`. `numericLexical` present XOR (`valueForm = absent` AND `absentReason`). Binary float is not an admitted source.

### 3.2 UnitReference

| Field | Type | Card. |
|---|---|---|
| `unitCode` or `unitExpression` | string | 1 |
| `codeSystem` | string / IRI | 1 |
| `systemVersion` | string | 1 before conversion |
| `altCodes` | list `{system, code, version, mappingStrength}` | 0..n |
| `definitionRevisionId` | string | 0..1; req before conversion |

### 3.3 MonetaryAmount (embedded)

| Field | Type | Card. | Notes |
|---|---|---|---|
| `valueState` | enum `exact \| interval \| approximate \| absent` | 1 | absent ≠ 0 |
| `sign` | enum `+ \| − \| 0` | 1 if present | negative-zero policy declared if used |
| `coefficient` | integer-string | 1 if present | or equivalent exact decimal lexical |
| `scale` | non-negative integer | 1 if present | **declared**, not inferred |
| `currencyRef` | CurrencyReference | 1 if present | inseparable |
| `roundingMode` | enum e.g. `half_even \| half_up \| toward_zero \| …` | 0..1 | named; no ambient default |
| `roundingStage` | enum `line \| after_sum \| none` | 0..1 | Case A: line vs sum remain distinct |
| `computedVsAsserted` | enum | 0..1 | computed cites a receipt |
| `absentReason` | enum | 0..1 | |

### 3.4 CurrencyReference

| Field | Type | Card. |
|---|---|---|
| `alphabeticCode` | string | 1 |
| `numericCode` | string | 0..1 |
| `catalogueId` | string | 1 |
| `catalogueEdition` | string | 1 |
| `catalogueDigest` | string | 0..1 recommended |
| `codeClass` | enum `active \| historic \| fund \| testing \| metal \| unknown \| non_iso` | 0..1 |
| `publishedMinorUnit` | integer | 0..1; **null if unknown** — never default 2 |

### 3.5 ExchangeRateObservation (independent)

| Field | Type | Card. |
|---|---|---|
| `id` | identifier | 1 |
| `baseCode` / `quoteCode` | string | 1 / 1 |
| `directionAsPublished` | enum `base_per_quote \| quote_per_base` plus unit count | 1 |
| `rateDecimal` | exact decimal lexical | 1 |
| `unitCount` | integer | 1 default 1 |
| `sourceId` | identifier | 1 |
| `seriesId` | identifier | 0..1 |
| `purposeCode` | code (`information_reference \| customs \| internal_planning \| …`) | 1 |
| `quality` | enum `provisional \| final \| estimated \| stale` | 1 |
| `observationTime` | Instant | 1 |
| `publicationTime` | Instant | 0..1 |
| `retrievalTime` | Instant | 1 |
| `effectiveFrom` / `effectiveTo` | Instant | 1 / 0..1 |
| `usageRestriction` | text | 0..1 |
| `supersedesRef` | reference | 0..1 |

**Lifecycle.** `recorded → published → superseded | withdrawn`. Guard: a published observation is immutable. Actor: catalogue steward (record) / publisher (authority) / host finance role (bind to a valuation). Evidence: publisher snapshot + retrieval digest. Effect of correction: new observation; **no write** to previously published MonetaryAmount or CalculationReceipt.

### 3.6 Temporal shapes (embedded)

| Field | Instant | CivilDateTime | ExactDuration | NominalDuration |
|---|---|---|---|---|
| payload | RFC 3339 date-time | civil date-time lexical | seconds lexical | calendar-unit tuple |
| offset / Z | required (`-00:00` only if unknown) | optional | n/a | n/a |
| `tzId` | 0..1 | 0..1 (req if zoned) | — | — |
| `calendarKey` | — | 0..1 | — | 0..1 |
| `tzdbVersion` | 0..1 | 0..1 req if resolving | — | — |
| `bindingMode` | `absolute` | `instant \| zoned \| floating` **req** | — | — |
| `disambiguationPolicy` | — | `earlier \| later \| compatible \| reject \| preserve_unresolved` req if zoned | — | — |
| `resolvedOffset` | — | 0..1 **computed** | — | — |

WorkingAvailability is **not** a column on these shapes. It is a derived record: `{calendarRevision, date, leaveSet, locationRef, dstRulesPin, result, inputsDigest}`.

### 3.7 LocalizedText (embedded)

| Field | Type | Card. |
|---|---|---|
| `text` | string | 1 |
| `languageTagOriginal` | string | 1 |
| `languageTagCanonical` | string | 0..1 computed, never silently overwrites original |
| `script` / `dir` | code | 0..1 |
| `role` | enum `label \| description \| legal` | 0..1 |

DesignationAssertion adds `objectRef`, `fieldPath`, `version`, `effectiveFrom/To`, `asserterRef`, `supersedesRef`, `state`.

### 3.8 Version quadruple (do not collapse)

1. **Schema version** — shape of the contract (`0.3.0-research.1` on candidates).  
2. **Definition version** — UCUM / QUDT / ISO 4217 edition / tzdb release / IANA language-subtag File-Date.  
3. **Object revision** — host record or independent observation version.  
4. **Lifecycle state** — draft / published / superseded / withdrawn.

Same-version round-trip must preserve lexical trailing zeros, original language tag and unresolved civil time. Cross-version change is refuse or an explicit migration map.

### 3.9 Qualified relations

- QuantityValue `unitRef` → UnitReference.  
- QuantityValue `kindRef` → QuantityKind.  
- MonetaryAmount `currencyRef` → CurrencyReference.  
- MonetaryAmount `valuationRateRef` → ExchangeRateObservation (optional).  
- CalculationReceipt `inputs[]` → QuantityValue and/or MonetaryAmount; `rateRefs[]` → ExchangeRateObservation.  
- CivilDateTime `calendarRef` → CalendarReference; `tzdbPin` → TzdbRelease.  
- LocalizedText / DesignationAssertion `objectRef` → host identity (**not** a new identity).  
- WorkingAvailability `locationHint` → WM-XCT-010 **optional, non-determining**.

---

## 4. Question routes (≥15)

Bundle: `EM-XCT-06`. Layers: `L-Qty`, `L-Money`, `L-Time`, `L-Text`, `L-XCut`.

Missing-context rule for all routes: **refuse the operation**, keep recorded facts, propose `request-pin | request-policy | request-disambiguation`. Never invent unit, scale, rate, timezone, locale or zero.

| ID | Layer | Question | Expected facts / artifacts | Permitted proposed action | Missing-context behavior |
|---|---|---|---|---|---|
| Q1 | L-Qty | Are kind and unit present and pinned? | `quantityKindId`, vocab version, unit code/system/version | accept embed / `reject-incomplete` | refuse compare and convert |
| Q2 | L-Qty | Temperature **point** or **difference**? | `pointOrDifference` | convert-with-offset / convert-scale-only / refuse | refuse °C↔K as if ratio |
| Q3 | L-Qty | Same dimension — are kinds substitutable? | kind pair, dimension vector | refuse unless exact kind match | refuse |
| Q4 | L-Qty | Which definition revision authorises conversion? | factor/offset, `definitionRevisionId`, rounding | emit ConversionReceipt / refuse | refuse |
| Q5 | L-Money | Are amount and currency inseparable and exact? | lexical or coefficient+scale, currency, catalogue edition | persist pair | refuse; zero is not absence |
| Q6 | L-Money | Line rounding or after-sum rounding? | `roundingMode`, `roundingStage` | compute the declared one; keep the other distinct | refuse unnamed rule |
| Q7 | L-Money | Is the FX quote attributed? | base, quote, direction, source, observation/effective time, purpose | bind ExchangeRateObservation | refuse convert |
| Q8 | L-Money | May a rate correction rewrite a published estimate? | prior observation id, new observation, published result id | supersede rate; **never** rewrite result | — |
| Q9 | L-Money | May EUR and USD be added? | currencies, `policyContextId`, rate set | add only under named policy | refuse |
| Q10 | L-Time | What is the binding mode? | `instant \| zoned \| floating`, offset or Z | accept | reject unqualified local at boundary |
| Q11 | L-Time | Does this local time fall in a DST gap or overlap? | civil local, tzId, tzdb release, disambiguation policy | preserve civil + policy; derive instant only if policy ≠ preserve | reject silent pick |
| Q12 | L-Time | Do eight nominal hours in calendar A equal availability in calendar B on date D? | two calendar revisions, date, leave, location, DST | compute separately; never equate | result = unknown, not equal |
| Q13 | L-Text | Does a translated label create a new product or release? | object id + LocalizedText set | attach label | identity unchanged |
| Q14 | L-Text | Does a locale decimal separator change stored magnitude? | `numericLexical` vs display string | display only | store unchanged |
| Q15 | L-Text | Is the language tag well-formed, valid, and File-Date pinned? | original tag, canonical form, registry File-Date | record original; map preferred-value as annotation | do not drop tag |
| Q16 | L-XCut | Unchanged short code, changed issuer/version? | code + old edition + new edition | treat as potential new definition | require pin |
| Q17 | L-XCut | Is imported reference data a right to re-serve it? | licence / MA policy / publisher restriction | cite as evidence | no new serve-right |
| Q18 | L-Money | Unknown currency — assume two decimal places? | codeClass, publishedMinorUnit | refuse assumption; require explicit scale marked unresolved | refuse |

**Minimal startup example (Case A).**  
Invoice line `IL-441`:

- QuantityValue: `numericLexical = "2.500"`, kind = count, unit = UCUM `1` (or a pinned piece-code), valueForm = point, exactness = exact.  
- MonetaryAmount (unit price): coefficient `1995`, scale `2`, currency `EUR`, catalogue `ISO4217`, edition pin `E`, valueState = exact.  
- CalculationReceipt: operation = `multiply`, roundingMode = `half_even`, roundingStage = **`line`**, result = `49.88` EUR.  
- LocalizedText: `{text:"Widget", languageTagOriginal:"en", role:label}` and `{text:"Widget-Gerät", languageTagOriginal:"de", role:label}` on product `P-1`.  
- No ERP, no FX feed, no ambient locale. A different receipt that rounds **after summation** is a different fact.

---

## 5. Five facets for each independent type

Delegate only to a contract actually opened. Dependencies on unread ISO 80000 clauses, full ISO 4217 tables and a general conversion engine are **unresolved**.

### QuantityValue — embedded

1. **Identity / class.** Value object; identity is the host’s.  
2. **Direct properties.** Lexical magnitude, kind, unit, form, point-or-difference, exactness.  
3. **Recognition / observation.** Parse decimal or rational string. Reject binary float as authoritative.  
4. **Capabilities / actions.** Compare and convert only if kinds match and pins exist. Emit receipts. Never execute a physical or financial act.  
5. **Context / evidence.** Vocab and unit-system pins; origin category; host sensitivity.

### UnitDefinitionRevision — independent when versioned

1. Class: reference-data revision.  
2. Properties: code, system, version, factor, offset, scale type, special-function flag.  
3. Recognition: steward release + digest.  
4. Capabilities: be cited. Not a licence to convert silently.  
5. Context: UCUM 2.2 / QUDT 3.5.x / SI Brochure as chosen pins — **unresolved** which one is “the” system.

### MonetaryAmount — embedded

1. Class: value object on a host economic document.  
2. Properties: sign, coefficient, scale, currencyRef, rounding intent, valueState.  
3. Recognition: exact decimal only.  
4. Capabilities: same-currency add; multiply by a QuantityValue under a receipt. Mixed-currency add is a policy action, not a field.  
5. Context: catalogue edition; host SoR named by the adopter (not “the ERP”).

### CurrencyDefinition — pinned snapshot

1. Class: catalogue entry at an edition.  
2. Properties: codes, class/status, published minor unit if stated, successor.  
3. Recognition: SIX MA lists as *evidence* of ISO 4217 designations (landing page claim).
4. Capabilities: resolve a code. Not legal-tender, capital-control or FX-convertibility oracle.  
5. Context: edition, digest, licence boundary (we did not copy lists).

### ExchangeRateObservation — independent

1. Class: observation record.  
2. Properties: pair, direction, rate, times, purpose, quality, restriction.  
3. Recognition: publisher snapshot + retrieval time.  
4. Capabilities: be cited by a CalculationReceipt. Not a payment instruction.  
5. Context: ECB page: information only, transactions strongly discouraged. Fed H.10: noon NY buying rates certified for US customs; past releases not revised — **not** the same disclaimer as ECB; do not equate.

### Instant — embedded

1. Class: temporal value.  
2. Properties: RFC 3339, time-scale id if not UTC.  
3. Recognition: offset or `Z` required.  
4. Capabilities: order on the same scale.  
5. Context: time-scale governance (UTC leap policy is deferred as an engine).

### CivilDateTime — embedded

1. Class: temporal value.  
2. Properties: local fields, tzId, calendarKey, bindingMode, disambiguationPolicy, tzdb pin.  
3. Recognition: preserve gap (no such local time) and overlap (two instants). Temporal documents `earlier | later | compatible | reject`.
4. Capabilities: resolve to Instant only with policy + pin.  
5. Context: IANA tzdb is a mirror of civil decisions, not the legal instrument.

### ExactDuration / NominalDuration — embedded

1. Class: two value types.  
2. Properties: SI seconds vs calendar parts.  
3. Recognition: kind is declared, not inferred from the word “hour”.  
4. Capabilities: exact add on ExactDuration; nominal add only under a named calendar algorithm.  
5. Context: OWL-Time distinguishes Instant / Interval / Duration and treats TimeZone as a stub — useful split, not a working-calendar engine.

### WorkingAvailability — derived, not master

1. Class: computed result.  
2. Properties: result interval or hours + full input digest.  
3. Recognition: refuse if any governing input is missing.  
4. Capabilities: answer Q12. Never authorise staffing by itself (I3).  
5. Context: employer or jurisdiction policy owner — **not** HRIS by default, **not** address.

### LocalizedText — embedded; DesignationAssertion — optional independent

1. Class: designation, not entity.  
2. Properties: text, original tag, role.  
3. Recognition: BCP 47 well-formedness always; validity only against a pinned File-Date.  
4. Capabilities: display, filter. Cannot change object identity.  
5. Context: IANA Language Subtag Registry; CLDR for *formatting only*.

---

## 6. Authority matrix

Do not assume HRIS or ERP is mandatory or authoritative anywhere.

| Fact class | Semantic owner | Authoritative system | Allowed writer | Read purpose | Effective / recorded / as-of | Conflicts | Disclosure | Retention |
|---|---|---|---|---|---|---|---|---|
| SI quantity, unit, dimension | BIPM / CGPM | SI Brochure 9th ed (2019, text updated 2026), DOI `10.59161/AUEZ1291` | We cite; we do not redefine kelvin | interpret kind/unit | brochure edition | non-SI “accepted” units ≠ SI status | CC BY 4.0 on the landing | retain edition cited |
| Unit *codes* | Chosen steward (UCUM Org, QUDT.org, UN/CEFACT) | Pinned release | Steward; adopter imports evidence | parse / compare | release tag | UCUM vs QUDT vs SI disagreements recorded, not hidden | UCUM rights reserved; QUDT CC BY 4.0 on pages opened | retain used edition |
| QuantityValue | Host object owner | Host system of record named by adopter | Host writer | display / compute | event time ≠ record time | incommensurable → refuse | host sensitivity | host policy |
| Currency codes | ISO 4217 MA (SIX, per its landing) | Pinned List One/Two/Three edition | MA allocates; we import evidence only | identify currency | edition status, not “today” | withdrawn / successor codes | do not republish paid/full tables as if MA | retain snapshot + digest |
| MonetaryAmount | Host (invoice, estimate) | Host SoR | Host finance role | price / report | declaration time | mixed CCY without policy → refuse | financial sensitivity | host + legal |
| FX observation | Publisher (e.g. ECB) or named internal source | Publisher system | Publisher authors; steward records a copy | estimate / convert **under declared purpose** | observation ≠ publication ≠ effective ≠ retrieval | two publishers → require policy; reversed pair ≠ same obs | ECB: information only, not transaction | retain observation + restriction as long as derived results exist |
| Civil time rules | Competent jurisdiction / legal instrument | Instrument first; tzdb as mirror | Jurisdiction; tzdb editors mirror | resolve civil ↔ instant | announcement vs effective instant vs tzdb release | legal change vs lagged tzdb is a tracked divergence | public | retain tzdb release used |
| Working calendar / availability | Employer or public-holiday authority | Named policy store | That authority | staffing **calculation**, not permission | dated revision | two calendars never silently equal | may be internal | host |
| Language tags | IANA Language Subtag Registry | Registry File-Date | IANA | well-formed / valid | File-Date | deprecated subtag → preferred-value as annotation | public | pin File-Date |
| Formatting locale | Product UX policy | CLDR release **if** used | UX owner | render only | CLDR version | never writes canonical magnitude | public patterns | optional |
| Designation text | Content owner | CMS / host | author / translator | display | source revision of designated object | duplicate (object, role, tag) | content may be sensitive; tag is not | host |
| CalculationReceipt | Computing system | Same | compute service | audit / replay | computation instant | rounding-context change = new receipt | may be internal | retain with inputs |

**Imported reference data is evidence, not a new right to serve it.**

---

## 7. Invariants (≥12) and negative cases (≥12)

### 7.1 Invariants

| ID | Invariant | Schema can check | Semantic code can check | Trusted host | Expert judgment |
|---|---|---|---|---|---|
| I1 | Magnitude is inseparable from unit or currency | pair presence | — | — | — |
| I2 | Unknown ≠ 0; missing ≠ 0; unavailable rate ≠ 1 | forbid numeric 0 as the only encoding of absent | valueState vs coefficient | — | — |
| I3 | Formatted / display string ≠ canonical numeric | separate fields | — | — | — |
| I4 | Successful calculation ≠ permission to pay or staff | receipts have no `execute` flag | — | policy engine | legal / operational approval |
| I5 | Same physical dimension ⇏ same quantity kind | — | kind-id equality, not dimension-only | pinned vocab authenticity | novel kinds (torque/energy, Hz/Bq, temp point/delta) |
| I6 | Temperature point ≠ temperature difference | `pointOrDifference` required on interval-scale kinds | conversion path selection | — | whether a sensor output is a point |
| I7 | Mixed-currency arithmetic requires explicit policy + rate set | refuse if currencies differ and no policyRef | rate pair/direction match | publisher authenticity | whether purpose fits the contract |
| I8 | Rate correction supersedes the observation; does not mutate a prior published result | observation immutability | link `supersedesRef` | write ACLs | materiality of a revision |
| I9 | Civil local time in a gap or overlap is preserved; instant chosen only under named policy + tzdb pin | bindingMode, policy enum | gap/overlap detection against pinned tzdb | tzdb release integrity | legal DST instrument vs mirror lag |
| I10 | Eight nominal hours in two dated calendars ⇏ equal availability | WorkingAvailability not typed as Duration | — | calendar revision authenticity | leave / holiday plurality |
| I11 | Translation / label ⇏ new entity | designation points at existing objectRef | — | — | whether two strings are the same work |
| I12 | Locale separator ⇏ stored magnitude change | numeric field ≠ display field | — | — | — |
| I13 | No unnamed rounding rule; line-round ≠ sum-round unless declared identical | roundingStage enum | replay with stored context | — | accounting presentation choice |
| I14 | Conversion requires definition pins; mismatched pin = refuse | pin fields present | pin equality | snapshot integrity | whether two editions are compatible |
| I15 | Schema version ≠ definition version ≠ object revision ≠ lifecycle state | four distinct fields | — | — | — |
| I16 | Same-version round-trip preserves lexical trailing zeros, original language tag, unresolved civil time | lexical compare | — | — | — |
| I17 | Cross-version: refuse or explicit migration; no silent field reinterpretation | version tokens | migration map | — | whether a field changed meaning |
| I18 | Address does not determine timezone or working calendar | no such default | — | — | optional *hint* vs determination |
| I19 | Imported reference data is evidence, not a serving right | — | — | licence / robots / MA terms | redistribution law |
| I20 | FX direction is part of identity; reversed pair is a different observation | base≠quote stored | refuse treating `1/r` as the same id | — | whether inversion is exact in decimal |

**Immutable correction.** Published MonetaryAmount, ExchangeRateObservation, CalculationReceipt and DesignationAssertion are not edited in place. Correction = successor + closed effective interval on the predecessor.

**Replay.** Replay uses the stored rounding context, pins and inputs. A changed context is a new receipt (I13, N10).

**Conflict.** Two publishers, two calendars, two language assertions for the same `(object, role, tag)` are conflicts, not merges.

**Reference drift.** Short code unchanged + issuer/version changed = Q16 / N1.

**Rights.** I19.

**Same-version round-trip.** I16.

**Cross-version refusal / migration.** I17.

### 7.2 Negative cases (Case D and extensions)

| ID | Case | Required behavior |
|---|---|---|
| N1 | Unchanged short unit/currency code; issuer or version changed | Treat as potential new definition; require pin |
| N2 | Reversed FX pair used as if the same rate | Distinct observation; inversion only via a receipt |
| N3 | Stale as-of quote used as current | Flag or refuse; do not silently apply |
| N4 | Ambiguous local time silently coerced to one instant | Preserve civil; require policy |
| N5 | Unknown currency assumed two decimal places | Refuse; scale must be explicit and marked unresolved |
| N6 | Incompatible quantity kinds added (e.g. entropy + heat capacity; temp point + temp delta) | Refuse |
| N7 | Self-certified calibration treated as SI-traceable | Record as self-certified; do not upgrade |
| N8 | Unknown treated as zero | Refuse |
| N9 | Duplicate designation language on same object+role | Flag conflict |
| N10 | Missing designation language defaulted to `en` | Missing is missing |
| N11 | Rounding context changed between compute and replay | New receipt or fail replay |
| N12 | Definition pin mismatched or dropped after import | Refuse conversion; lost provenance is N13 |
| N13 | Provenance stripped on import | Import is evidence with source citation or it is incomplete |
| N14 | DST-gap local time dropped | Preserve |
| N15 | 8 h in calendar A treated as 8 h availability in calendar B | Refuse equality |
| N16 | Float64 used as money or exact quantity store | Refuse as canonical |
| N17 | Ambient locale used as unit, currency, scale or calendar context | Refuse |
| N18 | Successful FX multiply treated as payment authorisation | I4 |
| N19 | Address used as timezone | I18 |
| N20 | CLDR used as currency, unit or timezone *identity* | Formatting only |

---

## 8. Exact arithmetic, FX, timezone, designation

### 8.1 Exact arithmetic and rounding

**Proposal.** Canonical store is an exact decimal lexical string **or** `(sign, integer coefficient, scale)`. Trailing zeros are significant when `exactness` or `scale` says so (`2.50` is not `2.5` under that policy).

**Observation / limit.** We opened the General Decimal Arithmetic landing only shallowly (one fetch returned insufficient content). IEEE 754-2019 clause text was **not** read. We therefore **do not** claim IEEE 754 decimal conformance. We **do** reject binary float as a canonical money or exact-quantity representation on practice-school and candidate-spec grounds (008 and 032 both insist on exact decimal lexical form; Fowler Money/Quantity practice school says the same).

**Rounding.** Mode, tie rule and stage (`line` vs `after_sum`) are explicit inputs to every CalculationReceipt. Ambient locale must not supply separator, scale or rounding. Rational conversion factors are allowed when both numerator and denominator are integers **and** a definition revision is cited; rounding happens only at the declared step.

**Bounded executable behavior that is defensible for a small independent implementation:**

1. Exact decimal multiply of quantity × unit price with declared scale and rounding mode (Case A).  
2. Same-currency add.  
3. BCP 47 *well-formedness* check (syntax).  
4. RFC 3339 parse requiring offset or `Z`.  
5. Refuse mixed-currency add, refuse unqualified local time, refuse unknown-as-zero, refuse float canonical store.

Not defensible in first publication: a general unit-conversion engine, a holiday engine, a cross-rate triangulator, uncertainty propagation, payment execution.

### 8.2 FX direction, source and date

Record **base**, **quote**, **direction as published**, **unit count**, **source**, **purpose**, **observation time**, **publication time**, **retrieval time**, **effective interval**, **quality**.  

ECB euro reference rates: quoted as foreign units per **one euro**; published about 16:00 CET on TARGET working days; *“published for information purposes only. Using the rates for transaction purposes is strongly discouraged.”*

Inverse `1/r` is a **derived** receipt, not the same observation, and is not in general an exact decimal. Cross rates are derived unless the publisher printed them. A correction is a new observation (I8). Mixed EUR/USD addition without a named policy and rate set is refused (Case B).

### 8.3 Timezone, calendar versions, DST

Pin the tzdb release (example current on the IANA pages we saw: 2026-era lettered releases; one teammate extract reported `2026d` on 2026-09-11 — treat the exact letter as **environment-specific**, not as a claim we hashed). Future political change can invalidate a previously computed instant derived from a civil time; therefore store **civil + resolved instant + tzdb pin** when resolution is performed.

DST **gap**: that local time does not exist. DST **overlap**: it exists twice. Temporal’s documented options are `compatible | earlier | later | reject`. This contour adds `preserve_unresolved` as the default when the host is not entitled to choose. Offset + local + zone may disagree after a zone-definition change; that conflict is recorded, not repaired in place.

Eight nominal working hours are a NominalDuration. Availability is a derived function of dated calendar revision, leave, location and DST. Those inputs are separately governed. An address must not silently supply them.

### 8.4 Qualified designation identity

Object identity is the host id (product, model release, party). `(languageTag, role, text revision)` is an assertion. A model-release label in two languages remains one release (Case C). Locale-specific decimal separators never change stored magnitude. Duplicate or missing designation language is a finding, not a default to `en`.

---

## 9. Source table

Verification depth key: **L** landing only; **S** selected sections via summarizer; **U** unread / unverified.

| # | Official URL | Version / date / section actually seen | Claim used | Boundary implication | A / R / U | Depth |
|---|---|---|---|---|---|---|
| 1 | `https://ver.cy/models/wm-xct-008-quantity-unit/spec.yaml` | 0.3.0-research.1; generated 2026-08-23; publishableCanonical false | Mixin Quantity/Unit; money out; kind≠dimension≠unit | Profile, do not merge with 032 | Adopt as profile | S |
| 2 | `https://ver.cy/models/wm-xct-009-time-calendar/spec.yaml` | 0.3.0-research.1; generated 2026-08-22; no brief hash | Instant/civil/duration/working-day derived | Profile shapes; defer engines | Adopt as profile | S |
| 3 | `https://ver.cy/models/wm-xct-010-location-referencing-address/spec.yaml` | 0.3.0-research.1 | Address / location fabric | Unrelated to calendar contour | Reject as calendar | S |
| 4 | `https://ver.cy/models/wm-xct-031-localization-language/spec.yaml` | 0.3.0-research.1; 2026-09-03; single-provider-waiver | Binding mixin; tag ≠ identity; CLDR not content | Profile tags; new LocalizedText | Adopt as profile | S |
| 5 | `https://ver.cy/models/wm-xct-032-currency-monetary-value/spec.yaml` | 0.3.0-research.1; 2026-09-03; publishableCanonical false | Exact decimal + catalogue pin; FX referenced | Profile amount; independent rate record | Adopt as profile | S |
| 6 | `https://www.bipm.org/en/publications/si-brochure` | 9th ed 2019, text updated 2026; DOI 10.59161/AUEZ1291; CC BY 4.0 | Official SI Brochure pointer | SI is meaning authority, not a code registry | Adopt pointer | L |
| 7 | `https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf` | 9th ed 2019 selected §§2.1, 2.3.1, 2.3.3 | Quantity = number × unit; dimension convention; t/°C = T/K − 273.15; interval same numeric in K or °C; defining constants exact | Point vs difference; do not treat °C point as ratio-convertible | Adopt selected distinctions | S (not full-brochure audit) |
| 8 | `https://www.bipm.org/documents/20126/2071204/JCGM_200_2012.pdf` | JCGM 200:2012 defs 1.1, 1.2, 1.9, 1.19, 1.30 | quantity; kind of quantity; measurement unit; quantity value; nominal property | Nominal property must not be forced into QuantityValue | Adopt those five defs | S |
| 9 | `https://ucum.org/ucum` | v2.2 dated 2024-06-17 on the page we opened | Unit *code* grammar; `{}` annotations semantically empty; Cel is a special interval-scale unit; arbitrary units incommensurable | Adopt as optional expression system; reject as kind ontology | Adopt / reject as stated | S |
| 10 | `https://www.qudt.org/pages/QUDToverviewPage.html` | overview undated on page | QuantityKind ≠ Unit ≠ Dimension | Adopt four-way split | Adopt split | L |
| 11 | `https://github.com/qudt/qudt-public-repo/releases` | v3.5.0 (2026-07), v3.5.1 (2026-08), later snapshot | Value-affecting reclassifications between 3.5.0 and 3.5.1 | Pin version if QUDT is used | Adopt pin requirement | L |
| 12 | `https://www.w3.org/TR/owl-time/` | 15 Nov 2022 CRD also visible; 2017 Rec exists — **status mixed across extracts** | Instant / Interval / Duration; TimeZone stub | Align class split; reject as tz/working-calendar engine | Adopt split; status **unverified** | L |
| 13 | `https://www.rfc-editor.org/rfc/rfc5646.html` | RFC 5646 / BCP 47, Sep 2009 | Well-formed ≠ valid; tag designates language of content, not object identity | LocalizedText language field | Adopt | S |
| 14 | `https://www.rfc-editor.org/rfc/rfc3339.html` | RFC 3339, Jul 2002 | Timestamp is an instant with stated UTC relationship; `-00:00` = offset unknown | Instant shape | Adopt | S |
| 15 | `https://data.iana.org/time-zones/tz-link.html` | tzdb theory/link page | Public-domain tz data; **not authoritative**; governments control rules; leap-second “right” vs POSIX | Pin release; do not treat tzid as law | Adopt | S |
| 16 | `https://tc39.es/proposal-temporal/docs/` and `…/timezone.html` | proposal docs (Stage 4 claimed in one teammate extract — treat implementation status as **not an ECMA-262 claim by us**) | Instant ≠ PlainDateTime ≠ ZonedDateTime ≠ Duration; gap/overlap disambiguation | Adopt type split + explicit policy; defer shipping Temporal | Adopt split | S |
| 17 | `https://cldr.unicode.org/` | landing; current numeric version not reliably visible | Locale *data* for formatting | Reject as identity oracle | Adopt as optional format source | L |
| 18 | `https://www.six-group.com/en/products-services/financial-information/market-reference-data/data-standards.html` | MA landing; Bulgaria/EUR 1 Jan 2026 change stated on page | SIX claims to be the only recognized authoritative source on ISO 4217 *code designations*; lists said free online | Adopt MA identity and pin-to-edition; do not copy lists | Adopt scope | L |
| 19 | `https://www.iso.org/iso-4217-currency-codes.html` | ISO 4217:2015 scope landing | Alpha + numeric codes; minor units; lists 1/2/3 | Scope only; full text unread | Unknown contents | L |
| 20 | `https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html` | page extract dated 18 Sep 2026 in one fetch | Information-only reference rates; 1 EUR = x foreign; ~16:00 CET | Purpose-qualify FX observations | Adopt policy example | L |
| 21 | `https://www.federalreserve.gov/releases/h10/about.htm` | about page last update 6 Feb 2023 | Noon NY buying rates; certified for US customs; past releases not revised | **Not** the same non-transactional sentence as ECB | Unknown as “non-transactional” in the ECB sense | L |
| 22 | Fowler Money / Quantity essays (`martinfowler.com`) | 2003/2004 practice essays | Amount+currency together; no floats; no mixed-currency add | Competing modelling school, not a standard | Adopt as school | L (teammate; not re-opened here as primary law) |
| 23 | ISO 80000 series | — | System of quantities | Paywalled | Reject conformance claims | U |
| 24 | IEEE 754-2019 full text | — | Decimal formats | Unread | No conformance claim | U |
| 25 | ISO 8601-1/2, ISO 20022 amount types | — | Civil date / payment amount profiles | Unread beyond candidate citations | Scope unknown at clause level | U |
| 26 | Brief SHA-256 column | supplied by assignment | File identity | Hash ≠ semantics; we did not hash | Not verified | U |

**Licensing and unread-source limits.** SI Brochure landing: CC BY 4.0. QUDT pages opened: CC BY 4.0. UCUM: rights reserved (Regenstrief / UCUM Org). ISO 4217 full lists and ISO 80000: not copied, not clause-audited. IANA tzdb: public domain per tz-link. RFC 5646 / RFC 3339: IETF document terms. No standards-conformance sentence is made for any of the above.

---

## 10. Acceptance criteria, highest-risk alternatives, publication limits, assignment

### 10.1 Acceptance criteria (both providers; Cases A–D)

A suite passes only if **silent success is impossible** on every negative in §7.2.

**A — Startup invoice.**  
An invoice line carries exact fractional quantity, unit price and currency. A CalculationReceipt declares multiplication and the rounding stage. A translated product label does not change product identity. No hidden ERP, FX feed or locale is consulted. Rounding per line and rounding after summation are distinct receipts.

**B — International matrix.**  
A monetary estimate cites an ExchangeRateObservation with base/quote, direction, observation/effective time and purpose. A later rate correction creates a new observation and leaves the published estimate unchanged. Mixed EUR/USD addition without a named policy is refused. Eight nominal hours in two dated calendars do not establish equal availability; leave, location and DST are separate inputs. A local time in a DST gap or overlap is stored as civil + policy; the system does not silently pick an instant.

**C — Hardware / AI.**  
A temperature point is not a temperature difference. Equal dimension is not kind substitutability. A unit conversion cites definition revision and rounding and emits a receipt. A model-release label in two languages is one release. A locale decimal separator never changes stored magnitude. Nonlinear units, uncertainty propagation and real financial or workforce *actions* are explicitly deferred.

**D — Historical / drift negatives.**  
N1–N20 are refused or flagged. In particular: unchanged short code with changed issuer/version; reversed FX pair; stale as-of quote; ambiguous local time; unknown currency with assumed 2 dp; incompatible kinds; self-certified calibration upgraded; unknown as zero; duplicate/missing designation language; silently changed rounding context; mismatched definition pin; lost provenance after import.

**Cross-cutting acceptance.**  
Same-version round-trip preserves lexical form. Cross-version without a map is refused. Reference validators are distinct from host policy and from actual source resolution. Unknown is not zero. An unavailable rate is not one. A formatted string is not the canonical value. A successful calculation is not permission to execute a payment or a staffing decision.

### 10.2 Highest-risk design alternatives (reject)

1. One giant value bag (`amount`, `code`, `when`, `label` as a single type).  
2. Inferring unit from currency minor units, or currency from locale.  
3. Inferring timezone or working calendar from an address.  
4. Treating CLDR or a language tag as object identity.  
5. Treating ECB or H.10 series as executable / dealable FX.  
6. Adding mixed currencies without a policy record.  
7. Equating eight hours across calendars.  
8. Binary float as canonical store.  
9. Ambient locale as implicit context.  
10. Unknown = 0; missing rate = 1.  
11. Same dimension ⇒ same kind (temperature point vs delta).  
12. Manufacturing independent lifecycles for every embedded primitive.  
13. Equating a file hash with semantic compatibility.  
14. Claiming ISO 4217 or SI *conformance* from landings and selected paragraphs.

### 10.3 Proposed publication limits

- Label any first issue `0.3.x-research`. Keep `publishableCanonical = false` until: (i) raw spec bytes are re-read without summarizer truncation, (ii) 031/032 second-provider waiver is closed or explicitly accepted as a limitation, (iii) no conformance sentence is left standing without a cited clause.  
- Do not publish ISO 4217 code tables, UCUM atom tables or CLDR XML as if Vercy were the steward.  
- Do not modify external state.  
- Preserve inherited publication holds on WM-XCT-010; do not recast it as a calendar model.  
- Record the 008/032 money-boundary disagreement instead of merging the types.

### 10.4 Step-by-step implementation / research assignment

1. Freeze the five contracts in §1.1 as TypeSpec or JSON Schema **for embedded values and the one independent rate record only**. No engine.  
2. Implement the refuse-paths for N1–N20 and the missing-context rule in §4. That is the startup deliverable.  
3. Pin, as *evidence snapshots* inside the adopting dimension and without a redistribution claim: one UCUM version (2.2 is what the UCUM page showed), one ISO 4217 list edition retrieved from the MA, one tzdb release, one IANA language-subtag File-Date.  
4. Implement Case A end-to-end: quantity × price, declared line rounding, bilingual label, no FX, no locale math.  
5. Implement Case B as **tests that fail closed**: mixed-currency add, rate correction, DST gap/overlap, two working calendars.  
6. Implement Case C as **tests plus explicit deferral records** for nonlinear units, uncertainty and workforce action.  
7. Separately research WorkingAvailability as a derived service with dated calendar revisions — do not fold it into Duration.  
8. Re-fetch the SI Brochure PDF and the ISO 4217 scope/MA pages before any sentence that looks like conformance. Read VIM 1.1–1.30 and UCUM special-unit sections at clause depth if a second research increment is funded.  
9. Keep QuantityValue and MonetaryAmount as **neighbors sharing numeric fidelity only**.  
10. Do not stand up an FX feed, tz compiler or CLDR snapshot as a prerequisite for publishing an invoice.

---

### Closing

EM-XCT-06 is a **contour**: Quantity, Money, UnitReference, CalendarReference, LocalizedText, plus reusable magnitude / range / date conventions. The safe first publication is a handful of embeddable values, a few pins, one independently identified rate observation, and a long list of things the schema will **refuse** rather than guess. That is enough for a startup invoice and for an international estimate. It is not a metrology laboratory, a bank, a workforce management product or a translation memory — and it should not pretend to be.
