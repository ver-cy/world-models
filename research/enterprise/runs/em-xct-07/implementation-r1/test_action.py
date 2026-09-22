import copy
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
import action as a
from fixtures import fixture,descriptive,NOW,ALL
from history import validate_snapshot
from native import export_snapshot,verify_export,records

class ActionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
        self.x,self.i,self.policy,self.definition=fixture(self.root/'state.db')
        self.key='key-first-0001'
    def tearDown(self): self.tmp.cleanup()
    def send(self,intent=None,key=None,now=NOW,**opts):
        return self.x.dispatch(a.encoded(intent or self.i),key or self.key,self.i['actorId'],now,**opts)
    def snapshot(self,now=NOW):
        s=self.x.snapshot(now); validate_snapshot(s); return s
    def actions(self,allowed,now=NOW,*,side=None):
        p=copy.deepcopy(self.policy)
        for which in ([side] if side else ['principalScope','delegateScope']): p[0][which]['actions']=allowed
        self.x.set_policy(p,now); return p
    def pending(self):
        self.actions(['submit','read','cancel','observe']); self.assertEqual(self.send()['status'],'current-execution-denied')
    def committed(self):
        r=self.send(); self.assertEqual(r['status'],'committed'); return r
    def changed(self,**fields):
        i=copy.deepcopy(self.i); i.update(fields); return i

    def test_three_distinct_profiles(self):
        for name in ('matrix','ai-service'):
            x,i,p,d=fixture(self.root/(name+'.db'),name)
            self.assertNotEqual(i['actorId'],i['principalId'])
            self.assertEqual(x.dispatch(a.encoded(i),self.key,i['actorId'],NOW)['status'],'committed')
            self.assertEqual(validate_snapshot(x.snapshot(NOW))['effects'],1)
    def test_commit_readback_order_and_duplicates(self):
        r=self.committed(); self.assertEqual(r['receipt']['payload']['afterLabels'],['alpha','beta','alpha'])
        s=self.snapshot(); self.assertEqual(len(s['requests']),1); self.assertEqual(len(s['resources']),2)
        self.assertEqual(r,self.x.lookup(self.key,self.i['actorId'],NOW))
    def test_repeat_after_intervening_update_preserves_original_receipt(self):
        original=self.committed()
        later=self.changed(expectedRevision=1,parameters={'labels':['later']}); self.send(later,'key-second-0002')
        self.assertEqual(self.send(),original); self.assertEqual(self.snapshot()['resources'][-1]['labels'],'["later"]')
    def test_array_reorder_same_key_conflicts(self):
        self.committed(); changed=self.changed(parameters={'labels':['beta','alpha','alpha']})
        self.assertEqual(self.send(changed)['status'],'key-conflict'); self.assertEqual(validate_snapshot(self.snapshot())['effects'],1)
    def test_whitespace_and_property_order_do_not_change_intent(self):
        original=self.committed()
        raw=json.dumps(dict(reversed(list(self.i.items()))),indent=4)
        self.assertEqual(self.x.dispatch(raw,self.key,self.i['actorId'],NOW),original)
    def test_host_request_id_not_part_of_retry_digest(self):
        r=self.committed(); self.assertNotIn('requestId',self.i); self.assertEqual(r['intentDigest'],a.digest(self.i))
        forged=self.changed(requestId=r['requestId']); self.assertEqual(self.send(forged),a.WITHHELD)
    def test_duplicate_wire_keys_float_bool_and_surrogate_refused(self):
        good=a.encoded(self.i).decode()
        bads=[good.replace('"expectedRevision":0','"expectedRevision":0,"expectedRevision":1'),
              good.replace('"expectedRevision":0','"expectedRevision":0.0'),
              good.replace('"expectedRevision":0','"expectedRevision":true'),
              good.replace('"alpha"','"\\ud800"'),good.replace('"expectedRevision":0','"expectedRevision":NaN')]
        for raw in bads: self.assertEqual(self.x.dispatch(raw,self.key,self.i['actorId'],NOW),a.WITHHELD)
        self.assertEqual(self.snapshot()['requests'],[])
    def test_wire_unicode_preserved_without_normalization(self):
        value={'supplementary':'\U0001F680','é':['e\u0301','é']}
        self.assertEqual(a.parse(a.encoded(value)),value)
        self.assertNotEqual(a.digest({'x':'e\u0301'}),a.digest({'x':'é'}))
    def test_actor_spoof_and_other_dimension_refused(self):
        self.assertEqual(self.x.dispatch(a.encoded(self.i),self.key,'urn:synthetic:intruder',NOW),a.WITHHELD)
        self.assertEqual(self.send(self.changed(dimensionId='urn:synthetic:other')),a.WITHHELD)
        self.assertEqual(self.snapshot()['requests'],[])
    def test_no_submit_permission_means_no_pending_creation(self):
        self.actions(['execute','read']); self.assertEqual(self.send(),a.WITHHELD); self.assertEqual(self.snapshot()['requests'],[])
    def test_pending_denial_can_be_retried_with_current_rights(self):
        self.pending(); rid=self.snapshot()['requests'][0]['requestId']
        self.actions(ALL); self.assertEqual(self.committed()['requestId'],rid)
        self.assertEqual(validate_snapshot(self.snapshot())['effects'],1)
    def test_principal_and_delegate_intersection(self):
        for side in ('principalScope','delegateScope'):
            self.actions(['submit','read'],side=side); self.assertEqual(self.send()['status'],'current-execution-denied')
        self.assertEqual(validate_snapshot(self.snapshot())['effects'],0)
    def test_scope_mismatch_cannot_be_combined_between_rules(self):
        p=copy.deepcopy(self.policy); p[0]['principalScope']['actions']=['submit','read']; p[0]['delegateScope']['actions']=ALL
        q=copy.deepcopy(self.policy[0]); q['principalScope']['actions']=ALL; q['delegateScope']['actions']=['submit','read']; p.append(q)
        self.x.set_policy(p,NOW); self.assertEqual(self.send()['status'],'current-execution-denied')
    def test_exact_scope_axes(self):
        for field,value in [('audience','urn:synthetic:other'),('purpose','other'),('resourceId','urn:synthetic:other'),('principalId','urn:synthetic:other')]:
            self.assertEqual(self.send(self.changed(**{field:value})),a.WITHHELD)
        self.assertEqual(self.snapshot()['requests'],[])
    def test_delegated_boolean_and_inconsistent_mode_refused(self):
        p=copy.deepcopy(self.policy); p[0]['delegated']=True
        with self.assertRaises(a.Refused): self.x.set_policy(p,NOW)
        p=copy.deepcopy(self.policy); p[0]['mode']='direct-representation'
        with self.assertRaises(a.Refused): self.x.set_policy(p,NOW)
    def test_policy_scope_time_is_half_open(self):
        p=copy.deepcopy(self.policy)
        for side in ('principalScope','delegateScope'): p[0][side]['validUntil']=NOW+1
        self.x.set_policy(p,NOW); self.committed()
        self.assertEqual(self.x.lookup(self.key,self.i['actorId'],NOW+1),a.WITHHELD)
    def test_expiry_no_first_effect_at_boundary(self):
        r=self.send(now=self.i['expiresAt']); self.assertEqual(r['status'],'expired')
        self.assertEqual(validate_snapshot(self.snapshot(self.i['expiresAt']))['effects'],0)
    def test_committed_request_never_turns_expired(self):
        original=self.committed(); self.assertEqual(self.send(now=NOW+101),original)
        self.assertEqual(self.snapshot(NOW+101)['requests'][0]['state'],'committed')
    def test_current_execute_revocation_does_not_hide_permitted_lookup(self):
        original=self.committed(); self.actions(['read'])
        self.assertEqual(self.send()['status'],'current-execution-denied')
        self.assertEqual(self.x.lookup(self.key,self.i['actorId'],NOW),original)
        self.snapshot()
    def test_execute_without_read_changes_resource_but_always_withholds(self):
        self.actions(['submit','execute']); self.assertEqual(self.send(),a.WITHHELD)
        self.assertEqual(self.send(),a.WITHHELD); self.assertEqual(self.x.lookup(self.key,self.i['actorId'],NOW),a.WITHHELD)
        self.assertEqual(validate_snapshot(self.snapshot())['effects'],1)
    def test_all_denied_disclosure_shapes_are_equal(self):
        self.committed(); self.actions(['submit','execute','cancel','observe'])
        calls=[self.send(),self.send(self.changed(parameters={'labels':['conflict']})),self.x.lookup('absent-key-000',self.i['actorId'],NOW),
               self.x.cancel('absent-key-000',self.i['actorId'],NOW),self.x.observe(self.key,self.i['actorId'],NOW,'caller-unknown','Lost response'),
               self.x.dispatch('{bad',self.key,self.i['actorId'],NOW)]
        self.x.retire_key(self.key,self.i['actorId'],NOW); calls.append(self.send())
        self.assertTrue(all(x==a.WITHHELD for x in calls)); self.snapshot()
    def test_conflict_requires_read_for_original_and_new_context(self):
        self.committed(); changed=self.changed(purpose='different-purpose')
        self.assertEqual(self.send(changed),a.WITHHELD)
    def test_definition_revision_cannot_be_overwritten(self):
        self.x.add_definition(self.definition,NOW)
        d=copy.deepcopy(self.definition); d['name']='Changed silently'
        with self.assertRaises(a.Refused): self.x.add_definition(d,NOW)
    def test_executable_text_cannot_change_the_fixed_effect(self):
        d=copy.deepcopy(self.definition); d.update(version='malicious',effectBoundary='send money')
        with self.assertRaises(a.Refused): self.x.add_definition(d,NOW)
    def test_definition_resource_identity_collision_rejected(self):
        with self.assertRaises(a.Refused): self.x.add_resource(self.definition['definitionId'],[],NOW)
        d=copy.deepcopy(self.definition); d['definitionId']=self.i['resourceId']
        with self.assertRaises(a.Refused): self.x.add_definition(d,NOW)
    def test_policy_freshness_order_at_same_second_is_validated(self):
        self.pending(); self.actions(ALL); self.committed(); s=self.snapshot()
        v=copy.deepcopy(s); trial=next(e for e in reversed(v['events']) if e['kind']=='try')
        trial['payload']['decision']['policyRevision']-=1
        with self.assertRaises(a.Refused): validate_snapshot(v)
    def test_descriptive_definition_catalogued_but_not_executed(self):
        d=descriptive(self.definition); self.x.add_definition(d,NOW)
        i=self.changed(definition=a.definition_ref(d)); p=copy.deepcopy(self.policy)
        for side in ('principalScope','delegateScope'): p[0][side]['definition']=i['definition']
        self.x.set_policy(p,NOW)
        self.assertEqual(self.send(i)['status'],'definition-not-executable')
        s=self.snapshot(); self.assertEqual(len(s['definitions']),2); self.assertEqual(s['requests'],[])
        self.assertEqual(len(records(s)),3)
    def test_definition_retirement_rechecked_at_execution(self):
        self.pending(); self.actions(ALL); self.x.retire_definition(self.i['definition'],NOW)
        self.assertEqual(self.send()['status'],'current-execution-denied'); self.snapshot()
    def test_definition_deadline_rechecked(self):
        d=copy.deepcopy(self.definition); d['version']='short'; d['validUntil']=NOW+1
        self.x.add_definition(d,NOW); i=self.changed(definition=a.definition_ref(d)); p=copy.deepcopy(self.policy)
        for side in ('principalScope','delegateScope'): p[0][side]['definition']=i['definition']
        self.x.set_policy(p,NOW); self.assertEqual(self.send(i,now=NOW+1)['status'],'current-execution-denied'); self.snapshot(NOW+1)
    def test_stale_resource_rejects_terminally(self):
        self.committed(); r=self.send(key='key-stale-0002'); self.assertEqual(r['status'],'rejected-precondition'); self.snapshot()
    def test_transaction_rollback_before_and_after_effect(self):
        for fault in ('before-effect','after-effect'):
            self.assertEqual(self.send(_fault=fault),a.WITHHELD)
            s=self.snapshot(); self.assertEqual(s['requests'],[]); self.assertEqual(s['events'],[]); self.assertEqual(len(s['resources']),1)
        self.committed()
    def test_lost_response_reconciles_same_key(self):
        with self.assertRaises(a.ResponseLost): self.send(_fault='after-commit')
        lookup=self.x.lookup(self.key,self.i['actorId'],NOW); self.assertEqual(lookup['status'],'committed')
        self.assertEqual(self.send(),lookup); self.assertEqual(validate_snapshot(self.snapshot())['effects'],1)
    def test_concurrent_duplicate_requests_one_effect(self):
        barrier=threading.Barrier(6)
        def run(_): barrier.wait(); return self.send()
        with ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(run,range(6)))
        self.assertTrue(all(r==results[0] and r['status']=='committed' for r in results))
        self.assertEqual(validate_snapshot(self.snapshot())['effects'],1)
    def test_cancel_and_execute_race_has_one_terminal_outcome(self):
        self.pending(); self.actions(ALL); barrier=threading.Barrier(2)
        def execute(): barrier.wait(); return self.send()
        def cancel(): barrier.wait(); return self.x.cancel(self.key,self.i['actorId'],NOW)
        with ThreadPoolExecutor(max_workers=2) as pool:
            f=pool.submit(execute); g=pool.submit(cancel); f.result(); g.result()
        s=self.snapshot(); state=s['requests'][0]['state']; self.assertIn(state,('committed','cancelled'))
        self.assertEqual(validate_snapshot(s)['effects'],int(state=='committed'))
    def test_cancel_pending_then_retry_cannot_execute(self):
        self.pending(); self.assertEqual(self.x.cancel(self.key,self.i['actorId'],NOW)['status'],'cancelled')
        self.actions(ALL); self.assertEqual(self.send()['status'],'cancelled'); self.snapshot()
    def test_cancel_after_commit_preserves_receipt(self):
        original=self.committed(); self.assertEqual(self.x.cancel(self.key,self.i['actorId'],NOW),original); self.snapshot()
    def test_compensation_new_request_restores_previous_value(self):
        original=self.committed(); receipt=original['receipt']
        i=self.changed(expectedRevision=1,parameters={'labels':['draft']},compensatesReceiptId=receipt['eventId'])
        result=self.send(i,'key-compensate-0002'); self.assertEqual(result['status'],'committed')
        self.assertEqual(self.send(),original); self.assertEqual(validate_snapshot(self.snapshot())['effects'],2)
    def test_compensation_refuses_intervening_update(self):
        receipt=self.committed()['receipt']; self.send(self.changed(expectedRevision=1,parameters={'labels':['intervening']}),'key-other-0002')
        i=self.changed(expectedRevision=2,parameters={'labels':['draft']},compensatesReceiptId=receipt['eventId'])
        self.assertEqual(self.send(i,'key-compensate-0003')['status'],'rejected-precondition'); self.snapshot()
    def test_compensation_refuses_wrong_before_value(self):
        receipt=self.committed()['receipt']; i=self.changed(expectedRevision=1,parameters={'labels':['invented']},compensatesReceiptId=receipt['eventId'])
        self.assertEqual(self.send(i,'key-compensate-0002')['status'],'rejected-precondition'); self.snapshot()
    def test_observation_correction_is_append_only_not_effect_undo(self):
        original=self.committed()
        first=self.x.observe(self.key,self.i['actorId'],NOW,'caller-unknown','Original response lost')['event']
        correction=self.x.observe(self.key,self.i['actorId'],NOW,'caller-observed-success','Later response received',first['eventId'])
        self.assertEqual(correction['status'],'recorded'); self.assertEqual(self.x.lookup(self.key,self.i['actorId'],NOW),original)
        self.assertEqual(self.x.observe(self.key,self.i['actorId'],NOW,'caller-observed-failure','Fork',first['eventId']),a.WITHHELD)
        s=self.snapshot(); self.assertIn(first,s['events']); self.assertEqual(validate_snapshot(s)['effects'],1)
    def test_receipt_cannot_be_observation_predecessor(self):
        r=self.committed(); self.assertEqual(self.x.observe(self.key,self.i['actorId'],NOW,'caller-unknown','Invalid predecessor',r['receipt']['eventId']),a.WITHHELD); self.snapshot()
    def test_key_retirement_preserves_nonreuse_tombstone(self):
        self.committed(); self.x.retire_key(self.key,self.i['actorId'],NOW); self.x.retire_key(self.key,self.i['actorId'],NOW)
        self.assertEqual(self.send()['status'],'key-retired'); self.assertEqual(validate_snapshot(self.snapshot())['effects'],1)
    def test_pending_key_cannot_be_purged(self):
        self.pending()
        with self.assertRaises(a.Refused): self.x.retire_key(self.key,self.i['actorId'],NOW)
    def test_missing_store_not_recreated_and_wrong_epoch_refused(self):
        other=a.Executor(self.root/'missing.db','epoch.missing')
        self.assertEqual(other.lookup(self.key,self.i['actorId'],NOW),a.WITHHELD); self.assertFalse(other.path.exists())
        other=a.Executor(self.x.path,'epoch.wrong'); self.assertEqual(other.lookup(self.key,self.i['actorId'],NOW),a.WITHHELD)
    def test_backward_clock_rejected(self):
        self.committed(); self.assertEqual(self.send(now=NOW-1),a.WITHHELD)
    def test_coherent_restore_is_explicitly_not_detectable(self):
        backup=self.root/'older.db'; shutil.copyfile(self.x.path,backup); self.committed()
        restored=a.Executor(backup,self.x.expected_epoch)
        # This demonstrates a LIMIT, not a safety success: same epoch accepts old history.
        s=restored.snapshot(NOW); self.assertEqual(validate_snapshot(s)['effects'],0)
        self.assertEqual(restored.dispatch(a.encoded(self.i),self.key,self.i['actorId'],NOW)['status'],'committed')
    def test_history_tampering_rejected(self):
        self.committed(); s=self.snapshot()
        variants=[]
        v=copy.deepcopy(s); v['events'][-1]['payload']['afterLabels']=['forged']; variants.append(v)
        v=copy.deepcopy(s); v['requests'][0]['state']='pending'; variants.append(v)
        v=copy.deepcopy(s); v['events']=v['events'][1:]; variants.append(v)
        v=copy.deepcopy(s); v['events'][2]['payload']['decision']['allowed']=False; variants.append(v)
        v=copy.deepcopy(s); v['events'][2]['payload']['decision']['policyRevision']=0; variants.append(v)
        v=copy.deepcopy(s); v['resources'][-1]['labels']='["forged"]'; variants.append(v)
        v=copy.deepcopy(s); v['requests'][0]['intent']['parameters']['labels'].reverse(); v['requests'][0]['intent']['parameters']['labels'].append('bad'); variants.append(v)
        for v in variants:
            with self.assertRaises(a.Refused): validate_snapshot(v)
    def test_export_interruption_recovery_and_exact_readback(self):
        self.committed(); s=self.snapshot(); target=self.root/'export'
        with self.assertRaises(a.Refused): export_snapshot(s,target,_fail_after=3)
        with self.assertRaises(a.Refused): verify_export(target)
        result=export_snapshot(s,target); self.assertEqual(result['effects'],1)
        self.assertEqual(export_snapshot(s,target),result)
    def test_export_missing_extra_and_modified_files_rejected(self):
        self.committed(); target=self.root/'export'; export_snapshot(self.snapshot(),target)
        extra=target/'unexpected.txt'; extra.write_text('unexpected')
        with self.assertRaises(a.Refused): verify_export(target)
        extra.unlink(); chosen=next((target/'records').glob('evt*.json')); raw=chosen.read_bytes(); chosen.write_bytes(raw+b' ')
        with self.assertRaises(a.Refused): verify_export(target)
        chosen.write_bytes(raw); chosen.unlink()
        with self.assertRaises(a.Refused): verify_export(target)
    def test_export_changed_snapshot_does_not_overwrite(self):
        self.committed(); target=self.root/'export'; export_snapshot(self.snapshot(),target)
        with self.assertRaises(a.Refused): export_snapshot(self.snapshot(),target)

if __name__=='__main__': unittest.main(verbosity=2)
