import subprocess
from pathlib import Path
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
D=REPO/"research/enterprise/runs/em-leg-01/provider-dossier.json"; O=REPO/"research/enterprise/runs/em-leg-01/claude-study.raw.md"
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent IDs. Decide REUSE ONLY, PROFILE or NEW MODEL for EM-LEG-01 Contract, obligation and service-level agreement. Resolve ownership between WM-ECO-006 Commercial Contract and WM-XCT-029 Obligation/Commitment. Test whether ContractAmendment, FulfilmentEvidence or SLA needs a separate aggregate. Distinguish contractual SLA from operational SLO; the registry reserves WM-SFT-016 Service Level/SLO but it is only a candidate. Address party identity at signing, amendment vs novation/new contract, partial fulfilment, evidence revocation, disputed performance, breach/remedy, and preservation of signed text. Walk the negative case (internal SLO presented as contractual guarantee) and acceptance case (two amendments, partial performance, disputed SLA). Return at most 1100 words with headings Verdict; Boundary; SLA/SLO split; Required profile; Invariants; Scenario walkthrough; Gaps and publication holds. A profile gets no new ID.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode: raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8'); print(O); print(O.stat().st_size)
