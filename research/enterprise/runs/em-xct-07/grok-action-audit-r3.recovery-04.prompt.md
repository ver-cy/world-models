SAME FROZEN R3 SOURCE RECOVERY 4/9. Browser paragraph rendering adds blank separator lines; all nonempty lines and indentation are verified unchanged. These are static display fragments, not raw-byte hash verification.
Do not audit yet. Reply only ACK 4/9 if all code in this fragment is visible. No tools.
BEGIN action_bundle.py fragment 4/9
d=?',(intent['compensatesReceiptId'],)).fetchone()
                        original=json.loads(old[0]) if old else None
                        p=original['payload'] if original else {}
                        original_request=c.execute('SELECT body FROM requests WHERE id=?',(original['requestId'],)).fetchone() if original else None
                        oi=json.loads(original_request[0])['intent'] if original_request else {}
                        same_context=all(oi.get(k)==intent[k] for k in ('actorId','principalId','purpose','audience','dimensionId'))
                        valid=bool(valid and original and original['kind']=='receipt' and same_context and p['resourceId']==intent['resourceId'] and p['definition']==intent['definition'] and p['afterRevision']==intent['expectedRevision'] and p['beforeLabels']==intent['parameters']['labels'])
                        reason='compensation-precondition'
                    if not valid: self._terminal(c,m,request,'rejected-precondition',reason,now,trial['eventId'])
                    else:
                        if _fault=='before-effect': raise Refused('injected-rollback')
                        after=row['revision']+1
                        require(after<=9007199254740991,'revision-overflow')
                        c.execute('INSERT INTO resources VALUES(?,?,?,?,?)',(intent['resourceId'],after,_json(intent['parameters']['labels']),now,m['control_sequence']))
                        if _fault=='after-effect': raise Refused('injected-rollback')
                        receipt=self._event(c,m,request,'receipt',{'definition':intent['definition'],'resourceId':intent['resourceId'],'beforeRevision':row['revision'],'afterRevision':after,'beforeLabels':json.loads(row['labels']),'afterLabels':intent['parameters']['labels'],'compensatesReceiptId':intent['compensatesReceiptId'],'tryEventId':trial['eventId']},now)
                        request['receiptId']=receipt['eventId']; request['state']='committed'; self._save(c,request)
                result=self._out(c,request,readable)
            if _fault=='after-commit': raise ResponseLost('Committed transaction; caller did not receive the response. Reconcile using the SAME key.')
            return result
        except (ValueError,sqlite3.Error,KeyError,TypeError,IndexError,AttributeError,OverflowError,RecursionError): return dict(WITHHELD)

    def _terminal(self,c,m,request,state,reason,now,trial=None):
        require(request['state']=='pending','terminal-transition')
        self._event(c,m,request,'disposition',{'from':'pending','to':state,'reason':reason,'tryEventId':trial},now)
        request['state']=state; self._save(c,request)

    def lookup(self,key,actor,now):
        try:
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                request=self._get(c,slot)
                if not request: return dict(WITHHELD)
                return self._out(c,request,bool(matching_rules(self._policy(c,m),request['intent'],'read',now)))
        except (ValueError,sqlite3.Error,KeyError,TypeError,IndexError,AttributeError,OverflowError,RecursionError): return dict(WITHHELD)

    def cancel(self,key,actor,now):
        try:
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                r=self._get(c,slot)
                if not r: return dict(WITHHELD)
                policy=self._policy(c,m); readable=bool(matching_rules(policy,r['intent'],'read',now))
                if r['keyRetired']: return self._out(c,r,readable)
                matches=matching_rules(policy,r['intent'],'cancel',now)
                if not matches and not readable: return dict(WITHHELD)
                trial=self._event(c,m,r,'try',{'decision':{'action':'cancel','policyRevision':m['policy_revision'],'allowed':bool(matches),'matchedRuleDigests':matches,'definitionAvailable':self._definition(c,r['intent'],now)[1]}},now)
                if not matches: return self._out(c,r,readable,'current-cancellation-denied')
                if r['state']=='pending':
                    state='expired' if now>=r['intent']['expiresAt'] else 'cancelled'
                    self._terminal(c,m,r,state,'deadline' if state=='expired' else 'authorized-cancellation',now,trial['eventId'])
                return self._out(c,r,readable)
        except (ValueError,sqlite3.Error,KeyError,TypeError,IndexError,AttributeError,OverflowError,RecursionError): return dict(WITHHELD)

    def observe(self,key,actor,now,claim,reason,corrects=None):
        try:
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                r=self._get(c,slot)
                if not r: return dict(WITHHELD)
                policy=self._policy(c,m); readable=bool(matching_rules(policy,r['intent'],'read',now))
                matches=matching_rules(policy,r['intent'],'observe',now)
                if not readable or not matches or r['keyRetired']: return dict(WITHHELD)
                if corrects:
                    old=c.execute('SELECT body FROM events WHERE id=?',(corrects,)).fetchone()
                    previous=json.loads(old[0]) if old else None
                    require(previous and previous['kind']=='observation' and previous['requestId']==r['requestId'] and previous['payload']['observerId']==actor,'observation-predecessor')
                    observations=[json.loads(x[0]) for x in c.execute('SELECT body FROM events')]
                    require(not any(x['kind']=='observation' and x['payload']['correctsEventId']==corrects for x in observations),'observation-already-corrected')
                trial=self._event(c,m,r,'try',{'decision':{'action':'observe','policyRevision':m['policy_revision'],'allowed':True,'matchedRuleDigests':matches,'definitionAvailable':self._definition(c,r['intent'],now)[1]}},now)
                e=self._event(c,m,r,'observation',{'observerId':actor,'claim':claim,'reason':reason,'correctsEventId':corrects,'tryEventId':trial['eventId']},now)
      
END fragment 4/9