# Validation Guidance

Developer testing supports selection and packaging but does not replace organizationally independent validation where that is required.

## Discrimination and ranking gate

Determine whether ranking performance is adequate and stable for the intended decision use.

Required evidence: held-out ranking metrics, segment results, uncertainty or sampling context, benchmark comparison.
Assess: out-of-sample ranking, segment consistency, temporal variation, benchmark improvement, material bias.
Policy: Use predeclared, use-specific thresholds; do not treat a statistically nonzero score or in-sample fit as acceptance.

- Pass: All applicable dimensions meet documented risk-based thresholds and no material contradictory evidence remains. Route: continue to the next validation dimension
- Pass With Limitation: Residual weakness is bounded, non-material for the stated use, documented, and assigned a monitoring or approval condition. Route: continue while carrying the explicit limitation
- Remediate: A material but correctable weakness has a credible diagnostic and remediation path. Route: return to diagnosis, repair, recalibration, or respecification
- Reject: Evidence is absent, contradictory, outside appetite, or not remediable within scope. Route: stop and escalate or reject the candidate

## Calibration and horizon gate

Determine whether PD levels match the selected target and horizon semantics across relevant periods and segments.

Required evidence: calibration target, observed-versus-estimated results, horizon profile, segment and period results, probability-bound and survival/cumulative reconciliation checks.
Assess: target alignment, level bias, PD bounds, conditional-to-cumulative consistency, nondecreasing cumulative default probability where mathematically applicable, horizon shape, segment concentration, uncertainty and event scarcity.
Policy: Apply thresholds and remediation actions defined before seeing final results; diagnose target, semantics, or segmentation mismatch before recalibration.

- Pass: All applicable dimensions meet documented risk-based thresholds and no material contradictory evidence remains. Route: continue to the next validation dimension
- Pass With Limitation: Residual weakness is bounded, non-material for the stated use, documented, and assigned a monitoring or approval condition. Route: continue while carrying the explicit limitation
- Remediate: A material but correctable weakness has a credible diagnostic and remediation path. Route: return to diagnosis, repair, recalibration, or respecification
- Reject: Evidence is absent, contradictory, outside appetite, or not remediable within scope. Route: stop and escalate or reject the candidate

## Stability, assumptions, and sensitivity gate

Determine whether performance, relationships, assumptions, and sensitivity remain credible for intended conditions.

Required evidence: out-of-time results, segment drift, assumption diagnostics, scenario or perturbation sensitivity, known limitations.
Assess: performance stability, population and feature drift, assumption validity, economic sensitivity, override behavior, limitation materiality.
Policy: Require diagnostics proportional to risk; a limitation may pass only when bounded, governed, and monitored, otherwise remediate or reject.

- Pass: All applicable dimensions meet documented risk-based thresholds and no material contradictory evidence remains. Route: continue to the next validation dimension
- Pass With Limitation: Residual weakness is bounded, non-material for the stated use, documented, and assigned a monitoring or approval condition. Route: continue while carrying the explicit limitation
- Remediate: A material but correctable weakness has a credible diagnostic and remediation path. Route: return to diagnosis, repair, recalibration, or respecification
- Reject: Evidence is absent, contradictory, outside appetite, or not remediable within scope. Route: stop and escalate or reject the candidate
