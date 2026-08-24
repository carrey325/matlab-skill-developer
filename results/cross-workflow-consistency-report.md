# Cross-Workflow Consistency Report

## Scope and result

All 17 released Workflow Skills were checked for terminology, responsibility, input/output handoffs, regime applicability, duplicated decision graphs, duplicated mandatory atoms, duplicated reviews, and provider-boundary leakage. No unresolved family-level conflict remains.

## Confirmed boundaries

- Lifetime PD, LGD, and EAD own parameter development; ECL consumes their governed outputs and never recreates their development logic.
- IFRS 9, CECL, and internal economic-loss uses are explicit ECL branches. IFRS 9 SICR/staging remains inside ECL only.
- Scorecard, lifetime PD, and broader default-model workflows have distinct targets and deliverables; deep and multinomial models remain candidate branches.
- Developer testing, independent validation, and post-approval monitoring are separate responsibilities. Monitoring explicitly selects continue, limited use, recalibrate, redevelop, or escalate.
- Portfolio risk owns EL/UL, concentration, contribution, and economic-capital outputs; stress testing owns scenario selection and macro-to-risk translation.
- Rating transitions, credit curves, structural default risk, and CDS valuation/implied-risk analysis have separate market inputs and decisions. CDS excludes trading and hedging decisions.
- VaR/ES estimation produces frozen forecasts. Backtesting independently aligns P&L, selects tests, diagnoses failures, and routes remediation.
- Climate scenario tools manipulate scenarios only. Climate-to-financial-risk translation, geospatial mapping, and uncertainty implementation remain explicit GAPs.

## Applicability invariants

- A source is shared only as immutable raw/normalized evidence; conclusions, atoms, decisions, and PASS reviews are workflow-specific.
- Cross-domain sources require an explicit dimension and rationale. Vendor/MathWorks evidence may support implementation or replay, never professional or regulatory authority.
- Downstream reuse preserves purpose, horizon, population, regime, calibration date, limitations, and accountable owner.
- Provider availability never selects purpose, policy, method, threshold, disposition, escalation, or approval.

## Regression evidence

- Cross-workflow decision-signature duplication: 0.
- Mandatory-atom overlap at or above the 50% rejection threshold: 0 pairs.
- Duplicated normalized review records among the 16 rebuilt workflows: 0.
- Provider or internal-IR leakage in released packages: 0 findings.
- Lifetime-PD v1.1 protected aggregate hash: unchanged.
