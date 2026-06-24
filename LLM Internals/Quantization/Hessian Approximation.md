Correct Objective

ΔL ≈ 1/2 ΔwᵀHΔw

Measures actual quantization damage.

--------------------------------

Problem

Hessian size:

N × N

For billions of weights:

Impossible to store or compute.

--------------------------------

Observation

Diagonal terms:

Sensitivity of individual weights.

Off-diagonal terms:

Interactions between weights.

--------------------------------

First Approximation

Ignore interactions.

Keep only diagonal.

--------------------------------

Diagonal Hessian

Storage:

O(N)

instead of

O(N²)

--------------------------------

Damage Approximation

ΔL

≈

1/2 Σ Hii (Δwi)²

--------------------------------

Interpretation

Weight Damage

=

Sensitivity

×

Quantization Error²

--------------------------------

Second Observation

Do not compute Hessian
for entire model.

Quantize layer by layer.

Use local curvature.

--------------------------------

Research Direction

Need more accuracy than
diagonal approximation

but much cheaper than
full Hessian.
