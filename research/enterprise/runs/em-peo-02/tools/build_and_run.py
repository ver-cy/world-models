import csv,hashlib,json,subprocess
from pathlib import Path
import yaml
W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");R=W/'research/enterprise/runs/em-peo-02';IDS={'WM-ORG-005','WM-PER-001','WM-ORG-016'}
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def proj(p):
 raw=p.read_bytes();d=yaml.safe_load(raw.decode());fs=[]
 for b in d['structure']['bundles']:
  for l in b['layers']:
   for f in l['findings']:
    fs.append({'id':f['id'],'name':f['name'],'description':f['description'],'data_elements':[{k:e.get(k) for k in ('id','name','description','value_kind','cardinality','required')} for e in f.get('data_elements',[])]})
 return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'publication':d['publication'],'model':d['model'],'findings':fs,'functions':[{k:x.get(k) for k in ('id','name','description')} for x in d['functions']],'composition':d['composition'],'adjudication':d['researchAdjudication'],'statistics':d['statistics']}
reg=j(W/'research/enterprise/registry.json');q=j(W/'research/enterprise/queue.json');u=rows(W/'planning/VERCY-UNIFIED-MEGA-REGISTRY.csv');rel=rows(W/'planning/VERCY-MODEL-RELATIONS.csv')
d={'contour':next(x for x in reg['units'] if x['id']=='EM-PEO-02'),'queue':next(x for x in q['units'] if x['id']=='EM-PEO-02'),'reservations':[x for x in u if x.get('model_id') in IDS],'relations':[x for x in rel if x.get('source_model_id') in IDS or x.get('target_model_id') in IDS],'specs':{'WM-ORG-005':proj(W/'publications/wm-org-005-employment/spec.yaml'),'WM-PER-001':proj(W/'publications/wm-per-001-person/spec.yaml'),'WM-ORG-016':proj(W/'publications/wm-org-016-work-assignment/spec.yaml')},'limits':['All are non-canonical reviewable drafts; complete specs parsed and pinned; registry relations/v1 fields non-normative.']}
R.mkdir(parents=True,exist_ok=True);D=R/'provider-dossier.json';D.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p="""Independent enterprise metamodel review. Use only dossier, no tools/browsing/invented IDs. Decide EM-PEO-02 Work Relations and Assignments over WM-ORG-005 Employment, WM-PER-001 Person, WM-ORG-016 Work Assignment. Choose reuse/profile/complete reserved/unassigned candidate only with independent identity/lifecycle. Separate employer, work customer and staffing supplier; employee, contractor, agency worker; person anchor, employment/engagement relationship, employer-scoped EmployeeProfile, position/work assignment, lifecycle event, and JoinerMoverLeaver case. Test rehire and concurrent relations. State when a new relation is needed versus assignment version. Employee number scoped to employer. Offboarding starts access verification; it never proves revocation. Walk freelancer misclassified as employee and HR card closure falsely treated as access revocation. Acceptance: dual employment, agency labor, rehire after termination, incomplete offboarding with preserved history. Return <=1200 words headings Verdict; Evidence; Identity/mastership; Relationship kinds/parties; Employee profile and numbering; Assignment/versioning; JML/access boundary; Invariants; Scenarios; Profile shape; Holds. No canonical/installability claims.\n\nDOSSIER\n"""+D.read_text(encoding='utf-8')
x=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=p,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if x.returncode:raise SystemExit(x.stderr)
(R/'claude-study.raw.md').write_text(x.stdout.rstrip()+'\n',encoding='utf-8');print(D.stat().st_size,len(x.stdout))
