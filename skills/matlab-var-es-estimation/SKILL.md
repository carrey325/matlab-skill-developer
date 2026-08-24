---
name: matlab-var-es-estimation
description: Implement selected value-at-risk and expected-shortfall estimation calls in MATLAB without choosing the distribution, horizon, confidence level, or risk policy.
---

# Implement VaR and ES Estimation in MATLAB

## Scope

Implement, review, or repair `valueAtRisk` and `expectedShortfall` calls for a distribution and risk convention already selected by the user or upstream workflow.

Do not choose the distribution, risk horizon, confidence level, loss sign convention, or risk limit.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected returns/loss distribution, confidence level, horizon, and sign convention.

## Capability Contract

### Required Inputs

- Distribution input in the selected MATLAB representation and a valid confidence level.

### Conditional Inputs

- Tail, sample, and distribution parameters only when the selected representation requires them.

### Input Validation

- Validate probability bounds, distribution support, input dimensions, and loss/return sign convention before interpreting output.

## Critical Rules

### Intent Preservation

- Return the documented numerical measure only; do not convert it into a business limit or reverse sign without instruction.

### Data and Unit Conventions

- Keep horizon, currency/return units, and confidence level explicit.

### Execution Boundaries

- Route model-performance testing to `$matlab-var-es-backtesting`.

## Failure Handling

- Stop on invalid confidence levels, incompatible distribution inputs, unsupported data types, or unspecified sign conventions.

## Gotchas

- Estimation functions are not backtests; they do not establish forecast adequacy.

## Reference Loading

- Load [the VaR and ES estimation reference](references/matlab-functions.md) before coding the selected measure.
