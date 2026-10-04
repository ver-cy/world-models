#!/usr/bin/env python3
"""Publish a sanitized enterprise research program, without inventing model availability.

v2 (2026-09-21): standard site shell (site.css + assets/site-shell.js header/footer)
and the site language rule: English at /enterprise/, full copies at
/ru|es|el|zh/enterprise/ for the index, English and Russian copies for the 111
per-contour briefs, hreflang everywhere. Translations live in
research/enterprise/i18n/*.json; any missing key falls back to the Russian
source text in registry.json, so new research content publishes immediately
and gains translations later. CLI contract, machine artifacts and the
111-contour assertion are unchanged.
"""
from __future__ import annotations
import argparse, html, json, re, shutil
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
LANGS=['en','ru','es','el','zh']
BRIEF_LANGS=['en','ru']
OG_LOCALE={'en':'en_US','ru':'ru_RU','es':'es_ES','el':'el_GR','zh':'zh_CN'}

def read(p): return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Site plain-punctuation rule: rendered pages carry no em/en dashes, curly
# quotes or guillemets even when authored research text does.
PLAIN={'«':'"','»':'"','—':'-','–':'-','‘':"'",'’':"'",'“':'"','”':'"'}
def plain(x):
    if isinstance(x,str):
        for k,v in PLAIN.items(): x=x.replace(k,v)
        return x
    if isinstance(x,list): return [plain(i) for i in x]
    return x
def e(x): return html.escape(plain(str(x)),quote=True)
def li(items): return '<ul>'+''.join('<li>'+e(x)+'</li>' for x in items)+'</ul>'

# Russian is the authoring language of the research registry; these are the
# source strings every ui.<lang>.json translates. Keys missing from a
# translation file render in Russian rather than breaking the build.
UI_RU={
 'title_index':'Enterprise: реестр моделей компании',
 'desc_index':'Модели для Измерения компании, 111 индивидуальных исследовательских заданий, опубликованные компоненты и статусы Claude/Grok.',
 'eyebrow':'Vercy / Enterprise',
 'h1':'Измерение компании.<br>От небольшой команды до группы компаний.',
 'lede':'Реестр из 111 исследовательских направлений: 82 предметные модели, 18 ландшафтов, 10 общих контрактов и основа композиции. Для каждого задана граница, вопросы, инварианты и приёмочный сценарий.',
 'box_start':'Можно начать сейчас.',
 'box_start_p':'Ниже доступны подборки действующих опубликованных моделей. Исследовательская программа уточняет их совместимость и создаёт недостающие модели. Опубликованная спецификация может иметь зрелость reviewable-draft; её ограничения видны в карточке.',
 'act_create':'Создать Измерение','act_registry':'Открыть реестр','act_json':'JSON','act_contract':'Контракт исследования','act_status':'Статусы',
 'h2_start':'Начните с нужных компонентов',
 'start_p':'Передайте своему ИИ-агенту этот текст. Данные компании и правила доступа остаются в вашем Измерении.',
 'dl_prompt':'Скачать инструкцию','dl_pins':'Подборки с версиями и контрольными суммами','dl_agents':'Контракт для агента',
 'profiles_note':'Подборки проверяют наличие и целостность пакетов. Совместимость конкретных профилей и отношения с локальными мастер-системами проверяются при установке. HR, договоры и юрлицо добавляются только при необходимости.',
 'profile_components':'{n} опубликованных компонентов с проверенными версиями и SHA-256.',
 'h2_extend':'Как расширять Измерение',
 'recipes_note':'Расширенная исследовательская подборка. Она не объявляется полностью готовым установочным пакетом.',
 'h2_registry':'Реестр и индивидуальные задания',
 'registry_p':'Queued означает, что подготовлено задание. Researching означает начатый проход. Завершение и публикация подтверждаются отдельно.',
 'search_ph':'Компания, проект, договор, аналитика…','search_aria':'Поиск по реестру','kind_aria':'Вид направления','kinds_all':'Все виды',
 'count_initial':'111 направлений','count_shown':'Показано: {n} из 111',
 'h2_order':'Порядок исследования и публикации',
 'order_p':'Claude и Grok независимо исследуют границу и источники. Их выводы сопоставляются, разногласия сохраняются, затем проверяются схема, семантика, зависимости и сценарии. Готовый результат публикуется сразу с честным статусом зрелости. Реестр не утверждает, что все 111 исследований уже выполнены.',
 'notice_h2':'Готовность к работе с данными',
 'notice_p':'Спецификации и стартовые подборки доступны. Совместная автоматическая установка ещё требует доработки: успешное скачивание не означает, что Измерение прошло проверку. <a href="/models/wm-org-017-performance-objective-review/NATIVE-REFERENCE.md">Отдельный проверенный пример модели оценки</a> уже содержит объект и запись состояния. Следующим шагом исследуется и дорабатывается общее ядро установки.',
 'b_published':'Опубликованные результаты','b_open':'Открыть результат',
 'b_boundary':'Предметная граница и кандидатные типы','b_questions':'Вопросы глубокого исследования',
 'b_invariants':'Проверяемые инварианты','b_scenario':'Сквозной приёмочный сценарий',
 'b_negative':'Отрицательный пример','b_tracks':'Сопоставляемые подходы',
 'b_candidates':'Кандидаты в действующем каталоге',
 'b_no_candidates':'Граница и маршрут reuse / extension / new model ещё не выбраны.',
 'b_requirements':'Требования к результату',
 'b_req_p':'Каждая карточка исполняется вместе с <a href="/enterprise/RESEARCH-PROTOCOL.md">полным контрактом исследования</a>: определения, поля и кратности, жизненный цикл, источники, мастерство данных, права, пять граней объекта, минимум восемь инвариантов, положительные и отрицательные примеры, зависимости, миграция и ограничения применимости.',
 'b_brief_json':'Машиночитаемое задание JSON',
 'b_no_version':'без версии','b_installable':'доступна для установки','b_not_installable':'не устанавливается автоматически','b_no_runtime':'отсутствует в runtime',
 'b_candidate_small':'Смысловое соответствие требует исследования границ; наличие опубликованной модели не завершает эту карточку.',
 'b_back':'Реестр Enterprise','note_ru':'Заметка исследования (по-русски):',
 'states.queued':'В очереди исследования','states.researching':'Исследуется',
 'states.published-partial':'Частично опубликовано; исследование продолжается','states.published':'Результат опубликован',
 'states.reuse-verified':'Переиспользование проверено','states.blocked':'Требует разрешения проблемы','states.complete':'Исследование завершено',
 'kinds.subject':'Предметная модель','kinds.landscape':'Ландшафт','kinds.contract':'Общий контракт','kinds.foundation':'Основа композиции',
 'prompt':'Прочитай https://ver.cy/AGENTS.md и https://ver.cy/enterprise/AGENTS.md. Создай в моём рабочем пространстве Измерение компании. Выбери минимальную подборку из https://ver.cy/enterprise/starter-selections.json по реальным потребностям, проверь текущие опубликованные версии и зависимости. Раздели человека, трудовые отношения, членство, назначения и юрлица; сохрани источники, права и неизвестные факты. Уточни только недостающие сведения о назначении, владельце и доступе. Данные компании храни в согласованном месте; их публикация на ver.cy не подразумевается.',
}

STYLE='''.enterprise{max-width:1160px;margin:auto;padding:56px 24px 96px}
.enterprise h1{font-size:clamp(32px,5vw,56px);line-height:1.08;margin:14px 0 18px}
.enterprise .v-lede{font-size:19px;color:var(--v-muted);max-width:var(--v-reading,780px)}
.enterprise h2{margin-top:2.2em;font-size:clamp(22px,3vw,30px)}
.enterprise .muted,.enterprise small{color:var(--v-muted)}
.enterprise .actions{display:flex;gap:18px;flex-wrap:wrap;margin:20px 0}
.enterprise article,.enterprise .box,.enterprise details{border:1px solid var(--v-line);border-radius:12px;padding:20px;margin:14px 0;background:var(--v-panel)}
.enterprise .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
.enterprise .tag{display:inline-block;border-radius:5px;background:var(--v-line);padding:3px 10px;font-size:13px;margin:0 6px 6px 0}
.enterprise .state{color:var(--v-green,#b9ecd4)}
.enterprise input,.enterprise select{background:var(--v-panel);color:var(--v-text);border:1px solid var(--v-line);border-radius:7px;padding:12px;font-size:16px}
.enterprise input{min-width:260px;flex:1}
.enterprise summary{cursor:pointer;font-weight:650}
.enterprise pre{white-space:pre-wrap;overflow-wrap:anywhere;background:var(--v-bg);border:1px solid var(--v-line);padding:18px;border-radius:8px}
.enterprise .v-note{border-left:2px solid var(--v-cyan);padding-left:14px;color:var(--v-muted);font-size:15px}
.enterprise code{overflow-wrap:anywhere}
.enterprise a:focus,.enterprise input:focus,.enterprise select:focus,.enterprise summary:focus{outline:2px solid var(--v-cyan);outline-offset:3px}
.enterprise [hidden]{display:none!important}
.enterprise article p{color:var(--v-muted)}
.enterprise article h3{margin:8px 0}
'''

def load_i18n(src):
    ui={'ru':{'strings':UI_RU,'recipes':{},'profiles':{}}}
    units={'ru':{}}
    d=src/'i18n'
    for lang in LANGS:
        if lang=='ru': continue
        up=d/('ui.%s.json'%lang);np=d/('units.%s.json'%lang)
        ui[lang]=read(up) if up.exists() else {'strings':{},'recipes':{},'profiles':{}}
        units[lang]=read(np) if np.exists() else {}
    return ui,units

def page(lang,title,description,path,body,hreflangs,updated,script=''):
    """Standard site page: canonical head contract + site shell (header/footer via /assets/site-shell.js)."""
    canon='https://ver.cy'+path
    alt=''.join('<link rel="alternate" hreflang="%s" href="https://ver.cy%s">'%(hl,hp) for hl,hp in hreflangs)
    alt+='<link rel="alternate" hreflang="x-default" href="https://ver.cy%s">'%dict(hreflangs)['en']
    data={'@context':'https://schema.org','@type':'CollectionPage','name':title,'description':description,'url':canon,'isPartOf':{'@type':'WebSite','name':'Vercy','url':'https://ver.cy/'},'dateModified':updated,'inLanguage':lang}
    return ('<!doctype html>\n<html lang="'+lang+'"><head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
      '<title>'+e(title)+' · Vercy</title>\n<meta name="description" content="'+e(description)+'">\n'
      '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<meta name="theme-color" content="#0b1c2c">\n'
      '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n'
      '<link rel="canonical" href="'+canon+'">\n'+alt+'\n'
      '<meta property="og:type" content="website"><meta property="og:title" content="'+e(title)+' · Vercy"><meta property="og:description" content="'+e(description)+'"><meta property="og:url" content="'+canon+'"><meta property="og:site_name" content="Vercy"><meta property="og:locale" content="'+OG_LOCALE[lang]+'">\n'
      '<meta name="twitter:card" content="summary"><meta name="twitter:title" content="'+e(title)+' · Vercy"><meta name="twitter:description" content="'+e(description)+'">\n'
      '<link rel="stylesheet" href="/assets/site.css">\n<style>'+STYLE+'</style>\n'
      '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script>\n'
      '</head><body>\n<main class="enterprise">\n'+body+'\n</main>\n<script src="/assets/site-shell.js"></script>'+script+'\n</body></html>\n')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--site-root',type=Path,default=ROOT.parent.parent/'ver.cy');a=ap.parse_args()
    src=ROOT/'research/enterprise';out=a.site_root/'enterprise';out.mkdir(parents=True,exist_ok=True)
    reg=read(src/'registry.json');queue=read(src/'queue.json');pins=read(src/'starter-selections.json');runtime=read(a.site_root/'models/runtime-index.json')
    ui,units_i18n=load_i18n(src)
    by={m['modelId']:m for m in runtime['models']};qs={u['id']:u for u in queue['units']}
    assert len(reg['units'])==111 and len(qs)==111 and {u['id'] for u in reg['units']}==set(qs)
    updated=str(queue['updated_at'])[:10]

    def t(lang,key):
        return plain(ui.get(lang,{}).get('strings',{}).get(key) or UI_RU[key])
    def uf(lang,uid,field,default):
        v=units_i18n.get(lang,{}).get(uid,{}).get(field)
        return plain(v if v not in (None,'',[]) else default)
    def base(lang): return '/enterprise/' if lang=='en' else '/%s/enterprise/'%lang
    def outdir(lang): return out if lang=='en' else a.site_root/lang/'enterprise'
    def ru_note(lang,text):
        if not text: return ''
        if lang=='ru': return '<p>'+e(text)+'</p>'
        return '<p class="v-note">'+e(t(lang,'note_ru'))+' '+e(text)+'</p>'

    index_hreflangs=[(l,base(l)) for l in LANGS]
    public_units=[]
    cards={l:[] for l in LANGS}
    for unit in reg['units']:
        u=dict(unit);q=qs[u['id']];uid=u['id'];slug=uid.lower()
        candidates=[]
        for c in u.get('vercy_candidates',[]):
            m=by.get(c['model_id']);candidates.append(dict(c,runtime=None if m is None else {k:m.get(k) for k in ['id','modelId','name','version','status','installable','pageUrl','specUrl','agentsUrl','digest','requires','unresolvedRequires']}))
        u['vercy_candidates']=candidates;u['research_progress']=q;u['brief_url']='https://ver.cy/enterprise/models/'+slug+'/';public_units.append(u)
        brief_hreflangs=[(l,base(l)+'models/'+slug+'/') for l in BRIEF_LANGS]
        for lang in BRIEF_LANGS:
            target=outdir(lang)/'models'/slug;target.mkdir(parents=True,exist_ok=True)
            name=uf(lang,uid,'name',u['name']);scope=uf(lang,uid,'scope',u['scope'])
            state=t(lang,'states.'+q['status']);kind=t(lang,'kinds.'+u['kind'])
            candidate_html=''
            for c in candidates:
                m=c['runtime'];mid=c['model_id']
                candidate_html+='<li>'+('<a href="'+e(m['pageUrl'])+'">'+e(mid)+' · '+e(m['name'])+'</a> · '+e(m['version'] or t(lang,'b_no_version'))+' · '+(t(lang,'b_installable') if m['installable'] else t(lang,'b_not_installable')) if m else e(mid)+' · '+t(lang,'b_no_runtime'))+'<br><small>'+e(t(lang,'b_candidate_small'))+'</small></li>'
            body='<nav class="v-breadcrumb"><a class="v-breadcrumb-link" href="'+('/' if lang=='en' else '/%s/'%lang)+'">Vercy</a> · <a class="v-breadcrumb-link" href="'+base(lang)+'">'+e(t(lang,'b_back'))+'</a></nav>'
            body+='<p class="muted">'+e(uid)+' · '+e(kind)+' · '+e(u['wave'])+'</p><h1>'+e(name)+'</h1><p class="v-lede">'+e(scope)+'</p><p class="state">'+e(state)+'</p><p>Claude: '+e(q['claude_status'])+'; Grok: '+e(q['grok_status'])+'.</p>'
            if q['publication_urls']:body+='<h2>'+e(t(lang,'b_published'))+'</h2><ul>'+''.join('<li><a href="'+e(url)+'">'+e(t(lang,'b_open'))+'</a></li>' for url in q['publication_urls'])+'</ul>'
            body+=ru_note(lang,q.get('remaining_scope',''))
            body+='<h2>'+e(t(lang,'b_boundary'))+'</h2>'+li(u['candidate_types'])
            body+='<h2>'+e(t(lang,'b_questions'))+'</h2>'+li(uf(lang,uid,'specific_questions',u['specific_questions']))
            body+='<h2>'+e(t(lang,'b_invariants'))+'</h2>'+li(uf(lang,uid,'proposed_invariants',u['proposed_invariants']))
            body+='<h2>'+e(t(lang,'b_scenario'))+'</h2><p>'+e(uf(lang,uid,'acceptance_scenario',u['acceptance_scenario']))+'</p>'
            body+='<h2>'+e(t(lang,'b_negative'))+'</h2><p>'+e(uf(lang,uid,'negative_case',u['negative_case']))+'</p>'
            body+='<h2>'+e(t(lang,'b_tracks'))+'</h2>'+li(uf(lang,uid,'comparison_tracks',u['comparison_tracks']))
            body+='<h2>'+e(t(lang,'b_candidates'))+'</h2>'+('<ul>'+candidate_html+'</ul>' if candidates else '<p>'+e(t(lang,'b_no_candidates'))+'</p>')
            body+='<h2>'+e(t(lang,'b_requirements'))+'</h2><p>'+t(lang,'b_req_p')+'</p><p><a href="/enterprise/models/'+slug+'/brief.json">'+e(t(lang,'b_brief_json'))+'</a></p>'
            (target/'index.html').write_text(page(lang,name,scope,base(lang)+'models/'+slug+'/',body,brief_hreflangs,updated),encoding='utf-8')
        dump(out/'models'/slug/'brief.json',u)
        for lang in LANGS:
            name=uf(lang,uid,'name',u['name']);scope=uf(lang,uid,'scope',u['scope'])
            state=t(lang,'states.'+q['status']);kind=t(lang,'kinds.'+u['kind'])
            href=(base(lang) if lang in BRIEF_LANGS else '/enterprise/')+'models/'+slug+'/'
            cards[lang].append('<article data-kind="'+e(u['kind'])+'" data-state="'+e(q['status'])+'" data-search="'+e((uid+' '+u['name']+' '+name+' '+scope+' '+' '.join(u['candidate_types'])).lower())+'"><span class="tag">'+e(uid)+'</span><span class="tag">'+e(kind)+'</span><h3><a href="'+href+'">'+e(name)+'</a></h3><p>'+e(scope)+'</p><p class="state">'+e(state)+'</p></article>')

    public=dict(reg,units=public_units,updated_at=queue['updated_at'],runtime_generated_at=runtime['generatedAt']);dump(out/'registry.json',public);dump(out/'queue.json',queue);dump(out/'starter-selections.json',pins)
    shutil.copy2(src/'RESEARCH-PROTOCOL.md',out/'RESEARCH-PROTOCOL.md')
    for lang in LANGS:
        prompt=t(lang,'prompt')
        fn='start-company-dimension.txt' if lang=='en' else 'start-company-dimension.%s.txt'%lang
        (out/fn).write_text(prompt+'\n',encoding='utf-8')
    (out/'AGENTS.md').write_text('''# Vercy Enterprise program

Read https://ver.cy/AGENTS.md and the nearest owner Dimension policy first.
The 111 entries in registry.json are research contours, not 111 installed or finished models.
Use starter-selections.json as optional model selections. Re-resolve the runtime index, verify exact version/digest, required closure and semantic fit before installation. Retain reviewable-draft assurance and publication holds. These selections are not complete company models or native vercy.lock files.
Team participant records and the separate Membership/Work Assignment models overlap: preserve one authoritative relationship identity, link or project it, and record a boundary decision before combining them. Person civil-identity fields are not required merely to collaborate; record only purpose-necessary information. No real company is required to install every selected model.
Use a Company as business identity; do not manufacture a second identity when it is identical to the legal organization. Declare distinct boundaries when group, brand, legal entity and management perimeter differ.
Create the private Dimension owner package, purpose, authority, master systems, model lock and event log. Publish only generic specifications here. Never send private instance records to this public catalogue.
Research status is in queue.json. The per-contour brief and RESEARCH-PROTOCOL.md govern research completion; a published draft may still leave its larger contour unfinished.
Check queue.json platform_issues before claiming installation completion. The generic package downloader and current native V1-V3 validator are not fully aligned. A semantic package pin is not executable readiness. Preserve validation failures; never invent permissive runtime schemas or weaken the validator. The optional WM-ORG-017 reference binding is documented at https://ver.cy/models/wm-org-017-performance-objective-review/NATIVE-REFERENCE.md and requires both native and nested case validation.
''',encoding='utf-8')

    counts=Counter(q['status'] for q in queue['units'])
    kinds_keys=['subject','landscape','contract','foundation']
    for lang in LANGS:
        target=outdir(lang);target.mkdir(parents=True,exist_ok=True)
        def rc(rid,field,default):
            v=ui.get(lang,{}).get('recipes',{}).get(rid,{}).get(field)
            return v if v else default
        profiles=''
        for p in pins['profiles']:
            pname=ui.get(lang,{}).get('profiles',{}).get(p['name']) or p['name']
            profiles+='<article><h3>'+e(pname)+'</h3><p>'+t(lang,'profile_components').replace('{n}',str(len(p['requiredClosure'])))+'</p><ul>'+''.join('<li><a href="'+e(m['pageUrl'])+'">'+e(m['name'])+'</a> <small>'+e(m['version'])+' · '+e(m['assurance'])+'</small></li>' for m in p['requiredClosure'])+'</ul></article>'
        recipes=''.join('<details><summary>'+e(rc(p['id'],'name',p['name']))+'</summary><p>'+e(rc(p['id'],'trigger',p['trigger']))+'</p><p>'+', '.join('<a href="'+((base(lang) if lang in BRIEF_LANGS else '/enterprise/')+'models/'+i.lower()+'/')+'">'+i+'</a>' for i in p['research_contours'])+'</p><p class="muted">'+e(t(lang,'recipes_note'))+'</p></details>' for p in reg['recipes'])
        progress='; '.join(t(lang,'states.'+k)+': '+str(v) for k,v in counts.items())
        prompt=t(lang,'prompt')
        prompt_fn='/enterprise/start-company-dimension.txt' if lang=='en' else '/enterprise/start-company-dimension.%s.txt'%lang
        body='<span class="v-eyebrow">'+e(t(lang,'eyebrow'))+' · '+e(updated)+'</span><h1>'+t(lang,'h1')+'</h1><p class="v-lede">'+e(t(lang,'lede'))+'</p>'
        body+='<div class="box"><strong>'+e(t(lang,'box_start'))+'</strong><p>'+e(t(lang,'box_start_p'))+'</p><p>'+e(progress)+'</p></div>'
        body+='<nav class="actions"><a href="#start">'+e(t(lang,'act_create'))+'</a><a href="#registry">'+e(t(lang,'act_registry'))+'</a><a href="/enterprise/registry.json">'+e(t(lang,'act_json'))+'</a><a href="/enterprise/RESEARCH-PROTOCOL.md">'+e(t(lang,'act_contract'))+'</a><a href="/enterprise/queue.json">'+e(t(lang,'act_status'))+'</a></nav>'
        if queue.get('platform_issues'):
            body+='<div class="box"><h2>'+e(t(lang,'notice_h2'))+'</h2><p>'+t(lang,'notice_p')+'</p></div>'
        body+='<h2 id="start">'+e(t(lang,'h2_start'))+'</h2><p>'+e(t(lang,'start_p'))+'</p><pre>'+e(prompt)+'</pre>'
        body+='<p><a href="'+prompt_fn+'">'+e(t(lang,'dl_prompt'))+'</a> · <a href="/enterprise/starter-selections.json">'+e(t(lang,'dl_pins'))+'</a> · <a href="/enterprise/AGENTS.md">'+e(t(lang,'dl_agents'))+'</a></p>'
        body+='<div class="grid">'+profiles+'</div><p class="muted">'+e(t(lang,'profiles_note'))+'</p>'
        body+='<h2>'+e(t(lang,'h2_extend'))+'</h2>'+recipes
        body+='<h2 id="registry">'+e(t(lang,'h2_registry'))+'</h2><p>'+e(t(lang,'registry_p'))+'</p>'
        body+='<div class="actions"><input id="search" type="search" placeholder="'+e(t(lang,'search_ph'))+'" aria-label="'+e(t(lang,'search_aria'))+'"><select id="kind" aria-label="'+e(t(lang,'kind_aria'))+'"><option value="">'+e(t(lang,'kinds_all'))+'</option>'+''.join('<option value="'+k+'">'+e(t(lang,'kinds.'+k))+'</option>' for k in kinds_keys)+'</select></div>'
        body+='<p id="count" aria-live="polite">'+e(t(lang,'count_initial'))+'</p><section class="grid" id="cards">'+''.join(cards[lang])+'</section>'
        body+='<h2>'+e(t(lang,'h2_order'))+'</h2><p>'+e(t(lang,'order_p'))+'</p>'
        script='<script>const search=document.getElementById(\'search\'),kind=document.getElementById(\'kind\'),cards=[...document.querySelectorAll(\'#cards article\')];const shown='+json.dumps(t(lang,'count_shown'),ensure_ascii=False)+';function filter(){const q=search.value.toLowerCase().trim();let n=0;for(const card of cards){card.hidden=!(card.dataset.search.includes(q)&&(!kind.value||card.dataset.kind===kind.value));if(!card.hidden)n++;}document.getElementById(\'count\').textContent=shown.replace(\'{n}\',n);}search.addEventListener(\'input\',filter);kind.addEventListener(\'change\',filter);</script>'
        (target/'index.html').write_text(page(lang,re.sub('<[^>]+>',' ',t(lang,'title_index')).strip() if '<' in t(lang,'title_index') else t(lang,'title_index'),t(lang,'desc_index'),base(lang),body,index_hreflangs,updated,script),encoding='utf-8')

    assert len(list((out/'models').glob('*/brief.json')))==111
    shell=a.site_root/'assets/site-shell.js'
    shell_text=shell.read_text(encoding='utf-8')
    anchor='<a href="${localizedHref(\'/research/\')}">${t.research}</a>'
    if 'href="/enterprise/"' not in shell_text:
        assert anchor in shell_text,'Discovery anchor changed; inspect rather than guess'
        shell.write_text(shell_text.replace(anchor,anchor+'<a href="/enterprise/">Enterprise</a>',1),encoding='utf-8')
    llms=a.site_root/'llms.txt';llms_text=llms.read_text(encoding='utf-8')
    if 'https://ver.cy/enterprise/' not in llms_text:
        llms.write_text(llms_text+'\n## Enterprise model program\n\nEnterprise company model registry: https://ver.cy/enterprise/\nAgent instructions: https://ver.cy/enterprise/AGENTS.md\nResearch registry and per-contour assignments: https://ver.cy/enterprise/registry.json\nPublished model selections with pins: https://ver.cy/enterprise/starter-selections.json\nResearch progress, separate from package lifecycle: https://ver.cy/enterprise/queue.json\n',encoding='utf-8')
    print(json.dumps({'output':str(out),'contours':111,'states':dict(counts),'profiles':len(pins['profiles']),'languages':LANGS,'brief_languages':BRIEF_LANGS},ensure_ascii=False))

if __name__=='__main__':main()
