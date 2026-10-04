"""Deterministic post-commit native evidence, with a manifest written LAST."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib
import json
from action import encoded, digest, require, Refused, parse
from history import validate_snapshot

def stamp(second): return datetime.fromtimestamp(second,timezone.utc).isoformat().replace('+00:00','Z')
def file_bytes(value): return json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False).encode('utf-8')+b'\n'
def sha(raw): return hashlib.sha256(raw).hexdigest()

def records(snapshot):
    validate_snapshot(snapshot)
    m=snapshot['meta']; result={}; previous={}; object_ids=set()
    provenance={'source':m['issuer'],'assurance':'synthetic-reference-only'}
    def obj(oid,rid,kind,name,time,facet,state='active'):
        record={'recordType':'object','schemaVersion':'1.0.0','recordId':rid,'objectId':oid,'objectType':kind,'name':name,
                'recordedAt':stamp(time),'previousRecordId':previous.get(oid),'state':state,'facets':facet,'provenance':provenance}
        require(rid not in result,'native-id-collision'); result[rid]=record; previous[oid]=rid; object_ids.add(oid)
    for row in snapshot['definitions']:
        d=parse(row['body'])
        obj(d['definitionId'],'rec.def.'+row['digest'],'urn:vercy:enterprise:ActionDefinition:0.1.0',d['name'],row['recorded_at'],{'enterpriseActionDefinition':d})
    for row in snapshot['resources']:
        if row['revision']==0: require(row['id'] not in object_ids,'native-subject-collision')
        obj(row['id'],'rec.resource.'+digest({'id':row['id'],'revision':row['revision']}),'urn:vercy:synthetic:OrderedLabelResource','Synthetic ordered-label resource',row['recorded_at'],{'syntheticLabels':{'revision':row['revision'],'labels':parse(row['labels'])}})
    for r in snapshot['requests']:
        require(r['requestId'] not in object_ids,'native-subject-collision')
        immutable={k:r[k] for k in ('requestId','keyHash','intentDigest','intent','submittedAt','submissionEventId')}
        obj(r['requestId'],'rec.'+r['requestId'],'urn:vercy:enterprise:ActionRequest:0.1.0','Synthetic action request',r['submittedAt'],{'enterpriseActionRequest':immutable})
    for e in snapshot['events']:
        request=next(r for r in snapshot['requests'] if r['requestId']==e['requestId'])
        subjects=[e['requestId'],request['intent']['definition']['definitionId']]
        if e['kind']=='receipt': subjects.append(e['payload']['resourceId'])
        for field in ('correctsEventId','compensatesReceiptId'):
            if e['payload'].get(field): subjects.append(e['payload'][field])
        require(e['eventId'] not in result,'native-id-collision')
        result[e['eventId']]={'recordType':'event','schemaVersion':'1.0.0','eventId':e['eventId'],
              'eventType':'urn:vercy:enterprise:action:'+e['kind']+':0.1.0','subjectIds':list(dict.fromkeys(subjects)),
              'occurredAt':stamp(e['recordedAt']),'recordedAt':stamp(e['recordedAt']),'actorId':e['issuerId'],
              'payload':{'enterpriseActionEvent':e},'provenance':provenance}
    return result

def export_snapshot(snapshot,target,*,_fail_after=None):
    """Privileged export. A retry must use the identical snapshot including cut/time.

    Files are append-only and exact-match on retry. Partial writes are detectable;
    no claim of an atomic native multi-file commit. No changes go back to execution.
    """
    target=Path(target); require(not target.is_symlink(),'export-symlink')
    recs=records(snapshot)
    blobs={'snapshot.json':file_bytes(snapshot)}
    for rid,record in recs.items(): blobs['records/'+rid+'.json']=file_bytes(record)
    manifest={'format':'enterprise-action-export/0.1.0','dimensionId':snapshot['meta']['dimension'],'executorEpoch':snapshot['meta']['epoch'],
              'controlSequence':snapshot['meta']['control_sequence'],'eventSequence':len(snapshot['events']),
              'exportedAt':stamp(snapshot['meta']['clock']),'files':{name:sha(raw) for name,raw in sorted(blobs.items())},
              'assurance':'synthetic-evidence-not-authenticated-current-state'}
    blobs['manifest.json']=file_bytes(manifest)
    for index,(name,raw) in enumerate(blobs.items(),1):
        path=target/name
        require(not path.is_symlink() and not path.parent.is_symlink(),'export-symlink')
        path.parent.mkdir(parents=True,exist_ok=True)
        if path.exists(): require(path.read_bytes()==raw,'export-existing-content')
        else:
            with path.open('xb') as f: f.write(raw)
        if _fail_after==index: raise Refused('injected-export-interruption')
    return verify_export(target)

def validate_native_records(snapshot,stored_records):
    """Explicit nested validation of the full supplied package record set.

    Caller must collect the complete authorized set for this binding; this checks
    that set against the supplied cut, not all records/permissions in a Dimension.
    """
    require(type(stored_records) is list,'native-record-list')
    expected=records(snapshot); actual={}
    for r in stored_records:
        require(type(r) is dict,'native-record-shape')
        rid=r.get('recordId') if r.get('recordType')=='object' else r.get('eventId')
        require(type(rid) is str and rid not in actual,'native-record-identity'); actual[rid]=r
    require(set(actual)==set(expected),'native-record-closure')
    for rid,value in expected.items(): require(actual[rid]==value,'native-record-projection')
    return {'valid':True,'records':len(actual),'scope':'supplied complete package set and snapshot; not authenticated latest-history'}

def verify_export(target):
    """Whole exact-file closure + deterministic semantic replay; no trust bootstrap."""
    target=Path(target)
    require(not target.is_symlink(),'export-symlink')
    require((target/'manifest.json').is_file(),'export-incomplete')
    require(not any(p.is_symlink() for p in target.rglob('*')),'export-symlink')
    # This privileged archive is larger than an individual bounded wire intent.
    manifest=json.loads((target/'manifest.json').read_text(encoding='utf-8'),object_pairs_hook=_unique_pairs)
    require(set(manifest)=={'format','dimensionId','executorEpoch','controlSequence','eventSequence','exportedAt','files','assurance'},'manifest-shape')
    require(manifest['format']=='enterprise-action-export/0.1.0','manifest-version')
    expected=set(manifest['files'])|{'manifest.json'}
    actual={p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file()}
    require(expected==actual,'export-file-closure')
    for name,expected_hash in manifest['files'].items():
        require(name in actual and '..' not in Path(name).parts and not Path(name).is_absolute(),'export-path')
        require(sha((target/name).read_bytes())==expected_hash,'export-file-digest')
    snapshot=json.loads((target/'snapshot.json').read_text(encoding='utf-8'),object_pairs_hook=_unique_pairs)
    result=validate_snapshot(snapshot); recs=records(snapshot)
    require(set(manifest['files'])=={'snapshot.json'}|{'records/'+rid+'.json' for rid in recs},'native-closure')
    for rid,record in recs.items(): require((target/'records'/f'{rid}.json').read_bytes()==file_bytes(record),'native-projection')
    m=snapshot['meta']
    require(manifest['dimensionId']==m['dimension'] and manifest['executorEpoch']==m['epoch'] and manifest['controlSequence']==m['control_sequence'] and manifest['eventSequence']==len(snapshot['events']) and manifest['exportedAt']==stamp(m['clock']),'export-cut')
    require(manifest['assurance']=='synthetic-evidence-not-authenticated-current-state','export-assurance')
    return {**result,'files':len(actual),'controlSequence':m['control_sequence'],'exportedAt':manifest['exportedAt']}

def _unique_pairs(items):
    result={}
    for key,value in items:
        require(key not in result,'duplicate-key'); result[key]=value
    return result
