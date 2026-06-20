## LLM Memory

1. Weights
   Learned parameters
   Biggest memory consumer

2. Activations
   Intermediate computations

3. KV Cache
   Stores past attention states

--------------------------------

7B Model

7 Billion Parameters

FP16:

1 Parameter = 2 Bytes

Total:

≈14GB

--------------------------------

Key Observation

Most memory is spent storing
billions of weight values.

Researchers ask:

Do we really need all 16 bits
for every weight?

This question leads to Quantization.
