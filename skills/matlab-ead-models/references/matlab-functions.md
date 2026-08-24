# EAD Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. No model was executed. Maintain the selected exposure definition, table variables, and object class throughout the calculation.

## Model construction

- `eadModel = fitEADModel(data,ModelType)`; `eadModel = fitEADModel(___,Name=Value)`. Model type is `Regression`, `Tobit`, or `Beta`; it returns the matching EAD object. [Source](https://ww2.mathworks.cn/help/risk/fiteadmodel.html), R2021b; Beta support R2022b.
- Regression: `RegressionEADModel = fitEADModel(data,ModelType)` or `fitEADModel(___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.ead.regression.html), R2021b.
- Tobit: `TobitEADModel = fitEADModel(data,ModelType)` or `fitEADModel(___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.ead.tobit.html), R2021b.
- Beta: `BetaEADModel = fitEADModel(data,ModelType)` or `fitEADModel(___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.ead.beta.html), R2022b.

## Prediction and diagnostics

- `predictedEAD = predict(eadModel,data)`; `predictedEAD = predict(___,Name=Value)` returns a `NumRows`-by-1 numeric EAD vector. [Source](https://ww2.mathworks.cn/help/risk/tobit.predict.html), R2021b.
- `CalMeasure = modelCalibration(eadModel,data)`; `[CalMeasure,CalData] = modelCalibration(___,Name=Value)` returns R-squared, RMSE, correlation, and sample-mean-error measures. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.ead.tobit.modelcalibration.html), R2023a.
- `modelCalibrationPlot(eadModel,data)`; `modelCalibrationPlot(___,Name=Value)`; `h = modelCalibrationPlot(ax,___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.ead.tobit.modelcalibrationplot.html), R2023a.
- `DiscMeasure = modelDiscrimination(eadModel,data)`; `[DiscMeasure,DiscData] = modelDiscrimination(___,Name=Value)` returns AUROC/ROC information. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.ead.tobit.modeldiscrimination.html), R2021b.
- `modelDiscriminationPlot(eadModel,data)`; `modelDiscriminationPlot(___,Name=Value)`; `h = modelDiscriminationPlot(ax,___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.ead.tobit.modeldiscriminationplot.html), R2021b.
