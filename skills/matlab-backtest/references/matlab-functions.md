# MATLAB Backtest Functions

Official MathWorks documentation was inspected on 2026-08-20. Treat entries as documentation-inspected unless execution evidence is supplied.

## `backtestStrategy`

- Product: Financial Toolbox.
- Base signature: `strategy = backtestStrategy(name,rebalanceFcn,Name=Value)`.
- `RebalanceFrequency` supports documented integer, duration, calendar-duration, or datetime schedules.
- `LookbackWindow` controls rolling data passed to the callback.
- `TransactionCosts`, `InitialWeights`, fee properties, `UserData`, and `EngineDataList` are release-sensitive configuration properties.
- Source: [backtestStrategy](https://www.mathworks.com/help/finance/backteststrategy.html).

### Rebalance callback signatures

- No state, no signals: `newWeights = fcn(weights,assetPrices)`.
- No state, signals: `newWeights = fcn(weights,assetPrices,signalData)`.
- `UserData`, no signals: `[newWeights,userData] = fcn(weights,assetPrices,userData)`.
- `UserData`, signals: `[newWeights,userData] = fcn(weights,assetPrices,signalData,userData)`.
- `EngineDataList` replaces the first weights input with engine data; inspect the official page for the selected state combination.

## `backtestEngine`

- Base signature: `engine = backtestEngine(strategies,Name=Value)`.
- Strategies are the positional input; prices are not constructor inputs.
- Rate, basis, borrowing, and initial-value properties must match the implementation brief.
- Detailed results remain empty before a backtest is run.
- Source: [backtestEngine](https://www.mathworks.com/help/finance/backtestengine.html).

## `runBacktest`

- Without signals: `engine = runBacktest(engine,pricesTT,Name=Value)`.
- With signals: `engine = runBacktest(engine,pricesTT,signalTT,Name=Value)`.
- Price columns represent assets; the optional signal timetable must share the required time dimension.
- `Start` and `End` select the execution range and interact with lookback/warmup.
- Introduced in R2020b.
- Source: [runBacktest](https://www.mathworks.com/help/finance/backtestengine.runbacktest.html).

## `summary`

- `summary(engine)` returns a table with metric row names and strategy columns.
- Inspect row names at runtime rather than assuming every release/configuration exposes identical metrics.
- Source: [summary](https://www.mathworks.com/help/finance/backtestengine.summary.html).

## `equityCurve`

- `equityCurve(engine)` plots portfolio-value paths after execution.
- Source: [equityCurve](https://www.mathworks.com/help/finance/backtestengine.equitycurve.html).

## Result Properties

- `Returns`: per-time-step strategy returns.
- `Positions`: per-strategy asset positions.
- `Turnover`: strategy turnover.
- `BuyCost` and `SellCost`: transaction-cost results.
- `Fees`: fee results when configured and supported.

## `tick2ret` and Numeric Functions

- `tick2ret` changes row count by one and preserves table/timetable behavior according to input type and release.
- Extract numeric contents before calling numeric-only functions such as `cov`.
- Source: [tick2ret](https://www.mathworks.com/help/finance/tick2ret.html).
