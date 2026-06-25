GPTQ is NOT training.

No SGD.

No epochs.

No backprop.

--------------------------------

Calibration samples

↓

Only used to collect
activation statistics.

--------------------------------

For each sample

activation vector xi

--------------------------------

Layer Hessian

H

=

Σ xi xiᵀ

=

XXᵀ

--------------------------------

One Hessian is built
using all samples.

Not one Hessian per sample.

--------------------------------

Different samples may want
different compensations.

H averages their importance.

--------------------------------

Final weights are obtained
in one quantization pass.

No repeated optimization.

--------------------------------

GPTQ computes H⁻¹ once.

--------------------------------

After quantizing a column

↓

Compensate remaining columns

↓

Update H⁻¹

↓

Continue

--------------------------------

No reinversion required.

Matrix-update formulas
allow efficient updates.

--------------------------------

This is what makes GPTQ
practical for LLMs.
