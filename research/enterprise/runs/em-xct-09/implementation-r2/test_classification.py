"""Behavioral counterexamples for the original local category-set dialect."""
import copy,hashlib,json,sys,time,unittest
from pathlib import Path
import classification_review as r
from fixtures import AT,START,END,ACTOR,make,repin,grant,evaluate,code,snapshot,profile,release

class ReviewTests(unittest.TestCase):
    def test_three_business_contexts(self):
        for name in ('startup','international','ai-team'):
            with self.subTest(name=name):
                f=make(name);result=evaluate(f)
                for k,v in f['expected'].items():self.assertEqual(result[k],v)
                self.assertEqual(result['effects'],[])
    def test_excluded_code_preserves_source_conformance(self):
        f=make('startup');repin(f,'urn:synthetic:assignment:1',lambda a:a.update(values=[code('urn:synthetic:scheme:startup','1','C')]))
        a=evaluate(f)['assignments'][0];self.assertEqual(a['sourceConformance'],'conforms');self.assertEqual(a['selectedConformance'],'does-not-conform')
    def test_profile_only_without_assignment(self):
        f=make('startup');f['packet'].update(mode='profile',assignments=[]);f['host']=grant(f['packet'])
        self.assertEqual(evaluate(f)['outcome'],'conforms-to-local-profile')
    def test_empty_forbidden_slot(self):
        f=make('startup');repin(f,'urn:synthetic:profile:base',lambda d:d.update(min=0));repin(f,'urn:synthetic:profile:narrow',lambda d:d.update(min=0,max=0,allowed=[]));repin(f,'urn:synthetic:assignment:1',lambda d:d.update(values=[]))
        self.assertEqual(evaluate(f)['outcome'],'conforms-to-local-profile')
    def test_multiple_independent_categories(self):
        f=make('startup');repin(f,'urn:synthetic:assignment:1',lambda d:d.update(values=[code('urn:synthetic:scheme:startup','1',c) for c in ('A','B')]))
        self.assertEqual(evaluate(f)['outcome'],'conforms-to-local-profile')
    def test_narrowing_cannot_change_meaning_identity_or_unit(self):
        for field in ('subjectClass','unit','slot','meaning'):
            f=make('startup');repin(f,'urn:synthetic:profile:narrow',lambda d:d.update({field:'different'}))
            with self.subTest(field=field),self.assertRaises(r.Invalid):evaluate(f)
    def test_narrowing_cannot_widen_cardinality(self):
        f=make('startup');repin(f,'urn:synthetic:profile:narrow',lambda d:d.update(max=3))
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_profile_cannot_invent_code(self):
        f=make('startup');repin(f,'urn:synthetic:profile:narrow',lambda d:d['allowed'].append(code('urn:synthetic:scheme:startup','1','NEW')))
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_parent_digest_mismatch(self):
        f=make('startup');repin(f,'urn:synthetic:profile:narrow',lambda d:d['parent'].update(digest='sha256:'+'0'*64))
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_profile_cycle(self):
        f=make('startup');d=next(s for s in f['packet']['snapshots'] if s['id']=='urn:synthetic:profile:narrow');d['payload']['parent']=r.pin(d);d['digest']=r.snapshot_digest(d);f['packet']['profile']=r.pin(d);f['host']=grant(f['packet'])
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_required_only_is_explicit_unsupported(self):
        f=make('startup');repin(f,'urn:synthetic:profile:base',lambda d:d.update(strength='preferred'));repin(f,'urn:synthetic:profile:narrow',lambda d:d.update(strength='preferred'))
        self.assertEqual(evaluate(f)['outcome'],'unsupported')
    def test_cached_ancestor_cannot_bypass_eight_profile_limit(self):
        for count in (8,9):
            f=make('startup');p=f['packet'];scheme=p['snapshots'][0];chain=[]
            for i in range(count):chain.append(profile('urn:synthetic:profile:depth:'+str(i),scheme,'Project',['A','B'],chain[-1] if chain else None))
            p.update(mode='profile',assignments=[],snapshots=[scheme]+chain,baseProfile=r.pin(chain[-2]),profile=r.pin(chain[-1]));f['host']=grant(p)
            with self.subTest(count=count):
                if count==8:self.assertEqual(evaluate(f)['outcome'],'conforms-to-local-profile')
                else:
                    with self.assertRaisesRegex(r.Invalid,'deep profile ancestry'):evaluate(f)
    def test_profile_minimum_beyond_instance_capacity_is_unsupported(self):
        for minimum in (32,33):
            f=make('startup');p=f['packet'];codes=[str(i) for i in range(minimum)]
            scheme=release('urn:synthetic:release:wide','urn:synthetic:scheme:wide','1',codes)
            wide=profile('urn:synthetic:profile:wide',scheme,'Project',codes);wide['payload'].update(min=minimum,max=minimum);wide['digest']=r.snapshot_digest(wide)
            p.update(mode='profile',assignments=[],snapshots=[scheme,wide],baseProfile=r.pin(wide),profile=r.pin(wide));f['host']=grant(p)
            with self.subTest(minimum=minimum):self.assertEqual(evaluate(f)['outcome'],'conforms-to-local-profile' if minimum==32 else 'unsupported')
    def test_conflicting_release_coordinate_across_profiles_is_rejected(self):
        f=make('international');p=f['packet'];scheme=p['snapshots'][0]['payload']['scheme']
        repin(f,'urn:synthetic:release:old',lambda d:d['concepts'][0].update(status='retired',selectable=False))
        repin(f,'urn:synthetic:release:new',lambda d:d.update(scheme=scheme,version='1'))
        repin(f,'urn:synthetic:profile:target',lambda d:d.update(allowed=[code(scheme,'1','A')]))
        repin(f,'urn:synthetic:crosswalk:1',lambda d:d['entries'][0].update(targets=[code(scheme,'1','A')]))
        cross=p['snapshots'][-1];e=cross['payload']['entries'][0]
        f['host']=grant(p,[{'snapshotDigest':cross['digest'],'entryId':e['id'],'approver':e['approver'],'evidence':e['evidence'][0]}])
        with self.assertRaisesRegex(r.Invalid,'Conflicting source payloads'):evaluate(f)
    def test_identical_release_payload_in_distinct_capture_is_allowed(self):
        f=make('startup');duplicate=copy.deepcopy(f['packet']['snapshots'][0]);duplicate['id']='urn:synthetic:release:second-capture';duplicate['capture']['id']+=':second';duplicate['digest']=r.snapshot_digest(duplicate)
        f['packet']['snapshots'].append(duplicate);f['host']=grant(f['packet'])
        self.assertEqual(evaluate(f)['outcome'],'conforms-to-local-profile')
    def test_other_same_coordinate_payload_conflicts_are_rejected(self):
        for kind,field,new in [('slot-profile','meaning','Different meaning'),('assignment','state','disputed'),('crosswalk','complete',False)]:
            f=make('international');p=f['packet'];duplicate=copy.deepcopy(next(s for s in p['snapshots'] if s['payload']['kind']==kind));duplicate['id']+=':conflicting-capture';duplicate['payload'][field]=new;duplicate['digest']=r.snapshot_digest(duplicate);p['snapshots'].append(duplicate);f['host']=grant(p)
            with self.subTest(kind=kind),self.assertRaisesRegex(r.Invalid,'Conflicting source payloads'):evaluate(f)
    def test_duplicate_crosswalk_pin_is_rejected(self):
        f=make('international');f['packet']['crosswalks']*=2;f['host']=grant(f['packet'])
        with self.assertRaisesRegex(r.Invalid,'Duplicate selected crosswalk'):evaluate(f)
    def test_selected_old_revision_has_notice_when_correction_is_captured(self):
        f=make('startup');p=f['packet'];old=p['snapshots'][3];new=copy.deepcopy(old);new['id']+=':revision2';new['payload'].update(revision=2,corrects=r.pin(old));new['digest']=r.snapshot_digest(new);p['snapshots'].append(new);f['host']=grant(p)
        result=evaluate(f)
        self.assertEqual(result['outcome'],'conforms-to-local-profile')
        self.assertTrue(any(c['rule']=='SOURCE-REVISION-CONTEXT' and new['id'] in c['evidence'] for c in result['checks']))
    def test_proposed_assignment_conformance_is_accompanied_by_notice(self):
        f=make('startup');repin(f,'urn:synthetic:assignment:1',lambda d:d.update(state='proposed'));result=evaluate(f)
        self.assertEqual(result['outcome'],'conforms-to-local-profile');self.assertTrue(any(c['rule']=='PROPOSED-ASSIGNMENT' for c in result['checks']))
    def test_concept_validity_exclusion_has_precise_detail(self):
        f=make('startup');repin(f,'urn:synthetic:release:old',lambda d:d['concepts'][0].update(validUntil=AT));result=evaluate(f)
        self.assertEqual(result['outcome'],'does-not-conform');self.assertEqual(result['assignments'][0]['sourceConformance'],'outside-valid-time')
    def test_deprecated_or_time_expired_target_never_becomes_candidate(self):
        for changes in ({'status':'deprecated'},{'validUntil':AT}):
            f=make('international');repin(f,'urn:synthetic:release:new',lambda d:d['concepts'][0].update(changes));result=evaluate(f)
            with self.subTest(changes=changes):self.assertIsNone(result['candidate']);self.assertEqual(result['migrationDisposition'],'human-review-required')
    def test_context_mismatched_competitor_remains_packet_evidence(self):
        f=make('international');p=f['packet'];other=copy.deepcopy(p['snapshots'][-1]);other['id']+=':other';other['payload']['id']+=':other';other['payload']['context']['jurisdiction']='another-region';other['payload']['entries'][0]['targets'][0]['code']='B';other['digest']=r.snapshot_digest(other);p['snapshots'].append(other);p['crosswalks'].append(r.pin(other));f['host']['packetDigest']=r.digest(p)
        result=evaluate(f)
        self.assertEqual(result['outcome'],'candidate-only');self.assertEqual(len(result['alternatives']),1);self.assertTrue(any(c['rule']=='MAPPING-CONTEXT' for c in result['checks']));self.assertEqual(p['snapshots'][-1],other)
    def test_combined_replay_budget_refuses_without_truncation(self):
        f=make('international');p=f['packet'];original=copy.deepcopy(p['snapshots'][-1]);p['snapshots']=p['snapshots'][:-1];p['crosswalks']=[]
        for number in range(2):
            cross=copy.deepcopy(original);cross['id']+=':wide:'+str(number);cross['payload']['id']+=':wide:'+str(number);entries=[]
            for i in range(64):
                e=copy.deepcopy(original['payload']['entries'][0]);e['id']+=':'+str(i);e['targets']=[code('urn:synthetic:scheme:wide','1',str(j)+':'+'x'*190) for j in range(16)];entries.append(e)
            cross['payload']['entries']=entries;cross['digest']=r.snapshot_digest(cross);p['snapshots'].append(cross);p['crosswalks'].append(r.pin(cross))
        f['host']=grant(p);before=r.encode(p);self.assertLess(len(before),r.LIMIT)
        with self.assertRaisesRegex(r.Invalid,'Canonical value exceeds1MiB'):evaluate(f)
        self.assertEqual(r.encode(p),before)
    def test_partial_release_is_not_a_closed_world(self):
        f=make('startup');repin(f,'urn:synthetic:release:old',lambda d:d.update(complete=False,concepts=[]))
        self.assertEqual(evaluate(f)['outcome'],'insufficient-context')
    def test_duplicate_code_not_silently_deduplicated(self):
        f=make('startup');repin(f,'urn:synthetic:release:old',lambda d:d['concepts'].append(copy.deepcopy(d['concepts'][0])))
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_lexical_homonyms_do_not_merge(self):
        f=make('international');result=evaluate(f)
        source=f['packet']['snapshots'][3]['payload']['values'][0];target=result['candidate']
        self.assertEqual(source['code'],target['code']);self.assertNotEqual(source['scheme'],target['scheme'])
        self.assertEqual(result['assignments'][0]['subjectId'],'urn:synthetic:subject:1')
    def test_missing_scheme_is_never_label_resolved(self):
        f=make('startup');repin(f,'urn:synthetic:assignment:1',lambda d:d['values'][0].pop('scheme'))
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_lowercase_is_not_uppercase(self):
        f=make('startup');repin(f,'urn:synthetic:assignment:1',lambda d:d['values'][0].update(code='a'))
        self.assertEqual(evaluate(f)['outcome'],'does-not-conform')
    def test_approval_claim_needs_independent_host_ack(self):
        f=make('international');f['host']['approvals']=[]
        self.assertEqual(evaluate(f)['migrationDisposition'],'human-review-required')
    def test_changed_mapping_does_not_inherit_old_approval(self):
        f=make('international');repin(f,'urn:synthetic:crosswalk:1',lambda d:d['entries'][0]['targets'][0].update(code='B'))
        result=evaluate(f);self.assertIsNone(result['candidate']);self.assertFalse(result['alternatives'][0]['hostApprovalAcknowledged'])
    def test_scores_never_select(self):
        f=make('ai-team');a=evaluate(f);self.assertIsNone(a['candidate']);self.assertEqual([x['scoreAsClaimed'] for x in a['alternatives']],['0.99','0.98'])
    def test_profile_exclusion_does_not_hide_competitor(self):
        f=make('ai-team')
        repin(f,'urn:synthetic:crosswalk:1',lambda d:[e.update(state='approved',approver=ACTOR) for e in d['entries']])
        repin(f,'urn:synthetic:profile:target',lambda d:d.update(allowed=[d['allowed'][0]]))
        cross=next(s for s in f['packet']['snapshots'] if s['payload']['kind']=='crosswalk')
        f['host']['approvals']=[{'snapshotDigest':cross['digest'],'entryId':e['id'],'approver':ACTOR,'evidence':e['evidence'][0]} for e in cross['payload']['entries']]
        a=evaluate(f);self.assertIsNone(a['candidate']);self.assertEqual(len(a['alternatives']),2);self.assertEqual(a['alternatives'][1]['targets'][0]['eligibility'],'not-allowed')
    def test_split_union_not_pairwise_exact(self):
        f=make('international');repin(f,'urn:synthetic:crosswalk:1',lambda d:d['entries'][0].update(predicate='union-association',targets=[code('urn:synthetic:scheme:other-region','2',c) for c in ('A','B')]))
        a=evaluate(f);self.assertIsNone(a['candidate']);self.assertEqual(len(a['alternatives'][0]['targets']),2)
    def test_retirement_with_empty_target(self):
        f=make('international');repin(f,'urn:synthetic:crosswalk:1',lambda d:d['entries'][0].update(targets=[]))
        a=evaluate(f);self.assertIsNone(a['candidate']);self.assertEqual(a['alternatives'][0]['targets'],[])
    def test_empty_source_birth_is_preserved_in_packet(self):
        f=make('international');repin(f,'urn:synthetic:crosswalk:1',lambda d:d['entries'][0].update(sources=[]))
        before=r.encode(f['packet']);result=evaluate(f)
        self.assertIsNone(result['candidate']);self.assertEqual(r.encode(f['packet']),before)
        self.assertEqual(f['packet']['snapshots'][-1]['payload']['entries'][0]['sources'],[])
    def test_nonexact_mapping_never_promoted(self):
        for pred in ('closeMatch','broadMatch','narrowMatch','relatedMatch'):
            f=make('international');repin(f,'urn:synthetic:crosswalk:1',lambda d:d['entries'][0].update(predicate=pred))
            with self.subTest(predicate=pred):self.assertIsNone(evaluate(f)['candidate'])
    def test_wrong_jurisdiction_not_globally_reused(self):
        f=make('international');f['packet']['jurisdiction']='synthetic-region-B';f['host']['packetDigest']=r.digest(f['packet'])
        a=evaluate(f);self.assertIsNone(a['candidate']);self.assertTrue(any(c['rule']=='MAPPING-CONTEXT' for c in a['checks']))
    def test_chain_request_does_not_change_skos_semantics(self):
        f=make('international');f['packet']['inference']='chain-requested';f['host']['packetDigest']=r.digest(f['packet'])
        a=evaluate(f);self.assertEqual(a['migrationDisposition'],'unsupported-chain');self.assertIsNone(a['candidate'])
    def test_direct_mode_does_not_traverse_two_hop_correspondence(self):
        f=make('international')
        def chain(d):
            original=copy.deepcopy(d['entries'][0]);middle=code('urn:synthetic:scheme:international','1','B')
            d['entries'][0]['targets']=[middle];original['id']+=':second';original['sources']=[middle];d['entries'].append(original)
        repin(f,'urn:synthetic:crosswalk:1',chain)
        cross=next(s for s in f['packet']['snapshots'] if s['payload']['kind']=='crosswalk')
        f['host']['approvals']=[{'snapshotDigest':cross['digest'],'entryId':e['id'],'approver':ACTOR,'evidence':e['evidence'][0]} for e in cross['payload']['entries']]
        result=evaluate(f);self.assertIsNone(result['candidate']);self.assertEqual(len(result['alternatives']),1)
        self.assertEqual(result['alternatives'][0]['targets'][0]['code']['version'],'1')
    def test_merge_does_not_migrate_one_member_as_the_union(self):
        f=make('international');repin(f,'urn:synthetic:crosswalk:1',lambda d:d['entries'][0]['sources'].append(code('urn:synthetic:scheme:international','1','B')))
        cross=next(s for s in f['packet']['snapshots'] if s['payload']['kind']=='crosswalk');f['host']['approvals'][0]['snapshotDigest']=cross['digest']
        a=evaluate(f);self.assertIsNone(a['candidate']);self.assertEqual(len(a['alternatives'][0]['sources']),2)
    def test_selected_historical_correction_preserves_old_snapshot(self):
        f=make('startup');old=f['packet']['snapshots'][3];oldbytes=r.encode(old)
        new=copy.deepcopy(old);new['id']+=':correction';new['payload'].update(revision=2,corrects=r.pin(old),values=[code('urn:synthetic:scheme:startup','1','B')]);new['digest']=r.snapshot_digest(new)
        f['packet']['snapshots'].append(new);f['packet']['assignments']=[r.pin(new)];f['host']['packetDigest']=r.digest(f['packet'])
        self.assertEqual(evaluate(f)['outcome'],'conforms-to-local-profile');self.assertEqual(r.encode(old),oldbytes)
    def test_partial_crosswalk_cannot_prove_unique_candidate(self):
        f=make('international');repin(f,'urn:synthetic:crosswalk:1',lambda d:d.update(complete=False));cross=next(s for s in f['packet']['snapshots'] if s['payload']['kind']=='crosswalk');f['host']['approvals'][0]['snapshotDigest']=cross['digest']
        a=evaluate(f);self.assertIsNone(a['candidate']);self.assertEqual(a['outcome'],'insufficient-context')
    def test_wm_identifier_migration_refused(self):
        f=make('international');f['packet']['mode']='metamodel-migration';f['host']['packetDigest']=r.digest(f['packet'])
        self.assertEqual(evaluate(f)['migrationDisposition'],'refuse-model-id-migration')
    def test_retired_target_does_not_destroy_historical_membership(self):
        f=make('international');repin(f,'urn:synthetic:release:new',lambda d:d['concepts'][0].update(status='retired'))
        a=evaluate(f);self.assertEqual(a['assignments'][0]['sourceConformance'],'conforms');self.assertIsNone(a['candidate'])
    def test_nonselectable_target_rejected(self):
        f=make('international');repin(f,'urn:synthetic:release:new',lambda d:d['concepts'][0].update(selectable=False))
        self.assertIsNone(evaluate(f)['candidate'])
    def test_half_open_assignment_interval(self):
        f=make('startup');repin(f,'urn:synthetic:assignment:1',lambda d:d.update(validUntil=AT))
        self.assertEqual(evaluate(f)['assignments'][0]['sourceConformance'],'outside-valid-time')
    def test_unknown_future_capture_not_known_now(self):
        f=make('startup');s=f['packet']['snapshots'][3];s['capture']['at']='2026-09-23T00:00:00Z';s['digest']=r.snapshot_digest(s);f['packet']['assignments']=[r.pin(s)];f['host']['packetDigest']=r.digest(f['packet'])
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_read_permission_is_exact_actor_purpose_packet(self):
        for change in ('actor','purpose','packetDigest','dimensionId'):
            f=make('startup');f['host'][change]='sha256:'+'0'*64 if change=='packetDigest' else 'different'
            with self.subTest(change=change),self.assertRaisesRegex(r.Denied,'NOT AUTHORIZED'):evaluate(f)
    def test_expired_grant_cannot_replay_read(self):
        f=make('startup');f['host']['validUntil']=AT
        with self.assertRaises(r.Denied):evaluate(f)
    def test_tamper_fails_even_if_read_grant_reissued(self):
        f=make('startup');f['packet']['snapshots'][0]['payload']['concepts'][0]['definition']='Changed meaning';f['host']['packetDigest']=r.digest(f['packet'])
        with self.assertRaises(r.Invalid):evaluate(f)
    def test_ambiguous_authoritative_revisions_not_recency_sorted(self):
        f=make('startup');old=f['packet']['snapshots'][3];new=copy.deepcopy(old);new['id']+=':revision2';new['payload'].update(revision=2,corrects=r.pin(old));new['digest']=r.snapshot_digest(new);f['packet']['snapshots'].append(new);f['packet']['assignments'].append(r.pin(new));f['host']['packetDigest']=r.digest(f['packet'])
        self.assertEqual(evaluate(f)['outcome'],'insufficient-context')
    def test_identical_review_and_json_roundtrip(self):
        f=make('international');a=evaluate(f);value={'packet':f['packet'],'assessment':a};before=r.encode(value)
        self.assertEqual(r.encode(evaluate(f)),r.encode(a));self.assertEqual(r.encode(r.migrate_snapshot(r.decode(before),r.VERSION)),before);self.assertFalse(r.inspect_snapshot(value)['authorized'])
    def test_changed_approval_changes_assessment_identity(self):
        f=make('international');a=evaluate(f);f['host']['approvals']=[];b=evaluate(f)
        self.assertNotEqual(a['assessmentId'],b['assessmentId']);self.assertEqual(a['packetDigest'],b['packetDigest'])
    def test_lossful_version_conversion_refused(self):
        f=make('startup');v={'packet':f['packet'],'assessment':evaluate(f)}
        with self.assertRaises(r.Invalid):r.migrate_snapshot(v,'0.0.1')
    def test_forged_assessment_cannot_pass_replay(self):
        f=make('ai-team');a=evaluate(f);a['candidate']=code('urn:synthetic:scheme:ai-team','2','A')
        with self.assertRaises(r.Invalid):r.inspect_snapshot({'packet':f['packet'],'assessment':a})
    def test_duplicate_json_and_floats_controls(self):
        for raw in (b'{"x":1,"x":2}',b'{"x":0.99}',b'{"x":"a\\nb"}',b'\xef\xbb\xbf{}'):
            with self.subTest(raw=raw),self.assertRaises(r.Invalid):r.decode(raw)
    def test_input_budget(self):
        with self.assertRaises(r.Invalid):r.decode(b' '*(2*r.LIMIT+1))
    def test_native_identity_is_assessment_not_classified_subject(self):
        f=make('startup');v={'packet':f['packet'],'assessment':evaluate(f)};obj,fact=r.native_records(v,AT)
        self.assertNotEqual(obj['objectId'],'urn:synthetic:subject:1');self.assertEqual(fact['subjectId'],obj['objectId']);self.assertTrue(r.validate_native_fact(fact)['valid'])
    def test_native_wrong_subject_or_digest_is_rejected(self):
        f=make('startup');v={'packet':f['packet'],'assessment':evaluate(f)};_,fact=r.native_records(v,AT)
        for changed in ('subject','digest','rank'):
            bad=copy.deepcopy(fact)
            if changed=='subject':bad['subjectId']='urn:synthetic:subject:1'
            elif changed=='digest':bad['provenance']['snapshotDigest']='sha256:'+'0'*64
            else:bad['authority']['rank']=False
            with self.subTest(changed=changed),self.assertRaises(r.Invalid):r.validate_native_fact(bad)
    def test_native_no_supersession_or_capture_before_evidence(self):
        f=make('startup');v={'packet':f['packet'],'assessment':evaluate(f)}
        with self.assertRaises(r.Invalid):r.native_records(v,START)
        _,fact=r.native_records(v,AT);fact['supersedes']=['urn:synthetic:old']
        with self.assertRaises(r.Invalid):r.validate_native_fact(fact)

if __name__=='__main__':
    if sys.flags.optimize:raise SystemExit('Do not run tests with Python -O')
    start=time.perf_counter();suite=unittest.defaultTestLoader.loadTestsFromTestCase(ReviewTests);result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'format':'vercy-classification-tests','passed':result.testsRun-len(result.failures)-len(result.errors),'failed':len(result.failures)+len(result.errors),'seconds':round(time.perf_counter()-start,3),'buildId':r.build_id(),'sourceDigests':{n:hashlib.sha256((Path(__file__).parent/n).read_bytes()).hexdigest() for n in ('classification_review.py','classification.schema.json','fixtures.py','test_classification.py')},'testNames':sorted(n for n in dir(ReviewTests) if n.startswith('test_')),'limits':'Original local dialect; no remote standard conformance or production authority validation.'}
    (Path(__file__).parent/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    raise SystemExit(not result.wasSuccessful())
