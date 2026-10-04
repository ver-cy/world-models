from pathlib import Path
import copy,json,sys,hashlib,datetime
W=Path(__file__).parent;P=W/'implementation';sys.path.insert(0,str(P))
import disclosure as d
from test_disclosure import fixture,p
from acceptance import native_pair,MASTER,WRITER
base,review,snapshot,cap=fixture();checks=[]
def proposal(padding):
 x=copy.deepcopy(base);x['body']['members'][0]['fields']=[{'name':'field'+str(i),'kind':'string','classificationBindings':[p('classification'+str(j)+'x'*padding) for j in range(8)]} for i in range(64)]
 return d.seal(x)
def reject(label,fn,expected):
 try:fn()
 except d.Invalid as e:
  assert str(e)==expected,(label,str(e));checks.append({'case':label,'observed':'rejected','reason':str(e)})
 else:raise AssertionError(label+' was accepted')
lo,hi=0,470
while lo<hi:
 mid=(lo+hi+1)//2
 try:proposal(mid);lo=mid
 except d.Invalid as e:
  assert str(e)=='size';hi=mid-1
near=proposal(lo);size=len(d.canonical(near));assert d.MAX_BYTES-size<512
assert d.import_records([],[near],near['dimension'],cap)==[near]
obj,fact=native_pair(near,'2026-09-21T12:00:00Z')
reject('near-cap record imports but native envelope exceeds independent cap',lambda:d.validate_native(fact,obj,dimension=near['dimension'],capability=cap,now='2026-09-21T12:00:00Z',master=MASTER,writer=WRITER),'size')
sn=copy.deepcopy(snapshot);sn['proposal']=d.pin(near);sn['members']=near['body']['members'];sn['activeReviews']=[]
sn['reviewers']=['urn:synthetic:reviewer:'+str(i)+'x'*470 for i in range(64)]
reject('near-cap record and larger actor catalogue exceed snapshot cap',lambda:d.inspect(near,[],sn,cap,sn['asOf']),'size')
small=proposal(80);obj,fact=native_pair(small,'2026-09-21T12:00:00Z');assert d.validate_native(fact,obj,dimension=small['dimension'],capability=cap,now='2026-09-21T12:00:00Z',master=MASTER,writer=WRITER)==small
sn['proposal']=d.pin(small);sn['members']=small['body']['members'];assert d.inspect(small,[],sn,cap,sn['asOf'])['status']=='insufficient-context'
checks.append({'case':'smaller record with same expanded actor catalogue supports envelope and snapshot preflight','observed':'passed','recordBytes':len(d.canonical(small))})
sw=copy.deepcopy(snapshot);sw['withdrawnReviews']=[p('withdrawn'),p('withdrawn')];sw['withdrawnReviews'][1]['digest']='sha256:'+'0'*64
reject('conflicting withdrawn revision',lambda:d.inspect(base,[review],sw,cap,sw['asOf']),'conflicting withdrawn revision')
reject('register >128',lambda:d.import_records([],[base]*129,base['dimension'],cap),'record bounds')
reject('active supplied reviews >64',lambda:d.inspect(base,[review]*65,snapshot,cap,snapshot['asOf']),'review set')
badproposal=d.seal(dict(base,dimension='urn:synthetic:other'))
reject('proposal Dimension mismatch',lambda:d.inspect(badproposal,[review],snapshot,cap,snapshot['asOf']),'proposal scope')
report={'status':'passed','executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Post-audit Codex supplement; external providers did not review or execute this script. Existing release code unchanged. Documents a fails-closed capacity limit, not a capacity fix.','codeSha256':hashlib.sha256((P/'disclosure.py').read_bytes()).hexdigest(),'nearCapRecordBytes':size,'perValueCap':d.MAX_BYTES,'checks':checks}
(W/'post-audit-boundary-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(report))
