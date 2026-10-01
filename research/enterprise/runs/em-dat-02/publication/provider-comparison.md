# EM-DAT-02 provider comparison

Claude and Grok agree to complete reserved WM-DAT-008 as Data Product without a new model or runtime identifier. Dataset, Distribution, interface contract, pipeline/run, observation, assessment, offering, agreement and authorization remain separately mastered.

Both require Product and Catalog Record to keep separate identities and lifecycles. Reconciliation makes DataProduct, ProductCatalogRecord and ConsumerEntitlementBinding three separately rooted objects mastered by WM-DAT-008. They may share one publication facade but are not one type and are not aggregate children that disappear with Product withdrawal.

Claude initially described entitlement as a dependent relation; Grok showed that approval, suspension, effective interval and audit require identity. The reconciled object is therefore separately rooted but dependent on Product Version and external terms/authority references. It is neither agreement nor access grant and allocates no model identifier.

The frozen audit accepted all four boundary decisions and returned REVISE for rule IDs, lifecycle, identity keys, version triggers, relation holds and fixtures. All 16 blocking groups and 13 non-blocking findings were remediated once without rerunning the audit. Candidate `0.3.1-candidate.3` has 28 stable invariants and 27 fixtures.
