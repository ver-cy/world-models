import subprocess
from pathlib import Path
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
D=REPO/"research/enterprise/runs/em-lnd-01/provider-dossier.json"; O=REPO/"research/enterprise/runs/em-lnd-01/claude-study.raw.md"
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent IDs. Decide REUSE ONLY, PROFILE or NEW MODEL for EM-LND-01 Organizational Structure Landscape. Test whether OrganizationLandscape, StructureAxis or StructureSnapshot has independent identity/lifecycle, or whether the landscape is a deterministic query/projection over WM-ORG-002 units, WM-ORG-003 teams, WM-ORG-004 positions and WM-ORG-016 assignments. Define separate administrative, functional, project and supervisory axes; axis-specific cardinality/cycle rules; bitemporal as-of reconstruction; future reorganization; scenario vs authoritative facts. Ensure Person and Unit are referenced, not copied. Walk matrix-assignment negative case and three-axis/future-reorganization acceptance case. Return at most 1100 words with headings Verdict; Boundary; Axis and snapshot semantics; Required profile; Invariants; Scenario walkthrough; Gaps and publication holds. A profile gets no new ID.

FROZEN DOSSIER
"""+D.read_text(encoding='utf-8')
r=subprocess.run(['claude','-p','--model','opus','--effort','high','--tools',''],input=prompt,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=900)
if r.returncode: raise SystemExit(r.stderr)
O.write_text(r.stdout.rstrip()+'\n',encoding='utf-8'); print(O); print(O.stat().st_size)
