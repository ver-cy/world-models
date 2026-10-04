"""Invented classifications; never copied organization data or licensed codes."""
import copy,json
from pathlib import Path
import classification_review as r

AT='2026-09-22T10:00:00Z'
START='2026-01-01T00:00:00Z'
END='2027-01-01T00:00:00Z'
ACTOR='urn:synthetic:reviewer'
def code(s,v,c):return {'scheme':s,'version':v,'code':c}
def snapshot(id,payload):
    s={'id':id,'source':'urn:synthetic:publisher','sourceRevision':'revision1','sourceDigest':r.digest(payload),'capture':{'id':id+':capture','actor':'urn:synthetic:capturer','at':AT,'method':'Synthetic fixture construction'},'payload':payload}
    s['digest']=r.snapshot_digest(s);return s
def release(id,scheme,version,codes):
    return snapshot(id,{'kind':'scheme-release','scheme':scheme,'version':version,'complete':True,'concepts':[{'code':c,'definition':'Invented category '+c,'status':'active','selectable':True,'validFrom':START,'validUntil':None} for c in codes]})
def profile(id,release,subject,allowed,parent=None):
    rd=release['payload']
    return snapshot(id,{'kind':'slot-profile','id':id+':source','version':'1','parent':r.pin(parent) if parent else None,'subjectClass':subject,'unit':subject,'slot':'category','meaning':'Independent category selections for the declared subject unit','strength':'required','releasePins':[r.pin(release)],'allowed':[code(rd['scheme'],rd['version'],x) for x in allowed],'min':1,'max':2})
def grant(packet,approvals=()):
    return {'format':'vercy-classification-host-context','dimensionId':packet['dimensionId'],'owner':packet['owner'],'actor':ACTOR,'purpose':packet['purpose'],'packetDigest':r.digest(packet),'validFrom':START,'validUntil':END,'approvals':list(approvals)}
def make(name):
    subject='Document' if name=='ai-team' else 'Project'
    scheme='urn:synthetic:scheme:'+name
    old=release('urn:synthetic:release:old',scheme,'1',['A','B','C'])
    base=profile('urn:synthetic:profile:base',old,subject,['A','B','C'])
    narrowed=profile('urn:synthetic:profile:narrow',old,subject,['A','B'],base)
    binding=snapshot('urn:synthetic:assignment:1',{'kind':'assignment','id':'urn:synthetic:binding:1','revision':1,'subjectId':'urn:synthetic:subject:1','subjectClass':subject,'unit':subject,'slot':'category','profile':r.pin(base),'values':[code(scheme,'1','A')],'origin':'human','method':None,'score':None,'assertedAt':START,'validFrom':START,'validUntil':None,'state':'asserted','corrects':None})
    packet={'format':'vercy-classification-review-packet','version':r.VERSION,'id':'urn:synthetic:review:'+name,'revision':1,'previousDigest':None,'owner':'urn:synthetic:owner:'+name,'dimensionId':'urn:synthetic:dimension:'+name,'purpose':'classification-review','jurisdiction':'synthetic-region-A','knowledgeAt':AT,'effectiveAt':AT,'targetAt':AT,'mode':'assignment','inference':'direct-only','baseProfile':r.pin(base),'profile':r.pin(narrowed),'assignments':[r.pin(binding)],'crosswalks':[],'snapshots':[old,base,narrowed,binding]}
    approvals=[]
    expected={'outcome':'conforms-to-local-profile','migrationDisposition':'not-requested'}
    if name!='startup':
        # International deliberately reuses A under a distinct publisher namespace.
        targetscheme='urn:synthetic:scheme:other-region' if name=='international' else scheme
        new=release('urn:synthetic:release:new',targetscheme,'2',['A','B'])
        target=profile('urn:synthetic:profile:target',new,subject,['A','B'])
        entries=[]
        for n,c in enumerate(['A'] if name=='international' else ['A','B']):
            approved=name=='international'
            entries.append({'id':'urn:synthetic:mapping:'+str(n),'sources':copy.deepcopy(binding['payload']['values']),'targets':[code(targetscheme,'2',c)],'predicate':'exactMatch','state':'approved' if approved else 'candidate','approver':ACTOR if approved else None,'evidence':['urn:synthetic:evidence:mapping'],'validFrom':START,'validUntil':None,'origin':'human' if approved else 'model-suggested','method':None if approved else {'id':'urn:synthetic:classifier','version':'3'},'score':None if approved else ['0.99','0.98'][n],'lossNote':'No loss asserted by fixture author; not independently proven.'})
        cross=snapshot('urn:synthetic:crosswalk:1',{'kind':'crosswalk','id':'urn:synthetic:crosswalk:source','version':'1','context':{'unit':subject,'purpose':packet['purpose'],'jurisdiction':packet['jurisdiction']},'complete':True,'entries':entries})
        packet.update(mode='migration',profile=r.pin(target),crosswalks=[r.pin(cross)])
        packet['snapshots'] += [new,target,cross]
        if name=='international':approvals=[{'snapshotDigest':cross['digest'],'entryId':entries[0]['id'],'approver':ACTOR,'evidence':entries[0]['evidence'][0]}]
        expected={'outcome':'candidate-only' if name=='international' else 'human-review-required','migrationDisposition':'proposed-candidate' if name=='international' else 'human-review-required'}
    return {'packet':packet,'host':grant(packet,approvals),'expected':expected}

def repin(fixture,id,modify):
    """Edit synthetic inputs and update all affected references, without re-approval."""
    p=fixture['packet'];target=next(s for s in p['snapshots'] if s['id']==id)
    modify(target['payload'])
    old=target['digest'];target['digest']=r.snapshot_digest(target)
    pending=[(id,old,target['digest'])]
    def rewrite(v,sid,before,after):
        if isinstance(v,dict):
            if set(v)=={'id','digest'} and v['id']==sid and v['digest']==before:v['digest']=after
            else:
                for x in v.values():rewrite(x,sid,before,after)
        elif isinstance(v,list):
            for x in v:rewrite(x,sid,before,after)
    while pending:
        sid,before,after=pending.pop(0);rewrite(p,sid,before,after)
        for s in p['snapshots']:
            new=r.snapshot_digest(s)
            if new!=s['digest']:
                previous=s['digest'];s['digest']=new;pending.append((s['id'],previous,new))
    fixture['host']['packetDigest']=r.digest(p)

def evaluate(f):return r.review(f['packet'],f['host'],ACTOR,f['packet']['purpose'],AT)

if __name__=='__main__':
    out=Path(__file__).parent/'examples';out.mkdir(exist_ok=True)
    for name in ('startup','international','ai-team'):
        f=make(name);result=evaluate(f)
        for k,v in f['expected'].items():assert result[k]==v,(name,k,result)
        (out/(name+'.json')).write_text(json.dumps(f,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Three synthetic fixtures created and expected dispositions checked')
