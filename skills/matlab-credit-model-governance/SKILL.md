---
name: matlab-credit-model-governance
description: Implement selected MATLAB fairness, disparate-impact mitigation, and model-explainability analyses for credit models without choosing governance thresholds or policy.
---

# Implement Credit Model Governance Analyses in MATLAB

## Scope

Implement, review, or repair selected fairness measurement, fairness weighting, disparate-impact removal, partial-dependence, ICE, LIME, and Shapley analysis for an existing credit model.

Do not select sensitive attributes, reference groups, fairness thresholds, repair fractions, approval decisions, or governance policy.

## Prerequisites

- MATLAB R2026a and Statistics and Machine Learning Toolbox.
- A selected trained model or scoring function, response convention, sensitive attributes, data split, and requested governance outputs.

## Capability Contract

### Required Inputs

- Aligned observations, true binary labels where fairness metrics are requested, and selected sensitive-attribute names.
- A selected model/scoring function and compatible data when prediction-level metrics or explanations are requested.

### Conditional Inputs

- Positive class, reference group, observation weights, repair fraction, numeric predictor list, query points, categorical variables, and plot choices when specified.

### Input Validation

- Validate response/prediction alignment, binary-label type and convention, exact sensitive-attribute names, and the model's expected predictor schema.
- Fit data transformers and calculated fairness weights on training observations only; validate compatible application to held-out observations.

## Critical Rules

### Intent Preservation

- Preserve the supplied protected groups, fairness metric, model, query point, and mitigation strategy. Do not interpret a metric as a legal or approval recommendation.

### Data and Unit Conventions

- Keep labels, positive-class convention, prediction units, and score-versus-probability semantics explicit.
- Preserve supplied table and source-variable names; do not substitute guessed aliases.
- Apply a fitted `disparateImpactRemover` to new data using `transform`; do not fit it on the test set.

### Execution Boundaries

- Use `$matlab-credit-scorecard-modeling` to create, bin, fit, or validate a full `creditscorecard` object.
- Use `$matlab-credit-default-deep-learning` to construct or train a neural network before governance analysis.

## Failure Handling

- Stop on missing Statistics and Machine Learning Toolbox support, incompatible labels, empty protected groups, unavailable requested predictors, model/schema mismatch, or missing selected governance policy.
- Report the function or object, MATLAB release, and full diagnostic before proposing a correction.

## Gotchas

- Fairness metrics measure the supplied label and prediction conventions. Never invert an outcome or choose a decision threshold to make a metric look favorable.

## Reference Loading

- Load [evaluation findings](references/evaluation-findings.md) only for fairness or explainability regression repair.
- Load [verified governance gotchas](references/gotchas.md) before constructing fairness metrics from a supplied table and prediction vector.
- Load [fairness and mitigation references](references/fairness-and-mitigation.md) for metrics, weights, and disparate-impact removal.
- Load [explainability references](references/explainability.md) for partial dependence, ICE, LIME, or Shapley work.
