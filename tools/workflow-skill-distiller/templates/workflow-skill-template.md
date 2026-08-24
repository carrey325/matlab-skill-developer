---
name: {{ skill_name }}
description: {{ description }}
---

# Purpose

{{ workflow.purpose }}

# Scope and Applicability

{{ workflow.scope }}

{{ workflow.trigger }}

{{ workflow.not_for }}

## Exclusions

{% for exclusion in workflow.exclusions %}- {{ exclusion }}
{% endfor %}

# Required Inputs

{% for item in inputs %}- {{ item.description }}
{% endfor %}

# Professional Workflow

Decision steps are complete only when the applied rule, supporting evidence, applicability, fallback consideration, and accountable owner are recorded. Implementation, assessment, and packaging steps must retain reproducible inputs, assumptions, outputs, diagnostics, and limitations.

{% if support_context %}The implementation, technical assessment, and packaging steps share the following context:

- Inputs: {{ support_context.inputs_text }}.
- Outputs: {{ support_context.outputs_text }}.

{% endif %}
{% for task in tasks %}## {{ task.title }}

{% if task.actions %}
- Work: {{ task.actions | join('; ') }}.
{% endif %}
{% if not task.shared_context | default(false) %}
- Inputs: {{ task.inputs_text }}.
- Outputs: {{ task.outputs_text }}.
{% endif %}

{% endfor %}# Decision Policy

Use the inputs below to frame each judgment. Read [decision rules](references/decision-rules.md) before choosing a route; that reference contains the conditions, rationale, applicability, exclusions, and missing-information behavior.

{% for decision in decision_summaries %}- **{{ decision.title }}.** Consider {{ decision.inputs }}. If the evidence is missing or contradictory: {{ decision.fallback }}
{% endfor %}

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

{% for gate in validation_gates %}- **{{ gate.title }}.** Assess: {{ gate.assessment_text }}. {{ gate.acceptance_policy }}
{% endfor %}

# Failure and Recovery

{% for item in recoveries %}- {{ item }}
{% endfor %}

# Stop / Escalation Conditions

{% for item in stop_conditions %}- {{ item }}
{% endfor %}

# Deliverables

{% for item in outputs %}- {{ item.description }}
{% endfor %}

# Workflow-Owned Professional Reasoning

These responsibilities stay with the workflow even when implementation is delegated:

{% for item in reasoning_capabilities %}- {{ item }}
{% endfor %}

# Delegated / Implementation Capabilities

Delegate these only after the professional specification and acceptance policy are fixed. A tool's availability never establishes appropriateness.

{% for item in delegated_capabilities %}- {{ item }}
{% endfor %}

# Reference Loading

{% for reference in references %}- Read [{{ reference.title }}]({{ reference.path }}) when {{ reference.when }}.
{% endfor %}

# Final Quality Checks

- Confirm purpose, definitions, applicability, material assumptions, and acceptance policy are explicit.
- Confirm every material selection records the applied rule and evidence-based rationale.
- Confirm validation distinguishes relevant performance, calibration or reconciliation, stability, sensitivity, assumptions, and limitations.
- Confirm developer testing is not represented as organizationally independent validation or regulatory approval.
- Escalate rather than inventing missing material information.
