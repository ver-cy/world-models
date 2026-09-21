**ACCEPT WITH LIMITS.** No concrete release blocker in this file.

B4 is fixed in source. There is no global `str.replace`. After `create_dimension` writes into `temp`, the adapter checks `dimension['id']==namespace` and `canonical.location==str(temp)`, then writes **only** `canonical.location` to `str(target)`. It then requires **exactly one** AGENTS.md line `- Canonical location: <temp>` and replaces that line. A different template shape fails closed (`BOOTSTRAP`).

Namespace is bound three times: `namespace==plan['dimensionId']` before create, `--namespace` on the trusted skill, and `dimension['id']==namespace` after create. Empty starting lock and `not target.exists()` keep the path NEW-ONLY.

Lease matches `stage()`: sibling `.{name}.composition-write.lock`, `owner.json` inside the try, `BUSY` on collision. Work stays in a prefix-checked temp dir. V3 runs on `temp` via trusted `vercy.py validate`; policy and lock bytes are re-read; the plan is re-validated; target is required still absent; then `os.rename`. `finally` deletes only an uncommitted prefix-matched temp and always drops the lease.

Prior “bootstrap not reviewed” is withdrawn for this file.

Limits that remain (not defects against the bounded claim):

- Trust is the caller-supplied skill. `c.load` is `json.loads`; the adapter assumes JSON-compatible `dimension.yaml` and that exact AGENTS line. Codex native acceptance already passed against that skill; this review did not re-run it.
- Other template files are not scanned for leftover `temp` paths. That is the two-field design.
- `--preset commercial-company` is hardcoded and documented.
- Native V3 here is envelope/registry structure. Companion / nested semantics stay outside the composer.

Do not raise research assurance. Reviewable-draft; NEW commercial-company Dimensions only.
