Memory Systems - Beginning

Transformer-XL introduced memory.

Stores hidden-state representations across chunks.

---

Problem:

Transformer-XL keeps recent information.

Not necessarily important information.

---

Observation:

Recent ≠ Important

---

Human memory does not work by recency alone.

Humans remember:

* important facts
* entities
* events

and forget many recent but unimportant details.

---

New Research Question:

Instead of:

How much history should we keep?

Ask:

Which information is worth keeping?

---

Key Shift:

Store important information

instead of

storing latest information.

---

Memory cannot grow forever.

Otherwise memory itself becomes another huge context window.

---

Therefore memory must be selective.

---

Goal:

Store compressed useful knowledge.

Not raw history.

---

New Problem:

After storing information:

How do we find the right memory later?

---

Storage and Retrieval are different problems.

Memory without retrieval is like a library without a catalog.

---

New Architecture:

Model

*

External Memory

*

Retrieval Mechanism

---

This becomes foundation for:

RAG

Agent Memory

Vector Databases

Modern Retrieval Systems

---

Next Question:

How can we represent meaning mathematically so that relevant memories can be found efficiently?

This leads to:

Embeddings and Similarity Search.
