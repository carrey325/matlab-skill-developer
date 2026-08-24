---
name: matlab-credit-scorecard-modeling
description: Implement selected credit scorecard screening, binning, fitting, scoring, and validation work in MATLAB; do not choose the credit policy or modeling method.
---

# Implement Credit Scorecard Modeling in MATLAB

## Scope

Implement, review, or repair MATLAB for an already selected consumer-credit scorecard implementation. Cover predictor screening, the Binning Explorer interface, and the full Financial Toolbox `creditscorecard` lifecycle.

Do not select scorecard policy, approval thresholds, rejection-inference policy, fairness policy, or the business definition of good and bad observations.

## Prerequisites

- MATLAB R2026a baseline.
- Financial Toolbox for `creditscorecard` and its methods; Risk Management Toolbox for `screenpredictors` and Binning Explorer.
- A selected implementation brief identifying the response, good label, predictor set, data table, desired binning/fitting operation, and expected output.

## Capability Contract

### Required Inputs

- A nonempty MATLAB table with the selected response and implementation-specific columns.
- Explicit names for any identifier, response, predictor, and weight columns whose defaults are unsuitable.

### Conditional Inputs

- Binning, missing-data, coefficient-constraint, score-scaling, and validation settings only when the selected operation needs them.

### Input Validation

- Validate table variable names, response cardinality, predictor eligibility, weight validity, and compatibility between the selected object state and method.
- Preserve supplied labels and units; do not infer a business label or threshold from frequencies.

## Critical Rules

### Intent Preservation

- Use only the selected object and operation. Ask for a completed implementation brief when the request requires modeling-method selection.
- Treat parameters recorded for another evaluation scenario as evidence, never as defaults. Do not transfer its binning algorithm or thresholds unless the current request selects them.

### Data and Unit Conventions

- Keep variable names case-sensitive, retain row alignment, and preserve the supplied good-label, response, and observation-weight conventions.

### Execution Boundaries

- Do not convert a scorecard to the compact deployment object here; load `$matlab-compact-credit-scorecard` for that task.
- Do not claim model approval or production suitability from MATLAB output alone.

## Failure Handling

- Stop on unavailable toolboxes, unsupported input types, absent variables, nonbinary response data, invalid weights, or an operation that requires an unfitted/binned state not supplied by the brief.
- Report the function, object state, MATLAB release, and full diagnostic before proposing a code correction.

## Gotchas

- The second output of `score` is already a points table; preserve it as a table when joining identifiers or exporting results.

## Reference Loading

- Load [evaluation findings](references/evaluation-findings.md) only for scorecard regression repair.
- Load [verified scorecard gotchas](references/gotchas.md) before binning, fitting, scaling, scoring, or exporting a scorecard result.
- Load [the function reference](references/matlab-functions.md) before constructing or changing a scorecard call.
- Load [the Binning Explorer reference](references/binning-explorer.md) only for the app or Live Editor interface.
