---
name: backtest-workflow
description: Plans or reviews an investment-strategy backtest from hypothesis and point-in-time data through strategy, benchmark, sampling, costs, implementation selection, execution, and evaluation. Use when strategy design, rebalance policy, lookback, warmup, costs, lag, benchmark, in/out-of-sample structure, or interpretation must be decided. Do not use for code-only implementation of an already specified backtest or for live trading.
---

# Execute Portfolio Backtest Workflow

## When to Use

- Design a backtest from a research question or compare strategies.
- Choose universe, benchmark, sampling, signal timing, rebalance policy, lookback, costs, lag, and evaluation periods.
- Review a backtest for look-ahead, survivorship, corporate-action, tuning, or cost bias.
- Produce an implementation brief and a defensible performance assessment.

## When Not to Use

- The strategy, schedule, inputs, costs, and MATLAB operations are already fixed; use `matlab-backtest` directly.
- The task is live execution, order management, instrument pricing, or attribution without a backtest-design question.
- The request asks for a performance guarantee or treats simulated results as future performance.

## Inputs and Conventions

Resolve the hypothesis, decision rule, universe formation, point-in-time sources, benchmark, data adjustment, calendar/timezone, return convention, rebalance timing, implementation lag, lookback, warmup, holdings/cash, transaction costs, fees, borrowing, in-sample/OOS split, and requested metrics.

Do not approximate calendar frequency with a fixed observation count when calendar semantics matter. Do not assume a zero-cost or zero-lag strategy when the comparison depends on trading.

## Implementation Selection

### Method-to-Object Map

| Backtest need | MATLAB implementation object | Selection condition |
|---|---|---|
| Standard portfolio strategy with rolling price/signal windows | `backtestStrategy` + `backtestEngine` | Callback, schedule, state, cost, and output semantics fit the official engine |
| Stateful strategy requiring approved user or engine data | Same engine with state properties | Required state is representable by documented interfaces |
| Nonstandard fills, cash flows, instruments, or accounting | Custom engine outside this capability | Official engine cannot represent essential economics faithfully |

Prefer the official engine only when it represents the strategy without hiding essential assumptions. A custom engine requires independent tests for position drift, fills, costs, return alignment, cash, and benchmark accounting.

### Operation-to-Function Map

| Selected operation | MATLAB function/property family |
|---|---|
| Define strategy and rebalance logic | `backtestStrategy` and a rebalance function |
| Configure environment and rates | `backtestEngine` |
| Run with prices and optional signals | `runBacktest` |
| Summarize performance | `summary` |
| Plot equity | `equityCurve` |
| Inspect detailed paths | `Returns`, `Positions`, `Turnover`, `BuyCost`, `SellCost`, `Fees` |

## Workflow

### Define the Research Claim and Evaluation Design

1. State hypothesis, audience, decision criterion, and benchmark.
2. Define sample partitions before tuning and record searched parameters and selection rules.
3. Select metrics and robustness checks appropriate to the claim; avoid universal Sharpe, drawdown, or turnover thresholds.
4. Stop when the hypothesis is untestable or the requested evidence cannot support the proposed conclusion.

### Build a Point-in-Time Research Sample

1. Audit availability dates for prices, signals, universe membership, classifications, and revisions.
2. Resolve adjustments, corporate actions, calendar, timezone, missing data, and benchmark alignment.
3. Stop on leakage, survivorship that cannot be characterized, unresolvable corporate actions, or inconsistent timestamps.

### Specify the Strategy and Trading Model

1. Define strategy logic and required state without looking at held-out outcomes.
2. Choose observation or calendar schedule, lookback, warmup, implementation lag, costs, fees, cash, borrowing, and initial holdings.
3. Stop when trading assumptions or state behavior are materially undefined.

### Select the Engine and Freeze the Implementation Brief

1. Choose the official or custom engine based on representational fit, not convenience.
2. Specify ordered assets, price and signal timetable contracts, callback state, schedule, lookback, warmup, start/end, initial weights, costs/fees, engine rates, requested outputs, and chronology/cost checks.
3. Hand the frozen brief to `matlab-backtest` without embedding signatures or code.

### Run the Experiment

1. Freeze the selected configuration and execute through the language implementation.
2. Preserve configuration, data versions, dates, warnings, fallbacks, skipped rebalances, and runtime evidence.
3. Return coding/runtime failures to the language skill; return strategy or research-design failures to the responsible workflow stage.

### Evaluate the Evidence and Its Limits

1. Prove that each rebalance used only information available at that time.
2. Reconcile positions, cash, turnover, costs, fees, and benchmark treatment.
3. Separate warmup, calibration, validation, and held-out performance.
4. Compare with an appropriate baseline and assess sensitivity without data-mined thresholds.
5. Report limitations, instability, and simulation status; do not authorize live trading.

## Output and Implementation Brief

Return the research contract, point-in-time audit, selected engine and operations, frozen parameters, MATLAB brief, execution evidence, performance/robustness results, failed checks, and limitations.
