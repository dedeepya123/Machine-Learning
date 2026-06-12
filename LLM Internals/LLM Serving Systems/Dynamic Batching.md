## Dynamic Batching vs Continuous Batching

Static Batching → fixed batch, fixed execution.
Dynamic Batching → batch formed dynamically from arriving requests, but batch remains fixed once execution starts.
Continuous Batching → requests can join and leave while generation is already running.

## Memory Fragmentation

Requests continuously allocate and free KV cache memory.
Free memory becomes scattered.
Total free memory may be sufficient but not available as one large contiguous region.
Similar to classical OS memory fragmentation.

Deep Insight

Modern LLM serving increasingly starts looking like:

Operating Systems
+
Memory Management
+
Scheduling
+
GPU Programming

rather than only deep learning.
