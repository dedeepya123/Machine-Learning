## RoPE (Rotary Position Embeddings)

Research Goal:

Make attention depend on relative position naturally.

Wanted:

Attention score to depend on:

(j - i)

instead of absolute positions.

---

Key Idea:

Rotate Q and K according to token position.

Position p:

Q_p = R(pθ)Q

K_p = R(pθ)K

where R is a rotation matrix.

---

Attention Score:

(Q_i)^T K_j

=

(R(iθ)Q)^T (R(jθ)K)

Using rotation property:

R(a)^T R(b) = R(b-a)

becomes:

Q^T R((j-i)θ) K

---

Important Result:

Absolute positions disappear.

Only relative distance:

(j - i)

remains.

---

Why This Is Powerful:

Tokens with the same relative distance produce similar geometric relationships.

The model can reuse patterns regardless of absolute location.

---

Implementation:

Head dimensions are split into pairs.

Each pair behaves like a small 2D vector.

Each pair is rotated by a position-dependent angle.

Different pairs use different frequencies.

---

Benefits:

* Relative position emerges naturally
* No giant position tables
* Integrates directly into attention
* Better extrapolation than earlier approaches

---

Core Insight:

RoPE encodes position through geometry.

Position is represented as rotations of Q and K vectors.

Relative distance appears automatically in the attention dot product.
