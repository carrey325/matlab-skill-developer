# Evidence Policy

## Source Hierarchy

Use the strongest source for each layer:

1. Official MathWorks documentation, release notes, installed help, and official examples for MATLAB functions and toolbox behavior.
2. Primary regulatory, standards-body, exchange, or authoritative institutional sources for governed workflow rules.
3. Peer-reviewed or canonical technical literature for models and statistical methodology.
4. Reputable industry practice for professional workflow design.
5. Existing skills for structure and observed failure evidence after independent review.

## Evidence Placement

- Store domain-method and convention evidence, plus professionally relevant governance and control evidence, with the workflow skill.
- Store MATLAB function, object, signature, option, product, release, runtime, and gotcha evidence with `matlab-<capability>`.
- If one source supports both layers, create separate records describing the distinct claims rather than copying mixed guidance into both skills.

For each nontrivial claim record:

- claim or decision supported;
- source title and locator;
- publisher and access date;
- release/toolbox or rule effective date when relevant;
- executed, inspected, inherited, inferred, or unverified status;
- adaptation and limitations.

Never rely on search-result snippets. Paraphrase rather than copying long passages.

## MATLAB Verification Loop

1. Check installed release and licensed products when execution is available.
2. Inspect exact help or official documentation for signatures, types, options, defaults, and version history.
3. Build a minimal case only when testing is in scope.
4. Inspect warnings, solver/status outputs, dimensions, dates, units, and tolerances.
5. Add an independent invariant or benchmark where practical.
6. Record release-specific behavior in the MATLAB implementation skill or its reference.

If MATLAB cannot be executed or testing is out of scope, label code and claims accurately and do not claim runtime validation.

## Existing-Skill Adaptation

Inspect existing workflow and implementation skills separately. Do not inherit undocumented functions, stale behavior, hidden dependencies, example-specific constants, or domain assertions. Move each retained rule to the layer that owns it.
