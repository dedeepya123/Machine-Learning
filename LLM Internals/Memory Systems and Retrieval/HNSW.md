HNSW (Hierarchical Navigable Small World)

Problem:

A single graph still becomes huge for billions of vectors.

Search may require many hops.

---

Human Navigation Insight:

Humans navigate:

Global
↓
Regional
↓
Local

Not tiny step-by-step movement.

---

Researchers asked:

Can vector search also happen at multiple scales?

---

Core Idea:

Build multiple graph layers.

Top Layer:

Few nodes.

Long-range jumps.

---

Middle Layers:

Moderate detail.

---

Bottom Layer:

All vectors.

Maximum precision.

---

Search Procedure:

Start at top layer.

↓

Navigate greedily.

↓

Find good region.

↓

Descend one level.

↓

Repeat.

↓

Reach bottom layer.

↓

Retrieve nearest vectors.

---

Small World Property:

Large networks can be traversed in surprisingly few hops if long-range and local connections both exist.

---

HNSW Combines:

1. Local Connections

Precise search.

2. Long-Range Connections

Fast movement.

3. Hierarchical Layers

Global → Local navigation.

---

Result:

Very fast approximate nearest neighbor retrieval.

Used heavily in modern vector databases.

---

Main Insight:

HNSW is an indexing structure for semantic memory.

It organizes embeddings so nearest memories can be found efficiently without scanning all vectors.

---

Next Question:

After retrieving memories, how do we combine them with an LLM so the model can actually use the retrieved information?

This leads to Retrieval-Augmented Generation (RAG).
