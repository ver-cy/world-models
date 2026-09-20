# WM-SFT-006 bounded external research focus

Produce one concise, complete `model-research.schema.json` result for
`WM-SFT-006 Vulnerability Record`.

## Frozen boundary

- Treat the model as the authority-qualified record of a security
  vulnerability: stable identifiers and aliases, descriptions and problem
  types, affected product and version assertions, discovery and disclosure
  evidence, severity and exploitation assessments, references, credits,
  lifecycle, changes and provenance.
- Distinguish the vulnerability from a generic weakness class, one concrete
  deployed-system exposure, software or product identity, an advisory, patch,
  exploit, threat, incident, risk-acceptance decision and remediation task.
- Keep CVE CNA and ADP assertions attributable. Treat NVD enrichment, CVSS,
  CWE, CPE, EPSS, KEV, CSAF/VEX and OSV as versioned profiles or external
  assertions, not interchangeable truth.
- Preserve contradictory affected-version, severity and exploitability claims
  with source, scope, method, event time and knowledge time.
- Do not include physical-object properties and do not enable exploit creation.

## Size and evidence limits

- Target 6 bundles, 12 layers, 24 findings, 72 discriminating questions, 24
  artifacts and 10 functions.
- Use at least 8 current primary official sources from at least 4 independent
  organizations. Prefer CVE Program, NIST NVD/CVSS, MITRE CWE, FIRST, CISA,
  OASIS CSAF/VEX or STIX, and OSV/OpenSSF schema materials.
- Every structure and function element needs source references.
- State provider, regional, version and conformance limitations as holds.
