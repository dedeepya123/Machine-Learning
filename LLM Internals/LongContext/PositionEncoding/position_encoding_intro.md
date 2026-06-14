## Positional Encoding Story — Part 1

Problem:

Self-attention has no notion of order.

Attention computes:

QK^T

using token embeddings only.

Nothing in the attention equations tells the model:

* Which token came first
* Which token came later
* Distance between tokens

---

Why RNNs did not have this problem:

RNNs process tokens sequentially.

Order is built into computation.

Transformers removed recurrence and gained parallelism, but lost order information.

---

Research Question:

How do we tell the Transformer where each token is located?

---

First Idea:

Create position embeddings.

For every position:

p_0, p_1, p_2, ...

Add them to token embeddings:

x_i + p_i

Now the same word appearing at different positions gets different representations.

---

Limitation:

If training context is 2048:

Only positions:

p_0 ... p_2047

are learned.

What happens at position 50000?

There is no learned embedding.

Model cannot naturally generalize.

---

Next Research Question:

Can we generate position information using a mathematical function instead of learning a separate embedding for every position?

This leads to Sinusoidal Positional Encoding.
