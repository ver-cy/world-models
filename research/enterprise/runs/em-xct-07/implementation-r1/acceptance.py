"""Install the standalone companion in three NEW synthetic Vercy Dimensions."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from pathlib import Path
from datetime import datetime,timedelta,timezone
from fixtures import fixture,descriptive,NOW,ALL
HERE=Path(__file__).parent; SLUG='enterprise-action-requests'; MID='vr.profile.'+SLUG
def require(ok,message):
    if not ok: raise RuntimeError(message)
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def run(composer,skill):
    composer=Path(composer).resolve(); skill=Path(skill).resolve()
    pins=json.loads((HERE/'tool-pins.json').read_text(encoding='utf-8'))
    for key,root in [('composerFiles',composer),('skillFiles',skill)]:
        for name,h in pins[key].items(): require(sha(root/name)==h,'Changed pinned tool: '+name)
    import install_fixture
    sys.path.insert(0,str(skill/'scripts')); from write_record import append
    from validate_dimension import validate as outer_validate
    at=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'); reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-action-native-') as tmp:
        root=Path(tmp)
        for profile in ('startup','matrix','ai-service'):
            dim='urn:synthetic:dimension:'+profile; target=root/profile
            proof=install_fixture.install(HERE,skill,target,dim,profile)
            checks={name:('sha256:'+sha(target/'models/reference'/SLUG/name)==expected) for name,expected in proof['assets'].items()}
            require(all(checks.values()),'Installed bytes differ')
            installed=target/'models/reference'/SLUG/'action_bundle.py'
            ms=importlib.util.spec_from_file_location('installed_action_'+profile,installed); module=importlib.util.module_from_spec(ms); ms.loader.exec_module(module)
            x,i,rules,definition=fixture(root/(profile+'.db'),profile,executor_type=module.Executor)
            x.add_definition(descriptive(definition),NOW)
            key='native-first-0001'; actor=i['actorId']
            try: x.dispatch(module.encoded(i),key,actor,NOW,_fault='after-commit')
            except module.ResponseLost: pass
            else: raise RuntimeError('Response-loss injection did not occur')
            original=x.lookup(key,actor,NOW); require(original['status']=='committed','Missing retained result')
            later=copy.deepcopy(i); later.update(expectedRevision=1,parameters={'labels':['intervening']})
            second=x.dispatch(module.encoded(later),'native-second-0002',actor,NOW); require(second['status']=='committed','Second intent failed')
            require(x.dispatch(module.encoded(i),key,actor,NOW)==original,'Replay changed old receipt')
            stale=copy.deepcopy(i); stale.update(expectedRevision=2,parameters={'labels':['draft']},compensatesReceiptId=original['receipt']['eventId'])
            require(x.dispatch(module.encoded(stale),'native-stale-0003',actor,NOW)['status']=='rejected-precondition','Intervening update accepted for compensation')
            compensate=copy.deepcopy(i); compensate.update(expectedRevision=2,parameters={'labels':i['parameters']['labels']},compensatesReceiptId=second['receipt']['eventId'])
            require(x.dispatch(module.encoded(compensate),'native-compensate-0004',actor,NOW)['status']=='committed','Valid compensation failed')
            observed=x.observe(key,actor,NOW,'caller-unknown','Synthetic response lost')['event']
            require(x.observe(key,actor,NOW,'caller-observed-success','Retained receipt read',observed['eventId'])['status']=='recorded','Correction failed')
            denied=copy.deepcopy(rules)
            for side in ('principalScope','delegateScope'): denied[0][side]['actions']=['submit','read','cancel']
            x.set_policy(denied,NOW); pending=copy.deepcopy(i); pending.update(expectedRevision=3)
            require(x.dispatch(module.encoded(pending),'native-pending-0005',actor,NOW)['status']=='current-execution-denied','Current denial ignored')
            require(x.cancel('native-pending-0005',actor,NOW)['status']=='cancelled','Cancel failed')
            snap=x.snapshot(NOW); semantic=module.validate_snapshot(snap)
            export_dir=root/(profile+'-export'); exported=module.export_snapshot(snap,export_dir)
            native=module.records(snap); stored=[]; stored_paths={}
            # Generated dict order: all object revisions first, then events by sequence.
            for rid,record in native.items():
                src=export_dir/'records'/(rid+'.json'); written=append(target,record['recordType'],src,expected_head=record.get('previousRecordId'))
                path=target/written['written']; stored_paths[rid]=path
                stored.append(json.loads(path.read_text(encoding='utf-8')))
            nested=module.validate_native_records(snap,stored); outer=outer_validate(target); require(outer['valid'],'Native outer validation failed: '+json.dumps(outer))
            # Real stored nested tamper: the native envelope stays structurally valid.
            receipt=next(e for e in snap['events'] if e['kind']=='receipt'); path=stored_paths[receipt['eventId']]; original_bytes=path.read_bytes()
            tampered=json.loads(original_bytes); tampered['payload']['enterpriseActionEvent']['payload']['afterLabels']=['forged']
            path.write_bytes(module.file_bytes(tampered)); outer_tampered=outer_validate(target)
            require(outer_tampered['valid'],'Expected generic envelope-only pass for nested tamper')
            mutated=[json.loads(p.read_text(encoding='utf-8')) for p in stored_paths.values()]
            try: module.validate_native_records(snap,mutated)
            except module.Refused as error: require(str(error)=='native-record-projection','Wrong nested rejection')
            else: raise RuntimeError('Stored tamper accepted by companion')
            path.write_bytes(original_bytes); module.validate_native_records(snap,[json.loads(p.read_text(encoding='utf-8')) for p in stored_paths.values()])
            try: append(target,'event',export_dir/'records'/(receipt['eventId']+'.json'))
            except Exception as error: require('already exists' in str(error) or 'duplicate' in str(error).lower(),'Unexpected duplicate refusal')
            else: raise RuntimeError('Native duplicate event was overwritten')
            outer.pop('dimension',None)
            reports.append({'profile':profile,'dimensionId':dim,'installedAssets':checks,'installedCompanionExecuted':True,'semantic':semantic,'export':exported,'nativeOuter':outer,'nativeNested':nested,'storedNestedTamperRejected':True,'genericOuterAcceptedNestedTamper':True,'originalBytesRestored':path.read_bytes()==original_bytes,'duplicateNativeEventRefused':True,'simulatedPublicationMetadataOnly':True,'installationRoute':proof['route']})
    return {'format':'vercy-action-native-acceptance','executedAt':at,'passed':len(reports),'failed':0,'profiles':reports,
       'sourceDigests':{name:sha(HERE/name) for name in ('action_bundle.py','action.schema.json','spec.json','AGENTS.md','runtime-model.reference.json','fixtures.py','acceptance.py','install_fixture.py','tool-pins.json')},
       'limits':'Three fresh synthetic organizational Dimensions. Generic native validation is separate from explicit nested history validation. No existing-Dimension migration, real credentials, external effects, authenticated latest-history proof or production deployment.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True)
    args=ap.parse_args(); result=run(args.composer,args.skill); Path(args.report).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'failed':result['failed']}))
