Vector Search Clarification

Embeddings and Vector Search are different.

---

Embedding Model

Creates semantic vectors.

Text

↓

Embedding

↓

Vector

---

Vector Search

Does not create embeddings.

Uses embeddings.

Goal:

Find nearest vectors efficiently.

---

Analogy

Embedding Model:

Creates GPS coordinates.

Vector Search:

Creates navigation system.

---

Researchers first tried:

Partition semantic space into clusters.

(K-Means, IVF, etc.)

---

Then asked:

Do humans search by regions?

Not really.

Humans often move from related concept to related concept.

---

New Idea:

Represent semantic space as a graph.

Each vector becomes a node.

Edges connect nearby vectors.

---

Search Process:

Start from some node.

↓

Move to better neighbor.

↓

Repeat.

↓

Reach target area.

---

This is graph-based retrieval.

---

Core Insight:

Instead of scanning vectors,

navigate through vectors.

---

Next Question:

Can we build multiple graph layers so search jumps across huge spaces quickly before zooming into local neighborhoods?

This leads to HNSW.
