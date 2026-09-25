import subprocess
from pathlib import Path


REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
DOSSIER = REPO / "research/enterprise/runs/em-knw-01/provider-dossier.json"
OUTPUT = REPO / "research/enterprise/runs/em-knw-01/claude-study.raw.md"


def main():
    prompt = """You are an independent enterprise metamodel boundary reviewer. Use only the frozen dossier below. Do not browse, execute code, or invent IDs.

Decide REUSE ONLY, PROFILE, or NEW MODEL for EM-KNW-01 Document, knowledge and terminology. Test the boundaries among Document/Record, Document Revision, file/URL/carrier, Knowledge Article, Concept, Term/Designation and Taxonomy/Classification Scheme. In particular resolve the apparent overlap: WM-KNW-006 says the concept owns scheme membership/relations/governance, while WM-KNW-018 says the scheme aggregate owns concepts, labels, relations, mappings and releases. Recommend an ownership rule that avoids dual masters and preserves standalone concept identity when appropriate.

Walk the negative case (new URL becomes new knowledge and same labels merge) and acceptance case (move a document between systems, retain revisions, and preserve conflicting definitions of one word in distinct contexts). Address identity, immutable versions/releases, provenance, content digest versus record identity, language/context, same-as versus lexical equality, deprecation/dispute and cross-system migration. Return at most 1100 words with headings: Verdict; Aggregate boundaries; Ownership reconciliation; Required profile; Invariants; Scenario walkthrough; Gaps and publication holds. A profile gets no new model ID.

FROZEN DOSSIER
""" + DOSSIER.read_text(encoding="utf-8")
    result = subprocess.run(
        ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
        input=prompt, text=True, encoding="utf-8", errors="replace",
        capture_output=True, timeout=900, check=False,
    )
    if result.returncode:
        raise SystemExit(f"Claude failed ({result.returncode}):\n{result.stderr}")
    OUTPUT.write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
    print(OUTPUT)
    print(OUTPUT.stat().st_size)


if __name__ == "__main__":
    main()
