# Decision Rules

Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.

## Select monitoring population and baseline

Use observable evidence to select monitoring population and baseline without preselecting the result.

### Inputs

- approved use and data comparability (required): Approved population, current use, reference period, outcome maturity, and data-definition continuity.

### Rules

#### Comparable Monitoring Window

- Conditions: approved use and data comparability equals current use and definitions match approval.
- Rationale: Monitoring comparisons are meaningful when current population, definitions, and outcome maturity match the approved use.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for approved population, current use, reference period, outcome maturity, and data-definition continuity.; do not infer comparable-monitoring-window from provider availability.

#### Change Assessment Before Monitoring

- Conditions: approved use and data comparability equals material use or definition change.
- Rationale: A material change requires impact assessment; it must not be disguised as ordinary drift.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for approved population, current use, reference period, outcome maturity, and data-definition continuity.; do not infer change-assessment-before-monitoring from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select monitoring population and baseline.

## Apply institution-approved threshold policy

Use observable evidence to apply institution-approved threshold policy without preselecting the result.

### Inputs

- approved monitoring policy (required): Metric definitions, amber/red criteria, observation requirements, aggregation rules, and authority.

### Rules

#### Apply Policy Thresholds

- Conditions: approved monitoring policy equals threshold policy approved and applicable.
- Rationale: Thresholds are policy inputs tied to use and sample adequacy; the workflow does not invent universal values.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for metric definitions, amber/red criteria, observation requirements, aggregation rules, and authority.; do not infer apply-policy-thresholds from provider availability.

#### Escalate Policy Gap

- Conditions: approved monitoring policy equals threshold missing stale or inapplicable.
- Rationale: A missing or stale threshold requires policy escalation rather than an improvised pass/fail rule.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for metric definitions, amber/red criteria, observation requirements, aggregation rules, and authority.; do not infer escalate-policy-gap from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to apply institution-approved threshold policy.

## Diagnose input and population drift

Use observable evidence to diagnose input and population drift without preselecting the result.

### Inputs

- distribution change evidence (required): Changes in population mix, predictors, missingness, data lineage, policy, and economic environment.

### Rules

#### Document External Drift

- Conditions: distribution change evidence equals change driven by explainable business or macro shift.
- Rationale: Explainable external drift still requires impact testing; it is not automatically a model defect.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for changes in population mix, predictors, missingness, data lineage, policy, and economic environment.; do not infer document-external-drift from provider availability.

#### Repair Data Or Implementation

- Conditions: distribution change evidence equals change driven by lineage or implementation break.
- Rationale: Data or implementation breaks require operational remediation before model performance is interpreted.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for changes in population mix, predictors, missingness, data lineage, policy, and economic environment.; do not infer repair-data-or-implementation from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to diagnose input and population drift.

## Diagnose calibration and discrimination change

Use observable evidence to diagnose calibration and discrimination change without preselecting the result.

### Inputs

- mature outcome evidence (required): Observed outcomes, expected outcomes, ranking metrics, segments, confidence, and time stability.

### Rules

#### Recalibration Candidate

- Conditions: mature outcome evidence equals ranking stable but calibration shifted.
- Rationale: Stable ranking with systematic level bias may support controlled recalibration after cause and representativeness are established.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for observed outcomes, expected outcomes, ranking metrics, segments, confidence, and time stability.; do not infer recalibration-candidate from provider availability.

#### Redevelopment Candidate

- Conditions: mature outcome evidence equals ranking or segment ordering materially degraded.
- Rationale: Material ranking deterioration indicates model relationship failure and normally requires redevelopment assessment.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for observed outcomes, expected outcomes, ranking metrics, segments, confidence, and time stability.; do not infer redevelopment-candidate from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to diagnose calibration and discrimination change.

## Assess overrides and use divergence

Use observable evidence to assess overrides and use divergence without preselecting the result.

### Inputs

- override and decision use record (required): Override rates, reasons, concentrations, approval patterns, downstream transformations, and unapproved uses.

### Rules

#### Retain With Override Monitoring

- Conditions: override and decision use record equals overrides controlled and outcome-improving.
- Rationale: Controlled overrides may continue when authority, rationale, concentration, and outcomes are monitored.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for override rates, reasons, concentrations, approval patterns, downstream transformations, and unapproved uses.; do not infer retain-with-override-monitoring from provider availability.

#### Escalate Use Risk

- Conditions: override and decision use record equals systematic overrides or unapproved use.
- Rationale: Systematic overrides or use outside approval indicate governance or model-use risk, not a calibration-only issue.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for override rates, reasons, concentrations, approval patterns, downstream transformations, and unapproved uses.; do not infer escalate-use-risk from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to assess overrides and use divergence.

## Classify remediation as recalibration or redevelopment

Use observable evidence to classify remediation as recalibration or redevelopment without preselecting the result.

### Inputs

- root cause and change scope (required): Whether weakness is level-only, relationship-level, data-definition, structural, or use-related.

### Rules

#### Controlled Recalibration

- Conditions: root cause and change scope equals level shift with stable structure and representative target.
- Rationale: Recalibration is appropriate only when structure remains valid and the new target is representative.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for whether weakness is level-only, relationship-level, data-definition, structural, or use-related.; do not infer controlled-recalibration from provider availability.

#### Redevelopment

- Conditions: root cause and change scope equals structural relationship or scope changed.
- Rationale: Structural or scope change requires redevelopment and validation, not relabelled recalibration.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for whether weakness is level-only, relationship-level, data-definition, structural, or use-related.; do not infer redevelopment from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to classify remediation as recalibration or redevelopment.

## Determine interim model-use status

Use observable evidence to determine interim model-use status without preselecting the result.

### Inputs

- finding materiality and controls (required): Impact, uncertainty, affected decisions, compensating controls, and remediation duration.

### Rules

#### Continue With Limitation

- Conditions: finding materiality and controls equals minor bounded issue with effective control.
- Rationale: Temporary continued use requires explicit scope, control, ownership, and expiry.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for impact, uncertainty, affected decisions, compensating controls, and remediation duration.; do not infer continue-with-limitation from provider availability.

#### Restrict Or Stop Use

- Conditions: finding materiality and controls equals material uncontrolled impact.
- Rationale: Material uncontrolled impact requires restriction or suspension rather than waiting for the next cycle.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for impact, uncertainty, affected decisions, compensating controls, and remediation duration.; do not infer restrict-or-stop-use from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to determine interim model-use status.

## Select final monitoring action

Use observable evidence to select final monitoring action without preselecting the result.

### Inputs

- combined monitoring evidence (required): Threshold results, root cause, materiality, control strength, prior breaches, and governance policy.

### Rules

#### Continue Use

- Conditions: combined monitoring evidence equals all applicable measures acceptable and no material change.
- Rationale: Continued use requires a complete monitoring record, not merely absence of a red metric.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for threshold results, root cause, materiality, control strength, prior breaches, and governance policy.; do not infer continue-use from provider availability.

#### Continue With Limitation

- Conditions: combined monitoring evidence equals bounded weakness controlled for a defined period.
- Rationale: Limited use requires a named control, scope, owner, expiry, and breach escalation.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for threshold results, root cause, materiality, control strength, prior breaches, and governance policy.; do not infer continue-with-limitation from provider availability.

#### Controlled Recalibration

- Conditions: combined monitoring evidence equals systematic level bias with stable rank and valid structure.
- Rationale: Recalibration is a governed change only when the structure and population remain valid.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for threshold results, root cause, materiality, control strength, prior breaches, and governance policy.; do not infer controlled-recalibration from provider availability.

#### Redevelop And Revalidate

- Conditions: combined monitoring evidence equals material relationship scope or data-generating process changed.
- Rationale: Structural deterioration requires redevelopment and validation rather than repeated level adjustment.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for threshold results, root cause, materiality, control strength, prior breaches, and governance policy.; do not infer redevelop-and-revalidate from provider availability.

#### Escalate Validation Or Owner Action

- Conditions: combined monitoring evidence equals material uncertainty uncontrolled use or repeated breach.
- Rationale: Repeated or material findings require validation, owner remediation, restriction, or governance escalation under policy.
- Applies to: Ongoing monitoring after approval for credit-risk models and their implemented data and use environment..
- Excludes: initial model development, independent validation.
- If information is missing: Stop this decision and obtain evidence for threshold results, root cause, materiality, control strength, prior breaches, and governance policy.; do not infer escalate-validation-or-owner-action from provider availability.

### Fallback

Outcome: stop and request evidence. Stop and request the missing or conflicting evidence needed to select final monitoring action.
