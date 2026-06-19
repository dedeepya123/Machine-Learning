Late Interaction and ColBERT

Problem with DPR

Document

↓

Encoder

↓

One Vector

---

Issue:

A single vector must represent an entire document.

Long documents contain many topics.

Compression causes information loss.

---

Key Insight

One document vector becomes an information bottleneck.

---

Researchers ask:

Why compress all token representations into one vector?

Why not keep token-level information?

---

Transformer Output

Token1 → vector

Token2 → vector

Token3 → vector

...

---

Instead of:

All Tokens

↓

One Vector

Keep:

All Token Vectors

---

This leads to Late Interaction.

---

Late Interaction

Query Tokens:

q₁, q₂, ...

Document Tokens:

d₁, d₂, ...

---

For each query token:

Find best matching document token.

Example:

max(qᵢ · dⱼ)

---

Then aggregate scores.

---

This is the MaxSim idea.

---

ColBERT

(Contextualized Late Interaction over BERT)

One of the most important retrieval systems.

---

Advantages

Preserves token-level evidence.

Better retrieval quality.

Less information loss.

---

Tradeoff

More vectors.

More storage.

More compute.

---

Comparison

DPR:

One vector per document.

Fast.

---

ColBERT:

Many vectors per document.

More accurate.

---

Main Insight

DPR compresses.

ColBERT preserves.

Retrieval quality improves when token-level information is retained.

---

Next Question

If retrieval itself becomes powerful, how do modern systems combine retrieval, reranking, memory, and reasoning into a complete production-grade RAG pipeline?
