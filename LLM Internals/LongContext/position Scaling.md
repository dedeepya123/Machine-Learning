Long Context Scaling Story — Part 2

Problem:

RoPE works mathematically for huge positions.

But model was trained only on smaller positional geometries.

Long contexts cause distribution shift.

---

Research Question:

Can we make large positions look like positions seen during training?

---

Simple Idea:

Before applying RoPE:

p

→

p / scale

Example:

scale = 64

128K position

→

2000 position

---

Effect:

RoPE angles become smaller.

Clock rotations remain closer to training regime.

---

Benefits:

* No retraining
* No architecture changes
* Easy implementation

---

Observation:

Works surprisingly well for extending context.

---

New Problem:

Uniform scaling compresses all positions.

Short-range distances are also compressed.

Nearby token distinctions become less precise.

---

Key Realization:

Need a smarter scaling strategy.

Want:

* Preserve local geometry
* Extend global context

This leads to NTK-aware scaling and later long-context methods.
