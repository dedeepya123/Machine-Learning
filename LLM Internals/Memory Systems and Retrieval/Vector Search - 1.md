Vector Search - First Organizing Idea

Problem:

Brute force retrieval compares query against every memory.

Complexity:

O(N)

Not practical for millions or billions of vectors.

---

Key Insight:

Organize semantic space into regions.

Search relevant regions only.

---

Analogy:

Google Maps does not search every coffee shop on Earth.

It first narrows search to nearby regions.

---

Researchers apply the same idea to embeddings.

---

Method:

Partition vector space.

Create clusters.

Store nearby vectors together.

---

K-Means Clustering

Goal:

Create K clusters.

Each cluster has a centroid.

---

Algorithm:

1. Initialize centroids.

2. Assign vectors to nearest centroid.

3. Move centroid to cluster average.

4. Repeat until convergence.

---

Retrieval:

Query

↓

Find nearest centroid

↓

Search vectors inside that cluster

---

Advantages:

Much fewer comparisons.

Large speedup.

---

Limitation:

Nearest neighbor may lie in adjacent cluster.

Therefore search becomes approximate.

---

Approximate Nearest Neighbor Search (ANN)

Tradeoff:

Slight loss in accuracy

for

massive speed improvement.

---

Main Insight:

Instead of searching all vectors,

search only the most relevant region.

---

Next Question:

Can we organize vectors so search navigates through nearby vectors like a graph instead of relying only on clusters?

This leads to graph-based retrieval and HNSW.
