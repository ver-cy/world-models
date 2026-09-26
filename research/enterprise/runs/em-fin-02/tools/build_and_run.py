import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-fin-02"
IDS = {"WM-ECO-015", "WM-ECO-016", "WM-ECO-017", "WM-ECO-009", "WM-ECO-008", "WM-XCT-014"}


def read_json(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def full_spec(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}
def text_doc(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}

registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-FIN-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-FIN-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-ECO-015": full_spec(W / "publications/wm-eco-015-financial-account/spec.yaml"),
        "WM-ECO-016": full_spec(W / "publications/wm-eco-016-financial-transaction-journal-entry/spec.yaml"),
        "WM-ECO-017_adjacent": full_spec(W / "publications/wm-eco-017-financial-position-balance/spec.yaml"),
        "WM-ECO-009_adjacent": full_spec(W / "publications/wm-eco-009-payment/spec.yaml"),
        "WM-ECO-008_adjacent": full_spec(W / "publications/wm-eco-008-invoice-commercial-document/spec.yaml"),
    },
    "prior_research": {
        "EM-FIN-01": text_doc(W / "research/enterprise/runs/em-fin-01/local-evidence.md"),
        "EM-FIN-03": text_doc(W / "research/enterprise/runs/em-fin-03/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-FIN-02 Account, Posting and Financial Transaction across reserved WM-ECO-015 Financial Account and WM-ECO-016 Financial Transaction / Journal Entry. Place FinancialAccount, LedgerAccount, JournalEntry, Posting and FinancialTransaction. Resolve the contradiction that WM-ECO-015 describes institution/ledger-operator accounts while excluding chart-of-accounts governance, yet WM-ECO-016 says WM-ECO-015 owns chart-of-accounts records. Separate bank/custody/payment accounts from general-ledger accounts and from time-bound positions/balances. Define how one economic event maps to multiple journal entries in different ledgers without cross-ledger balancing, and how closed-period correction preserves the original entry. Test one business event recognized in statutory and management ledgers with different rules/currencies, followed by a correction after hard close. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Account boundaries; Economic event/transaction/journal/posting; Multi-ledger mapping; Currency and balancing; Correction and period close; Lifecycle; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
