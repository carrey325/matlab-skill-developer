---
name: matlab-lifetime-ecl
description: Implement selected lifetime expected credit loss aggregation with portfolioECL in MATLAB without choosing PD, LGD, EAD, discounting, or accounting policy.
---

# Implement Lifetime ECL in MATLAB

## Scope

Implement, review, or repair `portfolioECL` code after the PD, LGD, EAD, discounting, aggregation, and reporting conventions are selected.

Do not select component models, macroeconomic scenarios, accounting treatment, discounting policy, or provisioning decisions.

## Prerequisites

- MATLAB R2026a and Risk Management Toolbox.
- A complete selected ECL implementation contract covering compatible PD, LGD, EAD, time, discounting, and aggregation inputs.

## Capability Contract

### Required Inputs

- Inputs conforming to the selected `portfolioECL` syntax, with explicit time and portfolio alignment.

### Conditional Inputs

- Discounting, scenario, individual/portfolio aggregation, and output controls when selected by the contract.

### Input Validation

- Validate dimensions across PD, LGD, and EAD; probability and loss/exposure domains; horizon alignment; and discounting inputs.

## Critical Rules

### Intent Preservation

- Aggregate the supplied components without replacing their models or assumptions.

### Data and Unit Conventions

- Keep probability, loss, exposure, currency, time-step, and discount-rate units explicit and compatible.

### Execution Boundaries

- Build or repair individual components with `$matlab-lifetime-pd-models`, `$matlab-lgd-models`, and `$matlab-ead-models`.

## Failure Handling

- Stop on incompatible dimensions, invalid domains, missing time/discount definitions, or incomplete ECL methodology.

## Gotchas

- `portfolioECL` is shared across PD, LGD, and EAD categories but is maintained here once to prevent diverging aggregation guidance.
- In table inputs, every non-ID column is a scenario value column; remove calendar metadata unless the selected value-table contract explicitly includes it.

## Reference Loading

- Load [evaluation findings](references/evaluation-findings.md) only for Cox-PD/ECL regression repair.
- Load [verified ECL gotchas](references/gotchas.md) before assembling table-form `portfolioECL` inputs.
- Load [the ECL function reference](references/matlab-functions.md) before implementing the selected aggregation.
