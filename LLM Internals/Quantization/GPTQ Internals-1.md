GPTQ is not fine-tuning.

No gradients.

No backprop.

No optimizer.

--------------------------------

Goal

Preserve layer outputs.

--------------------------------

Layer

Y = WX

--------------------------------

Quantized Layer

Yq = WqX

--------------------------------

Error

Yq - Y

=

EX

--------------------------------

GPTQ minimizes

||EX||²

--------------------------------

Calibration Data

Used only to collect
layer activations X.

--------------------------------

Key Observation

Objective depends on

XXᵀ

--------------------------------

GPTQ Hessian Approximation

H ≈ XXᵀ

--------------------------------

OBS needed H⁻¹

GPTQ uses

(XXᵀ)⁻¹

inside one layer.

--------------------------------

Process

Quantize one column

↓

Compute error

↓

Compensate using remaining
unquantized columns

↓

Repeat sequentially

--------------------------------

No retraining.

Only intelligent rounding
plus compensation.
