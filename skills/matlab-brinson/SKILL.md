---
name: matlab-brinson
description: Writes, reviews, or repairs MATLAB Brinson-attribution code when MATLAB is explicitly requested or is the default language and brinson-workflow has supplied the implementation plan. Use directly when the AssetTable data contract and required functions are already fixed. It does not choose the benchmark, taxonomy, period or weight policy, attribution method, or any required materiality and interpretation policy.
---

# Implement Brinson Attribution in MATLAB

## Scope

Translate an approved Brinson implementation brief into correct MATLAB table construction and function calls, or repair code for explicitly selected Brinson operations. Do not perform benchmark, taxonomy, method, or interpretation decisions.

## Prerequisites

- MATLAB R2022b or later and Financial Toolbox for `brinsonAttribution`.
- A `brinson-workflow` MATLAB implementation brief, or a direct request with an approved AssetTable contract and selected functions.
- Ordered asset-period returns, categories, portfolio and benchmark weights, period convention, and required outputs.

## Capability Contract

### Required Inputs

- ordered asset-period key;
- decimal asset returns and exactly one category per key;
- portfolio and benchmark weights using the supplied timing convention;
- selected Brinson functions, outputs, and reconciliation tolerance.

### Conditional Inputs

- period prices when return conversion is selected;
- explicit cash/bond rows, category labels, and weights when required by the brief;
- chart requests and display labels when selected.

### Input Validation

- Check equal column lengths, unique asset-period keys, supported types, finite values, and the documented six-column order.
- Check period numbering, category coverage, asset order, and period weight sums against the supplied contract.
- Reject missing benchmark, taxonomy, or timing decisions rather than choosing them.

## Critical Rules

### Intent Preservation

- Preserve the approved benchmark, taxonomy, periods, weight timing, return convention, cash treatment, and operations.
- Do not normalize or impute silently; report constructor warnings and original values.
- Escalate domain ambiguity to `brinson-workflow` or the user.

### Data and Unit Conventions

- Keep one consistent asset-period ordering across names, returns, categories, and both weight columns.
- Preserve decimal-return, currency, period, and beginning/end-of-period conventions.
- When converting prices, keep time in rows and assets in columns before applying the selected return function.

### Execution Boundaries

- Consult [references/matlab-functions.md](references/matlab-functions.md) only for selected functions.
- Construct the documented table and capture warnings, object dimensions, properties, and output table shapes.
- Verify MATLAB-level coverage and numerical reconciliations; leave economic interpretation and any required approval to the workflow.

## Failure Handling

- Missing release/product: report the unavailable object and stop.
- Table type/shape/order failure: rebuild from the supplied asset-period key without changing domain inputs.
- Constructor normalization warning: preserve original sums and return the issue to the workflow; do not accept silently.
- Function/runtime failure: correct only the MATLAB signature or representation and retain the diagnostic.
- Missing benchmark/taxonomy/timing policy: return to `brinson-workflow` rather than inventing it.

## Gotchas

- `brinsonAttribution` accepts one table input.
- The table uses the documented six-column positional order.
- Price-to-return output orientation must match the asset-period flattening order.
- Do not transpose a table; orient vectors before table construction.
- Example-local helpers are not toolbox functions unless their source is present.
- Read [references/gotchas.md](references/gotchas.md) for function-specific failures.

## Reference Loading

- Read [references/matlab-functions.md](references/matlab-functions.md) for the selected Brinson or return function.
- Read [references/gotchas.md](references/gotchas.md) only for affected calls or diagnostics.
