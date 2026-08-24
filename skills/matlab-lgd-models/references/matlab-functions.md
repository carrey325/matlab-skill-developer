# LGD Function Evidence

Official MathWorks pages were inspected on 2026-08-21 for MATLAB R2026a. Model fitting, prediction, calibration, and discrimination were then exercised in the isolated `comparing-lgd-models` evaluation; verified failures and corrections are recorded in `gotchas.md`. Maintain the selected loss definition, table variables, and model class across all object methods.

## Model construction and conditional LGD

- `lgdModel = fitLGDModel(data,ModelType)`; `lgdModel = fitLGDModel(___,Name,Value)`. Model type is `Regression`, `Tobit`, or `Beta`; it returns the matching LGD object. [Source](https://ww2.mathworks.cn/help/risk/fitlgdmodel.html), R2021a; Beta support R2022b.
- Regression: `RegressionLGDModel = fitLGDModel(data,ModelType)` or `fitLGDModel(___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.lgd.regression.html), R2021a.
- Tobit: `TobitLGDModel = fitLGDModel(data,'Tobit')` or `fitLGDModel(___,Name,Value)`. For explicit two-sided censoring use `'CensoringSide','both','LeftLimit',0,'RightLimit',1`; `LowerLimit` and `UpperLimit` are not valid option names. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.lgd.tobit.html), R2021a; option names verified in R2026a.
- Beta: `BetaLGDModel = fitLGDModel(data,ModelType)` or `fitLGDModel(___,Name=Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.lgd.beta.html), R2022b.
- `ConditionalLGD = fryeJacobsLGD(ConditionalPD,BaselinePD,BaselineLGD,Correlation)` accepts scalar/vector conditional PD values in `(0,1)` and returns a compatible scalar/vector conditional LGD. [Source](https://ww2.mathworks.cn/help/risk/fryejacobslgd.html), R2024b.

## Prediction and diagnostics

- `LGD = predict(lgdModel,data)` returns a `NumRows`-by-1 LGD vector. [Source](https://ww2.mathworks.cn/help/risk/regression.predict.html), R2021a.
- `CalMeasure = modelCalibration(lgdModel,data)`; `[CalMeasure,CalData] = modelCalibration(___,Name,Value)` returns R-squared, RMSE, correlation, and sample-mean-error measures. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.lgd.regression.modelcalibration.html), R2023a.
- `modelCalibrationPlot(lgdModel,data)`; `modelCalibrationPlot(___,Name,Value)`; `h = modelCalibrationPlot(ax,___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.lgd.regression.modelcalibrationplot.html), R2023a.
- `DiscMeasure = modelDiscrimination(lgdModel,data)`; `[DiscMeasure,DiscData] = modelDiscrimination(___,Name,Value)` returns AUROC/ROC information. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.lgd.regression.modeldiscrimination.html), R2021a.
- `modelDiscriminationPlot(lgdModel,data)`; `modelDiscriminationPlot(___,Name,Value)`; `h = modelDiscriminationPlot(ax,___,Name,Value)`. [Source](https://ww2.mathworks.cn/help/risk/risk.credit.lgd.regression.modeldiscriminationplot.html), R2021a.
