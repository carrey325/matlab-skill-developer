---
name: matlab-compact-credit-scorecard
description: Implement selected compact credit scorecard conversion, scoring, probability-of-default, and validation work in MATLAB without choosing credit-model policy.
---

# Implement Compact Credit Scorecards in MATLAB

## Scope

Implement, review, or repair conversion of a fitted `creditscorecard` to `compactCreditScorecard`, and code that displays points, scores data, calculates PD, or validates that compact object.

Do not choose scorecard construction, binning, fitting, or deployment policy.

## Prerequisites

- MATLAB R2026a baseline and Risk Management Toolbox.
- Financial Toolbox when the task converts a full `creditscorecard` object.
- A selected operation and either a compact object or a full scorecard whose fitted/binned status is explicit.

## Capability Contract

### Required Inputs

- A selected `compactCreditScorecard` operation, or a fitted full scorecard for `compact` conversion.
- A scoring or validation table with required predictor names and compatible data types when scoring, PD, or validation is requested.

### Conditional Inputs

- Point-display options, scaling already established on the full scorecard, and validation inputs when the selected method requires them.

### Input Validation

- Verify the full scorecard was binned and fitted before conversion, and verify compact predictor names against the supplied data before scoring.

## Critical Rules

### Intent Preservation

- Preserve the source scorecard's fitted coefficients, bin definitions, labels, and score scaling. Do not refit or alter them here.

### Data and Unit Conventions

- Preserve predictor types and names exactly; distinguish score output from probability-of-default output.

### Execution Boundaries

- Route full scorecard construction, variable screening, binning, and fitting to `$matlab-credit-scorecard-modeling`.

## Failure Handling

- Stop on missing Risk Management Toolbox, an unfitted source scorecard, unmatched predictors, invalid scoring data, or attempts to change model policy through the compact object.

## Gotchas

- `compact` is a conversion operation with full-scorecard prerequisites; a compact object is not a substitute for refitting a model.

## Reference Loading

- Load [the compact scorecard function reference](references/matlab-functions.md) before coding or repairing an operation.
