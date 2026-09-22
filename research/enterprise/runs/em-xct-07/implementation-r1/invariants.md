# Invariants

1. A definition does not grant any submit, execute or read right.
2. The same definition ID/version has immutable content; descriptive-only definitions cannot execute.
3. A request has one host identity, immutable intent and one submission; current decisions are outside its digest.
4. Retained key reuse requires exact canonical bytes and digest in the same authenticated actor/store namespace.
5. Ordered label arrays and duplicates are preserved; duplicate JSON keys, floats and surrogates are refused.
6. Both exact scopes in one current rule must authorize the operation; partial scopes from separate rules do not combine.
7. Disclosure is checked independently and unauthorized diagnostics are uniformly withheld.
8. Policy changes, definition retirement and effects are serialized; history retains global control order.
9. At most one effect receipt belongs to a request and its resource update commits atomically with it.
10. Only pending transitions to a terminal state; committed replay never becomes expired.
11. A first effect requires now < expiresAt and the exact current resource revision.
12. Cancel and commit races yield one terminal outcome; neither rewrites prior evidence.
13. Compensation is a new request with the same narrow context, exact original before-labels and original after-revision.
14. Observations describe caller knowledge; corrections append a linear same-observer edge and never rewrite receipts.
15. Retired keys retain their slot and cannot be reused; pending keys cannot be retired.
16. The epoch detects a wrong store but cannot detect a coherent old restore; external reconciliation is required.
17. Native exports are deterministic evidence with explicit cut/time; file closure is checked separately from trust.
18. Archive replay validates referenced current-at-cut policy and effect history; it is not proof of latest authentic history.
19. Native outer schemas do not substitute for nested semantic validation.
20. Published lifecycle and reviewable-draft assurance remain distinct; studies cannot satisfy implementation audits.
