# MathWorks Example Replayer

Convert each selected real example into a provenance-bearing trace with source ID, title, URL, exact section or anchor, input summary, expected output summary, mapped process nodes, expected material decisions and rule IDs, validation-gate outcomes, recovery or stop expectations, deliverables, and adjacent handoff.

Synthetic adversarial traces must set source provenance to null and state that they test behavior rather than reproduce a source. Node visitation alone does not count as professional decision coverage. Verify each expected rule and outcome exists in the IR and that each gate outcome is valid.

Return `REGRANULARIZE` when required professional actions cannot be represented, and `RESYNTHESIZE` when an applicable path is absent.
