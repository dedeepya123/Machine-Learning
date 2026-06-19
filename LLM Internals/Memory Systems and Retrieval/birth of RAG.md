Birth of RAG

Problem:

Memory retrieval can find information.

But retrieval alone is not useful.

The LLM must be able to use the retrieved information.

---

Before RAG

Knowledge stored inside model weights.

This is called Parametric Knowledge.

Advantages:

Fast access.

Disadvantages:

Hard to update.

Requires retraining.

Knowledge becomes stale.

---

Researchers ask:

Why store all knowledge in weights?

Why not retrieve knowledge when needed?

---

Key Insight

Separate:

Knowledge

and

Reasoning

---

Knowledge:

External Memory

Reasoning:

LLM

---

RAG Pipeline

Question

↓

Embedding

↓

Vector Search

↓

Retrieve Relevant Documents

↓

Append Retrieved Context To Prompt

↓

LLM Reads Context

↓

Generate Answer

---

Meaning of RAG

Retrieval:

Find relevant information.

Augmented:

Add retrieved information to model input.

Generation:

Generate final response.

---

Human Analogy

Humans often:

Search

↓

Read

↓

Reason

↓

Answer

RAG gives LLMs a similar workflow.

---

Big Conceptual Shift

Before:

Knowledge + Reasoning = Model Weights

After:

Knowledge = External Memory

Reasoning = LLM

---

Connection To Previous Topics

Memory Systems

↓

Vector Search

↓

Retrieval

↓

RAG

---

Next Question

What if retrieval is imperfect?

How do we ensure the retriever finds the best information?

This leads to Dense Retrieval, Sparse Retrieval, Hybrid Retrieval, and Reranking.
