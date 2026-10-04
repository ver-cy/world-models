from pathlib import Path
import sys,json,tempfile
W=Path(__file__).parent;sys.path.insert(0,str(W/'sync-audit-r3-candidate'))
from fixtures import *
from sync_register import assess_rounds,decode,encode,digest
with tempfile.TemporaryDirectory() as tmp:
    h=Harness(Path(tmp)/'h1.sqlite');r1='urn:synthetic:round:1';r2='urn:synthetic:round:2'
    h.round(r1,['a','b']);h.call('round-open',{'id':r2,'scopeId':SCOPE,'epochId':EPOCH,'purpose':PURPOSE,'consistency':'source-snapshot','consistencyEvidence':evidence('snapshot'),'visibilityCovered':True,'previousRoundId':r1,'notEarlierEvidence':evidence('order')})
    commit=h.commit(h.batch('empty',[],round_id=r2,page=0,terminal=True),OTHER);seal=h.call('round-seal',{'id':r2,'errors':[]},OTHER)
    result={'H1':{'intakeOnlyCommit':commit,'intakeOnlySeal':seal,'assessment':assess_rounds(h.archive(),r1,r2)}};h.close()
    h=Harness(Path(tmp)/'m1.sqlite');h.round(r1,['a'])
    keys=sorted(('candidate-'+str(i) for i in range(20)),key=lambda x:digest([SCOPE,EPOCH,x]),reverse=True)
    h.commit(h.batch(keys[0],[item('a',operation='source-deleted')]))
    h.commit(h.batch(keys[-1],[item('a',operation='inaccessible')]))
    h.round(r2,[],r1);a=h.archive()
    result['M1']={'before':assess_rounds(a,r1,r2),'afterCanonicalRoundTrip':assess_rounds(decode(encode(a)),r1,r2)};h.close()
result['H1']['reproduced']=len(result['H1']['assessment']['candidates'])==2
result['M1']['reproduced']=result['M1']['before']!=result['M1']['afterCanonicalRoundTrip']
(W/'r3-reproductions.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v['reproduced'] for k,v in result.items()}))
