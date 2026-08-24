# Skill Quality and Evaluation Standards

## Choose Capability Granularity

- Prefer a coherent professional task with a stable input-output contract.
- Split subproblems with materially different triggers, inputs, method-selection logic, acceptance criteria, or implementation dependencies.
- Keep closely shared work together when separation would primarily duplicate context or create routing overhead.
- Treat the initial boundary as a hypothesis. Use representative and adjacent examples to decide whether to split, merge, or rename skills during iteration.
- Keep granularity analysis in development artifacts unless users need it to operate the final skill.

## Define the Abstraction Boundary

Treat a capability as a domain workflow plus optional language implementations.

- The workflow decides why, when, and what method applies, plus which controls and acceptance criteria are professionally relevant.
- A language implementation decides only how to express the selected work correctly in that language and runtime.
- Do not use `api` as the implementation-layer name. Use `matlab-<capability>`, `python-<capability>`, or `r-<capability>`.
- Do not duplicate domain rules in implementation skills or language mechanics in workflow skills.

## Design Selection Metadata

- Use lowercase hyphen-case names of at most 64 characters.
- Name workflow skills `<capability>-workflow` and MATLAB skills `matlab-<capability>`.
- Keep workflow descriptions discriminating and include the capability's main positive and negative boundary.
- Put detailed `When to Use` and `When Not to Use` sections in the workflow body.
- Keep MATLAB descriptions simple: explicit/default MATLAB programming or a MATLAB brief produced by the workflow. State that method selection belongs elsewhere.
- Test true-positive and false-positive selection for both layers.

## Use Contracts Selectively

Use structured contracts only where ambiguity would change execution, safety, units, or reproducibility. Do not turn every instruction into a schema.

- Workflow contracts should capture material decisions, conventions, professionally relevant controls, and the implementation brief.
- MATLAB contracts should capture required inputs, conditional inputs, types, shapes, units, and validation.
- Ordinary explanatory context can remain concise prose.

## Establish Feedback Loops Without Duplication

- Put domain failure gates inside the workflow stage that owns the decision.
- Use readiness, implementation selection, construction/configuration, execution, and verification as development concerns, not required final headings. Let the visible sequence follow professional practice.
- Put MATLAB product, signature, type, shape, solver, and runtime failures in the MATLAB skill.
- Do not repeat the same failure policy in both a workflow stage and a generic failure section.
- Do not claim success after a failed verification gate.

## Develop From Evidence

1. Establish realistic selection and behavior baselines when feasible.
2. Classify defects as capability-granularity, workflow selection/reasoning, implementation-brief, language knowledge, execution, or output defects.
3. Add the smallest rule to the layer that owns the defect.
4. Prefer official product documentation for language behavior and authoritative domain sources for professional methods.
5. Distinguish executed, inspected, inherited, inferred, and unverified evidence.

## Review Maintainability

- Keep `SKILL.md` below 500 lines and use direct one-level references.
- Add a contents section to references longer than 100 lines when useful.
- Use POSIX-style relative paths inside portable skills.
- Scope volatile behavior by release or effective date.
- Remove unused resources and repeated rules.
- Audit that a direct MATLAB coding request does not load domain workflow content unnecessarily.

## Reject Common Anti-Patterns

- Fixed paired-suite assumptions.
- A mandatory five-stage visible workflow regardless of the capability's natural sequence.
- Universal controls, reconciliations, governance, acceptance, or reporting sections without professional relevance.
- `matlab-<capability>-api` names.
- Method selection or detailed professional triggers in MATLAB skills.
- MATLAB signatures, code blocks, or runtime gotchas in workflow skills.
- Generic `Task-to-Function Routing` that mixes method classification with function documentation.
- Procedural prompts disguised as prerequisites.
- Repeated failure logic across layers.
- Universal finance thresholds without mandate or evidence.
