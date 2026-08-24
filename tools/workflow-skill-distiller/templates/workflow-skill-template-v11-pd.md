---
name: {{ skill_name }}
description: {{ description }}
---

# Purpose

{{ workflow.purpose }}

# Scope and Applicability

{{ workflow.scope }}

Use this workflow when {{ workflow.trigger }} Do not use it when {{ workflow.not_for }}

## Exclusions

{% for exclusion in workflow.exclusions %}- {{ exclusion }}
{% endfor %}

# Required Inputs

{% for item in inputs %}- {{ item.name }}: {{ item.description }}
{% endfor %}

# Professional Workflow

{% for task in tasks %}## {{ task.title }}

{{ task.objective }}

- Assess or perform: {{ task.actions | join('; ') }}.
- Required inputs: {{ task.inputs | join(', ') }}.
- Produce: {{ task.outputs | join(', ') }}.
{% if task.completion %}- Complete only when: {{ task.completion | join('; ') }}.
{% endif %}{% if task.decisions %}- Apply these professional decisions: {{ task.decisions | join(', ') }}.
{% endif %}

{% endfor %}# Decision Policy

Use the concise policies below and load [decision rules](references/decision-rules.md) for conditions, rationale, applicability, exclusions, and missing-information behavior.

{% for decision in decisions %}- {{ decision.title }}: {{ decision.purpose }} Fallback: {{ decision.fallback.instruction }}
{% endfor %}

# Validation and Acceptance Criteria

Use risk-based acceptance. A completed calculation is not evidence of acceptability.

{% for gate in validation_gates %}- {{ gate.title }}: assess {{ gate.assessment_dimensions | join(', ') }}. {{ gate.acceptance_policy }}
{% endfor %}

# Failure and Recovery

{% for item in recoveries %}- {{ item }}
{% endfor %}

# Stop / Escalation Conditions

{% for item in stop_conditions %}- {{ item }}
{% endfor %}

# Deliverables

{% for item in outputs %}- {{ item.name }}: {{ item.description }}
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
