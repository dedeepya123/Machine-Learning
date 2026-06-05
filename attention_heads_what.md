# What Do Attention Heads Actually Learn?

## My Confusion

In CNNs, it is relatively easy to understand what gets learned:

```text
Early Layers:
Edges
Corners
Textures

Middle Layers:
Shapes
Object Parts

Deep Layers:
Objects
Semantics
```

There is a clear hierarchy of visual features.

In NLP, this feels less obvious.

Questions:

* What are the equivalent of edges and textures in language?
* How can the same attention head work across different sentences?
* What exactly is being learned?

---

# Key Insight

Attention heads do NOT memorize words.

A head does not learn:

```text
dog → tired
```

or

```text
beautiful → flower
```

Instead, heads learn reusable relationships that occur across many sentences.

Just like CNN filters learn reusable visual patterns.

---

# CNN Analogy

CNN does not learn:

```text
This specific cat image
```

It learns:

```text
Edge patterns
Texture patterns
Shape patterns
```

which appear in many images.

Similarly, attention heads learn:

```text
Subject ↔ Verb relationships
Verb ↔ Object relationships
Modifier ↔ Noun relationships
Entity ↔ Pronoun relationships
Long-range dependencies
```

which appear in many sentences.

---

# What Is Actually Learned?

A head learns a way of measuring relevance.

Conceptually:

```text
Head 1:
Who is performing the action?

Head 2:
What object is affected?

Head 3:
Which noun does this adjective modify?

Head 4:
Which previous entity does this pronoun refer to?
```

These are not hardcoded.

They emerge from training.

---

# Why Does It Generalize Across Sentences?

Example:

```text
The dog was tired.
The cat was tired.
The horse was tired.
```

The model does not memorize:

```text
dog ↔ tired
cat ↔ tired
horse ↔ tired
```

Instead it learns a more general pattern:

```text
Entity experiencing a state
```

This relationship appears repeatedly across training data.

Therefore the learned pattern transfers to new sentences.

---

# What Are The "Edges" Of Language?

Language does not have visual primitives like:

```text
Edges
Corners
Textures
```

Instead, the fundamental reusable patterns are things like:

```text
Semantic similarity
Grammatical roles
Dependency relationships
Phrase structure
Entity references
Contextual meaning
```

These are the NLP equivalents of visual primitives.

---

# Rough Hierarchy In Transformers

Early Layers:

```text
Word meaning
Semantic similarity
Local grammatical relationships
```

Middle Layers:

```text
Phrase structure
Dependency relationships
Syntax
```

Deeper Layers:

```text
Sentence meaning
Entity tracking
Long-range dependencies
```

Higher Layers:

```text
Reasoning
Task-specific abstractions
Complex concepts
```

This hierarchy is not as clean as CNNs, but the idea is similar.

---

# Multi-Head Attention Mental Model

Do NOT think:

```text
Head 1 attends to word A
Head 2 attends to word B
```

Think:

```text
Head 1 learns one type of relationship.

Head 2 learns another type of relationship.

Head 3 learns another type of relationship.
```

Each head is a specialized relationship detector.

---

# What To Keep In Mind

The biggest mindset shift from CV to NLP is:

```text
CNN Filters
=
Reusable Visual Pattern Detectors

Attention Heads
=
Reusable Relationship Detectors
```

Language understanding emerges because the network learns increasingly sophisticated relationships between words, phrases, entities, and concepts across layers.
