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
    ap=argparse.ArgumentParser();ap.add_argument('--companion-package',type=Path,required=True);ap.add_argument('--contour',required=True);ap.add_argument('--site-root',type=Path,default=ROOT.parent.parent/'ver.cy');ap.add_argument('--allow-deferred-provider-audit',action='store_true',help='Explicit reviewable-draft exception under enterprise AGENTS.md; requires completed independent studies, a completed accepting audit and visible recovery holds. Never accepts a BLOCK verdict.');a=ap.parse_args()
    source=a.companion_package.resolve();spec=read(source/'spec.json');meta=spec['metaModel'];review=read(source/'review.json')
    slug=meta['id'];version=meta['version'];mid=meta['registryId'];relative='/models/'+slug+'/';immutable=relative+'versions/'+version+'/'
    if not all(part and all(c.isalnum() or c in '.-' for c in part) for part in [slug,version]):raise ValueError('Unsafe publication name')
    if meta['kind']!='companion-contract' or mid!='vr.profile.'+slug:raise ValueError('Explicit original companion identity required')
    if re.fullmatch(r'EM-[A-Z]+-[0-9]+',a.contour) is None:raise ValueError('Invalid research contour')
    if spec['canonicalUrl']!='https://ver.cy'+immutable+'spec.json':raise ValueError('Canonical version URL mismatch')
    if spec['composition']['runtimeImports']!=[]:raise ValueError('This bounded publisher supports semantic references only')
    if review['disposition']!='publish bounded reviewable draft' or set(review['providers'])!={'Claude','Grok'}:raise ValueError('Explicit independent provider dispositions required')
    pending=[name for name,x in review['providers'].items() if x['status']!='complete']
    complete=[x for x in review['providers'].values() if x['status']=='complete']
    if not complete or any(x['disposition']!='ACCEPT WITH LIMITS' for x in complete):raise ValueError('No accepting audit or unresolved provider verdict')
    if pending:
        # Enterprise AGENTS.md explicitly permits a visible draft with an unavailable pass.
        # A failed or blocking semantic review is not an availability exception.
        if not a.allow_deferred_provider_audit or review.get('contourStatus')!='partial' or not review.get('publicationHolds') or not review.get('auditSummary'):raise ValueError('Unavailable audit needs explicit partial-publication exception and visible holds')
        if set(review.get('studies',{}))!={'Claude','Grok'} or any(x.get('status')!='complete' for x in review['studies'].values()):raise ValueError('Both independent research studies must already be complete')
        for name in pending:
            x=review['providers'][name]
            if x['status']!='unavailable-browser' or x['disposition']!='NOT REVIEWED' or not x.get('recovery') or not x.get('manifest',{}).get('reason'):raise ValueError('Only documented browser unavailability can defer an audit')
    for n,d in (review['candidateFiles'] | review['reviewedFiles']).items():
        p=(source/n).resolve()
        if not p.is_relative_to(source) or sha(p)!=d:raise ValueError('Reviewed candidate changed: '+n)
    if not read(source/'test-results.json')['passed'] or read(source/'acceptance-results.json')['passed']!=3:raise ValueError('Executed implementation and three acceptance scenarios required')
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
    manifest={'format':'vercy-enterprise-companion-publication','runtimeId':mid,'version':version,'status':'published','researchAssurance':'reviewable-draft','contour':a.contour,'contourStatus':'partial','specUrl':'https://ver.cy'+immutable+'spec.json','specDigest':'sha256:'+sha(target/'spec.json'),'pageUrl':'https://ver.cy'+relative,'packageUrl':'https://ver.cy'+immutable+slug+'-'+version+'.zip','semanticFingerprint':None,'review':'review.json','nativeScope':review.get('nativeScope','Three synthetic new Dimensions; own companion identity, explicit nested validation and trusted host state required. Exact binding limits are in bindings/native-v3.md.')}
    if pending:manifest.update(deferredProviderAudits=pending,publicationHolds=review['publicationHolds'])
    if review.get('adoptionNotice'):
        required=review.get('requiredReading',['AGENTS.md','model-spec.md','adoption-limits.md','publication-addendum.md'])
        for n in required:
            p=(target/n).resolve()
            if not p.is_relative_to(target.resolve()) or not p.is_file():raise ValueError('Missing required adoption reading: '+n)
        manifest.update(adoptionNotice=review['adoptionNotice'],requiredReading=['https://ver.cy'+immutable+n for n in required])
    if meta.get('logicalKind')=='embedded-value-profile':
        manifest['nativeScope']='Three synthetic new Dimensions; embedded values on existing hosts, no independent quantity instance identity. Explicit nested/pair validation and trusted host state required. Read bindings/native-v3.md and the publication addendum.'
    dump(target/'profile-manifest.json',manifest)
    body='<nav><a href="/models/?q='+html.escape(a.contour)+'">← Catalogue</a> · <a href="/enterprise/models/'+a.contour.lower()+'/">Research contour</a></nav>'
    body+='<p class="v-eyebrow">'+html.escape(a.contour)+' · Enterprise profiles · Published '+version+'</p><h1>'+html.escape(meta['name'])+'</h1><p class="v-lede">'+html.escape(spec['model']['purpose'])+'</p>'
    st=spec['statistics'];body+='<p><strong>'+str(st['bundles'])+' bundles · '+str(st['layers'])+' layers · '+str(st['findings'])+' findings · '+str(st['questions'])+' questions</strong></p>'
    body+='<nav class="actions"><a href="#structure">Explore structure</a><a href="'+immutable+'spec.json">Specification and structure JSON</a><a href="'+immutable+slug+'-'+version+'.zip">Download model package</a><a href="'+immutable+'AGENTS.md">Agent instructions</a><a href="'+immutable+'model-spec.md">Semantic contract</a></nav>'
    if pending:body+='<section class="box"><h2>Independent audit still pending</h2><p>'+html.escape(review['auditSummary'])+'</p><ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in review['publicationHolds'])+'</ul></section>'
    if review.get('adoptionNotice'):
        body+='<section class="box"><h2>Required adoption limits</h2><p>'+html.escape(review['adoptionNotice'])+'</p><p><a href="'+immutable+'publication-addendum.md">Publication addendum and exact limits</a></p></section>'
    catalogue=spec.get('catalogue',{})
    adoption=catalogue.get('adoption','Start with a pinned external claim, a file capture, an acquisition activity and an attributed account. Add evidence relationships and purpose-qualified assessments when needed. The package includes three synthetic examples, a closed schema, a reference validator and native installation checks.')
    limits=catalogue.get('limits','Truth, permissions and source independence are never inferred. A trusted host must authenticate actors, hold the latest complete register and invoke the companion validator.')
    body+='<section class="box"><h2>Use in a Company Dimension</h2><p>'+html.escape(adoption)+'</p><p><strong>Research assurance: reviewable-draft.</strong> This is a bounded original companion. '+html.escape(limits)+' <a href="'+immutable+'adoption-limits.md">Adoption limits</a>.</p></section>'
    body+='<h2 id="structure">Bundles → Layers → Findings → Questions</h2><p>Collect the expected evidence for each question. Unknown context remains explicit. Listed actions confer no operational permission.</p><div class="actions"><button id="expand" type="button">Expand all</button><button id="collapse" type="button">Collapse all</button></div>'+render_tree(spec)
    audit_summary=review.get('auditSummary','Claude and Grok performed independent studies and separate static implementation audits.')
    body+='<section class="box"><h2>Research and validation</h2><p>'+html.escape(audit_summary)+' Executed tests and native checks are recorded separately. <a href="/enterprise/research/'+a.contour.lower()+'/">Research dossier</a> · <a href="'+immutable+'review.md">Review and limits</a> · <a href="'+immutable+'test-results.json">Tests</a> · <a href="'+immutable+'acceptance-results.json">Native acceptance</a> · <a href="'+immutable+'checksums.json">Checksums</a>.</p><p>Catalogue identity: <code>'+mid+'</code>. '+a.contour+' remains a broader, partially covered research contour. Parent models are semantic references; no subtype or whole-parent conformance is asserted.</p></section>'
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
    if catalogue:
        entry.update(alternate_names=[a.contour,meta['name'],*catalogue['alternateNames']],domain=catalogue['domain'],tags=[a.contour,*catalogue['tags']],aligned_model_ids=['vr.'+x['id'].lower() for x in spec['composition']['semanticReferences']])
    if pending:entry['provenance']=audit_summary+' Original Codex synthesis; reviewable draft with explicit recovery holds.'
    if review.get('adoptionNotice'):
        entry['installation_requirements']=entry.get('installation_requirements','')+' '+review['adoptionNotice']+' Required reading: '+'https://ver.cy'+immutable+'publication-addendum.md'
    dump(parent/'catalogue-entry.json',entry)
    shutil.copytree(parent,a.site_root/'models'/slug,dirs_exist_ok=True)
    cards=read(a.site_root/'models/catalog-index.json');cards=[x for x in cards if x['id']!=mid]
    cards.append({'id':mid,'name':meta['name'],'version':version,'family':entry['family'],'category':entry['category'],'industry':entry['industry'],'domain':entry['domain'],'tags':entry['tags'],'url':relative,'status':'published','sourceUrl':entry['source_url']});dump(a.site_root/'models/catalog-index.json',cards)
    print(json.dumps({'publication':manifest,'statistics':st}));refresh_cards(a.site_root);return 0


def refresh_cards(site_root) -> None:
    """Rebuild the catalogue card store so every published model has its card.

    Owner decision 2026-10-04: card pages render from ver.cy/models/cards/,
    built by ver.cy/tools/build_cards.py from the sources this step writes.
    """
    import os, subprocess, sys
    from pathlib import Path as _Path
    builder = _Path(site_root) / "tools" / "build_cards.py"
    if builder.is_file():
        subprocess.run([sys.executable, str(builder)], check=True, env={**os.environ, "PYTHONUTF8": "1"})


if __name__=='__main__':raise SystemExit(main())
