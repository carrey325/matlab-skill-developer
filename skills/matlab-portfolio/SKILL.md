---
name: matlab-portfolio
description: Writes, reviews, or repairs MATLAB portfolio-optimization code when MATLAB is explicitly requested or is the default language and portfolio-workflow has supplied the implementation plan. Use directly when the object, operations, and financial parameters are already fixed. It does not select the portfolio method, benchmark role, constraints, or any applicable approval and interpretation policy.
---

# Implement Portfolio Optimization in MATLAB

## Scope

Translate an approved portfolio implementation brief into correct MATLAB code, or repair code for explicitly selected portfolio objects and functions. Preserve the supplied domain intent; do not perform portfolio-method selection.

## Prerequisites

- MATLAB and Financial Toolbox in a release supporting every selected function.
- A `portfolio-workflow` MATLAB implementation brief, or an equivalent direct request that specifies the object, operations, asset order, inputs, parameters, and required outputs.
- The data, moments, scenarios, benchmark/current weights, constraints, and conventions required by the selected calls.

## Capability Contract

### Required Inputs

- selected MATLAB object or standalone function path;
- ordered asset names and corresponding numeric inputs;
- selected operations and parameters;
- required output artifacts and verification tolerance.

### Conditional Inputs

- scenarios and confidence level for scenario-risk objects;
- benchmark weights for tracking operations;
- initial weights for turnover, costs, or trade outputs;
- group matrix, bounds, cardinality, target return/risk, or custom objective when selected;
- solver configuration only when the selected problem class requires it.

### Input Validation

- Check dimensions, finiteness, asset order, covariance symmetry/diagonal, probability bounds, and parameter units.
- Check the installed release and products before using release-sensitive functions.
- Reject an incomplete brief instead of selecting a financial method or inventing a constraint.

## Critical Rules

### Intent Preservation

- Use exactly the selected object, objective, benchmark treatment, constraints, and operations.
- Do not relax or replace financial requirements to obtain solver success.
- Escalate missing domain decisions to `portfolio-workflow` or the user.

### Data and Unit Conventions

- Keep observations and assets in the orientation required by the selected function.
- Distinguish prices, simple returns, continuous returns, moments, and scenarios.
- Preserve supplied frequency, compounding, annualization, risk-free-rate, target, cost, and tracking-error units.
- Keep all vectors and matrices in one identical asset order.

### Execution Boundaries

- Consult [references/matlab-functions.md](references/matlab-functions.md) only for functions selected in the brief.
- Capture Code Analyzer findings, warnings, solver/exit status, dimensions, and nonfinite outputs when execution is available.
- Verify function-level outputs and requested numerical invariants; leave professional interpretation and any required approval to the workflow.
- Do not submit trades or expand a code task into portfolio advice.

## Failure Handling

- Missing product or release support: identify the unavailable function and stop.
- Signature, option, type, or shape failure: preserve the diagnostic and correct only the MATLAB call or input representation.
- Solver/runtime failure: return the status and last verified configuration; do not change the objective or constraints.
- Failed numerical invariant: report the failed check and do not claim a valid solution.
- Missing method or convention: return to `portfolio-workflow`; do not choose it in this skill.

## Gotchas

- `estimateFrontier` optional outputs are trades, not risk and return.
- `estimatePortMoments` returns risk before return.
- `Portfolio`, `PortfolioCVaR`, and `PortfolioMAD` do not share every data or analysis method.
- `riskBudgetingPortfolio` returns numeric weights, not a portfolio object.
- Conditional bounds and cardinality can require a mixed-integer solver.
- Read [references/gotchas.md](references/gotchas.md) for function-specific recurring failures.

## Reference Loading

- Read [references/matlab-functions.md](references/matlab-functions.md) for exact functions selected by the implementation brief.
- Read [references/gotchas.md](references/gotchas.md) only when using the affected function or repairing a related failure.
