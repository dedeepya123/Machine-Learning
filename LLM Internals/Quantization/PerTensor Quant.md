Per-Tensor Quantization

Entire Weight Matrix

↓

One Scale

↓

One Zero Point

--------------------------------

Problem

Some channels contain:

0.01
0.02
0.03

Others contain:

12
15
-10

--------------------------------

Large values determine scale.

Small values lose precision.

May collapse to zero.

--------------------------------

This increases:

Quantization Error

--------------------------------

Research Question

Why use one ruler
for entire matrix?

--------------------------------

Per-Channel Quantization

Each channel gets:

Own Scale

Own Zero Point

--------------------------------

Benefits

Preserves small values.

Reduces quantization error.

Improves model quality.

--------------------------------

Deep Intuition

Per-Tensor

=

One ruler for everyone

Per-Channel

=

Each channel gets
its own ruler
