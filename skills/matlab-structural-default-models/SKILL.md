---
name: matlab-structural-default-models
description: Implement selected Merton structural default-probability calculations in MATLAB; do not choose the structural-model assumptions or credit decision policy.
---

# Implement Structural Default Models in MATLAB

## Scope

Implement, review, or repair `mertonmodel` and `mertonByTimeSeries` code after the structural default-probability method and input conventions are selected.

Do not choose the debt horizon, equity/asset assumptions, calibration policy, or default-use decision.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected Merton calculation form and explicit market/debt input conventions.

## Capability Contract

### Required Inputs

- Explicit inputs for the selected Merton function, including their dates, units, and observation alignment.

### Conditional Inputs

- Time-series estimation controls only for `mertonByTimeSeries`.

### Input Validation

- Validate numeric domains, dates, vector alignment, and whether the selected function expects point-in-time or time-series inputs.

## Critical Rules

### Intent Preservation

- Preserve supplied financial conventions and estimation choices; do not silently substitute a calibration method.

### Data and Unit Conventions

- Keep price, volatility, debt, rate, maturity, and probability units explicit and mutually consistent.

### Execution Boundaries

- Keep copula portfolio simulation and rating-transition calculations outside this skill.

## Failure Handling

- Stop on invalid domains, inconsistent dates, solver/convergence diagnostics, or unselected model assumptions.

## Gotchas

- Treat output probability and inferred structural quantities as model outputs, not independently validated credit decisions.

## Reference Loading

- Load [the Merton function reference](references/matlab-functions.md) for exact syntax and release-scoped behavior.
