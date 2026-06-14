## Long Context Scaling Story — Part 3 (NTK Scaling Intuition)

Problem With Uniform Position Scaling:

p

→

p / scale

Helps large positions look similar to training positions.

But compresses all distances equally.

---

Example:

10 → 0.156

11 → 0.172

Distance:

1

becomes

0.016

Local positional resolution decreases.

---

Key Observation:

Language depends heavily on nearby token relationships.

Not all positional distances are equally important.

---

RoPE Angle:

angle = p × θ_i

Contains:

* Position (p)
* Frequency (θ_i)

---

Research Question:

Instead of scaling positions, can we modify frequencies?

---

Insight:

Fast frequencies wrap around quickly and cause long-context problems.

Slow frequencies already behave well.

Need a smarter scaling strategy.

---

NTK Scaling Goal:

Preserve local positional geometry.

Compress long-range positional geometry.

Keep attention behavior similar to training.

---

Result:

Nearby tokens remain almost unchanged.

Far positions become more manageable.

Better long-context extrapolation than uniform scaling.

---

New Research Question:

Can we move beyond pure extrapolation and actually teach the model to understand longer contexts?

This leads to Position Interpolation and later YaRN.
