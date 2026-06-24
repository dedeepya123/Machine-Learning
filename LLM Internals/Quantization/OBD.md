Goal of OBD

Originally:

Pruning

Not quantization.

--------------------------------

Problem

Full Hessian too large.

--------------------------------

OBD Assumption

Ignore interactions.

Hij = 0

for i ≠ j

Keep only diagonal.

--------------------------------

Loss Approximation

ΔL ≈ 1/2 Σ Hii (Δwi)^2

--------------------------------

Pruning

wi → 0

Therefore

Δwi = -wi

--------------------------------

OBD Importance

Importance(i)

=

1/2 Hii wi²

--------------------------------

Interpretation

Weight Magnitude

×

Sensitivity

--------------------------------

Small Importance

Safe to remove.

--------------------------------

Large Importance

Protect.

--------------------------------

Procedure

Compute importance

↓

Sort weights

↓

Remove lowest importance

↓

Fine-tune

↓

Repeat

--------------------------------

Limitation

Assumes weights
are independent.

Ignores interactions.

Cannot compensate errors.

--------------------------------

This limitation
leads to OBS.
