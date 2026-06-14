## Why does Multi-Query Attention work even though all heads share the same K and V?

Initial Intuition:

In Multi-Head Attention every head has:

Q_i, K_i, V_i

Each head learns different behaviors.

Therefore it seems every head needs separate K and V.

---

Researcher Insight:

Most specialization appears to come from Queries.

Query answers:

"What am I searching for?"

Key answers:

"What information does this token contain?"

---

MQA Idea:

Keep:

Q_1, Q_2, ..., Q_h

Share:

K_shared
V_shared

---

Why It Still Works:

Attention score:

score = QK^T

Even if K is shared:

Q_1 K^T

Q_2 K^T

Q_3 K^T

are different because queries are different.

Different heads can still attend differently.

---

Memory Benefit:

Traditional MHA:

h K heads
h V heads

MQA:

1 K head
1 V head

KV cache memory becomes much smaller.

---

Why Quality Does Not Collapse:

Many attention heads learn similar or redundant K/V representations.

Queries still provide substantial specialization.

---

Limitation:

Sharing one K/V head reduces expressiveness.

Some quality loss is observed.

This motivates GQA (Grouped Query Attention).
