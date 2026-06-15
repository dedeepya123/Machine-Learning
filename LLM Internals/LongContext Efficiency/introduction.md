## Long Context Efficiency - Beginning

Problem solved previously:

Can model represent and understand long contexts?

Solutions:

RoPE
NTK Scaling
Position Interpolation
YaRN

---

New Problem:

Even if model understands 128K or 1M tokens,

can we afford to compute attention over all of them?

---

Standard Attention:

Each token attends to all other tokens.

Attention matrix size:

N × N

Complexity:

O(N²)

---

Examples:

2K context:

~4 million attention entries

---

128K context:

~16 billion attention entries

---

1M context:

~1 trillion attention entries

---

FlashAttention does NOT solve O(N²).

It reduces memory movement and computes attention more efficiently.

Model still attends to everyone.

---

New Research Question:

Do we need full attention at all?

---

Core Insight:

In many situations information is local.

Current token often needs:

* nearby words
* nearby sentences
* nearby paragraphs

and only occasionally needs distant information.

---

Fundamental Tradeoff:

Full Attention

Pros:

* direct communication between any tokens

Cons:

* O(N²)

---

Sparse Attention

Pros:

* much cheaper

Cons:

* may lose long-range communication

---

Entire Long Context Efficiency Field:

Goal:

Preserve long-range reasoning

while avoiding full O(N²) attention.

---

Next Topic:

Sliding Window Attention

Idea:

Allow token to attend only to nearby tokens.
