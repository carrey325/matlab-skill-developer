# Target Skill Structure Index

Use only headings that materially help the target capability. These patterns are development aids, not mandatory final outlines. The two skill types have different abstraction boundaries and must not be merged into one generic structure.

Determine the capability boundary and number of skills before choosing an outline. Keep granularity reasoning in development notes unless it materially helps users operate the final skill.

## Capability Family

```text
<capability>-workflow/       # domain reasoning and implementation selection
matlab-<capability>/         # MATLAB implementation
python-<capability>/         # optional future peer
r-<capability>/              # optional future peer
```

This is not a paired suite. A workflow can exist before any language implementation, and several language implementations can consume the same workflow brief.

## Template 1: Workflow Skill

Folder: `<capability>-workflow/`

- `SKILL.md`
- `agents/openai.yaml`
- `references/` only for substantial domain controls, methods, conventions, or reporting guidance
- `scripts/` only for fragile language-neutral deterministic checks
- `assets/` only for user-facing templates copied into deliverables
- `evals/` when supported

Possible `SKILL.md` structure:

```markdown
# Execute <Capability> Workflow

## When to Use
## When Not to Use

## Inputs and Conventions

## Implementation Selection
### Method-to-Object Map
### Operation-to-Function Map

## Workflow
### <Natural Professional Stage>
### <Next Natural Professional Stage>

## Output and Implementation Brief
## Reference Loading
```

During development, use these five concerns as a completeness checklist:

1. readiness and preflight;
2. implementation selection;
3. construction and configuration;
4. execution;
5. verification.

They do not prescribe the visible headings, ordering, or number of stages. Combine, rename, reorder, or omit visible stages when the capability's professional practice supports a clearer sequence, while ensuring no material concern is accidentally lost.

Workflow rules:

- Put domain purpose, method choice, benchmark selection, constraints, conventions, and interpretation here. Include controls, reconciliations, governance, acceptance, and reporting only when professionally relevant to the capability.
- Put detailed positive and negative triggers here as well as a concise discovery description in frontmatter.
- Make failure gates local to the workflow stage that owns the decision; do not duplicate a generic failure section unless it adds non-overlapping behavior.
- The implementation brief must state selected language, object/model, operations, ordered inputs, parameters, conventions, outputs, and verification criteria.
- Function names may appear in implementation-selection maps, but signatures, code patterns, shapes, runtime diagnostics, and gotchas belong to the language implementation.

## Template 2: MATLAB Implementation Skill

Folder: `matlab-<capability>/`

- `SKILL.md`
- `agents/openai.yaml`
- `references/` for function-by-function MATLAB documentation and evidence
- `scripts/` only for repeated fragile MATLAB mechanics
- `assets/` only when copied into generated MATLAB deliverables
- `evals/` when supported

Possible `SKILL.md` structure:

```markdown
# Implement <Capability> in MATLAB

## Scope

## Prerequisites

## Capability Contract
### Required Inputs
### Conditional Inputs
### Input Validation

## Critical Rules
### Intent Preservation
### Data and Unit Conventions
### Execution Boundaries

## Failure Handling
## Gotchas
## Reference Loading
```

MATLAB rules:

- `Scope` says only that the skill writes, reviews, or repairs MATLAB code for an already selected implementation.
- `Prerequisites` answers one question: what environment, products, and information are required to run this skill? Do not put procedural prompts there.
- Do not include `When to Use`, `When Not to Use`, `Implementation Selection`, method classifications, professional workflow, interpretation, governance, or reporting.
- Do not add `Task-to-Function Routing`. Organize references by MATLAB object/function and give exact signatures, inputs, outputs, patterns, and evidence for each.
- `Failure Handling` covers coding, product, signature, type, shape, solver/runtime, and execution failures only. Domain failures remain in the workflow stage that owns them.
- Keep the MATLAB trigger concise: explicit/default MATLAB programming, or a workflow-generated MATLAB implementation brief.

## Reference Files

Workflow references may contain:

- domain methods and selection criteria;
- professional conventions and relevant controls;
- stage gates and reconciliations when the capability needs them;
- reporting and approval requirements when professionally relevant.

MATLAB references may contain:

- object/function name and availability;
- exact signatures, options, input types, output shapes, and defaults;
- minimal coding patterns;
- runtime diagnostics and verified gotchas;
- official evidence record and release scope.

Do not place the same rule in both layers. The workflow selects and specifies; the MATLAB skill implements and preserves.

## Supporting Files

- `evals/evals.json`: skill, version, cases, context, and assertions.
- `agents/openai.yaml`: display name, short description, and default prompt.
- `manifest.yaml`: optional packaging metadata only.
