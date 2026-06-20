Quantization Error

Quantization maps:

Original Weight

↓

Nearest Integer Level

--------------------------------

Example

0.126731

↓

0.125

Error

=

0.001731

--------------------------------

Quantization Error

=

Original Weight

-

Recovered Weight

--------------------------------

Why Error Happens

Continuous values

↓

Discrete Levels

Need snapping.

--------------------------------

INT8

256 levels

Small step size

Low error

--------------------------------

INT4

16 levels

Large step size

Higher error

--------------------------------

Fewer Bits

↓

Fewer Levels

↓

Larger Step Size

↓

More Quantization Error

--------------------------------

Tradeoff

More Bits

=

More Memory
Less Error

Less Bits

=

Less Memory
More Error

--------------------------------

Observation

Neural Networks are robust.

Small errors often do not
significantly affect outputs.

--------------------------------

Next Insight

Not all weights are equally important.

Why use the same quantization
for every weight?

This leads to:

Per-Tensor

vs

Per-Channel Quantization.
