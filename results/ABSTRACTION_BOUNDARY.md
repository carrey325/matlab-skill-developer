# Capability Family Abstraction Boundary

Updated: 2026-08-21

## Family Structure

```text
<capability>-workflow/   domain reasoning and implementation selection
matlab-<capability>/     MATLAB coding and runtime correctness
python-<capability>/     optional future peer
r-<capability>/          optional future peer
```

This is not a paired API suite. The workflow is the capability's professional layer; language skills are replaceable implementations.

## Ownership

| Concern | Workflow | MATLAB implementation |
|---|---:|---:|
| Detailed when-to-use / when-not-to-use | yes | no |
| Purpose, method, benchmark, conventions, and professionally relevant governance | yes | no |
| Method-to-object and operation-to-function selection | yes | no |
| Implementation brief and required acceptance criteria | yes | consume only |
| MATLAB environment, product, and release requirements | no | yes |
| Exact signatures, types, shapes, patterns, diagnostics | no | yes |
| Runtime coding failures and function gotchas | no | yes |
| Professional interpretation and approval when relevant | yes | no |

The workflow's visible stages follow the capability's natural professional sequence. Readiness, implementation selection, construction/configuration, execution, and verification are development completeness concerns rather than mandatory headings.

## Granularity Review

The three current boundaries remain coherent after review; this assessment is development evidence and is not copied into the generated skills.

| Capability | Stable contract | Reconsider or split when |
|---|---|---|
| Portfolio optimization | mandate and inputs to a selected allocation solution and implementation brief | estimation-only, optimization-only, or trade-construction requests develop materially different triggers, inputs, acceptance criteria, or dependencies |
| Portfolio backtesting | research hypothesis and point-in-time data to a reproducible simulated evidence package | custom execution/accounting engines or research-design-only work require distinct state, validation, and implementation dependencies |
| Brinson attribution | benchmark/category/period policy and aligned holdings data to reconciled attribution effects | factor, fixed-income, transaction, residual, or reporting-only attribution introduces a different model contract or acceptance logic |

## Current Families

| Capability | Workflow | MATLAB implementation |
|---|---|---|
| Portfolio optimization | `portfolio-workflow` | `matlab-portfolio` |
| Portfolio backtesting | `backtest-workflow` | `matlab-backtest` |
| Brinson attribution | `brinson-workflow` | `matlab-brinson` |

The former `matlab-portfolio-api`, `matlab-backtest-api`, and `matlab-brinson-api` drafts were removed from `matlab-skill/`. Their useful content was split between the workflow and MATLAB layers; the original historical project files remain untouched.
