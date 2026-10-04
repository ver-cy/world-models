NO-TOOLS scoped follow-up on one remaining blocking defect. Enterprise Assertion Provenance 0.1.0 is a bounded trusted-host reviewable draft. Previous compact closure audit: Claude BLOCK on metadata revision receipts laundering an old review; Grok ACCEPT WITH LIMITS. Both raw responses remain preserved; no vote averaging. We adopted the exact genesis-receipt fix and five regression tests.

Current code now computes review_at=prior[(a['id'],1)]['recordedAt'] and compares BOTH previous-assessment receipt and explicit basis receipts to that identity-genesis receipt. Corrections of the same Activity cannot change it. Different review ID, current-active full dependency closure and available/non-mismatched captures remain required for non-insufficient genesis or label/basis/activity changes. Host authentication/current root/config/clock/concurrency and generic write-only receipts/errors remain external. This proves registration order, NOT real-world execution or evidence relevance.

Review only this fix and regressions against the preceding findings; return ACCEPT WITH LIMITS or BLOCK with concrete residuals. No tools, execution, web or publication permission. Full current provenance.py, exact contract paragraph, original blocking report, fixture helpers and the five appended tests are supplied. The other 76 tests were supplied fully in the preceding compact pass to both reviewers and are unchanged; this prompt does not repeat them or the schema/harness. Reported local result now 81 tests and three native Dimensions passed. Do not claim your own execution or whole-package conformance. Confirm final sentinel and any truncation.

PRECEDING CLAUDE FINDING (untrusted review evidence)
# Scoped closure audit: EAP 0.1.0 genesis/basis-swap and fresh-review fixes

**Verdict: BLOCK on this exact candidate.** The fix is narrow and cheap. Everything else in scope looks acceptable with the stated limits.

## Input integrity

- **Truncation:** none observed. Both files end with their `END FILE` markers.
- **Test count:** I counted 76 test methods in `Tests`, numbered 1 `test_three_profiles` through 76 `test_canonical_encoding_control_and_unicode_vector`, plus the fixture helpers.
- **Contract excerpts:** received through `END EXCERPTS`.
- **Final sentinel:** `AP-CLOSURE-76-FULL-TESTS` received.
- **Not verified:** I executed nothing. I could not check the stated SHA-256 values or the reported 76 passes and native results.
- **Omitted context:** the schema, native harness and full contract were not re-read. This verdict does not ratify them.

## Blocking finding: fresh-review timing uses the revision receipt, so metadata revisions restore the bypass

In `semantic`, the two new timing guards compare against `a['recordedAt']`. That is the receipt of the pinned Activity *revision*, not of the review event:

```python
require(old is None or old['recordedAt']<a['recordedAt'], ...)
require(all(prior[...]['recordedAt']<=a['recordedAt'] for p in r['basis']), ...)
```

Activity anchors (actor, mode, times, inputs, method) cannot change on correction. So a metadata-only `correct` revision is the same registered event with a newer receipt. `test_review_metadata_revision_is_not_fresh_execution` states exactly this principle, but the code enforces it only when the review ID is the same.

**Variant 1: reassessment with an older alternate review.** This works directly on the `ai-team` fixture, using the same construction as `test_prior_review_cannot_reassess_later_judgement` plus one extra step:

1. Register review R2, then assessment A1 with activity R1.
2. Add `revision(R2, notes=[...])`, giving R2′ with a receipt later than A1.
3. Add `revision(A1, label='supported', activity=pin(R2′))`.

Every check passes: the IDs differ, R2′ is the current head, R2′ is recorded after A1, and the basis is recorded before R2′. It is accepted. A review registered before the previous judgement becomes "fresh" through a metadata edit.

**Variant 2: return to the original review through an insufficient step.**

1. A1 (limited, R1) → A2 (insufficient, R2). This is allowed because the label is insufficient.
2. Add R1′, a metadata revision of R1.
3. A3 (limited, R1′) passes, because the ID check compares only against A2's activity and R1′ is recorded after A2.

**Variant 3: genesis whose review precedes its basis.**

1. Register review R at t1 and capture C2 at t2.
2. Add R′, a metadata revision of R, at t3.
3. A new assessment with activity `pin(R′)` and basis `[pin(C2)]` passes the "before its evidence basis" check, even though the review event was registered before C2 existed.

**Impact:** The unchanged-label basis-swap and genesis closure checks do hold. But the same-Activity pseudo-fresh fix is only closed for a literally identical ID. The change's own claim that metadata revisions are not fresh execution does not hold.

**Minimal fix:** compare against the Activity identity's genesis receipt in both guards.

```python
review_at=prior[(a['id'],1)]['recordedAt']
require(old is None or old['recordedAt']<review_at, ...)
require(all(prior[(p['id'],p['revision'])]['recordedAt']<=review_at for p in r['basis']), ...)
```

This closes all three variants. A metadata-corrected review first registered after the previous assessment remains usable. A stricter alternative is to require `a['revision']==1` for any new judgement. Either way, update the contract wording from "recorded after" to "first registered (revision 1) after".

**Tests to add:**
- Variant 1 rejected.
- Variant 2 rejected.
- Variant 3 rejected.
- Positive case: a review first registered after A1, then metadata-corrected, is accepted for reassessment.

## Non-blocking findings (fix while re-cutting)

1. **Test precision on the capture rules.** `test_assessment_genesis_rejects_mismatched_basis`, `test_changed_judgement_rejects_transitive_stale_capture` and `test_changed_judgement_rejects_withdrawn_basis` use bare `assertRaises(p.Invalid)`. In each, the review's own closure reaches the superseded capture revision 1, so rejection comes from the stale-head rule. The "captured and not mismatched" rule on a *current* head is never exercised in isolation. Add a case where a capture is created at genesis with `integrity='mismatched'`, then used as basis, and assert on the `'unavailable or mismatched capture'` message.
2. **The Activity-ID rule is a declaration, not proof.** Any writer with an Activity grant can mint a new review ID by copying content, as `test_changed_judgement_positive` does. The contract already says execution is not verified. Keep saying that registration order is all this proves.

## Verified by reading (in scope)

- **new_judgement coverage:** the trigger covers genesis, label change (including supported → limited), basis swap and activity change. Reductions to insufficient and metadata-only corrections keep their retained pins, and view warnings remain.
- **Transitive closure:** the current-head, active and capture-state check is applied through the full closure, not just to immediate pins.
- **Pin field movement:** clearing `retained` means an existing pin moved to a different field counts as new.
- **Import/migrate/snapshot:** `import_snapshot`, `migrate` and `validate_snapshot` require keyword `now`, run `config_check` at that instant and bound inner receipts. The tests cover future receipts, expired configuration and a missing clock.
- **Encoding vector:** the hex matches sorted keys, the `\n` short escape, lowercase `\u0001` and raw U+2028/U+2029.
- **Fixture genesis:** the `ai-team` fixture assessment (limited, current closure, basis recorded before review) is a valid positive genesis under the new rules.

## Unchanged residuals

These remain as you stated: an authenticated actor, and a host-owned latest root, config and clock with serialized updates; generic write-only errors; a byte cap before parsing; a CPU budget (every `admit` revalidates the whole ledger); rollover planning; and the deferred PKI, fetch, legal, retention, disclosure and production/parent conformance work. No execution, web or publication authorization is implied.

END FINDING

FULL CURRENT provenance.py SHA256 304b788ec16f175f79ac2b7e2b0f4923ea1f1fbb3671d40fb1e3b55bed4b71db
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
            review_at=prior[(a['id'],1)]['recordedAt']
            require(old is None or old['recordedAt']<review_at,'Fresh review must be first registered after the previous assessment')
            require(all(prior[(p['id'],p['revision'])]['recordedAt']<=review_at for p in r['basis']),'Review first registered before its evidence basis')
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

END CODE

EXACT FIXTURE HELPERS
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


END HELPERS

FIVE APPENDED TESTS
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


END TESTS

EXACT CONTRACT PARAGRAPH
A correction follows the immediate previous revision and digest, retains all prior rows and immutable anchors, and remains active. Unchanged historical dependencies may be retained when correcting notes, limitations, selectors, rationale or reducing an assessment label to insufficient. Every new assessment with a non-insufficient label, and every change to a non-insufficient assessment's label, basis or activity, requires every immediate and transitive dependency to be a current active revision; Capture dependencies must be available without declared integrity mismatch. On such a correction the review Activity must have a different ID and be first registered (revision 1 receipt) after the previous assessment. Every such review must be first registered (revision 1 receipt) no earlier than its explicit basis revisions. This check does not certify the new judgement or truth. Keeping label, basis and activity unchanged permits metadata maintenance, with changed-dependency warnings intact. Reduction to insufficient remains available when dependencies have changed; reduction from supported to limited uses the same current-basis rule as other non-insufficient reassessment. A pin moved to a different field is a new reference, even if its bytes were already present elsewhere in the record. Newly introduced/replaced immediate pins must be current and active. Correcting a judgement about an older account does not retarget it to the latest account; a fresh review needs a new review Activity and assessment. Withdrawal is terminal and changes only revision, previousDigest, receipt, writer, state, change and reason. It cannot rewrite the withdrawn content. Resurrecting, deleting or truncating records is unsupported. Retracting a capture/account/link or correcting its basis does not automatically negate an external claim or alter downstream epistemic kinds; a view reports the affected dependency pins for reassessment.
END CONTRACT
FINAL SENTINEL AP-FIRST-REGISTRATION-81
