---
name: workflow-skill-distiller
description: Distill authoritative professional evidence into auditable, agent-neutral workflow skills. Use when defining a bounded professional workflow, building its evidence corpus, extracting knowledge atoms, synthesizing a Workflow IR, reviewing it, or binding implementation capabilities. Do not use for direct provider-specific coding or to summarize a document without a workflow objective.
---

# Workflow Skill Distiller

Use the six-stage evidence-first pipeline: Task Contract, Acquire and Extract, Synthesize, Generate, Review and Rewrite, Capability and Granularity Harmonization.

Keep professional reasoning, generated workflow instructions, and implementation bindings separate. A workflow must remain meaningful without a particular agent runtime, programming language, or provider.

## Operating Rules

- Start from a bounded task contract and use `scripts/init_workflow.py` to create the standard workspace.
- Run source, atom, and Workflow IR validation before moving to the next stage.
- Validate `extraction/evidence-coverage.yaml`; a required current claim cannot rely only on historical or superseded material.
- Do not use a vendor example as the sole professional authority. Use examples for replay and regression only.
- Represent every material professional selection with structured inputs, conditions, rationale, applicability, exclusions, missing-information behavior, evidence, and fallback.
- Require risk-based gate outcomes (`PASS`, `PASS_WITH_LIMITATION`, `REMEDIATE`, `REJECT`); workflow completion alone is not acceptance evidence.
- Render skills only from a validated Workflow IR with `scripts/generate_skill.py`.
- Count replay coverage from explicit decision rules and gate outcomes, not from node visitation. Real replays require source provenance; synthetic cases must say they are synthetic.
- Treat a non-PASS review verdict as a routing instruction. `REGRANULARIZE` goes through Stage 5, then returns to Stage 2 before regeneration and review.
- Keep provider bindings in `alignment/`; generated `SKILL.md` packages must not mention implementation providers.
- Separate workflow-owned model specification from delegated model fitting and keep developer testing distinct from independent validation or approval.

## Role Guidance

Read only the role file needed for the active stage:

- [source scout](roles/source-scout.md) and [corpus normalizer](roles/corpus-normalizer.md) for Stage 1 acquisition.
- [knowledge extractor](roles/knowledge-extractor.md), [knowledge engineer](roles/knowledge-engineer.md), and [decision modeler](roles/decision-modeler.md) for extraction and synthesis.
- [skill writer](roles/skill-writer.md) for Stage 3.
- The reviewer and aligner role files for Stages 4 and 5.

## References

- Read [schema and artifact conventions](references/artifact-conventions.md) before creating or editing structured artifacts.
- Read [quality gates](references/quality-gates.md) before issuing a final verdict.
- Read [pilot boundary](references/develop-lifetime-pd-pilot.md) only for the first pilot.
