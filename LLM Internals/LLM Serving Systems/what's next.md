## Where are we now?

Completed:

1. LLM Learning

   * Pretraining
   * Scaling Laws
   * GPT-3
   * Instruction Tuning
   * RLHF

2. LLM Internals

   * Transformer
   * Forward Pass
   * Backprop
   * Optimizers
   * Training Pipeline

3. LLM Inference

   * Autoregressive Generation
   * KV Cache
   * Inference Internals

4. LLM Serving Systems

   * Batching
   * Continuous Batching
   * PagedAttention
   * vLLM

Next Chapter:

## LLM Inference Efficiency

Main Research Question: Can we make Transformer computation itself faster?

Researcher Discovery:

Attention was often limited not by computation but by memory movement.

This led to a new line of research:

Memory-Bound Computation
→ IO Efficiency
→ FlashAttention

Next Question:

Why can GPUs be extremely powerful yet still spend most of their time waiting for memory?
