# Enterprise Monetary Calculation

Preserve exact monetary inputs, record an explicit rounding policy and reproduce a same-currency total with every residual visible. English reviewable draft, part of the broader EM-XCT-06 research contour.

Read model-spec.md and adoption-limits.md. Run `python test_monetary.py`; native checks: `python acceptance.py --composer PATH --skill PATH --report acceptance-results.json`. requirements.txt pins the Python validation library; tool-pins.json pins the separate Vercy installation toolchain.

Canonical catalogue: https://ver.cy/models/enterprise-monetary-calculation/. Research: https://ver.cy/enterprise/research/em-xct-06/. Examples are synthetic. This package performs no FX, quantity-price multiplication, payment, posting, legal, calendar or localization operation.
