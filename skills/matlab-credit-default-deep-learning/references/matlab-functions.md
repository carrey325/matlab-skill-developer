# MATLAB R2026a neural-network reference

Use these records only after the implementation brief has selected the data contract, architecture, loss, and training policy. Evidence was inspected on 2026-08-21 from official MATLAB R2026a documentation; example sections are excluded.

## `dlnetwork`

- Construct a trainable network from a layer array or layer graph. Build residual paths with named layers and explicit connections; validate the resulting graph before training.
- A trained `dlnetwork` is the output class of `trainnet`.
- Evidence: [official page](https://ww2.mathworks.cn/help/deeplearning/ref/dlnetwork.html), R2026a.

## `trainingOptions`

- Syntax: `options = trainingOptions(solverName)` or `trainingOptions(solverName,Name=Value)`.
- Solvers include `"sgdm"`, `"rmsprop"`, `"adam"`, `"lbfgs"`, and `"lm"`.
- Relevant controls include `InitialLearnRate`, `MiniBatchSize`, `MaxEpochs`, `Shuffle`, `ValidationData`, `ValidationFrequency`, `OutputNetwork`, `ExecutionEnvironment`, and `Plots`.
- `ExecutionEnvironment` accepts `"cpu"` among supported settings; select it only when the request requires CPU execution.
- Evidence: [official page](https://ww2.mathworks.cn/help/deeplearning/ref/trainingoptions.html), R2026a.

## `trainnet`

- Syntax includes `net = trainnet(features,targets,net,lossFcn,options)` and `net = trainnet(data,net,lossFcn,options)`.
- Feature data may be a numeric array, `dlarray`, table, datastore, minibatch queue, or categorical array. The selected loss can include `"binary-crossentropy"`.
- Output is a `dlnetwork`; `[net,info]` also returns training information.
- Evidence: [official page](https://ww2.mathworks.cn/help/deeplearning/ref/trainnet.html), R2026a.

## Prediction and export

- Use the prediction API compatible with the selected `dlnetwork` and data layout. Preserve the training feature order and test-row alignment.
- Save only the requested model, predictions, metrics, and figures; do not add checkpoints or choose a deployment format unless supplied.
- Evidence: [predict](https://ww2.mathworks.cn/help/deeplearning/ref/dlnetwork.predict.html) and [minibatchpredict](https://ww2.mathworks.cn/help/deeplearning/ref/minibatchpredict.html), R2026a.
