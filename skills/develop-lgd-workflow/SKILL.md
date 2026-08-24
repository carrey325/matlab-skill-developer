---
name: develop-lgd-workflow
description: Develop and developer-test an LGD model using explicit economic-loss, recovery, cure, censoring, downturn, segmentation, calibration, and use decisions. Use when a model owner must turn defaulted-exposure recovery experience into an LGD model package for a declared portfolio and use. Not for PD and EAD development, ECL aggregation, or production deployment.
---

# Purpose

Develop and developer-test an LGD model using explicit economic-loss, recovery, cure, censoring, downturn, segmentation, calibration, and use decisions.

# Scope and Applicability

Professional LGD development for prudential, accounting-support, or internal-risk uses while preserving purpose-specific loss definitions and downturn requirements.

A model owner must turn defaulted-exposure recovery experience into an LGD model package for a declared portfolio and use.

Do not use for PD or EAD development, ECL aggregation, production deployment, or organizationally independent validation.

## Exclusions

- PD and EAD development
- ECL aggregation
- production deployment
- independent model approval

# Required Inputs

- Intended LGD use and jurisdiction.
- Defaulted exposure and recovery cash-flow lineage.
- Collateral, cure, cost, timing, and macroeconomic information.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Intended LGD use and jurisdiction, defaulted exposure and recovery cash-flow lineage, collateral, cure, cost, timing, and macroeconomic information.
- Outputs: LGD definition and data contract, candidate and selected LGD model, calibration and limitation record, developer validation and monitoring design.

## Determine LGD purpose and loss concept

- Inputs: Signed-off prudential, accounting-support, or internal economic-loss purpose.
- Outputs: Decision record for determine LGD purpose and loss concept.

## Select workout or market LGD basis

- Inputs: Availability and reliability of post-default cash flows versus observable market prices.
- Outputs: Decision record for select workout or market LGD basis.

## Define recoveries, costs, and discounting

- Inputs: Evidence that recoveries, direct and indirect costs, dates, and discount-rate basis are complete.
- Outputs: Decision record for define recoveries, costs, and discounting.

## Determine cure and return-to-performing treatment

- Inputs: Observed cure definition, probation, re-default behaviour, and consistency with the default framework.
- Outputs: Decision record for determine cure and return-to-performing treatment.

## Treat incomplete recovery and censoring

- Inputs: Share and characteristics of unresolved defaults at the observation cutoff.
- Outputs: Decision record for treat incomplete recovery and censoring.

## Determine downturn calibration requirement

- Inputs: Governing purpose and evidence that recoveries or losses vary materially with adverse conditions.
- Outputs: Decision record for determine downturn calibration requirement.

## Select LGD segmentation

- Inputs: Differences in collateral, seniority, product, recovery process, jurisdiction, and cure behaviour.
- Outputs: Decision record for select LGD segmentation.

## Select LGD model family

- Inputs: Boundedness, mass points, censoring, cure mixture, sample size, and interpretability requirements.
- Outputs: Decision record for select LGD model family.

## Determine LGD model disposition

- Inputs: Calibration, ranking, stability, sensitivity, assumptions, and unresolved limitations assessed separately.
- Outputs: Decision record for determine LGD model disposition.

## Execute the approved LGD computation

- Work: Run the approved computational specification without changing professional choices.

## Assess LGD technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the LGD professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Determine LGD purpose and loss concept.** Consider signed-off prudential, accounting-support, or internal economic-loss purpose. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine LGD purpose and loss concept.
- **Select workout or market LGD basis.** Consider availability and reliability of post-default cash flows versus observable market prices. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select workout or market LGD basis.
- **Define recoveries, costs, and discounting.** Consider evidence that recoveries, direct and indirect costs, dates, and discount-rate basis are complete. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define recoveries, costs, and discounting.
- **Determine cure and return-to-performing treatment.** Consider observed cure definition, probation, re-default behaviour, and consistency with the default framework. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine cure and return-to-performing treatment.
- **Treat incomplete recovery and censoring.** Consider share and characteristics of unresolved defaults at the observation cutoff. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to treat incomplete recovery and censoring.
- **Determine downturn calibration requirement.** Consider governing purpose and evidence that recoveries or losses vary materially with adverse conditions. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine downturn calibration requirement.
- **Select LGD segmentation.** Consider differences in collateral, seniority, product, recovery process, jurisdiction, and cure behaviour. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select LGD segmentation.
- **Select LGD model family.** Consider boundedness, mass points, censoring, cure mixture, sample size, and interpretability requirements. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select LGD model family.
- **Determine LGD model disposition.** Consider calibration, ranking, stability, sensitivity, assumptions, and unresolved limitations assessed separately. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine LGD model disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **LGD technical fitness.** Assess: select workout or market LGD basis, define recoveries, costs, and discounting, determine cure and return-to-performing treatment, treat incomplete recovery and censoring. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **LGD use and release boundary.** Assess: determine LGD purpose and loss concept, determine LGD model disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- LGD definition and data contract.
- Candidate and selected LGD model.
- Calibration and limitation record.
- Developer validation and monitoring design.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide applicability — Determine LGD purpose and loss concept
- Decide basis — Select workout or market LGD basis
- Decide cashflow — Define recoveries, costs, and discounting
- Decide cure — Determine cure and return-to-performing treatment
- Decide window — Treat incomplete recovery and censoring
- Decide downturn — Determine downturn calibration requirement
- Decide segment — Select LGD segmentation
- Decide family — Select LGD model family
- Decide disposition — Determine LGD model disposition
- Package LGD evidence — Package the LGD professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute LGD analysis
- Compute LGD validation evidence

# Reference Loading

- Read [regulatory evidence](references/regulatory-evidence.md) when checking the authority, locator, applicability, or interpretation of a material claim.
- Read [decision rules](references/decision-rules.md) when making a professional decision or applying its fallback.
- Read [validation guidance](references/validation-guidance.md) when planning or evaluating validation, acceptance, and recovery.

# Final Quality Checks

- Confirm purpose, definitions, applicability, material assumptions, and acceptance policy are explicit.
- Confirm every material selection records the applied rule and evidence-based rationale.
- Confirm validation distinguishes relevant performance, calibration or reconciliation, stability, sensitivity, assumptions, and limitations.
- Confirm developer testing is not represented as organizationally independent validation or regulatory approval.
- Escalate rather than inventing missing material information.
