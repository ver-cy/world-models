# Frozen no-tools implementation audit: EM-XCT-04 Enterprise Temporal History 0.1.0

Act as an independent adversarial semantic reviewer. Do not browse, call tools, run code, contact anyone or modify anything. Audit the supplied candidate, not the larger research wish list. The owner separately authorizes publication; you cannot grant it. Choose BLOCK or ACCEPT WITH LIMITS and list concrete defects with reproducing inputs and violated contract claims. Distinguish implementation bugs from explicit adoption limits. Do not claim execution, byte-hash recomputation or parent/production conformance.

This candidate is a trusted-host pure single-scope assertion history with opaque external payload pins. It implements no domain engine, payload validation, conflict storage, erasure or backdated source bootstrap. Current host policies/clock/latest root and durable conflict artifacts are required integrations. Read and write gates are not IAM. Current-root metadata can change while selected historical content is stable; exact sequence is needed for same-second reproducibility.

Research reconciliation: both providers recommended this bounded boundary. Slug is enterprise-temporal-history. Schema pin is mandatory here (Grok suggested optional). One fixed numeric-triplet grammar, not generic SemVer compatibility. Claude's substituted facet taxonomy was rejected in favor of the canonical five supplied below. Claude's erasure exception would break exact-prefix immutability; erasure is outside this release. Grok's rejected-write-in-successful-sequence proposal was rejected: conflicts stay in the host's separately restricted audit. No historical receipt bootstrap exists. The wrong Enterprise Identity landing URL in research returned 404; the actual identity profile is under WM-XCT-036, and no implementation depends on it. Grok's one closed-closed worked-example sentence was internally reversed; the code enforces end exclusion.

Tests reported by Codex: 60 behavior tests, three fresh native Dimensions, nested-invalid and predecessor/digest/truncation rejection. Treat these as reports to assess, not your execution. Native outer validation alone is insufficient. Check stale roots, clock misuse, replay after archive/config changes, temporal boundaries, schema/value repinning, erased-vs-unknown claims, current rights before diagnostics, shape strictness, snapshot prefix preservation and any documentation/code mismatch.

All file sections are complete unless explicitly marked excerpt. JSON/YAML inputs are compact-rendered with identical parsed data; original byte hashes are provenance declarations, not independently verified by you. Review the full supplied content, and explicitly report missing/truncated input. Do not use final sentinel alone as evidence that an earlier file was complete.

PART 1 OF 2. This is the complete executable core and contract. In a two-message browser delivery, acknowledge receipt ONLY and wait for PART 2 before a verdict.


FILE temporal.py original_sha256=d2cde405e7530f55a2027c6923c5c7ef95cf07804843d978fc2c3e67d0034dd5
"""Bounded trusted-host bitemporal snapshots; no database, IAM or domain engine."""
from pathlib import Path
import copy,datetime,hashlib,json,re
from jsonschema import Draft202012Validator,FormatChecker
HERE=Path(__file__).resolve().parent
class Invalid(ValueError):pass
def require(ok,message):
    if not ok:raise Invalid(message)
def encode(x):
    try:return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
    except (ValueError,TypeError,UnicodeError,RecursionError) as e:raise Invalid('Invalid JSON value') from e
def digest(x):return 'sha256:'+hashlib.sha256(encode(x)).hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
SCHEMA=load(HERE/'temporal.schema.json')
def instant(t):
    require(type(t) is str and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',t) is not None,'Unsupported timestamp')
    try:datetime.datetime.strptime(t,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:raise Invalid('Invalid calendar instant') from e
    return t
def shape(x,kind):
    require(len(encode(x))<=8*1024*1024,'8 MiB limit exceeded')
    checker=FormatChecker()
    require('uri' in checker.checkers and 'date-time' in checker.checkers,'Required format checker unavailable')
    s={'$schema':SCHEMA['$schema'],'$defs':SCHEMA['$defs'],'$ref':'#/$defs/'+kind}
    errors=list(Draft202012Validator(s,format_checker=checker).iter_errors(x))
    require(not errors,'Closed schema violation: '+(errors[0].message if errors else ''))
    def walk(v):
        if isinstance(v,dict):
            for k,w in v.items():
                if k in {'validFrom','validUntil','validTo','recordedAt','sourceRecordedAt'} and w is not None:instant(w)
                if k=='sequence':require(type(w) is int,'Sequence must have integer JSON encoding')
                if k in {'digest','expectedHead'} and w is not None:require(re.fullmatch(r'sha256:[0-9a-f]{64}',w) is not None,'Invalid digest encoding')
                if k=='version':require(re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)',w) is not None,'Unsupported version grammar')
                walk(w)
        elif isinstance(v,list):
            for w in v:walk(w)
    walk(x)
def configuration(config,now):
    shape(config,'config');instant(now)
    require(config['validFrom']<config['validUntil'],'Empty configuration interval')
    require(config['validFrom']<=now<config['validUntil'],'Current configuration unavailable')
    for name in ['readers','purposes','acceptedSchemas','acceptedStates']:
        require(len({encode(x) for x in config[name]})==len(config[name]),'Duplicate configuration entry')
    # One definition per ID/version; exact bytes cannot silently change under the same schema/profile pin.
    pins=config['acceptedSchemas']+[x['profile'] for x in config['acceptedStates']]
    seen={}
    for p in pins:
        key=(p['id'],p['version']);require(key not in seen or seen[key]==p['digest'],'Repointed binding');seen[key]=p['digest']
    axes=set()
    for p in config['acceptedStates']:
        key=(encode(p['profile']),p['axis']);require(key not in axes,'Duplicate state axis definition');axes.add(key)
        require(len(set(p['codes']))==len(p['codes']),'Duplicate state code')
def matching(ledger,config):
    for k in ['dimension','timeline','scope']:require(ledger[k]==config[k],'Wrong governed scope')
def head(ledger):return digest(ledger['commits'][-1]) if ledger['commits'] else None
def empty(config):return dict(format='vercy-enterprise-temporal',version='0.1.0',dimension=config['dimension'],timeline=config['timeline'],scope=copy.deepcopy(config['scope']),commits=[])
def segments(rows,config=None):
    previous=None
    for s in rows:
        if s['validTo'] is not None:require(s['validFrom']<s['validTo'],'Empty/reversed interval')
        if previous is not None:require(previous['validTo'] is not None and previous['validTo']<=s['validFrom'],'Unsorted/overlapping intervals')
        previous=s
        if config is not None:
            require(s['schema'] in config['acceptedSchemas'],'Unaccepted schema binding')
            if s['state'] is not None:
                state=s['state'];require(any(state['profile']==r['profile'] and state['axis']==r['axis'] and state['code'] in r['codes'] for r in config['acceptedStates']),'Unaccepted state vocabulary binding')
def validate_ledger(ledger,*,now):
    """Structural history only; this cannot establish historical writer authorization."""
    shape(ledger,'ledger');instant(now);keys=set();revisions=set();last=None;pin_definitions={};value_definitions={}
    for i,c in enumerate(ledger['commits'],1):
        q=c['request'];require(c['sequence']==i,'Non-contiguous receipt sequence')
        require(c['recordedAt']<=now,'Future receipt')
        require(last is None or c['recordedAt']>=last['recordedAt'],'Receipt clock moved backwards')
        require(q['expectedHead']==(digest(last) if last else None),'Broken head chain')
        require(q['key'] not in keys and q['revision'] not in revisions,'Reused commit identity');keys.add(q['key']);revisions.add(q['revision'])
        require(q['sourceRecordedAt'] is None or q['sourceRecordedAt']<=c['recordedAt'],'Source record time after receipt')
        require(q['operation']==('record' if last is None else q['operation']) and (last is None or q['operation']!='record'),'Wrong genesis operation')
        if last is not None:require(last['request']['operation']!='archive','Archive is terminal')
        if q['operation']=='archive':require(last is not None and encode(q['segments'])==encode(last['request']['segments']),'Archive rewrites timeline')
        segments(q['segments'])
        for s in q['segments']:
            v=s['value'];vk=(v['id'],v['revision']);require(vk not in value_definitions or value_definitions[vk]==v['digest'],'Payload revision repointed');value_definitions[vk]=v['digest']
            for b in [s['schema']]+([] if s['state'] is None else [s['state']['profile']]):
                k=(b['id'],b['version']);require(k not in pin_definitions or pin_definitions[k]==b['digest'],'Binding repointed across history');pin_definitions[k]=b['digest']
        last=c
    return True
def validate_extension(old,new,*,now):
    validate_ledger(old,now=now);validate_ledger(new,now=now)
    require(encode({k:v for k,v in old.items() if k!='commits'})==encode({k:v for k,v in new.items() if k!='commits'}),'Scope/header changed')
    require(len(new['commits'])>=len(old['commits']) and encode(new['commits'][:len(old['commits'])])==encode(old['commits']),'History rewritten/truncated')
    return True
def admit(ledger,request,config,*,actor,now):
    """Pure function. Host selects trusted current config/root, actor and clock; serializes persistence."""
    configuration(config,now);require(actor==config['writer'],'Write denied')
    validate_ledger(ledger,now=now);matching(ledger,config);shape(request,'request')
    # Repeat is checked before expected-head and archive guards; first receipt is retained.
    for c in ledger['commits']:
        if c['request']['key']==request['key']:
            require(c['writer']==actor and encode(c['request'])==encode(request),'Conflicting replay')
            return copy.deepcopy(ledger)
    require(request['expectedHead']==head(ledger),'Head conflict')
    require(not ledger['commits'] or ledger['commits'][-1]['request']['operation']!='archive','Archive is terminal')
    segments(request['segments'],config)
    result=copy.deepcopy(ledger);result['commits'].append(dict(sequence=len(ledger['commits'])+1,recordedAt=now,writer=actor,request=copy.deepcopy(request)))
    validate_extension(ledger,result,now=now)
    return result
def resolve(ledger,config,*,actor,purpose,validAt,knownAt,now,knownSequence=None):
    configuration(config,now)
    require(actor in config['readers'] and purpose in config['purposes'],'Read denied')
    validate_ledger(ledger,now=now);matching(ledger,config);instant(validAt);instant(knownAt)
    require(knownAt<=now,'Future knowledge cutoff')
    require(knownSequence is None or type(knownSequence) is int and 0<=knownSequence<=len(ledger['commits']),'Invalid knowledge sequence')
    known=[c for c in ledger['commits'] if c['recordedAt']<=knownAt and (knownSequence is None or c['sequence']<=knownSequence)]
    c=known[-1] if known else None
    result={'status':'insufficient-context','missing':['No registered timeline at this knowledge cutoff'] if c is None else ['No segment covers this valid instant'],'validAt':validAt,'knownAt':knownAt,'knownSequence':knownSequence,'commit':None if c is None else {'revision':c['request']['revision'],'sequence':c['sequence'],'recordedAt':c['recordedAt'],'digest':digest(c)},'segment':None,'archivedAsKnown':False if c is None else c['request']['operation']=='archive','archiveNow':bool(ledger['commits'] and ledger['commits'][-1]['request']['operation']=='archive'),'inputDigest':digest(ledger),'policyDigest':digest(config),'truth':'not-evaluated','domainValidation':'not-executed','transitionLegality':'not-evaluated'}
    if c:
        for s in c['request']['segments']:
            if s['validFrom']<=validAt and (s['validTo'] is None or validAt<s['validTo']):result.update(status='recorded-assertion',missing=[],segment=copy.deepcopy(s));break
    return result
def migrate(ledger,target,*,now):
    validate_ledger(ledger,now=now);require(target=='0.1.0','Unsupported migration/downgrade; retain full history');return json.loads(encode(ledger))
def validate_snapshot(fact,*,now,previous=None):
    """Additional semantic check AFTER native envelope validation; requires trusted previous snapshot."""
    require(fact['path']=='temporal.timeline.snapshot','Wrong native path');ledger=fact['value'];validate_ledger(ledger,now=now)
    require(fact['subjectId']==ledger['timeline'],'Wrong timeline subject')
    require(fact['provenance']['snapshotDigest']==digest(ledger),'Snapshot digest mismatch')
    if previous is None:
        require(fact['supersedes']==[] and fact['provenance']['previousSnapshotDigest'] is None,'Unexpected predecessor')
    else:
        validate_snapshot(previous,now=now) if not previous['supersedes'] else validate_ledger(previous['value'],now=now)
        require(previous['path']=='temporal.timeline.snapshot' and previous['subjectId']==previous['value']['timeline'],'Wrong previous timeline binding')
        require(previous['provenance']['snapshotDigest']==digest(previous['value']),'Previous snapshot digest mismatch')
        require(fact['factId']!=previous['factId'] and fact['supersedes']==[previous['factId']],'Wrong snapshot predecessor identity')
        require(fact['provenance']['previousSnapshotDigest']==digest(previous['value']),'Wrong previous snapshot digest')
        validate_extension(previous['value'],ledger,now=now)
    return True

END FILE temporal.py


FILE test_temporal.py original_sha256=1ab650a7460b122714e431f5e5d7f2d2fdca41389dd54c14aeb2981f374b20cb
import copy,json,unittest,datetime
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
    def test_clock_regression(self):
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
if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TemporalTests);result=unittest.TextTestRunner(verbosity=1).run(suite)
    Path('test-results.json').write_text(json.dumps({'passed':result.wasSuccessful(),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'codeDigest':t.digest(Path(t.__file__).read_text(encoding='utf-8'))},indent=2)+'\n',encoding='utf-8')
    raise SystemExit(not result.wasSuccessful())

END FILE test_temporal.py


FILE temporal.schema.json original_sha256=9981cbdf92849382df1bd49f5e75789361967f66629907b12abd66649c035cd4
{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/temporal.schema.json","type":"object","properties":{"format":{"const":"vercy-enterprise-temporal"},"version":{"const":"0.1.0"},"dimension":{"type":"string","format":"uri","minLength":3,"maxLength":512},"timeline":{"type":"string","format":"uri","minLength":3,"maxLength":512},"scope":{"type":"object","properties":{"subject":{"type":"string","format":"uri","minLength":3,"maxLength":512},"predicate":{"type":"string","format":"uri","minLength":3,"maxLength":512},"context":{"type":"string","format":"uri","minLength":3,"maxLength":512}},"required":["subject","predicate","context"],"additionalProperties":false},"commits":{"type":"array","items":{"type":"object","properties":{"sequence":{"type":"integer","minimum":1,"maximum":1000},"recordedAt":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":512},"request":{"type":"object","properties":{"key":{"type":"string","format":"uri","minLength":3,"maxLength":512},"revision":{"type":"string","format":"uri","minLength":3,"maxLength":512},"expectedHead":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"operation":{"enum":["record","correct","archive"]},"reason":{"type":"string","minLength":1,"maxLength":2048},"sourceRecordedAt":{"anyOf":[{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},{"type":"null"}]},"segments":{"type":"array","items":{"type":"object","properties":{"validFrom":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"validTo":{"anyOf":[{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},{"type":"null"}]},"value":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"revision":{"type":"string","format":"uri","minLength":3,"maxLength":512},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","revision","digest"],"additionalProperties":false},"schema":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"state":{"anyOf":[{"type":"object","properties":{"profile":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"axis":{"type":"string","format":"uri","minLength":3,"maxLength":512},"code":{"type":"string","minLength":1,"maxLength":2048}},"required":["profile","axis","code"],"additionalProperties":false},{"type":"null"}]}},"required":["validFrom","validTo","value","schema","state"],"additionalProperties":false},"minItems":0,"maxItems":100}},"required":["key","revision","expectedHead","operation","reason","sourceRecordedAt","segments"],"additionalProperties":false}},"required":["sequence","recordedAt","writer","request"],"additionalProperties":false},"minItems":0,"maxItems":1000}},"required":["format","version","dimension","timeline","scope","commits"],"additionalProperties":false,"$defs":{"ledger":{"type":"object","properties":{"format":{"const":"vercy-enterprise-temporal"},"version":{"const":"0.1.0"},"dimension":{"type":"string","format":"uri","minLength":3,"maxLength":512},"timeline":{"type":"string","format":"uri","minLength":3,"maxLength":512},"scope":{"type":"object","properties":{"subject":{"type":"string","format":"uri","minLength":3,"maxLength":512},"predicate":{"type":"string","format":"uri","minLength":3,"maxLength":512},"context":{"type":"string","format":"uri","minLength":3,"maxLength":512}},"required":["subject","predicate","context"],"additionalProperties":false},"commits":{"type":"array","items":{"type":"object","properties":{"sequence":{"type":"integer","minimum":1,"maximum":1000},"recordedAt":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":512},"request":{"type":"object","properties":{"key":{"type":"string","format":"uri","minLength":3,"maxLength":512},"revision":{"type":"string","format":"uri","minLength":3,"maxLength":512},"expectedHead":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"operation":{"enum":["record","correct","archive"]},"reason":{"type":"string","minLength":1,"maxLength":2048},"sourceRecordedAt":{"anyOf":[{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},{"type":"null"}]},"segments":{"type":"array","items":{"type":"object","properties":{"validFrom":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"validTo":{"anyOf":[{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},{"type":"null"}]},"value":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"revision":{"type":"string","format":"uri","minLength":3,"maxLength":512},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","revision","digest"],"additionalProperties":false},"schema":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"state":{"anyOf":[{"type":"object","properties":{"profile":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"axis":{"type":"string","format":"uri","minLength":3,"maxLength":512},"code":{"type":"string","minLength":1,"maxLength":2048}},"required":["profile","axis","code"],"additionalProperties":false},{"type":"null"}]}},"required":["validFrom","validTo","value","schema","state"],"additionalProperties":false},"minItems":0,"maxItems":100}},"required":["key","revision","expectedHead","operation","reason","sourceRecordedAt","segments"],"additionalProperties":false}},"required":["sequence","recordedAt","writer","request"],"additionalProperties":false},"minItems":0,"maxItems":1000}},"required":["format","version","dimension","timeline","scope","commits"],"additionalProperties":false},"config":{"type":"object","properties":{"dimension":{"type":"string","format":"uri","minLength":3,"maxLength":512},"timeline":{"type":"string","format":"uri","minLength":3,"maxLength":512},"scope":{"type":"object","properties":{"subject":{"type":"string","format":"uri","minLength":3,"maxLength":512},"predicate":{"type":"string","format":"uri","minLength":3,"maxLength":512},"context":{"type":"string","format":"uri","minLength":3,"maxLength":512}},"required":["subject","predicate","context"],"additionalProperties":false},"validFrom":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"validUntil":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":512},"readers":{"type":"array","items":{"type":"string","format":"uri","minLength":3,"maxLength":512},"minItems":1,"maxItems":100},"purposes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":2048},"minItems":1,"maxItems":100},"acceptedSchemas":{"type":"array","items":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"minItems":1,"maxItems":100},"acceptedStates":{"type":"array","items":{"type":"object","properties":{"profile":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"axis":{"type":"string","format":"uri","minLength":3,"maxLength":512},"codes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":2048},"minItems":1,"maxItems":100}},"required":["profile","axis","codes"],"additionalProperties":false},"minItems":0,"maxItems":100}},"required":["dimension","timeline","scope","validFrom","validUntil","writer","readers","purposes","acceptedSchemas","acceptedStates"],"additionalProperties":false},"request":{"type":"object","properties":{"key":{"type":"string","format":"uri","minLength":3,"maxLength":512},"revision":{"type":"string","format":"uri","minLength":3,"maxLength":512},"expectedHead":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"operation":{"enum":["record","correct","archive"]},"reason":{"type":"string","minLength":1,"maxLength":2048},"sourceRecordedAt":{"anyOf":[{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},{"type":"null"}]},"segments":{"type":"array","items":{"type":"object","properties":{"validFrom":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"validTo":{"anyOf":[{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},{"type":"null"}]},"value":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"revision":{"type":"string","format":"uri","minLength":3,"maxLength":512},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","revision","digest"],"additionalProperties":false},"schema":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"state":{"anyOf":[{"type":"object","properties":{"profile":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"axis":{"type":"string","format":"uri","minLength":3,"maxLength":512},"code":{"type":"string","minLength":1,"maxLength":2048}},"required":["profile","axis","code"],"additionalProperties":false},{"type":"null"}]}},"required":["validFrom","validTo","value","schema","state"],"additionalProperties":false},"minItems":0,"maxItems":100}},"required":["key","revision","expectedHead","operation","reason","sourceRecordedAt","segments"],"additionalProperties":false},"segment":{"type":"object","properties":{"validFrom":{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},"validTo":{"anyOf":[{"type":"string","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$","format":"date-time"},{"type":"null"}]},"value":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"revision":{"type":"string","format":"uri","minLength":3,"maxLength":512},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","revision","digest"],"additionalProperties":false},"schema":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"state":{"anyOf":[{"type":"object","properties":{"profile":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"axis":{"type":"string","format":"uri","minLength":3,"maxLength":512},"code":{"type":"string","minLength":1,"maxLength":2048}},"required":["profile","axis","code"],"additionalProperties":false},{"type":"null"}]}},"required":["validFrom","validTo","value","schema","state"],"additionalProperties":false},"SchemaBinding":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"StateReference":{"type":"object","properties":{"profile":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":512},"version":{"type":"string","pattern":"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$","maxLength":50},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","version","digest"],"additionalProperties":false},"axis":{"type":"string","format":"uri","minLength":3,"maxLength":512},"code":{"type":"string","minLength":1,"maxLength":2048}},"required":["profile","axis","code"],"additionalProperties":false}}}
END FILE temporal.schema.json


FILE model-spec.md original_sha256=0b9cf83a36654528a5ce1df4a239f6d02e28e97e6c82db43d80994d03730052a
# Enterprise Temporal History 0.1.0

Original bounded companion for a Company Dimension, with reviewable-draft assurance. This is a history of **recorded assertions**, not proof of what people knew, what actually happened, or whether a domain action was lawful. No SQL, SCXML, OWL-Time, ISO or complete parent-model conformance is claimed.

## Boundary, identities and fields

One Timeline aggregate belongs to exactly one Dimension and one fixed `(subject, predicate, context)` FactScope. All four references and the timeline ID are required absolute URIs. References are opaque: no automatic fetch, normalization, alias, company identity, or master discovery. A separate scope is required for another legal entity, environment, competing master or simultaneous value. Host governance must prevent two current timelines being registered as the same scope; this single-aggregate reference cannot discover them.

| Type | Identity and cardinality | Owner and lifecycle |
|---|---|---|
| Timeline | Independently assigned `timeline` URI; exactly one scope, 0..1000 commits | Configured host master; empty → open → archived. No reopen or erase operation |
| TimelineCommit | Opaque revision URI and scope-local idempotency key; contiguous positive receipt sequence; exactly one complete snapshot | Host assigns receipt and writer; immutable once admitted. Not a domain event or artifact revision |
| ValidSegment | Embedded value at a position in a commit; 0..100 per snapshot; one interval, one external value pin, one schema binding, optional state reference | Domain master asserts effective interval. No independently editable segment identity |
| SchemaBinding | Value tuple `(id, version, digest)` | External schema publisher owns meaning; current host config accepts exact tuple for new writes. Binding is immutable within history |
| StateReference | One profile binding, one axis URI, one code | Domain profile owner defines code. Membership only; no statechart execution, transition event or legality inference |
| TimelineAnswer | Ephemeral derived view for one scope and explicit cutoffs | Current host reader/purpose authorization; no new master or operational permission |

`temporal.schema.json` is the closed field/type/cardinality contract. All keys shown are required; optional concepts use explicit null. Unknown keys reject. External value pin requires an ID URI, a distinct-purpose opaque revision URI, and declared sha256 digest. This reference does not fetch the payload, recompute its external digest, validate its domain schema, authenticate the source, or establish the value's truth. The same external `(id,revision)` cannot be declared with different digests in one history. IDs and digests do not prove equality of real-world objects.

Schema/profile `version` uses the deliberately narrow `normal-semver-triplet` grammar: three nonnegative ASCII integers separated by dots, no leading zeroes except zero, prerelease/build parts unsupported. This is only a pin grammar; version order never proves compatibility. `active` is a valid domain code only under an accepted vocabulary, never a schema version. External object revision, timeline revision, schema version and domain state occupy separate fields. A schema pin ID/version cannot silently acquire different bytes. Changing a declared schema version requires an exact accepted new tuple; old segments retain their original pins. Historical reads do not reinterpret records using the current schema.

Each commit includes `sequence`, `recordedAt`, `writer` and the exact request. Request has `key`, `revision`, `expectedHead`, `operation`, `reason`, nullable `sourceRecordedAt`, and complete `segments`. `reason` is attributed explanatory text, not a validated classification of a domain event. It must explain removals, new future assertions and backdated corrections; mixed intent needs clear text or separate commits. A commit changes assertions about effective history, not the external domain object itself. `sourceRecordedAt` is source-declared metadata, may be null, and cannot follow receipt in this narrow profile. It never chooses knowledge order. Source events/observation times are outside this executable schema and may be linked through separately governed provenance records.

## Time and querying

All instants use a real Gregorian date in exact ASCII `YYYY-MM-DDTHH:MM:SSZ`, seconds 00..59. No fractions, local times, explicit numeric offsets, uncertain dates or leap seconds. Reject unsupported input; never round or infer midnight/zone. A civil-date or clock conversion needs a separately reviewed adapter and pinned rules. A future **valid** instant is allowed for a scheduled assertion; a future **recorded** instant or knowledge cutoff is rejected against trusted `now`.

Intervals are half-open `[validFrom, validTo)`. `validTo:null` explicitly means no asserted upper bound, not an unknown date or eternal truth. Start is always known. Empty/reversed intervals and overlaps reject; segments must be sorted. Adjacent boundaries are legal, and an open segment must be last. Gaps and an empty snapshot are permitted and return `insufficient-context`; they are not false, absent or unassigned. Explicit negation needs a separately pinned domain value. A snapshot replaces the entire scope's current asserted timeline, so omitted periods become unknown in that new recorded view. Previous snapshots remain intact.

The trusted host assigns non-decreasing receipt instants and strictly increasing contiguous sequences within this one timeline. Two commits in the same second are permitted; sequence resolves them. Clock regression rejects. Sequences cannot compare different timelines or Dimensions; no global consistency or synchronized-clock claim exists.

`resolve(... validAt, knownAt, knownSequence=None)` first checks **current** full-timeline reader and purpose permission, then validates history and cutoffs. It chooses the latest commit with receipt ≤ knownAt and, if supplied, sequence ≤ knownSequence; then selects the segment covering validAt. No hidden defaults to “now”. `knownSequence=0` deliberately precedes all receipts. Instant-only cutoffs include all received commits in that second; they can gain a later commit with that same second. **Pin the returned sequence for stable historical content.** A supplied sequence is an additional upper bound, not an assertion that a commit existed at the timestamp. Before first receipt and uncovered periods produce distinct missing-context explanations. Denied reads raise a denial before inspecting ledger/query contents; denied is never an unknown-fact answer.

Returned value remains a `recorded-assertion`, with truth, domain validation and transition legality explicitly unevaluated. The view includes commit revision/sequence/receipt/digest, exact segment, and query input/configuration digests. `archivedAsKnown` belongs to the selected history; `archiveNow` describes the current supplied root and is expressly current context. Root/policy digests and archiveNow may change when historical content remains the same. Consequently reproducibility means the selected historical commit and segment under the pinned cutoff, not byte equality of all current-context metadata. Full-history authority is required for this view; no partial redaction or hidden contrary-evidence signal is supplied.

## Writes, authority, conflicts and imports

`admit(ledger, request, config, actor, now)` is a pure **trusted-host internal** function. The host authenticates actor, selects its current configuration/latest complete root/clock, and serializes durable persistence. It must enforce request size limits before parsing. Config includes exact dimension/timeline/scope, a half-open current validity interval, one writer, full-history readers, purposes and accepted schema/state pins. Claimed source authorship grants nothing. On grant rotation, old writer attribution remains; static validation does not retrospectively authenticate it. A write-only caller must receive only a receipt or generic rejection, never the function's whole returned ledger or detailed exceptions.

First operation is `record`; subsequent operations are `correct` or `archive`. Host stamps every new sequence, receipt and writer; caller-supplied receipt fields are rejected. A correction must match the current head digest. Complete snapshots intentionally serialize even disjoint changes; no automatic merge, last-writer contest resolution, branch or cross-scope transaction exists. Rejected head, replay and authority attempts leave the input unchanged. **The host must durably record its own restricted conflict/rejection artifact** before reporting a conflict; this library has no conflict store or network side effect. A competing master's assertion needs a distinct governed scope and an explicit authority-resolution process. Receipt does not certify priority or correctness.

Repeated key with byte-equivalent request and the same authenticated writer is a no-op, retaining the original receipt even after the head moved or archival. Current authorization/config validity is still checked. Replay compares the complete canonical request, including original expectedHead; it does not rewrite it to the new head. Same key/different request or writer rejects. Changing keys with a reused revision also rejects. Admission is not a durable transaction service.

Archive appends a new commit with exactly the prior segments and freezes further new writes. It does not deactivate the subject, close business-valid periods, retract an assertion or delete retained history. An identical retry remains permitted. **Erasure, tombstones, retention schedules and legal-hold decisions are unimplemented, separate integrations.** Do not promise perpetual retention or adopt this reference where the required disposal path is absent. No source-knowledge bootstrap can insert earlier local receipt times: import must call admit with the actual local host time and retain earlier source time only as metadata. A structurally valid imported ledger cannot prove it was actually received then; only a trusted host archive/chain can supply that assurance.

## Integrity, native binding and migration

`validate_ledger` checks shape and internal temporal/identity chain consistency against explicit trusted now. `validate_extension` additionally requires exact old headers and the entire old commit prefix. They require the host's trusted latest predecessor, cannot detect an omitted newer root, and do not establish historical authorization. Export/import the complete same-version ledger losslessly; `migrate` rejects any other contract version. No automatic schema migration, SCD2/SQL/XTDB adapter, partial export or existing-Dimension upgrade is implemented.

The encoding named **vercy-python-json-v1** is UTF-8 of Python `json.dumps(sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)`. There is no Unicode normalization. Integers for sequence must use integer JSON encoding, not Boolean or `1.0`. This profile is not RFC 8785; independent language ports must reproduce fixtures exactly. Invalid Unicode, nonfinite numbers and unsupported JSON values reject. JSON objects reaching the callable must come from an input parser that rejects duplicate keys; the bundled file loader is for trusted fixture/archive files. Hashes provide consistency against a trusted predecessor, not signatures, anti-rollback storage or origin authenticity.

Bounds: ≤1000 commits, ≤100 segments per snapshot and ≤8 MiB serialized root. These are structural ceilings, not measured production capacity. Full validation scans retained history and admission copies it; host limits, concurrency, availability, monitoring and rollover/migration planning are required before production growth. Overflow refuses the operation without truncation.

Specification dependency graph has no runtime imports. Exact WM-XCT-009, 021 and 022 references are conceptual selected-pattern alignments only. Instance references and package composition are separate graphs. No universal WM ID or parent subtype is created. A native V3 fact stores one complete timeline under `temporal.timeline.snapshot` with its own companion namespace. The native outer validator permits object-shaped values and is **not** this nested semantic validator. `validate_snapshot` checks timeline subject, snapshot digest, unique successor fact ID, predecessor linkage and append-only extension after native envelope validation. Trusted previous snapshot selection is external. Initial installation tests fresh synthetic Dimensions; existing-Dimension migration remains deferred.

## Invariants and minimum use

I01 scope/Dimension remain fixed; I02 opaque revision/schema version/state remain separate; I03 host receipt order differs from effective/source time; I04 positive half-open nonoverlapping sorted intervals; I05 gaps/pre-receipt are unknown; I06 full prior snapshot prefix survives correction; I07 request-bound idempotency retains first receipt; I08 expected-head conflict cannot overwrite; I09 current reader/purpose gate precedes diagnostics; I10 immutable schema/value pins across history; I11 archive preserves history and blocks new commits; I12 unsupported migration refuses loss; I13 explicit nested native validation; I14 no transition/permission/truth inferred; I15 equal-second history needs sequence for stable content; I16 new accepted bindings never reinterpret old content.

A startup needs one governed scope, local config, a pinned domain value/schema and its first snapshot; state references are optional. A matrix group uses separate assignment scopes. An AI deployment uses an environment-qualified artifact binding; model-weight revision, deployment status, evaluation schema and record revision remain different references. No example is a claim about any real organization. The full question routes live in spec.json; missing artifacts remain insufficient context. Allowed actions describe operations to propose or execute under host authority, not grants from this package.

END FILE model-spec.md

END PART 1 — WAIT FOR PART 2

PART 2 OF 2. Now audit PART 1 plus this complete supplement, without tools. If any part is unavailable or truncated, disclose that and block claims of full review. This is the final part.


FILE AGENTS.md original_sha256=68d7646822c52ad02e2ac16c65d8d024efefe02ed60a52796c327a71f62861a9
# Agent instructions

Read model-spec.md, temporal.schema.json and temporal.py. Read spec.json for the Bundle → Layer → Finding → Question → Artifact → Action tree. Query explicit valid/recorded cutoffs; pin sequence for reproducibility within a second. Unknown is not false. Schema version, artifact revision, timeline revision and state are separate.

This is a trusted-host reference, not a security boundary. Host supplies authenticated actor, current config, latest complete root, clock and durable serialization. Enforce raw input size limits and duplicate-key rejection before parsing. Invoke admit on every new request, preserve first receipt on replay, record restricted host conflict artifacts for rejected writes, and persist atomically. Return only receipt/generic error to a writer without full history read authority. Config and diagnostic details stay inside the host.

Never backdate local receipt using source time, merge competing masters, infer truth or transition legality, silently truncate timestamps, invoke external adapters, or dispose of history. Archive freezes new commits while retaining reads. Retention/erasure and existing-Dimension migration require a separate integration. Validate native envelope and nested snapshot separately against the trusted latest predecessor. Current read rights apply to old history too. Static import validation proves only internal consistency. Do not contact people, access external payloads or execute domain transitions on the basis of this package.

END FILE AGENTS.md


FILE acceptance.py original_sha256=fe01aa2e851e9e6c2132cf83928d677978bd375f321a85d4fc6c24317a35a5b9
"""Trusted synthetic new-Dimension composition, admission and snapshot checks."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import temporal as p
from test_temporal import fixture,T1,T2,NOW
HERE=Path(__file__).resolve().parent
PROFILE_ID='vr.profile.enterprise-temporal-history'
SLUG='enterprise-temporal-history'
def run(composer,skill):
    p.require(__debug__,'Run without -O');composer=Path(composer).resolve();skill=Path(skill).resolve();pins=p.load(HERE/'tool-pins.json')
    for field,root in [('composerFiles',composer),('skillFiles',skill),('upstreamFiles',HERE/'upstream')]:
        for n,h in pins[field].items():p.require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'Unexpected trusted asset: '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    reports=[];at=c.now();expires=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    with tempfile.TemporaryDirectory(prefix='vercy-authority-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(folder,name,source,url):
            raw=source.read_bytes();dest=assets/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':folder+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':url}
        def release(mid,version,folder,spec,agents,base,native):
            ds=descriptor(folder,spec.name,spec,base+spec.name);da=descriptor(folder,'AGENTS.md',agents,base+'AGENTS.md');binding=None
            if native:
                binding={'id':'urn:vercy:binding:enterprise-temporal-history','version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',HERE/'runtime-model.reference.json',base+'runtime-model.reference.json'),'instanceSchema':descriptor(folder,'temporal.schema.json',HERE/'temporal.schema.json',base+'temporal.schema.json'),'companionValidator':descriptor(folder,'temporal.py',HERE/'temporal.py',base+'temporal.py'),'scope':'Own companion namespace/specification; no parent subtype. Explicit nested validation and admission required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':da,'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':at,'scope':'Synthetic candidate-installation exercise, not global parent ratification; publication and research assurance are separate.'}}
        parent='wm-xct-009-time-calendar';up=HERE/'upstream'/parent
        semantic=release('vr.wm-xct-009','0.3.0-research.1',parent,up/'spec.yaml',up/'AGENTS.md','https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/upstream/'+parent+'/',False)
        companion=release(PROFILE_ID,'0.1.0',SLUG,HERE/'spec.json',HERE/'AGENTS.md','https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/',True)
        companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ['startup','group','ai-team']:
            config,initial,first,second,q1,q2=fixture(name);target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json');dimension=config['dimension']
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:temporal','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic temporal reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:temporal:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic temporal '+name,dimension)
            installed=target/'models/composed'/SLUG/'temporal.py';p.require(c.digest(installed.read_bytes())==companion['binding']['companionValidator']['digest'],'Code differs');p.require(c.digest((installed.parent/'temporal.schema.json').read_bytes())==companion['binding']['instanceSchema']['digest'],'Schema differs')
            ms=importlib.util.spec_from_file_location('installed_temporal_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            replay1=module.admit(initial,q1,config,actor=config['writer'],now=T1);replay2=module.admit(replay1,q2,config,actor=config['writer'],now=T2)
            p.require(replay1==first and replay2==second,'Admission differs');oid=config['timeline'];operator='urn:synthetic:timeline-operator';register='urn:synthetic:governance-register'
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':timeline','name':'Synthetic temporal timeline','description':'Own companion namespace, not a domain state-machine subtype','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':register,'synthetic':True},'accessClass':'synthetic-private'}
            path=root/(name+'-object.json');path.write_bytes(p.encode(obj));append(target,'object',path);facts=[]
            for i,snapshot in enumerate([first,second],1):
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot-r'+str(i),'subjectId':oid,'path':'temporal.timeline.snapshot','value':snapshot,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[] if i==1 else [oid+':snapshot-r1'],'status':'asserted','provenance':{'source':register,'synthetic':True,'snapshotDigest':p.digest(snapshot),'previousSnapshotDigest':None if i==1 else p.digest(first)},'authority':{'source':operator,'rank':0},'masterSystem':register,'accessClass':'synthetic-private'}
                path=root/(name+'-fact'+str(i)+'.json');path.write_bytes(p.encode(fact));result=append(target,'fact',path);facts.append(target/result['written'])
            f1,f2=[p.load(x) for x in facts];p.require([f1['value'],f2['value']]==[first,second],'Stored roundtrip differs')
            module.validate_snapshot(f1,now=NOW);module.validate_snapshot(f2,now=NOW,previous=f1)
            def query(k):return module.resolve(f2['value'],config,actor=config['readers'][0],purpose='research',validAt='2026-02-01T00:00:00Z',knownAt=k,now=NOW)
            before,after=query('2026-01-31T00:00:00Z'),query('2026-02-11T00:00:00Z')
            p.require(before['segment']['value']==q1['segments'][0]['value'] and after['segment']['value']==q2['segments'][1]['value'],'Bitemporal stored answers differ')
            native=native_validate(target);p.require(native['valid'],'Native validation failed')
            original=facts[-1].read_bytes();bad=copy.deepcopy(f2);bad['value']['commits'][0]['request']['segments'][0]['validFrom']='not-an-instant';facts[-1].write_bytes(p.encode(bad));outer=native_validate(target);nested=False
            try:module.validate_snapshot(bad,now=NOW,previous=f1)
            except module.Invalid:nested=True
            finally:facts[-1].write_bytes(original)
            p.require(outer['valid'] and nested,'Native/companion distinction missing')
            negatives=[]
            for label,mutator in [('truncation',lambda x:x['value']['commits'].clear()),('digest',lambda x:x['provenance'].update(snapshotDigest='sha256:'+'0'*64)),('subject',lambda x:x.update(subjectId='urn:synthetic:wrong')),('predecessor',lambda x:x.update(supersedes=[]))]:
                bad=copy.deepcopy(f2);mutator(bad);failed=False
                try:module.validate_snapshot(bad,now=NOW,previous=f1)
                except module.Invalid:failed=True
                p.require(failed,'Accepted '+label);negatives.append(label)
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':1,'facts':2,'native':native,'roundTripEqualsInput':True,'admissionReplayedThroughInstalledCompanion':True,'negativeCasesRejected':negatives,'storedAnswers':[before,after],'invalidNestedSnapshot':{'native':outer,'companionRejected':nested},'envelopeAuthorityMeaning':'Snapshot storage only, not domain fact priority','pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-temporal-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'temporal.py',HERE/'temporal.schema.json',HERE/'spec.json',HERE/'tool-pins.json',HERE/'test_temporal.py']},'limits':'Three synthetic new Dimensions; own companion plus optional semantic-only parent. No IAM, domain truth/transition, durable concurrency, production capacity or existing-Dimension migration proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))

END FILE acceptance.py


FILE whole-object-coverage.yaml original_sha256=d7591ea1735788c0808b743060fc1e7896494f0ac0986fe95949da89128e94e6
{"canonicalFacets":["identity-class","direct-properties","recognition-observation","capabilities-behaviour-actions","context-evidence"],"types":{"Timeline":{"identity-class":{"status":"required","coverage":"Governed timeline URI and fixed scope"},"direct-properties":{"status":"required","coverage":"Header and append-only bounded commits"},"recognition-observation":{"status":"required","coverage":"Recorded history observed via explicitly cut view; source truth not inferred"},"capabilities-behaviour-actions":{"status":"required","coverage":"Host admission, archival and query"},"context-evidence":{"status":"required","coverage":"Current config and exact predecessor root"}},"TimelineCommit":{"identity-class":{"status":"required","coverage":"Revision URI, key and local sequence"},"direct-properties":{"status":"required","coverage":"Host receipt/writer, exact request and complete snapshot"},"recognition-observation":{"status":"required","coverage":"Registration is local receipt, not human awareness or event observation"},"capabilities-behaviour-actions":{"status":"required","coverage":"Immutable; superseded by a new commit, never edited"},"context-evidence":{"status":"required","coverage":"Previous digest, reason and source-declared time"}},"ValidSegment":{"identity-class":{"status":"required","coverage":"Embedded commit-relative value, no independent identity"},"direct-properties":{"status":"required","coverage":"Half-open effective interval and exact external pins"},"recognition-observation":{"status":"required","coverage":"Coverage membership only, truth and real-world observation unevaluated"},"capabilities-behaviour-actions":{"status":"required","coverage":"No independent mutation; new full snapshot for correction"},"context-evidence":{"status":"required","coverage":"Schema/state bindings and containing commit"}},"SchemaBinding":{"identity-class":{"status":"required","coverage":"Whole id/version/digest tuple"},"direct-properties":{"status":"required","coverage":"Numeric triplet grammar and sha256 syntax"},"recognition-observation":{"status":"required","coverage":"Exact accepted tuple comparison, payload conformance untested"},"capabilities-behaviour-actions":{"status":"required","coverage":"Read-only pin; new version for changed definition"},"context-evidence":{"status":"required","coverage":"External publisher responsibility and historical preservation"}},"StateReference":{"identity-class":{"status":"required","coverage":"Profile pin plus axis/code embedded value"},"direct-properties":{"status":"required","coverage":"One optional status axis membership"},"recognition-observation":{"status":"required","coverage":"Vocabulary membership only, not proof of a transition"},"capabilities-behaviour-actions":{"status":"required","coverage":"No state machine or domain effect executed"},"context-evidence":{"status":"required","coverage":"Host domain definition/evidence, no executable delegation"}},"TimelineAnswer":{"identity-class":{"status":"required","coverage":"Ephemeral query result, no persistent domain identity"},"direct-properties":{"status":"required","coverage":"Explicit cutoffs, selected commit/segment, missing context"},"recognition-observation":{"status":"required","coverage":"Shows recorded assertion or insufficient context, not truth"},"capabilities-behaviour-actions":{"status":"required","coverage":"Current full-reader query, no writer authority"},"context-evidence":{"status":"required","coverage":"Input/root/policy digests and explicit current vs historical archive context"}}},"limits":"Each value/derived type is scoped individually; no mass/physical dimension invented. Conceptual references do not claim executable delegation."}
END FILE whole-object-coverage.yaml


FILE mastership-and-rights.yaml original_sha256=9dc4b36a2a84e8e636f1ec54b2bd043ed08849c224370353ac13ff4cc587e46f
{"facts":[{"fact":"scope/identity","semanticOwner":"Domain scope steward","master":"Configured local register","writer":"Current configured writer after host identity check","readerPurpose":"Whole timeline reader and purpose gate","validTime":"Scope fixed in this profile","provenance":"Registration config","conflict":"Duplicate scope detected by external registry","retention":"Host-owned, erasure integration required"},{"fact":"effective segments and state declarations","semanticOwner":"Domain fact owner","master":"One designated writer per governed scope","writer":"Authenticated configured writer","readerPurpose":"Current full-history readers/purposes","validTime":"Half-open UTC-second segments","provenance":"Commit writer/reason/sourceRecordedAt plus optional external provenance model","conflict":"Expected-head/replay rejection; host durable conflict artifact","retention":"Archive retains all history; no disposal implementation"},{"fact":"receipt/order/head","semanticOwner":"Timeline operator","master":"Trusted host serialized store/clock","writer":"Host only","readerPurpose":"Current full-history gate","validTime":"Local recorded axis, never business-valid time","provenance":"Contiguous sequence and predecessor digest","conflict":"Clock regression or stale head rejects","retention":"No truncation/rollover in current implementation"},{"fact":"schema/state profile definitions","semanticOwner":"External schema/domain publisher","master":"External source, exact accepted pin list locally","writer":"Host steward changes current config; definitions not edited here","readerPurpose":"Pins may also be sensitive; full-history gate","validTime":"Historical segment retains exact pin","provenance":"ID/version/digest declaration, not signature","conflict":"Repointed ID/version rejects","retention":"Host must retain accessible definitions for interpretation"}]}
END FILE mastership-and-rights.yaml


FILE requirements.txt original_sha256=5bc814e05c852ada4731d68f061aab75fd7b9d4f2fd332360a9f5362984a7e89
jsonschema==4.26.0
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1

END FILE requirements.txt


FILE runtime-model.reference.json original_sha256=f2b69d8ae6f6a9426be693458f53894ff7c3e04fe5038890adf5b65d06edbd17
{"format":"vercy-runtime-model-schema","schemaVersion":"1.0.0","modelId":"vr.profile.enterprise-temporal-history","paths":{"temporal.timeline.snapshot":{"valueTypes":["object"],"units":[null]}}}
END FILE runtime-model.reference.json


FILE adoption-limits.md original_sha256=900fdd220b08eb5f0830cdb2f642887a4e7dcdb577f6ef71d49212078917ce15
# Adoption limits

Reviewable draft; one single-valued scope and one host sequencer. No real-organization validation, distributed consistency, engine adapter, fine-grained disclosure, IAM, payload validation, transition engine, signatures, clock attestation, durable conflicts, erasure or existing-Dimension migration. Full snapshots have structural limits, not an enterprise throughput claim. Before production, implement durable serialized storage, scope uniqueness, authentication and current rights, a reliable clock, conflict audit, strict input parser/budgets and locally required retention/disposal. Historical source times never establish earlier local knowledge. Parent source/profile holds remain in crosswalk.json.

END FILE adoption-limits.md


FILE migration.md original_sha256=1f3d53b0cf5c34d16f63c1319b9680ae3da4063733c459ac7ade5585f4292f10
# Migration and loss

Only complete same-contract-version JSON roundtrip is implemented and tested. A different version refuses. Keep the original root and all pins; perform any new conversion in a separately governed staging process with explicit loss, provenance, rollback and ownership. Source SQL system-time columns are not automatically business-valid time. SCD2 can lose recorded history; timezone/fractional conversions can lose precision. No such adapter is included or silently executed. Native acceptance covers new synthetic Dimensions only. Rollback to an older root is not an allowed history update; restoration is an operational recovery requiring the complete trusted chain.

END FILE migration.md

COMPLETE SPEC TREE / COMPOSITION / METADATA (contract already fully supplied in part 1):
{"metaModel":{"id":"enterprise-temporal-history","registryId":"vr.profile.enterprise-temporal-history","version":"0.1.0","name":"Enterprise Temporal History","kind":"companion-contract"},"canonicalUrl":"https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/spec.json","researchAssurance":"reviewable-draft","researchContour":"EM-XCT-04","model":{"purpose":"Record effective timelines, preserve earlier recorded views and bind schemas and domain states without rewriting history."},"composition":{"runtimeImports":[],"semanticReferences":[{"id":"WM-XCT-009","version":"0.3.0-research.1","specDigest":"sha256:060511804c09ed5992e3fdf222839f97a0d340db0a2cba3c4c08aded7767e90d","relation":"selected-pattern-alignment-not-subtype"},{"id":"WM-XCT-021","version":"0.3.0-research.1","specDigest":"sha256:87c8c50f6f4c2eb3478751f01a08c6c37c6a85f97f4c056505b13cdf561314e9","relation":"selected-pattern-alignment-not-subtype"},{"id":"WM-XCT-022","version":"0.3.0-research.2","specDigest":"sha256:40ced88212f4c90690bdbb35bf2429fe627d11793bee5e587b5b10b99f49fe85","relation":"selected-pattern-alignment-not-subtype"}]},"structure":{"bundles":[{"id":"TH-B-scope","name":"Scope and interpretation","description":"Scope and interpretation with explicit uncertainty and host responsibility.","layers":[{"id":"TH-L-identity","name":"Identity and boundaries","description":"Identity and boundaries for one governed temporal assertion scope.","findings":[{"id":"TH-F01","name":"What is the governed fact scope?","description":"What is the governed fact scope?","questions":[{"id":"TH-Q01","text":"What is the governed fact scope?","kind":"governed-context","answer_data":["Dimension, timeline and subject/predicate/context URIs","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A01","name":"Dimension, timeline and subject/predicate/context URIs","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT01","description":"Compare exact references; request missing context"}]},{"id":"TH-F02","name":"What survives a rename, transfer or split?","description":"What survives a rename, transfer or split?","questions":[{"id":"TH-Q02","text":"What survives a rename, transfer or split?","kind":"governed-context","answer_data":["External identity decision and fixed timeline header","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A02","name":"External identity decision and fixed timeline header","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT02","description":"Keep stable scope; create a new governed scope when meaning changes"}]},{"id":"TH-F03","name":"Can two masters or values apply simultaneously?","description":"Can two masters or values apply simultaneously?","questions":[{"id":"TH-Q03","text":"Can two masters or values apply simultaneously?","kind":"governed-context","answer_data":["Scope/master register and separate context keys","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A03","name":"Scope/master register and separate context keys","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT03","description":"Separate scopes; request an authority decision, never silently choose a winner"}]}]},{"id":"TH-L-bindings","name":"Schema and state bindings","description":"Schema and state bindings for one governed temporal assertion scope.","findings":[{"id":"TH-F04","name":"Which schema interprets this value?","description":"Which schema interprets this value?","questions":[{"id":"TH-Q04","text":"Which schema interprets this value?","kind":"governed-context","answer_data":["Exact schema ID, numeric version and digest; external payload pin","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A04","name":"Exact schema ID, numeric version and digest; external payload pin","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT04","description":"Check accepted tuple; delegate payload validation"}]},{"id":"TH-F05","name":"Which status axis and vocabulary are in use?","description":"Which status axis and vocabulary are in use?","questions":[{"id":"TH-Q05","text":"Which status axis and vocabulary are in use?","kind":"governed-context","answer_data":["State profile pin, axis and code","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A05","name":"State profile pin, axis and code","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT05","description":"Check vocabulary membership only"}]},{"id":"TH-F06","name":"Did a legitimate domain transition occur?","description":"Did a legitimate domain transition occur?","questions":[{"id":"TH-Q06","text":"Did a legitimate domain transition occur?","kind":"governed-context","answer_data":["Host transition definition, execution and provenance evidence","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A06","name":"Host transition definition, execution and provenance evidence","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT06","description":"Route to the domain owner; report legality not evaluated"}]}]}]},{"id":"TH-B-history","name":"Effective and recorded history","description":"Effective and recorded history with explicit uncertainty and host responsibility.","layers":[{"id":"TH-L-valid","name":"Effective intervals","description":"Effective intervals for one governed temporal assertion scope.","findings":[{"id":"TH-F07","name":"What is recorded as effective on the selected date?","description":"What is recorded as effective on the selected date?","questions":[{"id":"TH-Q07","text":"What is recorded as effective on the selected date?","kind":"governed-context","answer_data":["Explicit validAt and selected segment","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A07","name":"Explicit validAt and selected segment","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT07","description":"Resolve within the selected recorded snapshot"}]},{"id":"TH-F08","name":"Does the exact endpoint belong to this interval?","description":"Does the exact endpoint belong to this interval?","questions":[{"id":"TH-Q08","text":"Does the exact endpoint belong to this interval?","kind":"governed-context","answer_data":["Half-open interval boundaries","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A08","name":"Half-open interval boundaries","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT08","description":"Exclude validTo; reject zero duration or overlap"}]},{"id":"TH-F09","name":"What do uncovered periods or an empty snapshot mean?","description":"What do uncovered periods or an empty snapshot mean?","questions":[{"id":"TH-Q09","text":"What do uncovered periods or an empty snapshot mean?","kind":"governed-context","answer_data":["Coverage gaps and missing-context explanation","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A09","name":"Coverage gaps and missing-context explanation","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT09","description":"Return insufficient context, never false"}]}]},{"id":"TH-L-receipt","name":"Receipts and corrections","description":"Receipts and corrections for one governed temporal assertion scope.","findings":[{"id":"TH-F10","name":"What had this Dimension recorded by a cutoff?","description":"What had this Dimension recorded by a cutoff?","questions":[{"id":"TH-Q10","text":"What had this Dimension recorded by a cutoff?","kind":"governed-context","answer_data":["knownAt, optional knownSequence and selected receipt","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A10","name":"knownAt, optional knownSequence and selected receipt","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT10","description":"Choose the latest eligible commit; before first receipt return unknown"}]},{"id":"TH-F11","name":"Which of two same-second receipts is intended?","description":"Which of two same-second receipts is intended?","questions":[{"id":"TH-Q11","text":"Which of two same-second receipts is intended?","kind":"governed-context","answer_data":["Host sequence and receipt time","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A11","name":"Host sequence and receipt time","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT11","description":"Pin the returned sequence for stable historical content"}]},{"id":"TH-F12","name":"How does a late correction preserve earlier answers?","description":"How does a late correction preserve earlier answers?","questions":[{"id":"TH-Q12","text":"How does a late correction preserve earlier answers?","kind":"governed-context","answer_data":["Two complete snapshots and predecessor digest","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A12","name":"Two complete snapshots and predecessor digest","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT12","description":"Append a corrected snapshot; compare historical answers"}]}]}]},{"id":"TH-B-control","name":"Authority and controlled operations","description":"Authority and controlled operations with explicit uncertainty and host responsibility.","layers":[{"id":"TH-L-writes","name":"Write integrity","description":"Write integrity for one governed temporal assertion scope.","findings":[{"id":"TH-F13","name":"Was this retry already applied?","description":"Was this retry already applied?","questions":[{"id":"TH-Q13","text":"Was this retry already applied?","kind":"governed-context","answer_data":["Original key, full request and first receipt","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A13","name":"Original key, full request and first receipt","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT13","description":"Return unchanged root only for exact authorized replay"}]},{"id":"TH-F14","name":"Is this write based on the current head?","description":"Is this write based on the current head?","questions":[{"id":"TH-Q14","text":"Is this write based on the current head?","kind":"governed-context","answer_data":["Expected/current head and host conflict artifact","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A14","name":"Expected/current head and host conflict artifact","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT14","description":"Reject stale writes; host records conflict without altering history"}]},{"id":"TH-F15","name":"Who may assert this scope now?","description":"Who may assert this scope now?","questions":[{"id":"TH-Q15","text":"Who may assert this scope now?","kind":"governed-context","answer_data":["Current host config, authenticated writer and mastership evidence","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A15","name":"Current host config, authenticated writer and mastership evidence","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT15","description":"Require current grant; preserve old attribution"}]}]},{"id":"TH-L-reads","name":"Historical disclosure","description":"Historical disclosure for one governed temporal assertion scope.","findings":[{"id":"TH-F16","name":"May this role read historical data for this purpose?","description":"May this role read historical data for this purpose?","questions":[{"id":"TH-Q16","text":"May this role read historical data for this purpose?","kind":"governed-context","answer_data":["Current full-timeline reader/purpose decision","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A16","name":"Current full-timeline reader/purpose decision","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT16","description":"Deny before hidden ledger/query diagnostics"}]},{"id":"TH-F17","name":"Does a pinned assertion establish truth or permission?","description":"Does a pinned assertion establish truth or permission?","questions":[{"id":"TH-Q17","text":"Does a pinned assertion establish truth or permission?","kind":"governed-context","answer_data":["Selected assertion plus independently governed evidence","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A17","name":"Selected assertion plus independently governed evidence","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT17","description":"Report truth and transition legality as unevaluated"}]}]}]},{"id":"TH-B-adoption","name":"Adoption and continuity","description":"Adoption and continuity with explicit uncertainty and host responsibility.","layers":[{"id":"TH-L-continuity","name":"Archival and import","description":"Archival and import for one governed temporal assertion scope.","findings":[{"id":"TH-F18","name":"What changes when this timeline is archived?","description":"What changes when this timeline is archived?","questions":[{"id":"TH-Q18","text":"What changes when this timeline is archived?","kind":"governed-context","answer_data":["Archive commit and unchanged segment snapshot","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A18","name":"Archive commit and unchanged segment snapshot","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT18","description":"Freeze new writes; retain historical reads"}]},{"id":"TH-F19","name":"How can an imported history avoid forged local knowledge?","description":"How can an imported history avoid forged local knowledge?","questions":[{"id":"TH-Q19","text":"How can an imported history avoid forged local knowledge?","kind":"governed-context","answer_data":["Actual local receipt and separate sourceRecordedAt","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A19","name":"Actual local receipt and separate sourceRecordedAt","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT19","description":"Admit at local receipt; refuse backdated bootstrap"}]},{"id":"TH-F20","name":"Which precision or calendar adapter is required?","description":"Which precision or calendar adapter is required?","questions":[{"id":"TH-Q20","text":"Which precision or calendar adapter is required?","kind":"governed-context","answer_data":["Original civil/offset/fractional time and pinned conversion rules","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A20","name":"Original civil/offset/fractional time and pinned conversion rules","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT20","description":"Reject unsupported input; do not silently truncate"}]}]},{"id":"TH-L-integration","name":"Composition and migration","description":"Composition and migration for one governed temporal assertion scope.","findings":[{"id":"TH-F21","name":"What is the minimum useful Company Dimension setup?","description":"What is the minimum useful Company Dimension setup?","questions":[{"id":"TH-Q21","text":"What is the minimum useful Company Dimension setup?","kind":"governed-context","answer_data":["One scope, config, external value/schema pin and first snapshot","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A21","name":"One scope, config, external value/schema pin and first snapshot","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT21","description":"Install own companion identity and validate nested snapshot"}]},{"id":"TH-F22","name":"Can we migrate or export without losing recorded history?","description":"Can we migrate or export without losing recorded history?","questions":[{"id":"TH-Q22","text":"Can we migrate or export without losing recorded history?","kind":"governed-context","answer_data":["Full same-version ledger, checksums, predecessor and loss analysis","If unavailable: insufficient-context; name missing evidence. A denied read remains denied."]}],"artifacts":[{"id":"TH-A22","name":"Full same-version ledger, checksums, predecessor and loss analysis","description":"Exact references or reproducible report; no implicit truth or authority."}],"actions":[{"id":"TH-ACT22","description":"Allow same-version roundtrip; refuse unsupported migration"}]}]}]}]},"statistics":{"bundles":4,"layers":8,"findings":22,"questions":22,"artifacts":22,"actions":22},"catalogue":{"alternateNames":["Time, states and versions","Bitemporal fact history"],"domain":["Enterprise","Temporal history","Lifecycle"],"tags":["temporal","history","bitemporal","schema","lifecycle"],"adoption":"Start with one fact scope, a pinned domain value and its schema, then append complete effective-time snapshots. Query by effective date and recorded cutoff; later corrections preserve earlier recorded views. The package includes three synthetic examples, a closed schema, a reference validator and native installation checks.","limits":"A trusted host owns authentication, latest history, receipt clock and durable conflict handling. This companion does not establish source truth, domain transition legality or payload-schema conformance."}}
END COMPLETE TREE

END FROZEN CANDIDATE EM-XCT-04-R1. Return verdict, actual supplied-input completeness, concrete findings, and limits.
