# Evaluation findings

Development-only evidence for scorecard portions of scenarios 07-09.

| Scenario | Conditions | Prompt SHA-256 | Result history | Evidence |
|---|---|---|---|---|
| 07 | no-skill, r0 | `41c27f7705d0f4cedc205c67b801fb41332545542fc15e2f5cd6c8f69c5f0d6f` | both failed | `07-credit-reweighting/runs` |
| 08 | no-skill, r0-r2 | `edc1779e75c715c2e3b06f80fc04b3b372556de23065f21db9f432e696078a9f` | all failed before comparison completed | `08-credit-disparate-impact-removal/runs` |
| 09 | no-skill, r0 | `ff13956b308c30eae5421f9cab684482b44281ae0d5345e6f34d73fa1f7b5066` | both failed before explanations | `09-scorecard-explainability/runs` |

Governance-owned failures are mirrored in its findings file. New rounds must add hashes, C/P/R/G, and evidence before the next snapshot.

| Scenario | Condition | Snapshot SHA-256 | Result | Canonical finding |
|---|---|---|---|---|
| 07 | r1 | `dfe473d24332f0ad8aec040f7bb21edd6c0a9c3fc4c837f5291d8595b579f8f2` | failed after model fit | governance owns prediction-label type mismatch |
| 08 | r3 | `dfe473d24332f0ad8aec040f7bb21edd6c0a9c3fc4c837f5291d8595b579f8f2` | failed before remover fit | governance owns invented source alias |
| 07 | r2 | `0d74713a4eed077ae153aaff0b3b78a7b93a3f680e77755c5b1d7f159eec0875` | protocol failed after complete execution | governance owns selected four-band AgeGroup mismatch |
| 08 | r4 | `0d74713a4eed077ae153aaff0b3b78a7b93a3f680e77755c5b1d7f159eec0875` | protocol failed after complete execution | governance owns missing derivation/validation of four-band AgeGroup |
| 09 | r1 | `ffe695615ac6bc5d760295982b027f9a9c59cb79b42053a70ab7c9150c214613` | MATLAB exit 1; C/P/R/G `0/0.2/0/0`, gated `0` | top-level `MaxNumBins`/`MinBinSize` rejected by `autobinning`; verified canonical fix uses Split `AlgorithmOptions={"MaxNumBins",5,"MinCount",50}`; evidence `09-scorecard-explainability/failures/F001-autobinning-split-options` |
| 09 | r2 | `3d75dd1e753f1d95c3a28f7b4827ea82554f0f737ae0f71074a412fd952b6b6f` | MATLAB exit 1; C/P/R/G `0/0.3/0/0.1`, gated `0` | binning and fitting passed; `formatpoints` rejected invented scaling arguments; verified `PointsOddsAndPDO=[600 50 20]`; evidence `09-scorecard-explainability/failures/F002-formatpoints-scaling` |
| 09 | r3 | `664b2adc33ed18521535d0931d8627cef64b73a729903d19fa513c5d33309edc` | generation failed; C/P/R/G `0/0/0/0`, gated `0` | fresh agent incorrectly reported that prescribed absolute paths were absent and wrote no script; sampling-specific path-resolution noise, archived at `09-scorecard-explainability/failures/F003-agent-path-resolution` |
| 09 | r4 | `1e37d91c97ee7e027ff93d189a40793767a18b2c992154da5abee6599c258d6d` | MATLAB exit 1; C/P/R/G `0/0.3/0.1/0.1`, gated `0` | scorecard fit/scaling and PDP passed; governance owns unsupported ICE `Conditional="individual"` and pending explainer-query signatures; evidence `09-scorecard-explainability/failures/F004-explainer-query-signatures` |
| 07 | r3 | `57fe9be8332b58096ec46e8e97b56a80b8b25b3318c919886629af22eedd3a53` | execution/artifacts passed; C/P/R/G `0/0.2/0.2/0.1`, gated `0` | derived four-band AgeGroup and training-only weights passed, but default Stepwise `fitmodel` violated selected full-model contract; canonical `07-credit-reweighting/failures/F003-full-model-selection` |
| 08 | r5 | `57fe9be8332b58096ec46e8e97b56a80b8b25b3318c919886629af22eedd3a53` | execution/artifacts passed; C/P/R/G `0/0.2/0.2/0.1`, gated `0` | group derivation and training-only remover passed, but both scorecards used default Stepwise instead of selected FullModel; canonical `08-credit-disparate-impact-removal/failures/F004-full-model-selection` |
| 09 | r5 | `2710ec60a282383e1aef54bc2efa1a7aab11e37ff816e60aef22c8c4150db6d3` | MATLAB exit 1; C/P/R/G `0/0.2/0.1/0.1`, gated `0` | governance owns explainer result-property failure; this snapshot also used default Stepwise instead of selected FullModel; canonical `09-scorecard-explainability/failures/F005-explainer-result-properties` |
| 07 | r4 | `d58bd65e39ddd1ca2a75756bbfe35bbf69233a3474b7356aa3bc721e1d6a4956` | execution/artifacts passed; C/P/R/G `0/0.2/0.2/0.1`, gated `0` | FullModel fix passed, but agent imported scenario 09's Split 5/50 binning into an automatic-binning-only request, changing the hidden reference predictions; canonical `07-credit-reweighting/failures/F004-cross-scenario-binning` |
| 08 | r6 | `d58bd65e39ddd1ca2a75756bbfe35bbf69233a3474b7356aa3bc721e1d6a4956` | execution/artifacts passed; C/P/R/G `0/0.2/0.2/0.1`, gated `0` | training-only remover and FullModel passed, but cross-scenario Split 5/50 parameters changed both reference scorecards; canonical `08-credit-disparate-impact-removal/failures/F005-cross-scenario-binning` |
| 08 | r7 | `e77cffe5666738c2ad7e00b793178b25990480ce51f32009e5f51dba1be8ad81` | generation aborted; C/P/R/G `0/0/0/0`, gated `0` | agent declined to resolve the explicitly scoped snapshot filename and requested clarification; sampling-specific path-resolution noise, canonical `08-credit-disparate-impact-removal/failures/F006-agent-path-resolution` |
| 07 | r5 | `e77cffe5666738c2ad7e00b793178b25990480ce51f32009e5f51dba1be8ad81` | passed; C/P/R/G `0.4/0.3/0.2/0.1`, gated `1.0` | independent FullModel refits, deterministic holdout, four-band derivation, training-only fairness weights, PD/threshold tolerance, fairness artifacts, and weight ownership passed |
| 08 | r8 | `b6d7df342075e29d02df5fd1071f0cd295cbb48bd201452b4dc7cf084834c8b7` | passed; C/P/R/G `0.4/0.3/0.2/0.1`, gated `1.0` | independent remover/refits, deterministic holdout, four-band validation, training-only repair, PD/threshold tolerance, model types, and all artifacts passed |
| 09 | r6 | `d58bd65e39ddd1ca2a75756bbfe35bbf69233a3474b7356aa3bc721e1d6a4956` | passed; C/P/R/G `0.4/0.3/0.2/0.1`, gated `1.0` | independent Split 5/50 FullModel refit, point scaling, scores/points tolerance, fixed query, PDP/ICE, LIME/Shapley objects/values, and artifacts passed |
| 09 | final-regression | `bdd4d6a9ea253189233e4b107ac5dc6abd20fabfe0eb65f8709781e4ebfbf567` | failed; C/P/R/G `0/0.3/0/0.1`, gated `0` | fresh merged agent wrapped the already-tabular `score` points output with `array2table`, creating a nested table rejected by `writetable`; canonical F006 |

## Final merged regression

| Scenario | Condition | Prompt SHA-256 | Snapshot SHA-256 | Result | C/P/R/G; gate | Evidence |
|---|---|---|---|---|---|---|
| 07 | final-regression | `41c27f7705d0f4cedc205c67b801fb41332545542fc15e2f5cd6c8f69c5f0d6f` | `59ba974eef9a447212a6398a8040ded58f40b58a3e8eda0e7c9843736916ae2e` | passed | `0.4/0.3/0.2/0.1`; `1.0` | `07-credit-reweighting/runs/final-regression` |
| 08 | final-regression | `edc1779e75c715c2e3b06f80fc04b3b372556de23065f21db9f432e696078a9f` | `59ba974eef9a447212a6398a8040ded58f40b58a3e8eda0e7c9843736916ae2e` | passed | `0.4/0.3/0.2/0.1`; `1.0` | `08-credit-disparate-impact-removal/runs/final-regression` |
| 09 | final-regression-r2 | `ff13956b308c30eae5421f9cab684482b44281ae0d5345e6f34d73fa1f7b5066` | `e87f86b0f45a688aca04bbb18dfa017452d216466e35b4931dbc9f33ecc190cb` | passed | `0.4/0.3/0.2/0.1`; `1.0` | `09-scorecard-explainability/runs/final-regression-r2` |
