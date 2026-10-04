# R2 audit adjudication and R3 corrections

Both complete actual responses were read. Claude Opus 5 High reports a full static no-tools audit and **revise-before-release (narrow)**. Grok Heavy reports internal team coordination and an accepting verdict **with an explicit source truncation**: about 24,500 characters of the installed bundle were not visible to its reviewers. The submitted attachment preview matched all 246,554 characters; provider-side context omission still occurred. This is NOT a complete independent implementation audit and NOT a strict no-tools pass. Preserve the raw response and repair evidence delivery using smaller complete fragments in the next round; do not resend the same oversized packet.

Claude confirms all R1 corrections. Its new concrete findings are accepted:

| Finding | R3 disposition |
|---|---|
| ID/token/hash/URI grammar accepts a trailing newline under Python `$` | Replace ambiguous end anchors with a negative any-character assertion usable in Python and ECMAScript; test malformed endings. No claim that all regex engines are identical. |
| Resource or definition can be created under an existing request ID, poisoning later validation | Check requests and events in admin admission; also collision-check generated request/Event IDs across all four namespaces. Refuse before commit. |
| Reader/observer receives Dimension-wide event/control counters | Strip both counters from caller receipt and observation projections; preserve them only in privileged native evidence. Update docs and tests. |
| Low-privilege but authorized callers can consume the finite event capacity | Explicit accepted fixture limit: all event-producing operations need host rate/admission limits; no quota or rollover implementation is claimed. Explain that event capacity binds first, approximately 3,333 never-executed pending requests or 2,500 first commits before replays/observations/cancellations. Do not call it enterprise-scale storage. |
| Noncanonical manifest/snapshot bytes and numeric type coercion pass verification | Require canonical snapshot bytes and canonical manifest bytes with exact integer cut fields. Preserve exact byte-root meaning. |
| History accepts zero-rights replay or unreadable denied-cancel events the executor cannot emit | Align historical replay admission and denied-cancel checks with the executor. |
| Event/object identity overlap and only-submission error shape | Require disjoint IDs and explicitly reject empty operation tails. |
| Installed AGENTS refers to missing adoption docs and dependency declaration | Install README, semantic contract, adoption limits and requirements alongside original five assets; read back all nine. |
| Avoidable repeated scans | Use policy-control binary search and request lookup map; retain bounded-reference performance limits and avoid claiming benchmark results. |
| Coverage/mastership detail | Explicitly cover the synthetic resource object and host policy/retirement overlays; keep them fixture support, not extra canonical enterprise models. |

Grok's claim that raw SQL seeding is necessarily an invalid history is not accepted: the tests explicitly construct histories, run the full semantic replay, then exercise actual public capacity rollback. This proves that boundary behavior for those seeded histories, not 10,000 public API calls, a rich enterprise workload or performance. Preserve that limit. Definitions and request caps are still enforced by the same atomic count guard; the event cap makes 10,000 fully admitted requests unreachable in this reference. Additional endpoint assertions are useful but do not replace the missing source audit.

Grok's expiry concern misreads `trial_for(..., allowed=False)`: that parameter disables the allowed-required check, rather than requiring the stored decision to equal false. Its incomplete source context is a material limit. A second independent observation means another occurrence by the same authenticated actor under this actor-scoped API; a second observer identity is not supported.

The current working R3 code has begun these changes. R2's 46 frozen files and their 63 source/bundle tests and three native results remain immutable. Do not call working R3 tested until fresh reports match its final bytes. Complete docs/schema/bundle/tests/native installations, freeze R3 and obtain focused complete-source checks from both providers. No additional general research study is needed. R2 must not be released as frozen.
