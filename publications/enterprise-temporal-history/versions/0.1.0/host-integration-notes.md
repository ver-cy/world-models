# Host integration notes after the third static audit

Codex clarification of residual low-severity findings N1–N3. This supplement was written after Claude's frozen R3 audit and is not represented as independently reviewed by either provider. It does not change the executable implementation.

Apply the trusted-reference clock-skew guard to **every call that takes now**, including reads, static validation and native snapshot validation, as well as admission. A backward read clock can create a read outage; a forward read clock can activate future policy or accept a future cutoff. A forward excursion can affect both inner timeline receipts and outer native storage receipts. In either layer it can prevent valid successors until verified catch-up. Quarantine and freeze the affected root, preserve restricted evidence, then use verified catch-up with current policy or an explicitly governed new identity/migration that discloses loss of continuity. No automatic repair is implemented.

The native predecessor is assumed to be trusted and already validated, including its own predecessor linkage. No-op native successor snapshots are allowed by append-only prefix semantics; the host can avoid duplicate storage facts. Global native fact uniqueness remains external.

N3's remaining direct prefix-branch case was executed independently by Codex in audit-supplement.py. It recomputes both snapshot digests and uses a correctly linked successor carrying a truncated ledger, requiring the specific History rewritten/truncated exception. The same supplement demonstrates native forward-receipt failure for current and predecessor envelopes. These three checks supplement, rather than replace or renumber, the 86 frozen behavior tests and three native installation fixtures.
