---
name: portfolio-workflow
description: Plans or reviews portfolio optimization from mandate and data through method selection, constraints, implementation choice, execution evidence, and solution assessment. Use when the objective, benchmark role, estimation policy, trading assumptions, or allocation method must be decided or reviewed. Do not use for a code-only request whose method and operations are already fixed, for live order submission, or for unrelated pricing and risk tasks.
---

# Execute Portfolio Optimization Workflow

## When to Use

- Define or review a portfolio optimization study from an investment objective.
- Choose among minimum variance, efficient frontier, maximum Sharpe, CVaR, MAD, risk budgeting, or a custom objective.
- Decide whether a benchmark is descriptive, an objective, or a tracking-error constraint.
- Establish bounds, leverage, groups, cardinality, turnover, costs, holdings, or implementation lag.
- Compare allocation methods or prepare a reviewable implementation brief.

## When Not to Use

- The request already specifies the method, operations, parameters, and MATLAB deliverable; use `matlab-portfolio` directly.
- The task is only backtesting, Brinson attribution, instrument pricing, or live trade execution.
- The user asks for an organization-specific limit or production allocation without the required domain approval.

## Inputs and Conventions

Resolve material choices before implementation:

- investment purpose, horizon, universe, and eligible assets;
- objective and primary risk measure;
- expected-return, covariance, or scenario estimation policy;
- benchmark role and benchmark weights when relevant;
- current holdings, budget, leverage, bounds, group exposure, cardinality, turnover, and costs;
- currency, return type, compounding, frequency, annualization, risk-free rate, and missing-data policy;
- research, advisory, or production context and any approval required for actual decision use.

Ask when a missing choice changes the economic result. Do not silently assume zero costs, unlimited tracking error, unrestricted group tilts, or a maximum-Sharpe objective.

## Implementation Selection

### Method-to-Object Map

| Professional method | MATLAB implementation object | Selection condition |
|---|---|---|
| Mean-variance, minimum variance, efficient frontier, maximum Sharpe | `Portfolio` | Expected returns/covariance are part of the mandate |
| Conditional value-at-risk | `PortfolioCVaR` | Tail loss is the selected risk measure and scenarios/confidence are defined |
| Mean absolute deviation | `PortfolioMAD` | Scenario-based absolute deviation is the selected risk measure |
| Risk budgeting / risk parity | Standalone risk-budgeting functions | Target risk contributions are the objective |
| Custom objective | `Portfolio` custom-objective path | The objective and required convexity/solver conditions are established |

If no supported method faithfully represents the mandate, stop and report the capability gap rather than selecting the nearest available object.

### Operation-to-Function Map

| Selected operation | MATLAB function family |
|---|---|
| Set moments or estimate them from return data | `setAssetMoments`, `estimateAssetMoments` |
| Set or simulate scenarios | `setScenarios`, `simulateNormalScenariosByData`, `simulateNormalScenariosByMoments` |
| Configure budget, bounds, groups, tracking, turnover, costs, or cardinality | `setBudget`, `setBounds`, `setGroups`, `setTrackingError`, `setTurnover`, `setCosts`, `setMinMaxNumAssets` |
| Generate a frontier or target portfolio | `estimateFrontier`, `estimateFrontierByReturn`, `estimateFrontierByRisk` |
| Select maximum Sharpe | `estimateMaxSharpeRatio` |
| Solve a custom objective | `estimateCustomObjectivePortfolio` |
| Compute risk budgeting and contributions | `riskBudgetingPortfolio`, `portfolioRiskContribution` |
| Check feasibility and portfolio measures | `checkFeasibility`, `estimatePortMoments`, `estimatePortRisk`, `estimatePortReturn` |

## Workflow

### Frame the Investment Mandate and Evidence Base

1. State the investment question and decision owner.
2. Audit asset identity, data meaning, frequency, availability dates, missingness, and estimation sample.
3. Record every material convention and constraint in economic terms and units.
4. Stop on contradictory objectives, infeasible policy requirements, missing benchmark semantics, or unsupported production authority.

### Choose the Formulation and Prepare the Implementation

1. Select the professional method from the mandate, not from whichever code already exists.
2. Choose the MATLAB object and operations from the maps above.
3. Identify required moments, scenarios, confidence level, solver class, benchmark, holdings, and trade assumptions.
4. Record alternatives only when a meaningful unresolved choice remains; recommend one with its tradeoff.
5. Create an implementation brief containing:

   - selected language and MATLAB object;
   - ordered asset list and data representation;
   - selected operations and parameters;
   - constraints with units and hard/advisory status;
   - requested weights, trades, frontier, measures, tables, or plots;
   - feasibility, constraint, and numerical acceptance checks.

Do not place MATLAB signatures or code in the brief. Hand the brief to `matlab-portfolio`.

### Run Without Changing the Mandate

1. Use the selected language implementation skill to construct and run the code.
2. Preserve runtime evidence, warnings, solver status, dimensions, and applied configuration.
3. Return coding, signature, type, shape, and runtime failures to the language layer.
4. Return objective, convention, or infeasibility decisions to the workflow stage that owns them. Never relax the mandate merely to make execution succeed.

### Assess the Solution for Its Intended Decision

1. Reconcile weights, budget, leverage, bounds, groups, tracking error, turnover, costs, and cardinality.
2. Confirm the computed portfolio corresponds to the selected objective and frequency conventions.
3. Review estimation sensitivity and concentration appropriate to the research context.
4. Separate expected optimization outputs from realized backtest evidence.
5. Report assumptions, limitations, and unresolved choices. Include approval state only when the decision context requires it; do not authorize production trades.

## Output and Implementation Brief

Return the resolved mandate, method selection, implementation map, conventions, constraint ledger, execution evidence, verification results, and limitations. Include approval status only when professionally relevant. The MATLAB brief must be complete enough that `matlab-portfolio` can code without making a domain decision.
