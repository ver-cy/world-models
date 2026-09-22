from copy import deepcopy

D = lambda c: "sha256:" + c * 64

def valid_case():
    release = {
        "kind":"ModelRelease", "releaseId":"rel-1", "modelId":"vr.example", "version":"1.2.3",
        "packageByteDigest":D("1"), "semanticFingerprint":D("2"),
        "canonicalizationProfileRef":"urn:vercy:canonicalization:json-semantic-v1",
        "canonicalizationProfileDigest":D("3"), "immutableLocator":"urn:sha256:" + "1"*64,
        "registryEntryRef":"vr.wm-xct-013:entry:vr.example", "lockSetRef":"vr.wm-xct-040:lock:1",
        "resolutionReceiptRef":"vr.wm-xct-040:receipt:1", "catalogueProjectionRef":"model-publication/v1:vr.example:1.2.3",
        "createdAt":"2026-09-22T00:00:00Z"
    }
    receipt = {"receiptId":"receipt-1", "resolutionReceiptRef":release["resolutionReceiptRef"], "lockSetRef":release["lockSetRef"], "subjectDigest":D("1"), "closureDigest":D("4"), "targetContext":"linux-amd64-python-3.14", "resolved":True, "staged":True, "mandatoryClosureComplete":True, "memberCount":1, "members":[{"digest":D("5"), "locator":"urn:sha256:"+"5"*64, "available":True, "withdrawnForNewUse":False}]}
    assessment = {"kind":"AcceptanceAssessment", "assessmentId":"assess-1", "subjectReleaseRef":"rel-1", "subjectDigest":D("1"), "profileRef":"urn:vercy:profile:em-xct-10:0.1.0", "profileDigest":D("6"), "toolPins":[{"name":"vercy-release-gate", "version":"0.1.0", "artifactDigest":D("7")}], "fixtureSetRef":"urn:vercy:fixtures:em-xct-10:0.1.0", "fixtureSetDigest":D("8"), "fixtureResult":"pass", "criterionResults":[{"criterion":"schema", "result":"pass"},{"criterion":"negative-fixtures", "result":"pass"}], "outcome":"pass", "assessorRef":"urn:vercy:assessor:reference", "assessedAt":"2026-09-22T00:10:00Z", "effectiveAt":"2026-09-22T00:10:00Z", "evidenceRefs":["e-1"]}
    evidence = [{"kind":"ConformanceEvidenceRef", "evidenceId":"e-1", "assessmentRef":"assess-1", "subjectDigest":D("1"), "evidenceType":"fixture-log", "contentDigest":D("9"), "locator":"urn:sha256:"+"9"*64, "producingToolDigest":D("7"), "retentionClass":"release-lifetime"}]
    return release, receipt, [assessment], evidence, [], []

def withdrawal(release):
    return {"kind":"WithdrawalNotice", "noticeId":"withdraw-1", "subjectReleaseRef":release["releaseId"], "registryWithdrawalActRef":"vr.wm-xct-013:act:withdraw-1", "authorityRef":"urn:vercy:authority:maintainers", "reasonCode":"superseded", "effectiveAt":"2026-09-23T00:00:00Z", "scopes":["new-install","discovery"], "retainsReleaseBytes":True, "retainsEvidence":True, "retainsPriorLockResolution":True, "retainsTransitiveClosure":True}

def blocking_hold(release, *scopes):
    return {"kind":"PublicationHoldDisposition", "holdId":"hold-1", "subjectReleaseRef":release["releaseId"], "scopes":list(scopes), "severity":"blocking", "reasonCode":"evidence-insufficient", "state":"open", "openedBy":"urn:vercy:reviewer", "openedAt":"2026-09-22T00:20:00Z"}
