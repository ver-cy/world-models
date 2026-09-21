# Transitions

Create: currently granted recorder, scoped type, trusted receipt; active genesis revision 1 with no predecessor. Correct: same identity/type/scope/anchors, current grant, active predecessor and immediate digest; full new revision, prior rows retained. Withdraw: same guard and exact retained content; terminal state, only change metadata allowed. Retry: current rights plus identical payload ignoring restamped receipt; preserve original receipt. Reject: no input mutation.

Activity/new acquisition/new method/purpose/account-kind/external claim version changes require new identities where specified by anchors. Dependency corrections/withdrawals yield impact warnings, never automatic negation or rights. Serialized in-memory admission is not a concurrent transaction service.
