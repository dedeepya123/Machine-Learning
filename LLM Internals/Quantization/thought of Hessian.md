Goal

Quantization changes weights.

Need to estimate:

Loss increase after quantization.

--------------------------------

First Derivative

dL/dw

Tells:

Slope

Direction training should move.

--------------------------------

Problem

After training:

dL/dw ≈ 0

Therefore gradient gives little
information about quantization damage.

--------------------------------

Second Derivative

d²L/dw²

Tells:

Curvature

Sensitivity of loss to movement.

--------------------------------

Small Curvature

Flat valley

Weight can move safely.

--------------------------------

Large Curvature

Sharp valley

Small movement increases loss greatly.

--------------------------------

Taylor Expansion

Used to estimate:

L(w + Δw)

using local information.

--------------------------------

Expansion gives:

Current loss

+

Gradient term

+

Curvature term

--------------------------------

After training

Gradient term ≈ 0

Therefore:

ΔL ≈ 1/2 ΔwᵀHΔw

--------------------------------

Hessian

Matrix of second derivatives.

Represents curvature/sensitivity
for all weights together.

--------------------------------

Importance is NOT Hessian alone.

Need:

Quantization Error

Δw

+

Sensitivity

H

Together determine:

Loss increase.
