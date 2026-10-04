import csv,hashlib,json
from pathlib import Path
import yaml
WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models");OUT=WORLD/'research/enterprise/runs/em-org-05/provider-dossier.json';IDS={'WM-ORG-003','WM-ORG-006'}
SELECT={'team-identifier-assignment','team-boundary-and-entity-distinction','containing-and-managing-organization','team-type-and-category','team-charter-and-mandate','decision-rights-ownership-and-reporting-line','membership-assignment-record','role-and-position-binding','external-and-non-human-participants','nesting-and-inherited-membership','membership-provisioning-and-sync-authority','allocation-and-capacity','team-status-lifecycle','effective-dating-and-time-semantics','formation-and-dissolution','merge-split-and-transfer-events','interfaces-dependencies-and-collaborations','access-privacy-and-retention','team-entitlements-and-member-capabilities','authoritative-membership-identifier-and-master-system','member-agent-and-organization-or-group-bindings','membership-type-profile-classification-and-scheme-version','admission-rejection-decision-conditions-and-effective-time','role-concept-scope-unit-and-validity','participation-activity-project-and-contribution-references','employment-office-subscription-citizenship-licence-and-access-boundary','proposed-pending-active-suspended-ended-rejected-and-revoked-state','valid-decision-event-observation-and-knowledge-time','permission-prohibition-duty-and-compliance-reference','benefit-service-resource-and-access-entitlement-reference'}
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def project(p):
 raw=p.read_bytes();d=yaml.safe_load(raw.decode('utf-8'));fs=[];idx=[]
 for b in d['structure']['bundles']:
  ls=[]
  for l in b['layers']:
   ls.append({k:l.get(k) for k in ('id','name','description')})
   for f in l['findings']:
    if f['id'] in SELECT:fs.append({'bundle':b['id'],'layer':l['id'],'finding':{'id':f['id'],'name':f['name'],'description':f['description'],'source_refs':f.get('source_refs'),'questions':[q.get('text') for q in f.get('questions',[])],'data_elements':[{k:e.get(k) for k in ('id','name','description','value_kind','cardinality','required')} for e in f.get('data_elements',[])]}})
  idx.append({'id':b['id'],'name':b['name'],'description':b.get('description'),'layers':ls})
 return {'source_file':p.relative_to(WORLD).as_posix(),'source_bytes':len(raw),'source_sha256':hashlib.sha256(raw).hexdigest(),'publication':d['publication'],'metaModel':d['metaModel'],'model':d['model'],'structure_index':idx,'selected_findings':fs,'functions':[{k:f.get(k) for k in ('id','name','description')} for f in d['functions']],'composition':d['composition'],'researchAdjudication':d['researchAdjudication'],'statistics':d['statistics']}
def main():
 reg=j(WORLD/'research/enterprise/registry.json');q=j(WORLD/'research/enterprise/queue.json');u=rows(WORLD/'planning/VERCY-UNIFIED-MEGA-REGISTRY.csv');rel=rows(WORLD/'planning/VERCY-MODEL-RELATIONS.csv')
 d={'contour':next(x for x in reg['units'] if x['id']=='EM-ORG-05'),'queue_reservation':next(x for x in q['units'] if x['id']=='EM-ORG-05'),'registry_reservations':[x for x in u if x.get('model_id') in IDS],'relationship_ledger':[x for x in rel if x.get('source_model_id') in IDS or x.get('target_model_id') in IDS],'current_specs':{'WM-ORG-003':project(WORLD/'publications/wm-org-003-team/spec.yaml'),'WM-ORG-006':project(WORLD/'publications/wm-org-006-membership/spec.yaml')},'evidence_limits':['Both publications are reviewable drafts with publishableCanonical false.','WM-ORG-006 is Codex-only under a single-provider waiver and has no independent external review.','Complete specs parsed and pinned; selected findings form the compact reviewer projection.','Registry relationships and Enterprise v1 fields are non-normative.']}
 OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(OUT);print(OUT.stat().st_size)
if __name__=='__main__':main()
