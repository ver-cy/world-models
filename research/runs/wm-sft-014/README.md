# WM-SFT-014 - Defect / Bug research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 16 | 6 | 12 | 25 | 104 | 8 | 11 |

The Claude result passed the complete provider schema and semantic validator.
The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. A separate no-tools Claude adversarial audit
challenged the result without adding findings or functions and found no
critical conflict.

The audit confirmed `entity` as the subject-model entry kind. The modelled
thing is one persistent, identified and versioned defect record with its own
lifecycle. Evidence artifacts are immutable entity-internal values rather than
independent aggregate members. The frozen registry-plane `standalone-mm` value
remains a separate catalogue classification. A cohort-scoped trend report is
kept as a deferred split candidate because its identity is not rooted in one
defect.

Publication holds cover the owner-authorized single-provider waiver, live
verification of all sixteen sources, limited clause-level access to two
paywalled standards, the unresolved WM-ACT-021 parent relation, empty frozen
namespace/source fields and two artifact identity strategies that must not use
dates or attribute values as identifiers. The package therefore remains
`reviewable-draft`, `canonical_publishable` is false, and every public artifact
exposes the waiver and holds.

Published draft:
<https://ver.cy/models/wm-sft-014-defect-bug/>
