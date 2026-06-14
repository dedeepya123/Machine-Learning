## Long Context Scaling Story — Part 1

Observation:

RoPE can mathematically generate encodings for arbitrarily large positions.

Example:

Position 2048
Position 128000
Position 1000000

All have valid rotations.

---

Research Question:

If RoPE can represent huge positions, why does model quality drop at long contexts?

---

Key Insight:

Representable ≠ Learned

The model was trained only on positions:

0 → Training Length

Example:

0 → 2048

The weights learned to operate within this positional geometry.

---

Problem 1:

Periodic rotations.

sin() and cos() eventually wrap around.

Large positions produce increasingly complex rotational patterns.

This can create aliasing-like behavior.

---

Problem 2:

Distribution Shift.

Training saw:

R(10θ)

R(100θ)

R(1000θ)

Never saw:

R(100000θ)

When such rotations appear at inference time, the model operates outside its training distribution.

---

Important Realization:

The bottleneck is not attention computation.

The bottleneck is positional geometry.

---

Research Direction:

Can we modify RoPE itself so that very large positions resemble positions seen during training?

This becomes the beginning of RoPE Scaling methods.
