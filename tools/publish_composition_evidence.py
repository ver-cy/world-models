"""Publish the sanitized WM-XCT-040 evidence and reproducible reference package.

Run after publish_model_research.py. No raw CLI streams or private conversation
locators are exposed. The final version directory is immutable once deployed.
"""
import argparse,hashlib,html,json,shutil,zipfile
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--run',type=Path,required=True);ap.add_argument('--publication',type=Path,required=True);ap.add_argument('--site-root',type=Path,required=True);a=ap.parse_args()
    run=a.run;pub=a.publication;site=a.site_root;slug=pub.name
    release=json.loads((pub/'publication.json').read_text(encoding='utf-8'))['version']
    assert release and all(c in '0123456789.' for c in release), 'invalid release version'
    zip_name='package-'+release+'.zip'
    evidence=site/'enterprise/research/wm-xct-040';evidence.mkdir(parents=True,exist_ok=True)
    safe=['shared-boundary.md','audit-prompt.md','audit-input-manifest.json','final-review-prompt.md','final-review-input-manifest.json','claude-audit.md','claude-final.md','claude-remediation.md','remediation-review-prompt.md','remediation-review-manifest.json','grok-bootstrap.prompt.md','grok-bootstrap.md','grok-remediation.prompt.md','grok-remediation.md','grok-study.md','grok-audit.md','grok-final.md','codex.result.json','synthesis.result.json','synthesis.validation.json','adjudication.json','source-verification.json','audit-remediation.json','research-reconciliation.md','publication-verification.json','english-publication.json','english-publication-verification.json']
    for n in safe:
        if (run/n).is_file():shutil.copy2(run/n,evidence/n)
    keys=['provider','requested_model','actual_models','model','mode','status','started_at','completed_at','seconds','prompt_sha256','response_sha256','scope','reviewed_files','evidence_format']
    manifests=[]
    for p in sorted(run.glob('*.manifest.json')):
        v=json.loads(p.read_text(encoding='utf-8'));manifests.append({'manifest':p.name,**{k:v[k] for k in keys if k in v},'originalManifestSha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (evidence/'provider-evidence.json').write_text(json.dumps(manifests,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for p in (run/'implementation').rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts or p.suffix not in {'.py','.md','.json','.yaml','.lock','.txt'}:continue
        rel=p.relative_to(run/'implementation');dest=pub/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
    tests=json.loads((pub/'test-results.json').read_text(encoding='utf-8'));acceptance=json.loads((pub/'acceptance-results.json').read_text(encoding='utf-8'))
    marker='<!-- composition-reference-package -->'
    body=(pub/'index.html').read_text(encoding='utf-8')
    if marker not in body:
        extra=marker+'<section><h2>Compose a verified set of models</h2><p>This contract records versions, dependencies, authority and data schemas for a new company Dimension. Existing Dimensions require a separate migration.</p><p><a href="README.md">Instructions and limitations</a> · <a href="model-spec.md">Detailed model</a> · <a href="'+zip_name+'">Complete package '+release+'</a> · <a href="/enterprise/research/wm-xct-040/">Claude, Grok and verification evidence</a></p><p>'+str(tests['tests'])+' automated tests and '+str(acceptance['passed'])+' new-Dimension scenarios passed. Nested semantics are validated separately from V3. All examples are synthetic.</p><p>Version 0.1.1 publishes English documentation; executable code and schemas remain unchanged from the reviewed 0.1.0 implementation.</p><ul>'+''.join('<li><a href="'+n+'">'+html.escape(n)+'</a></li>' for n in ['field-catalog.json','whole-object-coverage.json','composition-plan.schema.json','policy.schema.json','crosswalk.json','test-results.json','acceptance-results.json'])+'</ul></section>'
        assert '</main>' in body;body=body.replace('</main>',extra+'</main>',1);(pub/'index.html').write_text(body,encoding='utf-8')
    files=sorted(p for p in pub.rglob('*') if p.is_file() and 'versions' not in p.relative_to(pub).parts and p.suffix!='.zip' and p.name!='package-checksums.json')
    checks={p.relative_to(pub).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (pub/'package-checksums.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
    with zipfile.ZipFile(pub/zip_name,'w',zipfile.ZIP_DEFLATED) as z:
        for p in files+[pub/'package-checksums.json']:
            info=zipfile.ZipInfo(p.relative_to(pub).as_posix(),date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,p.read_bytes())
    version=pub/'versions'/release;version.mkdir(parents=True,exist_ok=True)
    for p in files+[pub/'package-checksums.json',pub/zip_name]:
        target=version/p.relative_to(pub);target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():assert target.read_bytes()==p.read_bytes(),'immutable version differs: '+str(target)
        else:shutil.copy2(p,target)
    target=site/'models'/slug;shutil.copytree(pub,target,dirs_exist_ok=True)
    names=sorted(p.name for p in evidence.iterdir() if p.is_file() and p.name not in {'index.html','evidence-checksums.json'})
    checks={n:hashlib.sha256((evidence/n).read_bytes()).hexdigest() for n in names};(evidence/'evidence-checksums.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
    links=''.join('<li><a href="'+html.escape(n)+'">'+html.escape(n)+'</a></li>' for n in names+['evidence-checksums.json'])
    text='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>WM-XCT-040: research and verification</title><link rel="canonical" href="https://ver.cy/enterprise/research/wm-xct-040/"><meta name="description" content="Vercy Model Composition Resolution: independent Claude and Grok reviews, reconciled findings and reproducible verification."><style>body{max-width:960px;margin:40px auto;padding:24px;font:18px/1.6 system-ui;color:#203044}a{color:#125bb5}</style></head><body><main><a href="/enterprise/">Enterprise registry</a><h1>WM-XCT-040: research and verification</h1><p>Codex synthesized the model, verified primary sources and ran the tests. Grok conducted independent research and file audits through the browser. Claude reviewed files through the CLI. The unsuccessful Claude research attempt remains recorded separately and is not counted as completed research.</p><p>Reviewer roles, audit boundaries, findings and remaining limitations are recorded in adjudication.json, provider-evidence.json and audit-remediation.json. Reviewer opinions do not grant operational authority or establish standards conformance.</p><p>The technical reviews concern implementation 0.1.0. Release 0.1.1 publishes English documentation with unchanged executable code and schemas. Original review inputs and responses retain their original language and bytes as historical evidence. The 0.1.0 package remains immutable in the version archive.</p><p><a href="/models/wm-xct-040-model-composition-resolution/">Model and package</a> · <a href="/models/wm-xct-040-model-composition-resolution/README.md">Usage instructions</a> · <a href="research-reconciliation.md">Reconciled findings</a></p><ul>'''+links+'</ul></main></body></html>\n'
    (evidence/'index.html').write_text(text,encoding='utf-8')
    print(json.dumps({'model':slug,'version':release,'files':len(files),'evidence':len(names),'zipBytes':(pub/zip_name).stat().st_size}))
if __name__=='__main__':main()
