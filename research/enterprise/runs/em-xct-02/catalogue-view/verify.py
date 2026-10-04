from pathlib import Path
from urllib.request import Request,urlopen
import datetime,hashlib,json,re,subprocess,sys,tempfile
W=Path(__file__).parent
R=Path('R:/02_PROJECTS/02_Meta_Models_Platforms/Ver.cy/current/ver-cy/world-models')
S=R.parent.parent/'ver.cy'
MID='vr.profile.enterprise-fact-authority'
checks=[]
def check(n,v):
    assert v,n
    checks.append({'check':n,'passed':True})
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(b):return 'sha256:'+hashlib.sha256(b).hexdigest()
def get(u):
    with urlopen(u,timeout=45) as res:
        assert res.status==200
        return res.read()
old={x['id']:x for x in load(W/'runtime-before.json')['models']}
current={x['id']:x for x in load(S/'models/runtime-index.json')['models']}
check('Exactly one explicit companion added',set(current)-set(old)=={MID} and not set(old)-set(current))
for mid,row in old.items():check('Unchanged previous runtime entry '+mid,row==current[mid])
m=current[MID]
check('Published own identity and installability',m['version']=='0.1.0' and m['status']=='published' and m['installable'])
check('EM-XCT-02 is a discoverable alias, not a fabricated WM ID','EM-XCT-02' in m['aliases'] and m['id']==MID)
check('No executable dependency on semantic-only parent',m['requires']==[] and m['relations']==[{'type':'aligned','target':'vr.wm-xct-001'}])
spec=get(m['specUrl'])
check('Original production specification exact digest',sha(spec)==m['digest'])
check('Original package exact release digest',sha(get(m['packageUrl']))=='sha256:558d5a1b459429dadb199a3ab9ec0fcef0f2c0fb32c38e0f77c50e6809ce3574')
root=S/'models/enterprise-fact-authority';v=load(root/'structure.json')
check('View pins actual normative specification',v['sourceSpecDigest']==m['digest'] and v['sourceSpecUrl']==m['specUrl'] and v['normative'] is False)
md=get(v['sourceDocumentUrl'])
check('View pins actual source document bytes',sha(md)==v['sourceDocumentDigest'])
qs={};fs=[]
for b in v['structure']['bundles']:
    for l in b['layers']:
        for f in l['findings']:
            fs.append(f)
            for q in f['questions']:qs[q['id']]=q
check('All 18 routes represented exactly once',sorted(qs)==[f'Q{i:02d}' for i in range(1,19)] and len(fs)==18 and len({f['id'] for f in fs})==18)
for line in md.decode().splitlines():
    if re.match(r'\| Q\d\d \|',line):
        q,fq,a,act=[s.strip() for s in line.strip('|').split('|')]
        fid,text=[s.strip() for s in fq.split('→',1)]
        f=next(f for f in fs if f['id']==fid)
        check('Exact question, artifact and guarded action '+q,qs[q]['text']==text and f['artifacts'][0]['name']==a and f['actions'][0]['description']==act and len(qs[q]['answer_data'])==2)
check('Six layers follow released structure',sum(len(b['layers']) for b in v['structure']['bundles'])==6 and len(v['structure']['bundles'])==4)
for file,digest in load(root/'view-manifest.json')['files'].items():check('View manifest '+file,sha((root/file).read_bytes())=='sha256:'+digest)

if '--live' not in sys.argv:
    # Reject corruption and path escape before any catalogue is written.
    original=load(root/'catalogue-entry.json')
    with tempfile.TemporaryDirectory(prefix='vercy-companion-catalogue-') as tmp:
        tmp=Path(tmp);models=tmp/'models';d=models/original['code'];d.mkdir(parents=True)
        for key in ['spec_url','agents_url']:
            dest=tmp/original[key].lstrip('/');dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes((S/original[key].lstrip('/')).read_bytes())
        for kind in ['digest','escape','identity','missing']:
            entry=dict(original)
            if kind=='digest':entry['spec_digest']='sha256:'+'0'*64
            if kind=='escape':entry['spec_url']='/models/../../outside.json'
            if kind=='identity':entry['registry_id']='vr.profile.wrong'
            if kind=='missing':entry['agents_url']='/models/missing/AGENTS.md'
            (d/'catalogue-entry.json').write_text(json.dumps(entry),encoding='utf-8')
            result=subprocess.run([sys.executable,str(S/'tools/build_bitrix_catalog_import.py'),'--models-root',str(models),'--output',str(tmp/'import.json')],capture_output=True,text=True)
            expected={'digest':'digest mismatch','escape':'unsafe companion','identity':'identity/version mismatch','missing':'unsafe companion'}[kind]
            check('Reject invalid companion '+kind,result.returncode!=0 and expected in result.stdout+result.stderr and not (tmp/'import.json').exists())
else:
    for file in ['index.html','structure.json','catalogue-entry.json','view-manifest.json']:
        check('Live exact view '+file,get('https://ver.cy/models/enterprise-fact-authority/'+file)==(root/file).read_bytes())
    live=json.loads(get('https://ver.cy/models/runtime-index.json'))
    check('Live runtime matches generated projection',live==load(S/'models/runtime-index.json'))
    for query in ['EM-XCT-02','Enterprise Fact Authority',MID]:
        from urllib.parse import quote
        search=json.loads(get('https://ver.cy/api/v1/models/search/?q='+quote(query)))
        check('Live search '+query,search['matches'][0]['id']==MID and search['matches'][0]['digest']==m['digest'])
    req=Request('https://ver.cy/api/v1/models/resolve/',data=json.dumps({'query':'EM-XCT-02','client':{'agent':'catalogue-view-verification','version':'1'}}).encode(),headers={'Content-Type':'application/json'})
    resolved=json.loads(get(req))
    check('Resolver returns own immutable companion',resolved['status']=='resolved' and resolved['resolution']['id']==MID and resolved['resolution']['digest']==m['digest'])
    body=get('https://ver.cy/models/?q=EM-XCT-02').decode()
    check('Main catalogue serves model card for contour search','href="/models/enterprise-fact-authority/"' in body and 'Enterprise Fact Authority' in body)
    brief=get('https://ver.cy/enterprise/models/em-xct-02/').decode()
    check('Enterprise brief links catalogue view','https://ver.cy/models/enterprise-fact-authority/' in brief)
out={'scope':'Catalogue registration and source-pinned navigation view; no semantic contract revision or new provider audit claimed.','verifiedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checksPassed':len(checks),'checks':checks,'model':m,'structure':v['statistics']}
name='live-verification.json' if '--live' in sys.argv else 'local-verification.json'
(W/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'report':name,'checksPassed':len(checks)}))
