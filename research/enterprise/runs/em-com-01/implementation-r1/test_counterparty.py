import unittest
from copy import deepcopy
from counterparty import Invalid, project_current, validate_profile
from fixtures import D, valid_case
AT="2026-06-01T00:00:00Z"
class ProfileTests(unittest.TestCase):
  def parts(self): return list(valid_case())
  def project(self,mut=None,purpose=None):
    p=self.parts(); mut and mut(p); return project_current(*p,"set-1",AT,purpose)
  def invalid(self,mut):
    with self.assertRaises(Invalid): self.project(mut)
  def test_tri_role_one_party(self): self.assertEqual([x["role"] for x in self.project()["rolesAt"]],["customer","partner","supplier"])
  def test_purpose_projection(self): self.assertEqual(len(self.project(purpose="billing")["contactsFor"]),1)
  def test_wrong_purpose_empty(self): self.assertEqual(self.project(purpose="marketing")["contactsFor"],[])
  def test_duplicate_set_key(self):
    def m(p): x=deepcopy(p[0][0]); x["setId"]="set-2"; p[0].append(x)
    self.invalid(m)
  def test_duplicate_set_id(self):
    def m(p): x=deepcopy(p[0][0]); x["partyRef"]="urn:party:other"; p[0].append(x)
    self.invalid(m)
  def test_observer_is_identity_component(self):
    p=self.parts(); x=deepcopy(p[0][0]); x.update(setId="set-2",observerDimensionRef="urn:dimension:seller-b"); p[0].append(x); self.assertTrue(validate_profile(*p,AT))
  def test_role_does_not_mint_party(self): self.invalid(lambda p:p[1][0].__setitem__("partyRef","urn:party:copy"))
  def test_customer_only_014(self): self.invalid(lambda p:p[1][0].__setitem__("upstreamModel","WM-ORG-015"))
  def test_supplier_only_015(self): self.invalid(lambda p:p[1][1].__setitem__("upstreamModel","WM-ORG-014"))
  def test_partner_only_015(self): self.invalid(lambda p:p[1][2].__setitem__("upstreamModel","WM-ORG-014"))
  def test_dangling_role_set(self): self.invalid(lambda p:p[1][0].__setitem__("setRef","missing"))
  def test_zero_upstream_digest(self): self.invalid(lambda p:p[1][0].__setitem__("upstreamDigest",D("0")))
  def test_missing_upstream_version(self): self.invalid(lambda p:p[1][0].__setitem__("upstreamVersion",""))
  def test_copied_relationship_state(self): self.invalid(lambda p:p[1][0].__setitem__("relationshipState","active"))
  def test_invalid_interval(self): self.invalid(lambda p:p[1][0].__setitem__("validTo","2025-01-01T00:00:00Z"))
  def test_expired_role_absent(self):
    s=self.project(lambda p:p[1][0].__setitem__("validTo","2026-05-01T00:00:00Z")); self.assertNotIn("customer",[x["role"] for x in s["rolesAt"]])
  def test_superseded_role_absent(self):
    def m(p): x=deepcopy(p[1][0]); x.update(bindingId="role-new",upstreamRecordRef="urn:014:customer:new",validFrom="2026-05-01T00:00:00Z"); p[1].append(x); p[1][0]["supersededByRef"]="role-new"
    s=self.project(m); self.assertNotIn("urn:014:customer:acme",[x["upstreamRecordRef"] for x in s["rolesAt"]])
  def test_invalid_scope_kind(self): self.invalid(lambda p:p[2][0].__setitem__("scopeKind","global"))
  def test_group_requires_target(self): self.invalid(lambda p:p[2][0].__setitem__("targetRef",""))
  def test_dangling_scope_set(self): self.invalid(lambda p:p[2][0].__setitem__("setRef","missing"))
  def test_endpoint_model_must_be_per010(self): self.invalid(lambda p:p[3][0].__setitem__("endpointModel","WM-XCT-024"))
  def test_contact_value_smuggling(self): self.invalid(lambda p:p[3][0].__setitem__("contactValue","billing@example.com"))
  def test_contact_consent_smuggling(self): self.invalid(lambda p:p[3][0].__setitem__("consent",True))
  def test_contact_requires_purpose(self): self.invalid(lambda p:p[3][0].__setitem__("purpose",""))
  def test_contact_dangling_role(self): self.invalid(lambda p:p[3][0].__setitem__("roleBindingRef","missing"))
  def test_contact_dangling_scope(self): self.invalid(lambda p:p[3][0].__setitem__("scopeBindingRef","missing"))
  def test_contact_cross_set_rejected(self):
    def m(p): x=deepcopy(p[0][0]); x.update(setId="set-2",partyRef="urn:party:other"); p[0].append(x); p[2][0]["setRef"]="set-2"
    self.invalid(m)
  def test_expired_contact_absent(self):
    s=self.project(lambda p:p[3][0].__setitem__("validTo","2026-05-01T00:00:00Z")); self.assertEqual(s["contactsFor"],[])
  def test_bare_segment_rejected(self): self.invalid(lambda p:p[4][0].__setitem__("schemeRef",""))
  def test_segment_version_required(self): self.invalid(lambda p:p[4][0].__setitem__("schemeVersion",""))
  def test_segment_source_required(self): self.invalid(lambda p:p[4][0].__setitem__("sourceRef",""))
  def test_segment_method_governed(self): self.invalid(lambda p:p[4][0].__setitem__("method","guessed"))
  def test_conflicting_segments_coexist(self):
    def m(p): x=deepcopy(p[4][0]); x.update(assertionId="segment-2",code="watch",sourceRef="urn:credit-desk:2"); p[4].append(x)
    self.assertEqual(len(self.project(m)["segmentsAt"]),2)
  def test_superseded_segment_absent(self):
    def m(p): x=deepcopy(p[4][0]); x.update(assertionId="segment-2",code="standard",supersedesRef="segment-1",assertedAt="2026-04-01T00:00:00Z"); p[4].append(x)
    self.assertEqual([x["code"] for x in self.project(m)["segmentsAt"]],["standard"])
  def test_missing_superseded_segment(self): self.invalid(lambda p:p[4][0].__setitem__("supersedesRef","missing"))
  def test_future_segment_not_current(self):
    s=self.project(lambda p:p[4][0].__setitem__("assertedAt","2027-01-01T00:00:00Z")); self.assertEqual(s["segmentsAt"],[])
  def test_display_cache_must_be_non_authoritative(self): self.invalid(lambda p:p[0][0].__setitem__("displayCache",{"name":"Acme"}))
  def test_empty_display_cache_rejected(self): self.invalid(lambda p:p[0][0].__setitem__("displayCache",{}))
  def test_null_display_cache_rejected(self): self.invalid(lambda p:p[0][0].__setitem__("displayCache",None))
  def test_string_display_cache_rejected(self): self.invalid(lambda p:p[0][0].__setitem__("displayCache","Acme"))
  def test_non_record_input_rejected(self):
    with self.assertRaises(Invalid): validate_profile(["not-a-record"],[],[],[],[],AT)
  def test_explicit_non_authoritative_cache_allowed(self):
    s=self.project(lambda p:p[0][0].__setitem__("displayCache",{"authoritative":False,"values":{"name":"Acme"}})); self.assertEqual(len(s["rolesAt"]),3)
  def test_multi_set_projection_isolated(self):
    p=self.parts(); x=deepcopy(p[0][0]); x.update(setId="set-2",partyRef="urn:party:other"); p[0].append(x); r=deepcopy(p[1][0]); r.update(bindingId="role-other",setRef="set-2",upstreamRecordRef="urn:014:customer:other"); p[1].append(r); out=project_current(*p,"set-1",AT); self.assertNotIn("role-other",[x["bindingId"] for x in out["rolesAt"]]); self.assertEqual(out["provenance"]["partyRef"],"urn:party:acme")
  def test_self_segment_supersession_rejected(self): self.invalid(lambda p:p[4][0].__setitem__("supersedesRef","segment-1"))
  def test_dangling_role_supersession_rejected(self): self.invalid(lambda p:p[1][0].__setitem__("supersededByRef","missing"))
  def test_strict_time_offset(self): self.invalid(lambda p:p[1][0].__setitem__("validFrom","2026-01-01T00:00:00"))
  def test_projection_has_provenance(self): self.assertEqual(self.project()["provenance"]["profile"],"EM-COM-01")
if __name__=="__main__": unittest.main()
