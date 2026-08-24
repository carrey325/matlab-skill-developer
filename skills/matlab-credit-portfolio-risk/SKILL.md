---
name: matlab-credit-portfolio-risk
description: Implement selected corporate credit portfolio simulation, capital, concentration, and risk-contribution calculations in MATLAB without selecting the credit-risk methodology.
---

# Implement Credit Portfolio Risk in MATLAB

## Scope

Implement, review, or repair MATLAB using `creditDefaultCopula`, `creditMigrationCopula`, `asrf`, and `concentrationIndices` after the portfolio-risk method and conventions are already selected.

Do not select portfolio composition, dependence assumptions, capital policy, confidence level, or reporting interpretation.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected default or migration copula workflow, or an explicit ASRF/concentration calculation contract.
- Aligned counterparty, rating/default, exposure, and scenario inputs required by the selected object.

## Capability Contract

### Required Inputs

- The selected object/function, data dimensions, scenario count, and requested risk measure.

### Conditional Inputs

- Correlations, transition/default data, confidence levels, recovery inputs, and simulation controls only when the selected operation requires them.

### Input Validation

- Validate dimensions, probability/rating conventions, portfolio alignment, and post-simulation result shapes before aggregating results.

## Critical Rules

### Intent Preservation

- Preserve the supplied portfolio and model assumptions exactly; do not substitute default risk for migration risk or vice versa.

### Data and Unit Conventions

- Keep probability units, exposure units, counterparty order, and scenario dimensions explicit throughout the call chain.

### Execution Boundaries

- Keep market VaR/ES backtesting, Merton PD estimation, CDS pricing, and transition-curve construction in their dedicated skills.

## Failure Handling

- Stop on inconsistent portfolio dimensions, invalid probability/correlation inputs, absent toolbox support, or unresolved simulation diagnostics.

## Gotchas

- Object methods with identical names belong to different copula classes; dispatch from the object type, not the bare method name.

## Reference Loading

- Load [the copula and portfolio-risk reference](references/matlab-functions.md) for exact object-specific calls.
