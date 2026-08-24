# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Set risk-based validation scope

Use observable evidence to set risk-based validation scope without preselecting the result.

### Inputs

- model materiality and change (required): Model use, exposure, complexity, change magnitude, prior findings, and potential harm.

### Rules

#### Full Scope Validation

- Conditions: model materiality and change equals new or materially changed high-impact model.
- Rationale: Material new or changed models require conceptual, data, implementation, outcomes, governance, and use review.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for model use, exposure, complexity, change magnitude, prior findings, and potential harm.; do not infer full-scope-validation from provider availability.

#### Targeted Validation

- Conditions: model materiality and change equals limited change with current prior validation.
- Rationale: A targeted review is acceptable only when unchanged areas remain supported and the rationale is documented.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for model use, exposure, complexity, change magnitude, prior findings, and potential harm.; do not infer targeted-validation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to set risk-based validation scope.

## Determine validator independence

Use observable evidence to determine validator independence without preselecting the result.

### Inputs

- validation governance evidence (required): Reporting line, development involvement, incentives, authority, competence, and access to evidence.

### Rules

#### Independent Validation

- Conditions: validation governance evidence equals validator independent with effective challenge authority.
- Rationale: Independent personnel must have competence, evidence access, and authority to challenge model owners.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for reporting line, development involvement, incentives, authority, competence, and access to evidence.; do not infer independent-validation from provider availability.

#### Independence Defect

- Conditions: validation governance evidence equals validator designed or owns material model components.
- Rationale: Material development responsibility prevents the work from being represented as independent validation.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for reporting line, development involvement, incentives, authority, competence, and access to evidence.; do not infer independence-defect from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine validator independence.

## Assess conceptual soundness

Use observable evidence to assess conceptual soundness without preselecting the result.

### Inputs

- conceptual evidence (required): Purpose alignment, theory, assumptions, variable logic, segmentation, horizon, and alternatives.

### Rules

#### Conceptually Supported

- Conditions: conceptual evidence equals design and assumptions align with intended use.
- Rationale: Conceptual support requires a coherent link from use and data-generating process to model design and assumptions.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for purpose alignment, theory, assumptions, variable logic, segmentation, horizon, and alternatives.; do not infer conceptually-supported from provider availability.

#### Conceptual Remediation

- Conditions: conceptual evidence equals material assumption or use mismatch.
- Rationale: A material design/use mismatch requires remediation regardless of development fit.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for purpose alignment, theory, assumptions, variable logic, segmentation, horizon, and alternatives.; do not infer conceptual-remediation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess conceptual soundness.

## Verify data and implementation

Use observable evidence to verify data and implementation without preselecting the result.

### Inputs

- reproduction and lineage results (required): Independent data lineage checks, code reproduction, transformations, parameter version, and output reconciliation.

### Rules

#### Implementation Verified

- Conditions: reproduction and lineage results equals independent reproduction matches controlled tolerances.
- Rationale: Validation should reproduce material outputs from controlled inputs and confirm the implemented specification.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for independent data lineage checks, code reproduction, transformations, parameter version, and output reconciliation.; do not infer implementation-verified from provider availability.

#### Implementation Finding

- Conditions: reproduction and lineage results equals material unexplained output difference.
- Rationale: Unexplained differences are implementation defects and cannot be waived by conceptual review.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for independent data lineage checks, code reproduction, transformations, parameter version, and output reconciliation.; do not infer implementation-finding from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to verify data and implementation.

## Select benchmark and challenger evidence

Use observable evidence to select benchmark and challenger evidence without preselecting the result.

### Inputs

- alternative model feasibility (required): Materiality, available data, model complexity, accepted practice, and prior benchmarks.

### Rules

#### Quantitative Benchmark

- Conditions: alternative model feasibility equals credible independent alternative can be constructed.
- Rationale: An independent benchmark tests whether complexity and model choices materially improve decision-relevant performance.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for materiality, available data, model complexity, accepted practice, and prior benchmarks.; do not infer quantitative-benchmark from provider availability.

#### Qualitative Benchmark With Limitation

- Conditions: alternative model feasibility equals quantitative benchmark infeasible with evidence.
- Rationale: If a benchmark cannot be built, validation must document why and strengthen sensitivity and limitations review.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for materiality, available data, model complexity, accepted practice, and prior benchmarks.; do not infer qualitative-benchmark-with-limitation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select benchmark and challenger evidence.

## Judge outcomes and stability

Use observable evidence to judge outcomes and stability without preselecting the result.

### Inputs

- outcomes analysis (required): Calibration, discrimination, segment results, time stability, overrides, use tests, and backtesting as applicable.

### Rules

#### Outcomes Supported

- Conditions: outcomes analysis equals multiple outcome dimensions support intended use.
- Rationale: No single statistic establishes validity; outcomes must be assessed across calibration, ranking, stability, and relevant segments.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for calibration, discrimination, segment results, time stability, overrides, use tests, and backtesting as applicable.; do not infer outcomes-supported from provider availability.

#### Outcomes Remediation

- Conditions: outcomes analysis equals material deterioration or segment failure.
- Rationale: Material deterioration or concentrated failure requires remediation even when an aggregate metric passes.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for calibration, discrimination, segment results, time stability, overrides, use tests, and backtesting as applicable.; do not infer outcomes-remediation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to judge outcomes and stability.

## Classify limitations and compensating controls

Use observable evidence to classify limitations and compensating controls without preselecting the result.

### Inputs

- limitation materiality (required): Impact, likelihood, detectability, affected use, available controls, and remediation time.

### Rules

#### Validation Limitation

- Conditions: limitation materiality equals bounded impact with enforceable controls.
- Rationale: A limitation may be accepted only when use boundaries, controls, ownership, and remediation are enforceable.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for impact, likelihood, detectability, affected use, available controls, and remediation time.; do not infer validation-limitation from provider availability.

#### Validation Blocker

- Conditions: limitation materiality equals unbounded or uncontrolled material impact.
- Rationale: A material uncontrolled limitation blocks use or requires immediate escalation.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for impact, likelihood, detectability, affected use, available controls, and remediation time.; do not infer validation-blocker from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to classify limitations and compensating controls.

## Issue independent validation disposition

Use observable evidence to issue independent validation disposition without preselecting the result.

### Inputs

- combined validation findings (required): Severity and interaction of conceptual, implementation, outcomes, governance, and limitation findings.

### Rules

#### Pass Validation

- Conditions: combined validation findings equals no material unresolved finding.
- Rationale: PASS requires sufficient evidence across all applicable validation components and does not erase minor observations.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for severity and interaction of conceptual, implementation, outcomes, governance, and limitation findings.; do not infer pass-validation from provider availability.

#### Remediate Or Pass With Limitation

- Conditions: combined validation findings equals material finding with feasible controlled remediation.
- Rationale: Controlled limitations or remediation may be appropriate only with explicit authority, timing, and use restrictions.
- Applies to: Formal validation of PD, LGD, EAD, scorecard, default, ECL-parameter, or portfolio credit-risk models by personnel with sufficient organizational independence..
- Excludes: model development, developer self-testing.
- If information is missing: Stop this decision and obtain evidence for severity and interaction of conceptual, implementation, outcomes, governance, and limitation findings.; do not infer remediate-or-pass-with-limitation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to issue independent validation disposition.
