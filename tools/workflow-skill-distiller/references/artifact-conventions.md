# Artifact Conventions

All structured artifacts use UTF-8 YAML or JSON and `schema_version: "1.0.0"`. Keep paths relative to the workflow workspace. IDs are stable after first publication; revise content through versioned artifacts rather than silently reusing an ID.

Stage boundaries are strict: extraction writes atoms and conflicts, synthesis writes models and the Workflow IR, generation writes only the skill package, review writes verdicts, and alignment writes provider bindings. No role may skip an earlier validation gate.

Use source IDs in evidence records and knowledge-atom IDs in Workflow IR claims. A high authority tier does not override a more applicable rule from another regime.
