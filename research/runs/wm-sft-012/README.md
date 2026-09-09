# WM-SFT-012 - SBOM / Supply-chain Manifest research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 14 | 6 | 11 | 25 | 87 | 5 | 10 |

The Claude result passed the complete provider schema and semantic validator.
The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. A separate no-tools Claude adversarial audit
challenged the result without adding findings or functions and found no
critical conflict.

The audit confirmed `aggregate` as the subject-model entry kind. The aggregate
root is the manifest identity and revision series; each immutable revision is a
versioned member and the unit of publication. Component entries, relationship
assertions, licence expressions and digests are revision-local children whose
identifiers must never be mistaken for global component identity. The frozen
registry-plane `standalone-mm` value remains a separate catalogue
classification.

Publication holds cover the owner-authorized single-provider waiver, live
verification of CycloneDX, CISA, purl and regulatory pins, unresolved
REFERENCE-only ownership language, three artifact-identity corrections,
explicit allocation of series/revision invariants and a non-gating completeness
claim missing from the delivered function record. Vulnerability/VEX, signing,
transparency, licence-compliance and deployed-asset neighbours also lack final
registry IDs. The package therefore remains `reviewable-draft`,
`canonical_publishable` is false, and every public artifact exposes the waiver
and holds.

Published draft:
<https://ver.cy/models/wm-sft-012-sbom-supply-chain-manifest/>
