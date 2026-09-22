# R3 adoption addendum: exact wording corrections only

Both complete code and adoption-document reviews accepted with explicit limits. Code/schema/spec/installer and all 46 frozen R3 files remain unchanged. The final addendum applies the following exact edits to the previously supplied publication-addendum-r3.md. Confirm whether these wording corrections introduce any remaining blocker; use no tools. This is disclosure only, not a new implementation round. Reply briefly with disposition and any concrete contradiction.

OLD: Archive replay checks control order, per-table times, operation completeness, policy selection and effect consistency, but does not impose one globally monotonic recorded-time sequence across all administrative tables.
NEW: Archive replay checks control order, operation completeness, policy selection and effect consistency. Policy and event times are monotonic within their tables; definition and resource creation times are bounded only by the cut clock and use-time checks. Replay does not impose one globally monotonic recorded-time sequence across all administrative tables.

OLD: The nine-file fixture does not install review.json or this addendum; consult them from the complete released package, and retain them locally if offline review is needed.
NEW: The nine-file fixture does not install review.json or this addendum. Its README also links to model-fields.md, whole-object-coverage.yaml, mastership-and-rights.yaml, composition.yaml, crosswalk.json, invariants.md and migration.md, which are not installed. Claims about all adoption documentation mean only the nine listed assets; consult the complete released package and retain its documents locally for offline use.

OLD: Generated-ID collision and cross-table backdating have no dedicated R3 tests.
NEW: Generated-ID collision, snapshot-level newline identifiers and cross-table backdating have no dedicated R3 tests.

APPENDED: 
## Documentation precision

Frozen field-table prose is informative; closed schema and the semantic contract govern the bounded reference. Resource references can name a resource absent at admission; execution then rejects the precondition. Rule issuerId denotes the policy issuer, not an event issuer. Pin.revision has no auxiliary host sequence implementation. The field tables omit Policy array cardinality (0 to 128 Rules), the standalone Labels definition, and code-validated snapshot/manifest/resource rows; they are not a complete replacement for schema and code. README wording about attempts means effect execution needs current execute permission; another retained right can still produce a denied try. Historical “R2 adds” wording remains capture-time history. The acceptance workflow executes the installed companion; tests themselves are not installed.

Final addendum SHA-256 (host-computed, not a claim of your verification): 445bff81252918d68e073c56fd19c8e14fea149c1e12a7a6cec992a8bcf16a3c
