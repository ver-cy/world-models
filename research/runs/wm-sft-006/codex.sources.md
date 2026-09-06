# WM-SFT-006 Codex source ledger

Status: verified primary-source discovery for the Codex fallback. This is not
an external-provider result.

| ID | Primary source | Intended use |
| --- | --- | --- |
| SRC-001 | CVE Program, CVE Record Format, https://cveproject.github.io/cve-schema/ | Record identity, CNA and ADP containers, content and lifecycle. |
| SRC-002 | CVE Program, field documentation, https://cveproject.github.io/cve-schema/schema/docs/ | Machine constraints and field-level semantics. |
| SRC-003 | NIST NVD, JSON 2.0 feeds, https://nvd.nist.gov/vuln/data-feeds | Source-labelled enrichment, CPE applicability, metrics and history. |
| SRC-004 | MITRE, CWE downloads, https://cwe.mitre.org/data/downloads.html | Versioned weakness classification. |
| SRC-005 | FIRST, CVSS 4.0, https://www.first.org/cvss/v4.0/specification-document | Severity vector and metric-group semantics. |
| SRC-006 | FIRST, EPSS, https://www.first.org/epss/ | Time-varying exploitation-probability signal. |
| SRC-007 | CISA, KEV Catalog, https://www.cisa.gov/known-exploited-vulnerabilities-catalog | Known-exploitation and operational-priority assertion. |
| SRC-008 | OASIS, CSAF 2.0 Errata 01, https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/os/csaf-v2.0-errata01-os.html | Advisory, VEX product status and remediation profiles. |
| SRC-009 | OpenSSF, OSV schema, https://ossf.github.io/osv-schema/ | Ecosystem vulnerability identity, aliases and affected ranges. |
| SRC-010 | OASIS, STIX 2.1, https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html | Threat-intelligence vulnerability object and external relations. |
| SRC-011 | W3C, PROV-O, https://www.w3.org/TR/prov-o/ | Claim and transformation provenance. |
| SRC-012 | IETF, RFC 3339, https://www.rfc-editor.org/rfc/rfc3339 | Event and knowledge timestamps. |

Boundary note: these sources define records, classifications and exchange
profiles. Product applicability, deployed exposure, organizational risk and
remediation priority remain source-, environment- and policy-qualified.
