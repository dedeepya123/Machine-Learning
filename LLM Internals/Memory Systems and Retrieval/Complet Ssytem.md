Step 0: We Have Documents

Suppose we have:

Doc 1:
OpenAI was founded by Sam Altman...

Doc 2:
Transformer architecture was introduced...

Doc 3:
Attention is all you need...
Step 1: Chunking

Modern RAG usually does NOT store entire documents.

Researchers learned:

Huge document
↓
Hard retrieval

So we split.

Example:

Doc 1

Chunk A:
OpenAI was founded by...

Chunk B:
OpenAI products...

Chunk C:
OpenAI research...

Now memory contains:

Chunk A
Chunk B
Chunk C
...

instead of whole documents.

Step 2: Embedding Generation

Now your question:

Which embedding model?

Depends on system.

Examples:

DPR encoder
Contriever
ColBERT encoder
E5
BGE
OpenAI embedding models

Conceptually:

Chunk
↓
Embedding Model
↓
Vector

Example:

Chunk A:
OpenAI was founded by Sam Altman

↓

v
A
	​

Chunk B:
OpenAI products include ChatGPT

↓

v
B
	​

Step 3: Store In Memory

We DON'T store only vectors.

We store:

ID = 101

Text:
OpenAI was founded by Sam Altman

Vector:
v_A

Think:

Memory Record

{
  text
  vector
  metadata
}

This is the mapping you were asking about.

Vector DB stores:

Vector
↓
Pointer
↓
Original Text

Very important.

The text is never lost.

Step 4: Query Arrives

User asks:

Who founded OpenAI?

Same embedding model.

Query
↓
Embedding Model
↓
q

Now we have:

q
Step 5: Vector Search

Now vector search finally enters.

We have:

Query Vector q

and

v_A
v_B
v_C
...

Search:

sim(q,v
i
	​

)

for nearest vectors.

This is exactly the vector search chapter we studied.

Result:

Nearest:

v_A
v_F
v_X
Step 6: Text Recovery

Vector DB says:

v_A
↓
ID 101
↓
Text:
OpenAI was founded by Sam Altman

This is why vector-to-text mapping exists.

We don't give vectors to LLM.

We recover:

Original Text
Now Let's Place DPR

DPR pipeline:

Chunk
↓
DPR Encoder
↓
ONE VECTOR

Stored:

Chunk A
↓
v_A

Query:

Question
↓
DPR Query Encoder
↓
q

Vector search:

q
vs

v_A
v_B
v_C

Simple.

Now Let's Place ColBERT

This is where confusion usually happens.

Instead of:

Chunk
↓
ONE VECTOR

ColBERT does:

Chunk
↓
Transformer
↓
Token Vectors

Example:

OpenAI
was
founded
by
Sam
Altman

↓

d
1
	​

,d
2
	​

,d
3
	​

,d
4
	​

,d
5
	​

,d
6
	​


So one chunk stores:

Chunk A

d₁
d₂
d₃
d₄
d₅
d₆

not one vector.

Query:

Who founded OpenAI

↓

q
1
	​

,q
2
	​

,q
3
	​


Now retrieval score becomes:

Query Token
↓
Best Matching
Document Token

(MaxSim)

Instead of:

q⋅d

like DPR.

Where Does Vector Search Happen In ColBERT?

This is the subtle part.

Vector search still exists.

But now it's searching among:

Token Vectors

rather than:

One Document Vector

Conceptually:

DPR:

Query Vector
↓
Search Document Vectors

ColBERT:

Query Token Vectors
↓
Search Token Representations

Same retrieval idea.

Richer matching.

The Entire Connected Picture
Documents
↓
Chunking
↓
Chunks

Chunk
↓
Embedding Model
(DPR / ColBERT / E5 / BGE ...)
↓
Vectors

Store:

{
  Text Chunk
  Vector(s)
}

inside Memory DB
(Vector Database)

--------------------------------

User Query
↓
Embedding Model
↓
Query Vector(s)

--------------------------------

Vector Search

Find nearest chunk vectors

--------------------------------

Recover Original Text

Chunk A
Chunk B
Chunk C

--------------------------------

Optional Reranker

Reorder chunks

--------------------------------

Build Prompt

Context:
Chunk A
Chunk B

Question:
...

--------------------------------

LLM

Reads TEXT

Reasons

Answers
Biggest Clarification

The thing I want you to remember is:

Retriever
≠
LLM

Retriever's job:

Text
↓
Vectors
↓
Find Relevant Chunks

LLM's job:

Relevant Chunks
↓
Reason
↓
Generate Answer

The LLM almost never sees the vectors.

The vectors are only an efficient indexing/search mechanism.
