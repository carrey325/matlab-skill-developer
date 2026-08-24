# Evaluation findings

Scenario 02 mirror index. Lifetime-PD owns failures before aggregation; lifetime-ECL owns the r4 `portfolioECL` table-shape failure. Detailed run records remain in the suite evaluation directory.

| Condition | Result | Canonical evidence |
|---|---|---|
| no-skill | failed before ECL | `02-cox-pd-and-ecl/runs/no-skill` |
| r0 | failed before ECL | `02-cox-pd-and-ecl/runs/r0-baseline` |
| r1 | failed before ECL | `02-cox-pd-and-ecl/runs/r1` |
| r2 | failed before ECL | `02-cox-pd-and-ecl/runs/r2` |
| r3 | failed before ECL | `02-cox-pd-and-ecl/runs/r3` |
| r4 | failed in ECL | Long annual table exposed `Year` as a PD value column; canonical F004. |
| r5 | passed, gated `1.0` | `02-cox-pd-and-ecl/runs/r5`; independent Cox/ECL assertions in `ground-truth/assert_run.m`, canonical snapshot `716ad17362280087538bf8ef5e9ab44af64a47f24d3f2676e1b6e8cc3683154a`. |
| final-regression | failed before load | sampling-specific parent-directory fixture resolution; lifetime-PD canonical finding owns retry evidence. |
| final-regression-r2 | no script generated | sampling-specific snapshot path-resolution request; lifetime-PD canonical finding owns retry evidence. |
| final-regression-r3 | passed, gated `1.0` | fresh merged-skill agent; canonical evidence `02-cox-pd-and-ecl/runs/final-regression-r3`. |
