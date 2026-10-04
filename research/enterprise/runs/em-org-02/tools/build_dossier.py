import csv, hashlib, json
from pathlib import Path
import yaml

WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT=WORLD/"research/enterprise/runs/em-org-02/provider-dossier.json"
IDS={"WM-ORG-001","WM-ORG-010","WM-ORG-011"}
SELECT={
"qualified-identifiers","canonical-key-selection","entity-resolution-and-duplicates","entity-legal-form","entity-category-and-personality","formation-act-and-creation-date","registry-entry-and-authority","entity-status-vs-registration-status","lifecycle-event-records","succession-and-continuity","dissolution-and-expiry","operating-sites-and-branches",
"register-anchored-legal-entity-identity","cross-scheme-identifier-alignment","legal-name-variants-and-name-history","entity-legal-form-and-jurisdiction-of-formation","legal-personality-and-capacity","registration-authority-identification","register-legal-effect","registration-act-dates-and-record-currency","registration-status-and-entity-status","legal-entity-event-record-and-effective-dating","succession-merger-division-and-conversion","dissolution-liquidation-and-restoration","branch-and-establishment-registration","redomiciliation-and-foreign-qualification","registration-evidence-documents-and-extracts","data-quality-discrepancies-and-challenge-process","provenance-source-attribution-and-observation-time",
"establishment-kind-record","operator-attachment-record","site-binding-record","presence-recognition-record","local-mandate-record","registration-evidence-record","presence-continuity-record","reporting-scope-record","presence-governance-record"}

def j(path): return json.loads(path.read_text(encoding='utf-8-sig'))
def rows(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def project(path):
 raw=path.read_bytes(); d=yaml.safe_load(raw.decode('utf-8')); findings=[]; index=[]
 for b in d['structure']['bundles']:
  ls=[]
  for l in b['layers']:
   ls.append({k:l.get(k) for k in ('id','name','description')})
   for f in l['findings']:
    if f['id'] in SELECT:
     findings.append({'bundle':b['id'],'layer':l['id'],'finding':{'id':f['id'],'name':f['name'],'description':f['description'],'source_refs':f.get('source_refs'),'questions':[q.get('text') for q in f.get('questions',[])],'data_elements':[{k:e.get(k) for k in ('id','name','description','value_kind','cardinality','required')} for e in f.get('data_elements',[])]}})
  index.append({'id':b['id'],'name':b['name'],'description':b.get('description'),'layers':ls})
 return {'source_file':path.relative_to(WORLD).as_posix(),'source_bytes':len(raw),'source_sha256':hashlib.sha256(raw).hexdigest(),'publication':d.get('publication'),'metaModel':d.get('metaModel'),'model':d.get('model'),'structure_index':index,'selected_findings':findings,'functions':[{k:f.get(k) for k in ('id','name','description')} for f in d.get('functions',[])],'composition':d.get('composition'),'researchAdjudication':d.get('researchAdjudication'),'statistics':d.get('statistics')}
def main():
 reg=j(WORLD/'research/enterprise/registry.json'); queue=j(WORLD/'research/enterprise/queue.json'); uni=rows(WORLD/'planning/VERCY-UNIFIED-MEGA-REGISTRY.csv'); rel=rows(WORLD/'planning/VERCY-MODEL-RELATIONS.csv')
 d={'contour':next(x for x in reg['units'] if x['id']=='EM-ORG-02'),'queue_reservation':next(x for x in queue['units'] if x['id']=='EM-ORG-02'),'registry_reservations':[x for x in uni if x.get('model_id') in IDS],'relationship_ledger':[x for x in rel if x.get('source_model_id') in IDS or x.get('target_model_id') in IDS],'current_specs':{'WM-ORG-001':project(WORLD/'publications/wm-org-001-organization/spec.yaml'),'WM-ORG-010':project(WORLD/'publications/wm-org-010-legal-entity-registration/spec.yaml'),'WM-ORG-011':project(WORLD/'publications/wm-org-011-business-establishment-branch/spec.yaml')},'evidence_limits':['All three current publications are reviewable drafts with publishableCanonical false.','WM-ORG-011 used a single-provider waiver and lacks independent external review.','The complete specs were parsed and pinned by byte count and SHA-256; selected findings form the compact reviewer projection.','Registry relations and Enterprise v1 properties remain non-normative.']}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(OUT);print(OUT.stat().st_size)
if __name__=='__main__':main()
