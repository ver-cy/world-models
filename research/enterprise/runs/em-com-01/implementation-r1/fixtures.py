D=lambda c:"sha256:"+c*64
def valid_case():
    sets=[{"kind":"CounterpartyRelationshipSet","setId":"set-1","partyRef":"urn:party:acme","observerDimensionRef":"urn:dimension:seller-a","createdAt":"2026-01-01T00:00:00Z"}]
    roles=[
      {"kind":"CommercialRoleBinding","bindingId":"role-c","setRef":"set-1","role":"customer","upstreamModel":"WM-ORG-014","upstreamRecordRef":"urn:014:customer:acme","upstreamVersion":"0.3.0-research.1","upstreamDigest":D("1"),"sourceMasterRef":"urn:crm:a","validFrom":"2026-01-01T00:00:00Z"},
      {"kind":"CommercialRoleBinding","bindingId":"role-s","setRef":"set-1","role":"supplier","upstreamModel":"WM-ORG-015","upstreamRecordRef":"urn:015:supplier:acme","upstreamVersion":"0.3.0-research.1","upstreamDigest":D("2"),"sourceMasterRef":"urn:procurement:a","validFrom":"2026-02-01T00:00:00Z"},
      {"kind":"CommercialRoleBinding","bindingId":"role-p","setRef":"set-1","role":"partner","upstreamModel":"WM-ORG-015","upstreamRecordRef":"urn:015:partner:acme","upstreamVersion":"0.3.0-research.1","upstreamDigest":D("3"),"sourceMasterRef":"urn:partner:a","validFrom":"2026-03-01T00:00:00Z"}]
    scopes=[{"kind":"AccountScopeBinding","scopeBindingId":"scope-le","setRef":"set-1","scopeKind":"legal-entity","targetRef":"urn:legal-entity:seller-a","sourceMasterRef":"urn:legal-master:a","validFrom":"2026-01-01T00:00:00Z"}]
    contacts=[{"kind":"ContactAssignment","assignmentId":"contact-1","setRef":"set-1","endpointRef":"urn:per-010:endpoint:billing","endpointModel":"WM-PER-010","purpose":"billing","roleBindingRef":"role-c","scopeBindingRef":"scope-le","validFrom":"2026-01-01T00:00:00Z"}]
    segments=[{"kind":"SegmentationAssertion","assertionId":"segment-1","setRef":"set-1","code":"strategic","schemeRef":"urn:scheme:account-tier","schemeVersion":"3.0.0","sourceRef":"urn:crm-score-job:17","method":"derived","assertedAt":"2026-03-01T00:00:00Z","validFrom":"2026-03-01T00:00:00Z"}]
    return sets,roles,scopes,contacts,segments
