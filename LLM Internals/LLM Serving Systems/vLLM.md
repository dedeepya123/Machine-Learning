## If PagedAttention solved fragmentation, why was vLLM needed?

Observation:

PagedAttention solves how KV cache is stored.

It does not solve the entire serving problem.

Problems Before vLLM:

1. Static batching wastes GPU utilization.
2. Continuous batching causes memory fragmentation.
3. Traditional serving systems often reserve large KV-cache memory regions in advance.

Issue:

A request may reserve memory for hundreds or thousands of future tokens that are never generated.

Large amounts of GPU memory are wasted.

Researcher Insight:

Using paged blocks, memory can grow incrementally.

Allocate blocks only when needed.

This is similar to demand paging in operating systems.

PagedAttention:

* KV cache split into fixed-size blocks
* Logical-to-physical mapping
* Reduced fragmentation

vLLM:

A complete serving architecture including:

* Scheduler
* Continuous batching
* PagedAttention memory management
* Efficient GPU execution

Deep Insight:

PagedAttention is a memory-management technique.

vLLM is a full serving system built around it.

Historical Lesson:

Major serving improvements often come from systems engineering rather than changing the Transformer itself.

Result:

Same GPU
→ Higher memory utilization
→ More concurrent requests
→ Higher throughput
→ Lower cost
