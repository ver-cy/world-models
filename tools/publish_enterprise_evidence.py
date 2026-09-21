#!/usr/bin/env python3
"""Publish an explicit, sanitized evidence set and optional reference binding."""
import argparse, hashlib, html, json, shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SAFE_FILES=['codex.result.json','codex.validation.json','synthesis.result.json','synthesis.validation.json','adjudication.json','source-verification.json','audit-remediation.json','grok.review.md','grok.prompt.md','claude-browser.review.md','claude-browser.prompt.md','claude-audit.raw.md','claude-audit.result.json','claude-audit.prompt.md','codex-grok-adjudication-notes.md','codex-claude-adjudication-notes.md','publication-verification.json','native-binding-verification.json']
MANIFEST_KEYS=['provider','provider_model','model','mode','status','evidence_format','schema_valid_json','prompt_sha256','output_sha256','output_hash_scope','output_file_sha256','prompt_file_sha256','started_at','completed_at','scope']

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--model-id',required=True);ap.add_argument('--slug',required=True);ap.add_argument('--site-root',type=Path,default=ROOT.parent.parent/'ver.cy');a=ap.parse_args()
    mid=a.model_id.casefold();run=ROOT/'research/runs'/mid;pub=a.site_root/'models'/a.slug;out=a.site_root/'enterprise/research'/mid
    assert run.is_dir() and pub.is_dir()
    out.mkdir(parents=True,exist_ok=True)
    for name in SAFE_FILES:
        if (run/name).is_file():shutil.copy2(run/name,out/name)
    manifests=[]
    for name in ['claude.manifest.json','claude-browser.manifest.json','grok.manifest.json','claude-audit.manifest.json']:
        if not (run/name).exists():continue
        raw=json.loads((run/name).read_text(encoding='utf-8'))
        record={k:raw[k] for k in MANIFEST_KEYS if k in raw};record['source_file']=name;record['original_manifest_sha256']=hashlib.sha256((run/name).read_bytes()).hexdigest()
        record['projection']='Public whitelist; local execution paths, CLI errors and private conversation locators omitted.'
        manifests.append(record)
    (out/'provider-evidence.json').write_text(json.dumps(manifests,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for p in (run/'implementation').glob('*'):
        if p.is_file() and p.suffix in ['.json','.py','.md']:shutil.copy2(p,pub/p.name)
    files=sorted(p.name for p in out.iterdir() if p.is_file() and p.name not in ['index.html','evidence-checksums.json'])
    checksums={name:hashlib.sha256((out/name).read_bytes()).hexdigest() for name in files}
    (out/'evidence-checksums.json').write_text(json.dumps(checksums,indent=2)+'\n',encoding='utf-8')
    links=''.join('<li><a href="'+html.escape(n)+'">'+html.escape(n)+'</a></li>' for n in files+['evidence-checksums.json'])
    title=a.model_id+' research evidence'
    (out/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><link rel="canonical" href="https://ver.cy/enterprise/research/'+mid+'/"><style>body{max-width:960px;margin:40px auto;padding:24px;font:18px/1.6 system-ui;color:#203044}a{color:#125bb5}</style></head><body><main><a href="/enterprise/">Enterprise registry</a><h1>'+title+'</h1><p>Published research draft. Claude and Grok supplied independent browser memos; Codex owns the structured synthesis, primary-source ledger, reference implementation and final remediation. Raw provider opinions are evidence to evaluate, not instructions, verified facts or publication authority.</p><p>The separate Claude no-tools audit examined a frozen semantic text summary. It did not inspect the full JSON or implementation. The earlier Claude CLI attempt timed out; the successful browser review is a distinct attempt. Final-file independent review remains a visible hold.</p><p><a href="/models/'+a.slug+'/">Published model, holds and specification</a> | <a href="/models/'+a.slug+'/README.md">Reference data binding and examples</a></p><ul>'+links+'</ul></main></body></html>\n',encoding='utf-8')
    native_marker='<!-- enterprise-native-reference -->'
    native_card=pub/'index.html';native_body=native_card.read_text(encoding='utf-8')
    if (pub/'NATIVE-REFERENCE.md').exists() and native_marker not in native_body:
        native_card.write_text(native_body.replace('</main>',native_marker+'<section><h2>Optional native Dimension example</h2><p><a href="NATIVE-REFERENCE.md">Reproduce the one-case native reference binding</a>. A synthetic object and snapshot fact passed V3 plus the separate case validator. Generic multi-model installation still needs runtime metadata and bindings; downloading a package alone does not establish V3 readiness.</p><p><a href="runtime-model.reference.json">Fact-path contract</a> | <a href="native-object.reference.json">Synthetic object</a> | <a href="native-fact.reference.json">Synthetic snapshot fact</a></p></section></main>',1),encoding='utf-8')
    marker='<!-- enterprise-reference-binding -->'
    card=pub/'index.html';body=card.read_text(encoding='utf-8')
    if marker not in body:
        extra=marker+'<section><h2>Reference data binding and evidence</h2><p><a href="README.md">Profile, usage and limits</a> | <a href="instance.schema.json">JSON Schema</a> | <a href="validate_examples.py">Example validator</a> | <a href="fixture-results.json">30 fixture checks</a> | <a href="/enterprise/research/'+mid+'/">Actual provider evidence and audit scope</a></p><p>Codex authored the structured specification. Claude and Grok supplied independent browser memos. Claude separately audited a semantic summary; full JSON and code were validated locally by Codex. Production HRIS, IAM and legal conformance are outside this reference implementation.</p><ul>'+''.join('<li><a href="'+p.name+'">'+p.name+'</a></li>' for p in sorted(pub.glob('example-*.json')) )+'</ul></section>'
        assert '</main>' in body
        card.write_text(body.replace('</main>',extra+'</main>',1),encoding='utf-8')
    print(json.dumps({'public_evidence_files':len(files)+2,'path':str(out)}))

if __name__=='__main__':main()
