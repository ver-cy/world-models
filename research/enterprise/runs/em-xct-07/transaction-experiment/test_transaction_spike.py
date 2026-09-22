"""Behavioral research experiments, not metamodel acceptance or provider audit."""
import copy, hashlib, json, sqlite3, tempfile, unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from pathlib import Path
import transaction_spike as t

class Transactions(unittest.TestCase):
    def setUp(self):
        area=Path(__file__).parent/'spike-temporary';area.mkdir(exist_ok=True)
        self.tmp=tempfile.TemporaryDirectory(prefix='vercy-action-spike-',dir=area);self.path=Path(self.tmp.name)/'demo.sqlite';self.req=t.create_fixture(self.path);self.actor=self.req['actor']
    def tearDown(self): self.tmp.cleanup()
    def send(self,req=None,now=100,**kw): return t.submit(self.path,req or self.req,self.actor,now,**kw)
    def rejected(self,req,reason):
        before=t.inspect_fixture(self.path)
        with self.assertRaisesRegex(t.Refused,'^'+reason+'$'):self.send(req)
        self.assertEqual(before,t.inspect_fixture(self.path))
    def test_retry_one_effect(self):
        a=self.send();b=self.send(now=101);self.assertEqual(a['receipt'],b['receipt']);self.assertTrue(b['replay']);self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_changed_payload_same_key(self):
        self.send();q=copy.deepcopy(self.req);q['value']=['beta','alpha'];self.rejected(q,'key-conflict')
    def test_key_order_preserves_intent(self):
        a=self.send();b=self.send(dict(reversed(list(self.req.items()))));self.assertEqual(a['receipt'],b['receipt'])
    def test_fresh_policy_observation_not_intent(self):
        a=self.send();t.policy_change(self.path,until=1100);b=self.send(now=200);self.assertEqual(a['receipt'],b['receipt'])
    def test_proposal_no_effect(self):
        q=copy.deepcopy(self.req);q['mode']='proposal';self.rejected(q,'proposal-not-execution')
    def test_document_permission_reference_not_authority(self):
        q=copy.deepcopy(self.req);q['permission_ref']='Publish';self.rejected(q,'shape')
    def test_revoked_execution(self):
        t.policy_change(self.path,execute=False);self.rejected(self.req,'not-authorized')
    def test_revoked_before_retry_preserves_effect(self):
        self.send();t.policy_change(self.path,execute=False);self.rejected(self.req,'not-authorized');self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_cached_read_denied(self):
        self.send();t.policy_change(self.path,read=False)
        with self.assertRaisesRegex(t.Refused,'not-authorized'):t.read_result(self.path,self.req,self.actor,101)
        self.assertEqual(self.send(now=102),{'outcome':'withheld'});self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_execute_without_read_commits_withheld(self):
        t.policy_change(self.path,read=False);self.assertEqual(self.send(),{'outcome':'withheld'});self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_read_right_survives_execute_revocation(self):
        a=self.send();t.policy_change(self.path,execute=False);self.assertEqual(t.read_result(self.path,self.req,self.actor,101)['receipt'],a['receipt'])
    def test_scope_fields(self):
        for k in ['dimension','executor','epoch','definition','resource']:
            with self.subTest(k=k):q=copy.deepcopy(self.req);q[k]+='-wrong';self.rejected(q,'scope')
    def test_authority_party_and_purpose(self):
        for k in ['actor','principal','purpose']:
            with self.subTest(k=k):q=copy.deepcopy(self.req);q[k]+='-wrong';self.rejected(q,'not-authorized')
    def test_wrong_session(self):
        with self.assertRaisesRegex(t.Refused,'not-authorized'):t.submit(self.path,self.req,'urn:demo:impostor',100)
        self.assertEqual(t.inspect_fixture(self.path)['effects'],0)
    def test_expiration(self):
        with self.assertRaisesRegex(t.Refused,'expired-request'):self.send(now=900)
        with self.assertRaisesRegex(t.Refused,'not-authorized'):self.send(now=1000)
        self.assertEqual(t.inspect_fixture(self.path)['effects'],0)
    def test_stale_resource_and_replay_after_intervening_write(self):
        a=self.send();q=copy.deepcopy(self.req);q.update(key='second',revision=1,value=['newer']);self.send(q)
        self.assertEqual(self.send()['receipt'],a['receipt']);self.assertEqual(t.inspect_fixture(self.path)['value'],['newer'])
        q.update(key='third',revision=0);self.rejected(q,'stale-resource')
    def test_rolls_back_effect_when_receipt_not_written(self):
        before=t.inspect_fixture(self.path)
        with self.assertRaisesRegex(RuntimeError,'injected-before-commit'):self.send(failpoint='between-effect-and-receipt')
        self.assertEqual(before,t.inspect_fixture(self.path));self.send();self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_unknown_to_caller_after_commit(self):
        with self.assertRaises(t.ResponseLost):self.send(failpoint='after-commit-before-response')
        a=t.read_result(self.path,self.req,self.actor,101);b=self.send(now=102);self.assertEqual(a['receipt'],b['receipt']);self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_two_independent_connections(self):
        with ThreadPoolExecutor(max_workers=2) as pool:out=list(pool.map(lambda _:self.send(),range(2)))
        self.assertEqual(out[0]['receipt'],out[1]['receipt']);self.assertEqual(sum(x['replay'] for x in out),1);self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_retired_key_never_blank(self):
        self.send();t.retire_key(self.path,self.req['key']);self.rejected(self.req,'retired-key');self.assertEqual(t.inspect_fixture(self.path)['effects'],1)
    def test_missing_database_does_not_create_history(self):
        absent=Path(self.tmp.name)/'missing.sqlite'
        with self.assertRaises(sqlite3.OperationalError):t.submit(absent,self.req,self.actor,100)
        self.assertFalse(absent.exists())
    def test_three_profiles_and_delegation_admission(self):
        for profile in ['startup','matrix','ai']:
            with self.subTest(profile=profile):
                p=Path(self.tmp.name)/(profile+'.sqlite');q=t.create_fixture(p,profile);a=t.submit(p,q,q['actor'],100);self.assertEqual(a['outcome'],'observed')
                if profile!='startup':
                    t.policy_change(p,delegated=False)
                    with self.assertRaisesRegex(t.Refused,'not-authorized'):t.submit(p,q,q['actor'],101)
    def test_compensation_is_new_request_with_version_guard(self):
        self.send();q=copy.deepcopy(self.req);q.update(key='compensation',revision=1,value=['draft']);self.send(q);self.assertEqual(t.inspect_fixture(self.path)['effects'],2);self.assertEqual(t.inspect_fixture(self.path)['value'],['draft'])
    def test_original_intent_retained_after_retry(self):
        self.send();self.send(now=101)
        with closing(sqlite3.connect(self.path)) as c:raw=c.execute('SELECT body FROM requests').fetchone()[0]
        self.assertEqual(raw,t.encoded(self.req))

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Transactions);result=unittest.TextTestRunner(verbosity=1).run(suite)
    root=Path(__file__).parent
    report={'scope':'Research-only transaction spike; NOT Vercy installation or metamodel acceptance','tests':result.testsRun,'passed':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'sqliteVersion':sqlite3.sqlite_version,'files':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ['transaction_spike.py','test_transaction_spike.py']},'limits':['Trusted test session, policy, clock and fixture administration, no real authentication','Single local SQLite store, no external effect or native Vercy event export','Exception injection and independent connections, not power-loss or OS-crash verification','Compensation test changes a value using a new key; full compensation relationship/lifecycle not implemented','Unknown to caller after commit reconciles with retained store; missing record is not proof about a lost/replaced store','No full schema, whole-object specification, audit, publication or production authorization claim']}
    (root/'transaction-spike-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
