import subprocess
from pathlib import Path
REPO=Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
DOSSIER=REPO/"research/enterprise/runs/em-knw-02/provider-dossier.json"
OUT=REPO/"research/enterprise/runs/em-knw-02/claude-study.raw.md"
prompt="""You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent IDs. Decide REUSE ONLY, PROFILE or NEW MODEL for EM-KNW-02. Resolve the major overlap between WM-KNW-010 Decision/Rationale and WM-REC-010 Decision/Approval Record: should both persist, and if so which facts each masters without dual truth? Test Claim identity/state, reified Evidence/Citation (which is a relationship, not evidence truth), Argument structure, alternatives and decision lifecycle. Distinguish observation/source material, citation stance, claim assessment and decision choice. Test evidence later contested/retracted while two decisions cite it: trace impact without rewriting claims, citations, rationale or decisions. Preserve rejected alternatives and dissent. Return at most 1100 words with headings Verdict; Boundary and ownership; Required profile; Invariants; Scenario walkthrough; Gaps and publication holds. A profile gets no new ID.

FROZEN DOSSIER
"""+DOSSIER.read_text(encoding="utf-8")
r=subprocess.run(["claude","-p","--model","opus","--effort","high","--tools",""],input=prompt,text=True,encoding="utf-8",errors="replace",capture_output=True,timeout=900)
if r.returncode: raise SystemExit(r.stderr)
OUT.write_text(r.stdout.rstrip()+"\n",encoding="utf-8"); print(OUT); print(OUT.stat().st_size)
