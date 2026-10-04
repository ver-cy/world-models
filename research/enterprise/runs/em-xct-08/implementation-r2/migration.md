# Migration and recovery

This release introduces an original companion, not a subtype or replacement of a World Model. Existing source keys need explicit qualification and continuity evidence; unmatched kinds/unknown generations cannot be silently coerced. Export source descriptions and review mappings before acquisition.

There is no writable archive migration. inspect_import accepts an exact supported archive only as historical evidence and emits a structured LossReport on unsupported/inconsistent input. No lossy conversion, token resume or origin-host takeover is attempted. A new host needs a new local register/epoch and verified fresh baseline. A normal process restart can reopen the current locally owned database after host continuity verification. Old/cloned databases cannot be detected internally.

Future schema/algorithm changes require new pinned versions and separately reviewed migrations preserving lexical keys, generations, purpose, mapping revisions/pins, accepted and quarantine ordinals, grants/catalogue chronology and receipt/head history. Removing a native projection does not undo a commit. Database rollback is not a semantic correction; retain evidence and reconcile externally.
