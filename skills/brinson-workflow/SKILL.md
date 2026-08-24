---
name: brinson-workflow
description: Plans or reviews Brinson performance attribution from benchmark, hierarchy, return and weight conventions through implementation selection, execution, reconciliation, and interpretation. Use when defining or reviewing allocation, selection, and interaction attribution across categories or periods. Do not use for a code-only AssetTable/function task, factor attribution, fixed-income attribution, or a benchmark-free performance review.
---

# Execute Brinson Attribution Workflow

## When to Use

- Decompose active return into allocation, selection, and interaction effects.
- Define benchmark, mutually exclusive category hierarchy, periods, return convention, and weight timing.
- Reconcile portfolio and benchmark performance to category attribution.
- Review multi-period Brinson results or prepare a stakeholder-facing interpretation.

## When Not to Use

- The benchmark, categories, periods, weights, returns, and MATLAB operations are already fixed; use `matlab-brinson` directly.
- The task requires factor, fixed-income, transaction-based, or other attribution not represented by the selected Brinson model.
- No valid benchmark or mutually exclusive category mapping can be established.

## Inputs and Conventions

Resolve portfolio and benchmark universes, asset identifiers, benchmark authority, category taxonomy and effective dates, equal-interval periods, beginning/end-of-period weight convention, return convention, currency treatment, cash and fees, missing holdings, corporate actions, multi-period linking, and any reporting policy required by the intended use.

Do not infer categories, benchmark weights, cash treatment, or materiality thresholds. Obtain approval for organization-specific taxonomy or reporting policy when those choices are part of the task.

## Implementation Selection

### Method-to-Object Map

| Attribution need | MATLAB implementation object | Boundary |
|---|---|---|
| Category-based allocation, selection, and interaction attribution | `brinsonAttribution` | Requires one category per asset, benchmark weights, comparable period returns, and supported linking semantics |
| Factor, fixed-income, transaction, or residual attribution | Outside this capability | Select a different workflow and implementation rather than forcing Brinson |

### Operation-to-Function Map

| Selected operation | MATLAB function family |
|---|---|
| Construct attribution model | `brinsonAttribution` |
| Compute total/category effects | `totalAttribution`, `categoryAttribution` |
| Inspect category returns/weights | `categoryReturns`, `categoryWeights` |
| Produce consolidated output | `summary` |
| Visualize effects/returns/weights | `attributionsChart`, `categoryReturnsChart`, `categoryWeightsChart` |

## Workflow

### Establish the Attribution Question and Policy

1. State the attribution question, audience, benchmark, and any approval owner required by the intended use.
2. Confirm that category-based allocation, selection, and interaction effects answer the question; route unsupported attribution types elsewhere.
3. Resolve category hierarchy, period and weight timing, return, currency, cash, linking, and any professionally relevant reporting or approval policy.
4. Stop if the benchmark or taxonomy is not fit for the question.

### Align and Reconcile the Attribution Data

1. Audit coverage, identifiers, category exclusivity, effective dates, periods, weight timing, returns, currency, cash, and fees.
2. Establish ordered asset-period keys and check that returns and weights refer to the same periods.
3. Stop when coverage, weight totals, categories, or period alignment cannot be reconciled sufficiently for attribution.

### Select Outputs and Prepare the Implementation

1. Choose single/multi-period scope, output levels, charts, and reconciliation tolerances.
2. Select the MATLAB object and functions from the maps above.
3. Create a brief containing ordered asset-period keys, returns, categories, portfolio/benchmark weights, period and weight timing, cash/currency treatment, selected operations, requested outputs, and reconciliation checks.
4. Hand the brief to `matlab-brinson` without embedding table-construction code or function signatures.

### Run, Reconcile, and Interpret the Attribution

1. Execute through the selected language implementation.
2. Preserve input coverage, normalization warnings, object properties, effect tables, and runtime evidence.
3. Return code/table failures to the language layer and benchmark/taxonomy/timing failures to the responsible workflow stage.
4. Reconcile portfolio and benchmark weight coverage by period, then reconcile portfolio return, benchmark return, active return, and total/category effects within stated tolerances.
5. Investigate residuals, missing holdings, cash, costs, currency, timing, and linking before interpretation.
6. Interpret signs and dominant contributors in context; do not infer manager skill or apply universal materiality thresholds.
7. Report limitations and approval state only when the intended use requires one.

## Output and Implementation Brief

Return the attribution question, benchmark/taxonomy policy, data and timing audit, selected implementation, MATLAB brief, execution evidence, reconciliation, contextual interpretation, and limitations. Include reporting or approval state only when professionally relevant.
