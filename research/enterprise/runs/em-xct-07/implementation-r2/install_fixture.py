"""Explicit NEW synthetic Dimension fixture for an object/Event-only binding.

WM-XCT-040 0.1.1 rejects empty fact-path maps. This helper does NOT modify it or
claim its composition acceptance. The pinned native creator/validator allow an
empty map. This is a test installer, not an existing-Dimension migration tool.
"""
from pathlib import Path
import hashlib,json,subprocess,sys

FILES=('spec.json','AGENTS.md','runtime-model.reference.json','action.schema.json','action_bundle.py')
def raw_json(value): return json.dumps(value,ensure_ascii=False,indent=2).encode('utf-8')+b'\n'
def sha(raw): return 'sha256:'+hashlib.sha256(raw).hexdigest()
def require(ok,message):
    if not ok: raise RuntimeError(message)
def install(package,skill,target,dimension,profile):
    package=Path(package).resolve();skill=Path(skill).resolve();target=Path(target).absolute()
    require(target.parent.is_dir() and not target.exists(),'New target required')
    raw={name:(package/name).read_bytes() for name in FILES}
    spec=json.loads(raw['spec.json']); mid=spec['metaModel']['registryId']; version=spec['metaModel']['version']
    runtime=json.loads(raw['runtime-model.reference.json'])
    require(runtime=={'format':'vercy-runtime-model-schema','schemaVersion':'1.0.0','modelId':mid,'paths':{}},'Exact object/Event-only runtime required')
    cmd=[sys.executable,str(skill/'scripts/create_dimension.py'),'--target',str(target),'--name','Synthetic action '+profile,'--namespace',dimension,'--owner','urn:synthetic:owner:installation','--preset','commercial-company','--purpose','Synthetic action contract acceptance']
    dry=subprocess.run(cmd+['--dry-run'],capture_output=True,text=True,encoding='utf-8');require(dry.returncode==0,'Native creator dry run failed: '+dry.stderr)
    proc=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8');require(proc.returncode==0,'Native creator failed: '+proc.stderr)
    location='models/reference/enterprise-action-requests'; out=target/location;out.mkdir(parents=True)
    # Copy AGENTS first, then the other exact pinned candidate assets.
    for name in ('AGENTS.md',)+tuple(n for n in FILES if n!='AGENTS.md'):
        require((package/name).read_bytes()==raw[name],'Candidate changed during fixture install')
        (out/name).write_bytes(raw[name])
    registry=json.loads((target/'registries/meta-models.yaml').read_text(encoding='utf-8'))
    require(registry.get('models')==[],'Creator did not produce an empty fixture registry')
    registry['models']=[{'id':mid,'version':version,'agents':location+'/AGENTS.md','specification':location+'/spec.json','specificationDigest':sha(raw['spec.json']),
      'runtimeSchema':location+'/runtime-model.reference.json','runtimeSchemaDigest':sha(raw['runtime-model.reference.json']),
      'bindingScope':'Object facets and native Event payloads; explicit installed companion validation required.'}]
    (target/'registries/meta-models.yaml').write_bytes(raw_json(registry))
    lock=json.loads((target/'vercy.lock').read_text(encoding='utf-8'));require(lock.get('models')==[],'Nonempty starting lock')
    lock['models']=[{'id':mid,'version':version,'status':'candidate','simulationOnly':True,'digest':sha(raw['spec.json']),
       'specUrl':spec['canonicalUrl'],'agentsUrl':spec['canonicalUrl'].rsplit('/',1)[0]+'/AGENTS.md','location':location,'readiness':'native-binding'}]
    (target/'vercy.lock').write_bytes(raw_json(lock))
    proof={'format':'enterprise-action-native-fixture-installation','dimensionId':dimension,'modelId':mid,'version':version,
       'simulatedPublicationMetadataOnly':True,'route':'pinned native creator + explicit local candidate binding; NOT WM-XCT-040 composition acceptance',
       'assets':{name:sha(value) for name,value in raw.items()},'limits':'New synthetic Dimension only; no download, authentication, migration, production deployment or automatic execution of model code.'}
    (target/'action-fixture-installation.json').write_bytes(raw_json(proof))
    report=subprocess.run([sys.executable,str(skill/'scripts/vercy.py'),'validate',str(target)],capture_output=True,text=True,encoding='utf-8')
    data=json.loads(report.stdout);require(report.returncode==0 and data.get('valid'),'Native control validation failed: '+report.stdout)
    require(all((out/name).read_bytes()==value for name,value in raw.items()),'Installed asset readback mismatch')
    return proof
