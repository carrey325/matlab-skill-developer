# MATLAB Backtest Gotchas by Function

## `backtestStrategy`

- Put transaction costs on the strategy, not the engine.
- Do not invent a `SignalData` property; signals are passed to `runBacktest`.
- Do not use `Inf` as a rebalance schedule; use a documented type selected by the workflow.
- Strategy names must be unique and valid MATLAB variable names.

## Rebalance Functions

- Match callback inputs and outputs to signals, `UserData`, and `EngineDataList` exactly.
- Define each local function once.
- Local functions do not automatically see ordinary script workspace variables.
- Return one weight per asset and the required state output.
- Do not normalize when the supplied plan intentionally uses cash or borrowing.

## `runBacktest`

- Pass prices to `runBacktest`, not `backtestEngine`.
- Pass optional signals as the third positional argument.
- Align signal and price time dimensions.
- Do not let a closure read future rows outside the engine-supplied rolling window.

## Timetables and Numeric Calls

- Extract numeric contents before calling `cov` or another numeric-only function.
- Account for the row dropped by `tick2ret` in lookback guards.
- Preserve row times and asset order when converting table representations.

## `summary`

- Metrics are rows, not table variables such as `tbl.SharpeRatio`.
- Detailed engine properties are empty until execution completes.

Legacy `dowPortfolio.xlsx` row counts, date-dimension names, and window limits are fixture-specific.
