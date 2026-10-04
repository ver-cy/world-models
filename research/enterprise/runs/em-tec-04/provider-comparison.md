# EM-TEC-04 provider comparison

Claude and Grok agree to complete reserved WM-SFT-010 as Runtime / Compute Environment and allocate no new model or runtime identifier. WM-SFT-002 remains the logical system/application master, WM-SFT-009 owns deployment occurrence and desired placement, and WM-XCT-039 supplies mastership and bounded impact projection semantics.

The first Claude study proposed DeployedInstance as a WM-SFT-010 subject. Grok challenged that ownership: live replicas may outnumber and outlive one deployment occurrence, but they must not become competing logical-system masters. The reconciled candidate therefore uses `RuntimeOccupantRecord`, a dependent observation bound to one WM-SFT-002 subject, one WM-SFT-009 occurrence and one immutable artifact version. Its runtime key is a scoped correlation key, not independent gold-copy identity.

Both providers treat Configuration Item as an effective-dated designation over an eligible external or WM-SFT-010 subject. Withdrawal closes the designation and never destroys the designated subject. Asset identity stays external and joins a resource only through dated evidence.

Grok required explicit environment/resource/cluster/node stratification and separate membership versus hosting intervals. The frozen audit added resource-to-environment containment, historical status assertions, endpoint rules, typed resource kinds, correction and succession records, functional-edge conflict rules, and a named mastership split for desired and observed facts.

The final candidate has 27 invariants, four required external relations where semantically mandatory, and 28 fixtures. It is a reviewable completion of the existing reservation, not a canonical publication claim.
