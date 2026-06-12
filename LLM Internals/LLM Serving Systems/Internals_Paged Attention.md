## What is a logical block in PagedAttention?

Logical Block:

Represents the position of KV cache data in the sequence.

Example:

Logical Block 0 -> Tokens 1-16

Logical Block 1 -> Tokens 17-32

Logical Block 2 -> Tokens 33-48

Logical Block 3 -> Tokens 49-64

Logical blocks describe sequence order.

They do not describe physical memory location.

Physical Block:

Actual GPU memory location storing KV data.

Example:

Logical 0 -> Physical 22

Logical 1 -> Physical 5

Logical 2 -> Physical 17

Logical 3 -> Physical 8

Mapping Table:

Maintains logical-to-physical mapping.

Similar to OS page tables.

How Attention Works:

Attention still computes:

softmax(QK^T)V

Nothing changes mathematically.

Only KV retrieval changes.

Using the mapping table:

Attention gathers KV blocks from their physical locations and performs normal attention computation.

Key Insight:

PagedAttention changes memory management, not Transformer mathematics.

Deep Intuition:

KV cache becomes a collection of pages instead of one large contiguous array.

This is conceptually similar to virtual memory in operating systems.

## Summary 
Prefill allocates enough logical blocks to hold prompt KV cache.
Each logical block maps to a physical GPU memory block.
Generated tokens are appended into the current last block.
A new physical block is not allocated for every token.
New block allocation happens only when the current block becomes full.
KV cache therefore grows block-by-block as generation proceeds.
This is conceptually similar to pages in OS memory management.
Small unused space may exist in the final block (internal fragmentation), but overall memory utilization is much better than requiring large contiguous allocations.
