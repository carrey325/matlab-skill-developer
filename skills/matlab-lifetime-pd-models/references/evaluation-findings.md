# Evaluation findings

Development-only evidence from isolated `gpt-5.6-terra` medium runs on MATLAB R2026a. Load for regression repair, not ordinary modeling. Evidence paths are relative to `skill-evaluations/consumer-credit-risk-featured-examples/`.

| Scenario | Condition | Prompt SHA-256 | Result | Finding | Evidence |
|---|---|---|---|---|---|
| 01 | no-skill | `4e34c1eb928620d0c2d509178b38154f4704d15691fca534e87f3e7291eff773` | failed | generated conditional syntax error | `01-stress-testing-panel-pd/runs/no-skill` |
| 01 | r0 | same | failed | macro fields validated before keyed join | `01-stress-testing-panel-pd/runs/r0-baseline` |
| 01 | r1 | same | failed | scenario shocks incorrectly required a historical time key | `01-stress-testing-panel-pd/runs/r1` |
| 01 | r2 | same | failed | heterogeneous table variables concatenated for missingness | `01-stress-testing-panel-pd/runs/r2` |
| 01 | r3 | same | failed | invalid cell-of-string-scalars table selector | `01-stress-testing-panel-pd/runs/r3` |
| 01 | r4 | same | failed | IDs not contiguous after join | `01-stress-testing-panel-pd/runs/r4` |
| 01 | r5 | same | failed | invented `Age` alias; sampling-specific | `01-stress-testing-panel-pd/runs/r5` |
| 02 | no-skill | `d25dee64e360112e67f8aa2c21ffe6d27f187471aee09e5c84eecec8f18e4de2` | failed | invented `ModelType` option | `02-cox-pd-and-ecl/runs/no-skill` |
| 02 | r0 | same | failed | unsupported generic predictor roles | `02-cox-pd-and-ecl/runs/r0-baseline` |
| 02 | r1 | same | failed | unsupported `outerjoin` option; sampling-specific | `02-cox-pd-and-ecl/runs/r1` |
| 03 | no-skill | `e7091547ce0e75927a325e2fdb943892f5fa5e51457bc54a60f7d79aa59168af` | failed | invented `ModelType` option | `03-ttc-pit-pd/runs/no-skill` |
| 03 | r0 | same | failed | heterogeneous table concatenation | `03-ttc-pit-pd/runs/r0-baseline` |
| 03 | r1 | same | failed | invalid generated source character; sampling-specific | `03-ttc-pit-pd/runs/r1` |

All historical gates are `0`; immutable snapshots preserve recoverable historical skill hashes. New rows must record full prompt and snapshot hashes, C/P/R/G, and gate before the next snapshot.

| Scenario | Condition | Prompt SHA-256 | Snapshot SHA-256 | Result | C/P/R/G; gate | Finding |
|---|---|---|---|---|---|---|
| 01 | r6 | `4e34c1eb928620d0c2d509178b38154f4704d15691fca534e87f3e7291eff773` | `947d4be2e1cba60b87057f19482d755038d68882f63cbe018629f8767ccbaf63` | failed | `0/0.2/0/0`; `0` | Recurrent invalid cell-of-string-scalars selector, caused by a contradictory code block in the skill itself. |
| 02 | r2 | `d25dee64e360112e67f8aa2c21ffe6d27f187471aee09e5c84eecec8f18e4de2` | `b7c3714e0ba72406da7407721e7cca6f392c1dad7351b6630a1e8342711558cf` | failed | `0/0.2/0/0`; `0` | Same recurrent table-selector failure before Cox fit/ECL. |
| 03 | r2 | `e7091547ce0e75927a325e2fdb943892f5fa5e51457bc54a60f7d79aa59168af` | `947d4be2e1cba60b87057f19482d755038d68882f63cbe018629f8767ccbaf63` | failed | `0/0.2/0/0`; `0` | Invented undefined `duplicated` helper while validating macro-year uniqueness. |
| 01 | r7 | `4e34c1eb928620d0c2d509178b38154f4704d15691fca534e87f3e7291eff773` | `a3b68efae1e749835bd639390ad4aa1418a88acf27fc903249af4b657fe511d5` | protocol failed | `0.4/0.2/0.2/0`; `0` | MATLAB and artifacts passed, but YOB was placed in `LoanVars` instead of selected `AgeVar`. |
| 02 | r3 | `d25dee64e360112e67f8aa2c21ffe6d27f187471aee09e5c84eecec8f18e4de2` | `bef46d2c98be2b16e17d9492435099fba3d705679002aec9ab41cba98dfe27fb` | failed | `0/0.2/0/0`; `0` | Required nonexistent `Year` fields in static per-ID LGD/EAD tables. |
| 03 | r3 | `e7091547ce0e75927a325e2fdb943892f5fa5e51457bc54a60f7d79aa59168af` | `a3b68efae1e749835bd639390ad4aa1418a88acf27fc903249af4b657fe511d5` | protocol failed | `0.4/0.2/0.2/0`; `0` | MATLAB and artifacts passed, but YOB was placed in `LoanVars` instead of selected `AgeVar`. |
| 01 | r8 | `4e34c1eb928620d0c2d509178b38154f4704d15691fca534e87f3e7291eff773` | `f9792745cfc0b8d2ec3e84b1dcb06ec0f2209dcccc84903ce550a22b4113b8c1` | passed | `0.4/0.3/0.2/0.1`; `1.0` | Independent refit, prediction tolerance, roles, split, scenarios, and artifacts passed. |
| 02 | r4 | `d25dee64e360112e67f8aa2c21ffe6d27f187471aee09e5c84eecec8f18e4de2` | `cab0a32c2cdc00431443eb33634aab3244cf667db51cc741710be846c1599671` | failed | `0/0.3/0/0.1`; `0` | `portfolioECL` interpreted `Year` as a PD value column; the lifetime-ECL skill owns the verified rule. |
| 03 | r4 | `e7091547ce0e75927a325e2fdb943892f5fa5e51457bc54a60f7d79aa59168af` | `f9792745cfc0b8d2ec3e84b1dcb06ec0f2209dcccc84903ce550a22b4113b8c1` | passed | `0.4/0.3/0.2/0.1`; `1.0` | Independent refit, prediction/metric tolerance, roles, split, and artifacts passed. |
| 02 | r5 | `d25dee64e360112e67f8aa2c21ffe6d27f187471aee09e5c84eecec8f18e4de2` | `716ad17362280087538bf8ef5e9ab44af64a47f24d3f2676e1b6e8cc3683154a` | passed | `0.4/0.3/0.2/0.1`; `1.0` | Independent Cox refit, ID holdout, all four PD outputs, wide-table ECL, object roles, numeric tolerance, and artifacts passed. |
| 02 | final-regression | `d25dee64e360112e67f8aa2c21ffe6d27f187471aee09e5c84eecec8f18e4de2` | `87be76fdeb143ad36e2557ecc5b5cbfec50d0b9fa8926718a90b91965febd2e7` | failed | `0/0/0/0.1`; `0` | Fresh agent resolved fixture relative to parent `runs` rather than its own final-regression directory; sampling-specific path construction, archived and retried fresh. |
| 02 | final-regression-r2 | same | `4b3f226f224c0ab66f880c73bdb655e11da0f5d1358caca6777e786882c5eec6` | generation aborted | `0/0/0/0`; `0` | Fresh agent requested exact snapshot paths despite their scoped presence; sampling-specific prompt path resolution, archived before another fresh retry. |
| 02 | final-regression-r3 | same | `1a497f3d4e92ecba1542a6e0f005a3bfc922a60922fd5ba2cde65d99dc78cc20` | passed | `0.4/0.3/0.2/0.1`; `1.0` | Fresh merged-skill agent passed independent Cox refit, recovered deterministic 60/40 ID split, four PD outputs, ECL, and artifact assertions. |
| 01 | final-regression | `4e34c1eb928620d0c2d509178b38154f4704d15691fca534e87f3e7291eff773` | `7f86955b593b590622cf57200708bafb4a1b8f617e9d2fcd68ca0232e99123e9` | passed | `0.4/0.3/0.2/0.1`; `1.0` | Fresh merged-skill agent passed independent panel-PD refit, deterministic split, stress scenarios, numeric, role, and artifact assertions. |
| 03 | final-regression | `e7091547ce0e75927a325e2fdb943892f5fa5e51457bc54a60f7d79aa59168af` | `7f86955b593b590622cf57200708bafb4a1b8f617e9d2fcd68ca0232e99123e9` | passed | `0.4/0.3/0.2/0.1`; `1.0` | Fresh merged-skill agent passed independent TTC/PIT refits, prediction and metric tolerances, role, split, and artifact assertions. |
