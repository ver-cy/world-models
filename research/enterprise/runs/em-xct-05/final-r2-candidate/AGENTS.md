# Agent use

Read model-spec.md, spec.json and disclosure.schema.json. Identify the proposal, its exact source members and all bound context. Ask for missing facts by question ID; unknown is not permission. Seal and import only with host-approved write authority. Request a review from an authorized reviewer; preserve rejection/inconclusive/conflict rather than rewriting them.

Use load() on wire bytes, validate() on each record, import_records() on the complete bounded register, validate_native() plus native envelope validation for stored facts, and inspect() only under an independently constructed trusted current snapshot. These operations do not fetch source data or contact people. Capability dictionaries are host assertions, never user-supplied credentials. Current access permission is required even for historical data.

Return restricted diagnostics only to authorized internal consumers. Never forward them verbatim to recipients. Never infer serving rights, classification comparability, anonymity, source truth, successful delivery or destruction from hashes or review status. A documented proposed action in the question tree does not authorize its execution. Follow the organization's actual access, records and custody decisions.
