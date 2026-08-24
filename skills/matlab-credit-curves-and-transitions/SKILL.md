---
name: matlab-credit-curves-and-transitions
description: Implement selected default-probability curve bootstrap and credit transition calculations in MATLAB without choosing market-data, rating, or threshold conventions.
---

# Implement Credit Curves and Transitions in MATLAB

## Scope

Implement, review, or repair `bondDefaultBootstrap`, `transprob`, `transprobfromthresholds`, and `transprobtothresholds` after the curve or transition method is selected.

Do not select source bonds, ratings policy, threshold definition, interpolation policy, or credit-risk interpretation.

## Prerequisites

- MATLAB R2026a and Financial Toolbox.
- An explicit selected operation and aligned bond, rating, transition, or threshold data.

## Capability Contract

### Required Inputs

- The selected function, input matrix/table dimensions, dates, probability orientation, and desired output form.

### Conditional Inputs

- Bootstrap, recovery, ratings, threshold, and maturity conventions only when required by the selected operation.

### Input Validation

- Validate square transition matrices, probability bounds, rating-state ordering, date order, and market-data alignment.

## Critical Rules

### Intent Preservation

- Preserve state ordering and supplied market conventions. Do not reorder ratings or re-scale probabilities silently.

### Data and Unit Conventions

- Keep probability matrices, threshold vectors, dates, recovery values, and curve units explicit.

### Execution Boundaries

- Keep CDS pricing, Merton structural PD, and copula simulation in their dedicated skills.

## Failure Handling

- Stop on invalid probability mass, inconsistent matrix dimensions, missing market data, or nonselected curve assumptions.

## Gotchas

- Threshold-to-transition and transition-to-threshold operations are directional inverses only under their documented assumptions; do not treat them as generic array transforms.

## Reference Loading

- Load [the curve and transition reference](references/matlab-functions.md) for exact signatures and expected shapes.
