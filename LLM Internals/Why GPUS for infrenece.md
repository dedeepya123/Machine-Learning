## If inference is sequential, why are GPUs still useful?

Researcher Observation:

Inference generates tokens one-by-one.

This creates a sequential dependency.

However:

Generating a single token still requires running the entire Transformer.

Important Insight:

Inference is sequential across generated tokens.

But computation inside one token is massively parallel.

For every generated token:

* All Transformer layers execute.
* All attention blocks execute.
* All FFN blocks execute.
* All model parameters participate.

Most Computation:

The majority of Transformer computation consists of:

Matrix Multiplications

Examples:

Q = XWQ

K = XWK

V = XWV

FFN projections

Output projections

GPU Role:

GPUs are optimized for performing huge numbers of matrix multiplications simultaneously.

Deep Intuition:

A GPU is essentially a massive matrix multiplication engine.

Another Bottleneck:

Researchers discovered that inference is often not limited by computation alone.

Large models require constantly reading billions of parameters from GPU memory.

This creates:

Memory Bandwidth Bottlenecks

Sometimes GPUs spend more time moving weights than multiplying them.

Final Mental Model:

Training:

Parallel across tokens.

Inference:

Sequential across generated tokens.

But every generated token still requires enormous parallel computation inside the Transformer.

This is why GPUs remain essential for LLM inference.
