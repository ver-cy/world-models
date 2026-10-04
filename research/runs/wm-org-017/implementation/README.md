# Performance case reference profile

This companion belongs to WM-ORG-017 version 0.3.0-research.1. It demonstrates a bounded JSON data binding for synthetic cases. Read the published model AGENTS.md and spec.yaml before using it.

Run with Python 3 and `jsonschema` installed:

```sh
python validate_examples.py
```

The script validates five positive examples and 25 semantic/schema mutations. It writes fixture-results.json and checks the declared expected failure for each mutation. It does not authenticate policy references or implement a production application.

The positive examples cover concurrent employment context isolation and contested credit; a founder draft with no fictitious employment; narrative-only contractor assessment; repeated calibration and appeals; and authorized content redaction with minimal lineage metadata. All identifiers and facts are synthetic.

Each case has one governing work context. Person, employment, contract, organization, work assignment and original evidence remain external authoritative objects. External references are not copies and are not permission grants. Use a separate governed binding to resolve and authorize them.

Assessment valid_at is the time to which a judgment applies; issued_at is its issuance time; recorded_at is when this reference store records it. Source observations have their own timestamps. Corrections retain explicit predecessor identity. Post-issuance calibration must supersede the preceding assessment. Redaction can retain only policy-authorized minimum linkage; the example does not permit indefinite retention. Full unlinking is deferred.

Disclosure records describe a proposed purpose-qualified projection, not an executed export. This profile rejects omitted applicable appeal context. Exceptional disclosure and pre-issuance calibration need separately reviewed profiles. The model must never autonomously decide hiring, pay, promotion or dismissal.

Installation into a Vercy Dimension installs the semantic package. It does not automatically create these case records or connect an HRIS. Production IAM, evidence-source adapters, field-level export, concurrency enforcement and retention execution require a reviewed implementation. General state-transition completeness is not claimed by these fixtures.

Sources, provider evidence, audit scope and holds: https://ver.cy/enterprise/research/wm-org-017/
