---
name: matlab-backtest
description: Writes, reviews, or repairs MATLAB portfolio-backtest code when MATLAB is explicitly requested or is the default language and backtest-workflow has supplied the implementation plan. Use directly when the strategy, schedule, state, costs, and required engine operations are already fixed. It does not design the strategy, select research methods, set evaluation policy, or interpret investment merit.
---

# Implement Portfolio Backtests in MATLAB

## Scope

Translate an approved backtest implementation brief into correct MATLAB code, or repair explicitly selected `backtestStrategy`, `backtestEngine`, and related function calls. Do not design the strategy or research workflow.

## Prerequisites

- MATLAB and Financial Toolbox in a release supporting all selected backtesting properties and functions.
- A `backtest-workflow` MATLAB implementation brief, or a direct request specifying strategy logic, engine operations, data, schedule, state, costs, and outputs.
- Adjusted price data and any required signal/state inputs in the agreed representation.

## Capability Contract

### Required Inputs

- ordered asset-price timetable and strategy name;
- selected rebalance function behavior and exact configured state mode;
- rebalance schedule, lookback, start/end or warmup treatment;
- engine rates/value settings, required outputs, and verification tolerance.

### Conditional Inputs

- signal timetable when selected;
- `UserData` or `EngineDataList` fields when selected;
- initial weights, transaction-cost function/rates, and fee configuration when selected.

### Input Validation

- Check unique increasing row times, asset order, timetable widths, finiteness policy, and price/signal time alignment.
- Check strategy-name validity, weight length, supported schedule types, and callback signature implied by the supplied configuration.
- Reject missing strategy or research decisions rather than choosing them.

## Critical Rules

### Intent Preservation

- Preserve supplied strategy logic, schedule, lookback, state, costs, cash/borrowing, and execution window.
- Do not normalize weights unless the brief requires full investment.
- Escalate missing design choices to `backtest-workflow` or the user.

### Data and Unit Conventions

- Preserve row times, asset order, adjusted-price status, rate conventions, basis, currency, and cost units.
- Treat rolling windows passed by the engine as the allowed information set.
- Extract numeric data from tables/timetables only where the selected numeric function requires it.

### Execution Boundaries

- Consult [references/matlab-functions.md](references/matlab-functions.md) only for selected functions and properties.
- Match callback inputs/outputs exactly to signals, `UserData`, and `EngineDataList`.
- Capture MATLAB diagnostics, rebalance date/window, warnings, skipped periods, and engine output shapes.
- Verify code-level chronology and engine outputs; leave hypothesis design and any requested professional performance interpretation to the workflow.

## Failure Handling

- Missing release/property: identify the unsupported item and stop.
- Callback arity or output failure: correct only the function signature and configured state interface.
- Timetable/type/shape failure: preserve dates and asset order while correcting the MATLAB representation.
- Runtime strategy failure: return the date, window, state, and diagnostic; do not change strategy economics.
- Missing research decision or leakage policy: return to `backtest-workflow` rather than inventing one.

## Gotchas

- Strategies are passed to `backtestEngine`; prices and optional signals are passed to `runBacktest`.
- Transaction costs belong to `backtestStrategy`.
- Callback signatures vary with signals, `UserData`, and `EngineDataList`.
- `summary` metrics are rows and strategies are columns.
- Local functions do not automatically see ordinary script workspace variables.
- Read [references/gotchas.md](references/gotchas.md) for function-specific failures.

## Reference Loading

- Read [references/matlab-functions.md](references/matlab-functions.md) for the selected object, function, or property.
- Read [references/gotchas.md](references/gotchas.md) only for affected calls or diagnostics.
