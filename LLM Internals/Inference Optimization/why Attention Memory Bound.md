## How did researchers prove standard attention is memory-bound?

Standard Attention:

1. S = QK^T
2. P = softmax(S)
3. O = PV

Observation:

S has shape:

N × N

For large sequence lengths this becomes extremely large.

Memory Traffic:

Step 1:

Compute S = QK^T

Write S to HBM.

Step 2:

Read S from HBM.

Compute softmax.

Write P to HBM.

Step 3:

Read P from HBM.

Read V.

Compute output.

Write output.

Problem:

Large attention matrices are repeatedly written and read from GPU memory.

Memory traffic grows approximately with N².

Researcher Insight:

The bottleneck is not the mathematical operations.

The bottleneck is moving intermediate attention matrices between HBM and compute units.

Key Question:

Do we really need to materialize the entire attention matrix?

This question led directly to FlashAttention.

Deep Insight:

FlashAttention is primarily an IO optimization rather than a mathematical optimization.
