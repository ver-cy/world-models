# Selected source inspection

Read 2026-09-09. Sources support selected distinctions, not full conformance.
All schema fields, operational safeguards and hierarchy are authored Vercy
proposals. No private person lookup or real credential operation was performed.

- SRC-001 [W3C VC 2.0](https://www.w3.org/TR/vc-data-model-2.0/): verification is distinct from claim truth; holder need not be subject. Keep issuer trust and relying policy explicit.
- SRC-002 [W3C Bitstring Status List 1.0](https://www.w3.org/TR/vc-bitstring-status-list/): status purpose matters; optional TTL is milliseconds, has no assumed default, and does not override list validity. No status-list adapter implemented here.
- SRC-003 [HL7 FHIR R5 Practitioner](https://hl7.org/fhir/R5/practitioner.html): qualification has identifier, code, period and issuer. Qualification alone does not authorize a role at a specific organization or location. Healthcare-specific mapping only.
- SRC-004 [GMC licence to practise](https://www.gmc-uk.org/registration-and-licensing/our-registers/a-guide-to-our-registers/the-licence-to-practise): registration and licence are distinct; the UK example includes revalidation. Do not universalize its rules or determine anyone's legal eligibility.
- SRC-005 [EU regulated professions](https://europa.eu/youreurope/citizens/work/professional-qualifications/regulated-professions/index_en.htm): regulation and recognition depend on jurisdiction; even the illustrated automatic recognition route requires authority steps. Not a global recognition rule.
- SRC-006 [Credential Engine handbook](https://www.credreg.net/ctdl/handbook): selected graph, job-license, maintenance and revocation-profile passages. Scheme maintenance is distinct from holder renewal. Handbook header says 2024-02-20; exact schema release pin pending. Direct License term page could not be retrieved and is not admitted as inspected evidence.

Holds: exact dated pins, updates/errata, source reuse licenses, jurisdictional
profiles and full clause-level mappings remain unverified. This is not a
professional licensing decision service or exhaustive standards audit.
