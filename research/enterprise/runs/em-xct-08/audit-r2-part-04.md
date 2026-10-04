Continuation of the same frozen R2 no-tools audit. ACK only; do not audit yet.
FRAGMENT 4/15
PAYLOAD BEGIN
        self.db.execute('PRAGMA journal_mode=DELETE');self.db.execute('PRAGMA synchronous=FULL')
        if config is not None:
            try:
                self.db.execute('BEGIN IMMEDIATE')
                require(not self.db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall(),'new empty store required')
                self.db.execute('CREATE TABLE bootstrap (id INTEGER PRIMARY KEY CHECK(id=1), body BLOB NOT NULL)')
                self.db.execute('CREATE TABLE journal (seq INTEGER PRIMARY KEY, body BLOB NOT NULL)')
                self.db.execute('INSERT INTO bootstrap VALUES (1,?)',(encode(config),));self.db.commit()
            except BaseException:self.db.rollback();raise
        self.config=decode(self.db.execute('SELECT body FROM bootstrap WHERE id=1').fetchone()[0])
    def close(self):self.db.close()
    def _events(self):return [decode(row[0]) for row in self.db.execute('SELECT body FROM journal ORDER BY seq')]
    def execute(self,command,actor,now,*,fault=None):
        """actor/now are verified host inputs. Fault hook is test-only."""
        try:
            self.db.execute('BEGIN IMMEDIATE');events=self._events();state,root=replay(self.config,events)
            require(not events or time(now)>=time(events[-1]['recordedAt']),'host clock rollback')
            result,retained=apply(state,command,actor,now,len(events)+1)
            if retained:
                require(len(events)<MAX_EVENTS,'event budget')
                event={'sequence':len(events)+1,'previousDigest':root,'actor':actor,'recordedAt':now,'command':deepcopy(command),'result':result}
                event['digest']=digest(event)
                validate('JournalEvent',event)
                # Keep every committed cut exportable under the same byte budget.
                encode({'format':'vercy-source-sync-archive','version':VERSION,'config':self.config,'events':events+[event],'state':state,'root':event['digest'],'resumable':False})
                self.db.execute('INSERT INTO journal VALUES (?,?)',(event['sequence'],encode(event)))
            if fault:fault('before-commit')
            self.db.commit()
            if fault:fault('after-commit')
            return deepcopy(result)
        except BaseException:self.db.rollback();raise
    def archive(self,actor):
        """Privileged full-store export, not a public/partial disclosure API."""
        require(actor==self.config['admin'],'full export requires host administrator')
        self.db.execute('BEGIN')
        try:
            events=self._events();state,root=replay(self.config,events)
            out={'format':'vercy-source-sync-archive','version':VERSION,'config':self.config,'events':events,'state':state,'root':root,'resumable':False}
            encode(out);self.db.commit();return deepcopy(out)
        except BaseException:self.db.rollback();raise
    def read_receipt(self,scope,purpose,epoch,batch_key,actor,now):
        self.db.execute('BEGIN')
        try:
            state,_=replay(self.config,self._events())
            if not permitted(state,actor,scope,purpose,'read',now):result=deepcopy(DENIED)
            else:
                receipt=state['batches'].get(digest([scope,epoch,batch_key]))
                result=deepcopy(receipt) if receipt and receipt['content']['purpose']==purpose else {'status':'not-found'}
            self.db.commit();return result
        except BaseException:self.db.rollback();raise

def validate_archive(archive):
    encode(archive)
    require(set(archive)=={'format','version','config','events','state','root','resumable'},'archive fields')
    require(archive['format']=='vercy-source-sync-archive' and archive['version']==VERSION,'unsupported archive version')
    require(archive['resumable'] is False,'archive is never resumable')
    state,root=replay(archive['config'],archive['events'])
    require(state==archive['state'] and root==archive['root'],'archive derived state/root mismatch')
    return {'valid':True,'scope':'historical-consistency-only','resumable':False,'events':len(archive['events'])}

def assess_rounds(archive,earlier,later):
    """Privileged offline analysis of a complete restricted archive; no effects."""
    validate_archive(archive);s=archive['state'];a=s['rounds'].get(earlier);b=s['rounds'].get(later)
    if a is None or b is None:return {'status':'insufficient-context','candidates':[]}
    x,y=a['definition'],b['definition']
    ok=a['complete'] and b['complete'] and a['sealedSequence']<b['sealedSequence'] and x['scopeId']==y['scopeId'] and x['purpose']==y['purpose'] and x['consistency']==y['consistency']=='source-snapshot' and x['visibilityCovered'] and y['visibilityCovered'] and y['previousRoundId']==earlier and y['notEarlierEvidence'] is not None
    if not ok:return {'status':'insufficient-context','candidates':[]}
    def observed(r):return {digest(o['lineage']):o for slot in r['pages'] for o in s['batches'][slot]['occurrences']}
    old,new=observed(a),observed(b);candidates=[];explicit=[]
    for key,o in old.items():
        if key in new:continue
        unavailable=[p for receipt in s['batches'].values() if receipt['content']['scopeId']==x['scopeId'] and a['sealedSequence']<receipt['sequence']<=b['sealedSequence'] for p in receipt['occurrences'] if p['lineage']==o['lineage'] and p['operation'] in ('source-deleted','removed-from-scope','inaccessible')]
        if unavailable:explicit.append({'lineage':o['lineage'],'operation':unavailable[-1]['operation'],'evidenceOccurrence':unavailable[-1]['id']})
        else:candidates.append({'conclusion':'not-observed-in-comparable-rounds','lineage':o['lineage'],'earlierRound':earlier,'laterRound':later,'permittedAction':'steward-review-only'})
    return {'status':'assessed','candidates':candidates,'explicitAvailabilityEvidence':explicit,'effects':[]}

def resume_archive(_):raise Invalid('Archive resume refused; new local acquisition baseline required')

def inspect_import(raw):
    """Read-only import report; never creates a database or grants live authority."""
    try:
        archive=decode(raw);report=validate_archive(archive)
        return {**report,'status':'historical-only','lossReport':None}
    except (ValueError,TypeError,KeyError,ValidationError) as error:
        return {'valid':False,'status':'refused','resumable':False,'lossReport':{'code':'unsupported-or-inconsistent-archive','detail':str(error),'action':'retain original; supply an exact supported archive; no lossy conversion attempted'}}

def historical_cut(archive,known_at):
    """Privileged historical view. Current disclosure must be enforced by its host."""
    validate_archive(archive);time(known_at)
    events=[e for e in archive['events'] if time(e['recordedAt'])<=time(known_at)]
    state,root=replay(archive['config'],events)
    return {'knownAt':known_at,'events':len(events),'root':root,'state':state,'resumable':False}

PROFILE_ID='vr.profile.enterprise-source-synchronization'

def native_value(archive):
    validate_archive(archive)
    return {**{k:deepcopy(v) for k,v in archive.items() if k!='state'},'format':'vercy-source-sync-journal-snapshot'}

def archive_from_native(value):
    encode(value);Draft202012Validator(SCHEMA).validate(value)
    state,root=replay(value['config'],value['events']);require(root==value['root'],'native journal root mismatch')
    return {**deepcopy(value),'format':'vercy-source-sync-archive','state':state}

def native_records(archive,captured_at,previous_fact=None):
    """Privileged restricted projection. Never imports or resumes a register."""
    validate_archive(archive);time(captured_at)
    config=archive['config'];oid=config['registerId'];root=archive['root'].split(':')[1]
    require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._:-]{2,159}',oid) is not None,'native register ID requires 3..160 safe characters; no automatic rewriting')
    require(not archive['events'] or time(captured_at)>=time(archive['events'][-1]['recordedAt']),'capture precedes journal')
    obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':sync-register','name':'Source synchronization register','recordedAt':captured_at,'previousRecordId':None,'state':'active','provenance':{'source':oid,'dimensionId':config['dimensionId']},'accessClass':'restricted'}
    value=native_value(archive)
    fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot:'+root,'subjectId':oid,'path':'sync.register.snapshot','value':value,'unit':None,'validFrom':captured_at,'validTo':None,'recordedAt':captured_at,'supersedes':[] if previous_fact is None else [previous_fact['factId']],'status':'asserted','provenance':{'source':oid,'dimensionId':config['dimensionId'],'snapshotDigest':digest(value),'previousSnapshotDigest':None if previous_fact is None else digest(previous_fact['value'])},'authority':{'source':config['admin'],'rank':0},'masterSystem':oid,'accessClass':'restricted'}
    validate_native_snapshot(fact,previous_fact)
    return obj,fact

def validate_native_snapshot(fact,previous=None):
    """Run after native outer validation; caller provides trusted predecessor."""
    a=archive_from_native(fact['value']);config=a['config'];oid=config['registerId']
    require(fact['recordType']=='fact' and fact['schemaVersion']=='1.0.0' and fact['path']=='sync.register.snapshot','snapshot envelope')
    require(fact['subjectId']==oid and fact['factId']==oid+':snapshot:'+a['root'].split(':')[1] and fact['masterSystem']==oid,'snapshot identity')
    require(fact['authority']=={'source':config['admin'],'rank':0} and fact['accessClass']=='restricted','snapshot storage authority/class')
    require(fact['status']=='asserted' and fact['unit'] is None and fact['validTo'] is None and fact['validFrom']==fact['recordedAt'],'snapshot times/status')
    time(fact['recordedAt']);require(not a['events'] or time(fact['recordedAt'])>=time(a['events'][-1]['recordedAt']),'capture precedes journal')
    expected={'source':oid,'dimensionId':config['dimensionId'],'snapshotDigest':digest(fact['value']),'previousSnapshotDigest':None if previous is None else digest(previous['value'])}
    require(fact['provenance']==expected,'snapshot provenance/digest')
    require(fact['supersedes']==([] if previous is None else [previous['factId']]),'snapshot predecessor')
    if previous is not None:
        old=archive_from_native(previous['value'])
        require(previous['subjectId']==oid and previous['path']=='sync.register.snapshot' and previous['factId']==oid+':snapshot:'+old['root'].split(':')[1],'predecessor identity')
        require(previous['provenance']['snapshotDigest']==digest(previous['value']),'predecessor digest')
        require(config==old['config'] and len(a['events'])>len(old['events']) and a['events'][:len(old['events'])]==old['events'],'snapshot must strictly extend exact predecessor')
        require(time(fact['recordedAt'])>=time(previous['recordedAt']),'capture time rollback')
    return {'valid':True,'scope':'historical-restricted-projection','resumable':False}

END FILE sync_register.py

BEGIN FILE sync.schema.json sha256:fb9c7244025e77ac4cc68ae00ae89c7b65d5fe378742417cc0758a1ffa797aca
Complete JSON values, minified for review; spec.model.scope uses the explicitly identified identical earlier text. SHA identifies original formatted bytes.

PAYLOAD END — FRAGMENT 4/15
