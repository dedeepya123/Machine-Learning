Memory Access - Efficient Search

Problem:

We can represent memories as embeddings.

We can compare embeddings using cosine similarity or dot product.

But retrieval is still expensive.

---

Brute Force Retrieval

Given:

Query embedding q

Memory embeddings:

m1,m2,...,mN

Compute:

q·m1

q·m2

...

q·mN

Then choose highest similarity.

---

This is Exact Nearest Neighbor Search.

Advantages:

Always correct.

---

Disadvantages:

Must compare against every memory.

Complexity:

O(N)

Does not scale to millions or billions of memories.

---

Important Observation:

Memory retrieval now faces a problem similar to attention.

More memories

↓

More comparisons

↓

More compute

---

Researchers ask:

Can we find relevant memories without comparing against every memory?

---

Human Analogy:

Humans do not scan every memory.

Relevant regions become active.

---

Key Insight:

Semantic space itself should help search.

Nearby meanings are already clustered together.

---

New Goal:

Find nearest memories efficiently.

Not necessarily exactly.

---

This leads to Approximate Nearest Neighbor Search (ANN).

Tradeoff:

Slightly less accuracy

for

massive speed improvement.

---

Next Question:

How can semantic space be organized into regions so search only visits relevant areas instead of scanning all memories?
