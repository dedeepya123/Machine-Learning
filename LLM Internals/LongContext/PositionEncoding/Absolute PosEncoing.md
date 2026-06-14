## Positional Encoding Story — Part 2

Problem:

Learned position embeddings do not naturally generalize beyond training length.

Example:

Train up to 2048 positions.

Position 50000 has no learned embedding.

---

Research Question:

Can we generate position information using a mathematical function?

Requirements:

1. Every position should be unique.
2. Nearby positions should be similar.
3. Relative distance should be recoverable.
4. Should work for arbitrarily large positions.
5. No learned parameters.

---

Solution:

Sinusoidal Positional Encoding.

For different dimensions:

Use sin() and cos() waves with different frequencies.

Fast waves + slow waves together create a unique signature for each position.

---

Why use multiple frequencies?

A single wave repeats.

Many frequencies together make positions distinguishable.

---

Why use both sin and cos?

Trigonometric identities allow relative position information to be expressed using linear relationships.

This is useful because attention layers are built from linear operations.

---

Advantages:

* No learned position table
* Can generate encodings for any position
* Nearby positions remain related
* Relative position information becomes easier to learn

---

Researchers initially thought this solved positional encoding.

Later, very long contexts revealed new limitations.

This led to the next question:

Does attention really need absolute positions, or does it mainly need relative positions?
