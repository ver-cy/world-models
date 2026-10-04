"""Synthetic behavior tests and fixtures for the original reference contract."""
import copy,json,unittest
from unittest.mock import patch
from datetime import datetime,timedelta
from pathlib import Path
import provenance as p
HERE=Path(__file__).resolve().parent
U='urn:synthetic:'
CLAIM={'id':U+'claim:capacity','revision':1,'digest':'sha256:'+'a'*64}
METHOD={'id':U+'method:inspection','revision':1,'digest':'sha256:'+'b'*64}
NOW='2026-09-21T12:00:00Z'
def config():return {'id':U+'configuration','dimension':U+'dimension','validFrom':'2026-01-01T00:00:00Z','validUntil':'2030-01-01T00:00:00Z','writers':[{'kind':k,'scope':U+'scope','actors':[U+'writer']} for k in p.ANCHORS],'readers':[U+'reader'],'purposes':['research']}
def empty():return {'format':'vercy-assertion-provenance','version':'0.1.0','dimension':U+'dimension','records':[]}
def stamp(i):return (datetime(2026,9,21,10,0,0)+timedelta(seconds=i)).strftime('%Y-%m-%dT%H:%M:%SZ')
def row(kind,n,**kw):
    return {'id':U+n,'kind':kind,'scope':U+'scope','revision':1,'previousDigest':None,'recordedAt':stamp(1),'writer':U+'writer','state':'active','change':'create','reason':'Synthetic evidence-backed entry','notes':[],**kw}
def capture(n='capture',**kw):return row('Capture',n,**({'sourceRef':U+'source:document','sourceVersion':'v1','sourceAuthor':U+'document-author','aboutRef':U+'system','obtainedAt':'2026-09-21T09:00:00Z','mode':'file','availability':'captured','representationDigest':'sha256:'+'c'*64,'originRef':U+'declared-origin','integrity':'not-tested'}|kw))
def activity(c,n='acquisition',**kw):return row('Activity',n,**({'actor':U+'observer','mode':'file-acquisition','startedAt':'2026-09-21T08:00:00Z','endedAt':'2026-09-21T09:30:00Z','inputs':[p.pin(c)],'observedTarget':None,'method':METHOD}|kw))
def account(a,n='account',**kw):return row('ProvenanceRecord',n,**({'claim':CLAIM,'aboutRef':U+'system','asserter':U+'asserter','epistemicKind':'source-asserted','activity':p.pin(a) if a else None,'limitations':['Source statement; no live-system verification.']}|kw))
def link(c,n='evidence',**kw):return row('EvidenceLink',n,**({'claim':CLAIM,'evidence':p.pin(c),'attributedTo':U+'relation-author','relation':'cites','selector':'whole captured representation','rationale':'Reference context without automatic support'}|kw))
def add(ledger,r,cfg=None):
    r=copy.deepcopy(r);r['recordedAt']=stamp(len(ledger['records'])+1)
    return p.admit(ledger,r,cfg or config(),r['writer'],r['recordedAt']),r
def revision(r,**kw):return {**copy.deepcopy(r),'revision':r['revision']+1,'previousDigest':p.digest(r),'change':'correct',**kw}
def fixture(name='startup'):
    g=empty();g,c=add(g,capture());g,a=add(g,activity(c));g,pr=add(g,account(a));g,l=add(g,link(c))
    if name=='group':
        g,c2=add(g,capture('copy',sourceRef=U+'source:second-report'))
        g,a2=add(g,activity(c2,'second-acquisition'));g,pr2=add(g,account(a2,'second-account'))
        g,l2=add(g,link(c2,'counterevidence',relation='refutes',rationale='Second writer explicitly disputes the same pinned claim'))
    if name=='ai-team':
        g,s=add(g,activity(c,'synthesis',actor=U+'ai-agent',mode='synthesis',inputs=[p.pin(pr)]))
        g,inferred=add(g,account(s,'inference',epistemicKind='inferred',asserter=U+'ai-agent'))
        g,review=add(g,activity(c,'review',actor=U+'human-reviewer',mode='review',inputs=[p.pin(inferred)]))
        g,assessment=add(g,row('ConfidenceAssessment','assessment',account=p.pin(inferred),assessor=review['actor'],activity=p.pin(review),method=METHOD,scheme=p.SCHEME,purpose='Plan a separate live check',label='limited',basis=[p.pin(c)],limitations=['File analysis is not live observation.']))
    return g
def view(g,**kw):return p.view(g,config(),U+'reader','research',CLAIM,NOW,NOW,**kw)

class Tests(unittest.TestCase):
    def test_three_profiles(self):
        for name in ['startup','group','ai-team']:self.assertTrue(p.validate_ledger(fixture(name),config()))
    def test_no_truth_or_permission_inference(self):
        v=view(fixture());self.assertEqual((v['truth'],v['permissions']),('not-evaluated','not-inferred'))
    def test_shared_origin_not_independence(self):self.assertEqual(view(fixture('group'))['independence']['status'],'known-shared-origin')
    def test_distinct_roots_remain_unknown(self):
        g=fixture();g,c=add(g,capture('distinct',originRef=U+'other',representationDigest='sha256:'+'d'*64));g,a=add(g,activity(c,'distinct-event'));g,_=add(g,account(a,'distinct-account'))
        self.assertEqual(view(g)['independence']['status'],'unknown')
    def test_review_does_not_promote_inference(self):
        v=view(fixture('ai-team'));self.assertEqual(v['accounts'][-1]['epistemicKind'],'inferred');self.assertEqual(v['assessments'][0]['label'],'limited')
    def test_citation_has_no_support_default(self):self.assertEqual(view(fixture())['links'][0]['relation'],'cites')
    def test_unknown_empty_register(self):self.assertEqual(view(empty())['status'],'insufficient-context')
    def test_author_observer_asserter_recorder_separate(self):
        g=fixture();self.assertEqual(len({g['records'][0]['sourceAuthor'],g['records'][1]['actor'],g['records'][2]['asserter'],g['records'][0]['writer']}),4)
    def test_wrong_actor_denied(self):
        with self.assertRaises(p.Denied):p.admit(empty(),capture(),config(),U+'owner',stamp(1))
    def test_missing_write_grant(self):
        c=config();c['writers']=c['writers'][1:]
        with self.assertRaises(p.Denied):p.admit(empty(),capture(),c,U+'writer',stamp(1))
    def test_write_rotation_preserves_attribution(self):
        g=fixture();r=revision(g['records'][0],writer=U+'writer2',notes=['Correct attribution context']);c=config();c['writers'][0]['actors']=[U+'writer2'];g,r=add(g,r,c)
        self.assertEqual(r['sourceAuthor'],U+'document-author');self.assertEqual(g['records'][0]['writer'],U+'writer')
    def test_read_denied_before_malformed_input(self):
        with self.assertRaisesRegex(p.Denied,'^Read denied$'):p.view({'SECRET':'bad'},config(),U+'intruder','research',None,'bad',NOW)
    def test_purpose_gate(self):
        with self.assertRaises(p.Denied):p.view(fixture(),config(),U+'reader','other',CLAIM,NOW,NOW)
    def test_expired_config(self):
        with self.assertRaises(p.Denied):p.view(fixture(),config(),U+'reader','research',CLAIM,NOW,'2030-01-01T00:00:00Z')
    def test_replay_retains_receipt(self):
        g=fixture();r=copy.deepcopy(g['records'][0]);r['recordedAt']=NOW
        self.assertEqual(p.admit(g,r,config(),U+'writer',NOW),g)
    def test_replay_rechecks_rights(self):
        g=fixture();c=config();c['writers']=c['writers'][1:];r=copy.deepcopy(g['records'][0]);r['recordedAt']=NOW
        with self.assertRaises(p.Denied):p.admit(g,r,c,U+'writer',NOW)
    def test_conflicting_replay(self):
        g=fixture();r=copy.deepcopy(g['records'][0]);r['notes']=['conflicting'];r['recordedAt']=NOW
        with self.assertRaises(p.Invalid):p.admit(g,r,config(),U+'writer',NOW)
    def test_corrective_impact_and_past_knowledge(self):
        g=fixture();old=copy.deepcopy(g);g,_=add(g,revision(g['records'][0],integrity='mismatched'))
        self.assertTrue(view(g)['impacts'][0]['requiresReview']);self.assertEqual(g['records'][2]['epistemicKind'],'source-asserted')
        v=p.view(g,config(),U+'reader','research',CLAIM,stamp(4),NOW)
        self.assertEqual(v,p.view(old,config(),U+'reader','research',CLAIM,stamp(4),NOW))
    def test_withdrawal_preserves_external_claim(self):
        g=fixture();g,_=add(g,revision(g['records'][0],change='withdraw',state='withdrawn'))
        self.assertTrue(view(g)['impacts'][0]['requiresReview']);self.assertEqual(view(g)['truth'],'not-evaluated')
    def test_withdraw_dependent_after_input_withdrawn(self):
        g=fixture();g,_=add(g,revision(g['records'][0],change='withdraw',state='withdrawn'));g,_=add(g,revision(g['records'][2],change='withdraw',state='withdrawn'))
        self.assertEqual(view(g)['status'],'insufficient-context')
    def test_terminal_withdrawal(self):
        g=fixture();g,r=add(g,revision(g['records'][0],change='withdraw',state='withdrawn'))
        with self.assertRaises(p.Invalid):add(g,revision(r,state='active'))
    def test_reject_withdrawal_content_change(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,revision(g['records'][0],change='withdraw',state='withdrawn',originRef=U+'new'))
    def test_source_pin_is_immutable(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,revision(g['records'][0],representationDigest='sha256:'+'d'*64))
    def test_no_auto_carryover_to_new_claim(self):
        claim={**CLAIM,'revision':2,'digest':'sha256:'+'e'*64}
        v=p.view(fixture(),config(),U+'reader','research',claim,NOW,NOW);self.assertEqual(v['accounts'],[])
    def test_file_cannot_be_live(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,activity(g['records'][0],'fake-live',mode='live-observation',observedTarget=U+'system'))
    def test_inference_cannot_be_observation(self):
        g=fixture('ai-team')
        with self.assertRaises(p.Invalid):add(g,account(g['records'][4],'fake-observed',epistemicKind='observed'))
    def test_live_declaration_positive(self):
        g=empty();g,c=add(g,capture(mode='live-api'));g,a=add(g,activity(c,mode='live-observation',observedTarget=U+'system'));g,_=add(g,account(a,epistemicKind='observed'));self.assertTrue(p.validate_ledger(g))
    def test_observed_target_mismatch(self):
        g=empty();g,c=add(g,capture(mode='live-api'))
        with self.assertRaises(p.Invalid):add(g,activity(c,mode='live-observation',observedTarget=U+'other'))
    def test_unverified_requires_limitations(self):
        with self.assertRaises(p.Invalid):add(empty(),account({},activity=None,epistemicKind='unverified',limitations=[]))
    def test_unknown_and_unavailable_are_explicit(self):
        g=empty();g,c=add(g,capture(availability='unavailable',representationDigest=None));g,_=add(g,link(c));g,_=add(g,row('ProvenanceRecord','unknown',claim=CLAIM,aboutRef=U+'system',asserter=U+'asserter',epistemicKind='unverified',activity=None,limitations=['Awaiting source']))
        self.assertEqual(view(g)['status'],'insufficient-context');self.assertTrue(view(g)['impacts'][1]['sourceGaps'])
    def test_schema_closed(self):
        with self.assertRaises(p.Invalid):add(empty(),capture(password='secret'))
    def test_unknown_kind_and_nonrecord(self):
        for r in [{'kind':'Alien'},None]:
            with self.assertRaises(p.Invalid):p.admit(empty(),r,config(),U+'writer',stamp(1))
    def test_nested_pin_required(self):
        g=fixture();r=link(g['records'][0],'broken');r['evidence']['digest']='sha256:'+'0'*64
        with self.assertRaises(p.Invalid):add(g,r)
    def test_no_future_or_self_reference(self):
        g=fixture();r=activity(g['records'][0],'self',mode='synthesis');r['inputs']=[{'id':r['id'],'revision':1,'digest':'sha256:'+'f'*64}]
        with self.assertRaises(p.Invalid):add(g,r)
    def test_cross_scope_link(self):
        g=fixture();r=link(g['records'][0],'other-scope',scope=U+'other')
        with self.assertRaises(p.Invalid):p.validate_ledger({**g,'records':g['records']+[{**r,'recordedAt':stamp(5)}]})
    def test_new_reliance_on_superseded_revision_rejected(self):
        g=fixture();c=g['records'][0];g,_=add(g,revision(c,notes=['Correction']))
        with self.assertRaises(p.Invalid):add(g,link(c,'stale'))
    def test_bad_calendar(self):
        with self.assertRaises(p.Invalid):add(empty(),capture(obtainedAt='2026-02-30T09:00:00Z'))
    def test_activity_clock(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,activity(g['records'][0],'late',endedAt='2027-01-01T00:00:00Z'))
    def test_input_cannot_follow_synthesis_event(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,activity(g['records'][0],'premature',mode='synthesis',startedAt='2026-09-20T00:00:00Z',endedAt='2026-09-20T01:00:00Z'))
    def test_future_knowledge(self):
        with self.assertRaises(p.Invalid):p.view(fixture(),config(),U+'reader','research',CLAIM,'2027-01-01T00:00:00Z',NOW)
    def test_receipt_spoof(self):
        with self.assertRaises(p.Invalid):p.admit(empty(),capture(),config(),U+'writer',NOW)
    def test_non_monotone_receipt(self):
        g=fixture();r=capture('backdated')
        with self.assertRaises(p.Invalid):p.admit(g,r,config(),U+'writer',stamp(1))
    def test_prefix_rewrite_and_truncation(self):
        g=fixture()
        for records in [g['records'][:-1],[]]:
            with self.assertRaises(p.Invalid):p.validate_extension(g,{**g,'records':records},config())
    def test_dimension_header(self):
        with self.assertRaises(p.Invalid):p.validate_ledger({**fixture(),'dimension':U+'other'},config())
    def test_no_numeric_confidence(self):
        g=fixture('ai-team');r=revision(g['records'][-1],label=0.95)
        with self.assertRaises(p.Invalid):add(g,r)
    def test_assessment_scheme_and_review(self):
        for fields in [{'scheme':METHOD},{'assessor':U+'imposter'},{'method':CLAIM},{'limitations':[]}]:
            g=fixture('ai-team')
            with self.assertRaises(p.Invalid):add(g,revision(g['records'][-1],**fields))
    def test_import_roundtrip_and_lossy_refusal(self):
        g=fixture('ai-team');self.assertEqual(p.import_snapshot(json.loads(p.encode(g)),config(),now=NOW),g)
        with self.assertRaises(p.Invalid):p.migrate(g,config(),'legacy-owner-and-confidence',now=NOW)
    def test_rejection_does_not_mutate(self):
        g=fixture();original=p.encode(g)
        with self.assertRaises(p.Invalid):add(g,revision(g['records'][0],previousDigest='sha256:'+'0'*64))
        self.assertEqual(p.encode(g),original)
    def test_correct_unchanged_historical_dependencies(self):
        g=fixture();g,_=add(g,revision(g['records'][0],integrity='mismatched'))
        for i,kw in [(1,{'notes':['Event note']}),(2,{'limitations':['Capture mismatch now known']}),(3,{'rationale':'Updated caution without changing historical endpoint'})]:
            g,_=add(g,revision(g['records'][i],**kw))
        self.assertTrue(view(g)['impacts'][0]['requiresReview'])
    def test_correct_assessment_after_account_correction(self):
        g=fixture('ai-team');assessment=g['records'][-1];g,_=add(g,revision(g['records'][5],limitations=['New limitation']))
        g,_=add(g,revision(assessment,label='insufficient',limitations=['Account changed; retained historical target']))
        self.assertEqual(view(g)['assessments'][0]['label'],'insufficient');self.assertTrue(view(g)['impacts'][-1]['requiresReview'])
    def test_new_account_can_describe_existing_event_with_changed_input(self):
        g=fixture();g,_=add(g,revision(g['records'][0],integrity='mismatched'));g,_=add(g,account(g['records'][1],'new-account'))
        self.assertTrue(view(g)['impacts'][-2]['requiresReview'])
    def test_changed_dependency_pin_requires_current_head(self):
        g=fixture('ai-team');old=g['records'][4];g,new=add(g,revision(old,notes=['Correct event note']))
        g,account2=add(g,revision(g['records'][5],activity=p.pin(new)))
        with self.assertRaises(p.Invalid):add(g,revision(account2,activity=p.pin(old)))
    def test_ascii_calendar_and_newline_strict(self):
        for bad in ['2026-09-21T0١:00:00Z','2026-99-99T09:00:00Z','2026-09-21T09:00:00Z\n']:
            with self.assertRaises(p.Invalid):add(empty(),capture(obtainedAt=bad))
    def test_missing_format_support_fails_closed(self):
        checker=p.FormatChecker();checker.checkers=dict(checker.checkers);checker.checkers.pop('date-time')
        with patch.object(p,'FormatChecker',return_value=checker):
            with self.assertRaisesRegex(p.Invalid,'format checker unavailable'):p.validate_ledger(empty())
    def test_fractional_revision_encoding_rejected(self):
        g=fixture();candidate=copy.deepcopy(g);candidate['records'][-1]['revision']=1.0
        with self.assertRaisesRegex(p.Invalid,'fractional encoding'):p.validate_extension(g,candidate,config())
        r=link(g['records'][0],'float-pin');r['evidence']['revision']=1.0
        with self.assertRaises(p.Invalid):add(g,r)
    def test_actual_prefix_rewrite_rejected(self):
        g=fixture();c=copy.deepcopy(g);c['records'][-1]['rationale']='Rewritten history'
        self.assertTrue(p.validate_ledger(c,config()))
        with self.assertRaisesRegex(p.Invalid,'prefix rewritten'):p.validate_extension(g,c,config())
    def test_cross_revision_self_derivation(self):
        g=fixture('ai-team');original=g['records'][5];g,s=add(g,activity(g['records'][0],'self-cycle',mode='synthesis',inputs=[p.pin(original)]))
        with self.assertRaisesRegex(p.Invalid,'Self-derivation'):add(g,revision(original,activity=p.pin(s)))
    def test_current_capture_failure_visible(self):
        g=fixture();g,_=add(g,revision(g['records'][0],integrity='mismatched'))
        changed=view(g)['impacts'][0]['changedDependencies'];self.assertEqual(changed[0]['currentCaptureState']['integrity'],'mismatched')
    def test_assessment_genesis_semantic_guards(self):
        base=fixture('ai-team');prototype=base['records'][-1];g={**base,'records':base['records'][:-1]}
        for fields,message in [({'scheme':METHOD},'Unknown confidence scheme'),({'assessor':U+'imposter'},'reviewer/method mismatch'),({'method':CLAIM},'reviewer/method mismatch')]:
            r={**copy.deepcopy(prototype),**fields,'id':U+'bad-assessment'}
            with self.assertRaisesRegex(p.Invalid,message):add(g,r)
    def test_snapshot_digest_and_predecessor(self):
        g=fixture();new,_=add(g,revision(g['records'][0],notes=['New metadata']))
        def fact(ledger,n,previous=None):return {'recordType':'fact','path':'provenance.register.snapshot','factId':U+'snapshot'+str(n),'subjectId':ledger['dimension']+':provenance-register','value':ledger,'supersedes':[] if previous is None else [previous['factId']],'provenance':{'snapshotDigest':p.digest(ledger),'previousSnapshotDigest':None if previous is None else p.digest(previous['value'])}}
        f1=fact(g,1);f2=fact(new,2,f1);self.assertTrue(p.validate_snapshot(f1,config(),now=NOW));self.assertTrue(p.validate_snapshot(f2,config(),f1,now=NOW))
        for field in ['snapshotDigest','previousSnapshotDigest']:
            bad=copy.deepcopy(f2);bad['provenance'][field]='sha256:'+'0'*64
            with self.assertRaises(p.Invalid):p.validate_snapshot(bad,config(),f1,now=NOW)
        with self.assertRaises(p.Invalid):p.validate_snapshot(f2,config(),now=NOW)
    def test_uniform_read_denial_when_config_expired(self):
        with self.assertRaisesRegex(p.Denied,'^Read denied$'):p.view(None,config(),U+'intruder','research',None,'bad','2030-01-01T00:00:00Z')
    def test_json_size_bound(self):
        with self.assertRaisesRegex(p.Invalid,'8 MiB'):p.encode('x'*(8*1024*1024))


    def test_changed_judgement_needs_fresh_review(self):
        g=fixture('ai-team')
        with self.assertRaisesRegex(p.Invalid,'fresh review'):add(g,revision(g['records'][-1],label='supported'))
    def test_changed_judgement_positive(self):
        g=fixture('ai-team');assessment=g['records'][-1];review=copy.deepcopy(g['records'][-2]);review['id']=U+'fresh-review'
        g,r=add(g,review);g,_=add(g,revision(assessment,label='supported',activity=p.pin(r)))
        self.assertEqual(view(g)['assessments'][0]['label'],'supported')
    def test_changed_judgement_rejects_withdrawn_basis(self):
        g=fixture('ai-team');assessment=g['records'][-1];review=copy.deepcopy(g['records'][-2]);review['id']=U+'fresh-review'
        g,r=add(g,review);g,_=add(g,revision(g['records'][0],change='withdraw',state='withdrawn'))
        with self.assertRaises(p.Invalid):add(g,revision(assessment,label='supported',activity=p.pin(r)))
    def test_changed_judgement_rejects_transitive_stale_capture(self):
        g=fixture('ai-team');assessment=g['records'][-1];review=copy.deepcopy(g['records'][-2]);review['id']=U+'fresh-review'
        g,r=add(g,review);g,_=add(g,revision(g['records'][0],integrity='mismatched'))
        with self.assertRaises(p.Invalid):add(g,revision(assessment,label='supported',activity=p.pin(r),basis=[p.pin(g['records'][5])]))
    def test_retained_pin_cannot_change_field(self):
        g=fixture('ai-team');assessment=g['records'][-1];old_account=g['records'][5]
        g,_=add(g,revision(old_account,notes=['Correction']))
        with self.assertRaisesRegex(p.Invalid,'superseded'):add(g,revision(assessment,label='insufficient',basis=[p.pin(old_account)]))
    def test_import_future_receipt_rejected(self):
        g=empty();r=capture();r['recordedAt']='9999-12-31T23:59:59Z';g['records']=[r]
        self.assertTrue(p.validate_ledger(g,config())) # Offline structural check only.
        with self.assertRaisesRegex(p.Invalid,'trusted now'):p.import_snapshot(g,config(),now=NOW)
        with self.assertRaisesRegex(p.Invalid,'trusted now'):p.migrate(g,config(),p.VERSION,now=NOW)
        with self.assertRaisesRegex(p.Invalid,'trusted now'):p.validate_extension(empty(),g,config(),now=NOW)
        fact={'recordType':'fact','path':'provenance.register.snapshot','factId':U+'snapshot','subjectId':g['dimension']+':provenance-register','value':g,'supersedes':[],'provenance':{'snapshotDigest':p.digest(g),'previousSnapshotDigest':None}}
        with self.assertRaisesRegex(p.Invalid,'trusted now'):p.validate_snapshot(fact,config(),now=NOW)
    def test_import_requires_host_clock(self):
        with self.assertRaises(TypeError):p.import_snapshot(fixture(),config())

    def test_assessment_genesis_rejects_mismatched_basis(self):
        g=fixture('ai-team');assessment=copy.deepcopy(g['records'][-1]);assessment['id']=U+'new-assessment'
        g,c=add(g,revision(g['records'][0],integrity='mismatched'));assessment.update(label='supported',basis=[p.pin(c)])
        with self.assertRaises(p.Invalid):add(g,assessment)
    def test_basis_swap_needs_new_review_identity(self):
        g=fixture('ai-team');assessment=g['records'][-1]
        with self.assertRaisesRegex(p.Invalid,'fresh review activity ID'):add(g,revision(assessment,basis=[p.pin(g['records'][5])]))
    def test_review_metadata_revision_is_not_fresh_execution(self):
        g=fixture('ai-team');assessment=g['records'][-1];g,r=add(g,revision(g['records'][-2],notes=['Metadata only']))
        with self.assertRaisesRegex(p.Invalid,'fresh review activity ID'):add(g,revision(assessment,label='supported',activity=p.pin(r)))
    def test_genesis_review_cannot_precede_basis_receipt(self):
        g=fixture('ai-team');assessment=copy.deepcopy(g['records'][-1]);assessment['id']=U+'new-assessment'
        g,c=add(g,capture('late-basis'));assessment['basis']=[p.pin(c)]
        with self.assertRaisesRegex(p.Invalid,'before its evidence basis'):add(g,assessment)
    def test_prior_review_cannot_reassess_later_judgement(self):
        g=fixture('ai-team');assessment=g['records'][-1];g['records']=g['records'][:-1]
        review=copy.deepcopy(g['records'][-1]);review['id']=U+'earlier-alternate-review';g,r=add(g,review);g,assessment=add(g,assessment)
        with self.assertRaisesRegex(p.Invalid,'after the previous assessment'):add(g,revision(assessment,label='supported',activity=p.pin(r)))
    def test_expired_import_configuration_rejected(self):
        with self.assertRaises(p.Denied):p.import_snapshot(fixture(),config(),now='2030-01-01T00:00:00Z')
    def test_canonical_encoding_control_and_unicode_vector(self):
        value={'revision':1,'a':'é\n\u0001\u2028\u2029'}
        self.assertEqual(p.encode(value).hex(),'7b2261223a22c3a95c6e5c7530303031e280a8e280a9222c227265766973696f6e223a317d')

    def test_old_alternate_review_metadata_cannot_refresh_execution(self):
        g=fixture('ai-team');assessment=g['records'][-1];g['records']=g['records'][:-1]
        review=copy.deepcopy(g['records'][-1]);review['id']=U+'earlier-alternate-review';g,r=add(g,review);g,assessment=add(g,assessment)
        g,corrected=add(g,revision(r,notes=['Metadata correction after assessment']))
        with self.assertRaisesRegex(p.Invalid,'first registered after'):add(g,revision(assessment,label='supported',activity=p.pin(corrected)))
    def test_insufficient_roundtrip_cannot_reuse_old_execution(self):
        g=fixture('ai-team');a=g['records'][-1];r1=g['records'][-2];r2=copy.deepcopy(r1);r2['id']=U+'second-review';g,r2=add(g,r2)
        g,a=add(g,revision(a,label='insufficient',activity=p.pin(r2)));g,r1=add(g,revision(r1,notes=['Later notes']))
        with self.assertRaisesRegex(p.Invalid,'first registered after'):add(g,revision(a,label='limited',activity=p.pin(r1)))
    def test_review_metadata_cannot_move_registration_after_basis(self):
        g=fixture('ai-team');a=copy.deepcopy(g['records'][-1]);a['id']=U+'new-assessment';review=g['records'][-2]
        g,c=add(g,capture('late-basis'));g,r=add(g,revision(review,notes=['Later metadata']));a.update(activity=p.pin(r),basis=[p.pin(c)])
        with self.assertRaisesRegex(p.Invalid,'first registered before'):add(g,a)
    def test_genuinely_later_registered_review_can_be_metadata_corrected(self):
        g=fixture('ai-team');a=g['records'][-1];review=copy.deepcopy(g['records'][-2]);review['id']=U+'new-review';g,r=add(g,review)
        g,r=add(g,revision(r,notes=['Metadata maintenance']));g,_=add(g,revision(a,label='supported',activity=p.pin(r)))
        self.assertEqual(view(g)['assessments'][0]['label'],'supported')
    def test_current_mismatched_capture_guard_isolated(self):
        g=fixture('ai-team');a=copy.deepcopy(g['records'][-1]);a['id']=U+'different-assessment';review=copy.deepcopy(g['records'][-2]);review['id']=U+'new-review'
        g,c=add(g,capture('bad-current-capture',integrity='mismatched'));g,r=add(g,review);a.update(activity=p.pin(r),basis=[p.pin(c)])
        with self.assertRaisesRegex(p.Invalid,'unavailable or mismatched capture'):add(g,a)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests);result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'testsRun':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful()}
    (HERE/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    if result.wasSuccessful():
        (HERE/'examples').mkdir(exist_ok=True)
        for name in ['startup','group','ai-team']:
            instance=fixture(name);cfg=config();instance['dimension']=cfg['dimension']=U+'dimension:'+name
            for suffix,value in [('.json',instance),('.config.json',cfg)]:
                (HERE/'examples'/(name+suffix)).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
