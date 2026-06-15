## Transformer-XL

Problem:

Full Attention:

Expensive

O(N²)

---

Sliding Window:

Efficient

But forgets distant information.

---

Sparse Attention:

Adds shortcuts

But attention patterns are manually designed.

---

New Question:

Why repeatedly attend to old tokens?

Can model remember useful information instead?

---

Core Idea:

Process text in chunks.

Example:

Chunk1
Chunk2
Chunk3

---

After processing a chunk:

Store hidden states.

These become memory.

---

When processing next chunk:

Attention can see:

Previous Memory

*

Current Chunk

---

Attention becomes:

Q[M,H]^T

where:

M = memory

H = current chunk

---

Benefits:

Long-range information survives across chunks.

Model can access information beyond local window.

---

Important:

Transformer-XL memory is NOT KV Cache.

KV Cache:

Inference optimization.

---

Transformer-XL:

Architectural memory mechanism.

---

Key Insight:

Instead of attending to all previous tokens,

carry useful representations forward.

---

Research Shift:

Full Attention

↓

Sparse Connections

↓

Memory

---

Next Question:

Do we really need to store all previous hidden states?

Can we store only the important information?

This eventually leads toward retrieval and modern memory systems.
