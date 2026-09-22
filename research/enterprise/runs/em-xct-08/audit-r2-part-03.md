Continuation of the same frozen R2 no-tools audit. ACK only; do not audit yet.
FRAGMENT 3/15
PAYLOAD BEGIN
    return c is not None and any(x['id']==mapping['targetId'] and x['kind']==mapping['expectedTargetKind'] for x in c['subjects']) and {'sourceKind':scope['sourceObjectKind'],'targetKind':mapping['expectedTargetKind'],'purpose':mapping['purpose']} in c['pairs']
def mapping_outcome(state,scope_id,item,purpose):
    lin=lineage(state,scope_id,item['key'])
    if lin is None:return {'status':'continuity-unknown','pin':None}
    matches=[h[-1] for h in state['mappings'].values() if h[-1]['lineage']==lin and h[-1]['definition']['purpose']==purpose and h[-1]['state']=='active']
    require(len(matches)<=1,'ambiguous active mappings')
    if not matches:return {'status':'unmapped','pin':None}
    m=matches[0];definition=m['definition']
    if state['scopes'][scope_id]['sourceObjectKind']!=state['scopes'][definition['scopeId']]['sourceObjectKind'] or not eligible_mapping(state,definition) or not within(item['observedAt'],definition['validFrom'],definition['validTo']):
        return {'status':'active-pin-suspended','pin':None}
    return {'status':'mapped','pin':{'mappingId':definition['id'],'revision':m['revision'],'catalogueRevision':state['catalogue']['revision'],'policyRevision':state['policy']['revision']}}
def occurrence_by_id(state,oid):
    return next((x for b in state['batches'].values() for x in b['occurrences'] if x['id']==oid),None)
def event_id(state,seq,suffix):return state['config']['registerId']+':'+str(seq)+':'+suffix

def apply(state,command,actor,now,seq):
    """Trusted host reducer. Return result + whether a journal entry is retained."""
    time(now)
    op=command.get('op') if type(command)==dict else None
    body=command.get('body') if type(command)==dict else None
    admin=actor==state['config']['admin']
    # Authorization precedes schema diagnostics and any receipt lookup.
    if op in ('source','scope','catalogue','policy','epoch-open','epoch-close','fence'):
        if not admin:return deepcopy(DENIED),False
    elif op in ('commit','round-open','round-seal','mapping','mapping-state'):
        try:
            if op=='commit':scope,purpose=body['content']['scopeId'],body['content']['purpose']
            elif op=='mapping-state':m=state['mappings'][body['id']][-1]['definition'];scope,purpose=m['scopeId'],m['purpose']
            elif op=='round-seal':r=state['rounds'][body['id']]['definition'];scope,purpose=r['scopeId'],r['purpose']
            else:scope,purpose=body['scopeId'],body['purpose']
            if not permitted(state,actor,scope,purpose,'map' if op.startswith('mapping') else 'intake',now):return deepcopy(DENIED),False
        except (KeyError,TypeError):return deepcopy(DENIED),False
    else:return deepcopy(DENIED),False
    validate('Command',command);evidence_check(body,state['config']['protectedNamespace'])
    if op=='source':
        require(body['id'] not in state['sources'],'source identity exists')
        require(not any((s['tenant'],s['environment'],s['productRef'],s['generation'])==(body['tenant'],body['environment'],body['productRef'],body['generation']) for s in state['sources'].values()),'duplicate declared source identity')
        state['sources'][body['id']]=deepcopy(body)
    elif op=='scope':
        require(body['id'] not in state['scopes'] and body['sourceId'] in state['sources'],'scope/source identity')
        fingerprint=digest({k:v for k,v in body.items() if k!='id'})
        require(all(s['fingerprint']!=fingerprint for s in state['scopes'].values()),'duplicate scope')
        state['scopes'][body['id']]={**deepcopy(body),'fingerprint':fingerprint}
    elif op in ('policy','catalogue'):
        previous=state[op];require(body['revision']==(previous['revision']+1 if previous else 1),'configuration revision')
        if op=='policy':
            for g in body['grants']:require(time(g['validFrom'])<time(g['validTo']),'grant window')
        else:require(len({s['id'] for s in body['subjects']})==len(body['subjects']),'duplicate target')
        state[op]=deepcopy(body)
    elif op=='mapping':
        require(body['id'] not in state['mappings'] and body['scopeId'] in state['scopes'],'mapping identity')
        incoming_key(state,body['scopeId'],body['key'],actor,body['purpose'],now)
        require(body['issuer']==actor,'mapping issuer must be authenticated steward')
        require(body['key']['generation'] is not None,'unknown generation cannot map')
        time(body['validFrom']);require(body['validTo'] is None or time(body['validFrom'])<time(body['validTo']),'mapping window')
        if body['corrects'] is not None:require(body['corrects'] in state['mappings'],'missing correction predecessor')
        require(eligible_mapping(state,body),'target kind or aboutness policy')
        state['mappings'][body['id']]=[{'definition':deepcopy(body),'lineage':lineage(state,body['scopeId'],body['key']),'revision':1,'state':'proposed','recordedAt':now,'sequence':seq,'actor':actor,'reason':'proposal','catalogueRevision':state['catalogue']['revision']}]
    elif op=='mapping-state':
        h=state['mappings'][body['id']];old=h[-1];require(old['revision']==body['expectedRevision'],'mapping revision')
        transitions={'proposed':{'active','disputed','retracted'},'active':{'disputed','retracted'},'disputed':{'active','retracted'},'retracted':set()}
        require(body['to'] in transitions[old['state']],'mapping transition')
        if body['to']=='active':
            require(eligible_mapping(state,old['definition']),'target kind or aboutness policy')
            require(not any(x[-1]['state']=='active' and x[-1]['lineage']==old['lineage'] and x[-1]['definition']['purpose']==old['definition']['purpose'] for mid,x in state['mappings'].items() if mid!=body['id']),'active mapping already exists')
            previous=old['definition']['corrects']
            require(previous is None or state['mappings'][previous][-1]['state']=='retracted','corrected claim not retracted')
        h.append({**deepcopy(old),'revision':old['revision']+1,'state':body['to'],'recordedAt':now,'sequence':seq,'actor':actor,'reason':body['reason'],'catalogueRevision':state['catalogue']['revision']})
    elif op=='epoch-open':
        require(body['id'] not in state['epochs'] and body['scopeId'] in state['scopes'],'epoch identity')
        require(not any(e['scopeId']==body['scopeId'] and e['status']=='open' for e in state['epochs'].values()),'scope already has open epoch')
        state['epochs'][body['id']]={**deepcopy(body),'status':'open','head':None,'fence':1,'progress':0,'openedAt':now,'openedSequence':seq,'closedAt':None,'closedSequence':None}
    elif op in ('epoch-close','fence'):
        e=state['epochs'].get(body['id']);require(e is not None and e['status']=='open','epoch not open')
        if op=='fence':require(body['expectedFence']==e['fence'],'stale fence');e['fence']+=1
        else:
            require(not any(r['definition']['epochId']==body['id'] and not r['sealed'] for r in state['rounds'].values()),'seal open rounds, including partial evidence, before epoch close')
            e.update(status='closed',closedAt=now,closedSequence=seq,closeReason=body['reason'])
    elif op=='round-open':
        require(body['id'] not in state['rounds'],'round exists')
        e=state['epochs'].get(body['epochId']);require(e is not None and e['status']=='open' and e['scopeId']==body['scopeId'],'round epoch')
        require((body['previousRoundId'] is None)==(body['notEarlierEvidence'] is None),'round order evidence')
        if body['previousRoundId'] is not None:
            old=state['rounds'].get(body['previousRoundId']);require(old is not None and old['sealed'] and old['definition']['scopeId']==body['scopeId'],'round predecessor')
        state['rounds'][body['id']]={'definition':deepcopy(body),'pages':[],'sealed':False,'errors':[],'openedSequence':seq,'sealedSequence':None,'complete':False}
    elif op=='round-seal':
        r=state['rounds'][body['id']];require(not r['sealed'],'round already sealed')
        pages=[state['batches'][p] for p in r['pages']]
        r.update(sealed=True,errors=deepcopy(body['errors']),sealedSequence=seq)
        r['complete']=bool(pages and pages[-1]['content']['terminal'] and not body['errors'] and all(not b['quarantine'] and all(o['key']['generation'] is not None and o['operation']=='snapshot-read' for o in b['occurrences']) for b in pages))
    elif op=='commit':
        c=body['content'];e=state['epochs'].get(c['epochId'])
        if e is None or e['status']!='open' or e['scopeId']!=c['scopeId']:return deepcopy(DENIED),False
        slot=digest([c['scopeId'],c['epochId'],c['batchKey']]);cd=digest(c);old=state['batches'].get(slot)
        def conflict(reason):
            state['conflicts'].append({'id':event_id(state,seq,'conflict'),'scopeId':c['scopeId'],'epochId':c['epochId'],'attemptId':body['attemptId'],'actor':actor,'recordedAt':now,'sequence':seq,'reason':reason,'suppliedDigest':cd,'retainedDigest':old['contentDigest'] if old else None})
            return deepcopy(DENIED),True
        if old is not None:
            if old['actor']!=actor:return conflict('principal-collision')
            if old['contentDigest']!=cd or old['content']!=c:return conflict('changed-content')
            return {'status':'committed','receiptId':old['id']},False
        if e['head']!=body['expectedHead']:return conflict('stale-head')
        if e['fence']!=body['fence']:return conflict('stale-fence')
        require(c['empty']==(len(c['items'])==0),'empty declaration')
        if c['roundId'] is None:require(c['pageIndex'] is None and not c['terminal'],'round/page mismatch')
        else:
            r=state['rounds'].get(c['roundId']);require(r is not None and not r['sealed'],'round not open')
            d=r['definition'];require((d['scopeId'],d['epochId'],d['purpose'])==(c['scopeId'],c['epochId'],c['purpose']),'round context')
            require(c['pageIndex']==len(r['pages']),'page chain gap')
            require(not r['pages'] or not state['batches'][r['pages'][-1]]['content']['terminal'],'page after terminal')
        rid=event_id(state,seq,'receipt');occ=[];quarantine=[]
        for ordinal,item in enumerate(c['items']):
            if item['kind']=='quarantine':quarantine.append({**deepcopy(item),'id':rid+':quarantine:'+str(ordinal),'ordinal':ordinal,'state':'open'});continue
            incoming_key(state,c['scopeId'],item['key'],actor,c['purpose'],now);time(item['observedAt'])
            if item['sourceEventTime'] is not None:time(item['sourceEventTime'])
            correction=item['correction']
            if correction is not None:
                prev=occurrence_by_id(state,correction['occurrenceId']);require(prev is not None,'missing corrected occurrence')
                require(prev['lineage'] is not None and prev['lineage']==lineage(state,c['scopeId'],item['key']),'correction lineage')
                require(permitted(state,actor,c['scopeId'],c['purpose'],'map',now),'correction requires steward authority')
                asserted=state['scopes'][c['scopeId']]['sourceId'] if correction['basis']=='source-asserted' else actor
                require(correction['assertedBy']==asserted,'correction attribution mismatch')
            outcome=mapping_outcome(state,c['scopeId'],item,c['purpose'])
            occ.append({**deepcopy(item),'id':rid+':occurrence:'+str(ordinal),'ordinal':ordinal,'lineage':lineage(state,c['scopeId'],item['key']),'mapping':outcome,'recordedAt':now,'sequence':seq})
        receipt={'id':rid,'content':deepcopy(c),'contentDigest':cd,'actor':actor,'attemptId':body['attemptId'],'committedAt':now,'sequence':seq,'previousHead':e['head'],'fence':e['fence'],'progress':e['progress']+1,'policyRevision':state['policy']['revision'],'occurrences':occ,'quarantine':quarantine,'received':len(c['items']),'accepted':len(occ),'quarantined':len(quarantine)}
        require(receipt['received']==receipt['accepted']+receipt['quarantined'],'conservation')
        state['batches'][slot]=receipt;e.update(head=rid,progress=e['progress']+1)
        if c['roundId'] is not None:state['rounds'][c['roundId']]['pages'].append(slot)
        return {'status':'committed','receiptId':rid},True
    return {'status':'recorded'},True

def replay(config,events):
    require(type(events)==list and len(events)<=MAX_EVENTS,'event budget')
    state=initial(config);previous=digest(config);last=None
    for seq,event in enumerate(events,1):
        validate('JournalEvent',event)
        require(set(event)=={'sequence','previousDigest','actor','recordedAt','command','result','digest'},'event fields')
        require(event['sequence']==seq and event['previousDigest']==previous,'event chain')
        require(last is None or time(event['recordedAt'])>=time(last),'host recorded time moved backwards')
        expected=digest({k:v for k,v in event.items() if k!='digest'});require(event['digest']==expected,'event digest')
        result,retained=apply(state,event['command'],event['actor'],event['recordedAt'],seq)
        require(retained and result==event['result'],'event outcome')
        previous=expected;last=event['recordedAt']
    return state,previous

class Register:
    def __init__(self,path,config=None):
        self.path=Path(path)
        if config is not None:
            initial(config)
            with self.path.open('xb'):pass
        require(config is not None or self.path.is_file(),'explicit bootstrap required')
        self.db=sqlite3.connect(str(self.path),timeout=10,isolation_level=None)

PAYLOAD END — FRAGMENT 3/15
