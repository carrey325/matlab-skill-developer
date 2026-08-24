# Claims Reserving Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No reserving calculation was executed. The selected technique owns its own object type; dispatch common result methods from that object rather than by bare method name.

## `developmentTriangle`

- Construct: `dT = developmentTriangle(data)`; `dT = developmentTriangle(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.html), R2020b.
- `selectedLinkRatiosTable = cdfSummary(developmentTriangle)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.cdfsummary.html).
- `claimsPlot(dT)`; `claimsPlot(dT,Name,Value)`; `h = claimsPlot(ax,___)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.claimsplot.html), R2021a.
- `fullTriangleTable = fullTriangle(developmentTriangle)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.fulltriangle.html).
- `LinkRatioAveragesTable = linkRatioAverages(developmentTriangle)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.linkratioaverages.html).
- `LinkRatiosTable = linkRatios(developmentTriangle)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.linkratios.html).
- `linkRatiosPlot(dT)`; `h = linkRatiosPlot(ax,___)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.linkratiosplot.html), R2021a.
- `projectedUltimateClaims = ultimateClaims(dT)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.ultimateclaims.html).
- `developmentTriangleTable = view(developmentTriangle)`. [Source](https://ww2.mathworks.cn/help/risk/developmenttriangle.view.html).

## `chainLadder`

- Construct: `cl = chainLadder(dT_reported,dT_paid)`. [Source](https://ww2.mathworks.cn/help/risk/chainladder.html), R2020b.
- `ibnrClaims = ibnr(cl)`; `ibnrClaims = ibnr(___,referenceClaimsType)`. [Source](https://ww2.mathworks.cn/help/risk/chainladder.ibnr.html).
- `unpaidClaimsEstimateTable = summary(cl)`. [Source](https://ww2.mathworks.cn/help/risk/chainladder.summary.html).
- `unpaidClaimsEstimate = unpaidClaims(cl)`; `unpaidClaimsEstimate = unpaidClaims(___,referenceClaimsType)`. [Source](https://ww2.mathworks.cn/help/risk/chainladder.unpaidclaims.html).

## `expectedClaims`

- Construct: `ec = expectedClaims(dT_reported,dT_paid,earnedPremium)`; `ec = expectedClaims(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/expectedclaims.html), R2020b.
- `ibnrClaims = ibnr(ec)`. [Source](https://ww2.mathworks.cn/help/risk/expectedclaims.ibnr.html).
- `unpaidClaimsEstimateTable = summary(ec)`. [Source](https://ww2.mathworks.cn/help/risk/expectedclaims.summary.html).
- `projectedUltimateClaims = ultimateClaims(ec)`. [Source](https://ww2.mathworks.cn/help/risk/expectedclaims.ultimateclaims.html).
- `unpaidClaimsEstimate = unpaidClaims(ec)`. [Source](https://ww2.mathworks.cn/help/risk/expectedclaims.unpaidclaims.html).

## `bornhuetterFerguson`

- Construct: `bf = bornhuetterFerguson(dT_reported,dT_paid,expectedClaims)`. [Source](https://ww2.mathworks.cn/help/risk/bornhuetterferguson.html), R2020b.
- `ibnrClaims = ibnr(bf)`; `ibnrClaims = ibnr(___,referenceClaimsType)`. [Source](https://ww2.mathworks.cn/help/risk/bornhuetterferguson.ibnr.html).
- `unpaidClaimsEstimateTable = summary(bf)`. [Source](https://ww2.mathworks.cn/help/risk/bornhuetterferguson.summary.html).
- `projectedUltimateClaims = ultimateClaims(bf)`; `projectedUltimateClaims = ultimateClaims(___,referenceClaimsType)`. [Source](https://ww2.mathworks.cn/help/risk/bornhuetterferguson.ultimateclaims.html).
- `unpaidClaimsEstimate = unpaidClaims(bf)`; `unpaidClaimsEstimate = unpaidClaims(___,referenceClaimsType)`. [Source](https://ww2.mathworks.cn/help/risk/bornhuetterferguson.unpaidclaims.html).

## `capeCod`

- Construct: `cc = capeCod(dT_reported,dT_paid,earnedPremium)`. [Source](https://ww2.mathworks.cn/help/risk/capecod.html), R2021a.
- `ibnrClaims = ibnr(cc)`. [Source](https://ww2.mathworks.cn/help/risk/capecod.ibnr.html).
- `unpaidClaimsEstimateTable = summary(cc)`. [Source](https://ww2.mathworks.cn/help/risk/capecod.summary.html).
- `projectedUltimateClaims = ultimateClaims(cc)`. [Source](https://ww2.mathworks.cn/help/risk/capecod.ultimateclaims.html).
- `unpaidClaimsEstimate = unpaidClaims(cc)`. [Source](https://ww2.mathworks.cn/help/risk/capecod.unpaidclaims.html).
