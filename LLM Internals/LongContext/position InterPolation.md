Position Interpolation (PI)

Problem:

Model trained on 2K context.

Want:

32K+ context.

Direct RoPE extrapolation causes distribution shift.

---

Core Idea:

Compress positions before applying RoPE.

Example:

p' = p × (2048 / 32768)

32K positions are squeezed into original 2K RoPE range.

---

Inside RoPE:

Original:

angle = p × θ

New:

angle = p' × θ

Only positions change.

RoPE frequencies remain unchanged.

---

Key Difference From RoPE Scaling:

RoPE Scaling:

Inference-only trick.

No weight updates.

---

Position Interpolation:

Uses fine-tuning.

Model weights are updated.

---

Fine-Tuning Process:

1. Start from pretrained model.
2. Use compressed positions.
3. Feed long-context documents.
4. Run normal forward pass.
5. Compute loss.
6. Backpropagate.
7. Update all weights using AdamW.

---

What Model Learns:

Compressed positional geometry now represents long contexts.

Model adapts attention patterns and retrieval behavior accordingly.

---

Core Insight:

Instead of forcing the model to extrapolate to unseen positional geometries,

keep geometry familiar and train the model to understand the compressed space.
