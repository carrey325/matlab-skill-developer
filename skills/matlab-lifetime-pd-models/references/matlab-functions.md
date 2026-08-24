# Lifetime PD Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No model was executed. Fit and prediction data must remain compatible with the selected model object and its event/time convention.

## Model construction

### `fitLifetimePDModel`

- Syntax: `pdModel = fitLifetimePDModel(data,ModelType)`; `pdModel = fitLifetimePDModel(___,Name,Value)`.
- Contract: `data` is a panel-data table with an ID column and binary response where `1` represents default. Model type is `Logistic`, `Probit`, or `Cox`; return object is the selected PD class.
- Use `IDVar`, `AgeVar`, `LoanVars`, `MacroVars`, and `ResponseVar` to identify the selected model roles. `LoanVars` and `MacroVars` accept the selected predictor names; `Cox` requires `AgeVar`.
- Evidence: [official page](https://ww2.mathworks.cn/help/risk/fitlifetimepdmodel.html), introduced R2020b.

### Model-class entries

- Logistic: `LogisticPDModel = fitLifetimePDModel(data,ModelType)` or `fitLifetimePDModel(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.logistic.html), R2020b.
- Probit: `ProbitPDModel = fitLifetimePDModel(data,ModelType)` or `fitLifetimePDModel(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.probit.html), R2020b.
- Cox: `CoxPDModel = fitLifetimePDModel(data,ModelType,AgeVar=agevar_value)` or `fitLifetimePDModel(___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.cox.html), R2021b.
- Custom: `CustomLifetimePDModel = customLifetimePDModel(pdFcnHandle,IDVar=idvar_value,ResponseVar=responsevar_value)` or `customLifetimePDModel(___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.customlifetimepdmodel.html), R2022b.

## Prediction and diagnostics

- `conditionalPD = predict(pdModel,data)` returns one conditional PD per input row. [Source](https://ww2.mathworks.cn/help/risk/logistic.predict.html), introduced R2020b.
- `LifeTimePredictedPD = predictLifetime(pdModel,data)` or `predictLifetime(___,Name,Value)` returns documented lifetime PD values. [Source](https://ww2.mathworks.cn/help/risk/logistic.predictlifetime.html), introduced R2020b.
- `CalMeasure = modelCalibration(pdModel,data,GroupBy)`; `[CalMeasure,CalData] = modelCalibration(___,Name,Value)` returns grouped calibration measures and optional data. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.logistic.modelcalibration.html), R2023a.
- `modelCalibrationPlot(pdModel,data,GroupBy)`; `modelCalibrationPlot(___,Name,Value)`; `h = modelCalibrationPlot(ax,___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.logistic.modelcalibrationplot.html), R2023a.
- `DiscMeasure = modelDiscrimination(pdModel,data)`; `[DiscMeasure,DiscData] = modelDiscrimination(___,Name,Value)` returns AUROC/ROC data. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.logistic.modeldiscrimination.html), R2020b.
- `modelDiscriminationPlot(pdModel,data)`; `modelDiscriminationPlot(___,Name,Value)`; `h = modelDiscriminationPlot(ax,___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.pd.logistic.modeldiscriminationplot.html), R2021a.
- `pdModel = discardResiduals(pdModel)` removes retained residual information from a fitted Cox object. [Source](https://ww2.mathworks.cn/help/risk/cox.discardresiduals.html), R2023a.
