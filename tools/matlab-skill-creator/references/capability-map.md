# Capability Map

Use only rows relevant to the requested capability. The workflow column owns domain reasoning; the MATLAB column owns implementation mechanics after selection.

| Capability | Workflow focus | MATLAB implementation focus | Common low-freedom controls when relevant |
|---|---|---|---|
| Portfolio optimization | mandate, objective, benchmark role, constraints, estimation policy, approval | portfolio objects/functions, signatures, bounds, solver diagnostics, frontiers | unit alignment, feasibility, solver status, constraint reconciliation |
| Risk measurement | valuation scope, horizon, confidence, aggregation, limits | VaR/ES functions, covariance/simulation calls, shapes, diagnostics | sign conventions, time alignment, aggregation, coverage tests |
| Backtesting | hypothesis, universe, sampling, benchmark, costs, OOS policy, evaluation | timetables, callbacks, schedules, engine calls, result properties | point-in-time data, no look-ahead, corporate actions, deterministic costs |
| Scenario and stress testing | scenario governance, plausibility, transmission, action | shock/revaluation functions, simulation calls, aggregation mechanics | scenario provenance, base-date consistency, complete position coverage |
| Pricing and valuation | contract terms, market data, model selection, calibration policy, controls | instrument/model functions, curves, solver calls, Greeks | conventions, calibration residuals, independent benchmarks |
| Performance attribution | hierarchy, benchmark, cash flows, linking policy, interpretation | attribution objects/functions, table construction, output properties | reconciliation to total return, currency and period linking |
| Data preparation | source contract, lineage, quality policy, calendars | import, timetable alignment, missing-data functions, corporate-action mechanics | timezone/calendar normalization, identifier integrity, no silent imputation |
| Reporting | audience, materiality, approvals, disclosures | table/chart/export functions and reproducible rendering | totals reconciliation, provenance, frozen run metadata |

## Standard Resource Package

Create only resources that the skill directly loads:

- Workflow: `domain-controls.md`, `methods.md`, `conventions.md`, or `reporting.md`.
- MATLAB: `matlab-functions.md`, `gotchas.md`, or deterministic MATLAB scripts.
- Shared evaluation metadata may live outside either skill when the harness supports a family-level location.

Do not put domain controls in MATLAB references or MATLAB signatures in workflow references.

The final column is a prompt for professional judgment, not a requirement to add every listed control or a dedicated control section.
