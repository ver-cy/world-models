import csv,hashlib,json,subprocess
from pathlib import Path
import yaml
W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");R=W/'research/enterprise/runs/em-peo-01';P=W/'publications/wm-per-001-person/spec.yaml'
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
raw=P.read_bytes();d=yaml.safe_load(raw.decode());fs=[]
for b in d['structure']['bundles']:
 for l in b['layers']:
  for f in l['findings']:
   fs.append({'id':f['id'],'name':f['name'],'description':f['description'],'questions':[q.get('text') for q in f.get('questions',[])],'data_elements':[{k:e.get(k) for k in ('id','name','description','value_kind','cardinality','required')} for e in f.get('data_elements',[])]})
reg=j(W/'research/enterprise/registry.json');q=j(W/'research/enterprise/queue.json');u=rows(W/'planning/VERCY-UNIFIED-MEGA-REGISTRY.csv')
dossier={'contour':next(x for x in reg['units'] if x['id']=='EM-PEO-01'),'queue':next(x for x in q['units'] if x['id']=='EM-PEO-01'),'reservation':next(x for x in u if x.get('model_id')=='WM-PER-001'),'spec':{'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'publication':d['publication'],'model':d['model'],'findings':fs,'functions':[{k:x.get(k) for k in ('id','name','description')} for x in d['functions']],'composition':d['composition'],'adjudication':d['researchAdjudication'],'statistics':d['statistics']},'limits':['Non-canonical reviewable draft; complete spec parsed and pinned; registry/v1 mappings non-normative.']}
R.mkdir(parents=True,exist_ok=True);D=R/'provider-dossier.json';D.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
prompt="""Independent enterprise metamodel review. Use only dossier; no tools, browsing or invented IDs. Decide REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, or identifier-unassigned candidate for EM-PEO-01 Person and Contextual Identity over WM-PER-001. Test stable person identity versus names, contacts, local accounts, pseudonyms and identity evidence; prevent matching by display name/email alone; preserve name history; purpose-bound disclosure; employer/HRIS is not universal owner. Distinguish identity assertion, evidence artifact, contact point and account binding. Walk negative duplicate-name merge and acceptance with three systems, two namesakes and name change, where uncertain match remains proposal. Return <=1100 words: Verdict; Evidence; Boundary/mastership; Matching/linking contract; Names/contacts/pseudonyms; Privacy/disclosure; Invariants; Scenarios; Profile shape; Holds. No canonical/installability claims.\n\nDOSSIER\n"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode:raise SystemExit(r.stderr)
(R/'claude-study.raw.md').write_text(r.stdout.rstrip()+'\n',encoding='utf-8');print(D.stat().st_size,len(r.stdout))
