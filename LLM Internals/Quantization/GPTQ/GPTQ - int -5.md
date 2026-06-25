Goal:

Preserve layer output

WX

--------------------------------

Quantize column i

wi → qi

--------------------------------

Error

ei = qi - wi

--------------------------------

Creates output error

ei xi

--------------------------------

Need compensation.

--------------------------------

Optimization:

Minimize

||(E + ΔW)X||²

--------------------------------

Hessian of objective:

H = XXᵀ

--------------------------------

Optimal OBS-style correction:

Δw

=

-(ei / (H⁻¹)ii)

(H⁻¹):,i

--------------------------------

(H⁻¹):,i

↓

Tells which columns
can absorb error.

--------------------------------

(H⁻¹)ii

↓

Normalizes correction amount.

--------------------------------

Correction applied only
to remaining FP columns.

--------------------------------

Already quantized columns
are frozen.

--------------------------------

Next column quantizes
the corrected weights,
not the original weights.
