# Missing-test supplement to the accepted focused audit
No tools or web. Your previous response reported test_authority.py truncated after test_no_authority in the large attachment. Here is the COMPLETE unchanged 53-test source as plain chat text, plus adoption-limit clarifications directly drawn from Claude's final holds. No implementation, schema, own spec or native acceptance code changed after the accepted focused audit. Check the previously unread successor-writer, closure, extension and negative cases; do not claim to execute tests. Confirm END OF TEST SUPPLEMENT visible and give a concise supplemental verdict/any concrete defect. This is a review, not publication authorization.

## test_authority.py
```
import copy,json,unittest
from pathlib import Path
import authority as a
P=Path(__file__).resolve().parent
NOW='2026-09-21T12:00:00Z';START='2026-01-01T00:00:00Z';END='2027-01-01T00:00:00Z'
G='urn:synthetic:governor';W='urn:synthetic:writer';READ='urn:synthetic:reader'
D='urn:synthetic:dimension';S='urn:synthetic:scope';F='urn:synthetic:predicate';SUB='urn:synthetic:subject'
def config():return {'id':'urn:synthetic:config','dimension':D,'validFrom':START,'validUntil':END,'governors':[{'actor':G,'scope':S,'predicate':F}],'readers':[READ],'purposes':['governance-review']}
def policy():
    return {'id':'urn:synthetic:authority','dimension':D,'scope':S,'predicate':F,'governs':'values','definitionAuthorityRef':'urn:synthetic:definition-owner-record','change':'genesis','revision':1,'previousDigest':None,'recordedAt':'2026-09-21T10:00:00Z','validFrom':START,'validUntil':END,'evidence':['urn:synthetic:appointment'],'issuedBy':G,'accountable':'urn:synthetic:owner','state':'active','stewardships':[{'id':'urn:synthetic:stewardship','party':'urn:synthetic:steward','duties':['resolve-conflict'],'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:mandate']}],'rules':[{'id':'urn:synthetic:rule:'+s,'source':'urn:synthetic:source:'+s,'priority':0,'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:rule-evidence']} for s in ['a','b']],'writeGrants':[{'id':'urn:synthetic:write:'+s,'source':'urn:synthetic:source:'+s,'writers':[W],'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:write-evidence']} for s in ['a','b']]}
def observation(n=1,value='A'):
    return {'id':'urn:synthetic:observation:'+str(n),'dimension':D,'scope':S,'predicate':F,'change':'genesis','revision':1,'previousDigest':None,'recordedAt':'2026-09-21T10:00:0'+str(n)+'Z','validFrom':START,'validUntil':END,'evidence':['urn:synthetic:evidence:'+str(n)],'subject':SUB,'source':'urn:synthetic:source:'+('a' if n==1 else 'b'),'writer':W,'state':'asserted','value':{'datatype':'urn:synthetic:string','lexical':value}}
def fixture(profile='startup'):
    c=config();p=policy()
    if profile=='group':p['rules'][1]['priority']=10
    if profile=='ai-team':p['stewardships']=[]
    ledger=a.admit(a.empty(D),p,'authority',c,G,p['recordedAt'])
    for x in [observation(),observation(2,'B' if profile!='ai-team' else 'A')]:ledger=a.admit(ledger,x,'observation',c,W,x['recordedAt'])
    return c,ledger
def query(l,c,**kw):
    args=dict(actor=READ,purpose='governance-review',scope=S,predicate=F,subject=SUB,validAt=NOW,knownAt=NOW,now=NOW);args.update(kw)
    return a.evaluate(l,c,**args)
def revision(x,at='2026-09-21T10:01:00Z',**changes):
    y=copy.deepcopy(x);y.update(revision=x['revision']+1,previousDigest=a.digest(x),recordedAt=at,change='retraction' if changes.get('state')=='retracted' else 'correction');y.update(changes);return y
class Tests(unittest.TestCase):
    def setUp(self):self.c,self.l=fixture()
    def test_equal_conflict(self):
        r=query(self.l,self.c);self.assertEqual(r['status'],'contested');self.assertEqual(len(r['evidence']),2);self.assertEqual(r['routeTo'],['urn:synthetic:steward']);self.assertIsNone(r['value'])
    def test_lower_priority_late_csv(self):
        c,l=fixture('group');r=query(l,c);self.assertEqual(r['value']['lexical'],'A');self.assertEqual(len(r['observationIds']),2)
    def test_same_value_corroboration(self):
        c,l=fixture('ai-team');self.assertEqual(query(l,c)['status'],'preferred');self.assertEqual(query(l,c)['routeTo'],[])
    def test_reverse_import_receipts(self):
        l=a.empty(D);p=policy();l=a.admit(l,p,'authority',self.c,G,p['recordedAt'])
        for x in [dict(observation(2,'B'),recordedAt='2026-09-21T10:00:01Z'),dict(observation(),recordedAt='2026-09-21T10:00:02Z')]:l=a.admit(l,x,'observation',self.c,W,x['recordedAt'])
        left=query(l,self.c);right=query(self.l,self.c)
        for k in ['inputDigest','observationPins']:left.pop(k);right.pop(k)
        self.assertEqual(left,right)
    def test_owner_not_writer(self):
        x=observation(3);x['writer']='urn:synthetic:owner'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,x['writer'],x['recordedAt'])
    def test_steward_not_governor(self):
        x=policy();x['issuedBy']='urn:synthetic:steward'
        with self.assertRaises(a.Invalid):a.admit(a.empty(D),x,'authority',self.c,x['issuedBy'],x['recordedAt'])
    def test_confused_deputy(self):
        x=policy();x['issuedBy']=W
        with self.assertRaises(a.Invalid):a.admit(a.empty(D),x,'authority',self.c,W,x['recordedAt'])
    def test_no_authority(self):self.assertEqual(query(a.empty(D),self.c)['status'],'unknown')
    def test_no_observations(self):
        self.l['observations']=[];self.assertEqual(query(self.l,self.c)['reason'],'no-ranked-observation')
    def test_overlapping_authorities(self):
        p=policy();p['id']+=':other';p['recordedAt']='2026-09-21T10:02:00Z'
        for x in p['rules']+p['stewardships']+p['writeGrants']:x['id']+=':other'
        l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt']);self.assertEqual(query(l,self.c)['status'],'authority-contested')
        x=observation(3)
        with self.assertRaises(a.Invalid):a.admit(l,x,'observation',self.c,W,'2026-09-21T11:00:00Z')
    def test_ambiguous_rules(self):
        p=revision(self.l['authorities'][0]);r=copy.deepcopy(p['rules'][0]);r['id']+=':duplicate';p['rules'].append(r)
        l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt']);self.assertEqual(query(l,self.c)['reason'],'overlapping-source-rules')
    def test_ambiguous_write_grants(self):
        p=revision(self.l['authorities'][0]);r=copy.deepcopy(p['writeGrants'][0]);r['id']+=':duplicate';r['writers']=['urn:synthetic:other'];p['writeGrants'].append(r)
        l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt']);x=observation(3);x['source']='urn:synthetic:source:a';x['recordedAt']='2026-09-21T11:00:00Z'
        with self.assertRaises(a.Invalid):a.admit(l,x,'observation',self.c,W,x['recordedAt'])
    def test_priority_does_not_grant_write(self):
        p=revision(self.l['authorities'][0]);p['writeGrants']=[];l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt'])
        self.assertEqual(query(l,self.c)['status'],'contested')
        x=observation(3);x['recordedAt']='2026-09-21T11:00:00Z'
        with self.assertRaises(a.Invalid):a.admit(l,x,'observation',self.c,W,x['recordedAt'])
    def test_write_grant_does_not_grant_precedence(self):
        p=revision(self.l['authorities'][0]);p['rules']=[];l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt'])
        x=observation(3);x['recordedAt']='2026-09-21T11:00:00Z';l=a.admit(l,x,'observation',self.c,W,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'unknown')
    def test_replay_idempotent(self):
        self.assertEqual(a.admit(self.l,self.l['observations'][0],'observation',self.c,W,NOW),self.l)
    def test_conflicting_replay(self):
        x=observation();x['value']['lexical']='C'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
    def test_backdate_receipt(self):
        x=observation(3)
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
    def test_future_receipt(self):
        x=observation(3);x['recordedAt']='2026-09-22T00:00:00Z'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
    def test_head_order(self):
        x=observation(3);x['recordedAt']=self.l['observations'][0]['recordedAt']
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,x['recordedAt'])
    def test_correction_history(self):
        old=query(self.l,self.c);x=revision(self.l['observations'][1]);x['value']['lexical']='A'
        l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred')
        self.assertEqual(query(l,self.c,knownAt='2026-09-21T10:00:02Z')['status'],old['status']);self.assertEqual(len(l['observations']),3)
    def test_retraction_history(self):
        x=revision(self.l['observations'][1],state='retracted');l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred')
        self.assertEqual(query(l,self.c,knownAt='2026-09-21T10:00:02Z')['status'],'contested')
    def test_retroactive_rule(self):
        x=revision(self.l['authorities'][0]);x['rules'][1]['priority']=1
        l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred');self.assertEqual(query(l,self.c,knownAt='2026-09-21T10:00:02Z')['status'],'contested')
    def test_transfer_preserves_valid_history(self):
        cutoff='2026-10-01T00:00:00Z';x=revision(self.l['authorities'][0],change='closure');x['validUntil']=cutoff
        for part in x['rules']+x['stewardships']+x['writeGrants']:part['validUntil']=cutoff
        l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt']);new=policy();new['id']+=':successor';new['recordedAt']='2026-09-21T10:02:00Z';new['validFrom']=cutoff;new['accountable']='urn:synthetic:successor'
        for part in new['rules']+new['stewardships']+new['writeGrants']:part['id']+=':successor';part['validFrom']=cutoff
        l=a.admit(l,new,'authority',self.c,G,new['recordedAt']);self.assertEqual(query(l,self.c)['accountable'],'urn:synthetic:owner');self.assertEqual(query(l,self.c,validAt=cutoff)['accountable'],'urn:synthetic:successor')
    def test_unknown_source_retained(self):
        x=revision(self.l['authorities'][0]);x['rules']=x['rules'][:1];l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt']);r=query(l,self.c);self.assertEqual(len(r['unrankedObservationIds']),1);self.assertEqual(len(r['evidence']),2)
    def test_denied_no_data(self):
        with self.assertRaisesRegex(a.Denied,'^Read denied$'):query({'secret':'bad'},self.c,actor='urn:synthetic:intruder')
    def test_purpose_denied(self):
        with self.assertRaises(a.Denied):query(self.l,self.c,purpose='advertising')
    def test_expired_root(self):
        with self.assertRaises(a.Invalid):query(self.l,self.c,now=END)
    def test_future_knowledge(self):
        with self.assertRaises(a.Invalid):query(self.l,self.c,knownAt=END)
    def test_cross_dimension(self):
        self.l['dimension']='urn:wrong'
        with self.assertRaises(a.Invalid):query(self.l,self.c)
    def test_scope_shopping(self):
        x=observation(3);x['scope']='urn:ungranted'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,x['recordedAt'])
    def test_policy_scope(self):
        x=policy();x['predicate']='urn:ungranted'
        with self.assertRaises(a.Invalid):a.admit(a.empty(D),x,'authority',self.c,G,x['recordedAt'])
    def test_value_not_coerced(self):
        self.l['observations'][0]['value']['lexical']='01';self.l['observations'][1]['value']['lexical']='1';self.assertEqual(query(self.l,self.c)['status'],'contested')
    def test_same_source_conflict(self):
        self.l['observations'][1]['source']=self.l['observations'][0]['source'];self.assertEqual(query(self.l,self.c)['status'],'contested')
    def test_future_steward(self):
        self.l['authorities'][0]['stewardships'][0]['validFrom']='2026-10-01T00:00:00Z';r=query(self.l,self.c);self.assertEqual(r['status'],'contested');self.assertEqual(r['routeTo'],[])
    def test_exclusive_interval_end(self):
        self.assertEqual(query(self.l,self.c,validAt=END)['status'],'unknown')
    def test_expired_write_grant(self):
        for r in self.l['authorities'][0]['writeGrants']:r['validUntil']='2026-09-21T11:00:00Z'
        x=observation(3);x['recordedAt']=NOW
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
        self.assertEqual(query(self.l,self.c)['status'],'contested')
    def test_query_wrong_subject(self):
        r=query(self.l,self.c,subject='urn:synthetic:different');self.assertEqual(r['status'],'unknown');self.assertEqual(r['observationIds'],[])
    def test_appended_copy_isolated(self):
        x=observation(3);l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);x['value']['lexical']='mutated';self.assertEqual(l['observations'][-1]['value']['lexical'],'A');self.assertEqual(len(self.l['observations']),2)
    def test_restamped_retry(self):
        x=copy.deepcopy(self.l['observations'][0]);x['recordedAt']=NOW;l=a.admit(self.l,x,'observation',self.c,W,NOW);self.assertEqual(l,self.l)
    def test_snapshot_truncation(self):
        candidate=copy.deepcopy(self.l);candidate['observations'].pop();a.validate_ledger(candidate,self.c)
        with self.assertRaises(a.Invalid):a.validate_extension(self.l,candidate,self.c)
    def test_snapshot_rewrite(self):
        candidate=copy.deepcopy(self.l);candidate['observations'][0]['value']['lexical']='changed'
        with self.assertRaises(a.Invalid):a.validate_extension(self.l,candidate,self.c)
    def test_snapshot_extension(self):
        x=observation(3);l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);self.assertTrue(a.validate_extension(self.l,l,self.c))
    def test_rotated_source_writer_can_retract(self):
        x=revision(self.l['authorities'][0]);x['writeGrants'][0]['writers']=['urn:synthetic:new-writer'];l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt'])
        obs=revision(l['observations'][0],at='2026-09-21T10:02:00Z',state='retracted',writer='urn:synthetic:new-writer');l=a.admit(l,obs,'observation',self.c,obs['writer'],obs['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred');self.assertEqual(l['observations'][0]['writer'],W)
    def test_closure_cannot_change_accountable(self):
        x=revision(self.l['authorities'][0],change='closure',validUntil='2026-12-01T00:00:00Z',accountable='urn:synthetic:other')
        for part in x['rules']+x['stewardships']+x['writeGrants']:part['validUntil']=x['validUntil']
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'authority',self.c,G,x['recordedAt'])
    def test_no_authority_retains_evidence(self):
        self.l['authorities']=[];r=query(self.l,self.c);self.assertEqual(r['status'],'unknown');self.assertEqual(len(r['observationIds']),2);self.assertEqual(len(r['evidence']),2)
    def test_part_is_not_party(self):
        self.l['authorities'][0]['stewardships'][0]['id']=self.l['authorities'][0]['stewardships'][0]['party']
        with self.assertRaises(a.Invalid):a.validate_ledger(self.l,self.c)
    def test_null_not_unknown(self):
        self.l['observations'][0]['value']=None
        with self.assertRaises(a.Invalid):query(self.l,self.c)
    def test_round_trip(self):self.assertEqual(a.import_snapshot(a.export_ledger(self.l,self.c),self.c),self.l)
    def test_duplicate_json_key(self):
        with self.assertRaises(a.Invalid):a.import_snapshot('{"format":"a","format":"b"}',self.c)
    def test_migration(self):
        self.assertEqual(a.migrate(self.l,'0.1.0'),self.l)
        with self.assertRaises(a.Invalid):a.migrate(self.l,'0.0.1')
    def test_atomic_rejection(self):
        old=copy.deepcopy(self.l);x=observation(3);x['value']['lexical']='\ud800'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,x['recordedAt'])
        self.assertEqual(self.l,old)
    def test_schema_negatives(self):
        for field,value in [('revision',True),('scope','not uri'),('state','proposed'),('recordedAt','2026-09-31T00:00:00Z'),('validFrom','2026-01-01T00:00:00+02:00')]:
            with self.subTest(field=field):
                x=policy();x[field]=value
                with self.assertRaises(a.Invalid):a.validate_record(x,'authority')
    def test_graph_negatives(self):
        for change in ['digest','anchor','part-party','part-source','part-time','part-id']:
            with self.subTest(change=change):
                x=revision(self.l['authorities'][0]);l=copy.deepcopy(self.l)
                if change=='digest':x['previousDigest']='0'*64
                if change=='anchor':x['predicate']='urn:other'
                if change=='part-party':x['stewardships'][0]['party']='urn:other'
                if change=='part-source':x['rules'][0]['source']='urn:other'
                if change=='part-time':x['rules'][0]['validUntil']='2028-01-01T00:00:00Z'
                if change=='part-id':x['rules'][0]['id']=x['id']
                l['authorities'].append(x)
                with self.assertRaises(a.Invalid):a.validate_ledger(l,self.c)
if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    report={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful(),'scope':'Reference semantics including authority, temporal history, negative admission and disclosure; not authenticated production service'}
    (P/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');raise SystemExit(not result.wasSuccessful())

```

## adoption-limits.md
```
# Additional adoption limits from the focused audit

These clarify existing behavior; they do not add permissions or change the implementation.

1. **Latest snapshot is a host responsibility.** validate_extension checks a candidate against the previous snapshot supplied by the trusted host. It cannot know whether that previous snapshot is the latest. Supplying an older root defeats rollback detection. The production host must retain the latest accepted digest, compare-and-set it atomically, verify outer supersedes/previousSnapshotDigest links and admit each new row. The reference acceptance writes those outer links; it does not implement a durable chain-validation service. Passing validate_extension(x, x) is valid replay, not evidence that x is current.
2. **Closure before a future part is outside the simple operation.** A cutoff earlier than a nested part's validFrom would create an empty clipped interval, so guarded closure rejects. Resolve the future appointment by an explicit reviewed correction before closure, or use a future adapter supporting coordinated term changes. The library does not silently remove the future part.
3. **Revival is explicit correction.** An authorized correction may change a retracted record back to active/asserted, with preserved prior revisions and a new receipt. It is not automatic resurrection. Full-term corrections remain broad under the scoped governor/current source-writer trust.
4. **Scale is unproven.** Schema array limits of 10,000 are shape limits, not demonstrated throughput. The reference rereads schemas and performs repeated history checks. No production-scale performance claim is made.
5. **Host error handling.** Denied is raised by evaluate for a reader/purpose denial. admit uses Invalid for rejection, including authorization rejection. Host endpoints must sanitize all raw exceptions and never disclose the returned complete ledger to write-only callers. This package is not a web service.
6. **References and discovery.** WM-XCT-002 and WM-XCT-012 are documentary-only semantic references. Native acceptance explicitly selects both the separately identified companion and the semantic-only WM-XCT-001 parent as roots; it does not prove an independently omitted parent is needed or resolved. The custom companion ID is available in this package and local Dimension registry, not as an independently registered canonical public WM resolver entry.
7. **Evidence limits.** External reviews do not execute code or authenticate downloads. Code/schema/native tool pins and complete package checksums are separate from their verdicts. The acceptance report's sourceDigests are a subset, while final package checksums cover every shipped file. Candidate publication metadata used before deployment is not a live-publication proof; production readback and the downloaded-package rerun supply that proof separately.
8. **Record and evidence privacy.** All provided instances are synthetic. A production register, its input digest, competing sources and steward identities are not inherently public. Preserve all-or-deny full-register access until a separately reviewed partial-disclosure adapter exists.

```

END OF TEST SUPPLEMENT
