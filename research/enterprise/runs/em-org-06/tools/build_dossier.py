import csv,hashlib,json
from pathlib import Path
import yaml
W=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");O=W/'research/enterprise/runs/em-org-06/provider-dossier.json';IDS={'WM-ORG-004','WM-XCT-023'}
SEL={'position-identifier-and-keys','assigned-duties-and-responsibilities','occupational-classification','grade-level-and-job-evaluation','unit-and-cost-center-placement','capacity-fte-and-schedule','vacancy-and-occupancy-state','budget-and-funding-source','delegated-authority-and-decision-rights','prescribed-regulatory-responsibilities','position-lifecycle-states','effective-dated-change-and-history','abstract-role-binding','role-assertion-reification','assertion-identifier-and-sameness','role-type-and-axes','host-kind-and-reference','scope-cascade-and-derivation','player-kind-and-vacancy','role-validity-period','role-status-lifecycle','basis-of-authority','delegation-and-on-behalf-of','representation-and-limits','role-multiplicity','segregation-and-conflict','participation-vs-standing-role'}
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def proj(p):
 raw=p.read_bytes();d=yaml.safe_load(raw.decode());fs=[];idx=[]
 for b in d['structure']['bundles']:
  ls=[]
  for l in b['layers']:
   ls.append({k:l.get(k) for k in ('id','name','description')})
   for f in l['findings']:
    if f['id'] in SEL:fs.append({'bundle':b['id'],'layer':l['id'],'finding':{'id':f['id'],'name':f['name'],'description':f['description'],'questions':[q.get('text') for q in f.get('questions',[])],'data_elements':[{k:e.get(k) for k in ('id','name','description','value_kind','cardinality','required')} for e in f.get('data_elements',[])]}})
  idx.append({'id':b['id'],'name':b['name'],'layers':ls})
 return {'source_file':p.relative_to(W).as_posix(),'source_bytes':len(raw),'source_sha256':hashlib.sha256(raw).hexdigest(),'publication':d['publication'],'model':d['model'],'structure_index':idx,'selected_findings':fs,'functions':[{k:f.get(k) for k in ('id','name','description')} for f in d['functions']],'composition':d['composition'],'researchAdjudication':d['researchAdjudication'],'statistics':d['statistics']}
def main():
 reg=j(W/'research/enterprise/registry.json');q=j(W/'research/enterprise/queue.json');u=rows(W/'planning/VERCY-UNIFIED-MEGA-REGISTRY.csv');rel=rows(W/'planning/VERCY-MODEL-RELATIONS.csv')
 d={'contour':next(x for x in reg['units'] if x['id']=='EM-ORG-06'),'queue_reservation':next(x for x in q['units'] if x['id']=='EM-ORG-06'),'registry_reservations':[x for x in u if x.get('model_id') in IDS],'relationship_ledger':[x for x in rel if x.get('source_model_id') in IDS or x.get('target_model_id') in IDS],'current_specs':{'WM-ORG-004':proj(W/'publications/wm-org-004-position/spec.yaml'),'WM-XCT-023':proj(W/'publications/wm-xct-023-party-role/spec.yaml')},'evidence_limits':['Both are non-canonical reviewable drafts.','Complete specs parsed and pinned; selected findings are a compact projection.','Registry relations and v1 fields are non-normative.']}
 O.parent.mkdir(parents=True,exist_ok=True);O.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(O);print(O.stat().st_size)
if __name__=='__main__':main()
