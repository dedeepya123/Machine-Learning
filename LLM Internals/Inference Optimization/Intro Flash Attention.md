## If softmax requires all attention scores, how can FlashAttention avoid storing the entire attention matrix?

Observation:

Softmax:

# softmax(x_i)

e^(x_i)
/ Σ e^(x_j)

appears to require all scores simultaneously.

Researcher Question:

Can softmax be computed incrementally?

Key Insight:

Maintain running statistics instead of storing all scores.

Running Statistics:

1. Running maximum (m)

m = max(scores seen so far)

2. Running denominator (l)

l = Σ e^(score - m)

These can be updated block-by-block.

FlashAttention Strategy:

Instead of computing full QK^T:

* Load small K,V blocks
* Compute local attention scores
* Update running softmax statistics
* Update output
* Discard block
* Move to next block

Result:

No N×N attention matrix is ever materialized.

Memory Complexity:

Standard Attention:

O(N²)

FlashAttention:

O(N)

Deep Insight:

FlashAttention computes exactly the same attention result.

The innovation is not changing attention mathematics.

The innovation is changing how attention is executed and how intermediate results are stored.


## Why subtract max in softmax?

Softmax:

softmax(x_i) = e^(x_i) / Σe^(x_j)

Large values can overflow:

e^(1000)

Small values can underflow:

e^(-1000)

Solution:

Subtract maximum value:

# softmax(x_i)

e^(x_i - m)
/ Σe^(x_j - m)

where:

m = max(x)

This gives exactly the same softmax but much better numerical stability.

---

## FlashAttention Goal:

Avoid storing the full attention matrix QK^T.

Instead process attention scores block-by-block.

---

Running Statistics:

1. Running Maximum

m_new = max(m_old, m_block)

2. Running Denominator

l_new =
l_old * e^(m_old - m_new)
+
Σ e^(s_j - m_new)

This rescales old contributions when maximum changes.

---

Key Insight:

The running denominator after all blocks is exactly equal to the denominator obtained from processing the whole row at once.

No approximation is made.

---

FlashAttention Stores:

* Running max (m)
* Running denominator (l)
* Running output accumulator (o)

It does NOT store the full attention matrix.

---

Used In:

* Training
* Inference

Main Benefit:

Less HBM traffic.

Same mathematical result.

## FlashAttention Final Math

Standard Attention:

o = softmax(S)V

where:

S = QK^T

Can be written as:

o = n / l

where:

Numerator:

n = Σ e^(s_i - m) v_i

Denominator:

l = Σ e^(s_i - m)

and:

m = max(scores)

---

Running Maximum:

m_new = max(m_old, m_block)

---

Running Denominator:

l_new =
l_old * e^(m_old - m_new)
+
Σ e^(s_j - m_new)

---

Running Numerator:

n_new =
n_old * e^(m_old - m_new)
+
Σ e^(s_j - m_new) v_j

---

Final Output:

o = n / l

after all blocks are processed.

---

Key Insight:

Instead of storing the full attention matrix, FlashAttention stores only:

* Running maximum (m)
* Running denominator (l)
* Running numerator (n)

This is sufficient to compute exactly the same attention output.

---

Deep Insight:

FlashAttention does not change the attention formula.

It changes the execution strategy to minimize memory movement.
