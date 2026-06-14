## LLM Story So Far

1. How do models learn?
   → Training

2. How do models become useful?
   → Instruction Tuning + RLHF

3. How do models generate text?
   → Autoregressive Inference + KV Cache

4. How do we serve millions of users?
   → Continuous Batching

5. How do we store KV efficiently?
   → PagedAttention

6. How do we compute attention efficiently?
   → FlashAttention

New Bottleneck:

KV Cache memory.

Observation:

FlashAttention reduces attention computation cost but does not reduce KV cache size.

KV cache still grows with:

* Number of tokens
* Number of layers
* Number of heads

Research Question:

## Do we need separate K/V heads for every attention head?

Idea:

Keep separate Query heads.

Share K and V across heads.

Result:

Multi-Query Attention (MQA)

Benefits:

* Smaller KV cache
* Lower memory usage
* Better serving efficiency

Tradeoff:

Some quality loss.

Next Question:

Can we get most of the memory savings of MQA while keeping most of the quality of Multi-Head Attention?

This leads to Grouped Query Attention (GQA).
