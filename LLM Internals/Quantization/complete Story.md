# Quantization Chapter — Complete Story

We didn't just learn algorithms.

We learned how the field evolved.

Chapter 1 — Motivation

Question:

Why are LLMs expensive?

We learned:

FP representation
Memory bottleneck
Bandwidth bottleneck
Why INT helps
Chapter 2 — Basic Quantization

Question:

How do we convert real numbers into integers?

We learned:

Scale
Zero-point
Symmetric
Asymmetric
Per-tensor
Per-channel
PTQ vs QAT
Chapter 3 — Why Naive Quantization Fails

Question:

Why can't we round every weight?

We learned:

Quantization error
Different weights matter differently
Chapter 4 — Measuring Importance

Question:

How do we measure important weights?

We learned:

Taylor expansion
First derivative
Second derivative
Hessian
Curvature
Chapter 5 — OBD

Question:

Can we approximate the Hessian?

We learned:

Diagonal approximation
Weight importance
Chapter 6 — OBS

Question:

Can other weights compensate?

We learned:

Full Hessian
Hessian inverse
Compensation
Chapter 7 — GPTQ

Question:

OBS is impossible for LLMs. How do we approximate it?

We learned:

Calibration activations
XX
T
Layer reconstruction
Sequential column quantization
Error compensation
Efficient inverse updates
Chapter 8 — AWQ

Question:

Instead of repairing errors, can we avoid creating them?

We learned:

Activation statistics
Important channels
Scaling
Per-channel protection
Chapter 9 — Activation Quantization

Question:

Why stop at weights?

We learned:

Dynamic activations
Static weights
Runtime challenges
Activation outliers
Chapter 10 — SmoothQuant

Question:

Can we move activation difficulty into weights?

We learned:

Equivalent scaling
Channel scaling
Calibration
Static activation quantization
Chapter 11 — The Complete Taxonomy

You now understand how the entire field is organized:

Quantization
│
├── PTQ
│
├── QAT
│
├── Symmetric / Asymmetric
│
├── Per Tensor / Per Channel / Per Group
│
├── Weight / Activation
│
└── Optimization Algorithms
      │
      ├── Naive
      ├── GPTQ
      ├── AWQ
      └── SmoothQuant

This taxonomy is something many engineers never build explicitly, but it's what lets you place new methods naturally.

What You've Really Learned

Notice something.

Initially you probably thought quantization meant:

"Convert FP16 to INT4."

Now your mental model is much richer.

You know it's really about:

Numerical representation.
Information loss.
Optimization under constraints.
Hardware efficiency.
GPU memory bandwidth.
Calibration.
Second-order optimization.
Activation statistics.
Runtime vs offline trade-offs.

That's a systems-level understanding.
