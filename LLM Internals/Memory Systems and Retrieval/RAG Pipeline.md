Modern Production RAG Pipeline

Documents
↓
Embedding Model
↓
Vectors Stored

--------------------------------

User Query
↓
Query Embedding
↓
Vector Search
↓
Top-K Document Chunks

Important:

LLM does NOT receive vectors.

LLM receives original text chunks.

--------------------------------

Reranker

Input:

Question + Chunk

Goal:

Reorder retrieved chunks by relevance.

More accurate than retriever.

--------------------------------

Prompt Construction

Context:
Chunk A
Chunk B
Chunk C

Question:
...

--------------------------------

LLM

Reads:
Context + Question

Performs:
Reasoning
Summarization
Generation

--------------------------------

Responsibilities

Memory System:
Stores information

Retriever:
Finds candidate information

Vector Search:
Efficient search engine

Reranker:
Selects best information

LLM:
Reasons over retrieved information

--------------------------------

Big Insight

Modern AI systems are often:

Memory
+
Retriever
+
Vector Search
+
Reranker
+
LLM

working together.
