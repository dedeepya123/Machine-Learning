## What is a Serving System?

A serving system is the software responsible for running LLM inference for many users efficiently.

Responsibilities:

* Accept requests
* Queue requests
* Schedule requests
* Manage KV cache
* Batch requests
* Execute GPU workloads
* Return responses

What is vLLM?

vLLM is an open-source LLM inference and serving framework.

It is not a model.

It is infrastructure used to serve models efficiently.

What does vLLM manage?

* Continuous batching
* Scheduling
* PagedAttention
* KV cache memory
* GPU execution

What does the "v" mean?

Inspired by the idea of virtual memory.

PagedAttention uses concepts similar to OS paging and page tables.

Is vLLM an OS?

No.

But conceptually it behaves somewhat like a mini operating system for LLM inference because it manages memory, scheduling, and resources.

Model vs Serving System:

Llama → Model

vLLM → Serving Framework

Deep Insight:

Training teaches the model.

Serving systems make the model usable at scale.
