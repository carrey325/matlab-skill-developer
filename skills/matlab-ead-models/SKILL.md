---
name: matlab-ead-models
description: Implement selected exposure-at-default model fitting, prediction, calibration, and discrimination work in MATLAB without choosing the exposure-model methodology or policy.
---

# Implement EAD Models in MATLAB

## Scope

Implement, review, or repair selected EAD model objects, `fitEADModel`, prediction, calibration, and discrimination code.

Do not select the EAD family, credit-conversion assumptions, exposure horizon, scenario policy, or credit decision rules.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected EAD model method, training/prediction data contract, and exposure convention.

## Capability Contract

### Required Inputs

- Selected model/function, compatible EAD observations, predictors, and requested output.

### Conditional Inputs

- Beta, Regression, Tobit, calibration, or discrimination controls when required by the selected call.

### Input Validation

- Validate EAD domains, observation/predictor alignment, target type, and model-specific assumptions.

## Critical Rules

### Intent Preservation

- Preserve the supplied exposure definition and selected model type; do not rescale or infer exposure conventions.

### Data and Unit Conventions

- Keep currencies, exposure units, time horizons, conditioning data, and grouping explicit.

### Execution Boundaries

- Use `$matlab-lifetime-ecl` for ECL aggregation and the PD/LGD skills for other ECL components.

## Failure Handling

- Stop on invalid exposure domains, target/predictor mismatch, unsupported model options, or missing selected assumptions.

## Gotchas

- Same-named calibration and discrimination methods are model-object methods; dispatch using the selected EAD class.

## Reference Loading

- Load [the EAD function reference](references/matlab-functions.md) before constructing or evaluating the selected model.
