**Disposition: accept-with-explicit-limits.** These edits are disclosure-only. They do not change the freeze and do not add a release blocker.

No concrete contradiction with the reconstructed code/schema/spec:

- History really does keep policy and event times ordered inside those tables; definition/resource rows are only cut-clock plus use-time checks (`definition-future` / `resource-future` / pin and precondition `recorded_at` vs try time). The new sentence is stricter and more accurate than “per-table times.”
- Installer `FILES` is still the nine assets; README’s extra links were never installed. Narrowing “all adoption documentation” to that list removes an overclaim.
- Adding “snapshot-level newline identifiers” to the untested set matches the lack of a snapshot-ID grammar test; it does not invent coverage.
- The appended notes match the executor (absent resource at admission → later `rejected-precondition`; execute vs other-right denied try; rule `issuerId` ≠ event `issuerId`; `Pin.revision` is opaque syntax only).

Unchanged limits still apply: host authority/continuity/rate limits, finite event budget, projection/archive gaps, candidate lock ≠ publication. No publication authority implied.