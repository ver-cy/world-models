# Enterprise Assertion Provenance — architectural reconciliation

Date: 2026-09-21. Status: research and implementation specification in progress. This is Codex's synthesis of the two preserved independent studies and direct source checks. It is not a completed executable contract, frozen implementation audit, native installation result or publication approval.

## Chosen boundary

Use an original companion, with its own future runtime identity and specification digest, associated with WM-XCT-012 for discovery. Do not claim full conformance to WM-XCT-012, WM-XCT-026 or WM-XCT-028. Their full source/legal/domain-profile holds remain. Selective semantic alignment is sufficient; no new universal WM row is needed.

Narrow the first implementation to accounts about **external claim revisions**. General artifact lineage remains with the broader provenance model. Claim propositional content, valid time, truth interpretation and conflict adjudication stay with the external claim owner. An artifact capture can be evidence for a claim; it is not itself a proposition with an epistemic kind.

Separate **Capture**, **Activity**, **ProvenanceRecord**, **EvidenceLink** and **ConfidenceAssessment**, plus a governed **ProvenanceRegister** aggregate for storage/history. This revises the earlier Codex combined CaptureActivity proposal. One analysis activity can consume many captures, generate multiple accounts and be reviewed separately; collapsing event and representation would lose this cardinality. The aggregate must preserve each record's independent identity and exact revision pins.

## Disagreement disposition

| Issue | Provider proposal or limit | Decision and reason |
|---|---|---|
| Epistemic order | Claude proposes observed > source-asserted > inferred > proposed > unverified | **Reject the total order.** These describe the basis and role of an account, not a universal truth or quality scale. Check kind-specific prerequisites independently. An inference can be better supported than an unreliable observation; a proposal concerns intent |
| Proposal and lifecycle | Grok places proposal in lifecycle while also using account-kind | **Keep orthogonal.** An issued account can describe a proposal; withdrawing that account does not execute or cancel the proposed action |
| Capture versus activity | Claude separates them; Grok and the earlier Codex proposal combine them | **Separate.** A representation and the event that acquired or generated it have different identities, reuse and cardinalities. The implementation may serialize them together, but it must not merge them |
| Scope of observation | Both prohibit AI-over-file being described as a live check | **Adopt a bounded consistency rule.** Account about-ref, activity's declared observed target and evidence role must match. Synthesis does not become direct observation because its inputs were captures or a human agreed. These checks validate declarations; they cannot prove a live connection happened |
| Source author versus recorder | Studies sometimes speak of the source author as the account author | **Keep separate roles.** Source author, observer, synthesizer, account asserter, recorder and assessor remain independently attributable. Reading a document does not transfer authorship or responsibility |
| Independence | Claude would count disjoint closures, distinct origin keys and distinct digests as independent; Grok also proposes independent labels | **Reject inferred independence.** Those checks can detect known shared inputs and byte copies; they cannot prove independence. Output known-shared-origin or unknown. Any asserted independence needs a separate attributable basis and still remains a declaration |
| Disclosure | Grok suggests placeholders revealing hidden evidence existence; Claude suggests closure-wide all-or-deny | **Choose full-register all-or-deny for the first reference.** Hidden existence, counts, IDs and contrary-evidence flags can be sensitive. A partial-disclosure model requires separate authorization and leakage review |
| Current root | Grok describes current root as unique visible non-superseded record | **Reject view-dependent history.** The trusted host holds one accepted register root independent of the reader's projection. As-of selection is a derived view, not proof of freshness or a new root |
| Retraction | Both preserve history and trigger dependent review | **Adopt.** Changed support creates an impact result; it does not automatically negate the external claim or rewrite old account kind. Reassessment and correction require explicit authority |
| Confidence | Both require scheme, method, purpose and assessor; wider numeric semantics differ | **First increment: qualitative, method-qualified assessments only.** No implicit score, default probability or arithmetic. Numerical probability/calibration and cross-scheme mappings are deferred rather than accepted as a bare number with labels |
| Parent digests | Both compare the brief's spec digests with publication.json synthesis digests and flag a mismatch | **Resolve the apparent mismatch using direct evidence.** These hash different artifacts. The exact spec bytes were retrieved, compared to local bytes and independently matched to the public runtime index. The spec digests are valid pins for the parent specifications; neither digest is the new companion's identity. Original provider warnings remain preserved |
| Full parent read | Claude read parts through a summarizing reader, including incomplete 028 detail | **Do not upgrade the provider's evidence claim.** Direct local inventories contain the complete parsed specifications; targeted findings, fields and all holds were separately examined. This does not re-verify every legacy external source |
| Integrity and authenticity | Both distinguish byte integrity from truth; some in-toto wording implies authentication | **A digest is only byte binding.** Authentication requires separately verified signature/trust-policy evidence. The standalone reference must not label a declared digest or attribution authenticated |
| Source versions | Grok cites both SLSA 1.2 and 1.0, plus additional project release claims | **Use the directly checked SLSA 1.2 build-provenance page.** Unchecked provider release dates/tags and nanopublication details remain provider assertions; not normative anchors |

## Exact parent-pin reconciliation

`upstream-verification.json` records public byte comparisons for spec.yaml, AGENTS.md and publication.json. `crosswalk.proposal.json` separately records the runtime index digest/version checks. These are different from the providers' summarizer views.

| Parent | Published version | SHA-256 of spec.yaml bytes |
|---|---|---|
| WM-XCT-012 | 0.3.0-research.1 | aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5 |
| WM-XCT-026 | 0.3.0-research.1 | efd72d845af742b7aa7d7592e5f6087ef034145f468a799927163cd6eb599ee5 |
| WM-XCT-028 | 0.3.0-research.1 | 3aab7ecb4ba7d4e56d650060b982058c4253e5bcbd621e2784480e8cc4f3d636 |

The different `synthesis_sha256` values identify the publisher's synthesis input. Their difference is expected. No field named `parent digest` is needed to prove a raw specification digest.

## Implementation boundary and acceptance work

Implement the following before making an installable-publication claim:

1. A closed versioned schema for five independently identified record types and one aggregate. No embedded claim text, credential values, implicit source fetching or arbitrary executable extensions. Explicit nullable unknowns and required cardinalities.
2. Capture representation identity separate from Activity occurrence identity; exact external claim revision pin and about-ref; account-author/source-author separation; method-qualified qualitative assessments.
3. Local typed graph checks. Internal record references must pin revision and digest. Design links, evidence references and actual derivation edges must not be conflated. Avoid a circular admission requirement in which an account requires a link that itself requires the not-yet-created account: links may target an exact external claim pin, or an explicitly atomic authorized graph submission must be specified.
4. A pure admission function under trusted host configuration, clock and current-root control. Exact replay, conflicting replay, immutable correction, authorized retraction, source-writer changes and history-prefix validation need independent tests. A durable authenticated concurrent service remains out of scope.
5. Historical account views and dependency-impact results. Source unavailability differs from source withdrawal, integrity failure and falsehood. Exact old pins remain interpretable. Updated target claims never inherit prior support automatically.
6. Full-register read/purpose gate with uniform denial, before detailed diagnostics. Static roles express configuration checks only; IAM and user authentication remain external.
7. Separate whole-object facets, mastership, lifecycle and migration decisions for every type. The earlier working proposal supplies 17 question routes to refine, not a completed normative schema.
8. Three synthetic fixtures: startup file acquisition/source statement; group conflicting accounts and shared-origin detection; AI synthesis plus human review that retains inference status. Neither actual organization data nor a claim about named companies is used.
9. Executed positive, at least ten distinct negative, history, retraction, rights, replay, round-trip and lossy-migration-refusal tests. Missing evidence must be an allowed explicit state; migration must not invent calibration or live-observation evidence.
10. Own native identity/specification and semantic-only parent binding, then new-Dimension composition tests. Deliberately invalid nested data must be rejected by the companion; passing native envelope validation alone is insufficient.
11. A frozen **implementation** audit by both actual providers, with exact artifacts and honest truncation/source limits; remediation if necessary. These independent studies are not that audit.
12. Authorized publication only after a non-critically-conflicted usable package exists; immutable archive, public digest/catalogue checks, downloaded-package tests, queue/outcome updates and isolated commit.

## Remaining scope

This contour is in research, with both independent studies complete. No implementation, test pass, installation or new metamodel release is claimed here. Outstanding work is concrete in the list above. Sector/legal/clinical/forensic profiles, PKI, source connectors, independent-source proof, probabilistic confidence, partial disclosure, retention/erasure and production concurrency remain separately bounded follow-up work. No provider text authorizes a publication or changes the owner's permissions.
