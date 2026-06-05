# Self-Attention: Intuition and Motivation

## Problem

In language, the meaning of a word depends on its surrounding words.

Example:

```text
The animal near the river was tired.
```

To understand the word "tired", information about "animal" is important.

Therefore, we need a mechanism that transforms a word's semantic representation into a contextual representation.

---

## How RNNs Solve This

RNNs build contextual representations sequentially.

```text
word1 → word2 → word3 → ...
```

Each hidden state carries information from previous words.

This allows semantic representations to gradually become contextual representations.

### Limitations

* Sequential computation
* Difficult parallelization
* Long information paths
* Long-range dependencies are harder to learn

---

## Key Insight from Attention

Bahdanau Attention introduced a new idea:

Instead of forcing all information to be remembered, retrieve relevant information when needed.

Researchers realized:

```text
Retrieval > Remembering Everything
```

This led to the idea of Self-Attention.

---

## Main Idea of Self-Attention

Instead of building context through recurrence, allow every word to directly interact with every other word.

Goal remains:

```text
Semantic Representation
        ↓
Contextual Representation
```

But context is now built through retrieval rather than sequential memory propagation.

---

## Query, Key, and Value

Each word learns three different representations.

### Query (Q)

Represents:

```text
What information am I looking for?
```

or

```text
What context do I need?
```

Query is a learned transformation of the word embedding.

---

### Key (K)

Represents:

```text
What information do I offer?
```

or

```text
How should other words match against me?
```

Key is used only for computing relevance.

---

### Value (V)

Represents:

```text
What information should I contribute
if another word attends to me?
```

Value is used only for information transfer.

---

## Why Learn Separate Q, K, and V?

A word participates in attention in three different roles:

1. Searching for information.
2. Advertising what information it contains.
3. Providing information to others.

These are different responsibilities.

Therefore, separate learned transformations are used:

```text
WQ → Search Representation
WK → Matching Representation
WV → Information Representation
```

---

## What Do WQ, WK, and WV Learn?

Unlike CNNs, which learn spatial patterns such as edges and textures, attention learns relational patterns between words.

Conceptually:

### WQ learns

```text
What kind of context should this word search for?
```

Examples:

* Subject information
* Modifier information
* Long-range dependencies
* Semantic context

---

### WK learns

```text
How should this word advertise itself to others?
```

---

### WV learns

```text
What information should this word contribute if selected?
```

---

## Computing Relevance

For a given word:

1. Create its Query representation.
2. Compare it with the Keys of all words.
3. Obtain relevance scores.
4. Apply Softmax to obtain attention weights.

These weights indicate:

```text
How important is each word
for understanding the current word?
```

---

## Building the Contextual Representation

The attention weights are used to combine the Value vectors.

```text
Weighted Sum of Values
```

The result becomes the new contextual representation of the word.

Intuitively:

```text
Current Meaning
+
Relevant Information From Other Words
=
Contextual Representation
```

---

## Single-Head Self-Attention

Single-Head Attention learns one notion of relevance.

One set of:

```text
WQ
WK
WV
```

produces one contextual representation space.

The model learns one way of determining how words relate to each other.

---

## Core Mental Model

RNN:

```text
Context is accumulated through time.
```

Self-Attention:

```text
Context is retrieved through relevance.
```

or

```text
RNN:
Remember information.

Self-Attention:
Find information when needed.
```

---

## Historical Evolution

```text
RNN
↓
LSTM / GRU
↓
Seq2Seq
↓
Bahdanau Attention
↓
Self-Attention
↓
Transformer
↓
Modern LLMs
```

Key Shift:

```text
Memory-Centric Computation
        ↓
Retrieval-Centric Computation
```
