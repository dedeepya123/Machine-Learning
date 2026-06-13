## FlashAttention on GPU

GPU Memory Hierarchy:

Registers
↓
Shared Memory
↓
HBM (GPU DRAM)

Goal:

Keep computation close to registers/shared memory and avoid repeated HBM accesses.

---

Standard Attention:

1. Compute S = QK^T
2. Write S to HBM
3. Read S
4. Compute Softmax
5. Write P
6. Read P
7. Compute PV

Problem:

Large N×N matrices repeatedly move between compute units and HBM.

Memory traffic dominates runtime.

---

FlashAttention:

Process attention block-by-block.

Example:

Block size = 128

Q block × K block
→ Local score matrix

Update:

* Running max (m)
* Running denominator (l)
* Running numerator (n)

Discard local score matrix.

Move to next block.

---

Key Difference:

The full N×N attention matrix is never materialized.

---

Training Benefits:

* Much lower memory usage
* Longer sequence lengths
* Larger batch sizes
* Reduced OOM issues

---

Inference Benefits:

* Efficient processing of long KV caches
* Less memory traffic
* Faster token generation

---

Deep Insight:

FlashAttention performs nearly the same mathematical operations as standard attention.

The speedup comes primarily from reducing memory movement, not reducing FLOPs.

---

Core Idea:

Fetch data once.
Reuse heavily.
Avoid HBM reads/writes.
Keep computation near fast memory.
