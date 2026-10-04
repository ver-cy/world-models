"""One synthetic near-capacity run; recorded timings are not an SLA."""
from pathlib import Path
from copy import deepcopy
from time import perf_counter
from datetime import datetime,timezone
import argparse,hashlib,json,platform,sqlite3,subprocess,sys,tempfile
import sync_register as p
from fixtures import Harness,ADMIN,WRITER,SCOPE,EPOCH,PURPOSE,item,evidence
HERE=Path(__file__).parent
def run():
    with tempfile.TemporaryDirectory(prefix='sync-capacity-') as tmp:
        root=Path(tmp);db=root/'store.sqlite';h=Harness(db);setup_start=perf_counter();archive=h.archive();seq=len(archive['events'])+1;now=h.now()
        def prospective(count):
            rec=item();rec['key']['value']='K'*256;rec['content']=evidence('P'*210)
            body=h.batch('bulk',[deepcopy(rec) for _ in range(count)]);state=deepcopy(archive['state']);command={'op':'commit','body':body}
            result,kept=p.apply(state,command,WRITER,now,seq);assert kept
            event={'sequence':seq,'previousDigest':archive['root'],'actor':WRITER,'recordedAt':now,'command':command,'result':result,'outcomeDigest':p.digest(state)};event['digest']=p.digest(event)
            full={**archive,'events':archive['events']+[event],'state':state,'root':event['digest']}
            return len(p.encode(full)),body
        sample={'sequence':p.MAX_EVENTS,'previousDigest':'sha256:'+'0'*64,'actor':ADMIN,'recordedAt':now,'command':{'op':'fence','body':{'id':EPOCH,'expectedFence':1000000,'evidence':evidence('capacity-fence')}},'result':{'status':'recorded'},'outcomeDigest':'sha256:'+'0'*64,'digest':'sha256:'+'0'*64}
        reserve=(p.MAX_EVENTS-seq)*len(p.encode(sample))+6000
        low,high=0,256
        while low<high:
            middle=(low+high+1)//2
            try:size,_=prospective(middle);fits=size+reserve<=p.MAX_BYTES
            except p.Invalid:fits=False
            if fits:low=middle
            else:high=middle-1
        assert low>0
        _,body=prospective(low);h.reg.execute({'op':'commit','body':body},WRITER,now)
        # Keep the large retained state from the start: this stresses full replay.
        fence=1;write_times=[]
        for _ in range(seq,p.MAX_EVENTS-2):
            start=perf_counter();h.call('fence',{'id':EPOCH,'expectedFence':fence,'evidence':evidence('capacity-fence')});write_times.append(perf_counter()-start);fence+=1
        at_capacity=h.archive();setup_seconds=perf_counter()-setup_start
        start=perf_counter();h.archive();archive_seconds=perf_counter()-start
        start=perf_counter();h.reg.read_receipt(SCOPE,PURPOSE,EPOCH,'bulk',WRITER,h.now());read_seconds=perf_counter()-start
        request={'command':{'op':'commit','body':h.batch('capacity-race',[])},'actor':WRITER,'now':h.now()}
        inp=root/'request.json';inp.write_text(json.dumps(request),encoding='utf-8');outputs=[root/'one.json',root/'two.json'];h.close()
        start=perf_counter();workers=[subprocess.Popen([sys.executable,str(HERE/'fault_worker.py'),str(db),str(inp),str(out),'none'],stdout=subprocess.PIPE,stderr=subprocess.PIPE) for out in outputs]
        runs=[]
        for worker in workers:
            _,err=worker.communicate(timeout=120);runs.append({'exitCode':worker.returncode,'stderr':err.decode('utf-8')})
        race_seconds=perf_counter()-start
        assert all(x['exitCode']==0 for x in runs),runs
        replies=[json.loads(out.read_text()) for out in outputs];assert replies[0]==replies[1] and replies[0]['status']=='committed'
        reg=p.Register(db);after_race=reg.archive(ADMIN)
        # Fill to the exact retained-event cap, then prove a no-event retry still works.
        while len(after_race['events'])<p.MAX_EVENTS:
            reg.execute({'op':'fence','body':{'id':EPOCH,'expectedFence':fence,'evidence':evidence('capacity-fence')}},ADMIN,request['now']);fence+=1;after_race=reg.archive(ADMIN)
        start=perf_counter();assert reg.execute(request['command'],WRITER,request['now'])==replies[0];retry_seconds=perf_counter()-start
        final=reg.archive(ADMIN);reg.close();assert final==after_race
        size=len(p.encode(final));assert size>p.MAX_BYTES*0.85 and size<=p.MAX_BYTES
    files=('benchmark.py','sync_register.py','sync.schema.json','fixtures.py','fault_worker.py')
    return {'format':'vercy-source-sync-capacity-run','executedAt':datetime.now(timezone.utc).isoformat(),'passed':True,'buildId':p.BUILD_ID,'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'eventLimit':p.MAX_EVENTS,'canonicalByteLimit':p.MAX_BYTES,'retainedEvents':len(final['events']),'canonicalBytes':size,'budgetFillFraction':round(size/p.MAX_BYTES,4),'bulkRecords':low,'setupSeconds':round(setup_seconds,3),'lastSetupWriteSeconds':round(write_times[-1],3),'maxSetupWriteSeconds':round(max(write_times),3),'archiveSeconds':round(archive_seconds,3),'readReceiptSeconds':round(read_seconds,3),'twoProcessExactRetrySeconds':round(race_seconds,3),'writerTimeouts':0,'retryAtLimitSeconds':round(retry_seconds,3),'sourceDigests':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in files},'limits':'One synthetic local run with large state present from early history, not an SLA, statistical benchmark or power-loss test. Host load/storage/dependency changes can cause latency and SQLite busy errors; admission and capacity recovery remain external. Original R3 2000-event/8MiB caps are withdrawn, not certified by this smaller run.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--report',required=True);a=ap.parse_args();r=run();Path(a.report).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in r.items() if k not in ('sourceDigests','limits')}))
