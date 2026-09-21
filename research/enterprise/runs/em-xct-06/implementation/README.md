# Enterprise Monetary Calculation

Preserve exact monetary inputs, record an explicit rounding policy and reproduce a same-currency total with every residual visible. English reviewable draft, part of the broader EM-XCT-06 research contour.

Read model-spec.md and adoption-limits.md. Run `python test_monetary.py`; native checks: `python acceptance.py --composer PATH --skill PATH --report /path/outside-package/native-results.json`. requirements.txt pins the Python validation library; tool-pins.json pins the separate Vercy installation toolchain.

Canonical catalogue: https://ver.cy/models/enterprise-monetary-calculation/. Research: https://ver.cy/enterprise/research/em-xct-06/. Examples are synthetic. This package performs no FX, quantity-price multiplication, payment, posting, legal, calendar or localization operation.

Tests never regenerate frozen examples or reports. To save a fresh unit report, use `python test_monetary.py --report /path/outside-package/unit-results.json`. Python 3.12.14 is the tested interpreter. Native binding checks genesis records only; the host owns current head and rights. Hard lifetime limit: 256 receipts per Dimension; no paging, retirement or retention implementation.
