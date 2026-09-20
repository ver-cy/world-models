# WM-SFT-006 Codex pre-provider boundary

Status: preparatory boundary analysis. This is not a provider result.

- Root identity is one authority-qualified vulnerability record, not a weakness
  taxonomy class, affected deployed asset, security advisory or incident.
- Product identity and version semantics remain external and source-qualified.
  Affectedness is an assertion with range syntax, platform and evidence.
- CVE CNA content and ADP enrichments must remain attributable. NVD data is an
  enrichment, not the CVE Program master record.
- CVSS measures severity under a versioned scoring system. EPSS estimates
  exploitation probability. CISA KEV is a catalog inclusion assertion. None is
  a universal risk or remediation priority.
- CSAF/VEX and OSV may project overlapping vulnerability and affected-product
  data but retain their own profiles and loss boundaries.
- Discovery, reservation, disclosure, publication, update, rejection,
  exploitation observation and knowledge times remain distinct.
- Preserve conflicting descriptions, affected versions, severity scores and
  remediation claims rather than selecting a source silently.
- Safe agent operations exclude exploit generation, unauthorized scanning,
  disclosure that violates coordination policy and destructive history edits.

Adjudication must reject any structure that identifies vulnerabilities only by
free text or score, treats every weakness or misconfiguration as a CVE, equates
affectedness with exposure in a deployed system, treats severity as risk, or
collapses advisory, remediation, exploit and incident lifecycles into this
record.
