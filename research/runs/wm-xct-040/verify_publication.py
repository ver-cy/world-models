from pathlib import Path,PurePosixPath
from urllib.request import urlopen,Request
from concurrent.futures import ThreadPoolExecutor
import argparse,datetime,hashlib,json,sys,subprocess,zipfile,io,tempfile

def main():
 p=argparse.ArgumentParser();p.add_argument('--site',type=Path,required=True);p.add_argument('--skill',type=Path,required=True);p.add_argument('--report',type=Path,required=True);a=p.parse_args()
 base='https://ver.cy/models/wm-xct-040-model-composition-resolution/';local=a.site/'models/wm-xct-040-model-composition-resolution';checks=[]
 def get(url):
  with urlopen(url,timeout=40) as r:assert r.status==200;return r.read()
 def check(name,yes):
  assert yes,name;checks.append({'check':name,'passed':True})
 for n in ['spec.yaml','AGENTS.md','index.html','publication.json','package-0.1.0.zip','package-checksums.json']:
  check('public byte identity '+n,get(base+n)==(local/n).read_bytes())
 manifest=json.loads(get(base+'package-checksums.json'))
 def asset(pair):
  n,h=pair;raw=get(base+'versions/0.1.0/'+n);return n,hashlib.sha256(raw).hexdigest()==h
 with ThreadPoolExecutor(max_workers=6) as pool:
  for n,ok in pool.map(asset,manifest.items()):check('immutable version asset '+n,ok)
 spec_digest='sha256:'+hashlib.sha256(get(base+'spec.yaml')).hexdigest()
 index=json.loads(get('https://ver.cy/models/runtime-index.json'));model=next(m for m in index['models'] if m['id']=='vr.wm-xct-040')
 check('runtime exact version and digest',model['version']=='0.1.0' and model['digest']==spec_digest and model['installable'] and model['status']=='published' and model['requires']==[])
 search=json.loads(get('https://ver.cy/api/v1/models/search/?q=WM-XCT-040'))
 check('catalogue search exact ID',any(x['id']=='vr.wm-xct-040' for x in search['matches']))
 req=Request('https://ver.cy/api/v1/models/resolve/',data=json.dumps({'query':'WM-XCT-040','client':{'agent':'composition-publication-verifier','version':'1'}}).encode(),headers={'Content-Type':'application/json'})
 resolved=json.loads(get(req));check('resolver exact published model',resolved['status']=='resolved' and resolved['resolution']['id']=='vr.wm-xct-040')
 evidence='https://ver.cy/enterprise/research/wm-xct-040/';em=json.loads(get(evidence+'evidence-checksums.json'))
 with ThreadPoolExecutor(max_workers=6) as pool:
  for n,ok in pool.map(lambda pair:(pair[0],hashlib.sha256(get(evidence+pair[0])).hexdigest()==pair[1]),em.items()):check('evidence '+n,ok)
 with tempfile.TemporaryDirectory(prefix='vercy-published-composition-') as tmp:
  target=Path(tmp)
  with zipfile.ZipFile(io.BytesIO(get(base+'package-0.1.0.zip'))) as z:
   for info in z.infolist():
    q=PurePosixPath(info.filename);assert not q.is_absolute() and '..' not in q.parts and ':' not in info.filename and '\\' not in info.filename
    dest=target.joinpath(*q.parts);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(info))
  for n,h in json.loads((target/'package-checksums.json').read_text(encoding='utf-8')).items():assert hashlib.sha256((target/n).read_bytes()).hexdigest()==h
  for cmd in [[sys.executable,str(target/'test_composition.py')],[sys.executable,str(target/'acceptance.py'),'--skill',str(a.skill),'--report',str(target/'downloaded-acceptance.json')]]:
   result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8');assert result.returncode==0,result.stderr+result.stdout
  unit=json.loads((target/'test-results.json').read_text(encoding='utf-8'));native=json.loads((target/'downloaded-acceptance.json').read_text(encoding='utf-8'))
  check('downloaded package tests and native acceptance',unit['passed'] and native['passed']==3 and native['failed']==0)
 report={'modelId':'WM-XCT-040','version':'0.1.0','verifiedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'specDigest':spec_digest,'checks':checks,'publicZipUnitTests':unit,'publicZipNativeAcceptance':native,'status':'published-and-verified','limitations':'Reference commercial-company bootstrap only, semantic-only models remain separate, no existing-Dimension migration, no universal domain conformance.'}
 a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'checks':len(checks),'status':report['status'],'specDigest':spec_digest}))
if __name__=='__main__':main()
