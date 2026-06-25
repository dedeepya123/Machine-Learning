GPTQ Objective

Preserve layer outputs.

--------------------------------

Layer

Y = WX

--------------------------------

Quantized Layer

Ŷ = ŴX

--------------------------------

Objective

||WX − ŴX||²

--------------------------------

Define

E = Ŵ − W

--------------------------------

Objective becomes

||EX||²

--------------------------------

Expand

L = Tr(EXXᵀEᵀ)

--------------------------------

Observation

XXᵀ appears naturally.

--------------------------------

Take derivatives

First derivative

↓

EXXᵀ

--------------------------------

Second derivative

↓

XXᵀ

--------------------------------

Therefore

H = XXᵀ

for the layer reconstruction
objective.

--------------------------------

Interpretation

XXᵀ captures activation
statistics.

--------------------------------

Large activation directions

↓

More sensitive.

--------------------------------

Rare activation directions

↓

Less sensitive.

--------------------------------

OBS uses

true Hessian.

--------------------------------

GPTQ uses

layer Hessian

H = XXᵀ

--------------------------------

Much cheaper.

Still captures enough
curvature information
for compensation.
