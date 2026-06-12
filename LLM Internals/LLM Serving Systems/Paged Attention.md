## Why was PagedAttention introduced?

Problem:

Continuous batching causes requests to constantly enter and leave.

KV cache memory is repeatedly allocated and freed.

This creates memory fragmentation.

Traditional Approach:

Store KV cache as one contiguous memory region.

Issue:

Total free memory may be sufficient.

But a large contiguous region may not exist.

Result:

Poor memory utilization.

Researcher Insight:

Does KV cache really need contiguous memory?

Operating systems solved a similar problem using paging.

Idea:

Split KV cache into fixed-size blocks.

Store blocks anywhere in GPU memory.

Maintain a mapping table from logical blocks to physical blocks.

Benefits:

* Eliminates most fragmentation
* Better memory utilization
* More concurrent requests
* Higher throughput
* Lower serving cost

Deep Intuition:

PagedAttention treats KV cache similarly to how operating systems treat virtual memory.

Logical KV blocks are mapped to physical memory blocks.

Key Insight:

The breakthrough was not in Transformer math.

It was in memory management.

Historical Impact:

PagedAttention became the foundation of vLLM and modern high-performance LLM serving systems.

## Summary
PagedAttention eliminates KV-cache memory fragmentation by storing KV caches in fixed-size blocks instead of requiring contiguous memory allocation. A mapping table translates logical KV blocks to physical memory blocks, similar to how virtual memory uses page tables in operating systems. This greatly improves GPU memory utilization and serving throughput.
