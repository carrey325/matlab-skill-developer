---
name: matlab-credit-default-swaps
description: Implement selected credit default swap pricing and spread calculations in MATLAB without choosing the contract, curve, recovery, or valuation methodology.
---

# Implement Credit Default Swaps in MATLAB

## Scope

Implement, review, or repair `cdsprice` and `cdsspread` calls for an already selected CDS valuation contract.

Do not select contractual terms, discount/default curve construction, recovery assumptions, or trading decisions.

## Prerequisites

- MATLAB R2026a and Financial Toolbox.
- A complete selected CDS contract and explicitly aligned date, curve, spread, and recovery conventions.

## Capability Contract

### Required Inputs

- The selected pricing or spread function and all required contract, curve, and date inputs.

### Conditional Inputs

- Optional accrual, payment-frequency, recovery, and convention parameters only when specified by the valuation brief.

### Input Validation

- Validate date ordering, curve dimensions, rate/spread units, and any contract-specific frequency or basis values.

## Critical Rules

### Intent Preservation

- Preserve the supplied contract and curve conventions; do not normalize percentages, dates, or recovery assumptions without instruction.

### Data and Unit Conventions

- Keep all dates, day-count conventions, rates, and spreads explicit.

### Execution Boundaries

- Route default-curve bootstrap construction to `$matlab-credit-curves-and-transitions`.

## Failure Handling

- Stop on invalid dates, missing curve points, incompatible dimensions, unavailable products, or incomplete contract terms.

## Gotchas

- Pricing and spread inversion have different required inputs; select the documented function from the requested result, not from a guessed curve convention.

## Reference Loading

- Load [the CDS function reference](references/matlab-functions.md) before coding a valuation call.
