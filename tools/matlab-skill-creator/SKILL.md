---
name: matlab-skill-creator
description: Creates or updates capability workflow skills and MATLAB implementation skills for finance, quantitative investing, portfolio management, and risk management. Use when researching, structuring, testing, auditing, or iterating a capability family such as portfolio optimization, backtesting, attribution, risk measurement, scenarios, pricing, data preparation, or reporting. Do not use merely to execute an existing analysis or MATLAB task.
---

# Create MATLAB Finance and Risk Skills

## Preserve Development Boundaries

- Treat this skill's directory as the source of the development standard, not as the destination for generated capabilities.
- Create generated capability families in a separate user-selected development directory.
- Synchronize a requested skill to a discovery directory only when the user explicitly requests installation or pull.
- Before synchronization, validate the source, inspect the destination, report material overwrites or stale files, and preserve unrelated content.

## Determine Capability Granularity

Determine capability granularity before development. Prefer a capability that corresponds to a coherent professional task with a stable input-output contract.

Split a capability when its subproblems have materially different triggers, inputs, method-selection logic, acceptance criteria, or implementation dependencies. Keep work together when those elements are substantially shared and splitting would only create routing overhead or duplicate context.

Treat the initial boundary as a development hypothesis. Test it with representative positive, negative, narrow, and adjacent examples; then split, merge, or rename skills when observed routing, implementation-brief, or acceptance failures show that the boundary is wrong. Record this reasoning in the development contract or evaluation notes. Do not require a granularity discussion or a fixed number of child skills in the generated skill itself.

## Define a Capability Family

Do not model a capability as a fixed pair. Model it as one domain workflow with zero or more language implementations:

```text
<capability>-workflow/
matlab-<capability>/
python-<capability>/        # optional future implementation
r-<capability>/             # optional future implementation
```

The current standard develops the workflow and MATLAB members only. Python and R members are future peers, not children of the MATLAB skill.

### Workflow Ownership

The `<capability>-workflow` skill owns:

- detailed positive and negative triggers;
- professional purpose, users, outcomes, and domain reasoning;
- method selection and implementation selection;
- inputs, conventions, and business rules, plus controls, reconciliations, governance, acceptance, and reporting when professionally relevant;
- the capability's natural end-to-end professional sequence;
- the implementation brief handed to the selected language skill.

### MATLAB Ownership

The `matlab-<capability>` skill owns only:

- MATLAB, toolbox, release, MCP, and environment prerequisites;
- required and conditional coding inputs supplied by the user or workflow;
- exact MATLAB functions, objects, signatures, types, shapes, options, and release evidence;
- intent-preserving code construction, execution boundaries, runtime diagnostics, and verified gotchas.

Exclude domain reasoning, method selection, professional interpretation, governance, and end-to-end workflow from the MATLAB skill. It may reject an incomplete implementation brief, but it must not fill the gap by choosing the financial method.

### Trigger Boundary

- Put detailed `When to Use` and `When Not to Use` guidance in the workflow skill.
- Keep the MATLAB skill trigger simple: use it when the user requests or defaults to MATLAB implementation, or when the workflow has selected MATLAB and supplied an implementation brief.
- A direct code-only request may invoke `matlab-<capability>` without loading the workflow if the method, operations, and required inputs are already explicit.

## Follow the Development Sequence

Skip a stage only for a stated, concrete reason.

### 1. Research and Develop the Workflow Skill

1. Study user material, authoritative domain sources, industry practice, and relevant existing skills.
2. Define purpose, users, positive and negative scenarios, inputs, outputs, conventions, quality bar, professionally relevant governance scope, and realistic examples.
3. Map domain methods to supported implementation objects and domain operations to implementation functions without embedding code signatures.
4. Use preflight, implementation selection, construction/configuration, execution, and verification as five development concerns to check for completeness. Do not require them as visible headings or force them into five stages. Structure the generated workflow in the natural professional sequence of the capability, combining, renaming, reordering, or omitting visible stages when justified.
5. Make failure gates part of the responsible workflow stage instead of duplicating a generic failure section.
6. Complete [references/capability-contract.md](references/capability-contract.md). Read [references/capability-map.md](references/capability-map.md), [references/evidence-policy.md](references/evidence-policy.md), and [references/freedom-matrix.md](references/freedom-matrix.md) as needed.
7. Produce a language-neutral implementation brief plus the selected language, objects, operations, parameters, and acceptance checks.

### 2. Research and Develop the MATLAB Skill

1. Inspect installed MATLAB help when available, then official MathWorks documentation, release notes, examples, and relevant MATLAB Agentic Toolkit material.
2. For each function selected by the workflow, record product, release, exact signature, input types, output shapes, defaults, alternatives, and evidence state.
3. Organize guidance by MATLAB function or object, not by professional method categories.
4. Keep `Prerequisites` factual: identify only the environment, products, and information required to run the skill.
5. Define required inputs, conditional inputs, and input validation without recreating the professional workflow.
6. Encode intent preservation, data/unit conventions, execution boundaries, runtime failure handling, and verified gotchas.
7. Never encode an unverified function, option, signature, product, MCP method, default, or release guarantee. Label unexecuted code accurately.

### 3. Arrange the Family

1. Apply the two separate structures in [references/output-patterns.md](references/output-patterns.md).
2. Keep each `SKILL.md` short and route detailed evidence directly to one-level references.
3. Keep domain controls with the workflow and MATLAB function evidence with the MATLAB implementation.
4. Remove unused generated examples, assets, scripts, references, and empty directories.

### 4. Test and Iterate

1. Test workflow selection with positive and negative scenarios.
2. Test the proposed capability granularity with representative narrow, broad, and adjacent requests; split, merge, or rename the family when examples expose materially different contracts or routing behavior.
3. When requested and feasible, adapt official MathWorks examples into small synthetic MATLAB cases covering valid inputs, missing implementation inputs, numerical boundaries, misuse, and runtime failure.
4. Convert observed MATLAB errors into regression cases before changing function guidance.
5. Make the smallest change that fixes the responsible workflow, granularity, or MATLAB defect.
6. Rerun relevant validation and distinguish executed, inspected, inherited, and unverified evidence.

### 5. Reconcile and Complete

1. Verify that observed examples support the chosen capability boundary and number of skills.
2. Verify that all domain decisions exist only in the workflow and all MATLAB signatures exist only in the MATLAB skill or its references.
3. Verify that the workflow produces enough information for MATLAB implementation without the MATLAB skill choosing a method.
4. Run canonical `quick_validate.py` on every skill and `scripts/audit_skill_suite.py` on the workflow/MATLAB family members.
5. Report skipped tests, unavailable products, unexecuted code, and known limitations.

## Apply Target-Skill Standards

- Use imperative body instructions and only `name` and `description` in frontmatter.
- Name the domain skill `<capability>-workflow` and the MATLAB implementation `matlab-<capability>`; never add `-api`.
- Assign freedom per operation: contextual domain choices belong in the workflow; fragile language mechanics belong in tested implementation guidance or scripts.
- Make finance conventions explicit at the layer that owns them. The workflow chooses conventions; the MATLAB skill validates and preserves the supplied values.
- Require domain approval for organization-specific limits, regulatory interpretation, client reporting, or production trade actions.
- Read [references/skill-quality-standards.md](references/skill-quality-standards.md) for final quality review.

## Define Completion

Deliver only when representative examples support the chosen granularity, the workflow and MATLAB skill select correctly, the abstraction boundary is clean, the workflow produces a complete implementation brief, the MATLAB skill preserves that intent, evidence is release-scoped, validations pass, and development/install state is reported accurately.
