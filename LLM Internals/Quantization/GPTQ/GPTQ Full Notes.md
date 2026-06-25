# GPTQ (Generative Pretrained Transformer Quantization)

## 1. Motivation

Large Language Models are typically stored using FP16/BF16 weights.

Example:

* 7B model
* 7 billion weights
* FP16 = 2 bytes per weight

Memory:

[
7B \times 2 \approx 14GB
]

This makes inference expensive.

A natural idea is:

```text
Store weights in lower precision
(INT8, INT4, etc.)
```

This process is called quantization.

---

## 2. The Problem with Naive Quantization

Suppose a weight:

[
w = 0.73
]

gets quantized to:

[
q = 1
]

Quantization error:

[
e = q-w
]

Every weight suffers some rounding error.

The problem is:

```text
Not all weights are equally important.
```

Some weights can tolerate large errors.

Some weights are extremely sensitive.

Therefore:

```text
Same quantization error
≠
Same impact on model quality.
```

This naturally leads to the question:

```text
How do we measure weight importance?
```

---

## 3. OBD and OBS Background

Researchers studying pruning faced the same question.

They used Taylor expansion of the loss.

Suppose weights change by:

[
\Delta w
]

Then:

[
L(w+\Delta w)
]

can be approximated using Taylor series.

Since a trained network is near a local optimum:

[
\nabla L \approx 0
]

the first-order term disappears.

The dominant term becomes:

[
\Delta L
\approx
\frac12
\Delta w^T
H
\Delta w
]

where:

[
H
=

\frac{\partial^2 L}
{\partial w^2}
]

is the Hessian.

---

### Interpretation

The Hessian captures:

#### Diagonal Terms

[
H_{ii}
]

Tell us:

```text
How sensitive the loss is
to changing weight i.
```

#### Off-Diagonal Terms

[
H_{ij}
]

Tell us:

```text
How weight i and weight j
interact.
```

---

### OBD

Optimal Brain Damage:

Uses only diagonal Hessian.

Assumes weights are independent.

Fast but ignores interactions.

---

### OBS

Optimal Brain Surgeon:

Uses full Hessian.

Accounts for weight interactions.

Provides optimal compensation.

However:

```text
Full Hessian is impossible
for modern LLMs.
```

---

## 4. GPTQ's Key Insight

GPTQ borrows the OBS idea.

But instead of studying:

```text
Final model loss
```

GPTQ studies:

```text
Layer reconstruction error.
```

---

Consider one linear layer:

[
Y = WX
]

After quantization:

[
\hat Y = \hat W X
]

GPTQ wants:

[
WX
\approx
\hat W X
]

---

Objective:

[
L
=

|WX-\hat W X|^2
]

Define:

[
E
=

\hat W-W
]

Then:

[
L
=

|EX|^2
]

---

## 5. Where Does the Hessian Come From?

Expanding:

[
L
=

|EX|^2
]

leads to:

[
L
=

Tr(EXX^TE^T)
]

Notice:

[
XX^T
]

appears naturally.

Taking derivatives:

First derivative:

[
EXX^T
]

Second derivative:

[
XX^T
]

Therefore:

[
H
=

XX^T
]

for the layer reconstruction objective.

---

## 6. Meaning of XXᵀ

Suppose:

[
X
=

[x_1,x_2,\ldots,x_n]
]

contains activations entering a weight matrix.

Then:

[
XX^T
]

captures:

```text
Activation statistics.
```

Specifically:

### Diagonal

Which activation dimensions are strong.

### Off-Diagonal

Which activation dimensions occur together.

---

Interpretation:

```text
Weights connected to important
activation directions matter more.
```

This acts as a local Hessian.

---

## 7. Calibration Data

GPTQ does NOT train the model.

No:

* SGD
* Backprop
* Fine-tuning

Instead:

1. Take a few hundred samples.
2. Run a forward pass.
3. Collect activations.
4. Build:

[
H = XX^T
]

Only once.

---

## 8. Sequential Quantization

Suppose:

[
W=[w_1,w_2,w_3,\ldots]
]

GPTQ quantizes one column at a time.

---

### Step 1

Quantize:

[
w_1
]

to:

[
q_1
]

Error:

[
e_1=q_1-w_1
]

---

### Problem

This changes layer output.

---

### Solution

Compensate using remaining columns.

Modify:

[
w_2,w_3,\ldots
]

so output remains close.

---

Then:

```text
Freeze column 1.
```

Move to column 2.

Repeat.

---

## 9. Compensation

GPTQ asks:

```text
Given the error introduced
by quantizing column i,

how should remaining columns
change to minimize output error?
```

OBS showed that the optimal correction depends on:

[
H^{-1}
]

The correction is:

[
\Delta w
========

-\frac{e_i}
{(H^{-1})*{ii}}
(H^{-1})*{:,i}
]

---

### Interpretation

[
(H^{-1})_{:,i}
]

tells:

```text
Which columns can absorb
the error from column i.
```

---

[
(H^{-1})_{ii}
]

acts as a normalization factor.

---

Thus:

```text
Error is redistributed
to remaining floating-point columns.
```

---

## 10. Why Sequential Processing Works

After compensating:

[
w_2,w_3,\ldots
]

have already been adjusted.

When quantizing column 2:

GPTQ quantizes the updated version.

Not the original.

Therefore:

```text
Error is repaired immediately
before moving on.
```

This prevents error accumulation.

---

## 11. Final GPTQ Pipeline

1. Take calibration samples.
2. Run forward pass.
3. Collect activations.
4. Build:

[
H=XX^T
]

5. Compute:

[
H^{-1}
]

6. Quantize one column.
7. Compute quantization error.
8. Compensate using:

[
H^{-1}
]

9. Freeze column.
10. Repeat for all columns.
11. Move to next layer.

---

## Interview One-Liner

GPTQ is a post-training quantization algorithm that treats quantization as a layer reconstruction problem, approximates the local Hessian using activation statistics (H=XX^T), and uses OBS-style second-order compensation through (H^{-1}) to sequentially quantize weight columns while minimizing output reconstruction error.



- GPTQ is post-training quantization (PTQ).
- It uses calibration data, not retraining.
- It minimizes layer reconstruction error, not final language-model loss.
  H≈XXT acts as a local Hessian.
- Compensation comes from OBS-inspired second-order optimization.
- Quantization is performed column-by-column sequentially.
- Already quantized columns are frozen; remaining columns absorb the error.
