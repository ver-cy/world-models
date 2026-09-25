import subprocess
from pathlib import Path


REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
DOSSIER = REPO / "research/enterprise/runs/em-fin-03/provider-dossier.json"
OUTPUT = REPO / "research/enterprise/runs/em-fin-03/claude-study.raw.md"


def main():
    dossier = DOSSIER.read_text(encoding="utf-8")
    prompt = f"""You are an independent enterprise metamodel boundary reviewer.
Use only the frozen dossier below. Do not browse, execute code, or invent registry IDs.

Decide one disposition for EM-FIN-03: REUSE ONLY, PROFILE, or NEW MODEL. Test whether
payment allocation and reconciliation have identity/lifecycle independent from Payment,
or should remain owned semantics of WM-ECO-009. Cover partial payments, one payment across
multiple invoices, multiple payments against one invoice, overpayment, disputed residual,
cross-currency allocation and FX/rounding evidence, payment reversal, settlement finality,
and invoice cancellation versus correction/credit. Preserve the rule that reconciliation
does not prove delivery. Walk the stated negative and acceptance cases.

Return at most 1000 words with these headings: Verdict; Boundary; Required semantics;
Invariants; Scenario walkthrough; Gaps and publication holds. Clearly distinguish reuse,
profile constraints, and any truly independent new aggregate. A profile does not receive a
new catalogue/runtime ID. Treat the two source models as reviewable drafts under their
listed holds.

FROZEN DOSSIER
{dossier}
"""
    result = subprocess.run(
        ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=900,
        check=False,
    )
    if result.returncode:
        raise SystemExit(f"Claude failed ({result.returncode}):\n{result.stderr}")
    OUTPUT.write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
    print(OUTPUT)
    print(OUTPUT.stat().st_size)


if __name__ == "__main__":
    main()
