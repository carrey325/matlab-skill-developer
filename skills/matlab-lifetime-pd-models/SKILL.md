---
name: matlab-lifetime-pd-models
description: Implement selected lifetime probability-of-default model construction, prediction, calibration, and discrimination work in MATLAB without choosing the credit modeling methodology.
---

# Implement Lifetime PD Models in MATLAB

## Scope

Implement, review, or repair selected lifetime PD models (`Logistic`, `Probit`, `Cox`, or custom), fitting, prediction, calibration, discrimination, and residual handling.

Do not select the PD model family, covariates, stress scenario, horizon policy, or credit decision criteria.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected PD model type, training/prediction data contract, response/event convention, and horizon definition.

## Capability Contract

### Required Inputs

- The selected model object/function and compatible training or prediction data.

### Conditional Inputs

- Censoring, survival, grouping, calibration, discrimination, and residual controls when required by the selected model.

### Input Validation

- Validate event encoding, time horizon, predictor compatibility, grouping alignment, and model-specific data requirements.

## Critical Rules

### Intent Preservation

- Preserve the chosen model family and event convention. Do not change conditional, cumulative, marginal, or survival interpretation.

### Data and Unit Conventions

- Express table variable lists as string arrays or cell arrays of character vectors; never use a cell array of string scalars.
- Pass the selected years-on-books variable as `AgeVar`; keep it out of `LoanVars` so lifetime-PD age semantics remain explicit.
- Keep PD units, time horizons, observation dates, and group definitions explicit.

### Execution Boundaries

- Use `$matlab-lifetime-ecl` for ECL aggregation and the dedicated LGD/EAD skills for those models.

## Failure Handling

- Stop on inconsistent event/time data, model/data mismatch, invalid probabilities, unavailable toolbox support, or unselected modeling assumptions.

## Gotchas

- `predict` and `predictLifetime` have distinct result semantics; choose from the requested PD horizon rather than a method name alone.
- Validate staged macro inputs at the stage where they become model inputs; historical keyed data and scenario-shock tables can have different selected schemas.
- Use lifetime-PD role arguments and restore ID-contiguous ordering after table joins or concatenation.

## Reference Loading

- Load [evaluation findings](references/evaluation-findings.md) only when regression-testing or repairing generated lifetime-PD implementations.
- Load [verified lifetime-PD gotchas](references/gotchas.md) before constructing a panel with macro predictors or changing PD model inputs.
- Load [the lifetime PD function reference](references/matlab-functions.md) by model class before coding.
