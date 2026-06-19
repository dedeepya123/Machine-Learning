Retriever vs Vector Search

Retriever and Vector Search are not the same.

---

Retriever:

Responsible for finding relevant documents.

Goal:

Question

↓

Relevant Documents

---

Vector Search:

One possible mechanism used by a retriever.

Goal:

Query Vector

↓

Nearest Document Vectors

---

Sparse Retrieval

Works using keywords.

Examples:

* TF-IDF
* BM25

Advantages:

Good at exact matching.

Fast.

---

Limitation:

Cannot understand semantic similarity.

Example:

reside ≠ live

as keywords.

---

Dense Retrieval

Uses embeddings.

Pipeline:

Query

↓

Embedding

↓

Vector Search

↓

Nearest Documents

---

Advantages:

Understands semantic meaning.

Example:

reside ≈ live

through embeddings.

---

Dense Retrieval uses Vector Search.

Vector Search is the search engine.

Retriever is the overall retrieval component.

---

Hybrid Retrieval

Combines:

Sparse Retrieval

*

Dense Retrieval

---

Benefits:

Exact keyword matching

*

Semantic matching

---

Hierarchy

Retriever

├── Sparse Retrieval

├── Dense Retrieval

│ └── Vector Search

└── Hybrid Retrieval

---

Main Insight:

Vector Search is a tool.

Retriever is the system that decides and finds relevant information.

---

Next Question:

How do we train dense retrievers so relevant documents become close to queries and irrelevant documents become far away?
