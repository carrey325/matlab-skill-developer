# MATLAB Portfolio Functions

Official MathWorks documentation was inspected on 2026-08-20. Unless a run artifact is supplied, treat these entries as documentation-inspected rather than freshly executed.

## `Portfolio`

- Product: Financial Toolbox.
- Purpose: represent portfolio moments, constraints, costs, turnover, tracking, and portfolio optimization operations selected by the workflow.
- Typical construction: `Portfolio(AssetList=names, AssetMean=mu, AssetCovar=Sigma)` using name-value syntax supported by the installed release.
- Validate that asset names, mean length, covariance rows/columns, and all later vectors share one order.
- Source: [Portfolio](https://www.mathworks.com/help/finance/portfolio.html).

## `PortfolioCVaR`

- Product: Financial Toolbox.
- Required information for selected calls: asset scenarios and probability level.
- Set scenarios with `setScenarios`; set confidence with `setProbabilityLevel` before computing CVaR results.
- Source: [PortfolioCVaR](https://www.mathworks.com/help/finance/portfoliocvar.html).

## `PortfolioMAD`

- Product: Financial Toolbox.
- Required information: asset-return scenarios.
- Use object-supported scenario, frontier, risk, and return functions rather than `Portfolio`-only moment methods.
- Source: [PortfolioMAD](https://www.mathworks.com/help/finance/portfoliomad.html).

## Moment and Scenario Functions

- `setAssetMoments(obj,mu,Sigma)` sets supplied moments on a compatible object.
- `estimateAssetMoments(obj,data,...)` estimates asset moments from observation-by-asset return data for supported objects.
- `setScenarios(obj,scenarioReturns)` supplies observation-by-asset scenarios to scenario objects.
- `simulateNormalScenariosByData` and `simulateNormalScenariosByMoments` are scenario-object functions; inspect the installed signature before use.
- `estimateScenarioMoments(obj)` returns scenario mean and covariance for supported objects.

## Constraint Functions

- `setDefaultConstraints(obj)` applies the documented long-only, fully invested defaults.
- `setBudget(obj,lower,upper)` constrains the sum of risky-asset weights.
- `setBounds(obj,lower,upper,...)` sets asset bounds; conditional bounds can change solver class.
- `setGroups(obj,G,lower,upper)` requires one column per asset in `G`.
- `setTrackingPort` and `setTrackingError` use benchmark weights in the exact asset order.
- `setTurnover`, `setOneWayTurnover`, and `setCosts` can require initial/current weights.
- `setMinMaxNumAssets` adds cardinality constraints.
- `checkFeasibility(obj,pwgt)` checks candidate portfolios against supported constraints.
- Source list: [Portfolio object functions](https://www.mathworks.com/help/finance/portfolio.html).

## Frontier and Measure Functions

- `[pwgt,pbuy,psell] = estimateFrontier(obj,...)`: portfolios are columns; optional outputs are trades.
- `estimateFrontierByReturn` and `estimateFrontierByRisk`: target units must match the object input frequency and risk proxy.
- `estimateFrontierLimits`: inspect the installed signature before choosing endpoints.
- `[risk,ret] = estimatePortMoments(p,pwgt)`: `Portfolio` risk is the first output.
- `estimatePortRisk(obj,pwgt)` and `estimatePortReturn(obj,pwgt)`: use the selected object's native risk and mean return.
- `estimateMaxSharpeRatio(p)`: risk-free rate comes from the configured `Portfolio` object.
- Sources: [estimateFrontier](https://www.mathworks.com/help/finance/portfolio.estimatefrontier.html), [estimatePortMoments](https://www.mathworks.com/help/finance/portfolio.estimateportmoments.html), and [estimatePortReturn](https://www.mathworks.com/help/finance/portfolio.estimateportreturn.html).

## `estimateCustomObjectivePortfolio`

- Introduced in R2022b; later releases add options.
- Signature family: `[pwgt,pbuy,psell,exitflag] = estimateCustomObjectivePortfolio(p,fun,Name=Value)`.
- The objective is a function of weights and must satisfy documented continuity/convexity requirements for the selected constraints.
- Source: [estimateCustomObjectivePortfolio](https://www.mathworks.com/help/finance/portfolio.estimatecustomobjectiveportfolio.html).

## Risk-Budgeting Functions

- `[pwgt,exitflag] = riskBudgetingPortfolio(Sigma,budget,Name=Value)`; introduced R2022a and returns numeric weights.
- `portfolioRiskContribution(pwgt,Sigma,Name=Value)` returns relative contributions by default; use `RiskContributionType="absolute"` when selected.
- Sources: [riskBudgetingPortfolio](https://www.mathworks.com/help/finance/riskbudgetingportfolio.html) and [portfolioRiskContribution](https://www.mathworks.com/help/finance/portfolioriskcontribution.html).

## Solver Functions

- Use `setSolver` or `setSolverMINLP` only when selected by the implementation brief and supported for the configured objective/constraints.
- Conditional bounds and cardinality can make the problem mixed-integer.
- Source: [Choosing and Controlling the Solver](https://www.mathworks.com/help/finance/choosing-and-controlling-the-solver.html).
