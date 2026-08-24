# Structural Default Model Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No function was executed.

### `mertonmodel`

- Syntax: `[PD,DD,A,Sa] = mertonmodel(Equity,EquityVol,Liability,Rate)`; `[PD,DD,A,Sa] = mertonmodel(___,Name,Value)`.
- Contract: equity, equity volatility, and liability threshold are positive; equity volatility is annualized. Returns default probability, distance to default, asset value, and asset volatility.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/mertonmodel.html), introduced R2017a.

### `mertonByTimeSeries`

- Syntax: `[PD,DD,A,Sa] = mertonByTimeSeries(Equity,Liability,Rate)`; `[PD,DD,A,Sa] = mertonByTimeSeries(___,Name,Value)`.
- Contract: equity and liability threshold are positive and rate is annualized. Returns the same output family after time-series estimation.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/mertonbytimeseries.html), introduced R2017a.
