import copy,datetime,json,unittest
from pathlib import Path
import identity_profile as p
HERE=Path(__file__).resolve().parent
class IdentityTests(unittest.TestCase):
 def setUp(self):
  self.policy=p.load(HERE/'examples/policy.json');self.rows=p.load(HERE/'examples/startup.json');self.a=copy.deepcopy(self.rows[0])
 def query(self,rows=None,**kw):
  defaults={'valid_at':'2026-01-01T00:00:00Z','known_at':'2026-01-01T00:00:00Z','evaluation_at':'2026-09-21T00:00:00Z','reader':'urn:synthetic:actor:steward','purpose':self.policy['purpose']};defaults.update(kw)
  return p.resolve(rows if rows is not None else self.rows,{k:self.a['binding'][k] for k in ['scheme','schemeVersion','issuer','scope','value']},self.policy,**defaults)
 def append(self,a,state='retracted',recorded='2025-08-01T00:00:00Z',effective='2025-02-01T00:00:00Z'):
  e=copy.deepcopy(a['history'][-1]);e.update(id=e['id']+':next',previousDigest=p.digest(a['history'][-1]),state=state,recordedAt=recorded,effectiveAt=effective);a['history'].append(e);return a
 def invalid(self,a):
  with self.assertRaises(p.Invalid):p.validate(a,self.policy)
 def seal(self,a):
  previous=None
  for e in a['history']:
   e['previousDigest']=p.digest(previous) if previous else p.claim_digest(a);previous=e
  return a
 def other(self):
  b=copy.deepcopy(self.a);b['id']+=':other'
  for e in b['history']:e['id']+=':other'
  return self.seal(b)
 def test_three_profiles(self):
  for n in ['startup','group','ai-team']:p.validate_set(p.load(HERE/('examples/'+n+'.json')),self.policy)
 def test_three_person_references_one_subject(self):
  for a in self.rows:
   self.a=a;r=self.query();self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['targets'],['urn:synthetic:subject:person:p1']);self.assertFalse(r['grantsAccess'])
 def test_equal_authority_conflict(self):
  b=self.other();b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['status'],'contested')
 def test_negative_conflict(self):
  b=self.other();b['relation']='not-same-assertion';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['status'],'contested')
 def test_negative_only_not_silently_absent(self):
  self.a['relation']='not-same-assertion';r=self.query([self.seal(self.a)]);self.assertEqual(r['status'],'denied-in-input');self.assertEqual(r['opposing'],[self.a['id']])
 def test_candidate_inert(self):
  self.a['relation']='probable-entity-match';self.a['history']=self.a['history'][:1];self.assertEqual(self.query([self.seal(self.a)])['status'],'candidate')
 def test_candidate_cannot_activate(self):self.a['relation']='probable-entity-match';self.invalid(self.a)
 def test_email_evidence_not_sufficient(self):
  self.a['history'][1]['evidence']=[{'ref':'urn:synthetic:email','kind':'email-match','description':'Same mailbox'}];self.invalid(self.a)
 def test_unknown_no_claim(self):self.assertEqual(self.query([])['status'],'unknown')
 def test_account_person_refused(self):self.a['binding']['kind']='user-account';self.invalid(self.a)
 def test_service_account_person_refused(self):self.a['binding']['kind']='service-account';self.invalid(self.a)
 def test_retract_history(self):
  later=self.append(copy.deepcopy(self.a));self.assertEqual(self.query([later])['status'],'unknown');self.assertEqual(self.query([later],known_at='2025-06-01T00:00:00Z')['status'],'accepted-in-input')
 def test_bitemporal_effective_date(self):
  later=self.append(copy.deepcopy(self.a));self.assertEqual(self.query([later],valid_at='2025-01-15T00:00:00Z')['status'],'accepted-in-input')
 def test_history_preserved_after_append(self):
  old=self.query([self.a],known_at='2025-06-01T00:00:00Z');new=self.query([self.append(copy.deepcopy(self.a))],known_at='2025-06-01T00:00:00Z')
  for k in ['status','targets','supporting','opposing','excluded']:self.assertEqual(old[k],new[k])
 def test_retracted_terminal(self):self.append(self.a);self.append(self.a,'asserted','2025-09-01T00:00:00Z');self.invalid(self.a)
 def test_disputed_blocks_resolution(self):self.append(self.a,'disputed');self.assertEqual(self.query([self.a])['status'],'contested')
 def test_predecessor_tamper(self):self.a['history'][1]['previousDigest']='sha256:'+'0'*64;self.invalid(self.a)
 def test_event_order(self):self.a['history'][1]['recordedAt']=self.a['history'][0]['recordedAt'];self.invalid(self.a)
 def test_actor_cannot_assert(self):self.a['history'][1]['actor']='urn:synthetic:actor:importer';self.invalid(self.a)
 def test_expired_authority(self):self.a['history'][1]['recordedAt']='2028-01-01T00:00:00Z';self.invalid(self.a)
 def test_policy_tamper(self):self.policy['purpose']='different';self.invalid(self.a)
 def test_wrong_dimension(self):self.a['dimension']='urn:other:dimension';self.invalid(self.a)
 def test_cross_dimension_target(self):self.a['target']['id']='urn:other:subject:p1';self.invalid(self.a)
 def test_issuer_scope_isolation(self):
  b=self.other();b['binding']['assignmentId']+=':other';b['binding']['scope']='urn:synthetic:tenant:other';b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['targets'],[self.a['target']['id']])
 def test_reassignment_temporal(self):
  rows=p.load(HERE/'examples/group.json');self.a=rows[0];self.assertEqual(self.query(rows,valid_at='2025-03-01T00:00:00Z')['targets'],['urn:synthetic:subject:person:pa']);self.assertEqual(self.query(rows,valid_at='2025-10-01T00:00:00Z')['targets'],['urn:synthetic:subject:person:pc'])
 def test_overlapping_reassignments_contested(self):
  b=self.other();b['binding']['assignmentId']+=':new';b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['status'],'contested')
 def test_qualified_assignment_not_overwritten(self):
  b=self.other();b['binding']['value']='different'
  with self.assertRaises(p.Invalid):p.validate_set([self.a,b],self.policy)
 def test_missing_qualification(self):del self.a['binding']['issuer'];self.invalid(self.a)
 def test_normalization_refused(self):self.a['binding']['comparison']='lowercase';self.invalid(self.a)
 def test_value_case_preserved(self):
  b=self.other();b['binding']['assignmentId']+=':new';b['binding']['value']='e7';b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['targets'],[self.a['target']['id']])
 def test_same_as_refused(self):self.a['relation']='owl:sameAs';self.invalid(self.a)
 def test_closure_refused(self):self.a['inferencePermitted']=True;self.invalid(self.a)
 def test_unknown_time_not_epoch(self):self.a['binding']['validFrom']=None;self.invalid(self.a)
 def test_interval_bounds(self):self.a['validTo']=self.a['validFrom'];self.invalid(self.a)
 def test_assignment_bounds(self):self.a['binding']['validTo']='2025-02-01T00:00:00Z';self.invalid(self.a)
 def test_read_denied(self):
  with self.assertRaises(p.Invalid):self.query(reader='urn:synthetic:actor:intruder')
 def test_current_authority_expiry(self):
  with self.assertRaises(p.Invalid):self.query(evaluation_at='2028-01-01T00:00:00Z')
 def test_future_knowledge_refused(self):
  with self.assertRaises(p.Invalid):self.query(known_at='2027-01-01T00:00:00Z')
 def test_replay_noop(self):self.assertEqual(p.import_assertion(self.rows,self.a,self.policy,now='2026-09-21T00:00:00Z'),self.rows)
 def test_history_extension(self):
  new=self.append(copy.deepcopy(self.a));out=p.import_assertion(self.rows,new,self.policy,now=new['history'][-1]['recordedAt']);self.assertEqual(out[0],new);self.assertEqual(len(self.rows[0]['history']),2)
 def test_history_truncation_refused(self):
  a=copy.deepcopy(self.a);a['history']=a['history'][:1]
  with self.assertRaises(p.Invalid):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_endpoint_change_refused(self):
  b=self.append(copy.deepcopy(self.a));b['target']['id']='urn:synthetic:subject:person:p2'
  with self.assertRaises(p.Invalid):p.import_assertion(self.rows,b,self.policy,now='2026-09-21T00:00:00Z')
 def test_round_trip(self):self.assertEqual(json.loads(p.encode(self.rows)),self.rows)
 def test_lossy_round_trip_refused(self):del self.a['binding']['sourceRecord'];self.invalid(self.a)
 def test_unknown_version_refused(self):self.a['version']='9';self.invalid(self.a)
 def test_undeclared_field_refused(self):self.a['resolutionStatus']='accepted';self.invalid(self.a)
 def test_policy_no_self_grant(self):self.a['policy']={'allow':True};self.invalid(self.a)
 def test_duplicate_event_id_refused(self):
  b=self.other();b['history'][0]['id']=self.a['history'][0]['id'];b['history'][1]['previousDigest']=p.digest(b['history'][0])
  with self.assertRaises(p.Invalid):p.validate_set([self.a,b],self.policy)


 def test_empty_set_invalid_policy(self):
  self.policy['readers']='urn:synthetic:actor:steward'
  with self.assertRaises(p.Invalid):self.query([])
 def test_empty_set_duplicate_actor(self):
  self.policy['actors'].append(copy.deepcopy(self.policy['actors'][0]))
  with self.assertRaises(p.Invalid):p.validate_set([],self.policy)
 def test_retagging_both_kinds_refused(self):
  self.a['binding']['kind']=self.a['target']['kind']='service-account';self.a['target']['id']='urn:synthetic:subject:service-account:bot';self.invalid(self.a)
 def test_unregistered_scheme_version_refused(self):self.a['binding']['schemeVersion']='2';self.invalid(self.a)
 def test_target_kind_namespace_refused(self):self.a['target']['id']='urn:synthetic:subject:service-account:bot';self.invalid(self.a)
 def test_dot_segment_refused(self):self.a['target']['id']='urn:synthetic:subject:person:a/../b';self.invalid(self.a)
 def test_percent_encoded_namespace_refused(self):self.a['target']['id']='urn:synthetic:subject:person:%2e%2e/other';self.invalid(self.a)
 def test_prefix_near_miss_refused(self):self.a['target']['id']='urn:synthetic:subject:personality:p1';self.invalid(self.a)
 def test_effective_after_window_refused(self):
  self.a['validTo']='2025-07-01T00:00:00Z';self.append(self.a,effective='2025-08-01T00:00:00Z');self.invalid(self.a)
 def test_effective_at_exclusive_end_refused(self):
  self.a['validTo']='2025-08-01T00:00:00Z';self.append(self.a,effective='2025-08-01T00:00:00Z');self.invalid(self.a)
 def test_not_yet_known_has_reason(self):
  r=self.query([self.a],known_at='2024-01-01T00:00:00Z');self.assertEqual(r['status'],'unknown');self.assertEqual(r['excluded'][0]['reason'],'not-effective-or-known')
 def test_positive_with_different_negative(self):
  b=self.other();b['target']['id']='urn:synthetic:subject:person:p2';b['relation']='not-same-assertion';r=self.query([self.seal(self.a),self.seal(b)]);self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['opposing'],[b['id']])
 def test_independent_identical_claims_retained(self):
  b=self.other();r=self.query([self.seal(self.a),self.seal(b)]);self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(len(r['supporting']),2)
 def test_source_evidence_matches_assignment(self):
  self.a['history'][1]['evidence'][0]['ref']='urn:synthetic:wrong-source';self.invalid(self.a)
 def test_backdated_correction_supersedes_later_effect(self):
  self.a['history'][1]['effectiveAt']='2025-06-01T00:00:00Z';self.a['history'][1]['recordedAt']='2025-06-02T00:00:00Z'
  corrected=self.append(copy.deepcopy(self.a),effective='2025-01-01T00:00:00Z')
  self.assertEqual(self.query([corrected],valid_at='2025-06-15T00:00:00Z')['status'],'unknown')
  self.assertEqual(self.query([corrected],valid_at='2025-06-15T00:00:00Z',known_at='2025-06-15T00:00:00Z')['status'],'accepted-in-input')


 def test_backdated_import_refused(self):
  a=self.append(copy.deepcopy(self.a),recorded='2025-01-02T00:00:00Z',effective='2025-01-01T00:00:00Z')
  with self.assertRaisesRegex(p.Invalid,'trusted receipt'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_future_import_refused(self):
  a=self.append(copy.deepcopy(self.a),'disputed',recorded='2026-12-01T00:00:00Z',effective='2026-12-01T00:00:00Z')
  with self.assertRaisesRegex(p.Invalid,'trusted receipt'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_new_claim_backdating_refused(self):
  a=self.other();a['history']=a['history'][:1]
  with self.assertRaisesRegex(p.Invalid,'trusted receipt'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_live_proposal_import(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0]['recordedAt']='2026-09-21T00:00:00Z'
  self.assertEqual(len(p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')),4)
 def test_receipt_must_exceed_global_head(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0]['recordedAt']=self.rows[0]['history'][-1]['recordedAt']
  with self.assertRaisesRegex(p.Invalid,'import head'):p.import_assertion(self.rows,a,self.policy,now=a['history'][0]['recordedAt'])
 def test_disputed_candidate_cannot_veto(self):
  b=self.other();b['relation']='probable-entity-match';b['history']=b['history'][:1];self.seal(b);self.append(b,'disputed')
  r=self.query([self.a,b]);self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['candidateDisputes'],[b['id']])
 def test_proposed_negative_is_not_positive_candidate(self):
  b=self.other();b['relation']='not-same-assertion';b['history']=b['history'][:1];self.seal(b)
  r=self.query([b]);self.assertEqual(r['status'],'proposal-only');self.assertEqual(r['candidates'],[]);self.assertEqual(r['negativeProposals'],[b['id']])
 def test_assignment_identity_is_issuer_qualified(self):
  rows=copy.deepcopy(self.rows);rows[1]['binding']['assignmentId']=rows[0]['binding']['assignmentId'];self.seal(rows[1]);p.validate_set(rows,self.policy)
 def test_empty_local_suffix_refused(self):self.a['target']['id']='urn:synthetic:subject:person:';self.invalid(self.a)
 def test_unicode_timestamp_refused(self):
  with self.assertRaises(p.Invalid):p.stamp('２０２５-01-01T00:00:00Z')
 def test_genesis_commits_claim(self):
  self.a['target']['id']='urn:synthetic:subject:person:p2'
  with self.assertRaisesRegex(p.Invalid,'predecessor'):p.validate(self.a,self.policy)
 def test_unresolved_endpoint_cannot_activate(self):
  self.a['endpointResolution']['source']='unresolved';self.seal(self.a)
  with self.assertRaisesRegex(p.Invalid,'resolved endpoint'):p.validate(self.a,self.policy)
 def test_restricted_data_denied_by_synthetic_policy(self):
  self.a['binding']['personalDataClass']='restricted'
  with self.assertRaisesRegex(p.Invalid,'classification'):p.validate(self.a,self.policy)
 def test_lone_surrogate_encode_refused(self):
  with self.assertRaises(p.Invalid):p.encode({'reason':chr(0xd800)})
 def test_duplicate_json_member_refused(self):
  import tempfile
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/'duplicate.json';path.write_text('{"x":1,"x":2}')
   with self.assertRaisesRegex(p.Invalid,'duplicate JSON'):p.load(path)


 def test_latest_reason_surrogate_rejected_at_import(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0].update(recordedAt='2026-09-21T00:00:00Z',actor='urn:synthetic:actor:importer',reason='x'+chr(0xd800))
  with self.assertRaisesRegex(p.Invalid,'canonically encoded'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_latest_evidence_surrogate_rejected_at_import(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0]['recordedAt']='2026-09-21T00:00:00Z';a['history'][0]['evidence'][0]['description']='x'+chr(0xd800)
  with self.assertRaisesRegex(p.Invalid,'canonically encoded'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_proposal_cannot_squat_assignment(self):
  s=self.other();s['history']=s['history'][:1];s['binding']['assignmentId']='urn:synthetic:assignment:hr-9';s['binding']['value']='bogus';s['history'][0].update(recordedAt='2026-09-21T00:00:00Z',actor='urn:synthetic:actor:importer');self.seal(s)
  rows=p.import_assertion(self.rows,s,self.policy,now='2026-09-21T00:00:00Z')
  g=self.other();g['id']+=':genuine';g['binding']['assignmentId']=s['binding']['assignmentId'];g['binding']['value']='E9';g['history']=g['history'][:1];g['history'][0].update(id=g['history'][0]['id']+':genuine',recordedAt='2026-09-22T00:00:00Z');self.seal(g)
  rows=p.import_assertion(rows,g,self.policy,now='2026-09-22T00:00:00Z')
  active=self.append(g,'asserted',recorded='2026-09-23T00:00:00Z',effective='2026-09-22T00:00:00Z')
  rows=p.import_assertion(rows,active,self.policy,now='2026-09-23T00:00:00Z');self.a=active
  r=self.query(rows,valid_at='2026-09-24T00:00:00Z',known_at='2026-09-24T00:00:00Z',evaluation_at='2026-09-24T00:00:00Z');self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(len(r['retainedObservationConflicts']),1)
 def test_retraction_releases_observation_reservation(self):
  old=self.append(copy.deepcopy(self.a));g=self.other();g['binding']['value']='E9';self.seal(g);p.validate_set([old,g],self.policy)
 def test_active_observation_conflict_still_rejected(self):
  g=self.other();g['binding']['value']='E9';self.seal(g)
  with self.assertRaisesRegex(p.Invalid,'active asserted assignment'):p.validate_set([self.a,g],self.policy)
 def test_dispute_prior_must_be_effective_at_query(self):
  b=self.other();b['history'][1].update(effectiveAt='2025-06-01T00:00:00Z',recordedAt='2025-06-02T00:00:00Z');self.seal(b);self.append(b,'disputed','2025-07-01T00:00:00Z','2025-02-01T00:00:00Z')
  r=self.query([self.a,b],valid_at='2025-03-01T00:00:00Z',known_at='2025-08-01T00:00:00Z');self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['candidateDisputes'],[b['id']])
 def test_space_in_subject_uri_rejected_by_format(self):
  self.a['target']['id']='urn:synthetic:subject:person:p1 extra'
  with self.assertRaisesRegex(p.Invalid,'SCHEMA'):p.validate(self.a,self.policy)
 def test_nonascii_separator_in_uri_rejected_by_format(self):
  self.a['target']['id']='urn:synthetic:subject:person:p1'+chr(0xff0f)+'p2'
  with self.assertRaisesRegex(p.Invalid,'SCHEMA'):p.validate(self.a,self.policy)
 def test_resealed_endpoint_change_rejected_at_import(self):
  a=self.append(copy.deepcopy(self.a));a['target']['id']='urn:synthetic:subject:person:p2';self.seal(a)
  with self.assertRaisesRegex(p.Invalid,'claim-bearing content changed'):p.import_assertion(self.rows,a,self.policy,now=a['history'][-1]['recordedAt'])

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(IdentityTests))
 (HERE/'test-results.json').write_text(json.dumps({'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sourceDigests':{str(x.relative_to(HERE)):__import__('hashlib').sha256(x.read_bytes()).hexdigest() for x in [HERE/'identity_profile.py',HERE/'identity-profile.schema.json',Path(__file__),*sorted((HERE/'examples').glob('*.json'))]},'tests':result.testsRun,'passed':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors)},indent=2)+'\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)
