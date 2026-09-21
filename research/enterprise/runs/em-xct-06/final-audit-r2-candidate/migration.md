## Migration and minimum use

Minimum useful configuration: one subject, one receipt, one exact monetary input, one admitted currency/context and one explicit rounding policy. No ERP or HRIS is required. Three synthetic profiles exercise startup line rounding, matrix reconciliation with negative amounts and AI estimate precision; none represent real company internals. Run python test_monetary.py with Python 3.11+ and jsonschema 4.26.0. Native verification is a separate acceptance.py run with the exact tool-pins.json toolchain.

Only same-version lossless roundtrip is implemented. Unknown versions and unknown fields fail closed. Upgrade/downgrade needs an explicit future mapping, preservation of old bytes and recomputation under a new receipt ID; never edit a version label or reseal an earlier issuer's result as if it were their approval. Rollback restores the prior complete verified register and original validator, not an obsolete authorization.
