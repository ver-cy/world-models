# WM-XCT-006 Codex source ledger

Status: verified primary-source discovery for the Codex fallback. This is not
an external-provider result.

| ID | Primary source | Intended use |
| --- | --- | --- |
| SRC-001 | W3C, Verifiable Credentials Data Model 2.0, https://www.w3.org/TR/vc-data-model-2.0/ | Claims, credentials, presentations and actor roles. |
| SRC-002 | W3C, VC Data Integrity 1.0, https://www.w3.org/TR/vc-data-integrity/ | Proof purpose, suite, challenge, domain and verification. |
| SRC-003 | W3C, Bitstring Status List 1.0, https://www.w3.org/TR/vc-bitstring-status-list/ | Privacy-aware status and freshness. |
| SRC-004 | W3C, Data Integrity BBS Cryptosuites 1.0, https://www.w3.org/TR/vc-di-bbs/ | Draft selective-disclosure and unlinkable derived-proof profile. |
| SRC-005 | IETF, RFC 9901 SD-JWT, https://www.rfc-editor.org/rfc/rfc9901 | Selective disclosures, digests and holder binding. |
| SRC-006 | OpenID Foundation, OpenID4VP 1.0, https://openid.net/specs/openid-4-verifiable-presentations-1_0-final.html | Verifier requests, presentations and protocol binding. |
| SRC-007 | NIST, Zero-Knowledge Proofs, https://csrc.nist.gov/projects/pec/zkproof | Statement, public instance and private witness boundary. |
| SRC-008 | ZKProof Community Reference 0.3, https://docs.zkproof.org/reference | Proof-system terminology, setup and security assumptions. |
| SRC-009 | W3C, PROV-O, https://www.w3.org/TR/prov-o/ | Proof-generation and verification provenance. |
| SRC-010 | IETF, RFC 3339, https://www.rfc-editor.org/rfc/rfc3339 | Event and knowledge timestamps. |

Boundary note: a proof verifies a declared statement under pinned inputs and
assumptions. Identity truth, issuer trust, current status, authorization,
eligibility and business acceptance remain separate source-qualified outcomes.
