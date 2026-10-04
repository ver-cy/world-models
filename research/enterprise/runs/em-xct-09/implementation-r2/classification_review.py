"""Original bounded offline classification assessment. No business writes or network."""
from __future__ import annotations
import hashlib,json,re
from datetime import datetime
from pathlib import Path
from jsonschema import Draft202012Validator,FormatChecker

HERE=Path(__file__).resolve().parent
MODEL='vr.profile.enterprise-classification-review'
VERSION='0.1.0'
LIMIT=1024*1024

class Invalid(ValueError): pass
class Denied(ValueError): pass

def require(condition,message):
    if not condition: raise Invalid(message)

def _check(value,depth=0):
    require(depth<=32,'Nesting exceeds32')
    if isinstance(value,str):
        require(not any(ord(c)<32 or 127<=ord(c)<=159 or 0xD800<=ord(c)<=0xDFFF for c in value),'Invalid control/surrogate string')
    elif type(value) is int: require(abs(value)<=9007199254740991,'Integer out of range')
    elif value is None or type(value) is bool: pass
    elif isinstance(value,list):
        for x in value:_check(x,depth+1)
    elif isinstance(value,dict):
        for k,v in value.items():
            require(isinstance(k,str),'Nonstring key');_check(k,depth+1);_check(v,depth+1)
    else: raise Invalid('Unsupported value type; floating point is not accepted')

def encode(value):
    _check(value)
    raw=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
    require(len(raw)<=LIMIT,'Canonical value exceeds1MiB')
    return raw

def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()

def decode(raw):
    require(isinstance(raw,bytes) and len(raw)<=2*LIMIT,'Raw input exceeds2MiB or is not bytes')
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'Duplicate JSON key');d[k]=v
        return d
    try:
        value=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs)
        encode(value)
        return value
    except (UnicodeError,json.JSONDecodeError,RecursionError) as exc:raise Invalid('Invalid UTF-8 JSON') from exc

def stamp(s):
    require(isinstance(s,str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z',s) is not None,'Expected UTC seconds timestamp')
    try: return datetime.strptime(s,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as exc: raise Invalid('Invalid calendar timestamp') from exc

def interval(start,end):
    stamp(start)
    if end is not None:require(stamp(start)<stamp(end),'Empty/reversed half-open interval')

def within(at,start,end):return start<=at and (end is None or at<end)

def schema(value,name):
    encode(value)
    whole=json.loads((HERE/'classification.schema.json').read_text(encoding='utf-8'))
    selected=whole if name=='native' else {'$defs':whole['$defs'],'$ref':'#/$defs/'+name}
    validator=Draft202012Validator(selected,format_checker=FormatChecker())
    errors=list(validator.iter_errors(value))
    require(not errors,'Shape violation: '+('/'.join(map(str,errors[0].absolute_path)) if errors else ''))

def snapshot_digest(snapshot):return digest({k:v for k,v in snapshot.items() if k!='digest'})
def pin(snapshot):return {'id':snapshot['id'],'digest':snapshot['digest']}
def key(code):return code['scheme'],code['version'],code['code']
def code_value(k):return dict(zip(('scheme','version','code'),k))

def build_id():
    return digest({n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ['classification_review.py','classification.schema.json']})

def _assess(packet,approvals):
    """Consistency evaluator. Caller supplies already-authorized input; no access grant."""
    schema(packet,'packet')
    for name in ('knowledgeAt','effectiveAt','targetAt'):stamp(packet[name])
    require((packet['revision']==1)==(packet['previousDigest'] is None),'Revision/predecessor mismatch')
    require(len({x['id'] for x in packet['snapshots']})==len(packet['snapshots']),'Duplicate snapshot ID')
    snaps={x['id']:x for x in packet['snapshots']}
    findings=[];compiled={};approval_keys=set();source_coordinates={}
    # Approval basis is retained as evidence for replay, never used as a future grant.
    for a in approvals:
        k=(a['snapshotDigest'],a['entryId'],a['approver'],a['evidence'])
        require(k not in approval_keys,'Duplicate approval basis');approval_keys.add(k)
    def add(rule,outcome,question,evidence=()):
        f={'rule':rule,'outcome':outcome,'question':question,'evidence':list(evidence)}
        if f not in findings:findings.append(f)
    def get(ref,kind):
        require(ref['id'] in snaps,'Missing referenced snapshot')
        s=snaps[ref['id']]
        require(s['digest']==ref['digest'] and s['payload']['kind']==kind,'Wrong snapshot pin/kind')
        return s
    for s in snaps.values():
        require(snapshot_digest(s)==s['digest'],'Snapshot digest mismatch')
        stamp(s['capture']['at'])
        require(s['capture']['at']<=packet['knowledgeAt'],'Snapshot not known at knowledge cut')
        d=s['payload']
        coordinate=(d['kind'],d['scheme'],d['version']) if d['kind']=='scheme-release' else (d['kind'],d['id'],d['revision'] if d['kind']=='assignment' else d['version'])
        body=encode(d)
        require(coordinate not in source_coordinates or source_coordinates[coordinate]==body,'Conflicting source payloads for one coordinate')
        source_coordinates[coordinate]=body
        if d['kind']=='scheme-release':
            require(len({c['code'] for c in d['concepts']})==len(d['concepts']),'Duplicate code in release')
            for c in d['concepts']:interval(c['validFrom'],c['validUntil'])
        elif d['kind']=='assignment':
            interval(d['validFrom'],d['validUntil']);stamp(d['assertedAt'])
            require(d['assertedAt']<=s['capture']['at'],'Assertion after capture')
            require(len(set(map(key,d['values'])))==len(d['values']),'Duplicate category selection')
            require(d['origin']!='model-suggested' or d['method'] is not None,'Missing model method/version')
            if d['corrects'] is not None:
                old=get(d['corrects'],'assignment')['payload']
                require((old['id'],old['subjectId'],old['slot'])==(d['id'],d['subjectId'],d['slot']) and old['revision']<d['revision'],'Invalid correction predecessor')
        elif d['kind']=='crosswalk':
            require(len({e['id'] for e in d['entries']})==len(d['entries']),'Duplicate mapping entry ID')
            for e in d['entries']:
                interval(e['validFrom'],e['validUntil'])
                for side in ('sources','targets'):require(len(set(map(key,e[side])))==len(e[side]),'Duplicate mapping member')
                require(e['origin']!='model-suggested' or e['method'] is not None,'Missing model method/version')
                require(e['state']!='approved' or (e['approver'] is not None and bool(e['evidence'])),'Unattributed approval claim')
                require(e['sources'] or e['targets'],'Empty-to-empty correspondence')
    def compile_profile(ref,stack=()):
        require(ref['id'] not in stack and len(stack)<8,'Cyclic/deep profile ancestry')
        s=get(ref,'slot-profile');d=s['payload']
        if ref['id'] in compiled:
            cached=compiled[ref['id']]
            require(len(stack)+len(cached['ancestry'])<=8,'Cyclic/deep profile ancestry')
            return cached
        require(d['min']<=d['max'],'Reversed cardinality')
        allowed=set(map(key,d['allowed']));require(len(allowed)==len(d['allowed']),'Duplicate allowed code')
        require(d['min']<=len(allowed),'Unsatisfiable finite-set minimum')
        releases={};ready=True
        if d['min']>32:
            ready=False;add('PROFILE-CAPACITY','unsupported','Supply a profile whose minimum fits the32-selection instance capacity or a separately evaluated larger-capacity adapter.',[s['id']])
        require(d['releasePins'],'Missing release pins')
        for rp in d['releasePins']:
            rs=get(rp,'scheme-release');rd=rs['payload'];rk=(rd['scheme'],rd['version'])
            require(rk not in releases,'Conflicting or duplicate release snapshots')
            releases[rk]=rs
            if not rd['complete']:
                ready=False;add('RELEASE-COMPLETE','insufficient-context','Who supplies the complete frozen enumeration?',[rs['id']])
        require(len(releases)==len(d['releasePins']),'Duplicate release pin')
        for k in sorted(allowed):
            require(k[:2] in releases,'Allowed code has no release pin')
            rd=releases[k[:2]]['payload']
            if rd['complete']:require(k[2] in {c['code'] for c in rd['concepts']},'Allowed code absent from complete release')
        if d['strength']!='required':
            ready=False;add('BINDING-DIALECT','unsupported','Supply a required finite category-set profile or a separate evaluated adapter.',[s['id']])
        ancestry=[pin(s)]
        if d['parent'] is not None:
            parent=compile_profile(d['parent'],stack+(ref['id'],));pd=parent['data']
            same=all(d[k]==pd[k] for k in ('subjectClass','unit','slot','meaning','strength'))
            same_pins={digest(p) for p in d['releasePins']}=={digest(p) for p in pd['releasePins']}
            require(same and same_pins,'Profile changes identity/meaning/release; not a restriction')
            require(allowed<=parent['allowed'] and d['min']>=pd['min'] and d['max']<=pd['max'],'Profile widens constraints')
            ready=ready and parent['ready'];ancestry+=parent['ancestry']
            if allowed!=parent['allowed']:add('PROFILE-COVERAGE','notice','Which formerly classifiable subjects now lack a permitted category?',[s['id'],d['parent']['id']])
        result={'data':d,'allowed':allowed,'releases':releases,'ready':ready,'ancestry':ancestry}
        compiled[ref['id']]=result
        return result
    base=compile_profile(packet['baseProfile']);target=compile_profile(packet['profile'])
    if packet['mode']!='migration' and packet['mode']!='metamodel-migration':
        require(packet['baseProfile'] in target['ancestry'],'Selected profile is not a descendant of the base')
    require((packet['mode']=='profile')==(not packet['assignments']),'Assignment presence does not match mode')
    require(packet['mode'] in ('migration','metamodel-migration') or not packet['crosswalks'],'Crosswalks outside migration mode')
    require(len({p['id'] for p in packet['crosswalks']})==len(packet['crosswalks']),'Duplicate selected crosswalk')
    selected=[get(p,'assignment') for p in packet['assignments']]
    require(len({s['id'] for s in selected})==len(selected),'Duplicate selected assignment')
    results=[];alternatives=[];candidate=None;disposition='not-requested'
    for s in selected:
        a=s['payload'];require(a['profile']==packet['baseProfile'],'Assignment source profile not pinned as base')
        require(all(a[k]==base['data'][k] for k in ('subjectClass','unit','slot')),'Assignment subject/slot contract mismatch')
        successors=[x['id'] for x in snaps.values() if x['payload']['kind']=='assignment' and x['payload']['corrects']==pin(s)]
        if successors:add('SOURCE-REVISION-CONTEXT','notice','A captured correction exists; confirm the selected revision is intended for this historical review.',[s['id'],*successors])
        if a['state']=='proposed':add('PROPOSED-ASSIGNMENT','notice','Conformance checks this proposal only; who may authorize an operative assignment?',[s['id']])
    if len(selected)>1:
        add('ASSIGNMENT-SELECTION','insufficient-context','Which source revision/assignment is authoritative for this review?',[s['id'] for s in selected])
    for s in selected:
        a=s['payload']
        def validate_selection(p,at,new):
            if p['data']['strength']!='required':return 'unsupported'
            if not p['ready']:return 'insufficient-context'
            if not all(a[k]==p['data'][k] for k in ('subjectClass','unit','slot')):return 'does-not-conform'
            if a['state'] in ('disputed','withdrawn'):return 'insufficient-context'
            if not within(at,a['validFrom'],a['validUntil']):return 'outside-valid-time'
            if not p['data']['min']<=len(a['values'])<=p['data']['max']:return 'does-not-conform'
            if not set(map(key,a['values']))<=p['allowed']:return 'does-not-conform'
            for v in a['values']:
                rd=p['releases'][key(v)[:2]]['payload'];c=next(c for c in rd['concepts'] if c['code']==v['code'])
                if not within(at,c['validFrom'],c['validUntil']):return 'outside-valid-time'
                if new and (c['status']!='active' or not c['selectable']):return 'does-not-conform'
            return 'conforms'
        historic=validate_selection(base,packet['effectiveAt'],False)
        selected_result=validate_selection(target,packet['effectiveAt'],False) if packet['mode']=='assignment' else 'not-requested'
        results.append({'assignmentSnapshot':s['id'],'subjectId':a['subjectId'],'stateAsClaimed':a['state'],'sourceConformance':historic,'selectedConformance':selected_result})
        if historic!='conforms':add('SOURCE-ASSIGNMENT',historic,'Provide an applicable, conforming source assignment and its authority evidence.',[s['id']])
        if selected_result not in ('conforms','not-requested'):add('SELECTED-PROFILE',selected_result,'Which permitted category or profile revision addresses this subject?',[s['id']])
    if packet['mode']=='metamodel-migration':
        disposition='refuse-model-id-migration';add('MODEL-MIGRATION','unsupported','Compare complete model specifications and prepare an independently authorized installation/migration plan.')
    elif packet['inference']=='chain-requested':
        disposition='unsupported-chain';add('CHAIN-EXECUTION','unsupported','Supply reviewed direct correspondence evidence or a separately defined chain-evaluation policy; SKOS entailments are not denied.')
    elif packet['mode']=='migration':
        disposition='human-review-required'
        if len(selected)!=1 or len(selected[0]['payload']['values'])!=1:
            add('MIGRATION-INPUT','unsupported','Select one independently justified source assignment with one category for this bounded migration review.')
        else:
            a=selected[0]['payload'];source=key(a['values'][0]);complete=True;applicable=[]
            for ref in packet['crosswalks']:
                s=get(ref,'crosswalk');d=s['payload']
                ctx={'unit':a['unit'],'purpose':packet['purpose'],'jurisdiction':packet['jurisdiction']}
                if d['context']!=ctx:
                    add('MAPPING-CONTEXT','notice','This crosswalk belongs to a different declared context.',[s['id']]);continue
                if not d['complete']:complete=False
                for e in d['entries']:
                    if source not in set(map(key,e['sources'])):continue
                    live=within(packet['targetAt'],e['validFrom'],e['validUntil']) and e['state'] not in ('rejected','superseded')
                    ack=any((s['digest'],e['id'],e['approver'],ev) in approval_keys for ev in e['evidence'])
                    eligible=[]
                    for t in e['targets']:
                        tk=key(t);p=target['releases'].get(tk[:2]);reason='not-allowed'
                        if p and not p['payload']['complete']:reason='unknown-release-completeness'
                        elif tk in target['allowed'] and p:
                            c=next(c for c in p['payload']['concepts'] if c['code']==t['code'])
                            reason='eligible' if c['status']=='active' and c['selectable'] and within(packet['targetAt'],c['validFrom'],c['validUntil']) else 'inactive-or-not-selectable'
                        eligible.append({'code':t,'eligibility':reason})
                    alternatives.append({'crosswalkSnapshot':s['id'],'entryId':e['id'],'sources':e['sources'],'targets':eligible,'predicate':e['predicate'],'stateAsClaimed':e['state'],'hostApprovalAcknowledged':ack,'applicableAtTarget':live,'scoreAsClaimed':e['score'],'methodAsClaimed':e['method'],'lossNote':e['lossNote']})
                    if live:applicable.append((s,e,ack,eligible))
            if not complete:add('CROSSWALK-COMPLETE','insufficient-context','Who supplies complete correspondence evidence for this declared context?')
            distinct={key(t) for _,e,_,_ in applicable for t in e['targets']}
            single=[]
            for s,e,ack,eligible in applicable:
                if len(e['sources'])==len(e['targets'])==1 and e['predicate']=='exactMatch' and e['state']=='approved' and ack and eligible[0]['eligibility']=='eligible':single.append(e['targets'][0])
            safe=bool(applicable) and all(len(e['sources'])==len(e['targets'])==1 and e['predicate']=='exactMatch' and e['state']=='approved' and ack for _,e,ack,_ in applicable)
            identity_ok=all(a[k]==target['data'][k] for k in ('subjectClass','unit','slot')) and base['data']['meaning']==target['data']['meaning']
            if (complete and target['ready'] and base['ready'] and safe and len(distinct)==1 and single and identity_ok and target['data']['min']<=1<=target['data']['max'] and results[0]['sourceConformance']=='conforms' and a['state']=='asserted'):
                candidate=single[0];disposition='proposed-candidate'
            else:add('MIGRATION-REVIEW','human-review-required','Resolve source validity, context, alternatives, correspondence authority and target eligibility; no automatic assignment is permitted.')
    outcomes={f['outcome'] for f in findings}
    if 'insufficient-context' in outcomes:outcome='insufficient-context'
    elif 'unsupported' in outcomes:outcome='unsupported'
    elif outcomes & {'does-not-conform','outside-valid-time'}:outcome='does-not-conform'
    elif disposition=='human-review-required':outcome='human-review-required'
    elif disposition=='proposed-candidate':outcome='candidate-only'
    else:outcome='conforms-to-local-profile'
    basis=sorted(approvals,key=lambda x:encode(x))
    bid=build_id();pid=digest(packet)
    return {'format':'vercy-classification-assessment','version':VERSION,'assessmentId':digest({'packet':pid,'build':bid,'approvalBasis':basis}),'packetId':packet['id'],'packetDigest':pid,'buildId':bid,'owner':packet['owner'],'dimensionId':packet['dimensionId'],'purpose':packet['purpose'],'knowledgeAt':packet['knowledgeAt'],'effectiveAt':packet['effectiveAt'],'targetAt':packet['targetAt'],'outcome':outcome,'checks':findings,'assignments':results,'migrationDisposition':disposition,'candidate':candidate,'alternatives':alternatives,'approvalBasis':basis,'effects':[],'claims':'Bounded snapshot consistency only; no truth, full taxonomy, identity change, live assignment, permission grant or standards conformance.'}

def review(packet,host,actor,purpose,now):
    """Host authenticates actor/time and verifies grant origin before this call."""
    try:
        schema(host,'host');stamp(now);interval(host['validFrom'],host['validUntil'])
        if not isinstance(packet,dict):raise Denied('NOT AUTHORIZED')
        if not (host['actor']==actor and host['purpose']==purpose and within(now,host['validFrom'],host['validUntil']) and host['packetDigest']==digest(packet)):raise Denied('NOT AUTHORIZED')
        if not all(packet.get(k)==host[k] for k in ('dimensionId','owner','purpose')):raise Denied('NOT AUTHORIZED')
    except Invalid as exc:raise Denied('NOT AUTHORIZED') from exc
    schema(packet,'packet');require(packet['knowledgeAt']<=now,'Knowledge cut is in future')
    result=_assess(packet,host['approvals'])
    schema(result,'assessment')
    schema({'packet':packet,'assessment':result},'native')
    return result

def inspect_snapshot(value):
    """Replay historical consistency; not read authorization or approval verification."""
    schema(value,'native')
    assessment=value['assessment'];require(isinstance(assessment,dict) and isinstance(assessment.get('approvalBasis'),list),'Missing approval evidence')
    # Validate recorded basis against the host schema's approval shape without granting access.
    hs=json.loads((HERE/'classification.schema.json').read_text(encoding='utf-8'))['$defs']['host']['properties']['approvals']
    require(Draft202012Validator(hs).is_valid(assessment['approvalBasis']),'Invalid recorded approval basis')
    require(encode(_assess(value['packet'],assessment['approvalBasis']))==encode(assessment),'Assessment replay mismatch')
    return {'consistent':True,'authorized':False,'effects':[]}

def migrate_snapshot(value,target_version):
    inspect_snapshot(value)
    if target_version!=VERSION:raise Invalid('No lossless upgrade/downgrade adapter is published')
    return decode(encode(value))

def native_records(value,captured_at):
    """Host-authorized recording of a local Assessment; source subjects stay external."""
    inspect_snapshot(value);stamp(captured_at)
    a=value['assessment'];require(captured_at>=a['knowledgeAt'],'Capture precedes review knowledge cut')
    oid='urn:vercy:classification-assessment:'+a['assessmentId'].split(':')[1]
    provenance={'source':oid,'dimensionId':a['dimensionId']}
    obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':r1','objectId':oid,'objectType':MODEL+':assessment','name':'Classification assessment','recordedAt':captured_at,'previousRecordId':None,'state':'active','provenance':provenance,'accessClass':'restricted'}
    fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot','subjectId':oid,'path':'classification.assessment.snapshot','value':decode(encode(value)),'unit':None,'validFrom':captured_at,'validTo':None,'recordedAt':captured_at,'supersedes':[],'status':'asserted','provenance':{**provenance,'snapshotDigest':digest(value)},'authority':{'source':a['owner'],'rank':0},'masterSystem':oid,'accessClass':'restricted'}
    validate_native_fact(fact)
    return obj,fact

def validate_native_fact(fact):
    require(isinstance(fact,dict) and set(fact)=={'recordType','schemaVersion','factId','subjectId','path','value','unit','validFrom','validTo','recordedAt','supersedes','status','provenance','authority','masterSystem','accessClass'},'Invalid native fact envelope')
    inspect_snapshot(fact['value']);a=fact['value']['assessment']
    oid='urn:vercy:classification-assessment:'+a['assessmentId'].split(':')[1]
    require((fact['recordType'],fact['schemaVersion'],fact['path'])==('fact','1.0.0','classification.assessment.snapshot'),'Wrong native fact contract')
    require((fact['subjectId'],fact['factId'],fact['masterSystem'])==(oid,oid+':snapshot',oid),'Wrong native assessment identity')
    require(encode(fact['authority'])==encode({'source':a['owner'],'rank':0}) and fact['accessClass']=='restricted','Wrong native owner/class')
    require(fact['status']=='asserted' and fact['unit'] is None and fact['validTo'] is None and fact['supersedes']==[],'Unsupported native state')
    stamp(fact['recordedAt']);require(fact['validFrom']==fact['recordedAt'] and fact['recordedAt']>=a['knowledgeAt'],'Wrong native capture time')
    require(encode(fact['provenance'])==encode({'source':oid,'dimensionId':a['dimensionId'],'snapshotDigest':digest(fact['value'])}),'Wrong native provenance/digest')
    return {'valid':True,'scope':'restricted-local-assessment-snapshot','authorized':False}

if __name__=='__main__':
    import argparse,sys
    from datetime import timezone
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--packet',required=True);ap.add_argument('--host',required=True);ap.add_argument('--actor',required=True);ap.add_argument('--purpose',required=True);args=ap.parse_args()
    def read(path):
        with Path(path).open('rb') as f:return decode(f.read(2*LIMIT+1))
    try:
        result=review(read(args.packet),read(args.host),args.actor,args.purpose,datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
        print(encode(result).decode('utf-8'))
    except (Invalid,Denied,OSError) as exc:
        print(json.dumps({'status':'not-authorized' if isinstance(exc,Denied) else 'rejected-input','reason':str(exc) if not isinstance(exc,OSError) else 'Input file unavailable','effects':[]}),file=sys.stderr);sys.exit(2)
