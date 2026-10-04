import csv, hashlib, json
from pathlib import Path
import yaml
WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models"); OUT=WORLD/'research/enterprise/runs/em-org-04/provider-dossier.json'
SELECT={'unit-identifier-scheme','unit-naming-and-designation','unit-kind-classification','unit-existence-status','collaboration-vs-unit-typing','parent-child-containment','concurrent-hierarchies','reporting-lines','cross-unit-affiliations','unit-mandate-scope','delegated-authority-limits','accountable-role','segregation-of-duties','reorganization-act','unit-lineage','effective-dating-bitemporality','as-of-reconstruction','record-authority','evidence-and-validation','projection-fidelity'}
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def main():
 p=WORLD/'publications/wm-org-002-organizational-unit/spec.yaml';raw=p.read_bytes();d=yaml.safe_load(raw.decode('utf-8'));findings=[];idx=[]
 for b in d['structure']['bundles']:
  ls=[]
  for l in b['layers']:
   ls.append({k:l.get(k) for k in ('id','name','description')})
   for f in l['findings']:
    if f['id'] in SELECT:findings.append({'bundle':b['id'],'layer':l['id'],'finding':{'id':f['id'],'name':f['name'],'description':f['description'],'source_refs':f.get('source_refs'),'questions':[q.get('text') for q in f.get('questions',[])],'data_elements':[{k:e.get(k) for k in ('id','name','description','value_kind','cardinality','required')} for e in f.get('data_elements',[])]}})
  idx.append({'id':b['id'],'name':b['name'],'description':b.get('description'),'layers':ls})
 reg=j(WORLD/'research/enterprise/registry.json');q=j(WORLD/'research/enterprise/queue.json');u=rows(WORLD/'planning/VERCY-UNIFIED-MEGA-REGISTRY.csv');rel=rows(WORLD/'planning/VERCY-MODEL-RELATIONS.csv')
 dossier={'contour':next(x for x in reg['units'] if x['id']=='EM-ORG-04'),'queue_reservation':next(x for x in q['units'] if x['id']=='EM-ORG-04'),'registry_reservation':next(x for x in u if x.get('model_id')=='WM-ORG-002'),'relationship_ledger':[x for x in rel if x.get('source_model_id')=='WM-ORG-002' or x.get('target_model_id')=='WM-ORG-002'],'current_spec':{'source_file':p.relative_to(WORLD).as_posix(),'source_bytes':len(raw),'source_sha256':hashlib.sha256(raw).hexdigest(),'publication':d['publication'],'metaModel':d['metaModel'],'model':d['model'],'structure_index':idx,'selected_findings':findings,'functions':[{k:f.get(k) for k in ('id','name','description')} for f in d['functions']],'composition':d['composition'],'researchAdjudication':d['researchAdjudication'],'statistics':d['statistics']},'evidence_limits':['The current publication is reviewable-draft and publishableCanonical false.','Complete spec parsed and pinned by digest; selected findings form the compact reviewer projection.','Enterprise v1 fields and registry relations are non-normative.']}
 OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(OUT);print(OUT.stat().st_size)
if __name__=='__main__':main()
