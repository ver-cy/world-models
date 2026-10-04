"""Internal consistency of complete fixture snapshots; not authenticated admission.

A coherent old or fabricated snapshot can pass. Trusted latest export/continuity
roots, authentication, authority verification and disclosure remain host duties.
"""
import re
from bisect import bisect_right
from action import Refused, require, validate, digest, encoded, parse, matching_rules, definition_ref, Executor, MAX_ROWS

def fields(value,names):
    require(type(value) is dict and set(value)==set(names.split()),'snapshot-fields')

def integer(value,minimum=0): require(type(value) is int and minimum<=value<=9007199254740991,'snapshot-integer')

def validate_snapshot(s):
    try: return _validate(s)
    except (KeyError,TypeError,IndexError,ValueError,AttributeError,OverflowError,RecursionError) as e:
        if isinstance(e,Refused): raise
        raise Refused('snapshot-malformed') from None

def _validate(s):
    fields(s,'format meta definitions policies resources requests events')
    for name in ('definitions','policies','resources','requests','events'):
        require(type(s[name]) is list and len(s[name])<=MAX_ROWS,'snapshot-list-bounds')
    require(s['format']=='enterprise-action-snapshot/0.1.0','snapshot-version')
    m=s['meta']; fields(m,'id dimension issuer epoch clock policy_revision control_sequence')
    require(m['id']==1 and type(m['id']) is int,'snapshot-meta')
    Executor._time(m['clock']); integer(m['policy_revision']); integer(m['control_sequence'])
    for k in ('dimension','issuer','epoch'):
        require(type(m[k]) is str and re.fullmatch('[A-Za-z0-9][A-Za-z0-9._:-]{2,127}',m[k]) is not None,'snapshot-id')
    definitions={}; ordinals=[]
    for row in s['definitions']:
        fields(row,'id version body digest available recorded_at control_sequence retired_sequence ordinal')
        d=validate('ActionDefinition',parse(row['body'])); pin=definition_ref(d)
        require(row['id']==d['definitionId'] and row['version']==d['version'] and row['digest']==pin['sha256'],'definition-digest')
        integer(row['ordinal'],1); integer(row['control_sequence'],1); Executor._time(row['recorded_at'])
        require(row['recorded_at']<=m['clock'] and row['control_sequence']<=m['control_sequence'],'definition-future')
        retired=row['retired_sequence']
        if retired is not None:
            integer(retired,1); require(row['control_sequence']<retired<=m['control_sequence'],'retirement-sequence')
        require(type(row['available']) is int and row['available']==int(retired is None),'definition-availability')
        key=(d['definitionId'],d['version']); require(key not in definitions,'definition-duplicate')
        definitions[key]=(d,row); ordinals.append(row['ordinal'])
    require(ordinals==list(range(1,len(ordinals)+1)),'definition-order')
    policies={}; previous_control=-1; previous_time=0
    for row in s['policies']:
        fields(row,'revision body recorded_at control_sequence')
        integer(row['revision']); integer(row['control_sequence']); Executor._time(row['recorded_at'])
        require(row['revision']==len(policies) and previous_control<row['control_sequence']<=m['control_sequence'],'policy-order')
        require(previous_time<=row['recorded_at']<=m['clock'],'policy-time')
        policies[row['revision']]=(validate('Policy',parse(row['body'])),row)
        previous_control=row['control_sequence']; previous_time=row['recorded_at']
    require(policies and m['policy_revision']==len(policies)-1 and policies[0][0]==[] and policies[0][1]['control_sequence']==0,'policy-root')
    if len(policies)==MAX_ROWS: require(policies[MAX_ROWS-1][0]==[],'policy-revocation-reserve')
    policy_controls=[row['control_sequence'] for _,row in policies.values()]
    def current_policy(e):
        rev=bisect_right(policy_controls,e['controlSequence'])-1; policy,row=policies[rev]
        require(row['recorded_at']<=e['recordedAt'],'policy-future'); return rev,policy
    def definition_at(intent,e):
        pin=intent['definition']; d,row=definitions[(pin['definitionId'],pin['version'])]
        require(definition_ref(d)==pin and row['control_sequence']<=e['controlSequence'] and row['recorded_at']<=e['recordedAt'],'definition-pin')
        available=(row['retired_sequence'] is None or e['controlSequence']<row['retired_sequence']) and d['validFrom']<=e['recordedAt']<d['validUntil']
        return d,available
    requests={}; slots=set()
    for r in s['requests']:
        validate('ActionRequestSnapshot',r); i=r['intent']
        require(r['requestId'] not in requests and r['keyHash'] not in slots,'request-identity')
        require(i['dimensionId']==m['dimension'] and digest(i)==r['intentDigest'],'intent-digest')
        require(r['submittedAt']<=m['clock'],'request-future')
        requests[r['requestId']]=r; slots.add(r['keyHash'])
    resource_rows={}; live={}; expected_resources=[]
    for row in s['resources']:
        fields(row,'id revision labels recorded_at control_sequence')
        require(type(row['id']) is str and re.fullmatch('[A-Za-z0-9][A-Za-z0-9._:-]{2,127}',row['id']) is not None,'resource-id')
        integer(row['revision']); Executor._time(row['recorded_at']); validate('Labels',parse(row['labels']))
        integer(row['control_sequence'],1); require(row['control_sequence']<=m['control_sequence'],'resource-control-sequence')
        key=(row['id'],row['revision']); require(key not in resource_rows,'resource-duplicate'); resource_rows[key]=row
        require(row['recorded_at']<=m['clock'],'resource-future')
        if row['revision']==0:
            live[row['id']]=row; expected_resources.append(row)
    definition_ids={key[0] for key in definitions}
    resource_ids={key[0] for key in resource_rows}
    require(not definition_ids & resource_ids and not set(requests) & (definition_ids|resource_ids),'object-kind-collision')
    object_ids=set(requests)|definition_ids|resource_ids
    # Each host transaction is one complete operation. Empty control-sequence
    # gaps are reads/snapshots/refusals; retained fragments cannot form an operation.
    groups={}
    for e in s['events']:
        validate('Event',e)
        groups.setdefault(e['controlSequence'],[]).append(e)
    for group in groups.values():
        first=group[0]
        require(all((e['requestId'],e['recordedAt'],e['issuerId'])==(first['requestId'],first['recordedAt'],first['issuerId']) for e in group),'operation-context')
        kinds=[e['kind'] for e in group]
        base=kinds[1:] if kinds[0]=='submission' else kinds
        require(base,'operation-shape')
        if base==['key-retirement']: require(kinds==base,'operation-shape')
        elif base[0]=='delivery': require(base in (['delivery','try'],['delivery','try','receipt'],['delivery','try','disposition']),'operation-shape')
        else: require(kinds==base and base in (['try'],['try','disposition'],['try','observation']),'operation-shape')
    # Admin mutations and operation groups cannot share a transaction identity.
    controls=set(groups)
    admin=[]
    for _,row in definitions.values():
        admin.append(row['control_sequence'])
        if row['retired_sequence'] is not None: admin.append(row['retired_sequence'])
    admin += [row['control_sequence'] for _,row in policies.values()]
    admin += [row['control_sequence'] for row in s['resources'] if row['revision']==0]
    require(len(set(admin))==len(admin) and not controls & set(admin),'control-operation-collision')
    seen={}; states={}; receipts={}; retired=set(); corrected=set(); last_time=0; last_control=0; used_trials=set()
    def precondition(intent,event):
        row=live.get(intent['resourceId'])
        valid=bool(row and row['revision']==intent['expectedRevision'] and row['control_sequence']<=event['controlSequence'] and row['recorded_at']<=event['recordedAt'])
        rid=intent['compensatesReceiptId']
        if rid:
            original=seen.get(rid)
            if not original or original['kind']!='receipt': return False
            old_i=requests[original['requestId']]['intent']; p=original['payload']
            valid=bool(valid and all(old_i[k]==intent[k] for k in ('actorId','principalId','purpose','audience','dimensionId')) and p['resourceId']==intent['resourceId'] and p['definition']==intent['definition'] and p['afterRevision']==intent['expectedRevision'] and p['beforeLabels']==intent['parameters']['labels'])
        return valid
    def trial_for(e,action,allowed=True):
        t=seen.get(e['payload']['tryEventId'])
        require(t and t['kind']=='try' and t['requestId']==e['requestId'] and t['controlSequence']==e['controlSequence'] and t['recordedAt']==e['recordedAt'],'trial-link')
        require(t['payload']['decision']['action']==action and (not allowed or t['payload']['decision']['allowed']),'trial-authority')
        require(t['eventId'] not in used_trials,'trial-reused'); used_trials.add(t['eventId'])
        return t
    for index,e in enumerate(s['events'],1):
        validate('Event',e); rid=e['requestId']; kind=e['kind']; p=e['payload']
        require(e['sequence']==index and e['eventId'] not in seen,'event-sequence')
        require(e['eventId'] not in object_ids,'event-object-collision')
        require(last_time<=e['recordedAt']<=m['clock'] and last_control<=e['controlSequence']<=m['control_sequence'],'event-order')
        last_time=e['recordedAt']; last_control=e['controlSequence']
        require(rid in requests and rid not in retired and e['issuerId']==m['issuer'],'event-context')
        r=requests[rid]; intent=r['intent']; now=e['recordedAt']
        require(now>=r['submittedAt'],'event-before-admission')
        rev,policy=current_policy(e); definition,available=definition_at(intent,e)
        if kind=='submission':
            require(rid not in states and e['eventId']==r['submissionEventId'] and now==r['submittedAt'],'submission-identity')
            require(p['intentDigest']==r['intentDigest'] and definition['mode']=='synthetic-executable' and intent['purpose'] in definition['purposes'],'submission-definition')
            require(matching_rules(policy,intent,'submit',now),'submission-permission'); states[rid]='pending'
        else:
            require(rid in states,'missing-submission')
            if kind=='delivery': require(p['intentDigest']==r['intentDigest'],'delivery-digest')
            elif kind=='try':
                d=p['decision']; matches=matching_rules(policy,intent,d['action'],now)
                require(d['policyRevision']==rev and d['matchedRuleDigests']==matches and d['definitionAvailable']==available,'decision-evidence')
                require(d['allowed']==bool(matches and (available if d['action']=='execute' else True)),'decision-outcome')
                if d['action']=='execute':
                    require(any(matching_rules(policy,intent,a,now) for a in ('submit','execute','read','cancel','observe')),'rightless-replay')
                    prev=s['events'][index-2] if index>=2 else None
                    require(prev and prev['kind']=='delivery' and prev['requestId']==rid and prev['controlSequence']==e['controlSequence'],'try-delivery')
                    tail=None
                    if states[rid]=='pending':
                        if now>=intent['expiresAt']: tail='disposition'
                        elif d['allowed']: tail='receipt' if precondition(intent,e) else 'disposition'
                    expected=['delivery','try']+([tail] if tail else [])
                    if groups[e['controlSequence']][0]['kind']=='submission': expected.insert(0,'submission')
                elif d['action']=='cancel':
                    require(d['allowed'] or matching_rules(policy,intent,'read',now),'unreadable-denied-cancel')
                    expected=['try']+(['disposition'] if d['allowed'] and states[rid]=='pending' else [])
                else:
                    require(d['allowed'],'observation-try-permission'); expected=['try','observation']
                require([x['kind'] for x in groups[e['controlSequence']]]==expected,'operation-incomplete')
            elif kind=='receipt':
                trial_for(e,'execute'); require(states[rid]=='pending' and now<intent['expiresAt'] and precondition(intent,e),'receipt-guard')
                row=live[intent['resourceId']]
                require(row['recorded_at']<=now,'resource-before-creation')
                expected={'definition':intent['definition'],'resourceId':intent['resourceId'],'beforeRevision':row['revision'],'afterRevision':row['revision']+1,'beforeLabels':parse(row['labels']),'afterLabels':intent['parameters']['labels'],'compensatesReceiptId':intent['compensatesReceiptId'],'tryEventId':p['tryEventId']}
                require(p==expected,'receipt-effect')
                row={'id':intent['resourceId'],'revision':p['afterRevision'],'labels':encoded(p['afterLabels']).decode('utf-8'),'recorded_at':now,'control_sequence':e['controlSequence']}
                live[row['id']]=row; expected_resources.append(row); receipts[rid]=e['eventId']; states[rid]='committed'
            elif kind=='disposition':
                require(states[rid]=='pending','terminal-rewrite')
                if p['to']=='cancelled':
                    trial_for(e,'cancel'); require(now<intent['expiresAt'] and p['reason']=='authorized-cancellation','cancel-guard')
                elif p['to']=='expired':
                    t=seen.get(p['tryEventId']); require(t and t['kind']=='try','expiry-try')
                    action=t['payload']['decision']['action']; require(action in ('cancel','execute'),'expiry-action')
                    trial_for(e,action,allowed=(action=='cancel'))
                    require(now>=intent['expiresAt'] and p['reason']=='deadline','expiry-guard')
                else:
                    trial_for(e,'execute'); require(now<intent['expiresAt'] and not precondition(intent,e),'rejection-guard')
                    require(p['reason']==('compensation-precondition' if intent['compensatesReceiptId'] else 'resource-revision'),'rejection-reason')
                states[rid]=p['to']
            elif kind=='observation':
                trial_for(e,'observe'); require(matching_rules(policy,intent,'read',now) and p['observerId']==intent['actorId'],'observation-rights')
                predecessor=p['correctsEventId']
                if predecessor:
                    old=seen.get(predecessor)
                    require(old and old['kind']=='observation' and old['requestId']==rid and old['payload']['observerId']==p['observerId'] and predecessor not in corrected,'correction-chain')
                    corrected.add(predecessor)
            elif kind=='key-retirement':
                require(states[rid]!='pending','pending-retirement'); retired.add(rid)
        seen[e['eventId']]=e
    require(set(states)==set(requests),'missing-history')
    for rid,r in requests.items():
        require(r['state']==states[rid] and r['receiptId']==receipts.get(rid) and r['keyRetired']==(rid in retired),'snapshot-lifecycle')
    require(sorted(expected_resources,key=lambda x:(x['id'],x['revision']))==s['resources'],'resource-history')
    return {'valid':True,'definitions':len(definitions),'requests':len(requests),'events':len(seen),'effects':len(receipts),
            'assurance':'internal-consistency-only-not-authenticity-or-latest-history'}
