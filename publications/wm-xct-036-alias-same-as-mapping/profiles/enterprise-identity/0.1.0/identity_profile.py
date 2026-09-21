"""Bounded, offline enterprise assertion profile. No endpoint writes or matching.

Policy, clock and input completeness are caller trust inputs. This reference
checks declared constraints; it does not authenticate users or evidence.
"""
import argparse,copy,datetime,hashlib,json,re
from pathlib import Path
from urllib.parse import urlsplit
from jsonschema import Draft202012Validator,FormatChecker

HERE=Path(__file__).resolve().parent
if not {'uri','date-time'} <= set(FormatChecker.checkers):
    raise RuntimeError('Install jsonschema[format-nongpl]: uri and date-time checkers required')
class Invalid(ValueError):pass
def require(condition,message):
    if not condition:raise Invalid(message)
def encode(value):
    try:return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
    except (ValueError,UnicodeError,TypeError) as e:raise Invalid('value cannot be canonically encoded') from e
def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
def load(path):
    def unique(pairs):
        value={}
        for key,item in pairs:
            require(key not in value,'duplicate JSON member: '+key);value[key]=item
        return value
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(Invalid('nonfinite JSON number')))
def stamp(value):
    require(isinstance(value,str) and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',value) is not None,'UTC second precision timestamp required')
    try:return datetime.datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
    except (ValueError,TypeError) as e:raise Invalid('UTC second precision timestamp required') from e
def schema(value,name):
    document=load(HERE/'identity-profile.schema.json')
    contract=document if name=='assertion.schema.json' else document['$defs'][name.split('.')[0]]
    errors=sorted(Draft202012Validator(contract,format_checker=FormatChecker()).iter_errors(value),key=lambda e:str(e.path))
    require(not errors,'SCHEMA: '+('; '.join(e.message for e in errors[:3])))
def interval(start,end):require(end is None or stamp(start)<stamp(end),'empty or reversed interval')
def inside(time,start,end):return stamp(start)<=stamp(time) and (end is None or stamp(time)<stamp(end))
def key(binding):return tuple(binding[k] for k in ['scheme','schemeVersion','issuer','scope','value'])
def local_reference(value):
    # Restrictive comparison profile: never normalize an identifier silently.
    parts=urlsplit(value)
    require(parts.scheme in {'urn','https'},'local subject URI must be urn or https')
    require(not any(x in value for x in ['%','\\','?','#']),'noncanonical local subject URI')
    require(not any(x in {'.','..'} for x in parts.path.split('/')),'dot segment in local subject URI')
    require(parts.scheme!='https' or (parts.netloc and '@' not in parts.netloc),'invalid local subject authority')

def validate_policy(policy):
    schema(policy,'policy.schema.json');interval(policy['validFrom'],policy['validTo'])
    actors={item['actor']:item['states'] for item in policy['actors']}
    require(len(actors)==len(policy['actors']),'duplicate policy actor')
    local_reference(policy['subjectPrefix'])
    registers=set()
    for item in policy['schemeKinds']:
        k=tuple(item[x] for x in ['scheme','schemeVersion','issuer','scope'])
        require(k not in registers,'duplicate scheme registration');registers.add(k)
        require(item['issuer'] in policy['issuers'],'registered scheme issuer is not trusted')
    kinds=set();prefixes=[]
    for item in policy['subjectNamespaces']:
        local_reference(item['prefix'])
        require(item['kind'] not in kinds,'duplicate subject kind namespace');kinds.add(item['kind'])
        require(item['prefix'].startswith(policy['subjectPrefix']),'kind namespace outside local namespace')
        require(not any(item['prefix'].startswith(x) or x.startswith(item['prefix']) for x in prefixes),'overlapping kind namespaces')
        prefixes.append(item['prefix'])
    return actors

def claim_digest(assertion):return digest({k:v for k,v in assertion.items() if k!='history'})

def validate(assertion,policy):
    actors=validate_policy(policy);schema(assertion,'assertion.schema.json')
    encode(assertion)
    require(assertion['policyDigest']==digest(policy),'policy canonical JSON digest mismatch')
    require(assertion['dimension']==policy['dimension'] and assertion['purpose']==policy['purpose'],'wrong Dimension or purpose')
    b=assertion['binding'];target=assertion['target']
    require(b['personalDataClass'] in policy['dataClasses'],'data classification outside supplied policy')
    require(b['issuer'] in policy['issuers'],'untrusted identifier issuer')
    registrations=[x for x in policy['schemeKinds'] if all(x[k]==b[k] for k in ['scheme','schemeVersion','issuer','scope'])]
    require(len(registrations)==1 and registrations[0]['kind']==b['kind'],'binding kind does not match trusted scheme registration')
    local_reference(target['id'])
    namespaces=[x for x in policy['subjectNamespaces'] if x['kind']==target['kind']]
    require(len(namespaces)==1 and target['id'].startswith(namespaces[0]['prefix']) and len(target['id'])>len(namespaces[0]['prefix']),'target kind does not match local namespace')
    require(b['kind']==target['kind'],'different referent kinds: account ownership is not identity')
    require(target['id'].startswith(policy['subjectPrefix']),'subject outside local namespace')
    require(b['sourceReferentRef']!=target['id'],'source and target must remain distinct references in this profile')
    require(assertion['relation'] in policy['relations'],'relation outside supplied policy')
    interval(b['validFrom'],b['validTo']);interval(assertion['validFrom'],assertion['validTo'])
    require(inside(assertion['validFrom'],b['validFrom'],b['validTo']),'assertion starts outside assignment')
    if b['validTo'] is not None:require(assertion['validTo'] is not None and stamp(assertion['validTo'])<=stamp(b['validTo']),'assertion exceeds assignment')
    require(stamp(b['recordedAt'])>=stamp(b['validFrom']),'binding observed before assignment began')
    previous=None;ids=set()
    transitions={None:{'proposed'},'proposed':{'asserted','disputed','retracted'},'asserted':{'disputed','retracted'},'disputed':{'asserted','retracted'},'retracted':set()}
    for event in assertion['history']:
        require(event['id'] not in ids,'duplicate event identity');ids.add(event['id'])
        require(event['previousDigest']==(digest(previous) if previous else claim_digest(assertion)),'event predecessor mismatch')
        require(event['state'] in transitions[previous['state'] if previous else None],'invalid lifecycle transition')
        require(previous is None or stamp(event['recordedAt'])>stamp(previous['recordedAt']),'recorded time must strictly increase')
        require(stamp(event['recordedAt'])>=stamp(b['recordedAt']),'claim predates binding evidence')
        require(stamp(assertion['validFrom'])<=stamp(event['effectiveAt'])<=stamp(event['recordedAt']),'event time outside admissible past')
        require(inside(event['effectiveAt'],assertion['validFrom'],assertion['validTo']),'event takes effect outside assertion validity')
        require(inside(event['recordedAt'],policy['validFrom'],policy['validTo']),'authority inactive when event recorded')
        require(event['actor'] in actors and event['state'] in actors[event['actor']],'actor cannot issue this state')
        kinds={x['kind'] for x in event['evidence']}
        if event['state']=='asserted':
            require(all(x=='resolved' for x in assertion['endpointResolution'].values()),'activation requires resolved endpoint declarations')
            require(assertion['relation']!='probable-entity-match','candidate relation cannot activate')
            require({'source-record','review-decision'}<=kinds,'activation requires source evidence and review evidence')
            require(any(x['kind']=='source-record' and x['ref']==b['sourceRecord'] for x in event['evidence']),'source evidence does not match binding source record')
        previous=event
    return assertion
def validate_set(assertions,policy):
    validate_policy(policy)
    require(isinstance(assertions,list),'assertions must be a list')
    ids={};bindings={};event_ids=set()
    for a in assertions:
        validate(a,policy)
        require(a['id'] not in ids,'duplicate assertion ID in input; use import_assertion for replay')
        ids[a['id']]=a
        bid=(a['binding']['issuer'],a['binding']['assignmentId']);content=digest(a['binding'])
        # Proposals cannot reserve a source occurrence; a retained retraction
        # does not permanently prevent corrected source evidence.
        reserves=a['history'][-1]['state']!='retracted' and any(e['state']=='asserted' for e in a['history'])
        if reserves:
            require(bid not in bindings or bindings[bid]==content,'active asserted assignment has different binding content')
            bindings[bid]=content
        for event in a['history']:
            require(event['id'] not in event_ids,'event ID reused across assertions');event_ids.add(event['id'])
    return assertions
def import_assertion(existing,incoming,policy,*,now):
    """Pure import, with no filesystem writes. Caller commits under its own lock."""
    validate_set(existing,policy);validate(incoming,policy);stamp(now)
    require(inside(now,policy['validFrom'],policy['validTo']),'import clock outside policy validity')
    def check_receipt(new_events):
        require(all(e['recordedAt']==now for e in new_events),'new events must use trusted receipt time')
        head=max((stamp(e['recordedAt']) for a in existing for e in a['history']),default=None)
        require(head is None or stamp(now)>head,'receipt time must exceed input import head')
    for old in existing:
        if old['id']!=incoming['id']:continue
        if old==incoming:return copy.deepcopy(existing)
        old_base={k:v for k,v in old.items() if k!='history'};new_base={k:v for k,v in incoming.items() if k!='history'}
        require(old_base==new_base,'claim-bearing content changed; retract and use a new assertion ID')
        require(len(incoming['history'])>len(old['history']) and incoming['history'][:len(old['history'])]==old['history'],'history is not an append-only extension')
        check_receipt(incoming['history'][len(old['history']):])
        result=[copy.deepcopy(incoming if x['id']==old['id'] else x) for x in existing]
        validate_set(result,policy);return result
    check_receipt(incoming['history'])
    result=copy.deepcopy(existing+[incoming]);validate_set(result,policy);return result
def resolve(assertions,query_binding,policy,*,valid_at,known_at,evaluation_at,reader,purpose):
    """A view of the supplied complete-for-caller input only, never global truth."""
    validate_policy(policy);schema(query_binding,'query.schema.json')
    require(reader in policy['readers'] and purpose==policy['purpose'],'read purpose/actor denied by supplied policy')
    require(inside(evaluation_at,policy['validFrom'],policy['validTo']),'current policy is inactive')
    require(stamp(known_at)<=stamp(evaluation_at),'knowledge time exceeds evaluation time')
    stamp(valid_at);validate_set(assertions,policy)
    positives={};negative={};candidates=[];disputed=[];excluded=[];negative_proposals=[];candidate_disputes=[]
    for a in assertions:
        if key(a['binding'])!=key(query_binding):continue
        history=[e for e in a['history'] if stamp(e['recordedAt'])<=stamp(known_at) and stamp(e['effectiveAt'])<=stamp(valid_at)]
        if not history:excluded.append({'id':a['id'],'reason':'not-effective-or-known'});continue
        e=history[-1]
        if not inside(valid_at,a['validFrom'],a['validTo']) or not inside(valid_at,a['binding']['validFrom'],a['binding']['validTo']):excluded.append({'id':a['id'],'reason':'outside-validity'});continue
        if e['state']=='retracted':excluded.append({'id':a['id'],'reason':'retracted'});continue
        if e['state']=='disputed':
            prior=history[:-1]
            if any(x['state']=='asserted' for x in prior):disputed.append(a['id'])
            elif a['relation']=='not-same-assertion':negative_proposals.append(a['id'])
            else:candidate_disputes.append(a['id'])
            continue
        if e['state']=='proposed':
            (negative_proposals if a['relation']=='not-same-assertion' else candidates).append(a['id']);continue
        target=a['target']['id']
        bucket=negative if a['relation']=='not-same-assertion' else positives
        bucket.setdefault(target,[]).append(a['id'])
    contested=bool(disputed or len(positives)>1 or set(positives)&set(negative))
    status='contested' if contested else 'accepted-in-input' if positives else 'denied-in-input' if negative else 'candidate' if candidates or candidate_disputes else 'proposal-only' if negative_proposals else 'unknown'
    observations={}
    for a in assertions:
        bid=(a['binding']['issuer'],a['binding']['assignmentId'])
        observations.setdefault(bid,{}).setdefault(digest(a['binding']),[]).append(a['id'])
    binding_conflicts=[{'issuer':bid[0],'assignmentId':bid[1],'assertions':sorted(x for ids in values.values() for x in ids)} for bid,values in sorted(observations.items()) if len(values)>1]
    return {'retainedObservationConflicts':binding_conflicts,'status':status,'targets':sorted(positives),'supporting':sorted(x for v in positives.values() for x in v),'opposing':sorted(x for v in negative.values() for x in v),'disputed':sorted(disputed),'candidates':sorted(candidates),'excluded':sorted(excluded,key=lambda x:x['id']),'candidateDisputes':sorted(candidate_disputes),'negativeProposals':sorted(negative_proposals),'validAt':valid_at,'knownAt':known_at,'evaluationAt':evaluation_at,'reader':reader,'purpose':purpose,'targetKinds':sorted({a['target']['kind'] for a in assertions if a['target']['id'] in positives}),'inputDigest':digest(sorted(assertions,key=lambda x:x['id'])),'policyDigest':digest(policy),'scope':'supplied-input-only','grantsAccess':False,'globalEquality':False}
def main():
    p=argparse.ArgumentParser();p.add_argument('assertions');p.add_argument('--policy',required=True);a=p.parse_args()
    values=load(a.assertions);validate_set(values,load(a.policy));print(json.dumps({'valid':True,'assertions':len(values),'scope':'declared constraints only; caller authenticates policy and evidence'}))
if __name__=='__main__':main()
