import unittest
from copy import deepcopy
from acceptance import Invalid, derive_status, validate_release
from fixtures import D, blocking_hold, valid_case, withdrawal

CTX = "linux-amd64-python-3.14"
AT = "2026-09-24T00:00:00Z"

class GateTests(unittest.TestCase):
    def status(self, mutate=None):
        parts = list(valid_case())
        if mutate: mutate(parts)
        return derive_status(*parts, CTX, AT)

    def invalid(self, mutate):
        with self.assertRaises(Invalid): self.status(mutate)

    def test_valid_is_all_current(self):
        s=self.status(); self.assertTrue(all(s[x] for x in ("exists","installable","assured","canonical","eligibleForNewInstall","discoverableForNewConsumers")))
    def test_missing_digest_rejected(self): self.invalid(lambda p:p[0].__setitem__("packageByteDigest","TBD"))
    def test_zero_digest_rejected(self): self.invalid(lambda p:p[0].__setitem__("packageByteDigest",D("0")))
    def test_bad_semver_rejected(self): self.invalid(lambda p:p[0].__setitem__("version","v1.2"))
    def test_main_locator_rejected(self): self.invalid(lambda p:p[0].__setitem__("immutableLocator","https://x/main.zip"))
    def test_wildcard_lock_rejected(self): self.invalid(lambda p:p[0].__setitem__("lockSetRef","vr.wm-xct-040:lock:1.*"))
    def test_latest_receipt_rejected(self): self.invalid(lambda p:p[0].__setitem__("resolutionReceiptRef","vr.wm-xct-040:receipt:latest"))
    def test_digest_is_not_fingerprint(self): self.invalid(lambda p:p[0].__setitem__("semanticFingerprint",p[0]["packageByteDigest"]))
    def test_release_can_exist_without_fingerprint_but_not_canonical(self):
        s=self.status(lambda p:[p[0].pop(k,None) for k in ("semanticFingerprint","canonicalizationProfileRef","canonicalizationProfileDigest")]); self.assertTrue(s["installable"]); self.assertFalse(s["canonical"])
    def test_same_coordinate_new_bytes_rejected(self):
        r=valid_case()[0]; with_registered={(r["modelId"],r["version"]):D("a")}
        with self.assertRaises(Invalid): validate_release(r,with_registered)
    def test_same_coordinate_same_bytes_is_idempotent(self):
        r=valid_case()[0]; self.assertTrue(validate_release(r,{(r["modelId"],r["version"]):r["packageByteDigest"]}))
    def test_receipt_wrong_digest_rejected(self): self.invalid(lambda p:p[1].__setitem__("subjectDigest",D("a")))
    def test_wrong_target_context_rejected(self): self.invalid(lambda p:p[1].__setitem__("targetContext","other"))
    def test_unresolved_not_installable(self):
        s=self.status(lambda p:p[1].__setitem__("resolved",False)); self.assertFalse(s["installable"]); self.assertFalse(s["canonical"])
    def test_mutable_transitive_member_rejected(self): self.invalid(lambda p:p[1]["members"][0].__setitem__("locator","https://x/latest"))
    def test_missing_transitive_member_blocks_install(self):
        s=self.status(lambda p:p[1]["members"][0].__setitem__("available",False)); self.assertFalse(s["eligibleForNewInstall"])
    def test_assessment_cannot_transfer_to_same_fingerprint_other_bytes(self): self.invalid(lambda p:p[2][0].__setitem__("subjectDigest",D("a")))
    def test_tool_latest_rejected(self): self.invalid(lambda p:p[2][0]["toolPins"][0].__setitem__("version","latest"))
    def test_tool_digest_required(self): self.invalid(lambda p:p[2][0]["toolPins"][0].__setitem__("artifactDigest",""))
    def test_negative_fixture_failure_removes_assurance(self):
        s=self.status(lambda p:p[2][0].__setitem__("fixtureResult","fail")); self.assertFalse(s["assured"]); self.assertFalse(s["canonical"])
    def test_revoked_assessment_removes_assurance(self):
        s=self.status(lambda p:p[2][0].__setitem__("outcome","revoked")); self.assertFalse(s["assured"])
    def test_later_failure_supersedes_prior_pass(self):
        def m(p):
            a=deepcopy(p[2][0]); a.update(assessmentId="assess-2",supersedesRef="assess-1",outcome="fail",effectiveAt="2026-09-23T00:00:00Z",evidenceRefs=["e-2"])
            e=deepcopy(p[3][0]); e.update(evidenceId="e-2",assessmentRef="assess-2",contentDigest=D("a"),locator="urn:sha256:"+"a"*64)
            p[2].append(a); p[3].append(e)
        self.assertFalse(self.status(m)["assured"])
    def test_missing_superseded_assessment_rejected(self):
        self.invalid(lambda p:p[2][0].__setitem__("supersedesRef","missing"))
    def test_duplicate_criterion_rejected(self):
        self.invalid(lambda p:p[2][0]["criterionResults"].append({"criterion":"schema","result":"pass"}))
    def test_missing_evidence_rejected(self): self.invalid(lambda p:p[3].clear())
    def test_wrong_evidence_subject_rejected(self): self.invalid(lambda p:p[3][0].__setitem__("subjectDigest",D("a")))
    def test_evidence_kind_threshold(self):
        s=self.status(lambda p:p[3][0].__setitem__("evidenceType","signature")); self.assertFalse(s["assured"])
    def test_future_assessment_not_active(self):
        s=self.status(lambda p:p[2][0].__setitem__("effectiveAt","2027-01-01T00:00:00Z")); self.assertFalse(s["assured"])
    def test_duplicate_evidence_rejected(self):
        self.invalid(lambda p:p[3].append(deepcopy(p[3][0])))
    def test_unpinned_evidence_tool_rejected(self):
        self.invalid(lambda p:p[3][0].__setitem__("producingToolDigest",D("a")))
    def test_evidence_locator_binding_rejected(self):
        self.invalid(lambda p:p[3][0].__setitem__("locator","urn:sha256:"+"a"*64))
    def test_receipt_lock_set_mismatch_rejected(self):
        self.invalid(lambda p:p[1].__setitem__("lockSetRef","vr.wm-xct-040:lock:other"))
    def test_receipt_member_count_mismatch_rejected(self):
        self.invalid(lambda p:p[1].__setitem__("memberCount",2))
    def test_withdrawn_dependency_blocks_new_use(self):
        s=self.status(lambda p:p[1]["members"][0].__setitem__("withdrawnForNewUse",True)); self.assertTrue(s["installable"]); self.assertFalse(s["eligibleForNewInstall"]); self.assertFalse(s["canonical"])
    def test_future_hold_does_not_block_past(self):
        def m(p): h=blocking_hold(p[0],"canonical"); h["openedAt"]="2027-01-01T00:00:00Z"; p[4].append(h)
        self.assertTrue(self.status(m)["canonical"])
    def test_unknown_hold_state_rejected(self):
        def m(p): h=blocking_hold(p[0],"canonical"); h["state"]="mystery"; p[4].append(h)
        self.invalid(m)
    def test_stale_projection_reported(self):
        parts=valid_case(); s=derive_status(*parts,CTX,AT,projection={"installable":False,"canonical":True,"eligibleForNewInstall":True,"discoverableForNewConsumers":True}); self.assertFalse(s["projectionConsistent"]); self.assertEqual(s["projectionMismatches"],["installable"])
    def test_blocking_canonical_hold_only_blocks_canonical(self):
        def m(p): p[4].append(blocking_hold(p[0],"canonical"))
        s=self.status(m); self.assertFalse(s["canonical"]); self.assertTrue(s["installable"]); self.assertTrue(s["eligibleForNewInstall"])
    def test_blocking_new_install_hold_keeps_bytes_resolvable(self):
        def m(p): p[4].append(blocking_hold(p[0],"new-install"))
        s=self.status(m); self.assertFalse(s["eligibleForNewInstall"]); self.assertTrue(s["installable"])
    def test_blocking_discovery_hold_only_hides(self):
        def m(p): p[4].append(blocking_hold(p[0],"discovery"))
        s=self.status(m); self.assertFalse(s["discoverableForNewConsumers"]); self.assertTrue(s["eligibleForNewInstall"])
    def test_advisory_hold_does_not_block(self):
        def m(p): h=blocking_hold(p[0],"canonical"); h["severity"]="advisory"; p[4].append(h)
        self.assertTrue(self.status(m)["canonical"])
    def test_waiver_requires_authority_and_evidence(self):
        def m(p): h=blocking_hold(p[0],"canonical"); h["state"]="waived"; p[4].append(h)
        self.invalid(m)
    def test_valid_waiver_does_not_block(self):
        def m(p): h=blocking_hold(p[0],"canonical"); h.update(state="waived",closedAt="2026-09-23T00:00:00Z",authorityRef="urn:authority",dispositionEvidenceDigest=D("a")); p[4].append(h)
        self.assertTrue(self.status(m)["canonical"])
    def test_withdrawal_preserves_existence_and_installability(self):
        def m(p): p[5]=withdrawal(p[0])
        s=self.status(m); self.assertTrue(s["exists"]); self.assertTrue(s["installable"]); self.assertFalse(s["canonical"]); self.assertFalse(s["eligibleForNewInstall"]); self.assertFalse(s["discoverableForNewConsumers"])
    def test_future_withdrawal_not_yet_effective(self):
        def m(p): n=withdrawal(p[0]); n["effectiveAt"]="2027-01-01T00:00:00Z"; p[5]=n
        self.assertTrue(self.status(m)["canonical"])
    def test_destructive_withdrawal_rejected(self):
        def m(p): n=withdrawal(p[0]); n["retainsTransitiveClosure"]=False; p[5]=n
        self.invalid(m)
    def test_withdrawal_needs_013_act(self):
        def m(p): n=withdrawal(p[0]); n["registryWithdrawalActRef"]="local:withdraw"; p[5]=n
        self.invalid(m)

if __name__ == "__main__": unittest.main()
