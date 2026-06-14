## Long Context Era

Story So Far:

Training
→ Alignment
→ Inference
→ Serving
→ PagedAttention
→ FlashAttention
→ MQA/GQA

Researchers solved many inference bottlenecks.

New User Demand:

* Entire books
* Entire repositories
* Long conversations
* Large documents

Context windows started growing:

512
→ 2K
→ 8K
→ 32K
→ 128K
→ 1M+

---

New Observation:

FlashAttention reduces attention computation cost.

GQA reduces KV cache size.

But KV cache still grows linearly with context length.

Memory ∝ Context Length

---

Key Realization:

Long context is largely a memory problem.

Every new token adds KV cache entries at every layer.

Nothing is automatically removed.

---

Research Question:

Do we really need to remember every token equally?

This motivates:

* KV cache compression
* Sparse attention
* Retrieval systems
* Long context architectures

---

Before solving these, researchers encountered a more fundamental problem:

If a model was trained on 2K tokens, how can it operate at 32K or 128K tokens? 
This leads to positional encoding and RoPE.
