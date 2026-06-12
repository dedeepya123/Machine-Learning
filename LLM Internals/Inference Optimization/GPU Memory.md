## Why can a GPU perform trillions of operations per second yet still be slow?

Key Insight:

Performance depends on:

Performance = Computation + Data Movement

Not computation alone.

Memory Hierarchy:

Registers
↓
Shared Memory
↓
HBM (GPU DRAM)

Closer memory is much faster.

Concepts:

Compute-Bound:

* Computation dominates runtime.
* Faster computation improves performance.

Memory-Bound:

* Data movement dominates runtime.
* Faster computation gives little benefit.
* Need to reduce memory traffic.

Arithmetic Intensity:

Arithmetic Intensity = FLOPs / Bytes Moved

Measures how much computation is performed per byte transferred.

High intensity:
→ More compute-bound

Low intensity:
→ More memory-bound

Research Discovery:

Attention was often memory-bound.

GPU spent large amounts of time moving attention matrices between memory levels rather than performing computation.

Deep Insight:

The bottleneck was not math.

The bottleneck was memory movement.

This observation led directly to FlashAttention.
