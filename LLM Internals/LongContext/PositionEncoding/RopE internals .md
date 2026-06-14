## RoPE Internals

Example:

d_model = 4096

heads = 32

head_dim = 128

---

For every head:

Q shape:

(128)

K shape:

(128)

---

RoPE splits dimensions into pairs:

(q1,q2)

(q3,q4)

...

(q127,q128)

Total:

64 pairs per head.

---

Why pairs?

2D rotation is a natural geometric operation:

R(θ)

=

[[cosθ, -sinθ],
[sinθ, cosθ]]

---

Each pair behaves like a small 2D vector.

---

Position p:

Rotate pair by:

p × θ_i

Different pairs use different frequencies:

θ_1

θ_2

θ_3

...

θ_64

---

This is similar to sinusoidal positional encoding.

Different frequencies allow unique position signatures.

---

Applied To:

Q

K

Not applied to:

V

---

Inference:

1. Compute Q,K
2. Apply RoPE
3. Store rotated K in KV cache
4. Attention uses rotated Q and rotated K

---

Key Intuition:

Every pair acts like a tiny clock.

Different positions rotate the clocks differently.

Many clocks together uniquely represent position.

The relative rotation between Q and K naturally encodes:

(j - i)

which attention needs.
