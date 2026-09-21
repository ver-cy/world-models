# Enterprise Fact Authority · 0.1.0

An English reference contract for accountable parties, identified stewardship appointments, source precedence, separate write grants, and retained competing observations. It is a **reviewable draft** and a bounded increment of EM-XCT-02.

This package is discoverable alongside WM-XCT-001. That location is **not an `is-a` claim**: a predicate is not a controllable object, and these records are not conforming WM-XCT-001 control records. The unchanged parent specification remains the semantic reference for selected appointment, time and contestation patterns. See `boundary-decision.md` and `crosswalk.json`.

## Use the reference

Python 3.10+ and `pip install -r requirements.txt` are required. In a trusted environment:

```python
import authority as a
c = a.load('examples/startup.config.json')  # deployment-owned, trusted configuration
l = a.load('examples/startup.json')         # trusted synthetic historical archive
a.validate_ledger(l, c)
answer = a.evaluate(l, c, actor='urn:synthetic:reader', purpose='governance-review',
    scope='urn:synthetic:scope', predicate='urn:synthetic:predicate',
    subject='urn:synthetic:subject', validAt='2026-09-21T12:00:00Z',
    knownAt='2026-09-21T12:00:00Z', now='2026-09-21T12:00:00Z')
assert answer['status'] == 'contested'
assert answer['value'] is None
```

The examples use fixed synthetic time. An integrating service must supply its trusted receipt time and authenticated actor; users must not choose these or replace the configuration/ledger. `admit` performs an in-memory, atomic append into a **new** ledger. Persist it with concurrency control in a production adapter. Never expose `import_snapshot` as a write API: it validates trusted archives and does not authenticate their history. Native V3 validates only the outer snapshot envelope; invoke this companion explicitly before use and live admission. Validate each new full snapshot with validate_extension against the trusted prior snapshot. The native tool alone can store semantically invalid nested data.

Run `python test_authority.py`. To test new synthetic Dimensions, use `python acceptance.py --composer <trusted-WM-XCT-040-directory> --skill <trusted-vercy-skill-directory> --report acceptance-results.json`. Tool pins bind the expected local bytes; they do not sandbox Python imports or authenticate downloaded software.

## What is implemented

- Exact Dimension × scope × predicate governance, one-valued facts, explicit bounded UTC intervals and two temporal query axes.
- A value-accountable party distinct from a referenced definition-authority record, steward, publisher and writer.
- Source precedence separate from write grants; smaller priority numbers have higher precedence. Equal highest priority plus different tagged lexical values returns `contested` with both evidence references.
- Immutable revisions, previous-content digests, historical corrections, payload-idempotent replay preserving original receipt and receipt checks. A transfer uses distinct terms and preserves historical rows.
- All-or-nothing read projection for full-register readers; no partial visibility that hides a conflicting observation. Historical `routeTo` is informational at `routeValidAt`; resolve current routing before sending anything.
- Three small fixtures: startup (equal-priority disagreement), group (higher-precedence source beats later import), AI/software team (agreement with an explicit stewardship gap). They demonstrate patterns, not a full multinational competence graph or real company data.

## Deliberate limits

No authenticated publication, signatures, durable ledger, source connector, subject-to-scope verification, policy federation, recursive delegation, definition ownership resolution, adjudication workflow, confidence scoring, staleness detection, multi-valued predicates, units conversion, legal validity, production access enforcement or existing-Dimension migration. The trusted host determines correct scope and predicate cardinality. Malformed/missing authority never grants permission. A selected value is named `preferred`; it can still be false. Inputs may be incomplete; this library cannot prove it has all relevant observations or authorities.

Assignments and rules have their own stable IDs and intervals, but their versions are captured in an authority revision. Independent concurrent updates and reuse of one assignment across authorities are deferred. Missing steward yields an empty route; it never approves a disputed value. Full parent research and its historical source holds remain open.

## Native identity and host boundary

The companion has its own runtime ID `vr.profile.enterprise-fact-authority`, specification (`spec.json`) and object namespace. WM-XCT-001 is a separately pinned **semantic-only** reference. Snapshot storage belongs to the register operator, never an implicit steward grant. A part citation needs its containing authority revision/digest.

The host must keep the complete ledger and raw admit/validation diagnostics internal. A non-reader receives only a submission receipt or a generic rejection, not the full return value. Functions here are not a public API. Receipt retries preserve the originally stored recordedAt; a restamp alone is ignored. Source writer rotation can correct/retract earlier same-source observations under the current explicit grant. Structural snapshot truncation is checked against a trusted prior snapshot; forged or incomplete roots remain outside the trust boundary.
