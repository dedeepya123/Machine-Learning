Quantization introduces:

Δw₁

--------------------------------

Question

Can remaining weights
compensate?

--------------------------------

Loss Approximation

ΔL ≈ 1/2 ΔwᵀHΔw

--------------------------------

Fixed

Δw₁

--------------------------------

Choose

Δw₂

to minimize loss.

--------------------------------

Interaction Term

H₁₂

determines whether
compensation is possible.

--------------------------------

Large H₁₂

↓

Strong compensation possible.

--------------------------------

Small H₁₂

↓

Weights nearly independent.

--------------------------------

Optimal Compensation

Move other weights
in opposite direction
to reduce loss increase.

--------------------------------

Key Insight

Quantization error can be
redistributed through
the network.

--------------------------------

Birth of

Error Compensation

--------------------------------

Research Split

Ignore compensation

↓

OBD

Use compensation

↓

OBS
