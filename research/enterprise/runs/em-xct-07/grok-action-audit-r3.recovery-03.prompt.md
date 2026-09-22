SAME FROZEN R3 SOURCE RECOVERY 3/9. Browser paragraph rendering adds blank separator lines; all nonempty lines and indentation are verified unchanged. These are static display fragments, not raw-byte hash verification.
Do not audit yet. Reply only ACK 3/9 if all code in this fragment is visible. No tools.
BEGIN action_bundle.py fragment 3/9
actor,'key':key})
    @staticmethod
    def _get(c,slot):
        row=c.execute('SELECT body FROM requests WHERE slot=?',(slot,)).fetchone()
        return json.loads(row[0]) if row else None
    @staticmethod
    def _save(c,request): c.execute('UPDATE requests SET body=? WHERE id=?',(_json(request),request['requestId']))
    @staticmethod
    def _fresh_id(c,prefix):
        value=_id(prefix)
        for table in ('definitions','resources','requests','events'):
            require(not c.execute('SELECT 1 FROM '+table+' WHERE id=?',(value,)).fetchone(),'generated-id-collision')
        return value
    @staticmethod
    def _event(c,m,request,kind,payload,now):
        eid=Executor._fresh_id(c,'evt')
        cur=c.execute('INSERT INTO events(id,body) VALUES(?,?)',(eid,'{}'))
        e={'eventId':eid,'sequence':cur.lastrowid,'controlSequence':m['control_sequence'],'kind':kind,'requestId':request['requestId'],'recordedAt':now,'issuerId':m['issuer'],'payload':payload}
        validate('Event',e)
        c.execute('UPDATE events SET body=? WHERE sequence=?',(_json(e),cur.lastrowid)); return e
    @staticmethod
    def _definition(c,intent,now):
        pin=intent['definition']
        row=c.execute('SELECT * FROM definitions WHERE id=? AND version=? AND digest=?',(pin['definitionId'],pin['version'],pin['sha256'])).fetchone()
        if not row: return None,False
        d=json.loads(row['body'])
        return d,bool(row['available'] and d['validFrom']<=now<d['validUntil'])
    @staticmethod
    def _public_event(event):
        # A caller's one-request projection must not expose Dimension-wide
        # activity counters. The complete event remains in privileged evidence.
        return {k:v for k,v in event.items() if k not in ('sequence','controlSequence')}
    @staticmethod
    def _out(c,request,readable,code=None):
        if not readable: return dict(WITHHELD)
        if code and (not request or code=='key-conflict'): return {'status':code}
        result={'status':'key-retired' if request['keyRetired'] else request['state'],'requestId':request['requestId'],'intentDigest':request['intentDigest']}
        if code: result.update(status=code,requestState=request['state'])
        if request['receiptId']:
            result['receipt']=Executor._public_event(json.loads(c.execute('SELECT body FROM events WHERE id=?',(request['receiptId'],)).fetchone()[0]))
        return result

    def dispatch(self,raw,key,actor,now,*,_fault=None):
        """Admit/try a closed synthetic intent. Key is per authenticated actor/store.

        _fault is test instrumentation, never an untrusted transport parameter.
        Malformed, absent and unauthorized diagnostics share the withheld response.
        A response does not disclose whether execute-only actions produced effects.
        """
        try:
            intent=validate('Intent',parse(raw)); require(intent['actorId']==actor,'authenticated-actor')
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                require(intent['dimensionId']==m['dimension'],'dimension')
                policy=self._policy(c,m); request=self._get(c,slot)
                readable=bool(matching_rules(policy,intent,'read',now))
                if request:
                    readable=readable and bool(matching_rules(policy,request['intent'],'read',now))
                    if request['intentDigest']!=digest(intent) or encoded(request['intent'])!=encoded(intent):
                        return self._out(c,request,readable,'key-conflict')
                    if request['keyRetired']: return self._out(c,request,readable)
                definition,available=self._definition(c,intent,now)
                if request and not any(matching_rules(policy,intent,a,now) for a in ('submit','execute','read','cancel','observe')):
                    return dict(WITHHELD)
                if not request:
                    if not matching_rules(policy,intent,'submit',now): return dict(WITHHELD)
                    if not definition or definition['mode']!='synthetic-executable': return self._out(c,None,readable,'definition-not-executable')
                    if intent['purpose'] not in definition['purposes']: return self._out(c,None,readable,'definition-purpose')
                    request={'requestId':self._fresh_id(c,'req'),'keyHash':slot,'intentDigest':digest(intent),'intent':intent,'submittedAt':now,'submissionEventId':_id('placeholder'),'state':'pending','receiptId':None,'keyRetired':False}
                    e=self._event(c,m,request,'submission',{'intentDigest':request['intentDigest']},now)
                    request['submissionEventId']=e['eventId']
                    c.execute('INSERT INTO requests VALUES(?,?,?)',(request['requestId'],slot,_json(request)))
                self._event(c,m,request,'delivery',{'intentDigest':request['intentDigest']},now)
                matches=matching_rules(policy,intent,'execute',now)
                allowed=bool(matches and available)
                trial=self._event(c,m,request,'try',{'decision':{'action':'execute','policyRevision':m['policy_revision'],'allowed':allowed,'matchedRuleDigests':matches,'definitionAvailable':available}},now)
                if request['state']!='pending': return self._out(c,request,readable,None if allowed else 'current-execution-denied')
                if now>=intent['expiresAt']:
                    self._terminal(c,m,request,'expired','deadline',now,trial['eventId'])
                elif not allowed: return self._out(c,request,readable,'current-execution-denied')
                else:
                    row=c.execute('SELECT * FROM resources WHERE id=? ORDER BY revision DESC LIMIT 1',(intent['resourceId'],)).fetchone()
                    reason='resource-revision'
                    valid=bool(row and row['revision']==intent['expectedRevision'])
                    if intent['compensatesReceiptId']:
                        old=c.execute('SELECT body FROM events WHERE i
END fragment 3/9