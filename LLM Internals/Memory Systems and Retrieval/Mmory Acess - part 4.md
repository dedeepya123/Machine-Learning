Memory Access - Similarity Metrics

Problem:

Once meanings become vectors,

how do we determine whether two meanings are similar?

---

1. Euclidean Distance

Measures geometric distance.

Formula:

d(x,y)=√Σ(xᵢ-yᵢ)²

Small distance → close vectors.

Large distance → far vectors.

---

Limitation:

Two vectors can point in the same direction but have very different magnitudes.

Distance may still be large.

---

2. Dot Product

Formula:

a·b = Σ(aᵢbᵢ)

Measures alignment between vectors.

Large positive value:

Similar directions.

Zero:

Unrelated.

Negative:

Opposite directions.

---

Important Identity:

a·b = |a||b|cos(θ)

Dot product depends on:

* magnitude
* angle

---

3. Cosine Similarity

Formula:

(a·b)/(|a||b|)

Magnitude cancels.

Only angle remains.

Result:

cos(θ)

---

Interpretation:

1 → same direction

0 → unrelated

-1 → opposite directions

---

Why Cosine Similarity Is Popular

Semantic meaning often depends on direction rather than magnitude.

Words with similar meanings tend to have similar directions.

---

Connection To Attention

Attention computes:

QKᵀ

which is a similarity score.

Therefore attention itself performs a form of similarity search.

---

Big Insight

Attention Retrieval:

Find relevant information inside context.

Memory Retrieval:

Find relevant information inside external memory.

Both rely on vector similarity.

---

Main Insight:

Meaning Similarity becomes Vector Similarity.

This is the foundation of embeddings, retrieval systems, vector databases, RAG, and memory access.
