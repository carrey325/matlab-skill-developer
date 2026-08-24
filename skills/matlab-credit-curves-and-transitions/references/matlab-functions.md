# Credit Curve and Transition Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No calculation was executed. Preserve rating ordering and probability units as documented.

### `bondDefaultBootstrap`

- Syntax: `[ProbabilityData,HazardData] = bondDefaultBootstrap(ZeroData,MarketData,Settle)`; `[ProbabilityData,HazardData] = bondDefaultBootstrap(___,Name,Value)`.
- Contract: zero data is a dates/rates matrix or `IRDataCurve`; market data and settlement must be aligned. Returns date/default-probability data and hazard data.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/bonddefaultbootstrap.html), introduced R2017a; R2022b deprecates serial-date-number preference.

### `transprob`

- Syntax: `[transMat,sampleTotals,idTotals] = transprob(data)`; `[transMat,sampleTotals,idTotals] = transprob(___,Name,Value)`.
- Contract: accept documented migration data representations; return an `nRatings`-by-`nRatings` transition matrix in percent plus totals. R2024a adds an optional weights fourth data column.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/transprob.html), introduced R2010b.

### `transprobfromthresholds`

- Syntax: `trans = transprobfromthresholds(thresh)`.
- Contract: `thresh` is an `M`-by-`N` threshold matrix whose first entry per row is `Inf` and whose rows are monotonically nonincreasing. Returns transition probabilities in percent.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/transprobfromthresholds.html), introduced R2011b.

### `transprobtothresholds`

- Syntax: `thresh = transprobtothresholds(trans)`.
- Contract: `trans` is an `M`-by-`N` percentage transition matrix with nonnegative values no greater than 100 and rows summing to 100. Returns thresholds.
- Evidence: [official page](https://ww2.mathworks.cn/help/finance/transprobtothresholds.html), introduced R2011b.
