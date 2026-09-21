# EM-XCT-05 — R1 findings, reproduction and R2 revision

R1 and R2 are distinct frozen research candidates. R1 remains under `prototype-revisions/r1/` with its original 51-test report. Claude's R1 verdict is **REVISE**; Grok's R1 verdict is **ACCEPT WITH LIMITS for the prototype only**, explicitly excluding final model/native/production readiness. Codex does not average these verdicts. The reproducible defects take precedence. Both raw responses and exact eight-file freezes remain intact.

Codex executed four R1 witnesses: newline field alias accepted; missing Dimension reached record-shape diagnostics; self-supersession with the same identity/revision but a different digest accepted; expired rejection disappeared when a clearance remained. See `prototype-r1-reproductions.json`.

R2 fixes those cases and related findings:

- ASCII identity/key/revision grammar plus full-string code checks; calendar parsing independent of platform year padding; bounded integer parsing and UTF-8/surrogate/numeric edge tests.
- Nonempty qualified Dimension required before record diagnostics.
- Current proposal pin in the host snapshot; retired/repointed proposals cannot use matching old context alone.
- Complete disjoint active/withdrawn sets; one active revision per review identity; pre-capture review rejected before eligibility filters.
- Every result is explicitly non-authorizing and carries proposal/snapshot/time, counted pins and ignored verdicts/reasons. The first profile explicitly time-bounds negative verdicts too; persistent objections are a different future profile.
- Reference coherence within records; self-supersession checked by identity/revision; complete local import resolves internal links by exact digest/type, rejects cross-proposal identity and time reversal, and checks cycles.
- Three profiles use correctly named synthetic schema/shape/classification pins. The matrix example records a reviewer rejection of a subtraction risk. Host fixtures are marked internal and contain no serialized capability to be mistaken for a client credential.
- Evidence reports code, schema, tests and README hashes plus tool versions. Mixed-version migration stays explicitly refused, and revision tokens carry no implicit ordering.

R2 passes **78 executed tests**. Both providers received its same eight-file freeze independently for a new static audit. Their R1 conclusions do not approve R2 or a future complete metamodel package. `prototype-design.md` is subsequent Codex semantic design, outside the R2 code-audit corpus. Publication of this research evidence is not promotion of the prototype to an installable model.
