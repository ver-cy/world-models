from __future__ import annotations

import json
from pathlib import Path

REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
RUN = REPO / "research" / "enterprise" / "runs" / "em-fin-01"
RUN.mkdir(parents=True, exist_ok=True)
MODELS = {
    "WM-ECO-012": "wm-eco-012-budget",
    "WM-ORG-002": "wm-org-002-organizational-unit",
    "WM-ORG-004": "wm-org-004-position",
    "WM-ECO-016": "wm-eco-016-financial-transaction-journal-entry",
    "WM-XCT-032": "wm-xct-032-currency-monetary-value",
}
SELECTED = {
    "WM-ECO-012": {"budget-identity-purpose-and-owner","planning-horizon-financial-period-and-calendar","cash-accrual-commitment-statistical-basis-and-currency","financing-grant-transfer-borrowing-and-funding-source","economic-functional-programme-and-organizational-classification","budget-line-item-quantity-unit-cost-and-dimensions","baseline-economic-operational-assumptions-and-scenario","authorization-appropriation-conditions-and-effective-version","ceiling-envelope-allocation-allotment-and-availability","funding-source-earmark-restriction-and-release","actual-ledger-invoice-payment-and-cash-reference","transfer-reallocation-supplementary-budget-and-amendment","plan-forecast-commitment-actual-and-cash-variance"},
    "WM-ORG-002": set(), "WM-ORG-004": set(), "WM-ECO-016": set(), "WM-XCT-032": set(),
}


def load(slug: str) -> dict:
    t=(REPO/'publications'/slug/'spec.yaml').read_text(encoding='utf-8'); return json.loads(t[t.index('{'):])


def compact(mid: str, slug: str) -> dict:
    d=load(slug); findings=[]
    for b in d.get('structure',{}).get('bundles',[]):
        for l in b.get('layers',[]):
            for f in l.get('findings',[]):
                s=(f.get('id','')+' '+f.get('name','')+' '+f.get('description','')).lower()
                if f.get('id') in SELECTED[mid] or (mid!='WM-ECO-012' and any(k in s for k in ('cost centre','cost center','currency','monetary','actual','journal','organizational unit','unit placement'))):
                    if len(findings)<10:
                        findings.append({'id':f.get('id'),'name':f.get('name'),'description':f.get('description'),'dataElements':[{k:e.get(k) for k in ('id','name','description','value_kind','cardinality','required') if e.get(k) is not None} for e in f.get('data_elements',[])]})
    a=d.get('researchAdjudication') or {}
    return {'publication':d.get('publication'),'metaModel':d.get('metaModel'),'model':d.get('model'),'selectedFindings':findings,'functions':[{k:x.get(k) for k in ('id','name','description')} for x in d.get('functions',[])],'publicationHolds':a.get('publicationHolds') or []}


dossier={
 'contour':{
  'id':'EM-FIN-01','name':'Budget, responsibility centre and funding',
  'scope':'Versioned resource plan, scenarios, ceilings, allocations, funding sources and independent financial responsibility centres. Organizational structure and financial responsibility structure may differ.',
  'questions':['How are original budget, forecast, commitment and actual reconciled without conflation?','How is double counting prevented when multiple sources fund one project?','How does a cost/responsibility centre survive organizational reorganization?'],
  'invariants':['Period, currency and accounting/recognition basis are explicit.','A plan or forecast revision never mutates actual transactions.','Every allocation has source, destination, basis, amount/weight and residual rule.','Historical postings retain the responsibility-centre version effective at posting time.'],
  'acceptanceScenario':'Two sources fund one project; then an organizational reorganization and budget revision occur. Original plan, forecast, allocations and actuals remain reconcilable without double counting or rewriting historical centre attribution.',
  'negativeCase':'Moving a department rewrites past expenditure under a new centre or makes the same funding amount available twice.',
  'decision':'Choose REUSE ONLY, PROFILE, or NEW MODEL. Determine whether WM-ECO-012 already owns scenarios and funding allocations, and whether a missing cross-domain Responsibility Centre master has independent identity/lifecycle. Do not turn organizational units or journal postings into that master.'
 },
 'catalogueSearchFinding':'No dedicated Cost Centre / Responsibility Centre model or reserved registry entry was found. Multiple published models consume cost-centre codes, and WM-ORG-002 states finance is authoritative for cost centres while organizational-unit identifiers and ERP cost-centre codes are not the same identity.',
 'models':{mid:compact(mid,slug) for mid,slug in MODELS.items()}
}
out=RUN/'provider-dossier.json'; out.write_text(json.dumps(dossier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n'); print(json.dumps({'output':str(out),'bytes':out.stat().st_size}))
