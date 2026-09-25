from __future__ import annotations

import subprocess
from pathlib import Path

RUN = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models\research\enterprise\runs\em-dat-06")
dossier = (RUN / "provider-dossier.json").read_text(encoding="utf-8")
prompt = f"""You are the independent architecture reviewer for Vercy's Enterprise metamodel programme.

Review the frozen dossier for EM-DAT-06, Report definition and release instance. Decide exactly one: REUSE ONLY, PROFILE, COMPLETE RESERVED MODEL, or NEW MODEL.

The registry already reserves WM-REC-002 Report / Statement as a governed factual or analytical statement for an audience and reporting period, but it has no published specification. Determine the smallest useful boundary and whether completing this reserved model is justified.

Keep these authorities distinct:
- WM-REC-001 owns generic governed records, versions, instantiations and retention;
- WM-ACT-053 owns a processing run and resolved inputs/outputs;
- WM-ACT-044 owns the publication operation, delivery and correction propagation;
- WM-XCT-003 owns declarative disclosure/output shape policy;
- WM-MED-003 owns bibliographic publication/edition identity.

Test whether WM-REC-002 should own: reusable report-definition versions; parameter and reporting-grain contract; report issue/statement identity; reporting period, cutoff and as-of semantics; source snapshot/run references; metric and query references; disclosure-policy binding; correction/restatement lineage; artifact and publication references. Decide carefully which are owned children and which are external references.

Test the acceptance scenario: issue a report, correct an input fact, issue a successor without overwriting the first, and suppress a sensitive slice under the exact policy version. A report must remain explainable even if the dashboard later changes.

Address dashboards: decide whether a dashboard definition is a report-definition profile, a governed projection, or a distinct live-view aggregate. Do not allow arbitrary joins to bypass access/disclosure evaluation.

If completing WM-REC-002, provide minimal identity, lifecycle, 12-18 core fields, at least 10 invariants and four functions. Distinguish definition version, report issue, processing run, artifact and publication operation identities. Use only dossier evidence and label standards as alignment, not conformance.

Return at most 1100 English words with exact headings:
DECISION
BOUNDARY PROOF
MINIMAL CONTRACT
DASHBOARD DISPOSITION
ACCEPTANCE WALKTHROUGH
HOLDS AND PUBLICATION RECOMMENDATION

FROZEN DOSSIER
{dossier}
"""
completed = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, check=False, timeout=900,
)
output = completed.stdout.strip()
if completed.stderr.strip(): output += "\n\nCLI STDERR\n" + completed.stderr.strip()
(RUN / "claude-study.raw.md").write_text(output + "\n", encoding="utf-8", newline="\n")
print({"returncode": completed.returncode, "chars": len(output), "output": str(RUN / "claude-study.raw.md")})
raise SystemExit(completed.returncode)
