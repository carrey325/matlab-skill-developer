# VaR and ES Backtesting Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No backtest was executed. All constructors require aligned portfolio observations and forecast data; validate time, row counts, IDs, and levels before calling methods.

## VaR backtests: `varbacktest`

- Construct: `vbt = varbacktest(PortfolioData,VaRData)`; `vbt = varbacktest(___,Name,Value)`. R2023b adds `Time` and object support for append/select/plot/exceptions. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.html).
- `TestResults = bin(vbt)` or `bin(vbt,Name,Value)` — binomial test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.bin.html).
- `TestResults = cc(vbt)` or `cc(vbt,Name,Value)` — conditional coverage mixed test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.cc.html).
- `TestResults = cci(vbt)` or `cci(vbt,Name,Value)` — conditional coverage independence test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.cci.html).
- `TestResults = pof(vbt)` or `pof(vbt,Name,Value)` — proportion-of-failures test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.pof.html).
- `TestResults = runtests(vbt)` or `runtests(vbt,Name,Value)` — run selected/all VaR tests. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.runtests.html).
- `S = summary(vbt)` — report data summary. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.summary.html).
- `TestResults = tbf(vbt)` or `tbf(vbt,Name,Value)` — time-between-failures mixed test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.tbf.html).
- `TestResults = tbfi(vbt)` or `tbfi(vbt,Name,Value)` — time-between-failures independence test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.tbfi.html).
- `TestResults = tl(vbt)` — traffic-light test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.tl.html).
- `TestResults = tuff(vbt)` or `tuff(vbt,Name,Value)` — time-until-first-failure test. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.tuff.html).

## Shared backtest operations

- `vbt = append(vbt,newPortfolioData,newVaRData)`; `ebt = append(ebt,newPortfolioData,newVaRData,newESData)`; `___ = append(___,Time=newDates)`. Applies to supported VaR/ES objects. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.append.html), R2023b; ES extension in R2024a.
- `excTable = exceptions(btobj)` or `exceptions(btobj,Name=Value)` — return VaR/ES exceptions. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.exceptions.html).
- `plot(btobj)`; `plot(btobj,Name=Value)`; `hPlot = plot(___)` — visualize portfolio, risk forecasts, and exceptions. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.plot.html).
- `subbtobj = select(btobj,Name=Value)` — select VaR/ES backtest data. [Source](https://ww2.mathworks.cn/help/risk/varbacktest.select.html).

## Table-based ES backtests: `esbacktest`

- Construct: `ebt = esbacktest(PortfolioData,VaRData,ESData)`; `ebt = esbacktest(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktest.html), R2017b.
- `TestResults = runtests(ebt)` or `runtests(ebt,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktest.runtests.html).
- `S = summary(ebt)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktest.summary.html).
- `TestResults = unconditionalNormal(ebt)` or `unconditionalNormal(ebt,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktest.unconditionalnormal.html).
- `TestResults = unconditionalT(ebt)` or `unconditionalT(ebt,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktest.unconditionalt.html).

## Simulation-based ES backtests: `esbacktestbysim`

- Construct: `ebts = esbacktestbysim(PortfolioData,VaRData,ESData,DistributionName)`; `ebts = esbacktestbysim(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.html), R2017b.
- `TestResults = conditional(ebts)`; `[TestResults,SimTestStatistic] = conditional(ebts,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.conditional.html).
- `TestResults = minBiasAbsolute(ebts)`; `[TestResults,SimTestStatistic] = minBiasAbsolute(ebts,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.minbiasabsolute.html), R2020b.
- `TestResults = minBiasRelative(ebts)`; `[TestResults,SimTestStatistic] = minBiasRelative(ebts,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.minbiasrelative.html), R2020b.
- `TestResults = quantile(ebts)`; `[TestResults,SimTestStatistic] = quantile(ebts,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.quantile.html).
- `TestResults = runtests(ebts)` or `runtests(ebts,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.runtests.html).
- `ebts = simulate(ebts)` or `simulate(ebts,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.simulate.html).
- `S = summary(ebts)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.summary.html).
- `TestResults = unconditional(ebts)`; `[TestResults,SimTestStatistic] = unconditional(ebts,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbysim.unconditional.html).

## Du-Escanciano ES backtests: `esbacktestbyde`

- Construct: `ebtde = esbacktestbyde(PortfolioData,DistributionName)`; `ebtde = esbacktestbyde(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbyde.html), R2019b.
- `TestResults = conditionalDE(ebtde)`; `[TestResults,SimTestStatistic] = conditionalDE(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbyde.conditionalde.html).
- `TestResults = runtests(ebtde)` or `runtests(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbyde.runtests.html).
- `ebtde = simulate(ebtde)` or `simulate(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbyde.simulate.html).
- `S = summary(ebtde)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbyde.summary.html).
- `TestResults = unconditionalDE(ebtde)`; `[TestResults,SimTestStatistic] = unconditionalDE(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/esbacktestbyde.unconditionalde.html).
