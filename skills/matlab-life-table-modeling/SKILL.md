---
name: matlab-life-table-modeling
description: Implement selected life table calibration, generation, and conversion work in MATLAB without choosing mortality assumptions, population policy, or actuarial interpretation.
---

# Implement Life Table Modeling in MATLAB

## Scope

Implement, review, or repair `lifetablefit`, `lifetablegen`, and `lifetableconv` calls after the mortality model and life-table conventions are selected.

Do not select mortality families, population assumptions, extrapolation rules, or actuarial decisions.

## Prerequisites

- MATLAB R2026a and Financial Toolbox.
- A selected operation, survival or life-table data, and explicit age, period, and termination conventions.

## Capability Contract

### Required Inputs

- Selected life-table function plus input data in the documented representation.

### Conditional Inputs

- Parametric model, calibration, and forced-termination controls only when required by the selected call.

### Input Validation

- Validate age and period ordering, probability/rate domains, input lengths, and selected model-specific constraints.

## Critical Rules

### Intent Preservation

- Preserve chosen mortality and population conventions; do not infer assumptions from missing data.

### Data and Unit Conventions

- Keep ages, calendar periods, survival probabilities, death rates, and termination assumptions explicit.

### Execution Boundaries

- Keep insurance claims reserving in `$matlab-claims-reserving`.

## Failure Handling

- Stop on invalid age grids, nonphysical probabilities, unsupported model options, or incomplete conventions.

## Gotchas

- Fitting, generating, and forcing termination are separate stages; do not use output from one as though it implicitly sets assumptions for another.

## Reference Loading

- Load [the life-table function reference](references/matlab-functions.md) before implementing a selected operation.
