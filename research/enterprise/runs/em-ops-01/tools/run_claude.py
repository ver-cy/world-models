import subprocess
from pathlib import Path

WORLD = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
DOSSIER = WORLD / "research/enterprise/runs/em-ops-01/provider-dossier.json"
OUT = WORLD / "research/enterprise/runs/em-ops-01/claude-study.raw.md"

PROMPT = """You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier; do not browse, execute code or invent identifiers. Review EM-OPS-01 Process, Procedure and Execution and decide separately how to complete the two existing reserved candidates WM-ACT-003 Process / Workflow and WM-ACT-009 Method / Procedure. Allowed decisions are REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, MERGE/RETIRE DUPLICATE, or DEFER. No new runtime/model ID is allowed unless a third aggregate has provably independent identity and lifecycle.

Test these boundaries rigorously: method versus procedure versus process definition; immutable released definition/edition versus mutable draft; process variant versus new definition version; process instance versus activity/step execution; planned BPMN/CMMN path versus observed trace; task/work-item assignment versus execution event; manual exception, deviation, compensation and conformance; adoption of a method edition by an organization; historical replay after an instruction update. Decide which aggregate owns each identity and what it only references. Assess whether ProcessInstance and ActivityExecution belong inside WM-ACT-003 or require independent model identity. Preserve the distinction between a reusable knowledge artifact and an operational flow. Treat wildcard imports, unsupported MUC claims and candidate relation rows as holds.

Walk the negative case where a revised instruction changes completed history and the acceptance case with one process, two variants, a manual exception and a new procedure edition producing separate reproducible traces. Return at most 1200 words with headings Verdict; Evidence state; Boundary and aggregate identities; Version/variant/adoption semantics; Execution and trace contract; Invariants; Scenario walkthrough; Migration path; Gaps and publication holds. Do not claim installability, compatibility, standards conformance or approved relations without evidence.

FROZEN DOSSIER
""" + DOSSIER.read_text(encoding="utf-8")

result = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=PROMPT,
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True,
    timeout=900,
)
if result.returncode:
    raise SystemExit(result.stderr)
OUT.write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(OUT)
print(OUT.stat().st_size)
