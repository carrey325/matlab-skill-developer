# Evaluation findings

Development-only Terra-medium evidence on MATLAB R2026a.

| Scenario | Condition | Prompt SHA-256 | Result | Finding | Evidence |
|---|---|---|---|---|---|
| 10 | no-skill | `86368d38aaa4bacbfceeb87b2090eb9b17bbcead5cd4b8013c68b5e262e06eeb` | failed | invalid `PredictorVars` | `10-ordinal-credit-rating/runs/no-skill` |
| 10 | r0 | same | failed | invalid `PredictorVars` | `10-ordinal-credit-rating/runs/r0-baseline` |
| 10 | r1 | same | failed | unsupported confusion-chart construction | `10-ordinal-credit-rating/runs/r1` |
| 10 | r2 | same | failed | malformed result-table assembly; sampling-specific | `10-ordinal-credit-rating/runs/r2` |
| 10 | r3 | `f5260e69fd463465aeb8ee152b25bd81021e3407c6f1ab1ecf23ba92a4f6049b` | failed; C/P/R/G `0/0.3/0.1/0.1`, gated `0` | MATLAB execution reached reporting, then `confusionchart(...,Order=...)` failed because `Order` is unsupported; verified matrix-plus-label construction | `10-ordinal-credit-rating/failures/F004-confusion-chart-order` |
| 10 | r4 | `6904a61d01d47b1d3c1b45fc1af70444aff670eddc07dfe1840ec1a58b900b5c` | failed; C/P/R/G `0/0.3/0/0.1`, gated `0` | fit/prediction passed; result-table construction used a cell array of string scalars for `VariableNames`; verified string-array construction | `10-ordinal-credit-rating/failures/F005-table-variable-names` |
| 10 | r5 | `3713c86046646fe42dd5bae4139e981092e3852683ba37150e91aab19d661e21` | failed; C/P/R/G `0/0.1/0/0.1`, gated `0` | schema validation failed while vertically concatenating scalar names around a row predictor list; verified row-oriented assembly | `10-ordinal-credit-rating/failures/F006-name-list-orientation` |
| 10 | r6 | `9ad380f6d66d93f02e6c812fcac587fd841b7bbc3ac6ec23c0631b0fc45804a5` | passed; C/P/R/G `0.4/0.3/0.2/0.1`, gated `1.0` | independent stratified split, ordinal refit, label/probability tolerance, confusion matrix, class order, and artifacts all passed | `10-ordinal-credit-rating/runs/r6` |
| 11 | no-skill | `4e14651d1ef2ac5fcc418c755d1055d850697c7f71993c78874098d35c29b698` | failed | incompatible predictor-name concatenation | `11-payoff-default-multinomial/runs/no-skill` |
| 11 | r0 | same | failed | nominal category order treated as fixed | `11-payoff-default-multinomial/runs/r0-baseline` |
| 11 | r1 | same | execution passed | historical pass; final gated regression pending | `11-payoff-default-multinomial/runs/r1` |
| 10 | final-regression | `ba752d2c78c4f767e64b1cb50189d6d9c3d77b411c5db406bd5d1a395a819686` | failed; C/P/R/G `0/0.1/0/0.1`, gated `0` | table selection mixed a column `cellstr` and a cell containing a string scalar; homogeneous selector verified | `10-ordinal-credit-rating/failures/F007-table-selector-container` |
| 11 | final-regression | `ba752d2c78c4f767e64b1cb50189d6d9c3d77b411c5db406bd5d1a395a819686` | failed; C/P/R/G `0/0.1/0/0.1`, gated `0` | heterogeneous brace extraction attempted numeric/categorical concatenation before validation; typed validation verified | `11-payoff-default-multinomial/failures/F002-mixed-table-brace-extraction` |

## Final merged regression

| Scenario | Condition | Prompt SHA-256 | Snapshot SHA-256 | Result | C/P/R/G; gate | Evidence |
|---|---|---|---|---|---|---|
| 10 | final-regression-r2 | `86368d38aaa4bacbfceeb87b2090eb9b17bbcead5cd4b8013c68b5e262e06eeb` | `c9172adb1391afa5a2914141d47748a5cd364468b829f7e0e98234e8f4824f57` | passed | `0.4/0.3/0.2/0.1`; `1.0` | `10-ordinal-credit-rating/runs/final-regression-r2` |
| 11 | final-regression-r2 | `4e14651d1ef2ac5fcc418c755d1055d850697c7f71993c78874098d35c29b698` | `c9172adb1391afa5a2914141d47748a5cd364468b829f7e0e98234e8f4824f57` | passed | `0.4/0.3/0.2/0.1`; `1.0` | `11-payoff-default-multinomial/runs/final-regression-r2` |

New rounds must record full prompt/snapshot hashes and C/P/R/G before the next snapshot.
