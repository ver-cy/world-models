**Disposition: no blocker. The candidate with these corrections remains accept-with-explicit-limits.** I reviewed the supplied edit text statically against the previously reviewed code. I did not verify the addendum hash.

All edits match the code, with one exception:

- **Edit 1 (history times):** accurate. `_validate` checks that policy and event times are monotonic within their tables. Definition and revision-0 resource times are bounded only by the cut clock and by the `definition_at` and `precondition` checks.
- **Edit 2 (non-installed documents):** accurate, and it resolves D2.
- **Edit 3 (test gaps):** accurate, and it resolves D6.
- **Appended section:** accurate on the issuer role, `Pin.revision`, the Policy cardinality of 0 to 128, the omitted Labels definition and rows, the fact that a denied try can come from any retained right, the capture-time "R2 adds" wording, and non-installed tests. It resolves D3 through D5.

**One minor contradiction, non-blocking:** the sentence "Resource references can name a resource absent at admission; execution then rejects the precondition" is too absolute.
- *What the code does:* the check runs at each allowed try against the live revision. So if a request stays pending (execute denied) and the resource is created later at the expected revision, a later allowed try commits.
- *Suggested wording:* "an allowed try rejects the precondition only if the resource is still absent or at a different revision at that try; a pending request can commit after later creation."

**Optional:** the README's "Package and review state" list also cites "the executable sources" (`action.py`, `history.py`, `native.py`), which are not installed either. Edit 2 could name them alongside the other documents.

The unchanged release gates still apply: Grok's R3 result, executed reports against the frozen hashes, pinning the final addendum bytes in the release manifest, the final `review.json` disposition, and live publication verification.