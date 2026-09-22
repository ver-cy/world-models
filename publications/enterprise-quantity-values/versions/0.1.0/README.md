# Enterprise Quantity Values 0.1.0

An embedded scalar value profile for existing company objects. Start with AGENTS.md and model-spec.md. The specification includes 4 bundles, 8 layers and 20 concrete question routes. Every example is synthetic.

Run `python test_quantity.py --report /temporary/test-results.json`. For native acceptance run `python acceptance.py --composer /pinned/composer --skill /pinned/vercy-skill --report /temporary/native-results.json`. Keep generated reports outside immutable installed or downloaded release files. See tool-pins.json for exact toolchain bytes. Python 3.12.14 and jsonschema 4.26.0 were tested.
