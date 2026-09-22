# Migration and rollback

This is a new package; no live production state is migrated. D1 was an unpublished research draft. Do not mechanically import its client-bound request ID into the D2 digest. Keep D1 evidence unchanged and create new requests under D2 after host review. Legacy K1/K2 labels require human semantic mapping, never exactMatch by name.

For a definition edit, add a new immutable version. Old requests retain their old exact pin; current host policy and retirement still govern tries. There is no automatic rebinding of pending requests to a newer definition. For a changed request, explicitly create a new intent/key only with a new authorized business decision, never as response-loss recovery.

Schema/algorithm upgrades require new pinned releases and a versioned migration that preserves intent bytes, record IDs, policy chronology, predecessor evidence and retained key nonreuse. No automatic upgrade or downgrade ships. Unsupported/lossy conversions are refused. Removing the native export does not undo an effect; re-export from a trusted current master. Database rollback is not an undo operation: restoration requires external reconciliation before any dispatch. Compensation is a new guarded action, not destructive rollback.
