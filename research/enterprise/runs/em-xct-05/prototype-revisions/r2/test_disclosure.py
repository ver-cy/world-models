import copy,hashlib,json,unittest,sys,importlib.metadata
from pathlib import Path
import disclosure as d

def p(name,rev='1'):
    return {'id':'urn:synthetic:'+name,'revision':rev,'digest':'sha256:'+hashlib.sha256((name+rev).encode()).hexdigest()}

def fixture(profile='startup'):
    member={'key':'project-name','source':p('project'),'schema':p('project-schema'),'shape':p('name-only-shape'),
            'fields':[{'name':'name','kind':'string','classificationBindings':[p('name-classification')]}]}
    members=[member]
    if profile=='matrix':
        member['key']='group-summary';member['source']=p('group-aggregate');member['fields'][0]['name']='headcount';member['fields'][0]['kind']='integer'
        member['schema']=p('headcount-schema');member['shape']=p('headcount-summary-shape');member['fields'][0]['classificationBindings']=[p('headcount-classification')]
        other=copy.deepcopy(member);other['key']='unit-summary';other['source']=p('unit-aggregate');members.append(other)
    if profile=='ai':
        member['key']='release-notes';member['source']=p('model-release');member['fields'][0]['name']='releaseNotes'
        member['schema']=p('release-notes-schema');member['shape']=p('release-notes-shape');member['fields'][0]['classificationBindings']=[p('release-notes-classification')]
    proposal=d.seal({'format':'vercy-disclosure-research','version':d.VERSION,'type':'proposal','dimension':'urn:synthetic:dimension:'+profile,'id':'urn:synthetic:proposal:'+profile,'revision':'1',
       'body':{'author':'urn:synthetic:founder','capturedAt':'2026-09-21T10:00:00Z','audience':p('partner'),'purpose':p('release-briefing'),'environment':p('partner-portal'),'priorReleases':p('known-prior-release-context'),'custodyContext':p('custody-instructions'),'members':members}})
    review=d.seal({'format':'vercy-disclosure-research','version':d.VERSION,'type':'review','dimension':proposal['dimension'],'id':'urn:synthetic:review:'+profile,'revision':'1',
       'body':{'proposal':d.pin(proposal),'reviewer':'urn:synthetic:reviewer','authority':p('review-authority'),'method':p('bounded-manual-review'),'evidence':[p('synthetic-assessment')],'reviewedAt':'2026-09-21T10:01:00Z','validFrom':'2026-09-21T10:01:00Z','validTo':'2026-09-22T10:01:00Z','verdict':'cleared','residualRisk':'Synthetic scenario only. No claim of inference prevention.','supersedes':None}})
    if profile=='matrix':
        review['body']['verdict']='rejected';review['body']['residualRisk']='Synthetic reviewer identifies a subtraction path between group and unit headcounts exposing an individual indicator. This package is rejected. The validator does not calculate that risk.';review=d.seal(review)
    snapshot={'dimension':proposal['dimension'],'proposal':d.pin(proposal),'context':{k:copy.deepcopy(proposal['body'][k]) for k in ('audience','purpose','environment','priorReleases','custodyContext')},'members':copy.deepcopy(members),'proposalAuthors':['urn:synthetic:founder'],'reviewers':['urn:synthetic:reviewer','urn:synthetic:founder'],'authority':p('review-authority'),'activeReviews':[d.pin(review)],'withdrawnReviews':[],'separateReviewer':profile!='startup'}
    cap={'dimension':proposal['dimension'],'inspect':True,'record':True}
    return proposal,review,snapshot,cap

class ResearchPrototype(unittest.TestCase):
    def setUp(self):self.p,self.r,self.s,self.c=fixture();self.now='2026-09-21T12:00:00Z'
    def answer(self,**kw):return d.inspect(kw.get('proposal',self.p),kw.get('reviews',[self.r]),kw.get('snapshot',self.s),kw.get('capability',self.c),kw.get('now',self.now))
    def reseal_review(self):self.r=d.seal(self.r);self.s['activeReviews']=[d.pin(self.r)]
    def test_three_profiles(self):
        for profile in ('startup','matrix','ai'):
            with self.subTest(profile=profile):
                a,b,s,c=fixture(profile);self.assertEqual(d.inspect(a,[b],s,c,self.now)['status'],'rejected' if profile=='matrix' else 'applicable-review')
    def test_clearance_explicitly_not_authorization(self):self.assertIs(self.answer()['notServingAuthorization'],True)
    def test_startup_explicit_self_review(self):
        self.r['body']['reviewer']=self.p['body']['author'];self.reseal_review();self.assertEqual(self.answer()['status'],'applicable-review')
    def test_segregated_profile_refuses_self_review(self):
        self.s['separateReviewer']=True;self.r['body']['reviewer']=self.p['body']['author'];self.reseal_review();self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_revoked_reviewer(self):self.s['reviewers']=[];self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_revoked_author(self):self.s['proposalAuthors']=[];self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_changed_authority(self):self.s['authority']=p('review-authority','2');self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_withdrawn_clearance(self):self.s['withdrawnReviews']=[d.pin(self.r)];self.s['activeReviews']=[];self.assertEqual(self.answer(reviews=[])['status'],'insufficient-context')
    def test_future_review(self):self.assertEqual(self.answer(now='2026-09-21T10:00:30Z')['status'],'insufficient-context')
    def test_expiry_is_exclusive(self):self.assertEqual(self.answer(now=self.r['body']['validTo'])['status'],'insufficient-context')
    def test_start_is_inclusive(self):self.assertEqual(self.answer(now=self.r['body']['validFrom'])['status'],'applicable-review')
    def test_future_capture(self):self.assertEqual(self.answer(now='2026-09-20T10:00:00Z')['status'],'stale')
    def test_context_drift(self):
        for k in self.s['context']:
            with self.subTest(key=k):
                s=copy.deepcopy(self.s);s['context'][k]=p(k,'changed');self.assertEqual(self.answer(snapshot=s)['status'],'stale')
    def test_source_schema_shape_classification_drift(self):
        for k in ('source','schema','shape'):
            with self.subTest(key=k):
                s=copy.deepcopy(self.s);s['members'][0][k]=p(k,'2');self.assertEqual(self.answer(snapshot=s)['status'],'stale')
        self.s['members'][0]['fields'][0]['classificationBindings']=[p('binding','2')];self.assertEqual(self.answer()['status'],'stale')
    def test_added_member_needs_new_review(self):
        m=copy.deepcopy(self.p['body']['members'][0]);m['key']='another';self.p['body']['members'].append(m);self.p=d.seal(self.p);self.s['members']=self.p['body']['members']
        self.s['proposal']=d.pin(self.p)
        with self.assertRaisesRegex(d.Invalid,'review points to another proposal'):self.answer()
    def test_added_field_needs_new_review(self):
        f={'name':'budget','kind':'number','classificationBindings':[p('budget-binding')]};self.p['body']['members'][0]['fields'].append(f);self.p=d.seal(self.p);self.s['members']=self.p['body']['members']
        self.s['proposal']=d.pin(self.p)
        with self.assertRaisesRegex(d.Invalid,'review points to another proposal'):self.answer()
    def test_reordered_members_changes_pin(self):
        a,b,s,c=fixture('matrix');a['body']['members'].reverse();a=d.seal(a);s['members']=a['body']['members']
        s['proposal']=d.pin(a)
        with self.assertRaisesRegex(d.Invalid,'review points to another proposal'):d.inspect(a,[b],s,c,self.now)
    def test_current_unknown_member(self):self.s['members']=[];self.assertEqual(self.answer()['status'],'stale')
    def test_hidden_review_not_ignored(self):self.s['activeReviews'].append(p('hidden-review'));self.assertEqual(self.answer()['status'],'insufficient-context')
    def test_empty_review_set_is_not_clearance(self):self.s['activeReviews']=[];self.assertEqual(self.answer(reviews=[])['status'],'insufficient-context')
    def test_conflicting_active_reviews(self):
        other=copy.deepcopy(self.r);other['id']='urn:synthetic:other-review';other['body']['verdict']='rejected';other=d.seal(other);self.s['activeReviews'].append(d.pin(other));self.assertEqual(self.answer(reviews=[self.r,other])['status'],'conflict')
    def test_inconclusive_is_not_clearance(self):self.r['body']['verdict']='inconclusive';self.reseal_review();self.assertEqual(self.answer()['status'],'inconclusive')
    def test_rejection_is_not_clearance(self):self.r['body']['verdict']='rejected';self.reseal_review();self.assertEqual(self.answer()['status'],'rejected')
    def test_missing_capability_before_record_diagnostics(self):
        with self.assertRaisesRegex(d.Unauthorized,'^unavailable$'):self.answer(proposal={'bad':True},capability={})
    def test_cross_dimension_capability(self):
        self.c['dimension']='urn:synthetic:other'
        with self.assertRaises(d.Unauthorized):self.answer()
    def test_cross_dimension_review(self):
        self.r['dimension']='urn:synthetic:other';self.reseal_review()
        with self.assertRaises(d.Invalid):self.answer()
    def test_pre_capture_review(self):
        self.r['body']['reviewedAt']='2026-09-21T09:59:59Z';self.reseal_review()
        with self.assertRaises(d.Invalid):self.answer()
    def test_zero_validity_interval(self):
        self.r['body']['validTo']=self.r['body']['validFrom']
        with self.assertRaises(d.Invalid):d.seal(self.r)
    def test_invalid_calendar_date(self):
        self.p['body']['capturedAt']='2026-02-30T00:00:00Z'
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_missing_offset(self):
        with self.assertRaises(d.Invalid):self.answer(now='2026-09-21T12:00:00')
    def test_tampered_digest(self):
        self.p['body']['author']='urn:synthetic:someone'
        with self.assertRaisesRegex(d.Invalid,'digest'):d.validate(self.p)
    def test_no_payload_field(self):
        self.p['body']['members'][0]['values']={'budget':100}
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_no_nested_or_wildcard_fields(self):
        for name in ('owner.email','*','/notes/title','notes[0]'):
            with self.subTest(name=name):
                x=copy.deepcopy(self.p);x['body']['members'][0]['fields'][0]['name']=name
                with self.assertRaises(d.Invalid):d.seal(x)
    def test_no_object_or_array_kind(self):
        for kind in ('object','array'):
            with self.subTest(kind=kind):
                x=copy.deepcopy(self.p);x['body']['members'][0]['fields'][0]['kind']=kind
                with self.assertRaises(d.Invalid):d.seal(x)
    def test_missing_classification_not_public(self):
        self.p['body']['members'][0]['fields'][0]['classificationBindings']=[]
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_two_classification_schemes_representable(self):
        self.p['body']['members'][0]['fields'][0]['classificationBindings'].append(p('second-scheme-binding'));d.seal(self.p)
    def test_duplicate_field_rejected(self):
        f=copy.deepcopy(self.p['body']['members'][0]['fields'][0]);f['kind']='integer';self.p['body']['members'][0]['fields'].append(f)
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_duplicate_member_key(self):
        m=copy.deepcopy(self.p['body']['members'][0]);m['source']=p('different');self.p['body']['members'].append(m)
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_same_binding_revision_conflict(self):
        f=self.p['body']['members'][0]['fields'][0];other=copy.deepcopy(f['classificationBindings'][0]);other['digest']='sha256:'+'0'*64;f['classificationBindings'].append(other)
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_duplicate_json_keys(self):
        with self.assertRaises(d.Invalid):d.load(b'{"a":1,"a":2}')
    def test_float_and_nonfinite_json(self):
        for raw in (b'{"a":1.0}',b'{"a":NaN}',b'{"a":Infinity}'):
            with self.assertRaises(d.Invalid):d.load(raw)
    def test_roundtrip(self):self.assertEqual(d.load(d.canonical(self.p)),self.p)
    def test_unsupported_version(self):
        self.p['version']='0.0.0-prototype.1'
        with self.assertRaises(d.Invalid):d.seal(self.p)
    def test_idempotent_import(self):
        existing=d.import_records([],[self.p,self.r],self.p['dimension'],self.c);again=d.import_records(existing,[self.p,self.r],self.p['dimension'],self.c);self.assertEqual(existing,again)
    def test_immutable_revision_conflict_transactional(self):
        x=copy.deepcopy(self.p);x['body']['purpose']=p('other');x=d.seal(x);existing=[self.p]
        with self.assertRaises(d.Invalid):d.import_records(existing,[x],self.p['dimension'],self.c)
        self.assertEqual(existing,[self.p])
    def test_correction_preserves_history(self):
        x=copy.deepcopy(self.p);x['revision']='2';x['body']['purpose']=p('new-purpose');x=d.seal(x);result=d.import_records([self.p],[x],self.p['dimension'],self.c);self.assertEqual(len(result),2)
    def test_import_needs_write_assertion(self):
        self.c['record']=False
        with self.assertRaises(d.Unauthorized):d.import_records([],[self.p],self.p['dimension'],self.c)
    def test_identity_cannot_change_type(self):
        self.r['id']=self.p['id'];self.r['revision']='2';self.r=d.seal(self.r)
        with self.assertRaises(d.Invalid):d.import_records([self.p],[self.r],self.p['dimension'],self.c)
    def test_actor_catalog_cannot_be_substring(self):
        self.s['reviewers']='urn:synthetic:reviewer-extra'
        with self.assertRaises(d.Invalid):self.answer()
    def test_duplicate_reviews_not_votes(self):
        with self.assertRaises(d.Invalid):self.answer(reviews=[self.r,self.r])
    def test_input_bound(self):
        with self.assertRaises(d.Invalid):d.load(b' '*262145)
    def test_missing_dimension_cannot_authorize(self):
        for snapshot in (None,{}):
            with self.assertRaisesRegex(d.Unauthorized,'^unavailable$'):self.answer(proposal={'bad':True},snapshot=snapshot,capability={'inspect':True})
    def test_newline_field_alias(self):
        f=copy.deepcopy(self.p['body']['members'][0]['fields'][0]);f['name']='name\n';self.p['body']['members'][0]['fields'].append(f)
        with self.assertRaisesRegex(d.Invalid,'exact identifier syntax'):d.seal(self.p)
    def test_hidden_identity_characters(self):
        for char in ('\n','\u200b','\u202e','\x00','\ufeff'):
            with self.subTest(char=repr(char)):
                x=copy.deepcopy(self.p);x['id']+=char
                with self.assertRaises(d.Invalid):d.seal(x)
    def test_unpinned_current_proposal_not_applicable(self):
        self.s['proposal']=p('retired-proposal');self.assertEqual(self.answer()['reason'],'current-proposal-differs')
    def test_missing_proposal_pin_rejected(self):
        del self.s['proposal']
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()
    def test_self_supersession_different_digest(self):
        self.r['body']['supersedes']={'id':self.r['id'],'revision':self.r['revision'],'digest':'sha256:'+'0'*64}
        with self.assertRaisesRegex(d.Invalid,'self supersession'):d.seal(self.r)
    def test_active_superseded_review_rejected(self):
        other=copy.deepcopy(self.r);other['id']='urn:synthetic:replacement';other['body']['supersedes']=d.pin(self.r);other=d.seal(other);self.s['activeReviews'].append(d.pin(other))
        with self.assertRaisesRegex(d.Invalid,'superseded review still active'):self.answer(reviews=[self.r,other])
    def test_active_withdrawn_overlap_rejected(self):
        self.s['withdrawnReviews']=[d.pin(self.r)]
        with self.assertRaisesRegex(d.Invalid,'active and withdrawn overlap'):self.answer()
    def test_predate_checked_even_without_authority(self):
        self.r['body']['reviewedAt']='2026-09-21T09:59:59Z';self.reseal_review();self.s['reviewers']=[]
        with self.assertRaisesRegex(d.Invalid,'review predates proposal'):self.answer()
    def test_reference_revision_coherence(self):
        m=copy.deepcopy(self.p['body']['members'][0]);m['key']='other';m['source']['revision']='2';self.p['body']['members'].append(m)
        with self.assertRaisesRegex(d.Invalid,'incoherent reference pin'):d.seal(self.p)
    def test_binding_revision_coherence(self):
        field=self.p['body']['members'][0]['fields'][0];other=copy.deepcopy(field['classificationBindings'][0]);other['revision']='2';field['classificationBindings'].append(other)
        with self.assertRaisesRegex(d.Invalid,'incoherent reference pin'):d.seal(self.p)
    def test_expired_negative_preserved_in_report(self):
        other=copy.deepcopy(self.r);other['id']='urn:synthetic:expired-negative';other['body']['verdict']='rejected';other['body']['validTo']='2026-09-21T11:00:00Z';other=d.seal(other);self.s['activeReviews'].append(d.pin(other));a=self.answer(reviews=[self.r,other]);self.assertEqual(a['status'],'applicable-review');self.assertEqual(a['ignored'],[{'pin':d.pin(other),'verdict':'rejected','reason':'outside-window'}]);self.assertEqual(a['counted'],[d.pin(self.r)])
    def test_answer_binds_inputs(self):
        a=self.answer();self.assertEqual(a['proposal'],d.pin(self.p));self.assertEqual(a['snapshotDigest'],'sha256:'+hashlib.sha256(d.canonical(self.s)).hexdigest());self.assertEqual(a['at'],self.now)
    def test_multiple_active_revisions_rejected(self):
        other=copy.deepcopy(self.r);other['revision']='2';other=d.seal(other);self.s['activeReviews'].append(d.pin(other))
        with self.assertRaisesRegex(d.Invalid,'multiple active revisions'):self.answer(reviews=[self.r,other])
    def test_invalid_utf8(self):
        with self.assertRaisesRegex(d.Invalid,'JSON'):d.load(b'{"x":"\xff"}')
    def test_huge_integer(self):
        with self.assertRaisesRegex(d.Invalid,'integer'):d.load(b'{"x":'+b'1'*5000+b'}')
    def test_year_before_1000_platform_independent(self):self.assertEqual(d.instant('0999-01-01T00:00:00Z').year,999)
    def test_leap_second_refused(self):
        with self.assertRaisesRegex(d.Invalid,'timestamp'):d.instant('2026-12-31T23:59:60Z')
    def test_exponent_number_refused(self):
        with self.assertRaisesRegex(d.Invalid,'non-integer number'):d.load(b'{"x":1e2}')
    def test_unpaired_surrogate_refused(self):
        with self.assertRaisesRegex(d.Invalid,'string'):d.load(b'{"x":"\\ud800"}')
    def test_unsafe_integer_refused(self):
        with self.assertRaisesRegex(d.Invalid,'integer'):d.load(b'{"x":9007199254740992}')
    def test_import_rejects_dangling_proposal(self):
        with self.assertRaisesRegex(d.Invalid,'unresolved internal pin'):d.import_records([],[self.r],self.p['dimension'],self.c)
    def test_import_valid_supersession_chain(self):
        other=copy.deepcopy(self.r);other['revision']='2';other['body']['supersedes']=d.pin(self.r);other['body']['reviewedAt']='2026-09-21T10:02:00Z';other['body']['validFrom']='2026-09-21T10:02:00Z';other=d.seal(other)
        self.assertEqual(len(d.import_records([self.p,self.r],[other],self.p['dimension'],self.c)),3)
    def test_import_rejects_wrong_supersession_type(self):
        self.r['body']['supersedes']=d.pin(self.p);self.r=d.seal(self.r)
        with self.assertRaisesRegex(d.Invalid,'unresolved internal pin'):d.import_records([],[self.p,self.r],self.p['dimension'],self.c)
    def test_import_rejects_unknown_supersession(self):
        self.r['body']['supersedes']=p('unknown-review');self.r=d.seal(self.r)
        with self.assertRaisesRegex(d.Invalid,'unresolved internal pin'):d.import_records([],[self.p,self.r],self.p['dimension'],self.c)
    def test_import_cross_dimension(self):
        self.p['dimension']='urn:synthetic:elsewhere';self.p=d.seal(self.p)
        with self.assertRaisesRegex(d.Invalid,'record scope'):d.import_records([],[self.p],self.c['dimension'],self.c)
    def test_snapshot_extra_keys(self):
        self.s['allowServe']=True
        with self.assertRaisesRegex(d.Invalid,'snapshot shape'):self.answer()

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ResearchPrototype);result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'status':'passed' if result.wasSuccessful() else 'failed','testsRun':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'scope':'Codex prototype checks, not external audit, native integration or privacy/security conformance','codeSha256':hashlib.sha256(Path(d.__file__).read_bytes()).hexdigest(),'inputHashes':{n:hashlib.sha256(Path(__file__).with_name(n).read_bytes()).hexdigest() for n in ('disclosure.py','disclosure.schema.json','test_disclosure.py','README.md')},'python':sys.version,'jsonschema':importlib.metadata.version('jsonschema')}
    Path(__file__).with_name('test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    examples=Path(__file__).with_name('examples');examples.mkdir(exist_ok=True)
    for profile in ('startup','matrix','ai'):
        a,b,s,c=fixture(profile);(examples/(profile+'.json')).write_text(json.dumps({'fixtureKind':'synthetic-host-internal-only; never accept hostSnapshot or capabilities from a request','proposal':a,'reviews':[b],'hostSnapshot':s},indent=2)+'\n',encoding='utf-8',newline='\n')
    raise SystemExit(not result.wasSuccessful())
