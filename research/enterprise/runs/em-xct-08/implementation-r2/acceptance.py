"""Pinned composition/native installation in three new synthetic Dimensions."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import sync_register as p
HERE=Path(__file__).resolve().parent
SLUG='enterprise-source-synchronization'
def run(composer,skill):
    composer=Path(composer).resolve();skill=Path(skill).resolve();pins=json.loads((HERE/'tool-pins.json').read_text())
    for field,root in [('composerFiles',composer),('skillFiles',skill),('upstreamFiles',HERE/'upstream')]:
        for n,h in pins[field].items():p.require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'Unexpected trusted asset: '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    at=c.now();expires=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-sync-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(folder,name,source,base):
            raw=source.read_bytes();dest=assets/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            media='application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown' if name.endswith('.md') else 'application/yaml'
            return {'path':folder+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':media,'sourceUrl':base+name}
        def release(mid,version,folder,source,base,native):
            specname='spec.json' if native else 'spec.yaml';ds=descriptor(folder,specname,source/specname,base)
            binding=None
            if native:
                binding={'id':'urn:vercy:binding:'+SLUG,'version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',source/'runtime-model.reference.json',base),'instanceSchema':descriptor(folder,'sync.schema.json',source/'sync.schema.json',base),'companionValidator':descriptor(folder,'sync_register.py',source/'sync_register.py',base),'scope':'Own aggregate namespace; outer native validation plus explicit complete nested archive replay and trusted predecessor required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':descriptor(folder,'AGENTS.md',source/'AGENTS.md',base),'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:sync','evidence':'urn:synthetic:acceptance:sync','observedAt':at,'scope':'Synthetic candidate installation, not global parent ratification or evidence of production publication.'}}
        parent='wm-xct-012-provenance';base='https://ver.cy/models/'+SLUG+'/versions/0.1.0/'
        semantic=release('vr.wm-xct-012','0.3.0-research.1',parent,HERE/'upstream'/parent,base+'upstream/'+parent+'/',False)
        companion=release(p.PROFILE_ID,'0.1.0',SLUG,HERE,base,True);companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ('startup','international','ai-team'):
            fixture=p.decode((HERE/'examples'/(name+'.json')).read_bytes());dimension=fixture['config']['dimensionId'];target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json')
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:sync','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic source synchronization reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:sync'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:sync:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic source sync '+name,dimension)
            installed=target/'models/composed'/SLUG/'sync_register.py'
            for n,key in [('sync_register.py','companionValidator'),('sync.schema.json','instanceSchema')]:p.require(c.digest((installed.parent/n).read_bytes())==companion['binding'][key]['digest'],'Installed bytes differ')
            ms=importlib.util.spec_from_file_location('installed_sync_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            db=root/(name+'.sqlite');reg=module.Register(db,fixture['config']);mid=None
            for n,event in enumerate(fixture['events'],1):
                p.require(reg.execute(event['command'],event['actor'],event['recordedAt'])==event['result'],'Installed replay differs')
                if n==len(fixture['events'])-1:mid=reg.archive(fixture['config']['admin'])
            full=reg.archive(fixture['config']['admin']);reg.close();p.require(full==fixture,'Installed fixture round trip differs')
            obj,first=module.native_records(mid,at);_,second=module.native_records(full,at,first)
            paths=[]
            for i,(kind,record) in enumerate([('object',obj),('fact',first),('fact',second)]):
                path=root/(name+'-'+str(i)+'.json');path.write_bytes(module.encode(record));result=append(target,kind,path);paths.append(target/result['written'])
            stored=[module.decode(x.read_bytes()) for x in paths]
            p.require(stored==[obj,first,second],'Stored native bytes round trip differs')
            module.validate_native_snapshot(stored[1]);module.validate_native_snapshot(stored[2],stored[1]);native=native_validate(target);p.require(native['valid'],'Native validation failed')
            p.require(module.archive_from_native(second['value'])==fixture,'Reconstructed native archive differs')
            victim=paths[-1];original=victim.read_bytes();bad=copy.deepcopy(second);bad['value']['root']='sha256:'+'0'*64;victim.write_bytes(module.encode(bad));outer=native_validate(target);nested_rejected=False
            try:module.validate_native_snapshot(bad,first)
            except module.Invalid:nested_rejected=True
            finally:victim.write_bytes(original)
            p.require(outer['valid'] and nested_rejected,'Outer/nested distinction failed')
            truncation=False
            try:module.native_records(mid,at,second)
            except module.Invalid:truncation=True
            p.require(truncation,'Truncation accepted')
            bad=copy.deepcopy(second);bad['provenance']['snapshotDigest']='sha256:'+'0'*64;pin_rejected=False
            try:module.validate_native_snapshot(bad,first)
            except module.Invalid:pin_rejected=True
            p.require(pin_rejected,'Digest mismatch accepted')
            bad=copy.deepcopy(first);bad['subjectId']='urn:synthetic:wrong';subject_rejected=False
            try:module.validate_native_snapshot(bad)
            except module.Invalid:subject_rejected=True
            p.require(subject_rejected,'Wrong subject accepted')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'objects':1,'facts':2,'events':len(full['events']),'native':native,'installedReplayEqualsInput':True,'snapshotTruncationRejected':truncation,'snapshotDigestMismatchRejected':pin_rejected,'wrongSubjectRejected':subject_rejected,'invalidNestedSnapshot':{'native':outer,'companionRejected':nested_rejected},'resumable':False,'pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    names=['acceptance.py','sync_register.py','sync.schema.json','spec.json','tool-pins.json',*['examples/'+n+'.json' for n in ('startup','international','ai-team')]]
    return {'format':'vercy-source-sync-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in names},'limits':'Synthetic NEW Dimensions with candidate-publication metadata, pinned composer, semantic-only parent and separately identified companion. No production connector/IAM/evidence custody/migration/latest-root proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);a=ap.parse_args();report=run(a.composer,a.skill);Path(a.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))
