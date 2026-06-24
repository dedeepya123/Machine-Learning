OBD

Uses diagonal Hessian.

Assumes weights independent.

Measures damage after removing weight.

No repair.

--------------------------------

OBS Question

Can remaining weights
compensate for removed weight?

--------------------------------

Constraint

Remove weight:

w₁ → 0

--------------------------------

Goal

Minimize loss increase
after compensation.

--------------------------------

Loss Approximation

ΔL

≈

1/2 ΔwᵀHΔw

--------------------------------

OBS keeps full Hessian.

Uses interactions.

--------------------------------

Reason

Interactions tell us
which weights can compensate.

--------------------------------

Optimization

Minimize ΔL

subject to

removing a chosen weight.

--------------------------------

Key Result

Optimal compensation depends on

H⁻¹

--------------------------------

Interpretation

Hessian

↓

Who interacts with whom.

--------------------------------

Inverse Hessian

↓

How correction should be
distributed.

--------------------------------

OBD asks

"How important is this weight?"

--------------------------------

OBS asks

"How replaceable is this weight?"

--------------------------------

OBS more accurate

but computationally expensive.

This limitation eventually
motivates GPTQ.
