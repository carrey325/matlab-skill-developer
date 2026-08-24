# Freedom Matrix

## Decision rule

Score each operation separately. Choose the strictest level indicated by failure cost, sequencing sensitivity, and output reproducibility. Loosen it only when contextual judgment materially improves the result.

| Level | Use when | Target-skill form | Finance examples |
|---|---|---|---|
| High | Several methods are valid; context and user objectives dominate | Concise heuristics, alternatives, questions, decision criteria | Choose an optimizer family; select stress narratives; interpret attribution |
| Medium | A preferred pattern exists; parameters and datasets vary | Parameterized pseudocode, schemas, checklists, configurable scripts | Rolling-window backtest; covariance estimator configuration; scenario generation |
| Low | Errors are costly; ordering or consistency is critical | Tested script, fixed sequence, few validated parameters, fail-closed checks | Date alignment; P&L aggregation; risk-limit checks; constraint reconciliation |

## Escalation factors

Move toward lower freedom when any factor is present:

- production orders, limits, capital, regulatory reporting, or client reporting;
- silent numerical failure or convention mismatch;
- stateful or destructive MCP calls;
- path-dependent sequencing;
- exact reproducibility or audit requirements;
- sparse validation data or weak observability.

Move toward higher freedom when the task is exploratory, reversible, observable, and governed by explicit user choices.

## Required declaration

For each important target-skill operation, record:

```yaml
operation: estimate-covariance
freedom: medium
reason: estimator and regularization depend on sample size and mandate
guardrails:
  - require aligned total-return observations
  - report conditioning and missing-data treatment
implementation: parameterized pattern
```

Do not label a whole skill `high`, `medium`, or `low` without decomposing its fragile operations.
