Problem

Same quantization error

≠

Same model damage

--------------------------------

Need

Measure loss increase

after quantization.

--------------------------------

Let

Δw

=

Quantization error

--------------------------------

Use Taylor Expansion

L(w+Δw)

≈

L(w)

+

Gradient Term

+

Curvature Term

--------------------------------

Observation

Model already trained.

Gradient ≈ 0

Therefore first-order term vanishes.

--------------------------------

Remaining Damage

ΔL

≈

1/2

×

Curvature

×

(Δw)^2

--------------------------------

Interpretation

Damage depends on:

1. Quantization Error

2. Curvature

--------------------------------

Flat Valley

Small Curvature

↓

Quantization Safe

--------------------------------

Sharp Valley

Large Curvature

↓

Quantization Dangerous

--------------------------------

For Entire Network

Curvature becomes:

Hessian

--------------------------------

Why Hessian Appears

Need quantization damage

↓

Need loss increase

↓

Need Taylor expansion

↓

Need curvature

↓

Need Hessian
