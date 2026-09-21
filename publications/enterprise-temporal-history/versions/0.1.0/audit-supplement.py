from pathlib import Path
import copy,datetime,hashlib,json
import temporal as t
from test_temporal import TemporalTests,NOW
x=TemporalTests();x.setUp();a,b,c=x.snapshots();checks=[]
def rejected(label,fn,message):
    try:fn()
    except t.Invalid as e:assert str(e)==message,(label,str(e));checks.append(label)
    else:raise AssertionError(label)
bad=copy.deepcopy(c);bad['value']=copy.deepcopy(a['value']);bad['provenance']['snapshotDigest']=t.digest(bad['value'])
rejected('native exact-prefix branch after digest recomputation',lambda:x.snapshot(bad,b),'History rewritten/truncated')
future=copy.deepcopy(b);future.update(recordedAt='2026-12-31T00:00:00Z',validFrom='2026-12-31T00:00:00Z')
rejected('native forward receipt as current',lambda:x.snapshot(future,a),'Invalid snapshot receipt envelope')
rejected('native forward receipt as predecessor',lambda:x.snapshot(c,future),'Invalid snapshot receipt envelope')
report={'passed':len(checks),'checks':checks,'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'codeDigest':'sha256:'+hashlib.sha256(Path(t.__file__).read_bytes()).hexdigest(),'scope':'Codex post-audit supplemental checks; not independently reviewed'}
Path('audit-supplement-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
