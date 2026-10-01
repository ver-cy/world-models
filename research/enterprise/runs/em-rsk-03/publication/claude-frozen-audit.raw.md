**REVISE**

The honesty question resolves in the artifact's favour at the declaration level and against it at the schema level. `allocationBoundaryState: "unresolved-cluster"`, `decision: "NEW MODEL CANDIDATE CLUSTER"`, AD-04's second clause, the first hold and the identical `publicationStatement` in both candidates do keep the cluster explicitly unresolved and explicitly non-publishable, and no prose anywhere asserts one proven root. But `identityTest` is built in the shape of a single type — one `stableIdentityRule`, one `mastership` string, one `independentLifecycle` array — and that array is verbatim the `PermissionGrant` lifecycle, so the structure asserts what AD-04 denies. Fix items 1–4 and the cluster is honest as recorded.

Confirmed, both candidates: `modelId: null`, `registryId: null`, `allocationState: "unassigned"`, `newRuntimeId: false`, hold "No registry namespace or identifier is allocated and none may be guessed" — no identifier is allocated, and `EM-RSK-03.AD-*` / `.EP-*` / `.FX-*` are contour-scoped rule keys, not registry identifiers. `canonicalPublishable: false` in all three files, `executable: false` in the fixtures, and the holds keep crosswalk, relations, conversion and conformance open — no publication readiness is claimed.

Defect checklist (closed; 16 items):

1. `identityTest` is single-root shaped; replace with per-object entries under cluster wrapper.
2. Delete cluster-level lifecycle and use per-object lifecycles.
3. Add a real AccessRole version-identity rule and bind it.
4. Record per-object mastership and restore mastership hold.
5. Give delegated grant its own grant identity/lifecycle semantics.
6. Add revocation, propagation and audit field carriers including partial propagation.
7. Model live justification entries with kind, state and validity.
8. Restore fail-closed/unevaluable handling and absent-value semantics.
9. Add a closed principal-kind constraint.
10. Put CredentialMetadata under its explicit account/profile owner.
11. Split usable profile bases from pending neighbours.
12. Replace tautological rule-restatement fixtures with concrete cases.
13. Correct fixture mappings and cover every rule materially.
14. Delete the unkeyed duplicated invariants array.
15. Record WM-PER-002 interim disposition and failure alternative.
16. Add the publication statement to fixtures.
