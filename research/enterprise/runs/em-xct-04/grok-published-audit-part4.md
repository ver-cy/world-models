PUBLIC STATIC AUDIT INPUT, PART 4 OF 4. All parts are now supplied. Perform the independent no-tools static audit described in Part 1. State completeness honestly.

=Path(skill).resolve();pins=p.load(HERE/'tool-pins.json')
    for field,root in [('composerFiles',composer),('skillFiles',skill),('upstreamFiles',HERE/'upstream')]:
        for n,h in pins[field].items():p.require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'Unexpected trusted asset: '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    reports=[];at=c.now();expires=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    with tempfile.TemporaryDirectory(prefix='vercy-authority-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(folder,name,source,url):
            raw=source.read_bytes();dest=assets/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':folder+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':url}
        def release(mid,version,folder,spec,agents,base,native):
            ds=descriptor(folder,spec.name,spec,base+spec.name);da=descriptor(folder,'AGENTS.md',agents,base+'AGENTS.md');binding=None
            if native:
                binding={'id':'urn:vercy:binding:enterprise-temporal-history','version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',HERE/'runtime-model.reference.json',base+'runtime-model.reference.json'),'instanceSchema':descriptor(folder,'temporal.schema.json',HERE/'temporal.schema.json',base+'temporal.schema.json'),'companionValidator':descriptor(folder,'temporal.py',HERE/'temporal.py',base+'temporal.py'),'scope':'Own companion namespace/specification; no parent subtype. Explicit nested validation and admission required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':da,'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':at,'scope':'Synthetic candidate-installation exercise, not global parent ratification; publication and research assurance are separate.'}}
        parent='wm-xct-009-time-calendar';up=HERE/'upstream'/parent
        semantic=release('vr.wm-xct-009','0.3.0-research.1',parent,up/'spec.yaml',up/'AGENTS.md','https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/upstream/'+parent+'/',False)
        companion=release(PROFILE_ID,'0.1.0',SLUG,HERE/'spec.json',HERE/'AGENTS.md','https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/',True)
        companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ['startup','group','ai-team']:
            config,initial,first,second,q1,q2=fixture(name);target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json');dimension=config['dimension']
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:temporal','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic temporal reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:temporal:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic temporal '+name,dimension)
            installed=target/'models/composed'/SLUG/'temporal.py';p.require(c.digest(installed.read_bytes())==companion['binding']['companionValidator']['digest'],'Code differs');p.require(c.digest((installed.parent/'temporal.schema.json').read_bytes())==companion['binding']['instanceSchema']['digest'],'Schema differs')
            ms=importlib.util.spec_from_file_location('installed_temporal_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            replay1=module.admit(initial,q1,config,actor=config['writer'],now=T1);replay2=module.admit(replay1,q2,config,actor=config['writer'],now=T2)
            p.require(replay1==first and replay2==second,'Admission differs');checkAt=max(at,NOW);oid=config['timeline'];operator='urn:synthetic:timeline-operator';register='urn:synthetic:governance-register'
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':timeline','name':'Synthetic temporal timeline','description':'Own companion namespace, not a domain state-machine subtype','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':register,'synthetic':True},'accessClass':'synthetic-private'}
            path=root/(name+'-object.json');path.write_bytes(p.encode(obj));append(target,'object',path);facts=[]
            for i,snapshot in enumerate([first,second],1):
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot-r'+str(i),'subjectId':oid,'path':'temporal.timeline.snapshot','value':snapshot,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[] if i==1 else [oid+':snapshot-r1'],'status':'asserted','provenance':{'source':register,'synthetic':True,'snapshotDigest':p.digest(snapshot),'previousSnapshotDigest':None if i==1 else p.digest(first)},'authority':{'source':operator,'rank':0},'masterSystem':register,'accessClass':'synthetic-private'}
                path=root/(name+'-fact'+str(i)+'.json');path.write_bytes(p.encode(fact));result=append(target,'fact',path);facts.append(target/result['written'])
            f1,f2=[p.load(x) for x in facts];p.require([f1['value'],f2['value']]==[first,second],'Stored roundtrip differs')
            module.validate_snapshot(f1,dimension=dimension,now=checkAt);module.validate_snapshot(f2,dimension=dimension,now=checkAt,previous=f1)
            def query(k):return module.resolve(f2['value'],config,actor=config['readers'][0],purpose='research',validAt='2026-02-01T00:00:00Z',knownAt=k,now=NOW)
            before,after=query('2026-01-31T00:00:00Z'),query('2026-02-11T00:00:00Z')
            p.require(before['segment']['value']==q1['segments'][0]['value'] and after['segment']['value']==q2['segments'][1]['value'],'Bitemporal stored answers differ')
            native=native_validate(target);p.require(native['valid'],'Native validation failed')
            original=facts[-1].read_bytes();bad=copy.deepcopy(f2);bad['value']['commits'][0]['request']['segments'][0]['validFrom']='not-an-instant';facts[-1].write_bytes(p.encode(bad));outer=native_validate(target);nested=False
            try:module.validate_snapshot(bad,dimension=dimension,now=checkAt,previous=f1)
            except module.Invalid:nested=True
            finally:facts[-1].write_bytes(original)
            p.require(outer['valid'] and nested,'Native/companion distinction missing')
            negatives=[]
            for label,mutator in [('truncation',lambda x:x['value']['commits'].clear()),('digest',lambda x:x['provenance'].update(snapshotDigest='sha256:'+'0'*64)),('subject',lambda x:x.update(subjectId='urn:synthetic:wrong')),('predecessor',lambda x:x.update(supersedes=[]))]:
                bad=copy.deepcopy(f2);mutator(bad);failed=False
                if label=='truncation':bad['provenance']['snapshotDigest']=p.digest(bad['value'])
                try:module.validate_snapshot(bad,dimension=dimension,now=checkAt,previous=f1)
                except module.Invalid:failed=True
                p.require(failed,'Accepted '+label);negatives.append(label)
            cross_rejected=False
            try:module.validate_snapshot(f1,dimension='urn:synthetic:other-dimension',now=checkAt)
            except module.Invalid:cross_rejected=True
            p.require(cross_rejected,'Cross-Dimension snapshot admitted');negatives.append('cross-Dimension')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':1,'facts':2,'native':native,'roundTripEqualsInput':True,'admissionReplayedThroughInstalledCompanion':True,'negativeCasesRejected':negatives,'storedAnswers':[before,after],'invalidNestedSnapshot':{'native':outer,'companionRejected':nested},'envelopeAuthorityMeaning':'Later native storage of synthetic pre-existing host history; inner receipts do not establish earlier native Dimension existence or domain fact priority','pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-temporal-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'temporal.py',HERE/'temporal.schema.json',HERE/'spec.json',HERE/'tool-pins.json',HERE/'test_temporal.py']},'limits':'Three synthetic new Dimensions; own companion plus optional semantic-only parent. No IAM, domain truth/transition, durable concurrency, production capacity or existing-Dimension migration proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))

</file-content>
END FILE acceptance.py

## FILE whole-object-coverage.yaml
Raw SHA-256: d7591ea1735788c0808b743060fc1e7896494f0ac0986fe95949da89128e94e6

<file-content name="whole-object-coverage.yaml">
{
  "canonicalFacets": [
    "identity-class",
    "direct-properties",
    "recognition-observation",
    "capabilities-behaviour-actions",
    "context-evidence"
  ],
  "types": {
    "Timeline": {
      "identity-class": {
        "status": "required",
        "coverage": "Governed timeline URI and fixed scope"
      },
      "direct-properties": {
        "status": "required",
        "coverage": "Header and append-only bounded commits"
      },
      "recognition-observation": {
        "status": "required",
        "coverage": "Recorded history observed via explicitly cut view; source truth not inferred"
      },
      "capabilities-behaviour-actions": {
        "status": "required",
        "coverage": "Host admission, archival and query"
      },
      "context-evidence": {
        "status": "required",
        "coverage": "Current config and exact predecessor root"
      }
    },
    "TimelineCommit": {
      "identity-class": {
        "status": "required",
        "coverage": "Revision URI, key and local sequence"
      },
      "direct-properties": {
        "status": "required",
        "coverage": "Host receipt/writer, exact request and complete snapshot"
      },
      "recognition-observation": {
        "status": "required",
        "coverage": "Registration is local receipt, not human awareness or event observation"
      },
      "capabilities-behaviour-actions": {
        "status": "required",
        "coverage": "Immutable; superseded by a new commit, never edited"
      },
      "context-evidence": {
        "status": "required",
        "coverage": "Previous digest, reason and source-declared time"
      }
    },
    "ValidSegment": {
      "identity-class": {
        "status": "required",
        "coverage": "Embedded commit-relative value, no independent identity"
      },
      "direct-properties": {
        "status": "required",
        "coverage": "Half-open effective interval and exact external pins"
      },
      "recognition-observation": {
        "status": "required",
        "coverage": "Coverage membership only, truth and real-world observation unevaluated"
      },
      "capabilities-behaviour-actions": {
        "status": "required",
        "coverage": "No independent mutation; new full snapshot for correction"
      },
      "context-evidence": {
        "status": "required",
        "coverage": "Schema/state bindings and containing commit"
      }
    },
    "SchemaBinding": {
      "identity-class": {
        "status": "required",
        "coverage": "Whole id/version/digest tuple"
      },
      "direct-properties": {
        "status": "required",
        "coverage": "Numeric triplet grammar and sha256 syntax"
      },
      "recognition-observation": {
        "status": "required",
        "coverage": "Exact accepted tuple comparison, payload conformance untested"
      },
      "capabilities-behaviour-actions": {
        "status": "required",
        "coverage": "Read-only pin; new version for changed definition"
      },
      "context-evidence": {
        "status": "required",
        "coverage": "External publisher responsibility and historical preservation"
      }
    },
    "StateReference": {
      "identity-class": {
        "status": "required",
        "coverage": "Profile pin plus axis/code embedded value"
      },
      "direct-properties": {
        "status": "required",
        "coverage": "One optional status axis membership"
      },
      "recognition-observation": {
        "status": "required",
        "coverage": "Vocabulary membership only, not proof of a transition"
      },
      "capabilities-behaviour-actions": {
        "status": "required",
        "coverage": "No state machine or domain effect executed"
      },
      "context-evidence": {
        "status": "required",
        "coverage": "Host domain definition/evidence, no executable delegation"
      }
    },
    "TimelineAnswer": {
      "identity-class": {
        "status": "required",
        "coverage": "Ephemeral query result, no persistent domain identity"
      },
      "direct-properties": {
        "status": "required",
        "coverage": "Explicit cutoffs, selected commit/segment, missing context"
      },
      "recognition-observation": {
        "status": "required",
        "coverage": "Shows recorded assertion or insufficient context, not truth"
      },
      "capabilities-behaviour-actions": {
        "status": "required",
        "coverage": "Current full-reader query, no writer authority"
      },
      "context-evidence": {
        "status": "required",
        "coverage": "Input/root/policy digests and explicit current vs historical archive context"
      }
    }
  },
  "limits": "Each value/derived type is scoped individually; no mass/physical dimension invented. Conceptual references do not claim executable delegation."
}

</file-content>
END FILE whole-object-coverage.yaml

## FILE mastership-and-rights.yaml
Raw SHA-256: 9dc4b36a2a84e8e636f1ec54b2bd043ed08849c224370353ac13ff4cc587e46f

<file-content name="mastership-and-rights.yaml">
{
  "facts": [
    {
      "fact": "scope/identity",
      "semanticOwner": "Domain scope steward",
      "master": "Configured local register",
      "writer": "Current configured writer after host identity check",
      "readerPurpose": "Whole timeline reader and purpose gate",
      "validTime": "Scope fixed in this profile",
      "provenance": "Registration config",
      "conflict": "Duplicate scope detected by external registry",
      "retention": "Host-owned, erasure integration required"
    },
    {
      "fact": "effective segments and state declarations",
      "semanticOwner": "Domain fact owner",
      "master": "One designated writer per governed scope",
      "writer": "Authenticated configured writer",
      "readerPurpose": "Current full-history readers/purposes",
      "validTime": "Half-open UTC-second segments",
      "provenance": "Commit writer/reason/sourceRecordedAt plus optional external provenance model",
      "conflict": "Expected-head/replay rejection; host durable conflict artifact",
      "retention": "Archive retains all history; no disposal implementation"
    },
    {
      "fact": "receipt/order/head",
      "semanticOwner": "Timeline operator",
      "master": "Trusted host serialized store/clock",
      "writer": "Host only",
      "readerPurpose": "Current full-history gate",
      "validTime": "Local recorded axis, never business-valid time",
      "provenance": "Contiguous sequence and predecessor digest",
      "conflict": "Clock regression or stale head rejects",
      "retention": "No truncation/rollover in current implementation"
    },
    {
      "fact": "schema/state profile definitions",
      "semanticOwner": "External schema/domain publisher",
      "master": "External source, exact accepted pin list locally",
      "writer": "Host steward changes current config; definitions not edited here",
      "readerPurpose": "Pins may also be sensitive; full-history gate",
      "validTime": "Historical segment retains exact pin",
      "provenance": "ID/version/digest declaration, not signature",
      "conflict": "Repointed ID/version rejects",
      "retention": "Host must retain accessible definitions for interpretation"
    }
  ]
}

</file-content>
END FILE mastership-and-rights.yaml

## FILE requirements.txt
Raw SHA-256: 5bc814e05c852ada4731d68f061aab75fd7b9d4f2fd332360a9f5362984a7e89

<file-content name="requirements.txt">
jsonschema==4.26.0
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1

</file-content>
END FILE requirements.txt

## FILE runtime-model.reference.json
Raw SHA-256: f2b69d8ae6f6a9426be693458f53894ff7c3e04fe5038890adf5b65d06edbd17

<file-content name="runtime-model.reference.json">
{
  "format": "vercy-runtime-model-schema",
  "schemaVersion": "1.0.0",
  "modelId": "vr.profile.enterprise-temporal-history",
  "paths": {
    "temporal.timeline.snapshot": {
      "valueTypes": [
        "object"
      ],
      "units": [
        null
      ]
    }
  }
}

</file-content>
END FILE runtime-model.reference.json

## FILE adoption-limits.md
Raw SHA-256: 8ea3e18f26b0da30ddf6b9460520c0420c9fe5c971b05c4f2bf3a8db95028f52

<file-content name="adoption-limits.md">
# Adoption limits

Reviewable draft; one single-valued scope and one host sequencer. No real-organization validation, distributed consistency, engine adapter, fine-grained disclosure, IAM, payload validation, transition engine, signatures, clock attestation, durable conflicts, erasure or existing-Dimension migration. Full snapshots have structural limits, not an enterprise throughput claim. Before production, implement durable serialized storage, scope uniqueness, authentication and current rights, a reliable clock, conflict audit, strict input parser/budgets and locally required retention/disposal. Historical source times never establish earlier local knowledge. Parent source/profile holds remain in crosswalk.json.

At capacity, even a new archive commit may be refused; use host policy to freeze writes and plan migration before exhaustion. The host owns global native fact-ID uniqueness. The nested validator checks only the immediate predecessor ID and assumes native envelope checks were already performed.

The inner recorded axis belongs to the timeline host, not to the native Dimension storage log. A pre-existing trusted host timeline can be installed later; synthetic January/February receipts in acceptance do not assert that the newly created Dimension existed then. Clock authenticity and history authenticity remain host obligations. A mistakenly admitted forward receipt can disable all reads and writes until catch-up. Before admission, enforce a clock-skew guard against a trusted reference. If it fails, quarantine/freeze and preserve the original evidence; recovery needs verified catch-up with current policy or an explicitly governed new timeline identity with provenance and disclosed continuity loss. No in-place repair or automatic recovery is implemented.

</file-content>
END FILE adoption-limits.md

## FILE migration.md
Raw SHA-256: 06e3373c4727b1246656d115701bb314249add13f759a93ed6219f9fa41a9936

<file-content name="migration.md">
# Migration and loss

Only complete same-contract-version JSON roundtrip is implemented and tested. A different version refuses. Keep the original root and all pins; perform any new conversion in a separately governed staging process with explicit loss, provenance, rollback and ownership. Source SQL system-time columns are not automatically business-valid time. SCD2 can lose recorded history; timezone/fractional conversions can lose precision. No such adapter is included or silently executed. Native acceptance covers new synthetic Dimensions only. Rollback to an older root is not an allowed history update; restoration is an operational recovery requiring the complete trusted chain.

The inner recorded axis belongs to the timeline host, not to the native Dimension storage log. A pre-existing trusted host timeline can be installed later; synthetic January/February receipts in acceptance do not assert that the newly created Dimension existed then. Clock authenticity and history authenticity remain host obligations. A mistakenly admitted forward receipt can disable all reads and writes until catch-up. Before admission, enforce a clock-skew guard against a trusted reference. If it fails, quarantine/freeze and preserve the original evidence; recovery needs verified catch-up with current policy or an explicitly governed new timeline identity with provenance and disclosed continuity loss. No in-place repair or automatic recovery is implemented.

</file-content>
END FILE migration.md

## FILE bindings/native-v3.md
Raw SHA-256: 67d8e6d4929fd35fc0e291f426126db4a47f76c38910b815951c0fd6abec6f3b

<file-content name="bindings/native-v3.md">
# Native V3 binding

Install `vr.profile.enterprise-temporal-history` under its own namespace. The optional Time / Calendar parent is semantic-only. A timeline object owns `temporal.timeline.snapshot` facts containing the complete root. Outer fact provenance/authority describes snapshot storage, not domain fact precedence. Validate the outer envelope with V3, then `validate_snapshot` and `validate_extension` using the latest trusted predecessor. The nested validator is mandatory even when native validation passes. Do not expose full roots to write-only callers. acceptance.py replays admission and roundtrips two snapshots in three fresh synthetic Dimensions.

The inner recorded axis belongs to the timeline host, not to the native Dimension storage log. A pre-existing trusted host timeline can be installed later; synthetic January/February receipts in acceptance do not assert that the newly created Dimension existed then. Clock authenticity and history authenticity remain host obligations. A mistakenly admitted forward receipt can disable all reads and writes until catch-up. Before admission, enforce a clock-skew guard against a trusted reference. If it fails, quarantine/freeze and preserve the original evidence; recovery needs verified catch-up with current policy or an explicitly governed new timeline identity with provenance and disclosed continuity loss. No in-place repair or automatic recovery is implemented.

</file-content>
END FILE bindings/native-v3.md

## FILE crosswalk.json
Raw SHA-256: f0c6d2bde017e1ebc040f81ac313f81d4a1775d87db9b194cac9a4c492302328

<file-content name="crosswalk.json">
{
  "claim": "narrower/overlap, never exactMatch or subtype",
  "parents": [
    {
      "oldId": "N11",
      "currentId": "WM-XCT-009",
      "registryId": "vr.wm-xct-009",
      "version": "0.3.0-research.1",
      "runtimeStatus": "published",
      "installable": true,
      "assurance": "reviewable-draft",
      "sha256": "060511804c09ed5992e3fdf222839f97a0d340db0a2cba3c4c08aded7767e90d",
      "liveByteEqualityVerified": true,
      "relation": "narrower-selected-pattern-overlap",
      "action": "semantic-reference-only",
      "readScope": "Full files recursively parsed and all sections retained in research checkpoint; boundary, composition, holds and structured inventory inspected. No complete legacy validator/source conformance audit claimed.",
      "holds": [
        "Verify live availability, editions and claim-level support for every accepted primary source, including current tzdb, BIPM/IERS, IETF and Unicode releases.",
        "Complete jurisdictional profiles for holiday and working-day authorities and direct clause-level verification of paywalled ISO 8601-1/2 before promoting a universal completeness claim."
      ],
      "losses": "Narrow single-scope UTC-second linear snapshots; no broad parent conformance, engine, calendar or lifecycle readiness inherited."
    },
    {
      "oldId": null,
      "currentId": "WM-XCT-021",
      "registryId": "vr.wm-xct-021",
      "version": "0.3.0-research.1",
      "runtimeStatus": "published",
      "installable": true,
      "assurance": "reviewable-draft",
      "sha256": "87c8c50f6f4c2eb3478751f01a08c6c37c6a85f97f4c056505b13cdf561314e9",
      "liveByteEqualityVerified": true,
      "relation": "narrower-selected-pattern-overlap",
      "action": "semantic-reference-only",
      "readScope": "Full files recursively parsed and all sections retained in research checkpoint; boundary, composition, holds and structured inventory inspected. No complete legacy validator/source conformance audit claimed.",
      "holds": [
        "Verify live editions and claim-level support for all accepted SCXML, W3C PROV/OWL-Time, HL7 FHIR, DCMI, ISO and records-management sources.",
        "Validate the mixin against at least five independent profiles: publication, workflow/request, clinical interpretation, software release and records disposition."
      ],
      "losses": "Narrow single-scope UTC-second linear snapshots; no broad parent conformance, engine, calendar or lifecycle readiness inherited."
    },
    {
      "oldId": null,
      "currentId": "WM-XCT-022",
      "registryId": "vr.wm-xct-022",
      "version": "0.3.0-research.2",
      "runtimeStatus": "published",
      "installable": true,
      "assurance": "reviewable-draft",
      "sha256": "40ced88212f4c90690bdbb35bf2429fe627d11793bee5e587b5b10b99f49fe85",
      "liveByteEqualityVerified": true,
      "relation": "narrower-selected-pattern-overlap",
      "action": "semantic-reference-only",
      "readScope": "Full files recursively parsed and all sections retained in research checkpoint; boundary, composition, holds and structured inventory inspected. No complete legacy validator/source conformance audit claimed.",
      "holds": [
        "Live-source verification is outstanding for all 27 base sources and for the three newly admitted alternative sources (DataCite versioning, PAV 2.3.1, ADMS 2.00). Recency-sensitive pins must be re-checked at publication time: the IANA link-relations registry, the Git glossary build, the NIST SP 800-53 control release, and the DataCite guidance page, which is living documentation rather than a dated specification.",
        "Domain-profile validation has not been performed. The pack asserts applicability across regulated manufacturing, research data, software packaging, records management and web-resource publishing, but only US FDA 21 CFR Part 11 was actually retrieved; EU GMP Annex 11 is assumed similar and uncited. At least two contrasting profiles must be exercised before publication.",
        "Every external mapping must be rendered as declared alignment, never conformance, and the accepted DataCite, PAV and ADMS additions must carry that label explicitly along with their loss statements.",
        "Documented evidence gaps must appear in the published draft rather than be omitted: PREMIS 3.0 and OAIS returned HTTP 403, ISO 10007 and ISO 15489 are paywalled and unverified, and no normative bitemporal source was obtained, so the effective-period finding must ship marked as partial support.",
        "Source identifier remapping for the accepted findings and functions must be applied and re-checked before render, since the two packs use overlapping SRC identifiers for different documents."
      ],
      "losses": "Narrow single-scope UTC-second linear snapshots; no broad parent conformance, engine, calendar or lifecycle readiness inherited."
    }
  ],
  "candidates": [
    {
      "candidate": "TemporalValidity",
      "disposition": "implemented-narrow-value",
      "meaning": "Exact UTC-second half-open interval; calendar/uncertainty adapters deferred"
    },
    {
      "candidate": "Revision",
      "disposition": "split",
      "meaning": "Linear assertion commit here; opaque external artifact revision referenced; DAG/merge delegated conceptually to WM-XCT-022"
    },
    {
      "candidate": "LifecycleTransition",
      "disposition": "deferred-domain-execution",
      "meaning": "StateReference carries only vocabulary membership; actual transitions remain with domain host/WM-XCT-021"
    },
    {
      "candidate": "SchemaBinding",
      "disposition": "implemented-narrow-value",
      "meaning": "Accepted immutable id/version/digest tuple, not executable payload validation"
    }
  ]
}

</file-content>
END FILE crosswalk.json

## FILE tool-pins.json
Raw SHA-256: 9830b48feac14a372b427acbbb16db6bd37bded3f181ad3427ad0dfd86b43214

<file-content name="tool-pins.json">
{
  "composerVersion": "0.1.1",
  "composerFiles": {
    "composition.py": "78aa1c6c29f14c7adedefd7dd8b3683c845118c49bb48d04c5e92ae4989ce06e",
    "bootstrap_dimension.py": "5eb5491ecedcfa56ffe63d07383e9a650eed42a5d73f667c2feb2f34ea5180f5",
    "composition-plan.schema.json": "cc33e9ee4522cd586a2e1fb07307e6aa5361bf7cf3ca99a419c0f434d0e8a079",
    "policy.schema.json": "92e0386696c974b1e8a312b60ca08d981c223e9925c8f70dabdfa135b9041543"
  },
  "skillFiles": {
    "SKILL.md": "bbd714f5a0de9fad7b26df12be7fb31ce5935f3f54f3cd1037688121383cf963",
    "agents/openai.yaml": "f7234977b2cb542bc0fb1e7665a8a27684e0fa1400696dd6e086b4fef3829cb0",
    "mcp/server.py": "ef3b937e4ebcaa5d737f03f11e6ce5e0be80885e184c88a555e7a0d7b4c0e133",
    "references/autonomous-runtime.md": "ae9d728a214cb296dd97b9d172b60651270e77afcbab632fce04e84dd0a3453a",
    "references/compatibility.md": "b7c0b0ee6d16084f1422b9cb813d23c3f03cc45d047d17a43568067ebde34460",
    "references/concept-map.md": "c216fc5ffd94a55a254f2b61e1ef5630eb8ec09a5ae70db1617318662c43c3a1",
    "references/dimension-bootstrap.md": "7ab614fd1eba0326861d7d2d36cd690b99f26dd0f3333190401bf0782d8a6ed7",
    "references/federation-routing.md": "fb025d2cc62db14c553e0b364c70a47e6385d519d419dec706fb6cf483658159",
    "references/mcp-server.md": "7d1233ea34b34e927acf352c12bc367f58fda5bde249fb3e5e99aa05cff724ad",
    "references/memory-autostart.md": "d3b831e39f2dd5f32abc97d9748ef426e72c3f31e7dbcfff65296b4bf7de5e2e",
    "references/model-lifecycle.md": "9689f560884e12092ffa1fe0068e28f603095b6ffe8c719493f8f595fb3a06ee",
    "references/model-resolution-api.md": "f008dc97daa193b827b9eab76dbc574f104f8d464909cd5d0e71cb8a97749261",
    "references/presets.md": "71503847c1d67f1a227600cce96e5941ea4f3ac1cda1575fe849f18815962cb2",
    "references/public-entry.md": "15155eec00a259dfdf6a0469ccaceba444fcba635f1a42080b36063d924d22a6",
    "references/runtime-records.md": "71c495b38db59f048fe1ec27cd54e608adfeee5160e4d96141b18e43d6b1e809",
    "references/storage-selection.md": "2dd3b10bab2235d04fd3b7cf5411249bf54774efc734b9d08f93483c546bcc5a",
    "references/validation.md": "8c35e27e4fc6103b489ad8b34bd7b79eeb86a8e557752726e8f351ab4edfc9d0",
    "references/whole-object.md": "17d9a1275015c0152267f5a4a39659244ed16c25e81e748256a9324dc5bb7b66",
    "schemas/compatibility.schema.json": "bb32246583b04cedaff9d5e2aae75cca6e9afa014d73a6d4fcc9306054dec78a",
    "schemas/conflict-policy.schema.json": "dece868961a56fe0f50b93564986fb5862b5cbca6ecba138db894f9ea8f6a6c5",
    "schemas/dimension.schema.json": "b6645174e73f551d7bf27642c1887538a8e6d695d586d5101995e69dfa42ce57",
    "schemas/event.schema.json": "e0fbf7551d3b409bf8c04aad6cb6e2caa1dcbf3e703cee9ffe6ab23664f38db6",
    "schemas/fact.schema.json": "f15f9f652c44547384ed8ca7c0c5454a73ea7385de3ec18d8fed09502994ad0a",
    "schemas/object.schema.json": "ff7cab00542db5388946d0704b9aa3c33a49fc8057ec1df6ace7be00e1e43a0a",
    "schemas/relation.schema.json": "2b3b97267fbc400492948886af21010fd6592752c547269f723e7b989279135a",
    "schemas/runtime-model.schema.json": "2ce263747b220d16980bea70f1bca9c3bba59eeec90233d6c9b880759a902c42",
    "scripts/build_index.py": "807539c6d4522d0cbf8782e3a1466a471fa36895cb304b21ee704cb513112319",
    "scripts/create_dimension.py": "4cc00b03be88e9a2348eb681137d0b813b10aa0b76edc881f3e9ecf8345d5b8f",
    "scripts/migrate_dimension.py": "daae4db10760e9d44380c0606d016557ac3e52401f3a711ee11b5ad8c053f02a",
    "scripts/poll_model_requests.py": "91c4aede63bb2eee48e5d49fcdf59d75b0e23eb12511d012c419eb141167fea9",
    "scripts/query_dimension.py": "0c6e35345a91bdd85b7b129fedbb35f4359f6d786b39b927cc92870b65209c0c",
    "scripts/reconcile_models.py": "4fcf76ebaa08ebdbefd2f9ac6824337f8f7d0e9d0c05329f4b3b1669f6260236",
    "scripts/register_memory.py": "9479de2b71669042a73a2393280cc99c096795bf79f0a7eb3294025d2e82e406",
    "scripts/resolve_model_need.py": "25fb98bd2549c0bb7b743cebb62e666a14acd1bd7fa1a2de8548ae9f1d901d5d",
    "scripts/select_storage.py": "c08cdc15374cc496711cb2a6d3403808c008415abccfa3f3cf12f3015df400d3",
    "scripts/self_test.py": "fe9b493b5e7c33a58f97c4fe8c1b01b3457e5eca6e5e2732fbd3497bae402158",
    "scripts/validate_dimension.py": "815a938361420373b18448dda4caa5604d314230cf53fc6a07a9dcb96dd57df4",
    "scripts/vercy.py": "80e31ef4d4e02bab94859163f7975cbe9678e0b31db7d51ae7acd8506b65e20d",
    "scripts/vercy_runtime.py": "e538c64b9c824b503768b63dba5dc66a81c19ac7626eb9116579ba2925528664",
    "scripts/write_record.py": "c60274820fd3e5a55ec790f7e64fb0e0a7e218b7fe107f02d0fcb125091da4e5",
    "assets/dimension/AGENTS.md.template": "b435e4bc805e2aa084c648167350fd050993dab0aaa1d194697558de5586f69d",
    "assets/dimension/compatibility.yaml": "41244d13b2e8763f2f23c44f1ffefc7dde4801b4a54f5faa852d977e0f648a4f",
    "assets/dimension/context-routing.yaml": "52f3a4f8951e2faf3be8d6bd23af51fdfc477a347cc79db55bbcd3d717cd3f67",
    "assets/dimension/dimension.yaml": "e92c299d857962293f2a1c13d70717beff0ec955b3ab84ea1e2763d2cff3b1d7",
    "assets/dimension/federation.yaml": "358bf49507eb3f5c1e9fb86e45d9cc0ee9d14a8dc371f3af95af56dab0e6327b",
    "assets/dimension/memory.yaml": "50d47c53ee2be80d293a051c7c909cb2afdf8204f9a76eadfe5673eb6cd589b4",
    "assets/dimension/vercy.lock": "f360ae2f60e1d3f02bda506c3aed9587d6435a7d0200bef542888df32b469c99",
    "assets/icons/vercy-logo-1024.png": "8043b9a7080d1b64fea402ba0db8d42efb366862214fc1d68d8a99086401a705",
    "assets/icons/vercy-logo-512.png": "3832e0a25cec92cf22392a27c44b37524213844598c61a12d5032e3fea5fd690",
    "assets/presets/ai-subject.yaml": "ed547e7628d8c4509ed1873312b45f0521036b5235a3b795a2f2a0e4a147c3b7",
    "assets/presets/index.yaml": "69e79eb66cec03ab07badb301b0b4ebfb15b74b34daffeae78e7f11529140892",
    "assets/presets/kernel.yaml": "b699f89fc1d040e05584bb21e00a419a7704230caba42adc37cb70631defb43d",
    "assets/presets/organizational.yaml": "e70c6d196f1b5626f2e7646252dad4f2be961b7908ae198e9bc1d405cffad2a3",
    "assets/presets/personal.yaml": "c201473267e64958b9844e3557f8efc95b8be790581135c42c8c38566c841483",
    "assets/presets/reality.yaml": "2779668f8eeca66b74ff31527c323d3461f821089769ef5d7951c13afbfcad66",
    "assets/dimension/bindings/storage.yaml": "044db01cf746678283a98c96be0d1fb8a94997393b9161a5a32e59dfc813ba5c",
    "assets/dimension/data/index.md": "f10a3c8283ddc1ae608c6848cd561ac9b9d80a05ca684420ac185fa920b8b351",
    "assets/dimension/migrations/index.yaml": "9a20ae6fef67ca51d4c07a27558deb20af2a7b3dafe76893783ac01e86c0dce6",
    "assets/dimension/policies/access.yaml": "3b58ce30f6de01923dbbab069df0721552c3b9ab8ba405c30ac353ffb392779f",
    "assets/dimension/policies/autonomy.yaml": "6629691e60540e42eabeb63f746bcb99f79f383d7c85a57217e551d4ecc6ea27",
    "assets/dimension/policies/conflict-resolution.yaml": "241e97baa79198e4b02885f24ad1143b7ebfc3dbf52dc07e4bccb01ef31c72b2",
    "assets/dimension/policies/lifecycle.md": "91755112dd7854a7cb06598fcb53233c68b626bb015ca7f5a3a9307258eab232",
    "assets/dimension/policies/model-deployment.yaml": "637fc3ac655b7f5c2f36c814113b03803bce4366e62cb24bbeb4f36dba525771",
    "assets/dimension/registries/events.yaml": "8babba185339394a775d953024c857f6bcd4f6c1037bff9019af5c8512435fef",
    "assets/dimension/registries/meta-models.yaml": "4efb434d716f2c10a1c01deb79e44873ced31599446edab8b213e3fd7201206b",
    "assets/dimension/registries/meta-objects.yaml": "c1b417a3019d93c594dae9854951d57c3fcd73d73a88f258b3a13c8cb5e7e3d3",
    "assets/dimension/registries/model-links.yaml": "ecbac80f14627245ecdc5af12bb30331b88f688e8ebeaa34fba44ddc16e0c898",
    "assets/dimension/registries/model-requests.yaml": "7f01232fd4b812d942eed0e88f154f751e7f9fb1707402a5b6b4aaa16bdba319",
    "assets/dimension/data/events/README.md": "fa20d1960e40eee352679debcab28df245f9bef695ca72a27d28b69ab8e18737",
    "assets/dimension/data/facts/README.md": "80433bcda7964cb8819692bd442628f56b35aa6fca96bfde0d527b2d3ed38138",
    "assets/dimension/data/objects/README.md": "264ebb5440729741322828fd5e3c8a747c77a1662b0e64ab5ff9ce1a978ff4b8",
    "assets/dimension/data/relations/README.md": "d7a7d3e09a3c8d0c2e0304ffe89e5fa01ad9bde730497185a7a9da7d5bf51a22",
    "assets/presets/organizational/commercial-company.yaml": "ce8ee74e8fa61eec9583471f6b4982e920d172af3299bbfc2ed08163a6cbde2b",
    "assets/presets/organizational/community.yaml": "31cabe5a146e2b38d173f2cb08f7e5d0df60bbcf7f273082ba97b0dd7560f001",
    "assets/presets/organizational/family.yaml": "094438b226ed56859c72327d354e55e6ed2cd6c2658a1423ad345c326ac1a9c9",
    "assets/presets/organizational/state.yaml": "a2aaac7f20feaffe2494406ddc5b71629027fed6c04e94f65950dac991f6ff13"
  },
  "upstreamFiles": {
    "wm-xct-009-time-calendar/spec.yaml": "060511804c09ed5992e3fdf222839f97a0d340db0a2cba3c4c08aded7767e90d",
    "wm-xct-009-time-calendar/AGENTS.md": "f01631a0bba6ac2ec1903c8b1359e4d6b4e1fac6a1165b12d4b76be4b23e70c8",
    "wm-xct-009-time-calendar/publication.json": "1ab2061b5786df57e9eae47171864c2ff43e1538f582a5cc532bd3cf671e5ea1"
  }
}

</file-content>
END FILE tool-pins.json

## FILE host-integration-notes.md
Raw SHA-256: 8093da03e0e45b8584f55bedc0528121b0bede538519cd22f227505b89b56e77

<file-content name="host-integration-notes.md">
# Host integration notes after the third static audit

Codex clarification of residual low-severity findings N1–N3. This supplement was written after Claude's frozen R3 audit and is not represented as independently reviewed by either provider. It does not change the executable implementation.

Apply the trusted-reference clock-skew guard to **every call that takes now**, including reads, static validation and native snapshot validation, as well as admission. A backward read clock can create a read outage; a forward read clock can activate future policy or accept a future cutoff. A forward excursion can affect both inner timeline receipts and outer native storage receipts. In either layer it can prevent valid successors until verified catch-up. Quarantine and freeze the affected root, preserve restricted evidence, then use verified catch-up with current policy or an explicitly governed new identity/migration that discloses loss of continuity. No automatic repair is implemented.

The native predecessor is assumed to be trusted and already validated, including its own predecessor linkage. No-op native successor snapshots are allowed by append-only prefix semantics; the host can avoid duplicate storage facts. Global native fact uniqueness remains external.

N3's remaining direct prefix-branch case was executed independently by Codex in audit-supplement.py. It recomputes both snapshot digests and uses a correctly linked successor carrying a truncated ledger, requiring the specific History rewritten/truncated exception. The same supplement demonstrates native forward-receipt failure for current and predecessor envelopes. These three checks supplement, rather than replace or renumber, the 86 frozen behavior tests and three native installation fixtures.

</file-content>
END FILE host-integration-notes.md

## FILE audit-supplement.py
Raw SHA-256: 0e6eef9dd1cc755579fa8085ae39e29beb501f8b9efbc6910aefbff507e35f39

<file-content name="audit-supplement.py">
from pathlib import Path
import copy,datetime,hashlib,json
import temporal as t
from test_temporal import TemporalTests,NOW
x=TemporalTests();x.setUp();a,b,c=x.snapshots();checks=[]
def rejected(label,fn,message):
    try:fn()
    except t.Invalid as e:assert str(e)==message,(label,str(e));checks.append(label)
    else:raise AssertionError(label)
bad=copy.deepcopy(c);bad['value']=copy.deepcopy(a['value']);bad['provenance']['snapshotDigest']=t.digest(bad['value'])
rejected('native exact-prefix branch after digest recomputation',lambda:x.snapshot(bad,b),'History rewritten/truncated')
future=copy.deepcopy(b);future.update(recordedAt='2026-12-31T00:00:00Z',validFrom='2026-12-31T00:00:00Z')
rejected('native forward receipt as current',lambda:x.snapshot(future,a),'Invalid snapshot receipt envelope')
rejected('native forward receipt as predecessor',lambda:x.snapshot(c,future),'Invalid snapshot receipt envelope')
report={'passed':len(checks),'checks':checks,'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'codeDigest':'sha256:'+hashlib.sha256(Path(t.__file__).read_bytes()).hexdigest(),'scope':'Codex post-audit supplemental checks; not independently reviewed'}
Path('audit-supplement-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))

</file-content>
END FILE audit-supplement.py

## FILE audit-supplement-results.json
Raw SHA-256: a3c78fbcc0320d103a3a9bc7fd3f7d895545227f281d168b58ba1e4e7c90ab41

<file-content name="audit-supplement-results.json">
{
  "passed": 3,
  "checks": [
    "native exact-prefix branch after digest recomputation",
    "native forward receipt as current",
    "native forward receipt as predecessor"
  ],
  "executedAt": "2026-09-21T20:06:38.072962+00:00",
  "codeDigest": "sha256:b2897dd17ff65402733b23cd34ff9152c0c61e0af11a3df5b137d821e40b1857",
  "scope": "Codex post-audit supplemental checks; not independently reviewed"
}

</file-content>
END FILE audit-supplement-results.json

END OF COMPLETE FROZEN INPUT. No other file is part of this supplied audit.


END TRANSPORT PART 4 OF 4.