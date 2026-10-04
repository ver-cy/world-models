# Guarded lifecycle

Mapping: proposed -> active/disputed/retracted; active -> disputed/retracted; disputed -> active/retracted; retracted terminal. Activation checks catalogue/pair, uniqueness and corrected-predecessor retirement. Changed immutable anchors need a new ID.

Epoch: new -> open -> closed; one open per scope. Open starts fence 1/head null/progress 0. Admin advances fence; admitted first batches advance progress/head atomically. All rounds must be sealed before close. Closed epoch permits no commit even for an old key; current authorized read is separate.

Round: opened -> pages in contiguous order -> sealed once. Terminal stops later pages. Incomplete/errored rounds can be sealed without completeness. Snapshot assessment never changes mappings or subjects.

Batch: new admitted key -> immutable committed receipt; exact own retry returns prior acknowledgement without an event. Changed content, principal collision and stale new-admission preconditions retain a restricted diagnostic. Unauthorized/invalid calls and exact-retry telemetry are external. Quarantine stays open; resolution is deferred.
