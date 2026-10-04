# WM-SFT-008 - Build / Release research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 16 | 6 | 13 | 27 | 109 | 15 | 11 |

The Claude result passed the complete provider schema and semantic validator.
The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. A separate no-tools Claude adversarial audit
challenged the result without adding findings or functions and found no
critical conflict.

The audit confirmed `aggregate` as the subject-model entry kind, with Release
as the consistency and immutability root for release-scoped manifests,
artifact descriptors, variants, comparison reports and archives. A Build Run
retains a platform-issued identity and may exist without a release or feed more
than one release; whether it should become a separate event model remains an
explicit registry-review item. Registry-plane `standalone-mm` and subject-plane
`aggregate` remain separate classifications.

Publication holds cover live version pins, the owner-authorized
single-provider waiver, a missing frozen relation to the parent component and
three unnamed candidate relations, plus access/retention corrections around
signer identity, privacy applicability and field-level scope. Moving OCI
branches, SLSA status, independent build identity and ecosystem-specific yank
semantics remain visible research gaps. The package therefore remains
`reviewable-draft`, `canonical_publishable` is false, and every public artifact
exposes the waiver and holds.

Published draft:
<https://ver.cy/models/wm-sft-008-build-release/>
