#!/usr/bin/env python3
"""Publish a sanitized enterprise research program, without inventing model availability."""
from __future__ import annotations
import argparse, html, json, re, shutil
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def e(x): return html.escape(str(x),quote=True)
def li(items): return '<ul>'+''.join('<li>'+e(x)+'</li>' for x in items)+'</ul>'
STYLE='''body{margin:0;background:#10151d;color:#e9edf4;font:16px/1.65 system-ui,sans-serif}main{max-width:1160px;margin:auto;padding:38px 24px 80px}a{color:#7dd5ef}h1{font-size:clamp(32px,5vw,60px);line-height:1.1}h2{margin-top:2em}small,.muted{color:#abb9c9}nav,.actions{display:flex;gap:20px;flex-wrap:wrap}article,.box,details{border:1px solid #344050;border-radius:12px;padding:20px;margin:14px 0;background:#18202b}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}.tag{display:inline-block;border-radius:5px;background:#2b3b50;padding:3px 10px;font-size:13px;margin-right:6px}.state{color:#b9ecd4}input,select{background:#18202b;color:#fff;border:1px solid #56667a;border-radius:7px;padding:12px;font-size:16px}input{min-width:260px;flex:1}summary{cursor:pointer;font-weight:650}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#0b1017;padding:18px;border-radius:8px}table{width:100%;border-collapse:collapse}td,th{text-align:left;vertical-align:top;border-bottom:1px solid #344050;padding:10px}code{overflow-wrap:anywhere}a:focus,input:focus,select:focus,summary:focus{outline:2px solid #7dd5ef;outline-offset:3px}[hidden]{display:none!important}.wide{overflow-x:auto}'''

def page(title,description,path,body,script=''):
    data={'@context':'https://schema.org','@type':'CollectionPage','name':title,'description':description,'url':'https://ver.cy'+path,'isPartOf':{'@type':'WebSite','name':'Vercy','url':'https://ver.cy/'},'dateModified':'2026-09-21','inLanguage':'ru'}
    return '<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+e(title)+' · Vercy</title><meta name="description" content="'+e(description)+'"><link rel="canonical" href="https://ver.cy'+path+'"><meta property="og:title" content="'+e(title)+'"><meta property="og:description" content="'+e(description)+'"><meta property="og:type" content="website"><meta property="og:url" content="https://ver.cy'+path+'"><style>'+STYLE+'</style><script type="application/ld+json">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script></head><body><main><nav><a href="/">Vercy</a><a href="/models/">Каталог моделей</a><a href="/enterprise/">Enterprise</a><a href="/start/">Создать Измерение</a></nav>'+body+'</main>'+script+'</body></html>\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--site-root',type=Path,default=ROOT.parent.parent/'ver.cy');a=ap.parse_args()
    src=ROOT/'research/enterprise';out=a.site_root/'enterprise';out.mkdir(parents=True,exist_ok=True)
    reg=read(src/'registry.json');queue=read(src/'queue.json');pins=read(src/'starter-selections.json');runtime=read(a.site_root/'models/runtime-index.json')
    by={m['modelId']:m for m in runtime['models']};qs={u['id']:u for u in queue['units']}
    assert len(reg['units'])==111 and len(qs)==111 and {u['id'] for u in reg['units']}==set(qs)
    states={'queued':'В очереди исследования','researching':'Исследуется','published-partial':'Частично опубликовано; исследование продолжается','published':'Результат опубликован','reuse-verified':'Переиспользование проверено','blocked':'Требует разрешения проблемы','complete':'Исследование завершено'}
    kinds={'subject':'Предметная модель','landscape':'Ландшафт','contract':'Общий контракт','foundation':'Основа композиции'}
    public_units=[];cards=[]
    for unit in reg['units']:
        u=dict(unit);q=qs[u['id']];uid=u['id'];slug=uid.lower();target=out/'models'/slug;target.mkdir(parents=True,exist_ok=True)
        candidates=[]
        for c in u.get('vercy_candidates',[]):
            m=by.get(c['model_id']);candidates.append(dict(c,runtime=None if m is None else {k:m.get(k) for k in ['id','modelId','name','version','status','installable','pageUrl','specUrl','agentsUrl','digest','requires','unresolvedRequires']}))
        u['vercy_candidates']=candidates;u['research_progress']=q;u['brief_url']='https://ver.cy/enterprise/models/'+slug+'/';public_units.append(u)
        state=states[q['status']];candidate_html=''
        for c in candidates:
            m=c['runtime'];mid=c['model_id']
            candidate_html+='<li>'+('<a href="'+e(m['pageUrl'])+'">'+e(mid)+' · '+e(m['name'])+'</a> · '+e(m['version'] or 'без версии')+' · '+('доступна для установки' if m['installable'] else 'не устанавливается автоматически') if m else e(mid)+' · отсутствует в runtime')+'<br><small>Смысловое соответствие требует исследования границ; наличие опубликованной модели не завершает эту карточку.</small></li>'
        body='<p class="muted">'+e(uid)+' · '+e(kinds[u['kind']])+' · '+e(u['wave'])+'</p><h1>'+e(u['name'])+'</h1><p>'+e(u['scope'])+'</p><p class="state">'+e(state)+'</p><p>Claude: '+e(q['claude_status'])+'; Grok: '+e(q['grok_status'])+'.</p>'
        if q['publication_urls']:body+='<h2>Опубликованные результаты</h2><ul>'+''.join('<li><a href="'+e(url)+'">Открыть результат</a></li>' for url in q['publication_urls'])+'</ul>'
        body+='<p>'+e(q.get('remaining_scope',''))+'</p><h2>Предметная граница и кандидатные типы</h2>'+li(u['candidate_types'])+'<h2>Вопросы глубокого исследования</h2>'+li(u['specific_questions'])+'<h2>Проверяемые инварианты</h2>'+li(u['proposed_invariants'])+'<h2>Сквозной приёмочный сценарий</h2><p>'+e(u['acceptance_scenario'])+'</p><h2>Отрицательный пример</h2><p>'+e(u['negative_case'])+'</p><h2>Сопоставляемые подходы</h2>'+li(u['comparison_tracks'])+'<h2>Кандидаты в действующем каталоге</h2>'+('<ul>'+candidate_html+'</ul>' if candidates else '<p>Граница и маршрут reuse / extension / new model ещё не выбраны.</p>')+'<h2>Требования к результату</h2><p>Каждая карточка исполняется вместе с <a href="/enterprise/RESEARCH-PROTOCOL.md">полным контрактом исследования</a>: определения, поля и кратности, жизненный цикл, источники, мастерство данных, права, пять граней объекта, минимум восемь инвариантов, положительные и отрицательные примеры, зависимости, миграция и ограничения применимости.</p><p><a href="brief.json">Машиночитаемое задание JSON</a></p>'
        (target/'index.html').write_text(page(u['name'],u['scope'],'/enterprise/models/'+slug+'/',body),encoding='utf-8');dump(target/'brief.json',u)
        cards.append('<article data-kind="'+e(u['kind'])+'" data-state="'+e(q['status'])+'" data-search="'+e((uid+' '+u['name']+' '+u['scope']+' '+' '.join(u['candidate_types'])).lower())+'"><span class="tag">'+e(uid)+'</span><span class="tag">'+e(kinds[u['kind']])+'</span><h3><a href="models/'+slug+'/">'+e(u['name'])+'</a></h3><p>'+e(u['scope'])+'</p><p class="state">'+e(state)+'</p></article>')
    public=dict(reg,units=public_units,updated_at=queue['updated_at'],runtime_generated_at=runtime['generatedAt']);dump(out/'registry.json',public);dump(out/'queue.json',queue);dump(out/'starter-selections.json',pins)
    shutil.copy2(src/'RESEARCH-PROTOCOL.md',out/'RESEARCH-PROTOCOL.md')
    prompt='Прочитай https://ver.cy/AGENTS.md и https://ver.cy/enterprise/AGENTS.md. Создай в моём рабочем пространстве Измерение компании. Выбери минимальную подборку из https://ver.cy/enterprise/starter-selections.json по реальным потребностям, проверь текущие опубликованные версии и зависимости. Раздели человека, трудовые отношения, членство, назначения и юрлица; сохрани источники, права и неизвестные факты. Уточни только недостающие сведения о назначении, владельце и доступе. Данные компании храни в согласованном месте; их публикация на ver.cy не подразумевается.'
    (out/'start-company-dimension.txt').write_text(prompt+'\n',encoding='utf-8')
    (out/'AGENTS.md').write_text('''# Vercy Enterprise program

Read https://ver.cy/AGENTS.md and the nearest owner Dimension policy first.
The 111 entries in registry.json are research contours, not 111 installed or finished models.
Use starter-selections.json as optional model selections. Re-resolve the runtime index, verify exact version/digest, required closure and semantic fit before installation. Retain reviewable-draft assurance and publication holds. These selections are not complete company models or native vercy.lock files.
Team participant records and the separate Membership/Work Assignment models overlap: preserve one authoritative relationship identity, link or project it, and record a boundary decision before combining them. Person civil-identity fields are not required merely to collaborate; record only purpose-necessary information. No real company is required to install every selected model.
Use a Company as business identity; do not manufacture a second identity when it is identical to the legal organization. Declare distinct boundaries when group, brand, legal entity and management perimeter differ.
Create the private Dimension owner package, purpose, authority, master systems, model lock and event log. Publish only generic specifications here. Never send private instance records to this public catalogue.
Research status is in queue.json. The per-contour brief and RESEARCH-PROTOCOL.md govern research completion; a published draft may still leave its larger contour unfinished.
''',encoding='utf-8')
    profiles=''
    for p in pins['profiles']:
        profiles+='<article><h3>'+e(p['name'])+'</h3><p>'+str(len(p['requiredClosure']))+' опубликованных компонентов с проверенными версиями и SHA-256.</p><ul>'+''.join('<li><a href="'+e(m['pageUrl'])+'">'+e(m['name'])+'</a> <small>'+e(m['version'])+' · '+e(m['assurance'])+'</small></li>' for m in p['requiredClosure'])+'</ul></article>'
    recipes=''.join('<details><summary>'+e(p['name'])+'</summary><p>'+e(p['trigger'])+'</p><p>'+', '.join('<a href="models/'+i.lower()+'/">'+i+'</a>' for i in p['research_contours'])+'</p><p class="muted">Расширенная исследовательская подборка. Она не объявляется полностью готовым установочным пакетом.</p></details>' for p in reg['recipes'])
    counts=Counter(q['status'] for q in queue['units']);progress='; '.join(states[k]+': '+str(v) for k,v in counts.items())
    body='<p class="muted">Vercy / Enterprise · 21 сентября 2026</p><h1>Измерение компании.<br>От небольшой команды до группы компаний.</h1><p>Реестр из 111 исследовательских направлений: 82 предметные модели, 18 ландшафтов, 10 общих контрактов и основа композиции. Для каждого задана граница, вопросы, инварианты и приёмочный сценарий.</p><div class="box"><strong>Можно начать сейчас.</strong><p>Ниже доступны подборки действующих опубликованных моделей. Исследовательская программа уточняет их совместимость и создаёт недостающие модели. Опубликованная спецификация может иметь зрелость reviewable-draft; её ограничения видны в карточке.</p><p>'+e(progress)+'</p></div><nav class="actions"><a href="#start">Создать Измерение</a><a href="#registry">Открыть реестр</a><a href="registry.json">JSON</a><a href="RESEARCH-PROTOCOL.md">Контракт исследования</a><a href="queue.json">Статусы</a></nav><h2 id="start">Начните с нужных компонентов</h2><p>Передайте своему ИИ-агенту этот текст. Данные компании и правила доступа остаются в вашем Измерении.</p><pre>'+e(prompt)+'</pre><p><a href="start-company-dimension.txt">Скачать инструкцию</a> · <a href="starter-selections.json">Подборки с версиями и контрольными суммами</a> · <a href="AGENTS.md">Контракт для агента</a></p><div class="grid">'+profiles+'</div><p class="muted">Подборки проверяют наличие и целостность пакетов. Совместимость конкретных профилей и отношения с локальными мастер-системами проверяются при установке. HR, договоры и юрлицо добавляются только при необходимости.</p><h2>Как расширять Измерение</h2>'+recipes+'<h2 id="registry">Реестр и индивидуальные задания</h2><p>Queued означает, что подготовлено задание. Researching означает начатый проход. Завершение и публикация подтверждаются отдельно.</p><div class="actions"><input id="search" type="search" placeholder="Компания, проект, договор, аналитика…" aria-label="Поиск по реестру"><select id="kind" aria-label="Вид направления"><option value="">Все виды</option>'+''.join('<option value="'+k+'">'+e(v)+'</option>' for k,v in kinds.items())+'</select></div><p id="count" aria-live="polite">111 направлений</p><section class="grid" id="cards">'+''.join(cards)+'</section><h2>Порядок исследования и публикации</h2><p>Claude и Grok независимо исследуют границу и источники. Их выводы сопоставляются, разногласия сохраняются, затем проверяются схема, семантика, зависимости и сценарии. Готовый результат публикуется сразу с честным статусом зрелости. Реестр не утверждает, что все 111 исследований уже выполнены.</p>'
    script='''<script>const search=document.getElementById('search'),kind=document.getElementById('kind'),cards=[...document.querySelectorAll('#cards article')];function filter(){const q=search.value.toLowerCase().trim();let n=0;for(const card of cards){card.hidden=!(card.dataset.search.includes(q)&&(!kind.value||card.dataset.kind===kind.value));if(!card.hidden)n++;}document.getElementById('count').textContent='Показано: '+n+' из 111';}search.addEventListener('input',filter);kind.addEventListener('change',filter);</script>'''
    (out/'index.html').write_text(page('Enterprise: реестр моделей компании','Модели для Измерения компании, 111 индивидуальных исследовательских заданий, опубликованные компоненты и статусы Claude/Grok.','/enterprise/',body,script),encoding='utf-8')
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
    print(json.dumps({'output':str(out),'contours':111,'states':dict(counts),'profiles':len(pins['profiles'])},ensure_ascii=False))

if __name__=='__main__':main()
