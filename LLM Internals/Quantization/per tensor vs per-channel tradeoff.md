Per-Tensor

One Matrix

↓

One Scale

Benefits:

Simple
Fast
Hardware Friendly

Problem:

Higher Quantization Error

--------------------------------

Per-Channel

Each Channel

↓

Own Scale

Benefits:

Preserves Precision

Reduces Error

Better Accuracy

--------------------------------

Costs

1. More Scales To Store

2. More Bookkeeping

3. Less Uniform Computation

4. Slightly More Complex Inference

--------------------------------

Tradeoff

Per-Tensor

=

Simpler

Per-Channel

=

More Accurate

--------------------------------

Research Observation

Per-Channel often gives
significant accuracy gains
for relatively small extra cost.

--------------------------------

Next Natural Question

Even within a channel,
are all weights equally important?

If not,

how do we measure
weight importance?
