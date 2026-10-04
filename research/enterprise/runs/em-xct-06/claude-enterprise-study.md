# EM-XCT-06 research memo: Quantity, Money, Units, Calendars and Localized Text

**Study date:** 21 September 2026 (UTC). Written 22 September 2026.
**Status:** Independent research and design study. This is not an audit of any implementation, not a standards-conformance claim, and not permission to publish.
**Evidence tags used below:**
- **[N]** normative text I actually opened
- **[S]** something a source or Vercy candidate asserts
- **[I]** my inference
- **[P]** my proposal
- **[U]** unverified: from memory, or a source I couldn't open

---

## 0. How I read the sources, and the limits of that reading

- **Tool:** Every source I "opened" went through a fetch tool that turns the page into markdown and has a small model answer my prompt about it. So "read" here means I read a tool summary with extracted quotes. It does **not** mean a byte-level or clause-by-clause reading. Quotes below are as the tool returned them. Any field list may be incomplete or paraphrased.
- **Hashes:** I did not check any SHA-256 value. The Vercy specs show a "Synthesis SHA256" in their metadata. That is **not** the file hash in the brief, and I don't treat a matching hash as semantic compatibility.
- **Pages that failed:**
  - `iso.org/iso-4217-currency-codes.html`: HTTP 403
  - Temporal `docs/ambiguity.html`: 404. I read `docs/zoneddatetime.html` instead.
  - `qudt.org`: connection refused
  - SI Brochure PDF: the tool couldn't parse the binary. It stored a local copy, which I did **not** open, because the brief rules out using the local filesystem.
  - The General Decimal Arithmetic page gave only a table of contents.
- **Not used:** No private files, portfolio volumes, credentials, MCP tools or local code. I ran nothing.

---

## 1. Recommendation: split the contour and publish a small first slice

### 1.1 Challenging the boundary

**[I]** EM-XCT-06 is not one model. The five research words cover three different kinds of thing:

1. **Embedded value contracts.** These have no identity of their own and live inside a host record: magnitude, Quantity, MonetaryAmount, temporal values, LocalizedText, and the pinned references UnitReference, CurrencyReference, QuantityKindReference and CalendarReference.
2. **Independently identified governed records.** These have their own authority, correction behaviour and replay needs: FX rate observations, calculation/conversion receipts, working-calendar revisions and designation assertions.
3. **External reference data.** Examples: UCUM, QUDT, the ISO 4217 lists, tzdb, CLDR and the IANA Language Subtag Registry. **[P]** Vercy should hold these as **pinned evidence snapshots** (Artifacts), never as Vercy-mastered canonical objects, and never with an implied right to redistribute them.

A single "value bag" would merge all three. That would force embedded values into fake lifecycles and hide authority where it matters (who published a rate, who approved a calendar).

### 1.2 Minimal first publication

**[P] Publish in 0.1.0-research, as research only (not executable or production):**

| # | Type | Form | Why it's needed now |
|---|---|---|---|
| 1 | `Magnitude` (exact decimal or rational, plus value state and bounds) | Shared embedded contract | Every other type needs it. It's where floats, lost trailing zeros and unknown-as-zero get in. |
| 2 | `Quantity` | Embedded; narrow **profile of WM-XCT-008** | Acceptance cases A and C |
| 3 | `MonetaryAmount` | Embedded; near-exact **profile of WM-XCT-032** | Cases A and B |
| 4 | `UnitReference`, `QuantityKindReference`, `CurrencyReference`, `CalendarReference` | Embedded pinned references | Stops code drift (case D) |
| 5 | `TemporalValue` family: `Instant`, `CivilDateTime`, `CivilDate`, `ElapsedDuration`, `NominalDuration` | Embedded; narrow **profile of WM-XCT-009** | Cases B and D (DST gap and overlap) |
| 6 | `LocalizedText` | New small shared contract. It **uses the language-tag identity from WM-XCT-031**, which itself excludes content. | Cases A and C |
| 7 | `RateObservation` | **New independently identified record** | Case B: attribution, direction, correction |
| 8 | `CalculationReceipt` (covers conversion decisions) | **New independently identified record** | Cases A, B and C: replay, no rewriting |
| 9 | `WorkingCalendarRevision` | **New independently identified record**, minimal. Organisational calendars only. | Case B: "8 hours ≠ equal availability" |
| 10 | `DesignationAssertion` | **New independently identified record**, optional | Cases A and C: a label is not a new entity |
| — | `ReferenceDataSnapshot` | Evidence Artifact, not canonical | Pins plus rights |

**[P] Explicitly deferred.** Each of these gets a named refusal behaviour rather than a fake implementation:
- executing nonlinear or logarithmic conversions (dB, pH, Np);
- uncertainty propagation (GUM-style) beyond carrying an opaque statement;
- quantity calculus for vector or tensor values;
- organisation-local unit definitions (for example "pallet" or "seat-month");
- a non-ISO asset registry (crypto, loyalty points, internal transfer-pricing units);
- jurisdictional cash rounding;
- accounting postings, payment execution, tax;
- personal leave, individual availability and any staffing decision;
- arithmetic on non-Gregorian calendars;
- leap-second arithmetic beyond pinning;
- recurrence expansion.

**[I] Unsafe assumptions the first slice must name and block:**
- JSON `number` parsed as a binary float
- currency minor unit guessed from the code
- ambient process locale or time zone
- a "latest" rate
- a UTC offset used as a zone identity
- "1 day = 24 h"
- nominal hours treated as availability
- a new label treated as a new product
- equal dimension treated as substitutable (torque vs energy, Hz vs Bq, °C point vs K difference)
- `null`, missing or unknown treated as 0
- an unavailable rate treated as 1
- a formatted string stored as the value

### 1.3 Definitions of each proposed type

| Type | Definition | Identity, correction and split | Neighbour distinction | Semantic owner | Source | Applies on its own? | Lifecycle | Chosen form |
|---|---|---|---|---|---|---|---|---|
| Magnitude | An exact number (decimal or rational), or an explicit non-exact state (bounded, censored, unknown, …) | No identity. Correct it by revising the host. | Not a Quantity (no unit). Not a formatted string. | Vercy shared-contract steward | Host or receipt | No | None | Embedded |
| Quantity | Magnitude + unit + (optional, but required for arithmetic) quantity kind + point/difference role | No identity. Equality means same kind, role and unit after canonicalisation, **and** equal magnitude. | Not an observation act (a sibling model owns that). Not money. | XCT.QTY steward (WM-XCT-008 lineage) | Host | No | None | Embedded, profile of 008 |
| MonetaryAmount | An exact decimal amount bound to a pinned CurrencyReference, with a declared scale | None. Restating a value in a successor currency creates a **new** amount and receipt; the original is kept. | Not a price, posting or payment (032 says the same) | XCT.MON steward (032 lineage) | Host | No | None | Embedded, profile of 032 |
| UnitReference | A pinned reference to a unit expression inside a versioned code system | Identity is the tuple (system, version, canonical expression). Code drift means a new tuple, not an edit. | Not the unit definition. The registry owns that. | External registry; Vercy only pins | UCUM, UN/CEFACT Rec 20, QUDT | No | None | Embedded |
| QuantityKindReference | A pinned reference to a quantity kind | Tuple (vocabulary, version, id) | Not a dimension vector (many kinds share one dimension) | External vocabulary | QUDT or ISO 80000 kinds [U] | No | None | Embedded |
| CurrencyReference | A pinned code in a catalogue edition, plus its code class and minor unit **as of that edition** | Tuple (catalogue, edition, code). A reused code in a new edition is a different tuple. | Not a jurisdiction, legal tender status or exchangeability (032 says the same) | ISO 4217 Maintenance Agency, or the owning asset registry | SIX lists | No | None | Embedded |
| TemporalValue family | Instant; civil date-time with zone intent; civil date; elapsed duration; nominal (calendar) duration | None. A resolution (local → instant) is recorded inline with its policy and tzdb pin, or in a receipt. | Instant ≠ local wall time ≠ working time | XCT.TIME steward (009 lineage) | Host | No | None | Embedded, profile of 009 |
| CalendarReference | A pinned reference to either a civil calendar system (CLDR key + version) or a WorkingCalendarRevision | Tuple (kind, id, revision) | Not an address, and not derived from one (010) | Owner of the target | Host | No | None | Embedded |
| LocalizedText | A string + canonical BCP 47 tag + base direction | None. Inside a host set, at most one entry per (tag, role). | Not a designation assertion. Not locale formatting. | Host owns the text; 031 governs the tag | Host | No | None | Embedded |
| RateObservation | One published value of a named rate series for a base/quote pair at a stated observation time, with attribution and use terms | Vercy id + natural key (publisher, series, base, quote, period, publication sequence). **Immutable.** A correction is a new record that `supersedes` the old one. A series split means new series ids. | Not a conversion. Not a transaction rate. Not a policy choice of which rate to use. | Publisher is the authority for the value. The Vercy adopter owns the record. | ECB, Fed H.10, bank, internal treasury | **Yes** | recorded → superseded or withdrawn | New record |
| CalculationReceipt | An immutable record of a deterministic computation: pinned inputs, definitions, ordered steps, rounding context, exact and rounded result, purpose | Vercy id. Never edited. A correction is a new receipt with `supersedes`. **A receipt's result never becomes the master fact of its source.** | Not an approval, posting, payment or staffing decision | The calculating component's owner | The computation itself | **Yes** | issued → superseded or revoked | New record |
| WorkingCalendarRevision | An organisation-scoped definition of working intervals over civil dates in a named zone, pinned to its holiday sources and tzdb release | Stable `calendarId` + monotonic `revision`. A rule change means a new revision, never an edit. A scope change can split a calendar into new calendarIds. | Not a person's availability. Not a civil calendar system. Not a holiday proclamation. | Organisational calendar owner | Host policy + holiday authority evidence | **Yes** | draft → approved → effective → superseded or retired | New record |
| DesignationAssertion | A claim that text T, in language L, designates object O for a purpose, under an authority | Its own id. `designatedObjectRef` is **never** minted from the text. A translation is a new assertion linked by `translationOf`. | Not the object's identity. Not plain LocalizedText with no authority. | Owner of the designated object | Terminology, product or legal naming process | **Yes** | proposed → approved → deprecated or withdrawn | New record, optional |

---

## 2. Comparison with the Vercy candidates (summary-level reading only)

All five candidates, **as read**: version 0.3.0-research.1, entry kind *mixin*, status "published", adjudication "reviewable-draft", `Publishable Canonical: false`. **[S]** I keep all of those holds. My comparisons rest on tool summaries and are provisional until the byte-level semantic comparison already under way.

| Candidate | What I read | Relation to the EM-XCT-06 proposal | Decision | Losses and disagreements |
|---|---|---|---|---|
| **WM-XCT-008 Quantity/Unit** | Purpose; scope; bundles (kind and dimension, scale type, unit identity, expression grammar, value composition, numeric representation, conversion, uncertainty and tolerance, provenance); 12 constraints; 13 questions | **Broader.** My `Quantity`, `UnitReference` and `QuantityKindReference` are a **narrower profile.** | **Profile** (reuse the field semantics for kind, unit code/system/version, `numeric-value` exactness, `value-form`, `unit-absence-reason`, `scale-type`) | (a) I drop `value-components` (vectors), uncertainty and tolerance, and nonlinear conversion execution. Those are deferred, not lost. (b) **Disagreement:** 008 puts `provenance-kind`, `validation-outcome` and `validation-timestamp` *inside* the embeddable value. I'd move provenance to the host or a CalculationReceipt; otherwise every value becomes a mini-record (the value-bag risk). (c) Placeholder names like `quantity-calculus-homogeneity-data01` and `system-of-quantities-data02` (required 1..n) look unfinished. Base-quantity lists belong to the vocabulary snapshot, not to each value. (d) I didn't see an explicit **point vs difference** role. 008 handles Celsius through `scale-type` = interval and function conversion. I add `magnitudeRole`. (e) 008 lists `ratio` as a `value-form`, which mixes form with scale type. **Unresolved.** |
| **WM-XCT-009 Time/Calendar** | Time base; zone identity; transitions; gap/overlap policy (`gapPolicy`, `overlapPolicy`, `resolvedOffset`); legal authority for decrees; calendar systems and eras; business-day conventions mentioned; pins such as "tzdb 2026c + CLDR 48.2" | **Broader** for reference-data governance. **Overlap** on temporal value shapes. **Only mentioned, no fields seen,** for working-day calendars. | **Profile** for temporal values. **New** `WorkingCalendarRevision` (overlap, pending whether 009 has fields I didn't see). **Reuse** 009's zone and leap governance by reference. | (a) 009 requires a deterministic resolution policy. I also allow **`unresolved`** as a stored state (keep the local time, choose no instant), with `reject` as the policy. I think that's compatible, but it needs confirming. (b) 009 puts labour-law entitlements out of scope. That matches my exclusion of personal availability. (c) I didn't verify the brief's missing 009 hash or the "2026c" tzdb release claim; the IANA tz-link page I opened named no release. |
| **WM-XCT-010 Location/Address** | Address record, lifecycle, bitemporal axes, representation language | **Unrelated** to calendar semantics. At most it's evidence input for choosing a zone or holiday set. | **No reuse** in EM-XCT-06. At most an **adapter** that turns an address into a *proposed* zone or holiday-set candidate needing approval. | 010 assumes Gregorian ISO 8601 dates. An address must never silently set a zone, calendar, locale or currency. |
| **WM-XCT-031 Localization/Language** | Tag identity (`loc-locale-de-canonical-tag`, registry File-Date pin), script, direction, Unicode locale id, convention binding, preference, resolution trace. **Explicitly excludes translated content.** Adjudication was single-provider-waiver. | **Overlap** (the tag and the convention pin). **Unrelated** to content and designations. | **Reuse** the tag identity for `LocalizedText.lang`. **New** `LocalizedText` carrier and `DesignationAssertion`. | 031 treats preferences as potentially linkable personal data. I keep that sensitivity. It has a weaker adjudication basis (one provider). |
| **WM-XCT-032 Currency/Monetary Value** | Catalogue binding (`catalogue-id`, `catalogue-edition`, `alpha-code`); code class, status and succession; `minor-unit-applicable`; exact decimal (`amount-sign`, `amount-coefficient`, `amount-scale`, `canonical-amount`, `trailing-zero-significance`); determinacy states; rounding sources; ECB and Fed rate conventions; payments and FX publication out of scope | **Close to exact** for MonetaryAmount and CurrencyReference. **Narrower** than what I need for rates (032 has only a `conversion-reference`). | **Reuse/profile** for the amount. **New** `RateObservation` and `CalculationReceipt`. | (a) The summarizer said `declared-scale`, `rounding-intent`, `valuation-date` and `conversion-reference` were *inferred from scope*, so their exact names are **unverified**. (b) `amount-coefficient` typed as `number`: needs an arbitrary-precision integer string. (c) Non-ISO assets are out of scope in 032. I agree to defer them, but keep a `codeClass = non-iso-asset` slot with a mandatory registry pin. |

---

## 3. Fields, relations and lifecycle

### 3.1 Four kinds of versioning (kept separate)

- **Schema version:** the Vercy contract, e.g. `em-xct-06/0.1.0-research`. It changes the shape.
- **Definition version:** the external reference release, e.g. UCUM 2.2 (2024-06-17), QUDT v3.5.1, ISO 4217 amendment number or list date, tzdb release, CLDR 48.2, LSR File-Date. It changes meaning while leaving the shape alone.
- **Object revision:** a monotonic revision of an independent record (`WorkingCalendarRevision.revision`).
- **State:** the lifecycle status of an object or revision.

**[P]** A value is replayable only if all four are recoverable.

### 3.2 Embedded contracts

**Magnitude**

| Field | Type | Card. | Asserted/computed | Notes |
|---|---|---|---|---|
| `state` | enum {exact, measured, approximate, bounded, censored, unknown, not-applicable, withheld} | 1 | asserted | **unknown/withheld/not-applicable ⇒ `value` absent.** Never 0. |
| `form` | enum {decimal, rational} | 0..1 (1 if `value`) | asserted | |
| `value` | string, decimal `^-?(0|[1-9]\d*)(\.\d+)?$` | 0..1 | asserted | Trailing zeros are significant. No exponent in canonical form. |
| `numerator` / `denominator` | integer strings; denominator > 0 | 0..1 each | asserted | Only for `form = rational` |
| `scale` | int | 0..1 | **computed** from `value` | |
| `lower` / `upper` | Magnitude (exact only) | 0..1 | asserted | For `bounded` |
| `lowerInclusive` / `upperInclusive` | bool | 0..1 | asserted | |
| `comparator` | enum {<, ≤, ≥, >} | 0..1 | asserted | Only for `censored` |
| `significantDigits` | int | 0..1 | asserted | Measurement meaning, kept separate from `scale` |

Sensitivity is inherited from the host.

**Quantity**

| Field | Type | Card. | Notes |
|---|---|---|---|
| `magnitude` | Magnitude | 1 | |
| `unit` | UnitReference | 0..1 | Absent only if `unitAbsence` is set |
| `unitAbsence` | enum {unit-one, unknown, not-applicable} | 0..1 | Adopted from 008's `unit-absence-reason` |
| `kind` | QuantityKindReference | 0..1 | **Required before add, subtract, compare or convert** |
| `magnitudeRole` | enum {point, difference} | 0..1 | **Required** when the unit or kind is on an interval scale (°C, °F, dB-type) |
| `derivedBy` | ref → CalculationReceipt | 0..1 | Provenance by reference, not inline |

**UnitReference:** `system` (IRI, 1), `systemVersion` (string, 1), `expression` (as received, 1), `canonicalExpression` (computed, 0..1), `parserConformance` {full, limited} (0..1; required if `canonicalExpression` is present).

**QuantityKindReference:** `vocabulary` (IRI, 1), `vocabularyVersion` (1), `kindId` (1).

**CurrencyReference:** `catalogue` (IRI, 1), `catalogueEdition` (date or amendment id, 1), `code` (1), `numericCode` (0..1), `codeClass` {currency, fund, precious-metal, testing, no-currency, non-iso-asset} (1), `minorUnitAtEdition` (int, or `n/a`, or `unknown`; 1; **asserted from the snapshot, never defaulted**), `evidence` (ref → ReferenceDataSnapshot, 0..1).

**MonetaryAmount:** `amount` (Magnitude with `form = decimal`, 1), `currency` (CurrencyReference, 1), `declaredScale` (int, 1: the scale the host asserts; **not** derived from the currency), `derivedBy` (0..1). Sensitivity: host-defined. Compensation and deal amounts are often confidential.

**Temporal values**

| Type | Required fields | Notes |
|---|---|---|
| `Instant` | `value` (RFC 3339 with `Z`/offset; RFC 9557 annotation allowed), `precision`, `timeScale` (default UTC, **stated**) | `-00:00` / `Z` semantics as in RFC 9557 |
| `CivilDateTime` | `local` (date+time, no offset), `calendar` (CalendarReference, default iso8601 **stated**), `zoneId` (0..1), `zoneDataRelease` (1 if zoneId), `resolution` {unresolved, unique, gap, overlap}, `policy` {reject, earlier, later, compatible, defer} (0..1), `resolvedOffset` (0..1), `resolvedAt` (0..1) | Never collapse a gap or overlap silently |
| `CivilDate` | `date`, `calendar` | |
| `ElapsedDuration` | Quantity with kind = time and an SI second-based unit | Exact seconds |
| `NominalDuration` | ISO 8601 components (Y M W D h m s kept separate), `anchorRequired: true` | Not convertible to seconds without an anchor, zone and calendar |
| `WorkingTime` | Quantity (kind = nominal working time, unit h) + `calendar` → WorkingCalendarRevision (1) | Not elapsed time and not availability |

**LocalizedText:** `value` (string, 1), `lang` (031 canonical tag, 1), `receivedLang` (0..1), `dir` {ltr, rtl, auto} (0..1), `registryFileDate` (0..1). In a host set, the pair (`lang`, `role`) is unique.

### 3.3 Independent records

**RateObservation** (immutable)

| Field | Type | Card. | A/C | Sensitivity |
|---|---|---|---|---|
| `id` | ULID | 1 | minted | public-internal |
| `publisher` | ref (party/org) | 1 | asserted | |
| `seriesKey` | string (e.g. SDMX key) | 1 | asserted | |
| `rateType` | enum {reference, spot, closing, average, contractual, internal-budget} | 1 | asserted | |
| `base`, `quote` | CurrencyReference | 1 each | asserted | |
| `rate` | Magnitude (decimal) | 1 | asserted | Canonical meaning: **1 base = rate × quote** |
| `receivedValue`, `receivedConvention` | string, enum {quote-per-base, base-per-quote} | 1 each | asserted | Kept verbatim |
| `unitMultiplier` | int (e.g. 100) | 1 (default must be explicit 1) | asserted | |
| `observationPeriod` | CivilDate or Instant + zone | 1 | asserted | |
| `publishedAt`, `retrievedAt`, `recordedAt` | Instant | 1, 1, 1 | asserted, host, host | |
| `usePolicy` | text + code {information-only, transactional, internal} | 1 | asserted from publisher | |
| `rightsRef` | ref | 1 | host | Licence or terms; may restrict redistribution |
| `status` | enum {recorded, superseded, withdrawn} | 1 | lifecycle | |
| `supersedes` | ref → RateObservation | 0..1 | asserted | |
| `evidence` | ref → ReferenceDataSnapshot | 1 | host | |

**CalculationReceipt** (immutable)

| Field | Type | Card. | Notes |
|---|---|---|---|
| `id` | ULID | 1 | |
| `kind` | enum {multiply, sum, unit-convert, fx-convert, round, availability-evaluate} | 1 | |
| `inputs[]` | {role, value snapshot, sourceRef, sourceRevision} | 1..n | Values are **copied** so replay doesn't depend on mutable sources |
| `pins` | {unitSystemVersion, kindVocabularyVersion, catalogueEdition, rateObservationIds[], tzdbRelease, calendarRevisionIds[]} | 1 | Only the pins that apply are required |
| `factors[]` | {numerator, denominator, source definition ref} | 0..n | Exact rational |
| `steps[]` | ordered operation list | 1..n | Declares multiply-then-round versus round-then-sum |
| `rounding` | {mode, scaleOrIncrement, applyAt ∈ {per-line, per-document, per-step, none}, intermediatePrecision} | 1 (an explicit `none` is allowed) | Never ambient |
| `exactResult` | Magnitude (rational allowed) | 1 | |
| `result` | Quantity, MonetaryAmount or WorkingTime | 1 | |
| `residue` | Magnitude | 0..1 | exact − rounded |
| `purpose` | enum {estimate, quote-draft, reporting, illustration} | 1 | |
| `authorityNote` | const "computational only; no execution authority" | 1 | |
| `engine` | {name, version} | 1 | |
| `computedAt`, `requestedBy` | Instant, actor ref | 1, 1 | `requestedBy` may be personal data |
| `status`, `supersedes` | enum {issued, superseded, revoked}, ref | 1, 0..1 | |

**WorkingCalendarRevision:** `calendarId` (1), `revision` (int, 1), `ownerOrgUnit` (1), `scope` (site/team/role pool; **no persons**; 1), `zoneId` + `tzdbRelease` (1 each), `weeklyPattern` (per weekday: a list of local [start, end) intervals, 0..n), `holidaySources[]` (authority, edition, evidence; 0..n), `exceptions[]` (date → intervals; 0..n), `effectiveFrom` / `effectiveTo` (CivilDate), `status`, `approvedBy` (role ref), `approvedAt`, `evidence[]`.

**DesignationAssertion:** `id`, `designatedObjectRef` {model, objectId} (1), `text` (LocalizedText, 1), `designationType` {preferred, alternate, abbreviation, legal, marketing, deprecated} (1), `audienceScope` (0..1), `authority` (1), `translationOf` (0..1), `validFrom` / `validTo`, `status`, `evidence`. Unique on (object, lang, type, audienceScope) among `approved` assertions.

### 3.4 Lifecycle transitions (actor / guard / evidence)

| Record | Transition | Actor | Guard | Evidence |
|---|---|---|---|---|
| RateObservation | ∅ → recorded | ingestion adapter (host service identity) | pins resolve; rights allow storing; direction normalized, and the received form is kept | snapshot digest |
| | recorded → superseded | adapter | a newer observation with the same natural key carries `supersedes` | publisher correction notice |
| | recorded → withdrawn | data steward | publisher withdrawal, or a rights revocation | notice or legal ref |
| CalculationReceipt | ∅ → issued | calculation service | every required pin present; no float input; rounding declared | inputs + pins |
| | issued → superseded | calculation service on request | a new receipt exists; the old one is kept | reason code (rate-correction, input-correction) |
| | issued → revoked | steward | a defect was proven in the engine or inputs | defect report |
| WorkingCalendarRevision | draft → approved | calendar owner role | holiday sources pinned; tzdb pinned; no overlapping intervals | approval record |
| | approved → effective | trusted host at `effectiveFrom` | no other effective revision for the same `calendarId` and dates | clock + pins |
| | effective → superseded / retired | owner | a successor revision is approved, or the scope ends | |
| DesignationAssertion | proposed → approved | object owner or terminology authority | object exists; (lang, type, scope) unique | review record |
| | approved → deprecated / withdrawn | same | replacement named, or error shown | |

---

## 4. Question routes (19)

The bundles are: **QTY** (quantity and unit), **MON** (money and FX), **TIME** (temporal and calendar), **LANG** (text and designation), **CALC** (receipts). Where a route below says "flag", the output is always a *proposed* Action. No route executes a payment, posting or staffing change.

| # | Question | Bundle / layer | Expected facts and artifacts | Permitted proposed action | If context is missing |
|---|---|---|---|---|---|
| 1 | Is this number exact, bounded, censored or unknown? | QTY / magnitude | `Magnitude.state` | Mark unknown values that are stored as 0 | Return `unknown`, never 0 |
| 2 | Which quantity kind and unit (with pins)? | QTY / reference | UnitReference, QuantityKindReference, snapshot | Propose adding pins | Refuse arithmetic; flag "unpinned" |
| 3 | Is this a point or a difference? | QTY / scale | `magnitudeRole` | Propose setting the role | Refuse offset conversion |
| 4 | Can A and B be added or compared? | QTY / commensurability | kind match + role + dimension | Propose a conversion receipt | Refuse. Equal dimension alone isn't enough. |
| 5 | Convert X to unit U exactly? | CALC / unit-convert | factor as a rational + definition pin | Issue a receipt | Refuse if no factor pin or if the unit is nonlinear |
| 6 | What currency and catalogue edition? | MON / reference | CurrencyReference + snapshot | Propose a pin | Mark currency unresolved; minor unit `unknown` |
| 7 | What scale does this amount declare? | MON / amount | `declaredScale` | Flag a rescale | Refuse to infer from the code |
| 8 | Which rate observation, in which direction, as of when? | MON / rate | RateObservation | Propose ingesting evidence | Refuse the conversion. Rate ≠ 1. |
| 9 | Is the rate still valid for this purpose and date? | MON / rate policy | `usePolicy`, observation date vs valuation date, host staleness policy | Flag stale or misused | Refuse "latest" as implicit |
| 10 | Can EUR and USD be summed here? | MON / aggregation | host policy id + receipts | Propose a conversion policy | Return a per-currency vector |
| 11 | Was a published result affected by a rate correction? | CALC / lineage | receipts + `supersedes` chain | Propose a superseding receipt; the old one stays | Report "unknown impact" |
| 12 | Is this local time unique, a gap or an overlap under tzdb release R? | TIME / resolution | CivilDateTime + tzdb pin | Propose a resolution policy | Keep it `unresolved` |
| 13 | Elapsed or nominal duration? | TIME / duration | the type | Flag misuse | Refuse to convert nominal to seconds |
| 14 | How many working hours does calendar C rev N give on date D? | TIME / working calendar | WorkingCalendarRevision + receipt | Issue an *evaluation* receipt | Refuse. Don't default to 8 h. |
| 15 | Does equal nominal time mean equal availability? | TIME / availability | two receipts + an explicit "personal inputs out of scope" note | Flag an unsupported claim | Always answer "not established" |
| 16 | Which language is this text in, and is the tag valid for File-Date F? | LANG / tag | `lang` + 031 registry pin | Propose a canonical tag | Mark `und`; never guess from the script |
| 17 | Is this label a new object or a designation of an existing one? | LANG / designation | DesignationAssertion + object ref | Propose linking | Refuse to mint an object |
| 18 | Are two designations duplicates, or missing a language? | LANG / designation | uniqueness check | Propose deprecating one | Report the gap |
| 19 | Can this receipt be replayed exactly? | CALC / replay | pins + engine version + inputs | Flag drift | Report "not replayable" and list the missing pins |

**Minimal startup example (route 5, then 8, then 11).** A two-person startup quotes 12.5 GPU-hours, priced in EUR, to a US client. No ERP. It keeps a single YAML `CalculationReceipt` pinned to UCUM 2.2 and one ECB RateObservation copied into evidence with `usePolicy = information-only`. Its `purpose` is `estimate`. When the ECB corrects the rate (rare), the startup issues receipt #2 with `supersedes: #1`. The invoice it already sent keeps pointing at #1.

---

## 5. The five facets for each independent type

| Facet | RateObservation | CalculationReceipt | WorkingCalendarRevision | DesignationAssertion |
|---|---|---|---|---|
| **Identity/class** | ULID + natural key (publisher, series, base, quote, period, sequence) | ULID. Content hash of inputs+pins+steps as a replay key. | (`calendarId`, `revision`) | ULID. Never keyed by the text. |
| **Direct properties** | §3.3 | §3.3 | §3.3 | §3.3 |
| **Recognition/observation** | Publisher file or API. Kept verbatim, normalized to canonical direction, with a digest. | Emitted by an engine run and recognized by `engine` + `computedAt` | Recognized from an approved policy document | Recognized from a naming or terminology decision |
| **Capabilities/actions** | Can be cited by receipts. Can't be edited. Can't authorize a transaction. | Replay, compare, supersede. **No execution authority.** | Evaluate nominal working intervals for a date (by receipt). No personal availability. | Serve labels for display. Can't merge or split objects. |
| **Context/evidence** | ReferenceDataSnapshot, rights, use policy | Pins to every definition release; rate ids; calendar revisions | Holiday sources (authority + edition), tzdb pin, approval | Review record; `translationOf` |
| **Unresolved dependencies** | Party/org model for `publisher` (**unresolved**; no exact contract known) | Actor model for `requestedBy` (**unresolved**) | Org-unit model (**unresolved**); holiday governance **overlaps 009** (**unresolved** until 009 is read fully) | Target-object models (host-specific); TBX-style terminology (**unresolved**) |

For the embedded contracts, the facets fold into the host: identity is the host's, and observation and evidence arrive through `derivedBy` or snapshot references.

---

## 6. Authority matrix

| Fact | Semantic owner | Authoritative system | Allowed writer / read purpose | Effective / recorded / as-of | Conflict rule | Disclosure | Retention |
|---|---|---|---|---|---|---|---|
| Unit definitions and factors | BIPM (SI), UCUM or QUDT maintainers | Their releases; Vercy holds pinned snapshots | Ingestion adapter / any computation | Release date / `retrievedAt` / pin | The pin wins. A mismatch between registries is recorded, not resolved. | Per licence (SI Brochure CC BY 4.0 per BIPM page; others **not verified**) | Keep while any receipt cites it |
| Currency codes and minor units | ISO 4217 Maintenance Agency (SIX) | SIX lists / amendments | Adapter / reference | Amendment effective date / retrieval / edition | Edition pin wins | SIX terms **not read**; don't redistribute by default | Same as above |
| Rate values | Publisher (ECB, Fed, bank, treasury) | Publisher | Adapter / estimate and reporting only unless `usePolicy` allows more | Observation period / `recordedAt` / as-of | Newer publisher correction supersedes; old record kept | ECB: "information purposes only" [N]. Redistribution rights **not verified**. | Per financial-record policy (host) |
| Which rate policy applies | Host (finance/treasury, or the founder in a startup) | Host policy register — **not** Vercy, **not necessarily** ERP | Policy owner / calculation | Policy effective date | Policy version pinned in the receipt | Internal | Host |
| Calculation results | Computing component | Receipt store | Engine / audit, replay, display | `computedAt` | Never overwritten; superseded | Inherits the most sensitive input | ≥ the retention of what cites it |
| Civil time rules | Governments [N tz-link] | Legal instruments; tzdb mirrors them | Adapter / resolution | Law's effective date / tzdb release | Legal instrument over tzdb over local cache | tzdb public domain [U] | Keep releases that are cited |
| Working calendar | Organisation's calendar owner (HRIS is **one possible** host, not a required one) | Host-approved revision | Owner / capacity **estimation** only | `effectiveFrom` / `approvedAt` | A newer approved revision governs later dates only | Internal | Host |
| Personal leave or location | Individual + employer (a separate sensitive model) | **Out of scope** | — | — | — | Personal data | — |
| Language tags | IETF/IANA (LSR) | LSR File-Date pin | 031 / all | File-Date | Pin wins | Public | — |
| Designations | Owner of the designated object | Host naming process | Owner / display, search | `validFrom` | Approved over proposed; per-scope uniqueness | Pre-release model names may be confidential | Host |
| Locale formatting data | Unicode CLDR | CLDR release (48.2 current, 49 alpha, per the CLDR page) [N] | Renderer / display only | Release | Never the canonical value | Unicode terms [U] | — |

---

## 7. Invariants and negative cases

Check levels: **Sch** = schema, **Sem** = semantic code, **Host** = trusted host, **Exp** = expert judgment.

### 7.1 Invariants (16)

| # | Invariant | Check |
|---|---|---|
| I1 | No magnitude is ever a binary float. Decimal and rational values are lexical strings. | Sch (pattern) + Sem (reject JSON number) |
| I2 | `state ∈ {unknown, withheld, n/a}` ⇒ `value` absent. Absence is never 0. | Sch |
| I3 | Amount, currency and `declaredScale` always travel together | Sch |
| I4 | `minorUnitAtEdition` is asserted from a pinned snapshot, or `unknown`. It is never defaulted to 2. | Sch + Sem |
| I5 | Add, subtract and compare need equal `kind` (or a declared-compatible kind in the pinned vocabulary) **and** equal role, not just equal dimension | Sem |
| I6 | point + point is refused; point − point = difference; point + difference = point | Sem |
| I7 | Every conversion cites exact rational factors and the definition pin, in a receipt | Sch (fields) + Sem |
| I8 | A RateObservation stores the canonical direction **and** the verbatim received form and convention | Sch |
| I9 | Receipts and observations are immutable. A correction is a new record with `supersedes`. | Host (write-once storage) |
| I10 | Replaying a receipt with the same engine version and pins reproduces `exactResult` and `result` byte for byte | Sem + Host |
| I11 | A CivilDateTime with `resolution ∈ {gap, overlap}` and no policy has no `resolvedOffset` | Sch |
| I12 | Every zone-dependent value pins `zoneDataRelease` | Sch |
| I13 | WorkingTime is never summed with ElapsedDuration, or with WorkingTime from another calendar, without an evaluation receipt | Sem |
| I14 | A DesignationAssertion never creates or changes `designatedObjectRef` identity | Sch + Host |
| I15 | The formatted display string is never parsed back into a canonical value without explicit locale **and** a parse receipt | Sem |
| I16 | Same-version roundtrip (serialize → deserialize) preserves every lexical magnitude including trailing zeros. A cross-version read either migrates through a declared mapping or refuses. | Sem + Host |

### 7.2 Negative cases (16)

| # | Case | Expected outcome | Check |
|---|---|---|---|
| N1 | The same code `XYZ` appears in edition E2, but its issuer or meaning changed from E1 | Different CurrencyReference tuples; not equal; flag | Sem |
| N2 | A UCUM code resolved under a different system version from its pin (mismatched definition pin) | Refuse the conversion | Sem |
| N3 | A USD/EUR value ingested with the direction reversed (1.1490 read as USD per EUR when it was EUR→USD) | `receivedConvention` mismatch with the publisher profile; quarantine | Sem + Exp |
| N4 | Rate observation date is 40 days before the valuation date under a 5-day host policy | Stale; refuse, or require an override receipt | Host |
| N5 | 2026-03-29T02:30 Europe/Berlin [I, per the EU last-Sunday rule; verify against the pinned tzdb] | Kept as `gap` / `unresolved`; no instant | Sem |
| N6 | 2026-11-01T01:30 America/New_York (overlap) | Kept as `overlap`; both candidate instants listed; none chosen without a policy | Sem |
| N7 | Currency `unknown` with an assumed 2 decimal places | Refuse: `minorUnitAtEdition = unknown` | Sch |
| N8 | Adding torque (N·m) to energy (J) | Refuse: kind mismatch despite equal dimension | Sem |
| N9 | 20 °C point + 20 °C point | Refuse | Sem |
| N10 | A calibration certificate issued by the device vendor about its own device, cited as traceability | Accepted only as a *claim*; traceability not established | Exp |
| N11 | Missing quantity stored as `"0"` with `state = exact` after import | Can't be detected from the schema alone. Import lineage must show the source was null. Flag. | Host + Exp |
| N12 | Two approved `de` designations of the same type and scope for one release, and no `fr` where required | Uniqueness violation; missing-language finding | Sem |
| N13 | Rounding mode quietly changed from half-even to half-up between engine versions | Replay mismatch, found by I10 | Sem + Host |
| N14 | Import drops `retrievedAt`, `rightsRef` or `evidence` from a RateObservation | Reject the import (I8 and the rights rule) | Sch |
| N15 | A rate correction edits receipt #1's result in place | Refused by write-once storage | Host |
| N16 | A 0.3.0-shaped Quantity read by a 0.1-contract reader that doesn't know `magnitudeRole` | Refuse or migrate explicitly; never default the role to `point` | Sem |
| N17 | "12,5" parsed with ambient locale `en-US` → 125 | Refuse: no ambient locale (I15) | Sem |
| N18 | Replaying against a newer tzdb that changed a future rule | Report a difference; the original receipt stays valid for its pins | Sem |

---

## 8. Arithmetic, rounding, FX, time and designation behaviour

### 8.1 Exact arithmetic and rounding

- **[N]** The Python `decimal` docs state that it follows the General Decimal Arithmetic Specification. They show trailing-zero significance (`1.30 + 1.20 = 2.50`), eight rounding modes (default `ROUND_HALF_EVEN`), a default context precision of 28, the `Inexact` and `Rounded` signals, and that `Decimal(3.14)` from a float gives the exact *binary* value `3.1400000000000001243…`.
- **[P] Takeaways:**
  1. Precision and rounding context must be **declared per receipt**, never taken from a process-wide default.
  2. Raise an error on float input (the equivalent of the `FloatOperation` trap).
  3. Record `Inexact` in the receipt.
- **[P] Bounded executable behaviour worth building:** exact multiply, add and subtract on decimals and rationals; one `quantize` step with an explicit mode and increment; and a per-line vs per-document switch. That's about 200 lines in any language with a big-integer type, and it's the only engine I'd build in the first slice.

**Worked example (acceptance case A)** [P, arithmetic mine]. Three lines, each 1.5 h × 0.33 EUR/h:
- Exact per line: 0.495. Exact sum: 1.485.
- Round per line to 0.01 (either half-up or half-even) → 0.50 each → **1.50**
- Sum first, then round half-up → **1.49**
- Sum first, then round half-even → **1.48**

These are three legitimate results. The receipt's `rounding.applyAt` and `mode` fields decide which one applies. A validator that doesn't know the declared policy can't pick one.

### 8.2 Units

- **Factors:** Rational where the definition is exact. For example, inch = 0.0254 m exactly [U, NIST/1959 definition from memory]. Record it as 254/10000 with the definition source.
- **Temperature:** Temperature is affine. [N UCUM §§21–23]: special units are defined as triples (u, f, f⁻¹), e.g. "f_C(x) = x − 273.15", and "cannot participate in algebraic operations". So:
  - a 20 °C **point** → 293.15 K;
  - a 20 °C **difference** → 20 K;
  - °F point = °C × 9/5 + 32; °F difference = °C × 9/5.
- **Refused in the first slice:** logarithmic units and UCUM arbitrary units. [N UCUM §25.1]: "not comparable with any other arbitrary unit".
- **Annotations:** [N UCUM §6.2] curly-brace annotations are "meaningless by definition". So `kg{total}` and `kg` are the same unit. Don't use annotations to smuggle quantity-kind distinctions; use `kind`.
- **Declare conformance:** [N UCUM §2.2] limited-conformance parsers "may not detect equivalence". Record `parserConformance`.
- **Percent and ratios:** Keep `unit-one` or `%` with an explicit `kind` (e.g. mass fraction vs yield ratio). [U] The SI Brochure's text on dimension-one quantities was **not read** because the PDF couldn't be parsed.
- **Vocabulary drift:** [N QUDT releases] v3.5.0 reclassified BIT/BYTE/OCTET as counting/storage units; v3.4.0 changed how commensurability is derived. Concrete evidence that vocabulary pins matter.

### 8.3 FX direction, source and date

- **[N ECB page]**
  - rates are quoted against EUR as the base currency;
  - they're "published for information purposes only. Using the rates for transaction purposes is strongly discouraged";
  - they're updated around 16:00 CET after a 14:10 CET concertation;
  - EUR/RUB has been suspended since 1 March 2022;
  - USD was shown as 1.1490 on 21 September 2026.
- **[N Fed H.10, dated 21 Sept 2026]** "currency units per U.S. dollar except as noted by an asterisk". The fetch reported AUD, NZD and GBP as asterisked. I did **not** confirm EUR's convention on that fetch [U].
- **[P]** Store the canonical form "1 base = r quote" plus the verbatim received form. **Never** store a computed inverse as an observation; an inverse is a receipt step.

**Case B** [P, arithmetic mine]:

```
receipt:
  inputs:   USD 1000.00 (from estimate E)
  rate:     RateObservation{ECB, EUR→USD, 2026-09-21, r = 1.1490, usePolicy: information-only}
  steps:    divide 1000.00 by 1.1490
  exact:    1000/1.149 = 870.32201914…
  rounding: half-even @0.01 → EUR 870.32
  purpose:  estimate
```

If the publisher corrects r, a new RateObservation supersedes the old one. Receipt #2 cites it with `supersedes: #1`. The published estimate that cites #1 is unchanged.

**Mixed EUR and USD:** Without a pinned conversion policy, the sum is a per-currency vector `{EUR: x, USD: y}`, not a scalar.

### 8.4 Time zones, calendars and DST

- **[N Temporal docs]** The default `disambiguation` is `'compatible'`, which acts like 'earlier' for backward transitions and 'later' for forward transitions. `offset` defaults to `'reject'` in `from()`.
  - **[P]** Vercy should **not** adopt `compatible` as an implicit default. The resolution policy is a stored field. Absent a policy, the value stays `unresolved`.
  - **[P]** When a stored `resolvedOffset` conflicts with a newer tzdb, report the conflict (the spirit of `reject`). Don't silently re-resolve.
- **[N RFC 9557]** `Z` now means UTC is known but the local offset is unknown. The `!` critical flag means the receiver must process the suffix or reject the timestamp.
- **[N tz theory]** "The `tz` database predicts future timestamps, and current predictions will be incorrect after future governments change the rules." Pre-1970 data is thin.
  - **[P]** Store *future* civil appointments as a CivilDateTime + zone, and resolve late with a pinned release. Store *past* events as an Instant.

**Eight hours (case B)** [I, dates computed by me; holidays per the host's pinned sources]:
- Calendar A: Berlin site, rev 3.
- Calendar B: New York site, rev 7.
- On 2026-11-26, calendar B has a US Thanksgiving holiday exception (0 h) and calendar A has 8 h.
- A 22:00–06:00 local shift in New York starting 2026-10-31 crosses the overlap and lasts 9 elapsed hours for 8 nominal.
- So equal nominal WorkingTime doesn't mean equal elapsed time or equal availability. Leave and personal location are separately governed and out of scope.

### 8.5 Designation identity

- **[N RFC 5646]**
  - §2.1.1: tags are case-insensitive and case "MUST NOT be taken to carry meaning";
  - §2.2.9: well-formed ≠ valid (valid depends on the registry);
  - §3.4: `Preferred-Value` can change.
- **[P]** So canonical-tag equality is pinned to an LSR File-Date.
- **[P]** A German and an English label of one model release are two DesignationAssertions (or two LocalizedText entries) pointing to **one** release id.
- **[N CLDR page]** CLDR "is focused on languages and their regional variations". It's formatting data, not an identity oracle. A decimal comma produced by CLDR-based formatting never touches the stored `"12.5"`.

---

## 9. Source table

"Depth" means: **T** = read through the tool summary, with quoted passages; **H** = landing or metadata page only; **F** = fetch failed; **M** = memory only, unverified.

| Source (official URL) | Version / date / section | Claim used | Boundary implication | Decision | Depth |
|---|---|---|---|---|---|
| https://ver.cy/models/wm-xct-008-quantity-unit/spec.yaml | 0.3.0-research.1, generated 2026-08-23 | Fields and constraints in §2 | Quantity profile | Adopt as profile, with disagreements | T (no hash check) |
| https://ver.cy/models/wm-xct-009-time-calendar/spec.yaml | 0.3.0-research.1, generated 2026-08-22 | Gap/overlap policy, tzdb pins | Temporal profile | Adopt as profile; working calendar is new | T |
| https://ver.cy/models/wm-xct-010-location-referencing-address/spec.yaml | 0.3.0-research.1, generated 2026-08-23 | Address ≠ zone | Unrelated | Reject as calendar source | T |
| https://ver.cy/models/wm-xct-031-localization-language/spec.yaml | 0.3.0-research.1, generated 2026-09-03, single-provider waiver | Tag identity; content excluded | LocalizedText uses its tag | Adopt part | T |
| https://ver.cy/models/wm-xct-032-currency-monetary-value/spec.yaml | 0.3.0-research.1, generated 2026-09-03 | Amount and catalogue binding | Money profile | Adopt; some field names unverified | T |
| https://ucum.org/ucum | v2.2, 2024-06-17; §§2, 4, 6, 21–25, 30.4 | Conformance levels, annotations, special and arbitrary units | Temperature, refusal rules | Adopt | T |
| https://www.bipm.org/en/publications/si-brochure | 9th ed. (2019), "updates applied in 2026"; CC BY 4.0 | Current edition, licence | Pin the edition | Adopt as pin | H. PDF: F |
| https://github.com/qudt/qudt-public-repo/releases | v3.5.0 (2026-07-28), v3.5.1 (2026-08-29) | BIT/BYTE change; commensurability change | Vocabulary drift | Adopt as evidence | T (licence not seen) |
| https://www.qudt.org/ | — | — | — | Unknown | F |
| https://www.w3.org/TR/owl-time/ | CR Draft, 2022-11-15; §§4.1.x | Instant/Interval/TRS; time zone is a "stub" | TRS must be explicit | Adopt concepts; not a zone authority | T |
| https://www.rfc-editor.org/rfc/rfc9557.html | April 2024, Standards Track | Z semantics, `!` critical flag, `u-ca` | Instant serialization | Adopt | T |
| https://data.iana.org/time-zones/tz-link.html and https://data.iana.org/time-zones/theory.html | Undated pages | Governments set rules; abbreviations ambiguous; future predictions may fail | Legal authority ≠ tzdb | Adopt | T (release not named) |
| https://tc39.es/proposal-temporal/docs/zoneddatetime.html | Undated | `disambiguation` / `offset` defaults | No implicit `compatible` | Adopt the distinctions; reject the default as implicit | T. The ambiguity doc: F |
| https://www.rfc-editor.org/rfc/rfc5646.html | BCP 47; §§1, 2.1.1, 2.2.9, 3.4 | Case, validity, stability | Tag pinned to File-Date | Adopt | T |
| https://cldr.unicode.org/index | CLDR 48 (2025-10-29), 48.2 (2026-03-17), 49 alpha | Scope is locales | Formatting only | Adopt, limited | T (licence not confirmed) |
| https://www.six-group.com/en/products-services/financial-information/market-reference-data/data-standards.html | Undated; Bulgaria euro amendment effective 2026-01-01 mentioned | SIX is the Maintenance Agency; Lists 1–3; minor units | Catalogue edition pin | Adopt; list contents **not copied** | T (terms not read) |
| https://www.iso.org/iso-4217-currency-codes.html | — | — | — | Unknown | F (403) |
| https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html | Rates for 2026-09-21 | Information-only, EUR base, timing, RUB suspension | RateObservation `usePolicy` | Adopt | T |
| https://www.federalreserve.gov/releases/h10/current/default.htm | 2026-09-21 | Currency units per USD except asterisked | Direction varies by publisher | Adopt | T (EUR convention unconfirmed) |
| https://docs.python.org/3/library/decimal.html | Python 3 docs | Rounding modes, context, signals, float trap | Receipt rounding context | Adopt as practice evidence | T |
| https://speleotrove.com/decimal/decarith.html | v1.70, 2009-04-07 | Title and version only | — | Unknown | H |
| ISO 80000-1, JCGM 200 (VIM), JCGM 100 (GUM), IEEE 754-2019, ISO 4217 full text, EC Reg. 1103/97, NIST inch definition | — | Cited only through 008/032, or from memory | — | Unknown | M: paid or not opened. **No conformance claim.** |

**Licensing limits:** I copied no proprietary tables. Before any snapshot is redistributed, someone needs to read the redistribution terms for SIX, ECB, UCUM, QUDT and CLDR. Until then, every `ReferenceDataSnapshot.rightsRef` should default to "internal evidence only".

---

## 10. Acceptance criteria, risks, publication limits and next steps

### 10.1 Acceptance criteria

1. Case A reproduces the 1.50 / 1.49 / 1.48 split from three receipts that differ only in `rounding`. The product id is unchanged when a `de` designation is added.
2. Case B:
   - the receipt cites a RateObservation with base, quote, observation date, publisher and `usePolicy`;
   - a correction creates a new observation and receipt, and receipt #1 is byte-identical afterwards;
   - EUR+USD without a policy returns a vector;
   - Berlin and New York calendar evaluations for 2026-11-26 differ;
   - the gap and overlap examples stay `unresolved`.
3. Case C: °C point + point is refused; the difference conversion is exact; torque + energy is refused; every conversion receipt pins its definition release and rounding; the two-language release has one id; `"12,5"` is never parsed without explicit locale; log units and uncertainty propagation return an explicit `deferred` refusal.
4. Case D: all of N1–N18 produce their stated outcome, and each result is tagged Sch, Sem, Host or Exp.
5. Same-version roundtrip keeps every trailing zero. A cross-version read either migrates or refuses (N16).
6. No field anywhere accepts a JSON number for a magnitude.

### 10.2 Highest-risk alternatives

- **One universal "Value" object** covering quantity, money, time and text. Rejected: it loses kind and role safety, and it forces fake lifecycles.
- **Folding money into quantity** (currency as a unit). Rejected: 008 and 032 both say currency codes are not units; FX is time-dependent and attributed, while unit factors are definitional.
- **Inline provenance on every value** (008's current shape). Risky: it bloats embedded values and duplicates what receipts are for.
- **Resolving local times eagerly to UTC.** Rejected for future civil times (tz theory).
- **HRIS or ERP as the calendar or rate authority by default.** Rejected: the authority is the host's approved policy.
- **Letting CLDR or locale decide identity or parsing.** Rejected.

### 10.3 Publication limits

- Keep every inherited hold: research-only, `Publishable Canonical: false`, "reviewable-draft".
- No executable claim beyond the exact-arithmetic and rounding kernel.
- No standards-conformance claim.
- No redistribution of reference snapshots.
- No action beyond *proposed* Actions. Never payment, posting or staffing.

### 10.4 Next steps

1. **(Research)** Byte-level semantic reading of 008, 009, 031 and 032. Confirm the field names I marked unverified (032's scale, rounding and valuation fields; 009's working-day fields; 008's point/difference handling). Record the file hashes separately from the synthesis hashes.
2. **(Research)** Read clause text: the SI Brochure sections on dimension one, temperature and the decimal marker; the ISO 4217 scope page (retry, or use the ISO OBP preview); the Temporal ambiguity doc; RFC 9636; the ECB/SIX/UCUM/QUDT/CLDR terms of use.
3. **(Design)** Write JSON Schema for the embedded contracts and four records (strings for magnitudes). Write down the Sch/Sem/Host split for I1–I16.
4. **(Build, bounded)** One exact decimal/rational kernel with declared rounding, plus the receipt emitter, plus replay comparison. No FX feed, no tz engine: use a pinned tzdb via an existing library behind an adapter, with its release recorded.
5. **(Test)** Encode cases A–D and N1–N18 as fixtures with expected refusals.
6. **(Governance)** Name owners for RateObservation ingestion, calendar approval and designation approval in a sample startup profile and a sample multinational profile. Neither profile assumes ERP or HRIS.
7. **(Defer, tracked)** Uncertainty propagation, log units, local units, non-ISO asset registry, cash rounding, non-Gregorian arithmetic, availability using personal data. Each gets a refusal code and a named future model.
