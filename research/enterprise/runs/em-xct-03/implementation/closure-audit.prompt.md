NO-TOOLS scoped closure audit. Original Enterprise Assertion Provenance 0.1.0, bounded trusted-host companion. Earlier Claude and Grok audits both ACCEPT WITH LIMITS, but recommended fixing genesis/basis-swap confidence asymmetry and same-Activity-ID pseudo-fresh review. We implemented the fixes. Give ACCEPT WITH LIMITS or BLOCK on these changes in this exact candidate, not a new global conformance claim. No execution, web or publication authorization.

The full current provenance.py and all 76 test methods plus fixture helpers follow, uncompressed, to repair the previous Grok attachment truncation of test_provenance.py. The schema, full native harness, AGENTS and full contract were supplied in preceding audits, but are not repeated here: schema/native unchanged; updated normative contract excerpts supplied below. This standalone CLI pass is a scoped code/tests/contract-excerpt review, not full-file ratification of omitted context. Explicitly report any truncation and final sentinel. Prior responses, including the truncated-input Grok pass, remain preserved.

Rules: Capture, Activity, ProvenanceRecord, EvidenceLink, ConfidenceAssessment have exact local revision/digest refs and independent immutable anchors. An append-only bounded register uses strict per-second trusted receipts, config kind/scope writer grants, whole-register readers/purposes and current root supplied by a trusted host. Five epistemic kinds stay distinct. No truth, permission, source authenticity, probability or independent-source proof. Label enum insufficient/limited/supported is declared purpose-qualified judgement, not a probability. Schema is closed with exact required fields shown by fixtures, URI/date-time validators and bounded collections. The code independently parses all timestamps, rejects fractional revision encodings, gates view before ledger diagnostics, and explicitly enforces semantics beyond schema. Native V3 remains a separate envelope check.

Latest fixes: every non-insufficient assessment genesis and any change to its label/basis/activity triggers current-active transitive closure and captured/non-mismatched Capture requirements. Such corrections require a DIFFERENT Activity ID (not merely a new revision), recorded after the previous assessment. Review receipts must be no earlier than explicit basis receipts. Thus new-ID/genesis, unchanged-label basis swap and same-ID review-metadata bypasses are rejected. Metadata-only corrections with unchanged label/basis/activity and reductions to insufficient preserve historical pins/warnings. Evidence relevance and genuine event execution remain assessor/host declarations, not invented verification. Import/snapshot now also config_check at mandatory trusted now. Encoding control/Unicode byte vector added. Reported execution: all 76 tests and three distinct synthetic native Dimensions pass; you did not execute them.

Remaining integration requirements: authenticate actor, own latest complete root/config/clock, serialize updates; generic write-only receipt/errors (admit remains internal and returns ledger), preparse byte cap, CPU budget, rollover planning. Structural limits 10000 records / 8 MiB are not throughput claims. Deferred PKI/fetch/legal/retention/fine-grained disclosure/production or parent conformance.

FILE provenance.py SHA256 d66a839643607e044b3ef0b9d5817d57e4283f3c84538a3db258f56e27248ee8
"""Original bounded trusted-host reference; no IAM, fetching or truth inference."""
from pathlib import Path
from datetime import datetime
import copy,hashlib,json,re
from jsonschema import Draft202012Validator,FormatChecker,ValidationError
HERE=Path(__file__).resolve().parent
VERSION='0.1.0'
class Invalid(ValueError):pass
class Denied(PermissionError):pass
def require(ok,message):
    if not ok:raise Invalid(message)
def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def encode(value):
    try:raw=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
    except (TypeError,ValueError,UnicodeError,RecursionError) as e:raise Invalid('Not bounded JSON') from e
    require(len(raw)<=8*1024*1024,'Serialized JSON exceeds 8 MiB')
    return raw
def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
def pin(row):return {'id':row['id'],'revision':row['revision'],'digest':digest(row)}
SCHEMA=load(HERE/'provenance.schema.json')
SCHEME={k:SCHEMA['x-confidenceScheme'][k] for k in ['id','revision']}|{'digest':digest(SCHEMA['x-confidenceScheme'])}
def validate(value,kind=None):
    encode(value)
    require(kind is None or kind in SCHEMA['$defs'],'Unknown record type')
    checker=FormatChecker()
    require(all(k in checker.checkers for k in ['uri','date-time']),'Required URI/date-time format checker unavailable')
    todo=[value]
    while todo:
        item=todo.pop()
        if isinstance(item,dict):
            for k,v in item.items():
                if k=='revision':require(type(v) is int,'Revision must be a JSON integer without a fractional encoding')
                if k in ['recordedAt','obtainedAt','startedAt','endedAt','validFrom','validUntil']:instant(v)
                todo.append(v)
        elif isinstance(item,list):todo.extend(item)
    schema=SCHEMA if kind is None else {'$schema':SCHEMA['$schema'],'$defs':SCHEMA['$defs'],'$ref':'#/$defs/'+kind}
    try:Draft202012Validator(schema,format_checker=checker).validate(value)
    except (ValidationError,RecursionError) as e:raise Invalid('Schema mismatch') from e
def instant(s):
    require(isinstance(s,str) and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',s) is not None,'ASCII UTC instant required')
    try:return datetime.strptime(s,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:raise Invalid('Invalid UTC time') from e
def config_check(config,now):
    validate(config,'configuration');instant(now)
    require(config['validFrom']<config['validUntil'],'Empty configuration interval')
    if not config['validFrom']<=now<config['validUntil']:raise Denied('Access denied')
def gate(config,actor,purpose,now):
    try:config_check(config,now)
    except Denied:raise Denied('Read denied') from None
    if actor not in config['readers'] or purpose not in config['purposes']:raise Denied('Read denied')
def ref_slots(r):
    k=r['kind']
    if k=='Activity':return {'inputs':r['inputs']}
    if k=='ProvenanceRecord':return {'activity':[] if r['activity'] is None else [r['activity']]}
    if k=='EvidenceLink':return {'evidence':[r['evidence']]}
    if k=='ConfidenceAssessment':return {'account':[r['account']],'activity':[r['activity']],'basis':r['basis']}
    return {}
def refs(r):return [p for pins in ref_slots(r).values() for p in pins]
ANCHORS={
'Capture':['sourceRef','sourceVersion','aboutRef','obtainedAt','mode','availability','representationDigest'],
'Activity':['actor','mode','startedAt','endedAt','inputs','observedTarget','method'],
'ProvenanceRecord':['claim','aboutRef','asserter','epistemicKind'],
'EvidenceLink':['claim','evidence','attributedTo','relation'],
'ConfidenceAssessment':['account','assessor','method','scheme','purpose'],
}
def semantic(r,prior,heads,old=None):
    retained={(field,encode(p)) for field,pins in ref_slots(old).items() for p in pins} if old else set()
    new_judgement=r['kind']=='ConfidenceAssessment' and r['label']!='insufficient' and (old is None or any(r[f]!=old[f] for f in ['label','basis','activity']))
    if new_judgement:
        retained=set()
        if old is not None:require(r['activity']['id']!=old['activity']['id'],'Changed reliance judgement needs a fresh review activity ID')
    def resolve(p,types=None,current=None,field=None):
        target=prior.get((p['id'],p['revision']))
        require(target is not None and pin(target)==p,'Unresolved exact internal pin')
        require(target['scope']==r['scope'],'Cross-scope internal link')
        if current is None:current=(field,encode(p)) not in retained
        require(target['state']=='active','Reliance target was already withdrawn')
        if current:require(pin(heads[p['id']])==p,'New link to inactive or superseded revision')
        require(types is None or target['kind'] in types,'Wrong internal target type')
        return target
    k=r['kind']
    for field,pins in ref_slots(r).items():
        for p in pins:resolve(p,field=field)
    # Revision pins form a DAG; additionally reject self-support through a
    # previous revision of this same semantic identity.
    todo=list(refs(r));visited=set()
    while todo:
        p=todo.pop();key=(p['id'],p['revision'])
        require(p['id']!=r['id'],'Self-derivation across revisions')
        if new_judgement:
            target=prior[key];head=heads[p['id']]
            require(pin(head)==p and head['state']=='active','Changed reliance judgement has stale or withdrawn dependencies')
            require(target['kind']!='Capture' or (target['availability']=='captured' and target['integrity']!='mismatched'),'Changed reliance judgement has unavailable or mismatched capture')
        if key not in visited:
            visited.add(key);todo.extend(refs(prior[key]))
    if k=='Capture':
        require(r['obtainedAt']<=r['recordedAt'],'Capture after receipt')
        require((r['availability']=='captured')==(r['representationDigest'] is not None),'Capture digest/availability mismatch')
        require(r['availability']=='captured' or r['integrity']=='not-tested','Unavailable capture cannot have checked integrity')
    elif k=='Activity':
        require(r['startedAt']<=r['endedAt']<=r['recordedAt'],'Activity time mismatch')
        inputs=[resolve(p,['Capture','ProvenanceRecord'],field='inputs') for p in r['inputs']]
        for source in inputs:
            available_at=source['obtainedAt'] if source['kind']=='Capture' else None
            if source['kind']=='ProvenanceRecord' and source['activity'] is not None:
                producer=prior[(source['activity']['id'],source['activity']['revision'])]
                available_at=producer['endedAt']
            require(available_at is None or available_at<=r['endedAt'],'Input event follows consuming activity')
        if r['mode'] in ['file-acquisition','live-observation']:
            require(bool(inputs) and all(x['kind']=='Capture' for x in inputs),'Acquisition requires captures')
            mode='live-api' if r['mode']=='live-observation' else 'file'
            require(all(x['mode']==mode and x['availability']=='captured' for x in inputs),'Acquisition mode mismatch')
            require(all(r['startedAt']<=x['obtainedAt']<=r['endedAt'] for x in inputs),'Capture outside activity')
        if r['mode']=='live-observation':
            require(r['observedTarget'] is not None and all(x['aboutRef']==r['observedTarget'] for x in inputs),'Observed target mismatch')
        else:require(r['observedTarget'] is None,'Only live observation declares observed target')
        if r['mode'] in ['synthesis','review']:require(bool(inputs),'Analysis needs inputs')
        if r['mode']=='review':require(all(x['kind']=='ProvenanceRecord' for x in inputs),'Review targets accounts')
    elif k=='ProvenanceRecord':
        if r['epistemicKind']=='unverified':require(bool(r['limitations']),'Unverified account needs explicit limitations')
        else:require(r['activity'] is not None,'Account needs generating activity')
        if r['activity'] is not None:
            a=resolve(r['activity'],['Activity'],field='activity')
            expected={'observed':['live-observation'],'source-asserted':['file-acquisition','live-observation'],'inferred':['synthesis'],'proposed':['proposal']}
            require(r['epistemicKind']=='unverified' or a['mode'] in expected[r['epistemicKind']],'Epistemic/activity mismatch')
            if r['epistemicKind']=='observed':require(r['aboutRef']==a['observedTarget'],'Observed account target mismatch')
            if r['epistemicKind']=='source-asserted':
                require(all(resolve(p,['Capture'],current=False)['aboutRef']==r['aboutRef'] for p in a['inputs']),'Source assertion target mismatch')
    elif k=='EvidenceLink':resolve(r['evidence'],['Capture','ProvenanceRecord'],field='evidence')
    elif k=='ConfidenceAssessment':
        resolve(r['account'],['ProvenanceRecord'],field='account');a=resolve(r['activity'],['Activity'],field='activity')
        require(a['mode']=='review' and r['account'] in a['inputs'],'Assessment needs review of its exact account')
        require(a['actor']==r['assessor'] and a['method']==r['method'],'Assessment reviewer/method mismatch')
        require(r['scheme']==SCHEME,'Unknown confidence scheme pin')
        for p in r['basis']:resolve(p,['Capture','ProvenanceRecord','EvidenceLink'],field='basis')
        if new_judgement:
            require(old is None or old['recordedAt']<a['recordedAt'],'Fresh review must be recorded after the previous assessment')
            require(all(prior[(p['id'],p['revision'])]['recordedAt']<=a['recordedAt'] for p in r['basis']),'Review recorded before its evidence basis')
        if r['label']=='limited':require(bool(r['limitations']),'Limited assessment needs limitations')

def validate_ledger(ledger,config=None,now=None):
    validate(ledger)
    if now is not None:
        instant(now)
        require(all(r['recordedAt']<=now for r in ledger['records']),'Receipt follows trusted now')
    if config is not None:
        validate(config,'configuration');require(ledger['dimension']==config['dimension'],'Dimension mismatch')
    prior={};heads={};last=None
    for r in ledger['records']:
        require(last is None or last<r['recordedAt'],'Receipts must strictly increase')
        old=heads.get(r['id'])
        if old is None:
            require(r['revision']==1 and r['previousDigest'] is None and r['change']=='create' and r['state']=='active','Invalid genesis')
        else:
            require(r['kind']==old['kind'] and r['scope']==old['scope'],'Identity kind/scope changed')
            require(r['revision']==old['revision']+1 and r['previousDigest']==digest(old),'Broken revision chain')
            require(old['state']=='active','Withdrawal is terminal')
            require(all(r[f]==old[f] for f in ANCHORS[r['kind']]),'Identity anchor changed')
            require((r['change'],r['state']) in [('correct','active'),('withdraw','withdrawn')],'Invalid revision transition')
            if r['change']=='withdraw':
                allowed={'revision','previousDigest','recordedAt','writer','state','change','reason'}
                require(all(r[f]==old[f] for f in r if f not in allowed),'Withdrawal changes content')
        # A withdrawal preserves references even if those have subsequently
        # been superseded. It makes no new reliance assertion.
        if r['change']!='withdraw':semantic(r,prior,heads,old)
        prior[(r['id'],r['revision'])]=r;heads[r['id']]=r;last=r['recordedAt']
    return True

def admit(previous,record,config,actor,now):
    """Host-internal API. Return no ledger/diagnostics to a write-only client."""
    config_check(config,now)
    require(isinstance(record,dict) and record.get('kind') in ANCHORS,'Unknown record type')
    validate(record,record['kind'])
    if record['writer']!=actor or not any(g['kind']==record['kind'] and g['scope']==record['scope'] and actor in g['actors'] for g in config['writers']):
        raise Denied('Write denied')
    require(record['recordedAt']==now,'Receipt must equal trusted now')
    validate_ledger(previous,config,now)
    for old in previous['records']:
        if (old['id'],old['revision'])==(record['id'],record['revision']):
            require(encode({k:v for k,v in old.items() if k!='recordedAt'})==encode({k:v for k,v in record.items() if k!='recordedAt'}),'Conflicting replay')
            return copy.deepcopy(previous)
    candidate=copy.deepcopy(previous);candidate['records'].append(copy.deepcopy(record));validate_ledger(candidate,config,now)
    return candidate

def validate_extension(previous,candidate,config,now=None):
    validate_ledger(previous,config,now);validate_ledger(candidate,config,now)
    require(encode({k:v for k,v in previous.items() if k!='records'})==encode({k:v for k,v in candidate.items() if k!='records'}),'Register header changed')
    require(encode(candidate['records'][:len(previous['records'])])==encode(previous['records']),'Historical prefix rewritten or truncated')
    return True

def view(ledger,config,actor,purpose,claim,knownAt,now):
    gate(config,actor,purpose,now) # before any ledger/query diagnostic
    instant(knownAt);require(knownAt<=now,'Future knowledge cut');validate(claim,'pin');validate_ledger(ledger,config,now)
    known=[r for r in ledger['records'] if r['recordedAt']<=knownAt];heads={r['id']:r for r in known};by={(r['id'],r['revision']):r for r in known}
    def closure(r):
        result={};todo=list(refs(r))
        while todo:
            p=todo.pop();key=(p['id'],p['revision'])
            if key in result:continue
            node=by[key];result[key]=node;todo.extend(refs(node))
        return list(result.values())
    accounts=[r for r in heads.values() if r['kind']=='ProvenanceRecord' and r['claim']==claim]
    links=[r for r in heads.values() if r['kind']=='EvidenceLink' and r['claim']==claim]
    assessments=[r for r in heads.values() if r['kind']=='ConfidenceAssessment' and by[(r['account']['id'],r['account']['revision'])]['claim']==claim]
    impacts=[]
    for r in accounts+links+assessments:
        dependencies=closure(r)
        changed=[{'cited':pin(x),'current':pin(heads[x['id']]),'state':heads[x['id']]['state'],**({'currentCaptureState':{'availability':heads[x['id']]['availability'],'integrity':heads[x['id']]['integrity']}} if x['kind']=='Capture' else {})} for x in dependencies if pin(x)!=pin(heads[x['id']]) or heads[x['id']]['state']=='withdrawn']
        gaps=[{'pin':pin(x),'availability':x['availability'],'integrity':x['integrity']} for x in dependencies if x['kind']=='Capture' and (x['availability']=='unavailable' or x['integrity']=='mismatched')]
        impacts.append({'record':pin(r),'state':r['state'],'requiresReview':bool(changed or gaps),'changedDependencies':changed,'sourceGaps':gaps})
    origins={}
    for a in accounts:
        if a['state']!='active':continue
        for x in closure(a):
            if x['kind']=='Capture':
                for label,value in [('bytes',x['representationDigest']),('declared-origin',x['originRef'])]:
                    if value is not None:origins.setdefault((label,value),set()).add(a['id'])
    shared=[{'basis':k[0],'value':k[1],'accounts':sorted(v)} for k,v in sorted(origins.items()) if len(v)>1]
    return {'profileVersion':VERSION,'claim':copy.deepcopy(claim),'knownAt':knownAt,'inputSliceDigest':digest({**ledger,'records':known}),'configurationDigest':digest(config),
        'status':'context-available' if any(r['state']=='active' and r['epistemicKind']!='unverified' for r in accounts) else 'insufficient-context',
        'accounts':copy.deepcopy(accounts),'links':copy.deepcopy(links),'assessments':copy.deepcopy(assessments),'impacts':impacts,
        'independence':{'status':'known-shared-origin' if shared else 'unknown','shared':shared},
        'truth':'not-evaluated','permissions':'not-inferred'}

def import_snapshot(snapshot,config,*,now):
    config_check(config,now);validate_ledger(snapshot,config,now);return copy.deepcopy(snapshot)
def migrate(snapshot,config,targetVersion,*,now):
    require(targetVersion==VERSION,'Unsupported or lossy migration requires explicit mapping')
    return import_snapshot(snapshot,config,now=now)

def validate_snapshot(fact,config,previous=None,*,now):
    """Check companion snapshot pins; use V3 separately for the full envelope."""
    require(isinstance(fact,dict) and fact.get('recordType')=='fact' and fact.get('path')=='provenance.register.snapshot','Wrong snapshot envelope')
    require(isinstance(fact.get('factId'),str) and bool(fact['factId']),'Missing snapshot identity')
    config_check(config,now);ledger=fact.get('value');validate_ledger(ledger,config,now)
    require(fact.get('subjectId')==ledger['dimension']+':provenance-register','Wrong aggregate subject')
    provenance=fact.get('provenance',{})
    require(isinstance(provenance,dict) and provenance.get('snapshotDigest')==digest(ledger),'Wrong snapshot digest')
    if previous is None:
        require(provenance.get('previousSnapshotDigest') is None and fact.get('supersedes')==[],'Missing trusted previous snapshot')
    else:
        require(isinstance(previous,dict) and previous.get('recordType')=='fact' and previous.get('subjectId')==fact['subjectId'] and previous.get('path')==fact['path'],'Snapshot lineage mismatch')
        require(previous.get('factId')!=fact['factId'],'Snapshot identity reused')
        previous_ledger=previous.get('value');validate_extension(previous_ledger,ledger,config,now)
        previous_provenance=previous.get('provenance')
        require(isinstance(previous.get('factId'),str) and isinstance(previous_provenance,dict) and previous_provenance.get('snapshotDigest')==digest(previous_ledger),'Wrong previous snapshot digest')
        require(provenance.get('previousSnapshotDigest')==digest(previous_ledger) and fact.get('supersedes')==[previous.get('factId')],'Wrong snapshot predecessor')
    return True

END FILE provenance.py

FILE test_provenance.py SHA256 5e3f053099f47d9c3f76fdf6cf2869c2f514362bcc6e6d89abcc2924c61b509a
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

END FILE test_provenance.py

EXACT CURRENT CONTRACT EXCERPTS
ConfidenceAssessment uses the bundled original qualitative-reliance scheme, pinned by SHA-256 of the scheme's sorted compact UTF-8 JSON representation. The schema embeds the same scheme for a self-contained native installation. Labels are insufficient/limited/supported **for the named purpose under the named method**, not probability or universal confidence. Limited requires limitations. Activity must be review of the exact account, actor equals assessor and method pins match. Numerical values, percentages, cross-method averaging and automatic cross-scheme mapping are rejected/deferred. Method-pin authenticity, evidence relevance to the account/claim and the quality of the assessor's judgement remain external. Receipt ordering checks when the recorder registered a review; it does not authenticate the real-world execution time.

A correction follows the immediate previous revision and digest, retains all prior rows and immutable anchors, and remains active. Unchanged historical dependencies may be retained when correcting notes, limitations, selectors, rationale or reducing an assessment label to insufficient. Every new assessment with a non-insufficient label, and every change to a non-insufficient assessment's label, basis or activity, requires every immediate and transitive dependency to be a current active revision; Capture dependencies must be available without declared integrity mismatch. On such a correction the review Activity must have a different ID and be recorded after the previous assessment. Every such review must be recorded no earlier than its explicit basis revisions. This check does not certify the new judgement or truth. Keeping label, basis and activity unchanged permits metadata maintenance, with changed-dependency warnings intact. Reduction to insufficient remains available when dependencies have changed; reduction from supported to limited uses the same current-basis rule as other non-insufficient reassessment. A pin moved to a different field is a new reference, even if its bytes were already present elsewhere in the record. Newly introduced/replaced immediate pins must be current and active. Correcting a judgement about an older account does not retarget it to the latest account; a fresh review needs a new review Activity and assessment. Withdrawal is terminal and changes only revision, previousDigest, receipt, writer, state, change and reason. It cannot rewrite the withdrawn content. Resurrecting, deleting or truncating records is unsupported. Retracting a capture/account/link or correcting its basis does not automatically negate an external claim or alter downstream epistemic kinds; a view reports the affected dependency pins for reassessment.

`import_snapshot`, `migrate` and `validate_snapshot` require keyword `now` from the trusted host, require the configuration to be valid at that instant, and reject any inner receipt after that instant. `admit` and `view` always apply the same bound. `validate_ledger` and `validate_extension` accept an optional `now`; omitting it performs an offline consistency check only. These checks do not authenticate imported history or discover a newer root. An initial snapshot may contain a complete pre-existing history; accepting it is an explicit host bootstrap/import decision. A successor must have a different factId; a byte-identical no-op successor remains allowed. Previous-root trust and full native envelope checks remain host requirements.

Encoding test vector: input `{"revision":1,"a":"é\n\u0001\u2028\u2029"}` encodes to UTF-8 hex `7b2261223a22c3a95c6e5c7530303031e280a8e280a9222c227265766973696f6e223a317d`. Python uses the short escapes for backspace/form-feed/newline/carriage-return/tab, escapes quotes and backslashes, uses lowercase `\u00xx` for remaining control characters, and does not escape U+2028/U+2029. No Unicode normalization is performed.

END EXCERPTS
FINAL SENTINEL AP-CLOSURE-76-FULL-TESTS
