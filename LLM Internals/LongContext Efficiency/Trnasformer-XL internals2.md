Transformer-XL Memory Mechanism (Deep Understanding)

First: What Does XL Mean?

Transformer-XL stands for:

Transformer eXtra Long

Goal:

Allow context to extend beyond a fixed-length segment.

---

What Is A Hidden State?

Consider layer l.

Input to layer l:

h^(l-1)

For all tokens:

H^(l-1)

Shape:

(seq_len, d)

Inside the layer:

Step 1:

Q = HWQ

K = HWK

V = HWV

---

Step 2:

Attention

A = Softmax(QK^T)

Z = AV

---

Step 3:

Residual

H' = H + Z

---

Step 4:

FFN

F = FFN(H')

---

Step 5:

Residual

H^(l) = H' + F

---

This:

H^(l)

is called the hidden state output of layer l.

Shape:

(seq_len, d)

---

Normal Transformer

Suppose:

Chunk 1

contains:

x1 ... x512

---

After Layer 1:

H1^(1)

After Layer 2:

H1^(2)

...

After Layer L:

H1^(L)

---

Normally after processing Chunk 1:

Throw everything away.

Process Chunk 2 independently.

Chunk 1 information is lost.

---

Transformer-XL Question

Researchers asked:

Why throw away these representations?

Can we keep useful information as memory?

---

Processing Chunk 1

Layer l produces:

H1^(l)

Store:

M^(l) = H1^(l)

This becomes memory for layer l.

Important:

Memory is stored separately for every layer.

So:

M^(1)

M^(2)

M^(3)

...

all exist independently.

---

Why Memory Per Layer?

Different layers learn different information.

Early layers:

Local syntax

---

Middle layers:

Entities
Relationships

---

Higher layers:

Semantics
Reasoning

---

Researchers wanted each layer to access its own historical representation.

---

Processing Chunk 2

Chunk 2 enters layer l.

Current chunk representation:

H2^(l-1)

---

Important Question:

How are Q, K, and V computed?

Queries:

Q = H2^(l-1)WQ

Queries come ONLY from the current chunk.

Why?

Because we are updating Chunk 2.

Chunk 1 is already finished.

---

Keys:

K = [M^(l), H2^(l-1)]WK

Memory and current chunk are concatenated.

---

Values:

V = [M^(l), H2^(l-1)]WV

Memory and current chunk are concatenated.

---

Attention

Current chunk tokens attend to:

Memory

*

Current chunk

Attention becomes:

Q[M,H]^T

where:

M = memory

H = current chunk

---

Interpretation

Memory acts as:

Read-only context

---

Current chunk acts as:

Representations being updated

---

Visual View

Layer l

Memory M(l)
|
v
K,V

Current Chunk H(l-1)
|
+--> Q
+--> K
+--> V

Attention:

Q attends to [Memory + Current Chunk]

---

Example

Chunk 1:

"Alice lives in Paris."

---

Chunk 2:

"She works at Google."

---

Normal chunking:

Chunk 2 cannot access Alice.

---

Transformer-XL:

Memory contains Chunk 1 representations.

When processing:

"She"

attention can look into memory.

Find:

"Alice"

Long-range dependency preserved.

---

What Exactly Is Stored?

Not:

Raw tokens

---

Not:

Embeddings

---

Not:

KV Cache

---

Stored:

H^(l)

the hidden state outputs of layer l.

These are already processed representations.

---

Difference From KV Cache

Transformer-XL:

Stores hidden states H

Then later recomputes K and V.

Purpose:

Extend context across chunks.

---

KV Cache:

Stores K and V directly.

Purpose:

Avoid recomputation during autoregressive decoding.

---

Completely different motivations.

---

Memory Update Question

Suppose:

Memory currently contains:

Chunk 1

M^(l) = H1^(l)

---

Now Chunk 2 finishes.

Layer l produces:

H2^(l)

What happens?

---

Naive Idea

Store:

H1^(l) + H2^(l)

---

Then after Chunk 3:

H1^(l) + H2^(l) + H3^(l)

---

Problem:

Memory grows forever.

Eventually becomes huge.

---

Transformer-XL Solution

Use a fixed-size rolling memory.

---

Example

Chunk size:

L = 512

Memory size:

M = 1024

---

After Chunk 1

Memory:

[Chunk1]

512 states

---

After Chunk 2

Memory:

[Chunk1, Chunk2]

1024 states

---

After Chunk 3

Would become:

[Chunk1, Chunk2, Chunk3]

1536 states

Too large.

---

Keep only latest M states.

Memory becomes:

[Chunk2, Chunk3]

---

After Chunk 4

Memory becomes:

[Chunk3, Chunk4]

---

Memory behaves like a sliding window.

---

Mathematical Update

After processing chunk t:

M(t+1)^(l)

=

Last M rows of

[M(t)^(l), H(t)^(l)]

Meaning:

Concatenate

Old Memory

*

Current Chunk Output

Then keep only the most recent memory length.

---

Visual Timeline

After Chunk1:

Memory:
[C1]

---

After Chunk2:

Memory:
[C1,C2]

---

After Chunk3:

Memory:
[C2,C3]

---

After Chunk4:

Memory:
[C3,C4]

---

Training Detail

Memory is usually detached from gradients.

Why?

Otherwise backpropagation would flow through unlimited history.

Training would become impossible.

So memory is used during forward attention,

but not for infinite backward propagation.

---

Core Insight

Researchers shifted from:

Store tokens

to

Store representations

---

Memory becomes:

Compressed history

---

The first major memory-augmented Transformer idea.

---

Mental Model

Think of memory as a rolling notebook.

For every chunk:

1. Read notebook

2. Process current chunk

3. Update notebook

Notebook has fixed size.

Old pages eventually get discarded.

---

One-Line Summary

Transformer-XL extends context by storing hidden-state representations from previous chunks as layer-wise memory, allowing current tokens to attend to past representations without reprocessing all previous tokens.
