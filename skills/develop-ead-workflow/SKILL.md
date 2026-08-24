---
name: develop-ead-workflow
description: Develop and developer-test EAD or conversion-factor models with explicit exposure, product, horizon, limit, utilisation, boundary, calibration, and use decisions. Use when a model owner must estimate exposure at default from facility balances, limits, drawings, repayments, and product behaviour. Not for PD and LGD development, ECL aggregation, or credit-line management.
---

# Purpose

Develop and developer-test EAD or conversion-factor models with explicit exposure, product, horizon, limit, utilisation, boundary, calibration, and use decisions.

# Scope and Applicability

Professional EAD development for facilities and off-balance-sheet commitments under a declared prudential, accounting-support, or internal-risk purpose.

A model owner must estimate exposure at default from facility balances, limits, drawings, repayments, and product behaviour.

Do not use for PD or LGD development, ECL aggregation, limit management, production deployment, or independent approval.

## Exclusions

- PD and LGD development
- ECL aggregation
- credit-line management
- production deployment
- independent model approval

# Required Inputs

- Declared EAD use and exposure convention.
- Facility balance and limit history.
- Default timing, drawings, repayments, cancellations, and product terms.

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

The implementation, technical assessment, and packaging steps share the following context:

- Inputs: Declared EAD use and exposure convention, facility balance and limit history, default timing, drawings, repayments, cancellations, and product terms.
- Outputs: EAD definition and product segmentation, candidate and selected EAD or CCF model, boundary and calibration evidence, developer validation and monitoring design.

## Determine EAD purpose and exposure convention

- Inputs: Signed-off purpose, horizon, default linkage, and required exposure definition.
- Outputs: Decision record for determine EAD purpose and exposure convention.

## Define drawn and undrawn exposure components

- Inputs: Reconciled balances, limits, undrawn commitments, accrued amounts, and default dates.
- Outputs: Decision record for define drawn and undrawn exposure components.

## Choose product-specific EAD route

- Inputs: Whether the product permits additional drawings, cancellations, amortisation, or limit changes before default.
- Outputs: Decision record for choose product-specific EAD route.

## Determine whether CCF is a stable target

- Inputs: Availability and stability of undrawn amounts and realised pre-default drawings.
- Outputs: Decision record for determine whether CCF is a stable target.

## Select the pre-default observation horizon

- Inputs: Required forecast horizon and observed timing of material drawings before default.
- Outputs: Decision record for select the pre-default observation horizon.

## Treat limit changes and additional drawings

- Inputs: Evidence on authorised increases, temporary limits, cancellations, freezes, and borrower-initiated drawings.
- Outputs: Decision record for treat limit changes and additional drawings.

## Select EAD model family

- Inputs: Target type, repeated observations, boundary mass, sample size, and interpretability.
- Outputs: Decision record for select EAD model family.

## Control EAD and CCF boundary behaviour

- Inputs: Frequency and materiality of predictions below drawn balance or beyond supportable commitment assumptions.
- Outputs: Decision record for control EAD and CCF boundary behaviour.

## Determine EAD model disposition

- Inputs: Calibration by product and utilisation, stability, sensitivity, bounds, assumptions, and limitations.
- Outputs: Decision record for determine EAD model disposition.

## Execute the approved EAD computation

- Work: Run the approved computational specification without changing professional choices.

## Assess EAD technical evidence

- Work: Assess model or analysis evidence separately from final disposition.

## Package the EAD professional record

- Work: Package decisions, evidence, outputs, limitations, and handoffs.

# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

- **Determine EAD purpose and exposure convention.** Consider signed-off purpose, horizon, default linkage, and required exposure definition. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine EAD purpose and exposure convention.
- **Define drawn and undrawn exposure components.** Consider reconciled balances, limits, undrawn commitments, accrued amounts, and default dates. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to define drawn and undrawn exposure components.
- **Choose product-specific EAD route.** Consider whether the product permits additional drawings, cancellations, amortisation, or limit changes before default. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to choose product-specific EAD route.
- **Determine whether CCF is a stable target.** Consider availability and stability of undrawn amounts and realised pre-default drawings. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine whether CCF is a stable target.
- **Select the pre-default observation horizon.** Consider required forecast horizon and observed timing of material drawings before default. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select the pre-default observation horizon.
- **Treat limit changes and additional drawings.** Consider evidence on authorised increases, temporary limits, cancellations, freezes, and borrower-initiated drawings. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to treat limit changes and additional drawings.
- **Select EAD model family.** Consider target type, repeated observations, boundary mass, sample size, and interpretability. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to select EAD model family.
- **Control EAD and CCF boundary behaviour.** Consider frequency and materiality of predictions below drawn balance or beyond supportable commitment assumptions. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to control EAD and CCF boundary behaviour.
- **Determine EAD model disposition.** Consider calibration by product and utilisation, stability, sensitivity, bounds, assumptions, and limitations. If the evidence is missing or contradictory: Stop and request the missing or conflicting evidence needed to determine EAD model disposition.

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

- **EAD technical fitness.** Assess: define drawn and undrawn exposure components, choose product-specific EAD route, determine whether CCF is a stable target, select the pre-default observation horizon. Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.
- **EAD use and release boundary.** Assess: determine EAD purpose and exposure convention, determine EAD model disposition, provider and adjacent-workflow boundaries. Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.

# Failure and Recovery

- Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.

# Stop / Escalation Conditions

- Stop and escalate instead of producing a professional conclusion.

# Deliverables

- EAD definition and product segmentation.
- Candidate and selected EAD or CCF model.
- Boundary and calibration evidence.
- Developer validation and monitoring design.

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

- Decide applicability — Determine EAD purpose and exposure convention
- Decide exposure — Define drawn and undrawn exposure components
- Decide product — Choose product-specific EAD route
- Decide CCF — Determine whether CCF is a stable target
- Decide window — Select the pre-default observation horizon
- Decide limit — Treat limit changes and additional drawings
- Decide family — Select EAD model family
- Decide bounds — Control EAD and CCF boundary behaviour
- Decide disposition — Determine EAD model disposition
- Package EAD evidence — Package the EAD professional record

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

- Compute EAD analysis
- Compute EAD validation evidence

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
