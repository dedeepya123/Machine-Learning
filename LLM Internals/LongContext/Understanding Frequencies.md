Fast vs Slow Frequencies in RoPE

RoPE angle:

angle = p × θ_i

Different dimension pairs have different θ_i values.

---

Fast Frequencies:

Large θ_i

Clock rotates quickly.

Nearby positions produce noticeably different rotations.

Useful for local positional information.

Example:

Position 10 vs 11

---

Slow Frequencies:

Small θ_i

Clock rotates slowly.

Changes gradually over large distances.

Useful for global position information.

Example:

Position 1000 vs 5000

---

Long Context Problem:

At huge positions fast frequencies wrap around many times.

Rotational patterns become very different from training.

Distribution shift occurs.

---

NTK Scaling Intuition:

Instead of uniformly scaling all positions,

modify frequency behavior to preserve local geometry while making long-range geometry more stable.

---

Position Interpolation

Previous Methods:

Inference-only extrapolation.

Try to make huge positions resemble training positions.

---

New Idea:

Compress long contexts into training RoPE range.

Example:

32K context compressed into 2K positional range.

---

Key Difference:

Fine-tune model on compressed geometry.

Model learns new positional relationships.

No longer pure extrapolation.

---

Core Insight:

Instead of tricking the model at inference time,

teach the model the new positional geometry through training.
