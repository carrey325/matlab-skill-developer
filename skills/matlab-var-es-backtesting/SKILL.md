---
name: matlab-var-es-backtesting
description: Implement selected value-at-risk and expected-shortfall backtest objects and diagnostics in MATLAB without choosing the risk model, testing policy, or regulatory interpretation.
---

# Implement VaR and ES Backtesting in MATLAB

## Scope

Implement, review, or repair `varbacktest`, `esbacktest`, `esbacktestbysim`, and `esbacktestbyde` objects and their documented methods after the backtesting design is selected.

Do not select the risk model, test-family policy, confidence level, pass/fail threshold, or regulatory conclusion.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- Aligned portfolio, VaR, and where applicable ES data, plus selected object type and test operations.

## Capability Contract

### Required Inputs

- A selected backtest object, consistent time axis, portfolio observations, and required forecast series.

### Conditional Inputs

- VaR/ES IDs, levels, distribution/simulation controls, and test-specific options when required by the chosen object.

### Input Validation

- Validate row counts, time alignment, forecast columns, level vectors, and object-specific data requirements before appending or testing.

## Critical Rules

### Intent Preservation

- Preserve the selected object class and test set; methods with identical names are not interchangeable across backtest objects.

### Data and Unit Conventions

- Keep return/loss signs, confidence levels, timestamps, portfolio identifiers, and forecast units explicit.

### Execution Boundaries

- Use `$matlab-var-es-estimation` for producing selected risk estimates; this skill evaluates supplied forecasts.

## Failure Handling

- Stop on unequal sample lengths, missing timestamps, invalid levels, object/type mismatch, or unselected test interpretation.

## Gotchas

- Dispatch shared methods such as `runtests`, `summary`, `plot`, and `simulate` from the concrete object class.

## Reference Loading

- Load [the backtesting reference](references/matlab-functions.md) and then the needed object subsection before coding.
