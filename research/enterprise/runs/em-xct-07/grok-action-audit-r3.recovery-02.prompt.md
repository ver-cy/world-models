SAME FROZEN R3 SOURCE RECOVERY 2/9. Browser paragraph rendering adds blank separator lines; all nonempty lines and indentation are verified unchanged. These are static display fragments, not raw-byte hash verification.
Do not audit yet. Reply only ACK 2/9 if all code in this fragment is visible. No tools.
BEGIN action_bundle.py fragment 2/9
ritative fixture. Public methods return redacted results.

    The host must construct authenticated actor/time inputs and isolate admin API,
    exports and database access. The epoch pin detects a wrong store, not a coherent
    rollback. Restored stores require external continuity reconciliation before use.
    """
    def __init__(self,path,expected_epoch):
        self.path=Path(path).resolve(); self.expected_epoch=expected_epoch

    @classmethod
    def create(cls,path,dimension,issuer,now):
        require(re.fullmatch(SCHEMA['$defs']['Intent']['properties']['dimensionId']['pattern'],dimension) is not None,'dimension-id')
        require(re.fullmatch(SCHEMA['$defs']['Intent']['properties']['dimensionId']['pattern'],issuer) is not None,'issuer-id')
        cls._time(now)
        path=Path(path).resolve(); path.parent.mkdir(parents=True,exist_ok=True)
        # Exclusive create, so accidental use never truncates a prior history.
        with path.open('xb'): pass
        epoch=_id('epoch')
        c=sqlite3.connect(path)
        try:
            c.executescript(SQL)
            c.execute('INSERT INTO meta VALUES(1,?,?,?,?,0,0)',(dimension,issuer,epoch,now))
            c.execute('INSERT INTO policies VALUES(0,?,?,0)',('[]',now)); c.commit()
        finally: c.close()
        return cls(path,epoch)

    @staticmethod
    def _time(now): require(type(now) is int and 946684800<=now<=4102444800,'host-time')

    @contextmanager
    def _tx(self,now):
        self._time(now)
        c=sqlite3.connect(self.path.as_uri()+'?mode=rw',uri=True,timeout=15,isolation_level=None)
        c.row_factory=sqlite3.Row
        try:
            c.execute('PRAGMA synchronous=FULL'); c.execute('BEGIN IMMEDIATE')
            meta=dict(c.execute('SELECT * FROM meta WHERE id=1').fetchone())
            require(meta['epoch']==self.expected_epoch,'store-epoch')
            require(now>=meta['clock'],'host-clock-regression')
            mseq=meta['control_sequence']+1
            require(mseq<=9007199254740991,'control-sequence-overflow')
            c.execute('UPDATE meta SET clock=?,control_sequence=? WHERE id=1',(now,mseq))
            meta['control_sequence']=mseq; meta['clock']=now
            yield c,meta
            # Check before COMMIT: an overflowing operation, including its effect,
            # request and clock increment, rolls back as one unit.
            for table in ('definitions','policies','resources','requests','events'):
                require(c.execute('SELECT COUNT(*) FROM '+table).fetchone()[0]<=MAX_ROWS,'store-capacity')
            c.execute('COMMIT')
        except BaseException:
            if c.in_transaction: c.execute('ROLLBACK')
            raise
        finally: c.close()

    def set_policy(self,policy,now):
        """TRUSTED fixture host administration: verify issuer standing/basis externally."""
        validate('Policy',policy)
        with self._tx(now) as (c,m):
            rev=m['policy_revision']+1
            # Reserve the final policy row for a host-wide revocation. Never
            # overwrite older policy evidence or silently create a new store.
            require(not policy or rev<MAX_ROWS-1,'policy-revocation-reserve')
            c.execute('INSERT INTO policies VALUES(?,?,?,?)',(rev,_json(policy),now,m['control_sequence']))
            c.execute('UPDATE meta SET policy_revision=? WHERE id=1',(rev,))
            return rev

    def add_definition(self,definition,now):
        validate('ActionDefinition',definition)
        with self._tx(now) as (c,m):
            require(not c.execute('SELECT 1 FROM requests WHERE id=? UNION ALL SELECT 1 FROM events WHERE id=?',(definition['definitionId'],definition['definitionId'])).fetchone(),'object-kind-collision')
            require(not c.execute('SELECT 1 FROM resources WHERE id=?',(definition['definitionId'],)).fetchone(),'object-kind-collision')
            old=c.execute('SELECT body FROM definitions WHERE id=? AND version=?',(definition['definitionId'],definition['version'])).fetchone()
            if old:
                require(old['body']==_json(definition),'definition-version-conflict'); return
            c.execute('INSERT INTO definitions(id,version,body,digest,available,recorded_at,control_sequence) VALUES(?,?,?,?,1,?,?)',
                      (definition['definitionId'],definition['version'],_json(definition),digest(definition),now,m['control_sequence']))

    def retire_definition(self,reference,now):
        validate('DefinitionRef',reference)
        with self._tx(now) as (c,m):
            require(c.execute('UPDATE definitions SET available=0,retired_sequence=COALESCE(retired_sequence,?) WHERE id=? AND version=? AND digest=?',
                  (m['control_sequence'],reference['definitionId'],reference['version'],reference['sha256'])).rowcount==1,'unknown-definition')

    def add_resource(self,resource_id,labels,now):
        validate('Labels',labels)
        require(type(resource_id) is str and re.fullmatch(SCHEMA['$defs']['Intent']['properties']['resourceId']['pattern'],resource_id) is not None,'resource-id')
        with self._tx(now) as (c,m):
            require(not c.execute('SELECT 1 FROM requests WHERE id=? UNION ALL SELECT 1 FROM events WHERE id=?',(resource_id,resource_id)).fetchone(),'object-kind-collision')
            require(not c.execute('SELECT 1 FROM definitions WHERE id=?',(resource_id,)).fetchone(),'object-kind-collision')
            require(not c.execute('SELECT 1 FROM resources WHERE id=?',(resource_id,)).fetchone(),'resource-exists')
            c.execute('INSERT INTO resources VALUES(?,0,?,?,?)',(resource_id,_json(labels),now,m['control_sequence']))

    @staticmethod
    def _policy(c,m): return json.loads(c.execute('SELECT body FROM policies WHERE revision=?',(m['policy_revision'],)).fetchone()[0])
    @staticmethod
    def _slot(actor,key):
        require(type(key) is str and re.fullmatch('[A-Za-z0-9._:-]{8,128}',key) is not None,'retry-key')
        return digest({'actorId':
END fragment 2/9