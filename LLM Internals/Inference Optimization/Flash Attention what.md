FlashAttention is an IO-aware exact attention algorithm.
Instead of materializing the full attention matrix QK^T in GPU memory, it processes attention in small blocks that fit in fast on-chip memory (registers/shared memory).

It maintains running softmax statistics:

* Running maximum (m)
* Running denominator (l)
* Running numerator/output accumulator (n)

and computes exactly the same result as standard attention while dramatically reducing HBM memory reads and writes.

Key idea:

Reduce memory movement, not mathematical operations.

Benefits:

* Lower memory usage
* Faster training
* Faster inference
* Longer context lengths

FlashAttention is an exact attention algorithm, not an approximation.
