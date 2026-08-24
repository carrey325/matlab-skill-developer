# MATLAB Skill Developer

MATLAB Skill Developer is a publication-focused collection of production-ready skills, reusable skill-development components, and auditable release results. It contains no development workspaces, temporary artifacts, raw evidence files, or historical rebuild material.

## Published Results

- **41 complete skill packages:** 21 MATLAB implementation skills, 17 professional risk workflow skills, and 3 investment-analysis workflow skills.
- **17 professional risk workflows:** credit model development, independent validation and monitoring, expected credit loss, portfolio risk and stress testing, rating transitions, credit curves, structural default risk, CDS analysis, VaR/ES, and climate risk.
- **2 reusable toolkits:** `matlab-skill-creator` for consistent MATLAB skill authoring and audit, and `workflow-skill-distiller` for evidence-driven workflow synthesis, validation, generation, and release.
- **Traceable release results:** the workflow registry, capability mappings, MATLAB capability gaps, evidence indexes, and cross-workflow consistency reports.

## Repository Contents

| Directory | Contents |
|---|---|
| [`skills/`](skills/) | 41 self-contained skill packages, each with a `SKILL.md` entry point. |
| [`tools/matlab-skill-creator/`](tools/matlab-skill-creator/) | Core instructions, policies, scripts, and references for MATLAB Skill Creator. |
| [`tools/workflow-skill-distiller/`](tools/workflow-skill-distiller/) | Schemas, roles, templates, validators, generators, and release components for the six-stage Workflow Distiller. |
| [`results/`](results/) | The release registry, reports, evidence indexes, capability mappings, and GAP register. |

## Delivered Capabilities

MATLAB implementation skills perform calculations, modeling, testing, and result generation. Workflow skills own professional scope, evidence applicability, expert decisions, acceptance criteria, failure handling, escalation, and deliverables. This separation prevents implementation tools from replacing professional judgment.

The released risk workflow family contains **431 traceable knowledge atoms, 142 professional decisions, 299 decision rules, and 37 real example replays**. Its evidence index covers **66 sources from 14 organizations**. All 17 release packages pass the release validator, and all **27 automated tests pass**. Provider/MATLAB leakage and internal IR identifier leakage in final workflow skills are both zero.

## Quality and Scope

- Final workflow skills are runtime-neutral; implementation bindings and capability gaps are reported separately.
- Professional leaves use `EXACT`, `COMPOSITION`, `NO_PROVIDER_REQUIRED`, or `GAP` to state implementation coverage explicitly.
- Lifetime PD v1.1 remains the benchmark package; every other professional workflow has its own evidence, decisions, examples, and reviews.
- This publication excludes development workspaces, audit snapshots, virtual environments, caches, raw or normalized evidence corpora, performance experiments, and rejected builds.
- Runtime installation and external provider bindings are outside this repository's scope.

See the [`skills/` catalog](skills/README.md), the formal [`workflow registry`](results/workflow-registry.yaml), and the [`cross-workflow consistency report`](results/cross-workflow-consistency-report.md) for the complete release inventory.

