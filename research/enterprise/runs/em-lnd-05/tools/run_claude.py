import subprocess
from pathlib import Path
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
D=REPO/"research/enterprise/runs/em-lnd-05/provider-dossier.json"; O=REPO/"research/enterprise/runs/em-lnd-05/claude-study.raw.md"
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent IDs. Decide REUSE ONLY, PROFILE or NEW MODEL for EM-LND-05 Project/Program/Portfolio Landscape. Test whether DeliveryLandscape or DeliveryScope has independent identity/lifecycle, or is a view/membership assertion over WM-ACT-029 and WM-ACT-005. Define M:N participation of one project in multiple management views, projects to products and teams, shared resource conflicts, cost single-source rules and benefit attribution/allocation that prevents double counting. A tracker container is not a project. Walk the duplicate-budget negative case and one-project/two-products/four-teams acceptance case. Address authoritative vs scenario/as-of views. Return at most 1100 words with headings Verdict; Boundary; Membership/allocation semantics; Required profile; Invariants; Scenario walkthrough; Gaps and publication holds. A profile gets no new ID.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode: raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8'); print(O); print(O.stat().st_size)
