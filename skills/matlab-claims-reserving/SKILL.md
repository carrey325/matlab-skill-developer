---
name: matlab-claims-reserving
description: Implement selected insurance claims reserving objects and calculations in MATLAB without choosing reserving methodology, actuarial assumptions, or reporting conclusions.
---

# Implement Claims Reserving in MATLAB

## Scope

Implement, review, or repair `developmentTriangle`, `chainLadder`, `expectedClaims`, `bornhuetterFerguson`, and `capeCod` operations after a reserving technique and conventions are selected.

Do not select the reserving method, development factors, expected-loss assumptions, materiality rule, or actuarial sign-off.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A selected reserving technique and a consistently defined development triangle.

## Capability Contract

### Required Inputs

- Triangle data, development/origin definitions, and the selected object/function operation.

### Conditional Inputs

- Expected claims, link-ratio, tail, and plotting/reporting settings only when the selected technique needs them.

### Input Validation

- Validate triangle orientation, cumulative/incremental convention, missing-cell treatment, and alignment with technique-specific assumptions.

## Critical Rules

### Intent Preservation

- Preserve the selected technique and triangle convention. Do not move data between methods or infer actuarial selections.

### Data and Unit Conventions

- Keep claim currency, origin/development periods, and cumulative versus incremental meaning explicit.

### Execution Boundaries

- Keep mortality/life-table modeling in `$matlab-life-table-modeling`.

## Failure Handling

- Stop on malformed triangles, invalid dates/period labels, unsupported technique inputs, or missing selected assumptions.

## Gotchas

- Similar result methods (`ibnr`, `unpaidClaims`, `ultimateClaims`, `summary`) belong to different reserving objects and require their own object state.

## Reference Loading

- Load [the claims reserving reference](references/matlab-functions.md) by object family before implementing a call.
