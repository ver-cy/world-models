import json
import subprocess
from pathlib import Path
import yaml

WORLD=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
SITE=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver.cy")
PLMM_REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\product-landscape-meta-model")
AISMM_REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\software-meta-model")
OUT=WORLD/"research/enterprise/runs/em-lnd-06/provider-dossier.json"

def git(path,*args):
 return subprocess.check_output(['git','-C',str(path),*args],text=True,encoding='utf-8',errors='replace').strip()

def main():
 reg=json.loads((WORLD/'research/enterprise/registry.json').read_text(encoding='utf-8'))
 idx=json.loads((SITE/'models/runtime-index.json').read_text(encoding='utf-8'))
 runtime={x['modelId']:x for x in idx['models'] if x.get('modelId') in {'PLMM','AISMM'}}
 plmm_spec=yaml.safe_load((SITE/'models/vercy-plmm/spec.yaml').read_text(encoding='utf-8'))
 aismm_spec=yaml.safe_load((SITE/'models/vercy-aismm/spec.yaml').read_text(encoding='utf-8'))
 xct=yaml.safe_load((WORLD/'publications/wm-xct-039-managed-it-service-graph/spec.yaml').read_text(encoding='utf-8'))
 ids={'tenant-finding','service-finding','identity-map-finding','dependency-finding','state-finding','impact-finding','master-finding','write-finding','projection-finding','handover-finding','assurance-finding'}
 selected=[]
 for b in xct['structure']['bundles']:
  for l in b['layers']:
   for f in l['findings']:
    if f['id'] in ids: selected.append({'bundle':{k:b.get(k) for k in ('id','name','description')},'layer':{k:l.get(k) for k in ('id','name','description')},'finding':f})
 layers={p.relative_to(PLMM_REPO).as_posix():p.read_text(encoding='utf-8') for p in sorted(PLMM_REPO.rglob('*.layer.md'))}
 dossier={
  'contour':next(x for x in reg['units'] if x['id']=='EM-LND-06'),
  'runtime_index':runtime,
  'plmm_runtime_spec':plmm_spec,
  'aismm_runtime_spec_summary':{'metaModel':aismm_spec['metaModel'],'statistics':aismm_spec.get('statistics'),'source':aismm_spec.get('source')},
  'repository_pins':{
   'plmm':{'commit':git(PLMM_REPO,'rev-parse','HEAD'),'describe':git(PLMM_REPO,'describe','--always'),'last_commit':git(PLMM_REPO,'log','-1','--format=%cI %s'),'readme':(PLMM_REPO/'README.md').read_text(encoding='utf-8'),'layers':layers},
   'aismm':{'commit':git(AISMM_REPO,'rev-parse','HEAD'),'describe':git(AISMM_REPO,'describe','--tags','--always'),'last_commit':git(AISMM_REPO,'log','-1','--format=%cI %s'),'readme_head':'\n'.join((AISMM_REPO/'README.md').read_text(encoding='utf-8').splitlines()[:180])}},
  'managed_it_service_graph':{'publication':xct['publication'],'model':xct['model'],'selected_findings':selected,'functions':xct.get('functions'),'composition':xct.get('composition'),'researchAdjudication':xct['researchAdjudication']},
  'registry_policy':{'reserved_candidates':['PLMM','WM-XCT-039'],'rule':'PLMM already has reserved runtime id vr.vercy.plmm. Do not invent a replacement ID; decide whether to complete, profile or retire it.'}
 }
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(OUT); print(OUT.stat().st_size)
if __name__=='__main__': main()
