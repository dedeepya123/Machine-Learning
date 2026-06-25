OBS

Objective:
Final model loss

Hessian tells:

How sensitive loss is
to weight changes.

Diagonal:
Weight sensitivity

Off-diagonal:
Weight interactions

--------------------------------

GPTQ

Objective:

||WX - ŴX||²

Preserve layer output.

--------------------------------

X

=

Activations entering
a weight matrix.

--------------------------------

XXᵀ captures:

Which activation directions
are important.

Which activation dimensions
occur together.

--------------------------------

Not weight interactions.

Activation interactions.

--------------------------------

Weight importance now depends on:

Weight

×

Activation statistics

--------------------------------

If activation dimension
rarely appears

↓

Weight can be quantized
more aggressively.

--------------------------------

Each matrix has its own X.

Examples:

WQ → input to Q projection

WK → input to K projection

WV → input to V projection

MLP weights → MLP input

--------------------------------

XXᵀ acts as a local Hessian
for the layer reconstruction
objective.
