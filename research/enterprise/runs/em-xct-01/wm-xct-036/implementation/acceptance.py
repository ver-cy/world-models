"""Synthetic new-Dimension acceptance, using explicitly trusted local tools.

python acceptance.py --composer /trusted/WM-XCT-040 --skill /trusted/vercy/skills/vercy --report acceptance-results.json
Only this script's temporary directory is changed. No existing Dimension is used.
"""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from pathlib import Path
import identity_profile as p
HERE=Path(__file__).resolve().parent
def run(composer,skill):
    p.require(__debug__,'Run acceptance without -O')
    composer=Path(composer).resolve();skill=Path(skill).resolve()
    pins=p.load(HERE/'tool-pins.json')
    for name,h in pins['composerFiles'].items():p.require(hashlib.sha256((composer/name).read_bytes()).hexdigest()==h,'unexpected composer bytes: '+name)
    for name,h in pins['skillFiles'].items():p.require(hashlib.sha256((skill/name).read_bytes()).hexdigest()==h,'unexpected skill bytes: '+name)
    for name,h in pins['upstreamFiles'].items():p.require(hashlib.sha256((HERE/'upstream'/name).read_bytes()).hexdigest()==h,'unexpected upstream bytes: '+name)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    identity_policy=p.load(HERE/'examples/policy.json');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-identity-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(slug,name,source):
            raw=source.read_bytes();dest=assets/slug/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':slug+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'text/x-python' if name.endswith('.py') else 'application/json' if name.endswith('.json') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':'https://ver.cy/models/'+slug+('/versions/0.3.0-research.1/' if slug=='wm-xct-036-alias-same-as-mapping' and name in {'spec.yaml','AGENTS.md'} else '/profiles/enterprise-identity/0.1.0/' if name not in {'spec.yaml','AGENTS.md'} else '/')+name}
        releases=[]
        for slug in ['wm-xct-011-identifier-scheme','wm-xct-036-alias-same-as-mapping']:
            source=HERE/'upstream'/slug;raw=(source/'spec.yaml').read_text(encoding='utf-8');meta=json.loads(raw[raw.index('{'):])['metaModel']
            dspec=descriptor(slug,'spec.yaml',source/'spec.yaml');dagent=descriptor(slug,'AGENTS.md',source/'AGENTS.md')
            binding=None
            if meta['id']=='WM-XCT-036':
                runtime=descriptor(slug,'runtime-model.reference.json',HERE/'runtime-model.reference.json')
                instance=descriptor(slug,'identity-profile.schema.json',HERE/'identity-profile.schema.json')
                validator=descriptor(slug,'identity_profile.py',HERE/'identity_profile.py')
                binding={'id':'urn:vercy:binding:enterprise-identity-assertion','version':'0.1.0','forSpecificationDigest':dspec['digest'],'runtime':runtime,'instanceSchema':instance,'companionValidator':validator,'scope':'One bounded enterprise assertion snapshot; companion semantics required; no account ownership, endpoint merge, IAM or whole-model conformance.'}
            releases.append({'modelId':meta['registryId'],'version':meta['version'],'namespace':'urn:vercy:model:'+meta['registryId'],'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':dspec,'agents':dagent,'installationMode':'native-binding' if binding else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:identity','evidence':'urn:synthetic:acceptance:identity','observedAt':c.now(),'scope':'Only this reference binding and synthetic composition.'}})
        releases[1]['requires']=[{k:releases[0][k] for k in ['modelId','version']}]
        for name in ['startup','group','ai-team']:
            target=root/name;stage=root/(name+'-stage');policy_path=root/(name+'-composition-policy.json');lock_path=root/(name+'-lock.json');plan_path=root/(name+'-plan.json')
            dimension=identity_policy['dimension'];at=c.now()
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:identity','dimensionId':dimension,'owner':'urn:synthetic:owner:identity','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic enterprise identity reference'],'allowedModelIds':['vr.wm-xct-011','vr.wm-xct-036'],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:identity'],'allowReviewableDrafts':True,'validFrom':'2026-09-21T00:00:00Z','validUntil':'2027-01-01T00:00:00Z'}
            policy_path.write_bytes(c.encode(policy));lock_path.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:identity:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':'2026-12-31T23:59:59Z','baseLockDigest':c.digest(lock_path.read_bytes()),'roots':[{k:releases[1][k] for k in ['modelId','version']}],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(policy_path.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            plan_path.write_bytes(c.encode(plan));c.stage(plan_path,assets,policy_path,lock_path,stage)
            bootstrap(stage,policy_path,lock_path,skill,target,'Synthetic identity '+name,dimension)
            installed=target/'models/composed/wm-xct-036-alias-same-as-mapping/identity_profile.py'
            p.require(c.digest(installed.read_bytes())==releases[1]['binding']['companionValidator']['digest'],'installed validator differs')
            p.require(c.digest((installed.parent/'identity-profile.schema.json').read_bytes())==releases[1]['binding']['instanceSchema']['digest'],'installed schema differs')
            module_spec=importlib.util.spec_from_file_location('installed_identity_'+name,installed);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
            rows=p.load(HERE/('examples/'+name+'.json'));written_facts=[]
            for i,a in enumerate(rows):
                obj={'recordType':'object','schemaVersion':'1.0.0','recordId':a['id']+':object-r1','objectId':a['id'],'objectType':'vr.wm-xct-036:identity-assertion','name':'Synthetic identity assertion','description':'One assertion; never a Person or a resolution aggregate','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':'urn:synthetic:reference','synthetic':True},'accessClass':'synthetic-private'}
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':a['id']+':snapshot-r1','subjectId':a['id'],'path':'identity.assertion.snapshot','value':a,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[],'status':'asserted','provenance':{'source':'urn:synthetic:reference','synthetic':True},'authority':{'source':'urn:synthetic:actor:steward','rank':0},'masterSystem':'urn:synthetic:reference','accessClass':'synthetic-private'}
                for kind,value in [('object',obj),('fact',fact)]:
                    path=root/(name+str(i)+kind+'.json');path.write_bytes(p.encode(value));written=append(target,kind,path)
                    if kind=='fact':written_facts.append(target/written['written'])
            stored=[p.load(x)['value'] for x in written_facts]
            p.require(stored==rows,'stored assertion round-trip differs from source fixtures');module.validate_set(stored,identity_policy)
            v=native_validate(target);p.require(v['valid'],'native V3 failed')
            # Deliberately corrupt an actually stored nested snapshot. V3 should
            # still accept the outer object type, and the companion must reject.
            victim=written_facts[0];raw=victim.read_bytes();bad=p.load(victim);bad['value']['inferencePermitted']=True;victim.write_bytes(p.encode(bad))
            negative_v3=native_validate(target);rejected=False
            try:module.validate(p.load(victim)['value'],identity_policy)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(raw)
            p.require(negative_v3['valid'] and rejected,'expected native/companion distinction not observed')
            v.pop('dimension',None);negative_v3.pop('dimension',None)
            reports.append({'profile':name,'objects':len(rows),'facts':len(stored),'native':v,'roundTripEqualsInput':stored==rows,'companion':'Explicitly called on actual stored snapshots; not automatically enforced by native V3','invalidNestedSnapshot':{'native':negative_v3,'companionRejected':rejected},'installedValidatorDigest':c.digest(installed.read_bytes()),'pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-identity-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'identity_profile.py',HERE/'identity-profile.schema.json',HERE/'tool-pins.json',*sorted((HERE/'examples').glob('*.json'))]},'limits':'Synthetic new-Dimension assertion snapshots only. Upstream subjects, account ownership, IAM, source truth and existing-Dimension migrations are not tested.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))
