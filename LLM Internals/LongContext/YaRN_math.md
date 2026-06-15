## YaRN Mathematics

RoPE:

angle = p × θ_i

where θ_i is the frequency for dimension pair i.

---

Position Interpolation:

p' = p / s

Equivalent to:

θ_i' = θ_i / s

All frequencies are scaled equally.

---

Problem:

Fast frequencies and slow frequencies are treated the same.

Local positional information is compressed too much.

---

YaRN Idea:

Scale frequencies differently.

Fast frequencies:

Almost unchanged.

Slow frequencies:

Strongly compressed.

Middle frequencies:

Partially compressed.

---

Introduce blending coefficient:

α_i

0 ≤ α_i ≤ 1

---

Modified frequency:

θ_i' = (1 - α_i)θ_i + α_i(θ_i / s)

---

Cases:

α_i = 0

→ Original frequency preserved.

---

α_i = 1

→ Fully compressed frequency.

---

0 < α_i < 1

→ Blend of both.

---

Result:

Preserves local positional resolution.

Compresses long-range positional structure.

Better long-context behavior than uniform interpolation.

---

Deep Insight:

Different positional scales need different amounts of precision.

Allocate positional resolution where it matters most.
