# EM-XCT-02 research and reconciliation

Two independent studies received the same frozen English boundary on 2026-09-21: Claude through its actual CLI with web research enabled, Grok through the owner's browser in Heavy mode. Original answers and hash manifests are separate files. Claude reports `claude-opus-5`; Grok's backend version is not exposed and is not inferred. Codex's normalized contract is separate from both answers. All examples are synthetic.

The direct comparison parsed full published specifications of WM-XCT-001, WM-XCT-002 and WM-XCT-012, recursively inventoried their findings/data elements, compared spec/AGENTS/publication bytes to production and retained holds. This is not a fresh verification of every historical source or every proposed field. The archived semantic basis is 0.3.0-research.1 for each. No independent native instance validators/examples for this exact enterprise contract existed in those legacy semantic packages; new companion examples and tests are therefore explicit additions.

## Evidence and alternatives

`source-verification.json` records nine primary/public author sources, section/version, inspection limits, claim, chosen consequence, URL and download digest where available. A successful fetch is not conformance. All schema and code here are original; external standards/products are paraphrased and linked, with no copied schemas or source documents.

Three approaches informed the result:

1. **Standards:** PROV separates provenance agency from the target; ODRL makes policy conflict strategy explicit; NIST's ABAC abstract distinguishes authorization inputs. We use these as patterns, not a standard mapping. Detailed NIST clauses and unread ISO texts remain unverified here. [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/), [ODRL §2.10](https://www.w3.org/TR/2018/REC-odrl-model-20180215/#conflict), [NIST](https://csrc.nist.gov/pubs/sp/800/162/upd2/final).
2. **Operational practice:** Kubernetes field management detects conflicts but also supports force/update behavior; that is not enterprise truth. DataHub separates custom ownership types from the privilege to edit owners. Catalog ownership in OpenMetadata is a product convention, not universal fact authority. We separate assignment, precedence and write grant. [Kubernetes](https://kubernetes.io/docs/reference/using-api/server-side-apply/), [DataHub](https://docs.datahub.com/docs/ownership/ownership-types), [OpenMetadata](https://docs.open-metadata.org/v2.0.x/how-to-guides/guide-for-data-users/data-ownership).
3. **Alternative school:** domain ownership in data mesh motivates scoped governance; XTDB distinguishes valid/system time; Wikidata distinguishes statement ranks from references. Our exact-scope, retained-assertion algorithm is an original proposal, not an implementation of these systems or a CRDT. [Data mesh](https://martinfowler.com/articles/data-mesh-principles.html), [XTDB](https://docs.xtdb.com/concepts/key-concepts.html), [Wikidata](https://www.wikidata.org/wiki/Help:Ranking).

## Disagreements and decisions

| Issue | Claude | Grok | Codex disposition |
|---|---|---|---|
| Attach point | Profile of WM-XCT-001 | Reject subtype: predicate is abstraction, not controllable object | Discovery association only; independent companion contract. Original parent's semantics unchanged. Direct inspection confirms Grok's quoted boundary |
| Number of parent bundles | Fetch summarizer returned four; flagged discrepancy | Six in boundary | Full parsed source has six; discrepancy is summarization, not a source change |
| Definition versus values | Must separate governs=definition/values | Broad FactAuthority wording also includes meaning | 0.1.0 explicitly governs values; definition authority is unresolved external reference |
| Source rank and write rights | Separate precedence/admission/change right; 002 excludes writes | Distinct rank vs write permission | Separate MastershipRule and original WriteGrant; no 002 conformance claimed |
| Assignment identity | Independent identified records | Reject unidentifiable aggregate fields | Stable identified parts and immutable party/source anchor, versioned by containing authority revision. Independent streams and cross-authority portability deferred |
| Overlap | Suggested specificity algorithm | Refuse invented lattice | Exact scope only; overlapping operative records fail to select |
| Temporal proof | Bitemporal history is not authenticated publication | Separate authenticated policy clock/pin | Trusted receipt admission + pins; no signature/publication authenticity claim. Other clocks not invented |
| Disclosure | Predicate-level redacted contest projection proposed | Preserve conflict but restrict payload | Minimum all-or-deny full-register read; no partial projection, no count leakage to denied reader |
| Future knowledge | Suggested clamp | Explicit policy clock | Reject future knownAt; no silent alteration of question |
| Broad first increment | Many additional types | Narrow startup contract | Bounded original reference plus three small pattern fixtures; comprehensive group/AI governance deferred |

The executable contract selects a **preferred observation under policy**, never an objectively true fact. It is useful for building a Company Dimension's governance register today, but remains partial with respect to the broader registry contour. Source/subject authentication, real connectors, definition governance, independent assignment streams, federated competencies, durable transactions, full history/erasure policy and human adjudication are next research targets. Parent legal/source holds are inherited as limitations, not silently closed by this study.
