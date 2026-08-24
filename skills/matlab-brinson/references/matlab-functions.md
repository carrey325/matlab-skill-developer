# MATLAB Brinson Functions

Official MathWorks documentation was inspected on 2026-08-20. Treat entries as documentation-inspected unless execution evidence is supplied.

## `brinsonAttribution`

- Product: Financial Toolbox; introduced in R2022b.
- Constructor: `obj = brinsonAttribution(AssetTable)`.
- Accepts one table with `NumAssets * NumPeriods` rows.
- Documented left-to-right columns: Period, Name, Return, Category, PortfolioWeight, BenchmarkWeight.
- Weight values are normalized with a warning when period sums differ from one; preserve and report that warning.
- Source: [brinsonAttribution](https://www.mathworks.com/help/finance/brinsonattribution.html).

## `totalAttribution`

- Computes total Brinson attribution for the constructed object.
- Source: [totalAttribution](https://www.mathworks.com/help/finance/brinsonattribution.totalattribution.html).

## `categoryAttribution`

- Computes attribution by category.
- Source: [categoryAttribution](https://www.mathworks.com/help/finance/brinsonattribution.categoryattribution.html).

## `categoryReturns` / `categoryWeights`

- Return aggregate and periodic category returns or weights.
- Sources: [categoryReturns](https://www.mathworks.com/help/finance/brinsonattribution.categoryreturns.html) and [categoryWeights](https://www.mathworks.com/help/finance/brinsonattribution.categoryweights.html).

## `summary`

- Produces the object's consolidated attribution summary.
- Source: [Brinson summary](https://www.mathworks.com/help/finance/brinsonattribution.summary.html).

## Chart Functions

- `attributionsChart(obj)` plots attribution effects.
- `categoryReturnsChart(obj)` plots category returns.
- `categoryWeightsChart(obj)` plots category weights.
- Generate charts only when selected and after the workflow's numerical reconciliation.

## `tick2ret`

- For a time-by-asset numeric price matrix, output has one fewer time row.
- Transpose only when the supplied AssetTable ordering requires an asset-by-period matrix.
- Source: [tick2ret](https://www.mathworks.com/help/finance/tick2ret.html).

## Object Properties

Inspect `NumAssets`, `NumPeriods`, `NumCategories`, asset/category matrices, portfolio/benchmark category values, `PortfolioReturn`, `BenchmarkReturn`, and `ActiveReturn` according to the installed documentation. Do not use properties as substitutes for the workflow's benchmark and timing policy.
