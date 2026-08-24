---
name: matlab-credit-default-deep-learning
description: Implement selected MATLAB neural-network construction, training, prediction, and reporting for credit-default probability tasks without choosing the model architecture or policy.
---

# Implement Credit-Default Neural Networks in MATLAB

## Scope

Implement, review, or repair a selected MATLAB credit-default neural-network workflow: tabular encoding, `dlnetwork` construction, `trainingOptions`, `trainnet`, prediction, and probability reporting.

Do not choose an architecture, features, partition policy, probability threshold, training schedule, or credit decision rule.

## Prerequisites

- MATLAB R2026a and Deep Learning Toolbox; use Risk Management Toolbox only when the supplied data contract requires its data.
- A selected architecture, loss, predictor layout, data split, training options, and requested outputs.

## Capability Contract

### Required Inputs

- A compatible feature table or array and its selected binary response convention.
- The selected network layers/connections and a complete training or pretrained-network contract.

### Conditional Inputs

- One-hot encoding, validation data, CPU/GPU setting, network import/export, and plot controls when specified.

### Input Validation

- Validate feature/response row alignment, partition disjointness, categorical encoding, feature order, and finite binary targets.
- Before reporting probabilities, validate the requested output column, its row count, and its `[0,1]` domain.

## Critical Rules

### Intent Preservation

- Preserve the supplied architecture, loss, optimizer, and data split. Do not substitute a statistical PD model or simplify a residual network.

### Data and Unit Conventions

- Keep identifier columns out of network features when the implementation brief identifies them as partition keys.
- Preserve categorical feature order and use the supplied prediction feature order for every partition.

### Execution Boundaries

- Use `$matlab-credit-model-governance` for LIME, Shapley, partial-dependence, or fairness analysis.
- Do not infer a decision threshold or certify a network for production use.

## Failure Handling

- Stop on missing Deep Learning Toolbox support, invalid layer graph connections, incompatible training/validation schemas, nonfinite targets, or an unspecified architecture/training contract.
- Report the failing function, MATLAB release, model object class, and full diagnostic before changing a call.

## Gotchas

- Treat a network score as a probability only when the selected output/loss configuration makes that interpretation valid; do not silently apply an additional sigmoid or normalization.
- For an ID-level panel split, an ID may repeat over rows; validate partition membership by unique ID rather than requiring row-unique identifiers.
- Treat the supplied ordered feature contract as authoritative: do not infer it from `UserData` or shared columns, and validate its width and row-observation orientation against the input layer.

## Reference Loading

- Load [evaluation findings](references/evaluation-findings.md) only when regression-testing or repairing deep credit-default implementations.
- Load [verified deep-learning gotchas](references/gotchas.md) before validating or splitting ID-level panel data.
- Load [the neural-network function reference](references/matlab-functions.md) before building, training, predicting, or exporting a selected credit-default network.
