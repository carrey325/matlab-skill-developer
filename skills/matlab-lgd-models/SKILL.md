---
name: matlab-lgd-models
description: Implement selected loss-given-default model fitting, prediction, calibration, and discrimination work in MATLAB without choosing the loss-model methodology or policy.
---

# Implement LGD Models in MATLAB

## Scope

Implement, review, or repair selected LGD model objects, `fitLGDModel`, `fryeJacobsLGD`, prediction, calibration, and discrimination code.

Do not select the LGD family, explanatory variables, downturn/scenario policy, or loss interpretation.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected LGD model method, training/prediction data contract, and loss-data convention.

## Capability Contract

### Required Inputs

- Selected model/function, compatible LGD observations, predictors, and requested output.

### Conditional Inputs

- Beta, Regression, Tobit, Frye-Jacobs, calibration, or discrimination controls when required by the selected call.

### Input Validation

- Validate LGD domain, observation/predictor alignment, target type, and model-specific assumptions.

## Critical Rules

### Intent Preservation

- Preserve the supplied loss definition and selected model type; do not cap, transform, or reinterpret losses without instruction.

### Data and Unit Conventions

- Keep fractional/percentage loss units, exposure basis, conditioning data, and grouping explicit.

### Execution Boundaries

- Use `$matlab-lifetime-ecl` for ECL aggregation and `$matlab-lifetime-pd-models` or `$matlab-ead-models` for those components.

## Failure Handling

- Stop on invalid loss domains, target/predictor mismatch, unsupported model options, or missing selected assumptions.

## Gotchas

- Same-named calibration and discrimination methods are model-object methods; dispatch using the selected LGD class.

## Reference Loading

- Before table grouping, LGD model construction, or model-comparison data preparation, load [verified LGD gotchas](references/gotchas.md).
- Load [the LGD function reference](references/matlab-functions.md) before constructing or evaluating the selected model.
