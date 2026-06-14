## Positional Encoding Story — Part 3

Initial Thinking:

How do we tell the model where a token is?

This leads to absolute positional encodings.

---

Deeper Research Question:

Does language actually depend on absolute positions?

Example:

"The cat sat"

and

"Yesterday the cat sat"

The meaning of "cat" does not depend on being at position 2 or 3.

What matters is its relationship to nearby words.

---

Key Insight:

Language is often based on relative distance.

Attention itself is relational.

The model often cares more about:

Distance(token_i, token_j)

than

AbsolutePosition(token_i)

---

Relative Position Encoding:

Modify attention:

Score(i,j)

=

Q_i K_j^T

*

RelativeBias(i-j)

Now attention can directly use distance information.

---

Benefits:

* More aligned with language structure
* Same distance patterns can be reused everywhere
* Better generalization than purely absolute positions

---

New Problem:

Very large distances require handling huge numbers of relative positions.

Need a more scalable solution.

This leads to RoPE.

Core Idea:

Instead of adding position information, rotate Q and K vectors according to position.

Relative position information naturally emerges inside the attention dot product.

