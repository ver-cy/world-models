from __future__ import annotations

import subprocess
from pathlib import Path

RUN=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models\research\enterprise\runs\em-fin-01")
dossier=(RUN/'provider-dossier.json').read_text(encoding='utf-8')
prompt=f"""You are the independent architecture reviewer for Vercy's Enterprise metamodel programme.

Review the frozen dossier for EM-FIN-01 Budget, responsibility centre and funding. Decide a precise combination of REUSE ONLY, PROFILE, and NEW MODEL.

Test whether WM-ECO-012 already covers budget identity, immutable revisions, scenarios, ceilings, funding sources, allocation/allotment, amendments, forecasts, actual references and variance. Then decide whether Vercy lacks a reusable Responsibility Centre (cost/profit/investment/revenue centre) master.

The centre must not be conflated with WM-ORG-002 organizational unit, WM-ORG-004 position, WM-ECO-016 journal-entry dimension value, a mutable ERP code, a budget line or a legal entity. Prove independent identity/lifecycle if you recommend a model. Address reorganization, mergers/splits, effective periods, manager/accountability, legal-entity/ledger/chart bindings, currency/basis, hierarchy, aliases and historical posting pins.

Test funding allocation separately: source, destination, amount/weight, allocation basis, residual rule, effective period, restrictions, authority and conservation/no-double-counting. Decide whether allocation is owned by WM-ECO-012 or requires its own aggregate.

Acceptance: two funding sources finance one project; an organizational reorganization and budget revision follow. Original budget, forecast, allocation and actuals remain reconcilable; historical expenses stay attributed to the centre effective when posted; no amount is made available twice.

If recommending a new Responsibility Centre model, provide identity, lifecycle, 12-16 fields, 10+ invariants and 4 functions. Do not assign a numeric identifier; registry allocation is separate. Use dossier evidence only and state standards as alignment, not conformance.

Return at most 1100 English words with headings:
DECISION
BUDGET REUSE BOUNDARY
RESPONSIBILITY CENTRE PROOF
FUNDING ALLOCATION CONTRACT
ACCEPTANCE WALKTHROUGH
HOLDS AND PUBLICATION RECOMMENDATION

FROZEN DOSSIER
{dossier}
"""
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,check=False,timeout=900)
out=r.stdout.strip()
if r.stderr.strip(): out+='\n\nCLI STDERR\n'+r.stderr.strip()
(RUN/'claude-study.raw.md').write_text(out+'\n',encoding='utf-8',newline='\n')
print({'returncode':r.returncode,'chars':len(out),'output':str(RUN/'claude-study.raw.md')})
raise SystemExit(r.returncode)
