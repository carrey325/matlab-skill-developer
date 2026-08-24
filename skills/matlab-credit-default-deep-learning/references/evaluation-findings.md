# Evaluation findings

Development-only Terra-medium evidence on MATLAB R2026a.

| Scenario | Condition | Prompt SHA-256 | Result | Finding | Evidence |
|---|---|---|---|---|---|
| 04 | no-skill | `dc95b10bad9cec74952addf9ecb368e5937ebe0e503b8fb5219c35b24060d425` | failed | repeated panel IDs rejected | `04-deep-credit-default-networks/runs/no-skill` |
| 04 | r0 | same | failed | row-unique IDs required | `04-deep-credit-default-networks/runs/r0-baseline` |
| 04 | r1 | same | execution passed | historical pass; final gated regression pending | `04-deep-credit-default-networks/runs/r1` |
| 05 | no-skill | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | failed | network received six rather than four features | `05-deep-pd-interpret-and-stress/runs/no-skill` |
| 05 | r0 | same | failed | required optional `UserData` metadata | `05-deep-pd-interpret-and-stress/runs/r0-baseline` |
| 05 | r1 | same | failed | source categories confused with encoded names | `05-deep-pd-interpret-and-stress/runs/r1` |
| 05 | r2 | same | failed | shared `Year` treated as predictor | `05-deep-pd-interpret-and-stress/runs/r2` |
| 05 | r3 | same | failed | generated parse error; sampling-specific | `05-deep-pd-interpret-and-stress/runs/r3` |
| 05 | r4 | same | failed | nonexistent `dlnetwork.InputSizes` used | `05-deep-pd-interpret-and-stress/runs/r4` |
| 05 | r5 | same | failed | invented MAT aliases; sampling-specific | `05-deep-pd-interpret-and-stress/runs/r5` |

New rows must record full prompt/snapshot hashes and C/P/R/G before the next snapshot.

| Scenario | Condition | Prompt SHA-256 | Snapshot SHA-256 | Result | C/P/R/G; gate | Finding |
|---|---|---|---|---|---|---|
| 05 | r6 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `ce59313c828b94c3e520e248537fedc064b04428953bc4cae6d4377d3bb78296` | failed | `0/0.2/0/0.1`; `0` | Category-derived encoded names were column-oriented and failed horizontal assembly with `YOB`. |
| 05 | r7 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `51a12ca055313e043e4d47909380ec424570df3db127684efad6830447960329` | failed | `0/0.2/0/0.1`; `0` | Used undefined local `queryIndex` instead of supplied `S.queryIndex`; sampling-specific. |
| 05 | r8 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `f9a211e88a9e174f82a266d7cc01a89a5fa0ad606008fcca9acc64945b77993b` | failed | `0/0.3/0/0.1`; `0` | Network scoring passed; result table used reserved dimension name `Row`; verified nonreserved `Observation` variable name. |
| 05 | r9 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `85f12bd056cd5086ac44e7db27465450c148befad004171f4de31f0ff816887a` | failed | `0/0.3/0/0.1`; `0` | Reached explainability; governance owns invalid positional LIME type and incomplete query fit. |
| 05 | r10 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `c6980f49657bd58f4e7e75287bbe3cc865913b592f3a76c8458695b505174617` | failed | `0/0.2/0/0.1`; `0` | Transposed a validated n-by-4 tabular feature matrix before `dlnetwork/predict`, producing an invalid 2024-channel input; governance result-property fixes were not yet present in this snapshot. |
| 05 | r11 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `e105756459b2b1cfc306a50d84b8dba3c6799d3d5f1efa1139cda108d63165ad` | failed | `0/0.3/0/0.1`; `0` | Network scoring passed; governance owns missing `CategoricalPredictors="ScoreGroup"` for mixed-table LIME/Shapley inputs. |
| 05 | r12 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `e73c48b6b19dbaea792c515ab10ac4e93209e9c9e63442cbf4b623b785587d34` | failed | `0/0.3/0/0.1`; `0` | Declared ScoreGroup but preserved its ordinal categorical type; confirmed same F011 root because LIME rejects ordinal predictors. Canonical rule was corrected after this immutable snapshot. |
| 05 | r13 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `893021f951c6fe0b851d99de4eb8c8a4d29e1f013126362e3fb58878eeaef9f0` | failed after all model/explainer artifacts | `0.4/0.3/0.1/0.1`; `0` | Summary construction used unsupported `string(number,"%.6f")`; verified `compose` formatting. |
| 05 | r14 | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `a79a5a0a1bf06ec6eb7221a79b83d85ee6dc1ceefe9dcb4fa4cd9a49e7277d76` | passed | `0.4/0.3/0.2/0.1`; `1.0` | Independent base/stress network predictions, ordered one-hot contract, nonordinal fixed-query LIME/Shapley, finite contributions, no-training check, and all artifacts passed. |

## Final merged regression

| Scenario | Condition | Prompt SHA-256 | Snapshot SHA-256 | Result | C/P/R/G; gate | Evidence |
|---|---|---|---|---|---|---|
| 04 | final-regression | `dc95b10bad9cec74952addf9ecb368e5937ebe0e503b8fb5219c35b24060d425` | `fef799adf9a6392c8b73fb92d48d18812b485473b21598cd13e5ab9e3f592d63` | passed | `0.4/0.3/0.2/0.1`; `1.0` | `04-deep-credit-default-networks/runs/final-regression` |
| 05 | final-regression | `f6e96ecd1da45aa7c1d2743abbb8f46f13dc5c49f33fd1333e9e6acaab467878` | `ef02e277fa7e8052d81d4f2897d1d3946d40be7371830a2481284a823fc0dadf` | passed | `0.4/0.3/0.2/0.1`; `1.0` | `05-deep-pd-interpret-and-stress/runs/final-regression` |
