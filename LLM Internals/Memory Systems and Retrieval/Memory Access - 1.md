Memory Access - Part 1

Relevance

Core Question:

Given a query and many memories,

how does the system know which memory is relevant?

---

First Idea:

Match words.

Example:

Query:

"Where does Alice live?"

Memory:

"Alice lives in Paris."

Shared word:

Alice

---

Problem:

Query:

"What city does Alice reside in?"

Memory:

"Alice lives in Paris."

Words differ.

Meaning is same.

Humans retrieve correctly.

Simple word matching fails.

---

Key Insight:

Relevance is not based on words.

Relevance is based on meaning.

---

Researchers discovered two notions of similarity.

1. Lexical Similarity

Similarity of words.

Examples:

cat ↔ cat

Alice ↔ Alice

---

2. Semantic Similarity

Similarity of meaning.

Examples:

live ↔ reside

car ↔ automobile

---

Humans primarily use semantic similarity.

---

Memory Access Problem:

A useful memory may contain different words than the query.

Therefore memory retrieval cannot rely only on exact token matching.

---

Main Insight:

Relevance = Meaning Similarity

not

Relevance = Word Overlap

---

This creates the next research question:

How can meaning be represented mathematically so computers can compare meanings efficiently?

This leads to embeddings.
