#!/usr/bin/env python3
"""Publish an explicitly reviewed original companion through the model publisher.

Called by publish_model_research.py --companion-package PATH --contour EM-...
No new universal World Model identity or parent subtype is manufactured.
"""
from pathlib import Path
import argparse,datetime,hashlib,html,json,re,shutil,zipfile
from publish_model_research import render_tree
from build_enterprise_program import page
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--companion-package',type=Path,required=True);ap.add_argument('--contour',required=True);ap.add_argument('--site-root',type=Path,default=ROOT.parent.parent/'ver.cy');a=ap.parse_args()
    source=a.companion_package.resolve();spec=read(source/'spec.json');meta=spec['metaModel'];review=read(source/'review.json')
    slug=meta['id'];version=meta['version'];mid=meta['registryId'];relative='/models/'+slug+'/';immutable=relative+'versions/'+version+'/'
    if not all(part and all(c.isalnum() or c in '.-' for c in part) for part in [slug,version]):raise ValueError('Unsafe publication name')
    if meta['kind']!='companion-contract' or mid!='vr.profile.'+slug:raise ValueError('Explicit original companion identity required')
    if re.fullmatch(r'EM-[A-Z]+-[0-9]+',a.contour) is None:raise ValueError('Invalid research contour')
    if spec['canonicalUrl']!='https://ver.cy'+immutable+'spec.json':raise ValueError('Canonical version URL mismatch')
    if spec['composition']['runtimeImports']!=[]:raise ValueError('This bounded publisher supports semantic references only')
    if review['disposition']!='publish bounded reviewable draft' or set(review['providers'])!={'Claude','Grok'} or any(x['status']!='complete' or x['disposition']!='ACCEPT WITH LIMITS' for x in review['providers'].values()):raise ValueError('Independent terminal review dispositions required')
    for n,d in (review['candidateFiles'] | review['reviewedFiles']).items():
        p=(source/n).resolve()
        if not p.is_relative_to(source) or sha(p)!=d:raise ValueError('Reviewed candidate changed: '+n)
    if not read(source/'test-results.json')['passed'] or read(source/'acceptance-results.json')['passed']!=3:raise ValueError('Executed implementation and three native fixtures required')
    # IDs are unambiguous across the complete logical tree.
    ids=[];layers=[];findings=[]
    for b in spec['structure']['bundles']:
        ids.append(b['id']);layers+=b['layers']
        for l in b['layers']:
            ids.append(l['id']);findings+=l['findings']
            for f in l['findings']:
                ids.append(f['id'])
                for group in ['questions','artifacts','actions']:ids.extend(x['id'] for x in f[group])
    if len(ids)!=len(set(ids)) or len(findings)<15:raise ValueError('Incomplete or colliding question tree')
    parent=ROOT/'publications'/slug;target=parent/'versions'/version
    if target.exists():raise ValueError('Immutable release already exists')
    parent.mkdir(parents=True,exist_ok=True);shutil.copytree(source,target,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    shutil.copyfile(ROOT/'LICENSE',target/'LICENSE')
    manifest={'format':'vercy-enterprise-companion-publication','runtimeId':mid,'version':version,'status':'published','researchAssurance':'reviewable-draft','contour':a.contour,'contourStatus':'partial','specUrl':'https://ver.cy'+immutable+'spec.json','specDigest':'sha256:'+sha(target/'spec.json'),'pageUrl':'https://ver.cy'+relative,'packageUrl':'https://ver.cy'+immutable+slug+'-'+version+'.zip','semanticFingerprint':None,'review':'review.json','nativeScope':'Three synthetic new Dimensions; own companion identity, optional semantic-only parent, explicit nested validator and trusted previous root required.'}
    dump(target/'profile-manifest.json',manifest)
    body='<nav><a href="/models/?q='+html.escape(a.contour)+'">← Catalogue</a> · <a href="/enterprise/models/'+a.contour.lower()+'/">Research contour</a></nav>'
    body+='<p class="v-eyebrow">'+html.escape(a.contour)+' · Enterprise profiles · Published '+version+'</p><h1>'+html.escape(meta['name'])+'</h1><p class="v-lede">'+html.escape(spec['model']['purpose'])+'</p>'
    st=spec['statistics'];body+='<p><strong>'+str(st['bundles'])+' bundles · '+str(st['layers'])+' layers · '+str(st['findings'])+' findings · '+str(st['questions'])+' questions</strong></p>'
    body+='<nav class="actions"><a href="#structure">Explore structure</a><a href="'+immutable+'spec.json">Specification and structure JSON</a><a href="'+immutable+slug+'-'+version+'.zip">Download model package</a><a href="'+immutable+'AGENTS.md">Agent instructions</a><a href="'+immutable+'model-spec.md">Semantic contract</a></nav>'
    body+='<section class="box"><h2>Use in a Company Dimension</h2><p>Start with a pinned external claim, a file capture, an acquisition activity and an attributed account. Add evidence relationships and purpose-qualified assessments when needed. The package includes three synthetic examples, a closed schema, a reference validator and native installation checks.</p><p><strong>Research assurance: reviewable-draft.</strong> This is a bounded original companion. Truth, permissions and source independence are never inferred. A trusted host must authenticate actors, hold the latest complete register and invoke the companion validator. <a href="'+immutable+'adoption-limits.md">Adoption limits</a>.</p></section>'
    body+='<h2 id="structure">Bundles → Layers → Findings → Questions</h2><p>Collect the expected evidence for each question. Unknown context remains explicit. Listed actions confer no operational permission.</p><div class="actions"><button id="expand" type="button">Expand all</button><button id="collapse" type="button">Collapse all</button></div>'+render_tree(spec)
    body+='<section class="box"><h2>Research and validation</h2><p>Claude and Grok performed independent studies and separate static implementation audits. Executed tests and native checks are recorded separately. <a href="/enterprise/research/'+a.contour.lower()+'/">Research dossier</a> · <a href="'+immutable+'review.md">Review and limits</a> · <a href="'+immutable+'test-results.json">Tests</a> · <a href="'+immutable+'acceptance-results.json">Native acceptance</a> · <a href="'+immutable+'checksums.json">Checksums</a>.</p><p>Catalogue identity: <code>'+mid+'</code>. '+a.contour+' remains a broader, partially covered research contour. Parent models are semantic references; no subtype or whole-parent conformance is asserted.</p></section>'
    body+='<style>.bundle,.layer{border:1px solid var(--v-line);border-radius:12px;padding:18px;margin:16px 0}.bundle>summary,.layer>summary{cursor:pointer;display:flex;gap:14px;flex-wrap:wrap}.bundle>summary span,.layer>summary span{color:var(--v-muted)}.finding{border-top:1px solid var(--v-line);padding:20px 6px}.finding-head{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}.finding h4{font-size:1.2rem}.finding h5{font-size:1rem;margin:18px 0 8px}.artifact-list li span{display:block;color:var(--v-muted)}.question-list small{color:var(--v-cyan);margin-left:8px}.answer-shape{margin:10px 0}.answer-shape summary{cursor:pointer}button{background:var(--v-panel);color:var(--v-text);border:1px solid var(--v-line);border-radius:8px;padding:10px 16px;cursor:pointer}code{overflow-wrap:anywhere}@media(max-width:600px){.bundle,.layer{padding:10px}}</style><script>document.getElementById("expand").onclick=()=>document.querySelectorAll(".bundle,.layer,.answer-shape").forEach(x=>x.open=true);document.getElementById("collapse").onclick=()=>document.querySelectorAll(".bundle,.layer,.answer-shape").forEach(x=>x.open=false);document.querySelectorAll(".bundle").forEach(x=>x.open=true);</script>'
    title=meta['name']+' · '+a.contour
    content=page('en',title,spec['model']['purpose'],relative,body,[('en',relative)],datetime.datetime.now(datetime.timezone.utc).date().isoformat())
    (parent/'index.html').write_text(content,encoding='utf-8',newline='\n')
    (target/'index.html').write_text(page('en',title+' · '+version,spec['model']['purpose'],immutable,body,[('en',immutable)],datetime.datetime.now(datetime.timezone.utc).date().isoformat()),encoding='utf-8',newline='\n')
    dump(target/'checksums.json',{'algorithm':'sha256','files':{str(p.relative_to(target)).replace('\\','/'):sha(p) for p in sorted(target.rglob('*')) if p.is_file()},'excludes':['checksums.json',slug+'-'+version+'.zip']})
    with zipfile.ZipFile(target/(slug+'-'+version+'.zip'),'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(target.rglob('*')):
            if p.is_file() and p.suffix!='.zip':
                info=zipfile.ZipInfo(slug+'-'+version+'/'+str(p.relative_to(target)).replace('\\','/'),date_time=(2026,9,21,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,p.read_bytes())
    # Reuse the established companion catalogue shape, replacing every identity
    # and artifact path explicitly. It is an association, never a parent edge.
    entry=read(ROOT/'publications/enterprise-fact-authority/catalogue-entry.json')
    entry.update(registry_id=mid,model_id=a.contour,name=meta['name'],alternate_names=[a.contour,meta['name'],'Assertion provenance','Evidence and confidence'],code=slug,version=version,domain=['Enterprise','Provenance','Evidence'],tags=[a.contour,'provenance','evidence','assertion','confidence'],page_url=relative,source_url='https://ver.cy/enterprise/research/'+a.contour.lower()+'/',spec_url=immutable+'spec.json',agents_url=immutable+'AGENTS.md',yaml_url=immutable+'spec.json',spec_digest=manifest['specDigest'],structure_url=immutable+'spec.json',package_url=immutable+slug+'-'+version+'.zip',aligned_model_ids=['vr.wm-xct-012','vr.wm-xct-026','vr.wm-xct-028'],purpose=a.contour+': '+spec['model']['purpose'],namespace_uri='urn:vercy:model:'+mid,source_version=version,provenance='Scoped independent Claude/Grok studies and frozen implementation audits; original Codex synthesis.')
    dump(parent/'catalogue-entry.json',entry)
    shutil.copytree(parent,a.site_root/'models'/slug,dirs_exist_ok=True)
    cards=read(a.site_root/'models/catalog-index.json');cards=[x for x in cards if x['id']!=mid]
    cards.append({'id':mid,'name':meta['name'],'version':version,'family':entry['family'],'category':entry['category'],'industry':entry['industry'],'domain':entry['domain'],'tags':entry['tags'],'url':relative,'status':'published','sourceUrl':entry['source_url']});dump(a.site_root/'models/catalog-index.json',cards)
    print(json.dumps({'publication':manifest,'statistics':st}));return 0

if __name__=='__main__':raise SystemExit(main())
