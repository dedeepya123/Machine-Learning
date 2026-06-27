Why does an LLM generate one token at a time?

Because an autoregressive transformer models

P(xt ∣ x<t),

meaning each new token depends on all previously generated tokens.

The model cannot compute token t+2 until token t+1 is known.

Why is this now the bottleneck?

We've already made each forward pass much cheaper through FlashAttention, KV cache optimizations, and quantization.

However, a long response still requires one forward pass per decoding step, creating a fundamentally sequential process that limits GPU utilization.

The New Research Question

Instead of asking:

"How do we make one decoding step faster?"

researchers began asking:

"Can we safely predict several future tokens cheaply and then have the large model verify them all at once, reducing the number of expensive decoding steps?"

That question is the birth of Speculative Decoding.
