# Final focused remediation audit, EM-XCT-01 profile 0.1.0

Reply in English, no tools, execution or publication. Return BLOCK or ACCEPT WITH LIMITS for these focused changes. Retain prior audits. Do not claim a complete source or parent-model review or that you executed reported tests. Last full candidate got Claude BLOCK(narrow B1/B2) and Grok ACCEPT WITH LIMITS. This request changes those bytes; it is not a retry of a failure.

B1 fixed: validate now canonically encodes the complete assertion before accepting it, including its last event/evidence text. Tests put an escaped lone surrogate in both last reason and evidence.description, through live import.
B2 fixed: proposals never reserve an issuer-qualified assignment observation. Consistency is required only among non-retracted claims whose history reached asserted. Retraction releases reservation but retains evidence; conflicting carried observations across the whole input are returned in retainedObservationConflicts. A regression imports a bogus lowest-privilege proposal, then genuine observation with same source occurrence, then asserts the genuine one successfully. Another checks reservation release and another keeps rejecting conflicting active asserted observations. No fake source assignment IDs and no evidence deletion.
L1 / Grok CX3 fixed: prior=history[:-1] uses valid/known-time-filtered history when classifying a dispute. A later-effective activation cannot make an earlier valid-time proposal dispute veto acceptance.
L2 expressly defined: evaluation_at IS the independently trusted current clock supplied by caller; known_at must not exceed it. It is not a simulated future knowledge boundary. The API does not authenticate clocks. This is documented alongside live-import/storage-lock responsibility.
Grok CX5 counterexample was tested: with installed required URI format checker, spaces and U+FF0F in subject URI are rejected by SCHEMA, so no extra normalizer added.
Added re-sealed endpoint-change test reaches fixed-claim import check. Local results: 87 tests pass, three new-Dimension scenarios pass again after code change. You did not execute them.

Other limits remain explicit: snapshot/CLI validation does not enforce reception history; policy/clock/evidence/source kind are caller-trusted; a global head allows one transition per second; no inverse subject index; crosswalk is narrower/overlap rather than full conformance; native V3 requires outer rank metadata (0) but never consumes identity ranking, companion is separately invoked, existing-Dimension transactions deferred. Pins are trusted local source-byte checks, not a secure execution sandbox. Parse/decode exceptions fail closed but not all normalize to Invalid; schema must be protected after install. Source referent namespaces and assertion-ID namespace ownership remain external. Broad parent holds remain.

Scope below: entire final evaluator, the new regression tests, final documentation clarification, and compact reports/hashes. The combined schema is unchanged from the prior 11-file freeze; its hash is supplied, not its body. Earlier tests/native harness are unchanged except the newly shown tests and reports. Limit your verdict accordingly.

## Final evaluator
```python
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

```
## New regression tests (same IdentityTests helpers from prior freeze)
```python
 def test_latest_reason_surrogate_rejected_at_import(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0].update(recordedAt='2026-09-21T00:00:00Z',actor='urn:synthetic:actor:importer',reason='x'+chr(0xd800))
  with self.assertRaisesRegex(p.Invalid,'canonically encoded'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_latest_evidence_surrogate_rejected_at_import(self):
  a=self.other();a['history']=a['history'][:1];a['history'][0]['recordedAt']='2026-09-21T00:00:00Z';a['history'][0]['evidence'][0]['description']='x'+chr(0xd800)
  with self.assertRaisesRegex(p.Invalid,'canonically encoded'):p.import_assertion(self.rows,a,self.policy,now='2026-09-21T00:00:00Z')
 def test_proposal_cannot_squat_assignment(self):
  s=self.other();s['history']=s['history'][:1];s['binding']['assignmentId']='urn:synthetic:assignment:hr-9';s['binding']['value']='bogus';s['history'][0].update(recordedAt='2026-09-21T00:00:00Z',actor='urn:synthetic:actor:importer');self.seal(s)
  rows=p.import_assertion(self.rows,s,self.policy,now='2026-09-21T00:00:00Z')
  g=self.other();g['id']+=':genuine';g['binding']['assignmentId']=s['binding']['assignmentId'];g['binding']['value']='E9';g['history']=g['history'][:1];g['history'][0].update(id=g['history'][0]['id']+':genuine',recordedAt='2026-09-22T00:00:00Z');self.seal(g)
  rows=p.import_assertion(rows,g,self.policy,now='2026-09-22T00:00:00Z')
  active=self.append(g,'asserted',recorded='2026-09-23T00:00:00Z',effective='2026-09-22T00:00:00Z')
  rows=p.import_assertion(rows,active,self.policy,now='2026-09-23T00:00:00Z');self.a=active
  r=self.query(rows,valid_at='2026-09-24T00:00:00Z',known_at='2026-09-24T00:00:00Z',evaluation_at='2026-09-24T00:00:00Z');self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(len(r['retainedObservationConflicts']),1)
 def test_retraction_releases_observation_reservation(self):
  old=self.append(copy.deepcopy(self.a));g=self.other();g['binding']['value']='E9';self.seal(g);p.validate_set([old,g],self.policy)
 def test_active_observation_conflict_still_rejected(self):
  g=self.other();g['binding']['value']='E9';self.seal(g)
  with self.assertRaisesRegex(p.Invalid,'active asserted assignment'):p.validate_set([self.a,g],self.policy)
 def test_dispute_prior_must_be_effective_at_query(self):
  b=self.other();b['history'][1].update(effectiveAt='2025-06-01T00:00:00Z',recordedAt='2025-06-02T00:00:00Z');self.seal(b);self.append(b,'disputed','2025-07-01T00:00:00Z','2025-02-01T00:00:00Z')
  r=self.query([self.a,b],valid_at='2025-03-01T00:00:00Z',known_at='2025-08-01T00:00:00Z');self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['candidateDisputes'],[b['id']])
 def test_space_in_subject_uri_rejected_by_format(self):
  self.a['target']['id']='urn:synthetic:subject:person:p1 extra'
  with self.assertRaisesRegex(p.Invalid,'SCHEMA'):p.validate(self.a,self.policy)
 def test_nonascii_separator_in_uri_rejected_by_format(self):
  self.a['target']['id']='urn:synthetic:subject:person:p1'+chr(0xff0f)+'p2'
  with self.assertRaisesRegex(p.Invalid,'SCHEMA'):p.validate(self.a,self.policy)
 def test_resealed_endpoint_change_rejected_at_import(self):
  a=self.append(copy.deepcopy(self.a));a['target']['id']='urn:synthetic:subject:person:p2';self.seal(a)
  with self.assertRaisesRegex(p.Invalid,'claim-bearing content changed'):p.import_assertion(self.rows,a,self.policy,now=a['history'][-1]['recordedAt'])


```
## Documentation clarification


`evaluation_at` is the caller-supplied trusted current clock, not an arbitrary simulated future knowledge boundary. The function enforces `known_at <= evaluation_at`; the caller authenticates the clock. Static validation and the CLI do not enforce live reception history. At second precision, live imports are globally serialized to one new transition per second in the retained input set. An inverse subject index is not supplied.

Assignment observation reservations are scoped to claims that reached asserted and are not retracted. Unasserted proposals cannot permanently squat a source occurrence. Retraction releases that reservation without erasing the old observation; `retainedObservationConflicts` reports conflicting carried content across the full input, including proposals/retractions. Source truth is still external. A dispute uses only prior events effective at the queried valid time. A disputed previously asserted negative can produce contested even without a positive claim.

Integrity checks pin trusted local **source bytes**, not a hardened execution sandbox: Python import paths/bytecode and changes after verification remain part of the trusted environment. Loader parse/decode exceptions fail closed but are not all normalized to Invalid. Runtime schema integrity must be protected after installation. Source-referent namespaces, issuer qualification of assertion IDs, URI alias identity and complete parent endpoint admissibility remain external governance, not proven by string comparison.

## Source hashes
{"identity_profile.py":"bec1dcec0584c4dc8de2be4251366db2b4f56aa71d0f0e35ec11d29b3cdbd98f","identity-profile.schema.json":"d5dbab037ea7af7f5b9feef95929f461380d824849caad092af7ea1706cc54c7","test_identity.py":"cbfe56c1fc588a25500471d3524597ff500df8315887fc98b278f509efe1d698","acceptance.py":"dbd411081247b3d5bbb4661a3cb9616665ae8e3a5826642a00dc578095b3fd3c","README.md":"fe39b1c05572b3d835b0fc5ce7bd8bb6a2d8975e8dd2aeba98d1b08901964bd6","model-spec.md":"2cf9808893dfbf33e36d960e04fbc1ff0b1308b27d27f49187b1851fad875163"}
## Local reports
{"executedAt":"2026-09-21T17:18:00.054381+00:00","sourceDigests":{"identity_profile.py":"bec1dcec0584c4dc8de2be4251366db2b4f56aa71d0f0e35ec11d29b3cdbd98f","identity-profile.schema.json":"d5dbab037ea7af7f5b9feef95929f461380d824849caad092af7ea1706cc54c7","test_identity.py":"cbfe56c1fc588a25500471d3524597ff500df8315887fc98b278f509efe1d698","examples\\ai-team.json":"1b945c084570d40e97214c68e519731f0bce2baeb2675c34b203fc4d23ebde14","examples\\group.json":"04860545cf61f6d5bdd18a5a8e00294982e7477496196ae84e66825f4d127157","examples\\policy.json":"4062926e1a81fd95ae027b6f16e7acdc6864b3e2c812cbaf0fb8f60edc80b707","examples\\startup.json":"da6cef738511c163fc8b5e1622ede24020339ffa97965540c1a87df4c118a3af"},"tests":87,"passed":true,"failures":0,"errors":0}
{"format":"vercy-identity-profile-acceptance","executedAt":"2026-09-21T17:18:02Z","passed":3,"failed":0,"profiles":[{"profile":"startup","objects":3,"facts":3,"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"roundTripEqualsInput":true,"companion":"Explicitly called on actual stored snapshots; not automatically enforced by native V3","invalidNestedSnapshot":{"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"companionRejected":true},"installedValidatorDigest":"sha256:bec1dcec0584c4dc8de2be4251366db2b4f56aa71d0f0e35ec11d29b3cdbd98f","pins":[{"id":"vr.wm-xct-011","version":"0.3.0-research.1","digest":"sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834","mode":"semantic-only"},{"id":"vr.wm-xct-036","version":"0.3.0-research.1","digest":"sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17","mode":"native-binding"}]},{"profile":"group","objects":3,"facts":3,"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"roundTripEqualsInput":true,"companion":"Explicitly called on actual stored snapshots; not automatically enforced by native V3","invalidNestedSnapshot":{"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":3,"facts":3,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"companionRejected":true},"installedValidatorDigest":"sha256:bec1dcec0584c4dc8de2be4251366db2b4f56aa71d0f0e35ec11d29b3cdbd98f","pins":[{"id":"vr.wm-xct-011","version":"0.3.0-research.1","digest":"sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834","mode":"semantic-only"},{"id":"vr.wm-xct-036","version":"0.3.0-research.1","digest":"sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17","mode":"native-binding"}]},{"profile":"ai-team","objects":2,"facts":2,"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":2,"facts":2,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"roundTripEqualsInput":true,"companion":"Explicitly called on actual stored snapshots; not automatically enforced by native V3","invalidNestedSnapshot":{"native":{"valid":true,"conformanceLevel":"V3","schemas":"https://ver.cy/schemas/dimension/1.0/","counts":{"objects":2,"facts":2,"relations":0,"events":0},"errors":[],"warnings":[],"scope":"executable structure and record semantics; does not certify external truth, legal authority, or safety"},"companionRejected":true},"installedValidatorDigest":"sha256:bec1dcec0584c4dc8de2be4251366db2b4f56aa71d0f0e35ec11d29b3cdbd98f","pins":[{"id":"vr.wm-xct-011","version":"0.3.0-research.1","digest":"sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834","mode":"semantic-only"},{"id":"vr.wm-xct-036","version":"0.3.0-research.1","digest":"sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17","mode":"native-binding"}]}],"sourceDigests":{"acceptance.py":"dbd411081247b3d5bbb4661a3cb9616665ae8e3a5826642a00dc578095b3fd3c","identity_profile.py":"bec1dcec0584c4dc8de2be4251366db2b4f56aa71d0f0e35ec11d29b3cdbd98f","identity-profile.schema.json":"d5dbab037ea7af7f5b9feef95929f461380d824849caad092af7ea1706cc54c7","tool-pins.json":"9c664506473f41b3ebc23376caa28fd7e323c0158db7c1a6676ad3dbc8afc434","examples\\ai-team.json":"1b945c084570d40e97214c68e519731f0bce2baeb2675c34b203fc4d23ebde14","examples\\group.json":"04860545cf61f6d5bdd18a5a8e00294982e7477496196ae84e66825f4d127157","examples\\policy.json":"4062926e1a81fd95ae027b6f16e7acdc6864b3e2c812cbaf0fb8f60edc80b707","examples\\startup.json":"da6cef738511c163fc8b5e1622ede24020339ffa97965540c1a87df4c118a3af"},"limits":"Synthetic new-Dimension assertion snapshots only. Upstream subjects, account ownership, IAM, source truth and existing-Dimension migrations are not tested."}