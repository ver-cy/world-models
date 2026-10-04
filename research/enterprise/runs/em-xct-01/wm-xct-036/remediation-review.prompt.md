# EM-XCT-01 remediation review — second frozen candidate

Reply in English. No tools, execution, browsing, delegation or publication. This is a materially changed candidate following Claude BLOCK (F1 receipt-time import, F2 native claim overstatement, F3 empty policy, plus F4-F18) and Grok ACCEPT WITH LIMITS (BUG1-8). Review the supplied bytes and return BLOCK or ACCEPT WITH LIMITS, with remaining executable counterexamples. You do not grant publication authority. Do not claim you ran tests or verified upstream sources.

Changes: required trusted now on live import, all new events equal receipt time and after the global input head; exact replay remains no-op. Historical snapshot restore is separate and cannot use live import. Unconditional policy checks; scheme/version/issuer/scope-to-kind register and disjoint target-kind namespaces; restricted URN/HTTPS targets reject escapes/dot segments/empty suffix. Genesis hash commits fixed claim, later events link prior event. Assignment identity qualified by issuer. Candidate disputes cannot veto an accepted claim; proposed negatives separate, reviewed negatives denied-in-input. Effective time must be within claim validity. ASCII timestamps, encoder surrogate failure converted to Invalid, required format checkers, data-class policy and pre-validation reader gate. Source referent distinct from token, explicit endpoint resolution declarations. Combined schema is the actual contract; canonical JSON digest versus raw file hashes documented. Caller evidence/authentication remains external. No four-eyes or cryptographic attestation claims.

Grok's overlap objection is deliberately scoped: this stores potentially conflicting assertions, not authoritative assignment allocation. Overlapping different occurrences/targets are admitted as evidence and contested by query. Duplicate semantics under distinct assertion IDs remain independent claims. Scheme-version changes require a policy registration; cross-scheme alias resolution is deferred. Backdated effective retraction intentionally supersedes earlier activation from its effective date once recorded. These are explicit semantics, not hidden bugs.

Native note: checked actual V3 fact.schema.json; authority requires source AND integer rank, so simply removing rank would make the outer record invalid. Harness uses 0 only as outer snapshot metadata; identity resolver never consumes it. Outer asserted means 'this snapshot was recorded', never positive identity. Outer validity starts at snapshot receipt. Companion invocation is explicit; raw V3 does not enforce it, and existing-Dimension transactional updates are out of scope. Acceptance now checks stored==fixtures and installed schema+validator digests, pins skill/upstream files, and reports digests. Original 036 and 011 semantics/holds are unchanged. Crosswalk explicitly claims narrower usage/overlap, NOT full parent conformance or a ratified relation register. Thus EM-XCT-01 stays partial.

Scope of this input: complete revised evaluator, combined schema, tests, acceptance harness, README, model-spec, crosswalk; compact policy/startup fixture and current reports. Original broad source documents, tool source implementations, group/AI fixture bodies and other profile support files are NOT included in this second review. The original audits are retained, not replaced. 78 tests and three temporary native scenarios passed locally; reports are evidence claims, not your independently executed verification.

## FILE identity_profile.py
```
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
        require(bid not in bindings or bindings[bid]==content,'assignment ID reused for different binding content')
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
            prior=a['history'][:a['history'].index(e)]
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
    return {'status':status,'targets':sorted(positives),'supporting':sorted(x for v in positives.values() for x in v),'opposing':sorted(x for v in negative.values() for x in v),'disputed':sorted(disputed),'candidates':sorted(candidates),'excluded':sorted(excluded,key=lambda x:x['id']),'candidateDisputes':sorted(candidate_disputes),'negativeProposals':sorted(negative_proposals),'validAt':valid_at,'knownAt':known_at,'evaluationAt':evaluation_at,'reader':reader,'purpose':purpose,'targetKinds':sorted({a['target']['kind'] for a in assertions if a['target']['id'] in positives}),'inputDigest':digest(sorted(assertions,key=lambda x:x['id'])),'policyDigest':digest(policy),'scope':'supplied-input-only','grantsAccess':False,'globalEquality':False}
def main():
    p=argparse.ArgumentParser();p.add_argument('assertions');p.add_argument('--policy',required=True);a=p.parse_args()
    values=load(a.assertions);validate_set(values,load(a.policy));print(json.dumps({'valid':True,'assertions':len(values),'scope':'declared constraints only; caller authenticates policy and evidence'}))
if __name__=='__main__':main()

```

## FILE identity-profile.schema.json
```
{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"https://ver.cy/models/wm-xct-036-alias-same-as-mapping/profiles/enterprise-identity/0.1.0/identity-profile.schema.json","type":"object","additionalProperties":false,"properties":{"format":{"const":"vercy-enterprise-identity-assertion"},"version":{"const":"0.1.0"},"id":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"dimension":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"purpose":{"type":"string","minLength":1,"maxLength":1024},"policyDigest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},"binding":{"type":"object","additionalProperties":false,"properties":{"assignmentId":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"scheme":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"schemeVersion":{"type":"string","minLength":1,"maxLength":1024},"issuer":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"scope":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"value":{"type":"string","minLength":1,"maxLength":1024},"comparison":{"const":"exact-string"},"kind":{"enum":["person","organization","user-account","service-account"]},"validFrom":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"validTo":{"anyOf":[{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},{"type":"null"}]},"recordedAt":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"sourceRecord":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"sourceReferentRef":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"personalDataClass":{"enum":["synthetic","restricted"]},"credentialProhibition":{"const":true}},"required":["assignmentId","scheme","schemeVersion","issuer","scope","value","comparison","kind","validFrom","validTo","recordedAt","sourceRecord","sourceReferentRef","personalDataClass","credentialProhibition"]},"target":{"type":"object","additionalProperties":false,"properties":{"id":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"kind":{"enum":["person","organization","user-account","service-account"]}},"required":["id","kind"]},"relation":{"enum":["equivalent-in-context","not-same-assertion","probable-entity-match"]},"endpointResolution":{"type":"object","additionalProperties":false,"properties":{"source":{"enum":["resolved","unresolved","ambiguous"]},"target":{"enum":["resolved","unresolved","ambiguous"]}},"required":["source","target"]},"validFrom":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"validTo":{"anyOf":[{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},{"type":"null"}]},"inferencePermitted":{"const":false},"history":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"id":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"previousDigest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},"recordedAt":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"effectiveAt":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"actor":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"state":{"enum":["proposed","asserted","disputed","retracted"]},"reason":{"type":"string","minLength":1,"maxLength":1024},"evidence":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"ref":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"kind":{"enum":["source-record","review-decision","name-match","email-match","git-author","legacy-import"]},"description":{"type":"string","minLength":1,"maxLength":1024}},"required":["ref","kind","description"]},"minItems":1}},"required":["id","previousDigest","recordedAt","effectiveAt","actor","state","reason","evidence"]},"minItems":1}},"required":["format","version","id","dimension","purpose","policyDigest","binding","target","relation","endpointResolution","validFrom","validTo","inferencePermitted","history"],"$defs":{"policy":{"type":"object","additionalProperties":false,"properties":{"format":{"const":"vercy-identity-reference-policy"},"version":{"const":"0.1.0"},"id":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"dimension":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"purpose":{"type":"string","minLength":1,"maxLength":1024},"subjectPrefix":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-z][a-z0-9+.-]*:.+[:/]$"},"validFrom":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"validTo":{"anyOf":[{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},{"type":"null"}]},"issuers":{"type":"array","items":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"minItems":1,"uniqueItems":true},"relations":{"type":"array","items":{"enum":["equivalent-in-context","not-same-assertion","probable-entity-match"]},"minItems":1,"uniqueItems":true},"actors":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"actor":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"states":{"type":"array","items":{"enum":["proposed","asserted","disputed","retracted"]},"minItems":1,"uniqueItems":true}},"required":["actor","states"]},"minItems":1},"readers":{"type":"array","items":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"minItems":1,"uniqueItems":true},"schemeKinds":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"scheme":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"schemeVersion":{"type":"string","minLength":1,"maxLength":1024},"issuer":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"scope":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"kind":{"enum":["person","organization","user-account","service-account"]}},"required":["scheme","schemeVersion","issuer","scope","kind"]},"minItems":1},"subjectNamespaces":{"type":"array","items":{"type":"object","additionalProperties":false,"properties":{"kind":{"enum":["person","organization","user-account","service-account"]},"prefix":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-z][a-z0-9+.-]*:.+[:/]$"}},"required":["kind","prefix"]},"minItems":1},"dataClasses":{"type":"array","items":{"enum":["synthetic","restricted"]},"minItems":1,"uniqueItems":true}},"required":["format","version","id","dimension","purpose","subjectPrefix","validFrom","validTo","issuers","relations","actors","readers","dataClasses","schemeKinds","subjectNamespaces"]},"query":{"type":"object","additionalProperties":false,"properties":{"scheme":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"schemeVersion":{"type":"string","minLength":1,"maxLength":1024},"issuer":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"scope":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"value":{"type":"string","minLength":1,"maxLength":1024}},"required":["scheme","schemeVersion","issuer","scope","value"]},"binding":{"type":"object","additionalProperties":false,"properties":{"assignmentId":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"scheme":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"schemeVersion":{"type":"string","minLength":1,"maxLength":1024},"issuer":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"scope":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"value":{"type":"string","minLength":1,"maxLength":1024},"comparison":{"const":"exact-string"},"kind":{"enum":["person","organization","user-account","service-account"]},"validFrom":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"validTo":{"anyOf":[{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},{"type":"null"}]},"recordedAt":{"type":"string","format":"date-time","pattern":"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"sourceRecord":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"sourceReferentRef":{"type":"string","minLength":1,"maxLength":1024,"format":"uri","pattern":"^[a-zA-Z][a-zA-Z0-9+.-]*:"},"personalDataClass":{"enum":["synthetic","restricted"]},"credentialProhibition":{"const":true}},"required":["assignmentId","scheme","schemeVersion","issuer","scope","value","comparison","kind","validFrom","validTo","recordedAt","sourceRecord","sourceReferentRef","personalDataClass","credentialProhibition"]}}}
```

## FILE test_identity.py
```
import copy,datetime,json,unittest
from pathlib import Path
import identity_profile as p
HERE=Path(__file__).resolve().parent
class IdentityTests(unittest.TestCase):
 def setUp(self):
  self.policy=p.load(HERE/'examples/policy.json');self.rows=p.load(HERE/'examples/startup.json');self.a=copy.deepcopy(self.rows[0])
 def query(self,rows=None,**kw):
  defaults={'valid_at':'2026-01-01T00:00:00Z','known_at':'2026-01-01T00:00:00Z','evaluation_at':'2026-09-21T00:00:00Z','reader':'urn:synthetic:actor:steward','purpose':self.policy['purpose']};defaults.update(kw)
  return p.resolve(rows if rows is not None else self.rows,{k:self.a['binding'][k] for k in ['scheme','schemeVersion','issuer','scope','value']},self.policy,**defaults)
 def append(self,a,state='retracted',recorded='2025-08-01T00:00:00Z',effective='2025-02-01T00:00:00Z'):
  e=copy.deepcopy(a['history'][-1]);e.update(id=e['id']+':next',previousDigest=p.digest(a['history'][-1]),state=state,recordedAt=recorded,effectiveAt=effective);a['history'].append(e);return a
 def invalid(self,a):
  with self.assertRaises(p.Invalid):p.validate(a,self.policy)
 def seal(self,a):
  previous=None
  for e in a['history']:
   e['previousDigest']=p.digest(previous) if previous else p.claim_digest(a);previous=e
  return a
 def other(self):
  b=copy.deepcopy(self.a);b['id']+=':other'
  for e in b['history']:e['id']+=':other'
  return self.seal(b)
 def test_three_profiles(self):
  for n in ['startup','group','ai-team']:p.validate_set(p.load(HERE/('examples/'+n+'.json')),self.policy)
 def test_three_person_references_one_subject(self):
  for a in self.rows:
   self.a=a;r=self.query();self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['targets'],['urn:synthetic:subject:person:p1']);self.assertFalse(r['grantsAccess'])
 def test_equal_authority_conflict(self):
  b=self.other();b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['status'],'contested')
 def test_negative_conflict(self):
  b=self.other();b['relation']='not-same-assertion';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['status'],'contested')
 def test_negative_only_not_silently_absent(self):
  self.a['relation']='not-same-assertion';r=self.query([self.seal(self.a)]);self.assertEqual(r['status'],'denied-in-input');self.assertEqual(r['opposing'],[self.a['id']])
 def test_candidate_inert(self):
  self.a['relation']='probable-entity-match';self.a['history']=self.a['history'][:1];self.assertEqual(self.query([self.seal(self.a)])['status'],'candidate')
 def test_candidate_cannot_activate(self):self.a['relation']='probable-entity-match';self.invalid(self.a)
 def test_email_evidence_not_sufficient(self):
  self.a['history'][1]['evidence']=[{'ref':'urn:synthetic:email','kind':'email-match','description':'Same mailbox'}];self.invalid(self.a)
 def test_unknown_no_claim(self):self.assertEqual(self.query([])['status'],'unknown')
 def test_account_person_refused(self):self.a['binding']['kind']='user-account';self.invalid(self.a)
 def test_service_account_person_refused(self):self.a['binding']['kind']='service-account';self.invalid(self.a)
 def test_retract_history(self):
  later=self.append(copy.deepcopy(self.a));self.assertEqual(self.query([later])['status'],'unknown');self.assertEqual(self.query([later],known_at='2025-06-01T00:00:00Z')['status'],'accepted-in-input')
 def test_bitemporal_effective_date(self):
  later=self.append(copy.deepcopy(self.a));self.assertEqual(self.query([later],valid_at='2025-01-15T00:00:00Z')['status'],'accepted-in-input')
 def test_history_preserved_after_append(self):
  old=self.query([self.a],known_at='2025-06-01T00:00:00Z');new=self.query([self.append(copy.deepcopy(self.a))],known_at='2025-06-01T00:00:00Z')
  for k in ['status','targets','supporting','opposing','excluded']:self.assertEqual(old[k],new[k])
 def test_retracted_terminal(self):self.append(self.a);self.append(self.a,'asserted','2025-09-01T00:00:00Z');self.invalid(self.a)
 def test_disputed_blocks_resolution(self):self.append(self.a,'disputed');self.assertEqual(self.query([self.a])['status'],'contested')
 def test_predecessor_tamper(self):self.a['history'][1]['previousDigest']='sha256:'+'0'*64;self.invalid(self.a)
 def test_event_order(self):self.a['history'][1]['recordedAt']=self.a['history'][0]['recordedAt'];self.invalid(self.a)
 def test_actor_cannot_assert(self):self.a['history'][1]['actor']='urn:synthetic:actor:importer';self.invalid(self.a)
 def test_expired_authority(self):self.a['history'][1]['recordedAt']='2028-01-01T00:00:00Z';self.invalid(self.a)
 def test_policy_tamper(self):self.policy['purpose']='different';self.invalid(self.a)
 def test_wrong_dimension(self):self.a['dimension']='urn:other:dimension';self.invalid(self.a)
 def test_cross_dimension_target(self):self.a['target']['id']='urn:other:subject:p1';self.invalid(self.a)
 def test_issuer_scope_isolation(self):
  b=self.other();b['binding']['assignmentId']+=':other';b['binding']['scope']='urn:synthetic:tenant:other';b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['targets'],[self.a['target']['id']])
 def test_reassignment_temporal(self):
  rows=p.load(HERE/'examples/group.json');self.a=rows[0];self.assertEqual(self.query(rows,valid_at='2025-03-01T00:00:00Z')['targets'],['urn:synthetic:subject:person:pa']);self.assertEqual(self.query(rows,valid_at='2025-10-01T00:00:00Z')['targets'],['urn:synthetic:subject:person:pc'])
 def test_overlapping_reassignments_contested(self):
  b=self.other();b['binding']['assignmentId']+=':new';b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['status'],'contested')
 def test_qualified_assignment_not_overwritten(self):
  b=self.other();b['binding']['value']='different'
  with self.assertRaises(p.Invalid):p.validate_set([self.a,b],self.policy)
 def test_missing_qualification(self):del self.a['binding']['issuer'];self.invalid(self.a)
 def test_normalization_refused(self):self.a['binding']['comparison']='lowercase';self.invalid(self.a)
 def test_value_case_preserved(self):
  b=self.other();b['binding']['assignmentId']+=':new';b['binding']['value']='e7';b['target']['id']='urn:synthetic:subject:person:p2';self.assertEqual(self.query([self.seal(self.a),self.seal(b)])['targets'],[self.a['target']['id']])
 def test_same_as_refused(self):self.a['relation']='owl:sameAs';self.invalid(self.a)
 def test_closure_refused(self):self.a['inferencePermitted']=True;self.invalid(self.a)
 def test_unknown_time_not_epoch(self):self.a['binding']['validFrom']=None;self.invalid(self.a)
 def test_interval_bounds(self):self.a['validTo']=self.a['validFrom'];self.invalid(self.a)
 def test_assignment_bounds(self):self.a['binding']['validTo']='2025-02-01T00:00:00Z';self.invalid(self.a)
 def test_read_denied(self):
  with self.assertRaises(p.Invalid):self.query(reader='urn:synthetic:actor:intruder')
 def test_current_authority_expiry(self):
  with self.assertRaises(p.Invalid):self.query(evaluation_at='2028-01-01T00:00:00Z')
 def test_future_knowledge_refused(self):
  with self.assertRaises(p.Invalid):self.query(known_at='2027-01-01T00:00:00Z')
 def test_replay_noop(self):self.assertEqual(p.import_assertion(self.rows,self.a,self.policy,now='2026-09-21T00:00:00Z'),self.rows)
 def test_history_extension(self):
  new=self.append(copy.deepcopy(self.a));out=p.import_assertion(self.rows,new,self.policy,now=new['history'][-1]['recordedAt']);self.assertEqual(out[0],new);self.assertEqual(len(self.rows[0]['history']),2)
 def test_history_truncation_refused(self):
  a=copy.deepcopy(self.a);a['history']=a['history'][:1]
  with self.assertRaises(p.Invalid):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_endpoint_change_refused(self):
  b=self.append(copy.deepcopy(self.a));b['target']['id']='urn:synthetic:subject:person:p2'
  with self.assertRaises(p.Invalid):p.import_assertion(self.rows,b,self.policy,now='2026-09-21T00:00:00Z')
 def test_round_trip(self):self.assertEqual(json.loads(p.encode(self.rows)),self.rows)
 def test_lossy_round_trip_refused(self):del self.a['binding']['sourceRecord'];self.invalid(self.a)
 def test_unknown_version_refused(self):self.a['version']='9';self.invalid(self.a)
 def test_undeclared_field_refused(self):self.a['resolutionStatus']='accepted';self.invalid(self.a)
 def test_policy_no_self_grant(self):self.a['policy']={'allow':True};self.invalid(self.a)
 def test_duplicate_event_id_refused(self):
  b=self.other();b['history'][0]['id']=self.a['history'][0]['id'];b['history'][1]['previousDigest']=p.digest(b['history'][0])
  with self.assertRaises(p.Invalid):p.validate_set([self.a,b],self.policy)


 def test_empty_set_invalid_policy(self):
  self.policy['readers']='urn:synthetic:actor:steward'
  with self.assertRaises(p.Invalid):self.query([])
 def test_empty_set_duplicate_actor(self):
  self.policy['actors'].append(copy.deepcopy(self.policy['actors'][0]))
  with self.assertRaises(p.Invalid):p.validate_set([],self.policy)
 def test_retagging_both_kinds_refused(self):
  self.a['binding']['kind']=self.a['target']['kind']='service-account';self.a['target']['id']='urn:synthetic:subject:service-account:bot';self.invalid(self.a)
 def test_unregistered_scheme_version_refused(self):self.a['binding']['schemeVersion']='2';self.invalid(self.a)
 def test_target_kind_namespace_refused(self):self.a['target']['id']='urn:synthetic:subject:service-account:bot';self.invalid(self.a)
 def test_dot_segment_refused(self):self.a['target']['id']='urn:synthetic:subject:person:a/../b';self.invalid(self.a)
 def test_percent_encoded_namespace_refused(self):self.a['target']['id']='urn:synthetic:subject:person:%2e%2e/other';self.invalid(self.a)
 def test_prefix_near_miss_refused(self):self.a['target']['id']='urn:synthetic:subject:personality:p1';self.invalid(self.a)
 def test_effective_after_window_refused(self):
  self.a['validTo']='2025-07-01T00:00:00Z';self.append(self.a,effective='2025-08-01T00:00:00Z');self.invalid(self.a)
 def test_effective_at_exclusive_end_refused(self):
  self.a['validTo']='2025-08-01T00:00:00Z';self.append(self.a,effective='2025-08-01T00:00:00Z');self.invalid(self.a)
 def test_not_yet_known_has_reason(self):
  r=self.query([self.a],known_at='2024-01-01T00:00:00Z');self.assertEqual(r['status'],'unknown');self.assertEqual(r['excluded'][0]['reason'],'not-effective-or-known')
 def test_positive_with_different_negative(self):
  b=self.other();b['target']['id']='urn:synthetic:subject:person:p2';b['relation']='not-same-assertion';r=self.query([self.seal(self.a),self.seal(b)]);self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['opposing'],[b['id']])
 def test_independent_identical_claims_retained(self):
  b=self.other();r=self.query([self.seal(self.a),self.seal(b)]);self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(len(r['supporting']),2)
 def test_source_evidence_matches_assignment(self):
  self.a['history'][1]['evidence'][0]['ref']='urn:synthetic:wrong-source';self.invalid(self.a)
 def test_backdated_correction_supersedes_later_effect(self):
  self.a['history'][1]['effectiveAt']='2025-06-01T00:00:00Z';self.a['history'][1]['recordedAt']='2025-06-02T00:00:00Z'
  corrected=self.append(copy.deepcopy(self.a),effective='2025-01-01T00:00:00Z')
  self.assertEqual(self.query([corrected],valid_at='2025-06-15T00:00:00Z')['status'],'unknown')
  self.assertEqual(self.query([corrected],valid_at='2025-06-15T00:00:00Z',known_at='2025-06-15T00:00:00Z')['status'],'accepted-in-input')


 def test_backdated_import_refused(self):
  a=self.append(copy.deepcopy(self.a),recorded='2025-01-02T00:00:00Z',effective='2025-01-01T00:00:00Z')
  with self.assertRaisesRegex(p.Invalid,'trusted receipt'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_future_import_refused(self):
  a=self.append(copy.deepcopy(self.a),'disputed',recorded='2026-12-01T00:00:00Z',effective='2026-12-01T00:00:00Z')
  with self.assertRaisesRegex(p.Invalid,'trusted receipt'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_new_claim_backdating_refused(self):
  a=self.other();a['history']=a['history'][:1]
  with self.assertRaisesRegex(p.Invalid,'trusted receipt'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_live_proposal_import(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0]['recordedAt']='2026-09-21T00:00:00Z'
  self.assertEqual(len(p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')),4)
 def test_receipt_must_exceed_global_head(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0]['recordedAt']=self.rows[0]['history'][-1]['recordedAt']
  with self.assertRaisesRegex(p.Invalid,'import head'):p.import_assertion(self.rows,a,self.policy,now=a['history'][0]['recordedAt'])
 def test_disputed_candidate_cannot_veto(self):
  b=self.other();b['relation']='probable-entity-match';b['history']=b['history'][:1];self.seal(b);self.append(b,'disputed')
  r=self.query([self.a,b]);self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['candidateDisputes'],[b['id']])
 def test_proposed_negative_is_not_positive_candidate(self):
  b=self.other();b['relation']='not-same-assertion';b['history']=b['history'][:1];self.seal(b)
  r=self.query([b]);self.assertEqual(r['status'],'proposal-only');self.assertEqual(r['candidates'],[]);self.assertEqual(r['negativeProposals'],[b['id']])
 def test_assignment_identity_is_issuer_qualified(self):
  rows=copy.deepcopy(self.rows);rows[1]['binding']['assignmentId']=rows[0]['binding']['assignmentId'];self.seal(rows[1]);p.validate_set(rows,self.policy)
 def test_empty_local_suffix_refused(self):self.a['target']['id']='urn:synthetic:subject:person:';self.invalid(self.a)
 def test_unicode_timestamp_refused(self):
  with self.assertRaises(p.Invalid):p.stamp('２０２５-01-01T00:00:00Z')
 def test_genesis_commits_claim(self):
  self.a['target']['id']='urn:synthetic:subject:person:p2'
  with self.assertRaisesRegex(p.Invalid,'predecessor'):p.validate(self.a,self.policy)
 def test_unresolved_endpoint_cannot_activate(self):
  self.a['endpointResolution']['source']='unresolved';self.seal(self.a)
  with self.assertRaisesRegex(p.Invalid,'resolved endpoint'):p.validate(self.a,self.policy)
 def test_restricted_data_denied_by_synthetic_policy(self):
  self.a['binding']['personalDataClass']='restricted'
  with self.assertRaisesRegex(p.Invalid,'classification'):p.validate(self.a,self.policy)
 def test_lone_surrogate_encode_refused(self):
  with self.assertRaises(p.Invalid):p.encode({'reason':chr(0xd800)})
 def test_duplicate_json_member_refused(self):
  import tempfile
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/'duplicate.json';path.write_text('{"x":1,"x":2}')
   with self.assertRaisesRegex(p.Invalid,'duplicate JSON'):p.load(path)

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(IdentityTests))
 (HERE/'test-results.json').write_text(json.dumps({'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sourceDigests':{str(x.relative_to(HERE)):__import__('hashlib').sha256(x.read_bytes()).hexdigest() for x in [HERE/'identity_profile.py',HERE/'identity-profile.schema.json',Path(__file__),*sorted((HERE/'examples').glob('*.json'))]},'tests':result.testsRun,'passed':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors)},indent=2)+'\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)

```

## FILE acceptance.py
```
"""Synthetic new-Dimension acceptance, using explicitly trusted local tools.

python acceptance.py --composer /trusted/WM-XCT-040 --skill /trusted/vercy/skills/vercy --report acceptance-results.json
Only this script's temporary directory is changed. No existing Dimension is used.
"""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from pathlib import Path
import identity_profile as p
HERE=Path(__file__).resolve().parent
def run(composer,skill):
    p.require(__debug__,'Run acceptance without -O')
    composer=Path(composer).resolve();skill=Path(skill).resolve()
    pins=p.load(HERE/'tool-pins.json')
    for name,h in pins['composerFiles'].items():p.require(hashlib.sha256((composer/name).read_bytes()).hexdigest()==h,'unexpected composer bytes: '+name)
    for name,h in pins['skillFiles'].items():p.require(hashlib.sha256((skill/name).read_bytes()).hexdigest()==h,'unexpected skill bytes: '+name)
    for name,h in pins['upstreamFiles'].items():p.require(hashlib.sha256((HERE/'upstream'/name).read_bytes()).hexdigest()==h,'unexpected upstream bytes: '+name)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    identity_policy=p.load(HERE/'examples/policy.json');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-identity-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(slug,name,source):
            raw=source.read_bytes();dest=assets/slug/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':slug+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'text/x-python' if name.endswith('.py') else 'application/json' if name.endswith('.json') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':'https://ver.cy/models/'+slug+('/versions/0.3.0-research.1/' if slug=='wm-xct-036-alias-same-as-mapping' and name in {'spec.yaml','AGENTS.md'} else '/profiles/enterprise-identity/0.1.0/' if name not in {'spec.yaml','AGENTS.md'} else '/')+name}
        releases=[]
        for slug in ['wm-xct-011-identifier-scheme','wm-xct-036-alias-same-as-mapping']:
            source=HERE/'upstream'/slug;raw=(source/'spec.yaml').read_text(encoding='utf-8');meta=json.loads(raw[raw.index('{'):])['metaModel']
            dspec=descriptor(slug,'spec.yaml',source/'spec.yaml');dagent=descriptor(slug,'AGENTS.md',source/'AGENTS.md')
            binding=None
            if meta['id']=='WM-XCT-036':
                runtime=descriptor(slug,'runtime-model.reference.json',HERE/'runtime-model.reference.json')
                instance=descriptor(slug,'identity-profile.schema.json',HERE/'identity-profile.schema.json')
                validator=descriptor(slug,'identity_profile.py',HERE/'identity_profile.py')
                binding={'id':'urn:vercy:binding:enterprise-identity-assertion','version':'0.1.0','forSpecificationDigest':dspec['digest'],'runtime':runtime,'instanceSchema':instance,'companionValidator':validator,'scope':'One bounded enterprise assertion snapshot; companion semantics required; no account ownership, endpoint merge, IAM or whole-model conformance.'}
            releases.append({'modelId':meta['registryId'],'version':meta['version'],'namespace':'urn:vercy:model:'+meta['registryId'],'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':dspec,'agents':dagent,'installationMode':'native-binding' if binding else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:identity','evidence':'urn:synthetic:acceptance:identity','observedAt':c.now(),'scope':'Only this reference binding and synthetic composition.'}})
        releases[1]['requires']=[{k:releases[0][k] for k in ['modelId','version']}]
        for name in ['startup','group','ai-team']:
            target=root/name;stage=root/(name+'-stage');policy_path=root/(name+'-composition-policy.json');lock_path=root/(name+'-lock.json');plan_path=root/(name+'-plan.json')
            dimension=identity_policy['dimension'];at=c.now()
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:identity','dimensionId':dimension,'owner':'urn:synthetic:owner:identity','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic enterprise identity reference'],'allowedModelIds':['vr.wm-xct-011','vr.wm-xct-036'],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:identity'],'allowReviewableDrafts':True,'validFrom':'2026-09-21T00:00:00Z','validUntil':'2027-01-01T00:00:00Z'}
            policy_path.write_bytes(c.encode(policy));lock_path.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:identity:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':'2026-12-31T23:59:59Z','baseLockDigest':c.digest(lock_path.read_bytes()),'roots':[{k:releases[1][k] for k in ['modelId','version']}],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(policy_path.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            plan_path.write_bytes(c.encode(plan));c.stage(plan_path,assets,policy_path,lock_path,stage)
            bootstrap(stage,policy_path,lock_path,skill,target,'Synthetic identity '+name,dimension)
            installed=target/'models/composed/wm-xct-036-alias-same-as-mapping/identity_profile.py'
            p.require(c.digest(installed.read_bytes())==releases[1]['binding']['companionValidator']['digest'],'installed validator differs')
            p.require(c.digest((installed.parent/'identity-profile.schema.json').read_bytes())==releases[1]['binding']['instanceSchema']['digest'],'installed schema differs')
            module_spec=importlib.util.spec_from_file_location('installed_identity_'+name,installed);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
            rows=p.load(HERE/('examples/'+name+'.json'));written_facts=[]
            for i,a in enumerate(rows):
                obj={'recordType':'object','schemaVersion':'1.0.0','recordId':a['id']+':object-r1','objectId':a['id'],'objectType':'vr.wm-xct-036:identity-assertion','name':'Synthetic identity assertion','description':'One assertion; never a Person or a resolution aggregate','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':'urn:synthetic:reference','synthetic':True},'accessClass':'synthetic-private'}
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':a['id']+':snapshot-r1','subjectId':a['id'],'path':'identity.assertion.snapshot','value':a,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[],'status':'asserted','provenance':{'source':'urn:synthetic:reference','synthetic':True},'authority':{'source':'urn:synthetic:actor:steward','rank':0},'masterSystem':'urn:synthetic:reference','accessClass':'synthetic-private'}
                for kind,value in [('object',obj),('fact',fact)]:
                    path=root/(name+str(i)+kind+'.json');path.write_bytes(p.encode(value));written=append(target,kind,path)
                    if kind=='fact':written_facts.append(target/written['written'])
            stored=[p.load(x)['value'] for x in written_facts]
            p.require(stored==rows,'stored assertion round-trip differs from source fixtures');module.validate_set(stored,identity_policy)
            v=native_validate(target);p.require(v['valid'],'native V3 failed')
            # Deliberately corrupt an actually stored nested snapshot. V3 should
            # still accept the outer object type, and the companion must reject.
            victim=written_facts[0];raw=victim.read_bytes();bad=p.load(victim);bad['value']['inferencePermitted']=True;victim.write_bytes(p.encode(bad))
            negative_v3=native_validate(target);rejected=False
            try:module.validate(p.load(victim)['value'],identity_policy)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(raw)
            p.require(negative_v3['valid'] and rejected,'expected native/companion distinction not observed')
            v.pop('dimension',None);negative_v3.pop('dimension',None)
            reports.append({'profile':name,'objects':len(rows),'facts':len(stored),'native':v,'roundTripEqualsInput':stored==rows,'companion':'Explicitly called on actual stored snapshots; not automatically enforced by native V3','invalidNestedSnapshot':{'native':negative_v3,'companionRejected':rejected},'installedValidatorDigest':c.digest(installed.read_bytes()),'pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-identity-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'identity_profile.py',HERE/'identity-profile.schema.json',HERE/'tool-pins.json',*sorted((HERE/'examples').glob('*.json'))]},'limits':'Synthetic new-Dimension assertion snapshots only. Upstream subjects, account ownership, IAM, source truth and existing-Dimension migrations are not tested.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))

```

## FILE README.md
```
# Enterprise identity assertions

Version 0.1.0 is a bounded reference profile associated with WM-XCT-036 Alias / Same-as Mapping and a narrower WM-XCT-011 assignment carrier. Research assurance: **reviewable-draft**. It is available for inspection and synthetic adoption; it is not a certified enterprise identity service or complete parent-model implementation.

An assertion links a source's declared referent to one existing local subject in a named Dimension, purpose and validity interval. Its qualified identifier is the lookup carrier, not a claim that an identifier token is a Person. Several reviewed person-reference exports may identify one local Person. Git/tracker accounts and service accounts remain distinct kinds. Account ownership is a separate relationship, outside this release.

## Run and inspect

Use Python 3.12+ with `jsonschema[format-nongpl]>=4,<5`:

```text
python -m pip install "jsonschema[format-nongpl]>=4,<5"
python test_identity.py
python identity_profile.py examples/startup.json --policy examples/policy.json
```

The **executable schema** is `identity-profile.schema.json`. Four companion schema views are generated from its same definitions; the code loads the combined file only. Policy/claim/event digests are SHA-256 over UTF-8 JSON with sorted keys, no insignificant whitespace, `ensure_ascii=False`, and no nonfinite numbers. This Python serialization profile is not a claim of RFC 8785 conformance. Distribution/composer pins instead hash raw file bytes.

The fixtures are synthetic: three person-reference exports for a startup, scoped/reassigned references for a group, and separate human/service-account references for an AI team. They contain no organizational personnel records. The group example has a deliberately pre-agreed fixed end date; it does not demonstrate learning an assignment closure later.

## Read the result

`resolve()` returns `accepted-in-input`, `contested`, `denied-in-input`, `candidate`, `proposal-only`, or `unknown`. It includes supporting/opposing IDs, candidate disputes, negative proposals, exclusions, time coordinates, caller/purpose and digests. `accepted-in-input` means one admissible positive target in this supplied set. It does not prove global uniqueness, source completeness, identity or access rights. A negative assertion against a different target does not contradict a positive claim. A dispute of a previously asserted claim blocks acceptance; a disputed unasserted candidate does not veto an accepted claim.

Different assignment occurrences sharing a qualified key are **preserved**, not rejected on ingestion. Simultaneously active different target claims produce `contested` in the query. This is an assertion-evidence ledger, not an issuer's assignment allocator; write-time namespace exclusivity and a global collision register are deferred. Separate assertion IDs preserve independent supporting claims; replay idempotency is by assertion ID, not semantic deduplication.

## Live import and history

`import_assertion(existing, incoming, policy, now=trusted_receipt_time)` is pure and writes nothing. Every new event must use the supplied receipt time, strictly after the current input's recording head. At second precision, stage one transition per receipt; batch historical events are not accepted through the live import path. Identical replay is a no-op. Fixed claim content and all prior events must remain unchanged. Genesis commits to the fixed claim digest; subsequent events commit to the previous event. These hashes detect inconsistency, not forged signatures.

Historical fixture restoration is a separate, explicitly trusted snapshot operation. `validate_set()` alone cannot prove when data was received or whether history was truncated. A caller bypassing the live import function loses its historical-preservation guarantee. A real adapter must authenticate the clock/policy/evidence, persist the accepted set and import head under a lock, and compare the expected head. No production writer adapter is supplied.

Backdated **effective** corrections are allowed inside claim validity. At a given knowledge time, the latest recorded eligible correction wins from its effective date, including over an earlier activation. Past knowledge answers remain stable only when future additions pass the trusted live-import path and the input set is retained. Input digests include the complete supplied history and may change even when a historical answer does not.

## Trust and limitations

- Policy registers scheme/version/issuer/scope to referent kind, and assigns disjoint kind namespaces inside the local subject namespace. Changing two kind labels cannot bypass those declared registers. The source's real meaning, endpoint existence and evidence authenticity remain external checks. No four-eyes separation is enforced.
- Local subject references use a restrictive URN/HTTPS profile: no percent escapes, dot segments, query, fragment or backslash; an empty local suffix is refused. This is rejection, not silent URI normalization.
- One frozen policy covers writers **and readers**. Any policy change invalidates every pin and fails closed. There is no separate dynamically rotating read policy. The synthetic policy expires on 2027-01-01. Continued use needs an explicitly reviewed new policy/claim set; changing policy in place is not a supported migration. Current-clock checks must never be bypassed by backdating a real read.
- Binding fields form an immutable source observation. Later source-state changes to the same issuer-qualified assignment ID are not supported. No fake new source assignment ID may be invented to evade this limit. Unknown or pre-recorded future-effective assignments, historical assignment revision, cross-kind negatives, normalization, matching, transitive closure, endpoint merge/split, policy history, erasure and federation remain deferred.
- Raw V3 validates only the outer snapshot record. The **companion validator is mandatory and is explicitly invoked by the acceptance harness; native V3 does not automatically enforce it**. The outer `asserted` status means the snapshot was recorded, not that the inner identity claim is accepted. V3 requires a numeric rank; the harness uses neutral `0` on the snapshot only. The identity resolver never reads it and performs no authority ranking. Outer validity begins when the snapshot is recorded; identity time must be queried through `resolve()`.
- The acceptance harness checks byte-pinned tooling/upstream inputs, installed validator/schema digests and actual stored-snapshot equality. It creates three temporary new Dimensions and demonstrates that V3 alone accepts a bad nested assertion which the companion rejects. It is time-bounded to the disclosed 2026 fixture window. No existing-Dimension transactional update, persistent truncation prevention or production concurrency is tested.
- The parent models' original publication holds remain, including broad source verification and formal boundary work. This increment does not clear them. Independent study/audit scopes and unresolved limits are recorded separately.

See `model-spec.md`, `crosswalk.json`, `field-catalog.json`, `whole-object-coverage.json`, `mastership-and-rights.json`, `lifecycle.json`, and the test/acceptance reports. Start adoption with the full envelope and a trusted policy; never export a bare ID-to-person table as equivalent.

```

## FILE model-spec.md
```
# Enterprise identity-assertion profile 0.1.0

## Boundary and canonical ownership

This is a narrower usage and representation profile of WM-XCT-036, not a new subject model. Identifier assignment meaning is reused from WM-XCT-011. A source binding is a frozen carrier value in an assertion, whose source authority remains external. An assertion is its own identified claim. The resolution result is a derived, disposable query artifact; it has no subject mastership. The externally supplied policy is a reference-test binding of local governance, not a new policy model owned by identity.

Included WM-XCT-036 concerns: assertion envelope, endpoint reference boundary, relation classification, contextual validity, evidence, immutable transition history, and a scoped read contract. Matching engines, graph closure, redirects, global equality, cluster mastership, disclosure engines and endpoint mutations remain excluded. The exact included source finding/layer IDs are recorded in `crosswalk.json`.

The profile admits `equivalent-in-context`, `not-same-assertion` and `probable-entity-match`, using the existing relation register. All have `inferencePermitted=false`; the third can never enter asserted state. The existing definition of equivalent-in-context limits its claim to a named context; here that context is the adopting Dimension, declared purpose, referent kind and interval. It does not mean account ownership, loose resemblance or global OWL equality. We deliberately retain existing codes instead of adopting Grok's proposed new names. Scores, names and email matches cannot activate a claim on their own.

## Types, identities and relationships

| Type | Identity and role | Cardinality and ownership |
|---|---|---|
| QualifiedIdentifierAssignment | Source-issued `assignmentId`, exact `scheme`, `schemeVersion`, `issuer`, `scope`, `value`; occurrence validity and source record | One frozen assignment carrier per assertion. Issuer owns the assignment; importer cannot reinterpret it. Same issuer-qualified assignment ID with different observation content is refused; later assignment revisions are deferred. |
| IdentityAssertion | Local issuer-qualified `id`, Dimension, purpose, predicate, fixed source and target, fixed validity | One source and one target. A subject can have many independent assertions. Zero or many assertions may concern one qualified ID. Conflicting claims are data to preserve. |
| AssertionRevisionEvent | Distinct `id`, genesis claim digest / previous event digest, effective time, recorded time, actor, state, reason and evidence | Ordered one-to-many owned history. Event IDs are unique across the provided set. Source evidence is referenced, not copied as private content. |
| EvidenceReference | Source-qualified URI plus kind and description | One or more per event. Activation requires source-record and review-decision categories; authenticity is a caller responsibility. |
| ReferenceAuthorityPolicy | Independently supplied URI/version and digest, Dimension, purpose, namespace, issuer list, actor permissions, readers and interval | One frozen policy for the bounded input set. The Dimension policy owner supplies it. It is not self-issued by an assertion. |
| ResolutionView | Canonical input digest, policy digest and two temporal coordinates | Computed on demand over one supplied set. Returns supporting/opposing/candidate/disputed IDs. No editable canonical subject or aggregate is created. |

The executable contract is `identity-profile.schema.json`; `assertion.schema.json`, `binding.schema.json`, `policy.schema.json` and `query.schema.json` are generated companion views. Field-level types, requiredness and cardinalities derive from that combined contract. `field-catalog.json` maps their carrier fields to ownership, sensitivity and the governing contract. All object schemas are closed. Optional open end is `null`; missing required context is rejected, not guessed. No numeric confidence is encoded, so absence cannot be confused with zero.

## Lifecycle, temporal queries and correction

An assertion begins proposed. Proposed can become asserted, disputed or retracted. Asserted can become disputed or retracted. Disputed can become asserted or retracted. Retracted is terminal. These are recorded issuer declarations; a derived view separately evaluates eligibility and conflict.

Each event must be authorized by the supplied frozen policy at its recording time. Recording times increase strictly. Effective times may be retroactive but cannot precede the assertion's start or exceed their recording time; they must also precede an exclusive claim end. At `(validAt, knownAt)`, select the latest recorded event known then whose effective time has arrived. Both assertion and assignment intervals are half-open. A later correction can change a current view. Earlier knowledge answers are preserved only for a retained set extended through the trusted live-import path described in README.md; standalone snapshot validation cannot guarantee reception history. The report's digest may change when the supplied set grows even though the historical substantive answer stays the same.

A changed endpoint, purpose, predicate or validity window is a new assertion ID, after explicit retraction of the old claim when appropriate. Append-only history is enforced relative to the caller's existing input by `import_assertion`; the reference cannot prove that an arbitrary standalone input has not been falsified or truncated. Live imports require new events stamped with the trusted receipt time after the global input head; retrospective snapshot restoration is outside this API. Concurrent persistence, event authentication and historical-policy recovery are separate integration duties.

## Invariants

1. Compare exact qualified keys only; issuer and tenant scope are never inferred.
2. Preserve scheme version, raw value and assignment occurrence. This profile has no normalization transform.
3. The assignment's declared referent kind must equal the target kind. Both declarations must match a trusted scheme-kind register and the target kind namespace. This checks declared semantics, not the real source system.
4. The target must be in the policy's local subject namespace; no positive identifier-to-identifier chains are traversed.
5. Fixed assertion content cannot change under the same assertion ID; previous event digests and historical prefixes remain intact.
6. Candidate relations never activate. Activation requires both source evidence and reviewer evidence as declared categories.
7. Policy digest, Dimension, purpose, permitted issuer, actor/state grant and recording-time validity must agree.
8. Read purpose and actor must be allowed by the same frozen policy that pins all claims; independent read-policy rotation is not supported. Historical knowledge cannot exceed evaluation time.
9. Validity cannot exceed the assignment interval. Unknown starts and invalid/reversed windows are refused.
10. Multiple active target IDs, active opposition against a positive target, or a dispute of a previously asserted claim produce contested status. Unasserted candidate disputes cannot veto acceptance. Authority ranking is deliberately absent.
11. Reviewed negative-only input produces denied-in-input; proposed negatives produce proposal-only. Inert positive candidates produce candidate; no applicable claim produces unknown.
12. Replaying an identical assertion is a no-op; divergent content or history truncation is refused. The acceptance harness compares the actual stored JSON snapshots with the source fixtures; arbitrary external converters are not certified.
13. The resolver does not grant access, export equality, mutate endpoints or assert global completeness.
14. A V3-valid outer fact can contain a semantically invalid snapshot; companion validation is mandatory.

## Questions and artifact routes

| Question | Inspect / produce | Permitted next action |
|---|---|---|
| What does this source ID actually denote? | Binding kind and source record | Request source evidence; do not infer Person from Account |
| Who owns its namespace? | Scheme, issuer, scope | Compare only within the qualified key |
| Which scheme version governs comparison? | Version and exact-string declaration | Refuse unsupported normalization |
| Is this a new assignment occurrence? | Assignment ID and validity | Preserve prior occurrence and inspect source history |
| What local subject does the claim concern? | Target ID and kind | Verify namespace and reference externally |
| Who may assert this link? | Policy digest and event actor grant | Validate declared grant, then authenticate externally |
| What evidence supports activation? | Source-record and review-decision references | Keep name/email-only material proposed |
| Is the claim only a candidate? | Relation and history | Never auto-activate a score |
| What was effective at a date? | Valid time and event effective time | Produce a scoped temporal view |
| What was known at that date? | Recorded times and knownAt | Preserve earlier substantive answers |
| Is another claim incompatible? | Complete caller-selected input set | Return contested; do not choose a winner |
| Is there explicit opposition? | Negative assertions and opposing IDs | Retain negative knowledge distinctly |
| How is a mistake corrected? | Retraction plus successor assertion | Use append-only import; leave endpoints intact |
| Can this link disclose another Dimension? | Namespace and external access policy | Deny implicit disclosure |
| Is a replay identical? | Assertion identity, digest and history prefix | No-op or explicit conflict |
| What is missing for a real merge? | Separate migration/transaction plan | Defer endpoint merge and split |
| What survives a round-trip? | Complete closed envelope | Refuse field-dropping conversions |
| Is this globally unique or authenticated? | Scope and caller trust assumptions | Answer insufficient-context; do not claim proof |

Every answer is conditional on available authoritative context. If evidence or permission is missing, request the relevant artifact or return a refusal/unknown; do not synthesize facts.

## Adoption and migration

Start with the synthetic fixtures. A real deployment needs source-specific mapping, source-issued assignment identities, authenticated policy/evidence, retention and access controls, storage concurrency and an independently selected complete input set. The reference does not allocate those responsibilities to Git, HRIS or an ERP merely by naming them.

Legacy matcher scores or denormalized identity columns enter review as proposals. Do not import an existing merge as accepted truth. A changed profile version requires explicit semantic comparison; unknown versions are refused. No automated downgrade or in-place Dimension migration is supplied. WM-XCT-040's exact new-Dimension composition route is used only with explicit pins and separate semantic/native readiness.

## Binding interpretation and excluded parent obligations

The lookup token denotes `binding.sourceReferentRef`; the contextual relationship is between that source referent and `target.id`, never token-to-Person equality. `endpointResolution` records externally checked resolution declarations; asserted claims require both resolved. The policy scheme register is a profile restriction, not a complete WM-XCT-011 scheme definition. Source-specific granularity, exclusivity, full assignment revision, qualifier vocabularies and WM-XCT-036 kind-change lineage remain deferred. The crosswalk is a narrower/overlap usage mapping, **not full conformance** to every required field in those parent findings. No new registry edge or final mixin/relationship classification is ratified by this release.

```

## FILE crosswalk.json
```
{"profileVersion":"0.1.0","form":"narrower usage profile and explicit reference binding, not a new world-model","predecessor":"XCT-01 candidate fields are input hypotheses, not an exactMatch","candidates":[{"candidate":"IdentifierBinding","disposition":"reuse-carriage","model":"WM-XCT-011","version":"0.3.0-research.1","finding":"identifier-assignment-record","fields":["de-identifier-value","de-referent-ref","de-assignment-effective-time","de-assignment-recorded-time","de-assignment-validity-period"],"relation":"narrower","losses":"Exact-string profile only; unknown starts, arbitrary normalization and assignment issuance are deferred."},{"candidate":"IdentityAssertion","disposition":"profile","model":"WM-XCT-036","version":"0.3.0-research.1","findings":["als-tax-kind-register","als-tax-endpoint-scope","als-tax-conflict-change"],"relation":"narrower","losses":"Only contextual positive, explicit negative and inert candidate relations. No global equality or endpoint mutation."},{"candidate":"IdentityResolution","disposition":"derived-query-adapter","model":"WM-XCT-036","version":"0.3.0-research.1","relation":"overlap","losses":"Input-scoped one-hop answer only; no authoritative cluster, ranking, policy history, matching or merge."}],"fieldCrosswalk":{"scheme_uri":"binding.scheme","external_id":"binding.value plus issuer/scope/version/assignmentId; bare ID is insufficient","mapping_kind":"relation, closed subset with inference disabled","mapping_evidence":"history[].evidence references with declared kind"},"includedParentLayers":["als-asrt-identity-layer","als-tax-kind-catalogue","als-tax-subject-planes","als-state-l-temporal-frame","als-query-temporal-read","als-query-resolution-semantics"],"excludedConcerns":["reasoner","cluster mastership","endpoint merge/split","redirect execution","IAM","privacy/erasure enforcement","account ownership"],"upstream":[{"id":"WM-XCT-011","version":"0.3.0-research.1","url":"https://ver.cy/models/wm-xct-011-identifier-scheme/","files":[{"name":"spec.yaml","sha256":"aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834","bytes":293335,"publicMatchesLocal":true},{"name":"AGENTS.md","sha256":"aa912b04d27278cf822b1067a6ea64bb7bdd88f955165f08862bbd3e612dff43","bytes":932,"publicMatchesLocal":true},{"name":"publication.json","sha256":"796783e1c3a37632e89c157feb5be9b9f0dda8d4479a06729089f43666fcd7d3","bytes":1119,"publicMatchesLocal":true}],"holds":["Verify live availability, version and exact claim support for every source accepted into the synthesis.","Resolve or explicitly scope the deferred identifier families before promoting a claim of catalogue completeness."],"scope":"Full JSON parsed and recursively inventoried; current package files read and compared to public bytes. This is a boundary comparison, not independent re-verification of every legacy source or question."},{"id":"WM-XCT-036","version":"0.3.0-research.1","url":"https://ver.cy/models/wm-xct-036-alias-same-as-mapping/","files":[{"name":"spec.yaml","sha256":"21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17","bytes":1450032,"publicMatchesLocal":true},{"name":"AGENTS.md","sha256":"fc0527060b5c83f23f89ae6e83fc5dfdff4cf509fe1437e1a49e3916ff70e1ba","bytes":952,"publicMatchesLocal":true},{"name":"publication.json","sha256":"54848bc9a79c682c87f9e8224b7cdb021a016c8dc5280e41c63dbd775fe7e51c","bytes":2450,"publicMatchesLocal":true}],"holds":["Live re-verification is required for all 108 cited source URLs and version/edition pins before this leaves reviewable-draft status, especially the two Candidate-Recommendation-stage W3C drafts (RDF 1.2 Concepts, DID Resolution) and the expired idempotency-key Internet-Draft, none of which this no-tools audit could re-check.","This entire result was produced under an owner-authorized single-provider waiver: the repository owner instructed the queue to continue Claude-only from WM-XCT-013 onward after repeated Grok structured-output failures (authorized 2026-08-29), so no independent second-provider cross-check exists for WM-XCT-036, and that absence must stay visibly disclosed on this artifact.","The relationship contract for vr.wm-xct-036 is currently an empty array despite the model's boundary_notes and adversarial_checks describing eight distinct neighbor relations (parent WM-XCT-011, endpoint models, identifier authority, predicate vocabularies, reasoning/closure model, matching engine, authorization model, audit model); none is yet a ratified registry relation.","The registry review_state is explicitly 'boundary-review-required' with priority_confidence 'low'; this draft should not advance past reviewable-draft status until that formal boundary review resolves the entry-kind tension and the unverified WM-XCT-011 parent link noted in this audit.","Independent second-provider review was explicitly waived by the repository owner; this Claude-only result remains a reviewable draft."],"scope":"Full JSON parsed and recursively inventoried; current package files read and compared to public bytes. This is a boundary comparison, not independent re-verification of every legacy source or question."}],"verificationLimit":"Exact field/finding excerpts were read and retained; the broad historical source claims and full relation-contract ratification remain open.","parentFieldDisposition":{"de-referent-ref":"binding.sourceReferentRef is the source referent, while target.id is the local referent. Identifier token is only a lookup carrier.","endpoint_resolution_state":"endpointResolution.source/target: declared externally checked states; asserted requires resolved.","endpoint_kind_admissibility":"A profile proposal over source referent -> local referent of one registered kind, not a ratified complete parent predicate register. No token-to-Person equality.","scheme_granularity_exclusivity":"Deferred to external scheme governance; this profile accepts issuer/scope-qualified keys and does not certify the complete 011 scheme.","assignment_bitemporality":"Narrower frozen observation only. No same-assignment closure revision or future-effective pre-registration support.","relation_register_release":"Selected meanings pinned to 036 0.3.0-research.1; full register and relation contract remain unratified.","kind_change_lineage":"New claim ID and explicit retraction; automated successor link is deferred."},"conformanceClaim":"No complete parent conformance. Narrower/overlap usage and carrier mapping only; missing parent obligations remain explicit.","assignmentIdentity":"(issuer, assignmentId), not a globally unqualified external occurrence ID"}
```

## FILE examples/policy.json
```
{"format":"vercy-identity-reference-policy","version":"0.1.0","id":"urn:synthetic:policy:identity-v1","dimension":"urn:synthetic:dimension:identity","purpose":"synthetic-identity-review","subjectPrefix":"urn:synthetic:subject:","validFrom":"2025-01-01T00:00:00Z","validTo":"2027-01-01T00:00:00Z","issuers":["urn:synthetic:source:hr","urn:synthetic:source:git-person-map","urn:synthetic:source:tracker-person-map"],"relations":["equivalent-in-context","not-same-assertion","probable-entity-match"],"actors":[{"actor":"urn:synthetic:actor:steward","states":["proposed","asserted","disputed","retracted"]},{"actor":"urn:synthetic:actor:importer","states":["proposed"]}],"readers":["urn:synthetic:actor:steward"],"dataClasses":["synthetic"],"schemeKinds":[{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:startup","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:startup","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:suba","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:suba","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:subb","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:subb","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:other","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:other","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:startup","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:startup","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:suba","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:suba","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:subb","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:subb","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:other","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:other","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:startup","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:startup","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:suba","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:suba","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:subb","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:subb","kind":"service-account"},{"scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:other","kind":"person"},{"scheme":"urn:synthetic:scheme:service-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:other","kind":"service-account"}],"subjectNamespaces":[{"kind":"person","prefix":"urn:synthetic:subject:person:"},{"kind":"organization","prefix":"urn:synthetic:subject:organization:"},{"kind":"user-account","prefix":"urn:synthetic:subject:user-account:"},{"kind":"service-account","prefix":"urn:synthetic:subject:service-account:"}]}
```

## FILE examples/startup.json
```
[{"format":"vercy-enterprise-identity-assertion","version":"0.1.0","id":"urn:synthetic:assertion:startup-0","dimension":"urn:synthetic:dimension:identity","purpose":"synthetic-identity-review","policyDigest":"sha256:0f409afbf7750c803936b456a7f981360d848b2248e6b5c8f8e25d9aa9b09cf1","binding":{"assignmentId":"urn:synthetic:assignment:startup-0","scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:hr","scope":"urn:synthetic:tenant:startup","value":"E7","comparison":"exact-string","kind":"person","validFrom":"2025-01-01T00:00:00Z","validTo":null,"recordedAt":"2025-01-01T00:00:00Z","sourceRecord":"urn:synthetic:evidence:source-startup-0","sourceReferentRef":"urn:synthetic:source:hr:referent:startup-0","personalDataClass":"synthetic","credentialProhibition":true},"target":{"id":"urn:synthetic:subject:person:p1","kind":"person"},"relation":"equivalent-in-context","endpointResolution":{"source":"resolved","target":"resolved"},"validFrom":"2025-01-01T00:00:00Z","validTo":null,"inferencePermitted":false,"history":[{"id":"urn:synthetic:event:startup-0:proposed","previousDigest":"sha256:de1c0f715cf238bdf65cfc63fe76b664429a6492dccff41ad71361e1547e7215","recordedAt":"2025-01-01T00:00:00Z","effectiveAt":"2025-01-01T00:00:00Z","actor":"urn:synthetic:actor:steward","state":"proposed","reason":"Synthetic reviewed linkage; not a real source-system identity claim","evidence":[{"ref":"urn:synthetic:evidence:source-startup-0","kind":"source-record","description":"Synthetic source export identifies a referent of the declared kind"},{"ref":"urn:synthetic:evidence:review-startup-0","kind":"review-decision","description":"Synthetic steward decision, no authentication claim"}]},{"id":"urn:synthetic:event:startup-0:asserted","previousDigest":"sha256:d0412ae7966b92e79a256c5b823064bf5437a644bbfd4dee837a7f35947955b1","recordedAt":"2025-01-01T00:00:01Z","effectiveAt":"2025-01-01T00:00:00Z","actor":"urn:synthetic:actor:steward","state":"asserted","reason":"Synthetic reviewed linkage; not a real source-system identity claim","evidence":[{"ref":"urn:synthetic:evidence:source-startup-0","kind":"source-record","description":"Synthetic source export identifies a referent of the declared kind"},{"ref":"urn:synthetic:evidence:review-startup-0","kind":"review-decision","description":"Synthetic steward decision, no authentication claim"}]}]},{"format":"vercy-enterprise-identity-assertion","version":"0.1.0","id":"urn:synthetic:assertion:startup-1","dimension":"urn:synthetic:dimension:identity","purpose":"synthetic-identity-review","policyDigest":"sha256:0f409afbf7750c803936b456a7f981360d848b2248e6b5c8f8e25d9aa9b09cf1","binding":{"assignmentId":"urn:synthetic:assignment:startup-1","scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:git-person-map","scope":"urn:synthetic:tenant:startup","value":"person-7","comparison":"exact-string","kind":"person","validFrom":"2025-01-01T00:00:00Z","validTo":null,"recordedAt":"2025-01-01T00:00:00Z","sourceRecord":"urn:synthetic:evidence:source-startup-1","sourceReferentRef":"urn:synthetic:source:git-person-map:referent:startup-1","personalDataClass":"synthetic","credentialProhibition":true},"target":{"id":"urn:synthetic:subject:person:p1","kind":"person"},"relation":"equivalent-in-context","endpointResolution":{"source":"resolved","target":"resolved"},"validFrom":"2025-01-01T00:00:00Z","validTo":null,"inferencePermitted":false,"history":[{"id":"urn:synthetic:event:startup-1:proposed","previousDigest":"sha256:64d83895b8d189c458b25912c674e76c0e24c347a9e06ec63e0a41b1b23d492e","recordedAt":"2025-01-01T00:00:00Z","effectiveAt":"2025-01-01T00:00:00Z","actor":"urn:synthetic:actor:steward","state":"proposed","reason":"Synthetic reviewed linkage; not a real source-system identity claim","evidence":[{"ref":"urn:synthetic:evidence:source-startup-1","kind":"source-record","description":"Synthetic source export identifies a referent of the declared kind"},{"ref":"urn:synthetic:evidence:review-startup-1","kind":"review-decision","description":"Synthetic steward decision, no authentication claim"}]},{"id":"urn:synthetic:event:startup-1:asserted","previousDigest":"sha256:021505c7b54a551e4c92e20a4100e6eaefe526ee826fa29efe4dd2ec2231fd4e","recordedAt":"2025-01-01T00:00:01Z","effectiveAt":"2025-01-01T00:00:00Z","actor":"urn:synthetic:actor:steward","state":"asserted","reason":"Synthetic reviewed linkage; not a real source-system identity claim","evidence":[{"ref":"urn:synthetic:evidence:source-startup-1","kind":"source-record","description":"Synthetic source export identifies a referent of the declared kind"},{"ref":"urn:synthetic:evidence:review-startup-1","kind":"review-decision","description":"Synthetic steward decision, no authentication claim"}]}]},{"format":"vercy-enterprise-identity-assertion","version":"0.1.0","id":"urn:synthetic:assertion:startup-2","dimension":"urn:synthetic:dimension:identity","purpose":"synthetic-identity-review","policyDigest":"sha256:0f409afbf7750c803936b456a7f981360d848b2248e6b5c8f8e25d9aa9b09cf1","binding":{"assignmentId":"urn:synthetic:assignment:startup-2","scheme":"urn:synthetic:scheme:person-directory","schemeVersion":"1","issuer":"urn:synthetic:source:tracker-person-map","scope":"urn:synthetic:tenant:startup","value":"person-reference-7","comparison":"exact-string","kind":"person","validFrom":"2025-01-01T00:00:00Z","validTo":null,"recordedAt":"2025-01-01T00:00:00Z","sourceRecord":"urn:synthetic:evidence:source-startup-2","sourceReferentRef":"urn:synthetic:source:tracker-person-map:referent:startup-2","personalDataClass":"synthetic","credentialProhibition":true},"target":{"id":"urn:synthetic:subject:person:p1","kind":"person"},"relation":"equivalent-in-context","endpointResolution":{"source":"resolved","target":"resolved"},"validFrom":"2025-01-01T00:00:00Z","validTo":null,"inferencePermitted":false,"history":[{"id":"urn:synthetic:event:startup-2:proposed","previousDigest":"sha256:845d195106ec7cc18e62fc7d2650f0d460bcc8dde0d4bb1464d0f232759f46b3","recordedAt":"2025-01-01T00:00:00Z","effectiveAt":"2025-01-01T00:00:00Z","actor":"urn:synthetic:actor:steward","state":"proposed","reason":"Synthetic reviewed linkage; not a real source-system identity claim","evidence":[{"ref":"urn:synthetic:evidence:source-startup-2","kind":"source-record","description":"Synthetic source export identifies a referent of the declared kind"},{"ref":"urn:synthetic:evidence:review-startup-2","kind":"review-decision","description":"Synthetic steward decision, no authentication claim"}]},{"id":"urn:synthetic:event:startup-2:asserted","previousDigest":"sha256:9e54b31b1f7fe63d40ecfd2f41b2ed8335091e7c9ff020ba3512bd93597649e9","recordedAt":"2025-01-01T00:00:01Z","effectiveAt":"2025-01-01T00:00:00Z","actor":"urn:synthetic:actor:steward","state":"asserted","reason":"Synthetic reviewed linkage; not a real source-system identity claim","evidence":[{"ref":"urn:synthetic:evidence:source-startup-2","kind":"source-record","description":"Synthetic source export identifies a referent of the declared kind"},{"ref":"urn:synthetic:evidence:review-startup-2","kind":"review-decision","description":"Synthetic steward decision, no authentication claim"}]}]}]
```

## FILE test-results.json
```
{"executedAt":"2026-09-21T17:06:24.993950+00:00","sourceDigests":{"identity_profile.py":"59722ef63ad6ddd76e511de8f10c2c6c7fc70ea6667507b6998efbbdf9e1896e","identity-profile.schema.json":"d5dbab037ea7af7f5b9feef95929f461380d824849caad092af7ea1706cc54c7","test_identity.py":"872d8f55d30e5c73b16c21b97f7316f678406dbb90a2236fc4db531fc8fcbeac","examples\\ai-team.json":"1b945c084570d40e97214c68e519731f0bce2baeb2675c34b203fc4d23ebde14","examples\\group.json":"04860545cf61f6d5bdd18a5a8e00294982e7477496196ae84e66825f4d127157","examples\\policy.json":"4062926e1a81fd95ae027b6f16e7acdc6864b3e2c812cbaf0fb8f60edc80b707","examples\\startup.json":"da6cef738511c163fc8b5e1622ede24020339ffa97965540c1a87df4c118a3af"},"tests":78,"passed":true,"failures":0,"errors":0}
```

## FILE acceptance-results.json
```
{"format":"vercy-identity-profile-acceptance","executedAt":"2026-09-21T17:08:52Z","passed":3,"failed":0,"profiles":[{"profile":"startup","objects":3,"facts":3,"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"roundTripEqualsInput":true,"companion":"Explicitly called on actual stored snapshots; not automatically enforced by native V3","invalidNestedSnapshot":{"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"companionRejected":true},"installedValidatorDigest":"sha256:59722ef63ad6ddd76e511de8f10c2c6c7fc70ea6667507b6998efbbdf9e1896e","pins":[{"id":"vr.wm-xct-011","version":"0.3.0-research.1","digest":"sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834","mode":"semantic-only"},{"id":"vr.wm-xct-036","version":"0.3.0-research.1","digest":"sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17","mode":"native-binding"}]},{"profile":"group","objects":3,"facts":3,"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"roundTripEqualsInput":true,"companion":"Explicitly called on actual stored snapshots; not automatically enforced by native V3","invalidNestedSnapshot":{"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"companionRejected":true},"installedValidatorDigest":"sha256:59722ef63ad6ddd76e511de8f10c2c6c7fc70ea6667507b6998efbbdf9e1896e","pins":[{"id":"vr.wm-xct-011","version":"0.3.0-research.1","digest":"sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834","mode":"semantic-only"},{"id":"vr.wm-xct-036","version":"0.3.0-research.1","digest":"sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17","mode":"native-binding"}]},{"profile":"ai-team","objects":2,"facts":2,"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":2,"facts":2,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"roundTripEqualsInput":true,"companion":"Explicitly called on actual stored snapshots; not automatically enforced by native V3","invalidNestedSnapshot":{"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":2,"facts":2,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"companionRejected":true},"installedValidatorDigest":"sha256:59722ef63ad6ddd76e511de8f10c2c6c7fc70ea6667507b6998efbbdf9e1896e","pins":[{"id":"vr.wm-xct-011","version":"0.3.0-research.1","digest":"sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834","mode":"semantic-only"},{"id":"vr.wm-xct-036","version":"0.3.0-research.1","digest":"sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17","mode":"native-binding"}]}],"sourceDigests":{"acceptance.py":"dbd411081247b3d5bbb4661a3cb9616665ae8e3a5826642a00dc578095b3fd3c","identity_profile.py":"59722ef63ad6ddd76e511de8f10c2c6c7fc70ea6667507b6998efbbdf9e1896e","identity-profile.schema.json":"d5dbab037ea7af7f5b9feef95929f461380d824849caad092af7ea1706cc54c7","tool-pins.json":"9c664506473f41b3ebc23376caa28fd7e323c0158db7c1a6676ad3dbc8afc434","examples\\ai-team.json":"1b945c084570d40e97214c68e519731f0bce2baeb2675c34b203fc4d23ebde14","examples\\group.json":"04860545cf61f6d5bdd18a5a8e00294982e7477496196ae84e66825f4d127157","examples\\policy.json":"4062926e1a81fd95ae027b6f16e7acdc6864b3e2c812cbaf0fb8f60edc80b707","examples\\startup.json":"da6cef738511c163fc8b5e1622ede24020339ffa97965540c1a87df4c118a3af"},"limits":"Synthetic new-Dimension assertion snapshots only. Upstream subjects, account ownership, IAM, source truth and existing-Dimension migrations are not tested."}
```
