## YaRN (Yet another RoPE extensioN)

Problem With Position Interpolation:

All positions are compressed uniformly.

Example:

100 and 101

become

1.60 and 1.616

Difference becomes much smaller.

Local positional resolution decreases.

---

Observation:

Not all positional scales are equally important.

Near positions require high precision.

Far positions can tolerate more compression.

---

RoPE:

angle = p × θ_i

Different θ_i values create different frequencies.

Fast frequencies:

* Change rapidly
* Capture local positional details

Slow frequencies:

* Change slowly
* Capture long-range positional structure

---

Position Interpolation:

Compresses all frequencies equally.

---

YaRN:

Applies different treatment to different frequency ranges.

Goal:

Preserve local positional information.

Compress long-range positional information.

---

Training:

Uses fine-tuning on long-context data.

Normal training process:

Forward Pass
→ Loss
→ Backprop
→ AdamW Updates

All weights continue learning.

---

Benefits:

* Better retrieval
* Better reasoning
* Better long-context performance
* Better preservation of local positional structure

---

Evolution:

RoPE
↓
Scaling
↓
Interpolation
↓
YaRN

Main Insight:

Long-context extension is not just about fitting more positions.

It is about preserving the positional information that matters most.
