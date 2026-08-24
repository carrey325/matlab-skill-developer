---
name: matlab-credit-multinomial-modeling
description: Implement selected MATLAB ordinal or nominal multinomial credit-model fitting, prediction, and validation without choosing predictors, rating policy, or outcome taxonomy.
---

# Implement Credit Multinomial Models in MATLAB

## Scope

Implement, review, or repair selected ordinal or nominal `fitmnr` credit-model workflows, including categorical preparation, fitting, class/probability prediction, and validation outputs.

Do not choose credit-rating order, outcome classes, predictor set, interactions, sample policy, or model-selection criteria.

## Prerequisites

- MATLAB R2026a and Statistics and Machine Learning Toolbox.
- A selected response taxonomy, ordinal ordering when applicable, predictors, partition, `fitmnr` model type, and evaluation contract.

## Capability Contract

### Required Inputs

- An aligned table or predictor matrix with the selected response labels.
- Explicit `ModelType` and predictor/categorical-variable treatment when defaults are unsuitable.

### Conditional Inputs

- Formula, interactions, link, weights, dispersion, iteration controls, probability output, and confusion/metric reporting when selected.

### Input Validation

- Validate response cardinality, categorical order for ordinal models, predictor availability, row alignment, finite numeric predictors, and partition disjointness.
- Validate that predicted labels and posterior probabilities retain test-row order and use the model's class order.

## Critical Rules

### Intent Preservation

- Preserve the supplied nominal/ordinal distinction and class order. Do not infer credit-quality ordering from labels or model coefficients.

### Data and Unit Conventions

- Keep training, validation, test, and out-of-sample periods distinct; do not fit preprocessing or model coefficients using held-out rows.

### Execution Boundaries

- Use `$matlab-credit-model-governance` for fairness or explainability work and `$matlab-credit-scorecard-modeling` for `creditscorecard` workflows.
- Do not reinterpret class probabilities as default probabilities unless the implementation contract explicitly selects that mapping.

## Failure Handling

- Stop on undefined ordinal order, unsupported response/predictor types, nonconvergent fitting, empty classes after splitting, or an unspecified outcome/model contract.
- Report the exact `fitmnr` signature, MATLAB release, class labels, and full diagnostic before changing a call.

## Gotchas

- The `fitmnr` default is nominal; ordinal analysis must retain the explicitly supplied ordered categorical response and selected `ModelType`.

## Reference Loading

- Load [evaluation findings](references/evaluation-findings.md) only for multinomial regression repair.
- Load [verified multinomial gotchas](references/gotchas.md) before forming a table-based `fitmnr` call.
- Load [the multinomial-model function reference](references/matlab-functions.md) before fitting or predicting with a selected `fitmnr` model.
