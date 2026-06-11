## Phases of LLM Inferene

LLM inference consists of:

Prefill Phase — process the entire prompt, compute activations, and build the KV cache.
Decoding Phase — generate tokens sequentially using the KV cache.

Prefill is compute-intensive and highly parallelizable, while decoding is sequential and often underutilizes GPU compute resources.

## What was the first problem researchers faced when serving LLMs to many users?

Observation:

Inference is not a single workload.

It has two very different phases.

Phase 1: Prefill

Input prompt is processed.

All prompt tokens are run through the Transformer.

KV cache is built.

Characteristics:

* Highly parallel
* Large matrix multiplications
* High GPU utilization
* Similar to training forward pass

Phase 2: Decoding

Tokens are generated one at a time.

Uses KV cache.

Characteristics:

* Sequential
* Cannot parallelize across future tokens
* Lower GPU utilization
* Dominates latency for long outputs

Researcher Discovery:

A single user often cannot fully utilize a modern GPU during decoding.

Large portions of the GPU remain idle.

Analogy:

Using a 100-seat bus to transport one passenger.

First Serving Insight:

To improve utilization, researchers asked:

"Can multiple users share the same GPU simultaneously?"

This idea became:

Batching

Next Research Question:

If requests have different lengths and arrive at different times, how can batching actually work efficiently?
