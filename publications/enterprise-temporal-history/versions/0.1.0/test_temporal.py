import copy,json,unittest,datetime,hashlib
from pathlib import Path
import temporal as t
NOW='2026-09-21T18:00:00Z'
T1='2026-01-10T00:00:00Z';T2='2026-02-10T00:00:00Z';T3='2026-03-10T00:00:00Z'
def pin(name):return {'id':'urn:synthetic:'+name,'version':'1.0.0','digest':t.digest(name)}
def value(name):return {'id':'urn:synthetic:value:'+name,'revision':'urn:synthetic:value:'+name+':r1','digest':t.digest(name)}
def fixture(name='startup'):
    schema=pin('assignment-schema');profile=pin('assignment-state')
    config={'dimension':'urn:synthetic:dimension:'+name,'timeline':'urn:synthetic:timeline:'+name,'scope':{'subject':'urn:synthetic:assignment:'+name,'predicate':'urn:synthetic:assigned-team','context':'urn:synthetic:scope:'+name},'validFrom':'2026-01-01T00:00:00Z','validUntil':'2027-01-01T00:00:00Z','writer':'urn:synthetic:master:'+name,'readers':['urn:synthetic:reader'],'purposes':['research'],'acceptedSchemas':[schema],'acceptedStates':[{'profile':profile,'axis':'urn:synthetic:assignment-status','codes':['active','suspended']}]}
    def seg(start,end,team):return {'validFrom':start,'validTo':end,'value':value(team),'schema':schema,'state':{'profile':profile,'axis':'urn:synthetic:assignment-status','code':'active'}}
    q1={'key':'urn:synthetic:key:'+name+':1','revision':'urn:synthetic:revision:'+name+':1','expectedHead':None,'operation':'record','reason':'Synthetic initial source report','sourceRecordedAt':'2026-01-05T00:00:00Z','segments':[seg('2026-01-01T00:00:00Z',None,'team-a')]}
    e=t.empty(config);one=t.admit(e,q1,config,actor=config['writer'],now=T1)
    q2={'key':'urn:synthetic:key:'+name+':2','revision':'urn:synthetic:revision:'+name+':2','expectedHead':t.head(one),'operation':'correct','reason':'Synthetic late correction received February 10','sourceRecordedAt':'2026-01-20T00:00:00Z','segments':[seg('2026-01-01T00:00:00Z','2026-01-20T00:00:00Z','team-a'),seg('2026-01-20T00:00:00Z',None,'team-b')]}
    if name=='group':
        # Separate scope prevents a local assignment correction from becoming a global employment change.
        config['scope']['context']='urn:synthetic:group:matrix-assignment';one['scope']=copy.deepcopy(config['scope']);e['scope']=copy.deepcopy(config['scope'])
    if name=='ai-team':
        config['scope']['predicate']='urn:synthetic:deployment-artifact';config['scope']['subject']='urn:synthetic:deployment:staging'
        one['scope']=copy.deepcopy(config['scope']);e['scope']=copy.deepcopy(config['scope'])
        deployment_schema=pin('deployment-binding-schema');deployment_profile=pin('deployment-state')
        config['acceptedSchemas']=[deployment_schema];config['acceptedStates']=[{'profile':deployment_profile,'axis':'urn:synthetic:deployment-status','codes':['serving','draining']}]
        for q in [q1,q2]:
            for s in q['segments']:
                s['value']=value('model-build-11' if s['value']==value('team-a') else 'model-build-12');s['schema']=deployment_schema;s['state']={'profile':deployment_profile,'axis':'urn:synthetic:deployment-status','code':'serving'}
        one=t.admit(e,q1,config,actor=config['writer'],now=T1);q2['expectedHead']=t.head(one)
    one=t.admit(e,q1,config,actor=config['writer'],now=T1);q2['expectedHead']=t.head(one)
    two=t.admit(one,q2,config,actor=config['writer'],now=T2)
    return config,e,one,two,q1,q2
class TemporalTests(unittest.TestCase):
    def setUp(self):self.cfg,self.empty,self.one,self.two,self.q1,self.q2=fixture()
    def read(self,ledger=None,**kw):
        args=dict(actor='urn:synthetic:reader',purpose='research',validAt='2026-02-01T00:00:00Z',knownAt=NOW,now=NOW);args.update(kw)
        return t.resolve(self.two if ledger is None else ledger,self.cfg,**args)
    def write(self,q=None,ledger=None,**kw):
        args=dict(actor=self.cfg['writer'],now=T2);args.update(kw)
        return t.admit(self.one if ledger is None else ledger,self.q2 if q is None else q,self.cfg,**args)
    def bad(self,change):
        q=copy.deepcopy(self.q2);change(q)
        with self.assertRaises(t.Invalid):self.write(q)
    def test_bitemporal_as_known(self):self.assertEqual(self.read(knownAt='2026-01-31T00:00:00Z')['segment']['value'],value('team-a'))
    def test_bitemporal_corrected(self):self.assertEqual(self.read()['segment']['value'],value('team-b'))
    def test_before_correction_boundary(self):self.assertEqual(self.read(validAt='2026-01-19T23:59:59Z')['segment']['value'],value('team-a'))
    def test_exact_half_open_boundary(self):self.assertEqual(self.read(validAt='2026-01-20T00:00:00Z')['segment']['value'],value('team-b'))
    def test_before_first_receipt(self):self.assertEqual(self.read(knownAt='2026-01-09T23:59:59Z')['status'],'insufficient-context')
    def test_before_valid_coverage(self):self.assertEqual(self.read(validAt='2025-12-31T00:00:00Z')['status'],'insufficient-context')
    def test_empty_register(self):self.assertEqual(self.read(self.empty)['status'],'insufficient-context')
    def test_gap_unknown(self):
        q=copy.deepcopy(self.q2);q['segments'][1]['validFrom']='2026-02-03T00:00:00Z';out=self.write(q);self.assertEqual(self.read(out)['status'],'insufficient-context')
    def test_source_time_does_not_backdate_receipt(self):self.assertEqual(self.read(knownAt='2026-02-01T00:00:00Z')['commit']['recordedAt'],T1)
    def test_same_second_sequence(self):
        q=copy.deepcopy(self.q2);q['sourceRecordedAt']=None;out=self.write(q,now=T1)
        self.assertEqual(self.read(out,knownAt=T1)['segment']['value'],value('team-b'))
        self.assertEqual(self.read(out,knownAt=T1,knownSequence=1)['segment']['value'],value('team-a'))
    def test_zero_sequence_cut(self):self.assertEqual(self.read(knownSequence=0)['status'],'insufficient-context')
    def test_bad_sequence_cut(self):
        for cut in [True,1.0,-1,3]:
            with self.subTest(cut=cut),self.assertRaises(t.Invalid):self.read(knownSequence=cut)
    def test_future_known_rejected(self):
        with self.assertRaises(t.Invalid):self.read(knownAt='2027-01-01T00:00:00Z')
    def test_admission_rejects_input_ahead_of_host_clock(self):
        q=copy.deepcopy(self.q2);q['sourceRecordedAt']=None
        with self.assertRaises(t.Invalid):self.write(q,now='2026-01-09T00:00:00Z')
    def test_future_receipt_import(self):
        with self.assertRaises(t.Invalid):t.validate_ledger(self.two,now=T1)
    def test_forged_receipt_request_rejected(self):self.bad(lambda q:q.update(recordedAt=T1))
    def test_source_record_after_receipt(self):self.bad(lambda q:q.update(sourceRecordedAt=NOW))
    def test_overlap(self):self.bad(lambda q:q['segments'][1].update(validFrom='2026-01-19T00:00:00Z'))
    def test_open_interval_not_last(self):self.bad(lambda q:q['segments'][0].update(validTo=None))
    def test_zero_interval(self):self.bad(lambda q:q['segments'][0].update(validTo=q['segments'][0]['validFrom']))
    def test_reverse_interval(self):self.bad(lambda q:q['segments'][0].update(validTo='2025-01-01T00:00:00Z'))
    def test_unsupported_times(self):
        for x in ['2026-02-30T00:00:00Z','2026-01-01T00:00:00+00:00','2026-01-01T00:00:00.1Z','2026-01-01','2026-01-01T00:00:60Z','２０２６-01-01T00:00:00Z','2026-01-01T00:00:00Z\n']:
            with self.subTest(x=x):self.bad(lambda q:q['segments'][0].update(validFrom=x))
    def test_future_valid_allowed(self):self.assertEqual(self.read(validAt='2028-01-01T00:00:00Z')['status'],'recorded-assertion')
    def test_replay_preserves_first_receipt(self):self.assertEqual(self.write(self.q2,self.two,now=T3),self.two)
    def test_old_replay_after_new_commit(self):self.assertEqual(self.write(self.q1,self.two,now=T3),self.two)
    def test_conflicting_replay(self):
        q=copy.deepcopy(self.q2);q['reason']='Different'
        with self.assertRaises(t.Invalid):self.write(q,self.two,now=T3)
    def test_head_conflict(self):self.bad(lambda q:q.update(expectedHead=None))
    def test_reused_revision(self):self.bad(lambda q:q.update(revision=self.q1['revision']))
    def test_writer_denied(self):
        with self.assertRaises(t.Invalid):self.write(actor='urn:synthetic:competitor')
    def test_replay_rechecks_current_writer(self):
        self.cfg['writer']='urn:synthetic:new-writer'
        with self.assertRaises(t.Invalid):self.write(self.q2,self.two,actor='urn:synthetic:master:startup',now=T3)
    def test_denied_read_before_diagnostics(self):
        with self.assertRaisesRegex(t.Invalid,'Read denied'):self.read({'secret':'invalid'},actor='urn:synthetic:outsider',validAt='bad')
    def test_denied_purpose(self):
        with self.assertRaisesRegex(t.Invalid,'Read denied'):self.read(purpose='advertising')
    def test_expired_policy(self):
        with self.assertRaises(t.Invalid):self.read(now='2027-01-01T00:00:00Z')
    def test_scope_mismatch(self):
        self.cfg['scope']['context']='urn:synthetic:other'
        with self.assertRaises(t.Invalid):self.read()
    def test_schema_is_not_state(self):self.bad(lambda q:q['segments'][0]['schema'].update(version='active'))
    def test_unknown_schema_binding(self):self.bad(lambda q:q['segments'][0].update(schema=pin('unapproved')))
    def test_unknown_state(self):self.bad(lambda q:q['segments'][0]['state'].update(code='completed'))
    def test_state_is_optional(self):
        q=copy.deepcopy(self.q2);q['segments'][0]['state']=None;self.write(q)
    def test_binding_repoint_in_history(self):
        q=copy.deepcopy(self.q2);q['segments'][0]['schema']['digest']=t.digest('changed');self.cfg['acceptedSchemas']=[q['segments'][0]['schema']]
        with self.assertRaises(t.Invalid):self.write(q)
    def test_payload_revision_repoint(self):self.bad(lambda q:q['segments'][0]['value'].update(digest=t.digest('changed')))
    def test_new_schema_version_does_not_rewrite_old(self):
        q=copy.deepcopy(self.q2);b=copy.deepcopy(q['segments'][1]['schema']);b['version']='2.0.0';b['digest']=t.digest('schema2');self.cfg['acceptedSchemas'].append(b);q['segments'][1]['schema']=b
        out=self.write(q);self.assertEqual(self.read(out,knownAt=T1)['segment']['schema']['version'],'1.0.0');self.assertEqual(self.read(out)['segment']['schema']['version'],'2.0.0')
    def archive(self):
        q=copy.deepcopy(self.q2);q.update(key='urn:synthetic:key:archive',revision='urn:synthetic:revision:archive',expectedHead=t.head(self.two),operation='archive',reason='Stop changes, preserve retained history');return self.write(q,self.two,now=T3),q
    def test_archive_retains_history(self):
        out,q=self.archive();self.assertEqual(out['commits'][:2],self.two['commits']);self.assertEqual(self.read(out)['segment']['value'],value('team-b'));self.assertTrue(self.read(out)['archivedAsKnown']);self.assertFalse(self.read(out,knownAt=T1)['archivedAsKnown'])
    def test_archive_replay(self):
        out,q=self.archive();self.assertEqual(self.write(q,out,now=NOW),out)
    def test_archive_cannot_rewrite(self):
        q=copy.deepcopy(self.q2);q['operation']='archive'
        with self.assertRaises(t.Invalid):self.write(q)
    def test_archive_terminal(self):
        out,_=self.archive();q=copy.deepcopy(self.q2);q.update(key='urn:synthetic:key:after',revision='urn:synthetic:revision:after',expectedHead=t.head(out))
        with self.assertRaises(t.Invalid):self.write(q,out,now=NOW)
    def test_no_history_truncation(self):
        with self.assertRaises(t.Invalid):t.validate_extension(self.two,self.one,now=NOW)
    def test_no_prefix_rewrite(self):
        changed=copy.deepcopy(self.one);changed['commits'][0]['request']['reason']='rewrite'
        with self.assertRaises(t.Invalid):t.validate_extension(self.one,changed,now=NOW)
    def test_float_receipt_sequence(self):
        changed=copy.deepcopy(self.one);changed['commits'][0]['sequence']=1.0
        with self.assertRaises(t.Invalid):t.validate_ledger(changed,now=NOW)
    def test_digest_trailing_newline(self):self.bad(lambda q:q['segments'][0]['value'].update(digest=q['segments'][0]['value']['digest']+'\n'))
    def test_closed_schema(self):self.bad(lambda q:q.update(secret='unsupported'))
    def test_lossless_roundtrip(self):self.assertEqual(t.migrate(self.two,'0.1.0',now=NOW),self.two)
    def test_downgrade_rejected(self):
        with self.assertRaises(t.Invalid):t.migrate(self.two,'0.0.9',now=NOW)
    def test_no_implicit_truth_or_transition(self):
        r=self.read();self.assertEqual(r['truth'],'not-evaluated');self.assertEqual(r['transitionLegality'],'not-evaluated');self.assertEqual(r['domainValidation'],'not-executed')
    def test_mutable_return_not_input(self):
        r=self.read();r['segment']['value']['id']='urn:synthetic:changed';self.assertEqual(self.read()['segment']['value'],value('team-b'))
    def test_three_profiles(self):
        for name in ['startup','group','ai-team']:
            with self.subTest(name=name):c,e,a,b,_,_=fixture(name);t.validate_extension(a,b,now=NOW);self.assertEqual(b['scope'],c['scope'])
    def test_bounded_append_sequences_preserve_pinned_history(self):
        root=copy.deepcopy(self.two);saved=self.read(root,knownAt=T2,knownSequence=2)['segment']
        for i in range(3,33):
            q=copy.deepcopy(self.q2);q.update(key='urn:synthetic:key:'+str(i),revision='urn:synthetic:revision:'+str(i),expectedHead=t.head(root));q['segments'][1]['value']=value('team-'+str(i))
            root=self.write(q,root,now=T2);self.assertEqual(self.read(root,knownAt=T2,knownSequence=2)['segment'],saved)
    def test_empty_snapshot_is_not_false(self):
        q=copy.deepcopy(self.q2);q['segments']=[];self.assertEqual(self.read(self.write(q))['status'],'insufficient-context')
    def test_segment_overflow(self):self.bad(lambda q:q.update(segments=q['segments']*51))
    def test_unavailable_format_checker(self):
        from unittest.mock import patch
        with patch.object(t.FormatChecker,'checkers',{}),self.assertRaises(t.Invalid):self.read()
    def test_new_binding_must_not_mutate_config_history(self):
        self.cfg['acceptedSchemas'].append({**self.cfg['acceptedSchemas'][0],'digest':t.digest('different')})
        with self.assertRaises(t.Invalid):self.read()
    def test_archive_after_schema_retirement(self):
        self.cfg['acceptedSchemas']=[pin('replacement')];self.cfg['acceptedStates']=[];out,_=self.archive();self.assertTrue(self.read(out)['archivedAsKnown'])
    def test_retained_segments_after_pin_retirement(self):
        self.cfg['acceptedSchemas']=[pin('replacement')];self.cfg['acceptedStates']=[];q=copy.deepcopy(self.q2);q.update(key='urn:synthetic:new:key',revision='urn:synthetic:new:revision',expectedHead=t.head(self.two),reason='Clarify source metadata only');self.write(q,self.two,now=T3)
    def test_changed_interval_is_new_use_of_retired_pin(self):
        self.cfg['acceptedSchemas']=[pin('replacement')];q=copy.deepcopy(self.q2);q.update(key='urn:synthetic:new:key',revision='urn:synthetic:new:revision',expectedHead=t.head(self.two));q['segments'][1]['validTo']='2026-09-01T00:00:00Z'
        with self.assertRaises(t.Invalid):self.write(q,self.two,now=T3)
    def test_transplanted_history_rejected(self):
        for field in ['dimension','timeline','scope']:
            root=copy.deepcopy(self.two);root[field]='urn:synthetic:transplant' if field!='scope' else {**root['scope'],'context':'urn:synthetic:transplant'}
            with self.subTest(field=field),self.assertRaisesRegex(t.Invalid,'transplanted'):t.validate_ledger(root,now=NOW)
    def test_imported_clock_regression_branch(self):
        root=copy.deepcopy(self.two);root['commits'][1]['recordedAt']='2026-01-09T00:00:00Z'
        with self.assertRaisesRegex(t.Invalid,'moved backwards'):t.validate_ledger(root,now=NOW)
    def test_segment_bound_without_overlap(self):
        q=copy.deepcopy(self.q2);q['segments']=[];base=datetime.datetime(2026,1,1)
        for i in range(101):
            s=copy.deepcopy(self.q2['segments'][0]);s.update(validFrom=(base+datetime.timedelta(seconds=i)).strftime('%Y-%m-%dT%H:%M:%SZ'),validTo=(base+datetime.timedelta(seconds=i+1)).strftime('%Y-%m-%dT%H:%M:%SZ'));q['segments'].append(s)
        with self.assertRaisesRegex(t.Invalid,'Closed schema'):self.write(q)
    def snapshots(self):
        def f(root,n,prev):
            return dict(factId='urn:synthetic:native:'+str(n),path='temporal.timeline.snapshot',value=copy.deepcopy(root),subjectId=root['timeline'],provenance=dict(snapshotDigest=t.digest(root),previousSnapshotDigest=None if prev is None else t.digest(prev['value'])),supersedes=[] if prev is None else [prev['factId']],status='asserted',unit=None,recordedAt=NOW,validFrom=NOW,validTo=None)
        f1=f(self.one,1,None);f2=f(self.two,2,f1);archived,_=self.archive();return f1,f2,f(archived,3,f2)
    def snapshot(self,f,previous=None,**kw):
        args=dict(dimension=self.cfg['dimension'],now=NOW,previous=previous);args.update(kw);return t.validate_snapshot(f,**args)
    def test_snapshot_genesis_and_successors(self):
        a,b,c=self.snapshots();self.snapshot(a);self.snapshot(b,a);self.snapshot(c,b)
    def test_snapshot_missing_envelope(self):
        a,_,_=self.snapshots();del a['recordedAt']
        with self.assertRaisesRegex(t.Invalid,'Incomplete snapshot envelope'):self.snapshot(a)
    def test_snapshot_missing_provenance(self):
        a,_,_=self.snapshots();a['provenance']={}
        with self.assertRaisesRegex(t.Invalid,'Incomplete snapshot provenance'):self.snapshot(a)
    def test_snapshot_storage_state(self):
        for change in [dict(status='retracted'),dict(unit='kg'),dict(validTo=NOW)]:
            a,_,_=self.snapshots();a.update(change)
            with self.subTest(change=change),self.assertRaisesRegex(t.Invalid,'Unsupported snapshot envelope state'):self.snapshot(a)
    def test_snapshot_bad_receipt_envelope(self):
        a,_,_=self.snapshots();a['validFrom']=T1
        with self.assertRaisesRegex(t.Invalid,'Invalid snapshot receipt envelope'):self.snapshot(a)
    def test_snapshot_precedes_inner(self):
        a,_,_=self.snapshots();a.update(recordedAt='2026-01-09T00:00:00Z',validFrom='2026-01-09T00:00:00Z')
        with self.assertRaisesRegex(t.Invalid,'Snapshot precedes inner receipt'):self.snapshot(a)
    def test_snapshot_later_native_storage_does_not_rewrite_host_time(self):
        a,_,_=self.snapshots();self.snapshot(a);self.assertEqual(a['value']['commits'][0]['recordedAt'],T1);self.assertEqual(a['recordedAt'],NOW)
    def test_snapshot_wrong_path_or_subject(self):
        for field,message in [('path','Wrong native path'),('subjectId','Wrong timeline subject')]:
            a,_,_=self.snapshots();a[field]='urn:synthetic:wrong'
            with self.subTest(field=field),self.assertRaisesRegex(t.Invalid,message):self.snapshot(a)
    def test_snapshot_wrong_dimension(self):
        a,_,_=self.snapshots()
        with self.assertRaisesRegex(t.Invalid,'Wrong native Dimension'):self.snapshot(a,dimension='urn:synthetic:other')
    def test_snapshot_bad_digest(self):
        a,_,_=self.snapshots();a['provenance']['snapshotDigest']=t.digest('bad')
        with self.assertRaisesRegex(t.Invalid,'Snapshot digest mismatch'):self.snapshot(a)
    def test_snapshot_unexpected_predecessor(self):
        _,b,_=self.snapshots()
        with self.assertRaisesRegex(t.Invalid,'Unexpected predecessor'):self.snapshot(b)
    def test_snapshot_previous_nongenesis_envelope_checked(self):
        for change in [dict(status='retracted'),dict(unit='kg'),dict(validTo=NOW)]:
            _,b,c=self.snapshots();b.update(change)
            with self.subTest(change=change),self.assertRaisesRegex(t.Invalid,'Unsupported snapshot envelope state'):self.snapshot(c,b)
    def test_snapshot_previous_missing_fields(self):
        for field in ['provenance','path']:
            _,b,c=self.snapshots();del b[field]
            with self.subTest(field=field),self.assertRaisesRegex(t.Invalid,'Incomplete snapshot envelope'):self.snapshot(c,b)
    def test_snapshot_previous_wrong_binding(self):
        _,b,c=self.snapshots();b['subjectId']='urn:synthetic:wrong'
        with self.assertRaisesRegex(t.Invalid,'Wrong timeline subject'):self.snapshot(c,b)
    def test_snapshot_previous_wrong_digest(self):
        _,b,c=self.snapshots();b['provenance']['snapshotDigest']=t.digest('wrong')
        with self.assertRaisesRegex(t.Invalid,'Snapshot digest mismatch'):self.snapshot(c,b)
    def test_snapshot_previous_hash_link(self):
        a,b,_=self.snapshots();b['provenance']['previousSnapshotDigest']=t.digest('wrong')
        with self.assertRaisesRegex(t.Invalid,'Wrong previous snapshot digest'):self.snapshot(b,a)
    def test_snapshot_predecessor_identity(self):
        a,b,_=self.snapshots();b['factId']=a['factId']
        with self.assertRaisesRegex(t.Invalid,'Wrong snapshot predecessor identity'):self.snapshot(b,a)
    def test_snapshot_storage_clock_regression(self):
        a,b,_=self.snapshots();b.update(recordedAt=T2,validFrom=T2)
        with self.assertRaisesRegex(t.Invalid,'Snapshot receipt precedes predecessor'):self.snapshot(b,a)
    def test_scope_gate_before_history_diagnostics(self):
        self.cfg['scope']['context']='urn:synthetic:another';root=copy.deepcopy(self.two);root['commits'][1]['sequence']=9
        with self.assertRaisesRegex(t.Invalid,'Wrong governed scope'):self.read(root)
        with self.assertRaisesRegex(t.Invalid,'Wrong governed scope'):self.write(ledger=root)
    def test_forward_clock_excursion_needs_external_recovery(self):
        q=copy.deepcopy(self.q2);q.update(key='urn:synthetic:future:key',revision='urn:synthetic:future:revision',expectedHead=t.head(self.two));root=self.write(q,self.two,now='2026-12-31T00:00:00Z')
        with self.assertRaisesRegex(t.Invalid,'Future receipt'):self.read(root)
        with self.assertRaisesRegex(t.Invalid,'Future receipt'):self.write(q,root,now=NOW)
if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TemporalTests);result=unittest.TextTestRunner(verbosity=1).run(suite)
    Path('test-results.json').write_text(json.dumps({'passed':result.wasSuccessful(),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'codeDigest':'sha256:'+hashlib.sha256(Path(t.__file__).read_bytes()).hexdigest()},indent=2)+'\n',encoding='utf-8')
    raise SystemExit(not result.wasSuccessful())
