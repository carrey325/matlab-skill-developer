# MATLAB Portfolio Gotchas by Function

## `estimateAssetMoments` / `setScenarios`

- Rows are observations and columns are assets.
- Do not convert data that already contains returns.
- Do not cross `Portfolio` moment calls with scenario-object-only calls.

## `setBudget` / `setBounds`

- A lower budget greater than the upper budget is invalid.
- A scalar bound can imply a single-asset problem in some construction orders; establish asset count first when needed.
- Conditional bounds are not ordinary continuous bounds and may require a different solver.

## `setGroups` / `setTrackingError`

- Group matrices require one column per asset.
- Tracking portfolios are full weight vectors, not lists of asset indices.
- Benchmark and group order must match the object asset order.

## `estimateFrontier`

- Outputs two and three are buy and sell trades, not risk and return.
- Weight matrices place one portfolio in each column.
- Compute measures with object-supported measure functions.

## `estimatePortMoments`

- The output order is `[risk,return]`.
- Do not call it on an object that does not support it.

## `estimateCustomObjectivePortfolio`

- Compute a displayed objective value by evaluating the function at returned weights; an optional output is not the objective value.
- Pass `ObjectiveSense` as a name-value argument.
- Inspect `exitflag` and do not claim success after an adverse status.

## `riskBudgetingPortfolio` / `portfolioRiskContribution`

- `riskBudgetingPortfolio` returns a numeric vector, not a portfolio object.
- Relative risk contributions sum to one; absolute contributions use portfolio-risk units.

## MATLAB Tables and Syntax

- Use `array2table` when each weight should become a separate named variable.
- Do not transpose a table with `'`.
- Use `[~,idx] = min(x)` or `max(x)` when the index is required.
- MATLAB does not support a `?:` ternary operator.

Legacy `CAPMuniverse` dimensions and expected values are fixture-specific and must not be generalized.
