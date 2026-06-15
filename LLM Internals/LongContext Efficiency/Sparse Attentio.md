## Sparse Attention

Problem:

Sliding Window Attention is efficient.

But long-range communication disappears.

---

Observation:

Most attention connections are unnecessary.

Only a small number of long-range connections are important.

---

Idea:

Keep:

Local attention

*

Add a few long-range connections.

---

Full Attention:

Each token attends to N tokens.

Complexity:

O(N²)

---

Sparse Attention:

Each token attends to:

w + g

where:

w = local window

g = small number of global links

---

Complexity:

O(N(w+g))

Much smaller than O(N²).

---

Benefits:

* Preserves local reasoning
* Allows some long-range retrieval
* Much cheaper than full attention

---

Information Flow:

Sliding Window:

Information moves hop-by-hop.

---

Sparse Attention:

Long-range shortcut connections exist.

Information travels faster.

---

Key Design Question:

Which tokens should have global connections?

Common Patterns:

1. Fixed stride tokens

2. Global hub tokens

3. Block sparse attention

---

Examples:

Sparse Transformer

Longformer

BigBird

---

Main Tradeoff:

Efficiency ↑

Long-range communication partly preserved

But attention pattern must be manually designed.

---

Next Research Question:

Instead of manually designing sparse links,

can we carry information forward as memory?

This leads to Transformer-XL.
