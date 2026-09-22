SAME FROZEN R3 SOURCE RECOVERY 7/9. Browser paragraph rendering adds blank separator lines; all nonempty lines and indentation are verified unchanged. These are static display fragments, not raw-byte hash verification.
Do not audit yet. Reply only ACK 7/9 if all code in this fragment is visible. No tools.
BEGIN action_bundle.py fragment 7/9
es and (available if d['action']=='execute' else True)),'decision-outcome')
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

# SOURCE: native.py
"""Deterministic post-commit native evidence, with a manifest written LAST."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib
import json
import re

def stamp(second): return datetime.fromtimestamp(second,timezone.utc).isoformat().replace('+00:00','Z')
def file_bytes(value): return json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False).encode('utf-8')+b'\n'
def sha(raw): return hashlib.sha256(raw).hexdigest()
def record_path(rid): return 'records/'+sha(rid.encode('utf-8'))+'.json'

def records(snapshot):
    validate_snapshot(snapshot)
    m=snapshot['meta']; result={}; previous={}; object_ids=set()
    request_by_id={r['requestId']:r for r in snapshot['requests']}
    provenance={'source':m['issuer'],'assurance':'synthetic-reference-only'}
    def obj(oid,rid,kind,name,time,facet,state='active'):
        record={'recordType':'object','schemaVersion':'1.0.0','recordId':rid,'objectId':oid,'objectType':kind,'name':name,
                'recordedAt':stamp(time),'previousRecordId':previous.get(oid),'state':state,'facets':facet,'provenance':provenance}
        require(rid not in result,'native-id-collision'); result[rid]=record; previous[oid]=rid; object_ids.add(oid)
    for row in snapshot['definitions']:
END fragment 7/9