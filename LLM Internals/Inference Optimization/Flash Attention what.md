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

FlashAttention divides the huge attention computation into tiles. A query block attends to one key block at a time. Each tile computes a small matrix multiplication QtileKtileT
Running softmax statistics (m,l,n) are updated immediately, and the tile is discarded. Eventually every query token has attended to every key token, but without materializing the full attention matrix.
